def parse_duration(s):
    """Parse a human-readable duration string into a total number of seconds (int).

    Supported units (case-insensitive): d = 86400s, h = 3600s, m = 60s, s = 1s.
    A duration may combine multiple units in any order, e.g. "1h30m", "2d4h",
    "90s", "45m10s", "1d". Whitespace around or between tokens is allowed
    ("1h 30m"). Numbers are non-negative integers.

    Return the total number of seconds as an int. "0s" returns 0.

    Raise ValueError for input that is not a valid duration: the empty string,
    unknown units, a unit with no number, a number with no unit, or any leftover
    non-duration characters.
    """
    raise NotImplementedError
