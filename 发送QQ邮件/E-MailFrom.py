import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 第三方服务
import QQEMailSQM


# def mail():
    # ret = True
    # try:
    #     # 邮件的内容
    #     msg = MIMEText('测试发送邮件', 'plain', 'utf-8')
    #     # 发件人邮箱昵称、发件人邮箱账号
    #     msg['From'] = Header(QQEMailSQM.QQ_ID, 'utf-8')
    #     # 收件人邮箱昵称、收件人邮箱账号
    #     msg['To'] = Header(QQEMailSQM.QQ_ID, 'utf-8')
    #     # 邮件的主题，也可以说是标题
    #     msg['Subject'] = Header('测试Python发送邮件', 'utf-8')

    #     # 发件人邮箱中的SMTP服务器，端口是465
    #     smtpObj = smtplib.SMTP_SSL(QQEMailSQM.QQ_host, 465)
    #     # 发件人邮箱账号、授权码
    #     smtpObj.login(QQEMailSQM.QQ_ID, QQEMailSQM.QQ_SQM)
    #     # 发件人邮箱账号、收件人邮箱账号、发送邮件
    #     smtpObj.sendmail(QQEMailSQM.QQ_ID, QQEMailSQM.QQ_ID, msg.as_string())
    #     # 关闭连接
    #     smtpObj.quit()
    # except Exception:
    #     print(smtplib.SMTPException)
    #     print(Exception)
    #     ret = False
    # return ret
def mail():
    ret = True
    try:
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        # 主题
        msg['Subject'] = 'python发邮件带附件2'
        # 发件人
        msg['From'] = QQEMailSQM.QQ_ID
        # 收件人
        msg['To'] = QQEMailSQM.QQ_ID
        # 图片
        imageFile = "F:\\迅雷下载\\A\\[桜都字幕组][190503][メリー･ジェーン]おやすみせっくす 第2話兄を寝室へと誘う禁断の合図\\[封面][メリー･ジェーン]おやすみせっくす 第2話兄を寝室へと誘う禁断の合図.jpg"
        imageFile = open(imageFile, 'rb').read()
        msg_img = MIMEImage(imageFile)
        msg_img.add_header('Content-Disposition', 'attachment', filename="a4.jpg")
        # 文本
        Text = MIMEApplication(open('C:\\Users\\Administrator\\Desktop\\测功机换算公式大全.xls', 'rb').read())
        Text.add_header('Content-Disposition', 'attachment', filename='测功机换算公式大全.xls')
        # 压缩文件
        zipApart = MIMEApplication(open('F:\\南华\\SL-USBISP-3双龙电子驱动.7z', 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename='SL-USBISP-3双龙电子驱动.7z')
        # 正文
        msg.attach(MIMEText('发送附件', 'plain', 'utf-8'))
        # 添加附件
        msg.attach(msg_img)
        msg.attach(Text)
        msg.attach(zipApart)
        # 发件人邮箱中的SMTP服务器，端口是465
        smtpObj = smtplib.SMTP_SSL(QQEMailSQM.QQ_host, 465)
        # 发件人邮箱账号、授权码
        smtpObj.login(QQEMailSQM.QQ_ID, QQEMailSQM.QQ_SQM)
        # 发件人邮箱账号、收件人邮箱账号、发送邮件
        smtpObj.sendmail(QQEMailSQM.QQ_ID, QQEMailSQM.QQ_ID, msg.as_string())
        # 关闭连接
        smtpObj.quit()
    except smtplib.SMTPException as e:
        ret = False
        print('error:', e)
    return ret


if __name__ == "__main__":
    ret = mail()
    if ret:
        print('邮件发送成功')
    else:
        print('邮件发送失败')

