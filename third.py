import sys

s = input()

try:
    int(s)
except:
    print("this number is uncorrect")
    sys.exit()

s = int(s)
if s%4== 0 and s%100 != 0:
    print("Yes")
elif s%4==0 and s%400==0 and s%100==0:
    print("Yes")
else:
    print("No")
