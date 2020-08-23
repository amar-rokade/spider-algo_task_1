
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
if 1 <= T  and T <=500 :                                             # we check constraints first
    expression_list = []
    for i in range(1,T+1):
        exp = list(input('enter expression number {} : '.format(i)))  # converte input in list

        if 1 <= len(exp) and len(exp) <= pow(10,6):                   # check constraints second 
            expression_list.append(exp)
        elif len(exp) == 0:
            print("there's no such a prefix.")
        else :
            print("expression not valid because it's length more than  10^6!")
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
else :
    print("Please enter number between 1 and 500..")



# ==========================================================
#           TASK 2 B : Max Element in Array (BASIC MODE)
# ==========================================================
import array as arr
import sys                                      # we import required module
initial = []
n = int(input('Enter number of element in array: '))

if 1 <= n and n <= pow(10,5):                                # constrainats
    for i in range(n):
        initial.append(i+1)                                  # here we asign value as indices

    q = int(input('Enter number of queries to be performed: ')) 
    if 1<= q and q <= 100 :                                 # constrains checking
        query_list = []

        for i in range(1,q+1):
            try :                                           # we make sure  query correct or not 
                query = arr.array('L',map(int,input('enter expression number {} : '.format(i)).split()))
            except:
                sys.exit('Please make sure you add correct last element queries! try again')

            if 1 <= query[0] and query[1]<= n and 1 <= query[2] and query[2] <= pow(10,9): 
                query_list.append(query)
            else :
                sys.exit('Please make sure you add correct queries! try again')
        for query in query_list:
            for j in range(query[0]-1,query[1]):
                initial[j] = initial[j] + query[2]       # add 
        print(max(initial))                              # we print the max element in array
    else :
        print('Please Enter number of queries between 1 and 100. try again! ')
else : 
    print('please  enter number of element less than 10^5!')



# ==========================================================
#           TASK 2 B : Max Element in Array (HACKER MODE(1))
# ==========================================================
initial = []
n = int(input('Enter number of element in array: '))

if 1 <= n and n <= pow(10,5): 
    for i in range(n):
        initial.append(i+1)

    q = int(input('Enter number of queries to be performed: '))
    if 1<= q and q <= pow(10,5) :
        query_list = []
        for i in range(1,q+1):
            try :
                query = arr.array('L',map(int,input('enter expression number {} : '.format(i)).split()))
            except:
                sys.exit('Please make sure you add correct last element of query! try again')
            
            if 1 <= query[0] and query[1]<= n and 1 <= query[2] and query[2] <= pow(10,9):
                query_list.append(query)
            else :
                sys.exit('Please make sure you add correct queries! try again')
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
    else :
        print('Please Enter number of queries between 1 and 10^5. try again! ')
else : 
    print('please  enter number of element less than 10^5!')


