import os
import logging
import dotenv

from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection


class ResetDatabase(metaclass=Singleton):
    """
    Réinitialisation de la base de données
    """

    @log
    def lancer(self, test_dao=False):
        """
        Lancement de la réinitialisation des données
        Si test_dao = True : réinitialisation des données de test
        """

        dotenv.load_dotenv()

        schema = os.environ["POSTGRES_SCHEMA"]

        create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

        pop_db = open("data/pop_db.sql", encoding="utf-8")
        pop_db_as_string = pop_db.read()
        pop_db.close()

        init_db = open("data/init_db.sql", encoding="utf-8")
        init_db_as_string = init_db.read()
        init_db.close()

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(create_schema)
                    cursor.execute(init_db_as_string)
                    cursor.execute(pop_db_as_string)
        except Exception as e:
            logging.info(e)
            raise

        return True


if __name__ == "__main__":
    ResetDatabase().lancer()
