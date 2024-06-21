from itertools import islice, zip_longest

tutors = ["Иван", "Анастасия", "Петр", "Сергей", "Дмитрий", "Борис", "Елена", "Кирилл"]
klasses = ['9А', '7B', '9Б', '9В', '8Б', '10А']

rezult = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(rezult))
print(*islice(rezult, 9))
