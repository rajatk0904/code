def riffle_shuffle(sentence):
	lis_=sentence.split()
	len2=len(lis_)/2
	len1=len(lis_)-len2
	listB = lis_[:len1]
	listC=lis_[len1:]
	str_=""
	for i in range(0,len(listC)):
		str_=str_+" "+listB[i]+" "+listC[i]
	if(len(listC)<len(listB)):
		str_=str_+" "+listB[i+1]
	return str_[1:]
x=raw_input()
print riffle_shuffle(x)