def area_of_a_triangle(height, base, length):
    semi_perimeter = (height +base + length)/2
    
    return (semi_perimeter*(semi_perimeter - height)*(semi_perimeter - base)*(semi_perimeter-length))** 0.5