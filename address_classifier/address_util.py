# MAX_TOKENS = 10

STREET_TYPES = 'st', 'street', 'ave', 'avenue', 'ln', 'lane', 'cres', 'crescent', 'ct', 'court', 'rd', 'road', 'trail', 'blvd', 'pkwy'

SUITE_INDICATOR_TYPES = 'suite', 'ste', '#', 'apt'

STREET_DIRECTIONS = 'n', 'e', 's', 'w', \
                    'north', 'east', 'south', 'west', \
                    'ne', 'nw', 'se', 'sw', \
                    'north east', 'north west', 'south east', 'south west'

HIGHWAY_NAMES = 'us', 'highway', 'hwy', 'state', 'route'

BUILDING_INDICATOR_TYPES = 'building', 'bldg'

# Token types
EMPTY = 0
STREET_NUMBER = 1
STREET_NAME = 2
HIGHWAY_NAME = 3
STREET_DIRECTION = 4
STREET_TYPE = 5
SUITE_INDICATOR = 6
SUITE = 7
BUILDING_INDICATOR = 8
BUILDING_NUMBER = 9

DASH = 10
COMMA = 11

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
    BUILDING_INDICATOR: "BUILDING_INDICATOR",
    BUILDING_NUMBER: "BUILDING_NUMBER",
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
        elif (token in SUITE_INDICATOR_TYPES):
            result.append(SUITE_INDICATOR)
        elif (token.isdigit()):
            result.append(NUMERIC_STRING)
        elif(token in STREET_DIRECTIONS):
            result.append(STREET_DIRECTION)
        elif (token == '-'):
            result.append(DASH)
        elif (token == ','):
            result.append(COMMA)
        else:
            result.append(ALPHA_STRING)

    return result

def pretty_print(results):
    ret = "["
    for result in results:
        ret = ret + get_token_name(result) + ", "
    ret = ret + "]"

    return ret









