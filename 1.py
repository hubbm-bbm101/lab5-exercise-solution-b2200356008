def sumOfOddNums(n):
    sum = 0
    for x in range(1, n + 1):
        if x % 2 != 0:
            sum += x
    return sum

def avgOfEvenNums(n):
    sum = 0
    count = 0
    for x in range(1, n + 1):
        if x % 2 == 0:
            count += 1
            sum += x
    avg = sum / count
    return avg

n = int(input("Please enter a number: "))
print("The sum of odd numbers:", sumOfOddNums(n))
print("The average of even numbers:", avgOfEvenNums(n))
