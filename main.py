# # Завдання № 1
# from datetime import datetime

# date = input('Введіть дату у форматі "РРРР-ММ-ДД": ' )

# def get_days_from_today(date):
#     '''
#     Ця функція розраховує різницю між заданою і поточною датами
#     '''

#     try: 
#         given_date = datetime.strptime(date, '%Y-%m-%d').date()
#         current_date = datetime.today().date()
#         difference_days = given_date - current_date
#         return difference_days.days

#     except ValueError:
#         print ('Неправильний фомат дати!',)
      

# print(f"{get_days_from_today(date)} days")




# Завдання № 2
import random

def get_numbers_ticket(min_num, max_num, quantity):
    '''
    Функція дозволяє згенерувате потрібне число унікальних чисел для лотереї
    '''
    if min_num > 0 and max_num <= 1000 and quantity <= (max_num - min_num):
        unic_numbers = []
        while len(unic_numbers) < quantity:
            unic_number = random.randrange(min_num, max_num+1)
            if unic_number not in unic_numbers:
                unic_numbers.append(unic_number)   
    else:
        unic_numbers = []

    return sorted(unic_numbers)

print(get_numbers_ticket(10, 20, 9))