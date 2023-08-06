import faker
import pandas as pd
import pyperclip

def replicate_cliboard():
    # get the clipboard
    clipboard = pyperclip.paste()
    # get the clipboard as a list of lines
    clipboard_list = clipboard.splitlines()
    
    # split into columns based on \t
    clipboard_list = [line.split('\t') for line in clipboard_list]
    
    # convert to pandas dataframe
    df = pd.DataFrame(clipboard_list)
    
    # replace make the header column the first row
    df.columns = df.iloc[0]
    df = df.reindex(df.index.drop(0))
    
    return df


def generate_fake_data(n_lines, template, delimiter):
    df = replicate_cliboard()
    print(df)