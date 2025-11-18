
x = 10
y = 5
z = 9
f = lambda x: lambda y: lambda z: x + y + z
res = f(x)(y)(z)
print(res)
    
    
def multiply_with_memory(num): # Closure
    # num == 10
    def multiply(other_num):
        # other_num == 20
        return num * other_num
    return multiply

first = multiply_with_memory(10)
res = first(20)
print(res)

# ------------------------------
from pytest import fixture, mark

# Closure
def validation(num):
    def validate(other_num):
        return num > other_num
    return validate

def test_validation_closure():
    closure = validation(18)
    assert closure(16) == True
    assert closure(20) == False
    
def sumar(n1,n2):
    return n1+n2
    
# Callback
def calculator(n1, n2, operation):
    return operation(n1,n2)

res = calculator(10, 20, lambda n1,n2: n1*n2)
print(res)

# Decorator = Callback + Closure