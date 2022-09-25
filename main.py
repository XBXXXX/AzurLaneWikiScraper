# -*- coding: utf-8 -*-
import sys
from PySide6 import QtCore, QtWidgets, QtGui
import scraper as scr
from threading import Thread
from ui_myGui import Ui_mainWindow

class ScraperThread(Thread, scr.Scraper):
    def __init__(self, tag):
        Thread.__init__(self)
        scr.Scraper.__init__(self, tag)    
    def run(self) -> None:
        self.scraper_run()   
        print('-> '+ self.tag + ' Processing done.') 
        

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.Signal(str) 
    def write(self, text):
      self.textWritten.emit(str(text))
      loop = QtCore.QEventLoop()
      QtCore.QTimer.singleShot(10, loop.quit)
      loop.exec()
      QtWidgets.QApplication.processEvents()
       
class MyMainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self) -> None:
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        # my_variables
        self.url = 'https://wiki.biligame.com/blhx/'
        self.path = 'C:/Users/YUUHONN/Pictures/碧蓝航线WIKI'
        self.welcomeMessage = '-> 欢迎使用！为避免已下载的图片重复下载，请保持图片保存路径与上次使用时一致。'
        self.exit_path = False
        # my_settings
        with open('style.qss', 'r') as style_file: 
            style = style_file.read()
        self.setStyleSheet(style)
        self.setWindowIcon(QtGui.QIcon('icon/robot.svg'))
        self.pushButton.setIcon(QtGui.QIcon('icon/pause.svg'))
        self.pushButton_2.setIcon(QtGui.QIcon('icon/play.svg'))
        self.pushButton.setIconSize(QtCore.QSize(30,30))
        self.pushButton_2.setIconSize(QtCore.QSize(30,30))
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.lineEdit.setMaxLength(256)
        self.lineEdit_2.setMaxLength(256)
        self.lineEdit.setText(self.path)
        self.lineEdit_2.setText(self.url)
        # slot_connections
        self.pushButton_2.clicked.connect(self.start)
        self.pushButton.clicked.connect(self.stop)
        self.toolButton.clicked.connect(self.select)
        self.pushButton_3.clicked.connect(self.update)
        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)
        print(self.welcomeMessage)
        # 实例
        self.scraper_thread_bg = ScraperThread('bg')
        self.scraper_thread_other = ScraperThread('other')
        
    def outputWritten(self, text):
            cursor = self.textBrowser.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            cursor.insertText(text)
            self.textBrowser.setTextCursor(cursor)
            self.textBrowser.ensureCursorVisible()
    
    # 槽函数
    @QtCore.Slot()
    def start(self):
        if not self.scraper_thread_bg.is_alive():
            self.scraper_thread_bg = ScraperThread('bg')
        if not self.scraper_thread_bg.is_alive():
            self.scraper_thread_other = ScraperThread('other')
        try:
            self.path = self.lineEdit.text()
            self.scraper_thread_bg.set_save_path(self.path)
            self.scraper_thread_other.set_save_path(self.path)
            if self.checkBox.isChecked():
                self.scraper_thread_bg.start()
            if self.checkBox_2.isChecked():
                self.scraper_thread_other.start()
        except Exception as error_message:
            print(error_message)
    # slots         
    @QtCore.Slot()
    def stop(self):
        self.scraper_thread_bg.scraper_stop()
        self.scraper_thread_other.scraper_stop()

    @QtCore.Slot()
    def update(self):
        self.scraper_thread_bg.update()
        self.scraper_thread_other.update()
    
    @QtCore.Slot()
    def select(self):
        save_path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存图片的路径", options= QtWidgets.QFileDialog.Option.ReadOnly) 
        if save_path:
            self.lineEdit.setText(save_path)
           
    @QtCore.Slot()
    def close(self):
        self.scraper_thread_bg.scraper_stop()
        self.scraper_thread_other.scraper_stop()

                
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    mainWindow = MyMainWindow()
    app.aboutToQuit.connect(mainWindow.close)
    mainWindow.show()
    sys.exit(app.exec())