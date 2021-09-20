import sys
from PyQt5 import QtWidgets
import mainwindow
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtDesigner import *
from PyQt5.QtGui import *
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OWO")
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = None
        self.setGeometry(0, 0, 300, 300)
        self.setWindowOpacity(.9)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("no title")
        self.palette = self.palette()
        self.setPalette(self.palette)
        self.setStyleSheet('background-color: black;')
        self.penis = QPixmap('cum.png')
        self.setWindowTitle("MEEPS PICTURES:")
        #
        self.infoDump = QPlainTextEdit("<3")
        self.infoDump.setReadOnly(True)
        self.infoDump.setFixedHeight(200)
        self.infoDump.setStyleSheet('background-color: lightBlue; color: black;')
        self.infoDump.setFont(QFont('Arial', 9.5))
        #
        self.getinfo = QPushButton("Info:")
        self.getinfo.pressed.connect(self.geninfo)
        self.getinfo.setStyleSheet('background-color: cyan; color: black;')
        #
        self.sayHewwo = "Hello, "
        self.userGreet = os.environ['USER']
        self.formatTopBar = self.userGreet.title()
        self.top = self.sayHewwo + self.formatTopBar
        self.topBar = QLabel(self.top)
        self.topBar.setFont(QFont('Arial', 20))
        self.topBar.setFixedHeight(40)
        self.topBar.setStyleSheet('background-color: cyan; color: black')
        self.topBar.setAlignment(Qt.AlignCenter)
        ##
        self.clickMe = QPushButton("Dogs")
        self.clickMe.setStyleSheet('background-color: cyan; color: black;')
        self.clickMe.clicked.connect(self.firstboi)
        #
        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(10, 10, 200, 200)
        #bottom QtWidgets

        self.startStuff = QPushButton()
        self.startStuff.setIcon(QIcon("firefox.png"))
        self.startStuff.setIconSize(QSize(30,30))
        self.startStuff.setFixedSize(QSize(30,30))
        self.startStuff.pressed.connect(self.firefox)


        self.kritaopen = QPushButton()
        self.kritaopen.setIcon(QIcon("krita.png"))
        self.kritaopen.setIconSize(QSize(30,30))
        self.kritaopen.setFixedSize(QSize(30,30))
        self.kritaopen.pressed.connect(self.krita)


        self.konsoleopen = QPushButton()
        self.konsoleopen.setIcon(QIcon("konsole.png"))
        self.konsoleopen.setIconSize(QSize(30,30))
        self.konsoleopen.setFixedSize(QSize(30,30))
        self.konsoleopen.pressed.connect(self.konsole)

        self.dolphinopen = QPushButton()
        self.dolphinopen.setIcon(QIcon("dolphin.png"))
        self.dolphinopen.setIconSize(QSize(30,30))
        self.dolphinopen.setFixedSize(QSize(30,30))
        self.dolphinopen.pressed.connect(self.dolphin)


        self.kdevelop = QPushButton()
        self.kdevelop.setIcon(QIcon("kdevelop.png"))
        self.kdevelop.setIconSize(QSize(30,30))
        self.kdevelop.setFixedSize(QSize(30,30))
        self.kdevelop.pressed.connect(self.kdev)

        self.kateopen = QPushButton()
        self.kateopen.setIcon(QIcon("kate.png"))
        self.kateopen.setIconSize(QSize(30,30))
        self.kateopen.setFixedSize(QSize(30,30))
        self.kateopen.pressed.connect(self.kate)

        ##
        layout2 = QHBoxLayout()
        layout2.addWidget(self.startStuff)
        layout2.addWidget(self.kritaopen)
        layout2.addWidget(self.konsoleopen)
        layout2.addWidget(self.dolphinopen)
        layout2.addWidget(self.kdevelop)
        layout2.addWidget(self.kateopen)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.topBar)
        layout.addWidget(self.calendar)
        layout.addWidget(self.getinfo)
        layout.addWidget(self.infoDump)
        layout.addWidget(self.clickMe)
        layout.addLayout(layout2)

        self.bottompenis = QPixmap('cum.png')
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    def message(self, s):
        self.infoDump.appendPlainText(s)
    def geninfo(self):
        self.general = QProcess(self)
        self.general.readyReadStandardOutput.connect(self.done)
        self.general.start('bash', ["geninfo.sh"])
        self.general.finished.connect(self.done)
    def done(self):
        infoload = self.general.readAllStandardOutput()
        info = bytes(infoload).decode("utf8")
        self.message(info)
    def firefox(self):
        self.p = QProcess(self)
        self.p.start('bash', ["firefoxboi.sh"])
    def krita(self):
        self.p = QProcess(self)
        self.p.start('bash', ["krita.sh"])
    def konsole(self):
        self.p = QProcess(self)
        self.p.start('bash', ["konsole.sh"])
    def dolphin(self):
        self.p = QProcess(self)
        self.p.start('bash', ["dolphin.sh"])
    def kdev(self):
        self.p = QProcess(self)
        self.p.start('bash', ["kdevelop.sh"])
    def kate(self):
        self.p = QProcess(self)
        self.p.start('bash', ["kate.sh"])

    def firstboi(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()

        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
my_mainWindow = MainWindow()
my_mainWindow.show()
sys.exit(app.exec_())
