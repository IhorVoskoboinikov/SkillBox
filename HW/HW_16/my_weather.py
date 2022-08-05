# -*- coding: utf-8 -*-
from pprint import pprint
import peewee
import bs4
import requests
import re
import cv2
from bs4 import BeautifulSoup


class WeatherMaker:
    def __init__(self, site):
        self.html = requests.get(site).text
        self.list_weather = list()

    def get_weather_forecast(self):
        weather_date_pattern = r'[\d+]{4}-[\d+]{2}-[\d+]{2}'
        weather_temperature_pattern = r'[-|+]\d{2}'
        weather_pattern = r'^[А-Я][а-я]+'

        data_weather = bs4.BeautifulSoup(self.html, 'html.parser')
        all_data_weather = str(data_weather.find_all('div', {'class': "tabs"}))
        all_temperature = str(data_weather.find_all('div', {'class': "max"}))
        date_for_check = sorted(set(re.findall(weather_date_pattern, all_data_weather)))
        temperature_for_check = re.findall(weather_temperature_pattern, all_temperature)
        weather_for_check = [text for text in all_data_weather.split('"') if re.findall(weather_pattern, text)]
        for weather, temperature, date in zip(weather_for_check, temperature_for_check, date_for_check):
            self.list_weather.append({'weather': weather, 'temperature': temperature, 'date': date})

        pprint(self.list_weather)


class ImageMaker:

    def __init__(self):
        pass

    def draw_a_picture(self):
        sun_img_pattern = r'[Яя]сно'
        rain_img_pattern = r'[Дд]ождь'
        snow_img_pattern = r'[Сс]нег'
        base_im = 'python_snippets/external_data/probe.jpg'
        for weather_text in weather.list_weather:
            image_0 = cv2.imread(base_im)
            img_0_width, img_0_height = image_0.shape[:2]
            print(weather_text['погода'])
            if re.findall(sun_img_pattern, weather_text['погода']):
                img_to_draw = 'sun'
                self.sketch_background(img_for_sketch=image_0)
            elif re.findall(rain_img_pattern, weather_text['погода']):
                img_to_draw = 'rain'
            elif re.findall(snow_img_pattern, weather_text['погода']):
                img_to_draw = 'snow'
            else:
                img_to_draw = 'cloud'
            add_img = f'python_snippets/external_data/weather_img/{img_to_draw}.jpg'
            image_1 = cv2.imread(add_img)
            img_1_width, img_1_height = image_1.shape[:2]
            fontFace = cv2.FONT_HERSHEY_COMPLEX
            weather_img = cv2.putText(image_0, f'Дата: {weather_text["дата"]}', (5, 190), fontFace, 0.5, (0, 0, 0), 1)
            weather_img = cv2.putText(image_0, f'Температура: {weather_text["температура"]}', (5, 210), fontFace, 0.5,
                                      (0, 0, 0), 1)
            weather_img = cv2.putText(image_0, weather_text['погода'], (5, 230), fontFace, 0.5, (0, 0, 0), 1)
            image_0[:img_1_width, :img_1_height] = image_1[:]
            image_0[img_0_width - img_1_width:, img_0_height - img_1_height:] = image_1[:]
            # cv2.imwrite(f'img/{weather_text["дата"]}, {img_to_draw}.jpg', image_0)
            # cv2.imshow('Weather', image_0)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

    def sketch_background(self, img_for_sketch):
        i = 0
        k = 0
        for _ in range(50):
            img_for_sketch[:, 0 + i:50 + i] = (100 + k, 255 - k / 8, 255)
            i += 20
            k += 5
        return img_for_sketch


database = peewee.SqliteDatabase("db_weather.db")


class Weather(peewee.Model):
    class Meta:
        database = database


class FieldsToDatabase(Weather):
    weather = peewee.CharField()
    temperature = peewee.CharField()
    date = peewee.CharField()


FieldsToDatabase.create_table()


class DatabaseUpdater:

    # def get_data_from_database(self, from_date, to_date):
    #     pass

    def save_forecast_to_database(self, list_forecast_to_save):
        data_to_db = FieldsToDatabase.insert_many(list_forecast_to_save).execute()


weather = WeatherMaker(site='https://sinoptik.ua')
weather_img = ImageMaker()
db_update = DatabaseUpdater()
weather.get_weather_forecast()
db_update.save_forecast_to_database(list_forecast_to_save=weather.list_weather)
for data in FieldsToDatabase.select():
    print(f'Дата: {data.date} Погода: {data.weather} Температура: {data.temperature}')
# weather_img.draw_a_picture()
