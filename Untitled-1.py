# print("HELLO WORLD")


# name=input("Введите имя: ")
# age = int(input("Введите возраст: "))
# print(f"Ваше имя {name}")

# if name == 'Max':
#     print(f"Привет {name}")
# elif name == 'Andrei':
#     print (f"Пока {name}")

# for i in range(age): 
#     print(i)

# i=0
# while i <= 10:
#     print(i)
#     i+=1


res = 0.0
numOper = int(input("Введите кол-во операций: "))
a = float(input("Веедите первое число: "))
b = float(input("Введите второе число: "))

oper = (input("Введите знак операции: "))
if oper == '+':
        res = a + b  
elif oper == '-':
        res = a - b
elif oper == '*':
        res = a * b
elif oper == '/':
    if b == 0:
        print("Ноль нельзя")
    elif b != 0:
        res = a/b
elif oper == '^':
        res = a**b
f=1
while f<numOper: 
        b = float(input("Введите второе число: "))
        oper = (input("Введите знак операции: "))
        if oper == '+':
            res = res + b
            f+=1
        elif oper == '-':
            res = res - b
            f+=1
        elif oper == '*':
            res = res * b
            f+=1
        elif oper == '/':
            if b == 0:
                  print("Ноль нельзя")
            elif b != 0:
                res = res/b
                f+=1
        elif oper == '^':
            res = res**b
            f+=1
print(f"Ваш результат: {res}")        

    
   






