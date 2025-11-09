import numpy  as np
f=[]
num = 555230
for i in range(1, num + 1):
    if num % i == 0:
        f.append(i)
print(len(f))
print(f)

d=[i for i in range(1, num+1) if num % i == 0]
print(len(d))
print(d)

fnp = np.array(f)
dnp = np.array(d)
print(np.array_equal(fnp, dnp))

def factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def sumFactors(list):
    return np.sum(list)

import matplotlib.pyplot as plt
nvalues = []
snvalues = []
testeq = []
for i in range(1, 751):
    sn = int(sumFactors(factors(i)))
    nvalues.append(i)
    snvalues.append(sn)
    testeq.append(i+ 1)
plt.plot(nvalues, snvalues)
plt.plot(nvalues, testeq)
plt.show()
