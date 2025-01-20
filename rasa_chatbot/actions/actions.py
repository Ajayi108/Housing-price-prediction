import os
import pandas as pd
import joblib
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Define the full paths to the model files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
lr_model_path = os.path.join(BASE_DIR, "../../linear_regression_model.pkl")
rf_model_path = os.path.join(BASE_DIR, "../../random_forest_model.pkl")

# Load models
try:
    lr_model = joblib.load(lr_model_path)
    rf_model = joblib.load(rf_model_path)
except FileNotFoundError as e:
    lr_model = None
    rf_model = None
    print(f"Model loading error: {e}")

class ActionPredictPrice(Action):
    def name(self) -> Text:
        return "action_predict_price"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Extract slot values
        city = tracker.get_slot("city")
        beds = tracker.get_slot("beds")
        baths = tracker.get_slot("baths")
        living_space = tracker.get_slot("living_space")
        median_income = tracker.get_slot("median_income")

        # Prepare input data (skip missing values)
        input_data = {
            "City": city,
            "Beds": beds,
            "Baths": baths,
            "Living Space": living_space,
            "Median Household Income": median_income,
        }
        input_data = {k: v for k, v in input_data.items() if v is not None}  # Remove None values

        # Check if essential data is missing
        if not input_data:
            dispatcher.utter_message(
                text="I don't have enough data to make a prediction. Please provide more details about the house."
            )
            return []

        input_df = pd.DataFrame([input_data])

        # Perform predictions if models are loaded
        if lr_model and rf_model:
            try:
                lr_prediction = lr_model.predict(input_df)[0]
                rf_prediction = rf_model.predict(input_df)[0]
                dispatcher.utter_message(
                    text=(
                        f"Predictions:\n"
                        f"Linear Regression: ${lr_prediction:,.2f}\n"
                        f"Random Forest: ${rf_prediction:,.2f}"
                    )
                )
            except Exception as e:
                dispatcher.utter_message(
                    text=f"An error occurred during prediction: {str(e)}"
                )
        else:
            dispatcher.utter_message(
                text="Prediction models are not available. Please contact support."
            )

        return []
