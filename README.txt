
conda create --name certamen2 Python=3.12.7

conda activate certamen2

conda install numpy pandas matplotlib

conda install Django==5.1.3

conda env export > environment.yml
-----------------------------------------------------------------------------
en vscode
activo el environment seleccionando >python interpreter de certamen2

django-admin startapp CRUD

python manage.py startapp MisComunas

despues de editar y poner codigo

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
