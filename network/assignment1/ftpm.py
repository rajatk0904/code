import sys
import tarfile
import os.path
import ftplib
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
arguments=sys.argv
garbage=arguments.pop(0)
options=["-l","-a","-m","-s","-z","-p"]
j=0
for i in range(0,len(arguments)):
	if(arguments[i] not in options):
		j=i
		break
if(j+2>=len(arguments)):
	print "incorrect command"
	sys.exit(0)
server_=arguments[i]
#server_='172.20.176.233:/networks'
server=server_.split(":")[0]
try:
	path=server_.split(":")[1]
except:
	path="\\"
email=arguments[-1]
files=[]
user_id=raw_input("user_id:")
password=raw_input("password:")
for k in range(i+1,len(arguments)-1):
	files.append(arguments[k])
#print files

if("-m" not in arguments and len(files)>1):
	print "multiple files upload not allowed"
	sys.exit(0)
if("-z" in arguments):
	tar = tarfile.open("comp.tar.gz", "w:bz2")
	for name in files:
		try:
			tar.add(name)
		except:
			print name," does not exist"
	tar.close()
	new_files=["comp.tar.gz"]
else:
	new_files=[]
	for name in files:
		if(os.path.isfile(name)):
			new_files.append(name)
		else:
			print name," does not exist" 
#print new_files
links=[]
for file_ in new_files:
	filename = file_
	#print filename
	ftp = ftplib.FTP(server)
	link="ftp://"+server
	ftp.login(user_id, password)
	if("-p" in arguments):
		if(path[0]=='/'):
			path=path[1:]
		ftp.cwd(path)
		link=link+"/"+path
	myfile = open(filename, 'r')
	#print ftplib.FTP.dir(ftp)
	ftp.storlines('STOR ' + filename, myfile)
	myfile.close()
	link=link+"/"+filename
	links.append(link)
size=[]
for file_ in new_files:
	size.append(str(os.path.getsize(file_))+"KB")
text="The uploaded files are:"

for i in range(0,len(new_files)):
	text=text+"\n"+new_files[i]
	if("-l" in arguments):
		text=text+" ==>"+links[i]
	if("-s" in arguments):
		text=text+" ==>"+size[i]



emailfrom = "ftpm@ftpm.com"
emailto = email

msg = MIMEMultipart()
msg["From"] = "ftpm@ftpm.com"
msg["To"] = email
msg["Subject"] = "ftpm notification"
msg.preamble = "help I cannot send an attachment to save my life"
msg.attach( MIMEText(text) )
for fileToSend in new_files:
	ctype, encoding = mimetypes.guess_type(fileToSend)
	if ctype is None or encoding is not None:
	    ctype = "application/octet-stream"

	maintype, subtype = ctype.split("/", 1)

	if maintype == "text":
	    fp = open(fileToSend)
	    # Note: we should handle calculating the charset
	    attachment = MIMEText(fp.read(), _subtype=subtype)
	    fp.close()
	elif maintype == "image":
	    fp = open(fileToSend, "rb")
	    attachment = MIMEImage(fp.read(), _subtype=subtype)
	    fp.close()
	elif maintype == "audio":
	    fp = open(fileToSend, "rb")
	    attachment = MIMEAudio(fp.read(), _subtype=subtype)
	    fp.close()
	else:
	    fp = open(fileToSend, "rb")
	    attachment = MIMEBase(maintype, subtype)
	    attachment.set_payload(fp.read())
	    fp.close()
	    encoders.encode_base64(attachment)
	attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
	if("-a" in arguments):
		msg.attach(attachment)
server = smtplib.SMTP("localhost")
server.starttls()
#server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()