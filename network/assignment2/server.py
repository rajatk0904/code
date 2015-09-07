from socket import *
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
serverPort = int(raw_input('Server port: '))
serverSocket = socket(AF_INET6,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	print addr
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = riffle_shuffle(sentence)
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()