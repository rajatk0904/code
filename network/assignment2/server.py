from socket import *
buffer_size=1024
def chunkstring(string, length):
	return [string[0+i:length+i] for i in range(0, len(string), length)]
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
	length = connectionSocket.recv(buffer_size)
	#print length
	str_=""
	for k in range(0,int(length)):
		mod_str = connectionSocket.recv(buffer_size)
	#	print mod_str
		str_=str_+mod_str
	#str_=rest+str_
	#print str_
	riffle_sent = riffle_shuffle(str_)
	#print riffle_sent
	riffled_list=chunkstring(riffle_sent,buffer_size)
	y=len(riffled_list)
	#print y
	z="0"*(buffer_size-len(str(y)))+str(y)
	connectionSocket.send(z)
	#print y
	for riffle in riffled_list:
		connectionSocket.send(riffle)
	connectionSocket.close()