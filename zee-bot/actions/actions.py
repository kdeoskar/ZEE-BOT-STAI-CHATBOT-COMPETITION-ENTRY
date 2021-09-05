# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ValidateSchoolForm(Action):
    def name(self) -> Text:
        return "class_form"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[EventType]:

        required_slots = ["class","month","year","exam","message","subject1","email","subject","uniform","name","break"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:

                return [SlotSet("requested_slot",slot_name)]



        return [SlotSet("requested_slot",None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
    
        dispatcher.utter_message(template="utter_timetable_val", Name=tracker.get_slot("class"))
        return []

class Actionvideo(Action):
    def name(self) -> Text:
       return "school_vd"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        url="https://www.youtube.com/watch?v=0_e-wmnYPsw"
        dispatcher.utter_message("... Playing the video!")
        webbrowser.open(url)
        return []

class timetablepic(Action):
    def name(self) -> Text:
        return "show_timetable"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("class")
        D={"12A":"https://i.imgur.com/ryzkY6I.jpeg","12B":"https://i.imgur.com/rR3zZAm.jpeg","12C":"","12D":"","11A":"","11B":"","11C":"","11D":""}
        for dict in D.keys(): 
            print(name)
            if name==dict:
                val=D[dict] 
                print(val)   
                dispatcher.utter_message(image=val)
                
        return []



class timetablepic(Action):
    def name(self) -> Text:
        return "academic_calendar"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        month=tracker.get_slot("month")
        year=tracker.get_slot("year")
        print(year)
        print(type(year))
        D={"January":"Information of the academic year 2020-21 is not available! please retry","February":"Information of the academic year 2020-21 is not available! please retry",'March':"Information of the academic year 2020-21 is not available! please retry",'April':"https://i.imgur.com/f0Cffww.jpeg",'May':"https://i.imgur.com/ifhIV3S.jpeg",'June':"https://i.imgur.com/1UGk0jd.jpeg",'July':"https://i.imgur.com/oRUJAfj.jpeg",'August':"https://i.imgur.com/TskCuP9.jpeg",'September':"https://i.imgur.com/pb1zmal.jpeg",'October':"https://i.imgur.com/1bgxlEU.jpeg",'November':"https://i.imgur.com/KFOnmNq.jpeg",'December':"https://i.imgur.com/iEU89bG.jpeg"}
        D1={"January":"https://i.imgur.com/6Qkp79F.jpeg","February":"https://i.imgur.com/yoQgyBs.jpeg",'March':"https://i.imgur.com/OVKzB8L.jpeg",'April':"https://i.imgur.com/yoioSU7.jpeg",'May':"https://i.imgur.com/wl3WklD.jpeg",'June':"https://i.imgur.com/rV5bzTJ.jpeg",'July':"https://i.imgur.com/sof0F4p.jpeg",'August':"https://i.imgur.com/xNj9NlK.jpeg",'September':"Sorry, the table has not been updated from August 2022 onwards! please retry",'October':"Sorry, the table has not been updated from August 2022 onwards! please retry",'November':"Sorry, the table has not been updated from August 2022 onwards! please retry",'December':"Sorry, the table has not been updated from August 2022 onwards! please retry"}
        if year=="2021":
            for i in D.keys():
                if i==month:
                    val= D[i]
                    print(val)
                    if val=="Information of the academic year 2020-21 is not available! please retry":
                        dispatcher.utter_message(response="utter_academic_calendar",text=val)
                    else:
                        dispatcher.utter_message(response="utter_academic_calendar",image=val)
        elif year=="2022":
            for i in D1.keys():
                if i==month:
                    val= D1[i]
                    print(val)
                    if val=="Sorry, the table has not been updated from August 2022 onwards! please retry":
                        dispatcher.utter_message(template="utter_academic_calendar",text="Sorry, the table has not been updated from August 2022 onwards! please retry")
                    else:
                        dispatcher.utter_message(template="utter_academic_calendar",image=val)


class ExamSyllabus(Action):
    def name(self) -> Text:
        return "show_exam"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        cls = tracker.get_slot("class")
        exam = tracker.get_slot("exam")
        sub = tracker.get_slot("subject1")
        print("subject = ",sub)

        L=["final","halfyearly","preboard"]
        L1 = ["12A","12B","12C","12D","11A","11B","11C","11D","10A","10B","10C","10D","9A","9B","9C","9D","8A","8B","8C","8D","7A","7B","7C","7D","6A","6B","6C","6D","5A","5B","5C","5D","4A","4B","4C","4D","3A","3B","3C","3D","2A","2B","2C","2D","1A","1B","1C","1D"]
        D = {"maths":"https://i.imgur.com/h4Hcf6Z.jpeg","phy":"https://i.imgur.com/rcV7Hs2.jpeg","chem":"https://i.imgur.com/osH6KCz.jpeg","eng":"https://i.imgur.com/Aht65uG.jpeg","cs":"https://i.imgur.com/Uy3yrlm.jpeg"}
        D1 = {"maths":"https://i.imgur.com/N0kW8MH.jpeg","phy":"https://i.imgur.com/xVt20wA.jpeg","chem":"https://i.imgur.com/V4VvbYZ.jpeg","eng":"https://i.imgur.com/IpPgSkG.jpeg","cs":"https://i.imgur.com/rLh98Qj.jpeg"}
        if exam in L:
            for i in D.keys():
                if i==sub:
                    val1 = D[i]
                    print("The value of val1 is")
                    print(val1)
                    dispatcher.utter_message(image=val1)
            
        elif exam == "periodic":
            for j in D1.keys():
                if j==sub:
                    val2 = D1[j]
                    print(val2)
                    dispatcher.utter_message(image=val2)

        return[]

class ZoomIDS(Action):
    def name(self) -> Text:
        return "show_zoom"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name = tracker.get_slot("class")
        D = {"11A":"https://i.imgur.com/w5Zjzcx.jpeg","11B":"https://i.imgur.com/QfTXIXb.jpeg","11C":"https://i.imgur.com/z8RjKyL.jpeg","11D":"https://i.imgur.com/itgvPS0.jpeg","11E":"https://i.imgur.com/dTYhTSH.jpeg","12A":"https://i.imgur.com/FBZjOkU.jpeg","12B":"https://i.imgur.com/wjPFf7b.jpeg","12C":"https://i.imgur.com/gvcKsf1.jpeg","12D":"https://i.imgur.com/23tVRBO.jpeg","12E":"https://i.imgur.com/n0Znsa2.jpeg"}
        for dict in D.keys():
            if dict==name:
                val=D[dict]
                print(name)
                dispatcher.utter_message(image=val)

class EmailIDS(Action):
    def name(self) -> Text:
        return "show_email_ids"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name = tracker.get_slot("class")
        D = {"11A":"https://i.imgur.com/Miol4XI.jpeg","11B":"https://i.imgur.com/Miol4XI.jpeg","11C":"https://i.imgur.com/Miol4XI.jpeg","11D":"https://i.imgur.com/Miol4XI.jpeg","11E":"https://i.imgur.com/Miol4XI.jpeg","12A":"https://i.imgur.com/Miol4XI.jpeg","12B":"https://i.imgur.com/Miol4XI.jpeg","12C":"https://i.imgur.com/Miol4XI.jpeg","12D":"https://i.imgur.com/Miol4XI.jpeg","12E":"https://i.imgur.com/Miol4XI.jpeg"}
        for dict in D.keys():
            if dict==name:
                val=D[dict]
                print(name)
                dispatcher.utter_message(image=val)

class SchoolContacts(Action):
    def name(self) -> Text:
        return "school_contacts"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        val="https://i.imgur.com/5nQWWSc.png"
        dispatcher.utter_message(text="You can contact us through email and/or by number",image=val)




class Schoolfees(Action):
    def name(self) -> Text:
        return "school_fees"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name = tracker.get_slot("class")
        D = {"11A":"https://i.imgur.com/rL2nqKT.jpeg","11B":"https://i.imgur.com/rL2nqKT.jpeg","11C":"https://i.imgur.com/rL2nqKT.jpeg","11D":"https://i.imgur.com/rL2nqKT.jpeg","11E":"https://i.imgur.com/rL2nqKT.jpeg","12A":"https://i.imgur.com/wZrdTrt.jpeg","12B":"https://i.imgur.com/wZrdTrt.jpeg","12C":"https://i.imgur.com/wZrdTrt.jpeg","12D":"https://i.imgur.com/wZrdTrt.jpeg","12E":"https://i.imgur.com/Miol4XI.jpeg"}
        for dict in D.keys():
            if dict==name:
                val=D[dict]
                print(name)
                dispatcher.utter_message(image=val)

class ReportCard(Action):
    def name(self) -> Text:
        return "show_report_card"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("name")
        cls=tracker.get_slot("class")
        val="https://i.imgur.com/boRONdS.png"
        dispatcher.utter_message(text="{} studying in {} here's you report card..".format(name,cls),image=val)

        return[]

class event(Action):
    def name(self) -> Text:
        return "show_event"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("event")
        D={"mun":"https://i.imgur.com/FTeMwT4.jpeg","fest":"https://i.imgur.com/l5wKsMm.jpeg","quiz":"https://i.imgur.com/RtIGTI5.jpeg","art":"https://i.imgur.com/JE21Mej.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)   

class event(Action):
    def name(self) -> Text:
        return "show_event_contacts"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("event")
        D={"mun":"https://i.imgur.com/6m8Iwrj.png","fest":"https://i.imgur.com/6m8Iwrj.png","quiz":"https://i.imgur.com/6m8Iwrj.png","art":"https://i.imgur.com/6m8Iwrj.png"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)   


class EmailSubmit(Action):
    def name(self) -> Text:
        return "email_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        SendEmail1(
            tracker.get_slot("email"),
            tracker.get_slot("subject"),
            tracker.get_slot("message")
        )
        dispatcher.utter_message("Thanks for providing the details. We have sent you a mail at {}".format(tracker.get_slot("email")))
        return []

def SendEmail1(toaddr,subject,message):
    fromaddr = "chatbotxyz2021@gmail.com"
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
    # attachment = open(filename, "rb")
    #
    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')
    #
    # # To change the payload into encoded form
    # p.set_payload((attachment).read())
    #
    # # encode into base64
    # encoders.encode_base64(p)
    #
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # # attach the instance 'p' to instance 'msg'
    # msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()


    # Authentication
    try:
        s.login(fromaddr, "1234@xyz")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
    except:
        print("An Error occured while sending email.")
    finally:
        # terminating the session
        s.quit()


class LeaveSubmit(Action):
    def name(self) -> Text:
        return "leave_note_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        SendEmail(tracker.get_slot("message"),toaddr='xyzinternational.s@gmail.com',subject='Leave Note')
        dispatcher.utter_message("Thanks for providing the message. We have sent a mail regarding your absence")
        return []

def SendEmail(message,toaddr,subject):
    fromaddr = "chatbotxyz2021@gmail.com"
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
    # attachment = open(filename, "rb")
    #
    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')
    #
    # # To change the payload into encoded form
    # p.set_payload((attachment).read())
    #
    # # encode into base64
    # encoders.encode_base64(p)
    #
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # # attach the instance 'p' to instance 'msg'
    # msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()


    # Authentication
    try:
        s.login(fromaddr, "1234@xyz")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
    except:
        print("An Error occured while sending email.")
    finally:
        # terminating the session
        s.quit()




class ReportEmailSubmit(Action):
    def name(self) -> Text:
        return "report_email_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("name")
        cls=tracker.get_slot("class")
        sub="{} Report Card of {}".format(cls,name)
        mes="{}'s Report Card is attached herewith. He has done exceptionaly well! Please collect the cirtificate of excellence on the day of The Award Ceremony.    Here is the Report Card  https://i.imgur.com/boRONdS.png    ".format(name)
        SendEmailReport(tracker.get_slot("email"),subject=sub,message=mes)
        dispatcher.utter_message("Thanks for providing the details. We have sent a copy of your report card at {}".format(tracker.get_slot("email")))
        return []

def SendEmailReport(toaddr,subject,message):
    fromaddr = "chatbotxyz2021@gmail.com"
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = subject

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    # filename = "/home/ashish/Downloads/webinar_rasa2_0.png"
    # attachment = open(filename, "rb")
    #
    # # instance of MIMEBase and named as p
    # p = MIMEBase('application', 'octet-stream')
    #
    # # To change the payload into encoded form
    # p.set_payload((attachment).read())
    #
    # # encode into base64
    # encoders.encode_base64(p)
    #
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    #
    # # attach the instance 'p' to instance 'msg'
    # msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()


    # Authentication
    try:
        s.login(fromaddr, "1234@xyz")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
    except:
        print("An Error occured while sending email.")
    finally:
        # terminating the session
        s.quit()


class ActionCovid(Action):
    def name(self) -> Text:
       return "covid_cases"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        url="https://www.worldometers.info/coronavirus/country/oman/"
        dispatcher.utter_message("...Loading Covid cases")
        webbrowser.open(url)
        return []

class SchoolUniform(Action):
    def name(self) -> Text:
        return "school_uniform"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("uniform")
        D={"senior uniform":"https://i.imgur.com/xZuEwVf.jpeg","junior uniform":"https://i.imgur.com/SSN8Yj1.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(responce='utter_found_uniform',image=val) 
class SchoolHolidays(Action):
    def name(self) -> Text:
        return "holidays"
    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        name=tracker.get_slot("break")
        D={"summer break":"https://i.imgur.com/1UGk0jd.jpeg","winter break":"https://i.imgur.com/iEU89bG.jpeg"}
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(text="This is the {} schedule".format(name),image=val)   