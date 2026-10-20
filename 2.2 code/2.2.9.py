n = int(input())
numbers = [int(x) for x in input().split()]
sorted_numbers = sorted(numbers)
invert_numbers = sorted(numbers)[::-1]
if numbers != sorted_numbers and numbers != invert_numbers:
    print("not sorted")
elif numbers[0] < numbers[-1]:
    print("nondecreasing")
elif numbers[0] > numbers[-1]:
    print("nonincreasing")
elif numbers[0] == numbers[-1]:
    print("constant")