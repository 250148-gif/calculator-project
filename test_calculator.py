from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 0) == "خطأ: القسمة على صفر غير ممكنة"


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("جميع الاختبارات نجحت ✅")