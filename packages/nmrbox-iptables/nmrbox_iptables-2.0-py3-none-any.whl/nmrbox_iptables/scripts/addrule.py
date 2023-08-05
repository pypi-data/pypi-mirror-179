#!/usr/bin/env python3
import argparse
import configparser
import logging

import yaml

from nmrbox_iptables import nblogger, INPUT
from nmrbox_iptables.iptables import Manager


class CallIptables:

    def __init__(self, config):
        self.config = config

    def execute(self):
        self.test = self.config.get('test', False)
        if self.test and nblogger.getEffectiveLevel() > logging.INFO:
            nblogger.setLevel(logging.INFO)
        nblogger.info(f"test: {self.test}")
        if (m := self.config.get('multi', None)) is not None:
            self._multi(m)
            return
        print("No actions found")

    def _multi(self, m):
        comment = m['comment']
        ports = m['ports']
        chain_first = m.get('chain first',False)
        if (chain := m.get('chain', None)) is None:
            chain = INPUT
        insert = m.get('first accept', False)
        nblogger.info(f"multi: {chain} chain first {chain_first} {ports} beginning {insert} # {comment}")
        if self.test:
            return
        with Manager('addrule script',makesubchain=False) as mgr:
            if chain:
                mgr.setup_chain(chain,last_accept=not chain_first)
            mgr.add_accept_tcp_multi(ports,chain,insert,comment)


def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('yaml')
    parser.add_argument('-l', '--loglevel', default='WARN', help="Python logging level")

    args = parser.parse_args()
    nblogger.setLevel(getattr(logging, args.loglevel))
    with open(args.yaml) as f:
        c = yaml.safe_load(f)
    cipt = CallIptables(c)
    cipt.execute()


if __name__ == "__main__":
    main()
