from socket import *
buffer_size=1024
def chunkstring(string, length):
	return [string[0+i:length+i] for i in range(0, len(string), length)]

serverName = raw_input('Server IP: ')
serverPort = int(raw_input('Server Port: '))

message = raw_input('Input sentence: ')
chunked_strings=chunkstring(message,buffer_size)
y=len(chunked_strings)
clientSocket = socket(AF_INET6, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
z="0"*(buffer_size-len(str(y)))+str(y)
clientSocket.send(z)
#print y
for chunk_message in chunked_strings:
	clientSocket.send(chunk_message)
#	print chunk_message
length,garbage = clientSocket.recvfrom(buffer_size)
#print "length==>",length
str_=""

for i in range(0,int(length)):
	mod_str,garbage = clientSocket.recvfrom(buffer_size)
	str_=str_+mod_str
#str_=rest+str_
print 'From Server:', str_
clientSocket.close()