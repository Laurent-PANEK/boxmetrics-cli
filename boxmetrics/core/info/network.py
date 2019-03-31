import psutil
import time
import re
import copy
from socket import AF_INET, AF_INET6, SOCK_STREAM, SOCK_DGRAM
from .base import Info


class Network(Info):
    af_map = {AF_INET: "IPv4", AF_INET6: "IPv6", psutil.AF_LINK: "MAC"}

    duplex_map = {
        psutil.NIC_DUPLEX_FULL: "full",
        psutil.NIC_DUPLEX_HALF: "half",
        psutil.NIC_DUPLEX_UNKNOWN: "?",
    }

    proto_map = {
        (AF_INET, SOCK_STREAM): "tcp",
        (AF_INET6, SOCK_STREAM): "tcp6",
        (AF_INET, SOCK_DGRAM): "udp",
        (AF_INET6, SOCK_DGRAM): "udp6",
    }

    def __init__(self, *args):
        super(Network, self).__init__(*args)

    def config(self):
        netaddrs = psutil.net_if_addrs()
        netstats = psutil.net_if_stats()
        conf = dict()

        for k, d in netaddrs.items():
            netstats[k] = netstats[k]._asdict()
            netstats[k]["duplex"] = Network.duplex_map[netstats[k]["duplex"]]
            netstats[k]["speed"] = str(netstats[k]["speed"]) + "MB"
            conf[k] = netstats[k]
            for i, a in enumerate(d):
                netaddrs[k][i] = a._asdict()
                netaddrs[k][i]["family"] = Network.af_map[netaddrs[k][i]["family"]]
            conf[k]["addrs"] = netaddrs[k]
        return conf

    def stats(self):
        stats = self.__get_netstats(1)
        return self.__format_netstats(stats)

    def conns(self):
        sockets = psutil.net_connections("all")

        for i, con in enumerate(sockets):
            sockets[i] = con._asdict()
            del sockets[i]["fd"]
            sockets[i]["proto"] = Network.proto_map[
                (sockets[i]["family"], sockets[i]["type"])
            ]
            del sockets[i]["family"]
            del sockets[i]["type"]
            sockets[i]["laddr"] = dict(
                addr=sockets[i]["laddr"][0], port=sockets[i]["laddr"][1]
            )
            try:
                sockets[i]["raddr"] = dict(
                    addr=sockets[i]["raddr"][0], port=sockets[i]["raddr"][1]
                )
            except:
                sockets[i]["raddr"] = dict()

        return sockets

    def all(self):
        stats = self.stats()
        config = self.config()
        conns = self.conns()
        return dict(config=config, stats=stats, connections=conns)

    def __get_netstats(self, interval):
        tot_before = psutil.net_io_counters()
        pnic_before = psutil.net_io_counters(pernic=True)

        time.sleep(interval)

        tot_after = psutil.net_io_counters()
        pnic_after = psutil.net_io_counters(pernic=True)

        total = (tot_before, tot_after)
        pnic = self._zip_dict(pnic_before, pnic_after)

        return dict(total=total, pnic=pnic)

    def __format_netstats(self, netstats: dict):

        netstats["total"] = self.__format_nic(*netstats["total"])

        for key, data in netstats["pnic"].items():
            netstats["pnic"][key] = self.__format_nic(*data)

        return netstats

    def __format_nic(self, before, after):
        before = before._asdict()
        after = after._asdict()
        nic = dict()

        for key, data in after.items():
            if re.match(r"^bytes_", key):
                nic[key + "_per_sec"] = self._convert_bytes_per_second(
                    after[key] - before[key]
                )
                nic[key] = self._convert_bytes(data)
            else:
                nic[key] = after[key]

        return nic


NetworkInst = Network()
