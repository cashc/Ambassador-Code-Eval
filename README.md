# Ambassador-Code-Eval
Python Django backend REST API

`/` shows the browsable API.   
`/links` displays all the links in the DB with the option to create a new one.   
`/landing` has a shout out to Tim, the owner of the site.   
`/landing/?link=<title>` increments the title visited and shows an ad for that title.

### Technical spec

-	Back-end track: build a REST API and include a minimal front-end (e.g. a browsable API)

Your task is to build a REST API that can support the functionality described for the Link and Landing pages in the Functional spec. Please use [Django Rest Framework](http://www.django-rest-framework.org/) and host your project on [Heroku](https://dashboard.heroku.com). Your API should be able to:

-	Perform CRUD actions for Link pages
-	Track the number of visits to the Landing Page

You do not have to build a functional UI unless you want to show off your talents across the stack. We will test your API by using the Browsable API. You are encouraged to write tests to verify your own results.


## Resources
 - [PyCharm](https://www.jetbrains.com/help/pycharm/2016.3/creating-and-running-your-first-django-project.html)   
 - [Django-Rest-Framework](http://www.django-rest-framework.org/tutorial/quickstart/)   
 - [Simple Heroku deployment steps](https://www.dropbox.com/s/68sc3ihna7qdaiu/test.py?dl=0)   