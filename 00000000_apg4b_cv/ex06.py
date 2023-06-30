exp = input().split();
if (exp[1] == "+"):
  print(int(exp[0]) + int(exp[2]))
elif (exp[1] == "-"):
  print(int(exp[0]) - int(exp[2]))
elif (exp[1] == "*"):
  print(int(exp[0]) * int(exp[2]))
elif (exp[1] == "/" and int(exp[2]) != 0):
  print(int(exp[0]) // int(exp[2]))
else:
  print("error")