"""An irc bot program. Commands will be variable and modifiable.
* Connects to an irc server and listens to all chatter.
* prints any PMs recieved to the console, then checks to see if 
	a command was entered.
* do the command found or send an error message back, then loop.
^ Successful

*Refactor to have an object generator that contains fields linking back to
 all the 'parts' of a message. Better extendablity and cleaner.
 
Example PRIVMSG command:
:natsuPaw_!~piro@24.115.128.97.res-cmts.sesh.ptd.net PRIVMSG #rowancsc :hello world
"""

import sys
import socket

class Message():
	def __init__(self, mess):
		data = mess.split(' ')
		self.command = data[1] #the command of the mess
		if self.command == 'PRIVMSG':
			self.type = 'msg'
			self.target = data[2]
			self.message = mess.split(':')[2]
			self.split_msg = self.message.split(' ')
			self.nick = mess.split('!')[0][1:]
			self.hostname = mess.split('!')[1].split(' ')[0]
		else:
			self.type = 'nil'
	

def do_cmd(command=""):
	s.sendall("PRIVMSG #" + channel + " :\001ACTION does " + command +"\001\r\n")

#outdated isCommand. Left in till the new one is confirmed working.
"""def isCommand(data):
	dat = data.split(' ')
	if dat[1] == 'PRIVMSG' and dat[2] == nick:
		dat = data.split(':')
		dat = dat[2].split(' ')
		if dat[0] in commands:
			command = ' '.join(dat[1:])
			commands[dat[0]](command)
		else:
			dat = data.split(' ')
			user = dat[0][1:]
			user = dat[0].split('!')
			user = user[0][1:]
			print user
			s.sendall('PRIVMSG ' + user + ' :This is not one of my commands.\r\n')

"""

def processMessage(message):
	if message.type == 'msg' and message.target == nick:
		if message.split_msg[0] in commands:
			commands[message.split_msg[0]](' '.join(message.split_msg[1:]))
		else:
			s.sendall('PRIVMSG ' + message.nick + ' :This is not one of my commands.\r\n')
	if message.type == 'nil':
		pass





#Actual program

#Get & declare vars
commands = {'do':do_cmd}
server, nick, channel = '', '', ''
args = sys.argv[1:]
if len(args) == 3:
	server, nick, channel = args
else:
	print 'Invalid params, server nick channel'
	print args
	exit()

#make a connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, 6667))

#possibly factor out, just recieves a few lines before sending.
i = 0
while i < 3:
	data = s.recv(1024)
	print data
	i+=1


#register with the server and join the channel
s.sendall('pass secret\r\n')
s.sendall('nick ' + nick + '\r\n')
s.sendall('user ' + nick +  ' 8  *' + ' : ' + "Paw's bot\r\n")
s.sendall('JOIN #' + channel + '\r\n')

#program loop
while 1:
	data = s.recv(1024)
	mess = Message(data)
	processMessage(mess)
	print data
