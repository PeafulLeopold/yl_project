import random

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton
from PyQt6.QtGui import QIcon, QColor, QTextCharFormat, QPixmap, QIcon
from PyQt6 import QtCore, QtWidgets

from py_items.config import EVENTS, CSV_DATA
from py_items.main_menu import Ui_MainMenu
from py_items.book import Ui_Book
from py_items.calendar_ import Ui_Calendar
from py_items.lessons import Ui_Lessons
from py_items.ancient_world import Ui_AncientWorld
from py_items.middle_ages import Ui_MiddleAges
from py_items.revival_era import Ui_RevivalEra
from py_items.new_era import Ui_NewEra
from py_items.twenty_century import Ui_TwentyCentury
from py_items.modern_world import Ui_ModernWorld
from py_items.quiz_introduction import Ui_QuizIntroduction
from py_items.quiz_question import Ui_QuizQuestion
from py_items.quiz_result import Ui_QuizResult
from py_items.settings import Ui_Settings
from py_items.lesson import Ui_Lesson


THEME = 'light'


QUESTION_NUMBER = 1
AMOUNT_OF_QUESTIONS = 1
LEVEL = ''
USED_LINES = []
CORRECT_ANSWERS = 0


class Lesson(QMainWindow, Ui_Lesson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet('background-color: #ffe4b5;')
        self.return_button.clicked.connect(self.return_back)
        self.next_lesson_button.clicked.connect(self.open_next_lesson)
        self.previous_lesson_button.clicked.connect(self.open_previous_lesson)
        
        self.fourth_photo.setScaledContents(True)
        self.second_photo.setScaledContents(True)
        self.first_photo.setScaledContents(True)
        self.third_photo.setScaledContents(True)

        self.next_lesson_button.setIcon(QIcon('data/icons/next.svg'))
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.previous_lesson_button.setIcon(QIcon('data/icons/previous.svg'))
    

class ModernWorldFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        formatted_text = """
        <h1>Развитие технологий и их влияние на общество</h1>
        
        <h2>Общие сведения:</h2>
        <p>Развитие технологий — это процесс создания и внедрения новых инструментов, методов и систем, которые изменяют способы выполнения задач и взаимодействия между людьми. Технологии играют ключевую роль в формировании современного общества.</p>
        
        <h2>Историческое развитие технологий:</h2>
        <ul>
            <li><strong>Промышленная революция:</strong> переход от ручного труда к механизированному производству в XVIII-XIX веках.</li>
            <li><strong>Электрификация:</strong> внедрение электричества в повседневную жизнь и промышленность в начале XX века.</li>
            <li><strong>Информационная революция:</strong> развитие компьютеров и интернета во второй половине XX века.</li>
            <li><strong>Цифровая эпоха:</strong> повсеместное использование мобильных устройств, социальных сетей и облачных технологий в XXI веке.</li>
        </ul>
        
        <h2>Влияние технологий на общество:</h2>
        <ul>
            <li><strong>Коммуникация:</strong> технологии изменили способы общения между людьми, сделав его более быстрым и доступным.</li>
            <li><strong>Образование:</strong> онлайн-курсы и образовательные платформы сделали знания доступными для широкой аудитории.</li>
            <li><strong>Экономика:</strong> автоматизация и цифровизация изменили рынок труда, создав новые профессии и уничтожив старые.</li>
            <li><strong>Социальные изменения:</strong> технологии способствовали развитию социальных движений и активизировали гражданское участие.</li>
            <li><strong>Здоровье:</strong> медицинские технологии улучшили диагностику и лечение заболеваний, увеличив продолжительность жизни.</li>
        </ul>

        <h2>Проблемы и вызовы:</h2>
        <ul>
            <li><strong>Неравенство:</strong> доступ к технологиям может быть ограничен для определенных групп населения.</li>
            <li><strong>Конфиденциальность:</strong> вопросы безопасности данных и личной информации становятся все более актуальными.</li>
            <li><strong>Зависимость:</strong> чрезмерное использование технологий может привести к социальной изоляции и зависимости.</li>
            <li><strong>Экологические проблемы:</strong> производство технологий может негативно влиять на окружающую среду.</li>
        </ul>

        <h2>Будущее технологий:</h2>
        <p><b>Будущее технологий обещает новые возможности, такие как искусственный интеллект, виртуальная реальность и устойчивые энергетические решения. Однако важно учитывать этические аспекты и воздействие на общество при внедрении новых технологий.</p>

        <h2>Заключение:</h2>
        <p><b>Развитие технологий оказывает глубокое влияние на все аспекты жизни общества. Важно стремиться к сбалансированному подходу к использованию технологий, чтобы максимизировать их положительное воздействие и минимизировать негативные последствия.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Развитие технологий')
    
    def open_next_lesson(self):
        self.first_lesson_window = AncientFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = TwentyCenturySecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = ModernWorld()
        self.back.show()
        self.hide()


class TwentyCenturySecondLesson(Lesson):
    def __init__(self):
        super().__init__()

        formatted_text = """
        <h1>Вторая Мировая Война (1939-1945)</h1>
        
        <h2>Общие сведения:</h2>
        <p>Вторая Мировая Война — глобальный конфликт, который охватил большинство стран мира, включая все великие державы, и стал самым масштабным и разрушительным конфликтом в истории человечества. Война началась 1 сентября 1939 года и закончилась 2 сентября 1945 года.</p>
        
        <h2>Причины войны:</h2>
        <ul>
            <li><strong>Версальский договор:</strong> жесткие условия, наложенные на Германию после Первой Мировой Войны, способствовали росту недовольства.</li>
            <li><strong>Экономический кризис:</strong> Великая депрессия привела к социальным и политическим потрясениям в многих странах.</li>
            <li><strong>Национализм и экспансионизм:</strong> агрессивные действия Германии, Италии и Японии в стремлении расширить свои территории.</li>
            <li><strong>Неудача Лиги Наций:</strong> неспособность предотвратить агрессию со стороны стран-агрессоров.</li>
        </ul>
        
        <h2>Основные участники:</h2>
        <ol>
            <li><strong>Союзники:</strong> США, СССР, Великобритания, Франция, Китай и другие.</li>
            <li><strong>Оси:</strong> Германия, Италия, Япония и их союзники.</li>
        </ol>

        <h2>Ключевые события:</h2>
        <ul>
            <li><strong>Нападение на Польшу (1939):</strong> начало войны с вторжением Германии в Польшу.</li>
            <li><strong>Битва за Британию (1940):</strong> воздушная битва между Германией и Великобританией.</li>
            <li><strong>Операция Барбаросса (1941):</strong> нападение Германии на Советский Союз.</li>
            <li><strong>Перл-Харбор (1941):</strong> нападение Японии на США, что привело к вступлению США в войну.</li>
            <li><strong>День Д (1944):</strong> высадка союзников в Нормандии, которая стала поворотным моментом войны в Европе.</li>
            <li><strong>Хиросима и Нагасаки (1945):</strong> атомные бомбардировки японских городов, что способствовало окончанию войны.</li>
        </ul>

        <h2>Последствия войны:</h2>
        <ul>
            <li><b>Огромные человеческие потери: около 70-85 миллионов человек погибли.</li>
            <li><b>Разрушение экономики и инфраструктуры многих стран.</li>
            <li><b>Создание Организации Объединенных Наций для предотвращения будущих конфликтов.</li>
            <li><b>Холодная война: разделение мира на два лагеря — капиталистический и социалистический.</li>
            <li><b>Деколонизация: многие колонии получили независимость после войны.</li>
        </ul>

        <h2>Наследие Второй Мировой Войны:</h2>
        <p><b>Вторая Мировая Война оказала глубокое влияние на международные отношения и мировую политику. Она оставила множество уроков о необходимости сотрудничества между странами для поддержания мира и стабильности. Память о жертвах войны и ее последствиях продолжает оставаться важной частью исторической памяти человечества.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Вторая Мировая Война')
        
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/ger_pol.webp'))
        self.first_label.setText('Немецкая атака на Польшу')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/perl.webp'))
        self.second_label.setText('Атака на Перл-Харбор')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/england_fight.webp'))
        self.fourth_label.setText('Битва за Англию')

    def open_next_lesson(self):
        self.first_lesson_window = ModernWorldFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = TwentyCenturyFirstLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = TwentyCentury()
        self.back.show()
        self.hide()


class TwentyCenturyFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        formatted_text = """
        <h1>Первая Мировая Война (1914-1918)</h1>
        
        <h2>Общие сведения:</h2>
        <p>Первая Мировая Война — глобальный конфликт, который охватил большую часть Европы и затронул многие страны мира. Война началась 28 июля 1914 года и закончилась 11 ноября 1918 года.</p>
        
        <h2>Причины войны:</h2>
        <ul>
            <li><strong>Национализм:</strong> рост национальных чувств и стремление стран к расширению влияния.</li>
            <li><strong>Империализм:</strong> конкуренция между великими державами за колонии и ресурсы.</li>
            <li><strong>Военные альянсы:</strong> создание союзов (Тройственный союз и Антанта), которые увеличили вероятность конфликта.</li>
            <li><strong>События в Сараево:</strong> убийство австрийского наследника Франца Фердинанда стало спусковым крючком для войны.</li>
        </ul>
        
        <h2>Основные участники:</h2>
        <ol>
            <li><strong>Союзники:</strong> Великобритания, Франция, Россия, Италия (с 1915 года), США (с 1917 года).</li>
            <li><strong>Центральные державы:</strong> Германия, Австро-Венгрия, Османская империя, Болгария.</li>
        </ol>

        <h2>Ключевые события:</h2>
        <ul>
            <li><strong>Битва при Марне (1914):</strong> остановила немецкое наступление на Париж.</li>
            <li><strong>Галлиполи (1915):</strong> неудачная операция союзников по захвату проливов.</li>
            <li><strong>Битва на Сомме (1916):</strong> одна из самых кровопролитных битв войны.</li>
            <li><strong>Вступление США (1917):</strong> помощь союзникам и изменение хода войны.</li>
            <li><strong>Подписание Компьенского перемирия (1918):</strong> окончание боевых действий.</li>
        </ul>

        <h2>Последствия войны:</h2>
        <ul>
            <li><b>Огромные человеческие потери: около 10 миллионов солдат и 7 миллионов гражданских лиц погибли.</li>
            <li><b>Политические изменения: падение империй (Австро-Венгерской, Российской, Османской).</li>
            <li><b>Создание Лиги Наций как попытка предотвратить будущие войны.</li>
            <li><b>Экономические последствия: разрушение экономики многих стран и гиперинфляция в Германии.</li>
            <li><b>Социальные изменения: рост движения за права женщин и рабочие права.</li>
        </ul>

        <h2>Наследие Первой Мировой Войны:</h2>
        <p><b>Первая Мировая Война оказала глубокое влияние на мировую историю, став предвестником Второй Мировой Войны и изменив политическую карту мира. Она оставила множество уроков о жестокости войны и необходимости международного сотрудничества для поддержания мира.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Первая Мировая Война')
        
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/marna.webp'))
        self.first_label.setText('Битва близ реки Марны')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/somma.webp'))
        self.second_label.setText('Битва близ реки Соммы')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/peaceful_meeting.webp'))
        self.fourth_label.setText('Компьерский договор')

        self.third_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/gal.webp'))
        self.third_label.setText('Галлипольская операция')
    
    def open_next_lesson(self):
        self.first_lesson_window = TwentyCenturySecondLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = NewEraFirstLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = TwentyCentury()
        self.back.show()
        self.hide()


class NewEraFirstLesson(Lesson):
    def __init__(self):
        super().__init__()

        formatted_text = """
        <h1>Просвещение и его идеи (Новое время)</h1>
        
        <h2>Определение:</h2>
        <p>Просвещение — это культурное и интеллектуальное движение XVIII века, которое акцентировало внимание на разуме, науке и индивидуализме, противопоставляя их традиционным авторитетам.</p>
        
        <h2>Основные идеи Просвещения:</h2>
        <ul>
            <li><strong>Разум:</strong> вера в способность человеческого разума решать проблемы и улучшать общество.</li>
            <li><strong>Наука:</strong> акцент на научном методе и рациональном подходе к познанию мира.</li>
            <li><strong>Либерализм:</strong> идеи свободы, равенства и прав человека.</li>
            <li><strong>Секуляризм:</strong> отделение церкви от государства и уменьшение влияния религии на общественную жизнь.</li>
            <li><strong>Образование:</strong> доступ к знаниям и образование как средство улучшения жизни людей.</li>
        </ul>
        
        <h2>Ключевые фигуры Просвещения:</h2>
        <ol>
            <li><strong>Вольтер:</strong> критика религиозного фанатизма и защита гражданских прав.</li>
            <li><strong>Жан-Жак Руссо:</strong> идеи о социальной справедливости и естественном праве.</li>
            <li><strong>Дени Дидро:</strong> редактор "Энциклопедии", пропагандировавший знания и светские идеи.</li>
            <li><strong>Иммануил Кант:</strong> философия, подчеркивающая важность разума и автономии индивидов.</li>
        </ol>

        <h2>Влияние Просвещения:</h2>
        <ul>
            <li>Формирование современных демократических институтов и концепций прав человека.</li>
            <li>Влияние на революции: Американская и Французская революции были во многом вдохновлены идеями Просвещения.</li>
            <li>Развитие науки и образования, что привело к индустриальной революции.</li>
            <li>Создание новых философских течений, таких как гуманизм и утопический социализм.</li>
        </ul>

        <h2>Наследие Просвещения:</h2>
        <p>Идеи Просвещения продолжают оказывать влияние на современное общество, формируя основы демократии, прав человека и научного подхода к жизни. Оно стало основой для дальнейших социальных и политических изменений в мире.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Просвещение и его идеи')
    
    def open_next_lesson(self):
        self.first_lesson_window = TwentyCenturyFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = RevivalSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = NewEra()
        self.back.show()
        self.hide()


class RevivalSecondLesson(Lesson):
    def __init__(self):
        super().__init__()

        formatted_text = """
        <h1>Начало колонизации и глобализации в эпоху Возрождения</h1>
        
        <h2>Причины колонизации:</h2>
        <ul>
            <li><strong>Экономические интересы:</strong> поиск новых торговых путей и ресурсов.</li>
            <li><strong>Политическая конкуренция:</strong> стремление европейских держав расширить свои территории.</li>
            <li><strong>Технологические достижения:</strong> развитие навигации и мореплавания.</li>
        </ul>
        
        <h2>Ключевые события:</h2>
        <ol>
            <li><strong>Путешествия Христофора Колумба (1492):</strong> открытие Америки для Европы.</li>
            <li><strong>Экспедиции Васко да Гамы (1498):</strong> открытие морского пути в Индию.</li>
            <li><strong>Конкиста:</strong> завоевание испанцами территорий в Латинской Америке.</li>
        </ol>
        
        <h2>Влияние на мир:</h2>
        <ul>
            <li><b>Создание колоний и изменение местной культуры и экономики.</li>
            <li><b>Распространение европейских языков, религий и обычаев.</li>
            <li><b>Начало глобальной торговли: обмен товарами, идеями и технологиями между континентами.</li>
        </ul>

        <h2>Социальные и культурные последствия:</h2>
        <ul>
            <li><b>Увеличение миграции населения между Европой и колониями.</li>
            <li><b>Смешение культур и появление новых этнических групп.</li>
            <li><b>Появление новых форм искусства, литературы и науки под влиянием различных культур.</li>
        </ul>

        <p><b>Эпоха Возрождения стала отправной точкой для глобализации, которая кардинально изменила мир, создав новые связи между различными регионами.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Появление колонизации и глобализации')

        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/columb.webp'))
        self.first_label.setText('Христофор Колумб в Америке')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/vasko.webp'))
        self.second_label.setText('Васко Да Гама в Индии')
    
    def open_next_lesson(self):
        self.first_lesson_window = NewEraFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.second_lesson_window = RevivalFirstLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.back = RevivalEra()
        self.back.show()
        self.hide()




class RevivalFirstLesson(Lesson):
    def __init__(self):
        super().__init__() 
        
        formatted_text = """
        <h1>Реформация: основные факты</h1>
        
        <h2>Причины:</h2>
        <ul>
            <li><strong>Коррупция в церкви:</strong> продажа индульгенций и моральная деградация духовенства.</li>
            <li><strong>Возрождение интереса к античной культуре:</strong> гуманизм и новые идеи о человеке.</li>
            <li><strong>Технологические изменения:</strong> изобретение печатного пресса и распространение идей.</li>
        </ul>
        
        <h2>Основные события:</h2>
        <ol>
            <li><strong>95 тезисов Мартина Лютера (1517):</strong> критика индульгенций и призыв к реформам.</li>
            <li><strong>Создание протестантских церквей:</strong> Лютеранство, Кальвинизм и другие направления.</li>
            <li><strong>Тридентский собор (1545-1563):</strong> ответ католической церкви на реформаторские движения.</li>
        </ol>
        
        <h2>Влияние на религию:</h2>
        <ul>
            <li><b>Разделение христианской церкви на католическую и протестантские направления.</li>
            <li><b>Увеличение религиозной терпимости и разнообразия вероисповеданий.</li>
            <li><b>Упрощение церковных обрядов и акцент на личной вере.</li>
        </ul>

        <h2>Влияние на общество:</h2>
        <ul>
            <li><b>Рост грамотности благодаря переводу Библии на национальные языки.</li>
            <li><b>Изменение отношения к власти и правлению: идеи о праве народа на сопротивление.</li>
            <li><b>Укрепление индивидуализма и развитие новых социальных движений.</li>
        </ul>

        <p><b>Реформация стала важным этапом в истории Европы, оказавшим значительное влияние на религию, культуру и общественные структуры.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Реформация')
    
    def open_next_lesson(self):
        self.next_lesson_window = RevivalSecondLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = MiddleAgesSecondLesson()
        self.previous_lesson_window.show()
        self.hide() 
    
    def return_back(self):
        self.return_window = RevivalEra()
        self.return_window.show()
        self.hide()


class MiddleAgesFirstLesson(Lesson):
    def __init__(self):
        super().__init__()
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/scheme.webp'))
        self.first_label.setText('Схема феодальной иерархии')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/knight.jpg'))
        self.fourth_label.setText('Иллюстрация рыцаря')

        self.third_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/crestiane_life.webp'))
        self.third_label.setText('Сцена из жизни крестьян')

        self.second_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/feodal_zamok.webp'))
        self.second_label.setText('Средневековый замок')

        self.heading_label.setText('Феодализм в Европе')

        formatted_text = """
        <p style="color: black; font-size: 15px;">
            <b>Феодализм</b> — <i>это социально-экономическая система, существовавшая в Европе с IX по XV века, основанная на отношениях между землевладельцами и зависимыми крестьянами.<i></p> 
            
            <p><b>В центре системы находился король, который раздавал земли вассалам в обмен на военную службу. Лорды управляли своими землями и обеспечивали защиту подданным, а крестьяне работали на их земле, получая защиту и небольшой участок для себя.
            Общество было четко структурировано: дворянство включало рыцарей, а крестьяне делились на свободных и зависимых. Экономика основывалась на аграрном производстве, а культура характеризовалась развитием рыцарской культуры и христианства.</p>
            
            <p><b>Феодализм оказал значительное влияние на политическую структуру и способствовал образованию децентрализованных властей.
            С ростом городов и торговли в позднем Средневековье феодализм начал ослабевать, что привело к значительным изменениям в обществе. 
            </p>
        """

        self.main_text.setHtml(formatted_text)
    
    def open_next_lesson(self):
        self.next_lesson_window = MiddleAgesSecondLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = AncientThirdLesson()
        self.previous_lesson_window.show()
        self.hide() 

    def return_back(self):
        self.middle_ages_window = Middle_Ages()
        self.middle_ages_window.show()
        self.hide() 


class MiddleAgesSecondLesson(Lesson):
    def __init__(self):
        super().__init__()
        
        formated_text = """
        <h1>Крестовые походы: основные факты</h1>
        
        <h2>Причины:</h2>
        <ul>
            <li><strong>Религиозные:</strong> возвращение контроля над Иерусалимом.</li>
            <li><strong>Политические:</strong> укрепление власти королей и нобилитета.</li>
            <li><strong>Экономические:</strong> поиск новых торговых путей.</li>
        </ul>
        
        <h2>Основные события:</h2>
        <ol>
            <li><strong>Первый крестовый поход (1096-1099):</strong> успешное завоевание Иерусалима.</li>
            <li><strong>Третий крестовый поход (1189-1192):</strong> попытка вернуть Иерусалим, завершившаяся неудачей.</li>
            <li><strong>Четвертый крестовый поход (1202-1204):</strong> захват Константинополя вместо Иерусалима.</li>
        </ol>
        
        <h2>Последствия:</h2>
        <ol>
            <li><b>Углубление конфликта между христианами и мусульманами.</li>
            <li><b>Увеличение влияния церкви и рост рыцарских орденов.</li>
            <li><b>Развитие торговли между Востоком и Западом.</li>
            <li><b>Укрепление королевской власти.</li>
        </ol>

        <p><b>Эти ключевые моменты дают общее представление о крестовых походах и их значении.</b></p>
        """
        self.main_text.setHtml(formated_text)
        self.heading_label.setText('Крестовые походы и их последствия')
        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/krest_pohod.webp'))
        self.first_label.setText('Битва близ Иерусалима')
        
        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/taking_of_jerusalem.webp'))
        self.fourth_label.setText('Взятие Иерусалима')
    
    def return_back(self):
        self.ancient_times = Middle_Ages()
        self.ancient_times.show()
        self.hide()
    
    def open_next_lesson(self):
        self.next_lesson_window = RevivalFirstLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = MiddleAgesFirstLesson()
        self.previous_lesson_window.show()
        self.hide() 


class QuizResult(QMainWindow, Ui_QuizResult):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_button.clicked.connect(self.open_menu)
        self.restart_button.clicked.connect(self.restart_quiz)

        self.result_label.setText(f'{CORRECT_ANSWERS} из {AMOUNT_OF_QUESTIONS} баллов')

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
        

            
    def open_menu(self):
        global QUESTION_NUMBER
        global CORRECT_ANSWERS

        QUESTION_NUMBER = 1
        CORRECT_ANSWERS = 0

        self.menu_window = MainMenu()
        self.menu_window.show()
        self.hide()
    
    def restart_quiz(self):
        global QUESTION_NUMBER
        global CORRECT_ANSWERS

        self.new_quiz_window = QuizInroduction()
        self.new_quiz_window.show()
        self.hide()
        
        QUESTION_NUMBER = 1
        CORRECT_ANSWERS = 0

class QuizQuestion(QMainWindow, Ui_QuizQuestion):
    def __init__(self):
        global QUESTION_NUMBER
        global USED_LINES

        super().__init__()
        self.setupUi(self)
        self.end_button.clicked.connect(self.end_quiz)
        self.next_question_button.clicked.connect(self.open_next_question)

        self.valid_lines = [line for line in CSV_DATA if line[1] == LEVEL and line not in USED_LINES]
        self.random_line = random.choice(self.valid_lines)
        self.question, self.difficulty = self.random_line[0], self.random_line[1]
        self.first_variant = self.random_line[2]
        self.second_variant = self.random_line[3]
        self.third_variant = self.random_line[4]
        self.fourth_variant = self.random_line[5]
        self.answer = self.random_line[6]

        self.question_number_label.setText(f'Вопрос №{QUESTION_NUMBER}')
        QUESTION_NUMBER += 1
        
        self.question_label.setText(self.question)
        self.first_variant_button.setText(self.first_variant)
        self.second_variant_button.setText(self.second_variant)
        self.third_variant_button.setText(self.third_variant)
        self.fourth_variant_button.setText(self.fourth_variant)

        self.first_variant_button.clicked.connect(self.check_answer)
        self.second_variant_button.clicked.connect(self.check_answer)
        self.third_variant_button.clicked.connect(self.check_answer)
        self.fourth_variant_button.clicked.connect(self.check_answer)

        self.buttons = [self.first_variant_button, self.second_variant_button,
                        self.third_variant_button, self.fourth_variant_button]
        
        USED_LINES.append(self.random_line)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

            
    def check_answer(self):
        global CORRECT_ANSWERS

        given_answer = self.sender().text()

        if given_answer == self.answer:
            self.sender().setStyleSheet('background-color: green;')
            CORRECT_ANSWERS += 1
            
        else:
            self.sender().setStyleSheet('background-color: red;')

        for button in self.buttons:
            if button is not self.sender():
                button.setEnabled(False)

    def end_quiz(self):
        global QUESTION_NUMBER
        global CORRECT_ANSWERS

        QUESTION_NUMBER = 1
        CORRECT_ANSWERS = 0
        
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.hide()

    def open_next_question(self):
        if AMOUNT_OF_QUESTIONS >= QUESTION_NUMBER:
            self.next_question_window = QuizQuestion()
            self.next_question_window.show()
            self.hide()
        else:
            self.quiz_result_window = QuizResult()
            self.quiz_result_window.show()
            self.hide()


class AncientThirdLesson(Lesson):
    def __init__(self):
        super().__init__()
        
        formatted_text = """
        <h1>Религиозные и философские учения древней эпохи</h1>

        <h2>Общие сведения:</h2>
        <p>Древние религии и философские учения оказали огромное влияние на развитие человеческой мысли и культуры. Они формировали мировосприятие людей, их моральные ценности и социальные структуры.</p>

        <h2>Религиозные учения:</h2>
        <ul>
            <li><strong>Древний Египет:</strong> Религия была политеистической, с богами, такими как Ра, Осирис и Исис. Верования в загробную жизнь играли важную роль.</li>
            <li><strong>Древняя Месопотамия:</strong> Сумерки и аккадцы поклонялись множеству богов, таких как Мардук и Инанна. Религия была тесно связана с сельским хозяйством и природными явлениями.</li>
            <li><strong>Индуизм:</strong> Возник в Индии, включает в себя множество божеств и концепций, таких как карма и реинкарнация.</li>
            <li><strong>Буддизм:</strong> Основан Siddhartha Gautama (Буддой) в VI веке до н.э., учит о пути к просветлению и освобождению от страданий.</li>
            <li><strong>Зороастризм:</strong> Основан Зороастром в Персии, акцентирует внимание на борьбе между добром (Ахура Мазда) и злом (Ангра Майнью).</li>
        </ul>

        <h2>Философские учения:</h2>
        <ul>
            <li><strong>Древнегреческая философия:</strong> Началась с натурфилософов, таких как Фалес и Гераклит. Позже развивалась через Сократа, Платона и Аристотеля.</li>
            <li><strong>Конфуцианство:</strong> Основано Конфуцием в Китае, акцентирует внимание на морали, социальной гармонии и уважении к предкам.</li>
            <li><strong>Даосизм:</strong> Также возник в Китае, основан на учениях Лао-цзы. Пропагандирует гармонию с природой и следование Дао (путь).</li>
            <li><strong>Стоицизм:</strong> Развивался в Древней Греции и Риме, акцентирует внимание на внутреннем спокойствии и разумном принятии судьбы.</li>
            <li><strong>Эпикуреизм:</strong> Учение Эпикура, которое рассматривает счастье как высшую цель жизни, достигаемую через удовольствие и отсутствие страданий.</li>
        </ul>

        <h2>Влияние на современность:</h2>
        <p>Религиозные и философские учения древности продолжают оказывать значительное влияние на современные религии, этические системы и философские размышления. Они формируют основы мировоззрения миллионов людей по всему миру.</p>

        <h2>Заключение:</h2>
        <p>Изучение религиозных и философских учений древней эпохи позволяет лучше понять корни современных культурных и этических норм. Эти учения стали основой для многих традиций и верований, которые сохраняются до сих пор.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Религиозные и философские учения')
    
    def return_back(self):
        self.ancient_times_window = Ancient_World()
        self.ancient_times_window.show()
        self.hide()
    
    def open_next_lesson(self):
        self.next_lesson_window = MiddleAgesFirstLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = AncientSecondLesson()
        self.previous_lesson_window.show()
        self.hide()

class AncientSecondLesson(Lesson):
    def __init__(self):
        super().__init__()
        
        formatted_text = """
        <h1>Античная Греция и Рим</h1>

        <h2>Общие сведения:</h2>
        <p><b>Античная Греция и Рим стали основой западной цивилизации. Эти две культуры оказали значительное влияние на философию, искусство, науку и политические системы.</p>

        <h2>Античная Греция:</h2>
        <ul>
            <li><strong>География:</strong> Греция состояла из множества городов-государств (полисов), таких как Афины, Спарта и Коринф.</li>
            <li><strong>Философия:</strong> Философы, такие как Сократ, Платон и Аристотель, заложили основы западной философии.</li>
            <li><strong>Искусство:</strong> Греческое искусство известно своими скульптурами, архитектурой (например, Парфенон) и театром.</li>
            <li><strong>Демократия:</strong> Афины стали родиной демократии, где граждане имели право участвовать в управлении государством.</li>
        </ul>

        <h2>Древний Рим:</h2>
        <ul>
            <li><strong>География:</strong> Римская империя охватывала обширные территории от Британии до Ближнего Востока.</li>
            <li><strong>Право:</strong> Римское право стало основой современных правовых систем.</li>
            <li><strong>Архитектура:</strong> Римляне известны своими инженерными достижениями, такими как акведуки, дороги и Колизей.</li>
            <li><strong>Культура:</strong> Римская культура впитала много элементов греческой культуры, включая мифологию и искусство.</li>
        </ul>

        <h2>Влияние на современный мир:</h2>
        <p>Идеи античной Греции и Рима продолжают оказывать влияние на современную политику, право, искусство и философию. Концепции демократии, права человека и гражданских свобод имеют свои корни в этих древних цивилизациях.</p>

        <h2>Ключевые достижения:</h2>
        <ul>
            <li><strong>Философия и наука:</strong> Развитие логики, математики и естественных наук.</li>
            <li><strong>Литература:</strong> Произведения Гомера, Вергилия и других авторов остаются классикой мировой литературы.</li>
            <li><strong>Спорт:</strong> Олимпийские игры были учреждены в Древней Греции и продолжаются до сих пор.</li>
            <li><strong>Инженерия:</strong> Разработка новых технологий в строительстве и архитектуре.</li>
        </ul>

        <h2>Заключение:</h2>
        <p><b>Античная Греция и Рим стали краеугольными камнями западной цивилизации. Их достижения в различных областях продолжают вдохновлять человечество на протяжении веков.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Античная Греция и Рим')

        self.first_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/coleseum.webp'))
        self.first_label.setText('Римский Колизей')

        self.fourth_photo.setPixmap(QPixmap('data/lessons_photo/ancient_world/parphenon.webp'))
        self.fourth_label.setText('Древнегреческий Парфенон')
    
    def return_back(self):
        self.ancient_times_window = Ancient_World()
        self.ancient_times_window.show()
        self.hide()
    
    def open_next_lesson(self):
        self.next_lesson_window = AncientThirdLesson()
        self.next_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = AncientFirstLesson()
        self.previous_lesson_window.show()
        self.hide()



class AncientFirstLesson(Lesson):
    def __init__(self):
        super().__init__()
        
        formatted_text = """
        <h1>Появление цивилизаций</h1>

        <h2>Общие сведения:</h2>
        <p>Цивилизации — это сложные социальные структуры, которые характеризуются развитием городов, письменности, экономики и культуры. Появление цивилизаций стало ключевым моментом в истории человечества, ознаменовав переход от кочевого образа жизни к оседлому.</p>

        <h2>Исторические этапы появления цивилизаций:</h2>
        <ul>
            <li><strong>Неолитическая революция:</strong> около 10 000 лет до н.э. люди начали заниматься земледелием и скотоводством, что позволило им оседать на одном месте.</li>
            <li><strong>Первые города:</strong> с развитием сельского хозяйства появились первые города в Месопотамии, Египте, Индии и Китае.</li>
            <li><strong>Письменность:</strong> возникновение письменности (около 3500 года до н.э.) стало важным шагом для управления и передачи знаний.</li>
            <li><strong>Государства и империи:</strong> формирование первых государств и империй, таких как Шумер, Древний Египет и Хараппа.</li>
        </ul>

        <h2>Ключевые цивилизации:</h2>
        <ul>
            <li><strong>Шумерская цивилизация:</strong> одна из первых известных цивилизаций, возникшая в Месопотамии, известная своими городами-государствами.</li>
            <li><strong>Древний Египет:</strong> известен своими пирамидами, фараонами и развитой религией.</li>
            <li><strong>Индская цивилизация:</strong> развивалась вдоль реки Инд и известна своей городской планировкой и системой водоснабжения.</li>
            <li><strong>Древний Китай:</strong> одна из древнейших цивилизаций, известная своей философией, изобретениями и культурным наследием.</li>
            <li><strong>Майя и Ацтеки:</strong> высокоразвитые цивилизации в Центральной Америке с уникальными системами письменности и астрономии.</li>
        </ul>

        <h2>Влияние на современное общество:</h2>
        <p>Цивилизации заложили основы для развития современных государств, культур и экономик. Их достижения в области науки, искусства и технологий продолжают оказывать влияние на современное общество.</p>

        <h2>Проблемы и вызовы:</h2>
        <ul>
            <li><strong>Экологические проблемы:</strong> развитие цивилизаций часто приводило к истощению природных ресурсов и экологическим кризисам.</li>
            <li><strong>Социальное неравенство:</strong> рост богатства и власти у элитных классов часто сопровождался угнетением других слоев населения.</li>
            <li><strong>Конфликты:</strong> конкуренция за ресурсы и территорию приводила к войнам и конфликтам между цивилизациями.</li>
        </ul>

        <h2>Заключение:</h2>
        <p>Появление цивилизаций стало важным этапом в истории человечества, определившим развитие культуры, экономики и общества. Изучение этих процессов помогает нам лучше понять современный мир и его вызовы.</p>
        """

        self.main_text.setHtml(formatted_text)
        self.heading_label.setText('Появление цивилизаций')
    
    def open_next_lesson(self):
        self.first_lesson_window = AncientSecondLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_previous_lesson(self):
        self.previous_lesson_window = ModernWorldFirstLesson()
        self.previous_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Ancient_World()
        self.lessons.show()
        self.hide()


class Middle_Ages(QMainWindow, Ui_MiddleAges):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

            
    def open_first_lesson(self):
        self.first_lesson_window = MiddleAgesFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = MiddleAgesSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class Ancient_World(QMainWindow, Ui_AncientWorld):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.third_lesson.clicked.connect(self.open_third_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = AncientFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = AncientSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def open_third_lesson(self):
        self.third_lesson_window = AncientThirdLesson()
        self.third_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class RevivalEra(QMainWindow, Ui_RevivalEra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.second_lesson.clicked.connect(self.open_first_lesson)
        self.third_lesson.clicked.connect(self.open_second_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = RevivalFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = RevivalSecondLesson()
        self.second_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class NewEra(QMainWindow, Ui_NewEra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = NewEraFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class TwentyCentury(QMainWindow, Ui_TwentyCentury):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.first_lesson.clicked.connect(self.open_first_lesson)
        self.second_lesson.clicked.connect(self.open_second_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
    def open_first_lesson(self):
        self.first_lesson_window = TwentyCenturyFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def open_second_lesson(self):
        self.second_lesson_window = TwentyCenturySecondLesson()
        self.second_lesson_window.show()
        self.hide()

    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class ModernWorld(QMainWindow, Ui_ModernWorld):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.third_lesson.clicked.connect(self.open_first_lesson)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

    def open_first_lesson(self):
        self.first_lesson_window = ModernWorldFirstLesson()
        self.first_lesson_window.show()
        self.hide()
    
    def return_back(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class Lessons(QMainWindow, Ui_Lessons):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.return_button.clicked.connect(self.return_back)
        self.lessons_button.clicked.connect(self.open_lesson)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

    def open_lesson(self):
        item_text = self.epochesbox.currentText()

        if item_text == 'Древний мир (до 500г н.э)':
            self.ancient_world_lesson = Ancient_World()
            self.ancient_world_lesson.show()
            self.hide()
        
        elif item_text == 'Средневековье (500-1500гг)':
            self.middle_ages_lesson = Middle_Ages()
            self.middle_ages_lesson.show()
            self.hide()
        
        elif item_text == 'Эпоха Возрождения и Реформации (1500-1700гг)':
            self.revival_era_lesson = RevivalEra()
            self.revival_era_lesson.show()
            self.hide()

        elif item_text == 'Новое время (1700-1900гг)':
            self.new_era_lesson = NewEra()
            self.new_era_lesson.show()
            self.hide()

        elif item_text == 'XX век (1900-2000гг)':
            self.twenty_century_lesson = TwentyCentury()
            self.twenty_century_lesson.show()
            self.hide()
        
        elif item_text == 'Современный мир (2000г - настоящее время)':
            self.modern_world_lesson = ModernWorld()
            self.modern_world_lesson.show()
            self.hide()
    
    def return_back(self):
        self.book = Book()
        self.book.show()
        self.hide()


class Calendar(QMainWindow, Ui_Calendar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.return_button.setIcon(QIcon('data/icons/return.svg'))
        self.calendar.clicked.connect(self.show_event)
        self.return_button.clicked.connect(self.return_back) 
        self.format = QTextCharFormat()
        self.format.setBackground(QColor("red"))

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

        
        for event_date in EVENTS.keys():
            self.date = QtCore.QDate.fromString(event_date, 'yyyy-MM-dd')
            self.calendar.setDateTextFormat(self.date, self.format)
    
    def show_event(self):
        self.result.clear()
        selected_date = self.calendar.selectedDate()
        event = EVENTS.get(selected_date.toString('yyyy-MM-dd'), 'Информация об этой дате отсутствует.')
        self.result.insertPlainText(event)
    
    def return_back(self):
        self.book = Book()
        self.book.show()
        self.hide()


class QuizInroduction(QMainWindow, Ui_QuizIntroduction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.next_button.clicked.connect(self.next_window)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
        
            
    def next_window(self):
        global AMOUNT_OF_QUESTIONS
        global LEVEL

        AMOUNT_OF_QUESTIONS = int(self.amount_of_questions.text())
        LEVEL = self.chosen_level.currentText()

        self.quiz_question = QuizQuestion()
        self.quiz_question.show()
        self.hide()

    def return_back(self):
        self.new_menu = MainMenu()
        self.new_menu.show()
        self.hide()

class Book(QMainWindow, Ui_Book):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.return_page)
        self.calendar_button.clicked.connect(self.open_calendar)
        self.lesson_button.clicked.connect(self.open_lessons)
        
        self.back_button.setIcon(QIcon('data/icons/return.svg'))

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

            
    def return_page(self):
        self.menu = MainMenu()
        self.menu.show()
        self.hide()

    def open_calendar(self):
        self.new_calendar = Calendar()
        self.new_calendar.show()
        self.hide()
    
    def open_lessons(self):
        self.lessons = Lessons()
        self.lessons.show()
        self.hide()


class Settings(QMainWindow, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.save_changes_button.clicked.connect(self.update_changes)
        self.return_button.clicked.connect(self.return_back)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')
            
    def update_changes(self):
        global THEME

        if self.theme_choose.currentText() == 'Темная':
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Подтверждение изменений')
            msg_box.setText('Вы хотите применить изменения?')

            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            msg_box.button(QMessageBox.StandardButton.Yes).setText('Да')
            msg_box.button(QMessageBox.StandardButton.No).setText('Нет')

            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Yes:
                THEME = 'dark'
                self.setStyleSheet('background-color: #151719;')
                self.theme_choose.setCurrentIndex(1)

                for widget in self.widgets:
                    widget.setStyleSheet('color: white;')
            else:
                ...
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Подтверждение изменений')
            msg_box.setText('Вы хотите применить изменения?')

            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            msg_box.button(QMessageBox.StandardButton.Yes).setText('Да')
            msg_box.button(QMessageBox.StandardButton.No).setText('Нет')

            result = msg_box.exec()

            if result == QMessageBox.StandardButton.Yes:
                self.theme_choose.setCurrentIndex(0)
                self.setStyleSheet('background-color: #ffe4b5;')
                THEME = 'light'
                
                for widget in self.widgets:
                    widget.setStyleSheet('color: black;')
            
            else:
                ...

    def return_back(self):
        self.menu_window = MainMenu()
        self.menu_window.show()
        self.hide()


class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.quiz_button.setIcon(QIcon('data/icons/quiz.svg'))
        self.help_button.setIcon(QIcon('data/icons/help.svg'))
        self.settings_button.setIcon(QIcon('data/icons/settings.svg'))
        self.book_button.setIcon(QIcon('data/icons/book.svg'))

        self.book_button.clicked.connect(self.open_book)
        self.quiz_button.clicked.connect(self.open_quiz)
        self.settings_button.clicked.connect(self.open_settings)

        if THEME == 'dark':
            self.setStyleSheet('background-color: #151719;')

            for widget in self.widgets:
                widget.setStyleSheet('color: white;')
        else:
            self.setStyleSheet('background-color: #ffe4b5;')

            
    def open_quiz(self):
        self.quiz_introduction = QuizInroduction()
        self.quiz_introduction.show()
        self.hide()

    def open_book(self):
        self.book = Book()
        self.book.show()
        self.hide()
    
    def open_settings(self):
        self.settings_window = Settings()
        self.settings_window.show()
        self.hide()