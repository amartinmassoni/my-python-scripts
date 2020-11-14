#!/usr/bin/python3

import openpyxl
import logging
import re

def postfix_maillog_excel( maillog, output ):
    preffix = "^([A-Z][a-z][a-z] [0-9 ][0-9] [0-9]{2}:[0-9]{2}:[0-9]{2}) ([^ ]+) postfix/([a-z]+)\[([0-9]+)\]\: "
    re_message = re.compile( preffix + "[0-9A-F]{10,12}\:" )
    re_connect = re.compile( preffix + "connect from (.+)$" )
    re_disconnect = re.compile( preffix + "disconnect from (.+)$" )
    re_statistics = re.compile( preffix + "statistics: (.+)$" )
    re_timeout = re.compile( preffix + "(timeout after .+)$" )
    re_daemon = re.compile( preffix + "daemon started -- (.+)$" )
    for filename in sorted( maillog ):
        logging.debug( "Reading file %s...", filename )
        for line in open( filename ):
            if re_message.search( line ):
                pass
            elif re_connect.search( line ):
                pass
            elif re_disconnect.search( line ):
                pass
            elif re_statistics.search( line ):
                pass
            elif re_timeout.search( line ):
                pass
            elif re_daemon.search( line ):
                pass
            else:
                print( line )
    logging.debug( "Saving to %s...", output )

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument( "maillog", nargs = "+" )
    parser.add_argument( "-o", "--output", required = True )
    args = parser.parse_args()
    postfix_maillog_excel( maillog = args.maillog, output = args.output )

