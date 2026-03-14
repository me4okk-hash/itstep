# Задание 1

# def nsd(a, b):
#     if b == 0:
#         return a
#     return nsd(b, a % b)

# Задание 2

# def digits_sum(i):
#     if i < 10:
#         return i
#     else:
#         return i % 10 + digits_sum(i // 10)
    
# enter_number = int(input("Введiть число: "))
# print(f"Сума чисел {digits_sum(enter_number)}")

# Задание 3

def is_symmetric(lst):
    if len(lst) <= 1:
        return "список симетричний"
    if lst[0] != lst[-1]:
        return "список не симетричний"
    return is_symmetric(lst[1:-1])

enter_nums = input("Введiть числа через пробiл: ")
numbers = list(map(int, enter_nums.split()))
print(is_symmetric(numbers))