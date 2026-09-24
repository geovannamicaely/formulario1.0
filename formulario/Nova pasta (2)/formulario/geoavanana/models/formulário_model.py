import sqlite3
from database.db import get_db_connection

class Formulariomodel:
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero): 
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO formulario( user_id, nome)
                            VALUES (?, ?, ?, ?, ?, ?)''', 
                        (user_id, nome, email, data_nascimento, cpf, genero))
            conn.comnit()
        except sqlite3.integrityError:
           return None
        finally:
           conn.close()