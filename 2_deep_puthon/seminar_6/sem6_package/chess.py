def check_queens(crd: list[tuple]):
    """
    Пересечение ферзей
    crd: координаты восьми ферзей
    """
    for i in range(8):
        for j in range(i + 1, 8):
            row1, col1 = crd[i]
            row2, col2 = crd[j]
            if row1 == row2 or col1 == col2:
                return False
    return True
