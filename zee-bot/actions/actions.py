import sqlite3
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
import webbrowser


class ResetID(Action):

    def name(self) -> Text:
        return "action_reset_id"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Student ID reset, you can now enter a new one!")
        return [SlotSet("idno", None)]
      
class ValidateIdForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_id_form"

    def validate_idno(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE idno = :idno", {"idno": slot_value})
        a = c.fetchall()
        conn.close()

        if a == []:
            dispatcher.utter_message(text="Invalid id!")
            return {"idno": None}
        else:
            dispatcher.utter_message(text="Valid id!")
            return {"idno": slot_value}
        
class Actionvideo(Action):
    def name(self) -> Text:
       return "action_show_school_vid"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url="https://www.youtube.com/watch?v=0_e-wmnYPsw"
        dispatcher.utter_message("...Playing the video!")
        webbrowser.open(url)
        return []

class ExamSyllabus(Action):
    def name(self) -> Text:
        return "action_show_exam_syllabus"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
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

        return [SlotSet("class", None), SlotSet("exam", None), SlotSet("subject1", None)]
        
class ActionCovid(Action):
    def name(self) -> Text:
       return "action_show_COVIDinfo"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url="https://www.worldometers.info/coronavirus/country/oman/"
        dispatcher.utter_message("...Loading Covid cases")
        webbrowser.open(url)
        return []

class AcademicCalendar(Action):

    def name(self) -> Text:
        return "action_show_academic_calendar"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        month=tracker.get_slot("month")

        D={'April':"https://i.imgur.com/f0Cffww.jpeg",'May':"https://i.imgur.com/ifhIV3S.jpeg",'June':"https://i.imgur.com/1UGk0jd.jpeg",'July':"https://i.imgur.com/oRUJAfj.jpeg",'August':"https://i.imgur.com/TskCuP9.jpeg",'September':"https://i.imgur.com/pb1zmal.jpeg",'October':"https://i.imgur.com/1bgxlEU.jpeg",'November':"https://i.imgur.com/KFOnmNq.jpeg",'December':"https://i.imgur.com/iEU89bG.jpeg", "January":"https://i.imgur.com/6Qkp79F.jpeg","February":"https://i.imgur.com/yoQgyBs.jpeg",'March':"https://i.imgur.com/OVKzB8L.jpeg",}
        D1={"January":"https://i.imgur.com/6Qkp79F.jpeg","February":"https://i.imgur.com/yoQgyBs.jpeg",'March':"https://i.imgur.com/OVKzB8L.jpeg",'April':"https://i.imgur.com/yoioSU7.jpeg",'May':"https://i.imgur.com/wl3WklD.jpeg",'June':"https://i.imgur.com/rV5bzTJ.jpeg",'July':"https://i.imgur.com/sof0F4p.jpeg",'August':"https://i.imgur.com/xNj9NlK.jpeg",'September':"Sorry, the table has not been updated from August 2022 onwards! please retry",'October':"Sorry, the table has not been updated from August 2022 onwards! please retry",'November':"Sorry, the table has not been updated from August 2022 onwards! please retry",'December':"Sorry, the table has not been updated from August 2022 onwards! please retry"}

        for i in D.keys():
            if i==month:
                val= D[i]
                print(val)
                dispatcher.utter_message(text=f"Here is the academic calender for {month}",image=val)    
        return [SlotSet("month", None)]

class SchoolUniform(Action):

    def name(self) -> Text:
        return "action_show_uniform"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("uniform")
        D={"senior":"https://i.imgur.com/xZuEwVf.jpeg","junior":"https://i.imgur.com/SSN8Yj1.jpeg"}
        for dict in D.keys():
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(text='Here is the uniform',image=val)
                 
        return [SlotSet("uniform", None)]
        # if name=='senior':
        #     dispatcher.utter_message(image="https://i.imgur.com/xZuEwVf.jpeg") 
        
        # elif name=='junior':
        #     dispatcher.utter_message(image="https://i.imgur.com/SSN8Yj1.jpeg") 

# TO BE COMPLETED
class SchoolHolidays(Action):

    def name(self) -> Text:
        return "action_show_holiday"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("holiday")

        D={"summer break":"https://i.imgur.com/1UGk0jd.jpeg","winter break":"https://i.imgur.com/iEU89bG.jpeg"}
        for dict in D.keys():
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(text="This is the {} schedule".format(name),image=val)  

            elif name == "other":
                pass

class ZoomIDS(Action):
    def name(self) -> Text:
        return "action_show_zoom"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        idno = tracker.get_slot("idno")

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE idno = :idno", {"idno": idno})
        r = c.fetchone()
        conn.close()

        if r != None:
            cls = str(r[1])+r[2]
            D = {"11A":"https://i.imgur.com/w5Zjzcx.jpeg","11B":"https://i.imgur.com/QfTXIXb.jpeg","11C":"https://i.imgur.com/z8RjKyL.jpeg","11D":"https://i.imgur.com/itgvPS0.jpeg","11E":"https://i.imgur.com/dTYhTSH.jpeg","12A":"https://i.imgur.com/FBZjOkU.jpeg","12B":"https://i.imgur.com/wjPFf7b.jpeg","12C":"https://i.imgur.com/gvcKsf1.jpeg","12D":"https://i.imgur.com/23tVRBO.jpeg","12E":"https://i.imgur.com/n0Znsa2.jpeg"}
            for dict in D.keys():
                if dict==cls:
                    val=D[dict]
                    dispatcher.utter_message(image=val)
        
        elif r == None:
            dispatcher.utter_message(text="Student ID is required to access meeting ID's. Please enter yours and then ask for zoom meeting ID again!")
            #return [SlotSet("idno", "needed_for_zoom")]
        
class ReportCard(Action):

    def name(self) -> Text:
        return "action_show_report_card"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        idno = tracker.get_slot("idno")

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students WHERE idno = :idno", {"idno": idno})
        r = c.fetchone()
        conn.close()

        if r != None:
            val="https://i.imgur.com/boRONdS.png"
            dispatcher.utter_message(text=f"Here is your report card, {r[3]}!",image=val)

        if r == None:
            dispatcher.utter_message(text="Student ID is required to access meeting ID's. Please enter yours and then ask for your report card again!")
            #return [SlotSet("idno", "needed_for_report")]

class Events(Action):

    def name(self) -> Text:
        return "action_show_events"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name=tracker.get_slot("event")
        D={"mun":"https://i.imgur.com/FTeMwT4.jpeg",
        "fest":"https://i.imgur.com/l5wKsMm.jpeg",
        "quiz":"https://i.imgur.com/RtIGTI5.jpeg",
        "art":"https://i.imgur.com/JE21Mej.jpeg"}
        
        for dict in D.keys():
            print(name)
            if name==dict:
                val=D[dict]
                print(val)
                dispatcher.utter_message(image=val)  
        
        return [SlotSet("event", None)]

class timetablepic(Action):

    def name(self) -> Text:
        return "action_show_timetable"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cls=tracker.get_slot("class")
        D={"12A":"https://i.imgur.com/ryzkY6I.jpeg","12B":"https://i.imgur.com/rR3zZAm.jpeg","12C":"","12D":"","11A":"","11B":"","11C":"","11D":""}
        for dict in D.keys(): 
            if cls == dict:
                val = D[dict] 
                dispatcher.utter_message(image=val)
                
        return [SlotSet("class", None)]

