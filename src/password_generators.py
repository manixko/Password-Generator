import random
import string
from abc import ABC, abstractmethod

import nltk


class PasswordGenerator(ABC):
    """
    Base class for generating passwords.
    """
    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate password.
        """
        pass


class PinGenerator(PasswordGenerator):
    """
    Class to generate pin
    """
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self):
        pin = ''.join(random.choice(string.digits) for _ in range(self.length))
        return pin


class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generate random passwords
    """
    def __init__(self, length: int = 8,
                 include_digits: bool = False,
                 include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_digits:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate memorable passwords
    """
    def __init__(self, length: int = 4):
        self.vocabulary = nltk.corpus.words.words()
        self.length = length

    def generate(self):
        password = '-'.join(random.choice(self.vocabulary) for _ in range(self.length))
        return password

def main():
    generated_password = ''
    pass_type = input('choose an option:(Pin/Random/Memorable) ')
    pass_type = pass_type.lower()
    if pass_type == 'pin':
        while True:
            print('-'*20)
            print('| Generating Pin |')
            try:
                length = int(input('Enter Pin length(default : 4): '))
                generated_password = PinGenerator(length=length)
                print(f'Password : {generated_password.generate()}')
                break
            except ValueError:
                print('Invalid length, Try again')
    elif pass_type == 'random':
        while True:
            print('-'*20)
            print('| Generating Random Password |')
            try:
                length = int(input('Enter Pin length(default : 8): '))
                include_digit_input = input('Include Numbers?(Yes/No) ')
                include_symbols_input = input('Include Symbols?(Yes/No) ')
                if include_digit_input.lower() == 'yes':
                    include_digit = True
                elif include_digit_input.lower() == 'no':
                    include_digit = False
                else:
                    print('Invalid Answer, Try again')
                    continue
                if include_symbols_input.lower() == 'yes':
                    include_symbols = True
                elif include_symbols_input.lower() == 'no':
                    include_symbols = False
                else:
                    print('Invalid Answer, Try again')
                    continue
                generated_password = RandomPasswordGenerator(length=length, include_digits=include_digit, include_symbols=include_symbols)
                print(f'Password : {generated_password.generate()}')
                break
            except ValueError:
                print('Invalid length, Try again')
    elif pass_type == 'memorable':
        while True:
            print('-'*20)
            print('| Generating Memorable Password |')
            try:
                length = int(input('Enter Pin length(default : 4): '))
                generated_password = MemorablePasswordGenerator(length=length)
                print(f'Password : {generated_password.generate()}')
                break
            except ValueError:
                print('Invalid length, Try again')
    else:
        print('Invalid input!, Try again')
        main()


if __name__ == "__main__":
    main()
