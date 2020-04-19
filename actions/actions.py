from typing import Any, Text, Dict, List
import logging, json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)


class ActionFaqDistancing(Action):
    def name(self) -> Text:
        return "action_faq_distancing"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_distancing"]:
            text = """Social distancing is a public health practice that aims to prevent sick people 
            from coming in close contact with healthy people in order to reduce opportunities for disease transmission. 
            It can include large-scale measures like canceling group events or closing public spaces, as well as individual 
            decisions such as avoiding crowds."""
            message = {
                "type": "image",
                "payload": {
                    "title": "Social Distancing",
                    "src": "https://www.covidoumedicine.com/images/content/covid-19-curves.gif",
                },
            }
            dispatcher.utter_message(text=text, attachment=message)
        return []


class ActionFaqSpread(Action):
    def name(self) -> Text:
        return "action_faq_spread"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_spread"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "6 Steps to Prevent COVID-19",
                    "src": "https://www.youtube.com/embed/9Ay4u7OYOhA",
                },
            }
            dispatcher.utter_message(
                text="Take steps to lower your risk of getting sick with COVID-19. Here are some things you should do.",
                attachment=message,
            )
        return []


class ActionFaqSymptoms(Action):
    def name(self) -> Text:
        return "action_faq_symptoms"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_symptoms"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "COVID-19 Animation: What Happens If You Get Coronavirus?",
                    "src": "https://www.youtube.com/embed/5DGwOJXSxqg",
                },
            }
            dispatcher.utter_message(
                text="People with COVID-19 generally develop signs and symptoms, including mild respiratory symptoms and fever, on an average of 5-6 days after infection (mean incubation period 5-6 days, range 1-14 days). Most people infected with COVID-19 virus have mild disease and recover.",
                attachment=message,
            )
        return []


class ActionFaqStatus(Action):
    def name(self) -> Text:
        return "action_faq_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")

        logger.debug("Detected FAQ intent: {}".format(intent))

        if intent in ["faq_status"]:
            message = {
                "type": "video",
                "payload": {
                    "title": "[LIVE] Coronavirus Pandemic: Real Time Counter, World Map, News",
                    "src": "https://www.youtube.com/embed/NMre6IAAAiU",
                },
            }
            dispatcher.utter_message(attachment=message)
        return []
