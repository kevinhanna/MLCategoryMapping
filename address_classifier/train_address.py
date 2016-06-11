from simple_classifier import SimplePredictor
from address_classifier.address_dao import AddressDao

import address_classifier.address_util as au

adao = AddressDao()
training_addresses = adao.get_training_addresses("US")

for address in training_addresses:
    address[1] = au.pad_to_max(address[1])

test_addresses = adao.get_testing_addresses("US", 10)

sample = []
classification_1 = []
classification_2 = []
classification_3 = []
classification_4 = []
classification_5 = []
classification_6 = []
classification_7 = []

# Train for each position
for address in training_addresses:
    tokens = au.indentify_tokens(address[0])
    sample.append(tokens)
    print('%s\n%s\n%s' % (au.pretty_print(tokens), au.pretty_print(address[1]), address[0]))
    classification_1.append(address[1][0])
    classification_2.append(address[1][1])
    classification_3.append(address[1][2])
    classification_4.append(address[1][3])
    classification_5.append(address[1][4])
    classification_6.append(address[1][5])
    classification_7.append(address[1][6])

classifier_1 = SimplePredictor(sample_data=sample, target_classifications=classification_1)
classifier_2 = SimplePredictor(sample_data=sample, target_classifications=classification_2)
classifier_3 = SimplePredictor(sample_data=sample, target_classifications=classification_3)
classifier_4 = SimplePredictor(sample_data=sample, target_classifications=classification_4)
classifier_5 = SimplePredictor(sample_data=sample, target_classifications=classification_5)
classifier_6 = SimplePredictor(sample_data=sample, target_classifications=classification_6)
classifier_7 = SimplePredictor(sample_data=sample, target_classifications=classification_7)


for address in test_addresses:
    tokened_ag_address = au.indentify_tokens(address[1])
    split = au.normalize_address(address[1]).split()
    split = au.pad_to_max(split)

    # predited_1 = get_token_name(classifier_1.predict([address[1]])[0])
    predited_1 = au.get_token_name(classifier_1.predict([tokened_ag_address])[0])
    predited_2 = au.get_token_name(classifier_2.predict([tokened_ag_address])[0])
    predited_3 = au.get_token_name(classifier_3.predict([tokened_ag_address])[0])
    predited_4 = au.get_token_name(classifier_4.predict([tokened_ag_address])[0])
    predited_5 = au.get_token_name(classifier_5.predict([tokened_ag_address])[0])
    predited_6 = au.get_token_name(classifier_6.predict([tokened_ag_address])[0])
    predited_7 = au.get_token_name(classifier_7.predict([tokened_ag_address])[0])

    # print('Address: %s, %s %s %s %s %s %s %s ' % (address[0], predited_1, predited_2, predited_3, predited_4, predited_5, predited_6, predited_7))
    print("[%s, %s, %s, %s, %s, %s, %s]," % (predited_1, predited_2, predited_3, predited_4, predited_5, predited_6, predited_7))
    print('Address: %s' % (address[1]))
    print('\t%s: %s' % (split[0], predited_1))
    print('\t%s: %s' % (split[1], predited_2))
    print('\t%s: %s' % (split[2], predited_3))
    print('\t%s: %s' % (split[3], predited_4))
    print('\t%s: %s' % (split[4], predited_5))
    print('\t%s: %s' % (split[5], predited_6))
    print('\t%s: %s' % (split[6], predited_7))

