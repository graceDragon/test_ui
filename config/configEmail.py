# coding:utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
import readConfig as readConfig
from config.settings import BASE_PATH_HTML
from config.settings import SendEmail

localReadConfig = readConfig.ReadConfig()


class Email:
    def __init__(self):
        print "开始获取邮件配置信息..."
        global host, user, password, port, sender, title
        host = 'smtp.exmail.qq.com'
        user = 'liuyuliang@efang100.com'
        password = 'Lyl@112358'
        port = '25'
        sender = 'liuyuliang@efang100.com'
        title = 'UI Test Report'
        receiver_test = 'liuyuliang@efang100.com'
        receiver_online = 'liuyuliang@efang100.com/jihenggang@efang100.com/wangli@efang100.com/wangyueyong@efang100.com'
        # content = localReadConfig.get_email("content")
        # get receiver list
        EMAIL = SendEmail
        try:
            if EMAIL == 'test':
                self.value = receiver_test
            elif EMAIL == 'online':
                self.value = receiver_online
                print '收件人信息', self.value
        except Exception as e:
            raise e
        self.receiver = []
        for n in str(self.value).split("/"):
            self.receiver.append(n)

        # defined email subject
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "UI测试报告" + " " + date
        # 获取测试报告路径
        # self.html_path = localReadConfig.get_report('report_url')
        f = open(BASE_PATH_HTML, 'r')
        self.html_path = f.readline()
        f.close()
        print "获取邮件信息完成...", self.html_path, '1111'

        # 构造MIMEMultipart做为根容器
        # self.msg = MIMEMultipart('related')
        self.msg = MIMEMultipart()

    def config_header(self):
        """
        defined email header include subject, sender and receiver
        :return:
        """
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        """
        write the content of email
        :return:
        """
        # 邮件内容
        # f = open(os.path.join(readConfig.proDir, 'common', 'emailStyle.txt'))
        # html_path = "D:\\interfaceTest\\testResult\\html\\20171117\\20171117_103650.html"
        f = open(self.html_path)
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)

    # def config_image(self):
    #     """
    #     config image that be used by content
    #     :return:
    #     """
    #     # defined image path
    #     image1_path = os.path.join(readConfig.proDir, 'testData', 'img', '1.png')
    #     fp1 = open(image1_path, 'rb')
    #     msgImage1 = MIMEImage(fp1.read())
    #     # self.msg.attach(msgImage1)
    #     fp1.close()
    #
    #     # defined image id
    #     msgImage1.add_header('Content-ID', '<image1>')
    #     self.msg.attach(msgImage1)
    #
    #     image2_path = os.path.join(readConfig.proDir, 'testData', 'img', 'logo.png')
    #     fp2 = open(image2_path, 'rb')
    #     msgImage2 = MIMEImage(fp2.read())
    #     # self.msg.attach(msgImage2)
    #     fp2.close()
    #
    #     # defined image id
    #     msgImage2.add_header('Content-ID', '<image2>')
    #     self.msg.attach(msgImage2)

    # def config_file(self):
    #     """
    #     config email file
    #     :return:
    #     """
    #
    #     # if the file content is not null, then config the email file
    #     if self.check_file():
    #
    #         reportpath = self.log.get_result_path()
    #         zippath = os.path.join(readConfig.proDir, "testResult", "test.zip")
    #
    #         # zip file
    #         files = glob.glob(reportpath + '\*')
    #         f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
    #         for file in files:
    #             # 修改压缩文件的目录结构
    #             f.write(file, '/report/'+os.path.basename(file))
    #         f.close()
    #
    #         reportfile = open(zippath, 'rb').read()
    #         filehtml = MIMEText(reportfile, 'base64', 'utf-8')
    #         filehtml['Content-Type'] = 'application/octet-stream'
    #         filehtml['Content-Disposition'] = 'attachment; filename="test.zip"'
    #         self.msg.attach(filehtml)

    # def check_file(self):
    #     """
    #     check test report
    #     :return:
    #     """
    #     reportpath = self.log.get_report_path()
    #     if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
    #         return True
    #     else:
    #         return False

    def attachment_file(self):
        # 获取html文件路径，添加到邮件附件
        # html_path = localReadConfig.get_report('report_url')
        # html_path = "D:\\interfaceTest\\testResult\\html\\20171117\\20171117_103650.html"
        attachment = MIMEText(open(self.html_path, 'rb').read(), 'base64', 'gb2312')
        attachment['Content-Type'] = 'application/octet-stream'
        attachment["Content-Disposition"] = 'attachment; filename="test_report.html"'
        self.msg.attach(attachment)
        print '1'

    def send_email(self):
        """
        send email
        :return:
        """
        self.config_header()
        self.config_content()
        self.attachment_file()
        # try:
        #     smtp = smtplib.SMTP()
        #     smtp.connect(host)
        #     smtp.login(user, password)
        #     smtp.sendmail(sender, self.receiver, self.msg.as_string())
        #     smtp.quit()
        #     self.logger.info("The test report has send to somebody by email.")
        # except Exception as ex:
        #     self.logger.error(str(ex))

        smtp = smtplib.SMTP()
        smtp.connect(host)
        smtp.login(user, password)
        smtp.sendmail(sender, self.receiver, self.msg.as_string())
        smtp.quit()
        # self.logger.info("测试报告邮件发送完成.")


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    # email = MyEmail.get_email()
    # print email
    Email().send_email()

