from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
import threading
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(560, 430)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(15, 15, 450, 350)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(15, 380, 450, 35)
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton('Send', self)
        self.button.setGeometry(475, 380, 75, 35)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        user_input = f"<p style='color: #333333'>Me: {user_input}</p>"
        self.chat_area.append(user_input)
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        response = f"<p style='color: #333333; background-color: #E9E9E9'>Bot: {response}</p>"
        self.chat_area.append(response)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())
