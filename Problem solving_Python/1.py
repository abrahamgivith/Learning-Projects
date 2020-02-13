"""
This function counts the number of ascending numbers in a string

"""
def fun(input_str):
    count = 0       # Counts the ascending digits
    c_prev = 0      # This variable keeps track of the previous character
    biggest_value = []  # This array keeps track of all the counts of ascending numbers
    for c in input_str:
        print(c,c_prev,count)
        if c.isdigit():
            if int(c)> c_prev:
                count +=1
                biggest_value.append(count)
            else:
                count = 0
            c_prev = int(c)
    print(max(biggest_value))


"""
This function finds all the numbers divisible by 7 but not a multiple of 5 between 2000 and 3200
"""

def divisible_seven():
    return [x  for x in range(2000,3201) if x % 7 == 0 and  x % 5 != 0]

"""
This function returns the factorial of the given input number
"""


def factorial(input_number):
    fact = 1
    if int(input_number) == 0:
        return fact
    else:
        for x in range(1,int(input_number)+1):
            fact *= x
        return fact


"""
function to generate a dictionary that contains (i, i*i) such that is an integral number between 
1 and n (both included). and then the function should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def print_dictionary(number):
    return {x:x*x for x in range(1,int(number)+1)}


"""
function which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied :
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""

def list_and_tuple(input_string):
    list_output = input_string.split(sep = ',') # split the input string with comma delimiter
    tuple_output = tuple(list_output) # convert the list into a tuple
    return list_output, tuple_output


"""
Defining a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
"""

class String_op:
    def __init__(self):
        pass

    def getString(self):
        return input('Enter a String: ')

    def printString(self,input_string):
        print(input_string.upper())

"""
Function that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

from math import sqrt

def calcQ(input_D):
    D = input_D.split(sep = ',')
    C = 50
    H = 30
    Q = []
    for element in D:
        print(float(element))
        Q.append(str(int(sqrt(round( (2* C * float(element))/H)))))
    return ','.join(Q)


"""
function which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and
 j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""

def gen_matrix(numbers):
    ij_value = numbers.split(',') # separate the comma separated string into a list of numbers
    return [[(i*j) for i in range(0,int(ij_value[1]))]  for j in range(0,int(ij_value[0]))]

"""
function that accepts a comma separated sequence of words as input and prints the words in
 a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

def sort_words(inputString):
    listofwords = inputString.split(sep = ',')
    listofwords.sort()
    return ','.join(listofwords)

"""
program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

def printcapLines():
    lines = []
    while True:
        s = input('Enter a line:')
        if s:
            lines.append(s.upper())
        else:
            break

    for x in lines:
        print(x)


"""
 function that accepts a sequence of whitespace separated words as input and 
 prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

def sortalphanum(inputstring):
    sequence = inputstring.split(sep =' ')
    sequence = sorted(list(set(sequence)))
    return ' '.join(sequence)



"""
function which accepts a sequence of comma separated 4 digit binary numbers as its input 
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

def binaryDivision(inputdata):
    binary_sequence = inputdata.split(',')
    divisible = []
    [divisible.append(number) for number in binary_sequence if int(number,2)%5 ==0]
    return ','.join(divisible)

"""
Function which will find all such numbers between 1000 and 3000 (both included) such that 
each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
import copy
from math import pow

def findevendigits(*args):
    #Check if any arguments are given for the first and last value
    if args:
        first = args[0]
        last = args[1]
    # If not, take the default value
    else:
        first = 1000
        last = 3000
    # Initialize an list to hold the even digits
    evendigits =[]
    # Iterate from the first digit to last digit in the given limit
    for number in range(first,last+1):
        # Copy the number to a temporary location since we are modifying the original number
        temp_number = copy.copy(number)
        # Calculate the divisor value to be the power of 10 with length of digits in the number
        divisor = pow(10,(len(str(number))-1))
        # Initialize a list to hold all the digits in the number
        digits =[]
        while divisor>=1:
            # get the first digit of the number to be appended to digits[]
            digits.append(int(number/divisor))
            # After extracting the first digit modify the number to be the remaining value
            number %= divisor
            # Modify the divisor to reduce one place value
            divisor /=10
        # Check if all the elements in digit[] aka the number are even.
        if all(elem % 2 == 0 for elem in digits):
            # Append the copy of the number which we saved previously to the evendigits[]
            evendigits.append(str(temp_number))
    return ','.join(evendigits)

"""
Function that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

def countletterdigit(inputstring):
    letter =0
    digit = 0
    for char in inputstring:
        if char.isalpha():
            letter +=1
        elif char.isdigit():
            digit+=1
        else:
            pass
    return letter,digit


"""
Function that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""


def calcdigitsum(num):
    sum = int(num)
    multiple = int(num)
    count = 0
    while count<3:
        multiple = int(num) + (multiple * 10)
        sum += multiple
        count +=1
    return sum


"""
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81
"""


def square_odd(inputList):
    # Split the inputList into individual elements and then squared if they are found odd
    oddVals = [(int(x)*int(x)) for x in inputList.split(',') if int(x)%2 != 0]
    return ','.join([str(x) for x in oddVals])


"""
function that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""


def bank_balance(input_data):
    net_balance = 0
    account = input_data.split(' ')
    for index,element in enumerate(account):
        if element == 'D':
            net_balance += int(account[index+1])
        elif element == 'W':
            net_balance -= int(account[index+1])
        else:
            pass
    return net_balance


"""
A website requires the users to input username and password to register. 
function to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
function should accept a sequence of comma separated passwords and will check
 them according to the above criteria. Passwords that match the criteria are to be printed, 
 each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

def check_password(input_data):
    list_pw = input_data.split(sep = ',')
    accepted_pw = []
    for password in list_pw:
        if True in [letter.isalpha() for letter in password]:
            if True in [letter.isdigit() for letter in password]:
                if True in [letter.isupper() for letter in password]:
                    if '$' in password or '#' in password  or '@' in password:
                        if len(password)>= 6 and len(password) <= 12:
                            if ' ' not in password:
                                accepted_pw.append(password)
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    return ','.join(accepted_pw)


"""
program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""

def sort_name_age_height(input_data):
    print(input_data)




if __name__ == '__main__':
    #fun('acs231nh2456781dff45667')
    #test1 = divisible_seven()
    #test2 = factorial(input('Enter the number:'))
    #test3 = print_dictionary(8)
    #test4 = list_and_tuple(input('Enter the comma separated numbers'))

    """
    # test method for String_op class
    string_obj = String_op()
    test_str = string_obj.getString()
    string_obj.printString(test_str)
    """
    #test5 = calcQ(input('Enter comma separated values for D: '))
    #test6 = gen_matrix(input('Enter the two values comma separated: '))
    #test7 = sort_words(input('Enter the words comma separated:'))
    #printcapLines()
    #test8 = sortalphanum(input('Enter the string:'))
    #test9 = binaryDivision(input('Enter the string of 4 digit binary values:'))
    #test10 = findevendigits(10,3000)

    #test11 = countletterdigit(input('Enter the sentence:'))
    #print('LETTER:%d \nDIGIT:%d' %(test11[0],test11[1])
    #test12 = calcdigitsum(input('enter the number(0-9):'))
    #test13 = square_odd(input('Enter the list of numbers:'))
    #test14 = bank_balance(input('Enter data:'))
    #test15 = check_password(input('Enter password list:'))
    while True:
        s = input('Enter data( name, age, height):')
        if not s:
            break
        else:

    print(test15)

