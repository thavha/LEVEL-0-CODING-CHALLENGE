def area_of_a_triangle(length1, length2, length3):

    semi_perimeter = (length1 + length2 + length3) / 2

    area = (
        semi_perimeter
        * (semi_perimeter - length1)
        * (semi_perimeter - length2)
        * (semi_perimeter - length3)
    ) ** 0.5

    return area