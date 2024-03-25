# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Dict, List, Text
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk import Action, Tracker


# class ActionDefaultFallback(Action):
#     def name(self):
#         return "action_default_fallback"

#     def run(self, dispatcher, tracker, domain):
#         # Your fallback logic here
#         dispatcher.utter_message(
#             text="I'm sorry, I didn't understand that. Can you rephrase? This is a custom action!")
#         return []


class ActionCustomFallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher, tracker, domain):
        # Your custom logic here, e.g.,
        dispatcher.utter_message(template="utter_default")
        # You might log the unrecognized input for analysis

        return []  # No events
# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
