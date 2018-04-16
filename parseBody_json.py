def parse_body(file):
    f=open(file)

    name = "clean"+file
    results = open(name, "w+")
    lines = f.readlines()
    for i in range(len(lines)):
        comp = '"body":"\u003c!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\"\u003e\n\u003chtml\u003e\u003chead\u003e\n\u003ctitle\u003e400 Bad Request'
        comp1 = '"body":"\u003c!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\"\u003e\n\u003chtml\u003e\u003chead\u003e\n\u003ctitle\u003e400 Bad Request\u003c'
        temp = lines[i][:len(comp)]
        temp1 = lines[i] [:len(comp1)]
        if((temp != comp) and (temp1 != comp1)):
            print("Error")
            results.write("%s\n" % lines[i])

    results.close


parse_body("parseBody-banners-test-http2.txt")
