# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


class ActionBalance(Action):

    def name(self) -> Text:
        return "action_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product = tracker.get_slot("product")
        product_type = tracker.get_slot("product_type")

        product_amount = "234500 рублей"

        dispatcher.utter_message(text="Баланс {} {} {}".format(product_type, product, product_amount))

        return [SlotSet("product_amount", product_amount)]


class BalanceForm(FormAction):
    # Документация по формам -> https://rasa.com/docs/rasa/core/forms/

    def name(self) -> Text:
        return "balance_form_2"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["product", "product_type"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "product_type": self.from_entity(entity="product_type", intent=["balance_inform", "balance_search"]),
            "product": self.from_entity(entity="product", intent=["balance_inform", "balance_search"])
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        slot_product_type = tracker.get_slot('product_type')
        slot_product = tracker.get_slot('product')

        URL = "http://localhost:3000/products/"

        response = requests.get(url = URL) 
        data = response.json() 

        if data is not None and len(data) > 0:
            for product in data:
                if product['product'] == slot_product and product['product_type'] == slot_product_type:
                    product_str = ""
                    product_type_str = ""

                    if product['product'] == "card":
                        product_str = "карте"
                        if product['product_type'] == "debt":
                            product_type_str = "дебетовой"
                        elif product['product_type'] == "credit":
                            product_type_str = "кредитной"
                    else:
                        product_str = "счёте"

                    dispatcher.utter_message(text="Баланс на {} {} {} состовляет {} рублей."
                        .format(product_type_str, product_str, product['product_name'], product['balance'])
                    )
                    return []
            dispatcher.utter_message(text="Не могу найти продукт: {} {}. Можете повторить запрос?"
                .format(slot_product_type, slot_product)
            )
            return []
        else:
            dispatcher.utter_message(text="Сервер сейчас не работает. Попробуйте позже.")
            return []