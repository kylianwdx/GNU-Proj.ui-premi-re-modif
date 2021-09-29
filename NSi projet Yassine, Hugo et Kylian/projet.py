import sys
import csv
from PyQt5 import QtWidgets
from proj import Ui_MainWindow

class MaFenetre(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.datafile = "exhibits.csv"
        self.data = None
        self.connecteSignaux()
        self.montreData()
        return

    def connecteSignaux(self):
        self.actionQuitter.triggered.connect(self.close)
        self.action_propos.triggered.connect(self.montreAide)
        self.pushButton.clicked.connect(self.montreData)
        return
    
    def montreAide(self):
        with open("aide.html") as aide:
            html = aide.read()
        self.textEdit.setText(html)
        return
    
    def montreData(self):
        if not self.data:
            self.data = []
            with open(self.datafile) as csvfile:
                lecteur = csv.reader(csvfile)
                for ligne in lecteur:
                    self.data.append(ligne)
        html = "<table style='background: grey;'>"
        html += "<tr style='background: lightgrey;'><th>" + "</th><th>".join(self.data[0])+"</th></tr>"
        for ligne in self.data[1:]:
            html += "<tr style='background: lightyellow;'><td>" + "</td><td>".join(ligne)+"</td></tr>"
        html += "</table>"
        self.textEdit.setText(html)
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    f = MaFenetre()
    f.show()
    sys.exit( app.exec_() )
