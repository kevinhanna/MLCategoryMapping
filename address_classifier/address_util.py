# MAX_TOKENS = 10

STREET_TYPES = 'st', 'street', 'ave', 'avenue', 'ln', 'lane', 'cres', 'crescent', 'ct', 'court', 'rd', 'road', 'trail', 'blvd', 'pkwy'

SUITE_INDICATORS = 'suite', 'ste', '#', 'apt'

STREET_DIRECTIONS = 'n', 'e', 's', 'w', \
                    'north', 'east', 'south', 'west', \
                    'ne', 'nw', 'se', 'sw', \
                    'north east', 'north west', 'south east', 'south west'

HIGHWAY_NAMES = 'us', 'highway', 'hwy', 'state', 'route'

BUILDING_INDICATORS = 'building', 'bldg'

POBOX_INDICATORS = 'p.o.', 'box'


# Token types
EMPTY = 0
STREET_NUMBER = 10
STREET_NAME = 20
HIGHWAY_NAME = 30
HIGHWAY_NUMBER = 40
STREET_DIRECTION = 500
STREET_TYPE = 60
SUITE_INDICATOR = 70
SUITE = 80
BUILDING_INDICATOR = 90
BUILDING_NUMBER = 100
POBOX_INDICATOR = 1100
POBOX = 1200

DASH = 200
COMMA = 210

ALPHA_STRING = 300
NUMERIC_STRING = 310

ADDRESS_TOKEN_TYPES = {
    EMPTY: "EMPTY",
    STREET_NUMBER: "STREET_NUMBER",
    STREET_NAME: "STREET_NAME",
    HIGHWAY_NAME: "HIGHWAY_NAME",
    HIGHWAY_NUMBER: "HIGHWAY_NUMBER",
    STREET_DIRECTION: "STREET_DIRECTION",
    STREET_TYPE: "STREET_TYPE",
    SUITE_INDICATOR: "SUITE_INDICATOR",
    SUITE: "SUITE",
    ALPHA_STRING: "ALPHA_STRING",
    NUMERIC_STRING: "NUMERIC_STRING",
    BUILDING_INDICATOR: "BUILDING_INDICATOR",
    BUILDING_NUMBER: "BUILDING_NUMBER",
    POBOX_INDICATOR: "POBOX_INDICATOR",
    POBOX: "POBOX",
    DASH: "DASH",
    COMMA: "COMMA",
}


def get_token_name(type_id):
    return ADDRESS_TOKEN_TYPES.get(type_id)

def get_token_id(type_name):
    for id, name in ADDRESS_TOKEN_TYPES.items():
        if (name == type_name):
            return id;
    return None

def normalize_address(address):
    address = address.lower().replace('.', '').replace('-', ' - ').replace('#', ' # ').replace(',', ' , ')
    return address


def identify_tokens(address):

    tokens = normalize_address(address).split()

    result = []

    for token in tokens:
        if (token in STREET_TYPES):
            result.append(STREET_TYPE)
        elif (token in HIGHWAY_NAMES):
            result.append(HIGHWAY_NAME)
        elif (token in SUITE_INDICATORS):
            result.append(SUITE_INDICATOR)
        elif (token.isdigit()):
            result.append(NUMERIC_STRING)
        elif(token in STREET_DIRECTIONS):
            result.append(STREET_DIRECTION)
        elif (token == '-'):
            result.append(DASH)
        elif (token == ','):
            result.append(COMMA)
        elif (token in POBOX_INDICATORS):
            result.append(POBOX_INDICATOR)
        else:
            result.append(ALPHA_STRING)

    return result

def pretty_print(results):
    ret = "["
    for result in results:
        try:
            ret = ret + get_token_name(result) + ", "
        except TypeError:
            print ("oops: %s" % result)
    ret = ret + "]"

    return ret









