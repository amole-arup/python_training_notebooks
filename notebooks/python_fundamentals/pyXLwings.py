"""Example functions for use with xlwings"""

import xlwings as xw


def hello_xlwings():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


@xw.func
@xw.arg('Name', doc='This is the name for use in the greeting.')
def hello(name):
    return "hello {0}".format(name)


@xw.sub
def get_workbook_name():
    """Writes the name of the Workbook into Range("D3") of Sheet 1"""
    wb = xw.Book.caller()
    wb.sheets['Sheet1'].range('D3').value = wb.name


@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)


@xw.func
@xw.arg('data', ndim=2)
def add_one(data):
    """Adds 1 to every cell in Range"""
    return [[cell + 1 for cell in row] for row in data]


@xw.func
def myTriple(x):
    """Triple my number"""
    return 3 * x



# ------------------------------------------------------
#  Hong Kong Concrete Code added functions
#-------------------------------------------------------

# Note that only the HKConcStress function is exposed to Excel

def e_cu(f_cu):
   if f_cu < 60.0:
      return 0.0035
   else: 
      return (0.0035 - 0.00006 * (f_cu - 60.0)**0.5)


def eMod_d(f_cu):
    """Concrete modulus of stiffness - a function "eMod_d" that takes one parameter "f_cu" in MPa"""
    return 1000.0 * (3.46 * (f_cu/1.5)**0.5 + 3.21)


def e_c0(f_cu):
    """Concrete strain at max stress - a function 'ec_0' that takes one parameter 'f_cu'
    but also references a function 'eMod_d' - this is functional programming"""
    return (1.34 * f_cu) / 1.5 / (eMod_d(f_cu))


def f_max(f_cu):
    """Concrete maximum stress - a function 'f_max' that takes one parameter 'f_cu'"""
    return 0.67 * f_cu / 1.5


@xw.func
def HKConcStress(s,f_cu):
    """Returns concrete stress for any concrete strain according to HK codes (2015)
    - this function has two parameters, strain 's' and concrete cube strength (f_cu), and uses functions 'e_cu', 'e_c0' & 'f_max' """
    if s <= 0.0: 
        r = 0.0
    elif s < (e_c0(f_cu)): 
        r = 1.0 - (s / (e_c0(f_cu)) - 1.0)**2.0
    elif s < (e_cu(f_cu)): 
        r = 1.0
    else: 
        r = 0.0
    return (f_max(f_cu) * r)

#===============================================    
#  EC8 added functions
#===============================================

# Table 3.2: Values of the parameters describing the recommended Type 1 elastic response spectra
gparams1 = {"Ground Type":["S","T_B","T_C","T_D"],
            "A":[1.0,0.15,0.4,2.0],
            "B":[1.2,0.15,0.5,2.0],
            "C":[1.15,0.20,0.6,2.0],
            "D":[1.35,0.20,0.8,2.0],
            "E":[1.4,0.15,0.5,2.0]}

# Table 3.3: Values of the parameters describing the recommended Type 2 elastic response spectra
gparams2 = {"Ground Type":["S","T_B","T_C","T_D"],
            "A":[1.0,0.05,0.25,1.2],
            "B":[1.35,0.05,0.25,1.2],
            "C":[1.5,0.10,0.25,1.2],
            "D":[1.8,0.10,0.30,1.2],
            "E":[1.6,0.05,0.25,1.2]}

gparams = (gparams1,gparams2)

# Table 3.4 Recommended values of parameters descripbing the vertical elastic response spectra
vparams = {"Spectrum":["a_vg/a_g","T_B","T_C","T_D"],
            "Type_1":[0.9,0.05,0.15,1.0],
            "Type_2":[0.45,0.05,0.15,1.0]}

gparamsMS = {"Ground Type":["S","T_B","T_C","T_D"],
            "R":[1.0,0.15,0.4,2.0],
            "SS":[1.2,0.15,0.5,2.0],
            "FS":[1.15,0.20,0.6,2.0]}


# 3.2.2.3(1)P Malaysia NDP Table 3.4 Recommended values of parameters descripbing the vertical elastic response spectra
vparamsMS = {"Spectrum":["a_vg/a_g","T_B","T_C","T_D"],
            "Type_2":[0.70,0.05,0.15,1.0]}

            
@xw.func
def EC8_eta(xi=5.0):
    """damping correction factor"""
    return max(0.55,(10/(5+xi))**0.5)


@xw.func
def EC8_S(soil="B",eqtype=2):
    """3.2.2.2(2)P Tables 3.2 & 3.3 Soil Factor"""
    return gparams[eqtype-1][soil][0]


@xw.func
def EC8_T_B(soil="B",eqtype=2):
    """3.2.2.2(2)P Tables 3.2 & 3.3 Lower limit of constant spectral acceleration"""
    return gparams[eqtype-1][soil][1]


@xw.func
def EC8_T_C(soil="B",eqtype=2):
    """3.2.2.2(2)P Tables 3.2 & 3.3 Upper limit of constant spectral acceleration"""
    return gparams[eqtype-1][soil][2]


@xw.func
def EC8_T_D(soil="B",eqtype=2):
    """3.2.2.2(2)P Tables 3.2 & 3.3 Beginning of constant displacement range"""
    return gparams[eqtype-1][soil][3]


@xw.func
def EC8_S_e(T,a_g,soil="B",xi=5.0, eqtype=2):
    """3.2.2.2 Horizontal elastic response spectrum"""
    S = gparams[eqtype-1][soil][0]
    T_B = gparams[eqtype-1][soil][1]
    T_C = gparams[eqtype-1][soil][2]
    T_D = gparams[eqtype-1][soil][3]
    if T <= 0:
        S_e1 = a_g
    elif T <= T_B:
        S_e1 = a_g * S * (1 + T/T_B * (EC8_eta(xi)*2.5 - 1))
    elif T <= T_C:
        S_e1 = a_g * S * EC8_eta(xi) * 2.5
    elif T <= T_D:
        S_e1 = a_g * S * EC8_eta(xi) * 2.5 * (T_C / T)
    elif T <= 4:
        S_e1 = a_g * S * EC8_eta(xi) * 2.5 * (T_C * T_D / T**2)
    else:
        S_e1 = -99999
    return S_e1


@xw.func
def EC8_S_d(T,a_g,q=1.0,soil="B",xi=5.0, eqtype=2, beta=0.2):
    """3.2.2.2 Horizontal elastic response spectrum"""
    S = gparams[eqtype-1][soil][0]
    T_B = gparams[eqtype-1][soil][1]
    T_C = gparams[eqtype-1][soil][2]
    T_D = gparams[eqtype-1][soil][3]
    if T <= 0:
        S_d1 = a_g
    elif T <= T_B:
        S_d1 = a_g * S * (2/3 + T/T_B * (2.5/q - 2/3))
    elif T <= T_C:
        S_d1 = a_g * S * 2.5 / q
    elif T <= T_D:
        S_d1 = a_g * max(beta, S * 2.5 / q * (T_C / T))
    else:
        S_d1 = a_g * max(beta, S * 2.5 /q * (T_C * T_D / T**2))
    return S_d1


@xw.func
def EC8_S_ve(T,a_g,xi=5.0, eqtype=2):
    """3.2.2.2 Horizontal elastic response spectrum"""
    av_a = vparams["Type"+str(eqtype)][0]
    T_B = vparams["Type"+str(eqtype)][1]
    T_C = vparams["Type"+str(eqtype)][2]
    T_D = vparams["Type"+str(eqtype)][3]
    if T <= 0:
        S_v = av_a * a_g
    elif T <= T_B:
        S_v = av_a * a_g * (1 + T/T_B * (EC8_eta(xi) * 3.0 - 1))
    elif T <= T_C:
        S_v = av_a * a_g * EC8_eta(xi) * 3.0
    elif T <= T_D:
        S_v = av_a * a_g * EC8_eta(xi)* 3.0 * (T_C / T)
    elif T <= 4:
        S_v = av_a * a_g * EC8_eta(xi)* 3.0 * (T_C * T_D / T**2)
    else:
        S_v = -99999
    return S_v


@xw.func
def EC8_d_g(a_g,S,T_C,T_D):
    """3.2.2.4(1) Design ground displacement"""
    return 0.025 * a_g * S * T_C * T_D


@xw.func
def EC8_F_b(S_d,m,lmbda=1.0):
    """4.3.3.2.2(1)P Base shear force"""
    return (S_d * m * lmbda)


@xw.func
def EC8_T_1(C_t,H):
    """4.3.3.2.2(3) Approximate building period"""
    return C_t * H**0.75
