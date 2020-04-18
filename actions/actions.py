from typing import Any, Text, Dict, List
import logging

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
logger = logging.getLogger(__name__)

class ActionFaqDistancing(Action):

    def name(self) -> Text:
        return "action_faq_distancing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      intent = tracker.latest_message["intent"].get("name")

      logger.debug("Detected FAQ intent: {}".format(intent))

      if intent in ["faq_distancing"]:
        dispatcher.utter_message(template=f"utter_{intent}")
      return []