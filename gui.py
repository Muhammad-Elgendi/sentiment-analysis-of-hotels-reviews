# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from SentimentAnalyser import SentimentAnalyser
textbox2 = None
textbox =None

def window():
    global textbox2
    global textbox

    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.setGeometry(100,100,400,250)   

    # Create label
    l = QtGui.QLabel(w)
    l.setText("Enter An Hotel Review (In Arabic) :")
    l.move(10,20)

    # Create textbox
    textbox = QtGui.QLineEdit(w)
    textbox.move(20, 50)
    textbox.resize(360,40)

    # Create textbox2
    textbox2 = QtGui.QLineEdit(w)
    textbox2.move(20, 170)
    textbox2.resize(360,40)
    
    # Create button
    b = QtGui.QPushButton(w)
    b.setText("Analyse")
    b.move(20,100)
    b.clicked.connect(analyse)

    # Create button2
    b2 = QtGui.QPushButton(w)
    b2.setText("Train")
    b2.move(290,100)
    b2.clicked.connect(train)

    # Create label2
    l2 = QtGui.QLabel(w)
    l2.setText("Result :")
    l2.move(10,150)


    w.setWindowTitle("Sentiment Analyser")
    w.show()
    sys.exit(app.exec_())

def analyse():
   global textbox2
   global textbox
   review = str(textbox.text().toUtf8())
   analyser = SentimentAnalyser()
   predected_sentiment , probability = analyser.test(review)
   textbox2.setText("Sentiment is "+str(predected_sentiment)+" with probability = "+str(probability))

def train():
   global textbox2
   global textbox
   analyser = SentimentAnalyser()
   analyser.train()
   textbox2.setText("Training Done ^^")
	
if __name__ == '__main__':
   window()