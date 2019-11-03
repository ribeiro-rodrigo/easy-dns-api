import dns.zone
import dns.query
import dns.rdatatype
import dns.tsigkeyring
import dns.update
from dns.exception import FormError

from config.config_helper import ConfigHelper


class DNSService:

    def __init__(self, cfg: ConfigHelper):
        self.__server_host = cfg.config['dns']['server_host']
        self.__avaliable_zones = cfg.avaliable_zones
        self.__key = cfg.config['tsig']['key']
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

    def add_record(self, record):

        zone_from_record = self.__get_zone_from_record(record)

        keyring = dns.tsigkeyring.from_text({
            zone_from_record: self.__key
        })
        print(self.__key)
        action = dns.update.Update(zone_from_record, keyring=keyring)
        action.add(record['recordName'], record['ttl'], record['recordType'], record['answer'])
        response = dns.query.tcp(action, self.__server_host)

        print(response)

    def __get_zone_from_record(self, record):
        zone_filtered = list(
            filter(lambda domain: record['recordName'].endswith(domain), self.__avaliable_zones)
        )

        return zone_filtered[0] if zone_filtered else None

    @classmethod
    def __make_entry(cls, ttl, rdata):
        return [{
            'type': dns.rdatatype.to_text(rdata.rdtype),
            'ttl': str(ttl),
            'answer': str(rdata)
        }]






