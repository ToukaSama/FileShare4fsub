
from pyrogram import __version__
from levi import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Dᴇᴠ : <a href='https://t.me/About_meowtaro'>Touka Sama</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Anime_Sovereign'>Aɳιɱҽ_ʂσʋҽɾҽιɠɳ</a>\n○ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Sovereign'>Aɳιɱҽ_ʂσʋҽɾҽιɠɳ</a>\n○ Ongoing : <a href='https://t.me/Ongoing_Sovereign'>Hᴇɴᴛᴀɪ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/About_meowtaro'>ᴀɴɪᴍᴇ ᴄʜᴀᴛ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ', url='https://t.me/Anime_Sovereign')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
