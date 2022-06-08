__name__    = "SUDOKU"
__version__ = "1.0"
__author__  = "Charles De Lafontaine (DaddyChucky)"
__license__ = "MIT"

import logging
import static.constants as globals
from random import randint
from copy import deepcopy


class Sudoku:
    """
    Class for Sudoku!

    Attributes
    ----------
    logger:         Logger
        The main file logger of Sudoku.
    slots:          list
        Slots of the Sudoku (count=81 in a normal Sudoku game).
    helpers:        list
        Helpers of the Sudoku (maximum 81 times 9 at the starting point).
    filled_indexes: list
        List of indexes fullfilled with a number.

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
            self.filled_indexes = []
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
    
    def generate_game(self) -> None:
        self.logger.debug('Entering Sudoku::generate_game')
        self.logger.info('Generating game matrixes')
        self.generate_slots_and_helpers()
        self.logger.debug('Leaving Sudoku::generate_game')
    
    def generate_slots_and_helpers(self) -> None:
        self.logger.debug('Entering Sudoku::generate_slots')
        self.logger.info('Generating slots and helpers')
        for _ in range(globals.N_SLOTS):
            self.slots.append(globals.NO_ENTRY)
            default_helpers_dc: list = deepcopy(globals.DEFAULT_HELPERS)
            self.helpers.append(default_helpers_dc)
            self.helpers_sizes.append(len(default_helpers_dc))
        self.logger.info('Done generating slots and helpers')
        self.logger.info('Attributes info:')
        self.logger.debug('Slots:')
        self.logger.debug(self.slots)
        self.logger.debug('Helpers:')
        self.logger.debug(self.helpers)
        self.logger.debug('Size of helpers:')
        self.logger.debug(self.helpers_sizes)
        self.logger.debug('Leaving Sudoku::generate_slots')
    
    def choose_random_slot(self) -> tuple:
        self.logger.debug('Entering Sudoku::choose_random_slot')

        self.logger.info('Choosing a random slot')
        helpers_min_indexes:    list    = []
        helpers_min_val:        int     = min(self.helpers_sizes)
        for i, helpers_size in enumerate(deepcopy(self.helpers_sizes)):
            if (helpers_size == helpers_min_val or helpers_size > globals.MIN_HELPERS_SIZE_BYPASS) and helpers_size != 0 and i not in self.filled_indexes:
                helpers_min_indexes.append(i)
        if len(helpers_min_indexes) - 1 == 0:
            self.generate_end_game()
            exit(-1)
        self.logger.info('Done choosing a random slot')
        self.logger.debug('Helpers min val:')
        self.logger.debug(helpers_min_val)
        self.logger.debug('Helpers min indexes:')
        self.logger.debug(helpers_min_indexes)
        self.logger.info('Choosing an index')
        print(len(helpers_min_indexes) - 1)
        print(helpers_min_indexes)
        chosen_helpers_min_index:               int     = randint(0, len(helpers_min_indexes) - 1)
        chosen_index:                           int     = helpers_min_indexes[chosen_helpers_min_index]
        helpers_at_chosen_slot_index:           list    = self.helpers[chosen_index]
        index_of_helper_at_chosen_slot_index:   int     = randint(0, len(helpers_at_chosen_slot_index) - 1)
        value_of_helper_at_chosen_slot_index:   int     = helpers_at_chosen_slot_index[index_of_helper_at_chosen_slot_index]
        self.logger.info('Done choosing an index')
        self.logger.info('Chosen helpers min index:')
        self.logger.info(chosen_helpers_min_index)
        self.logger.info('Helpers at chosen slot index:')
        self.logger.info(helpers_at_chosen_slot_index)
        self.logger.debug('Index of helper at chosen slot index:')
        self.logger.debug(index_of_helper_at_chosen_slot_index)
        self.logger.debug('Value of helper at chosen slot index:')
        self.logger.debug(value_of_helper_at_chosen_slot_index)
        self.logger.info('Updating helpers')
        self.update_game(chosen_index, value_of_helper_at_chosen_slot_index)
        self.logger.info('Done updating helpers')
        self.logger.debug('Leaving Sudoku::choose_random_slot')
        return chosen_index, value_of_helper_at_chosen_slot_index

    def update_game(self, chosen_slot_index: int, value_of_helper_at_chosen_slot_index: int) -> None:
        self.logger.debug('Entering Sudoku::update_helpers')
        self.logger.info('Updating filled indexes')
        self.filled_indexes.append(chosen_slot_index)
        self.logger.debug('Filled indexes:')
        self.logger.debug(self.filled_indexes)
        self.logger.info('Done updating filled indexes')
        self.logger.info('Updating row helpers')
        row_index: int = chosen_slot_index // globals.N_ROWS
        self.logger.debug('Row index:')
        self.logger.debug(row_index)
        min_row_range: int = row_index * (globals.N_ROWS)
        self.logger.debug('Min row range:')
        self.logger.debug(min_row_range)
        max_row_range: int = (row_index + 1) * (globals.N_ROWS) - 1
        self.logger.debug('Max row range:')
        self.logger.debug(max_row_range)
        for i in range(min_row_range, max_row_range + 1):
            if value_of_helper_at_chosen_slot_index not in self.helpers[i]:
                continue
            self.helpers[i].remove(value_of_helper_at_chosen_slot_index)
            self.helpers_sizes[i] -= 1
        self.logger.debug('Helpers:')
        self.logger.debug(self.helpers)
        self.logger.debug('Helpers sizes:')
        self.logger.debug(self.helpers_sizes)
        self.logger.info('Done updating row helpers')

        self.logger.info('Updating column helpers')
        self.logger.info('Done updating column helpers')

        self.logger.debug('Leaving Sudoku::update_helpers')
    
    def generate_end_game(self):
        self.logger.debug('Entering Sudoku::generate_end_game')
        self.logger.info('Player reached the end of the game')
        self.logger.debug('Leaving Sudoku::generate_end_game')

sudoku: Sudoku = Sudoku('logging.log', logging.DEBUG)
sudoku.play()
for i in range(80):
    sudoku.choose_random_slot()

