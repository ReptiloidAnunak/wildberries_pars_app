
#!/bin/bash

echo "Aply migrations ... "

docker exec -it wb_api_server /bin/bash -c "./manage.py makemigrations && ./manage.py migrate"