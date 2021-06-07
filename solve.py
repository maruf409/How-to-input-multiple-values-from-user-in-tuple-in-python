n = int(input())
tou = []
k = list(map(int, input().split()))[:n]
w = tuple(k)
print(hash(w))

