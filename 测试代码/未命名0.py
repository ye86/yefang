# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:05:58 2018

@author: yefang
"""

import nmap
import argparse

def nmapScan(Host, Port):
    # 调用nmap的PortScanner类
    nm = nmap.PortScanner()
    # 使用scan方法进行扫描
    results = nm.scan(Host, str(Port))
    state = results['scan'][Host]['tcp'][Port]['state']
    print("[+] {} tcp/{} {}".format(Host, Port, state))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='192.168.10.187', help="Host like: 192.168.3.1")
    parser.add_argument('-p', dest='80', nargs='+', type=int, help="Port like: 80 443 21")
    args = parser.parse_args()
    Host = '192.168.10.187' #args.Host
    Ports = [x for x in range(1,61000)] #args.Ports

    for Port in Ports:
        nmapScan(Host,Port)

if __name__ == '__main__':
    main()