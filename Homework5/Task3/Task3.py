# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E

import os
os.system('cls') # при компиляции на Linux или MaxOS необходимо 'cls' за менить на 'clear'

def rle_encode(rawstring):
    encoded = '' 
    prev_char = '' 
    count = 1

    if not rawstring: 
        return '' 
    for char in rawstring: 
        if char != prev_char: 
            if prev_char: 
                encoded += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        encoded += str(count) + prev_char 
    return encoded

def rle_decode(encodedstring):
    decode = ''
    count = ''
    for char in encodedstring:
        # если символ - цифра
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

def main():
    print('Изначальная строка данных:')
    rawtext = str(input())
    print(rawtext)
    print()

    print('Сжатая строка данных:')
    compressed_text = rle_encode(rawtext) 
    print(compressed_text)
    print()

    print('Распакованная строка:')
    decompressed_text = rle_decode(compressed_text)
    print(decompressed_text)

if __name__ == '__main__':
    main()