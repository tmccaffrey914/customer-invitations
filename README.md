# Take Home Test
This package takes an input of Customer Information in the form of a Text File - either stored locally on the machine 
or at a given URL; and a Radius in Kilometers. The Radius is then used to determine which customers are within range 
of Dublin.

## 🏃How to Run 🚶
First things first, lets get our own copy of the project:
```shell script
git clone https://github.com/tmccaffrey914/customer-invitations.git
cd customer-invitations
```

The simplest way to get started is to run the project as a Pip distributed package. To do this, simply run:
```shell script
pip install .
```
(If you don't have Pip, please continue to the "How to Develop" Section)

That's it! We're set up. Now, we can start finding customers. We have the option to do this in one of two ways, we 
can supply a URL from which we can pull and process the customer data - or alternatively we can pass a filepath.

To process a URL:
```shell script
create-invite-list https://s3.amazonaws.com/intercom-take-home-test/customers.txt
``` 
To process a File Path:
```shell script
create-invite-list-from-file customers.txt
``` 

To show the full list of options, run either of these commands with the `--help` option.

## 👨‍💻 How to Develop (MacOS Instructions) 👩‍💻
This project was developed using Python 3.8.5, but it should support versions of Python greater than 3.6.

If you don't have Python Installed:
```shell script
brew install python
```
(If you dont have HomeBrew, get it here: https://brew.sh/)

Within the cloned repo, called "intercom" - run the following command to set up a Virtual Environment in which 
to install our Projects 3rd Party Dependencies without affecting the OS's versions of Python:
```shell script
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Now in your IDE, point the Python Interpreter to the VirtualEnv we just created and you should be good to go! 
The entry point is `src/cli.py`. 🤫

## 🧪 How to Test 🧪
While in the Project Root, and within your Virtual Env we set up earlier -  run the following from the CLI:
```shell script
python -m unittest discover src/tests -p 'Test*.py'
```
This runs all the tests at once, something useful in CI/CD Pipelines.

To get more hands on with the UnitTests, you can run them within your IDE using the same Python Interpreter 
that we set up in the "How to Develop" Section. Just make sure you set the "Working Directory" to be the Project Root.

## 🐳 Docker Instructions 🐳
In your Shell, Navigate to the Project Root and run:
```
docker image build -t invite-customers .
```
Once the Docker Image "invite-customers" has finished building, run the Image as a Container:
```
docker run invite-customers
```

## 😢 How to Uninstall 😢
Yes, this is needed too. Run: 
```shell script
pip uninstall intercom-take-home-test
```
