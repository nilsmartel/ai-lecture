#!/usr/local/bin/python3


def backtrack(variables, domain, constraints, setup={}):
    # Solution found
    if len(variables) == 0:
        return setup

    # create clones so we won't mutate call arguments
    setup = dict(setup)
    # Chose a variable and remove it from the remaing variables
    var = variables[0]
    variables = variables[1:]


    # set variable chosen at this step to all possilbe values
    # in domain
    for d in domain:
        setup[var] = d
        # all constraints are satisfied
        if all([c(setup) for c in constraints]):

            result = backtrack(variables, domain, constraints, setup)
            # No solutions found on this way
            if result is None:
                continue

            return result
    # No solution found
    return None

# Test Example from Lecture 4.2 - Backtracing
def example():
    variables = ['a', 'b', 'c']
    domain = [1, 2, 3]
    # Only returns false, if all keys
    # can be found inside the dict

    def req(d, keys):
        m = [key in d for key in keys]
        return not all(m)

    constraints = [
        lambda d: req(d, ['a', 'b']) or d['a'] > d['b'],
        lambda d: req(d, ['c', 'b']) or d['b'] != d['c'],
        lambda d: req(d, ['a', 'c']) or d['a'] != d['c'],
    ]
    backtrack(variables, domain, constraints)


result = example()

print(result)
