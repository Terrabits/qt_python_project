from PySide2.QtCore    import QObject, Slot


class Controller(QObject):
    def __init__(self, model, view, parent=None):
        QObject.__init__(self, parent)
        self.model          = model
        self.view           = view
        self.view.button_clicked.connect(self.handle_button_click)

    @Slot()
    def update_view_from_model(self):
        # Update window using current data from model
        pass

    @Slot()
    def handle_button_click(self):
        # clear current display
        self.view.id_string = None

        # prevent user from clicking again
        self.view.disable_inputs()

        # validate user input
        ip_address = self.view.ip_address.strip()
        if not ip_address:
            self.view.show_error('Enter IP address to continue')
            self.view.enable_inputs()
            self.view.emphasize_ip_address()
            return

        # could not connect?
        if not self.model.connect(ip_address):
            self.view.show_error(f'Could not connect to {ip_address}')
            self.view.enable_inputs()
            self.view.emphasize_ip_address()
            return

        # finish interaction with model
        id_string = self.model.id_string
        self.model.disconnect()

        # update gui
        self.view.id_string = id_string
        self.view.enable_inputs()
