n = 10000


# create sieve of eratosthenes
prime_n = n**2+n+41 + 1
primes = [True for _ in range(prime_n+1)]

for p in range(2, int(prime_n**0.5)+1):
	if primes[p]:
		for i in range(p*p, prime_n, p):
			primes[i] = False


# check conjecture
for x in range(n):
	val = x**2 + x + 41
	if not primes[val]:
		print('{} -> {} -> '.format(x, val), end='')
		print('NOT PRIME')
		break
