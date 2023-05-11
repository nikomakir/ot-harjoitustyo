import os
from dotenv import load_dotenv


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

SUDOKU_FILENAME = os.getenv("SUDOKU_FILENAME") or "sudoku.csv"
SUDOKU_FILEPATH = os.path.join(dirname, "..", "data", SUDOKU_FILENAME)
DIFFICULTY_FILENAME = os.getenv("DIFFICULTY_FILENAME") or "difficulty.csv"
DIFFICULTY_FILEPATH = os.path.join(dirname, "..", "data", DIFFICULTY_FILENAME)
