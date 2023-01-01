from urllib.request import urlopen
import smtplib
from datetime import datetime
import os
# from dotenv import load_dotenv, find_dotenv FOR LOCAL USE
from lxml import etree

# load_dotenv(find_dotenv()) FOR LOCAL USE

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# start_time = time.time()

COURSES_REQUESTED = [46668] #list of CRNs - this is a test CRN

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_PASSWORD')
MY_NUMBER = os.environ.get('MY_NUMBER')

f = open("eventlog.txt", "a+")

def is_open(CRN_NUMBER):
    #checks if there is at least ONE SEAT OPEN
    TERM = "202311"
    URL = f"https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_detail_sched?term_in={TERM}&crn_in={CRN_NUMBER}"
    response = urlopen(URL)
    html_parser = etree.HTMLParser()
    tree = etree.parse(response, html_parser)
    seats_avaliable = tree.xpath("/html/body/div[3]/table[1]/tr[2]/td/table/tr[2]/td[3]")[0].text
    course_info = tree.xpath("/html/body/div[3]/table[1]/tr[1]/th")[0].text
    if int(seats_avaliable) > 0:
        send_text(course_info, CRN_NUMBER)


def send_text(COURSE_REQUESTED, CRN_NUMBER): #executes if is_open calls when there is at least one seat
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(MY_EMAIL, MY_PASSWORD)
    contents = f"Course {COURSE_REQUESTED} CRN {CRN_NUMBER} Open!"
    s.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="{MY_NUMBER}@vtext.com",
            msg=f"Subject:Course Tracker Alert!\n\n{contents}"
    )
    f.write(f"{CRN_NUMBER} | {current_time} \n")


def lambda_handler(event, context):
    print(event)
    for course in COURSES_REQUESTED:
        is_open(course)
    

f.close()


# print("--- %s seconds ---" % (time.time() - start_time))







