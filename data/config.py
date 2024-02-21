from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili


text_about = """
Sifatli elektrik qidirib charchadingizmi ☹️endi buni bizda yechimi bor

<b>👨‍🔧Elektrik master uzb jamoamiz sizga yordam beradi
👨‍💻Bizda mavjud xizmatlar transformator stalba ishlari
🏠Xozirgi kunda uy sharoitida juda kop kerak bolayotgan 
Generator ups stabilizator qoyish xizmatlari
🏭Zavod va sexlarimiz uchun sifatli Kip avtomatika xizmatlari
🚗Elektromobillar uchun zaryadka o’rnatish xizmatlari
🏢Kop qavatli binolar uchun sifatli elektro demontaj ishlari</b>

Qisqacha qilib aytganda bizning jamoamiz bilan siz ozingiz xoxlagan elektronni ishlaringizni bir zumda xal qilishingiz mumkin 🤝☺️

Shunaqa sifatli elektrik xizmati sizga kerak bolsa bizni jamoamiz doim xizmatda💪👍

⚡️Elektrik xizmatidan foydalanish uchun quyidagi botga ariza
 qoldiring!

 ➡️@Elektirik_master_uz_bot


<a href="https://t.me/+PqkpywpkDcgyNzRi">Telegram</a> | <a href="https://www.instagram.com/elektrik.master.uzb?igsh=ZmQ3NmFlYTkxNXBp">Instagram</a>
"""