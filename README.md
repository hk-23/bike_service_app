# Hudson Sparklers - Bike Service Station App
Hudson Sparklers is the name of the Bike Service Station and this **Django Webapp** is used for the customers to book the services provided by the company and has an Admin page for the owners of the company.

## Basic Requirements
- Python 3.6+
- Pip
- Virtualenv(optional)

## Addition Requirements
- Django 3.0+
- Refer the requirements.txt file for all the requirement packages

## Getting Started
Once you have done installing Python and updated the path variables follow these instruction bellow
- Clone this repo:https://github.com/hk-23/bike_service_app.git
- cd into **bike_service_app** folder and this becomes your root for this project
- Now install the required packages (i.e. django..) using pip
```sh
$ cd bike_service_app
$ pip install -r requirements.txt
```
- Now run the following command to start the webapp
```sh
$ python manage.py runserver
```
- If this executes without any errors then now you can open the chrome or your favourite browser and go to: https://localhost:8000 or http://127.0.0.1:8000
- You will be able to see the home page now.

## User Types
This projects is a website for the customers and owners of Bike Service station and it has three user types in the application level:
- Admin
- Staff
- Customers
### Admin
The Admin is the Owner of the Website and he has All Previleges in the Admin Panel. The user_type: Admin can 
- Create/Edit/Delete a **Service**
- Create **Staff Account** user
- View All Details about the Staff and Customer
- Change the Status of a Booking made by the Customer to: 
    - Ready For Delivery
    - Delivered
    - Canceled

### Staff
The Staff Account users are the staffs or employes of the Bike Service Station and the Staff accounts and only created by the Admin. The Staff users can see the list of Services available but **cannot Add/Delete a Service**. The Role of the Staff User is for modifying the status of the Bookings made by the customer.

### Customer
 - Can Signup using email and mobile
 - Book one or many service availabe
 - View all past and present Booking History

The Customers cannot view the Admin Page. Its Viewed only by the Admin and Staff account users.

# Login Details
The application has some default data sets to play within the webpages and the credentials for accessing the accounts are as follows:
- Admin Account
    - Email : admin@hudsonsparklers.in
    - Password : Admin@pass123
- Staff Account
    - Email : staff1@hudsonsparklers.in
    - Password : Staff@pass123
- Customer Account 
    - Email : johndoe@mail.com
    - Password : Testpass123
    - Email : janedoe@mail.com
    - Password :Testpss123

**Customer Accounts** can be created using signup page in the website and Staff accounts can be created by using **Admin Account** users only (i.e. in the admin page).

# Sending Email
Since we are working with localhost and manipulating fake data sets(unauthorized emails), the emails are not actually sent But still the emails are send by **DEBUG MODE**. The Email can be viewed in the **Console/Terminal** which was first used to run the application(remember the python manage.py runserver command used at beginning).
Any mails send through the application can be viewed in that terminal.

The Emails are sent for the following purposes:
- Forgot Password
- When A Customer Books a Service
- When the Admin/Staff marks the booking as Ready/Delivered/Canceled


## Customizing Database
The project has a SQLite DB with sample datasets for you to use. If you want to connect with MySQL  then open the settings.py file in the bike_service folder and uncomment the lines from 93 to 102. So it looks like this after changing:
```python
93  DATABASES = {
94     "default": {
95         'ENGINE': 'django.db.backends.mysql',
96         'NAME': 'databasename',
97         'USER': 'username',
98         'PASSWORD': 'password',
99         'HOST': 'localhost',
100         'PORT': '3306',
101     }
102 }
```
If you are using MySql with cloud or different connection string, then change the host, user, password accordingly.

And to finally apply the schema in your DB apply the following command in the terminal from your project root (i.e bike_service_app)
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```
Now You are ready to use your own MYSql DB from your local machine.

Since you have Migrated to a new database you have to create an Admin Account to view the admin pages. Enter the following command and follow the instructions

```sh
$ python manage.py createsuperuser
```

After creating the superuser visit https://localhost:8000/superadmin and login using the credentials created by you at the previous step. Here your can create the Admin Account.

**PS:** The Superuser is used for the developers to manipulate the database and for develpopment purpose only. The superuser should not be mixed the the Application level User Types.

## Customizing Emails
Emails are for now only viewed in the terminal but in realtime its not the case. To enable sending email actually to the users, you will need an SMTP server with the following credentials
- SMTP HOST
- HOST USER
- HOST PASSWORD

If you have these credential then open the settings.py file and comment line no: 146 and  uncomment the lines from 148 to 153. So it looks like this after changing:

```python
146     #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #Development Only
147
148      EMAIL_HOST = '<smtp.host>'
149      EMAIL_PORT = 587
150      EMAIL_HOST_USER = '<username>'
151      EMAIL_HOST_PASSWORD = '<password>'
152      EMAIL_USE_TLS = True
153      DEFAULT_FROM_EMAIL = "admin@hudsonsparklers.in"
```

**PS:** Don't Forget to change the credentials accordingly.
 Now you are ready to send mails live. 
