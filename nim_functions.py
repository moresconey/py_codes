# Functions created by Ney Moresco - neymoresco@hotmail.com
# Create: 2020-09-14
# Last Update: --

# Clear strings (Only Numbers)
def clear_string(number:str):
    number = ''.join(e for e in number if e.isdigit())
    return number

# Clear Columns in Data Frame (Remove Special Characters)
def clear_df_columns(df):
    for column in df.columns:
        df[column] = df[column].str.replace(r'\W', "")
    return df

# Copy Text or Image to Clipboard
def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    if clip_type == 'text':
        win32clipboard.SetClipboardText(data, win32clipboard.CF_TEXT)
    else:
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

# Loading image on Memory
def read_imagem(file_dir:str):
    image = Image.open(file_dir)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    img_data = output.getvalue()[14:]
    output.close()
    return img_data

