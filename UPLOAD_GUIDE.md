# How to Upload Files to PythonAnywhere

## Method 1: Direct Upload through Web Interface (Easiest)
1. Log in to PythonAnywhere
2. Click on "Files" in the top menu
3. Navigate to your home directory
4. Click "Upload a file" button
5. Select djangogirls_deploy.zip from your computer
6. Wait for upload to complete

## Method 2: Using GitHub (Recommended for Development)
1. Create a GitHub repository
2. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/djangogirls.git
   git push -u origin main
   ```
3. On PythonAnywhere bash console:
   ```bash
   git clone https://github.com/yourusername/djangogirls.git
   ```

## Method 3: Using PythonAnywhere's Command Line Tools
1. Install pythonanywhere command line tool on your local machine:
   ```bash
   pip install pythonanywhere
   ```
2. Log in:
   ```bash
   pa-upload login
   ```
3. Upload files:
   ```bash
   pa-upload upload djangogirls_deploy.zip
   ```

## After Uploading
1. Open a Bash console in PythonAnywhere
2. Unzip the uploaded file:
   ```bash
   cd ~
   unzip djangogirls_deploy.zip -d djangogirls
   cd djangogirls
   ```
3. Continue with deployment steps in QUICK_DEPLOY.md

## Troubleshooting
- If the file is too large for direct upload:
  - Split it into smaller parts
  - Use GitHub method instead
- If you get permission errors:
  - Check file permissions: `ls -la`
  - Fix permissions if needed: `chmod -R 755 djangogirls`

Note: The GitHub method is recommended for ongoing development as it makes future updates easier.

