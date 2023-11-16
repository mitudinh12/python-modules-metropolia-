from flask import Flask, request, Response
import json
import mysql.connector


def task_1():
    app = Flask(__name__)

    @app.route('/echo/<text>')
    def echo(text):
        number = int(text)
        answer = isPrime(number)
        response = {
            "Number": text,
            "isPrime": answer
        }
        return response

    def isPrime(number):
        for i in range(2, number + 1):
            if number % i == 0 and i != number:
                return False
        return True

    if __name__ == "__main__":
        app.run(use_reloader=True, host="127.0.0.1", port=3000)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='dbuser',
    password='pass_word',
    autocommit=True
)
def task_2():
    def get_airport(icao_code):  # get airport name and location by ICAO code
        sql = f"SELECT name, municipality FROM airport WHERE ident= '{icao_code}';"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return {
            "ICAO": icao_code,
            "Name": result[0][0],
            "Location": result[0][1]
        }

    app = Flask(__name__)
    @app.route('/airport/<text>')
    def airport(text):
        response = get_airport(text)
        return response

    if __name__ == "__main__":
        app.run(use_reloader=True, host="127.0.0.1", port=3000)
task_2()