example1 = 'D2FE28'
example2 = '38006F45291200'
example3 = 'EE00D40C823060'
example4 = '8A004A801A8002F478'
example5 = '620080001611562C8802118E34'
example6 = 'C0015000016115A2E0802F182340'
example7 = 'A0016C880162017C3686B18A3D4780'
example8 = 'C200B40A82'
example9 = '04005AC33890'
example10 = '880086C3E88112'
example11 = 'CE00C43D881120'
example12 = 'D8005AC2A8F0'
example13 = 'F600BC2D8F'
example14 = '9C005AC2F8F0'
example15 = '9C0141080250320F1802104A08'
with open('input.txt') as file:
    instruction = file.readline()
import numpy
string = ''
for i in instruction:
    substring = bin(int(i,16))[2:]
    while len(substring) < 4:
        substring = '0' + substring
    string += substring
print(string)

def parse(string):
    # print('Parse is called on ', string)
    if '1' not in string:
        return [], [], string
    packetVersion = string[0:3]
    typeID = string[3:6]
    
    packetVersionList = [packetVersion]
    literalIntList = []
    if typeID == '100':
        #literal integer
        endOfPacket = False
        string = string[6:]
        literalInt = ''
        while not endOfPacket:
            if string[0] == '0':
                endOfPacket = True
            literalInt += string[1:5]
            string = string[5:]
        actualInt = int(literalInt, 2)
        literalIntList.append(actualInt)

        return packetVersionList, literalIntList, string
        # nextPacketVersionList, nextPacketLiteralIntList = parse(string)
        # packetVersionList += nextPacketVersionList
        # literalIntList.append(nextPacketLiteralIntList)

    else:
        #subpackets
        lenTypeID = string[6]
        if lenTypeID == '0':
            lenOfSubstring = int(string[7:7+15], 2)
            restOfString = string[7+15+lenOfSubstring:]
            string = string[7+15:7+15+lenOfSubstring]
            while '1' in string:
                subPacketVersionList, subPacketLiteralIntList, string = parse(string)
                packetVersionList += subPacketVersionList
                literalIntList += subPacketLiteralIntList
            # restOfStringVersionList, restOfStringLiteralList, string2 = parse(restOfString)
            # packetVersionList += restOfStringVersionList
            
            # literalIntList += restOfStringLiteralList
            string = restOfString
            # return packetVersionList, literalIntList, restOfString
        elif lenTypeID == '1':
            numOfSubpackets = int(string[7:7+11],2)
            numOfSubpacketsCounted = 0
            # while numOfSubpacketsCounted < numOfSubpackets:
            #     pass
            ids = []
            literals = []
            string = string[7+11:]
            for _ in range(numOfSubpackets):
                iss, ls, string = parse(string)
                ids += iss
                literals += ls

            # subPacketVersionList, subPacketLiteralIntList, string = parse(string[7+11:])
            # packetVersionList += subPacketVersionList
            packetVersionList += ids
            literalIntList += literals
    
    if typeID == '000':
        #sum
        # print('we are summing', literalIntList)
        summ =sum(i for i in literalIntList) 
        literalIntList = [summ]
    elif typeID == '001':
        product = numpy.prod(literalIntList)
        literalIntList = [product]
    elif typeID == '010':
        minn = min(literalIntList)
        literalIntList = [minn]
    elif typeID == '011':
        maxx = max(literalIntList)
        literalIntList = [maxx]
    elif typeID == '101':
        gt = int(literalIntList[0]>literalIntList[1])
        literalIntList = [gt]
    elif typeID == '110':
        lt = int(literalIntList[0]<literalIntList[1])
        literalIntList = [lt]
    elif typeID == '111':
        eq = int(literalIntList[0]==literalIntList[1])
        literalIntList = [eq]
    return packetVersionList, literalIntList, string
# print(int(parse(string)[1][0],2))
# print(parse(string))
# ids = []
# literals = []
# while '1' in string:
ids, literals, string = parse(string)
# ids += iss
# literals += ls
print(ids, literals, string)
print(sum(int(id,2) for id in ids))
# print(parse('110100010100101001000100100'))