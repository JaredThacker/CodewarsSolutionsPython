def positive_sum(arr):
    sum = 0
    for numbers in arr:
        if numbers > 0:
            sum = sum + numbers
    return sum  