from geoip import geolite2
import ipaddress

def parse_json(file, parseType, countryList):
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
        successStrings = ['"server":["Blue']
    elif(parseType == "ftp"):
        testString = '"data":{"banner"'
        compLen = len(testString)
        successString = '"data":{"banner":"220 Blue Coat FTP Service'
        failString = '"data":{"ftp":{}'


    iterator = 0
    for i in range(len(lines)):
        temp = lines[i].split(",")
        length = len(temp)
        #print(temp[0])
        for j in range(length):
            compString = temp[j][:compLen]
            #print(compString)
            #print(temp[j][:10])
            if(compString == testString):
                #print("matched testString")
                if(temp[j][:len(successString)] == successString):
                    #print("FOUND:")
                    #print(temp)
                    for k in range(length):
                        #print(temp[k])
                        if(temp[k][:5] == '{"ip"'):
                            iterator = iterator + 1
                            match = geolite2.lookup(temp[k][7:-1])
                            parse_match(match, countryList)



                #print(temp[j])
                #if(temp[j][:len(failString)] != failString):
                    #print(temp[j])
                    # for k in range(len(temp[j])):
                    #     test = ["Blue Coat", "BlueCoat","bluecoat"]
                    #     for word in test:
                    #         if(temp[j][k:k+len(word)] == word):
                    #             print("FOUND: ")
                    #             print(temp)


                #writeTo.write("%s\n" % temp[j])
    #         for successString in successStrings:
    #             if(temp[j][:len(successString)] == successString):
    #                 print("FOUND: ")
    #                 for k in range(length):
    #                     #print(temp[k])
    #                     # writeToFile.write("%s\n"% temp[k])
    #                     if(temp[k][:5] == '{"ip"'):
    #                         iterator = iterator + 1
    #                         print(temp[k])
    #                         match = geolite2.lookup(temp[k][7:-1])
    #                         print(match)
    # # writeToFile.close()
    print(iterator)

def parse_match(match, countryList):
    components = str(match)
    #print(components)
    components = components.split(" ")
    for comp in components:
        if(len(comp) == 12):
            val = str(len(comp))
            #print(str(comp[9:-1]))
            if(comp[9:-1] not in countryList):
                countryList.append(comp[9:-1])



    #writeTo.close()
def main():
    fileList = ["censys-21-ftp-banner-full_ipv4-results.json"]
    countryList = []
    #fileList = ["ftp-scan1.json","ftp-scan2.json","ftp-scan3.json","ftp-scan4.json","ftp-scan5.json","ftp-scan6.json","ftp+auth-scan7.json","ftp+auth-scan8.json", "ftp+auth-scan9.json","ftp-scan10.json", "ftp-scan11.json", "ftp-scan12.json"]
    #testIran1.json","testIran2.json","testIran3.json","testIran4.json","testIran5.json","testIran6.json","testIran7.json","testIran8.json","testIran9.json","testIran10.json","testIran11.json"]
    #fileList = ["banners-test-http80tes21.json"]
    #queryList =['"server":["BlueCoat','"server":["ProxySG','"server":["PacketShaper','"server":["Packeteer']
    for index in range(len(fileList)):
        print(fileList[index])
        parse_json(fileList[index], "ftp", countryList)

    for country in countryList:
        print(country)

# files = ["banners-test-http.json","banners-test-http8081.json"]
# types = ["ip","body","data","headers","server","authenticate"]
#
# for i in range(len(files)):
#     for j in range (len(types)):
#         parse_json(files[i], types[j])

main()
