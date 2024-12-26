import re

def input_data():
    text = input("Введите текст: ")
    return text

def frequency_analysis(text):
    text = ''.join(filter(str.isalnum, text))
    frequency = {}
    total_chars = len(text)
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    frequency_percentage = {char: count / total_chars for char, count in frequency.items()}
    return frequency_percentage

def print_result(frequency):
    print("Частотный анализ текста:")
    for char, freq in frequency.items():
        print(f"{char}: {freq:.4f}")
