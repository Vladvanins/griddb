list = ('в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов')
newlist = []
number = 0
string = ''
for i in list:
    if i.isdigit():
        if int(i) // 10 < 1:
            newlist.append('"' + '0' + i + '"')
        else:
            newlist.append('"' + i + '"')
    elif i[1:].isdigit() and (i[0] == '+' or i[0] == '-'):
        newlist.append('"' + i[0] + '0' + i[1:] + '"')
    else:
        newlist.append(i)

for i in newlist:
    string += i + ' '

print(string)
