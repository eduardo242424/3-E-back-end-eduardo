import sys
import pandas as pd
from PyQt5.QtDesigner import QApplication, Qwidget, 
from PyQt5.QtCore import Qt 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class CadastroAlunos(Qwidget):
    def __init__(self):
        super().__init__()

        self.alunos = []
        self.initUI()

    def initUI(self):