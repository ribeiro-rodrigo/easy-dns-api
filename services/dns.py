from config.config_helper import ConfigHelper


class DNSService:

    def __init__(self, cfg: ConfigHelper):
        self.__server_host = cfg.config['dns']['server_host']

    def transfer_zone(self, zone_name):
        pass






