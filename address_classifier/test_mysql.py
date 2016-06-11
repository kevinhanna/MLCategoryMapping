# import mysql.connector
#
# cnx = mysql.connector.connect(user='root', password='',
#                               host='127.0.0.1',
#                               database='listingAnalysis')
#
# cursor = cnx.cursor()
#
# query = "SELECT listing_history_id, ag_address, lis_address, match_details_address FROM listing_history WHERE match_details_address = %s limit %s"
#
# match = 1
# limit = 100
#
# cursor.execute(query, params=(match, limit))
# #cursor.execute(query)
#
# for (listing_history_id, ag_address, lis_address, match_details_address) in cursor:
#   print("{} - {}, {}, {}".format(
#       listing_history_id, ag_address, lis_address, match_details_address))
#
# cursor.close()



# test_addresses = [
#     "9416 HIGHWAY 6 LOOP",
#     "8400 E Crescent Pkwy Ste 250",
#     "400 Mack Avenue",
#     "222 S Herlong Ave",
#     "1526 Cortelyou Rd",
#     "417 N Wilson St",
#     "635 S Ellis St",
#     "N80W14962 Appleton Ave",
#     "800 Park Boulevard Ste 790",
#     "102 S Broadway",
#     "2720 Lake Wheeler Road, Suite 125",
#     "2110 W 2nd St",
#     "1104 Lockwood ln",
#     "9215 SW Canyon Rd.",
#     "4642 West Market St. Suite 155",
#     "2600 Hitching Post Trail",
#     "Ste. #123 345 7th St E",
#     "#405-220 3rd Avenue South",
#     "#405 - 220 3rd Avenue South",
#     "6835 Dayton Springfield Road",
#     "9436 W Lake Mead Blvd, #11F",
#     "7080 W State Road 84 # 10",
#     "7080 W State Road 84",
#     "9275 Sw 152nd St # 206",
#     "3328 Washington Road Suite D",
#     "18579 Us Route 11",
#     # "123 Four Five St. Building F suite 5",
#     "222 US-70",
# ]
#
# expected_results = [
#     [au.STREET_NUMBER, au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.SUITE_INDICATOR, au.SUITE, au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION, au.EMPTY],
#     [au.SUITE, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION, au.EMPTY, au.EMPTY],
#     [au.SUITE, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.STREET_DIRECTION, au.EMPTY, au.EMPTY],
#     [au.SUITE, au.STREET_NUMBER, au.STREET_NUMBER, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.STREET_NAME, au.STREET_TYPE, au.SUITE, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.SUITE, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPE, au.SUITE_INDICATOR, au.SUITE, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_NUMBER, au.HIGHWAY_NAME, au.HIGHWAY_NAME, au.EMPTY, au.EMPTY, au.EMPTY],
#     [au.STREET_NUMBER, au.STREET_DIRECTION, au.STREET_NAME, au.EMPTY, au.EMPTY, au.EMPTY, au.EMPTY],
# ]


from address_classifier.address_dao import AddressDao

adao = AddressDao()

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

training_addresses = [
    ["East IGNORE Street 801, Suite 8 Building",
     [STREET_DIRECTION, STREET_NAME, STREET_TYPE, STREET_NUMBER, SUITE_INDICATOR, NUMERIC_STRING, ALPHA_STRING],
     ], # Dummy to get around bug
    ["801 East Orange Street",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
     ],
    ["7111 E McDowell Rd",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
     ],
    ["995 W Haynes Rd",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE],
     ],
    ["1037 Vermont Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE],
     ],
    ["511 Calhoun Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE],
     ],
    ["1201 Harvey Road",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE],
     ],
    ["6614 Wisteria Drive",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE],
     ],
    ["13 Morin Street",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE],
     ],
    ["1307 U.S. 1",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME],
     ],
    ["1307 State Route 1",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME],
     ],
    ["2401 E 6th St Ste 3033",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE],
     ],
    ["2727 Enterprise Parkway, Suite 200",
     [STREET_NUMBER, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE],
     ],
    ["568 Eeast Harbor St. Suite 302",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE_INDICATOR, SUITE],
     ],
    ["568 Eeast Harbor St.",
     [STREET_NUMBER, STREET_NAME, STREET_NAME, STREET_TYPE],
     ],
    ["Ste. 123 345 7th St E",
     [SUITE_INDICATOR, SUITE, STREET_NUMBER, STREET_NAME, STREET_TYPE, STREET_DIRECTION],
     ],
    ["123-345 Seventh St E",
     [SUITE, STREET_NUMBER, STREET_NAME, STREET_TYPE, STREET_DIRECTION]
     ],
    ["9416 HIGHWAY 6 LOOP",
     [STREET_NUMBER, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME]
     ],
    ["7080 W State Road 84 # 10",
     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME]
     ],
    ["7080 W State Road 84",
     [STREET_NUMBER, STREET_DIRECTION, HIGHWAY_NAME, HIGHWAY_NAME, HIGHWAY_NAME]
    ],
    ["9436 W Lake Mead Blvd, #11F",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE]
     ],
    ["9436 W Lake Mead Blvd, Suite 11F",
     [STREET_NUMBER, STREET_DIRECTION, STREET_NAME, STREET_NAME, STREET_TYPE, SUITE]
    ]
]

