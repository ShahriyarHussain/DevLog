# DevLog - A blog for Devs

A simple blog with basic functionalities like posting texts with images, post tags, rich text formatting and also commenting to posts.

## Development
The project doesn't include any complex or sophisticated framework. It is built with the fundamental features of the Django framework and basic HTML, CSS. Following are steps to download the project on your machine and start developing.

***N.B.: It is recommended to fork the project and `git clone` it to your machine for additional development. It will later help us if you wish to merge you developments with pull requests.***

### Pre-requisites

This project requires at least `python 3.6` or above. `pip` should also installed which will be used to install required python packages. To check python version type following in terminal/CLI:
```
python3 --version
```

Most linux distribution come with some package manager using which python along with pip can be installed. Synaptic package manager also contains python distribution.
Please follow the link [**here**](https://www.python.org/downloads/) for the official download page of Python.

### Installing packages

It **Strongly Recommended** to setup a separate virtual environment for the project.

**Setting up virtual environment:**
```
pip3 install venv
python3 -m venv myvirtualenv
```
This will create the virtual environment. Now activate the virtual environment:
```
source myvirtualenv/bin/activate
```
*If you are using Windows CLI/Powershell then don't type the `source` command*

**Installing packages:**
The packages are written in the `requirements.txt` file. To install them all at once type the following command:
```
pip install -r requirements.txt
```
Run the command again if you face any errors. This should set you up to run the project on localhost.

### Running on localhost/browser
To check any errors:
```
python manage.py check
```
Run the project using:
```
python manage.py runserver
```
now go to `localhost` or `127.0.0.1:8000/` to check whether it ran properly or not.

**That's it. You are ready to go for development.**
