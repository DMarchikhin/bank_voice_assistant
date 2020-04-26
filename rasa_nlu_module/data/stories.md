<!-- SEARCH + INFORM  -->
<!-- DEBT CARD -->

## happy path + greet
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form
  - form{"name": "balance_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path + greet + thx
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form
  - form{"name": "balance_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

## happy path
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form
  - form{"name": "balance_form"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path + thx
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form
  - form{"name": "balance_form"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- SEARCH + INFORM  -->
<!-- CREDIT CARD -->


<!-- SEARCH + DECLINE  -->

## balance decline path + bye
* balance_search
  - utter_ask_product
* decline
  - utter_decline
* goodbye
  - utter_goodbye

## balance decline path + thx
* balance_search
  - utter_ask_product
* decline
  - utter_decline
* thanks
  - utter_goodbye

## balance decline path + greet + bye
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* decline
  - utter_decline
* goodbye
  - utter_goodbye

## balance decline path + greet + thx
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* decline
  - utter_decline
* thanks
  - utter_goodbye

<!-- SIMPLE STORIES  -->

## story thx
* thanks
  - utter_goodbye

## story bye
* goodbye
  - utter_goodbye


<!-- ## happy path
* greet
  - utter_greet
* balance_inform{"product": "card"}
  - balance_form
  - form{"product": "card"}
  - form{"product": null}
* balance_inform{"product_type": "debt"}
  - action_balance
  - form{"product": "card"}
  - form{"product": null} -->

<!-- ## happy path 2
* greet
  - utter_greet
* balance_search{"product":"card", "product_name":"вайт"}
  - balance_form
  - form{"product": "card"}
  - form{"product": null}
* balance_inform{"product_type": "debt"}
  - action_balance
  - form{"product": "card"}
  - form{"product": null}

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
  - utter_goodbye -->

<!-- ## balance + product short + greet
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"карта", "product_type":"дебетовая", "product_name":"вайт"}
  - action_balance
  - slot{"product_amount": "234000 рублей"} -->

