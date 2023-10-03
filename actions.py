# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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
from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")

        return []

class ActionShowMenu(Action):
    def name(self) -> Text:
        return "action_show_menu"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_show_menu")

        return []

class ActionCategoryOptions(Action):
    def name(self) -> Text:
        return "action_category_options"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract the category name using entity recognition
        category_entity = next(tracker.get_latest_entity_values("category"), None)
        
        menu_options = {
            "Beverages": ["Coffee", "Tea", "Soft Drinks", "Smoothies"],
            "Pastries": ["Croissant", "Muffin", "Danish"],
            "Sandwiches": ["Club Sandwich", "Veggie Wrap", "Turkey Panini"],
            "Salads": ["Caesar Salad", "Greek Salad", "Cobb Salad"],
            "Desserts": ["Cheesecake", "Chocolate Brownie", "Fruit Tart"],
            "Smoothies": ["Berry Blast", "Mango Tango", "Green Energy"],
            "Specialty Drinks": ["Iced Latte", "Matcha Latte", "Chai Latte"]
        }
        
        if category_entity:
            category_name = category_entity.lower().capitalize()  # Format the category name
            options = menu_options.get(category_name, [])
            
            if not options:
                response = f"Sorry, {category_name} is not a valid category. Please choose a valid category."
            else:
                formatted_options = "\n  - ".join(options)
                response = f"Great choice! Here are the options under {category_name}:\n  - {formatted_options}\nPlease let me know your selection and the quantity."
        else:
            response = "I'm sorry, I didn't understand the category. Please provide a valid category."

        dispatcher.utter_message(text=response)
        return []


class ActionSaveOrder(Action):
    def name(self) -> Text:
        return "action_save_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order_items = tracker.get_latest_entity_values("menu_item")

        if order_items:
            formatted_ordered_items = ", ".join(order_items)
            response = f"Got it! Your order so far: {formatted_ordered_items}. Would you like to add more items to your order?"
        else:
            response = "I'm sorry, I couldn't understand your order. Please provide a valid item and quantity."

        dispatcher.utter_message(text=response)

        return []






class ActionTakeaway(Action):
    def name(self) -> Text:
        return "action_takeaway"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_takeaway")

        return []



class ActionFAQOpeningHours(Action):
    def name(self) -> Text:
        return "action_faq_opening_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Our opening hours are from 8 AM to 10 PM, Monday to Saturday. We're closed on Sundays.")
        return []

class ActionFAQReservation(Action):
    def name(self) -> Text:
        return "action_faq_reservation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Certainly! You can make a reservation by emailing us at cafesky@gmail.com.")
        return []

class ActionFAQPaymentMethods(Action):
    def name(self) -> Text:
        return "action_faq_payment_methods"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "We accept cash, credit cards, and mobile payment methods like Apple Pay and Google Pay. Payment can be made at the cashier section in the cafe."
        dispatcher.utter_message(text=response)
        return []

class ActionFAQAllergens(Action):
    def name(self) -> Text:
        return "action_faq_allergens"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = "We take allergies seriously. Our menu items are labeled with allergen information. Please let us know about your allergies, and our staff will assist you."
        dispatcher.utter_message(text=response)
        return []