import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMessageBox
from PyQt5 import uic

DB_FILENAME = "database.db"



class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        # Load UI files
        self.page1 = uic.loadUi("ui/page1.ui")
        self.page2 = uic.loadUi("ui/page2.ui")
        self.page3 = uic.loadUi("ui/page3.ui")
        # Add pages to stacked widget
        self.addWidget(self.page1)  # index 0
        self.addWidget(self.page2)  # index 1
        self.addWidget(self.page3)  # index 2

        # Connect buttons for page 1
        self.page1.btnTeacher.clicked.connect(self.goto_login)
        self.page1.btnStudent.clicked.connect(self.goto_login)
        self.page1.btnRegister.clicked.connect(self.goto_register)

        # Connect buttons for page 2 (login)
        self.page2.btnLogin.clicked.connect(self.login_action)

        # Connect buttons for page 3 (register)
        self.page3.btnRegister.clicked.connect(self.register_action)
        self.page3.btnToLogin.clicked.connect(self.goto_login_from_register)

        self.setWindowTitle("Aplikasi Login")
        self.setCurrentIndex(0)

    def goto_login(self):
        self.setCurrentIndex(1)

    def goto_login_from_register(self):
        self.setCurrentIndex(1)

    def goto_register(self):
        self.setCurrentIndex(2)

    def login_action(self):
        username = self.page2.lineUsername.text()
        password = self.page2.linePassword.text()
        if not username or not password:
            QMessageBox.warning(self, "Login Gagal", "Username dan password harus diisi!")
            return

        # Cek ke tabel User
        conn = sqlite3.connect(DB_FILENAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM User WHERE username=? AND password=?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()
        if user:
            QMessageBox.information(self, "Login Berhasil", f"Selamat datang, {username}!")
            # Lanjut ke halaman aplikasi utama jika ada
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah!")

    def register_action(self):
        username = self.page3.lineUsername.text()
        email = self.page3.lineEmail.text()
        password = self.page3.linePassword.text()
        confirmpass = self.page3.lineConfirmPassword.text()
        if not username or not email or not password or not confirmpass:
            QMessageBox.warning(self, "Register Gagal", "Semua field harus diisi!")
            return
        elif password != confirmpass:
            QMessageBox.warning(self, "Register Gagal", "Password dan konfirmasi tidak sama!")
            return

        # Simpan ke tabel User
        try:
            conn = sqlite3.connect(DB_FILENAME)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO User (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Register Berhasil", "Registrasi berhasil, silakan login!")
            self.setCurrentIndex(1)
        except sqlite3.IntegrityError as e:
            if 'username' in str(e):
                QMessageBox.warning(self, "Register Gagal", "Username sudah terdaftar!")
            elif 'email' in str(e):
                QMessageBox.warning(self, "Register Gagal", "Email sudah terdaftar!")
            else:
                QMessageBox.warning(self, "Register Gagal", "Gagal mendaftar, silakan coba lagi.")

if __name__ == "__main__":
    # Pastikan database sudah dibuat oleh kode init_db yang ada di file yang lain
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec_())