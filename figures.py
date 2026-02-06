choice = input("Виберiть фигуру (а-к): ")
space = 7

if choice == 'а':
    for i in range(space):
        for j in range(space):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'б':
    for i in range(space):
        for j in range(space):
            if j <= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'в':
    for i in range(space):
        for j in range(space):
            if i <= space // 2 and j >= i and j <= space - 1 - i:
                 print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'г':
    for i in range(space):
        for j in range(space):
            if i >= space // 2 and j >= space - 1 - i and j <= i:
                 print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'д' or choice == 'е':
    for i in range(space):
        for j in range(space):
            if (j >= i and j <= space - 1 - i) or (j <= i and j >= space - 1 - i):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'ж':
    for i in range(space):
        for j in range(space):
            if j <= i and j <= space - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'з':
    for i in range(space):
        for j in range(space):
            if j >= i and j >= space - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'и':
    for i in range(space):
        for j in range(space):
            if j <= space - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif choice == 'к':
  for i in range(space):
        for j in range(space):
            if j >= space - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

else:
    print("Виберiть фiгуру вiд а до к")

