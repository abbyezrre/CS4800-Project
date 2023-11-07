from fakeB import *
from login import *
from user import *


def main():
    test = User()
    test.findUser("johnsmith209")
    
    if test is not None:
        print(test.get_lastname())

if __name__ == "__main__":
    main()