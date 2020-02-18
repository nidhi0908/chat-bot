## Generated Story 5575656197305734
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "anurag@gasf.com"}
    - slot{"email": "anurag@gasf.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

