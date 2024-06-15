from PyQt5.QtCore import Qt   
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout   

app = QApplication([])   
notes = []   
   
'''Інтерфейс'''   
# Параметри вікна   
notes_win = QWidget()   
notes_win.setWindowTitle('Easy_editor')   
notes_win.resize(900, 600)   

#розмітка
main_layout = QHBoxLayout()
colum_left = QVBoxLayout()
colum_right = QVBoxLayout()
main_layout.addLayout(colum_left)
main_layout.addLayout(colum_right)


folder_btn = QPushButton("Папка")
files_list = QListWidget()
colum_left.addWidget(folder_btn)
colum_left.addWidget(files_list)


picture = QLabel('Картинка')
control_panel = QHBoxLayout()
button_1 = QPushButton("utton 1")
button_2 = QPushButton("Button 2")
button_3 = QPushButton("Button 3")
button_4 = QPushButton("Button 4")



notes_win.show()   

app.exec_()