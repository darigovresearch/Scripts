# run_all.py is code to run all scripts one after the other in this repository

import os


def main():

    try:
        os.system("python download_flashcards.py")
        os.system("python clone_education.py")
        os.system("python update_education.py")
    except Exception as e:
        os.system("python3 download_flashcards.py")
        os.system("python3 clone_education.py")
        os.system("python3 update_education.py")


if __name__ == '__main__':
    main()
