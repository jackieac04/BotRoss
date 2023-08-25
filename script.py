import discord
from discord.ext import commands, tasks
import random
from token import TOKEN

intents = discord.Intents.default()  # This will enable all default intents
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# List of Bob Ross quotes
quotes = [
    "There's nothing wrong with having a tree as a friend.",
    "The secret to doing anything is believing that you can do it.",
    "We don't make mistakes, just happy little accidents.",
    "It's hard to see things when you are too close. Take a step back and look.",
   "We don't laugh because we feel good, we feel good because we laugh.",
   "Ever make mistakes in life? Let's make them birds. Yeah, they're birds now.",
   "Talent is a pursued interest. Anything you're willing to practice, you can do",
   "You can do anything you want. This is your world.",
    "Go out on limb. That's where the fruit is.",
    "We want happy paintings. Happy paintings. If you want sad things, watch the news.",
    "I really believe that if you practice enough, you could paint The Mona Lisa with a two-inch brush.",
    "The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. As long as you believe.",
    "I think there's an artist hidden at the bottom of every single one of us.",
    "You too can paint almighty pictures.",
    "No pressure. Just relax and watch it happen.",
    "Don't forget to make all these little things individuals — all of them special in their own way.",
    "Make love to the canvas.",
    "I like to beat the brush.",
    "They say everything looks better with odd numbers of things. But sometimes I put even numbers — just to upset the critics.",
    "We don't really know where this goes — and I'm not sure we really care."
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    post_quote.start()  # Start the loop to post quotes

@tasks.loop(hours=24)  # Loop runs once every 24 hours
async def post_quote():
    channel_id = 1061291761256902717
    channel = bot.get_channel(channel_id)
    quote = random.choice(quotes)
    await channel.send(quote)

@post_quote.before_loop
async def before_posting():
    await bot.wait_until_ready()  # Wait until the bot logs in

bot.run(TOKEN)
