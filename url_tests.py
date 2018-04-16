import time
import urlparse
import requests
import csv
from adapters import ForcedIPHTTPSAdapter

hosts = ['65.248.13.115','14.36.208.167','192.40.252.46','193.188.73.147','61.247.254.122','192.40.252.51','192.40.252.40','210.120.11.154','133.91.8.130','61.88.183.119','186.225.113.78','123.124.1.2','43.253.220.239','133.91.8.130','58.32.235.185','218.80.232.44','212.107.116.228','65.248.13.219','204.193.7.62','212.76.70.226','192.40.252.54','65.248.13.224','213.34.210.37','210.13.105.23',
'210.89.93.10','192.40.252.52','192.40.252.53','212.107.116.230','222.66.97.75','192.40.252.77','207.254.178.17','88.85.228.90','65.248.13.114','65.248.13.218','192.40.252.50']

def parse_urls():

    f = csv.reader(open('global.csv'))


    for host in hosts:
        print(host)

        for row in f:
            if(row[0] != 'url'):
                #if it is an http turn it into an https
                if(row[0][:5]!= 'https'):
                    temp='https'+row[0][4:-1]
                else:
                    temp = row[0][:-1]

                headers = temp[8:]
                print(headers)

                session = requests.Session()
                temphost = host+':8081'
                session.mount(temp, ForcedIPHTTPSAdapter(dest_ip=host))
                compString = "Access Denied"
                try:
                    r = session.get(temp, headers={'Host':headers},timeout = 1) #allow_redirects = False,
                    #r=requests.get(temp, timeout=1)

                except requests.exceptions.Timeout as e:
                    print("Timeout Error")
                        #break
                except requests.exceptions.ConnectionError as c:
                    print("Connection Error")
                        #break

                if((r.text[20:(20+len(compString))]) == compString):
                    print("Not Allowed!")

                else:
                    # print("Success"+row[0]+host)
                    print(r)



parse_urls()
