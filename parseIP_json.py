from geoip import geolite2
import ipaddress

def parseIP_locations(file):

    f=open(file)
    name = "ipLocations-"+file
    ip_locs= open(name, "w+")
    lines = f.readlines()
    for i in range(len(lines)):
        print(lines[i][7:-2])
        match = geolite2.lookup(lines[i][7:-2])
        ip_locs.write("%s\n"% match)

    ip_locs.close()

parseIP_locations("ip-banners-test-http8081.txt")
