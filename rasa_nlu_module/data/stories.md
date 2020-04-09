## balance happy path
* greet
  - utter_greet
* balance_search{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}
* thanks
  - utter_goodbye

## balance short happy path
* balance_search{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}

## balance short + bye happy path
* balance_search{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}
* goodbye
  - utter_goodbye

## balance short + thanks happy path
* balance_search{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}
* thanks
  - utter_goodbye

## balance short + greet happy path
* greet
  - utter_greet
* balance_search{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}

## balance + product
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}
* thanks
  - utter_goodbye

## balance + product short
* balance_search
  - utter_ask_product
* balance_inform{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}

## balance + product short + bye
* balance_search
  - utter_ask_product
* balance_inform{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}
* goodbye
  - utter_goodbye

## balance + product short + thanks
* balance_search
  - utter_ask_product
* balance_inform{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"}
* thanks
  - utter_goodbye

<!-- ## balance + product short + greet
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"} -->

