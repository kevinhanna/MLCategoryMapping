from simple_classifier import SimplePredictor

MAX_TOKENS = 7

STREET_TYPES = 'st', 'street', 'ave', 'avenue', 'ln', 'lane', 'cres', 'crescent', 'ct', 'court', 'rd', 'trail', 'blvd'

SUITE_INDICATOR_TYPES = 'suite', 'ste', '#', 'apt'

STREET_DIRECTIONS = 'n', 'e', 's', 'w', \
                    'north', 'east', 'south', 'west', \
                    'ne', 'nw', 'se', 'sw', \
                    'north east', 'north west', 'south east', 'south west', \
                    'northeast', 'northwest', 'southeast', 'southwest'

HIGHWAY_NAMES = 'us', 'highway', 'hwy', 'state', 'route'

# Token types
EMPTY = 0
STREET_NUMBER = 1
STREET_NAME = 2
HIGHWAY_NAME = 3
STREET_DIRECTION = 4
STREET_TYPE = 5
SUITE_INDICATOR = 6
SUITE = 7

ALPHA_STRING = 20
NUMERIC_STRING = 21

ADDRESS_TOKEN_TYPES = {
    EMPTY: "EMPTY",
    STREET_NUMBER: "STREET_NUMBER",
    STREET_NAME: "STREET_NAME",
    HIGHWAY_NAME: "HIGHWAY_NAME",
    STREET_DIRECTION: "STREET_DIRECTION",
    STREET_TYPE: "STREET_TYPE",
    SUITE_INDICATOR: "SUITE_INDICATOR",
    SUITE: "SUITE",
    ALPHA_STRING: "ALPHA_STRING",
    NUMERIC_STRING: "NUMERIC_STRING",
}


def get_token_name(type_id):
    return ADDRESS_TOKEN_TYPES.get(type_id)

def get_token_id(type_name):
    for id, name in ADDRESS_TOKEN_TYPES.items():
        if (name == type_name):
            return id;
    return None

def normalize_address(address):
    address = address.lower().replace('.', '').replace('-', ' ').replace('#', ' # ')
    return address


def indentify_tokens(address):

    tokens = normalize_address(address).split()

    result = []

    for token in tokens:
        if (token in STREET_TYPES):
            result.append(STREET_TYPE)
        elif (token in HIGHWAY_NAMES):
            result.append(HIGHWAY_NAME)
        elif (token in SUITE_INDICATOR_TYPES):
            result.append(SUITE_INDICATOR)
        elif (token.isdigit()):
            result.append(NUMERIC_STRING)
        elif(token in STREET_DIRECTIONS):
            result.append(STREET_DIRECTION)
        else:
            result.append(ALPHA_STRING)

    return __pad_to_max(result)

def __pad_to_max(list):
    return list+[EMPTY]*(MAX_TOKENS-len(list))

def __pretty_print(results):
    ret = "["
    for result in results:
        ret = ret + get_token_name(result) + ", "
    ret = ret + "]"

    return ret


#Address, sample, classification
training_addresses = [
    ["801 East Orange Street",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
     ],
    ["568 East Blue Harbor St.",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
     ],
    # ["7111 E McDowell Rd",
    #  [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
    #  ],
    # ["995 W Haynes Rd",
    #  [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
    #  ],
    ["1037 Vermont Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE],
     ],
    # ["511 Calhoun Street",
    #  [STREET_NUMBER, STREET_NAME, STREET_TYPE],
    #  ],
    # ["1201 Harvey Road",
    #  [STREET_NUMBER, STREET_NAME, STREET_TYPE],
    #  ],
    # ["6614 Wisteria Drive",
    #  [STREET_NUMBER, STREET_NAME, STREET_TYPE],
    #  ],
    # ["13 Morin Street",
    #  [STREET_NUMBER, STREET_NAME, STREET_TYPE],
    #  ],
    ["1307 U.S. 1",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME],
     ],
    ["1307 State Route 1",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME],
     ],
    ["9416 HIGHWAY 6 LOOP",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME]
     ],
    ["7080 W State Road 84",
     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME]
    ],
    ["8400 E Crescent Pkwy",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE]
     ],
]

temp_training_addresses = []

for address in training_addresses:
    temp_training_addresses.append([address[0] + ", Suite 123", address[1]+[SUITE_INDICATOR, SUITE]])
    # temp_training_addresses.append([address[0] + " #123", address[1] + [SUITE_INDICATOR, SUITE]])
    temp_training_addresses.append([address[0] + "Ste 12F", address[1] + [SUITE_INDICATOR, SUITE]])
    temp_training_addresses.append(["Suite 123 " + address[0] , [SUITE_INDICATOR, SUITE]+address[1]])
    # temp_training_addresses.append(["#123 " + address[0], [SUITE_INDICATOR, SUITE] + address[1]])
    temp_training_addresses.append(["123-" + address[0], [SUITE] + address[1]])

training_addresses = training_addresses+temp_training_addresses

for address in training_addresses:
    print(address[0])
    print(__pretty_print(address[1]))

print("#################")


for address in training_addresses:
    address[1] = __pad_to_max(address[1])


test_addresses = [
    ["9416 HIGHWAY 6 LOOP",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY]],
    ["8400 E Crescent Pkwy Ste 250",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY]],
    ["400 Mack Avenue",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY]],
    ["222 S Herlong Ave",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["1526 Cortelyou Rd",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY]],
    ["417 N Wilson St",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["635 S Ellis St",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["N80W14962 Appleton Ave",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY]],
    ["800 Park Boulevard Ste 790",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY, EMPTY]],
    ["102 S Broadway",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, EMPTY, EMPTY, EMPTY, EMPTY]],
    ["2720 Lake Wheeler Road, Suite 125",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY]],
    ["2110 W 2nd St",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["1104 Lockwood ln",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY]],
    ["9215 SW Canyon Rd.",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["4642 West Market St. Suite 155",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY]],
    ["2600 Hitching Post Trail",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["Ste. #123 345 7th St E",
     [SUITE_INDICATOR, SUITE_INDICATOR, SUITE, STREET_NUMBER, STREET_NAME, STREET_TYPE, STREET_DIRECTION]],
    ["#405-220 3rd Avenue South",
     [SUITE_INDICATOR, SUITE, STREET_NAME, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY]],
    ["#405 - 220 3rd Avenue South",
     [SUITE_INDICATOR, SUITE, STREET_NAME, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY]],
    ["6835 Dayton Springfield Road",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY]],
    ["9436 W Lake Mead Blvd, #11F",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE]],
    ["7080 W State Road 84 # 10",
     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, SUITE_INDICATOR, SUITE]],
    ["7080 W State Road 84",
     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY]],
    ["9275 Sw 152nd St # 206",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, SUITE]],
    ["3328 Washington Road Suite D",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY, EMPTY]],
    ["18579 Us Route 11",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY]],
    ["222 US-70",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY, EMPTY]]
    # "123 Four Five St. Building F suite 5",

]


#
# expected_results = [
#     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, EMPTY, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, EMPTY, EMPTY, EMPTY],
#     [SUITE_INDICATOR, SUITE, STREET_NUMBER, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY],
#     [SUITE, STREET_NAME, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY, EMPTY],
#     [SUITE, STREET_NAME, STREET_NAME, STREET_TYPE, STREET_DIRECTION, EMPTY, EMPTY],
#     [SUITE, STREET_NUMBER, STREET_NUMBER, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, SUITE_INDICATOR, SUITE],
#     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_DIRECTION, STREET_TYPE, SUITE_INDICATOR, SUITE, SUITE, EMPTY],
#     [STREET_NUMBER, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE, EMPTY, EMPTY],
#     [STREET_NUMBER, STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY],
#     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, EMPTY, EMPTY, EMPTY, EMPTY],
# ]

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
    tokens = indentify_tokens(address[0])
    sample.append(tokens)
    print('%s - %s - %s' % (tokens, address[1], address[0]))
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


for test_address in test_addresses:
    address = test_address[0]
    expected = test_address[1]

    tokened_address = indentify_tokens(address)
    split = normalize_address(address).split()
    split = __pad_to_max(split)

    # predited_1 = get_token_name(classifier_1.predict([address[1]])[0])
    predited_1 = get_token_name(classifier_1.predict([tokened_address])[0])
    predited_2 = get_token_name(classifier_2.predict([tokened_address])[0])
    predited_3 = get_token_name(classifier_3.predict([tokened_address])[0])
    predited_4 = get_token_name(classifier_4.predict([tokened_address])[0])
    predited_5 = get_token_name(classifier_5.predict([tokened_address])[0])
    predited_6 = get_token_name(classifier_6.predict([tokened_address])[0])
    predited_7 = get_token_name(classifier_7.predict([tokened_address])[0])

    # print('Address: %s, %s %s %s %s %s %s %s ' % (address[0], predited_1, predited_2, predited_3, predited_4, predited_5, predited_6, predited_7))
    print("[%s, %s, %s, %s, %s, %s, %s]," % (predited_1, predited_2, predited_3, predited_4, predited_5, predited_6, predited_7))
    print(__pretty_print(expected))
    print('Address: %s' % (address))
    print('\t%s: %s' % (split[0], predited_1))
    print('\t%s: %s' % (split[1], predited_2))
    print('\t%s: %s' % (split[2], predited_3))
    print('\t%s: %s' % (split[3], predited_4))
    print('\t%s: %s' % (split[4], predited_5))
    print('\t%s: %s' % (split[5], predited_6))
    print('\t%s: %s' % (split[6], predited_7))

