#создай приложение для запоминания информаци
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint
app=QApplication([])
win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(400, 200)
que=QLabel('Какой национальности не существует?')
button=QPushButton('Ответить')
radiogroupBox=QGroupBox('Варианты ответов')

rb1=QRadioButton('Энцы')
rb2=QRadioButton('Чулымцы')
rb3=QRadioButton('Смурфы')
rb4=QRadioButton('Алеуты')
l1=QVBoxLayout()
l2=QVBoxLayout()
l3=QHBoxLayout()
l1.addWidget(rb1)
l1.addWidget(rb2)
l2.addWidget(rb3)
l2.addWidget(rb4)
l3.addLayout(l1)
l3.addLayout(l2)
radiogroupBox.setLayout(l3)
l4=QVBoxLayout()
l4.addWidget(que,alignment=Qt.AlignCenter)
l4.addWidget(radiogroupBox)


ansgroup=QGroupBox('Результат теста')
ans=QLabel('Правельный ответ')
l5=QVBoxLayout()
l5.addWidget(ans)
ansgroup.setLayout(l5)
ansgroup.hide()
l4.addWidget(ansgroup)
l4.addWidget(button, stretch=1)
RadioGroupBox = QButtonGroup() 
RadioGroupBox.addButton(rb1)
RadioGroupBox.addButton(rb2)
RadioGroupBox.addButton(rb3)
RadioGroupBox.addButton(rb4)
win.setLayout(l4)
def show_results():
    radiogroupBox.hide()
    ansgroup.show()
    button.setText('Следуйщий вопрос')
def show_question():
    radiogroupBox.show()
    ansgroup.hide()
    button.setText('Ответить')
    

    RadioGroupBox.setExclusive(False)    
    rb1.setChecked(False)
    rb2.setChecked(False)
    rb3.setChecked(False)
    rb4.setChecked(False)
    RadioGroupBox.setExclusive(True) 
def start_test():
    if button.text() == 'Ответить':
        show_results()
    else:
        show_question()
answers = [rb1, rb2, rb3, rb4]
class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

        
def ask(ques):
    shuffle(answers)
    answers[0].setText(ques.right_answer)
    answers[1].setText(ques.wrong1)
    answers[2].setText(ques.wrong2)
    answers[3].setText(ques.wrong3)
    que.setText(ques.question)
    ans.setText(ques.right_answer)
    radiogroupBox.show()
    ansgroup.hide()
def check_answer():
    if answers[0].isChecked():
        ans.setText('Правильно!')
        win.score += 1
    if answers[0].isChecked():
        ans.setText('Правильно')
    else:
        ans.setText('Неправильно')
    radiogroupBox.hide()
    ansgroup.show()
    button.setText('Следуйщий вопрос')
    print ("Статистика:")
    print ("-Всего вопросов", win.total)
    print ("-Правильных ответов", win.score)
    print ("Рейтинг:", win.score/win.total * 100, "%")
question_list=[]
question_list.append (Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Бразильский', 'Испанский'))
question_list.append(
    Question('Дата основания Москвы',
    "1147",
    "1170",
    "1201" ,
    "1229"
    )
)

question_list.append(
    Question('Что находиться на Северном полюсе',
    "Антарктида",
    "Антарктика",
    "Северная Америка" ,
    "Гренландия"
    )
)

question_list.append(
    Question('Какой футбольной команды не существует?',
    "Барселона",
    "Реал мадрид",
    "ЦСКА" ,
    "Вперёд"
    )
)
question_list.append(
    Question('Какой планеты не существует?',
    "Метеор",
    "Земля",
    "Юпитер" ,
    "Нептун"
    )
)

question_list.append(
    Question('Какой самый короткий месяц?:)',
    "Апрель",
    "Февраль",
    "Август" ,
    "Май"
    )
)

win.cur_question=-1
win.score = 0
win.total = 0
def next_question():
    win.total += 1
    show_question()
    win.cur_question = randint(0, len(question_list) - 1)
    if win.cur_question ==len(question_list):
        win.cur_question=-1
    ask(question_list [win.cur_question])
    button.setText('Ответить')
    print ("Статистика:")
    print ("-Всего вопросов", win.total)
    print ("-Правильных ответов", win.score)
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

next_question()










button.clicked.connect(click_ok)


win.show()
app.exec()