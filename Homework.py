print("Введите текст:")
text = str(input())
print(text.upper())
#print(text)
without_a = text.replace('А', '').replace('а', '').replace('A', '').replace('a', '')
print(without_a)
text_whithout_last = text[:-1]
print(text_whithout_last)