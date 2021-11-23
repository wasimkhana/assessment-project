# Lost and Found (LOFO) RESTful Application

### Scenario
Let’s suppose a small startup wants to build a Lost and Found platform which would help the end user to search and view the lost items and upload the found items. Let’s suppose you got the opportunity to join this startup as a backend Intern. You must provide clear and complete documentation about how to run your program. You should be able to handle different routes in your app. A user should be able to register and then can login into the application. Provide a search based functionality provide on different parameters like location and itemname. A user should be able to add found item and can view lost items. The user must be able to update and delete the data from the existing set data.


- Table of Content
[ToC]

### Requirements

#### Functional Requirements
Following are the functions which the application will be able to perform.
* **User signup /signin**
User shall be able to sign up with his/her credentials for the first time and then can login to use the app features.
* **Item crud operations**
User shall be able create items (found-item posts), update posted/added item details, read all other user items and delete created items.
* **Search item**
User shall be search specific items through location and itemname information in the application.
* **Profile read and modify details**
User shall be able to view its own added/posted items and modify its profile details except email and username for better security and performance of the application.
* **Strong password acception**
User will need to enter strong password with at least 8 characters length and at least 1 special character, number and alphabet each.

#### Non-functional Requirements
Following are the non-functional requirements;
* **Security**
User password will be encrypted before storing in the database which cannot be understood if retrieved the data from database.
* **Performance**
The application should perform well and provide responsive messages on each operation.

### Detail Design and Architecture
The application include SQLite database for development phase. Later MySQL will be used for development phase.
* **Entity Relationship Digram**
A user can add multiple found items details. But an added item has must one-to-one relation with user.
![LOFO ER-Diagram](https://i.imgur.com/oaNQbOT.png)
* **Logical Schema**
A user will be assigned with an auto-id and will have unique email and username. An id helps in fast processing. The logical schema of user is given in Table-1.
![](https://i.imgur.com/fH7Z3YP.png)


   An item will item_id as primary key which will be automatically assigned, creation date which can help us in many way like perform cron-job and user foreign key for one-to-one must relationship. Table-2 includes the logical schema of an item.
![](https://i.imgur.com/4ZRnZJs.png)


* **Use Case Diagram**
The use following use case diagram shows all the possible interaction of the user with the system and different type of user of the application.

![](https://i.imgur.com/0oXxR0q.png)

### Implementation
A good framworks help to  develop quality products faster. Developers enjoy and get good development experience using frameworks. FastAPI is modern Python based web framework with high speed compare to Node.js and Go. It has detailed and friendly developer docs. The LOFO project includes the following concepts.
* **Model**
Model is used for modelling the application data. It mirrors a database table. An object of these model class is used to send or retrieve data from database with Object Relational Mapper(ORM) tool like SQLALchemy. ORM tool used to translate Python classes into relational database tables and concert function calls to SQL queries.

* **OAuth2 and JSON Web Tokens(JWT)**
JSON Web TOken (JWT) is a token format and OAuth2 is an authorization protocol which can use JWT as a token. OAuth uses client-side and server-side storage. Thus a built-in OAuth2 support in FastAPI for a JSON Web Tokens (JWT) is used for creating a token based login endpoint. Further a 30 minute session is created for a user to live and use the LOFO application features.

* **Password Hashing**
To secure user password, hashing function is created to encode the password before storing in the database. A password verifier function is used to compare the plain-password with the hashed-password while logging-in. A passlib library and dcrypt package is used to achieve hashing. To provide unicode support passlib is used to encode unicode passwords using utf-8 before running them through bcrypt.

* **Functional Operations**
Different operational functions are created for each operation like login, signup and get_item etc with specific well defined routes. Further FastAPI is used which is accessed thorugh REST API to call different routing functions of the application. Further APIRouter is used to organize the path operations related to a specific model like User and Item in our application. APIROuter is also called mini FastAPI and support all the same parameters, responses, dependencies and tags etc.

* **Regular Expression**
A python built-in 're' package is used for the regular expressions. Two expressions are used for email and passwods. A password expression check that passwords must be at least 8 characters long and must contain at least 1 alphabet, 1 integer and 1 special character.
    * Email expression
    (r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
    * Password expression
    (r'.*(?=.{8,})(?=.*\d)(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).*$')


* **System Specifiction**
The project work is performed on personal system with the following specifications:
    * Intel Core i5-4200U
    * 1.6GHz clock-speed
    * 8 GB RAM
    * Ubuntu 20.04 OS

### Testing
Testing and evaluation of the software system is the most crucial part of the software development life cycle as this phase certifies that either the system is ready to be rolled out to production or it needs some improvements. The testing phase adds value to the software and hence should be carried out with due care. It is a comparison between the expected result to the real results.

During testing of the LOFO application, three techniques are used FastAPI automatic documentation (provided by Swagger UI and ReDoc) and postman for playing with builted endpoints and Tableplus to check database tables and its instances.
The testing results of the endpoints are given below;

* **Signup**
To register the user in the LOFO application. One need to enter the required data. User schema is used to provide the fields structure.
![](https://i.imgur.com/6deHlfB.png)

   The profile is successfully created and assured through tableplus to check the registered user data.
![](https://i.imgur.com/Tb74gaM.png)

* **Login**
To use the item crud operations and user operations, one need to be registered and login. The login API is tested for token generation using postman tool.
![](https://i.imgur.com/Pv16dJd.png)

* **Create Item**
To post a found item in the application one need to login into the system.
![](https://i.imgur.com/wZtqv2a.png)

  Add details of the item he/she found as following: 
![](https://i.imgur.com/401KQRB.png)

  Here is the successful insertion of the item into the database of the application.
![](https://i.imgur.com/T4vO05p.png)

All other functionality of the LOFO application are tested accordingly and found sound results.

### Difficulties Faced during the task
Being new to FastAPI, I faced some errors during the implementation. But after studing the mistakes, it was easy to handle. I learnt the framework and can now produce products more faster.

I faced the following errors.
* **Use of equal sign in schema**
I copied the user model data to easily create the fields in the user schema but forgot to change '=' character with ':'. It use to hide the fields/schema in the FastAPI automatic documentation (Swagger UI and ReDoc). One use to face difficulty while creating user.

* **ProgrammingError**
I faced ProgrammingError when I was tring to update item details. This error is used to be shown in the terminal becuase of using unstructured/wrong format in the update questy of sqlalchemy. I solved using python dictionary.

* **rough routes and names issue**
I faced too difficulty while implementing the updated and delete APIs for item because of rough routing and naming of the operation functions. After refining the and standarizing the code. I easily implemented all other functionalities.


### Lost and Found application environment setup

#### **Step-1** Cloning repository

```
# clone porject
git clone https://github.com/Artaghal/assessment-project.git

#change directory
cd assessment-project/
```
#### **Step-2** Python-vitual environment and dependencies installation

```
# create app-env python-virtual environment
python3 -m venv app-env

# to install the required packages
pip install -r requirements
```

#### **Step-3** Activate python-virtual environment (app-env)
```
# activate app-env
source app-env/bin/activate
```

#### **Step-4** change directory and run application
```
# change dir
cd restApp

#run application
uvicorn main:app --reload

```
Copy the url and paste in the browser with a docs or redoc route like:
[localhost:8000/docs](localhost:8000/docs)
or
[localhost:8000/docs](localhost:8000/redoc)


Congratulations! :partying_face:

Link to the deployed application:
[LOFO Application](https://pymps9.deta.dev/docs)
