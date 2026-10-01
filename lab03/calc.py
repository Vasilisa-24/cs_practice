a = float(input("Введите число "))
c = input("Введите знак ")
b = float(input("Введите число "))

def summa(a,b):
    return a+b
def rasn(a,b):
    return a-b
def proisv(a,b):
    return a*b

if c=="+":
    print(summa(a,b))
elif c=="-":
    print(rasn(a,b))
elif c == "*":
    print(proisv(a,b))
