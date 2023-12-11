import discord
import random
import requests

DISCORD_BOT_TOKEN = ""
PEXELS_API_KEY = ""

class KafkaBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.change_presence(activity=discord.Game(name="Honkai: Star Rail"), status=discord.Status("dnd"))
        print("Bot is ready")


    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('!cat'):

            api_url = 'https://api.pexels.com/v1/search'
            headers = {'Authorization': PEXELS_API_KEY}
            params = {'query': 'cat', 'per_page': 50}  # You can adjust per_page as needed
            response = requests.get(api_url, headers=headers, params=params)
            
            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                cat_photos = data.get('photos', [])

                if cat_photos:
                    random_cat_photo = random.choice(cat_photos)
                    photo_url = random_cat_photo.get('src', {}).get('original', '')

                    embed = discord.Embed()
                    embed.set_image(url=photo_url)

                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("No cat photos found.")
            else:
                await message.channel.send("Failed to fetch cat photos.")

        elif message.content.startswith("!booba"):
            # Create an Embed instance
            embed = discord.Embed()
            
            # Set the image URL in the Embed
            horny_url = "https://media.tenor.com/8oy_9VcmVvEAAAAM/vorzek-vorzneck.gif"
            embed.set_image(url=horny_url)
            
            # Send the message with the embed
            await message.channel.send(embed=embed)      

        elif message.content.startswith("!help"):
            await message.channel.send("Hello Im Kafka\n\nYou can use 2 Commands right now\n!cat to generate a random Image of a Cat\n!booba to well get booba ( ͡° ͜ʖ ͡°)")      

intents = discord.Intents.all()
intents.messages = True 

client = KafkaBot(intents=intents)
client.run(DISCORD_BOT_TOKEN)

