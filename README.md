#Easily dealing with multiple files in Django

This is a Django 1.9 project which puts into practice what is stated at http://www.easydevmixin.com/2015/07/17/easily-dealing-with-multiple-files-in-django/

Inside the `tools/` directory is a `requirements.txt` file which you can use in order to install necessary third-party libraries.

The project uses a SQLite3 database. Before running it you must run:

1. `./manage.py makemigrations`
2. `./manage.py migrate`

So the DB will be set up.

After that, assuming you run the project on your local and use port 8000,  head to `http://localhost:8000/multiple_files`. A form will be presented where you can add multiple files.

Multiple files are added using the `multiple` attribute for a field-type html5 input, so use `Ctrl + click` or `Shift + click` to select multiple files from the files dialog (see http://www.w3schools.com/tags/att_input_multiple.asp).

Have fun!

EasyDevMixin

20161019
