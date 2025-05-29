# books_list_api 

Simple Flask App to demonstrate deployment to Azure web app cloud hosting

Steps
1. Sign in to the Azure portal at portal.azure.com (select free tier, need CC for identify verification)
1. Select Create a resource 
1. Search for Web App
1. Click the Create button
1. In Web app dialog, select
   -  Resource group: create a new one
   -  Name: unique name for app
   -  Operating system and runtime: python and linux
   -  Region: select or leave default
   -  App Service plan/Location: free tier
   -  Click the Create button to create the web app.
1. Once created, select Deployment Center and link Git repo 
1. Look at logs, may need to add requirements.txt (use pip freeze, probably only Flask and requests needed)
1. In build logs, in deployment center, if it succeeds the URL will be in deployment step
1. Make sure your app is called app.py
