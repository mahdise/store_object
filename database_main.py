import sqlite3


class Mahdi:
    def __init__(self):
        self.conn = sqlite3.connect('mahdi.db')
        self.table_of_db = [
                        'CREATE TABLE gamification_score ( user_id TEXT, object TEXT )',

            ]

        for self.x in self.table_of_db:
            try:
                self.conn.execute(self.x)

            except:
                print("no")
                pass
        self.conn.commit()

    def insert_data(self, user_id, obj):
        try:
            add_admin = SuperUser(self, user_id, obj)

        except:
            print("Could")

    def get_item(self, user_id):
        ep_value_from_database = self.conn.execute(
            "SELECT object FROM gamification_score WHERE user_id = ? ", [user_id]).fetchall()

        ep_value = list(ep_value_from_database[0])

        return ep_value[0]





class SuperUser:
    def __init__(self, logger, user_id, object):
        self.logger = logger
        self.username = str(user_id)
        self.password = str(object)
        self.insert_super_user_info()

    def insert_super_user_info(self):
        self.logger.conn.execute("""insert into gamification_score(user_id, object)values(?,?) """,
                                 (self.username, self.password))
        self.logger.conn.commit()


adf = Mahdi()