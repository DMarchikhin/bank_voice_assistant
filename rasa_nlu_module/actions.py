# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionBalance(Action):

    def name(self) -> Text:
        return "action_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product = tracker.get_slot("product")
        product_type = tracker.get_slot("product_type")
        product_name = tracker.get_slot("product_name")

        product_amount = "234500 рублей"

        dispatcher.utter_message(text="Баланс {} {} {} {}".format(product_type, product, product_name, product_amount))

        return [SlotSet("product_amount", product_amount)]
