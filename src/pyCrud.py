from pyBakend import pyConexion

con = pyConexion.Connection.connection('localhost', 'root', '12345678', 'peliculas')


def add_reg(cod, nom_peli):
    if con is not None:
        with con.cursor() as cursor:
            query = 'INSERT INTO pelicula(idPelicula, nombre) VALUES(%s,%s);'
            result = cursor.execute(query, (cod, nom_peli))
            print(result)
        con.commit()


def list_reg():
    if con is not None:
        with con.cursor() as cursor:
            query = 'SELECT * FROM pelicula;'
            cursor.execute(query)
            result = cursor.fetchall()
            print(result[0][1])


def del_reg(cod_peli):
    with con.cursor() as cursor:
        query = 'delete from pelicula where idPelicula=%s;'
        cursor.execute(query, cod_peli)
        print(cursor.rowcount, "Fila(s) afectas.")
    con.commit()


def edit_reg(cod_peli, nom_mod):
    with con.cursor() as cursor:
        query = "UPDATE pelicula " \
                "SET nombre = %s " \
                "WHERE idPelicula = %s;"
        val = (nom_mod, cod_peli)
        cursor.execute(query, val)
        print(cursor.rowcount, "Fila(s) afectas.")
    con.commit()


if __name__ == "__main__":
    cadena = "transformer".encode('utf-8')
    edit_reg(3, cadena)
