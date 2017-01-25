# -*- coding: utf-8 -*-
from meya import Component


class listDepCourses(Component):

    def start(self):
        depName = self.db.flow.get('dep_name')
        depName = str(depName)
        depName_ = depName[0:4].upper()
        lists = self.db.table('course_data_1').filter(subject = depName_)
        courses = [];
        if not lists:
            message = "no course"
        else:
            for single in lists:
                courses.append(single['number'] + "  " + single['title'])
            message = self.create_message(text='\n'.join(courses))
        return self.respond(message=message, action="decline_next")