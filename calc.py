import operator
from lookup import data


def error(msg):
    return f">> {msg}\n"


def calc(p, s):
    msg = ""
    try:
        p = int(p)
    except ValueError:
        try:
            p = float(p)
        except ValueError:
            return error("[P] and [s] must be numbers.")

    try:
        table = data[p]
    except KeyError:
        keys = sorted(data.keys())
        return error(f"[P] not found: {sorted(data.keys())}")

    try:
        s = int(s)
    except ValueError:
        try:
            s = float(s)
        except ValueError:
            return error("[P] and [s] must be numbers.")

    rows = sorted(table, key=operator.itemgetter(4))

    min_s = rows[0][4]
    max_s = rows[-1][4]
    if not min_s < s < max_s:
        return error(f"[s] out of range for [P]: {min_s}-{max_s}")

    for i, row in enumerate(rows):
        if row[4] >= s:
            lower_s_bound = rows[i - 1][4]
            upper_s_bound = row[4]
            lower_t_bound = rows[i - 1][0]
            upper_t_bound = row[0]
            lower_h_bound = rows[i - 1][3]
            upper_h_bound = row[3]
            break

    msg += f"[s] range: {lower_s_bound} - {upper_s_bound}\n"
    msg += f"[T] range: {lower_t_bound} - {upper_t_bound}\n"
    msg += f"[h] range: {lower_h_bound} - {upper_h_bound}\n"

    interpolated_t = lower_t_bound + (s - lower_s_bound) * (
        (upper_t_bound - lower_t_bound) / (upper_s_bound - lower_s_bound)
    )

    interpolated_h = lower_h_bound + (s - lower_s_bound) * (
        (upper_h_bound - lower_h_bound) / (upper_s_bound - lower_s_bound)
    )

    msg += f"\nInterpolated [T]: {interpolated_t}"
    msg += f"\nInterpolated [h]: {interpolated_h}"

    return msg
