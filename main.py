import console_ui

console_ui.draw_header("ГРА")

menu_options = ["Почати", "Налаштування", "Киш звiдси"]
console_ui.draw_menu(menu_options)

choice = input("Оберiть дiю: ")

if choice not in ["1", "2", "3"]:
    console_ui.draw_warning("Оберiть щось зi списку!")
else:
    print(f"Обрано дiю {choice}")