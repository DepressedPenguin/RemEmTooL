#!/usr/bin/python

# RemEmTool By Dpressed Penguin
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QPlainTextEdit, QLineEdit, QWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt

def remremWindow():
    app = QApplication(sys.argv)
    w = QWidget()
    # SET WINDOW_SIZE
    w.setGeometry(200,40,340,150)
    # SET WINDOW TITLE
    w.setWindowTitle("RemEmTool By Dp-Penguin")
    # SETICONWINDOW
    w.setWindowIcon(QIcon("icon"))
    # STYLE_WINDOW WITH .CSS
    w.setStyleSheet("background-color:#191919;")

    # MAKE LINE TO SPLIT THE WINDOW BTW REM AND EM
    Split_Line = QLabel(w)
    Split_Line.setStyleSheet("background-color:white;")
    Split_Line.setGeometry(167,0,3,150)
    Split_Line.show()

    # FUNCTION TO COUNT REM
    def count_rem():
        default_font = 16

        rem_wanted = PX_INPUT.text()

        px_value = float(rem_wanted)
        result = px_value / default_font
        REM_INPUT.setText(f"{result:.2f}rem")

    # MAKE INPUT FOR THE PX UNIT
    PX_INPUT = QLineEdit(w)
    PX_INPUT.setGeometry(10,10,145,40)
    PX_INPUT.setStyleSheet("""
        border:1px solid white;
        border-radius:5px;
        text-align: center;
        color:white;
        font-size:20px;
        """)
    PX_INPUT.setPlaceholderText("PX ?")
    PX_INPUT.show()

    # MAKE THE BTN THAT WILL CAPTURED THE CLICK CONVERT
    BTN_CONVERT_TO_REM = QPushButton(w)
    BTN_CONVERT_TO_REM.setText("COVERT")
    BTN_CONVERT_TO_REM.setStyleSheet("background-color:white;font-family:Courier")
    BTN_CONVERT_TO_REM.move(45,65)
    BTN_CONVERT_TO_REM.show()

    # MAKE INPUT FOR RESULT "REM VALUE"
    REM_INPUT = QLineEdit(w)
    REM_INPUT.setGeometry(10,105,145,40)
    REM_INPUT.setStyleSheet("""
        border:1px solid white;
        border-radius:5px;
        text-align: center;
        color:white;
        font-size:20px;
        """)
    REM_INPUT.setPlaceholderText("REM = ")
    REM_INPUT.show()

    # CLICK REM
    BTN_CONVERT_TO_REM.clicked.connect(count_rem)

    # CLICK EM
    def count_em():
        default_font = 14

        em_wanted = PX_2_INPUT.text()

        px_value = float(em_wanted)
        result = px_value / default_font
        EM_INPUT.setText(f"{result:.2f}em")

    # MAKE INPUT FOR THE PX UNIT
    PX_2_INPUT = QLineEdit(w)
    PX_2_INPUT.setGeometry(185,10,145,40)
    PX_2_INPUT.setStyleSheet("""
        border:1px solid white;
        border-radius:5px;
        text-align: center;
        color:white;
        font-size:20px;
        """)
    PX_2_INPUT.setPlaceholderText("PX ?")
    PX_2_INPUT.show()

    # MAKE THE BTN THAT WILL CAPTURED THE CLICK CONVERT
    BTN_CONVERT_TO_EM = QPushButton(w)
    BTN_CONVERT_TO_EM.setText("COVERT")
    BTN_CONVERT_TO_EM.setStyleSheet("background-color:white;font-family:Courier")
    BTN_CONVERT_TO_EM.move(220,65)
    BTN_CONVERT_TO_EM.show()

    # MAKE INPUT FOR RESULT "REM VALUE"
    EM_INPUT = QLineEdit(w)
    EM_INPUT.setGeometry(185,105,145,40)
    EM_INPUT.setStyleSheet("""
        border:1px solid white;
        border-radius:5px;
        text-align: center;
        color:white;
        font-size:20px;
        """)
    EM_INPUT.setPlaceholderText("EM = ")
    EM_INPUT.show()

    # CLICK EM
    BTN_CONVERT_TO_EM.clicked.connect(count_em)

    w.show()
    sys.exit(app.exec())

remremWindow()
