import dns.zone
import dns.query
import dns.rdatatype
import dns.tsigkeyring
import dns.resolver
import dns.update
import dns.opcode
from dns.exception import FormError

from config.config_helper import ConfigHelper
from models.record import Record


class DNSService:

    def __init__(self, cfg: ConfigHelper):
        self.__server_host = cfg.server_host
        self.__key = cfg.tsig_key
        self.__connection_timeout = cfg.connection_timeout

    def transfer_zone(self, zone_name):

        try:

            transferred_zone = dns.zone.from_xfr(
                dns.query.xfr(self.__server_host, zone_name)
            )
            records = []

            for name, ttl, rdata in transferred_zone.iterate_rdatas():
                entry = self.__make_entry(name, ttl, rdata)
                records.append(entry)

            return records

        except FormError as e:
            raise Exception(str(e))

    def resolve_domain(self, domain, type_record='A'):

        try:
            resolver = self.__make_resolver()
            return resolver.query(domain, type_record)
        except dns.resolver.NXDOMAIN as e:
            return None

    def add_record(self, record: Record):

        action = self.__make_action(record)
        action.add(record.name, record.ttl, record.type, record.answer)
        response = self.__execute_query(action)

        return response.opcode() == dns.opcode.UPDATE

    def delete_record(self, record: Record):

        action = self.__make_action(record)
        action.delete(record.name)
        response = self.__execute_query(action)

        return response.opcode() == dns.opcode.UPDATE

    def update_record(self, record: Record):

        action = self.__make_action(record)
        action.replace(record.name, record.ttl, record.type, record.answer)

        response = self.__execute_query(action)

        return response.opcode() == dns.opcode.UPDATE

    def __make_action(self, record: Record):
        keyring = dns.tsigkeyring.from_text({
            record.zone: self.__key
        })

        return dns.update.Update(record.zone, keyring=keyring)

    def __execute_query(self, action):
        return dns.query.tcp(action, self.__server_host)

    def __make_resolver(self):
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [self.__server_host]
        return resolver

    @classmethod
    def __make_entry(cls, name, ttl, rdata):
        return {
            'name': str(name),
            'type': dns.rdatatype.to_text(rdata.rdtype),
            'ttl': str(ttl),
            'answer': str(rdata)
        }





