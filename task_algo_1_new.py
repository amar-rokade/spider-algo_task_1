## ================== TASK 1 A ================================================================
## ==============================================================================================
# 1101 (13) can be expressed as the average of 1011 (11) and 1111 (15).
# Note: It can also be expressed as the average of 0000 and 11010 but the second string has length
# greater than the original string.
# Sample:
# Input:
# 4
# 1101
# Output:
# 1011 1111



#  input from user
legth_of_string = int(input())
# create the function here
def check_legth_of_number(legth_of_string,checking_number):
    if legth_of_string == len(format(checking_number, 'b')):
        return True
    else:
        return False

if legth_of_string <= pow(10,5): #cheking length of string
    #string input
    string = input()
    try:
        number_in_decimal = int(string, 2)
        if len(string) == legth_of_string:
            max_average_possible_number = 2 * number_in_decimal
            #  loop for checking the number for average
            for i in range(number_in_decimal + 1):
                result_of_average = (i + (max_average_possible_number - i)) / 2
                #  cheking condition
                if (result_of_average == number_in_decimal and
                        check_legth_of_number(legth_of_string, i) and
                        check_legth_of_number(legth_of_string, max_average_possible_number - i) and
                        i != number_in_decimal and max_average_possible_number - 1 != number_in_decimal
                ):
                    final = [i, max_average_possible_number - i]
                    # break the loop if  found any result
                    break
            if final:
                first_b = format(final[0], 'b')
                second_b = format(final[1], 'b')
                print('{} {}'.format(first_b, second_b))
    except:
        print('Please give proper binary number input which has only 0 and 1 number')



# ===================TASK 1 B =============================================
#   TASK 1(B) - Find the degree of symmetry of a string
#==========================================================================

# A: the degree of symmetry is 0 as it cannot be divided.
# ABAB : the degree of symmetry is 1. It can be divided only once into AB - AB which can’t be divided
# further into equal strings.
# AAAA: the degree of symmetry is 2.It can be divided into AA - AA, each AA can be further divided
# into A-A which cannot be divided any further.

input_len = int(input())
input_str = input()
#initialize degree of symmetry
a = 0
while input_len % 2 == 0:
    # devide lnput string in half
    first, second = input_str[:len(input_str) // 2], input_str[len(input_str) // 2:]
    if first == second:
        a += 1  #if equal then increased by 1
    else:
        break
    input_str = first
    input_len = len(first)
print(a)


# ===============================================================================
#                                TASK 1 C
# ===============================================================================

#Adit and Advay decide to play a game. The game is described as follows: Advay considers a
#sequence of 6 distinct numbers from the following {10,8,7,16,9,43}, not necessarily in the same
#order. Adit’s job is to guess the exact order of these 6 numbers. Adit can ask Advay some queries of the
#form ---> x y, for which Advay gives the answer of a[x]*a[y].
#Advay is very clever and limits the number of queries that can be asked to four. Formally, Adit can ask
#atmost 4 queries. Adit wants to write a program that gives the exact order of the sequence considering
#the answers he receives from Advay. Formally, the program should give the output for whatever
#answers Advay gives for Adit’s queries(Advay’s answers are always a product of 2 numbers (taken from
#the above sequence)
#).Adit is very busy with his intern. He turns to you for help. Please help him.

# initilize final result
final =  [None] * 6
a = [10, 8, 7, 16, 9, 43]
x = int(input('answer of a[{}] * a[{}]] : '.format(1, 4)))
y = int(input('answer of a[{}] * a[{}]] : '.format(2, 4)))
z = int(input('answer of a[{}] * a[{}]] : '.format(3, 5)))
w = int(input('answer of a[{}] * a[{}]] : '.format(1, 3)))

for i in range(5):
    for j in range(i+1,6):
        if a[i] * a[j] == x :
            x_input = [a[i],a[j]]

        elif a[i] * a[j] == y :
            y_input = [a[i],a[j]]

        elif a[i] * a[j] ==  z:
            z_input = [a[i],a[j]]

        elif a[i] * a[j] == w :
            w_input = [a[i],a[j]]

for p in x_input :
    for q in y_input :
        if p == q :
            final[3] = p #get 4th
            for r in x_input:
                if r != p :
                    final[0] = r #get 1st
            for r in y_input:
                if r !=p :
                    final[1] = r  #get 2nd

for p in z_input :
    for q in w_input :
        if p == q :
            final[2] = p #get 3th
            for r in z_input:
                if r != p :
                    final[4] = r #get 5st 

final[5] = list(set(a) - set(final))[0]  #get last element   
print(final)           
           



# ===============================================================================
#                                TASK 1 D
# ===============================================================================

# Adit is a great coder. However, he has a strange addiction to Chennai Bakery’s Schezwan Chicken
# Noodles(SCN).
# We consider a duration of n days numbered from 1 to n . You are given the following information
# about each day i of the n days:
# 1. Whether a contest takes place on day i or not.
# 2. Whether he eats SCN on day i or not.
# Adit is able to perform well in a contest on a given day only if he eats SCN on the same day. His
# initial rating is r units. For every contest in which he performs well, his rating improves by x units. His
# rating decreases by y units otherwise. You have to determine his rating at the end of the n days.
# Input
# The first line contains a positive integer n, r, x, y – the number of days under consideration, his initial
# rating, the parameter x , and the parameter y respectively .
# The second line contains the sequence of integers c 1 , c 2 , ..., c n separated by space, where:
# · c i equals 1 if a contest takes place on the i- th day; 0 otherwise.
# The third line contains the sequence of integers s 1 , s 2 , ..., s n separated by space, where:
# · s i equals 1 if he eats SCN on the i- th day; 0 otherwise.
# Output
# · Print a single line containing the string “promoted”(without quotes) if his rating is greater than his
# initial rating.
# · Print a single line containing the string “demoted”(without quotes) if his rating is lesser than his
# initial rating.
# · Print “no change” otherwise.

n, r, x, y = input().split()
n,r,x,y = map(int,[n,r,x, y] )
c = input()
s = input()
is_contest = c.split()
is_eat = s.split()
new_rating = r
for i in range(n):
    #contest happen and he eat
    if is_contest[i] == '1' and is_eat[i] == '1' :
        new_rating += x
    
    #contest happen and he not eat
    elif is_contest[i] == '1' and is_eat[i] == '0':
        new_rating -= y

if new_rating < r :
    print('demoted')
elif new_rating > r :
    print('promoted')
else:
    print('no change')