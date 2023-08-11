import random


def main():
    #maxymalna liczba prob
    max_number_of_tries = 7
    #
    number_of_tries = max_number_of_tries - 1

    random_word = choose_word()
    random_word_chars = list(random_word)
    floors_list = get_floors_list(random_word_chars)

    player_won = False
    player_lost = False

    while not player_won and not player_lost:
        letter = get_letter()
        is_letter_correct = check_if_letter_correct(letter, random_word_chars)

        if is_letter_correct:
            print('Twoja litera jest poprawna')
            floors_list = fill_guess(letter, random_word_chars, floors_list)
        else:
            print('Twoja litera jest niepoprawna')
            number_of_tries -= 1

        player_lost = check_if_lost(number_of_tries)
        player_won = check_if_won(floors_list)

        print_rest(number_of_tries, max_number_of_tries, floors_list)

    if player_won:
        print('Gratulacje, wygrales!')
    else:
        print(f'Przegrales... :(\n Slowo ktorego szukales to: {random_word}')


def print_rest(number_of_tries: int, max_number_of_tries: int, floors_list: list[str]):
    print(' '.join(floors_list))
    print_hangman_picture(max_number_of_tries - number_of_tries)


def check_if_won(floors_list: list[str]) -> bool:
    try:
        floors_list.index('_')
        return False
    except ValueError:
        return True


def check_if_lost(number_of_tries: int) -> bool:
    return number_of_tries <= 0


def fill_guess(letter: str, random_word_chars: list[str], floors_list: list[str])-> list[str]:
    some_letter_still_left = True
    old_letter_index = 0

    while some_letter_still_left:
        try:
            letter_index = random_word_chars.index(letter, old_letter_index)
            floors_list[letter_index] = letter
            old_letter_index = letter_index + 1
        except ValueError:
            some_letter_still_left = False

    return floors_list


def get_floors_list(random_word_chars: list[str]) -> list[str]:
    floors_list = []
    random_word_chars_length = len(random_word_chars)

    for _ in range(0, random_word_chars_length):
        floors_list.append('_')

    return floors_list


def print_hangman_picture(stage: int):
    with open(f'./hangman{stage}.txt', 'r') as hangmanFile:
        for line in hangmanFile.readlines():
            print(line.rstrip())


def check_if_letter_correct(letter: str, rsndom_word_chars: list[str]) -> bool:
    try:
        rsndom_word_chars.index(letter)
        return True
    except ValueError:
        return False


def get_letter() -> str:
    letter = ''
    is_input_incorrect = True

    while is_input_incorrect:
        letter = input('Podaj literke: ')

        if len(letter) != 1:
            print('Podaj JEDEN znak!')
        elif letter == ' ':
            print('Podaj znak, nie spacje!')
        else:
            is_input_incorrect = False

    return letter.lower()


def choose_word() -> str | None:
    with open('./words.txt', 'r') as file:
        all_words = file.readlines()
        lenght_of_all_words = len(all_words)
        random_word_index = random.randint(0, lenght_of_all_words - 1)
        random_word = all_words[random_word_index]
        return random_word.strip()

if __name__ == "__main__":
    main()

