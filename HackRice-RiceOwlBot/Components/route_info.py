# Write or paste code here. You can also use the blueprints as a starting point.
from meya import Component
import requests
import json

class route_info(Component):
    def start(self):
        latdata = self.db.user.get('lat')
        latdata = str(latdata)
        lngdata = self.db.user.get('lng')
        lngdata = str(lngdata)
        
        duncan_hall_place = "29.7201321,-95.3987562"
        key = "AIzaSyDKrFOPZ2rLlOY98169PQhFsBsbXt_vs0A"
        requests_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+latdata+","+lngdata+"&destinations="+duncan_hall_place+"&key=" + key
        distance_json = requests.get(requests_url)
        json_formatted = json.loads(distance_json.text)
        duration = json_formatted[u'rows'][0][u'elements'][0][u'duration'][u'text']
        distance = json_formatted[u'rows'][0][u'elements'][0][u'distance'][u'text']
        route_info = "You are "+ distance + " away from your destination. It takes about " + duration + " to arrive there." 
        message = self.create_message(text=route_info)
        return self.respond(message=message, action="next")
        