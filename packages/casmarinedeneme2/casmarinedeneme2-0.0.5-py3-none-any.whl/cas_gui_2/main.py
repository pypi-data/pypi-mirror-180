from PyQt5.QtWidgets import QApplication
#from functions import Interface
from cas_gui_2.functions import Interface

app = QApplication([])
window = Interface()
window.show()
app.exec_()