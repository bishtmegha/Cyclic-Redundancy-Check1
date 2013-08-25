print "Enter the bit string: ",
BitString = raw_input()
length = len(BitString)
print "Enter the genrator bit string: ",
GeneString = raw_input()
for i in xrange(0, len(GeneString)):
    BitString = BitString + '0'
print "Appended bitstring: ", BitString
quo = BitString
for i in xrange(0,length):
    if (BitString[i] == '0'):
         for j in xrange(i,len(GeneString +1)):
             BitString[j]=str(int(BitString[j]))^0
    else:
         BitString[i] = str(int(BitString[i])^int(GeneString[0]))
         BitString[i+1]= str(int(BitString[i+1])^int(GeneString[1]))       
         BitString[i+2]= str(int(BitString[i+2])^int(GeneString[2]))
         BitString[i+3]= str(int(BitString[i+3])^int(GeneString[3]))
        
for i in xrange(length ,length + len(GeneString)-1):
    print "Transmitted String is :"+BitString
for i in xrange(length,length+length+len(GeneString)-1):
    print quo