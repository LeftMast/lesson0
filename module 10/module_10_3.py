import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Создаем объект Lock для блокировки потоков

    def deposit(self):
        for _ in range(100):  # 100 транзакций пополнения
            amount = random.randint(50, 500)  # Случайная сумма пополнения
            with self.lock:  # Используем блокировку для безопасного доступа к балансу
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()  # Разблокируем, если баланс >= 500
            time.sleep(0.001)  # Имитация скорости выполнения пополнения

    def take(self):
        for _ in range(100):  # 100 транзакций снятия
            amount = random.randint(50, 500)  # Случайная сумма снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Используем блокировку для безопасного доступа к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокируем поток, если недостаточно средств
            time.sleep(0.001)  # Имитация скорости выполнения снятия

# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')