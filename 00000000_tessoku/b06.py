N = int(input())
A = list(map(int, input().split()))

sum = [0]
for i in range(N):
  sum.append(sum[i] + A[i])

Q = int(input())
for i in range(Q):
  l, r = map(int, input().split())
  atr = sum[r] - sum[l - 1]
  hzr = r - l + 1 - atr
  
  if (atr == hzr):
    print("draw")
  elif (atr > hzr):
    print("win")
  else:
    print("lose")