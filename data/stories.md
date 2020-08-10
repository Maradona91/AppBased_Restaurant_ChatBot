## Happy path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email
    - utter_goodbye


## location specified
* greet
    - utter_greet
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "lucknow"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email
    - utter_goodbye

## complete path 2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email


## complete path 3
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* dont_send_email
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email

## complete path 5
* greet
    - utter_greet
* restaurant_search{"location": "palakkad"}
    - slot{"location": "palakkad"}
    - action_validate_location
    - slot{"location_match": "zero"}
    - utter_not_operating
    - utter_goodbye

## complete path 6
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* send_mail
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* action_search_restaurants{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* action_search_restaurants{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop
    
## happy_path
* restaurant_search{"location": "dandeli"}
    - slot{"location": "dandeli"}
    - action_validate_location
    - slot{"location_match": "zero"}
    - utter_not_operating
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "dharwad", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "dharwad"}
    - action_validate_location
    - slot{"location_match": "zero"}
    - utter_not_operating
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian", "location": "goa"}
    - slot{"cuisine": "italian"}
    - slot{"location": "goa"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - utter_ask_email
* dont_send_email{"dont_send_email": "no"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - utter_ask_email
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "banaglore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "banaglore"}
    - action_validate_location
    - slot{"location_match": "zero"}
    - utter_not_operating
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "lucknow"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "lucknow"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* restaurant_search{"budget": "1000"}
    - slot{"budget": "1000"}
    - action_search_restaurants
    - slot{"location": "lucknow"}
    - utter_ask_email
* dont_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "299"}
    - slot{"budget": "299"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email
* dont_send_email{"location": "no"}
    - slot{"location": "no"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_validate_location
    - slot{"location_match": "zero"}

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* Email_Not_Valid
    - utter_ask_email
* send_mail
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "ho@jjjj.cocodjjd"}
    - slot{"emailid": "ho@jjjj.cocodjjd"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "surat", "budget": "600"}
    - slot{"budget": "600"}
    - slot{"cuisine": "italian"}
    - slot{"location": "surat"}
    - action_validate_location
    - slot{"location_match": "one"}
    - action_search_restaurants
    - action_search_restaurants
    - slot{"location": "surat"}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* Email_Not_Valid{"emailid": "dsdfsdsfsf"}
    - slot{"emailid": "dsdfsdsfsf"}
    - utter_ask_emailid
* send_mail{"emailid": "richa.arya6@gmail.com"}
    - slot{"emailid": "richa.arya6@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Ahemdabad", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Ahemdabad"}
    - action_validate_location
    - slot{"location_match": "zero"}
    - utter_not_operating
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_validate_location
    - slot{"location_match": "one"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
* affirm
    - utter_ask_email
* affirm
    - utter_ask_emailid
* send_mail{"emailid": "adsasdasd"}
    - slot{"emailid": "adsasdasd"}
    - action_send_email
    - utter_ask_emailid
* send_mail{"emailid": "bansalanshuman@gmail.com"}
    - slot{"emailid": "bansalanshuman@gmail.com"}
    - action_send_email
