import requests,smtplib,ssl
from bs4 import BeautifulSoup
from email.mime.* import MIMEText, MIMEMultipart
import time
sender="xxxx@gmail.com"
reciever="xxxx@xxxx.com"
data=None
# im using these headers because the sites I scrape are setup 
# to not allow scraping
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
globalStock=None #  You can either parse through and find this or input at beginning
port=465
password= "xxxx"
context=ssl.create_default_context()
message=MIMEMultipart("ALERT")
message["Subject"]="Mercari Alert"
message["From"]=sender
message["To"]=reciever
textmsg="Whatever alert message you'd like"
part=MIMEText(textmsg,"plain") #  plain denotes style argument for MIMEText constructor (vs "html")
message.attach(part)
# this part assumes sender is using a gmail address and has allowed lower security access in their 
# google privacy settings. I reccomend you make another gmail account solely for automation and alert 
# purposes and forward alert emails to a main email or a iMessage email to recieve texts
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
while True:
    time.sleep(10)
    data=requests.get("google.com",headers=headers)
    soup=BeautifulSoup(data.text,'html.parser')
    # This code below is where you have to develop something to parse
    # and either monitor for a price change or for a global stock number change
    # or for any other cvhange in page data 

    # the commented code below shows an example of using BeautifulSoup
    # to parse through the HTML and return data 
    # What my specific example does is parse through all of the items 
    # on a grid-style listing website and find the listed stock number
    # and then compare to a locally stored
    # 
    '''
    string=soup.find("div",{"class":"search-result-number"}).string
    string.split("1")
    string.split("件")
    string.split()
    number =int(''.join(c for c in string if c.isdigit() and c!='1'))
    '''
    globalStock=number
    if(number > globalStock):
        server.sendmail(sender,reciever,message.as_string())
        if(input("Continue Running? (Y/N)")=="N"):
            break
        globalStock = number
    # If something has sold and the global stock is less
    if(number < globalStock): 
        globalStock = number
    

        

    

        