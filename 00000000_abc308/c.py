N = int(input())
AB = []
for i in range(N):
  a, b = map(int, input().split())
  AB.append((a*10**20//(a+b),-(i + 1)))
AB.sort(reverse=True)
for ab in AB:
  print(-ab[1])