# Write or paste code here. You can also use the blueprints as a starting point.
# -*- coding: utf-8 -*-
from meya import Component

class generalCourse(Component):

    def start(self):
        answer = self.db.flow.get('answer')
        answer = str(answer)
        if answer == "Yes" or answer == "yes":
           action = "have"
        else:
           action = "decline"
        return self.respond(message=None, action = action)