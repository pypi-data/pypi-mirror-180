#!/bin/bash

# TODO
# TODO : Do we still need SCROT (Linux) ? Or is it possible to use Pillow (portable) instead?
# TODO



# *** DEPRECATED : Implement a Python script in RobotDeck.py instead !!!!
#                  --> We don't want to be dependant on Linux (it should work )



###################################################################################################
#
# --- Launching this script :
#   To launch this script and skip the installation / update of tools run : 
#       > ./launchRobotDeck.sh -s
#               or
#       > ./launchRobotDeck.sh --skip
#
# --- Prerequired Dependencies
#
#   For the script and the launcher to run, you will need these tools :
#       Base :
#       - Python3 (>= 3.6)
#
#       GUI testing (Linux) :
#       - scrot             -> For screenshot capacities
#
# --- Documentation
#
#   - To install these dependencies, please refer to the documentation page.
#   - Other dependencies will install automatically with PIP (See below for the detailed list.)
#
###################################################################################################

# Setting up the virtual environment for Python
install=true

if [ $# -ge 1 ] && [ $1 == "-s" ]; then
    install=false
fi

if [ $# -ge 1 ] && [ $1 == "--skip" ]; then
    install=false
fi

if [ $install == true ]; then
    python3 -m pip install pip --upgrade
    python3 -m pip install virtualenv --upgrade

    virtualenv -p `which python3` .venv;
fi

source ./.venv/bin/activate

if [ $install == true ]; then
    # Base
    pip install pip --upgrade
    pip install pylint --upgrade

    # GUI
    pip install Pillow --upgrade
    pip install PySide6 --upgrade      # We need to test PySide6 !

    # PyAutoGui Tools
    pip install pyautogui --upgrade
    pip install opencv-python --upgrade

    # Utilities
    pip install pyperclip --upgrade
fi

# Launch the RobotDeck
python RobotDeck.py
