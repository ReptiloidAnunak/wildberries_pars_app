#!/bin/bash


docker exec -it wb_api_server /bin/bash -c "./manage.py createsuperuser"