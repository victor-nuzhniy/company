# COMPANY

## Installation

### DB creation

For db creation using only flask functionality we need:
    - activate env;
    - in terminal '$env:FLASK_APP="api"' for windows;
    - run 'flask db init';
    - flask db migrate -m "0001" (vary name);
    - flask db stamp head;
    - flask db upgrade;
