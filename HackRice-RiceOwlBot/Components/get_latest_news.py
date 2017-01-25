# Write or paste code here. You can also use the blueprints as a starting point.
from meya import Component
import requests
from bs4 import BeautifulSoup
from meya.cards import Button
from meya.cards import Card
 
class get_latest_news(Component):
 
    def start(self):
        # read in the age, and default to `0` if invalid or missing
        r = requests.get("http://news.rice.edu/category/current-news/")
        soup = BeautifulSoup(r.text,"html.parser")
        ref = soup.find('h3',class_='entry-title').find('a')
        link = ref.get('href')
        newstitle = ref.string
        r2 = requests.get(link)
        soup2 = BeautifulSoup(r2.text,"html.parser")
        ref2 = soup2.find('div', class_='entry-content').find('img')
        imgsrc = ref2.get('src')
       
        buttons = [
            Button(text="Read More", url=link),
        ]
       
        card = Card(
            title = newstitle,
            text = "The news is for you. Enjoy! Hoo-hoo...",
            item_url = link,
            image_url=imgsrc,
            buttons=buttons,
        )
        message = self.create_message(card=card)
        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=message, action="next")