N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

other_price = P[0]
price = {}
for i in range(M):
  price[D[i]] = P[i+1]

total = 0
for i in range(N):
  if (C[i] in price):
    total += price[C[i]]
  else:
    total += other_price
print(total)