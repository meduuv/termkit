def clamp(value: int, minimum: int, maximum: int) -> int:
    """Clamp an integer to an inclusive range."""
    if minimum>maximum: raise ValueError('minimum cannot exceed maximum')
    return max(minimum,min(maximum,value))
