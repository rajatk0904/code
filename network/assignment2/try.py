def chunkstring(string, length):
	return [string[0+i:length+i] for i in range(0, len(string), length)]

def compress_strings(x):
	str_=""
	for t in x:
		str_=str_+t
	return str_
z="sf sf dfsdff dsfds fdssdf"
print z
x=chunkstring(z,5)
print x
y=compress_strings(x)
print y