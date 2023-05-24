import numpy as np
import pytest

from fuzzy_system import fuzzy_system


@pytest.fixture(scope="module")
def system_setup():
    return fuzzy_system()


@pytest.mark.parametrize(
    "error, delta, expected",
    [
        (-2, -2, -1.666),
        (-2, 0, -1),
        (0, -2, -1),
        (-2, 2, 0),
        (0, 0, 0),
        (2, -2, 0),
        (0, 2, 1),
        (2, 0, 1),
        (2, 2, 1.666),
    ],
)
def test_fuzzy_system(system_setup, error, delta, expected):
    sim = system_setup
    sim.input["error"] = error
    sim.input["delta"] = delta
    sim.compute()
    print(f"Error: {error}, Delta: {delta}, Output: {sim.output['output']}")
    assert np.isclose(sim.output["output"], expected, atol=0.001)
