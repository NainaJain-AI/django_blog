# Django Girls Blog Deployment Guide

## Pre-deployment Checklist
- [x] Requirements file updated
- [x] Production .env file created
- [x] WSGI configuration file prepared
- [x] Deployment commands script created
- [x] Static files collected
- [x] Database migrated

## PythonAnywhere Deployment Steps

### 1. Initial Setup
1. Log in to PythonAnywhere (https://www.pythonanywhere.com)
2. Go to the Web tab
3. Click "Add a new web app"
4. Choose "Manual configuration" (NOT "Django")
5. Select Python 3.10

### 2. Files Upload
1. Go to Files tab
2. Create directory: `/home/NainaJain/djangogirls`
3. Upload these files:
   - All project files
   - `.env.production` (will be renamed to .env)
   - `requirements.txt`
   - `pythonanywhere_wsgi.py`
   - `deploy_commands.sh`

### 3. Console Setup
1. Open a Bash console
2. Make deploy script executable:
   ```bash
   chmod +x /home/NainaJain/djangogirls/deploy_commands.sh
   ```
3. Run the deploy script:
   ```bash
   cd /home/NainaJain/djangogirls
   ./deploy_commands.sh
   ```

### 4. Web App Configuration
1. Go to Web tab
2. Under "Code" section:
   - Source code: `/home/NainaJain/djangogirls`
   - Working directory: `/home/NainaJain/djangogirls`
   - WSGI configuration file: Use content from `pythonanywhere_wsgi.py`

3. Under "Virtualenv" section:
   - Enter: `/home/NainaJain/.virtualenvs/djangogirls-virtualenv`

4. Under "Static files" section:
   Add:
   - URL: /static/
   - Directory: /home/NainaJain/djangogirls/static_root
   
   Add:
   - URL: /media/
   - Directory: /home/NainaJain/djangogirls/media

### 5. Final Steps
1. Click the "Reload" button in the Web tab
2. Visit your site at: http://NainaJain.pythonanywhere.com

### Troubleshooting
- Check the error log in the Web tab if the site doesn't work
- Ensure all paths match your PythonAnywhere username
- Verify the virtualenv is properly activated
- Make sure DEBUG is set to False in production
- Confirm ALLOWED_HOSTS contains your PythonAnywhere domain

Note: Replace 'NainaJain' with your actual PythonAnywhere username throughout this guide.

