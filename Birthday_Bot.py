import discord 
from discord.ext import commands, tasks
from datetime import datetime

client = commands.Bot(command_prefix = '!')
birthday = ['Arturo S. - January 16th', 'Melvin C-N. - Feburary 13th', 'Kristine P. - Feburary 22nd',
			'Evan N. - April 11th','Albert K. - May 1st','Andrew K. - May 1st','Paul M. - May 8th',
			'Justin K. - June 11th','Jalon O. - July 3rd','Muneer A. - July 23rd','Sydney Z. - September 25th',
			'Armando G. - September 30th','Niko Z. - October 14th','Julian C. - October 31st','Raph S. - November 17th',
			'Caleb A. - November 17th','Manny S. - November 27th','Walid A. - December 20th','Jalin A. - December 24th',
			'Justin G. - December 27th','Nicole N. - December 31st']

bdays = { 'arturo': 'Janurary 16th', 'j.cole' : 'January 28th', 'melvin' : 'Feburary 13th', 'kristine' : 'Feburary 22nd', 'evan' : 'April 11th',
		  'albert' : 'May 1st', 'andrew' : 'May 1st', 'paul' : 'May 8th', 'justin.k' : 'June 11th', 'jalon' : 'July 3rd', 'sydney' : 'September 25th',
		  'armando' : 'September 30th', 'niko' : 'October 14th', 'julian' : 'October 31st', 'raph' : 'November 17th', 'caleb' : 'November 17th',
		  'manny' : 'November 27th', 'walid' : 'December 20th', 'jalin' : 'December 24th', 'justin.g' : 'December 27th', 'nicole' : 'December 31st'}


#myList = {'arturo': [1, 16]}
#print(myList['arturo'][0]) # print 1
#print(myList[arg][0] + myList[arg][1]) # print name and month
# myMonth = datetime.datetime.strptime(myList[arg][0], '%m')

#was thinking maybe just having dictionary with keys of the birthday so like 116 and the value being the name and birthday string, that was easy way i thought of
#so next_bday = { 116 : "Arturo - Janurary 16th", ...}

next_bday = { 116 : "Arturo's - Janurary 16th ", 128 : "J.Cole's - January 28th", 213 : "Melvin's - Feburary 13th", 222 : "Kristine's - Feburary 22nd", 411 : "Evan's - April 11th",
		  501 : "Albert's & Andrew's - May 1st", 508 : 'Paul - May 8th', 611 : 'Justin K. - June 11th', 703 : 'Jalon - July 3rd', 925 : 'Sydney - September 25th',
		  930 : "Armando's - September 30th", 1014 : "Niko's - October 14th", 1031 : "Julian's - October 31st", 1117 : "Raph's & Caleb's - November 17th",
		  1127 : "Manny's - November 27th", 1220 : "Walid's - December 20th", 1224 : "Jalin's - December 24th", 1227 : "Justin G.'s - December 27th", 1231 : "Nicole's - December 31st" }
@client.event
async def on_ready():
		print('Bot is ready.')
  
@client.command()
async def bday(ctx, arg):
	new = arg.lower()
	if new == "all":
		temp = '\n'.join(birthday)
		await ctx.send(temp)
	elif new in bdays:
		await ctx.send(arg.capitalize() + " - " + bdays[new])
	elif new == "next":
		today = datetime.now()
		now = int(today.strftime("%m%d"))	#gets today's date
		closest = 0
		length = len(next_bday)	#gets length of dictionary next_bday
		for x in range(length):
			list = []
			for key in next_bday.keys():
				list.append(key)	
			closest = list[x]	#closet = key(x) ; meaning we get the value of the current key and set it == to closest
			if closest < now:
				continue
			elif closest == now:
				await ctx.send('There is a birthday today! ' + next_bday[closest] + '. Happy Birthday!! :partying_face: :tada:')
			elif closest > now:
				await ctx.send('The next birthday coming soon is ' + next_bday[closest] + '! Make sure to wish them a Happy Birthday that day.')
			break
	elif new == "help":
		help = " Use !bday + \n \t - all \n \t - someone's name \n \t - next "
		await ctx.send(help)
	else:
		print("arg: " + arg + " \n")
		try:
			print(bdays[new])
		except:
			print("invalid arg\n")
	
	




#temp = ""
#for x in birthday:
#        temp = temp + x + '\n'
#    print(temp)
#
client.run('OTc4NDY4MzQwMjQwNjI5ODIw.GMSOiz.Qwxh77J_OFDLtribm9oSYjluL4_yDTJorgxe2c')