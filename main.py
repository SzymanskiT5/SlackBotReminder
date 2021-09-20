from bot import SlackBot
from database import Database

db = Database()


def main():
    from excel import SheetScraper
    bot = SlackBot()

    db.config_db()
    loc = "/home/sebastian/Pulpit/Students Timesheet.xlsx"
    scraper = SheetScraper(loc)
    scraper.iterate_rows()
    bot.get_users_list()










if __name__ == "__main__":
    main()