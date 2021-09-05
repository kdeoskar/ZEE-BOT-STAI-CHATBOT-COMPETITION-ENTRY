# ZEE-BOT-STAI-CHATBOT-COMPETITION-ENTRY

This is a web based chatbot featuring voice commands 
To run the bot, you need to install **Rasa 2.0** in a **virtual environment**

# STEP-1
- Activate virtual env in a command prompt 
- Enter the following code for connecting the bot:
     ### > rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --cors "*"
     
# STEP-2
- Alongside run another command prompt (venv should be activated)
- Enter the following code:  
     ### > rasa run actions
     
# STEP-3
- Double click on the HTML file named "home.html" to run the website locally.
