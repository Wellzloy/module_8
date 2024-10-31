class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    # def get_vin(self):
    #     return self.__vin
    #
    # def set_vin(self, value: int):
    #     self.__vin = value
    def __is_valid_vin(self, vin_number: int):
        if not isinstance(vin_number, int):
            raise Exception("Некорректный тип данных для VIN номера")
        if not (1000000 <= vin_number <= 9999999):
            raise Exception("Неверный диапазон для VIN номера")
        return True

