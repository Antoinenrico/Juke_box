# Juke_box

### Storage

You have to follow this organisation :
static : scriptrico.js
templates : - indexrico.html
            - indexparametre.html
main file : all others

### The web interface

You’ll need to generate and activate a python3 virtual environment:  
```
$ python3 -m venv ./venv
$ source venv/bin/activate
```

You’ll know that the virtual environment is active when your prompt is prefixed
by `(venv)`. To exit the virtual environment simply type  
```
(venv) $ deactivate
```

Install the required dependencies within your virtual environment:  
```
(venv) $ pip install -r requirements.txt
```

Now you can finally launch the webserver:  
```
(venv) $ ./webserverrico.py
```

To view the webpage in your browser, open http://127.0.0.1:5000 in your web
browser.

### Start with

you have two option :
python3 cinq.py => you will acces to physical code
python3 webserverrico.py => this will generate web interface and if you click on init you will start few Gcode
