"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку"""
import sys
from sem6_package.module_task7 import *

params = sys.argv[1:]
if params:
    print(check_date(params[0]))
else:
    print(check_date('01.01.1600'))
    print(check_date('01.11.2025'))
    print(check_date('01.13.2024'))


"""Про ферзей, к сожалению, вообще не понял задачи, 
как ферзи друг друга бьют или не бьют"""