"""General utilities."""

__all__ = ["resolve_index", "resolve_continuous_slice", "pre_move"]


def resolve_index(length, index, clamp=False):
    # type: (int, int, bool) -> int
    """
    Resolve list index to a positive number.

    :param length: Length of the list.
    :param index: Input index.
    :param clamp: Whether to clamp between zero and the length.
    :return: Resolved index.
    :raises IndexError: Index out of range.
    """
    if index < 0:
        index += length
    if clamp:
        if index < 0:
            index = 0
        elif index > length:
            index = length
    elif index < 0 or index >= length:
        error = "index out of range"
        raise IndexError(error)
    return index


def resolve_continuous_slice(length, slc):
    # type: (int, slice) -> tuple[int, int]
    """
    Resolve continuous list slice according to length.

    :param length: Length of the list.
    :param slc: Continuous slice.
    :return: Index and stop.
    :raises IndexError: Slice is noncontinuous.
    """
    index, stop, step = slc.indices(length)
    if step != 1 or stop < index:
        error = "slice {} is noncontinuous".format(slc)
        raise IndexError(error)
    return index, stop


def pre_move(length, item, target_index):
    # type: (int, slice | int, int) -> tuple[int, int, int, int, int] | None
    """
    Perform checks before moving list values internally and get move indexes.

    :param length: Length of the list.
    :param item: Index/slice.
    :param target_index: Target index.
    :return: None or (target index, index, stop, post index, post_stop).
    """

    # Resolve slice/index.
    if isinstance(item, slice):
        index, stop = resolve_continuous_slice(length, item)
        if index == stop:
            return None
    else:
        index = resolve_index(length, item)
        stop = index + 1

    # Calculate target index, post index, and post stop.
    target_index = resolve_index(length, target_index, clamp=True)
    if index <= target_index <= stop:
        return None
    elif target_index > stop:
        post_index = target_index - (stop - index)
    else:
        post_index = target_index
    post_stop = post_index + (stop - index)

    return target_index, index, stop, post_index, post_stop
