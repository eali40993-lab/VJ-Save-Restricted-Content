import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8187759971:AAGrj9zWbq3LdeuuqyaleKTdoU3C66gGLjw")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28602638"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "409b8fbb8caa16e34f357309f82b7910")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5646681109"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://deephkdeephk:OmYH9Q0gkxN3am2a@cluster0.9lbynxc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "Deephk_bot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
