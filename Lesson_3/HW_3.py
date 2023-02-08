# 3. настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы

d = {
    'a': 1, 'b': 3, 'c': 3,'d': 2,'e': 1,
'f': 4,'g': 2,'h': 4,'i': 1,'k': 5,
'l': 1,'m': 3,'n': 1,'o': 1,'p': 3,
'q': 10,'r': 1,'s': 1,'t': 1,'v': 4,
'x': 8,'y': 4,'z': 10
}

def price ():   
    name = str(input())
    sum = 0
    for j in name:
        if j in d.keys():
         sum = sum + d[j]
    print(sum)
  
price()
