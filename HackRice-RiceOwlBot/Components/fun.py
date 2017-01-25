# Write or paste code here. You can also use the blueprints as a starting point.
# -*- coding: utf-8 -*-
import requests
import random
from meya import Component

fact=["The university’s founder and namesake, William Marsh Rice, buried his ashes on campus, beneath his statue. Making Rice the largest cemetery in all of Texas, with only one body buried on it. That we know of, at least… (Kidding! … probably).",
"The university has saved its students an estimated 30 million with its use of free textbooks.",
"The most famous Rice prank of all, in 1988, several students rotated the statue of William Rice so that he faced the Fondren library for the first time in 58 years. They even managed to convince a couple Houston police that they were doing a school project and were given a police escort to transport their materials.",
"Rice University is known for its pranking genius and loud gestures. In 1942, a student talked his friend at the Houston Zoo into letting him borrow a live elephant for a campaign. The sign read ‘this is no bull: vote for Baird’! (He won).",
"At the end of the year, seniors may take an unofficial ‘Purity Test’ containing 100 yes-or-no questions that gauge the various ‘activities’ they might have gotten up to during their time on campus.",
"In a tradition called Matriculation that is a close opposite of graduation, new students walk through the Sallyport and into the quad to integrate themselves into the university.",
"Rice is ranked second for universities with highest quality of life, and sixth for happiest students.",
"All students are required to finish two P.E. type classes of Lifetime Physical Activity Program, or LPAP, before graduation.",
"The wall at the entrance of Rice’s architecture building is known as the ‘Frog Wall’ for the croaking ‘frog noises’ it makes if you run your fingers over the holes.",
"Nearly half of all Rice students are from out of state."]
class fun(Component):
    def start(self):
        
        text=fact[random.randint(0,len(fact)-1)]
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")