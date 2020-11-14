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



# Nov 13 06:53:00 pasarela postfix/pickup[56646]: EF6546014B: uid=0 from=<root>
# Nov 13 06:53:01 pasarela postfix/cleanup[62996]: EF6546014B: message-id=<20201113055300.EF6546014B@pasarela.wpsnetwork.com>
# Nov 13 06:53:01 pasarela postfix/qmgr[1359]: EF6546014B: from=<root@pasarela.wpsnetwork.com>, size=5207, nrcpt=1 (queue active)
# Nov 13 06:53:02 pasarela postfix/smtp[62998]: EF6546014B: to=<seville.dbateam@onyxcentersource.com>, relay=smtp.socketlabs.com[142.0.191.0]:25, delay=2, delays=0.08/0.17/1.3/0.41, dsn=2.0.0, status=sent (250 2.0.0 Message received and queued as b30000002c3c62.)
# Nov 13 06:53:02 pasarela postfix/qmgr[1359]: EF6546014B: removed
