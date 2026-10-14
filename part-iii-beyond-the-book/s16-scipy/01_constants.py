"""SciPy Constants"""

from scipy import constants as sc
from utilities import clear_terminal, pause

def metric_constants() -> None:
    """Display metric prefix constants."""
    clear_terminal()
    print("Metric Constants:")
    print("----------------")
    print("quetta:", sc.quetta)    #1e+30
    print("ronna: ", sc.ronna)     #1e+27
    print("yotta: ", sc.yotta)     #1e+24
    print("zetta: ", sc.zetta)     #1e+21
    print("exa:   ", sc.exa)       #1e+18
    print("peta:  ", sc.peta)      #1000000000000000.0
    print("tera:  ", sc.tera)      #1000000000000.0
    print("giga:  ", sc.giga)      #1000000000.0
    print("mega:  ", sc.mega)      #1000000.0
    print("kilo:  ", sc.kilo)      #1000.0
    print("hecto: ", sc.hecto)     #100.0
    print("deka:  ", sc.deka)      #10.0
    print("deci:  ", sc.deci)      #0.1
    print("centi: ", sc.centi)     #0.01
    print("milli: ", sc.milli)     #0.001
    print("micro: ", sc.micro)     #1e-06
    print("nano:  ", sc.nano)      #1e-09
    print("pico:  ", sc.pico)      #1e-12
    print("femto: ", sc.femto)     #1e-15
    print("atto:  ", sc.atto)      #1e-18
    print("zepto: ", sc.zepto)     #1e-21
    print("yocto: ", sc.yocto)     #1e-24
    print("ronto: ", sc.ronto)     #1e-27
    print("quecto:", sc.quecto)    #1e-30
    pause()

def binary_constants() -> None:
    """Display binary prefix constants."""
    clear_terminal()
    print("Binary Constants:")
    print("----------------")
    print("kibi:", sc.kibi)    #1024
    print("mebi:", sc.mebi)    #1048576
    print("gibi:", sc.gibi)    #1073741824
    print("tebi:", sc.tebi)    #1099511627776
    print("pebi:", sc.pebi)    #1125899906842624
    print("exbi:", sc.exbi)    #1152921504606846976
    print("zebi:", sc.zebi)    #1180591620717411303424
    print("yobi:", sc.yobi)    #1208925819614629174706176
    pause()

def mass_constants() -> None:
    """Display mass constants."""
    clear_terminal()
    print("Mass Constants (in kg):")
    print("----------------------")
    print("gram:       ", sc.gram)        #0.001
    print("metric_ton: ", sc.metric_ton)  #1000.0
    print("grain:      ", sc.grain)       #6.479891e-05
    print("lb:         ", sc.lb)          #0.45359236999999997
    print("pound:      ", sc.pound)       #0.45359236999999997
    print("blob:       ", sc.blob)        #
    print("slinch:     ", sc.slinch)      #
    print("slug:       ", sc.slug)        #
    print("oz:         ", sc.oz)          #0.028349523124999998
    print("ounce:      ", sc.ounce)       #0.028349523124999998
    print("stone:      ", sc.stone)       #6.3502931799999995
    print("long_ton:   ", sc.long_ton)    #1016.0469088
    print("short_ton:  ", sc.short_ton)   #907.1847399999999
    print("troy_ounce: ", sc.troy_ounce)  #0.031103476799999998
    print("troy_pound: ", sc.troy_pound)  #0.37324172159999996
    print("carat:      ", sc.carat)       #0.0002
    print("atomic_mass:", sc.atomic_mass) #1.66053904e-27
    print("m_u:        ", sc.m_u)         #1.66053904e-27
    print("u:          ", sc.u)           #1.66053904e-27
    pause()

def angular_constants() -> None:
    """Display angular constants."""
    clear_terminal()
    print("Angular Constants (in rad):")
    print("--------------------------")
    # Values in radians
    print("degree:   ", sc.degree)     #0.017453292519943295
    print("arcmin:   ", sc.arcmin)     #0.0002908882086657216
    print("arcminute:", sc.arcminute)  #0.0002908882086657216
    print("arcsec:   ", sc.arcsec)     #4.84813681109536e-06
    print("arcsecond:", sc.arcsecond)  #4.84813681109536e-06
    pause()

def time_constants() -> None:
    """Display time constants."""
    clear_terminal()
    print("Time Constants (in sec):")
    print("-----------------------")
    print("minute:     ", sc.minute)      #60.0
    print("hour:       ", sc.hour)        #3600.0
    print("day:        ", sc.day)         #86400.0
    print("week:       ", sc.week)        #604800.0
    print("year:       ", sc.year)        #31536000.0
    print("Julian_year:", sc.Julian_year) #31557600.0
    pause()

def distance_constants() -> None:
    """Display distance constants."""
    clear_terminal()
    print("Distance Constants (in m):")
    print("-------------------------")
    print("inch:             ", sc.inch)              #0.0254
    print("foot:             ", sc.foot)              #0.30479999999999996
    print("yard:             ", sc.yard)              #0.9143999999999999
    print("mile:             ", sc.mile)              #1609.3439999999998
    print("mil:              ", sc.mil)               #2.5399999999999997e-05
    print("pt:               ", sc.pt)                #0.00035277777777777776
    print("point:            ", sc.point)             #0.00035277777777777776
    print("survey_foot:      ", sc.survey_foot)       #0.3048006096012192
    print("survey_mile:      ", sc.survey_mile)       #1609.3472186944373
    print("nautical_mile:    ", sc.nautical_mile)     #1852.0
    print("fermi:            ", sc.fermi)             #1e-15
    print("angstrom:         ", sc.angstrom)          #1e-10
    print("micron:           ", sc.micron)            #1e-06
    print("au:               ", sc.au)                #149597870691.0
    print("astronomical_unit:", sc.astronomical_unit) #149597870691.0
    print("light_year:       ", sc.light_year)        #9460730472580800.0
    print("parsec:           ", sc.parsec)            #3.0856775813057292e+16
    pause()

def pressure_constants() -> None:
    """Display pressure constants."""
    clear_terminal()
    print("Pressure Constants (in Pa):")
    print("--------------------------")
    print("atm:       ", sc.atm)         #101325.0
    print("atmosphere:", sc.atmosphere)  #101325.0
    print("bar:       ", sc.bar)         #100000.0
    print("torr:      ", sc.torr)        #133.32236842105263
    print("mmHg:      ", sc.mmHg)        #133.32236842105263
    print("psi:       ", sc.psi)         #6894.757293168361
    pause()

def area_constants() -> None:
    """Display area constants."""
    clear_terminal()
    print("Area Constants (in m²):")
    print("----------------------")
    print("hectare:", sc.hectare) #10000.0
    print("acre:   ", sc.acre)    #4046.8564223999992
    pause()

def volume_constants():
    """Display volume constants."""
    clear_terminal()
    print("Volume Constants (in m³):")
    print("------------------------")
    print("liter:           ", sc.liter)            #0.001
    print("litre:           ", sc.litre)            #0.001
    print("gallon:          ", sc.gallon)           #0.0037854117839999997
    print("gallon_US:       ", sc.gallon_US)        #0.0037854117839999997
    print("gallon_imp:      ", sc.gallon_imp)       #0.00454609
    print("fluid_ounce:     ", sc.fluid_ounce)      #2.9573529562499998e-05
    print("fluid_ounce_US:  ", sc.fluid_ounce_US)   #2.9573529562499998e-05
    print("fluid_ounce_imp: ", sc.fluid_ounce_imp)  #2.84130625e-05
    print("barrel:          ", sc.barrel)           #0.15898729492799998
    print("bbl:             ", sc.bbl)              #0.15898729492799998
    pause()

def speed_constants() -> None:
    """Display speed constants."""
    clear_terminal()
    print("Speed Constants (in m/s):")
    print("----------------------")
    print("kmh:           ", sc.kmh)            #0.2777777777777778
    print("mph:           ", sc.mph)            #0.44703999999999994
    print("mach:          ", sc.mach)           #340.5
    print("speed_of_sound:", sc.speed_of_sound) #340.5
    print("knot:          ", sc.knot)           #0.5144444444444445
    print("speed_of_light:", sc.speed_of_light) #299792458.0
    print("c:             ", sc.c)              #299792458.0
    pause()
    
def temperature_constants() -> None:
    """Display temperature constants."""
    clear_terminal()
    print("Temperature Constants (in K):")
    print("----------------------------")
    print("zero_Celsius      ", sc.zero_Celsius)      #273.15
    print("degree_Fahrenheit:", sc.degree_Fahrenheit) #0.5555555555555556
    pause()

def energy_constants() -> None:
    """Display energy constants."""
    clear_terminal()
    print("Energy Constants (in J):")
    print("-----------------------")
    print("eV:           ", sc.eV)            #1.6021766208e-19
    print("electron_volt:", sc.electron_volt) #1.6021766208e-19
    print("calorie:      ", sc.calorie)       #4.184
    print("calorie_th:   ", sc.calorie_th)    #4.184
    print("calorie_IT:   ", sc.calorie_IT)    #4.1868
    print("erg:          ", sc.erg)           #1e-07
    print("Btu:          ", sc.Btu)           #1055.05585262
    print("Btu_IT:       ", sc.Btu_IT)        #1055.05585262
    print("Btu_th:       ", sc.Btu_th)        #1054.3502644888888
    print("ton_TNT:      ", sc.ton_TNT)       #4184000000.0
    pause()

def power_constants() -> None:
    """Display power constants."""
    clear_terminal()
    print("Power Constants (in W):")
    print("------------------------")
    print("hp:        ", sc.hp)         #745.6998715822701
    print("horsepower:", sc.horsepower) #745.6998715822701
    pause()

def force_constants() -> None:
    """Display force constants"""
    clear_terminal()
    print("Force Constants (in N):")
    print("----------------------")
    print("dyn:           ", sc.dyn)             #1e-05
    print("dyne:          ", sc.dyne)            #1e-05
    print("lbf:           ", sc.lbf)             #4.4482216152605
    print("pound_force:   ", sc.pound_force)     #4.4482216152605
    print("kgf:           ", sc.kgf)             #9.80665
    print("kilogram_force:", sc.kilogram_force)  #9.80665
    pause()

def math_constants() -> None:
    """Display mathematical constants."""
    clear_terminal()
    print("Mathematical Constants:")
    print("----------------------")
    print("pi:           ", sc.pi)              #3.141592653589793
    print("golden:       ", sc.golden)          #1.618033988749895
    print("golden_ratio: ", sc.golden_ratio)    #1.618033988749895
    pause(end=True)

def main() -> None:
    """Display all constants."""
    metric_constants()
    binary_constants()
    mass_constants()
    angular_constants()
    time_constants()
    distance_constants()
    pressure_constants()
    area_constants()
    volume_constants()
    speed_constants()
    temperature_constants()
    energy_constants()
    power_constants()
    force_constants()
    math_constants()

if __name__ == "__main__":
    main()
