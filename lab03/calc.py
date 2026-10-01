a = float(input("Введите число "))
c = input("Введите знак ")
b = float(input("Введите число "))

def summa(a,b):
    return a+b
def rasn(a,b):
    return a-b

if c=="+":
    summa(a,b)
elif c=="-":
    rasn(a,b)
