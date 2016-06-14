from simple_classifier import SimplePredictor
from address_classifier.address_dao import AddressDao
from address_classifier.street_address import StreetAddress
from address_classifier.street_address_trainer import StreetAddressTrainer
import address_classifier.address_util as au

# pd.populate_training()
# pd.populate_street_address_test()


adao = AddressDao()
test_addresses = adao.get_testing_addresses("US")

sat = StreetAddressTrainer()

for address in test_addresses:
    tokened_ag_address = au.indentify_tokens(address['street_address'])
    address_tokens = au.normalize_address(address['street_address']).split()
    address_tokens = au.pad_to_max(address_tokens)

    predicteds = []
    # prediteds_1 = get_token_name(classifier_1.predict([address[1]])[0])
    for predictor in sat.get_predictors():
        predicteds.append(au.get_token_name(predictor.predict([tokened_ag_address])[0]))


    print('Address: %s' % (address['street_address']))
    print("Predicted: [%s, %s, %s, %s, %s, %s, %s]," % (predicteds[0], predicteds[1], predicteds[2], predicteds[3], predicteds[4], predicteds[5], predicteds[6]))
    print("Expected: %s" % (au.pretty_print(address['tokens'])))
    street_address_tokens = au.pad_to_max(au.indentify_tokens(address['street_address']))
    print('Input: %s\n' % au.pretty_print(street_address_tokens))

