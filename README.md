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

### Sensitive data

1. .env file must be created locally and filled with sensitive info:
    -SECRET_KEY
    -SQLALCHEMY_DATABASE_URI
    -ADMIN_PASSWORD
2. ADMIN_PASSWORD should be set for admin user creation, used in AdminUserRoute endpoint
    and then deleted with reloading app.

### Performing commits

1. Pre-commit hook installed, settings are in .pre-commit-config.yaml
2. To instantiate new hook settings change .pre-commit-config.yaml file
     and run     pre-commit install
3. To bypass hook checking run      git commit -m "..." --no-verify

### Testing app

1. For app testing use command
   - pytest --cov


## Usage

### Browsable API

1. Browsable API is accessable at '/api/spec.html'.

