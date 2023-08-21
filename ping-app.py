from PyQt5.QtWidgets import*
import sys
import socket

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: lightpink")
        self.setWindowTitle("Ali's Ping App")
        self.components()
        self.show()
    def components(self):
        self.labelname=QLabel("Please input web site name",self)
        self.output=QLineEdit(self)
        self.okey=QPushButton("Okey",self)
        self.space1=QLabel("  ",self)
        self.space2=QLabel("  ",self)
        self.space3=QLabel("  ",self)

        v_box=QVBoxLayout()
        h_box=QHBoxLayout()
        v_box.addWidget(self.labelname)
        v_box.addWidget(self.output)
        v_box.addStretch()
        v_box.addWidget(self.space1)
        v_box.addWidget(self.space2)
        v_box.addWidget(self.space3)

        v_box.addWidget(self.okey)
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.okey.clicked.connect(self.ping)

    def ping(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.space1.setText("Socket successfully created")
        except socket.error as err:
            self.space1.setText(f"Socket creation failed with error {err}")
            return

        port = 80

        try:
            host_ip = socket.gethostbyname(self.output.text())
        except socket.gaierror:
            self.space2.setText("Error resolving the host")
            return

        try:
            s.connect((host_ip, port))
            self.space2.setText(f"Socket has successfully connected to website, IP: {host_ip}, Port: {port}")
        except socket.error as err:
            self.space3.setText(f"Socket connection failed with error {err}")
            return
        finally:
            s.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Window()
    sys.exit(app.exec_())