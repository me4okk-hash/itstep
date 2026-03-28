try:
    number = float(input("Введiть число: "))
except Exception:
    print("Unknown exception")
except ValueError:
    print("Incorrect value")