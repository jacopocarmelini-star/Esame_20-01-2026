from database.DB_connect import DBConnect
from model.artist import Artist
from model.connessioni import Connessioni


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                FROM artist a"""
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'],n_album= 0)
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artisti_n_album(n_album):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select a.id, a.name, COUNT(*) as n_album
                    from artist a, album al
                    where al.artist_id = a.id
                    group by a.id, a.name
                    having COUNT(*)>= %s"""
        cursor.execute(query, (n_album,))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'], n_album=row['n_album'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_peso():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT LEAST(a1.artist_id, a2.artist_id) AS a1_id,
		GREATEST(a1.artist_id, a2.artist_id) AS a2_id,
		COUNT(DISTINCT t1.genre_id) AS peso
FROM album a1, album a2, track t1, track t2
WHERE t1.genre_id=t2.genre_id AND t1.album_id=a1.id AND t2.album_id=a2.id AND a1.artist_id<a2.artist_id
GROUP BY a1_id, a2_id"""
        cursor.execute(query)
        for row in cursor:
            result.append(Connessioni(**row))
        cursor.close()
        conn.close()
        return result