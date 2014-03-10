#! /usr/bin/python3
txtFile = open('wwfl.txt', 'r')
compressedFile = open('smallTxt.bin', 'wb')
wordBlock = []
wordBlockSize = 4
wordBlockCount = 0

def createBlock(wordBlock):
	        finalSlice = 0
	#       print(wordBlock)
	        for wordSlice in range(len(wordBlock[0])+1):
       #       print("\n")
	                if finalSlice != 0:
	                        break
	                for word in range(1, len(wordBlock)):
 #               print(wordBlock[0][:wordSlice],wordBlock[word][:wordSlice])
								                        if wordBlock[0][:wordSlice] != wordBlock[word][:wordSlice]:
																		                                finalSlice = wordSlice - 1
																						                                break
																									        if finalSlice == 0:

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
