import smtplib
from email.message import EmailMessage

sender = "your_email@gmail.com"
password = "your_app_password"
receiver = "recipient@gmail.com"

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = sender
msg["To"] = receiver
msg.set_content("Xin chào!\nĐây là email thử nghiệm gửi từ Python.")
#gắn nội dung văn bản

with smtplib.SMTP("smtp.gmail.com", 587) as server: #Kết nối tới Gmail SMTP
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("✅ Email sent successfully!")
