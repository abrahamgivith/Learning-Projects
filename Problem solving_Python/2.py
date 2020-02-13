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

if __name__ == '__main__':

    print(findPairForSUm([-1,1,2,3,4,4,5,9,10],101))
