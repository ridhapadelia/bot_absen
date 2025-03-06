import asyncio
import schedule
import time
import threading
from telegram import Bot

TOKEN = "8012962740:AAGe6hXjS-evnLnzS8PYeI-nK5e7lC4Bq0E"
CHAT_ID = "-1002295263097"

bot = Bot(token=TOKEN)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def kirim_pesan(teks):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=teks, parse_mode="Markdown")
        print(f"Pesan berhasil dikirim: {teks}")
    except Exception as e:
        print(f"Error saat mengirim pesan: {e}")

def tugas_bot(teks):
    asyncio.run_coroutine_threadsafe(kirim_pesan(teks), loop)

def run_loop():
    loop.run_forever()

threading.Thread(target=run_loop, daemon=True).start()

schedule.every().monday.at("08:00").do(lambda: tugas_bot("*Selamat Pagi✨*\nJangan lupa absen untuk memulai hari dengan semangat. Semoga harimu lancar dan menyenangkan!"))  
schedule.every().monday.at("17:00").do(lambda: tugas_bot("*Waktunya untuk istirahat!*\nJangan lupa absen sebelum meninggalkan kantor. Sampai jumpa di hari berikutnya!"))  

schedule.every().tuesday.at("11:20").do(lambda: tugas_bot("*Selamat Pagi✨*\nJangan lupa absen untuk memulai hari dengan semangat. Semoga harimu lancar dan menyenangkan!"))
schedule.every().tuesday.at("16:40").do(lambda: tugas_bot("*Waktunya untuk istirahat!*\nJangan lupa absen sebelum meninggalkan kantor. Sampai jumpa di hari berikutnya!"))

schedule.every().wednesday.at("09:21").do(lambda: tugas_bot("*Selamat Pagi✨*\nJangan lupa absen untuk memulai hari dengan semangat. Semoga harimu lancar dan menyenangkan!"))
schedule.every().wednesday.at("17:00").do(lambda: tugas_bot("*Waktunya untuk istirahat!*\nJangan lupa absen sebelum meninggalkan kantor. Sampai jumpa di hari berikutnya!"))

schedule.every().thursday.at(10:35").do("lambda: tugas_bot("*Selamat Pagi✨*\nJangan lupa absen untuk memulai hari dengan semangat. Semoga harimu lancar dan menyenangkan!"))
schedule.every().thursday.at("10:40").do(lambda: tugas_bot("*Waktunya untuk istirahat!*\nJangan lupa absen sebelum meninggalkan kantor. Sampai jumpa di hari berikutnya!"))

schedule.every().friday.at("08:00").do(lambda: tugas_bot("*Selamat Pagi✨*\nJangan lupa absen untuk memulai hari dengan semangat. Semoga harimu lancar dan menyenangkan!"))
schedule.every().friday.at("17:00").do(lambda: tugas_bot("*Waktunya untuk istirahat!*\nJangan lupa absen sebelum meninggalkan kantor. Sampai jumpa di hari berikutnya!"))

print("Bot berjalan, menunggu jadwal notifikasi...")

while True:
    schedule.run_pending()
    time.sleep(1)
