import streamlit as st
from graphviz import Digraph

# Function to generate the dialogue flow graph
def create_dialogue_flow():
    # Create a directed graph for the dialogue flow..
    Dialogue_flow = Digraph("Dialogue Flow with NLU Examples", format="png", engine="dot")

     # Define bot and user nodes with different shape and color for the bot and user 
    bot_style = {'shape': 'rectangle', 'style': 'filled', 'color': 'lightblue'}
    user_style = {'shape': 'ellipse', 'style': 'filled', 'color': 'green'}

    # Define nodes
    Dialogue_flow.node("start", "User: Hi (User Greets Bot (Intent: greet))" , **user_style )
    Dialogue_flow.node("utter_greet", "Bot: 'Hello! I'm here to help predict housing prices. Let's get started.'" , **bot_style)
    Dialogue_flow.node("ask_city", "Bot: 'In which city is the house located?'" , **bot_style)
    Dialogue_flow.node("provide_city", "User: 'The city is Miami.'" , **user_style)
    Dialogue_flow.node("ask_beds", "Bot: 'How many bedrooms does the house have?'", **bot_style)
    Dialogue_flow.node("provide_beds", "User: 'It has 3 bedrooms.'" , **user_style)
    Dialogue_flow.node("ask_baths", "Bot: 'How many bathrooms does the house have?'" , **bot_style)
    Dialogue_flow.node("provide_baths", "User: 'There are 2 bathrooms.'" , **user_style )
    Dialogue_flow.node("ask_living_space", "Bot: 'What is the living space area in square feet?'" , **bot_style)
    Dialogue_flow.node("provide_living_space", "User: 'The living space is 1500 square feet.'" , **user_style )
    Dialogue_flow.node("ask_zip_density", "Bot: 'What is the population density of the zip code?'" , **bot_style)
    Dialogue_flow.node("provide_zip_density", "User: 'The population density is 5000.'" , **user_style )
    Dialogue_flow.node("ask_income", "Bot: 'What is the median household income in that area?'" , **bot_style)
    Dialogue_flow.node("provide_income", "User: 'The median income is 100000.'" , **user_style )
    Dialogue_flow.node("action_predict", "Bot: Triggers Prediction Action (for both models) " "\nLinear Regression Prediction: $144,682.81"  "\n Random Forest Prediction: $1,465,460.58" , **bot_style)
    Dialogue_flow.node("utter_goodbye", "Bot: 'Goodbye! Have a great day.'" , **bot_style)
    Dialogue_flow.node("end", "End: User Ends Interaction (Intent: goodbye)" , **user_style)

    # Define edges to show the updated flow
    Dialogue_flow.edges([
        ("start", "utter_greet"),
        ("utter_greet", "ask_city"),
        ("ask_city", "provide_city"),
        ("provide_city", "ask_beds"),
        ("ask_beds", "provide_beds"),
        ("provide_beds", "ask_baths"),
        ("ask_baths", "provide_baths"),
        ("provide_baths", "ask_living_space"),
        ("ask_living_space", "provide_living_space"),
        ("provide_living_space", "ask_zip_density"),
        ("ask_zip_density", "provide_zip_density"),
        ("provide_zip_density", "ask_income"),
        ("ask_income", "provide_income"),
        ("provide_income", "action_predict"),
        ("action_predict", "utter_goodbye"),
        ("utter_goodbye", "end")
    ])

    return Dialogue_flow

# Streamlit title writup
st.title("Dialogue Flow Of the ChatBot")
st.write("This Page visualizes the dialogue flow for the chatbot.")

# Generate the dialogue flow graph
dialogue_flow = create_dialogue_flow()

# To Render the graph and display it in Streamlit
st.graphviz_chart(dialogue_flow.source)
