def plusplus (s):
    nums = mystr.split(" ")
    summa = 0
    for num in nums:
        summa += int(num)
    return summa


mystr = input()

print(plusplus(mystr))
    
