from socket import *
buffer_size=1024
def chunkstring(string, length):
	return [string[0+i:length+i] for i in range(0, len(string), length)]

serverName = raw_input('Server IP: ')
serverPort = int(raw_input('Server Port: '))

message = raw_input('Input sentence: ')
chunked_strings=chunkstring(message,buffer_size)
print chunked_strings
y=str(len(chunked_strings))
print y
clientSocket = socket(AF_INET6, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


#clientSocket.send(y)

'''
for chunk_message in chunked_strings:
	clientSocket.send(chunk_message)
	print chunk_message
length,garbage = clientSocket.recvfrom(buffer_size)
str_=""
for i in range(0,int(length)):
	mod_str,garbage = clientSocket.recvfrom(buffer_size)
	str_=str_+mod_str
print 'From Server:', str_'''
clientSocket.close()