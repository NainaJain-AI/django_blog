# Deploying from GitHub to PythonAnywhere

## 1. PythonAnywhere Initial Setup
1. Go to https://www.pythonanywhere.com
2. Log in or create an account
3. Open a Bash console from the Dashboard

## 2. Clone Your Repository
```bash
# In PythonAnywhere bash console
cd ~
git clone https://github.com/NainaJain-AI/django_blog.git djangogirls
cd djangogirls
```

## 3. Set Up Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 djangogirls-virtualenv
pip install -r requirements.txt
```

## 4. Create and Configure .env File
```bash
# In PythonAnywhere bash console
echo "SECRET_KEY=6-w*-ujtl%gi4s40t7t)nn@ul&uqpen^%+i0o+==$=-2zigj6f" > .env
echo "DEBUG=False" >> .env
echo "ALLOWED_HOSTS=['NainaJain.pythonanywhere.com']" >> .env
```

## 5. Set Up Web App
1. Go to Web tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10

## 6. Configure Web App
1. Under "Code" section:
   - Source code: /home/NainaJain/djangogirls
   - Working directory: /home/NainaJain/djangogirls
   - WSGI configuration file: Edit with content from your pythonanywhere_wsgi.py

2. Under "Virtualenv" section:
   - Enter: /home/NainaJain/.virtualenvs/djangogirls-virtualenv

3. Under "Static files":
   Add:
   - URL: /static/
   - Directory: /home/NainaJain/djangogirls/static_root
   
   Add another:
   - URL: /media/
   - Directory: /home/NainaJain/djangogirls/media

## 7. Final Setup
```bash
# In PythonAnywhere bash console
cd ~/djangogirls
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser
```

## 8. Reload Web App
1. Go back to Web tab
2. Click the big green "Reload" button
3. Visit your site at: https://NainaJain.pythonanywhere.com

## 9. Future Updates
To update your site with new changes:
```bash
cd ~/djangogirls
git pull origin main
python manage.py collectstatic --noinput
python manage.py migrate
```
Then reload your web app from the Web tab.

## Troubleshooting
- If static files aren't loading:
  - Check paths in Web tab
  - Run collectstatic again
- If you get a 500 error:
  - Check error logs in Web tab
  - Verify .env file settings
- If you get a "Could not connect to database" error:
  - Check database settings
  - Ensure migrations are applied

Remember to replace 'NainaJain' with your actual PythonAnywhere username throughout these instructions.

