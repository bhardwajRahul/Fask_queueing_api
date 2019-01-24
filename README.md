#Saavn Test Api
=============

Online API system using flask, flask-restful, sqlalchemy,

The project has been developed using Flask- A python Micro-web framework
and other additional packages describe below in Tech Stack Section.

Github link for the project - <https://github.com/bhardwajRahul/saavn_api>

Installation
------------

Before we begin, kindly install following on your system:-

-   [python3.x](http://www.python.org)
-   [Virtualenv](https://virtualenv.pypa.io/en/stable/)

How to Run the App?
-------------------

-   cd path/to/workspace
-   git clone <https://github.com/bhardwajRahul/saavn_api>
-   cd saavn_api
-   virtualenv -p ‘which python3’ venv
-   source venv/bin/activate
-   pip install -r requirements.txt
-   python3 worker.py (Seperate instance)
-   python3 run.py

Everything should be ready. In your browser open
<http://127.0.0.1:5000/>

Since Redis-Server is used for database optimisation (caching)
After running the app, type in following in terminal to establish
redis-connection

- redis-server

REST Endpoints
--------------

There are two major objects in the app:-

-   Implementation of query mechanism in Rest APIs for analytics
-   APIs to upload file for custom analytics

The endpoints and the corresponding REST operations are defined as
follows:-

Endpoints
--------------------

 -   [http://127.0.0.1:5000/api/users?platform=<platform>]

     Returns the filtered on the basis of platform and response are cached as well
    - Method: `GET`
    - URL path: `/api/users?platform=android`
    - Response:

    Header: `HTTP 200`
    Body:
      ```
      {
        "data": {
        "percentage_share": 66.43,
        "platform_users": 5933,
        "unique_users": 5932
        }
      }
      ```
    or

    Header: `HTTP <HTTP_CODE>`
    Body:
      ```json
      {
          "error": "ERROR_DESCRIPTION"
      }
      ```

 -   [http://127.0.0.1:5000/api/upload]
    
    Returns the task_id generated on uploading of file to the task queue
    - Method: `POST`
    - URL path: `/api/upload`
    - Request body:

    ```
    {
        Sample File for Upload
    }
    ```

  - Response:

    Header: `HTTP 200`
    Body:
      ```
      {
          {"data":{"task_id":"e8d310de-dc05-4612-a897-002d0b1c7fe6"},"status":"success"}

      }
      ```
    or

    Header: `HTTP <HTTP_CODE>`
    Body:
      ```json
      {
          "error": "ERROR_DESCRIPTION"
      }
      ```

 -   [http://127.0.0.1:5000/api/upload/<task_id>]
    
    Polling mechanism to check the status of Ingestion job
    Using unique ID of ingestion to get response for chosen ID
    - Method: `GET`
    - URL path: `/api/upload/e8d310de-dc05-4612-a897-002d0b1c7fe6`
    - Response:

    Header: `HTTP 200`
    Body:
      ```
    {
        "data": {
            "task_id": "e8d310de-dc05-4612-a897-002d0b1c7fe6",
            "task_result": true,
            "task_status": "finished"
        },
        "status": "success"
    }
      ```
    or

    Header: `HTTP <HTTP_CODE>`
    Body:
      ```json
      {
          "error": "ERROR_DESCRIPTION"
      }
      ```

Tech stack
----------

-   [Flask](http://flask.pocoo.org/) - Web Microframework for Python
-   [Flask-restful](https://flask-restful.readthedocs.io/en/latest/) -
    Extension for flask for quickly building REST APIs
-   [Flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) -
    An extension that handles SQLAlchemy database migrations for Flask
    applications using Alembic.
-   [Flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/) - This is an
    extension of flask that add supports for SQLAlchemy
-   [MySQL](https://www.mysql.com) - Database for the 
    project. It comes built in with python.
-   [RedisDB](https://redis.io/) - Key-Value based No-SQL DB to oprimize relational
    database by improving Read by caching data and queing data.
-    [Redis Queue](http://python-rq.org/) - RQ is a simple Python library for queueing jobs and processing them in the background with workers.
-   [Flask-Redis](https://github.com/underyx/flask-redis) - An flask extension of   [RedisPy](http://redis-py.readthedocs.io/en/latest/)
    to easliy used Redis with Python and Flask easily.

Development Thought process
---------------------------

-   Used Micro service Architecture for proper decoupling of service.
-   Test driven development is useful and leads to less errors in later
    stages of development.
-   Dependency injection helps a lot in Test driven development and also
    in making the project more modular and flexible. Though couldn’t use
    in the current project but would surely update the project using
    flask-injector.
-   Used RedisDB and Redis Queue which supported the whole architecture
    either its caching purpose or queueing and pooling the app.
-   Used Flask because it’s flexible and can be plugged with all the
    necessary modules on the go.

