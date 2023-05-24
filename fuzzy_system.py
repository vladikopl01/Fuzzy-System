import numpy as np
import skfuzzy.control as ctrl


def fuzzy_system():
    # Sparse universe makes calculations faster, without sacrifice accuracy.
    universe = np.linspace(-2, 2, 5)

    # Create the three fuzzy variables - two inputs, one output
    # - The error, or deviation from the ideal value
    # - The way the error is changing. This is the mathematical first derivative
    error = ctrl.Antecedent(universe, "error")
    delta = ctrl.Antecedent(universe, "delta")
    output = ctrl.Consequent(universe, "output")

    # Generate fuzzy membership functions
    # Negative Big, Negative Small, Zero, Positive Small, Positive Big
    names = ["nb", "ns", "ze", "ps", "pb"]
    error.automf(names=names)
    delta.automf(names=names)
    output.automf(names=names)

    # Negative Big: IF `error` == nb OR `delta` == nb
    rule0 = ctrl.Rule(
        antecedent=(
            (error["nb"] & delta["nb"])
            | (error["ns"] & delta["nb"])
            | (error["nb"] & delta["ns"])
        ),
        consequent=output["nb"],
        label="rule nb",
    )

    # Negative Small: IF `error` <= ns AND `delta` <= ps OR `error` <= ps AND `delta` <= ns
    rule1 = ctrl.Rule(
        antecedent=(
            (error["nb"] & delta["ze"])
            | (error["nb"] & delta["ps"])
            | (error["ns"] & delta["ns"])
            | (error["ns"] & delta["ze"])
            | (error["ze"] & delta["ns"])
            | (error["ze"] & delta["nb"])
            | (error["ps"] & delta["nb"])
        ),
        consequent=output["ns"],
        label="rule ns",
    )

    # Zero: IF `error` AND `delta` == ze
    rule2 = ctrl.Rule(
        antecedent=(
            (error["nb"] & delta["pb"])
            | (error["ns"] & delta["ps"])
            | (error["ze"] & delta["ze"])
            | (error["ps"] & delta["ns"])
            | (error["pb"] & delta["nb"])
        ),
        consequent=output["ze"],
        label="rule ze",
    )

    # Positive Small: IF `error` >= ps AND `delta` >= ns OR `error` >= ns AND `delta` >= ps
    rule3 = ctrl.Rule(
        antecedent=(
            (error["ns"] & delta["pb"])
            | (error["ze"] & delta["pb"])
            | (error["ze"] & delta["ps"])
            | (error["ps"] & delta["ps"])
            | (error["ps"] & delta["ze"])
            | (error["pb"] & delta["ze"])
            | (error["pb"] & delta["ns"])
        ),
        consequent=output["ps"],
        label="rule ps",
    )

    # Positive Big: IF `error` == pb OR `delta` == pb
    rule4 = ctrl.Rule(
        antecedent=(
            (error["ps"] & delta["pb"])
            | (error["pb"] & delta["pb"])
            | (error["pb"] & delta["ps"])
        ),
        consequent=output["pb"],
        label="rule pb",
    )

    system = ctrl.ControlSystem(rules=[rule0, rule1, rule2, rule3, rule4])
    sim = ctrl.ControlSystemSimulation(system, flush_after_run=21 * 21 + 1)
    return sim
