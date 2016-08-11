import address_classifier.address_util as au
from address_classifier.address_dao import AddressDao
from simple_classifier import SimplePredictor


class StreetAddressTrainer:
    MAX_SIZE = 0
    training_addresses = None
    predictors = None

    def __init__(self):
        # These should be passed, but it's a pretty specific list
        self.training_addresses = self.__get_training_addresses()
        self.tokenized_street_addresses = self.__tokenize_street_addresses()
        print("Done init")

    def __get_training_addresses(self):
        adao = AddressDao()
        self.training_addresses = adao.get_training_addresses("US")

        return self.training_addresses

    def __tokenize_street_addresses(self):
        tokenized_addresses = []

        for address in self.training_addresses:
            tokens = au.identify_tokens(address['street_address'])
            if (len(tokens) > self.MAX_SIZE):
                print("New max: %s" % au.identify_tokens(address['street_address']))
                self.MAX_SIZE = len(tokens)
                au.MAX_TOKENS = self.MAX_SIZE  #todo combine au functionality with this file

    def get_predictors(self):

        if self.predictors:
            return self.predictors
        else:
            return self.__generate_predictors()

    def __generate_predictors(self):
        # predictors = [None for i in range(self.MAX_SIZE-1)]
        predictors = []
        targets = [[] for i in range(self.MAX_SIZE)]#todo shouldn't need the -1
        street_addresses_tokenized = []


        for address in self.training_addresses:
            street_address = address['street_address']
            street_address_tokenized = self.pad_to_max(au.identify_tokens(street_address))
            street_addresses_tokenized.append(street_address_tokenized)

            tokens = self.pad_to_max(address['tokens'])

            for target, token in zip(targets, tokens):
                target.append(token)

        for target in targets:
            predictors.append(SimplePredictor(sample_data=street_addresses_tokenized, target_classifications=target))

        self.predictors = predictors

        return predictors

    def pad_to_max(self, list):
        retval =  list + [0] * (self.MAX_SIZE - len(list))
        return retval

    def predict(self, address):
        predicteds = []
        tokened_ag_address = self.pad_to_max(au.identify_tokens(address))
        for predictor in self.get_predictors():
            # predicteds.append(predictor.predict(self.pad_to_max([tokened_ag_address][0])))
            predicteds.append(predictor.predict([tokened_ag_address])[0])

        return predicteds




