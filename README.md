 Ajayi Ikponmwosa 22301241

 House Price Prediction app and chatbot

https://mygit.th-deg.de/ia28241/my-first-project

https://mygit.th-deg.de/ia28241/my-first-project/-/wikis/home
                      
# Project Description
This project is an app and chatbot that helps its used to make prediction of the housing prices accross 188 cities in the US. 

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
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.



## Support
for support contact : ikponmwosa.ajayi@stud.th-deg.de


