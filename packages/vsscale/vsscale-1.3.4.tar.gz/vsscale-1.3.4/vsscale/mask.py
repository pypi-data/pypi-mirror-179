from __future__ import annotations

from functools import partial

from vsexprtools import ExprOp, combine, norm_expr
from vskernels import Catrom
from vsmask.edge import EdgeDetect, Prewitt, PrewittTCanny
from vsmask.util import XxpandMode, expand
from vsrgtools import box_blur, gauss_blur, removegrain
from vsrgtools.util import wmean_matrix
from vstools import (
    check_variable, core, depth, expect_bits, get_depth, get_neutral_value, get_peak_value, get_y, iterate, plane,
    scale_thresh, scale_value, shift_clip_multi, split, vs
)

__all__ = [
    'descale_detail_mask', 'descale_error_mask',
    'simple_detail_mask', 'multi_detail_mask',
    'credit_mask',
    'ringing_mask'
]


def descale_detail_mask(
    clip: vs.VideoNode, rescaled: vs.VideoNode, thr: float = 0.05,
    inflate: int = 2, xxpand: tuple[int, int] = (4, 0)
) -> vs.VideoNode:
    mask = norm_expr([get_y(clip), get_y(rescaled)], 'x y - abs')

    mask = mask.std.Binarize(thr * get_peak_value(mask))

    if xxpand[0]:
        mask = iterate(mask, core.std.Maximum if xxpand[0] > 0 else core.std.Minimum, xxpand[0])

    if inflate:
        mask = iterate(mask, core.std.Inflate, inflate)

    if xxpand[1]:
        mask = iterate(mask, core.std.Maximum if xxpand[1] > 0 else core.std.Minimum, xxpand[1])

    return mask.std.Limiter()


def descale_error_mask(
    clip: vs.VideoNode, rescaled: vs.VideoNode,
    thr: float | list[float] = 0.38,
    expands: int | tuple[int, int, int] = (2, 2, 3),
    blur: int | float = 3, bwbias: int = 1, tr: int = 1
) -> vs.VideoNode:
    assert clip.format and rescaled.format

    y, *chroma = split(clip)

    bit_depth = get_depth(clip)
    neutral = get_neutral_value(clip)

    error = norm_expr([y, rescaled], 'x y - abs')

    if bwbias > 1 and chroma:
        chroma_abs = norm_expr(chroma, f'x {neutral} - abs y {neutral} - abs max')
        chroma_abs = Catrom().scale(chroma_abs, y.width, y.height)

        tv_low, tv_high = scale_value(16, 8, bit_depth), scale_value(235, 8, bit_depth)
        bias = norm_expr([y, chroma_abs], f'x {tv_high} >= x {tv_low} <= or y 0 = and {bwbias} 1 ?')
        bias = expand(bias, 2)

        error = norm_expr([error, bias], 'x y *')

    if isinstance(expands, int):
        exp1 = exp2 = exp3 = expands
    else:
        exp1, exp2, exp3 = expands

    assert exp1

    error = expand(error, exp1, mode=XxpandMode.RECTANGLE)

    if exp2:
        error = expand(error, exp2, mode=XxpandMode.ELLIPSE)

    scaled_thrs = [
        scale_value(val / 10, 32, bit_depth)
        for val in ([thr] if isinstance(thr, float) else thr)
    ]

    error = error.std.Binarize(scaled_thrs[0])

    for scaled_thr in scaled_thrs[1:]:
        bin2 = error.std.Binarize(scaled_thr)
        error = bin2.misc.Hysteresis(error)

    if exp3:
        error = expand(error, exp2, mode=XxpandMode.ELLIPSE)

    if tr > 1:
        avg = core.misc.AverageFrames(error, [1] * ((tr * 2) + 1)).std.Binarize(neutral)

        _error = combine([error, avg], ExprOp.MIN)
        shifted = shift_clip_multi(_error, (-tr, tr))
        _error = combine(shifted, ExprOp.MAX)

        error = combine([error, _error], ExprOp.MIN)

    if isinstance(blur, int):
        error = box_blur(error, blur)
    else:
        error = gauss_blur(error, blur)

    return error.std.Limiter()


def credit_mask(
    clip: vs.VideoNode, ref: vs.VideoNode, thr: int,
    blur: float | None = 1.65, prefilter: bool = True,
    expand: int = 8
) -> vs.VideoNode:
    from vardefunc.mask import Difference

    if blur is None or blur <= 0:
        blur_src, blur_ref = clip, ref
    else:
        blur_src = clip.bilateral.Gaussian(blur)
        blur_ref = ref.bilateral.Gaussian(blur)

    ed_mask = Difference().creditless(
        blur_src[0] + blur_src, blur_src, blur_ref,
        start_frame=0, thr=thr, prefilter=prefilter
    )

    credit_mask, bits = expect_bits(ed_mask)
    credit_mask = iterate(credit_mask, core.std.Minimum, 6)
    credit_mask = iterate(credit_mask, lambda x: core.std.Minimum(x).std.Maximum(), 8)
    if expand:
        credit_mask = iterate(credit_mask, core.std.Maximum, expand)
    credit_mask = credit_mask.std.Inflate().std.Inflate().std.Inflate()

    return credit_mask if bits == 16 else depth(credit_mask, bits)


def simple_detail_mask(
    clip: vs.VideoNode, sigma: float | None = None, rad: int = 3, brz_a: float = 0.025, brz_b: float = 0.045
) -> vs.VideoNode:
    from lvsfunc import range_mask

    brz_a = scale_thresh(brz_a, clip)
    brz_b = scale_thresh(brz_b, clip)

    y = plane(clip, 0)

    blur = gauss_blur(y, sigma) if sigma else y

    mask_a = range_mask(blur, rad=rad).std.Binarize(brz_a)

    mask_b = PrewittTCanny().edgemask(blur).std.Binarize(brz_b)

    mask = combine([mask_a, mask_b])

    return removegrain(removegrain(mask, 22), 11).std.Limiter()


def multi_detail_mask(clip: vs.VideoNode, thr: float = 0.015) -> vs.VideoNode:
    general_mask = simple_detail_mask(clip, rad=1, brz_a=1, brz_b=24.3 * thr)

    return combine([
        combine([
            simple_detail_mask(clip, brz_a=1, brz_b=2 * thr),
            iterate(general_mask, core.std.Maximum, 3).std.Maximum().std.Inflate()
        ], ExprOp.MIN), general_mask.std.Maximum()
    ], ExprOp.MIN)


def ringing_mask(
    clip: vs.VideoNode,
    rad: int = 2, brz: float = 0.35,
    thmi: float = 0.315, thma: float = 0.5,
    thlimi: float = 0.195, thlima: float = 0.392,
    credit_mask: vs.VideoNode | EdgeDetect = Prewitt()
) -> vs.VideoNode:
    assert check_variable(clip, ringing_mask)

    smax = get_peak_value(clip)

    thmi, thma, thlimi, thlima = (
        scale_thresh(t, clip) for t in [thmi, thma, thlimi, thlima]
    )

    if isinstance(credit_mask, vs.VideoNode):
        edgemask = depth(credit_mask, get_depth(clip))  # type: ignore
    elif isinstance(credit_mask, EdgeDetect):
        edgemask = credit_mask.edgemask(plane(clip, 0))

    edgemask = plane(edgemask, 0).std.Limiter()

    light = norm_expr(edgemask, f'x {thlimi} - {thma - thmi} / {smax} *')
    shrink = iterate(light, core.std.Maximum, rad)
    shrink = shrink.std.Binarize(scale_thresh(brz, clip))
    shrink = iterate(shrink, core.std.Minimum, rad)
    shrink = iterate(shrink, partial(core.std.Convolution, matrix=wmean_matrix), 2)

    strong = norm_expr(edgemask, f'x {thmi} - {thlima - thlimi} / {smax} *')
    expand = iterate(strong, core.std.Maximum, rad)

    mask = norm_expr([expand, strong, shrink], 'x y z max - 2 *')
    mask = mask.std.Convolution(wmean_matrix)

    return norm_expr(mask, 'x 2 *').std.Limiter()
