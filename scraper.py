import requests
# Essentially allows us to access a URl/ URL's.
from bs4 import BeautifulSoup
# BeautifulSoup allows us to parse that website data.
import smtplib
import time
from email.mime.multipart import MIMEMultipart # MIME message type combines HTML and plain text.
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


Uname = '' # Enter Username here.
Pword = '' # Enter password here.
Faddr = Uname + '' # Enter the from email address.
Taddr = '' # Enter the to email address.





url = 'https://www.amazon.co.uk/Canon-1-2L-USM-Lens-Black/dp/B000I2J2S6/ref=sr_1_5?crid=2MWU8TLJB6W7V&dchild=1&keywords=canon+1.4+50mm&qid=1601990115&sprefix=canon+1.4%2Caps%2C147&sr=8-5'

# Giving some information about our browser.
headers = {} # Here we would enter our User Agent, found by googling User Agent.


def check_price():
    # This is collecting all that data from the website.
    page = requests.get(url, headers=headers)

    # Here we create another variable called soup and pass in two arguments.
    # Additional note. I substitued out html.parser for html5lib as either this or lxml has the capability to fix
    # botched html elements which in this case were not letting me parse the title.
    soup = BeautifulSoup(page.content, 'html5lib')


    # Created a variable called title and using BeautifulSoup, returns the product title as it is called.
    # For price we are converting from text to numbers, then targeting specifically the first 6 numbers.
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").text.replace(",","")
    # With replace(",", "") will remove the problematic syntax error coming from the , thus can be converted to float.
    converted_price = float(price[1:5])

    if(converted_price < 1449.0):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 1449.0):
        send_mail()


def send_mail(username, password, fromaddr, toaddr, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('','') # Enter Username and Password

    subject = 'Lens price dropped!!'
    body = 'Check the Amazon link https://www.amazon.co.uk/Canon-1-2L-USM-Lens-Black/dp/B000I2J2S6/ref=sr_1_5?crid=2MWU8TLJB6W7V&dchild=1&keywords=canon+1.4+50mm&qid=1601990115&sprefix=canon+1.4%2Caps%2C147&sr=8-'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '', # Enter from email address.
        '', # Enter to email address.
        msg
    )
    print('HEY THE EMAIL HAS BEEN SENT')

    server.quit()


def email_stock_info(username, password, fromaddr, toaddr):
    email_msg = ''
    html_msg  = """\
	<html>
		<head>The lens price has droppped!!:</head>
		<body>
			<p>Check the Amazon link https://www.amazon.co.uk/Canon-1-2L-USM-Lens-Black/dp/B000I2J2S6/ref=sr_1_5?crid=2MWU8TLJB6W7V&dchild=1&keywords=canon+1.4+50mm&qid=1601990115&sprefix=canon+1.4%2Caps%2C147&sr=8-</p>
        </body>
    </html>
	"""

    mime_msg = MIMEMultipart('alternative')
    mime_msg.attach(MIMEText(email_msg, 'plain'))
    mime_msg.attach(MIMEText(html_msg, 'html'))


    body = ''

    mime_msg['Subject'] = 'Canon 50mm 1.2f lens'
    mime_msg['From'] = fromaddr
    mime_msg['To'] = toaddr


    send_mail(username, password, fromaddr, toaddr, mime_msg)



if __name__ == '__main__':
    email_stock_info(Uname, Pword, Faddr, Taddr)

check_price()

# Scope to use while loop and time sleep to check for the price drop every set time.

# while(True):
#     check_price()
#     time.sleep(60 * 60)
