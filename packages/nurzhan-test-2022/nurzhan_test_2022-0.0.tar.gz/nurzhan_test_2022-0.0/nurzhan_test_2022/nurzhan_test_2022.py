class Nurzhan:

    def __init__(self):
        print()

    def show(self,name): 
        print("Hello",name)


# 1 функция факториал
    def factorial(self,n):
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return print(factorial)

# 2 тубир
    def tubir(self,n):
        tubir = n ** 0.5
        return print(str(n) + " саннын тубири " + str(tubir) +" болады ")

# 3 дареже
    def dareje(self,n,m):
        dareje = n**m
        return print(str(n) + " саннын  " + str(m) +" дарежеси " + str(dareje) + " болады")

# 4 модуль
    def modul(self,n):
        if(n >= 0):
            return n
        else:
            return n * (-1)