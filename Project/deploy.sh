# deploy.sh

# Navigate to the project directory
cd /path/to/your/directory

# Pull changes from GitHub
git pull origin master

# Restart the web app on PythonAnywhere (if applicable)
pythonanywhere-reload-webapp your-web-app  # Replace with your web app name

# Install or update dependencies (if applicable)
source /path/to/your/virtualenv/bin/activate  # Activate virtual environment
pip install -r requirements.txt
