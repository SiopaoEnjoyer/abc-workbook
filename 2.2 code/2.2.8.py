n = int(input())
numbers = [int(x) for x in input().split()]
cd = abs(numbers[0] - numbers[1])
potato = True
for i in range(n-1):
    if abs(numbers[i] - numbers[i+1]) != cd:
        print(f"NO")
        potato = False
        break
if potato:
    print(f"YES")
    print(f"initial term: {numbers[0]}")
    if numbers[0] > numbers[1]:
        print(f"common difference: -{cd}")
    else:
        print(f"common difference: {cd}")


