import sqlite3

MAKE_THE_BANDS = 'CREATE TABLE IF NOT EXISTS BANDS(id INTEGER PRIMARY KEY, name TEXT, album TEXT, rating INTEGER);'
def connect():
    return sqlite3.connect("data.db")

INSERT_BAND = "INSERT INTO BANDS(name, album, rating) VALUES(?,?,?);"

GET_ALL_BANDS = 'SELECT * FROM BANDS;'
GET_BANDS_BY_NAME = 'SELECT * FROM BANDS WHERE name = ?;'
GET_BEST_PREP_FOR_BAND= 'SELECT * FROM BANDS WHERE name = ? ORDER BY rating DESC LIMIT 1;'
DEL_ITEM = 'DELETE FROM BANDS WHERE name = ?;'
def createTables(connection):
        with connection:
            connection.execute(MAKE_THE_BANDS)

def addBand(connection, name, album , rating):

    with connection:
        connection.execute(INSERT_BAND,(name,album,rating))

def getAllBands(connection):
    with connection:
       return connection.execute(GET_ALL_BANDS).fetchall()

def getBandsByName(connection, name):
    result = 'undefined'
    try:
        with connection:
            result = connection.execute(GET_BANDS_BY_NAME,(name,)).fetchall()
    except TypeError:
        print('Band not in list')
    else:
        print('Success')
    finally: print(result)
    #I am not 100% sure that lines 33-35 are necessary
    #but the code is working right now so they are here to stay


def getLatestAlbumFromBand(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREP_FOR_BAND, (name,)).fetchone()

def delItem(connection, name):
    with connection:
        connection.execute(DEL_ITEM,(name,))