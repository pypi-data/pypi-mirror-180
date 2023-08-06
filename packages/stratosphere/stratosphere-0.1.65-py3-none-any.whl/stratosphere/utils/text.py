import json
from collections.abc import KeysView


def stringify(d: object, max_len=200):
    if isinstance(d, KeysView):
        d = list(d)

    s = json.dumps(d)
    if len(s) > max_len:
        if isinstance(d, list):
            s = s[:max_len] + " ...]"
        elif isinstance(d, dict):
            s = s[:max_len] + " ...}"
        else:
            s = s[:max_len] + " ..."
    return s
