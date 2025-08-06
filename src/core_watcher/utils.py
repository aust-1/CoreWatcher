def value_to_color(value: float) -> str:
    if value < 30:
        return "#4CAF50"  # green
    if value < 60:
        return "#FFC107"  # amber
    return "#F44336"  # red
