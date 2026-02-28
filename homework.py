# Задание 1

# translate = {"hello": "Привiт", "how are you?": "Як справи?", "goodbye": "До побачення", "thank you": "Дякую", "please": "Будь ласка", "yes": "Так", "no": "Нi", "good morning": "Доброго ранку", "good night": "На добраніч", "i love you": "Я тебе люблю", "sorry": "Вибачте", "excuse me": "Перепрошую", "what is your name?": "Як вас звати?", "my name is...": "Мене звати...", "how are you?": "Як справи?", "i am fine, thank you.": "У мене все добре, дякую.", "see you later": "До зустрічі", "goodbye": "До побачення", "have a nice day": "Гарного дня", "i don't understand": "Я не розумію", "can you help me?": "Ви можете мне помочь?", "where is the bathroom?": "Где находится туалет?", "how much does it cost?": "Сколько это стоит?", "i am hungry": "Я голоден", "i am thirsty": "Я хочу пить", "i am tired": "Я устал", "i am happy": "Я счастлив", "i am sad": "Мне грустно", "i am angry": "Я злюсь", "i am bored": "Мне скучно", "i am excited": "Я взволнован", "i am scared": "Мне страшно", "i am confused": "Я запутался", "i am surprised": "Я удивлен", "i am proud": "Я горжусь", "i am sorry": "Мне жаль"}
# word = input("Введiть слово для перекладу: ").lower().strip()

# if word in translate:
#      print(f"Переклад: {translate[word]}")
# else:    
#     print("Слово не знайдено в словнику.")

# Задание 2

friends_dict = {}
friends_input =  input("Введiть кiлькiсть друзiв та iгри в якi вони, ігри що є укожного з них та у самого користувача: ")
 
for friend in friends_input.split(","):
    name, games = friend.split(":")
    friends_dict[name.strip()] = set(games.strip().split())
user_games_input = input("Введiть iгри, в якi ви граєте: ")
user_games = set(user_games_input.strip().split())
common_games = set()
for games in friends_dict.values():
    common_games.update(games.intersection(user_games))
print("Спільні ігри з друзями:")
for game in common_games:
    print(game)



