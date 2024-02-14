import time
from rich import print
import random

def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.01)
        # time.sleep(0)
    print()

def print_quickly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.005)
        # time.sleep(0)
    print()

def descision():
    return random.random() < 0.50



