from counterpartylib import server

options = {
        'database_file': None,
        'log_file':  None,
        'api_log_file':  None,
        'testnet':  False,
        'testcoin':  False,
        'backend_name':  None,
        'backend_connect':  'localhost',
        'backend_port':  8332,
        'backend_user':  '',
        'backend_password':  '',
        'backend_ssl':  False,
        'backend_ssl_verify': True,
        'backend_poll_interval': None,
        'rpc_host': '0.0.0.0',
        'rpc_port': 4000,
        'rpc_user': '',
        'rpc_password': '',
        'rpc_allow_cors': None,
        'force': False,
        'verbose': False
}

db = server.initialise(**options)
server.start_all(db)
