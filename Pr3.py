from enum import Enum
import random


class Temperature(Enum):
    celsius = 'C'
    fareingeth = 'F'
    kelvin = 'K'


def GenerateWeather():
    cities = ['Абакан','Сорск','Усть-Абакан','Таштып','Боград','Копьёво','Абаза','Черногорск']
    weather = {city: round(random.uniform(-30,30),1) for city in cities}
    return weather


def ConvertTemperature(celsius, unit):
    if unit == Temperature.celsius:
        return celsius
    elif unit == Temperature.fareingeth:
        return round(celsius * 9/5 +32, 1)
    elif unit == Temperature.kelvin:
        return round(celsius + 273.15, 1)
    
def GetWaetherUnits(city, weather):
    celsius = weather[city]
    fareingeth = ConvertTemperature(celsius, Temperature.fareingeth)
    kelvin = ConvertTemperature(celsius, Temperature.kelvin)
    return f"{celsius}{Temperature.celsius.value},{fareingeth}{Temperature.fareingeth.value}, {kelvin}{Temperature.kelvin.value}" 


def FilterCitys(weather, vibor):
    if vibor == '+':
        return list(filter(lambda i: i[1] > 0, weather.items()))
    elif vibor == '-':
        return list(filter(lambda i: i[1] <= 0, weather.items()))


def SortCity(weather, vibor =True):
    return sorted(weather.items(), key=lambda i: i[1], reverse=not vibor)


weather = GenerateWeather()


citys = ['Абакан','Сорск','Усть-Абакан','Таштып','Боград','Копьёво','Абаза','Черногорск']


city = input(f"Введите город о котором хотите узнать из списка: {citys}: ")
print("\n"f"Погода в {city}: {GetWaetherUnits(city, weather)}")


vibor = input("Введите + или - смотря как вы хотите отфильтровать города: ")
FilterCity = FilterCitys(weather, vibor)
print("\n"f"Города с погодой {'больше нуля' if vibor== '+' else 'меньше либо равно нуля' }: {FilterCity}")


SortCityAcs = SortCity(weather, vibor=True)
SortCityDesc = SortCity(weather, vibor=False)
print(f"Города отсортированные по возрастанию: {SortCityAcs}")
print(f"Города отсортированные по убыванию: {SortCityDesc}")
