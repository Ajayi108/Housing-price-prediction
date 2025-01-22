from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import pandas as pd
import joblib
import os

class ActionPredict(Action):
    def name(self) -> str:
        return "action_predict"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Fetch slot values
        city = tracker.get_slot("city")
        beds = tracker.get_slot("beds")
        baths = tracker.get_slot("baths")
        living_space = tracker.get_slot("living_space")
        zip_code_density = tracker.get_slot("zip_code_density")
        median_household_income = tracker.get_slot("median_household_income")

        # Define base directory and model paths
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory of the current Python file
        lr_model_path = os.path.join(base_dir, "../../linear_regression_model.pkl")  # Adjust relative path
        rf_model_path = os.path.join(base_dir, "../../random_forest_model.pkl")      # Adjust relative path

        # Load models
        lr_model = joblib.load(lr_model_path)
        rf_model = joblib.load(rf_model_path)

        # Prepare input data
        input_data = pd.DataFrame([{
            "City": city,
            "Beds": float(beds),
            "Baths": float(baths),
            "Living Space": float(living_space),
            "Zip Code Density": float(zip_code_density),
            "Median Household Income": float(median_household_income)
        }])

        # Make predictions
        try:
            lr_prediction = lr_model.predict(input_data)[0]
            rf_prediction = rf_model.predict(input_data)[0]
            dispatcher.utter_message(
                text=f"Predicted house price:\n- Linear Regression: ${lr_prediction:,.2f}\n- Random Forest: ${rf_prediction:,.2f}"
            )
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred during prediction: {e}")
        
        return [AllSlotsReset()]
