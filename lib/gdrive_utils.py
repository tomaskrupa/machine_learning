import pandas as pd


def read_csv_from_gdrive(filename: str, project: str = None, variable_path: str = None):
    fixed_path = "/content/gdrive/MyDrive/"
    variable_path = variable_path if variable_path else "git_repos/machine_learning/projects/"
    file_path = fixed_path + variable_path + project + "/data/" + filename
    print(f"Reading data from {file_path}")
    return pd.read_csv(file_path)
