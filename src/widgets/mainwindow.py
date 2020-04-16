from   .expose           import property_from_main_window
from   .expose           import property_from_widget
from   .expose           import read_only_from_widget
from   .images.icon      import create_icon
from   .stylesheet       import stylesheet
from   .ui_mainwindow    import Ui_MainWindow
from   PySide2.QtWidgets import QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # window style
        self.setWindowIcon(create_icon())
        self.setStyleSheet(stylesheet)

        # defaults
        self.ip_address = 'localhost'
        self.id_string  = None

        self.enable_inputs()
        self.emphasize_ip_address()

    # properties
    window_title = property_from_main_window('windowTitle')

    # ip address properties
    ip_address         = property_from_widget ('ipAddress', 'text')
    ip_address_enabled = property_from_widget ('ipAddress', 'enabled')

    # ip address methods
    select_ip_address  = read_only_from_widget('ipAddress', 'selectAll')
    focus_ip_address   = read_only_from_widget('ipAddress', 'setFocus')

    # id string
    id_string = property_from_widget('idString', 'text')

    # button properties
    button_text    = property_from_widget('button', 'text')
    button_enabled = property_from_widget('button', 'enabled')

    # button signals
    button_clicked = read_only_from_widget('button', 'clicked')

    # methods

    def enable_inputs(self):
        self.ip_address_enabled = True
        self.button_enabled     = True

    def disable_inputs(self):
        self.ip_address_enabled = False
        self.button_enabled     = False

    def emphasize_ip_address(self):
        self.select_ip_address()
        self.focus_ip_address()

    def show_error(self, message):
        QMessageBox.warning(self, 'Error', message)
