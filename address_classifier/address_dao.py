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


    def insert_listing_training(self, street_address, tokens, country):
        cursor = self.cnx.cursor()

        add_training = "INSERT INTO street_address_training VALUES(null, %s, %s, %s)"

        cursor.execute(add_training, (street_address, pickle.dumps(tokens), country))
        listing_training_id = cursor.lastrowid

        self.cnx.commit()
        cursor.close()

        return listing_training_id

    def delete_listing_training(self, country):
        cursor = self.cnx.cursor()

        add_training = "DELETE FROM street_address_training WHERE country = %s"

        cursor.execute(add_training, (country,))

        self.cnx.commit()
        cursor.close()


    def insert_address_testing(self, street_address, tokens, country):
        cursor = self.cnx.cursor()

        add_testing = "INSERT INTO street_address_testing VALUES(null, %s, %s, %s)"

        cursor.execute(add_testing, (street_address, pickle.dumps(tokens), country))
        listing_training_id = cursor.lastrowid

        self.cnx.commit()
        cursor.close()

        return listing_training_id

    def delete_address_testing(self, country):
        cursor = self.cnx.cursor()

        add_testing = "DELETE FROM street_address_testing WHERE country = %s"

        cursor.execute(add_testing, (country,))

        self.cnx.commit()
        cursor.close()


    def get_training_addresses(self, country):
        retval = []
        cursor = self.cnx.cursor()

        query = "SELECT street_address_training_id, street_address, tokens_pickle, country FROM street_address_training WHERE country = %s"

        cursor.execute(query, params=(country,))
        for (street_address_training_id, street_address, tokens_pickle, country) in cursor:
            retval.append({'street_address':street_address, 'tokens': pickle.loads(tokens_pickle), 'country':country})

        return retval

    def get_testing_addresses(self, country):
        retval = []
        cursor = self.cnx.cursor()

        query = "SELECT street_address_testing_id, street_address, tokens_pickle, country FROM street_address_testing WHERE country = %s"

        cursor.execute(query, params=(country,))
        for (street_address_training, street_address, tokens_pickle, country) in cursor:
            retval.append({'street_address':street_address, 'tokens': pickle.loads(tokens_pickle), 'country':country})

        return retval


    def get_ag_addresses(self, country, number):
        retval = []
        cursor = self.cnx.cursor()

        # TODO Distinct LIS
        query = "SELECT listing_history_id, ag_address, lis_address, match_details_address " \
                "FROM listing_history " \
                "WHERE ag_country = %s " \
                "LIMIT %s"

        cursor.execute(query, params=(country, number,))
        for (listing_history_id, ag_address, lis_address, match_details_address) in cursor:
            retval.append({'listing_history_id':listing_history_id,
                           'ag_address':ag_address,
                           'lis_address':lis_address,
                           'match_details_address':match_details_address})

        return retval