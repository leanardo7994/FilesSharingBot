#(Ā©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>ā Creator : <a href='https://t.me/LODGAN'>š š¢ š š š š”</a>\nā Language : <code>Python3</code>\nā Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\nā Channel : @Movies_Emperio\nā Support Group : @CinemasEmpire</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("š CLOSE", callback_data = "close")
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
