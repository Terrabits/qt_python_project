from pathlib        import Path
from PySide2.QtCore import QByteArray
from PySide2.QtGui  import QIcon, QPixmap


# path
root_path = Path(__file__).parent
filename  = root_path / 'icon.ico'

# read
with filename.open('rb') as f:
    icon_data = f.read()


def create_icon():
    data   = QByteArray(icon_data)
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    return QIcon(pixmap)
