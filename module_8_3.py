class Car:

    def __init__(self, model: str, VIN: int, numbers: str):
        self.model = model
        if self.__is_valid_vin(VIN):
            self.__vin = VIN
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not type(vin_number) == int:
            raise IncorrectVinNumber(message='ОШИБКА: Некорректный тип VIN, должен быть int!')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(message='ОШИБКА: Неверный диапазон для VIN номера!')
        return True

    def __is_valid_numbers(self, numbers):
        if not type(numbers) == str:
            raise IncorrectCarNumbers(message='ОШИБКА: Некорректный тип номера, должен быть str!')
        if not len(numbers) == 6:
            raise IncorrectCarNumbers(message='ОШИБКА: Неверная длина номера, должна быть 6!')
        return True
class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message

def main():
    try:
      first = Car('Model1', 7777777, 'A777MP')
    except IncorrectVinNumber as exc:
      print(exc.message)
    except IncorrectCarNumbers as exc:
      print(exc.message)
    else:
      print(f'{first.model} успешно создан')

    try:
      second = Car('Model2', 444, 'Л228ОХ')
    except IncorrectVinNumber as exc:
      print(exc.message)
    except IncorrectCarNumbers as exc:
      print(exc.message)
    else:
      print(f'{second.model} успешно создан')

    try:
      third = Car('Model3', 1428425, 'нет номера')
    except IncorrectVinNumber as exc:
      print(exc.message)
    except IncorrectCarNumbers as exc:
      print(exc.message)
    else:
      print(f'{third.model} успешно создан')

if __name__ == '__main__':
    main()