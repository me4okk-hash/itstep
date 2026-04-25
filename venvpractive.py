from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import random

console = Console()
history = []

moves = ["Камінь", "Ножиці", "Папір"]


def get_result(player, computer):
    if player == computer:
        return "Нічия"
    elif (
        (player == "Камінь" and computer == "Ножиці") or
        (player == "Ножиці" and computer == "Папір") or
        (player == "Папір" and computer == "Камінь")
    ):
        return "Ви перемогли!"
    else:
        return "Ви програли!"


def show_menu():
    menu_text = "1. Почати гру\n2. Історія ігор\n3. Вихід"
    panel = Panel(menu_text, title="Головне меню")
    console.print(panel)


def play_game():
    player = Prompt.ask(
        "Ваш вибір [Камінь/Ножиці/Папір]",
        choices=moves
    )

    computer = random.choice(moves)
    result = get_result(player, computer)

    console.print(f"Комп'ютер обрав: {computer}", style="cyan")

    if result == "Ви перемогли!":
        console.print(f"Результат: {result}", style="green")
    elif result == "Ви програли!":
        console.print(f"Результат: {result}", style="red")
    else:
        console.print(f"Результат: {result}", style="yellow")

    history.append({
        "player": player,
        "computer": computer,
        "result": result
    })


def show_history():
    if not history:
        console.print("Історії немає", style="yellow")
        return

    table = Table(title="Історія матчів")

    table.add_column("Раунд", style="cyan")
    table.add_column("Гравець", style="white")
    table.add_column("Комп'ютер", style="white")
    table.add_column("Результат")

    for i, match in enumerate(history, 1):
        result = match["result"]

        if result == "Ви перемогли!":
            colored_result = "[green]Ви перемогли![/green]"
        elif result == "Ви програли!":
            colored_result = "[red]Ви програли![/red]"
        else:
            colored_result = "[yellow]Нічия[/yellow]"

        table.add_row(
            str(i),
            match["player"],
            match["computer"],
            colored_result
        )

    console.print(table)


while True:
    show_menu()

    choice = Prompt.ask(
        "Оберіть дію",
        choices=["1", "2", "3"]
    )

    if choice == "1":
        play_game()
    elif choice == "2":
        show_history()
    elif choice == "3":
        break
