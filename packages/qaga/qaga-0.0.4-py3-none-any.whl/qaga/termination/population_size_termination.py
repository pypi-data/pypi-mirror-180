# Copyright (C) 2022 PlanQK
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from dimod import SampleSet

from .termination import Terminator, Termination
from ..problem import ProblemType


class PopulationSizeTerminator(Terminator[ProblemType]):
    """Terminating an algorithm due too small population.

    Args:
        num_individuals: Positive number of individuals the
            population must at least contain.

    """

    def __init__(self, num_individuals: int):
        assert num_individuals > 0
        self._num_individuals = num_individuals

    def should_terminate(self, population: SampleSet) -> bool:
        """Checks if the population has at least `num_individuals` individuals.

        Returns:
            `True` to terminate if `population` has less individuals
            than `num_individuals`, `False` to proceed if not.

        """
        return len(population) < self._num_individuals


class PopulationSizeTermination(Termination[ProblemType]):
    """Configuration on how little individuals an algorithm terminates.

    This is the preferred way to guarantee termination for easy/testing problems.

    Args:
        num_individuals: Positive number of individuals the
            population must at least contain.

    """

    def __init__(self, num_individuals: int):
        assert num_individuals > 0
        self.num_individuals = num_individuals

    def initialise(self, problem: ProblemType) -> Terminator[ProblemType]:
        """Configurates a `PopulationSizeTerminator[ProblemType]` with the
        respective number of individuals.

        """
        return PopulationSizeTerminator[ProblemType](self.num_individuals)
