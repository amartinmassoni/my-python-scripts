#!/usr/bin/python3

import time
import sys
import argparse
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate


def retry( attempts, delay, function, *positional, **named ):
    attempt = 0
    while attempt < attempts:
        attempt = attempt + 1
        try:
            return function( *positional, **named )
        except:
            if attempt < attempts:
                print( "Error at attempt", attempt, ":", sys.exc_info()[ 0 ], sys.exc_info()[ 1 ] )
            else:
                raise


def send_email( from_addr, to_addrs, subject, body ):
    msg = MIMEText( body, 'plain' )
    msg[ 'From' ] = from_addr
    msg[ 'To' ] = to_addrs
    msg[ 'Subject' ] = subject
    msg[ 'Date' ] = formatdate()

    srv = retry( 3, 10, smtplib.SMTP, 'localhost' )
    srv.send_message( msg )
    srv.quit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument( '--from', required = True, dest = 'from_' )
    parser.add_argument( '--to', required = True )
    parser.add_argument( '--subject', required = True )
    args = parser.parse_args()

    send_email( from_addr = args.from_, 
                to_addrs = args.to,
                subject = args.subject,
                body = sys.stdin.read() )

