# Odara
Sistema Papelaria

Como rodar o projeto?
Clone esse repositório.
Crie um virtualenv com Python 3.
Ative o virtualenv.
Instale as dependências.
Rode as migrações.
git clone https://github.com/rg3915/django-tenants-tutorial.git
cd django-tenants-tutorial
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py

docker-compose up -d  # O objetivo é rodar o PostgreSQL

python manage.py migrate
python manage.py test
python manage.py createsuperuser --username="admin" --email=""
