# Quick Deployment Steps

## 1. PythonAnywhere Setup
1. Go to https://www.pythonanywhere.com and create an account
2. Click "Web" in the dashboard
3. Click "Add a new web app"
4. Choose "Manual configuration"
5. Select Python 3.10

## 2. File Upload & Setup
1. Open a Bash console in PythonAnywhere
2. Run these commands:
   ```bash
   cd ~
   # Upload djangogirls_deploy.zip through the Files page
   unzip djangogirls_deploy.zip
   mkvirtualenv --python=/usr/bin/python3.10 djangogirls-virtualenv
   cd djangogirls
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   ```

## 3. Configure Web App
1. Go to the Web tab
2. Under "Code" section:
   - Source code: /home/YourUsername/djangogirls
   - Working directory: /home/YourUsername/djangogirls
   - WSGI configuration file: Use content from pythonanywhere_wsgi.py

3. Under "Virtualenv" section:
   - Enter: /home/YourUsername/.virtualenvs/djangogirls-virtualenv

4. Under "Static files":
   Add:
   - URL: /static/
   - Directory: /home/YourUsername/djangogirls/static_root
   
   Add another:
   - URL: /media/
   - Directory: /home/YourUsername/djangogirls/media

5. Click the big green "Reload" button

## 4. Final Check
1. Visit your site at: https://YourUsername.pythonanywhere.com
2. Test everything:
   - Login/Signup
   - Create a journal entry
   - Upload an image
   - Check if CSS is loading correctly

Need help? Check DEPLOYMENT.md for detailed instructions.

