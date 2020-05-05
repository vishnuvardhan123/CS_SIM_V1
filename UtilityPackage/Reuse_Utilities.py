from PyQt5.QtWidgets import QMessageBox

from moviepy.editor import *
import pygame
from pygame import display
from pygame import *
import webbrowser as wb


class errormsgs():

    def showMessageBox(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def readfile(self, readpath):
        wb.open_new(readpath)


"""
    def videofile(self,filepath):
        pygame.display.set_caption('CS Player')
        clip = VideoFileClip(filepath)
        clip.preview()
        pygame.quit()
"""
