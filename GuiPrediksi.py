from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QButtonGroup
from PyQt5.uic.properties import QtCore, QtGui

from newGui import Ui_MainWindow
import sys
from news_classification import predict
from classifier.NaiveBayesClassifier import NaiveBayesClassifier


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.input_list_lineInput = []
        self.input_list = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.resultOutput.setReadOnly(True)
        self.output = self.ui.resultOutput.document()
        self.ui.checkButton.clicked.connect(self.add_input_box)
        self.ui.actionquit.triggered.connect(self.close)
        self.ui.deleteButton.clicked.connect(self.delete_input_box)
        self.ui.actionReset.triggered.connect(self.reset_all)
        self.method = 0

        self.lstm = self.ui.lstmRadio
        self.naive = self.ui.naiveRadio

        self.lstm.toggled.connect(self.handleButtonClicked)
        self.naive.toggled.connect(self.handleButtonClicked)


    def handleButtonClicked(self):
        if self.ui.lstmRadio.isChecked():
            selected_value = 'Lstm'
            self.method = 0
            print(self.method)
        else:
            selected_value = 'naive bayes'
            self.method = 1
            print(self.method)
            # Perform any logic based on the selected value
        print(f'Selected value: {selected_value}')

    def add_input_box(self):
        if self.method == 0 :
            input_text = self.ui.inputNewsEdit.toPlainText()
            if input_text == "":
                print("isikan penggalan berita")
                return

            category = predict(input_text)
            self.output.setPlainText("Lstm : "+category)
        else:
            input_text = self.ui.inputNewsEdit.toPlainText()
            if input_text == "":
                print("isikan penggalan berita")
                return
            classifier = NaiveBayesClassifier()
            category = classifier.classifier(input_text)
            self.output.setPlainText("Naive : "+ category['label'])

    def delete_input_box(self):
        self.ui.inputNewsEdit.clear()
        self.resetRadio()

    def resetRadio(self):
        self.lstm.setAutoExclusive(False)
        self.lstm.setChecked(False)
        self.lstm.setAutoExclusive(True)
        self.lstm.setAutoExclusive(False)
        self.naive.setChecked(False)
        self.lstm.setAutoExclusive(True)

    def reset_all(self):
        self.ui.inputNewsEdit.clear()
        self.output.clear()
        self.resetRadio()


    def close(self):
        sys.exit()

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    create_app()