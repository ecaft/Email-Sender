import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

myaddress="example@email.com"
password="password"
def get_contacts(filename):
    name = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_files:
        for a_contact in contacts_files:
            emails.append(a_contact.split(' ',1)[0])
            name.append(a_contact.split(' ',1)[1].replace('\n','')) 
    return name, emails

def read_template(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content=template_file.read()
    return Template(template_file_content)

def main():
    names, emails=get_contacts('mycontacts.txt')
    message_template=read_template("message.txt")

    s=smtplib.SMTP(host='smtp.gmail.com',port=587)
    s.starttls()
    s.login(myaddress,password)

    for name,email in zip(names, emails):
        msg=MIMEMultipart()
        message=message_template.substitute(PERSON_NAME=name)
        msg['From']=myaddress
        msg['to']=email
        msg['Subject']='This is Test' #subject line
        msg.attach(MIMEText(message,'plain'))
        s.send_message(msg)
        del msg
    s.quit()
    print(message)
main()