from flask_script import Manager
from flask_script import Command
import logging.config

# instantiate the app object
app = Flask(__name__)
# get config values
# 1. first get config values from config.py
#    (defaults and values that do not need override)
app.config.from_pyfile('config.py')
# 2. read overrides from local_config.py
#    (ignore failure, file may not be there)
try:
    app.config.from_pyfile('local_config.py')
except IOError:
    app.logger.warning("Could not load local_config.py")
logging.config.dictConfig(
        app.config['LOGGING']
    )
# instantiate the manager object
manager = Manager(app)
# implementation of supported commands
class SubmitDOIs(Command):
    """
    Retrieves DOI data and decides that to do
    """

    def run(self):
        # Get DOI data and do stuff

# definition of commands supported
manager.add_command('submit_dois', SubmitDOIs())

if __name__ == "__main__":
    manager.run()
