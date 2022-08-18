{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "import sys\nimport requests\nimport random\nfrom ui_pruebapyqt5 import *\nfrom PySide2.QtCore import QTimer, QTime\n\nfrom PySide2.QtWidgets import QMenu, QMessageBox\nfrom PySide2.QtCore import Qt, QEvent\n\nclass MiApp(QMainWindow):\n    \n    def __init__(self):\n        super().__init__()\n        self.ui = Ui_MainWindow()\n        self.ui.setupUi(self)\n        \n        \n        timer = QTimer(self)\n        timer.timeout.connect(self.displayTime)\n        timer.start(1000)\n        \n        self.ui.btnConsultar.clicked.connect(self.clicked)\n        self.ui.listWidget.itemClicked.connect(self.itemClicked)\n        \n        \n#    def eventFilter(self, source, event):\n#        if event.type() == QEvent.ContextMenu and source is self.listWidget:\n#            menu =QMenu()\n#            menu.addAction('Informacion del personaje')\n#            if menu.exec_(event.globalPos()):\n#                item = source.itemAt(event.pos())\n#                ##########\n#            return True\n#        \n#        return super().eventFilter(source, event)\n\n    def itemClicked(self):\n        msg =QMessageBox()\n        msg.setWindowTitle(\"Ventana Secundaria\")\n        \n        id = self.numeros[self.ui.listWidget.currentRow()]\n        #print(id)\n        path = 'https://swapi.dev/api/people/' + str(id)\n        r = requests.get(path, timeout=10)\n        j = r.json()\n        datos = 'height: ' + str(j[\"height\"]) + '\\nmass: ' + str(j[\"mass\"]) + '\\nhair_color: ' + str(j[\"hair_color\"]) + '\\nskin_color: ' + str(j[\"skin_color\"]) + '\\neye_color: ' + str(j[\"eye_color\"]) + '\\nbirth_year: ' + str(j[\"birth_year\"]) + '\\ngender: ' + str(j[\"gender\"])\n        msg.setText(datos)\n        #print(str(j[\"name\"]))\n        x = msg.exec()\n        \n        \n    def clicked(self):\n        val = list(range(1, 84))\n        self.numeros = random.sample(val, 10)\n        k = 0;\n        self.ui.listWidget.clear()\n        for i in self.numeros:      \n            path = 'https://swapi.dev/api/people/' + str(i)\n            r = requests.get(path, timeout=10)\n            j = r.json()\n            #print(j[\"name\"])\n            self.ui.listWidget.insertItem(k, str(j[\"name\"]))\n            k = k + 1\n            \n\n    def displayTime(self):\n        currentTime = QTime.currentTime()\n        currentDate = QDate.currentDate()\n        hora = currentTime.toString('hh:mm:ss')\n        fecha = currentDate.toString(Qt.DefaultLocaleShortDate)\n        self.ui.lblHora.setText(hora)\n        self.ui.lblFecha.setText((fecha.upper()))\n        \nif __name__ == \"__main__\":\n     app = QApplication(sys.argv)\n     mi_app = MiApp()\n     mi_app.show()\n     sys.exit(app.exec_()) ",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "3c8faac1"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "28129dac"
    }
  ]
}