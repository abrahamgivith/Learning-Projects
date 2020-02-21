'''
Write a function that returns a pair of numbers from a inout array, such that the sum of the pair is equal to a given
sum.'
Assume, all numbers are integers, the array is ordered.

input : 1. An array
        2. Sum S

return a pair of numbers

eg. [1,2,3,5,9] , sum = 8
    returns (3,5)
'''

def findPairForSUm(arr, s):
    '''
    # O(NlogN) soln
    # Since the array is ordered, if difference of sum and any of the elements iterating from start becomes negative,
    # then the sum doesn't exist

    for num in arr:
        diff = s-num
        if diff <= 0:
            return 'No'
        elif diff in arr:
            return (num,diff)
        else:
            continue
    return 'NO'
    '''

    '''
    # O(N) Soln
    # Start with a pair of numbers from either end of the array, and if their sum is greater than the sum, 
    # shift the end element to left, or if it is lesser shift the start element to right
    '''
    low = 0
    high = len(arr) -1

    while(low<high):

        individual_sum = arr[low]+arr[high]
        if individual_sum < s:
            low +=1
        elif individual_sum > s:
            high -=1
        elif individual_sum == s:
            return (arr[low],arr[high])
        else:
            pass
    return 'No'


'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
'''
def print_pattern(w,h):

    line = ''
    center = 1
    for i in range(int((w - 3) / 2), 1, -3):
        line += '-' * i
        line += '.|.' * (center * 2 - 1)
        center += 1
        line += '-' * i

        print(line)
        line = ''
    line = ''

    line += '-' * (int(w / 2) - 3)
    line += 'WELCOME'
    line += '-' * (int(w / 2) - 3)
    print(line)
    line = ''
    center -= 1
    for i in range(3, int((w) / 2), 3):
        line += '-' * i
        line += '.|.' * (center * 2 - 1)
        center -= 1

        line += '-' * i
        print(line)
        line = ''

'''
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

'''

def minion_game(s):
    p1_sum = 0
    p2_sum = 0


    for i in range(len(s)):
        if s[i] in 'AEIOU':
            # Score for Kevin
            p1_sum += len(s) - i
        else:
            # Score for Stuart
            p2_sum +=len(s) - i


    if p1_sum > p2_sum:
        print('Kevin {}'.format(p1_sum) )
    elif p1_sum < p2_sum:
        print('Stuart {}'.format(p2_sum) )
    else:
        print('Draw')

if __name__ == '__main__':

    #print(findPairForSUm([-1,1,2,3,4,4,5,9,10],101))
    #print_pattern(21,7)
    minion_game('MALAYALAM')

'''
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of  that contains  or more vowels.
Also, these substrings must lie in between  consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output

ee
Ioo
Oeo
eeeee
'''
import re

def find_two_or_more_vowels(s):
    match = re.finditer(r'([aeiouAEIOU]{2,})', s)
    any_match = False
    for x in match:
        sec_match = re.match('[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]' + s[x.span()[0]:x.span()[
            1]] + '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', s[x.span()[0] - 1:x.span()[1] + 1])
        if sec_match:
            any_match = True
            print(s[x.span()[0]:x.span()[1]])
    if not any_match:
        print(-1)

'''
Task
You are given a string .
Your task is to find the indices of the start and end of string  in .

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Input Format

The first line contains the string .
The second line contains the string .

Sample Input

aaadaa
aa

Sample Output

(0, 1)  
(1, 2)
(4, 5)

'''


def find_all_indices_of_substrings(s,k):
    indices = set()

    # Make a slider of window len(k) through the whole input string
    for i in range(len(s)):
        match = re.search(k, s[i:len(s)])
        if match:
            tup = (match.start() + i, match.end() - 1 + i)
            indices.add(tup)

    if indices:
        for x in sorted(indices):
            print(x)
    else:
        print((-1, -1))
