from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    table = ""
    # elements used for border of the table
    frame = "│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘".split()
    vert = frame[0] # "|"
    hori = frame[1] # "─"
    upper = frame[2:5] # "┌, ┬, ┐"
    middle = frame[5:8] # "├, ┼, ┤"
    lower = frame[8:] # "└, ┴, ┘"
    
    rows_num = len(rows)
    cols_num = len(rows[0])

    # maximum width for each column including labels if needed
    col_width = []
    for col in range(cols_num):
        max_width = max([len(str(row[col])) for row in rows])
        if labels:
            max_width = max(max_width, len(str(labels[col])))
        col_width.append(max_width)

    # begin constructing table
    # upper border
    table += upper[0]
    for col in range(cols_num):
        # check the end of the row
        if col != cols_num-1:
            table += hori * (col_width[col]+2) + upper[1]
        else:
            table += hori * (col_width[col]+2) + upper[2]
    table += "\n"

    # optional one row of label
    if labels:
        table += vert
        if centered:           
            for col in range(cols_num):
                table += " " + str(labels[col]).center(col_width[col]) + " " + vert
        else:
            for col in range(cols_num):
                table += " " + str(labels[col]).ljust(col_width[col]) + " " + vert
        table += "\n"
        # lower border of labels
        table += middle[0]
        for col in range(cols_num):
            if col != cols_num-1:
                table += hori * (col_width[col]+2) + middle[1]
            else:
                table += hori * (col_width[col]+2) + middle[2]
        table += "\n"

    # add rows
    for row in range(rows_num):
        table += vert
        if centered:
            for col in range(cols_num):
                table += " " + str(rows[row][col]).center(col_width[col]) + " " + vert
        else:
            for col in range(cols_num):
                table += " " + str(rows[row][col]).ljust(col_width[col]) + " " + vert
        table += "\n"

    # lower border of table
    table += lower[0]
    for col in range(cols_num):
        if col != cols_num-1:
            table += hori * (col_width[col]+2) + lower[1]
        else:
            table += hori * (col_width[col]+2) + lower[2]

    return table
