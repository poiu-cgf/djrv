from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "25494342"))
API_HASH = getenv("API_HASH", "7995627013:AAEd-MdITChEE9RwNejtP60jkMoA2MnAEd0")
BOT_TOKEN = getenv("BOT_TOKEN", "417cd441a3e027226e7a1333b2ea4ea0")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuwM8kA0Z3pm3K1eVAJ0AFN81epXJebplrm9aH8MKgzDdB9JqQP35RZhdVGehoUcH_rqXi9Zho3ceoc053L9IO1oZ4glz85bs_JCBx31hQYeclHcj7u9ZdnlR4CPNTXFiL9p0EocNth47kbArn-J6JNwnAromjdz_4e1pUAKLLAWhZCtJEJ8ISxF93x4pQ6giJj09TcFtMilH15cf1PgGaO8ES66wNrtP7czrzKfzVx9kyMCXdhrMzfp4R-9EPcOras8ljxsvap20Vh_SGveq6yLLl1GXsQkL5Jsi_z3SLScXLsFanCSIbiuS3YofFZVeC5e-YDCMacCw9CIkDC2BB9o=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "@VIP_Netrogen")
ALIVE_NAME = getenv("ALIVE_NAME", "netrogen")
BOT_USERNAME = getenv("BOT_USERNAME", "Botmuozknet_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "Nitrogen")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Nitrogen")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@VIP_Netrogen")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "7423822482").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7423822482").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
