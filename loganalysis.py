#!/usr/bin/env python3

from loganalysisdb import db_connect
from datetime import date


def get_popular_articles():

    print("\nWhat are the most popular three articles of all time? \n")
    query = """
          select title, count(path) as views
          from articles inner join log
          on log.path = '/article/'||articles.slug
          where log.status = '200 OK'
          group by title
          order by views desc
          limit 3;"""
    popular_articles = db_connect(query)

    for index, (title, views) in enumerate(popular_articles, 1):
        print("{}. {} - {} views".format(index, title, views))


def get_popular_authors():

    print("\n\nWho are the most popular article authors of all time? \n")
    query = """
            select name, sum (views) as views
            from topreads inner join authart
            on authart.title = topreads.title
            group by name
            order by views desc"""

    popular_authors = db_connect(query)

    for index, (author, views) in enumerate(popular_authors, 1):
        print("{}. {} - {} views".format(index, author, views))


def get_error_requests():

    print("\n\nOn which days did more than 1% of requests lead to errors?  \n")
    query = """ select * from
            (select totals.date,
                ((errors.days * 100.00) /
                totals.days) as error_pct
                from (select date(time) as date,
                count(1) as days from log
                group by date) as totals
            join (select date(time) as date,
                count(1) as days
                from log
            where status != '200 OK'
                group by date) as errors
            on totals.date = errors.date) as pct
            where pct.error_pct >=1"""
    error_pct = db_connect(query)
    for (date, err_pct) in error_pct:
        print("{} - {} %\n\n".format(date.strftime("%B %d, %Y"),
              round(err_pct, 2)))


if __name__ == "__main__":
    get_popular_articles()
    get_popular_authors()
    get_error_requests()
