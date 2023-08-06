""" Test Management Tool """

# Version is replaced before building the package
__version__ = '1.20.0 (fb222fc)'

__all__ = [
    'Tree',
    'Test',
    'Plan',
    'Story',
    'Run',
    'Guest',
    'GuestSsh',
    'Result',
    'Status',
    'Clean']

from tmt.base import Clean, Plan, Run, Status, Story, Test, Tree
from tmt.result import Result
from tmt.steps.provision import Guest, GuestSsh
