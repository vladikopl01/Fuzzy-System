# Fuzzy Logic System

## Description

Many fuzzy control systems are tasked to keep a certain variable close to a specific value. For instance, the temperature for _an industrial chemical process_ or for _home heating management system_ might need to be kept relatively constant.

In order to do this, the system could look like this:

- Antecednets (Inputs):

  - `error`: How far away is the temperature from where we want it to be?
  - `delta`: How fast is the temperature changing?

- Consequents (Outputs):

  - `output`: How much should we adjust the temperature?

- Fuzzy sets (Membership Functions):

  - Negative Big: _nb = -2_
  - Negative Small: _ns = -1_
  - Zero: _ze = 0_
  - Positive Small: _ps = 1_
  - Positive Big: _pb = 2_

- Rules:

  - Negative Big: IF `error` == nb OR `delta` == nb
  - Negative Small: IF `error` <= ns AND `delta` <= ps OR `error` <= ps AND `delta` <= ns
  - Zero: IF `error` AND `delta` == ze
  - Positive Small: IF `error` >= ps AND `delta` >= ns OR `error` >= ns AND `delta` >= ps
  - Positive Big: IF `error` == pb OR `delta` == pb

> The system is implemented in Python and uses the [scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/) library.

## Installation

To install the system, you must first install the dependencies. The dependencies are listed in the `requirements.txt` file. To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the system, you must first create a new Python file. In this file, you must import the `fuzzy_system` function from the `fuzzy_system` module. You can then create a new instance of the Fuzzy System and get output predictions based on your input values.

```python
from fuzzy_system import fuzzy_system

sim = fuzzy_system()

sim.input["error"] = -2
sim.input["delta"] = 0
print(sim.output["output"])
# Prints -1

sim.input["error"] = 2
sim.input["delta"] = 0
print(sim.output["output"])
# Prints 1

sim.input["error"] = 0
sim.input["delta"] = 0
print(sim.output["output"])
# Prints 0
```

## Full set of Rules

Rule Negative Big:

- IF `error` == nb AND `delta` == nb THEN `output` = nb.
- IF `error` == nb AND `delta` == ns THEN `output` = nb.
- IF `error` == ns AND `delta` == nb THEN `output` = nb.

Rule Negative Small:

- IF `error` == nb AND `delta` == ze THEN `output` = ns.
- IF `error` == nb AND `delta` == ps THEN `output` = ns.
- IF `error` == ns AND `delta` == ns THEN `output` = ns.
- IF `error` == ns AND `delta` == ze THEN `output` = ns.
- IF `error` == ze AND `delta` == ns THEN `output` = ns.
- IF `error` == ze AND `delta` == nb THEN `output` = ns.
- IF `error` == ps AND `delta` == nb THEN `output` = ns.

Rule Zero:

- IF `error` == nb AND `delta` == pb THEN `output` = ze.
- IF `error` == ns AND `delta` == ps THEN `output` = ze.
- IF `error` == ze AND `delta` == ze THEN `output` = ze.
- IF `error` == ps AND `delta` == ns THEN `output` = ze.
- IF `error` == pb AND `delta` == nb THEN `output` = ze.

Rule Positive Small:

- IF `error` == ns AND `delta` == pb THEN `output` = ps.
- IF `error` == ze AND `delta` == pb THEN `output` = ps.
- IF `error` == ze AND `delta` == ps THEN `output` = ps.
- IF `error` == ps AND `delta` == ps THEN `output` = ps.
- IF `error` == ps AND `delta` == ze THEN `output` = ps.
- IF `error` == pb AND `delta` == ze THEN `output` = ps.
- IF `error` == pb AND `delta` == ns THEN `output` = ps.

Rule Positive Big:

- IF `error` == ps AND `delta` == pb THEN `output` = pb.
- IF `error` == pb AND `delta` == ps THEN `output` = pb.
- IF `error` == pb AND `delta` == pb THEN `output` = pb.
