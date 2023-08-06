import warnings

from stratosphere.utils.environment import is_pyodide

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    from tqdm.auto import tqdm

    if is_pyodide():
        tqdm.monitor_interval = 0


def progress(*args, **kwargs):
    return tqdm(*args, **kwargs, leave=False, delay=1)
