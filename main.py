from slack.errors import SlackApiError
from bot import SlackBot
from database import Database

db = Database()


def main() -> None:
    from excel import SheetScraper
    from models import Student
    Student.__table__.create(bind=db.engine, checkfirst=True)
    bot = SlackBot()
    loc = "/home/sebastian/Pulpit/Students Timesheet.xlsx"
    scraper = SheetScraper(loc)
    scraper.iterate_rows()
    list_of_students = scraper.list_of_students

    if list_of_students:
        try:
            bot.get_users_list(list_of_students)
            bot.send_message()
            print("Messages sended!")
        except SlackApiError as e:
            print(e)
    else:
        print("Everything is up to date")


if __name__ == "__main__":
    main()
