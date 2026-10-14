# SciPy Constants
#
# Constants in SciPy
# As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.
# These constants can be helpful when you are working with Data Science.
#
# PI is an example of a scientific constant.

from scipy import constants

print("pi =", constants.pi)
input("Press <ENTER> to continue...")

print(dir(constants))
input("Press <ENTER> to continue...")

# Unit Categories:
#
# - Metric
# - Binary
# - Mass
# - Angle
# - Time
# - Length
# - Pressure
# - Volume
# - Speed
# - Temperature
# - Energy
# - Power
# - Force

# Metric (SI) Prefixes:
# Return the specified unit in meter (e.g. centi returns 0.01)
print("Metric Prefixes")
print(constants.yotta)    #1e+24
print(constants.zetta)    #1e+21
print(constants.exa)      #1e+18
print(constants.peta)     #1000000000000000.0
print(constants.tera)     #1000000000000.0
print(constants.giga)     #1000000000.0
print(constants.mega)     #1000000.0
print(constants.kilo)     #1000.0
print(constants.hecto)    #100.0
print(constants.deka)     #10.0
print(constants.deci)     #0.1
print(constants.centi)    #0.01
print(constants.milli)    #0.001
print(constants.micro)    #1e-06
print(constants.nano)     #1e-09
print(constants.pico)     #1e-12
print(constants.femto)    #1e-15
print(constants.atto)     #1e-18
print(constants.zepto)    #1e-21
input("Press <ENTER> to continue...")

# Binary Prefixes:
# Return the specified unit in bytes (e.g. kibi returns 1024)
print("Binary Prefixes")
print(constants.kibi)    #1024
print(constants.mebi)    #1048576
print(constants.gibi)    #1073741824
print(constants.tebi)    #1099511627776
print(constants.pebi)    #1125899906842624
print(constants.exbi)    #1152921504606846976
print(constants.zebi)    #1180591620717411303424
print(constants.yobi)    #1208925819614629174706176
input("Press <ENTER> to continue...")

# Mass:
# Return the specified unit in kg (e.g. gram returns 0.001)
print("Mass Constants")
print(constants.gram)        #0.001
print(constants.metric_ton)  #1000.0
print(constants.grain)       #6.479891e-05
print(constants.lb)          #0.45359236999999997
print(constants.pound)       #0.45359236999999997
print(constants.oz)          #0.028349523124999998
print(constants.ounce)       #0.028349523124999998
print(constants.stone)       #6.3502931799999995
print(constants.long_ton)    #1016.0469088
print(constants.short_ton)   #907.1847399999999
print(constants.troy_ounce)  #0.031103476799999998
print(constants.troy_pound)  #0.37324172159999996
print(constants.carat)       #0.0002
print(constants.atomic_mass) #1.66053904e-27
print(constants.m_u)         #1.66053904e-27
print(constants.u)           #1.66053904e-27
input("Press <ENTER> to continue...")

# Angle:
# Return the specified unit in radians (e.g. degree returns 0.017453292519943295)
print("Angular Constants")
print(constants.degree)     #0.017453292519943295
print(constants.arcmin)     #0.0002908882086657216
print(constants.arcminute)  #0.0002908882086657216
print(constants.arcsec)     #4.84813681109536e-06
print(constants.arcsecond)  #4.84813681109536e-06
input("Press <ENTER> to continue...")

# Time:
# Return the specified unit in seconds (e.g. hour returns 3600.0)
print("Time Constants")
print(constants.minute)      #60.0
print(constants.hour)        #3600.0
print(constants.day)         #86400.0
print(constants.week)        #604800.0
print(constants.year)        #31536000.0
print(constants.Julian_year) #31557600.0
input("Press <ENTER> to continue...")

# Length:
# Return the specified unit in meters (e.g. nautical_mile returns 1852.0)
print("Distance Constants")
print(constants.inch)              #0.0254
print(constants.foot)              #0.30479999999999996
print(constants.yard)              #0.9143999999999999
print(constants.mile)              #1609.3439999999998
print(constants.mil)               #2.5399999999999997e-05
print(constants.pt)                #0.00035277777777777776
print(constants.point)             #0.00035277777777777776
print(constants.survey_foot)       #0.3048006096012192
print(constants.survey_mile)       #1609.3472186944373
print(constants.nautical_mile)     #1852.0
print(constants.fermi)             #1e-15
print(constants.angstrom)          #1e-10
print(constants.micron)            #1e-06
print(constants.au)                #149597870691.0
print(constants.astronomical_unit) #149597870691.0
print(constants.light_year)        #9460730472580800.0
print(constants.parsec)            #3.0856775813057292e+16
input("Press <ENTER> to continue...")

# Pressure:
# Return the specified unit in pascals (e.g. psi returns 6894.757293168361)
print("Pressure Constants")
print(constants.atm)         #101325.0
print(constants.atmosphere)  #101325.0
print(constants.bar)         #100000.0
print(constants.torr)        #133.32236842105263
print(constants.mmHg)        #133.32236842105263
print(constants.psi)         #6894.757293168361
input("Press <ENTER> to continue...")

# Area:
# Return the specified unit in square meters(e.g. hectare returns 10000.0)
print("Area Constants")
print(constants.hectare) #10000.0
print(constants.acre)    #4046.8564223999992
input("Press <ENTER> to continue...")

# Volume:
# Return the specified unit in cubic meters (e.g. liter returns 0.001)
print("Volume Constants")
print(constants.liter)            #0.001
print(constants.litre)            #0.001
print(constants.gallon)           #0.0037854117839999997
print(constants.gallon_US)        #0.0037854117839999997
print(constants.gallon_imp)       #0.00454609
print(constants.fluid_ounce)      #2.9573529562499998e-05
print(constants.fluid_ounce_US)   #2.9573529562499998e-05
print(constants.fluid_ounce_imp)  #2.84130625e-05
print(constants.barrel)           #0.15898729492799998
print(constants.bbl)              #0.15898729492799998
input("Press <ENTER> to continue...")

# Speed:
# Return the specified unit in meters per second (e.g. speed_of_sound returns 340.5)
print("Speed Constants")
print(constants.kmh)            #0.2777777777777778
print(constants.mph)            #0.44703999999999994
print(constants.mach)           #340.5
print(constants.speed_of_sound) #340.5
print(constants.knot)           #0.5144444444444445
input("Press <ENTER> to continue...")

# Temperature:
# Return the specified unit in Kelvin (e.g. zero_Celsius returns 273.15)
print("Temperature Constants")
print(constants.zero_Celsius)      #273.15
print(constants.degree_Fahrenheit) #0.5555555555555556
input("Press <ENTER> to continue...")

# Energy:
# Return the specified unit in joules (e.g. calorie returns 4.184)
print("Energy Constants")
print(constants.eV)            #1.6021766208e-19
print(constants.electron_volt) #1.6021766208e-19
print(constants.calorie)       #4.184
print(constants.calorie_th)    #4.184
print(constants.calorie_IT)    #4.1868
print(constants.erg)           #1e-07
print(constants.Btu)           #1055.05585262
print(constants.Btu_IT)        #1055.05585262
print(constants.Btu_th)        #1054.3502644888888
print(constants.ton_TNT)       #4184000000.0
input("Press <ENTER> to continue...")

# Power:
# Return the specified unit in watts (e.g. horsepower returns 745.6998715822701)
print("Energy Constants")
print(constants.hp)         #745.6998715822701
print(constants.horsepower) #745.6998715822701
input("Press <ENTER> to continue...")

# Force:
# Return the specified unit in newton (e.g. kilogram_force returns 9.80665)
print("Force Constants")
print(constants.dyn)             #1e-05
print(constants.dyne)            #1e-05
print(constants.lbf)             #4.4482216152605
print(constants.pound_force)     #4.4482216152605
print(constants.kgf)             #9.80665
print(constants.kilogram_force)  #9.80665
