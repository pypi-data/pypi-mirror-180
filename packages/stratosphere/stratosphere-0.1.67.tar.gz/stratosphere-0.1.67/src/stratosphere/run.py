from typing import Callable, List, Union

import pandas as pd
from stratosphere.store.db.database import next_ulid
from stratosphere.store.frames import json_normalize, reorder_columns
from stratosphere.utils.dicts import ObjectDictionary
from stratosphere.utils.text import stringify


class RunNotFoundException(Exception):
    """Exception raised if the run is not found."""

    def __init__(self, id_run):
        self.message = f"Run '{id_run}' not found. List with .df() the available runs."
        super().__init__(self.message)


class Runs(dict):
    def __init__(self, runs=None):
        if runs is None:
            runs = []

        if isinstance(runs, list) and len(runs) > 0 and isinstance(runs[0], Runs):
            # Context: we define a new experiment, passing in its definition
            # a list of Runs objects from 2+ experiments already executed.
            _runs = []
            for r in runs:
                _runs += r.values()
            runs = _runs
        elif isinstance(runs, Runs):
            # Context: we unpickle an experiment
            runs = runs.values()

        super().__init__({str(run.id_run): run for run in runs})

    def get_keys(self, name):
        if len(self) == 0:
            return []
        else:
            return list(getattr(self.first(), name).keys())

    def add(self, *runs_list):
        for runs in runs_list:
            for key in runs.keys():
                self[key] = runs[key]

    def first(self):
        return self[next(iter(self))]

    def df(self, max_level=None):
        # Load the dataframe from a dict or list of dicts.

        if len(self) == 0:
            # no runs!
            return pd.DataFrame(columns=["id_run"])

        df = json_normalize([{**run.fields, **{"id_run": run.id_run}} for run in self.values()], max_level=max_level)

        return reorder_columns(df, ["id_run"])

    def _repr_html_(self):
        return f"Runs(keys({len(self)})={stringify(self.keys())})"


class Run:
    """A run represents an instance of the experiment, obtained by
    combining the fixed and variable parameters. The Run objects
    (and the tracked fields)  must be serializable with cloudpickle.
    """

    def __init__(
        self,
        id_run: str = None,
        funcs: Union[Callable, List[Callable]] = None,
        kwargs: dict = None,
        params: dict = None,
        fields: dict = None,
    ):
        """Create a new run.

        Args:
            kwargs (dict, optional): Fixed parameters for all runs of an experiment. Defaults to None.
            parameters (dict, optional): Variable parameters to be considered for this run. Defaults to None.
            fields (dict, optional): fields to be tracked. Defaults to None.
            funcs (Union[Callable, List[Callable]], optional): One or more functions to be executed. Their
            only parameter is an instance of the Run class itself.
            experiment_name (str, optional): Name of the experiment the run belongs to. Defaults to None.
        """

        self.id_run = next_ulid() if id_run is None else id_run
        self.funcs = normalize_funcs(funcs)
        self.kwargs = ObjectDictionary(kwargs)
        self.params = ObjectDictionary(params)
        self.fields = ObjectDictionary(fields)
        self.exception = None

    def execute(self, funcs=None):
        if funcs is not None:
            self.funcs = normalize_funcs(funcs)

        self.exception = None

        for func in self.funcs:
            try:
                func(self)
            except Exception as e:  # noqa
                # We want to catch all exceptions in the distributed execution of runs,
                # It will then be reported by Experiment.execute.
                self.exception = f"{func.__qualname__.split('.')[0]}: {str(e)}"
                break

        return self

    def verify(self, func):
        func(self)

    def _repr_html_(self):
        return f'Run(id="{self.id_run}")'

    def df(self, max_level=None):
        # Load the dataframe from a dict or list of dicts.

        df = json_normalize([{**run.fields, **{"id_run": run.id_run}} for run in [self]], max_level=max_level)

        return reorder_columns(df, ["id_run"])


def normalize_funcs(funcs):
    if funcs is None:
        return []
    elif callable(funcs):
        return [funcs]
    else:
        return funcs
