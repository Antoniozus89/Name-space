def test_function():
    def inner_function():
        a = "Я в области видимости функции test_function"
        print(a)

    print(inner_function())
print(test_function())

