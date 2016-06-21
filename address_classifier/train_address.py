from address_classifier.address_dao import AddressDao
from address_classifier.street_address_trainer import StreetAddressTrainer
import address_classifier.address_util as au
from address_classifier.street_address import StreetAddress

# pd.populate_training()
# pd.populate_street_address_test()


adao = AddressDao()
test_addresses = adao.get_testing_addresses("US")
sample_addresses = adao.get_ag_addresses("US", 10)

sat = StreetAddressTrainer()

for address in test_addresses:
    tokened_ag_address = sat.pad_to_max(au.identify_tokens(address['street_address']))
    address_tokens = au.normalize_address(address['street_address']).split()
    address_tokens = sat.pad_to_max(address_tokens)

    predicteds = sat.predict(address['street_address'])
    equal = (predicteds == sat.pad_to_max(address['tokens']))

    print('\nEqual %s' % (equal))

    if (not equal):
        # print(predicteds)
        # # print(au.pad_to_max(address['tokens']))
        # print(sat.pad_to_max(address['tokens']))
        print('Address: %s' % (address['street_address']))
        print("Predicted: %s," % (au.pretty_print(predicteds)))
        print("Expected: %s" % (au.pretty_print(address['tokens'])))
        street_address_tokens = sat.pad_to_max(au.identify_tokens(address['street_address']))
        print('Input: %s' % au.pretty_print(street_address_tokens))

    sa1 = StreetAddress(address_tokens, predicteds)
    sa2 = StreetAddress(address_tokens, predicteds)

    print("Match: %s" % sa1.match_street_address(sa2))

for sample_address in sample_addresses:

    sa1 = StreetAddress(au.normalize_address(au.normalize_address(sample_address['ag_address'])).split(), sat.predict(sample_address['ag_address']))
    sa2 = StreetAddress(au.normalize_address(au.normalize_address(sample_address['lis_address'])).split(), sat.predict(sample_address['lis_address']))

    print("AG Address: %s" % sample_address['ag_address'])
    print("LIS Address: %s" % sample_address['lis_address'])
    print("Match: %s" % sa1.match_street_address(sa2))