import os
import logging
from logging.handlers import RotatingFileHandler
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7363689539:AAEjZ72VzeGawh_NuM4RfR2NO5Byk_uB2KE")
APP_ID = int(os.environ.get("APP_ID", "1040456"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed1edeaedb17b440dbb29b91ae757270")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002230365222"))
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6509521865"))
#Port
PORT = os.environ.get("PORT", "8880")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://test:test@cluster0.q9llhnj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
#Shortner (token system)
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "ce6146378959c8fdf69d72e3818fe0a9197b1ba7")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 28800)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/Media_Adholokam/6")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002070863117"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n ɪ ᴀᴍ ᴛᴏᴋᴇɴ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1480923991 5877164701 5069922547").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
#Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐁𝐫𝐨/𝐒𝐢𝐬 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥")
#?𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣>
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @Media_Adholokam</b>")
#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Media_Adholokam"
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)
LOG_FILE_NAME = "codeflixbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
