variables = ['a', 'b']
domains = Dict('a' => 0:6, 'b' => 0:9)

unaryConstraints = [
        (key='a', f= (a) -> a % 2 == 0)
]

binaryConstraints = [
                     (key=('a', 'b') f = (a, b) -> a+b == 4)
]

function oneof(tuple, elem)
    return tuple[1] == elem || tuple[2] == elem
end

function ac3(variables, domains, unary, binary)
    for v in variables
        domains[v] = [domain for domain in domains[v] if [c(domain) for c in unary if c.key == v]]

        worklist = map(n -> n.key, filter(b -> oneof(b.key,v), binary))
