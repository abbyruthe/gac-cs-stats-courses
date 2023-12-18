# list of integers -> int
def maximum (numbers):
#"""input a list of numbers and have that function return the largest value in
#that list"""
    value = numbers[0]
    for i in numbers:
        if i > value:
            value = i
    return value

# list of integers -> int
def minimum (numbers):
    """input a list of numbers and have that function return the smallest value
    in that list"""
    value = numbers[0]
    for i in numbers:
        if i < value:
            value = i
    return value

# list of integers -> int
def average(numbers):
    """input a list of numbers, have the function average add up all of the
numbers and divide by the number of values in the list"""
    length = len(numbers)
    returnint = 0
    for i in numbers:
        returnint += i
    average = returnint / length
    return average

# list of intergers -> int
def standardDeviation(numbers):
    """input a list of numbers, and compute the standard deviation of those
    values"""
    a = average(numbers)
    length = len(numbers)
    returnint = 0
    for i in numbers:
        returnint += (i-a)**2
    denominator = length - 1
    standardDeviation = math.sqrt(returnint / denominator)
    return standardDeviation


# list of integers, int -> int
def count_value(numbers, value):
    """input a list and a value, and the function returns the number of times
    the given value occurs in the list"""
    numberOfTimes = 0
    for i in numbers:
        if(i == value):
            numberOfTimes += 1
    return numberOfTimes

# list of int => int
def mode(numbers):
     """Finds and returns the most frequent value in the list."""
     max_count = count_value(numbers, numbers[0])
     mode = numbers[0]
     for i in range (0, len(numbers)):
          count = count_value(numbers, numbers[i])
          if max_count < count:
               max_count = count
               mode = numbers[i]
     return mode

