from pyrogram.types import InlineKeyboardButton

import config
from InflexMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝙰𝙳𝙳 𝙼𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["𝙶𝚁𝙾𝚄𝙿 "], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝙰𝙳𝙳 𝙼𝙴 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿"],
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [InlineKeyboardButton(text=_["COMMANDS"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["𝙲𝙷𝙰𝙽𝙽𝙴𝙻"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["𝙶𝚁𝙾𝚄𝙿"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["𝙾𝚆𝙽𝙴𝚁"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["𝚁𝙴𝙿𝙾"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons
