{% extends "web.html" %}
{% block body %}
import os
path = os.getcwd()
with open("backup.csv","r") as fi:
    students = fi.read()
    {% for f in students %}
        {{f}}+=1
    {% endfor %}
{% endblock %}
