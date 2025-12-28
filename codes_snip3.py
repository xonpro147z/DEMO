import smtplib 
email = 'hngo0131@gmail.com' 
password = 'rpqatrnaffqahyia' 
server = smtplib.SMTP('smtp.gmail.com', 587) 
# --- Đính kèm file ---

# --- Gửi email ---
server.starttls() 
server.login(email, password) 
message = 'Subject: Test Email\n\nThis is a test email' 
server.sendmail(email, 'hungngo120802@gmail.com', message) 
server.quit() 