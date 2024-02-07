def prime_nth(n):
      primes_list = []
      number = 2
      flag = 0
      while True:
            if len(primes_list) == n:
                  return primes_list[-1]
            for i in range(1,number+1):
                  if number % i == 0:
                        flag += 1
            if flag == 2:
                  primes_list.append(number)
            number += 1
            flag = 0


print("Given a number n, determine what the nth prime is.")
n =  int(input("Enter a number: "))

nthPrime = prime_nth(n)
print(f"The {n}th number prime is {nthPrime}")







