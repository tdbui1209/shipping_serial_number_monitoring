import json
from oracle_dataframe_query import OracleDataframeQuery
from email_sender import EmailSender


CONFIG = json.load(open('SFIS.json'))
USERNAME = CONFIG['username']
PASSWORD = CONFIG['password']
DSN = CONFIG['DB_URL']
CUSTOMER = CONFIG['customer']

# Query the data from the Oracle database
oracle_query = OracleDataframeQuery(USERNAME, PASSWORD, DSN)
query_command = "select DISTINCT(SHIPPING_SN) from SFISM4.R_SN_DETAIL_T where SHIPPING_SN like '120-636%'"
df = oracle_query.query(query_command)

# Calculate the total, start, end, last, numbers, and percent of remaining SSN
PREFIX_SSN = '120-636'
start = df['SHIPPING_SN'].min()
END = CONFIG['max_ssn']
last = df['SHIPPING_SN'].max()
total = int(END[len(PREFIX_SSN):]) - int(start[len(PREFIX_SSN):]) + 1
remaining = int(END[len(PREFIX_SSN):]) - int(last[len(PREFIX_SSN):]) + 1
percent_remaining = remaining / total * 100

# Create the HTML table
str_out = '''
    <table border='1'>
        <tr bgcolor='yellow'>
            <td>Customer</td>
            <td>Start SSN</td>
            <td>Last Used</td>
            <td>End SSN</td>
            <td>Total SSN</td>
            <td>SSN Left</td>
            <td>Used Percent</td>
        </tr>
    '''
str_out += '<tr>'
str_out += '<td>' + CUSTOMER + '</td>'
str_out += '<td>' + start + '</td>'
str_out += '<td>' + last + '</td>'
str_out += '<td>' + END + '</td>'
str_out += '<td>' + str(total) + '</td>'
str_out += '<td>' + str(remaining) + '</td>'
if percent_remaining >= 80:
    str_out += '<td bgcolor="red">' + str(percent_remaining) + '%' + '</td>'
else:
    str_out += '<td>' + str(percent_remaining) + '%' + '</td>'
str_out += '</tr>'
str_out += '</table>'

# Send the email
SUBJECT = 'Table Data'
email_sender = EmailSender(sender_email=CONFIG['sender'], receiver_email=CONFIG['01_MailAlertTo'],
                           subject=SUBJECT, message=str_out, host=CONFIG['smtpHost'],
                           port=CONFIG['smtpPort'], password=CONFIG['smtpPassword'])
email_sender.send_email()
