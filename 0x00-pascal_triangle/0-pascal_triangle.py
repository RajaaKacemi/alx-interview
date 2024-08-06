def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Generate the next row
        row = [1]  # Start with 1
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End with 1
        triangle.append(row)

    return triangle
