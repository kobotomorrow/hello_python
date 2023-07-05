N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

sum = [0]
for i in range(N):
  sum.append(sum[i] + A[i])

for i in range(Q):
  l, r = list(map(int, input().split()))
  print(sum[r] - sum[l - 1])