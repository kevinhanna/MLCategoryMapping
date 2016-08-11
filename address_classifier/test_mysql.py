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

for ta in training_addresses:
    adao.insert_listing_training(ta[0], ta[1], "US")

