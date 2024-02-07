print("Given a number n, determine what the nth prime is.")
n =  int(input("Enter a number: "))
primes = []
number = 2
flag = 0
while True:
    if len(primes) == n:
        break
    for i in range(1,number+1):
            if number % i == 0:
                flag += 1
        
    if flag == 2:
            primes.append(number)
    number += 1
    flag = 0
            


print(f"The {n}th number prime is {primes[-1]}")


