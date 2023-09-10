import sys
import os
import random


def main() -> None:
    print('Welcome to the word guessing game!')
    while True:
        option = input('Enter S to start the game, Q to quit \n').lower()

        if option == 's':
            start_the_game()
        elif option == 'q':
            quit_the_game()
        else:
            clean_screen()
            print('Invalid character entered. Try again')


def start_the_game() -> None:
    word = generate_the_word()
    used_letters = set()
    attempts_count = 10
    while attempts_count != 0:
        if check_the_victory(word, used_letters):
            print(f'Congratulations, you guessed the word! {word}')
            return
        clean_screen()
        letter = get_the_letter(attempts_count, word, used_letters)
        used_letters.add(letter)
        if letter in word:
            print(f'The letter {letter.upper()} is actually in the word!')
        else:
            print(f'Unfortunately, the letter {letter.upper()} is not in the word')
            attempts_count -= 1
    print(f'You lose! The word was: {word.upper()}')


def print_attempts_count(attempts_count: int) -> None:
    print(f'{attempts_count} attempts left')


def print_opened_letters_in_word(word: str, used_letters: set) -> None:
    print('Opened letters:', end=' ')
    for letter in word:
        if letter in used_letters:
            print(letter.upper(), end=' ')
        else:
            print('_', end=' ')
    print()


def print_opened_letters_at_all(word: str, used_letters: set) -> None:
    also_opened = set()
    for letter in used_letters:
        if letter not in word:
            also_opened.add(letter)
    if also_opened:
        print('Also opened: ')
        for letter in also_opened:
            print(letter, end=' ')
        print()


def get_the_letter(attempts_count: int, word: str, used_letters: set) -> str:
    print_all_information(attempts_count, word, used_letters)
    while True:
        letter = input('Enter the letter you want to see\n').lower()
        if not letter.isalpha() or len(letter) != 1:
            clean_screen()
            print_all_information(attempts_count, word, used_letters)
            print('You should enter only Latin letters')
        elif letter in used_letters:
            clean_screen()
            print_all_information(attempts_count, word, used_letters)
            print(f'Letter {letter.upper()} is already visible')
        else:
            return letter


def print_all_information(attempts_count: int, word: str, used_letters: set) -> None:
    print_attempts_count(attempts_count)
    print_opened_letters_in_word(word, used_letters)
    print_opened_letters_at_all(word, used_letters)


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_the_word() -> str:
    with open('words.txt') as file:
        words = [i.strip() for i in file]
    word = random.sample(words, 1)[0]
    return word


def quit_the_game():
    sys.exit(0)


def check_the_victory(word: str, used_letters: set) -> bool:
    victory = True
    for letter in word:
        victory *= (letter in used_letters)
    return victory


if __name__ == '__main__':
    main()
