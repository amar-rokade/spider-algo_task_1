# ================================================================================
#             TASK 3  A
# ================================================================================

import array as arr
input_nu = arr.array('i',map(int, list(input()))) 
def getSum(n): 
    sum = 0
    while (n != 0): 
        sum = sum + int(n % 10) 
        n = n//10
    return sum

def getStep(n):
    step = 1
    while n//10 !=0:
        n = getSum(n)
        step += 1
    return step
    
sum_inp = sum(input_nu)
if sum_inp < 10 and len(input_nu)<2 :
    print(0)
else : 
    step = getStep(sum_inp)
    print(step)


# ================================================================================
#             TASK 3  b
# ================================================================================

# i <= n <= m;
# 1 <= m <= 10^5
# 1 <= A[i] <= 10^9
# Output Format
# A single line containing an integer : the maximum possible strength of the wall.
# Input
# 2
# 4
# 2 3 5 8
# Output
# 8


n = int(input())
m = int(input())
A = arr.array('i',map(int,list(input().split())))
A = sorted(A)
if 0 < n and n <= m :
    while len(A) != n :
        A[1] = A[1] + A[0]
        del A[0]
        print(A)
        A = sorted(A)  
print(min(A))
   

# ================================================================================
#             TASK 3  b
# ================================================================================
from math import gcd 

def coprime(a, b):
    return gcd(a, b) == 1

a = int(input())
list_n = []
for i in range(2,a+1):
    list_n.append(i)

coprime_n = []
for i in range(0,a-2):
    b = list_n[i]
    c = [b]
    for j in range(i+1,a-1):
        if coprime(b, list_n[j]):
            c.append(list_n[j])
    coprime_n.append(c)

dic_n = {}
for i in range(len(coprime_n)):
    c = []
    a = coprime_n[i]
    for j in range(0,i):
        b = coprime_n[j]
        if a[0]  in b:
            c.append(b[0])
    k = 0
    for  k in range(1,10**5):
        if k not in c :
            dic_n[coprime_n[i][0]] = k
            coprime_n[i][0] = k
            break

print(sum(set(dic_n.values())))   

        
