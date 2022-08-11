from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "𝗛𝗲𝘆 𝗕𝗮𝗯𝘆  {}. \n\n𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 {} \n\n𝗦𝗲𝗻𝗱 𝗺𝗲 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗮𝗻𝗱 𝗶 𝘄𝗶𝗹𝗹 𝘀𝗲𝗻𝗱 𝗶𝘁 𝗯𝗮𝗰𝗸 𝗮𝗳𝘁𝗲𝗿 𝗿𝗲𝗺𝗼𝘃𝗶𝗻𝗴 𝘁𝗵𝗲 𝗳𝗼𝗿𝘄𝗮𝗿𝗱𝗲𝗱 𝘁𝗮𝗴. \n\n𝗕𝘆 @ABOUT_AJEET ♥"

    # About Message
    ABOUT = """
**𝗔𝗕𝗢𝗨𝗧 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧** 

𝗔 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗔𝗻𝗼𝗻𝘆𝗺𝗼𝘂𝘀 𝘀𝗲𝗻𝗱𝗲𝗿 𝗯𝗼𝘁 𝗯𝘆 @ABOUT_AJEET

𝗠𝗼𝗿𝗲 𝗯𝗼𝘁𝘀 : [𝗖𝗹𝗶𝗰𝗸 𝗵𝗲𝗿𝗲](https://t.me/ajeet_bots)

𝗦𝗼𝘂𝗿𝗰𝗲 𝗰𝗼𝗱𝗲 : [𝗖𝗹𝗶𝗰𝗸 𝗵𝗲𝗿𝗲](https://t.me/papa_bol_sakteho)

𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 : [𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺](docs.pyrogram.org)

𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : [𝗣𝘆𝘁𝗵𝗼𝗻](www.python.org)

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : [𓆩〭⃛〬𓆩〭⃛〬➤⃝✖‿✖•Ajͥeeͣtͫ](https://t.me/papa_bol_sakteho)
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🎪 About The Bot 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/AJEET_BOTS")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MODERN_ELEMENTS")],
    ]
