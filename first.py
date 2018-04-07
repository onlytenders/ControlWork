num = input("Enter the number: ")
try:
    int(num)
except:
    print("this number is uncorrect")

if  num[0] == '-':
    print("Число отрицательное")
    if len(num) == 3:
        print("Число двузначное")
    elif len(num) == 4:
        print("Число трехзначное")
    elif len(num) > 4:
        print("Число многозначное")
    else:
        print("Число однозначное")
else:
    print("Число положительное")
    if len(num) > 3:
        print("Число многозначное")
    elif len(num) == 3:
        print("Число трехзначное")
    elif len(num) == 2:
        print("Число двузначное")
    else:
        print("Число однозначное")
