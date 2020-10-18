import math
import random

alphab="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyz"
P = math.pow(10, -4)
V = 100  # паролей в день
T = 12   # дней


S = (V * T) / P
A = len(alphab)
L = 0

print("S=",S)
while math.pow(A, L) <= S:
    L += 1


password = ""
for _ in range(L):
    password += alphab[random.randint(0, A-1)]
print(f"Ваш пароль:\n{password}")
print(f"Пароль будет взломан через {A**L*P/V}")

input("Нажмите enter, чтобы закрыть консоль.")

