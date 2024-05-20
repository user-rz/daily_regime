import sqlite3

class Activity():

    def __init__(self, name, day, month, start_hour, start_minute, end_hour, end_minute):
        self.name = name
        self.day = day
        self.month = month
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute

    def write_in_db(self):
        conn = sqlite3.connect('regime.db')

        cursor = conn.cursor()
        cursor.execute('INSERT INTO ' + self.name + ' (day, month, start_hour, start_minute, end_hour, end_minute)'
                       + ' VALUES (' + str(self.day) + ', "' + self.month +
                       '", ' + str(self.start_hour) + ', ' + str(self.start_minute) +
                       ', ' + str(self.end_hour) + ', ' + str(self.end_minute) + ')')

        conn.commit()
        conn.close()
