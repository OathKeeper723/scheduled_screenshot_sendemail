# -*- coding: UTF-8 -*-
import schedule
from selenium import webdriver
import time
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

my_sender='443576278@qq.com'   
my_pass = 'yourqqsmtppassword'             
my_user1='x@qq.com'
my_user2='y@qq.com'

def send():
    ret=True
        #创建一个带附件的实例
    msg = MIMEMultipart()
    msg['From'] = Header("from", 'utf-8')
    msg['To'] =  Header("to", 'utf-8')
    msg['Subject'] = Header('title', 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    mail_msg = """
    <p>TEST</p>
    <p><img src="cid:image1"></p>
    """

    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open('test.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    #邮件正文内容
    msg.attach(MIMEText('content', 'plain', 'utf-8'))
    
    try:
        # 登录
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  
        server.login(my_sender, my_pass)


        server.sendmail(my_sender,[my_user1,my_user2],msg.as_string())
        server.quit()  
    except Exception,e: 
        traceback.print_exc()
        ret=False
    return ret

def shot():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    time.sleep(8)

    ele = driver.find_element_by_id("xixi_data_screenshot")

    ele.screenshot('waterQA.png')
    print("over!")
    driver.quit();
    return 1;

def screenshot():
    print('start screenshot')

    shot()
    print('send email')
    rs = send()
    print(rs)

if __name__ == "__main__":
    schedule.every().day.at('08:20').do(screenshot)
    print("waiting to send email util 08:20")
    while True:
        schedule.run_pending()