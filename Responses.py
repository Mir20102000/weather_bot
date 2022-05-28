from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("привет", "здравствуйте", "прив", "привет?"):
        return "Привет, как дела?"

    if user_message in ("хорошо", "хорошо, а у тебя?", "отлично", "отлично, а у тебя?", "норм", "норм, а у тебя?", "нормально",
                        "нормально, а у тебя?"):
        return "Я так рад за тебя! У меня также!"

    if user_message in ("hello", "hi", "hello?"):
        return "Hello, how are you?"

    if user_message in ("good, what about you?", "good, thanks", "good, thank you", "bad", "awesome, what about you?"):
        return "I'm glad! I'm same!"

    if user_message in ("who are you?", "who are you"):
        return "I am a bot that created Mirziyod. What about you?"

    if user_message in ("Кто ты?", "Кто ты"):
        return "Я бот, который создал Мирзиёд. А ты кто?"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%M:%S")
        return str(date_time)

    if user_message in ("время", "время?", "сколько время?", "сколько время"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%M:%S")
        return str(date_time)

    return "Ты написал то, что я не понимаю. Попробуй что-то простое."
