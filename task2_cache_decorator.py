"""
Задача 2. Кэширование
Декоратор cache с параметрами db и expiration
"""

class CacheDecorator:
    """
    Класс для кэширования результатов функции
    """
    def __init__(self, db):
        self.db = db
        self.cache = {}  # {thing: (result, remaining_uses)}
    
    def __call__(self, expiration):
        def decorator(func):
            def wrapper(thing):
                # Проверяем, есть ли thing в кэше
                if thing in self.cache:
                    result, remaining = self.cache[thing]
                    if remaining > 0:
                        self.cache[thing] = (result, remaining - 1)
                        return f"Info about: {thing} cached in {self.db}, expire={remaining - 1}"
                    else:
                        # Кэш истек, получаем новые данные
                        result = func(thing)
                        self.cache[thing] = (result, expiration - 1)
                        return f"Info about: {thing} from {self.db}, now cached with expire={expiration}"
                else:
                    # Первый запрос
                    result = func(thing)
                    self.cache[thing] = (result, expiration - 1)
                    return f"Info about: {thing} from {self.db}, now cached with expire={expiration}"
            return wrapper
        return decorator

# Создаем экземпляры декораторов для разных БД
cache_postgres = CacheDecorator('postgresql')
cache_sqlite = CacheDecorator('sqlite')

# Функция получения информации
def get_info(thing):
    """
    Функция, имитирующая получение информации из БД
    """
    # В реальном приложении здесь был бы запрос к БД
    return f"Информация о {thing}"

def demonstrate_caching():
    """
    Демонстрация работы кэширования согласно примеру
    """
    print("Задача 2: Декоратор кэширования")
    print("=" * 50)
    
    # Создаем декорированные функции с разными настройками
    @cache_postgres(5)  # 5 использований из кэша
    def get_info_postgres(thing):
        return get_info(thing)
    
    @cache_sqlite(3)  # 3 использования из кэша
    def get_info_sqlite(thing):
        return get_info(thing)
    
    # Демонстрация для bike_store
    print("\nДемонстрация для 'bike_store':")
    print("-" * 30)
    
    thing = "bike_store"
    
    # Postgres с expiration=5
    print("PostgreSQL:")
    for i in range(7):  # Вызовем больше раз, чтобы увидеть обновление кэша
        result = get_info_postgres(thing)
        print(result)
    
    print("\nSQLite:")
    # SQLite с expiration=3
    for i in range(6):
        result = get_info_sqlite(thing)
        print(result)
    
    # Демонстрация для users
    print("\n" + "=" * 50)
    print("Демонстрация для 'users':")
    print("-" * 30)
    
    thing = "users"
    
    # Postgres с expiration=5
    print("PostgreSQL:")
    for i in range(7):
        result = get_info_postgres(thing)
        print(result)
    
    print("\nSQLite:")
    # SQLite с expiration=3
    for i in range(6):
        result = get_info_sqlite(thing)
        print(result)

if __name__ == "__main__":
    demonstrate_caching()
