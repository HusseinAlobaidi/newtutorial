import datetime
from random import randint


def main():
    dob = input('Enter you Date of Birth : ')
    CurrentYear = datetime.datetime.now().year
    MyAge = CurrentYear - int(dob)
    print("Your age is {} year".format(MyAge))


main()
