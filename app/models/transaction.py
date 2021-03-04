from app import db, build_insert_query, logger, INSERT_QUERY_STRING

class Transaction:

    def __init__(self, data):
        self.channel_id = data['channel_id'].strip()
        self.channel_name = data['channel_name'].strip()
        self.from_user_name = data['user_name'].strip()
        self.from_user_id = data["user_id"].strip()
        self.text = data["text"].strip()

    def execute_select_check_sum(self, query):
        logger.debug("Running query %s for checking sum total points", query)
        try:
            cursor = db.cursor()
            cursor.execute(query)
            data = cursor.fetchone()
            if not data :
                return True, data["day_total"]
            else :
                return True, 0
        except Exception as e:
            logger.exception("Exception in getting the sum total for the day for the user.")
            return False, None

    def execute_user_feed(self, query):
        logger.debug("Executing query %s", query)
        try:
            cursor = db.cursor()
            cursor.execute(query)
            return True, cursor.fetchall()
        except Exception as e:
            logger.exception("Exception in running query %s", query)
            return False, None

    def insert(self, data):
        logger.debug("Inserting data to db")
        try:
            # query = build_insert_query(data)
            cursor = db.cursor()
            cursor.execute(INSERT_QUERY_STRING, (data['channel_id'], data['channel_name'], data['from_user_id'], data['from_user_name'], data['points'], data['to_user_id'], data['to_user_name'], data['post_id'], data['insertiontime'], data['message']))
            # if res == 0:
            #     return False
            db.commit()
            return True
        except Exception as e:
            logger.exception("Exception in inserting data to the db server")
            return False