import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("أهلاً بك في لعبة تخمين الرقم!")
    print("لقد اخترت رقماً سرياً بين 1 و 100. حاول تخمينه!")

    while True:
        guess = int(input("أدخل تخمينك: "))
        attempts += 1

        if guess < secret_number:
            print("رقمك صغير جداً. جرب رقماً أكبر.")
        elif guess > secret_number:
            print("رقمك كبير جداً. جرب رقماً أصغر.")
        else:
            print(f"مبروك! لقد فزت بعد {attempts} محاولات.")
            break

play_game()
