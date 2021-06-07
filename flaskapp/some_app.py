print("Hello world")

from flask import Flask

app = Flask(__name__)


# декоратор для вывода страницы по умолчанию
@app.route("/")
def hello():
    return " <html><head></head> <body> Hello World! </body></html>"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

from flask import render_template


import cv2
import numpy as np
import matplotlib.pyplot as plt
import image_slicer


# Открываем файл с картинкой.
tiles = image_slicer.slice('img.png', 4)

# Сдвигаем по часовой стрелки части картинки.
img_tmp = tiles[0].image
tiles[0].image = tiles[1].image
tiles[1].image = tiles[2].image
tiles[2].image = tiles[3].image
tiles[3].image = img_tmp

# Сохраняем новую картинку.
new_img = image_slicer.join(tiles)
new_img.save('new_img.png')

image_BGR = cv2.imread('img.png')
new_image_BGR = cv2.imread('new_img.png')

# наша новая функция сайта
@app.route("/data_to")
def data_to():
    # создаем переменные с данными для передачи в шаблон
    some_pars = {'user': 'Ivan', 'color': 'red'}
    some_str = 'Hello my dear friends!'
    some_value = 10
    # передаем данные в шаблон и вызываем его
    return render_template('simple.html', some_str=some_str,
                           some_value=some_value, some_pars=some_pars)


from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)

import os
# подключаем наш модуль и переименовываем
# для исключения конфликта имен
#import net as neuronet


