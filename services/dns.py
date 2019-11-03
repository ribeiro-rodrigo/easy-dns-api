import dns.zone
import dns.query
import dns.rdatatype
from dns.exception import FormError

from config.config_helper import ConfigHelper


class DNSService:

    def __init__(self, cfg: ConfigHelper):
        self.__server_host = cfg.config['dns']['server_host']
        print(cfg.avaliable_zones)

    def transfer_zone(self, zone_name):

        try:

            transferred_zone = dns.zone.from_xfr(dns.query.xfr(self.__server_host, zone_name))
            entries = {}

            for name, ttl, rdata in transferred_zone.iterate_rdatas():
                entry = self.__make_entry(ttl, rdata)

                if entries.get(str(name)):
                    entry = entries[str(name)] + entry

                entries[str(name)] = entry

            return entries

        except FormError as e:
            raise Exception(str(e))


    @classmethod
    def __make_entry(cls, ttl, rdata):
        return [{
            'type': dns.rdatatype.to_text(rdata.rdtype),
            'ttl': str(ttl),
            'answer': str(rdata)
        }]






