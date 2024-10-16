from app.commands import Command
import sys
sys.path.append('../../IS218_HW3_revised')
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class SubtractCommand(Command):

    def execute(self):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        print(number_1 - number_2)