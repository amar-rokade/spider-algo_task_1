
# ==========================================================
#           TASK 2 A : Longest Proper Prefix
# ==========================================================

# Constraints
# 1 ≤ T ≤ 500
# 1 ≤ The length of a single expression ≤ 106
# The total size all the input expressions is no more than 5*106

# SAMPLE
# Input:
# 3
# <<>>
# <>>>
# ><><>
# Output:
# 4
# 2
# 0


# #input  T
T = int(input('Enter the number of expression : '))
# Initialize input array
if 1 <= T  and T <=500 :
    expression_list = []
    for i in range(1,T+1):
        exp = list(input('enter expression number {} : '.format(i)))

        if 1 <= len(exp) and len(exp) <= pow(10,6):
            expression_list.append(exp)
        elif len(exp) == 0:
            print("there's no such a prefix.")
        else :
            print("expression not valid because it's length more than  10^6!")
    for expression in expression_list :
        a = 0
        if expression[0] != ">":
            for i in range(len(expression)-1):
                if expression[i] == "<" :
                    for j in range(i+1,len(expression)):
                        if expression[j] == '>':
                                a += 2
                                expression[j] = 0
                                break
        print(a)                     
else :
    print("Please enter number between 1 and 500..")



# ==========================================================
#           TASK 2 B : Max Element in Array (BASIC MODE)
# ==========================================================
import array as arr
initial = []
n = int(input('Enter number of element in array: '))

if 1 <= n and n <= pow(10,5): 
    for i in range(n):
        initial.append(i+1)

    q = int(input('Enter number of queries to be performed: ')) 
    if 1<= q and q <= 100 :
        query_list = []

        for i in range(1,q+1):
            query = arr.array('i',map(int,input('enter expression number {} : '.format(i)).split()))
            query_list.append(query)
        for query in query_list:
            for j in range(query[0]-1,query[1]):
                initial[j] = initial[j] + query[2]
        print(max(initial))
    else :
        print('Please Enter number of queries between 1 and 100. try again! ')
else : 
    print('please  enter number of element less than 10^5!')
