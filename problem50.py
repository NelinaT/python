The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
=======================================================================================================================================
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
============================================================================================================================================================
second way:
	from sympy import *
import time
print "Hello World!\n"


def alg(n):
    primes =[]
    i=2
    while sum(primes)<n:
        if isprime(i):
            primes.append(i)
        i=i+1
    fin_seq=[];l=len(primes);j=l
    while j!= 0:
        i=0
        while i+j<l+1:
            seq = primes[i:i+j]
            if sum(seq)<=n:
                if isprime(sum(seq)):
                    if len(seq)>len(fin_seq):
                        fin_seq = seq
            i=i+1
        j=j-1
    return(sum(fin_seq))
    start = time.time()
print(alg(1000000))
print('In '+ str(time.time()-start)+ ' seconds')

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
