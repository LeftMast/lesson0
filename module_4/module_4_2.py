def test_function():
    def inner_function():
        print("Я в области видимости функции test_fuction")
        inner_function()


test_function()
inner_function()  #Вызывает ошибку, так как функция вне области видимости ( не в global и не в bulit)