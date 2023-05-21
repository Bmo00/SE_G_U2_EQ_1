import sys
import serial as conecta
from pynput.keyboard import Controller
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Control.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None
        self.controlador = Controller()
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

    # Área de los Slots
    def accion(self):
        try:
            txt_btn = self.btn_accion.text()
            if txt_btn == "CONECTAR":  ##arduino == None
                self.btn_accion.setText("DESCONECTAR")
                puerto = "COM" + self.txt_puerto.text()
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=10)
                self.segundoPlano.start(10)
            elif txt_btn == "DESCONECTAR":
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.arduino.close()
            else:  # RECONECTAR
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                puerto = "COM" + self.txt_puerto.text()
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=10)
                self.segundoPlano.start(10)
        except Exception as error:
            print(error)

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    variable = self.arduino.readline().decode()
                    variable = variable.replace("\r", "")
                    variable = variable.replace("\n", "")
                    variable = variable.replace(" ", "")
                    print(variable)

                    if variable[0] == "1":
                        self.controlador.press("w")
                        self.btnUp.setStyleSheet("background-color: rgb(255, 255, 255); border: 10px; border-radius: 10px;")

                    else:
                        self.controlador.release("w")
                        self.btnUp.setStyleSheet("background-color:rgb(0, 0, 0);  color: white; border: 10px;  border-radius: 10px;")

                        # Arriba
                    if variable[1] == "1":
                        self.controlador.press("s")
                        self.btnDown.setStyleSheet("background-color: rgb(255, 255, 255); border: 10px; border-radius: 10px;")
                    else:
                        self.controlador.release("s")
                        self.btnDown.setStyleSheet("background-color:rgb(0, 0, 0);  color: white; border: 10px;  border-radius: 10px;")
                        # Abajo
                    if variable[2] == "1":
                        self.controlador.press("a")
                        self.btnLeft.setStyleSheet("background-color:rgb(255, 255, 255);  color: white; border: 10px;  border-radius: 10px;")

                    else:
                        self.controlador.release("a")
                        self.btnLeft.setStyleSheet("background-color:rgb(0, 0, 0);  color: white; border: 10px;  border-radius: 10px;")

                        # Izquierda
                    if variable[3] == "1":
                        self.controlador.press("d")
                        self.btnRight.setStyleSheet("background-color:rgb(255, 255, 255);  color: white; border: 10px;  border-radius: 10px;")

                    else:
                        self.controlador.release("d")
                        self.btnRight.setStyleSheet("background-color:rgb(0, 0, 0);  border: 10px;  border-radius: 10px;")

                        # Derecha
                    if variable[4] == "1":
                        self.controlador.press("c")
                        self.btnSelect.setStyleSheet("background-color:rgb(255, 255, 255);  color: white; border: 10px;  border-radius: 10px;")

                    else:
                        self.controlador.release("c")
                        self.btnSelect.setStyleSheet("background-color:rgb(0, 0, 0);  color: white; border: 10px;  border-radius: 10px;")

                        # Select
                    if variable[5] == "1":
                        self.controlador.press("v")
                        self.btnStart.setStyleSheet("background-color:rgb(255, 255, 255);  color: white; border: 10px;  border-radius: 10px;")

                    else:
                        self.controlador.release("v")
                        self.btnStart.setStyleSheet("background-color:rgb(0, 0, 0);  color: white; border: 10px;  border-radius: 10px;")

                        # Start
                    if variable[6] == "1":
                        self.controlador.press("i")
                        self.btnB.setStyleSheet("background-color: rgb(255, 255, 255); border: 10px; border-radius: 25px;")

                    else:
                        self.controlador.release("i")
                        self.btnB.setStyleSheet("background-color:rgb(255, 0, 0);  border: 10px;  border-radius: 25px;")

                        # B
                    if variable[7] == "1":
                        self.controlador.press("o")
                        self.btnA.setStyleSheet("background-color: rgb(255, 255, 255); border: 10px; border-radius: 25px;")

                    else:
                        self.controlador.release("o")
                        self.btnA.setStyleSheet("background-color:rgb(255, 0, 0);  border: 10px;  border-radius: 25px;")

                        # A


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
