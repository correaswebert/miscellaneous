"""
Column Aligner Program

This program aligns the columns given as input, either center align, or left, 
or right align. Columns are rendered with whitespaces from leftmost to 
rightmost. The maximum length word is the whitespace template.
"""

# currently only for right/left align
def adjustColumn(columns):
    whitespace_columns = []

    # calculate the amount of whitespace needed per word for padding
    for col in columns:
        max_word_len = 0    # max word length in the column
        words_len = []      # word length for each row of that column
        whitespaces = []    # whitespaces needed to adjust

        for word in col:
            word_len = len(word)
            words_len.append(word_len)
            max_word_len = word_len if word_len > max_word_len else max_word_len
        
        for word_len in words_len:
            whitespaces.append(max_word_len - word_len)
        whitespace_columns.append(whitespaces)

    return whitespace_columns

# assumes all entries of table are filled
def extractTableColumns(table):
    columns = []
    num_rows = len(table)
    num_cols = len(table[0])
    for col in range(num_cols):
        col_data = []
        for row in range(num_rows):
            col_data.append(str(table[row][col]))
        columns.append(col_data)
    return columns

def renderOutput(text_columns, whitespace_columns):
    num_rows = len(text_columns)    # columns are rows of text_columns
    num_cols = len(text_columns[0]) # columns are rows of whitespace_columns
    for col in range(num_cols):
        for row in range(num_rows):
            word = text_columns[row][col]
            padding = ' ' * whitespace_columns[row][col]
            print(padding, word, end=' ')
        print()

def csvExtractor(filename):
    import csv
    
    table = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
        for row in reader:
            table.append(row)
    return table

if __name__ == "__main__":
    table = csvExtractor('column_data.txt')
    text = extractTableColumns(table)
    whitespace = adjustColumn(text)
    renderOutput(text, whitespace)