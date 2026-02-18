import math


def clamp_angle(angle, min_angle, max_angle):
    val = int(round(float(angle)))
    if val < min_angle:
        return min_angle
    if val > max_angle:
        return max_angle
    return val


def trimmed_open_angle(open_angle, close_angle, reduction_deg):
    trim = max(0, int(reduction_deg))
    if open_angle > close_angle:
        return max(close_angle, open_angle - trim)
    if open_angle < close_angle:
        return min(close_angle, open_angle + trim)
    return open_angle


def ease_in_out(progress):
    if progress <= 0.0:
        return 0.0
    if progress >= 1.0:
        return 1.0
    return 0.5 - 0.5 * math.cos(math.pi * progress)


def ease_out_cubic(progress):
    if progress <= 0.0:
        return 0.0
    if progress >= 1.0:
        return 1.0
    p = 1.0 - progress
    return 1.0 - (p * p * p)


def calc_motion_duration(from_s1, from_s2, to_s1, to_s2, max_speed_dps, min_update_delay):
    max_delta = max(abs(to_s1 - from_s1), abs(to_s2 - from_s2))
    speed = max(1.0, float(max_speed_dps))
    return max(min_update_delay, max_delta / speed)


def is_hand_present(distance_mm, min_valid_mm, max_valid_mm):
    return min_valid_mm <= distance_mm <= max_valid_mm


def ewma_filter(prev_value, new_value, alpha):
    a = min(1.0, max(0.0, float(alpha)))
    if prev_value is None:
        return float(new_value)
    return (a * float(new_value)) + ((1.0 - a) * float(prev_value))
