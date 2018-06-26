# encoding: utf-8


# 定义的全局变量
class GlobalVar:
    g_iAU1 = [4,
              17, -10, 30, -4,
              50, 10, 30, -4,
              15, -10, 0, 0,
              48, 10, 0, 0]

    g_iAU2 = [8,
              16, 0, 40, -5,
              49, 0, 40, -5,
              18, 0, 40, -2,
              51, 0, 40, -2,
              15, 5, 20, -2,
              48, -5, 20, -5,
              17, 0, 5, 0,
              50, 0, 5, 0]

    g_iAU1625 = [3,
                 40, 0, -60, 5,
                 8, 0, -50, -4,
                 9, 0, -20, -10]

    g_iAU27 = [ 8,
                40, 0, -60, -5,
                8, 0, -50, -4,
                9, 0, -30, -10,
                10, 0, -25, -10,
                30, 0, -25, -10,
                63, 0, -25, -5,
                32, 0, -25, -10,
                65, 0, -25, -10]

    g_iAU4 = [ 14,
               17, -20, -20, 0,
               50, 20, -20, 0,
               16, -20, -20, 4,
               49, 20, -20, 4,
               18, -20, -20, 4,
               51, 20, -20, 4,
               15, 0, -10, 0,
               48, 0, -10, 0,
               21, 0, -8, 0,
               54, 0, -8, 0,
               67, 0, -6, 0,
               69, 0, -6, 0,
               71, 0, -6, 0,
               73, 0, -6, 0]

    g_iAU9 = [ 19,
               5, 0, 20, -4,
               25, 0, 20, 0,
               58, 0, 20, 0,
               26, 0, 20, -4,
               59, 0, 20, -4,
               33, 0, 10, 0,
               66, 0, 10, 0,
               16, 0, -10, 0,
               49, 0, -10, 0,
               17, 0, -15, 0,
               50, 0, -15, 0,
               18, 0, -10, 0,
               51, 0, -10, 0,
               22, 0, 6, 0,
               55, 0, 6, 0,
               68, 0, 3, 0,
               70, 0, 3, 0,
               72, 0, 3, 0,
               74, 0, 3, 0 ]

    g_iAU10 = [ 7,
                7, 0, 20, 5,
                25, 0, -10, -2,
                58, 0, -10, -2,
                26, 0, -10, -2,
                59, 0, -10, -2,
                33, 0, 15, 5,
                66, 0, 15, 5]

    g_iAU20 = [9,
               8, 0, 14, -4,
               31, 20, 0, -20,
               64, -20, 0, -20,
               32, 10, -10, 0,
               65, -10, -10, 0,
               33, 0, -6, -6,
               66, 0, -6, -6,
               26, 7, 0, -2,
               59, 7, 0, -2]

    g_iAU12 = [ 12,
                31, 10, 30, -3,
                64, -10, 30, -3,
                25, 0, 10, -2,
                58, 0, 10, -2,
                26, 0, 10, -2,
                59, 0, 10, -2,
                22, 0, 4, 0,
                55, 0, 4, 0,
                68, 0, 2, 0,
                70, 0, 2, 0,
                72, 0, 2, 0,
                74, 0, 2, 0]

    g_iAU18 = [7,
               31, -60, -8, 60,
               64, 60, -8, 60,
               33, 0, 10, 10,
               66, 0, 10, 10,
               7, 0, 0, 10,
               40, 0, 0, 10,
               8, 0, 5, 10]

    g_iAU45 = [12,
               21, 0, -14, 4,
               54, 0, -14, 4,
               22, 0, 6, 4,
               55, 0, 6, 4,
               67, 0, -11, 0,
               69, 0, -11, 0,
               71, 0, -11, 0,
               73, 0, -11, 0,
               68, 0, 4, 0,
               70, 0, 4, 0,
               72, 0, 4, 0,
               74, 0, 4, 0]

    g_iAU17 = [ 4,
               9, 0, -30, 0,
               8, 0, -20, 0,
               7, 0, -15, 0,
               40, 0, -15, -10]

    g_fAU1 = 0.0
    g_fAU2 = 0.0
    g_fAU1625 = 0.0
    g_fAU27 = 0.0
    g_fAU4 = 0.0
    g_fAU9 = 0.0
    g_fAU10 = 0.0
    g_fAU20 = 0.0
    g_fAU12 = 0.0
    g_fAU18 = 0.0
    g_fAU45 = 0.0
    g_fAU17 = 0.0
    DEBUG_FLAG = 1
    g_bMesh = False

    g_Triangle = [
        [12, 11, 1], [11, 0, 1], [1, 0, 34], [0, 44, 34], [44, 45, 34],
        [34, 45, 46], [12, 1, 13], [14, 12, 13], [13, 1, 2], [1, 34, 2],

        [2, 34, 46], [46, 45, 47], [29, 14, 15], [14, 13, 15], [15, 13, 16],
        [13, 2, 16], [2, 46, 49], [49, 46, 48], [46, 47, 48], [48, 47, 62],

        [16, 2, 17], [17, 2, 3], [3, 2, 50], [50, 2, 49], [15, 16, 18],
        [16, 17, 18], [50, 49, 51], [49, 48, 51], [15, 18, 19], [18, 17, 19],

        [50, 51, 52], [52, 51, 48], [29, 15, 20], [15, 19, 20], [19, 17, 23],
        [23, 17, 4], [17, 3, 4], [3, 50, 4], [4, 50, 56], [50, 52, 56],

        [52, 48, 53], [53, 48, 62], [20, 19, 21], [19, 23, 21], [20, 21, 22],
        [21, 23, 22], [20, 22, 24], [22, 23, 24], [56, 52, 54], [52, 53, 54],

        [56, 54, 55], [54, 53, 55], [56, 55, 57], [55, 53, 57], [28, 29, 27],
        [29, 20, 27], [27, 20, 26], [20, 24, 26], [24, 25, 26], [24, 23, 25],

        [23, 4, 25], [25, 4, 5], [4, 58, 5], [4, 56, 58], [56, 57, 58],
        [58, 57, 59], [59, 57, 53], [59, 53, 60], [53, 62, 60], [60, 62, 61],

        [26, 25, 5], [26, 5, 6], [26, 6, 33], [33, 6, 7], [6, 66, 7],
        [6, 59, 66], [5, 59, 6], [5, 58, 59], [28, 27, 30], [27, 31, 30],

        [27, 26, 31], [26, 33, 31], [66, 59, 64], [59, 60, 64], [64, 60, 63],
        [60, 61, 63], [31, 33, 7], [31, 7, 8], [7, 66, 64], [7, 64, 8],

        [30, 31, 32], [30, 32, 10], [32, 9, 10], [31, 9, 32], [31, 8, 9],
        [8, 64, 9], [9, 64, 65], [9, 65, 10], [65, 64, 63], [10, 65, 63]]


def set_g_fAU1(g_fAU1):
        GlobalVar.g_fAU1 = g_fAU1


def get_g_fAU1():
        return GlobalVar.g_fAU1


def set_g_fAU2(g_fAU2):
        GlobalVar.g_fAU2 = g_fAU2


def get_g_fAU2():
        return GlobalVar.g_fAU2


def set_g_fAU1625(g_fAU1625):
        GlobalVar.g_fAU1625 = g_fAU1625


def get_g_fAU1625():
        return GlobalVar.g_fAU1625


def set_g_fAU27(g_fAU27):
        GlobalVar.g_fAU27 = g_fAU27


def get_g_fAU27():
        return GlobalVar.g_fAU27


def set_g_fAU4(g_fAU4):
        GlobalVar.g_fAU4 = g_fAU4


def get_g_fAU4():
        return GlobalVar.g_fAU4


def set_g_fAU9(g_fAU9):
        GlobalVar.g_fAU9 = g_fAU9


def get_g_fAU9():
        return GlobalVar.g_fAU9


def set_g_fAU10(g_fAU10):
        GlobalVar.g_fAU10 = g_fAU10


def get_g_fAU10():
        return GlobalVar.g_fAU10


def set_g_fAU20(g_fAU20):
        GlobalVar.g_fAU20 = g_fAU20


def get_g_fAU20():
        return GlobalVar.g_fAU20


def set_g_fAU12(g_fAU12):
        GlobalVar.g_fAU12 = g_fAU12


def get_g_fAU12():
        return GlobalVar.g_fAU12


def set_g_fAU18(g_fAU18):
        GlobalVar.g_fAU1 = g_fAU18


def get_g_fAU18():
        return GlobalVar.g_fAU18


def set_g_fAU45(g_fAU45):
        GlobalVar.g_fAU45 = g_fAU45


def get_g_fAU45():
        return GlobalVar.g_fAU45


def set_g_fAU17(g_fAU17):
        GlobalVar.g_fAU17 = g_fAU17


def get_g_fAU17():
        return GlobalVar.g_fAU17


def set_g_iAU1(g_iAU1):
        GlobalVar.g_iAU1 = g_iAU1


def get_g_iAU1():
        return GlobalVar.g_iAU1


def set_g_iAU2(g_iAU2):
        GlobalVar.g_iAU2 = g_iAU2


def get_g_iAU2():
        return GlobalVar.g_iAU2


def set_g_iAU1625(g_iAU1625):
        GlobalVar.g_iAU1625 = g_iAU1625


def get_g_iAU1625():
        return GlobalVar.g_iAU1625


def set_g_iAU27(g_iAU27):
        GlobalVar.g_iAU27 = g_iAU27


def get_g_iAU27():
        return GlobalVar.g_iAU27


def set_g_iAU4(g_iAU4):
        GlobalVar.g_iAU4 = g_iAU4


def get_g_iAU4():
        return GlobalVar.g_iAU4


def set_g_iAU9(g_iAU9):
        GlobalVar.g_iAU9 = g_iAU9


def get_g_iAU9():
        return GlobalVar.g_iAU9


def set_g_iAU10(g_iAU10):
        GlobalVar.g_iAU10 = g_iAU10


def get_g_iAU10():
        return GlobalVar.g_iAU10


def set_g_iAU20(g_iAU20):
        GlobalVar.g_iAU20 = g_iAU20


def get_g_iAU20():
        return GlobalVar.g_iAU20


def set_g_iAU12(g_iAU12):
        GlobalVar.g_iAU12 = g_iAU12


def get_g_iAU12():
        return GlobalVar.g_iAU12


def set_g_iAU18(g_iAU18):
        GlobalVar.g_iAU1 = g_iAU18


def get_g_iAU18():
        return GlobalVar.g_iAU18


def set_g_iAU45(g_iAU45):
        GlobalVar.g_iAU45 = g_iAU45


def get_g_iAU45():
        return GlobalVar.g_iAU45


def set_g_iAU17(g_iAU17):
        GlobalVar.g_iAU17 = g_iAU17


def get_g_iAU17():
        return GlobalVar.g_iAU17


def set_DEBUG_FLAG(DEBUG_FLAG):
        GlobalVar.DEBUG_FLAG = DEBUG_FLAG


def get_DEBUG_FLAG():
        return GlobalVar.DEBUG_FLAG


def set_g_bMesh(g_bMesh):
        GlobalVar.g_bMesh = g_bMesh


def get_g_bMesh():
        return GlobalVar.g_bMesh


def set_g_Triangle(g_Triangle):
        GlobalVar.g_Triangle = g_Triangle


def get_g_Triangle():
        return GlobalVar.g_Triangle