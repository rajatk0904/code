from socket import *
serverName = raw_input('Server IP: ')
serverPort = int(raw_input('Server Port: '))
clientSocket = socket(AF_INET6, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = raw_input('Input sentence: ')
clientSocket.send(message)
modifiedSentence = clientSocket.recvfrom(1024)
print 'From Server:', modifiedSentence[0]
clientSocket.close()