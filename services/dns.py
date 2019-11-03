import dns.zone
import dns.query
import dns.rdatatype
import dns.tsigkeyring
import dns.update
import dns.opcode
from dns.exception import FormError

from config.config_helper import ConfigHelper
from models.record import Record


class DNSService:

    def __init__(self, cfg: ConfigHelper):
        self.__server_host = cfg.config['dns']['server_host']
        self.__key = cfg.config['tsig']['key']
        self.__connection_timeout = cfg.connection_timeout

    def transfer_zone(self, zone_name):

        try:

            transferred_zone = dns.zone.from_xfr(
                dns.query.xfr(self.__server_host, zone_name)
            )
            entries = {}

            for name, ttl, rdata in transferred_zone.iterate_rdatas():
                entry = self.__make_entry(ttl, rdata)

                if entries.get(str(name)):
                    entry = entries[str(name)] + entry

                entries[str(name)] = entry

            return entries

        except FormError as e:
            raise Exception(str(e))

    def add_record(self, record: Record):

        keyring = dns.tsigkeyring.from_text({
            record.zone: self.__key
        })

        action = dns.update.Update(record.zone, keyring=keyring)
        action.add(record.name, record.ttl, record.type, record.answer)
        response = dns.query.tcp(action, self.__server_host, timeout=self.__connection_timeout)

        return response.opcode() == dns.opcode.UPDATE

    def delete_record(self, record: Record):
        keyring = dns.tsigkeyring.from_text({
            record.zone: self.__key
        })

        action = dns.update.Update(record.zone, keyring=keyring)
        action.delete(record.name)
        response = dns.query.tcp(action,self.__server_host)

        return response.opcode() == dns.opcode.UPDATE

    @classmethod
    def __make_entry(cls, ttl, rdata):
        return [{
            'type': dns.rdatatype.to_text(rdata.rdtype),
            'ttl': str(ttl),
            'answer': str(rdata)
        }]






