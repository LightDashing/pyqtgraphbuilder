from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget
from PySide2.QtCore import Qt
import numpy as np
import pyqtgraph as pg
import sys
from main_menu import Ui_MainWindow
from settings_ui import Ui_Form
from pygraphplot_settings import Settings
from asyncqt import QEventLoop
import asyncio
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import TokenError


class SettingsWindow(QWidget, Ui_Form):

    def __init__(self, parent):
        self.parent = parent
        super(SettingsWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.raise_()
        self.setWindowModality(Qt.ApplicationModal)
        self.save_b.clicked.connect(self.save)
        self.auto_ch.stateChanged.connect(self.uncheck)
        self.reset.clicked.connect(self.reset_setts)
        self.active_edits = True
        self.inputs = [self.xmax, self.xmin, self.ymax, self.ymin, self.step]
        self.data = [self.parent.settings.setts['xMax'], self.parent.settings.setts['xMin'],
                     self.parent.settings.setts['yMax'], self.parent.settings.setts['yMin'],
                     self.parent.settings.setts['step']]
        self.load_setts()

    def load_setts(self):
        for i in range(len(self.inputs)):
            self.inputs[i].setText(str(self.data[i]))
        self.auto_ch.setChecked(self.parent.settings.setts['auto'])

    def reset_setts(self):
        self.parent.settings.reload_settings()
        self.load_setts()

    def uncheck(self):
        if self.active_edits:
            for i in range(len(self.inputs) - 1): self.inputs[i].setEnabled(False)
            self.active_edits = False
        else:
            for i in range(len(self.inputs) - 1): self.inputs[i].setEnabled(True)
            self.active_edits = True

    def save(self):
        if self.auto_ch.isChecked():
            self.parent.settings.setts['auto'] = True
            self.parent.settings.setts['step'] = float(self.step.text())
            self.parent.settings.save_settings()
        else:
            for i in range(len(self.inputs)): self.data[i] = float(self.inputs[i].text())
            self.parent.settings.setts['auto'] = False
            self.parent.settings.save_settings()


class MainWindow(QMainWindow, Ui_MainWindow):
    settings_window: SettingsWindow

    def closeEvent(self, event):
        print(event)
        close = QMessageBox.question(self,
                                     "Выход",
                                     "Вы уверены что хотите выйти?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            self.close()
            sys.exit(0)
        else:
            event.ignore()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = Settings()
        self.graphs = []
        self.add_graph_button.clicked.connect(self.add_graph)
        self.delete_graph_button.clicked.connect(self.del_graph)
        self.settings_b.clicked.connect(self.settings_call)
        self.clear_plot = self.graph_plot.saveState()
        item = self.graph_plot.getPlotItem()
        item.showGrid(x=True, y=True)
        self.plots = []
        self.limit1.setText("0")
        self.limit2.setText("15")
        self.show()

    def create_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def add_graph(self):
        function = self.function_inp.text()
        try:
            f = parse_expr(function)
        except (SyntaxError, TokenError):
            self.create_error(message="Введите функцию!")
            self.function_inp.clear()
            return
        self.graph_list.addItem(function)
        self.graphs.append(function)
        self.function_inp.clear()
        x_, y = [], []
        l1, l2 = int(self.limit1.text()) if self.limit1.text() else 0, int(
            self.limit2.text()) if self.limit2.text() else 10
        step = self.settings.setts['step']
        step = int((l2 - abs(l1)) // step)
        x_ = np.linspace(l1, l2, step)
        x_t = x_
        for j in range(len(x_)):
            x = symbols("x")
            try:
                y.append((float(f.subs(x, x_[j]))))
            except TypeError:
                x_t = np.delete(x_t, j)
                continue
        if len(y) == 0:
            self.graphs.pop(-1)
            self.graph_list.takeItem(self.graph_list.count() - 1)
            self.create_error("Функцию невозможно построить на данном промежутке!")
        pen = pg.mkPen(color=(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
        self.graph_plot.restoreState(self.clear_plot)
        if self.settings.setts['auto']:
            self.graph_plot.setXRange(l1, l2)
            self.graph_plot.setYRange(min(y), max(y))
        else:
            self.graph_plot.setXRange(self.settings.setts['xMin'], self.settings.setts['xMax'])
            self.graph_plot.setYRange(self.settings.setts['yMin'], self.settings.setts['yMax'])
        # self.graph_plot.setAspectLocked(l1, l2)
        plot = self.graph_plot.plot(x_t, y, pen=pen)
        item = self.graph_plot.getPlotItem()
        item.showGrid(x=True, y=True)
        self.plots.append(plot)

    def del_graph(self):
        item = self.graph_list.selectedItems()
        item = self.graph_list.row(item[0])
        self.graph_list.takeItem(item)
        self.graph_plot.removeItem(self.plots[item])
        self.plots.pop(item)

    def settings_call(self):
        self.settings_window = SettingsWindow(self)


app = QApplication()
loop = QEventLoop(app)
asyncio.set_event_loop(loop)
window = MainWindow()
window.show()
loop.run_forever()
