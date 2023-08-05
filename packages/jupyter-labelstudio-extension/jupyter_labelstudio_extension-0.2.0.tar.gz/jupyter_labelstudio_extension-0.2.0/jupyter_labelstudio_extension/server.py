from label_studio.server import _setup_env,_apply_database_migrations,_get_config,_create_user,_get_free_port,_app_run


from tornado.ioloop import IOLoop
from tornado import web
import os
from label_studio.core.utils.params import get_env
from label_studio.core.utils.common import start_browser
from label_studio.core.argparser import parse_input_args
import sys
import logging

logger = logging.getLogger(__name__)

DEFAULT_PORT=8080

def run():
    print("sysargc:",sys.argv[1:])
    input_args = parse_input_args(sys.argv[1:])
    print("input_arg:",input_args)
    host=DEFAULT_PORT
    if not get_env('HOST'):
        os.environ.setdefault('HOST',host)
    
    _setup_env()
    _apply_database_migrations()

    if input_args.log_level:
        os.environ.setdefault("LOG_LEVEL", input_args.log_level)

    config = _get_config(input_args.config_path)

    from label_studio.core.utils.common import start_browser

    # from label_studio.core.utils.common import collect_versions
    # versions = collect_versions()
    
    if get_env('USERNAME') and get_env('PASSWORD'):
        _create_user(input_args, config)

    cert_file = input_args.cert_file or config.get('cert')
    key_file = input_args.key_file or config.get('key')
    if cert_file or key_file:
        logger.error("Label Studio doesn't support SSL web server with cert and key.\n"
                    'Use nginx or other servers for it.')
        return
    
    # internal port and internal host for server start
    internal_host = input_args.internal_host or config.get('internal_host', '0.0.0.0')  # nosec
    internal_port = input_args.port or get_env('PORT') or config.get('port', 8080)

    try:
        internal_port = int(internal_port)
    except ValueError as e:
        logger.warning(f"Can't parse PORT '{internal_port}': {e}; default value 8080 will be used")
        internal_port = 8080

    internal_port = _get_free_port(internal_port, input_args.debug)

    # save selected port to global settings
    from django.conf import settings
    settings.INTERNAL_PORT = str(internal_port)

    # browser
    url = ('http://localhost:' + str(internal_port)) if not host else host
    start_browser(url, no_browser=True)

    _app_run(host=internal_host, port=internal_port)

    


if __name__ == "main":
    run()