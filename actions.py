from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
# importing the EmailMessage class
from email.message import EmailMessage
# Importing the smtplib libaray to send email
import smtplib
import zomatopy
import json
#from concurrent.futures import ThreadPoolExecutor
mailContent	 = []

config = { "user_key":"Your key"}

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		zomato = zomatopy.initialize_app(config)

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = int(tracker.get_slot('budget'))
		
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		
		cuisines_dict={'mexican':73,'american':1,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		
		#The below section is fing the price range for user.
		dispatcher.utter_message("\n Price: "+str(price))
		rangeMin = 0
		rangeMax = 10000
		if price == 1:
			rangeMax = 299
		elif price == 2:
			rangeMin = 300
			rangeMax = 700
		elif price == 3:
			rangeMin = 701
		elif price <= 300:
			rangeMax = 300
		elif price > 300 and price <=700:
			rangeMin = 301
			rangeMax = 700
		else:
			# default budget 
			rangeMin = 700
			rangeMax = 7500

		dispatcher.utter_message("\n Min: "+str(rangeMin) + " rangeMax: "+str(rangeMax))

		i = 1
		j=1
		response=""
		responseToDisplay=""
		global result_of_last_query
		result_of_last_query = ""
		index = 0
		count = 0
		# As each Zomato call returns only 20 resturants, we are running the loop multiple times, this will run until we have found out our 10 resturants that fit in the user's budget.
		for offsetCounter in (0,20,40,80,100,120,140):	
			try:			
				if i>=10:
					break
				#Zomato api is called to search for the resturants, order by rating has been handled in the rest call.
				results = zomato.restaurant_search(offsetCounter,"", lat, lon, str(cuisines_dict.get(cuisine.lower())), 20)
				d = json.loads(results)# print(len(d))
				if d['results_found'] == 0:
						response= "no results"
						responseToDisplay="no results"
						break
				else:
					for restaurant in d['restaurants']:
						if (int(restaurant['restaurant']['average_cost_for_two']) >= rangeMin) and(int(restaurant['restaurant']['average_cost_for_two']) <= rangeMax) and i <= 10:
							response = response + str(i) + ". " + restaurant['restaurant']['name'] + ", Avg. Rating: " + str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"/5" + ", Average Cost: " + str(restaurant['restaurant']['average_cost_for_two']) + " Address: " + restaurant['restaurant']['location']['address']+"\n"
							i += 1
						if (int(restaurant['restaurant']['average_cost_for_two']) >= rangeMin) and(int(restaurant['restaurant']['average_cost_for_two']) <= rangeMax) and j <= 5:
							responseToDisplay = responseToDisplay + str(j) + ". " + restaurant['restaurant']['name'] + ", Avg. Rating: " + str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"/5" + ", Average Cost: " + str(restaurant['restaurant']['average_cost_for_two']) + " Address: " + restaurant['restaurant']['location']['address']+"\n"
							j += 1
		
			except requests.exceptions.RequestException as e:
				s = getattr(e,'message', str(e))
				logger.info(s)
				message = 'Looks like something is wrong with me, please try again.'
				dispatcher.utter_message(message)
		global mailContent
		mailContent = response

		dispatcher.utter_message("--------------------\n" + responseToDisplay + "--------------------")
		return [SlotSet('location',loc)]

		
tier1_tier2 = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune","Agra","Ajmer","Aligarh","Amravati","Amritsar",
"Asansol","Aurangabad","Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar","Bikaner","Bilaspur","Bokaro Steel City","Chandigarh",
"Coimbatore","Cuttack","Dehradun","Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad","Gorakhpur","Gulbarga",
"Guntur","Gurgaon","Guwahati","Gwalior","Hamirpur","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur",
"Jhansi","Jodhpur","Kannur","Kanpur","Kakinada","Kochi","Kolhapur","Kollam","Kozhikode","Kurnool","Lucknow","Ludhiana","Madurai","Malappuram",
"Mathura","Goa","Mangalore","Meerut","Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Patna","Pondicherry","Purulia","Prayagraj",
"Raipur","Rajkot","Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri","Shimla","Solapur","Srinagar","Surat","Thiruvananthapuram","Thrissur",
"Tiruchirappalli","Tiruppur","Ujjain","Vellore","Vadodara","Varanasi","Bijapur","Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

operating_cities = [x.lower() for x in tier1_tier2]

# To Check if the given location exists. using zomato api.if found then save it, else inform the foodie don't have service currently in the given location.
class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		# dispatcher.utter_message(city)

		if city.lower() in operating_cities:
			return [SlotSet('location_match',"one")]
		else:
			return [SlotSet('location_match',"zero")]

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global mailContent
        
        # Construct the email 'subject' and the contents.
        mail_sub =  cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
                
        d_email_msg = "Hello Foodie: \nPlease find the searched resturants below: \n\n" + mailContent +"\n\nRegards,\nTeam Foodie"
        #d_email_msg = d_email_msg + d_email

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("email_address", "password")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = mail_sub
        msg['From'] = "From email address"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("** I have shared the details with your email id, hope I was helpful to you!! **")
        return []