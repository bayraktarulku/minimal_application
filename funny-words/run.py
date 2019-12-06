import argparse
import random
from words_list import select_word_list

# taken from http://marshmallow_666.tripod.com/cgi-bin/

def build_n_gram(lang='', words=1, join_with=' '):
    word_list = select_word_list(lang)
    return join_with.join(random.sample(word_list, words))


def run():
    parser = argparse.ArgumentParser()
    print(parser)
    parser.add_argument('-l', '--language',
        help='Selects the language in which words are returned',
        type=str, default=1)
    parser.add_argument('-w', '--words',
        help='how many funny words to generate per line',
        type=int, default=2)
    parser.add_argument('-n', '--number',
        help='how many lines of funny words to generate',
        type=int, default=1)
    parser.add_argument('-d', '--delimiter',
        help='what to put between the funny words',
        type=str, default=' ')
    args = parser.parse_args()
    print(args.language)

    for n in range(args.number):
        print(build_n_gram(args.language, args.words, args.delimiter))

if __name__ == '__main__':
    run()
