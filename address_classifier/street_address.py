import address_classifier.address_util as au

class StreetAddress:
    
    street_address_tokens = None
    street_address_types = None 
    
    def __init__(self, street_address_tokens, street_address_types):
        """
        :param street_address_tokens: e.g.: ["123", "Main", "St"]
        :param street_address_types: e.g.: [1, 3, 4] or using constants [au.STREET_NUMBER, au.STREET_NAME, au.STREET_TYPTE]
        """
        if (len(street_address_types) != len(street_address_tokens)):
            raise Exception("street_address_types is a different length list than street_address_tokens")

        self.street_address_tokens = street_address_tokens
        self.street_address_types = street_address_types
    
        
    def get_street_address_tokens(self):
            return self.street_address_tokens
            
    def get_street_address_types(self):
        return self.street_address_types

    def compile_address_types(self):
        retval = {au.STREET_NUMBER: [], au.STREET_NAME: [], au.STREET_TYPE: [], au.SUITE: [], au.BUILDING_NUMBER: []}
    
        for type, token in zip(self.street_address_types, self.street_address_tokens):
    
            if type == au.STREET_NUMBER:
                retval[au.STREET_NUMBER].append(token)
            elif type == au.STREET_NAME:
                retval[au.STREET_NAME].append(token)
            elif type == au.STREET_TYPE:
                retval[au.STREET_TYPE].append(token)
            elif type == au.SUITE:
                retval[au.SUITE].append(token)
            elif type == au.BUILDING_NUMBER:
                retval[au.BUILDING_NUMBER].append(token)
    
        return retval

    def match_street_address(self, target_street_address):

        source = self.compile_address_types()
        target = target_street_address.compile_address_types()

        match_details = {au.STREET_NUMBER: None, au.STREET_NAME: None, au.STREET_TYPE: None, au.SUITE: None, au.BUILDING_NUMBER: None}

        match_details[au.STREET_NUMBER] = self.match_street_number(source[au.STREET_NUMBER], target[au.STREET_NUMBER])
        match_details[au.STREET_NAME] = self.match_street_number(source[au.STREET_NAME], target[au.STREET_NAME])
        match_details[au.STREET_TYPE] = self.match_street_number(source[au.STREET_TYPE], target[au.STREET_TYPE])

        match_details[au.SUITE] = self.match_street_number(source[au.SUITE], target[au.SUITE])
        match_details[au.BUILDING_NUMBER] = self.match_street_number(source[au.BUILDING_NUMBER], target[au.BUILDING_NUMBER])
        return match_details


    def match_street_number(self, a, b):
        return a == b

    def match_street_name(self, a, b):
        return a == b

    def match_street_type(self, a, b):
        return a == b

    def match_suite(self, a, b):
        return a == b

    def match_building_number(self, a, b):
        return a == b