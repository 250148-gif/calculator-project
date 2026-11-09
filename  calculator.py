def add(a, b):
    """جمع عددين"""
    return a + b


def subtract(a, b):
    """طرح عددين"""
    return a - b


def multiply(a, b):
    """ضرب عددين"""
    return a * b


def divide(a, b):
    """قسمة عددين"""
    if b == 0:
        return "خطأ: القسمة على صفر غير ممكنة"
    return a / b


def main():
    print("=== الآلة الحاسبة ===")
    print("1. جمع")
    print("2. طرح")
    print("3. ضرب")
    print("4. قسمة")
    print("5. خروج")

    while True:
        choice = input("\nاختر عملية (1-5): ")

        if choice == "5":
            print("شكرًا لاستخدامك الآلة الحاسبة!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("اختيار غير صحيح، حاول مرة أخرى.")
            continue

        num1 = float(input("أدخل العدد الأول: "))
        num2 = float(input("أدخل العدد الثاني: "))

        if choice == "1":
            print(f"النتيجة: {add(num1, num2)}")
        elif choice == "2":
            print(f"النتيجة: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"النتيجة: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"النتيجة: {divide(num1, num2)}")


if __name__ == "__main__":
    main()