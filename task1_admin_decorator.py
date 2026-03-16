"""
Задача 1. Права администратора
Декоратор role_required(roles: list) для ограничения доступа
Доступны роли: admin и teacher
"""

# Глобальная переменная с ролью текущего пользователя
current_user_role = None

def role_required(allowed_roles):
    """
    Декоратор, который проверяет, имеет ли пользователь одну из допустимых ролей
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                return f"Доступ запрещен! Требуется одна из ролей: {allowed_roles}, текущая роль: {current_user_role}"
        return wrapper
    return decorator

# Создаем функцию, доступную для admin и teacher
@role_required(['admin', 'teacher'])
def secret_resource():
    """Функция, представляющая защищенный ресурс"""
    return "Секретный ресурс успешно получен!"

def process_list_operations():
    """
    Функция для работы со списком согласно заданию:
    1. Проверка наличия положительных чисел через any()
    2. Своя функция all для проверки, что все элементы - числа
    3. Сортировка списка через sorted()
    """
    print("\n=== Операции со списком ===")
    
    # Ввод списка от пользователя
    user_input = input("Введите элементы списка через пробел: ").split()
    
    # Преобразуем в числа, где это возможно
    processed_list = []
    for item in user_input:
        try:
            processed_list.append(int(item))
        except ValueError:
            try:
                processed_list.append(float(item))
            except ValueError:
                processed_list.append(item)
    
    print(f"Исходный список: {processed_list}")
    
    # 1. Проверка наличия хотя бы одного положительного числа
    has_positive = any(isinstance(x, (int, float)) and x > 0 for x in processed_list)
    print(f"1. Есть ли хотя бы одно положительное число? {has_positive}")
    
    # 2. Своя функция all для проверки, что все элементы - числа
    def my_all_numbers(lst):
        for item in lst:
            if not isinstance(item, (int, float)):
                return False
        return True
    
    all_numbers = my_all_numbers(processed_list)
    print(f"2. Все элементы являются числами? {all_numbers}")
    
    # 3. Сортировка списка (только числовые элементы, если есть смешанные)
    if all_numbers:
        sorted_list = sorted(processed_list)
        print(f"3. Отсортированный список: {sorted_list}")
    else:
        # Если есть нечисловые элементы, сортируем как строки
        string_list = [str(x) for x in processed_list]
        sorted_list = sorted(string_list)
        print(f"3. Отсортированный список (как строки): {sorted_list}")

def main():
    print("Задача 1: Декоратор прав администратора")
    print("Доступные роли: admin, teacher")
    print("-" * 40)
    
    global current_user_role
    
    # Тест 1: Пользователь с ролью admin
    print("\nТест 1: Пользователь с ролью 'admin'")
    current_user_role = 'admin'
    print(secret_resource())
    
    # Тест 2: Пользователь с ролью teacher
    print("\nТест 2: Пользователь с ролью 'teacher'")
    current_user_role = 'teacher'
    print(secret_resource())
    
    # Тест 3: Пользователь с ролью student (доступ запрещен)
    print("\nТест 3: Пользователь с ролью 'student'")
    current_user_role = 'student'
    print(secret_resource())
    
    # Выполнение операций со списком
    process_list_operations()

if __name__ == "__main__":
    main()