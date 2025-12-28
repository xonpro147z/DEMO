from flask import Flask #tạo ứng dụng web
from flask_mail import Mail, Message #Đến từ thư viện Flask-Mail, giúp gửi email dễ dàng trong Flask. 
app = Flask(__name__) #khởi tạo ứng dụng Flask

#cấu hình thông tin email
app.config['MAIL_SERVER'] = 'smtp.gmail.com' #máy chủ SMTP của Gmail
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True #bật mã hóa TLS
app.config['MAIL_USERNAME'] = 'hngo0131@gmail.com' 
app.config['MAIL_PASSWORD'] = 'rpqatrnaffqahyia' 
mail = Mail(app) #liên kết Flask-Mail với ứng dụng Flask
@app.route('/') 
#nếu có ai truy cập vào đường dẫn này, thì hãy chạy hàm này                                                                                                             
def send_email(): 
    msg = Message('KIỂM TRA', sender='hngo0131@gmail.com', 
    recipients=['hungngo120802@gmail.com']) 
    msg.body = 'xin chào! Đây là email thử nghiệm gửi từ Flask.' 
    mail.send(msg) 
    return 'Email sent' 
if __name__ == '__main__': 
    app.run()
    #Khởi động server web Flask cục bộ