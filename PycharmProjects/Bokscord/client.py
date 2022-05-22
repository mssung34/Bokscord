from re import I
import sys
import socket
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication

BUF_SIZE = 1024

IP = 'defult'
Name = 'defult'
Port = 0
sock = 0


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("login.ui", self)

        self.start.clicked.connect(self.take_text)
        self.name.returnPressed.connect(self.take_text)

    def input(self):
        self.IP_ADR = QTextEdit()
        self.name = QTextEdit()
        self.Set_Port = QTextEdit()

    def take_text(self):
        global IP, Name, Port, sock
        IP = self.IP_ADR.text()
        Name = self.name.text()
        Port = self.Set_Port.text()
        Port = (int(Port))

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, Port))
        sock.send(Name.encode())

        chat_window2 = WindowClass()
        chat_window2.exec_()
        QCoreApplication.instance().quit


class SocketClient(QThread):
    rcv_msg = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.is_run = False

    def connect(self):
        self.is_run = True

    def run(self):
        while True:
            r_msg = sock.recv(BUF_SIZE)
            r_msg = (r_msg.decode())
            if len(r_msg) >= 1:
                self.rcv_msg.emit(r_msg)


class credit(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("credit.ui", self)


class WindowClass(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chat_ui.ui", self)
        self.sock = SocketClient(self)
        self.sock.start(1)

        self.sock.rcv_msg.connect(self.recv_msg)
        self.Text_Butten.clicked.connect(self.send_msg)
        self.credit_Btn.clicked.connect(self.goto_credit)
        self.Clear_Btn.clicked.connect(self.clear_msg)
        self.Exit_Btn.clicked.connect(self.exit)
        self.Main_Btn.clicked.connect(self.goto_main)
        self.Room1_Btn.clicked.connect(self.goto_room1)
        self.Room2_Btn.clicked.connect(self.goto_room2)
        self.Room3_Btn.clicked.connect(self.goto_room3)

    def clear_msg(self):
        self.Show_Chat.clear()

    def goto_main(self):
        sock.send('!0'.encode())
        self.Main_Btn.setStyleSheet(
            "border-radius:20px;"
            "background-color:#fff;"
            "color:#5865f2;"      
        )
        self.Room1_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room2_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room3_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )

    def goto_room1(self):
        sock.send('!1'.encode())
        self.Main_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room1_Btn.setStyleSheet(
            "border-radius:20px;"
            "background-color:#fff;"
            "color:#5865f2;"
        )
        self.Room2_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room3_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )

    def goto_room2(self):
        sock.send('!2'.encode())
        self.Main_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room2_Btn.setStyleSheet(
            "border-radius:20px;"
            "background-color:#fff;"
            "color:#5865f2;"
        )
        self.Room1_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room3_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )

    def goto_room3(self):
        sock.send('!3'.encode())
        self.Main_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room3_Btn.setStyleSheet(
            "border-radius:20px;"
            "background-color:#fff;"
            "color:#5865f2;"
        )
        self.Room1_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )
        self.Room2_Btn.setStyleSheet(
            """
            QPushButton{
            border-radius:25px;
            background-color:#5865f2;
            color:#fff;
            }

            QPushButton:hover{
            border-radius:20px;
            background-color:#fff;
            color:#5865f2;
            }
            """
        )

    def exit(self):
        exit(0)

    def goto_credit(self):
        chat_window3 = credit()
        chat_window3.exec_()

    def send_msg(self):
        msg = self.msg_Edit.text()
        sock.send(msg.encode())
        self.msg_Edit.clear()

    def input_msg(self):
        self.msg_Edit = QTextEdit(self)
        self.msg_Edit.returnPressed.connect(self.send_msg)

    @pyqtSlot(str)
    def recv_msg(self, r_msg):
        if 'U_reset' in r_msg:
            self.Show_name.clear()
            r_msg = r_msg.replace('U_reset\n', '')
        if 'T_reset' in r_msg:
            self.Show_Chat.clear()
            r_msg = r_msg.replace('T_reset', '')
        if r_msg.startswith('@'):
            r_msg = r_msg.replace('@', '')
            self.Show_name.append(r_msg)
        else:
            self.Show_Chat.append(r_msg)

    def closeEvent(self, QCloseEvent):
        self.deleteLater()
        QCloseEvent.accept()
        exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = Login()
    chat_window.show()
    app.exec_()
