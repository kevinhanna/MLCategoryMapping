import mysql.connector

try:
   import cPickle as pickle
except:
   import pickle


class AddressDao:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='listingAnalysis')

    def __exit__(self, exc_type, exc_value, traceback):
        self.cnx.close()

    def __do_insert(self, do_work):
        cursor = self.cnx.cursor()

        do_work(cursor)

        self.cnx.commit()
        cursor.close()


    def insert_listing_training(self, address, tokens, country):
        cursor = self.cnx.cursor()

        add_training = "INSERT INTO listing_training VALUES(null, %s, %s, %s)"

        cursor.execute(add_training, (address, pickle.dumps(tokens), country))
        listing_training_id = cursor.lastrowid

        self.cnx.commit()
        cursor.close()

        return listing_training_id

    def get_training_addresses(self, country):
        retval = []
        cursor = self.cnx.cursor()

        query = "SELECT listing_training_id, address, tokens_pickle, country FROM listing_training WHERE country = %s"

        cursor.execute(query, params=(country,))
        for (listing_training_id, address, tokens_pickle, country) in cursor:
            retval.append([address, pickle.loads(tokens_pickle)]) #todo convert to dict

        return retval

    def get_testing_addresses(self, country, number):
        retval = []
        cursor = self.cnx.cursor()

        query = "SELECT listing_history_id, ag_address, lis_address, match_details_address " \
                "FROM listing_history " \
                "WHERE ag_country = %s " \
                "LIMIT %s"

        cursor.execute(query, params=(country, number,))
        for (listing_history_id, ag_address, lis_address, match_details_address) in cursor:
            retval.append([listing_history_id, ag_address, lis_address, match_details_address]) #todo convert to dict

        return retval