def top_n(items, n):
    """Return the top n items in an array, in descending order.
    
    Args:
        items (array): list or array-like object
        n (int): number of items to return

    Returns:
        array: top n items, in descending order

    Example:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    
    """
    return sorted(items, reverse=True)[:n]
