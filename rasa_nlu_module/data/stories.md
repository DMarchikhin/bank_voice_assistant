<!-- SEARCH + INFORM  -->
<!-- DEBT CARD -->

## happy path + greet
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path + greet + thx
* greet
  - utter_greet
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* thanks
  - utter_goodbye

## happy path
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path + thx
* balance_search
  - utter_ask_product
* balance_inform{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* thanks
  - utter_goodbye

<!-- DIRECT SEARCH + INFORM  -->
<!-- CREDIT CARD -->

## happy path + greet
* greet
  - utter_greet
* balance_direct_search{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path + greet + thx
* greet
  - utter_greet
* balance_direct_search{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* thanks
  - utter_goodbye

## happy path
* balance_direct_search{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* goodbye
  - utter_goodbye

## happy path + thx
* balance_direct_search{"product":"card", "product_type":"debt"}
  - balance_form_2
  - form{"name": "balance_form_2"}
  - form{"name": null}
* thanks
  - utter_goodbye

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