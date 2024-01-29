import json
import cx_Oracle
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


config = json.load(open('SFIS.json'))
username = config['username']
password = config['password']
dsn = config['DB_URL']

conn = cx_Oracle.connect(username, password, dsn)
cursor = conn.cursor()
cursor.execute("select DISTINCT(SHIPPING_SN) from SFISM4.R_SN_DETAIL_T where SHIPPING_SN like '120-636%'")

rows = cursor.fetchall()
descs = cursor.description

df = pd.DataFrame(rows, columns=[d[0] for d in descs])
customer = 'ZEBRA'
total = int('120-63616741'[len('120-636'):]) - int(df['SHIPPING_SN'].min()[len('120-636'):]) + 1
start = df['SHIPPING_SN'].min()
end = config['max_ssn']
last = df['SHIPPING_SN'].max()
left = total - len(df)
percent = round((len(df) / total) * 100, 2)
cursor.close()
conn.close()

str_out = """
    <table border="1">
        <tr bgcolor="yellow">
            <td>Customer</td>
            <td>Start SSN</td>
            <td>Last Used</td>
            <td>End SSN</td>
            <td>Total SSN</td>
            <td>SSN Left</td>
            <td>Used Percent</td>
        </tr>
    """
str_out += '<tr>'
str_out += '<td>' + customer + '</td>'
str_out += '<td>' + start + '</td>'
str_out += '<td>' + last + '</td>'
str_out += '<td>' + end + '</td>'
str_out += '<td>' + str(total) + '</td>'
str_out += '<td>' + str(left) + '</td>'
if percent >= 80:
    str_out += '<td bgcolor="red">' + str(percent) + '%' + '</td>'
else:
    str_out += '<td>' + str(percent) + '%' + '</td>'
str_out += '</tr>'
str_out += '</table>'

# Email configuration
sender_email = config['sender']
receiver_email = config['01_MailAlertTo']
subject = 'Table Data'
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Cc'] = config['01_MailCC']
message['Subject'] = subject
print(message)
# Attach the HTML content to the email
# message.attach(MIMEText(str_out, "html"))

# # Connect to the SMTP server and send the email
# smtpHost = config['smtpHost']
# smtpPort = config['smtpPort']
# smtpPassword = config['smtpPassword']
# with smtplib.SMTP(host=smtpHost, port=smtpPort) as server:
#     server.login(sender_email, smtpPassword)
#     server.sendmail(sender_email, receiver_email, message.as_string())
