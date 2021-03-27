from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message as message

@Client.on_message(filters.command(["id"]) & (filters.private | filters.group))
async def showid(client, message):

        user_id = message.chat.id
        await message.reply_text(
            f"Your ID : `{user_id}`",
            parse_mode="markdown"
        )
