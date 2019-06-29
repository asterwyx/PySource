numbers = [1,1,2,2,2,3,6,9,8,8,8,7]
kind = set(numbers)
print(kind)
for number in kind:
    print(number)
    
names = {'Mary':100,'Michael':95,'Cecil':93}
print(names)
names['Adam'] = 99
print(names)

kind.add(10)
print(kind)
kind.remove(8)
print(kind)

kind1 = set([58,4,3,69,1,1,4])
kind2 = kind & kind1
kind3 = kind | kind1
print(kind2)
print(kind3)
