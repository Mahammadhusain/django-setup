import subprocess
import os

#  -------------------------------------------------------------------------
#  ------------------------------- Create Project --------------------------
#  -------------------------------------------------------------------------
projectname = input('Enter Project name = ')
subprocess.run(f'django-admin startproject {projectname}', shell=True)
# ------------------- Open Project with Vs Code -----------------------
subprocess.run(f'code {projectname}', shell=True)

os.chdir(projectname)
# ------------------- Create Static Folder In Project -----------------------
os.mkdir('static')
ppath = os.getcwd()
os.chdir(projectname)

# Set path of Media | Static in (Setting.py)
file1 = open("settings.py", "a+")
L = ["STATICFILES_DIRS = [BASE_DIR / 'static'] \n", "MEDIA_ROOT =  BASE_DIR / 'media' \n","MEDIA_URL = '/media/' \n" ]
file1.writelines(L)
file1.close()

# Set path of image in (Url.py)
open("urls.py", "r")
line_index1 = 16

lines = None
ls = ['from django.urls import path,include','from django.conf import settings','from django.conf.urls.static import static'][::-1]


with open('urls.py', 'r') as file_handler:
    lines = file_handler.readlines()
for i in ls: 
    lines.insert(line_index1, i+'\n')



#  -------------------------------------------------------------------------
#  ------------------------------- Create App ------------------------------
#  -------------------------------------------------------------------------
os.chdir(ppath)
appname = input('Enter App name = ')
subprocess.run(f'django-admin startapp {appname}', shell=True)

# Go in App Directory
os.chdir(f"{appname}")


# ----------- Create all necessary PY Files in App ----------------
app__py_file_list = ['urls.py','form.py','serializers.py']
for i in app__py_file_list:
    with open(i, 'w') as fp:
        pass

# Create urls.py in App and write base code for url
urls_index = 0
appn = ["from django.urls import path","from .views import *"," ","urlpatterns = ["," ","    path('', HomeView,name='home'),"," ","]"][::-1]
with open('urls.py', 'r') as file_handler:
    lines = file_handler.readlines()
for i in appn: 
    lines.insert(urls_index, i+'\n')
with open('urls.py', 'w') as file_handler:
    file_handler.writelines(lines)

# Create form.py in App and write base code for Form
form_index = 0
appn = ["from django import forms"]
with open('form.py', 'r') as file_handler:
    lines = file_handler.readlines()
for i in appn: 
    lines.insert(form_index, i+'\n')
with open('form.py', 'w') as file_handler:
    file_handler.writelines(lines)

# write base code for For Views
view_index = 3
appn = ["def HomeView(request):","    context = {","      'h':'Hello world with django'","    }","    return render(request,'index.html',context)"][::-1]
with open('views.py', 'r') as file_handler:
    lines = file_handler.readlines()
for i in appn: 
    lines.insert(view_index, i+'\n')
with open('views.py', 'w') as file_handler:
    file_handler.writelines(lines)


# ------------------- Create (template )directory in App --------------------
os.mkdir('templates')
os.chdir('templates')

# ------------------- Create HTML Files in app/template ------------------
html_files_list = ['base.html','index.html'] 
for i in html_files_list:
    with open(i, 'w') as fp:
        pass

# Create base.html in App/templates and write base code for it
base_html_index = 0
appn = [
    '{% load static %}',
    ' '
    '<!DOCTYPE html>',
    '<html lang="en">',
    '<head>',
    '    <meta charset="UTF-8">',
    '    <meta http-equiv="X-UA-Compatible" content="IE=edge">',
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '    <title>',
    '        {% block title %}',
    '                                      ',
    '        {% endblock title %}',
    '    </title>',
    '</head>',
    '<body>',
    '  ',
    '  {% block body %}',
    '   ',
    '  {% endblock body %}',
    '  ',
    '</body>',
    '</html>',

    ][::-1]
with open('base.html', 'r') as file_handler:
    lines = file_handler.readlines()
for i in appn: 
    lines.insert(base_html_index, i+'\n')
with open('base.html', 'w') as file_handler:
    file_handler.writelines(lines)


# Create index.html in App/templates and write base code for it
index_html_index = 0
appn = [
    '{% extends "base.html" %}',
    '{% load static %}',
    '{% block title %}',
    '     Index | Page ',
    '{% endblock title %}',
    
    '   ',
    '{% block body %}',
    '  <h1>{{h}}</h1> ',
    '{% endblock body %}',
    '   ',
   
    ][::-1]
with open('index.html', 'r') as file_handler:
    lines = file_handler.readlines()
for i in appn: 
    lines.insert(index_html_index, i+'\n')
with open('index.html', 'w') as file_handler:
    file_handler.writelines(lines)

# ------ After Create App Register in to setting.py -----------
os.chdir("..")
os.chdir("..")
os.chdir(projectname)

app_index = 39
appn = [f"    '{appname}',"]
with open('settings.py', 'r') as file_handler:
    lines = file_handler.readlines()
for i in appn: 
    lines.insert(app_index, i+'\n')
with open('settings.py', 'w') as file_handler:
    file_handler.writelines(lines)

#  -------------------------------------------------------------------------
#  ------------------- Run Innitial Migarte Command ------------------------
#  -------------------------------------------------------------------------
os.chdir("..")
subprocess.run(f'python manage.py migrate', shell=True)
print('----------- Create Username and Password for Access Django Admin Panel -----------------')
subprocess.run(f'python manage.py createsuperuser', shell=True)


#  ------------------- Include App urls path in Project/urls.py ------------------------
os.chdir(projectname)

app_url_index = 22
line_index2 = 24
appurl = f'    path("", include("{appname}.urls")),'
impath = ']+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'
with open('urls.py', 'r') as file_handler:
    lines = file_handler.readlines()
for i in ls: 
    lines.insert(line_index1, i+'\n')

lines.insert(app_url_index, appurl+"\n")
lines.insert(line_index2, "\n"+impath)
# ---- Remove ] from Project/urls.py ------
lines.pop()
with open('urls.py', 'w') as file_handler:
    file_handler.writelines(lines)


subprocess.run(f'python manage.py runserver', shell=True)

print("""
_  _ ____ ___  ___  _   _    _  _ ____ ____ _  _ _ _  _ ____ 
|__| |__| |__] |__]  \_/     |__| |__| |    |_/  | |\ | | __
|  | |  | |    |      |      |  | |  | |___ | \_ | | \| |__]

""")


# Project Run related stuff
run_options = input('You want to run it ? (Y/N)')
if run_options == 'N' or 'n':
    subprocess.run(f'python manage.py runserver', shell=True)
else:
    print('-------------------- Have a good day ------------------')




