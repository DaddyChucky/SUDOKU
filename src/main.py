__name__    = "SUDOKU"
__version__ = "1.0"
__author__  = "Charles De Lafontaine (DaddyChucky)"
__license__ = "MIT"

import logging
import static.constants as globals


class Sudoku:
    """
    A class used to represent a Sudoku

    ...

    Attributes
    ----------
    attribute1 : TypeHere
    Description goes here

    Methods
    -------
    method(param1=TypeHere)
    Description goes here
    """

    def __init__(self, logging_file_name: str, logging_level) -> None:
        """
        Parameters
        ----------
        param1 : type
            Desc
        """
        try:
            logging.basicConfig(filename=logging_file_name, format=globals.DEFAULT_LOGGING_FORMAT, filemode=globals.DEFAULT_LOGGING_FILE_MODE)
            self.logger = logging.getLogger()
            self.logger.setLevel(logging_level)
            self.logger.debug('Entering Sudoku::__init__')
            self.logger.info('Logger successfully instantiated')
            self.logger.debug('Leaving Sudoku::__init__')
        except Exception as e:
            self.logger.exception(e)

    def play(self):
        """Application starting point by launching a fresh Sudoku game.

        Raises
        ------
        Exception
            Exception clause.
        """
        self.logger.debug('Entering Sudoku::play')



        self.logger.debug('Leaving Sudoku::play')

sudoku: Sudoku = Sudoku('logging.log', logging.DEBUG)
sudoku.play()
