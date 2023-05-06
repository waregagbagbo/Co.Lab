# Co.Lab
A simple web application that makes an API call to display 3-5 pieces of data you retrieve from the API service.

## Project Installation

Create a virtual environment  named .venv on the current interpreter

### Linux

sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

### macOS

python3 -m venv .venv
source .venv/bin/activate

### Windows

py -3 -m venv .venv
.venv\scripts\activate

Then Update pip
python -m pip install --upgrade pip

### Handling Staticfiles

- Make user staticfiles is installed in the apps
- import os as per the new version of Django

 For static files set folder and path locations as
 STATIC_URL = 'static/'
 STATICFILES_DIRS = [BASE_DIR/'static']

 Then head over to your root urls and import static and settings files
 add the static path to the urlpatterns as:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # for development only
 or if settings.DEBUG:urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


Install Django Crispy forms to use in the Contact FORM