# Final Deployment Checklist

## 1. Files Ready ✓
- [x] requirements.txt (with all dependencies)
- [x] .env.production (with DEBUG=False)
- [x] pythonanywhere_wsgi.py
- [x] deploy_commands.sh
- [x] static files collected in static_root/
- [x] deployment package script (deployment.ps1)

## 2. Database & Media ✓
- [x] All migrations created and applied
- [x] Media directory structure ready
- [x] Static files collected

## 3. Security Configurations ✓
- [x] DEBUG set to False in production
- [x] Secret key properly configured
- [x] ALLOWED_HOSTS configured for PythonAnywhere

## 4. PythonAnywhere Setup Required
1. Create a PythonAnywhere account if you haven't already
2. Create a new web app:
   - Choose Manual Configuration (not Django)
   - Python 3.10
3. Upload deployment package:
   ```bash
   # On PythonAnywhere console
   cd ~
   unzip djangogirls_deploy.zip
   ```
4. Set up virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 djangogirls-virtualenv
   pip install -r requirements.txt
   ```
5. Configure web app:
   - Source code: /home/NainaJain/djangogirls
   - Working directory: /home/NainaJain/djangogirls
   - Virtual environment: /home/NainaJain/.virtualenvs/djangogirls-virtualenv

## 5. Final Steps
1. Run migrations:
   ```bash
   python manage.py migrate
   ```
2. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
3. Configure static files in PythonAnywhere web app:
   - URL: /static/
   - Directory: /home/NainaJain/djangogirls/static_root
4. Configure media files:
   - URL: /media/
   - Directory: /home/NainaJain/djangogirls/media

## 6. Testing After Deployment
1. Visit your site: http://NainaJain.pythonanywhere.com
2. Test user registration
3. Test login/logout
4. Create a test journal entry
5. Test image upload
6. Verify static files (CSS, images)

Note: Replace 'NainaJain' with your actual PythonAnywhere username

