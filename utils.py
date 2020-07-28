import pandas as pd
import zipfile


def get_csv_head_inside_zip(zipfilename, csvfilename, sep=';', encoding='ISO-8859-1', nrows=0):
    dataset_head = None
    with zipfile.ZipFile(zipfilename) as file_zip:
        with file_zip.open(csvfilename) as csv:
            dataset_head = pd.read_csv(csv, sep=sep, encoding=encoding, nrows=nrows).columns.values
    return dataset_head


def open_csv_inside_zip(zipfilename, csvfilename, usecols=None, sep=';', encoding='ISO-8859-1', ):
    dataset = None
    with zipfile.ZipFile(zipfilename) as file_zip:
        with file_zip.open(csvfilename) as csv:
            if usecols:
                dataset = pd.read_csv(csv, sep=sep, encoding=encoding, usecols=usecols)
            else:
                dataset = pd.read_csv(csv, sep=sep, encoding=encoding)
    return dataset

def zip_analysis(zipfilename):
    with zipfile.ZipFile(zipfilename) as file_zip:
        print(*file_zip.namelist(), sep='\n')
