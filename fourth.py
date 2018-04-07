pins = [9874, 6587, 9632, 5412, 9856, 2541, 7895, 5489, 6589, 5482]

ent = int(input())

flat = 0
for pin in pins:
    flat+=1
    if pin == ent:
        print("Здравствуйте, жилец", flat,"квартиры")
    elif ent  not in pins:
        print("Неправильный пин")
        break
        
