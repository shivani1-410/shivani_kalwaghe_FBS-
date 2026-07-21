# Convert distant given in feet and inches into meter and centimeter.
feet = float(input ("enter the feet:"))
inches = float(input("enter the inches:"))
total_inches=feet*12+inches
meters=total_inches*0.0254
centimeter=total_inches*2.54

print("Distance in Meters:",meters)
print("Distance in Centimeter:",centimeter)


