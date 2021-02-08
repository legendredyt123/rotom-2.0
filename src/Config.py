import os

class Config:
    aid = int(os.environ.get("API_ID", "1907869"))
    ahash = os.environ.get("API_HASH", "8ef4942d4cb117b0b6eaa26f94b12fbb")
    bot_token = os.environ.get("BOT_TOKEN", "1689531050:AAGzNp2I_HvZLBx3PdsotxhCGzqIvq6g18M")
    sudo = [1097093376]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
