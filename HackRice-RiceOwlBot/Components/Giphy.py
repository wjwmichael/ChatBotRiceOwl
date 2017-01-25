# Write or paste code here. You can also use the blueprints as a starting point.
# -*- coding: utf-8 -*-
from meya import Component
from meya.cards import Image
import requests

API_KEY = "dc6zaTOxFJmzC"
API_URL = "http://api.giphy.com/v1/gifs/random?tag={tag}&api_key={key}"


class Giphy(Component):
    """Outputs a random giphy url based on passed in tag as either
    a property or flow db"""

    def start(self):
        # read in the gif type from the flow datastore
        # learn more: http://docs.meya.ai/docs/database-overview
        tag ="funny"

        # use the requests package to make an API call to giphy
        response = requests.get(API_URL.format(tag=tag, key=API_KEY))
        image_url = response.json()['data']['image_url']

        # create an image card and create the corresponding message
        image_card = Image(image_url=image_url)
        message = self.create_message(card=image_card)

        # respond with the message and "next" action
        return self.respond(message=message, action="next")