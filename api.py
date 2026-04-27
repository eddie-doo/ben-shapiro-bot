from flask import Flask, request, jsonify
import sqlite3
import random
from datetime import datetime
app = Flask(__name__)

# Cooldown timer
cooldown_until = 0

## Data ##
jokes = ["After an unsuccessful harvest, why did the farmer decide to try a career in music? Because he had a ton of sick beets.",
		"Why is it so cheap to throw a party at a haunted house? Because the ghosts bring all the boos.",
		"Which days are the strongest? Saturday and Sunday. The rest are weekdays.",
		"What's the difference between a well-dressed man on a unicycle and a poorly-dressed man on a bicycle? Attire.",
		"I hate my job—all I do is crush cans all day. It’s soda pressing.",
		"Of all the inventions of the last 100 years, the dry erase board has to be the most remarkable.",
		"Did you know that the first french fries weren’t cooked in France? They were cooked in Greece.",
		"To whoever stole my copy of Microsoft Office, I will find you. You have my Word.",
		"What did Yoda say when he saw himself in 4K? HDMI.",
		"I can't take my dog to the pond anymore because the ducks keep attacking him. That's what I get for buying a pure bread dog.",
		"During my calculus test, I had to sit between identical twins. It was hard to differentiate between them.",
		"What is the most expensive video-streaming service at this time? College.",
		"A boy asked his bitcoin-investing dad to borrow $10.00 worth of bitcoin. His dad said: \"$9.67? What do you need $10.32 for?\""]
		
dark_jokes = ["How do you fit 4 queers on a barstool? Flip it upside-down.",
			 "What's a pedophiles favorite part about halloween? Free delivery.",
			 "Why does Stephen Hawking do one-liners? Because he can't do stand up.",
			 "My Grandpa said, \"Your generation relies too much on technology!\" I replied, \"No, your generation relies too much on technology!\" Then I unplugged his life support.",
			 "What is both a fruit and a vegetable? A homosexual in a wheelchair!",
			 "Who was the greatest Jewish cook? Adolf Hitler.",
			 "What is the best hotel in the world? Auschwitz, it received over a million stars.",
			 "What did the boy with no hands get for Christmas? Gloves! (just kidding, he hasn't opened his present yet.)",
			 "My friend was showing me his tool shed and pointed to a ladder. \"That's my stepladder,\" he said. \"I never knew my real ladder.\"",
			 "I just read that someone in London gets stabbed every 52 seconds... poor guy ):",
			 "Today I was digging in my garden and I found a chest full of coins, I was so excited I wanted to run and tell my wife! But then I remembered why I was digging a hole in the garden..",
			 "When I was growing up, # = pound, not hashtag. Good thing it changed, since \"pound metoo\" would've been sending the wrong message."]
		
memes = ["NOJNmdvYz8Y4gAbLzg", "SXMJANRi4Gx7Nndllx", "ZVJ2IH0Ln2cCstAJLa",
			"YPYpWBd7ewsVgZO8TL" ,"gz8d8YF4pNKXFutpfD" ,"VX4dcq866vI0wAwEQE"];

## Command Behavior ##
@app.route("/command/")
def command():
	## Preliminary checks ##
	global cooldown_until
	current_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
	if(cooldown_until > current_timestamp):
		return 0; 

	# Get URL arguments
	command = request.args.get("command").split(" ")[0]
	sender = request.args.get("sender")
	sender_id = request.args.get("id")

	response_data = {}

	match command.lower():
		# Fun
		case "!sayhello":
			response_data['action'] = "WRITE"
			response_data['text'] = "Hello, {0}!".format(sender)
		case "!joke":
			response_data['action'] = "WRITE"
			response_data['text'] = jokes[random.randint(0,len(jokes)-1)]
		case "!meme":
			response_data['action'] = "GIPHY"
			response_data['text'] = memes[random.randint(0,len(memes)-1)]
		case "!darkjoke":
			response_data['action'] = "WRITE"
			response_data['text'] = dark_jokes[random.randint(0,len(dark_jokes)-1)]
		case "!owo":
			message = request.args.get("command").lower()
			message = message.replace("love", "wuv")
			message = message.replace("mr", "mistuh")
			message = message.replace("dog", "doggo")
			message = message.replace("cat", " kitteh ")
			message = message.replace("hello", "henwo")
			message = message.replace("hell", "heck")
			message = message.replace("fuck", "fwick")
			message = message.replace("fuk", "fwick")
			message = message.replace("shit", "shoot")
			message = message.replace("friend", "fwend")
			message = message.replace("stop", "stawp")
			message = message.replace("god", "gosh")
			message = message.replace("shit", "shoot")
			message = message.replace("dick", "peepee")
			message = message.replace("penis", "peepee")
			message = message.replace("damn", "darn")
			message = message.replace("this", "dis")
			message = message.replace("that","dat")
			
			message = message.replace("r", "w")
			message = message.replace("l", "w")
			
			message = message.split(" ")
			message[0] = ""
			
					
			message = " ".join(message)
			
			prefixes = ["OwO","hehe","*nuzzles*","*giggles*","*waises paw*","OwO whats this?","*notices bulge*","*unbuttons shirt*"]
			suffixes = [":3", ">:3", "xox", ">3<", "UwU", "hehe", "ɾ⚈▿⚈ɹ", "(・ω・)", "(ᗒᗨᗕ)", "murr~", "(*≧▽≦)", "( ﾟ∀ ﾟ)", "( ・ ̫・)", "(▰˘v˘▰)", "(・`ω´・)", "*gwomps*","(ﾉ´ з `)ノ","✾(〜 ☌ω☌)〜✾", "( •́ .̫ •̀ )", "( ´ ▽ ` ).｡ｏ♡"]
			
			response_data['action'] = "WRITE"
			if request.args.get("command").lower().replace("!owo","") == "":
				response_data['text'] = "Proper usage: !owo <text>"
			else:
				response_data['text'] = "{0} {1} {2}".format(prefixes[random.randint(0,len(prefixes)-1)], message, suffixes[random.randint(0,len(suffixes)-1)])
		case "!8ball":
			response_data['action'] = "WRITE"
			question = request.args.get("command").replace("!8ball","").replace(" ","")
			if question == "":
				response_data['text'] = "[🎱] Magic 8 Ball says.. your question is blank!"
			else:
				responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.",
				"As I see it, yes.","Most likely.", "Yes.","Signs point to yes.", "Reply hazy, try again.","Ask again later.","Better not to tell you now.",
				"Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook is not so good.", "Very doubtful."]
				response_data['text'] = "[🎱] Magic 8 Ball says.. {0}".format(responses[random.randint(0,len(responses)-1)])
		# Economy
		case "!stats":
			return 0
			user_check(sender, sender_id)
			c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
			result = c.fetchone()

			if result == None:
				response_data['action'] = "WRITE"
				response_data['text'] = "No user found."
			else:
				userName = result[0]
				userRank = result[2]
				userBalance = result[3]
				userLevel = result[4]
				userStreak = result[7]

				response_data['action'] = "WRITE"
				response_data['text'] = "[💎] Stats for {0}: {{Rank:\"{1}\", Balance:{2}, Level:{3}, Daily Streak:{4}}}".format(userName, userRank, userBalance, userLevel,userStreak)
		case "!addmoney":
			try:
				desiredAmount = int(request.args.get("command").split(" ")[1])
				c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (desiredAmount, sender_id))
				response_data['action'] = "WRITE"
				response_data['text'] = "[❕] {0} credits have added been to {1}'s account!".format(desiredAmount, sender)
			except Exception as e:
				response_data['action'] = "WRITE"
				response_data['text'] = "[❌] {0} That is not a valid number!".format(sender)
		case "!level":
			return 0;
			response_data['action'] = "WRITE"
			costs = [50, 150, 300, 500, 1000, 2000, 3000, 4000, 5000, 6500, 8000, 10000, 13000, 15000, 20000, 100000, 500000, 750000, 1000000]
			c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
			result = c.fetchone()
			
			if result[4] > 20:
				cost = 9999999
			else:
				cost = costs[result[4]]
			
			if (len(request.args.get("command").split(" ")) < 2 or request.args.get("command").split(" ")[1] != "-c"):
				response_data['text'] = "[❕] {0} Are you sure you want to upgrade to level {1} for {2} credits? Type \"level -c\" to confirm.".format(sender, result[4]+1, cost)
			elif result[3] < cost:
				response_data['text'] = "[❌] {0} You don't have enough credits to purchase this level up!".format(sender)
			else:
				c.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (cost, sender_id))
				c.execute("UPDATE users SET level = level + 1 WHERE id = ?", (sender_id,))
				response_data['text'] = "[❇️] {0} Congratulations! You have reached level {1}.".format(sender, result[4]+1)
		case "!sendmoney":
			c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
			result = c.fetchone()
			amount = parse_int(request.args.get("command").split(" ")[1])
			#print(request.args.get("command").split(" "))
			
			#if len(request.args.get("command").split(" ")) < 2:
			#	response_data['action'] = "WRITE"
			#	response_data['text'] = "{0} Proper usage: !sendmoney <amount> <username> {1}".format(sender, request.args.get("command"))
			if 'receiver_id' not in request.args:
				response_data['action'] = "MISSING_ID_SENDMONEY"
				response_data['receiver'] = request.args.get("command").replace("!sendmoney ","").replace(str(amount), "").replace(" ","",1)
				response_data['name'] = sender
				response_data['id'] = sender_id
				response_data['amount'] = amount
			elif request.args.get("receiver_id") == "undefined" or request.args.get("receiver_id") == "-1":
				response_data['action'] = "WRITE"
				response_data['text'] = "[❌] {0} That user does not exist!".format(sender)
			elif amount == -1:
				response_data['action'] = "WRITE"
				response_data['text'] = "[❌] {0} That is not a valid number!".format(sender)
			elif result[3] < amount:
				response_data['action'] = "WRITE"
				response_data['text'] = "[❌] {0} You do not have enough credits!".format(sender)
			else:
				response_data['action'] = "WRITE"
				user_check(request.args.get("receiver"),request.args.get("receiver_id"))
				c.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, sender_id))
				c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, request.args.get("receiver_id")))
				response_data['text'] = "[💰] {0} sent {1} credits to {2}!".format(sender, amount, request.args.get("receiver"))
		case "!daily":
			response_data['action'] = "WRITE"
			c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
			result = c.fetchone()
			current_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
			seconds_since_last =  current_timestamp - result[6]
			
			if(seconds_since_last < 86400):
				response_data['text'] = "[🌤️] You have already claimed your daily today!"
			elif(seconds_since_last > 86400 and seconds_since_last < 86400*2):
				c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (result[7]*50, sender_id))
				c.execute("UPDATE users SET daily_streak = daily_streak + 1 WHERE id = ?", (sender_id,))
				c.execute("UPDATE users SET last_claimed_daily = ? WHERE id = ?", (current_timestamp, sender_id,))
				response_data['text'] = "[🌤️] {0} Your daily credits have been claimed! (+{1} credits) (current streak: {2})".format(sender, result[7]*50, result[7])
			else:
				c.execute("UPDATE users SET daily_streak = 1 WHERE id = ?", (sender_id,))
				c.execute("UPDATE users SET last_claimed_daily = ? WHERE id = ?", (current_timestamp, sender_id,))
				c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (result[7]*50, sender_id))
				response_data['text'] = "[🌤️] {0} Your daily credits have been claimed! (+{1} credits) (current streak: {2})".format(sender, result[7]*50, result[7])
		case "!leaderboard":
			response_data['action'] = "WRITE"
			c.execute("SELECT * FROM users WHERE is_banned=0 ORDER BY balance DESC")
			result = c.fetchall()
			response_data['text'] = "[👑] Top Richest Users: 1.{0} ({1} credits) 2.{2} ({3} credits), 3. {4} ({5} credits)".format(result[0][0], result[0][3], result[1][0], result[1][3], result[2][0], result[2][3])
			
		# Gambling
		case "!coinflip":
			response_data['action'] = "WRITE"
			
			if(len(request.args.get("command").split(" ")) < 3):
				response_data['text'] = "{0} Proper usage: !coinflip <bet> <heads/tails>".format(sender)
			else:
				wager = parse_int(request.args.get("command").split(" ")[1])
				coinside = request.args.get("command").split(" ")[2].lower()
				c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
				result = c.fetchone()	
			
				if(wager == -1 or coinside not in ["heads","tails"]): # Verify valid input
					response_data['text'] = "{0} Proper usage: !coinflip <bet> <heads/tails>".format(sender)
				elif(result[3] < wager):
					response_data['text'] = "{0} You do not have enough credits to bet!".format(sender)
				else:
					win = random.randint(1,1000)
					if (win > (600 - (5 * result[4]))):
						c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (wager, sender_id))
						response_data['text'] = "[🪙] {0} flipped {1} ! You win {2} credits!".format(sender, coinside, wager)
					else:
						c.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (wager, sender_id))
						opposite = "Tails" if coinside == "heads" else "Heads"
						response_data['text'] = "[🪙] {0} flipped {1} ! Better luck next time ):".format(sender, opposite)
		case "!slots":
			response_data['action'] = "WRITE"
			if(len(request.args.get("command").split(" ")) < 2):
				response_data['text'] = "[🎰] {0} Proper usage: !slots <bet>".format(sender)
			else:
				wager = parse_int(request.args.get("command").split(" ")[1])
				c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
				result = c.fetchone()
				
				if(wager == -1):
					response_data['text'] = "[🎰] {0} Proper usage: !slots <bet>".format(sender)
				elif(wager > 40):
					response_data['text'] = '[🎰] {0} maximum bet for slots is 40!'.format(sender)
				elif(wager < 10):
					response_data['text'] = '[🎰] {0} minimum bet for slots is 10!'.format(sender)
				elif(result[3] < wager):
					response_data['text'] = "[🎰] {0} You do not have enough credits to bet!".format(sender)
				else:
					symbols = ["🍀","🎲","🍒","♠️","🍓","🍉","🍋"]
					outcome = [symbols[random.randint(0,len(symbols)-1)], symbols[random.randint(0,len(symbols)-1)], symbols[random.randint(0,len(symbols)-1)]]
					payout = -wager
						
					if(outcome == ["🍀","🍀","🍀"]):
						payout = wager*200
					elif(outcome == ["🎲","🎲","🎲"]):
						payout = wager*50
					elif(outcome == ["🍒","🍒","🍒"]):
						payout = wager*25
					elif(outcome == ["♠️","♠️","♠️"]):
						payout = wager*15
					elif(outcome == ["🍓","🍓","🍓"]):
						payout = wager*10
					elif(outcome == ["💵","💵","💵"]):
						payout = wager*5
					elif(outcome == ["🍋","🍋","🍋"]):
						payout = wager*2
					elif(not(outcome[0] != outcome[1] and outcome[0] != outcome[2] and outcome[1] != outcome[2])):
						payout = wager
							
					c.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (payout, sender_id))
						
					if payout == -wager:
						response_data['text'] = "[🎰] ══[{0}]-[{1}]-[{2}]══ Better luck next time {3}! (-{4} credits)".format(outcome[0],outcome[1],outcome[2], sender, wager)
					if payout == wager:
						response_data['text'] = "[🎰] ══[{0}]-[{1}]-[{2}]══ You came out even {3}! (+{4} credits)".format(outcome[0],outcome[1],outcome[2], sender, wager)
					if payout > wager:
						response_data['text'] = "[🎰] ══[{0}]-[{1}]-[{2}]══ Congratulations {3}! You won! (+{4} credits)".format(outcome[0],outcome[1],outcome[2], sender, payout)
		# Admin
		case "!cooldown":
			response_data['action'] = "WRITE"
			c.execute("SELECT * FROM users WHERE id=?", (sender_id,))
			result = c.fetchone()
			
			time = parse_int(request.args.get("command").split(" ")[1])
			
			if(result[2] != "Admin"):
				response_data['text'] = "[❌] {0} You don't have permission to run this command!".format(sender)
			elif(time == -1):
				response_data['text'] = "{0} Proper usage: !cooldown <time (in minutes)>".format(sender)
			elif(time > 15):
				response_data['text'] = "[❕]{0} Max time for cooldown is 15 minutes!".format(sender)
			else:
				current_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
				cooldown_until = current_timestamp + (time*60)
				response_data['text'] = "[❕] BEN BOT will be cooling down for {0} minutes.".format(time)

	return jsonify(response_data), {"Access-Control-Allow-Origin": "*"}
	
def parse_int(i): # Attempts to convert number to valid positive integer, if can't, return -1
	try:
		int(i)
	except:
		return -1
	
	if(int(i) > 0):
		return int(i)
	else:
		return -1
		

 
if __name__ == "__main__":
	app.run(debug=True)
