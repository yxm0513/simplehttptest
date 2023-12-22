vus=10
duration=30s


echo fastapi
k6 run --vus $vus --duration $duration fastapi-test.js
echo 
echo golang
k6 run --vus $vus --duration $duration golang-test.js
echo
echo flask
k6 run --vus $vus --duration $duration flask-test.js
echo
echo django
k6 run --vus $vus --duration $duration django-test.js
echo
