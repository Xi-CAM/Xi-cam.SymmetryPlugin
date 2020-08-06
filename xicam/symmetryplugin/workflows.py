"""Defines an example workflow to use in the ExamplePlugin."""
from xicam.core.execution import Workflow

from .operations import symmetry


class SymmetryWorkflow(Workflow):
    """Example workflow that contains two operations: invert and random_noise"""
    def __init__(self):
        super(SymmetryWorkflow, self).__init__(name="Symmetry Workflow")

        # Create instances of our operations
        symmetry_op = symmetry()
        # Add our operations to the workflow
        self.add_operations(symmetry_op)
