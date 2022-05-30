import pymysql as m


class Connection:
    @classmethod
    def connection(cls, server, usu, contra, db):
        con = None
        try:
            con = m.connect(host=server,
                            user=usu,
                            password=contra,
                            db=db)
            return con
        except (m.err.OperationalError, m.err.InternalError) as e:
            print(e)
            return con
        finally:
            if con is None:
                con.close()







