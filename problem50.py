def Is_Prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def list_of_primes(n):
    primeList=[]
    for i in range(2, n + 1):
        if Is_Prime(i):
            primeList.append(i)
    return primeList

limit = 1000000

primes = list_of_primes(limit)

sum = 0
count = 0

lastCount = 0
lastSum = 0



for i, p in enumerate(primes):
	lastPrimeIndex = 0
	for c in range(i, len(primes)):
		sum += primes[c]
		if sum < limit:
			if Is_Prime(sum):
				lastPrimeIndex = c
		else:
			break

	sum = 0

	# print("======== {} ========".format(i))
	for c in range(i, lastPrimeIndex + 1):
		sum += primes[c]
		# print(primes[c])

	# print(sum)		
	count = lastPrimeIndex + 1 - i

	if lastCount < count:
		lastCount = count
		lastSum = sum

	count = 0
	sum = 0

print("count: {}\nsum: {}".format(lastCount, lastSum))