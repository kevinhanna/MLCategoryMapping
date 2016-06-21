from address_classifier.address_dao import AddressDao
import address_classifier.address_util as au

adao = AddressDao()




training_addresses = [
    ["123-456 East Seven St, Building 8",
     [au.SUITE, au.DASH, au.STREET_NUMBER, au.STREET_DIRECTION, au.COMMA, au.STREET_NAME, au.STREET_TYPE, au.BUILDING_INDICATOR, au.BUILDING_NUMBER],
     ],
    ["801 East Orange Street",
     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE],
     ],
    ["2401 E 6th St Ste 3033",
     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE],
     ],
    ["1037 Vermont Street",
     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE],
     ],
    ["9416 HIGHWAY 6 LOOP",
     [au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NUMBER, au.HIGHWAY_NAME]
     ],
    ["1307 State Route 1",
     [au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.HIGHWAY_NUMBER],
     ],
    ["123-345 Seventh St E",
     [au.SUITE, au.DASH, au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION]
     ],
    ["2720 Lake Wheeler Road, Suite 125",
     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.COMMA, au.SUITE_INDICATOR, au.SUITE]
     ],
    ["9275 Sw 152nd St, Suite #206",
     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.COMMA, au.SUITE_INDICATOR, au.SUITE]
     ],
    ["P.O. Box 400",
     [au.POBOX_INDICATOR, au.POBOX_INDICATOR, au.POBOX]
     ],
    ["1555 W Brady",
     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME]
     ],
    ["1091 Highway 24 East",
     [au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NUMBER, au.STREET_DIRECTION]
     ],
    ["73-670 El Paseo",
     [au.SUITE, au.DASH, au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME]
     ],
    ["2980 I-35",
     [au.STREET_NUMBER, au.HIGHWAY_NAME, au.DASH, au.HIGHWAY_NUMBER]
     ],
    ["1215 Fry Rd. Suite D",
     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE]
     ]


]

def populate_training():
    adao.delete_listing_training("US")
    for ta in training_addresses:
        adao.insert_listing_training(ta[0], ta[1], "US")

test_addresses = [
    [
        "9416 HIGHWAY 6 LOOP",
        [au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NUMBER, au.HIGHWAY_NAME],
    ],[
        "8400 E Crescent Pkwy Ste 250",
        [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE],
    ],[
        "400 Mack Avenue",
        [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE],
    ],[
        "222 S Herlong Ave",
        [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE],
    ],[
        "1526 Cortelyou Rd",
        [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE],
    ],[
        "417 N Wilson St",
        [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE],
    ], [
        "N80W14962 Appleton Ave",
        [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE],
    ], ["2720 Lake Wheeler Road, Suite 125",
        [au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.COMMA, au.SUITE_INDICATOR, au.SUITE]
    ],
    ["9275 Sw 152nd St # 206",
        [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE]
    ],
    ["9275 Sw 152nd St, Suite #206",
        [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.COMMA, au.SUITE_INDICATOR, au.SUITE]
    ],
    # "635 S Ellis St",
    # "800 Park Boulevard Ste 790",
    # "102 S Broadway",
    # "2720 Lake Wheeler Road, Suite 125",
    # "2110 W 2nd St",
    # "1104 Lockwood ln",
    # "9215 SW Canyon Rd.",
    # "4642 West Market St. Suite 155",
    # "2600 Hitching Post Trail",
    # "Ste. #123 345 7th St E",
    # "#405-220 3rd Avenue South",
    # "#405 - 220 3rd Avenue South",
    # "6835 Dayton Springfield Road",
    # "9436 W Lake Mead Blvd, #11F",
    # "7080 W State Road 84 # 10",
    # "7080 W State Road 84",
    # "9275 Sw 152nd St # 206",
    # "3328 Washington Road Suite D",
    # "18579 Us Route 11",
    # "222 US-70",
]

expected_results = [
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.SUITE_INDICATOR, au.SUITE, au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION, au.EMPTY],
    [au.SUITE, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION, au.EMPTY, au.EMPTY],
    [au.SUITE, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION, au.EMPTY, au.EMPTY],
    [au.SUITE, au.STREET_NUMBER, au.STREET_NUMBER, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.SUITE, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.SUITE, au.EMPTY],
    [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY, au.EMPTY],
    [au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
]

def populate_street_address_test():
    adao.delete_address_testing("US")
    for address in test_addresses:
        adao.insert_address_testing(address[0], address[1], "US")

populate_training()
populate_street_address_test()