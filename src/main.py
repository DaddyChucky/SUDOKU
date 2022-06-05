__name__    = "SUDOKU"
__version__ = "1.0"
__author__  = "Charles De Lafontaine (DaddyChucky)"
__license__ = "MIT"

import logging
import static.constants as globals


class Sudoku:
    """
    Class for Sudoku!

    Attributes
    ----------
    logger: Logger
        The main file logger of Sudoku.
    slots: list
        Slots of the Sudoku (count=81 in a normal Sudoku game).
    helpers: list
        Helpers of the Sudoku (maximum 81 times 9 at the starting point).

    Methods
    -------
    __init__(logging_file_name: str, logging_level: Function)
    play()
    """

    def __init__(self, logging_file_name: str, logging_level) -> None:
        """ Initializes the Sudoku class.

        Parameters
        ----------
        logging_file_name : str
            File name of the logging file, including its type (preferably .log).
        logging_level : Function
            Logging level to be displayed in the logging file (please refer to the Logging module documentation).
        
        Raises
        ------
        Exception
            Any exception caused by the Logging module upon initialization of the Logger.
        """
        try:
            logging.basicConfig(filename=logging_file_name, format=globals.DEFAULT_LOGGING_FORMAT, filemode=globals.DEFAULT_LOGGING_FILE_MODE)
            self.logger = logging.getLogger()
            self.logger.setLevel(logging_level)
            self.logger.debug('Entering Sudoku::__init__')
            self.logger.info('Logger successfully instantiated')
            self.logger.info('Initializing attributes')
            self.slots          = []
            self.helpers        = []
            self.helpers_sizes  = []
            self.logger.info('Done initializing attributes')
            self.logger.info('Attributes info:')
            self.logger.info('Slots:')
            self.logger.info(self.slots)
            self.logger.info('Helpers:')
            self.logger.info(self.helpers)
            self.logger.info('Size of helpers:')
            self.logger.info(self.helpers_sizes)
            self.logger.debug('Leaving Sudoku::__init__')
        except Exception as e:
            self.logger.exception(e)

    def play(self):
        """Launches a fresh Sudoku game.

        Raises
        ------
        Exception
            Any exception non catched by function calls.
        """
        try:
            self.logger.debug('Entering Sudoku::play')
            self.generate_game()
            self.logger.debug('Leaving Sudoku::play')
        except Exception as e:
            self.logger.exception(e)
    
    def generate_game(self):
        self.logger.debug('Entering Sudoku::generate_game')

        self.logger.info('Generating game matrixes')
        self.generate_slots_and_helpers()

        self.logger.debug('Leaving Sudoku::generate_game')
    
    def generate_slots_and_helpers(self):
        self.logger.debug('Entering Sudoku::generate_slots')

        self.logger.info('Generating slots and helpers')
        for _ in range(globals.N_SLOTS):
            self.slots.append(globals.NO_ENTRY)
            self.helpers.append(globals.DEFAULT_HELPERS)
            self.helpers_sizes.append(len(globals.DEFAULT_HELPERS))
        self.logger.info('Done generating slots and helpers')
        self.logger.info('Attributes info:')
        self.logger.info('Slots:')
        self.logger.info(self.slots)
        self.logger.info('Helpers:')
        self.logger.info(self.helpers)
        self.logger.info('Size of helpers:')
        self.logger.info(self.helpers_sizes)
        self.logger.debug('Leaving Sudoku::generate_slots')


sudoku: Sudoku = Sudoku('logging.log', logging.DEBUG)
sudoku.play()
