import random
import itertools

letter_choices = list(map(chr, range(ord('a'), ord('f')+1)))


class Guesser():

    def __init__(self):
        self.guess_list = []

    def add_to_list(self, guess):
        self.guess_list.append(str(guess))
        return self.guess_list


class Maker():

    def __init__(self): pass

    def generate_secret(self):
        secret_list = []
        for x in itertools.repeat(None, 4):
            secret_list.append(''.join(random.choice(letter_choices)))
        return secret_list

    def compare(self, guess, secret):
        single_response_list = []
        for x, y in zip(guess, secret):
            if x == y:
                single_response_list.append('x')
            elif x in secret:
                single_response_list.append('o')
            else:
                single_response_list.append('_')

        return single_response_list


class Board():

    def __init__(self): pass

    def print_board(self, response_list, guess_list):
        for x in range(0, 14):
            if len(response_list) > x:
                print("{" + response_list[x] + "}" "[" + guess_list[x] + "]" + str(x+1))
            else:
                print("{    }[   ]" + str(x+1))


def game_engine():
    guesser = Guesser()
    maker = Maker()
    board = Board()
    response_list = []
    guess = ""

    print("'x' means correct letter in correct position, 'o' means correct letter in incorrect position"
          "\nGuess four letters from a through f")
    board.print_board(response_list, guesser.guess_list)
    secret = ''.join(maker.generate_secret())

    while guess != secret:
        guess = input("Enter four letters now\n:")
        guesser.add_to_list(guess)
        response = (maker.compare(guess, secret))
        response_str = ''.join(response)
        response_list.append(response_str)
        board.print_board(response_list, guesser.guess_list)
        if len(response_list) > 13:
            break

    if guess == secret:
        print("you win!")
    else:
        print("you lose!")

game_engine()
