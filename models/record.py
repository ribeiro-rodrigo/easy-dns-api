
class Record:
    def __init__(self, record_map: dict, avaliable_zones: list):
        self.__name = record_map['recordName']
        self.__type = record_map['recordType']
        self.__ttl = record_map['ttl']
        self.__answer = record_map['answer']
        self.__avaliable_zones = avaliable_zones

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def ttl(self):
        return self.__ttl

    @property
    def answer(self):
        return self.__answer

    @property
    def zone(self):
        zone_filtered = list(
            filter(lambda domain: self.__name.endswith(domain), self.__avaliable_zones)
        )

        return zone_filtered[0] if zone_filtered else None

    def is_valid_zone(self):
        return list(
            filter(lambda domain: self.__name.endswith(domain), self.__avaliable_zones)
        )


