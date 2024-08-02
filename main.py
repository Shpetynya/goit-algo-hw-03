# Завдання № 1
from datetime import datetime

date = input('Введіть дату у форматі "РРРР-ММ-ДД": ' )

def get_days_from_today(date):
    '''
    Ця функція розраховує різницю між заданою і поточною датами
    '''
    try:   
        given_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        difference_days = given_date - current_date
        return difference_days.days
    except ValueError:
        print ('Неправильний фомат дати!',)

print(f"{get_days_from_today(date)} days")




# Завдання № 2
import random

def get_numbers_ticket(min_num, max_num, quantity):
    '''
    Функція дозволяє згенерувате потрібне число унікальних чисел для лотереї
    '''
    if min_num > 0 and max_num <= 1000 and quantity >= min_num and quantity <= max_num:
        unic_numbers = []
        while len(unic_numbers) < quantity:
            unic_number = random.randint(min_num, max_num)
            if unic_number not in unic_numbers:
                unic_numbers.append(unic_number)
        return unic_numbers
    else:
        print('Числа мають бути позитивними та число випадкових чисел має бути у заданому діапазоні')
print(get_numbers_ticket(1, 49, 20))