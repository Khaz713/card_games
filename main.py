import sys

from PyQt6.QtWidgets import QApplication

from layout_main_window import MainWindow



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()






if __name__ == "__main__":
    main()
