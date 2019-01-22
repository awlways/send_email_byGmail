# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import time


def send_email(receiver, reveiver_name):
    username = 'smartiot.conf@gmail.com'
    password = '*******'
    sender = 'smartiot.conf@gmail.com'

    HOST = 'smtp.gmail.com'
    PORT = 25
    #主题
    subject = 'IEEE SmartIoT 2019, 9-11 August, 2019 at Tianjin, China'

    #邮件主题
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = 'SmartIoT 2019 <smartiot.conf@gmail.com>'
    msg['To'] = receiver

    #文字内容
    text = '''
    Dear Colleagues,

    Sorry if you receive this message multiple times. We really appreciate if you would 
    consider submitting your work to IEEE SmartIoT 2019, which will be located at Tianjin, China in 9-11 August, 2019. 

    The submission due date is May 10, 2019.

    If you have any question regarding it, please do not hesitate to contact us. Thank you.

    Look forwards to receiving your submission.  
    Best regards.

    IEEE SmartIoT 2019 Organization Committee
    smartiot.conf@gmail.com

    -------------------------------------------------------------------------------
    2019 IEEE International Conference on Smart Internet of Things (IEEE SmartIoT2019)
    Tianjin, China
    9-11 August, 2019
    http://www.ieee-smartiot.org/
    -------------------------------------------------------------------------------

    CALL FOR PAPERS

    Internet of Things (IoT) plays an important role in the current and future generation of information, network, and communication developing and applications. Smart IoT is an exciting emerging research field that has great potential to transform both our understanding of fundamental computer science principles and our standard of living. IoT is being employed in more and more areas making “Everything Smart”, such as smart home, smart city, intelligent transportation, environment monitoring, security systems, and advanced manufacturing. IEEE International Conference on Smart Internet of Things (IEEE SmartIoT) focuses on these challenges.

    2019 IEEE International Conference on Smart Internet of Things (IEEE SmartIoT 2019) will be held on 9th-11th, August 2019 at Tianjin, China. The primary goal of IEEE SmartIoT 2019 is to exchange, share and discuss the latest research, theories and applications for Smart Internet of Things and Cyber-Physical Systems (CPS). Prospective authors are invited to submit original research papers, which propose new methodologies, propose new research directions and discuss approaches or schemes for current existing issues. 

    Topics of interests include, but are not limited to:

    + Track 1. IoT Sensing, monitoring, networking and routing
    + Track 2. Big data analysis and Cloud computing
    + Track 3. Edge computing/Fog computing
    + Track 4. Smart cities, intelligent transportation and internet of vehicles
    + Track 5. Artificial Intelligence, Machine learning and Evolutionary Computing
    + Track 6. Social networks, multimedia and mobile computing
    + Track 7. Blockchain and Emerging research or Technologies
    + Track 8. Industrial 4.0 and Industrial IoT
    + Track 9. Control and decision making for smart IoT or CPS
    + Track 10. Security and privacy for smart IoT or CPS 

    SUBMISSION and PUBLICATION

    Papers need to be prepared according to the IEEE format, and submitted in PDF format via the SmartIoT 2019 submission site: https://ieee-smartiot.org/submission.jsp
    Accepted and presented papers will be included in the IEEE Conference Proceedings published by IEEE CS Press (indexed by EI). At least one author of accepted papers MUST register and present their work at the conference; otherwise, their papers will be removed from the digital libraries of IEEE CS and EI after the conference. Authors of 50% papers will be invited to submit their paper to a special issue in a SCI-indexed journal. Information about these journal special issues are available on the website.

    JOURNAL SPECIAL ISSUES

    Future Generation Computer Systems  (Elsevier, SCI, IF: 3.997)
    Ad Hoc Networks  (Elsevier, SCI, IF: 3.047)
    IEEE Access  (IEEE Journal, SCI, IF: 3.244)
    Sensors  (MDPI Journal, SCI, IF: 2.677)
    The Journal of Supercomputing  (Springer, SCI, IF: 1.326)
    Cluster Computing  (Springer, SCI, IF: 2.040)
    IEEE Transactions on Network Science and Engineering (IEEE, SCI)


    IMPORTANT DATES

    Submission Due: 10 May 2019
    Author Notification: 1 June 2019
    Camera-ready Paper Due: 20 June 2019
    Registration Due: 10 Aug 2019
    Conference Date: 9-11 Aug 2019

    Any question, please feel free to contact IEEE SmartIoT2019 Team
    by E-mail: smartiot.conf@gmail.com

    '''
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 构造附件
    sendfile = open(r'D:\\smartIOT\\CallForPaper\\2019\\SmartIoT2019-CFP.pdf', 'rb').read()
    text_att = MIMEText(sendfile, 'base64', 'utf-8')
    text_att["Content-Type"] = 'application/octet-stream'
    text_att.add_header('Content-Disposition', 'attachment', filename='SmartIoT2019-CFP.pdf')
    msg.attach(text_att)
    ret = True
    try:
        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(HOST, PORT)
        smtp.starttls()
        # smtp.set_debuglevel(1)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception:
        ret=False
    return ret

if __name__ == '__main__':
    receiver = csv.reader(open("D:\\smartIOT\\sendemail\\remaining.csv"))
    # resultsFile = open("D:\\smartIOT\\sendemail\\sendResult.txt","w+")
    with open("D:\\smartIOT\\sendemail\\sendResult.txt","a+") as resultsFile:
        resultsFile.write("email,name,status\r\n")
        for i in receiver:
            # Flag = send_email(i[0],i[1])
            Flag = send_email("weining@tju.edu.cn","dxd")
            # Flag = send_email("279288120@qq.com", "weining")
            Flag = True
            s = i[0]+","+i[1]
            if Flag:
                s += ",True"
            else:
                s += ",Flase"
            print s
            resultsFile.write(s+"\n")
            resultsFile.flush()
            time.sleep(5)
            break


