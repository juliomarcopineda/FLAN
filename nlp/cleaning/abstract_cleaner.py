#!/usr/bin/env python

"""
clean_abstract.py: Cleans abstract data from NIH projects to prepare the data
for natural langauge processing.
"""

__author__ = "Julio Pineda"

import pandas as pd


def main():
    data = pd.read_csv("~/flan/FLAN/nlp/data/RePORTER_PRJABS_C_FY2018_009.csv")
    sample = data['ABSTRACT_TEXT'][0]

    cleaner = AbstractCleaner(sample)
    cleaner.to_lower_case()

    print(cleaner.text)


class AbstractCleaner:
    def __init__(self, text):
        self.text = text

    def to_lower_case(self):
        self.text = self.text.lower()


if __name__ == '__main__':
    main()
