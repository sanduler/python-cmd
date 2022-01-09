import random
import string
import os
import sys
import getopt
import pyprind
# Name: Ruben Sanduleac
# Date: January 8th, 2022
# Description: Simple CMD Line Application

# cp -r <file-awal> >file-copy>


def main(argv):
    result_file_name = ''
    initial_word = ''
    gen_count = 0
    gen_result = 0

    try:
        opts, args = getopt.getopt(
            argv, "hw:c:r:o:", ["word=", "count=", "result=", "output="])
    except getopt.GetoptError:
        print("python cmd.py -w <initial word> -c <generate count> -r <generate result> -o <result file name>")

    for opt, arg in opts:
        if opt == "-h":
            print(
                "python cmd.py -w <initial word> -c <generate count> -r <generate result> -o <result file name>")
            sys.exit(2)
        elif opt in ("-w", "--word"):
            initial_word = arg
        elif opt in ("-c", "--generatecount"):
            gen_count = arg
        elif opt in ("-r", "--generateresult"):
            gen_result = arg
        elif opt in ("-o", "--outputfile"):
            result_file_name = arg

    if os.path.exists(result_file_name):
        print("Remove the existing file....")
        os.removal(result_file_name)

    for i in pyprind.prog_bar(range(int(gen_result))):
        # progress for generating a word
        result = ''.join((random.sample(initial_word, int(gen_count))))
        file = open(result_file_name, "a")
        file.write(result + "\n")
        file.close
        i += 1


if __name__ == "__main__":
    main(sys.argv[1:])
