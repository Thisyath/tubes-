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
        self.addWidget(self.page1)  # index 0: Welcome
        self.addWidget(self.page2)  # index 1: Register / Sign In
        self.addWidget(self.page3)  # index 2: Log In

        # --- PAGE 1 (WELCOME) BUTTONS ---
        # Pastikan objectName di .ui sama, misal: btnRegister → ke register, btnLogin → ke login
        self.page1.btnRegister.clicked.connect(self.goto_register)
        self.page1.btnLogin.clicked.connect(self.goto_login)

        # --- PAGE 2 (REGISTER) ---
        self.page2.btnSignIn.clicked.connect(self.register_action)
        self.page2.btnTeacher.clicked.connect(lambda: self.select_role("teacher"))
        self.page2.btnStudent.clicked.connect(lambda: self.select_role("student"))
        self.page2.linkLogin.mousePressEvent = lambda event: self.goto_login()

        # --- PAGE 3 (LOGIN) ---
        self.page3.btnLogin.clicked.connect(self.login_action)

        self.setWindowTitle("Learn Up App")
        self.setCurrentIndex(0)

        # Role selection state for registration
        self.selected_role = None

    def goto_register(self):
        self.setCurrentIndex(1)

    def goto_login(self):
        self.setCurrentIndex(2)

    def select_role(self, role):
        self.selected_role = role
        # Optional: visual feedback for selected role (highlight, etc.)

    def register_action(self):
        username = self.page2.lineUsername.text()
        email = self.page2.lineEmail.text()
        password = self.page2.linePassword.text()
        confirm = self.page2.lineConfirmPassword.text()
        role = self.selected_role

        if not username or not email or not password or not confirm or not role:
            QMessageBox.warning(self, "Register Gagal", "Semua field dan role harus diisi!")
            return
        if password != confirm:
            QMessageBox.warning(self, "Register Gagal", "Password dan konfirmasi tidak sama!")
            return

        try:
            conn = sqlite3.connect(DB_FILENAME)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO User (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            user_id = cur.lastrowid
            # Masukkan ke tabel Student/Teacher jika perlu
            if role == "student":
                cur.execute("INSERT INTO Student (user_id) VALUES (?)", (user_id,))
            elif role == "teacher":
                cur.execute("INSERT INTO Teacher (user_id) VALUES (?)", (user_id,))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Register Berhasil", "Registrasi berhasil, silakan login!")
            self.setCurrentIndex(2)
        except sqlite3.IntegrityError as e:
            if "username" in str(e):
                QMessageBox.warning(self, "Register Gagal", "Username sudah terdaftar!")
            elif "email" in str(e):
                QMessageBox.warning(self, "Register Gagal", "Email sudah terdaftar!")
            else:
                QMessageBox.warning(self, "Register Gagal", "Gagal mendaftar, silakan coba lagi.")

    def login_action(self):
        username = self.page3.lineUsername.text()
        password = self.page3.linePassword.text()
        if not username or not password:
            QMessageBox.warning(self, "Login Gagal", "Username dan password harus diisi!")
            return

        conn = sqlite3.connect(DB_FILENAME)
        cur = conn.cursor()
        cur.execute(
            "SELECT user_id, username FROM User WHERE username=? AND password=?",
            (username, password)
        )
        user = cur.fetchone()
        conn.close()
        if user:
            QMessageBox.information(self, "Login Berhasil", f"Selamat datang, {username}!")
            # TODO: Lanjutkan ke halaman utama aplikasi
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(960, 640)
    window.show()
    sys.exit(app.exec_())