def format_time(seconds):
    days, remainder = divmod(seconds, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}"

user_input = int(input("Введіть кількість секунд (від 0 до 8639999): "))

if 0 <= user_input < 8640000:
    print(format_time(user_input))
else:
    print("Число від 0 до 8639999 включно.")
