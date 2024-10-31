def row_to_list(row):
    values = row.strip().split(';')
    if '' in values:
        return None
    return values
