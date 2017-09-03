import json
import urllib.request
from datetime import datetime, timedelta
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem
from gui import *
from PyQt5 import QtWidgets


class Worker(QThread):
    list_of_dict_signals = pyqtSignal(list)
    def __init__(self):
        QThread.__init__(self)
        self.running = False
        self.time_sleep = 1

    def setTime(self, val):
        self.time_sleep = val

    def run(self):
        self.running = True
        while self.running:
            info = self.check_info()
            self.list_of_dict_signals.emit(info)
            self.sleep(self.time_sleep * 60)

    def request_info(self, node):
        info = None
        while info is None:
            url = 'https://api.storj.io/contacts/' + node
            try:
                info = urllib.request.urlopen(url, timeout=5)
                data = info.read()
                encoding = info.info().get_content_charset('utf-8')
                info = json.loads(data.decode(encoding))
            except urllib.request.HTTPError as err:
                if err.code == 404:
                    info = {'error': "Invalid ID or isn't register in Storj yet"}
        return info

    def node_status(self, info):
        last_seen = datetime.strptime(info['lastSeen'], "%Y-%m-%dT%H:%M:%S.%fZ")
        now = datetime.utcnow()
        if last_seen + timedelta(minutes=10) < now:
            node_status = 'Offline'
        else:
            node_status = 'Online'
        return node_status

    def check_info(self):
        nodes = open('Nodeslist.txt').read().split("\n")
        info_list = []
        for node in nodes:
            if node != '':
                info = self.request_info(node)
                if 'error' in info:
                    info_list.append(info)
                else:
                    info['status'] = self.node_status(info)
                    info['port'] = str(info['port'])
                    info['responseTime'] = (str(info['responseTime']).split('.'))[0] + ' ms'
                    info['lastSeen'] = (str(datetime.strptime(info['lastSeen'], "%Y-%m-%dT%H:%M:%S.%fZ")).split('.'))[0]
                    info['lastUpdate'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    info_list.append(info)
        return info_list


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myworker = Worker()
        self.myworker.list_of_dict_signals.connect(self.onDataFromThread)
        self.ui.pushButton.clicked.connect(self.on_start)
        self.ui.pushButton_2.clicked.connect(self.on_stop)

    def on_start(self):
        if not self.myworker.isRunning():
            self.myworker.start()
            self.myworker.setTime(self.ui.spinBox.value())

    def on_stop(self):
        self.myworker.running = False
        self.myworker.terminate()
        self.ui.statusbar.showMessage("Update stopped")

    def onDataFromThread(self, info):
        rows = len(info)
        self.ui.tableWidget.setRowCount(rows)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Node ID", "Status", 'Response', "IP", "Port", "Last Seen", "Last Update"])
        for i in range(rows):
            if 'error' in info[i]:
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(info[i]['error']))
            else:
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(info[i]['nodeID']))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(info[i]['status']))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(info[i]['responseTime']))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(info[i]['address']))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(info[i]['port'])))
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(info[i]['lastSeen']))
                self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(info[i]['lastUpdate']))
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.statusbar.showMessage("All nodes udpated")

    def closeEvent(self, event):
        reply = QMessageBox.question(self,'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.hide()
            self.myworker.running = False
            self.myworker.terminate()
            event.accept()
        else:
            event.ignore()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())