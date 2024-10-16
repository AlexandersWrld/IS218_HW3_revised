from app.commands import Command
import sys
sys.path.append('../../IS218_HW3_revised')
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class DivideCommand(Command):

    def execute(self):
        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))
        number_3 = Calculator.divide(number_1, number_2)
        try:
            print(number_3)
        except ZeroDivisionError:
            print("Error: Division by zero.")