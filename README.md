# Entaler
A web project, assignment from University

Assignement:
########################################
Deliverable 2
To be presented during the project class on 17 April for the group of Computer Science and on 19 April for the Electronics group.

The OS company wants you to create a CherryPy website in which you will describe the company, present the structure of the company and its employees, the software solutions which it offers and add a contact form. Identify the classes, implement them, store them inside arrays and parse the known data in order to display it.





Deliverable 3
To be presented during the project class on 15 May for the group of Computer Science and on 17 May for the Electronics group.

The OS company wants you to include a section on the website where the user can ask questions when dealing with problems which using the company's provided technologies. The company's representatives will answer and post the solutions on the website. Meanwhile, the company's general manager asks you to secure the personal information regarding the employees. Write in a file about the way the encryption and decryption is done and demonstrate how it has been coded. Hurry! The customers are calling and asking about online service!
########################################

The framwork chosen is Django insteand of CherryPy



How to run the project.
After unzipping, use terminal and go to the directory.

Install virtualenv, create a virtual environment and activate it. For example, on Ubuntu:
		
	sudo apt-get install python3-pip for 

Create a virtualenv:
	virtualenv venv .

Activate it:
    source bin/activate

Install requirements:
	pip install -r requirements/local.txt

Make local migrations for the DataBase:
	python3 src/manage.py makemigrations

Migrate:
	python3 src/manage.py migrate

Run server on default port:
	python3 src/manage.py runserver

Access localhost on browser.

Enjoy my homework.


