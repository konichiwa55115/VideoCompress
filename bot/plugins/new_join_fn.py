#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @AbirHasan2005


from bot.database import Database
from bot.localisation import Localisation
from bot import (
    UPDATES_CHANNEL,
    DATABASE_URL,
    SESSION_NAME
)
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid

db = Database(DATABASE_URL, SESSION_NAME)
CURRENT_PROCESSES = {}
CHAT_FLOOD = {}
broadcast_ids = {}

async def new_join_f(client, message):
    # delete all other messages, except for AUTH_USERS
    await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Localisation.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()


async def help_message_f(client, message):
    
   
    await message.reply_text(
        Localisation.HELP_MESSAGE,
     
        ),
        quote=True
    )
