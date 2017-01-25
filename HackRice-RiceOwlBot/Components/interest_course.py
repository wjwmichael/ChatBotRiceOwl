# Write or paste code here. You can also use the blueprints as a starting point.
from meya import Component
from meya.cards import Button
from meya.cards import Card

class interest_course(Component):

    def start(self):
        depName = self.db.flow.get('dep_name')
        interest = self.db.flow.get('interest')
        depName = str(depName)
        interest = str(interest)
        depName_ = depName[0:4].upper()
        lists = self.db.table('course_data_1').filter(subject = depName_)
        courses = [];
        messages = []
        if not interest:
            message = "you should input interest"
            messages.append(message)
        else:
            for courses in lists:
                if interest.lower() in courses['description'].lower():
                    title = "Course Title: "+str(courses.get('title'))
                    location = "Location:"+str(courses.get('location'))
                    find = location.find('DCH')
                    if find>-1:
                        imgsrc = self.db.table('img_data_1').filter(location = "DCH")[0].get('imgsrc');
                    find = location.find('HUM')
                    if find>-1:
                        imgsrc = self.db.table('img_data_1').filter(location = "HUM")[0].get('imgsrc');
                    find = location.find('HEB')
                    if find>-1:
                        imgsrc = self.db.table('img_data_1').filter(location = "HEB")[0].get('imgsrc');
                    find = location.find('HRG')
                    if find>-1:
                        imgsrc = self.db.table('img_data_1').filter(location = "HRG")[0].get('imgsrc');
                    description = "Discription:"+str(courses.get('description'))
                    buttons = [
                        Button(text="This course is great!", action = "course_rock"),
                        Button(text="This course is not so great!", action = "course_sucks"),
                        Button(text="I'm going to the class now",action = "cal_distance")
                        ]
                    card = Card(
                        title = title,
                        text = location+'\n'+'\n'+description,
                        image_url=imgsrc,
                        buttons=buttons,
                        )
                    message = self.create_message(card=card)
                    messages.append(message)
        return self.respond(messages=messages, action="next")