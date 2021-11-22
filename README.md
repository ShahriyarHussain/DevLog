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
if it doesn't show then `python3` must be installed first.

If you are on Ubuntu/Ubuntu based distros with `apt` package manager you install via the following command.

### On Linux Distros with `apt` package manager
```
sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip
```

Most linux distribution come with some package manager using which `python` along with `pip` can be installed. Synaptic package manager also contains python distribution.

On other operating systems(Windows/MacOS), please follow the link [**here**](https://www.python.org/downloads/). On MacOS, Python installation is also available using `brew`.

### Installing packages

It **Strongly Recommended** to setup a separate virtual environment for the project.

**Setting up virtual environment:**
```
pip3 install virtualenv
python3 -m venv myvirtualenv
```
This will create the virtual environment. Now activate the virtual environment:
```
source myvirtualenv/bin/activate
```
*If you are using Windows CLI/Powershell then don't type the `source` command*

**Installing packages:**
The packages are written in the `requirements.txt` file. To install them all at once type the following command. You must be in the project directory to run the Following command. or you may have the provide the full/absolute path:
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

If you still face any issues, try searching StackOverflow or other forums. It is likely that they will have the solution. Still if you can't solve, mail me  [**here**](mailto:dr6j0wkjg@relay.firefox.com).
