import os

ORG = os.environ.get('SUBSTRABAC_ORG', 'substra')
DEFAULT_PORT = os.environ.get('SUBSTRABAC_DEFAULT_PORT', '8000')
ORG_NAME = ORG.replace('-', '')
ORG_DB_NAME = ORG.replace('-', '_').upper()