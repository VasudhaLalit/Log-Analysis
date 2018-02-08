# Project - Log Analysis

## Introduction
This project is for the log analysis of the news database.

## Installation
The project uses two files and need python3 to run.
1. loganalysis.py
2. loganalysisdb.py

## Prerequisites
1. Make sure you have python3 installed on your machine.

2. Run below command to install psycopg2 module
    pip install psycopg2

3. Please download the vagrant/virtual machine from below url and follow the 
instructions to install.

    https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0

4. Download the "news" data from below link.
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

    To load the data cd into vagrant folder and use below command to load data into 'news' in PSQL.

    psql -d news -f newsdata.sql 
    
5. Create below views in "news" database.

    a. TopReads View
        CREATE VIEW TOPREADS AS
         SELECT articles.title,
            count(log.path) AS views
        FROM articles
        JOIN log ON log.path = ('/article/'::text || articles.slug)
        WHERE log.status = '200 OK'::text
        GROUP BY articles.title
        ORDER BY (count(log.path)) DESC;

    b. Authart view
        CREATE VIEW AUTHART AS
        SELECT authors.name,
            articles.title
        FROM authors
        JOIN articles ON authors.id = articles.author;

7. Start vagrant machine and CD into  the project folder.  Run below command to execute the loganalysis file.

python3 loganalysis.py

## Author
#_**Vasudha Lalit**_

## References
1. Udacity
2. http://pep8online.com