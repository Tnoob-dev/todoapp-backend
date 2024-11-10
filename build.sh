python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install reflex --upgrade
reflex init
reflex export
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate