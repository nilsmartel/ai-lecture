class UnaryConstraint:
    def __init__(self, var, tst):
        self.var = var
        self.tst

    def get_vars(self):
        return list(self.var)

    def test(self, value):
        return self.tst(value)


class BinaryConstraint:
    def __init__(self, var1, var2, tst):
        self.var1 = var1
        self.var2 = var2
        self.tst

    def get_vars(self):
        return list(self.var1, self.var2)

    def test(self, var1, var2):
        return self.tst(var1, var2)


X = ['x', 'y']

D = {
    'x': range(6),
    'y': range(10),
}

unaryConstraints = [
    UnaryConstraint('x', lambda x: x % 2 == 0)
]
binaryConstraints = [
    BinaryConstraint('x', 'y', lambda x, y: x+y == 4)
]


def ac3(X, D, R1, R2):
    def arc_reduce(x, y):
        change = True
        for cx in D[x]:


    for x in X:
        # make domain of x consistent with unary constraints
        D[x] = [d for d in D[x] if all([r(d) for r in R1 if x in r.get_vars()])]

        # Create worklist which contains all arcs we wish to prove consistent or not
        worklist = []
        for constraint in R2:
            if x in constraint.get_vars():
                worklist.append(constraint.get_vars())


        while len(worklist) != 0:
            arc = worklist.pop()
            x = arc[0]
            y = arc[1]
            if arc_reduce(x, y):
                if len(D[x]) == 0:
                    return None
                else:
                    s = []
                    for r in R2:
                        if x in r.get_vars() and y not in r.get_vars():
                            s.append(r)
                    worklist.extend(s)


