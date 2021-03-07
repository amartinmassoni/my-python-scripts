#!/usr/bin/python3

import sys
import argparse
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def send_email( from_addr, to_addrs, subject, body ):
    msg = MIMEText( body, 'plain' )
    msg[ 'From' ] = from_addr
    msg[ 'To' ] = to_addrs
    msg[ 'Subject' ] = subject
    msg[ 'Date' ] = formatdate()

    srv = smtplib.SMTP( 'localhost' )
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

