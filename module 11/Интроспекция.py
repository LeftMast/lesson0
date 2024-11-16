import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Получаем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', '__main__')

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }

    return info


# Пример создания пользовательского класса
class SampleClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value


# Пример использования функции
number_info = introspection_info(42)
print("Информация о числе 42:")
print(number_info)

# Создаем экземпляр пользовательского класса
sample_instance = SampleClass(10)

# Получаем информацию о экземпляре класса
class_info = introspection_info(sample_instance)
print("\nИнформация о экземпляре SampleClass:")
print(class_info)
