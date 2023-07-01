A = list(map(int, input().split()))
pre = 0
is_ok = True
for i in range(8):
  if (A[i] < pre):
    is_ok = False
    break
  if (A[i] < 100 or 675 < A[i]):
    is_ok = False
    break
  if (A[i] % 25 != 0):
    is_ok = False
    break
  pre = A[i]

if is_ok:
  print("Yes")
else:
  print("No")