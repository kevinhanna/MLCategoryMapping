from simple_classifier import SimplePredictor

MAX_TOKENS = 7

STREET_TYPES = 'st', 'street', 'ave', 'avenue', 'ln', 'lane', 'cres', 'crescent', 'ct', 'court', 'rd', 'trail'
SUITE_INDICATOR_TYPES = 'suite', 'ste', '#', 'apt'
STREET_DIRECTIONS = 'n', 'e', 's', 'w', \
                    'north', 'east', 'south', 'west', \
                    'ne', 'nw', 'se', 'sw', \
                    'north east', 'north west', 'south east', 'south west'

def translate(type_id):
    switcher = {
        0: "EMPTY",
        1: "STREET_NUMBER",
        2: "STREET_NAME",
        3: "STREET_DIRECTION",
        4: "STREET_TYPE",
        5: "SUITE_INDICATOR",
        6: "SUITE",
        7: "ALPHA_STRING",
        8: "NUMERIC_STRING",
    }
    return switcher.get(type_id)

def normalize_address(address):
    address = address.lower().replace('.', '').replace('-', ' ').replace('#', '')
    return address


def indentify_tokens(address):

    tokens = normalize_address(address).split()

    result = []

    for token in tokens:
        if (token in STREET_TYPES):
            result.append(STREET_TYPE)
        elif (token in SUITE_INDICATOR_TYPES):
            result.append(SUITE_INDICATOR)
        elif (token.isdigit()):
            result.append(NUMERIC_STRING)
        elif(token in STREET_DIRECTIONS):
            result.append(STREET_DIRECTION)
        else:
            result.append(ALPHA_STRING)

    return result+[0]*(MAX_TOKENS-len(result)) # Zero out to max length



# Token types
EMPTY = 0
STREET_NUMBER = 1
STREET_NAME = 2
STREET_DIRECTION = 3
STREET_TYPE = 4
SUITE_INDICATOR = 5
SUITE = 6

ALPHA_STRING = 7
NUMERIC_STRING = 8



#Address, sample, classification
training_addresses = [
    ["East IGNORE Street 801, Suite 8 Building",
     [STREET_DIRECTION, STREET_NAME, STREET_TYPE, STREET_NUMBER, SUITE_INDICATOR, NUMERIC_STRING, ALPHA_STRING],
     ], # Dummy to get around bug
    ["801 East Orange Street",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
     ],
    ["7111 E McDowell Rd",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
     ],
    ["995 W Haynes Rd",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
     ],
    ["1037 Vermont Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
     ],
    ["511 Calhoun Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
     ],
    ["1201 Harvey Road",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
     ],
    ["6614 Wisteria Drive",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
     ],
    ["13 Morin Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
     ],
    ["1307 U.S. 1",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, EMPTY, EMPTY, EMPTY, EMPTY],
     ],
    ["2401 E 6th St Ste 3033",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY],
     ],
    ["2727 Enterprise Parkway, Suite 200",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY, EMPTY],
     ],
    ["568 Eeast Harbor St. Suite 302",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY],
     ],
    ["Ste. 123 345 7th St E",
     [SUITE_INDICATOR, SUITE, STREET_NUMBER, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY],
     ],
    ["123-345 Seventh St E",
     [SUITE, STREET_NUMBER, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY, EMPTY]
     ]

]


test_addresses = [
    ["9416 HIGHWAY 6 LOOP"],
    ["8400 E Crescent Pkwy Ste 250"],
    ["400 Mack Avenue"],
    ["222 S Herlong Ave"],
    ["1526 Cortelyou Rd"],
    ["417 N Wilson St"],
    ["635 S Ellis St"],
    ["N80W14962 Appleton Ave"],
    ["800 Park Boulevard Ste 790"],
    ["102 S Broadway"],
    ["2720 Lake Wheeler Road, Suite 125"],
    ["2110 W 2nd St"],
    ["1104 Lockwood ln"],
    ["9215 SW Canyon Rd."],
    ["4642 West Market St. Suite 155"],
    ["2600 Hitching Post Trail"],
    ["Ste. #123 345 7th St E"],
    ["#405-220 3rd Avenue South"],
    ["#405 - 220 3rd Avenue South"]
]

sample = []
classification_1 = []
classification_2 = []
classification_3 = []
classification_4 = []
classification_5 = []
classification_6 = []
classification_7 = []

for address in training_addresses:

    sample.append(indentify_tokens(address[0]))

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
    tokened_address = indentify_tokens(address[0])
    split = normalize_address(address[0]).split()
    split = split+[0]*(MAX_TOKENS-len(split))

    # predited_1 = translate(classifier_1.predict([address[1]])[0])
    predited_1 = translate(classifier_1.predict([tokened_address])[0])
    predited_2 = translate(classifier_2.predict([tokened_address])[0])
    predited_3 = translate(classifier_3.predict([tokened_address])[0])
    predited_4 = translate(classifier_4.predict([tokened_address])[0])
    predited_5 = translate(classifier_5.predict([tokened_address])[0])
    predited_6 = translate(classifier_6.predict([tokened_address])[0])
    predited_7 = translate(classifier_7.predict([tokened_address])[0])

    # print('Address: %s, %s %s %s %s %s %s %s ' % (address[0], predited_1, predited_2, predited_3, predited_4, predited_5, predited_6, predited_7))
    print('Address: %s' % (address[0]))
    print('\t%s: %s' % (split[0], predited_1))
    print('\t%s: %s' % (split[1], predited_2))
    print('\t%s: %s' % (split[2], predited_3))
    print('\t%s: %s' % (split[3], predited_4))
    print('\t%s: %s' % (split[4], predited_5))
    print('\t%s: %s' % (split[5], predited_6))
    print('\t%s: %s' % (split[6], predited_7))

