#!/usr/bin/python
import logging

import sys
sys.path.append('lib')

from stock import Stock
from util import setup_logging

setup_logging()

stock = Stock()

report = stock.build_report()

for stn in report.stns():
    logging.info("Station: %s", stn.name)
    for loc in stn.locs():
        logging.info("  Location: %s", loc.name)
        for item in loc.items():
            output = []
            output.append("    %s: %d" % (item.name, item.have))
            if item.target > 0:
                output.append("/%d" % item.target)
                output.append(" (%.1f%%)" % item.percent)
            logging.info("".join(output))
