#! /usr/bin/python3

txtFile = open('wwfl.txt', 'r')
compressedFile = open('smallTxt.bin', 'wb')
wordBlock = []
wordBlockSize = 4
wordBlockCount = 0


def createBlock(wordBlock):
	finalSlice = 0
#	print(wordBlock)
	for wordSlice in range(len(wordBlock[0])+1):
	#	print("\n")
		if finalSlice != 0:
			break
		for word in range(1, len(wordBlock)):
	#		print(wordBlock[0][:wordSlice],wordBlock[word][:wordSlice])
			if wordBlock[0][:wordSlice] != wordBlock[word][:wordSlice]:
				finalSlice = wordSlice - 1
				break
	if finalSlice == 0:
		finalSlice = len(wordBlock[0])
	wordBlock[0] = wordBlock[0][:finalSlice] + '@' + wordBlock[0][finalSlice:]
	for word in range(1,len(wordBlock)):
		wordBlock[word] =  '@' + wordBlock[word][finalSlice:]


#	print(wordBlock)
#	print(finalSlice)
#	x = input()
	for word in wordBlock:
		compressedFile.write(bytes([len(word)]))
		compressedFile.write(word.encode('ascii'))
	return
def charstrip(idx,termlyst):
        masterTerm = idx
        print("MasterTerm is: ",termlyst[masterTerm])
        x = input()
        if idx+1 < len(termlyst):
                while termlyst[masterTerm][0] == termlyst[idx+1][0] and len(termlyst[idx+1]) > 1:
                        #print(termlyst[idx][0], str(idx))
                        termlyst[idx+1] = termlyst[idx+1][1:]
                        if idx+2 < len(termlyst):
                                idx += 1
                        else:
                                break
                print("end of loop")        
                termlyst[masterTerm] = termlyst[masterTerm][0] + str(idx-masterTerm) + termlyst[masterTerm][1:]
                for term in range(masterTerm, masterTerm +20):
                        print(termlyst[term])
                print("Final Term is: ", termlyst[idx])
                if idx+1 < len(termlyst):
                        charstrip(idx +1, termlyst)
                else:
                        print("done")
        else:
                print("done")
        
                
termlyst = []
for word in txtFile:
        termlyst.append(word)
idx = 0
charstrip(idx, termlyst)

    
##	word = word[:-1]	
##	wordBlock.append(word)
##	wordBlockCount += 1
##	if wordBlockCount == 2 and len(wordBlock[0]) > 1 and wordBlock[0][:2] != wordBlock[1][:2]:
###		print(wordBlock[0][:2], wordBlock[1][:2])
###		x = input()
##		compressedFile.write(bytes([len(wordBlock[0])]))
##		compressedFile.write(wordBlock[0].encode('ascii'))		
##		wordBlock[0] = wordBlock[1]
##		wordBlock.pop()
##		wordBlockCount = 1
##
##	if wordBlockCount == wordBlockSize:
##		createBlock(wordBlock)
##		wordBlock = []
##		wordBlockCount = 0

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
