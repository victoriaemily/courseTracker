virtualenv --python=/usr/bin/python3.8 venv
source venv/bin/activate
pip3 install -r requirements.txt -t venv/lib/python3.8/site-packages
cd venv/lib/python3.8/site-packages
touch __init__.py
cd ../
mv site-packages libs
zip -r9 deployment_package.zip .