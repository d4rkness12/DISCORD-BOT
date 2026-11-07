import discord # pyright: ignore[reportMissingImports]

class RegistrationView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button( label="Scripter 💻", style=discord.ButtonStyle.primary, row = 0 )
    async def scripter(self, interaction, button): await self.assign_role(interaction, "scripter")

    @discord.ui.button( label="Asset-designer 🎨", style=discord.ButtonStyle.primary, row = 0 )
    async def asset_designer(self, interaction, button): await self.assign_role(interaction, "asset-designer")
    
    @discord.ui.button( label="Tester 🎮", style=discord.ButtonStyle.primary, row = 1 )
    async def tester(self, interaction, button): await self.assign_role(interaction, "tester")

    @discord.ui.button( label="Gui-designer 🖼️", style=discord.ButtonStyle.primary, row = 1 )
    async def gui_designer(self, interaction, button): await self.assign_role(interaction, "gui-designer")

    #AI GEN 😒

    async def assign_role(self, interaction, role_name):

        member = interaction.user
        guild = interaction.guild

        role = discord.utils.get(guild.roles, name=role_name)
        null_role = discord.utils.get(guild.roles, name="null")

        if role is None:
            await interaction.response.send_message(
                "Role not found!",
                ephemeral=True
            )
            return

        selected_roles = [
            "scripter",
            "asset-designer",
            "tester",
            "gui-designer"
        ]

        current_roles = [
            r for r in member.roles
            if r.name in selected_roles
        ]

        if len(current_roles) >= 2:
            await interaction.response.send_message(
                "You can select a maximum of 2 roles!",
                ephemeral=True
            )
            return

        await member.add_roles(role)

        if null_role and null_role in member.roles:
            await member.remove_roles(null_role)

        await interaction.response.send_message(
            f"Successfully selected {role_name}!",
            ephemeral=True
        )