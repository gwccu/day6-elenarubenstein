# File name: warmupDay6.py
myNum = 7
guess = int(input("Guess the magic number "))

while guess != myNum:
    guess = int(input("Guess again "))
print("You guessed correctly.")

n = 2
m = 8
print(n**m)
ans = n**m
while n != ans:
    n*=n
print(n)
x = 10
while x >= 0:
    print (x)
    x -= 1