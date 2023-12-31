from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                             QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar,
                             QLabel, QMessageBox, QGridLayout, QLineEdit, QPushButton)
from PyQt6.QtGui import QAction, QIcon
import sys
# import sqlite3
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Connection using SQLite Database
# class DatabaseConnection:
#     def __init__(self, database_file='database.db'):
#         self.database_file = database_file
#
#     def connect(self):
#         connection = sqlite3.connect(self.database_file)
#         return connection


# Connection using MySQL Database
class DatabaseConnection:
    def __init__(self):
        self.host = os.getenv('APP14_HOST')
        self.user = os.getenv('APP14_USER')
        self.password = os.getenv('APP14_PASSWORD')
        self.database = os.getenv('APP14_DATABASE')

    def connect(self):
        connection = mysql.connector.connect(host=self.host,
                                             user=self.user,
                                             password=self.password,
                                             database=self.database)
        return connection


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(600, 500)

        file_menu_item = self.menuBar().addMenu('&File')
        edit_menu_item = self.menuBar().addMenu('&Edit')
        help_menu_item = self.menuBar().addMenu('&Help')

        add_student_action = QAction(QIcon('icons/add.png'), 'Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        search_action = QAction(QIcon('icons/search.png'), 'Search', self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Create toolbar and create toolbar elements
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Create status bar and add status bar elements
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton('Edit Record')
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton('Delete Record')
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        content = """
        This app was created as part of the udemy course titled
        'Python Mega Course'
         """
        self.setText(content)


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Get student name from selected row
        index = sms_app.table.currentRow()
        student_name = sms_app.table.item(index, 1).text()

        # Get id from the selected row
        self.student_id = sms_app.table.item(index, 0).text()

        # Add student name widget
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Add combo box of courses
        current_course_name = sms_app.table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(current_course_name)
        layout.addWidget(self.course_name)

        # Add mobile number widget
        current_mobile_number = sms_app.table.item(index, 3).text()
        self.mobile_number = QLineEdit(current_mobile_number)
        self.mobile_number.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile_number)

        # Add a submit button
        button = QPushButton('Update')
        button.clicked.connect(self.update_student)
        layout.addWidget(button)
        self.setLayout(layout)

    def update_student(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        # SQL query for SQLite Database
        # cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
        #                (self.student_name.text(),
        #                 self.course_name.itemText(self.course_name.currentIndex()),
        #                 self.mobile_number.text(),
        #                 self.student_id))

        # SQL query for MySQL Database
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
                       (self.student_name.text(),
                        self.course_name.itemText(self.course_name.currentIndex()),
                        self.mobile_number.text(),
                        self.student_id))

        connection.commit()
        cursor.close()
        connection.close()

        # Refresh the table
        sms_app.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Delete Student Data')

        layout = QGridLayout()
        confirmation = QLabel("Are you sure you want to delete?")
        yes = QPushButton('Yes')
        no = QPushButton('No')

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        # Get the index and student id from the selected row
        index = sms_app.table.currentRow()
        student_id = sms_app.table.item(index, 0).text()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()

        # SQL query for SQLite Database
        # cursor.execute("DELETE from students WHERE id = ?", (student_id, ))

        # SQL query for MySQL Database
        cursor.execute("DELETE from students WHERE id = %s", (student_id, ))

        connection.commit()
        cursor.close()
        connection.close()

        sms_app.load_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle('Success')
        confirmation_widget.setText("The record was deleted!")
        confirmation_widget.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Add combo box of courses
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        # Add mobile number widget
        self.mobile_number = QLineEdit()
        self.mobile_number.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile_number)

        # Add a submit button
        button = QPushButton('Register')
        button.clicked.connect(self.add_student)
        layout.addWidget(button)
        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()

        connection = DatabaseConnection().connect()
        cursor = connection.cursor()

        # SQL query for SQLite Database
        # cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
        #                (name, course, mobile))

        # SQL query for MySQL Database
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)",
                       (name, course, mobile))

        connection.commit()
        cursor.close()
        connection.close()
        sms_app.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('Search Student')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Create layout and input widget
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        # Create button
        button = QPushButton('Search')
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()

        # SQL query for SQLite Database
        # result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))

        # SQL query for MySQL Database
        cursor.execute("SELECT * FROM students WHERE name = %s", (name,))

        result = cursor.fetchall()
        rows = list(result)
        print(rows)
        items = sms_app.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            sms_app.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


app = QApplication(sys.argv)
sms_app = MainWindow()
sms_app.show()
sms_app.load_data()
sys.exit(app.exec())
