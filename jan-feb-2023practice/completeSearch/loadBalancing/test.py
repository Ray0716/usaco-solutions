def calculate_quadrants(upper_left_right, upper_right_lower, lower_left_right, upper_left_lower):
    total_points = upper_left_right + upper_right_lower + lower_left_right + upper_left_lower
    upper_left = (total_points - upper_left_right - upper_left_lower) // 2
    upper_right = upper_left_right - upper_left
    lower_right = lower_left_right - upper_right
    lower_left = upper_left_lower - lower_right

    return {
        "Upper Left": upper_left,
        "Upper Right": upper_right,
        "Lower Right": lower_right,
        "Lower Left": lower_left
    }

print(calculate_quadrants(2, 2, 2, 2))