f = lambda x: 3*x+1
print(f(2))

def build_quad_formula(a,b,c):
    return lambda x: a*x**2 + b*x + c

g = build_quad_formula(3, 0, 1)(2)
print(g)

h = build_quad_formula(2, 3, -5)
print(h(0))

i = (lambda x:x**2) (9)
print(i)

j = (lambda y: (lambda x: x**2 + y**2))(2)(3)
print(j)

# How to make dfa with lambda calc:
# take user input and convert each binary number as an element in a list?
# based on certain positions a certain lambda function will trigger?