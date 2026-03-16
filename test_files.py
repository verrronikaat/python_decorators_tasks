"""
Тестовый файл для демонстрации всех трех задач
Запускает каждую задачу последовательно
"""

import task1_admin_decorator
import task2_cache_decorator
import task3_safe_write

def run_all_tasks():
    """
    Запускает все три задачи последовательно
    """
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ ВСЕХ ТРЕХ ЗАДАЧ")
    print("=" * 60)
    
    # Задача 1
    print("\n" + "=" * 60)
    task1_admin_decorator.main()
    
    input("\nНажмите Enter для продолжения...")
    
    # Задача 2
    print("\n" + "=" * 60)
    task2_cache_decorator.demonstrate_caching()
    
    input("\nНажмите Enter для продолжения...")
    
    # Задача 3
    print("\n" + "=" * 60)
    task3_safe_write.demonstrate_safe_write()
    


if __name__ == "__main__":
    run_all_tasks() 
