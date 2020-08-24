
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
T = int(input())
# Initialize input array
if 1 <= T  and T <=500 :                                             # we check constraints first
    expression_list = []
    for i in range(1,T+1):
        exp = list(input())  # converte input in list
        if 1 <= len(exp) and len(exp) <= pow(10,6):                   # check constraints second 
            expression_list.append(exp)
    for expression in expression_list :
        a = 0
        if expression[0] == "<":                                    # checking first element of expression 
            for i in range(len(expression)-1):                      
                if expression[i] == "<" :                           
                    for j in range(i+1,len(expression)):
                        if expression[j] == '>':
                                a += 2                              # if we found pair then we incresed by 2
                                expression[j] = 0                   # we element pair for not take in part for new cheking
                                break                               # if we found e[J] ==  we break inner loop and checking new 
        print(a)                     

# ==========================================================
#           TASK 2 B : Max Element in Array (BASIC MODE)
# ==========================================================
import array as arr
import sys                                      # we import required module
initial = []
n = int(input())

if 1 <= n and n <= pow(10,5):                                # constrainats
    for i in range(n):
        initial.append(i+1)                                  # here we asign value as indices

    q = int(input()) 
    if 1<= q and q <= 100 :                                 # constrains checking
        query_list = []

        for i in range(1,q+1):
            try :                                           # we make sure  query correct or not 
                query = arr.array('L',map(int,input().split()))
            except:
                sys.exit(0)

            if 1 <= query[0] and query[1]<= n and 1 <= query[2] and query[2] <= pow(10,9): 
                query_list.append(query)
            else :
                sys.exit(0)
        for query in query_list:
            for j in range(query[0]-1,query[1]):
                initial[j] = initial[j] + query[2]       # add 
        print(max(initial))                              # we print the max element in array


# ==========================================================
#           TASK 2 B : Max Element in Array (HACKER MODE(1))
# ==========================================================
initial = []
n = int(input())

if 1 <= n and n <= pow(10,5): 
    for i in range(n):
        initial.append(i+1)

    q = int(input())
    if 1<= q and q <= pow(10,5) :
        query_list = []
        for i in range(1,q+1):
            try :
                query = arr.array('L',map(int,input().split()))
            except:
                sys.exit(0)
            
            if 1 <= query[0] and query[1]<= n and 1 <= query[2] and query[2] <= pow(10,9):
                query_list.append(query)
            else :
                sys.exit(0)
        list_update = {}                                   #here we initialize dic for get updated element
        for query in query_list:  
            for j in range(query[0]-1,query[1]):
                if j  in  list_update.keys() :             # cheking is indices alredy in dic or of 
                    d = list_update.update({j : list_update.get(j)+query[2]})    # indices present then we add this value by query[2]
                else :
                    list_update.update({j:j+query[2]+1})       # we add new key and value to dic
        
        for q in list_update.keys():
            initial[q] = list_update.get(q)                 # here we update value which required to update
        print(max(initial))                                 # print max element in array



