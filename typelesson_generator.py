import argparse
from random import randint, shuffle

parser = argparse.ArgumentParser(description='Typewriting lesson generator.')
parser.add_argument('letters', help='no other letters, than this')
parser.add_argument('-e', '--emphasis_letters', help='letters in every word')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
parser.add_argument('-m', '--mode', choices=['letters', 'words'], default='words',
                    help='generation mode, default: words')
parser.add_argument('-d', '--dictionary', help='filename for a dictionary file', default='/usr/share/dict/ngerman')
parser.add_argument('--max_chars', help='target char length', type=int, default=600)
parser.add_argument('--max_line_chars', help='target line char length', type=int, default=55)
parser.add_argument('--min_word_len', help='minimum word length', type=int, default=3)
parser.add_argument('--max_word_len', help='maximum word length', type=int, default=6)

args = parser.parse_args()

#print(args)

letters = list(args.letters)
if args.emphasis_letters:
    emphasis_letters = list(args.emphasis_letters)
    for ch in emphasis_letters:
        if ch not in letters:
            print('Parameter error: emphasis letters are not all in allowed letters!')
            exit(1)
else:
    emphasis_letters = []

line_char_count = 0
char_count = 0


def get_words():
    global args
    global letters
    global emphasis_letters

    words_local = []

    for line in open(args.dictionary):

        stripped_line = line.strip()

        if len(stripped_line) < args.min_word_len:
            continue

        if len(stripped_line) > args.max_word_len:
            continue

        is_emphasis = False
        if len(emphasis_letters) == 0:
            is_emphasis = True

        is_ok = True

        for ch in stripped_line:
            if ch not in letters:
                is_ok = False
                break
            if not is_emphasis and ch in emphasis_letters:
                is_emphasis = True

        if not is_ok or not is_emphasis:
            continue

        words_local.append(stripped_line)

    shuffle(words_local)
    return words_local


def handle_word_gap():
    global line_char_count
    global char_count

    if line_char_count > args.max_line_chars:
        line_char_count = 0
        print('')
    elif line_char_count > 0:
        line_char_count += 1
        char_count += 1
        print(' ', end='')


def handle_end_of_line():
    if char_count > args.max_chars:
        print('')
        return True
    return False


def add_word(word_local):
    global line_char_count
    global char_count

    length = len(word_local)

    print(word_local, end='')

    line_char_count += length
    char_count += length

print('')

if args.mode == 'words':
    words = get_words()
    print('Number of possible words for random selection:', len(words), '\n')

while True:
    if args.mode == 'letters':
        for word_length in range(args.min_word_len,
                                 (args.min_word_len + randint(0, args.max_word_len - args.min_word_len + 1))):
            word = ''
            for idx in range(word_length):
                letter_index = randint(0, len(letters) - 1)
                word += letters[letter_index]

            handle_word_gap()
            add_word(word)

        if handle_end_of_line():
            break

    elif args.mode == 'words':
        handle_word_gap()
        idx = randint(0, len(words) - 1)
        word = words[idx]
        add_word(word)

        if handle_end_of_line():
            break

print('')