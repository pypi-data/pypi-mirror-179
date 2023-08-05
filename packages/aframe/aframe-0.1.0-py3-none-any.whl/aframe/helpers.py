def xyz(x: float = 0.0, y: float = 0.0, z: float = 0.0):
    """Convenience wrapper for position attributes.

    Args:
        x (float, optional): Negative X axis extends left. Positive X Axis extends right. Defaults to 0.0.
        y (float, optional): Negative Y axis extends down. Positive Y Axis extends up.. Defaults to 0.0.
        z (float, optional): Negative Z axis extends in front. Positive Z Axis extends behind.. Defaults to 0.0.

    Returns:
        str: position
    """
    
    return f'{x} {y} {z}'

def attrs(**kwargs):
    """Builds string attributes for complex styling of attributes

    Returns:
        str: fused kwargs into prepared string
    """
    attrs = str()
    for k, v in kwargs.items():
        attrs += f'{k}: {v}; '
    return attrs[:-1]
