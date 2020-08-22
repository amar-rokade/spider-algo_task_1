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


#input  T
T = int(input('Enter the number of expression : '))
# Initialize input array
if 1 <= T  and T <=500 :
    expression_list = []
    for i in range(1,T+1):
        exp = list(input('enter expression number {} : '.format(i)))

        if 1 <= len(exp) and len(exp) <= (5 * pow(10,6)):
            expression_list.append(exp)
        elif len(exp) == 0:
            print("there's no such a prefix.")
        else :
            print("expression not valid because it's length more than 10^6!")
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

