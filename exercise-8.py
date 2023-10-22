import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='dbuser',
         password='pass_word',
         autocommit=True
         )
#8.1
def get_airport_from_ident(ident):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    database_result = cursor.fetchall()
    return database_result

#8.2
def get_airport_from_area(code):
    sql = f"SELECT name FROM airport WHERE iso_country = '{code}' ORDER BY type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
#8.3
def get_coordination(ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ident}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    database_result = cursor.fetchall()
    return database_result[0]

def calculate_distance(ident_1, ident_2):
    airport_1_coordination = get_coordination(ident_1)
    airport_2_coordination = get_coordination(ident_2)

    airport_1_name = get_airport_from_ident(ident_1)[0][0]
    airport_2_name = get_airport_from_ident(ident_2)[0][0]

    distance_between_airports = distance.distance(airport_1_coordination, airport_2_coordination).km
    print(f"Distance from {airport_1_name} to {airport_2_name} is {distance_between_airports} kilometers")

calculate_distance("1GA7","JP-2932")