# SlackBotReminder

.xlsx Scrapper connected to SlackBotApp.


<!-- ABOUT THE PROJECT -->

## About The Project

Hello! This project was made on my mentor demand. It scraps xlsx file and sends messages to students on Slack platform. 

### Functions

There is a special sheet format projected by my mentor. A student is able to buy month subscription which contains 4
meetings. All meetings are saved by mentor in the xlsx file. Every student has a slack account on workspace. This script will
be running every day and will check if the fourth meeting took place. After that slackbot sends message to the user and to
the mentor

### Stack

* slackclient==2.9.3
* SQLAlchemy==1.4.23
* SQLAlchemy-Utils==0.37.8
* openpyxl~=3.0.8

<!-- How to install -->
If you are using bash based system just run the script. If not then install extra libraries from requirements.txt.
Open your terminal in project folder and type:
* pip
  ```sh
  pip install -r requirements.txt
  ```

### Slack:

First you need to have slack workspace and bot app connected to your space. Documentation https://api.slack.com/

After creating an app on Slack, add environment variable BOT_TOKEN to your os.

### Bot scopes:

## How it works:


![obraz](https://user-images.githubusercontent.com/79137973/135668629-ce454dfb-19e9-473a-bb80-8fe674694a02.png)

This is how a sheet format looks like. The first row is always 7 and column is 5. The next fourth meeting is always 4 columns
ahead. The program iterates and checks where the last meeting was. For every fourth meeting, we need to check if there is one
before( to avoid mistakes) and one after(to check if there is no new subscription) and check current date also to avoid
mistakes with filling future dates. 

If the program has found a student with the last fourth meeting, it checks what month in a row it is.
After that program needs to find the student in the database and compares the month in the database or creates new record.
If the month in the database is other than in the sheet, the program sends messages to slack members and to the mentor.
Adding a student to the database is to avoid sending a message to student every day. There is also synchronization with googlesheets.

Bot message:
![obraz](https://user-images.githubusercontent.com/79137973/135146115-203af86e-3795-4db0-a07c-c94561b4dc24.png)


Now the mentor has autoreminder for his business . 

Enjoy!








<!-- CONTACT -->

## Contact

Sebastian Szymański - sebastian.szymanski.t5@gmail.com

