#Фибоначчи через рекурсию: Напишите рекурсивную функцию для вычисления числа Фибоначчи с индексом n. Напоминаю, что последовательность Фибоначчи определяется как: F(0) = 0, F(1) = 1 и F(n) = F(n-1) + F(n-2) для n > 1.

def Fib(n):
    if(n==0 or n==1):
        return n;   
    return Fib(n-1) + Fib(n-2)

res = Fib(6)
print(res)

