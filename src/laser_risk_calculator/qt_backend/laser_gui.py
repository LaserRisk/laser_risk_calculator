from dataclasses import fields

from qtpy.QtWidgets import QMainWindow

from pymodaq_gui.utils.custom_app import CustomApp
from pymodaq_gui.utils.utils import mkQApp
from pymodaq_gui.utils.dock import DockArea, Dock

from ..calculator.laser import Laser, LaserType


class LaserGui(CustomApp):

    params = [
        {'title': 'Name:', 'name': 'name', 'type': 'str', 'value': '',
         'tip': 'The name of your laser'},
        {'title': 'Laser Type:', 'name': 'laser_type', 'type': 'list', 'values': LaserType.names(),
         'value': LaserType.names()[0], 'tip': 'The type of your laser'},
        {'title': 'Pulse Duration:', 'name': 'pulse_duration', 'type': 'str', 'value': '',
         'tip': 'The duration of your laser in the string form: "100 fs"', 'visible': False},
        {'title': 'Wavelength:', 'name': 'wavelength', 'type': 'str', 'value': '',
         'tip': 'The wavelength of your laser in the string form: "515 nm"'},
    ]

    def __init__(self, dockarea):

        super().__init__(dockarea)

        # init the object parameters
        self.setup_ui()

    def setup_docks(self):
        dock_laser = Dock('Laser Settings')
        self.dockarea.addDock(dock_laser)

        dock_laser.addWidget(self.settings_tree)



def main():
    import sys
    app = mkQApp('Laser Risk')

    mainwindow = QMainWindow()
    mainwindow.setWindowTitle('laser Risk Calculator')
    dockarea = DockArea()
    mainwindow.setCentralWidget(dockarea)

    prog = LaserGui(dockarea)
    mainwindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
