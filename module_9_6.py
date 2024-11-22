def all_variants(text):
    """
    Генератор возвращает подпоследовательности строки `text` в порядке:
    - Сначала одиночные символы
    - Затем пары
    - Затем тройки и т.д.
    """
    n = len(text)
    # Перебираем длины подпоследовательностей от 1 до n
    for length in range(1, n + 1):
        # Генерируем подпоследовательности указанной длины
        for start in range(n - length + 1):
            yield text[start:start + length]

# Демонстрация работы функции-генератора
if __name__ == "__main__":
    print("Генерация подпоследовательностей строки 'abc':")
    a = all_variants("abc")
    for i in a:
        print(i)

    print("\nГенерация подпоследовательностей строки 'hello':")
    b = all_variants("hello")
    for i in b:
        print(i)