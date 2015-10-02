def fileToListOfIntFl(stringNameOfFile):
	with open(stringNameOfFile, 'r') as content_file:
	    list = []
	    for line in content_file:
	    	stripped = line.rstrip().split(" ")
	    	for (i, ele) in enumerate(stripped):
	    		if float(ele).is_integer():
	    			stripped[i] = int(ele)
	    		else:
	    			stripped[i] = float(ele)
	    	list.append(stripped)
	return list

if __name__ == "__main__":
	print(fileToListOfIntFl('input.txt'))