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

import numpy as np
from numpy.random import Generator, default_rng
from dimod import SampleSet
from typing import Callable

from .recombination import Recombinator
from .pair_recombination import PairRecombinator, PairRecombination
from ..problem import ProblemType


class RandomSectionsRecombinator(PairRecombinator[ProblemType]):
    """Pairwise recombination by flipping sections between bits.

    Randomly chooses bits that divide the genomes into sections, and flips
    the bits of every other section. Dividing bits belong to the section
    on their right. This is also known as k-point-crossover.

    Args:
        problem (ProblemType): The problem to perform recombination.

        num_bits (int): Positive, number of dividing bits. It must be at
        least 1 and smaller than the population size.

        recombination_rate (int): Positive number suggesting the amount of mates
            each individual is assigned to.

            The actual number can be both below or above this value depending on
            the existence of an appropriate apportionment. For instance, in a
            population consisting of two elements one cannot mate with more than
            one individual.

        rng (Generator, optional): A random number generator that can be
            specified if reproducability is needed.

    """

    def __init__(
        self,
        problem: ProblemType,
        num_bits: int,
        recombination_rate: int,
        rng: Generator = default_rng(),
    ):

        assert num_bits < len(
            self._problem.bqm
        ), f"Cannot divide a genome of length {len(self._problem.bqm)} in {num_bits+1} sections."
        assert num_bits >= 1, f"There must be at least one diving bit."

        self._problem = problem
        self._num_bits = num_bits
        super().__init__(recombination_rate, rng)

    def _mate(self, population: SampleSet, pairs: np.ndarray) -> SampleSet:
        strings = population.record.sample
        left = strings[pairs[0]]
        right = strings[pairs[1]]

        result = np.zeros((2 * len(pairs), strings.shape[1]), dtype=strings.dtype)

        indices = self._rng.choice()
        for i in range(len(pairs)):
            bits = self._rng.choice(len(population), size=self._num_bits, replace=False)
            bits = np.sort(bits)

            result[i] = left[i]
            j = 2 * i
            result[j] = right[i]

            section_start = 0
            should_swap = False
            for end_index in range(self._num_bits):
                section_end = bits[end_index]
                self._swap(
                    left[i],
                    result[i],
                    right[i],
                    result[j],
                    section_start,
                    section_end,
                    should_swap,
                )
                should_swap = not should_swap
                section_start = section_end

            section_end = -1
            self._swap(
                left[i],
                result[i],
                right[i],
                result[j],
                section_start,
                section_end,
                should_swap,
            )

        return SampleSet.from_samples_bqm(
            (result, self._problem.bqm.variables),
            self._problem.bqm,
            aggregate_samples=True,
        )

    def _swap(
        left_source,
        left_target,
        right_source,
        right_target,
        section_start,
        section_end,
        should_swap,
    ):
        if should_swap:
            left_target[section_start:section_end] = right_source[
                section_start:section_end
            ]
            right_target[section_start:section_end] = left_source[
                section_start:section_end
            ]


class RandomSectionsRecombination(PairRecombination[ProblemType]):
    """Configuration of pairwise recombination by flipping sections of bits.

    For random pairs of individuals bits are randomly choosen dividing genomes
    in sections for which every other one is flipped. It is a simple,
    uninformed recombination procedure.

    Does not guarantee monotonicity.

    Args:
        num_bits (int): Positive, number of dividing bits. It must be at
            least 1 and smaller than the population size.

        recombination_rate (int): Positive number suggesting the amount of mates
            each individual is assigned to.

            The actual number can be both below or above this value depending on
            the existence of an appropriate apportionment. For instance, in a
            population consisting of two elements one cannot mate with more than
            one individual.

        rng (Callable[[], Generator]], optional): A function that creates an
            isolated random number generator that can be specified if
            reproducability is needed.

    """

    def __init__(
        self, num_bits: int, recombination_rate: int, rng: Callable[[], Generator]
    ):
        self._num_bits = num_bits
        super().__init__(recombination_rate, rng)

    def initialise(self, problem: ProblemType) -> Recombinator[ProblemType]:
        """Configures a `RandomSectionsRecombination[ProblemType]` with respective
        `num_bits` and `recombination_rate`.

        """
        return RandomSectionsRecombinator[ProblemType](
            problem, self._num_bits, self._recombination_rate, self._rng()
        )
