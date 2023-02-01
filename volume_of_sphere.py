def calculate_volume_of_sphere(radius):
    pi = 3.14
    v = (4/3)*pi*radius*radius*radius
    return v

def main():
    radius1 = 30
    volume1 = calculate_volume_of_sphere(radius1)
    print(f"The volume of a sphere with a radius of {radius1} is: {volume1}")


    

    radius2 = 40
    volume2 = calculate_volume_of_sphere(radius2)
    print(f"The volume of a sphere with a radius of {radius2} is: {volume2}")

main()
