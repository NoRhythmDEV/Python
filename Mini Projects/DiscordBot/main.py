#bot token MTE4Mzc0OTA2MDE2MzgwMTE1OA.G0dIVi.TIvj09QRZWCj29JHu1hkfOyB0eE32D7jSYMRMA
#bot url https://discord.com/api/oauth2/authorize?client_id=1183749060163801158&permissions=8&scope=bot+applications.commands
# pexels api key: u3jJFSNNDqaXji6TYPMTKzAoZY9GYRoVsGU2fFcESedCpvqRlqpzBSY5

import discord
import random
import requests
from bs4 import BeautifulSoup
import os

PEXELS_API_KEY = "u3jJFSNNDqaXji6TYPMTKzAoZY9GYRoVsGU2fFcESedCpvqRlqpzBSY5"

class KafkaBot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.change_presence(activity=discord.Game(name="Honkai: Star Rail"), status=discord.Status("dnd"))
        print("Bot is ready")


    async def on_message(self, message):
        if message.content.startswith('!cat'):
            # Pexels API endpoint for cat photos
            api_url = 'https://api.pexels.com/v1/search'
            
            # Set up headers with the Pexels API key
            headers = {'Authorization': PEXELS_API_KEY}
            
            # Parameters for the Pexels API request
            params = {'query': 'cat', 'per_page': 50}  # You can adjust per_page as needed
            
            # Make the request to the Pexels API
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

intents = discord.Intents.all()
intents.messages = True 

client = KafkaBot(intents=intents)
client.run('MTE4Mzc0OTA2MDE2MzgwMTE1OA.G0dIVi.TIvj09QRZWCj29JHu1hkfOyB0eE32D7jSYMRMA')

