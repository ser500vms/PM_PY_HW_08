# """*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква 
# имеет определенную ценность. В случае с английским алфавитом очки 
# распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; 
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12"""
  
# en = {1: 'AEIOULNSTR',
#       2: 'DG',
#       3: 'BCMP',
#       4: 'FHVWY',
#       5: 'K',
#       8: 'JZ',
#       10: 'QZ'}
# ru = {1: 'АВЕИНОРСТ',
#       2: 'ДКЛМПУ',
#       3: 'БГЁЬЯ',
#       4: 'ЙЫ',
#       5: 'ЖЗХЦЧ',
#       8: 'ШЭЮ',
#       10: 'ФЩЪ'}


# lang = abs(int(input('Вводим 1 для английских букв, 2 для русских ')))
# word = input('Введите слово: ').upper()
# # if lang == 1:
# #     print('Ценность этого слова', sum([k for i in word for k, v in en.items() if i in v]), 'очков')
# # elif lang == 2:
# #     print('Ценность этого слова', sum([k for i in word for k, v in ru.items() if i in v]), 'очков')

# info_one = [k for i in word for k, v in ru.items() if i in v]


# info = []
# for i in word:
#     for k, v in ru.items():
#         if i in v:
#             info.append(k)
# print(info_one)
# print(info)



data = [1, 2, 4, 7, 8, 10]
# is_even = []
# for number in data:
#     if number % 2 == 0:
#         is_even.append(number)


is_even = [number for number in data if number % 2 == 0]

print(is_even)