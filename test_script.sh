# Script de teste que cria e aplica as migrations antes de rodar os testes
# Condição: estar com o ambiente virtual ligado

cd MonitorVoos/
python manage.py makemigrations
python manage.py migrate
python manage.py test