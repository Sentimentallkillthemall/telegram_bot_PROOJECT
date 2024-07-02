
import telebot
from telebot import types
from random import randrange
TOKEN = "7360213021:AAFz1-o5nlchTkXeWhXU3Cewb9Rrd5Q0iOw"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def language_choose(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ru = types.KeyboardButton('🇷🇺Русский язык🇷🇺')
    button_en = types.KeyboardButton('🇺🇸English Language🇺🇸')
    markup.add(button_ru, button_en)
    bot.send_message(message.chat.id, '🇺🇸Choose language!'
                                      '\n🇷🇺Выберете язык!', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '🇷🇺Русский язык🇷🇺')
def ru_start(message: types.Message):
    global language, bonus
    text = '✨Добро пожаловать в Sneaker Shop💎Желаем приятных покупок'
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_all = types.KeyboardButton('🏪Все товары🏪')
    button_information = types.KeyboardButton('📑Информация📑')
    button_discount = types.KeyboardButton('💰Скидка💰')
    markup.add(button_all, button_information, button_discount)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    language = 'ru'
    bonus = False


@bot.message_handler(commands=['🇺🇸English Language🇺🇸'])
def en_start(message: types.Message):
    global language, bonus
    text = '✨Welcome to Sneaker Shop💎Happy shopping'
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_all = types.KeyboardButton('🏪All goods🏪')
    button_discount = types.KeyboardButton('💰Discount💰')
    button_information = types.KeyboardButton('📑Information📑')
    markup.add(button_all, button_information, button_discount)
    bot.send_message(message.chat.id, text, reply_markup=markup)
    language = 'en'
    bonus = False


@bot.message_handler(func=lambda message: message.text == '🏪Все товары🏪')
def fitness_bot(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_sport_sneakers = types.KeyboardButton('🥇Для Спорта🥇')
    button_casual_sneakers = types.KeyboardButton('🗓Повседневная Обувь🗓')
    button_on_main = types.KeyboardButton('💲На Главную💲')
    markup.add(button_sport_sneakers, button_casual_sneakers, button_on_main)
    bot.send_message(message.chat.id, 'Выберите Категорию', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '🏪All goods🏪')
def fitness_bot(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_sport_sneakers = types.KeyboardButton('🥇For sport🥇')
    button_casual_sneakers = types.KeyboardButton('🗓Casual Shoes🗓')
    button_winter = types.KeyboardButton('❄️Winter Boots❄️')
    button_on_main = types.KeyboardButton('💲На Главную💲')
    markup.add(button_sport_sneakers, button_casual_sneakers, button_winter, button_on_main)
    bot.send_message(message.chat.id, 'Choose a category', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '🥇Для Спорта🥇')
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_basketball = types.KeyboardButton('🏀Для Баскетбола🏀')
    button_footbal = types.KeyboardButton('⚽️Для Футбола⚽️')
    button_volleyball = types.KeyboardButton('🏐Для Волейбола🏐')
    button_runners = types.KeyboardButton('🏃Для бега🏃')
    button_back = types.KeyboardButton('👋Назад👋')
    markup.add(button_basketball, button_footbal, button_volleyball, button_runners, button_back)
    bot.send_message(message.chat.id,'Какие кроссовки вам нужны?', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == '🏀Для Баскетбола🏀')
    def for_basketball(message):
        bot.send_message(message.chat.id, 'Вот все кроссовки, которые подойдут для баскетбола:\n'
                                          '1. Nike Air Max Impact 4\n'
                                          '2. Nike Lebron NXXT GEN\n'
                                          '3. UNDER ARMOR CURRY FLOW 10\n'
                                          '4. Jordan Luke 2\n'
                                          '5. Adidas DameCetified\n')
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_one = types.KeyboardButton('Nike Air Max Impact')
        button_two = types.KeyboardButton('Nike Lebron NXXT GEN')
        button_three = types.KeyboardButton('UNDER ARMOR CURRY FLOW 10')
        button_four = types.KeyboardButton('Jordan Luke 2')
        button_five = types.KeyboardButton('Adidas DameCetified')
        button_on_main = types.KeyboardButton('💲На Главную💲')

        markup.add(button_one, button_two, button_three, button_four, button_five, button_on_main)

        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Nike Air Max Impact")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('IMPACTNIKE4.jpg', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Nike Air Max Impact 4 — баскетбольные кроссовки, которые приятно всех удивили. Своим непритязательным внешним видом они удивляют игроков своей исключительной производительностью на корте. Эта бюджетная модель не только сохраняет качества, которые сделали ее предшественника Air Max Impact 3 хитом, но также содержит несколько улучшений. "
                                       "\n💵Цена: 135$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Nike Lebron NXXT GEN")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Версия двадцатой модели Джеймса NXXT Gen технологически немного попроще, чем классические LeBron 20: лёгкий сетчатый верх, амортизация Air Zoom, кожаные вставки на язычке, пятке, средней панели и в области носка "
                                       "\n💵Цена: 170$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "UNDER ARMOR CURRY FLOW 10")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Основываясь на успехах двух последних фирменных моделей Curry Brand, Curry Flow 10 получили оптимизированные технологии UA Flow и UA Warp 2.0 для улучшения ощущений при ходьбе и занятиях спортом, делая обувь более легкой и дышащей."
                                       "Улучшенная технология Warp 2.0 включает в себя стратегически расположенные ленты-тейпы различной ширины на верхней части для работы с самыми высокими стрессовыми нагрузками во время взрывных, быстрых фирменных движений Стефа, для точного передвижения на площадке и создания беспрецедентной поддержки и комфорта."
                                       "\n💵Цена: 160$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

            @bot.message_handler(func=lambda message: message.text == "2")
            def handle_get_picture(message):
                print(f"Received 'Get Picture' from {message.chat.id}")
                try:
                    with open('img.png', 'rb') as photo:
                        bot.send_photo(message.chat.id, photo,
                                       caption="Версия двадцатой модели Джеймса NXXT Gen технологически немного попроще, чем классические LeBron 20: лёгкий сетчатый верх, амортизация Air Zoom, кожаные вставки на язычке, пятке, средней панели и в области носка "
                                               "\n💵Цена: 170$💵")
                        print("Picture sent successfully")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Произошла ошибка.")
                    print("Picture not found")
                except Exception as e:
                    print(f"Error sending picture: {e}")
                    bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Jordan Luke 2")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_2.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Верх пары сделан из плетёного текстиля, синтетики (Fuse) и кожи, но в зависимости от расцветки что-то может меняться. Язычок из неопрена и искусственной кожи. Терморегуляция на базовом уровне.Протектор из прочного каучука. Рисунок, представляющий комбинацию треугольных фигур и узких линий, потрясающе цепляет паркет."
                                       "\n💵Цена: 130$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Adidas DameCetified")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_4.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="adidas Dame Certified получили легкую промежуточную подошву Bounce для повышенной амортизации и дышащий верх, обеспечивающий необходимую циркуляцию воздуха. Уникальный рельефный рисунок на резиновой подошве обеспечивает превосходное сцепление с паркетом. В дизайне добавлены классические три полоски adidas и фирменный брендинг Лилларда, включая его лого и прозвище Dolla."
                                       "\n💵Цена: 95$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == '⚽️Для Футбола⚽️')
    def for_basketball(message):
        bot.send_message(message.chat.id, 'Вот все бутсы, которые подойдут для футбола:\n'
                                          '1. Nike Phantom GT II\n'
                                          '2. Adidas Predator Edge\n'
                                          '3. PUMA Ultra Ultimate\n'
                                          '4. PUMA Future Z 1.4\n'
                                          '5. Nike Air Zoom Mercurial\n')

        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_one = types.KeyboardButton('Nike Phantom GT II')
        button_two = types.KeyboardButton('Adidas Predator Edge')
        button_three = types.KeyboardButton('PUMA Ultra Ultimate')
        button_four = types.KeyboardButton('PUMA Future Z 1.4')
        button_five = types.KeyboardButton('Nike Air Zoom Mercurial')
        button_on_main = types.KeyboardButton('💲На Главную💲')

        markup.add(button_one, button_two, button_three, button_four, button_five, button_on_main)

        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Nike Phantom GT II")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_5.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                                caption="Nike Phantom GT2 Elite FG, обновленный новой генеративной текстурой, усовершенствовал дизайн своего предшественника, основанный на данных, чтобы обеспечить улучшенное прикосновение и управление.Переработанный шевронный рисунок позволяет точно манипулировать мячом, увеличивая вращение для резкого падения и отклонения при ударах, а также дает вам доступ к полному списку возмутительных пасов KDB."
                                        "\n💵Цена: 235$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Adidas Predator Edge")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_7.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                                caption="Верх Zone Skin включает отдельные ребристые секции, каждая из которых обеспечивает свой тип контакта шипа с мячом. Внизу Power Facet переносит вес на переднюю часть стопы для мощных ударов. Адаптивный воротник Adidas PRIMEKNIT фиксирует вас, пока вы сохраняете контроль."
                                        "\n💵Цена: 180$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "PUMA Ultra Ultimate")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_6.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                                caption="Puma Ultra 2023 – это ультралегкие и ультрабыстрые бутсы, которые подходят для игроков, которые хотят демонстрировать свою скорость и ловкость на поле. Сверхлегкая специальная ткань ULTRAWEAVE со структурированной растяжкой в ​​четырех направлениях, снижающая вес и уменьшающая трение. Подошва SPEEDPLATE двойной плотности гарантирует быстрое движение. Верх бутс также имеет специальное покрытие GRIPCONTROL PRO, которое улучшает контроль мяча в любых условиях."
                                        "\n💵Цена: 180$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "PUMA Future Z 1.4")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_9.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                                caption="Бутсы имеют цельный верх без традиционного, внутреннего язычка, который выполнен из эластана и плотно охватывает стопу, удерживая ее при резких маневрах и боковых движениях, обеспечивая комфортную посадку и быструю адаптацию к стопе. Эластичный материал AdapLite, используемый так же при изготовлении верхней части бутс, позволяет верху изгибаться вместе со стопой при движении, обеспечивает стопе устойчивость и поддержку, усиливает конструкцию верха."
                                        "\n💵Цена: 200$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Nike Air Zoom Mercurial")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_8.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                                caption="Бутсы Nike Air Zoom Mercurial представляют собой стильную и технологичную обувь для футбола, сочетающую в себе комфорт и высокую производительность. Они оснащены технологией Air Zoom, которая обеспечивает амортизацию и отзывчивость при движении на поле.Дизайн бутс выполнен в современном стиле, что делает их привлекательными для игроков всех уровней. Материал верха обуви обеспечивает хорошую посадку и контроль над мячом.С учетом всех этих факторов, бутсы Nike Air Zoom Mercurial можно рекомендовать как отличный выбор для футболистов, ценящих комфорт, стиль и качество."
                                        "\n💵Цена: $285💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == '🏐Для Волейбола🏐')
    def for_basketball(message):
        bot.send_message(message.chat.id, 'Вот все кроссовки, которые подойдут для волейбола:\n'
                                          '1. Asics Upcourt 5\n'
                                          '2. Nike React HyperSet SE\n'
                                          '3. Nike Precision VI\n'
                                          '4. Adidas Speedcourt\n'
                                          '5. Nike Legend Essential 3 Next Nature\n')

        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_one = types.KeyboardButton('Asics Upcourt 5')
        button_two = types.KeyboardButton('Nike React HyperSet SE')
        button_three = types.KeyboardButton('Mizuno Wave Lightning Z6')
        button_four = types.KeyboardButton('Nike Air Zoom HyperAce 2')
        button_five = types.KeyboardButton('Puma All-Pro Nitro')
        button_on_main = types.KeyboardButton('💲На Главную💲')

        markup.add(button_one, button_two, button_three, button_four, button_five, button_on_main)

        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Asics Upcourt 5")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_10.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Верх из легкой сетки и набивка дарят премиальный комфорт, который завершает мягкая пена React. Технология от Nike активно используется в баскетболе и беге. Ее плюсы - износостойкость, упругость и высокая мягкасть. А вот подметка выполнена из каучука или Icy Sole. Nike React Hyperset являются прорывом в воллейбольной обуви. Традиции воллейбола и заимстования у баскетбола делают пару готовой к борьбе через сетку на самом высоком уровне." 
                                       "\n💵Цена: 60$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Nike React HyperSet SE")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_11.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Волейбольные кроссовки Nike React Hyperset сочетают в себе такие качества, как отличное сцепление, динамическую амортизацию и максимальный комфорт. Резкие остановки без потери темпа, уверенные прыжки и мягкие приземления – все это про надежную модель Hyperset, которые подойдут как новичкам, так и профессионалам!"
                                       "\n💵Цена: 135$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Mizuno Wave Lightning Z6")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_15.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Волейбольные кроссовки Mizuno Wave Lightning Z6 – универсальный солдат элитной категории. Модель совмещает в себе лёгкость, скорость, манёвренность и амортизацию 80 уровня. Инженеры Mizuno нашли равновесие в комфорте и безопасности, стабильности и энергичном отклике. Мгновенные реакции и динамичные выпады, уверенность и мощь в каждом шаге новых Mizuno Wave Lightning Z6, самых лёгких, амортизирующих и новых.Знакомый дизайн удивляет новыми решениями и яркими цветами."
                                       "\n💵Цена: $97💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Nike Air Zoom HyperAce 2")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_13.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Тренировочные воллейбольные кроссовки Nike Zoom Hyperace 2 с прочной конструкцией разработаны для поверхностей с твердым покрытием, оснащены модулем Zoom Air для легкой амортизации и клеткой из ТПУ, которая соответствует вашей ноге для удобной посадки и ощущения."
                                       "\n💵Цена: $90💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Puma All-Pro Nitro")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_14.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Благодаря пористому строению внешнего покрытия Puma All-Pro Nitro заимели очень крутую циркуляцию воздуха.Кроссовки подойдут как на широкую, так и узкую стопу. Проблему с подьёмом также должны обойти стороной.Амортизация представлена абсолютно новой технологией “Nitro sqd”. Это пена, собранная из двух нитро пен: внутренняя –  мягкая, внешняя- более жесткая и отзывчивая. Перемещаться по площадке одно удовольствие. Очень мягкий и плавный перекат. Пена гасит абсолютно любые ударные нагрузки."
                                       "\n💵Цена: 130$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

        @bot.message_handler(func=lambda message: message.text == '🏃Для бега🏃')
        def for_basketball(message):
            bot.send_message(message.chat.id, 'Вот все кроссовки, которые подойдут для бега:\n'
                                              '1. Asics Novablast 4\n'
                                              '2. Adidas Supernova Rise\n'
                                              '3. On Cloudeclipse\n'
                                              '4. Altra Via Olympus 2\n'
                                              '5. Nike Vaporfly 3\n')

            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_one = types.KeyboardButton('Asics Novablast 4')
            button_two = types.KeyboardButton('Adidas Supernova Rise')
            button_three = types.KeyboardButton('On Cloudeclipse')
            button_four = types.KeyboardButton('Altra Via Olympus 2')
            button_five = types.KeyboardButton('Nike Vaporfly 3')
            button_on_main = types.KeyboardButton('💲На Главную💲')

            markup.add(button_one, button_two, button_three, button_four, button_five, button_on_main)

            bot.send_message(message.chat.id, 'Выберите модель', reply_markup=markup)

            @bot.message_handler(func=lambda message: message.text == "Asics Novablast 4")
            def handle_get_picture(message):
                print(f"Received 'Get Picture' from {message.chat.id}")
                try:
                    with open('img_16.png', 'rb') as photo:
                        bot.send_photo(message.chat.id, photo,
                                       caption="Asics Novablast 4 представляют собой асфальтовую версию тренировочных кроссовок с упругой амортизацией и небольшим весом. Они стали более адаптивными и динамичными, чем предыдущие поколения. Обновленная версия Novablast объединила в себе передовые технологии и усовершенствованные материалы, обеспечивая бегунам стабильность и комфорт при каждом шаге. "
                                               "\n💵Цена: 140$💵")
                        print("Picture sent successfully")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Произошла ошибка.")
                    print("Picture not found")
                except Exception as e:
                    print(f"Error sending picture: {e}")
                    bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

            @bot.message_handler(func=lambda message: message.text == "Adidas Supernova Rise")
            def handle_get_picture(message):
                print(f"Received 'Get Picture' from {message.chat.id}")
                try:
                    with open('img_17.png', 'rb') as photo:
                        bot.send_photo(message.chat.id, photo,
                                       caption="Adidas Supernova Rise — это отличные универсальные кроссовки для ежедневных тренировок. Носок оснащен опорными стержнями, которые упрочняют переднюю часть подошвы, обеспечивая легкий рокерный прокат и эффективные переходы. Также в них используется совершенно новая подошва Dreamstrike+ на основе PEBA, которая хоть и не супер энергичная, но все же обеспечивает приличный энерговозврат."
                                               "\n💵Цена: 140$💵")
                        print("Picture sent successfully")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Произошла ошибка.")
                    print("Picture not found")
                except Exception as e:
                    print(f"Error sending picture: {e}")
                    bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

            @bot.message_handler(func=lambda message: message.text == "On Cloudeclipse")
            def handle_get_picture(message):
                print(f"Received 'Get Picture' from {message.chat.id}")
                try:
                    with open('img_18.png', 'rb') as photo:
                        bot.send_photo(message.chat.id, photo,
                                       caption="Cloudeclipse — это хорошие максималистские кроссовки, которые обеспечивают очень высокий уровень защиты от земли. Они имеют более упругий ход, чем большинство кроссовок с максимальной амортизацией, и лучше всего подходят для легких или восстановительных пробежек, поскольку их пенная подошва Helion не обеспечивает большого возврата энергии."
                                               "\n💵Цена: 180$💵")
                        print("Picture sent successfully")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Произошла ошибка.")
                    print("Picture not found")
                except Exception as e:
                    print(f"Error sending picture: {e}")
                    bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

            @bot.message_handler(func=lambda message: message.text == "Altra Via Olympus 2")
            def handle_get_picture(message):
                print(f"Received 'Get Picture' from {message.chat.id}")
                try:
                    with open('img_19.png', 'rb') as photo:
                        bot.send_photo(message.chat.id, photo,
                                       caption="VIA Olympus 2 знаменует собой заметный скачок вперед по сравнению с Altra, улучшая амортизацию и долговечность, сохраняя любимые черты своего предшественника — просторную посадку, слегка наклонную геометрию и непревзойденный комфорт."
                                               "\n💵Цена: 160$💵")
                        print("Picture sent successfully")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Произошла ошибка.")
                    print("Picture not found")
                except Exception as e:
                    print(f"Error sending picture: {e}")
                    bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

            @bot.message_handler(func=lambda message: message.text == "Nike Vaporfly 3")
            def handle_get_picture(message):
                print(f"Received 'Get Picture' from {message.chat.id}")
                try:
                    with open('img_12.png', 'rb') as photo:
                        bot.send_photo(message.chat.id, photo,
                                       caption="Vaporfly от Nike знаменует собой значительное обновление концепции «оригинальной суперобуви». Эта третья итерация, более легкая, быстрая и более устойчивая во время всех наших пробежек, является чудом марафона, однако ее более мягкая межподошва и более плавный отрыв носка делают ее менее подходящей для забегов на 5/10 км, чем ее предшественники. Верная своим корням, она возвышает выигрышную комбинацию ложкообразной углеродной пластины, упругой межподошвы Pebax и легкой конструкции."
                                               "\n💵Цена: 240$💵")
                        print("Picture sent successfully")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Произошла ошибка.")
                    print("Picture not found")
                except Exception as e:
                    print(f"Error sending picture: {e}")
                    bot.send_message(message.chat.id, "Ошибка при отправке картинки.")


@bot.message_handler(func=lambda message: message.text == '🥇For sport🥇')
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_basketball = types.KeyboardButton('🏀For Basketball🏀')
    button_footbal = types.KeyboardButton('⚽️For Football⚽️')
    button_volleyball = types.KeyboardButton('🏐For Volleyball🏐')
    button_runners = types.KeyboardButton('🏃For running🏃')
    button_on_main = types.KeyboardButton('💲На Главную💲')
    markup.add(button_basketball, button_footbal, button_volleyball, button_runners, button_on_main)
    bot.send_message(message.chat.id,'Which shoes do you need?', reply_markup=markup)




@bot.message_handler(func=lambda message: message.text == '🗓Повседневная Обувь🗓')
def fitness_bot(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_summer = types.KeyboardButton('☀️Летняя Обувь☀️')
    button_autumn = types.KeyboardButton('🍁Осенняя Обувь🍁')
    button_winter = types.KeyboardButton('❄️Зимняя Обувь❄️')
    button_spring = types.KeyboardButton('🌸Весенняя Обувь🌸')
    button_on_main = types.KeyboardButton('💲На Главную💲')
    markup.add( button_summer, button_autumn, button_winter,button_spring,  button_on_main)
    bot.send_message(message.chat.id, 'Выберите Категорию', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == '☀️Летняя Обувь☀️')
    def for_basketball(message):
        bot.send_message(message.chat.id, 'Вот лучшая обувь на лето:\n'
                                          '1. Asics GT-2160\n'
                                          '2. New Balance 990 v6\n'
                                          '3. Nike Air Zoom Spiridon Cage 2\n')

        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_one = types.KeyboardButton('Asics GT-2160')
        button_two = types.KeyboardButton('New Balance 990 v6')
        button_three = types.KeyboardButton('Nike Air Zoom Spiridon Cage 2')

        button_on_main = types.KeyboardButton('💲На Главную💲')

        markup.add(button_one, button_two, button_three, button_on_main)

        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=markup)

        @bot.message_handler(func=lambda message: message.text == "Asics GT-2160")
        def handle_get_picture(message):
            print(f"Received 'Get Picture' from {message.chat.id}")
            try:
                with open('img_20.png', 'rb') as photo:
                    bot.send_photo(message.chat.id, photo,
                                   caption="Кроссовки выполнены из текстиля и искусственной кожи. Межподошва с технологией GEL® обеспечивает амортизацию. Система поддержки TRUSSTIC® - литой элемент расположенный под центральной частью подошвы. Обеспечивает стабильность, легкость, предотвращает скручивание стопы."
                                           "\n💵Цена: 120$💵")
                    print("Picture sent successfully")
            except FileNotFoundError:
                bot.send_message(message.chat.id, "Произошла ошибка.")
                print("Picture not found")
            except Exception as e:
                print(f"Error sending picture: {e}")
                bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

        @bot.message_handler(func=lambda message: message.text == "New Balance 990 v6")
        def handle_get_picture(message):
            print(f"Received 'Get Picture' from {message.chat.id}")
            try:
                with open('img_21.png', 'rb') as photo:
                    bot.send_photo(message.chat.id, photo,
                                   caption="Кроссовки выполнены из текстиля и искусственной кожи. Межподошва с технологией GEL® обеспечивает амортизацию. Система поддержки TRUSSTIC® - литой элемент расположенный под центральной частью подошвы. Обеспечивает стабильность, легкость, предотвращает скручивание стопы."
                                           "\n💵Цена: 199$💵")
                    print("Picture sent successfully")
            except FileNotFoundError:
                bot.send_message(message.chat.id, "Произошла ошибка.")
                print("Picture not found")
            except Exception as e:
                print(f"Error sending picture: {e}")
                bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

        @bot.message_handler(func=lambda message: message.text == "Asics GT-2160")
        def handle_get_picture(message):
            print(f"Received 'Get Picture' from {message.chat.id}")
            try:
                with open('img_20.png', 'rb') as photo:
                    bot.send_photo(message.chat.id, photo,
                                   caption="Кроссовки выполнены из текстиля и искусственной кожи. Межподошва с технологией GEL® обеспечивает амортизацию. Система поддержки TRUSSTIC® - литой элемент расположенный под центральной частью подошвы. Обеспечивает стабильность, легкость, предотвращает скручивание стопы."
                                           "\n💵Цена: 120$💵")
                    print("Picture sent successfully")
            except FileNotFoundError:
                bot.send_message(message.chat.id, "Произошла ошибка.")
                print("Picture not found")
            except Exception as e:
                print(f"Error sending picture: {e}")
                bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

        @bot.message_handler(func=lambda message: message.text == "Nike Air Zoom Spiridon Cage 2")
        def handle_get_picture(message):
            print(f"Received 'Get Picture' from {message.chat.id}")
            try:
                with open('img_24.png', 'rb') as photo:
                    bot.send_photo(message.chat.id, photo,
                                   caption="Nike Air Zoom Spiridon Cage отличаются универсальностью и подходят как для повседневной носки, так и для занятий спортом. Их современный дизайн и технологии делают их привлекательным выбором для тех, кто ценит комфорт и стиль."
                                           "\n💵Цена: 135$💵")
                    print("Picture sent successfully")
            except FileNotFoundError:
                bot.send_message(message.chat.id, "Произошла ошибка.")
                print("Picture not found")
            except Exception as e:
                print(f"Error sending picture: {e}")
                bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == '🍁Осенняя Обувь🍁')
    def for_basketball(message):
        bot.send_message(message.chat.id, 'Вот лучшая обувь на :\n'
                                          '1. Dr. Martens 1460 Smooth\n'
                                          '2. Timberland Boots\n'
                                          '3. Nike Airmax 95\n')

        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_one = types.KeyboardButton('Dr. Martens 1460 Smooth')
        button_two = types.KeyboardButton('Timberland Boots')
        button_three = types.KeyboardButton('Nike Airmax 95')

        button_on_main = types.KeyboardButton('💲На Главную💲')

        markup.add(button_one, button_two, button_three, button_on_main)

        bot.send_message(message.chat.id, 'Выберите модель', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == "Dr. Martens 1460 Smooth")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('dr_martens.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption=" Ботинки Dr. Martens — это икона стиля, известная своей прочностью и уникальным дизайном. Они изготовлены из качественной натуральной кожи и имеют характерный жесткий подошву, которая обеспечивает отличную поддержку и комфорт. Эта обувь отлично подходит как для повседневной носки, так и для создания стильного образа."
                                       "\n💵Цена: 170$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Timberland Boots")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_22.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Бренд Timberland известен своими прочными ботинками, которые отлично подходят для активного образа жизни и занятий на свежем воздухе. Изготовленные из высококачественных материалов, ботинки Timberland комфортны, водонепроницаемы и долговечны. Они станут надежным выбором для тех, кто ценит комфорт и стиль."
                                       "\n💵Цена: 155$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")

    @bot.message_handler(func=lambda message: message.text == "Nike Airmax 95")
    def handle_get_picture(message):
        print(f"Received 'Get Picture' from {message.chat.id}")
        try:
            with open('img_23.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo,
                               caption="Nike Air Max 95 - это легендарная модель кроссовок, которая впервые была выпущена в 1995 году. Nike Air Max 95 стали популярными не только благодаря своей технической функциональности, но и из-за своего уникального дизайна, который делает их отличным выбором для повседневной носки и спортивных тренировок. Кроссовки доступны в различных цветовых решениях, что позволяет выбрать подходящий вариант для любого стиля."
                                       "\n💵Цена: 175$💵")
                print("Picture sent successfully")
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Произошла ошибка.")
            print("Picture not found")
        except Exception as e:
            print(f"Error sending picture: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке картинки.")


@bot.message_handler(func=lambda message: message.text == '💲На Главную💲')
def back(message):
    ru_start(message)


@bot.message_handler(func=lambda message: message.text == '👋Back👋')
def back(message):
    en_start(message)


@bot.message_handler(func=lambda message: message.text == '💰Discounts💰')
def bonus(message):
    global bonus
    if bonus == False:
        discount = randrange(5, 30, 5)
        bot.send_message(message.chat.id, f'Your discount: {discount}')
        bonus = True
    else:
        bot.send_message(message.chat.id, 'You already have a discount')


@bot.message_handler(func=lambda message: message.text == '💰Скидка💰')
def bonus(message):
    global bonus
    if bonus == False:
        discount = randrange(5, 30, 5)
        bot.send_message(message.chat.id, f'Ваша скидка: {discount}%')
        bonus = True
    else:
        bot.send_message(message.chat.id, 'У вас уже есть скидка')


bot.infinity_polling()
