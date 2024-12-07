"""
This type stub file was generated by pyright.
"""

import copy
import doctest
import random

from .compat import xrange
from .version import (
    __author__,
    __copyright__,
    __credits__,
    __email__,
    __license__,
    __status__,
    __url__,
    __version__,
)

"""
@var Unassigned: Helper object instance representing unassigned values

@sort: Problem, Variable, Domain
@group Solvers: Solver,
                BacktrackingSolver,
                RecursiveBacktrackingSolver,
                MinConflictsSolver
@group Constraints: Constraint,
                    FunctionConstraint,
                    AllDifferentConstraint,
                    AllEqualConstraint,
                    MaxSumConstraint,
                    ExactSumConstraint,
                    MinSumConstraint,
                    InSetConstraint,
                    NotInSetConstraint,
                    SomeInSetConstraint,
                    SomeNotInSetConstraint
"""
__all__ = [
    "Problem",
    "Variable",
    "Domain",
    "Unassigned",
    "Solver",
    "BacktrackingSolver",
    "RecursiveBacktrackingSolver",
    "MinConflictsSolver",
    "Constraint",
    "FunctionConstraint",
    "AllDifferentConstraint",
    "AllEqualConstraint",
    "MaxSumConstraint",
    "ExactSumConstraint",
    "MinSumConstraint",
    "InSetConstraint",
    "NotInSetConstraint",
    "SomeInSetConstraint",
    "SomeNotInSetConstraint",
]

class Problem:
    """
    Class used to define a problem and retrieve solutions
    """
    def __init__(self, solver=...) -> None:
        """
        @param solver: Problem solver used to find solutions
                       (default is L{BacktrackingSolver})
        @type solver:  instance of a L{Solver} subclass
        """
        ...

    def reset(self):  # -> None:
        """
        Reset the current problem definition

        Example:

        >>> problem = Problem()
        >>> problem.addVariable("a", [1, 2])
        >>> problem.reset()
        >>> problem.getSolution()
        >>>
        """
        ...

    def setSolver(self, solver):  # -> None:
        """
        Change the problem solver currently in use

        Example:

        >>> solver = BacktrackingSolver()
        >>> problem = Problem(solver)
        >>> problem.getSolver() is solver
        True

        @param solver: New problem solver
        @type  solver: instance of a C{Solver} subclass
        """
        ...

    def getSolver(self):  # -> BacktrackingSolver:
        """
        Obtain the problem solver currently in use

        Example:

        >>> solver = BacktrackingSolver()
        >>> problem = Problem(solver)
        >>> problem.getSolver() is solver
        True

        @return: Solver currently in use
        @rtype: instance of a L{Solver} subclass
        """
        ...

    def addVariable(self, variable, domain):  # -> None:
        """
        Add a variable to the problem

        Example:

        >>> problem = Problem()
        >>> problem.addVariable("a", [1, 2])
        >>> problem.getSolution() in ({'a': 1}, {'a': 2})
        True

        @param variable: Object representing a problem variable
        @type  variable: hashable object
        @param domain: Set of items defining the possible values that
                       the given variable may assume
        @type  domain: list, tuple, or instance of C{Domain}
        """
        ...

    def addVariables(self, variables, domain):  # -> None:
        """
        Add one or more variables to the problem

        Example:

        >>> problem = Problem()
        >>> problem.addVariables(["a", "b"], [1, 2, 3])
        >>> solutions = problem.getSolutions()
        >>> len(solutions)
        9
        >>> {'a': 3, 'b': 1} in solutions
        True

        @param variables: Any object containing a sequence of objects
                          represeting problem variables
        @type  variables: sequence of hashable objects
        @param domain: Set of items defining the possible values that
                       the given variables may assume
        @type  domain: list, tuple, or instance of C{Domain}
        """
        ...

    def addConstraint(self, constraint, variables=...):  # -> None:
        """
        Add a constraint to the problem

        Example:

        >>> problem = Problem()
        >>> problem.addVariables(["a", "b"], [1, 2, 3])
        >>> problem.addConstraint(lambda a, b: b == a+1, ["a", "b"])
        >>> solutions = problem.getSolutions()
        >>>

        @param constraint: Constraint to be included in the problem
        @type  constraint: instance a L{Constraint} subclass or a
                           function to be wrapped by L{FunctionConstraint}
        @param variables: Variables affected by the constraint (default to
                          all variables). Depending on the constraint type
                          the order may be important.
        @type  variables: set or sequence of variables
        """
        ...

    def getSolution(self):  # -> dict[Any, Any] | None:
        """
        Find and return a solution to the problem

        Example:

        >>> problem = Problem()
        >>> problem.getSolution() is None
        True
        >>> problem.addVariables(["a"], [42])
        >>> problem.getSolution()
        {'a': 42}

        @return: Solution for the problem
        @rtype: dictionary mapping variables to values
        """
        ...

    def getSolutions(self):  # -> list[Any] | list[dict[Any, Any]]:
        """
        Find and return all solutions to the problem

        Example:

        >>> problem = Problem()
        >>> problem.getSolutions() == []
        True
        >>> problem.addVariables(["a"], [42])
        >>> problem.getSolutions()
        [{'a': 42}]

        @return: All solutions for the problem
        @rtype: list of dictionaries mapping variables to values
        """
        ...

    def getSolutionIter(
        self,
    ):  # -> Iterator[Never] | Generator[dict[Any, Any], Any, None]:
        """
        Return an iterator to the solutions of the problem

        Example:

        >>> problem = Problem()
        >>> list(problem.getSolutionIter()) == []
        True
        >>> problem.addVariables(["a"], [42])
        >>> iter = problem.getSolutionIter()
        >>> next(iter)
        {'a': 42}
        >>> next(iter)
        Traceback (most recent call last):
          File "<stdin>", line 1, in ?
        StopIteration
        """
        ...

def getArcs(domains, constraints):  # -> dict[Any, Any]:
    """
    Return a dictionary mapping pairs (arcs) of constrained variables

    @attention: Currently unused.
    """
    ...

def doArc8(arcs, domains, assignments):  # -> bool:
    """
    Perform the ARC-8 arc checking algorithm and prune domains

    @attention: Currently unused.
    """
    ...

class Solver:
    """
    Abstract base class for solvers

    @sort: getSolution, getSolutions, getSolutionIter
    """
    def getSolution(self, domains, constraints, vconstraints):
        """
        Return one solution for the given problem

        @param domains: Dictionary mapping variables to their domains
        @type  domains: dict
        @param constraints: List of pairs of (constraint, variables)
        @type  constraints: list
        @param vconstraints: Dictionary mapping variables to a list of
                             constraints affecting the given variables.
        @type  vconstraints: dict
        """
        ...

    def getSolutions(self, domains, constraints, vconstraints):
        """
        Return all solutions for the given problem

        @param domains: Dictionary mapping variables to domains
        @type  domains: dict
        @param constraints: List of pairs of (constraint, variables)
        @type  constraints: list
        @param vconstraints: Dictionary mapping variables to a list of
                             constraints affecting the given variables.
        @type  vconstraints: dict
        """
        ...

    def getSolutionIter(self, domains, constraints, vconstraints):
        """
        Return an iterator for the solutions of the given problem

        @param domains: Dictionary mapping variables to domains
        @type  domains: dict
        @param constraints: List of pairs of (constraint, variables)
        @type  constraints: list
        @param vconstraints: Dictionary mapping variables to a list of
                             constraints affecting the given variables.
        @type  vconstraints: dict
        """
        ...

class BacktrackingSolver(Solver):
    """
    Problem solver with backtracking capabilities

    Examples:

    >>> result = [[('a', 1), ('b', 2)],
    ...           [('a', 1), ('b', 3)],
    ...           [('a', 2), ('b', 3)]]

    >>> problem = Problem(BacktrackingSolver())
    >>> problem.addVariables(["a", "b"], [1, 2, 3])
    >>> problem.addConstraint(lambda a, b: b > a, ["a", "b"])

    >>> solution = problem.getSolution()
    >>> sorted(solution.items()) in result
    True

    >>> for solution in problem.getSolutionIter():
    ...     sorted(solution.items()) in result
    True
    True
    True

    >>> for solution in problem.getSolutions():
    ...     sorted(solution.items()) in result
    True
    True
    True
    """
    def __init__(self, forwardcheck=...) -> None:
        """
        @param forwardcheck: If false forward checking will not be requested
                             to constraints while looking for solutions
                             (default is true)
        @type  forwardcheck: bool
        """
        ...

    def getSolutionIter(
        self, domains, constraints, vconstraints
    ):  # -> Generator[dict[Any, Any], Any, None]:
        ...
    def getSolution(
        self, domains, constraints, vconstraints
    ):  # -> dict[Any, Any] | None:
        ...
    def getSolutions(
        self, domains, constraints, vconstraints
    ):  # -> list[dict[Any, Any]]:
        ...

class RecursiveBacktrackingSolver(Solver):
    """
    Recursive problem solver with backtracking capabilities

    Examples:

    >>> result = [[('a', 1), ('b', 2)],
    ...           [('a', 1), ('b', 3)],
    ...           [('a', 2), ('b', 3)]]

    >>> problem = Problem(RecursiveBacktrackingSolver())
    >>> problem.addVariables(["a", "b"], [1, 2, 3])
    >>> problem.addConstraint(lambda a, b: b > a, ["a", "b"])

    >>> solution = problem.getSolution()
    >>> sorted(solution.items()) in result
    True

    >>> for solution in problem.getSolutions():
    ...     sorted(solution.items()) in result
    True
    True
    True

    >>> problem.getSolutionIter()
    Traceback (most recent call last):
       ...
    NotImplementedError: RecursiveBacktrackingSolver doesn't provide iteration
    """
    def __init__(self, forwardcheck=...) -> None:
        """
        @param forwardcheck: If false forward checking will not be requested
                             to constraints while looking for solutions
                             (default is true)
        @type  forwardcheck: bool
        """
        ...

    def recursiveBacktracking(
        self, solutions, domains, vconstraints, assignments, single
    ): ...
    def getSolution(self, domains, constraints, vconstraints):  # -> None:
        ...
    def getSolutions(self, domains, constraints, vconstraints): ...

class MinConflictsSolver(Solver):
    """
    Problem solver based on the minimum conflicts theory

    Examples:

    >>> result = [[('a', 1), ('b', 2)],
    ...           [('a', 1), ('b', 3)],
    ...           [('a', 2), ('b', 3)]]

    >>> problem = Problem(MinConflictsSolver())
    >>> problem.addVariables(["a", "b"], [1, 2, 3])
    >>> problem.addConstraint(lambda a, b: b > a, ["a", "b"])

    >>> solution = problem.getSolution()
    >>> sorted(solution.items()) in result
    True

    >>> problem.getSolutions()
    Traceback (most recent call last):
       ...
    NotImplementedError: MinConflictsSolver provides only a single solution

    >>> problem.getSolutionIter()
    Traceback (most recent call last):
       ...
    NotImplementedError: MinConflictsSolver doesn't provide iteration
    """
    def __init__(self, steps=...) -> None:
        """
        @param steps: Maximum number of steps to perform before giving up
                      when looking for a solution (default is 1000)
        @type  steps: int
        """
        ...

    def getSolution(
        self, domains, constraints, vconstraints
    ):  # -> dict[Any, Any] | None:
        ...

class Variable:
    """
    Helper class for variable definition

    Using this class is optional, since any hashable object,
    including plain strings and integers, may be used as variables.
    """
    def __init__(self, name) -> None:
        """
        @param name: Generic variable name for problem-specific purposes
        @type  name: string
        """
        ...

    def __repr__(self):  # -> Any:
        ...

Unassigned = ...

class Domain(list):
    """
    Class used to control possible values for variables

    When list or tuples are used as domains, they are automatically
    converted to an instance of that class.
    """
    def __init__(self, set) -> None:
        """
        @param set: Set of values that the given variables may assume
        @type  set: set of objects comparable by equality
        """
        ...

    def resetState(self):  # -> None:
        """
        Reset to the original domain state, including all possible values
        """
        ...

    def pushState(self):  # -> None:
        """
        Save current domain state

        Variables hidden after that call are restored when that state
        is popped from the stack.
        """
        ...

    def popState(self):  # -> None:
        """
        Restore domain state from the top of the stack

        Variables hidden since the last popped state are then available
        again.
        """
        ...

    def hideValue(self, value):  # -> None:
        """
        Hide the given value from the domain

        After that call the given value won't be seen as a possible value
        on that domain anymore. The hidden value will be restored when the
        previous saved state is popped.

        @param value: Object currently available in the domain
        """
        ...

class Constraint:
    """
    Abstract base class for constraints
    """
    def __call__(
        self, variables, domains, assignments, forwardcheck=...
    ):  # -> Literal[True]:
        """
        Perform the constraint checking

        If the forwardcheck parameter is not false, besides telling if
        the constraint is currently broken or not, the constraint
        implementation may choose to hide values from the domains of
        unassigned variables to prevent them from being used, and thus
        prune the search space.

        @param variables: Variables affected by that constraint, in the
                          same order provided by the user
        @type  variables: sequence
        @param domains: Dictionary mapping variables to their domains
        @type  domains: dict
        @param assignments: Dictionary mapping assigned variables to their
                            current assumed value
        @type  assignments: dict
        @param forwardcheck: Boolean value stating whether forward checking
                             should be performed or not
        @return: Boolean value stating if this constraint is currently
                 broken or not
        @rtype: bool
        """
        ...

    def preProcess(
        self, variables, domains, constraints, vconstraints
    ):  # -> None:
        """
        Preprocess variable domains

        This method is called before starting to look for solutions,
        and is used to prune domains with specific constraint logic
        when possible. For instance, any constraints with a single
        variable may be applied on all possible values and removed,
        since they may act on individual values even without further
        knowledge about other assignments.

        @param variables: Variables affected by that constraint, in the
                          same order provided by the user
        @type  variables: sequence
        @param domains: Dictionary mapping variables to their domains
        @type  domains: dict
        @param constraints: List of pairs of (constraint, variables)
        @type  constraints: list
        @param vconstraints: Dictionary mapping variables to a list of
                             constraints affecting the given variables.
        @type  vconstraints: dict
        """
        ...

    def forwardCheck(
        self, variables, domains, assignments, _unassigned=...
    ):  # -> bool:
        """
        Helper method for generic forward checking

        Currently, this method acts only when there's a single
        unassigned variable.

        @param variables: Variables affected by that constraint, in the
                          same order provided by the user
        @type  variables: sequence
        @param domains: Dictionary mapping variables to their domains
        @type  domains: dict
        @param assignments: Dictionary mapping assigned variables to their
                            current assumed value
        @type  assignments: dict
        @return: Boolean value stating if this constraint is currently
                 broken or not
        @rtype: bool
        """
        ...

class FunctionConstraint(Constraint):
    """
    Constraint which wraps a function defining the constraint logic

    Examples:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> def func(a, b):
    ...     return b > a
    >>> problem.addConstraint(func, ["a", "b"])
    >>> problem.getSolution()
    {'a': 1, 'b': 2}

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> def func(a, b):
    ...     return b > a
    >>> problem.addConstraint(FunctionConstraint(func), ["a", "b"])
    >>> problem.getSolution()
    {'a': 1, 'b': 2}
    """
    def __init__(self, func, assigned=...) -> None:
        """
        @param func: Function wrapped and queried for constraint logic
        @type  func: callable object
        @param assigned: Whether the function may receive unassigned
                         variables or not
        @type  assigned: bool
        """
        ...

    def __call__(
        self,
        variables,
        domains,
        assignments,
        forwardcheck=...,
        _unassigned=...,
    ):  # -> bool:
        ...

class AllDifferentConstraint(Constraint):
    """
    Constraint enforcing that values of all given variables are different

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(AllDifferentConstraint())
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 2)], [('a', 2), ('b', 1)]]
    """
    def __call__(
        self,
        variables,
        domains,
        assignments,
        forwardcheck=...,
        _unassigned=...,
    ):  # -> bool:
        ...

class AllEqualConstraint(Constraint):
    """
    Constraint enforcing that values of all given variables are equal

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(AllEqualConstraint())
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 1)], [('a', 2), ('b', 2)]]
    """
    def __call__(
        self,
        variables,
        domains,
        assignments,
        forwardcheck=...,
        _unassigned=...,
    ):  # -> bool:
        ...

class MaxSumConstraint(Constraint):
    """
    Constraint enforcing that values of given variables sum up to
    a given amount

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(MaxSumConstraint(3))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 1)], [('a', 1), ('b', 2)], [('a', 2), ('b', 1)]]
    """
    def __init__(self, maxsum, multipliers=...) -> None:
        """
        @param maxsum: Value to be considered as the maximum sum
        @type  maxsum: number
        @param multipliers: If given, variable values will be multiplied by
                            the given factors before being summed to be checked
        @type  multipliers: sequence of numbers
        """
        ...

    def preProcess(
        self, variables, domains, constraints, vconstraints
    ):  # -> None:
        ...
    def __call__(
        self, variables, domains, assignments, forwardcheck=...
    ):  # -> bool:
        ...

class ExactSumConstraint(Constraint):
    """
    Constraint enforcing that values of given variables sum exactly
    to a given amount

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(ExactSumConstraint(3))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 2)], [('a', 2), ('b', 1)]]
    """
    def __init__(self, exactsum, multipliers=...) -> None:
        """
        @param exactsum: Value to be considered as the exact sum
        @type  exactsum: number
        @param multipliers: If given, variable values will be multiplied by
                            the given factors before being summed to be checked
        @type  multipliers: sequence of numbers
        """
        ...

    def preProcess(
        self, variables, domains, constraints, vconstraints
    ):  # -> None:
        ...
    def __call__(
        self, variables, domains, assignments, forwardcheck=...
    ):  # -> bool:
        ...

class MinSumConstraint(Constraint):
    """
    Constraint enforcing that values of given variables sum at least
    to a given amount

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(MinSumConstraint(3))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 2)], [('a', 2), ('b', 1)], [('a', 2), ('b', 2)]]
    """
    def __init__(self, minsum, multipliers=...) -> None:
        """
        @param minsum: Value to be considered as the minimum sum
        @type  minsum: number
        @param multipliers: If given, variable values will be multiplied by
                            the given factors before being summed to be checked
        @type  multipliers: sequence of numbers
        """
        ...

    def __call__(
        self, variables, domains, assignments, forwardcheck=...
    ):  # -> bool:
        ...

class InSetConstraint(Constraint):
    """
    Constraint enforcing that values of given variables are present in
    the given set

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(InSetConstraint([1]))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 1)]]
    """
    def __init__(self, set) -> None:
        """
        @param set: Set of allowed values
        @type  set: set
        """
        ...

    def __call__(self, variables, domains, assignments, forwardcheck=...): ...
    def preProcess(
        self, variables, domains, constraints, vconstraints
    ):  # -> None:
        ...

class NotInSetConstraint(Constraint):
    """
    Constraint enforcing that values of given variables are not present in
    the given set

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(NotInSetConstraint([1]))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 2), ('b', 2)]]
    """
    def __init__(self, set) -> None:
        """
        @param set: Set of disallowed values
        @type  set: set
        """
        ...

    def __call__(self, variables, domains, assignments, forwardcheck=...): ...
    def preProcess(
        self, variables, domains, constraints, vconstraints
    ):  # -> None:
        ...

class SomeInSetConstraint(Constraint):
    """
    Constraint enforcing that at least some of the values of given
    variables must be present in a given set

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(SomeInSetConstraint([1]))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 1)], [('a', 1), ('b', 2)], [('a', 2), ('b', 1)]]
    """
    def __init__(self, set, n=..., exact=...) -> None:
        """
        @param set: Set of values to be checked
        @type  set: set
        @param n: Minimum number of assigned values that should be present
                  in set (default is 1)
        @type  n: int
        @param exact: Whether the number of assigned values which are
                      present in set must be exactly C{n}
        @type  exact: bool
        """
        ...

    def __call__(
        self, variables, domains, assignments, forwardcheck=...
    ):  # -> bool:
        ...

class SomeNotInSetConstraint(Constraint):
    """
    Constraint enforcing that at least some of the values of given
    variables must not be present in a given set

    Example:

    >>> problem = Problem()
    >>> problem.addVariables(["a", "b"], [1, 2])
    >>> problem.addConstraint(SomeNotInSetConstraint([1]))
    >>> sorted(sorted(x.items()) for x in problem.getSolutions())
    [[('a', 1), ('b', 2)], [('a', 2), ('b', 1)], [('a', 2), ('b', 2)]]
    """
    def __init__(self, set, n=..., exact=...) -> None:
        """
        @param set: Set of values to be checked
        @type  set: set
        @param n: Minimum number of assigned values that should not be present
                  in set (default is 1)
        @type  n: int
        @param exact: Whether the number of assigned values which are
                      not present in set must be exactly C{n}
        @type  exact: bool
        """
        ...

    def __call__(
        self, variables, domains, assignments, forwardcheck=...
    ):  # -> bool:
        ...

if __name__ == "__main__": ...