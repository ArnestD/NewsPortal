import logging
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

logging.basicConfig(level=logging.INFO, filename="general.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logging.basicConfig(level=logging.error, filename="errors.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logging.basicConfig(level=logging.error, filename="security.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")

logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")