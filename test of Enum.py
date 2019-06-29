from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Jan)
print(Month.Jan.name)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Sun
print(day1)
print(day1.name)
print(day1.value)
week = Weekday
print(week.Wed)
print(week['Tue'].name)
print(week(1))
print(Weekday(1).name)
print(Weekday)
for name, member in week.__members__.items():
    print(name, '=>', member, member.value)