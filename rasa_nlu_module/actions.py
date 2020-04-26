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
        return "balance_form"

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

        product_type = tracker.get_slot('product_type')
        product = tracker.get_slot('product')

        dispatcher.utter_message(text="SUCCESS {} {}.".format(product_type, product))

        return []