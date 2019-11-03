
class Record:
    def __init__(self, record_map: dict, zone, avaliable_zones: list):
        self.__name = record_map.get('recordName', None)
        self.__type = record_map.get('recordType', None)
        self.__ttl = record_map.get('ttl', None)
        self.__answer = record_map.get('answer', None)
        self.__zone = zone
        self.__avaliable_zones = avaliable_zones

    @property
    def name(self):
        return self.__name.split('.')[0]

    @property
    def full_name(self):
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
        return self.__zone

    def is_valid_zone(self):
        return self.__zone in self.__avaliable_zones


