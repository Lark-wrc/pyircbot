#Python Irc Bot (pyircbot)

A simple ircbot written as the result of something like a bet. Intentionally bare-bones and built with the socket module for the same reason. Original Goals were:
	* Connects to an irc server and listens to all chatter.
	* prints any PMs recieved to the console, then checks to see if 
        	a command was entered.
	* do the command found or send an error message back, then loop 

##Functions
bot connects to an irc server and channel specified, and accepts any of it's commands that are PM'd to it. Commands are currently:
	* Do command: has the bot /me the text after do.

##Usage
python ircbot.py <server> <nick> <channel> 
* server: irc.xxx.net
* nick: any valid irc nick (most are)
* channel: a channel on the server. DO NOT include the #.

Once the bot has joined the channel, just use "/msg <nick> <command> etc..." to run the bot's command.

##ToDo
* Implement proper command line args
* Multi channel/server mode
* Server side commands
* Loading a command set from a file before starting

<<<<<<< HEAD
##Changelog
*	1.1	Add the message class, which streamlined once isCommand function into what is now processMessage. 
		Also a few other odd cleanups of lame looking or implemented code.
=======
	Changelog
*	1.1	Add the message class, which streamlined once isCommand function into what is now processMessage. Also a few other odd cleanups of lame looking or implemented code.
>>>>>>> 77dc23ea538217cc54804845a6330cf7d6dc2117

*	1.0	Basic functionality, Do command was chosen for simplicity.
