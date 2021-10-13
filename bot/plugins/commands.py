#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
import random
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
PHOTO = [ 
"https://telegra.ph/file/cd1349ffbf6dccd5c93b0.jpg", 
"https://telegra.ph/file/31ff6b4f243ceaf334ec8.jpg", 
"https://telegra.ph/file/6d099d4e887b7c5a95100.jpg", 
"https://telegra.ph/file/e9f0a290456a43bdb8f04.jpg", 
"https://telegra.ph/file/c04aa7004b612f0f34dd2.jpg", 
"https://telegra.ph/file/35c7f9fb44ead611bde54.jpg", 
"https://telegra.ph/file/106cf60023420cca674f5.jpg", 
"https://telegra.ph/file/7480ba59914afb9fcd56f.jpg", 
"https://telegra.ph/file/58ee29b66366eceafb5e0.jpg", 
"https://telegra.ph/file/9bd82a5054fa9779c78b8.jpg"
]
db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🕊️ 𝗖𝗛𝗔𝗡𝗘𝗟 🕊️', url="https://t.me/moviehubcinema"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🤴 𝗢𝗡𝗪𝗘𝗥 🤴', url='https://t.me/OGGY123kph'),
        InlineKeyboardButton('🕊️ 𝗖𝗛𝗔𝗡𝗘𝗟 🕊️', url ='https://t.me/moviehubcinema')
    ],[
        InlineKeyboardButton('💘 𝗚𝗥𝗢𝗨𝗣 💘', url='https://t.me/moviehubgroupp')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
