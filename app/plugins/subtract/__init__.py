from app.commands import Command
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class MultiplyCommand(Command):

    def execute(self):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        print(number_1 - number_2)