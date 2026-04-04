def draw_header(title):
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def draw_menu(options_list):
    print("Дiї: ")
    width = 40
    
    for i, option in enumerate(options_list, start=1):
        print(f"[  {i}  ] {option}")

    print("=" * width)


def draw_warning(message):
    border = "!" * (len(message) + 4)
    print(border)
    print(f"! {message} !")
    print(border)
