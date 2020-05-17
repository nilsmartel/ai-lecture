#!/usr/local/bin/python3


def backtrack(variables, domain, constraints, setup={}):
    # create clones so we won't mutate call arguments
    setup = dict(setup)
    variables = list(variables)
    # Chose a variable and remove it from the remaing variables
    var = variables.pop()
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
    # Only returns true, if all keys
    # can be found inside the dict
    def req(d, keys):
        m = [key in d for key in keys]
        return all(m)
    constraints = [
        lambda d: req(d, ['a', 'b']) and d['a'] > d['b'],
        lambda d: req(d, ['c', 'b']) and d['b'] != d['c'],
        lambda d: req(d, ['a', 'c']) and d['a'] != d['c'],
    ]
    backtrack(variables, domain, constraints)

result = example()

print(result)
