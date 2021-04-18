from PyQt5 import QtWidgets, uic
import sys
from spi_utility_raster_ui import Ui_SPIUtilityDialogBase

class spiutility(QtWidgets.QMainWindow):
    def __init__(self):
        super(spiutility, self).__init__()

        self.ui = Ui_SPIUtilityDialogBase()
        self.ui.setupUi(self)
        
app = QtWidgets.QApplication([])

window = spiutility()

window.show()

sys.exit(app.exec())