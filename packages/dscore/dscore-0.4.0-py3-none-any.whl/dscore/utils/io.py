from pathlib import Path
import pandas as pd
import re

from tabulate import tabulate


def as_csv(df):
    df = df.replace(True, 1)
    df = df.replace(False, 0)
    return df.infer_objects().to_csv(sep=' ')


def as_dscore(df):
    # header
    # D and - are more readable than True and False
    df = df.replace(True, 'D')
    df = df.replace(False, '-')
    header = [f'# {0}. {df.index.name}']
    for i, col_name in enumerate(df.columns):
        header.append(f'# {i + 1}. {col_name}')
    header = '\n'.join(header)
    # tabulated data
    tabulated = tabulate(df, headers=range(len(df.columns) + 1))
    text = header + '\n' + tabulated
    return text


def save_file(text, path):
    path = Path(path)
    if path.exists():
        bak = path.with_suffix(path.suffix + '.bak')
        path.rename(bak)
    with open(path, 'w+') as f:
        f.write(text)


def write_dscore(df, name, savepath):
    dscore = as_dscore(df)
    path = savepath / (name + '.dscore')
    save_file(dscore, path)


def write_csv(df, name, savepath):
    csv = as_csv(df)
    path = savepath / (name + '.csv')
    save_file(csv, path)


def read_dscore(dscore_or_csv):
    path = Path(dscore_or_csv)
    with open(dscore_or_csv, 'r') as f:
        if path.suffix == '.dscore':
            columns = []
            while True:
                line = f.readline()
                if match := re.match('# \d+\. (.*)$', line):
                    columns.append(match.group(1))
                elif line.startswith('-'):
                    break
            df = pd.read_csv(f, sep='\s+', names=columns)
            df.iloc[:, 2:] = df.iloc[:, 2:].replace('-', False)
            df.iloc[:, 2:] = df.iloc[:, 2:].replace('D', True)
        else:
            df = pd.read_csv(path, sep=' ')
            df.iloc[:, 2:] = df.iloc[:, 2:].replace(0, False)
            df.iloc[:, 2:] = df.iloc[:, 2:].replace(1, True)

    # make sure to use float and not object
    df['dscore'] = df['dscore'].astype(float)
    return df
