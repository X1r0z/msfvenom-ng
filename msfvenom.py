#!/usr/bin/python

import os,sys
from payloads import payloads

def main():
    banner()
    output(payloads.keys())
    id = input(':')
    configure(payloads.keys()[id])

def banner():                        
    print '           ___'                       
    print ' _____ ___|  _|_ _ ___ ___ ___ _____'
    print '|     |_ -|  _| | | -_|   | . |     |'
    print '|_|_|_|___|_|  \_/|___|_|_|___|_|_|_|'
    print '         msfvenom payload generator'
    print

def output(msg):
    for i in msg:
        print msg.index(i),i

def configure(arch):
    output(payloads[arch].keys())
    id =input(':')
    generator(payloads[arch].keys()[id],arch)

def generator(payload,arch):
    args = ''
    for p in payloads[arch][payload]:
        args += p+'='+raw_input(p.upper()+':') + ' '
    command = 'msfvenom -p {0} {1} -f {2} > {3}'.format(payload,args,raw_input('FORMAT:'),raw_input('FILENAME:'))
    print '[*] Command:',command
    raw_input('[*] Press enter to run msfvenom \n')
    os.system(command)

main()
