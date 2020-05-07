from api.api_reader import ApiReader

class LocationApi:
    def __init__(self, latitude, longitude):
        self.locationApiReader = ApiReader("https://nominatim.openstreetmap.org/reverse?format=json&lat=%f&lon=%f" %
                                           (latitude, longitude))

    def get_location(self):
        """
        Reads the current location using the locationApiReader and returns the parsed result
        :return:  Location
        """
        location = self.locationApiReader.get()
        return self.parse_location(location)

    @classmethod
    def parse_location(cls, location):
        """
        :param location: location retrieved by the api
        :return: Location
        """
        if location is None:
            return None
        location = location.get('address')
        number = location.get('house_number')
        street = location.get('road')
        address = location.get('suburb')
        municipality = location.get('town')
        state = location.get('state')
        postcode = location.get('postcode')
        country = location.get('country')
        countryCode = location.get('country_code')
        return cls.Location(number, street, address, municipality, state, postcode, country, countryCode)

    class Location:
        def __init__(self, number, street, address, municipality, state, country, zipCode, countryCode):
            self.number = number
            self.street = street
            self.address = address
            self.municipality = municipality
            self.state = state
            self.country = country
            self.postcode = zipCode
            self.countryCode = countryCode
