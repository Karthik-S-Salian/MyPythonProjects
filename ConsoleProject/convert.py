from math import sqrt

print("CONVERTER")
print("to convert temperature enter 'T'")
print("to convert length enter      'L'")
print("to find volume enter         'V'")
print("to find perimeter enter      'P'")
print("To find area enter           'A'")
fun = input("Enter the required unit to convert: ")
fun = fun.lower()
# TEMPERATURE
if fun == "t":
    print("CONVERSION OF TEMPERATURE INTO CELSIUS FAHRENHEIT & KELVIN")

    i_form = input("Enter the unit to be converted: ").lower()
    unit1 = i_form[0]
    f_form = input("convert into: ").lower()
    unit2 = f_form[0]

    value = float(input("Enter the value of : "))

    if unit1 == "c" and unit2 == "f":
        celsius = value
        fahrenheit = (((5.0 / 9.0) * celsius) + 32)
        print(str(value) + "C= " + str(fahrenheit) + "F")
    elif unit1 == "f" and unit2 == "c":
        fahrenheit = value
        celsius = (((9.0 / 5.0) * fahrenheit) - 32)
        print(str(value) + "F= " + str(celsius) + "C")
    elif unit1 == "c" and unit2 == "k":
        celsius = value
        kelvin = celsius + 273
        print(str(value) + "C= " + str(kelvin) + "K")
    elif unit1 == "f" and unit2 == "k":
        fahrenheit = value
        kelvin = ((((9.0 / 5.0) * fahrenheit) + 32) + 273)
        print(str(value) + "F=" + str(kelvin) + "K")
    elif unit1 == "k" and unit2 == "c":
        kelvin = value
        celsius = kelvin - 273
        print(str(value) + "K=" + str(celsius) + "C")
    elif unit1 == "k" and unit2 == "f":
        kelvin = value
        fahrenheit = ((5.0 / 9.0) * (kelvin + 273) + 32)
        print(str(value) + "K=" + str(fahrenheit) + "F")
    else:
        print("INVALID INPUT")


# LENGTH
elif fun == "l":
    print("CONVERSION OF LENGTH INTO KILOMETER, METER, CENTIMETER ,INCH ,MILE & FOOT")

    unit1 = input("Enter the unit to be converted: ")
    unit2 = input("convert into: ")
    unit1 = unit1.lower()
    unit2 = unit2.lower()
    value = float(input("Enter the value of " + unit1 + ": "))
    if unit1 == "kilometer" and unit2 == "meter":
        km = value
        mtr = km * 1000
        print(str(value) + "km= " + str(mtr) + " m")
    elif unit1 == "meter" and unit2 == "kilometer":
        mtr = value
        km = mtr / 1000
        print(str(value) + "m= " + str(km) + " km")
    elif unit1 == "centimeter" and unit2 == "meter":
        cn = value
        mtr = cn / 100
        print(str(value) + "cm= " + str(mtr) + " m")
    elif unit1 == "meter" and unit2 == "centimeter":
        mtr = value
        cn = mtr * 100
        print(str(value) + "m=" + str(cn) + " cm")
    elif unit1 == "kilometer" and unit2 == "centimeter":
        km = value
        cn = km * 100000
        print(str(value) + "km=" + str(cn) + " cm")
    elif unit1 == "centimeter" and unit2 == "kilometer":
        cn = value
        km = cn / 100000
        print(str(value) + "cm=" + str(km) + " km")
    elif unit1 == "foot" and unit2 == "inch":
        foot = value
        inch = foot * 12
        print(str(value) + "f=" + str(inch) + " inch")
    elif unit1 == "inch" and unit2 == "foot":
        inch = value
        foot = inch / 12.0
        print(str(value) + "inch=" + str(foot) + " f")
    elif unit1 == "inch" and unit2 == "meter":
        inch = value
        meter = inch * 0.0254
        print(str(value) + "inch=" + str(meter) + " m")
    elif unit1 == "meter" and unit2 == "inch":
        meter = value
        inch = meter / 0.0254
        print(str(value) + "m=" + str(inch) + " inch")
    elif unit1 == "mile" and unit2 == "kilometer":
        mile = value
        km = mile * 1.602
        print(str(value) + "mile=" + str(km) + " km")
    elif unit1 == "kilometer" and unit2 == "mile":
        km = value
        mile = km / 1.602
        print(str(value) + "km=" + str(km) + " mile")
    elif unit1 == "yard" and unit2 == "centimeter":
        yard = value
        cm = yard * 91.44
        print(str(value) + "yard=" + str(cm) + " cm")
    elif unit1 == "centimeter" and unit2 == "yard":
        cm = value
        yard = cm / 91.44
        print(str(value) + "cm=" + str(yard) + " yard")
    else:
        print("INVALID INPUT")

# VOLUME
elif fun == "v":
    solid = input("Enter the solid: ")
    solid = solid.lower()
    if solid == "cube":
        value = float(input("Enter the length of side: "))
        vol = value ** 3
        print("the volume of cube=" + str(vol) + " m3")
    elif solid == "cuboid":
        value = float(input("Enter the length: "))
        value2 = float(input("Enter the breadth: "))
        value3 = float(input("Enter the height: "))
        vol = value * value2 * value3
        print("The volume of cuboid =" + str(vol) + " m3")
    elif solid == "sphere":
        value = float(input("Enter the length of radius: "))
        vol = ((4.0 / 3.0) * (value ** 3) * 3.14)
        print("the volume of sphere =" + str(vol) + " m3")
    elif solid == "cylinder":
        value = float(input("Enter the length of radius: "))
        value2 = float(input("Enter the value of height: "))
        vol = 3.14 * (value ** 2) * value2
        print("the volume of cylinder =" + str(vol) + " m3")
    elif solid == "hemisphere":
        value = float(input("Enter the length of radius: "))
        vol = ((2.0 / 3.0) * (value ** 3) * 3.14)
        print("the volume of hemisphere=" + str(vol) + " m3")
    elif solid == "cone":
        value = float(input("Enter the length of radius: "))
        value2 = float(input("Enter the value of height: "))
        vol = (1.0 / 3.0) * 3.14 * (value ** 2) * value2
        print("the volume of cone =" + str(vol) + " m3")
    else:
        print("INVALID INPUT")

# PERIMETER
elif fun == "p":
    shp = input("Enter the shape: ")
    shp = shp.lower()
    if shp == "square":
        value = float(input("Enter the length of side: "))
        pm = value * 4
        print("The perimeter of square = " + str(pm) + " m")
    elif shp == "rectangle":
        value = float(input("Enter the length: "))
        value2 = float(input("Enter the breadth: "))
        pm = (value + value2) * 2
        print("The perimeter of rectangle = " + str(pm) + " m")
    elif shp == "circle":
        value = float(input("Enter the length of radius: "))
        pm = 3.14 * value * 2
        print("The perimeter of square = " + str(pm) + " m")
    elif shp == "triangle":
        value = float(input("Enter the length of one side: "))
        value2 = float(input("Enter the length of 2nd side: "))
        value3 = float(input("Enter the length of 3rd side: "))
        pm = value + value2 + value3
        print("The perimeter of triangle = " + str(pm) + " m")
    elif shp == "parallelogram":
        value = float(input("Enter the length : "))
        value2 = float(input("Enter the height : "))
        pm = 2 * (value + value2)
        print("The perimeter of triangle = " + str(pm) + " m")
    elif shp == "rhombus":
        value = float(input("Enter the value of side: "))
        rhombus = 4 * value
        print("The perimeter of rhombus = " + str(rhombus) + " m")
    else:
        print("INVALID INPUT")

# AREA
elif fun == "a":
    shape = input("Enter the shape")
    shape = shape.lower()
    if shape == "square":
        value = float(input("Enter the length of side: "))
        sqr = value ** 2
        print("The area of square = " + str(sqr) + " m2")
    elif shape == "rectangle":
        value = float(input("Enter the length: "))
        value2 = float(input("Enter the breadth: "))
        rectangle = value * value2
        print("The area of rectangle = " + str(rectangle) + "m2")
    elif shape == "circle":
        value = float(input("Enter the length of radius: "))
        circle = (value ** 2) * 3.14
        print("The area of circle = " + str(circle) + " m2")
    elif shape == "triangle":
        value = float(input("Enter the length of one side: "))
        value2 = float(input("Enter the length of 2nd side: "))
        value3 = float(input("Enter the length of 3rd side: "))
        hp = (value + value2 + value3) / 2
        triangle = sqrt(hp * ((hp - value) * (hp - value2) * (hp - value3)))
        print("The area of triangle = " + str(triangle) + " m2")
    elif shape == "parallelogram":
        value = float(input("Enter the length : "))
        value2 = float(input("Enter the height : "))
        parallelogram = value * value2
        print("The area of parallelogram = " + str(parallelogram) + " m2")
    elif shape == "rhombus":
        value = float(input("Enter the length of diagonal: "))
        value2 = float(input("Enter the length of another diagonal: "))
        rhombus = 0.5 * value * value2
        print("The area of rhombus =" + str(rhombus) + " m2")
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
