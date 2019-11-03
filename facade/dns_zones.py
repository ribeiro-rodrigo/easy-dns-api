from services.dns import DNSService
from config.config_helper import ConfigHelper


class DNSZonesFacade:
    def __init__(self, dns_service: DNSService, cfg: ConfigHelper):
        self.__dns_service = dns_service
        self.__avaliable_zones = cfg.avaliable_zones

    def list_all_zones(self):

        all_zones = []

        for zone_name in self.__avaliable_zones:
            records = self.__dns_service.transfer_zone(zone_name)
            all_zones.append({"zone": zone_name, "records": records})

        return all_zones

