"""Main method for CHIRP (Used when compiled)."""

# Standard Python Libraries
import logging
from multiprocessing import freeze_support
import os
import sys
import time

# cisagov Libraries
from chirp import run
from chirp.common import OUTPUT_DIR, save_log, wait

if __name__ == "__main__":
    try:
        freeze_support()
        run.run()
        time.sleep(2)
        logging.log(
            70,
            "DONE! Your results can be found in {}.".format(
                os.path.abspath(OUTPUT_DIR)
            ),
        )
        wait()
        save_log()
        sys.exit(0)
    except KeyboardInterrupt:
        logging.error("Received an escape sequence. Goodbye.")
        save_log()
        sys.exit(0)
