from functools import lru_cache

def sortedSquaredArray(array):
    squares = []
    # Write your code here.
    for number in array:
       squares.append(sqr_number(number))
    squares.sort()
    return squares

@lru_cache(maxsize = 100)
def sqr_number(number):
    return number * number

input = [1, 2, 3, 5, 6, 8, 9,1, 2, 3, 5, 6, 8, 9]

print(sortedSquaredArray(input))

#expected = [1, 4, 9, 25, 36, 64, 81]


