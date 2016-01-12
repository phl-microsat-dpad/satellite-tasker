# Imagery Request - Satellite Tasking Form

## Overview

This module is currently composed of 3 pages:
- Submit a new tasking order: http://phl-microsat.cloudapp.net/tasking/
- View all tasks: http://phl-microsat.cloudapp.net/tasking/orders
- View details of a single task: http://phl-microsat.cloudapp.net/tasking/orders/3


## Dependencies
- Python 2.7
- Bower

## Install and Run
- Install python dependencies: `pip install -r requirements.txt`
- Install bower components: `bower install`
- Initialize database: `python create_db.py`
- Run the app: `python run.py`

Note: The app will run at port `3000`. (eg. `http://localhost:3000/orders`)