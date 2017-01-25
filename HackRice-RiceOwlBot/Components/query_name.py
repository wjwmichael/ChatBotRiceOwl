# Write or paste code here. You can also use the blueprints as a starting point.
# Write or paste code here. You can also use the blueprints as a starting point.
# Write or paste code here. You can also use the blueprints as a starting point.
from meya import Component
from meya.cards import Button
from meya.cards import Card

class query_name(Component):

    def start(self):
        condition = str(self.db.flow.get('course_subject'))
        print condition
        conditional =  self.db.table('course_data_1').filter(subject=condition)
        print conditional
        info = ""
        messages = []
        imgsrc = "https://s9.postimg.org/56ckls6gv/Duncan_Hall.jpg"
        for courses in conditional:
            title = "Course Title:"+str(courses.get('title'))
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
                ]
            card = Card(
                title = title,
                text = location+'\n'+'\n'+description,
                image_url=imgsrc,
                buttons=buttons,
                )
            message = self.create_message(card=card)
            messages.append(message)
        
        # self.db.table('course').filter(name__contains="COMP")
        return self.respond(messages=messages, action="next")