import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin người gửi và người nhận
sender = input("Email người gửi: ")
password = "rpqatrnaffqahyia"  # dùng App Password, KHÔNG dùng mật khẩu thật
receiver = input("Email người nhận: ")

# Tạo email
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = input("Tiêu đề email: ")

body = input("Nội dung email: ")
msg.attach(MIMEText(body, "plain"))

# Gửi mail
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error:", e)





