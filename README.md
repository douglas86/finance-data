## [Introduction](#table-of-content)

This is the 3rd project for Code Institute.

- This is a simple terminal emulator to talk to Google Spreadsheets
- This emulator will be used to update the sheet for day-to-day expenses of my financials
- It will often use the date of the server or computer that it is running on the know were to place the data

---

# Table of Content

- [Introduction](#introduction)
- [Project setup](#project-setup)
  - [Setting up this project locally](#setting-up-this-project-locally)
- [Planning](#planning)
  - [Technology Used](#technology-used)
  - [Flow Chart Diagram](#flow-chart-diagram)
- [User Stories and features](#user-stories-and-features)
  - [User Stories](#user-stories)
  - [Features](#features)
- [Plans for the future of this project](#plans-for-the-future-of-this-project)
  - [Add a total tab](#add-a-total-tab)
  - [Debit order calculations](#debit-orders-calculations)

---

## [Project setup](#table-of-content)

### Setting up this project locally

#### Setting up python on your local machine
- If you are a Linux user such as myself
- I used Python 3.12.0 for this project as seen in the runtime.txt file
- If you want to install Python 3.12.0 for this project on Linux, follow this [link](https://www.howtogeek.com/install-latest-python-version-on-ubuntu/)
- Method 1 should work
- If you are a window user, follow this [link](https://www.python.org/downloads/release/python-3120/)
- As I am a Linux user, I will show you how I did it on a Linux machine
- In the home directory on your system, there should be a hidden file called .bashrc
- This file is normally used to load certain commands when the terminal starts
- Set an alias in the .bashrc file for running python files
- alias py='python3.12'
- Now whenever you need to run a python file with python version 3.12
- Type the word py followed by a command

#### git cloning this project locally
- if using ssh, run the following command
- git clone git@github.com:douglas86/finance-data.git
- if using http, run the following command
- git clone https://github.com/douglas86/finance-data.git
- now that this program is local, you can run the following commands
- py run.py

## Setting up this project on Heroku
- create a file called runtime.txt, this tells heroku what version of python you want to use
- Head on over to heroku.com or just type heroku into Google it should be the first one that pops up
- Login to heroku
- on the heroku dashboard, click the button that says new then click new app
- give your app a name bear in mind that names have to be unique across the entire heroku organisation
- choose a region
- once the app has been created, go to the settings tab to add the environment variables
- in the config vars section, click on the button that says reveal config vars
- add CREDS as the key and all the code in the json file as the value
- add the following buildpacks for your app: heroku/python, heroku/nodejs
- make sure that the buildpacks are in the correct order with python being first
- Go to the Deploy tab at the top
- Under deployment method connect your GitHub repo
- once you are successfully connected
- scroll down until you get manual deploy as we want to see how the app looks
- choose a branch to deploy normally I choose the main branch then click deploy
- wait a few minutes for it to finish, once it has finished and build successfully, then click view
- with any luck it should be up and running on heroku

---

## [Planning](#table-of-content)

### [Technology Used](#table-of-content)
- I used Python version 3.12.0 for this project
- Intellij IDE for development
- Heroku for deployment
- google developer console for getting the correct credentials for communicating with Google servers
- gspread pip package for communicating with my spreadsheet
- libreoffice draw for designing the flow chart diagram

### [Flow Chart Diagram](#table-of-content)

Flow chart can be seen here as a [PDF](assets/pdf_documents/Finance.pdf) document

---

## [User Stories and Features](#table-of-content)

### [User Stories](#table-of-content)

### [Features](#table-of-content)

---

## [Plans for the future of this project](#table-of-content)

### [Add a total tab](#table-of-content)

- I am wanting to add a total tab at the end of december
- This total tab will be used to automatically calculate all the totals in withdrawals and deposit

### [Debit orders calculations](#table-of-content)

- When the spreadsheet is created initially from the template spreadsheet
- It creates a copy updating all debit orders at the start of the year
- What I would like to do as a future update is when the debit order stops at a certain time that year
- Say march, then in april that debit order is deleted, the template gets updated and re-ordered and updated again 
  in april month

---

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
