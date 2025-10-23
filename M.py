import os
import requests

# Read your secret token from the environment
TOKEN = os.getenv("LICHESS_KEY")
GAME_ID = "TLvCRnRj"

if not TOKEN:
    raise ValueError("❌ Missing LICHESS_KEY environment variable")

url = f"https://lichess.org/api/board/game/{GAME_ID}/resign"
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("✅ Game successfully resigned!")
elif response.status_code == 400:
    print("❌ Resign failed: Game may already be over or not controlled by this account.")
else:
    print(f"⚠️ Unexpected response {response.status_code}: {response.text}")
