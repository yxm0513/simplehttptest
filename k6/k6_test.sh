vus=10
duration=30s


echo fastapi
k6 run --vus $vus --duration $durations /k6/fastapi-test.js
echo 
echo golang
k6 run --vus $vus --duration $durations /k6/golang-test.js
echo
echo flask
k6 run --vus $vus --duration $durations /k6/flask-test.js
echo
echo django
k6 run --vus $vus --duration $durations /k6/django-test.js
echo
