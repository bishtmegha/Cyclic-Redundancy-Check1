print "enter the bit string",
BitString = raw_input()
length = len(BitString)
print "enter the genrator bit string",
GeneString = raw_input()
for i in xrange(0, len(GeneString)):
    BitString = BitString + '0'
print BitString
quo = BitString
for i in xrange(0,length):
    if (BitString[i] == '0'):
         for j in xrange(i,len(GeneString +1)):
             BitString[j]=BitString[j]^0
    else:
        BitString[i] = BitString[i]^GeneString[0]
        BitString[i+1]= BitString[i+1]^GeneString[1]         
        BitString[i+2]= BitString[i+2]^GeneString[2]
        BitString[i+3]= BitString[i+3]^GeneString[3]
        
for i in xrange(length ,length + len(GeneString)-1):
    print "Transmitted String is :"
for i in xrange(length,length+length+len(GeneString)-1):
    print quo     
        