
conda create --certamen2 myenv python=3.12.7

bash
conda activate certamen2

bash
conda install numpy pandas matplotlib
Exportar el Entorno:

conda env export > environment.yml

en vs code
activo el environment seleccionando el interpreter de certamen2

conda install Django==5.1.3

django-admin startapp CRUD

python manage.py startapp MisComunas

despues de editar 

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
