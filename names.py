names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'Токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for i in range(len(names)):
    names[i] = names[i].split(' ')
    names[i][-1] = names[i][-1].capitalize()
    print(f'Привет, {names[i][-1]}!')
    names[i] = ' '.join(names[i])
print(names)
