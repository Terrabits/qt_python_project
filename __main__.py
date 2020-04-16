from   src.controller    import Controller
from   src.model         import Model
from   src.widgets       import MainWindow as View
from   PySide2.QtWidgets import QApplication
import sys


def main():
    # required before any widget creation
    app = QApplication(sys.argv)

    # create objects
    model      = Model()
    view       = View()
    controller = Controller(model, view)

    # bring up window
    view.show()

    # Qt event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
