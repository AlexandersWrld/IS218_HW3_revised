from app.commands import Command
import sys
sys.path.append('../../IS218_HW3_revised')
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class DivideCommand(Command):

    def execute(self):
        try:
            number_1 = int(input('Enter your first number: '))
            number_2 = int(input('Enter your second number: '))
            print(number_1 / number_2)
        except ZeroDivisionError:
            print("Error: Division by zero.")
            
