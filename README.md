History
------------
This is an updated version of the original membaman project seen at https://github.com/shearichard/membaman . 

The intention of this version is make the original project work on a more recent version of Django (3.2 initially) and Python 3.x.

In migrating the project some parts of it are now broken and so this is work in progress to bring this version back up to the standard of the previous version.

Introduction
------------
Membaman is a membership management system intended for Youth and Sports Groups.

Its intended scope includes :

 * Membership registration within Organisations and sub-organisations
 * Invoicing and tracking of payments for regular payments
 * Production of PDF's to support the invoicing process
 * Production of CSV downloads to allow data transfer out of Membaman to other systems
 * Ability to email members and members caregivers with both regular and ad-hoc emails

Membaman is implemented in Django 3.2 and uses a sqlite database as a data repository. To date it has only been tested in Python 2.9.x . 


Environment Variables
-------------------
Using `direnv` to set a ENV VAR for the SECRET_KEY value when we cd into membaman. Longer term need a better solution.

Running Instructions
-------------------
Pipenv is used to create the necessary `virtualenv`.

Start the server as follows :
```
python manage.py runserver  --settings=membaman.settings.local 0.0.0.0:8000
```

Version
--------
0.3.0
