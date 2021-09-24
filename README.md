# SlackBotReminder

Xlsx. Scrapper connected to SlackBotApp.


<!-- ABOUT THE PROJECT -->

## About The Project

Hello! This project was made on my mentor demand. It scraps xlsx file and sends messages to students on Slack platform.

### Functions

There is special sheet format projected by my mentor. Student is able to buy month subscription which contains 4
meetings. All meetings are saved by mentor in xlsx file. Every student has slack account on workspace. This script will
be running every day and will check if fourth meeting took place. After that slackbot sends message to the user and to
the mentor

### Stack

* slackclient==2.9.3
* SQLAlchemy==1.4.23
* SQLAlchemy-Utils==0.37.8
* openpyxl~=3.0.8

<!-- How to install -->

## Settings:

### Slack:

First you need to have slack workspace and bot app connected to your space. Documentation https://api.slack.com/

After creating an app on Slack, add environment variable BOT_TOKEN to your os.

### Bot scopes:

## How it works:

This is how sheet format looks like. First row is always 7 and column is 5. Next fourth meeting is always 4 columns
ahead. Program iterates and checks where was last meeting. For every fourth meeting, we need to check if there is one
before( to avoid mistakes) and one after(to check if there is no new subscription) and check current date also to avoid
mistakes with filling future dates.

If program has found a student with last fourth meeting, it checks what month in a row it is.
After that program need to find student in database and compare month in database or create new record.
If month in database is other than in sheet, program sends messages to slack members and to mentor.
Adding student to database is to avoid sending every day message to student.


Now mentor has autoreminder for his business .

Enjoy!








<!-- CONTACT -->

## Contact

Sebastian Szymański - sebastian.szymanski.t5@gmail.com

