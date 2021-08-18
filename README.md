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


Congratulations you successfully run the application.

Link to the deployed application:
[LOFO Application](https://pymps9.deta.dev/docs)

Link to the details of the application:
[LOFO Details](https://hackmd.io/@Artaghal/r1AG_LceK)
