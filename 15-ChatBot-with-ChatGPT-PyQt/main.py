from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(560, 430)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(15, 15, 450, 350)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(15, 380, 450, 35)

        # Add the button
        self.button = QPushButton('Send', self)
        self.button.setGeometry(475, 380, 75, 35)

        self.show()


class Chatbot:
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())
