import time
import multiprocessing
def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Убираем пробелы и добавляем строку в список
    # Для демонстрации, можно вывести количество строк из файла
    print(f"Read {len(all_data)} lines from {name}")
if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Замените на реальные названия файлов
    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)  # Вызываем функцию для каждого файла
    linear_time = time.time() - start_time
    print(f"Linear execution time: {linear_time:.6f} seconds")
    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)  # Вызываем функцию для каждого файла параллельно
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing execution time: {multiprocessing_time:.6f} seconds")

