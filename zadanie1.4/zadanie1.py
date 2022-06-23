import sys
from random import random

from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QToolBar, QStatusBar, QGridLayout, QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(250, 250))

        self.setWindowTitle('Sort')

        layout = QGridLayout()

        self.input = QLineEdit()
        self.label1 = QLabel('wpisz liczby po przecinku')
        self.label = QLabel('')

        toolBar = QToolBar('Toolbar')
        toolBar.setIconSize(QSize(16, 16))
        self.addToolBar(toolBar)

        bSort = QAction(QIcon('bug--plus.png'), '&BSort', self)
        bSort.setStatusTip('sortowanie babelkowe')
        bSort.triggered.connect(self.sortowanieBabelkowe)
        toolBar.addAction(bSort)
        bSort.setCheckable(True)
        bSort.setShortcut(QKeySequence('Ctrl+g'))

        toolBar.addSeparator()

        sSort = QAction(QIcon('burn--pencil.png'), '&SSort', self)
        sSort.setStatusTip('sortowanie sort()')
        sSort.triggered.connect(self.sortowanieSort)
        toolBar.addAction(sSort)
        sSort.setCheckable(True)
        sSort.setShortcut(QKeySequence('Ctrl+h'))

        toolBar.addSeparator()

        iSort = QAction(QIcon('cassette--pencil.png'), '&ISort', self)
        iSort.setStatusTip('insertion sort')
        iSort.triggered.connect(self.cos)
        toolBar.addAction(iSort)
        iSort.setCheckable(True)
        iSort.setShortcut(QKeySequence('Ctrl+j'))

        toolBar.addSeparator()

        #pasek stanu
        self.setStatusBar(QStatusBar(self))

        # menu
        menu = self.menuBar()

        sortMenu = menu.addMenu('Sortowanie')
        sortMenu.addAction(bSort)
        sortMenu.addSeparator()

        sortMenu.addAction(sSort)
        sortMenu.addSeparator()

        sortMenu.addAction(iSort)
        sortMenu.addSeparator()

        # G R I D
        layout.addWidget(self.label1)
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def toolBarButtonClick(self, s):
        print('clicked', s)
        print(self.input.text())

    def sortowanieBabelkowe(self):
        input = self.input.text()
        lst = input.split(',')
        print(lst)
        try:
            n = len(lst)
            while n > 1:
                zamien = False
                for l in range(0, n - 1):
                    if int(lst[l]) > int(lst[l + 1]):
                        lst[l], lst[l + 1] = lst[l + 1], lst[l]
                        zamien = True

                n -= 1
                if zamien == False: break

            return self.label.setText(str(lst))
        except:
            self.label.setText('cos poszlo nie tak')



    def sortowanieSort(self):
        input = self.input.text()
        lst = input.split(',')
        try:
            n = [int(numeric_string) for numeric_string in lst]
            n.sort()
            self.label.setText(str(n))
            return str(n)
        except :
            self.label.setText('cos poszlo nie tak')

    def insertionSort(self, nums):
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            # And keep a reference of the index of the previous element
            j = i - 1
            # Move all items of the sorted segment forward if they are larger than
            # the item to insert
            while j >= 0 and int(nums[j]) > int(item_to_insert):
                nums[j + 1] = nums[j]
                j -= 1
            # Insert the item
            nums[j + 1] = item_to_insert

    def cos(self):
        hm = self.input.text()
        n = hm.split(',')
        try:
            self.insertionSort(n)
            self.label.setText(str(n))
        except:
            self.label.setText('cos poszlo nie tak')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()