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

from dataclasses import dataclass
from typing import Generic, Union, Callable

from dimod import SampleSet
from toolz.curried import pipe

from .mutation import Mutation, Mutator
from .recombination import Recombination, Recombinator
from .selection import Selection, Selector
from .startup import Startup
from .termination import Termination, Terminator
from .problem import ProblemType


@dataclass
class GeneticAlgorithm(Generic[ProblemType]):
    """Configurable implementation of a genetic algorithm.

    Solves minimisation problems of one specific subtype of `Problem`, i.e.
    problems that can be encoded as `dimod.BinaryQuadraticModel` potentially
    with additional domain knowledge.

    Returns a set of solutions as `dimod.SampleSet`. It is thus fully compatible
    with the `dimod`-API.

    This class itself is just a template that must be filled with respective
    components to work. `mutation`, `recombination`, and `selection` must
    thereby guarantee monotonicity, i.e. after their execution their best
    individual is not worse than the one of previous population.

    Args:
        startup (Startup[problemtype])): Determines the initial population. For
            instance, it can be random or used as a warm start.

        mutation (Mutation[ProblemType]): Improves quality of the current
            population by starting a local search from its individuals.

        recombination (Recombination[ProblemType]): Procreates new individuals
            by combining existing ones.

        selection (Selection[ProblemType]): Truncates low quality solutions to
            keep the population small.

        termination (Termination[ProblemType]): Allows to stop the algorithm if
            the population has achieved a certain quality level or takes too
            long.

    Note that this class is stateless, i.e. calling `optimise` multiple times
    parallelly works without any problems, as long as its components do not
    share a common object, for instance a file.

    """

    startup: Startup[ProblemType]
    mutation: Union[
        Mutation[ProblemType], Callable[[ProblemType], Mutator[ProblemType]]
    ]
    recombination: Union[
        Recombination[ProblemType], Callable[[ProblemType], Recombinator[ProblemType]]
    ]
    selection: Union[
        Selection[ProblemType], Callable[[ProblemType], Selector[ProblemType]]
    ]
    termination: Union[
        Termination[ProblemType], Callable[[ProblemType], Terminator[ProblemType]]
    ]

    def _factory_to_function(self, component, problem):
        return (component if callable(component) else component.initialise)(problem)

    def _initialise_components(self, problem: ProblemType):
        return [
            self._factory_to_function(component, problem)
            for component in [
                self.mutation,
                self.recombination,
                self.selection,
                self.termination,
            ]
        ]

    def optimise(self, problem: ProblemType) -> SampleSet:
        # Instantiate each component for a each optimisation run. Therefore, they have their own internal state that
        # should not interfere with the outside environment.
        mutator, recombinator, selector, terminator = self._initialise_components(
            problem
        )

        # Produce a first population
        population = self.startup.startup(problem)

        # Check termination condition, e.g. existence of a good solution.
        while not terminator.should_terminate(population):
            # Add new individuals by mutation and recombination.
            population = pipe(
                population,
                mutator.mutate,
                recombinator.recombine,
                # Truncate low quality individuals.
                selector.select,
            )

        return population
