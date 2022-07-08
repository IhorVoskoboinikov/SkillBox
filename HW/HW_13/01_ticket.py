# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os


def make_ticket(fio, from_, to, date):
    template_path = os.path.join('images', 'ticket_template.png')
    fond_path = os.path.join('images', 'ofont.ru_Hero.ttf')
    im = Image.open(template_path)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(fond_path, size=15)
    text_color = ImageColor.colormap['black']
    draw.text((50, 125), fio, font=font, fill=text_color)
    draw.text((50, 193), from_, font=font, fill=text_color)
    draw.text((50, 260), to, font=font, fill=text_color)
    draw.text((285, 260), date, font=font, fill=text_color)
    im.save('ticket_to_print.png')
    print('Ticket ready to print!')


if __name__ == '__main__':
    ticket = make_ticket
    ticket(fio='Воскобойников И. Л.', from_='Киев', to='Харьков', date='01. 08.')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
