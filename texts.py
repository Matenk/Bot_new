
all_info = 'Я бот, который уже не только считает ккал, ещё я могу предложить тебе товары из спортивного питания!'
all_mess = 'Введи команду /start чтобы начать общение!'
start = ('Я бот помогающий твоему здоровью! Нажми "Расчет", чтобы словить кринж или "Информация", '
         'чтобы познакомиться поближе, если ты понимаешь о чем я..')
buy_complete = 'Позравляем с покупкой!'

age_ = 'Введи свой возраст.'
growth_ = 'Введи свой рост в см.'
weight_ = 'Введи свой вес в кг. Обещаю никому не скажу (нет).'
formula = '(10 × вес в килограммах) + (6,25 × рост в сантиметрах) − (5 × возраст в годах) + 5'
others = 'Другие предложения'
other = 'Не нашли чего хотели? Не беда, напишите нашему администратору @serge_medIt и он поможет решить проблему!'
class Products:
    def __init__(self, name, info, price):
        self.name = name
        self.info = info
        self.price = price

product1 = Products('Creatine',
                    'Помогает мышцам получать больше энергии, поэтому оно особенно полезно для спортсменов, '
                    'которые хотят увеличить силу, выносливость и набрать мышечную массу.',
                    1000)

product2 = Products('Protein',
                    'Это концентрированный порошок, который стимулирует внутриклеточный белковый синтез, '
                    'необходимый для мышечного роста.',
                    1500)

product3 = Products('L-carnitine',
                    'Является мощным, но полностью безопасным утилизатором жира клеток тела, трансформируя его '
                    'непосредственно в энергию.',
                    1300)

product4 = Products('BCAA',
                    'Играют важную роль в производстве энергии во время выполнения упражнений.',
                    1200)



