import discord # pyright: ignore[reportMissingImports]
from registration_view import RegistrationView
import os

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

class Client(discord.Client):

    async def on_ready(self):
        print(f"Logged in as {self.user}")

        embed = discord.Embed(
            title="Player Registration",
            description="Choose your roles to join the server",
            color=discord.Color.from_rgb(52,52,52)
        )

        channel = self.get_channel(CHANNEL_ID)

        if channel:
            await channel.send(embed=embed, view = RegistrationView())

    async def on_member_join(self, member):

        await member.add_roles("null")

        embed = discord.Embed(
            title="Player Registration",
            description="Choose your roles to join the server",
            color=discord.Color.gray()
        )

        channel = self.get_channel(CHANNEL_ID)

        if channel:
            await channel.send(embed=embed)
            await channel.send(f"{member} has joined the server")

    #AI GEN 😒

    async def on_message(self, message):

        if message.author == self.user:
            return

        if message.content != "!roles": return

        selected_roles = [
            "owner",
            "scripter",
            "asset-designer",
            "tester",
            "gui-designer"
        ]

        user_roles = [
            role.name for role in message.author.roles
            if role.name in selected_roles
        ]

        await message.reply(
            f"{message.author} is having roles: {', '.join(user_roles)}"
        )

intents = discord.Intents.default()

intents.members = True
intents.message_content = True

client = Client(intents=intents)
client.run(os.getenv("MY_VAR"))