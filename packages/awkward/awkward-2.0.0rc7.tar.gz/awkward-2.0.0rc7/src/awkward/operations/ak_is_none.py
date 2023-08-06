# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import awkward as ak

np = ak._nplikes.NumpyMetadata.instance()


def is_none(array, axis=0, *, highlevel=True, behavior=None):
    """
    Args:
        array: Array-like data (anything #ak.to_layout recognizes).
        axis (int): The dimension at which this operation is applied. The
            outermost dimension is `0`, followed by `1`, etc., and negative
            values count backward from the innermost: `-1` is the innermost
            dimension, `-2` is the next level up, etc.
        highlevel (bool): If True, return an #ak.Array; otherwise, return
            a low-level #ak.contents.Content subclass.
        behavior (None or dict): Custom #ak.behavior for the output array, if
            high-level.

    Returns an array whose value is True where an element of `array` is None;
    False otherwise (at a given `axis` depth).
    """
    with ak._errors.OperationErrorContext(
        "ak.is_none",
        dict(array=array, axis=axis, highlevel=highlevel, behavior=behavior),
    ):
        return _impl(array, axis, highlevel, behavior)


def _impl(array, axis, highlevel, behavior):

    # Determine the (potentially nested) bytemask
    def getfunction_inner(layout, depth, **kwargs):
        if not isinstance(layout, ak.contents.Content):
            return

        backend = layout.backend

        if layout.is_option:
            layout = layout.to_IndexedOptionArray64()

            # Convert the option type into a union, using the mask
            # as a tag.
            tag = backend.index_nplike.asarray(layout.mask_as_bool(valid_when=False))
            index = backend.index_nplike.where(
                tag, 0, backend.nplike.asarray(layout.index)
            )

            return ak.contents.UnionArray.simplified(
                ak.index.Index8(tag),
                ak.index.Index64(index),
                [
                    ak._do.recursively_apply(
                        layout.content, getfunction_inner, behavior
                    ),
                    ak.contents.NumpyArray(
                        backend.nplike.array([True], dtype=np.bool_)
                    ),
                ],
            )

        elif layout.is_numpy or layout.is_unknown or layout.is_list or layout.is_record:
            return ak.contents.NumpyArray(
                backend.nplike.zeros(len(layout), dtype=np.bool_)
            )

    # Locate the axis
    def getfunction_outer(layout, depth, depth_context, **kwargs):
        depth_context["posaxis"] = ak._do.axis_wrap_if_negative(
            layout, depth_context["posaxis"]
        )
        if depth_context["posaxis"] == depth - 1:
            return ak._do.recursively_apply(layout, getfunction_inner, behavior)

    layout = ak.operations.to_layout(array)
    max_axis = layout.branch_depth[1] - 1
    if axis > max_axis:
        raise ak._errors.wrap_error(
            np.AxisError(f"axis={axis} exceeds the depth of this array ({max_axis})")
        )
    behavior = ak._util.behavior_of(array, behavior=behavior)
    depth_context = {"posaxis": axis}
    out = ak._do.recursively_apply(
        layout, getfunction_outer, behavior, depth_context=depth_context
    )
    return ak._util.wrap(out, behavior, highlevel)
