names = {'Mary':100,'Michael':95,'Cecil':93}
for name in names:
    print(names[name])
names['Adam'] = 99
print(names['Adam'])
print('Thomas' in names)
a = names.get('Thomas')
print(a)
names.pop('Mary')
for name in names:
    print(names[name])