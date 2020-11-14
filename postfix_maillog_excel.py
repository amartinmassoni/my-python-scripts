#!/usr/bin/python3

import openpyxl
import logging
import time
import re

class PostFixMessage:
    def __init__( self, pf_id, timestamp ):
        self.pf_id = pf_id
        self.from_timestamp = timestamp
        self.to_timestamp = timestamp
        self.items = []

    def add_line( self, timestamp, text ):
        self.to_timestamp = max( self.to_timestamp, timestamp )
        if text != "removed":
            self.items.append( text.split( ", " ) )

def postfix_maillog_excel( maillog, output ):
    preffix = "^([A-Z][a-z][a-z] [0-9 ][0-9] [0-9]{2}:[0-9]{2}:[0-9]{2}) [^ ]+ postfix/[a-z]+\[[0-9]+\]\: "
    re_message = re.compile( preffix + "([0-9A-F]{10,12}): (.+)$" )
    re_connect = re.compile( preffix + "connect from (.+)$" )
    re_disconnect = re.compile( preffix + "disconnect from (.+)$" )
    re_statistics = re.compile( preffix + "statistics: (.+)$" )
    re_timeout = re.compile( preffix + "(timeout after .+)$" )
    re_daemon = re.compile( preffix + "daemon started -- (.+)$" )
    current_year = time.strftime( "%Y" ) + " "
    pf_ids = []
    pf_messages = {}
    for filename in sorted( maillog ):
        logging.debug( "Reading file %s...", filename )
        for line in open( filename ):
            r1 = re_message.search( line )
            if r1:
                timestamp = time.strptime( current_year + r1.group( 1 ), "%Y %b %d %H:%M:%S" )
                pf_id = r1.group( 2 )
                if pf_id not in pf_messages:
                    pf_ids.append( pf_id )
                    pf_messages[ pf_id ] = PostFixMessage( pf_id, timestamp )
                pf_messages[ pf_id ].add_line( timestamp, r1.group( 3 ) )
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
    return ( pf_ids, pf_messages )

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.description = "Process one or more postfix maillog files, and return one Excel file"
    parser.add_argument( "maillog", nargs = "+", help = "Input: maillog files" )
    parser.add_argument( "-o", "--output", help = "Output: Excel file", required = True )
    args = parser.parse_args()
    pf_ids, pf_messages = postfix_maillog_excel( maillog = args.maillog, output = args.output )
