# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27891106")

API_HASH = os.environ.get("API_HASH", "a54985166cd86ecbe26b1f88d270aae1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6764623039:AAH5D0AOrysxGwCHgqS03PZvaBv9Bdxgl1Y") 

FORCE_SUB = os.environ.get("FORCE_SUB", "##Back up 🔙##") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "ikannada")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ikannada:i+me+alone3007@cluster3007.denxnj4.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6445341819').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
