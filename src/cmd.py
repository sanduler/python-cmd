import random
import string
import os
import pyprind
import sys
import getopt

# Name: Ruben Sanduleac
# Date: January 8th, 2022
# Description: Simple CMD Line Application

# cp -r <file-awal> >file-copy>
#


def main(argv):
    result_file_name = ''
    initial_word = ''
    gen_count = 0
    gen_result = 0

    try:
        opts, args = getopt.getopt(
            argv, "hw:c:r:o:", ["word=", "count=", "result=", "output="])
    except getopt.GetoptError:
        pass

    if os.path.exists(res_file_name):
        print("Remove the existing file....")
        os.removal(res_file_name)

    n = 100000
    for i in pyprind.prog_bar(range(n)):
        result = ''.join((random.sample(initial_word, gen_word_count)))
        file = open(res_file_name, "a")
        file.write(result + "\n")
        file.close


if __name__ == "__main__":
    main("ruben", 3, "result.txt")
