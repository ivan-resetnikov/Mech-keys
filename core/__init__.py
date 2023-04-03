import logging
open('crash.log', 'w').close()
logging.basicConfig(filename='crash.log', encoding='utf-8', level=logging.DEBUG)

import core.sound as sound
import core.theme as theme