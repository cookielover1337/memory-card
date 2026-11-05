from PyQt5.QtCore import Qt
from random import *
from time import *
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QButtonGroup, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,200)
v_line = QVBoxLayout()
time_line = QHBoxLayout()
button = QPushButton('Ответить')
box = QGroupBox('Варианты ответов')
title_blabla = QLabel('...')
warning_time = QLabel('Вопрос на время!')
time_left = QLabel('s')
boxmain_line = QHBoxLayout()
BOX_line = QVBoxLayout()
BOXTWO_line = QVBoxLayout()
variant_one = QRadioButton('...')
variant_two = QRadioButton('...')
variant_three = QRadioButton('...')
variant_four = QRadioButton('...')
main_win.right_ask_int = 0
main_win.ask_int= 0
answbox = QGroupBox('Результат теста')
ans = QLabel('Правильно/Неправильно')
corr_answ = QLabel('тоже надпись')
result_line = QVBoxLayout()
result_line.addWidget(ans, alignment =(Qt.AlignLeft|Qt.AlignTop))
result_line.addWidget(corr_answ, alignment =(Qt.AlignCenter))
answbox.setLayout(result_line)

group = QButtonGroup()

group.addButton(variant_two)
group.addButton(variant_three)
group.addButton(variant_four)
group.addButton(variant_one)
BOX_line.addWidget(variant_one)
BOX_line.addWidget(variant_two)
BOXTWO_line.addWidget(variant_three)
BOXTWO_line.addWidget(variant_four)
boxmain_line.addLayout(BOX_line)
boxmain_line.addLayout(BOXTWO_line)
box.setLayout(boxmain_line)

time_line.addWidget(title_blabla)
time_line.addWidget(warning_time, alignment = (Qt.AlignRight|Qt.AlignTop))
time_line.addWidget(time_left,alignment = (Qt.AlignRight|Qt.AlignTop))
v_line.addLayout(time_line)
time_left.hide()
warning_time.hide()
v_line.addWidget(box)

v_line.addWidget(answbox)
v_line.addWidget(button)
main_win.setLayout(v_line)
spisok = [variant_one,variant_two,variant_three,variant_four]

class Question():
    def __init__(self,question,correct,one,two,three):
        self.question = question
        self.correct = correct
        self.one = one
        self.two = two
        self.three = three
asks = []
asks.append(Question('Выберите несуществующий нутриент','Фосфотид','Белки','Жиры','Углеводы'))
asks.append(Question('Выберите соединение, которое не существует в природе','Сапонид','Глюкозад','Танид','Сквален'))
asks.append(Question('Какой национальности не существует?', 'Смурфы','Алеуты','Чулымцы','Энцы'))
def results():
    box.hide()
    warning_time.hide()
    time_left.hide()
    answbox.show()
    button.setText('Следущий вопрос')
    title_blabla.setText('Самый сложный вопрос в мире!')
def ask():
    
    box.show()
    group.setExclusive(False)
    variant_four.setChecked(False)
    variant_one.setChecked(False)
    variant_three.setChecked(False)
    variant_two.setChecked(False)
    group.setExclusive(True)
    answbox.hide()
    button.setText('Ответить')
    main_win.ask_int+=1
    print('Текущая статистика:')
    print('Кол-во вопросов:',main_win.ask_int)
    print('Всего правильных ответов:',main_win.right_ask_int)
    print('Рейтинг:', main_win.right_ask_int/main_win.ask_int*100)
    if randint(1,5) == 5:
        time_left.show()
        warning_time.show()

def shuff(question):
    shuffle(spisok)
    spisok[0].setText(question.correct)
    spisok[1].setText(question.one)
    spisok[2].setText(question.two)
    spisok[3].setText(question.three)
    title_blabla.setText(question.question)
    corr_answ.setText(question.correct)
    ask()
def next_question():
    currask = randint(0,len(asks)-1)
    shuff(asks[currask])

def ifelseifelse():
    if spisok[0].isChecked():
        ans.setText('Правильно!')
        main_win.right_ask_int+=1
        results()
        print('Обновлённая статистика:')
        print('Кол-во вопросов:',main_win.ask_int)
        print('Всего правильных ответов:',main_win.right_ask_int)
        print('Рейтинг:', main_win.right_ask_int/main_win.ask_int*100)
    elif spisok[1].isChecked() or spisok[2].isChecked() or spisok[3].isChecked():
        ans.setText('Неправильно!')
        results()
        print('Обновлённая статистика:')
        print('Кол-во вопросов:',main_win.ask_int)
        print('Всего правильных ответов:',main_win.right_ask_int)
        print('Рейтинг:', main_win.right_ask_int/main_win.ask_int*100)
def click_OK():
    if button.text()=='Ответить':
       ifelseifelse()
    else:
        next_question()
answbox.hide()
button.clicked.connect(click_OK)
next_question()
main_win.show()
app.exec_()