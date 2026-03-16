"""
Задача 3. Контекстный менеджер safe_write
Безопасная запись в файл с откатом изменений при ошибке
"""

class safe_write:
    """
    Контекстный менеджер для безопасной записи в файл
    При возникновении исключения отменяет все изменения
    """
    def __init__(self, filename):
        self.filename = filename
        self.file_content = None
        self.file = None
    
    def __enter__(self):
        # Читаем текущее содержимое файла, если он существует
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.file_content = f.read()
        except FileNotFoundError:
            self.file_content = ""  # Файл не существует
        
        # Открываем файл для записи
        self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Произошло исключение - отменяем изменения
            self.file.close()
            
            # Восстанавливаем исходное содержимое
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(self.file_content)
            
            # Выводим информацию об исключении
            print(f"Во время записи в файл возникло исключение {exc_type.__name__}")
            return True  # Поглощаем исключение
        
        # Нет исключения - сохраняем изменения
        self.file.close()
        return False

def demonstrate_safe_write():
    """
    Демонстрация работы контекстного менеджера safe_write
    """
    print("Задача 3: Контекстный менеджер safe_write")
    print("=" * 50)
    
    filename = "poem.txt"
    
    # Пример 1: Успешная запись
    print("\nПример 1: Успешная запись в файл")
    print("-" * 30)
    
    poem = """Вот моя деревня,
Вот мой дом родной,
Вот качусь я в санках
По горе крутой.
    
Вот свернули санки,
И я на бок - хлоп!
Кубарем качуся
Под гору, в сугроб."""
    
    with safe_write(filename) as file:
        file.write(poem)
    
    print("Запись выполнена успешно!")
    print("Содержимое файла:")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
    
    # Пример 2: Запись с исключением
    print("\nПример 2: Запись с исключением")
    print("-" * 30)
    
    try:
        with safe_write(filename) as file:
            file.write("Эта строка запишется...\n")
            file.write("И эта тоже...\n")
            # Искусственно вызываем исключение
            raise ValueError("Тестовая ошибка записи")
            file.write("А эта строка не должна записаться")
    except:
        pass  # Исключение уже обработано safe_write
    
    print("\nПроверяем содержимое файла после ошибки:")
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
    
    # Пример 3: Запись в несуществующий файл с ошибкой
    print("\nПример 3: Запись в новый файл с ошибкой")
    print("-" * 30)
    
    new_file = "new_poem.txt"
    
    with safe_write(new_file) as file:
        file.write("Это должно было записаться...\n")
        raise RuntimeError("Ошибка времени выполнения")
    
    print("Проверяем, существует ли файл:")
    try:
        with open(new_file, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("Файл не создан - откат изменений сработал правильно!")

if __name__ == "__main__":
    demonstrate_safe_write() 
