# BEN SHAPIRO BOT

This was the first version of BEN BOT that I had originally developed and deployed on Chat-Avenue's mobile room, and then onto KTC. This project has been deprecated in favor of "BEN BOT", an addon for modern versions of Codychat that integrate directly with the database. 

BEN SHAPIRO BOT tracks an internal SQLite database of user stats based on username. This was intended to be used alongside a userscript which dynamically extracts messages from the DOM and feeds them to the API, but I had lost the userscript part of the code

The bot also implements its own currency system ("credits") along with gambling commands. This was before the release of Codychat 4.0, when there was no native currency system built into the chat. Current versions of BEN-BOT interact directly with this currency instead.

## Commands 

### Fun

1. !sayhello - Responds with a greeting to the user  
2. !joke - Sends a random joke  
3. !meme - Sends a random meme via GIPHY  
4. !darkjoke - Sends a random dark joke  
5. !owo - Converts input text into “owo” style (usage: !owo <text>)  
6. !8ball - Magic 8 Ball response to a question (usage: !8ball <question>)  

### Economy

7. !stats - Displays user stats (rank, balance, level, daily streak) *(currently disabled)*  
8. !addmoney - Adds credits to your account (usage: !addmoney <amount>)  
9. !level - Upgrade your level using credits *(currently disabled, requires confirmation with -c)*  
10. !sendmoney - Send credits to another user (usage: !sendmoney <amount> <username>)  
11. !daily - Claim daily credits with streak bonuses  
12. !leaderboard - Displays top 3 richest users  

### Gambling

13. !coinflip - Bet credits on heads or tails (usage: !coinflip <bet> <heads/tails>)  
14. !slots - Slot machine game with varying payouts (usage: !slots <bet>)  

### Admin

15. !cooldown - Puts the bot into cooldown mode (usage: !cooldown <time in minutes>, max 15, admin only)
