#Попросить пользователя ввести слова через пробел. Отсортировать слова по количеству
#символов и вывести на экран результат.
t = (input('Input to text with space :'))
t = t.split()
t.sort(key=len)
print(t)