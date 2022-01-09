import random
import string
import os
import pyprind

# Name: Ruben Sanduleac
# Date: January 8th, 2022
# Description: Simple CMD Line Applicationxw


def main(initial_word, gen_word_count, res_file_name):
    if os.path.exists(res_file_name):
        print("Remove the existing file....")
        os.removal(res_file_name)

    n = 1000
    for i in range(n):
        result = ''.join((random.sample(initial_word, gen_word_count)))
        file = open(res_file_name, "a")
        file.write(result + "\n")
        file.close


if __name__ == "__main__":
    main("ruben", 3, "res.txt")
