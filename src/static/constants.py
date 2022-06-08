import logging

DEFAULT_LOGGING_FORMAT:     str     = '%(asctime)s %(message)s'
DEFAULT_LOGGING_FILE_MODE:  str     = 'w'
DEFAULT_LOGGING_FILE_NAME:  str     = 'logging.log'
DEFAULT_LOGGING_LEVEL               = logging.DEBUG
N_COLUMNS:                  int     = 9
N_ROWS:                     int     = N_COLUMNS
N_SLOTS:                    int     = N_COLUMNS * N_ROWS
DEFAULT_HELPERS:            list    = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
NO_ENTRY:                   int     = 0
MIN_HELPERS_SIZE_BYPASS:    int     = 1
SQUARES_OFFSETS:            dict    = {
    0:  [10, 11, 19, 20],
    1:  [9, 11, 18, 20],
    2:  [9, 10, 18, 19],
    3:  [13, 14, 22, 23],
    4:  [12, 14, 21, 23],
    5:  [12, 13, 21, 22],
    6:  [16, 17, 25, 26],
    7:  [15, 17, 24, 26],
    8:  [15, 16, 24, 25],
    9:  [1, 2, 19, 20],
    10: [0, 2, 18, 20],
    11: []

}
