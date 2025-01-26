 Ajayi Ikponmwosa 22301241

 House Price Prediction app and chatbot

 [Link to project](https://mygit.th-deg.de/ia28241/my-first-project)

 [Link to wiki](https://mygit.th-deg.de/ia28241/my-first-project/-/wikis/home)
                      
# Project Description
This project is an app and chatbot that helps its used to make visualize the data prediction of the housing prices accross 188 cities in the US. 

# Installation
Python 3.10.4 version was used for this project.


Use `pip install -r requirements.txt` in the terminal to install all dependensies in the reqirement.txt file needed to run this project.

```
pip install -r requirements.txt
```

Note, the following versions where used.

- rasa==3.6.21
- scikit-learn==1.1.3
- streamlit==1.41.1
- numpy==1.23.5
- graphviz==0.20.3
- matplotlib==3.5.3

# Data

The data set was gotten from kaggle. see link to data set below.

[Link to download data set](https://www.kaggle.com/datasets/jeremylarcher/american-house-prices-and-demographics-of-top-cities)

For the approach of removing outliers see link to wiki page: 
[Approach to remove Outliers](https://mygit.th-deg.de/ia28241/my-first-project/-/wikis/Outliers)

For the approach for adding fake data, see link to wiki:
[Fake data](https://mygit.th-deg.de/ia28241/my-first-project/-/wikis/Fake-data-)


# Basic usage

- First install all the the dependencies in the requirement.txt using `pip install -r requirements.txt`.

- Run `train_models.py` To get the pkl file of the model used for predictions. ie (to get linear_regression_model.pkl and random_forest_model.pkl)

- Run `AddFakeData.py` to add fake data to get the `American_Housing_Data_Augmented.csv` file.



create three terminals, two for rasa and one for streamlit.
- Navigate to the chatbot folder, ie. `cd .\rasa_chatbot\` on the two termnials for rasa.
```
cd .\rasa_chatbot\
```

- Run the commands `rasa train` on the terminal if the rasa model is unavailable.
```
rasa train
```

- on one terminal while in chatbot directory run the command `rasa run actions ` .
```
rasa run actions
```

- On the other terminal while in the chatbot directory, run The command `rasa run --enable-api` . wait till the rasa server is up and running.
```
rasa run --enable-api
```

- On the third terminal, while in the root directory, run the command `streamlit run home.py` to start streamlit page.
```
streamlit run home.py
```



## Visuals

to see a video of the app check  the [Video on wiki](https://mygit.th-deg.de/ia28241/my-first-project/-/wikis/home)


# Use cases

- predicting House price base on the user input.
-  To check area specific data.
- To explore the impact of different features on house prices
- To see market changes in prices.
- to quickly compare property prices.

see the use cases for each persona in the wiki page [Use cases](https://mygit.th-deg.de/ia28241/my-first-project/-/wikis/Use-cases-of-the-app)

# Request 

- The app is a multipage app implemented with streamlit.
- The data set is downloaded from kaggle.
- Two scikit learn models was used for training, Linear Reggression and random forest.
- 50 percent fake data is added to the data.
- Chat bot is implemented with rasa.
- Three user personas are described in the wiki, and a system persona.
- use cases are described in the wiki.
- dialogue is created using graphviz.
- All documentation and shown in the wiki. 




## Support
for support contact : ikponmwosa.ajayi@stud.th-deg.de


