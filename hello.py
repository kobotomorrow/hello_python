print("--- 出力 ---")
print(1)
print(0.1)
print("おはよう")
print('こんにちは')

a = "こんばんは"
b = "さようなら"
print(a, b)
print(a, b, sep="")
print(a, b, sep="|")

print("Hello", end="")
print("World")

print("")
print("---文字列展開---")
name = "Alice"
age = 12
print(f'{name}は{age}歳です')

x = 1.123456789
print(f'{x:.2f}')
print(f'{x:.10f}')

# 入力の受取り
# s = input()
# n = int(input())
# f = float(input())
# print(s, n, f)

# 入力の受取り(スペース区切り)
# a = list(input().split())
# b = list(map(int, input().split()))
# c = list(map(float, input().split()))
# print(a)
# print(b)
# print(c)

# 入力の受取り(行区切り)
# a = [input() for i in range(3)]
# b = [int(input()) for i in range(3)]
# C = [float(input()) for i in range(3)]
# print(a)
# print(b)
# print(C)

# 入力の受取り(スペース区切り + 行区切り)
# a = [list(input().split()) for i in range(3)]
# b = [list(map(int, input().split())) for i in range(3)]
# c = [list(map(float, input().split())) for i in range(3)]
# print(a)
# print(b)
# print(c)

print("")
print("--- 算術演算子 ---")
print(1 + 1)
print(1 - 1)
print(2 * 3)
print(5 / 2)
print(5 // 2)
print(5 % 2)

a = "Hello"
b = "Python"
c = a + b
print(c)

print("")
print("比較演算子")
n = 80
print(60 < n < 100)
print("a" < "b")
print("a" < "A")

print("")
print("--- 論理演算子 ---")
print(True and False)
print(True or False)
print(not True)

print("")
print("--- 条件分岐 ---")
a = 1
if a % 2 == 0:
  print("偶数です")
else:
  print("奇数です")
x = 75
if x > 80:
  print("優")
elif x > 70:
  print("良")
else :
  print("可")
  
print("")
print("--- 繰り返し ---")
for i in range(5):
  print(i)
  
s = "Python"
for c in s:
  print(c)
  
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
  print(fruit)
  
i = 0;
while i < 3:
  print(i)
  i += 1
  
print("")
print("--- 文字列 ---")
print(ord("A"))
print(chr(65))

print("1".zfill(3))
print("abc".upper())
print("ABC".lower())

s = "0123456789"
print(s[2:])
print(s[2:5])
print(s[:5])
print(s[::-1])

d = "abbccc"
print(d.count("a"))
print(d.count("b"))
print(d.count("c"))

e = "abcabc"
print(e.replace("a", "A"))

s = "abcde"
t = "bcd"
if t in s:
  print("tはsの部分文字列です")
else:
  print("tはsの部分文字列ではありません")
  
print("")
print("--- リスト ---")
a = ["one", "two", "three"]
print(len(a))
print(a[0])
print(a[-1])
a.append("four")
print(len(a))
print(a)

b = [0] * 3
print(b)

c = [1, 7, 5, 6, 2]
print(max(c))
print(min(c))
print(sorted(c))
print(sum(c))
c.sort()
print(c)

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(d.index(5))

a = [[] for _ in range(5)]
print(a)
a[0].append(1)
a[0].append(2)
a[3].append(3)
print(a)

print("")
print("--- 集合 ---")

print(set("aaa"))
print(set("aab"))
print(set("abc"))

a = set("abb")
print(len(a))

b = set()
b.add("A")
b.add("B")
b.add("A")
print(b)

b.remove("B")
print(b)

print("")
print("--- 連想配列 ---")
a = {"one":1, "two":2, "three":3}
print(a["two"])

for key,value in a.items():
  print(key, value)

b = {}
b["one"] = 1
b["five"] = 5
print(b)

d = dict()
for i in range(5):
  if i not in d:
    d[i] = 1
  else:
    d[i] += 1

for i in d.values():
  print(i)

print("")
print("--- 関数 ---")
def add(a, b):
  return a + b

print(add(1, 2))
