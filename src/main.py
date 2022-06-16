__name__ = "SUDOKU"
__version__ = "1.0"
__author__ = "Charles De Lafontaine (DaddyChucky)"
__license__ = "MIT"

import logging
import static.constants as globs
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
            logging.basicConfig(filename=logging_file_name, format=globs.DEFAULT_LOGGING_FORMAT,
                                filemode=globs.DEFAULT_LOGGING_FILE_MODE)
            self.logger = logging.getLogger()
            self.logger.setLevel(logging_level)
            self.logger.debug('Entering Sudoku::__init__')
            self.logger.debug('Logger successfully instantiated')
            self.logger.debug('Initializing attributes')
            self.slots: list = []
            self.helpers: list = []
            self.helpers_sizes: list = []
            self.filled_indexes: list = []
            self.board: dict = dict()
            self.logger.debug('Done initializing attributes')
            self.logger.debug('Attributes info:')
            self.logger.debug('Slots:')
            self.logger.debug(self.slots)
            self.logger.debug('Helpers:')
            self.logger.debug(self.helpers)
            self.logger.debug('Size of helpers:')
            self.logger.debug(self.helpers_sizes)
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
            for _ in range(globs.N_ROWS * globs.N_COLUMNS):
                self.choose_random_slot()
            self.draw_board()
            self.logger.debug('Leaving Sudoku::play')
        except Exception as e:
            self.logger.exception(e)

    def generate_game(self) -> None:
        self.logger.debug('Entering Sudoku::generate_game')
        self.logger.debug('Generating game matrixes')
        self.generate_slots_and_helpers()
        self.logger.debug('Leaving Sudoku::generate_game')

    def generate_slots_and_helpers(self) -> None:
        self.logger.debug('Entering Sudoku::generate_slots_and_helpers')
        self.logger.debug('Generating slots and helpers')
        for _ in range(globs.N_SLOTS):
            self.slots.append(globs.NO_ENTRY)
            default_helpers_dc: list = deepcopy(globs.DEFAULT_HELPERS)
            self.helpers.append(default_helpers_dc)
            self.helpers_sizes.append(len(default_helpers_dc))
        self.logger.debug('Done generating slots and helpers')
        self.logger.debug('Attributes info:')
        self.logger.debug('Slots:')
        self.logger.debug(self.slots)
        self.logger.debug('Helpers:')
        self.logger.debug(self.helpers)
        self.logger.debug('Size of helpers:')
        self.logger.debug(self.helpers_sizes)
        self.logger.debug('Leaving Sudoku::generate_slots_and_helpers')

    def choose_random_slot(self) -> tuple:
        self.logger.debug('Entering Sudoku::choose_random_slot')
        self.logger.debug('Choosing a random slot')
        helpers_min_indexes: list = []
        for i, helpers_size in enumerate(deepcopy(self.helpers_sizes)):
            if helpers_size >= globs.MIN_HELPERS_SIZE_BYPASS and i not in self.filled_indexes:
                helpers_min_indexes.append(i)
        if len(helpers_min_indexes) == 0:
            self.generate_end_game()
        self.logger.debug('Done choosing a random slot')
        self.logger.debug('Helpers min indexes:')
        self.logger.debug(helpers_min_indexes)
        self.logger.debug('Choosing an index')
        chosen_helpers_min_index: int = randint(0, len(helpers_min_indexes) - 1)
        chosen_index: int = helpers_min_indexes[chosen_helpers_min_index]
        helpers_at_chosen_slot_index: list = self.helpers[chosen_index]
        index_of_helper_at_chosen_slot_index: int = randint(0, len(helpers_at_chosen_slot_index) - 1)
        value_of_helper_at_chosen_slot_index: int = helpers_at_chosen_slot_index[index_of_helper_at_chosen_slot_index]
        self.logger.debug('Done choosing an index: ' + str(chosen_index) + ' with value of ' + str(value_of_helper_at_chosen_slot_index))
        self.logger.debug('Updating board')
        self.update_board(chosen_index, value_of_helper_at_chosen_slot_index)
        self.logger.debug('Done updating board')
        self.logger.debug('Chosen helpers min index:')
        self.logger.debug(chosen_helpers_min_index)
        self.logger.debug('Helpers at chosen slot index:')
        self.logger.debug(helpers_at_chosen_slot_index)
        self.logger.debug('Index of helper at chosen slot index:')
        self.logger.debug(index_of_helper_at_chosen_slot_index)
        self.logger.debug('Updating helpers')
        self.update_game(chosen_index, value_of_helper_at_chosen_slot_index)
        self.logger.debug('Done updating helpers')
        self.logger.debug('Leaving Sudoku::choose_random_slot')
        return chosen_index, value_of_helper_at_chosen_slot_index

    def update_game(self, chosen_slot_index: int, value_of_helper_at_chosen_slot_index: int) -> None:
        self.logger.debug('Entering Sudoku::update_game')
        self.logger.debug('Updating filled indexes')
        self.filled_indexes.append(chosen_slot_index)
        self.logger.debug('Filled indexes:')
        self.logger.debug(self.filled_indexes)
        self.logger.debug('Done updating filled indexes')
        self.logger.debug('Updating row helpers')
        row_index: int = chosen_slot_index // globs.N_ROWS
        self.logger.debug('Row index:')
        self.logger.debug(row_index)
        min_row_range: int = row_index * globs.N_ROWS
        self.logger.debug('Min row range:')
        self.logger.debug(min_row_range)
        max_row_range: int = (row_index + 1) * globs.N_ROWS - 1
        self.logger.debug('Max row range:')
        self.logger.debug(max_row_range)
        for i in range(min_row_range, max_row_range + 1):
            self.update_helpers(i, value_of_helper_at_chosen_slot_index)
        self.logger.debug('Helpers:')
        self.logger.debug(self.helpers)
        self.logger.debug('Helpers sizes:')
        self.logger.debug(self.helpers_sizes)
        self.logger.debug('Done updating row helpers')
        self.logger.debug('Updating column helpers')
        self.logger.debug('Updating columns above')
        i = chosen_slot_index + globs.N_ROWS
        while i <= globs.N_COLUMNS * globs.N_ROWS - 1:
            self.update_helpers(i, value_of_helper_at_chosen_slot_index)
            i += globs.N_ROWS
        self.logger.debug('Updating columns below')
        i = chosen_slot_index - 9
        while i >= 0:
            self.update_helpers(i, value_of_helper_at_chosen_slot_index)
            i -= globs.N_ROWS
        self.logger.debug('Done updating column helpers')
        self.logger.debug('Updating squares')
        self.logger.debug('Done updating squares')
        self.logger.debug('Leaving Sudoku::update_game')

    def update_helpers(self, i: int, value_of_helper_at_chosen_slot_index: int) -> None:
        if value_of_helper_at_chosen_slot_index not in self.helpers[i]:
            return
        self.helpers[i].remove(value_of_helper_at_chosen_slot_index)
        self.helpers_sizes[i] -= 1

    def generate_end_game(self) -> None:
        self.logger.debug('Entering Sudoku::generate_end_game')
        self.logger.debug('Leaving Sudoku::generate_end_game')

    def update_board(self, chosen_index: int, value_of_helper_at_chosen_slot_index: int) -> None:
        self.logger.debug('Entering Sudoku::update_board')
        self.board[chosen_index] = value_of_helper_at_chosen_slot_index
        self.logger.debug('Leaving Sudoku::update_board')

    def draw_board(self) -> None:
        self.logger.debug('Entering Sudoku::draw_board')
        temp_keys: list = []
        for key in sorted(self.board.keys()):
            if key % globs.N_ROWS == 0 and key != 0:
                print(str(temp_keys).replace(',', ' '), '\n')
                temp_keys.clear()
            temp_keys.append(self.board[key])
        self.logger.debug('Leaving Sudoku::draw_board')


sudoku: Sudoku = Sudoku('logging.log', logging.DEBUG)
sudoku.play()
