n, m = map(int, input().split())
price = [0] * n 
sold = ["UNSOLD"] * n

for _ in range(m):
    name, bid, item = map(str, input().split())
    bid, item = int(bid), int(item) - 1
    if bid > price[item]:
        sold[item] = name
        price[item] = bid

for i in sold:
    print(i)