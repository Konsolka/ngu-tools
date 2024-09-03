import math


def more_then_60(value):
    return True if value > 60.0 else False


def format_large_number(value):
    # Round the value
    rounded_value = round(value)

    # Determine the magnitude (e.g., million, billion)
    magnitude = int(math.log10(rounded_value)) if rounded_value > 0 else 0

    suffixes = ["", "K", "M", "B", "T", "Quad", "Quint", "Sext", "Sept", "Oct", "Non", "Dec", "Undec", 'Duodec',
                'Tredec', 'Quattuordec', 'Quindec', 'Sexdec', 'Septendec', 'Octodec', 'Nondec', 'Viginti']

    suffix_index = min(magnitude // 3, len(suffixes) - 1)
    suffix = suffixes[suffix_index]

    reduced_value = rounded_value / 10 ** (suffix_index * 3)
    formatted_value = f"{reduced_value:,.3f}".rstrip('0').rstrip('.')

    return f"{formatted_value} {suffix}"
