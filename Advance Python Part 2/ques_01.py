#Create two virtual environments, install few packages in the first one. How do you create a similar environment in the 
# second one?

# pip install virtualenv
# virtualenv env1
# env1\Scripts\activate
# pip install pandas
# pip install pyjokes
# pip freeze > requirements.txt
#deactivate
# virtualenv env2
# env2\Scripts\activate
# pip install -r requirements.txt
# pip freeze