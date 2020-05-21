#!/usr/local/bin/python3


class Constraint:
    def __init__(self, a, b, constraint_function):
        self.a = a
        self.b = b
        self.constraint_function = constraint_function

    def is_first(self, var):
        return self.a == var

    def is_second(self, var):
        return self.b == var

    def vars(self):
        return (self.a, self.b)

    def flip(self):
        return Constraint(self.b, self.a,
                          lambda b, a: self.constraint_function(a, b)
                          )

    def test(self, value_a, value_b):
        return self.constraint_function(value_a, value_b)

    def using(self, var):
        return self.a == var or self.b == var


def ac3(variables, domains, constraints):
    queue = []
    for c in constraints:
        queue.append(c)
        queue.append(c.flip())

    while len(queue) != 0:
        c = queue.pop(0)
        (a, b) = c.vars()
        changeddomain = revise(a, b, domains, c)

        if changeddomain:
            if len(domains[a]) == 0:
                return None

            for c in constraints:
                if c.using(b):
                    continue

                if c.is_first(a):
                    queue.append(c.flip())

                if c.is_second(a):
                    queue.append(c)


def revise(first, second, domains, constraint):
    changeddomain = False
    for value in domains[first]:
        matches = [v for v in domains[second] if constraint.test(value, v)]
        if len(matches) == 0:
            domains[first].remove(value)
            changeddomain = True

    return changeddomain



variables = ['a', 'b', 'c']
cons = [
    # A needs to b smaller than b
    Constraint('a', 'b', lambda a, b: a > b),
    # And B needs to be smaller than c
    Constraint('b', 'c', lambda b, c: b > c),
]

domains = {
    'a': [1, 2, 3],
    'b': [1, 2, 3],
    'c': [1, 2, 3],
}

ac3(variables, domains, cons)

print(domains)