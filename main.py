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

text = None
frequency = None
while True:
    print("Меню:")
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы программы")
    choice = input("Выберите пункт меню: ")
    if choice == '1':
        text = input_data()
    elif choice == '2':
        if text is not None:
            frequency = frequency_analysis(text)
        else:
            print("Сначала введите данные.")
    elif choice == '3':
        if frequency is not None:
            print_result(frequency)
        else:
            print("Сначала выполните алгоритм.")
    elif choice == '4':
        print("Завершение работы программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
