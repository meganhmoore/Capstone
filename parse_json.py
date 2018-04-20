from geoip import geolite2
import ipaddress

def parse_json(file, parseType, found_devices):
    f=open(file)
    # writeToFile = open("BlueCoatResults.txt","w+")
    name = file[:-5 ]
    name = parseType+"-"+name+".txt"

    # writeTo = open(name, "w+")

    lines=f.readlines()
    if(parseType == "ip"):
        compLen = 6
        testString = '{"ip":'
    elif(parseType == "body"):
        compLen = 6
        testString = '"body"'
    elif(parseType == "data"):
        compLen = 6
        testString = '"data"'
    elif(parseType == "headers"):
        compLen= 9
        testString = '"headers"'
    elif(parseType == "authenticate"):
        compLen = 18
        testString = '"www_authenticate"'
    elif(parseType == "server"):
        compLen = 8
        testString = '"server"'
        successStrings = ['"server":"Blue"']
        testBrands = ["McAfee","mcafee", "smartfilter", "SmartFilter", "netsweeper", "NetSweeper"]
    elif(parseType == "ftp"):
        testString = '"data":{"ftp":{'
        compLen = len(testString)
        successString = '"data":{"ftp":{"banner":"220 Blue Coat FTP Service"'
        failString = '"data":{"ftp":{}'


    iterator = 0
    for i in range(len(lines)):
        temp = lines[i].split(",")
        length = len(temp)
        #print(temp[0])
        for j in range(length):
            compString = temp[j][:compLen]
            #print(temp[j][:10])
            #if(compString == testString):
                #writeTo.write("%s\n" % temp[j])
            test_strings =["McAfee Web Gateway","mcafee web gateway", "smartfilter", "SmartFilter", "netsweeper", "NetSweeper"]
            for string in test_strings:
                for m in range(len(temp[j])-len(string)):
                    #print(temp[j][m:m+len(string)])

                    if(temp[j][m:m+len(string)] == string):
                        #print("FOUND: ")

                        for k in range(length):
                            if(len(temp[k]) < 150):
                                #print(temp[k])
                                if(temp[k][:5] == '{"ip"'):
                                    ip = temp[k][7:-1]
                                    #match = geolite2.lookup(ip)
                                    #print(match)
                                    if not(ip in found_devices):
                                        #print("NEW")
                                        iterator = iterator + 1
                                        found_devices[ip]=string
                                    break

                        # writeToFile.write("%s\n"% temp[k])
                        # if(temp[k][:5] == '{"ip"'):

                        #     print(temp[k])
                        #     match = geolite2.lookup(temp[k][7:-1])
                        #     print(match)
    # writeToFile.close()
    print(iterator)


    #writeTo.close()
fileList = ["banners-test-http.json","banners-test-http8081.json","banners-test-http8081test2.json","banners-test-http8081test3.json","banners-test-http8081test4.json","banners-test-http8081test5.json","banners-test-http8081test6.json","banners-test-http8081test7.json","banners-test-http8081test8.json","banners-test-http8081test9.json","banners-test-http8081test10.json"]
fileListTwo = ["cali_zgrab_ftp_220.json","ftp-scan1.json","ftp-scan2.json","ftp-scan3.json", "ftp-scan4.json","ftp-scan5.json","ftp-scan6.json","ftp-scan7.json","ftp-scan8.json","ftp-scan9.json","ftp-scan10.json","ftp-scan11.json","ftp-scan12.json","ftp-scan13.json","ftp-scan4.json","ftp+auth-scan7.json","ftp+auth-scan8.json","ftp+auth-scan9.json"]
#testIran1.json","testIran2.json","testIran3.json","testIran4.json","testIran5.json","testIran6.json","testIran7.json","testIran8.json","testIran9.json","testIran10.json","testIran11.json"]
#fileList = ["banners-test-http80tes21.json"]
#queryList =['"server":["BlueCoat','"server":["ProxySG','"server":["PacketShaper','"server":["Packeteer']


found_devices = {}
for index in fileList:
    print(index)
    parse_json(index, "server",found_devices)
for el in found_devices:
    print(geolite2.lookup(el))

found_devices = {}
for ind in fileListTwo:
    print(ind)
    parse_json(ind, "ftp",found_devices)

for el in found_devices:
    print(geolite2.lookup(el))

# files = ["banners-test-http.json","banners-test-http8081.json"]
# types = ["ip","body","data","headers","server","authenticate"]
#
# for i in range(len(files)):
#     for j in range (len(types)):
#         parse_json(files[i], types[j])
