#
#
# Gmail integration requires an account with "Less Secure App Access" enabled
# in the security settings.  Consider using a dedicated gmail account for this
# app.
#
#

import smtplib
import sys

def send_gmail(gmail_user, gmail_password, to, subject, body):

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
    except:
        print('Something went wrong with login...')
        end()

    if type(to)==list:
        email_to = ', '.join(to)
    else:
        email_to = to

    email_text = f'From: {gmail_user}\nTo: {email_to}\nSubject: {subject}\n\n{body}'
    print(email_text)

    try:
        server.sendmail(gmail_user, to, email_text)
        print('Email sent!')
    except:
        print('Something went wrong with email send...')

    server.close()

if __name__ == '__main__':
    #
    # send e-mail with cli
    # python3 gmail.py gmail_user@gmail.com password 'recipient1,recipient2,etc' 'subject' 'body'
    #
    send_gmail(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
