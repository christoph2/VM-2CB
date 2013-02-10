#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import vm_al as v

CALC_INT_INT     = 0
CALC_INT_LONG    = 1
CALC_INT_FLOAT   = 2
CALC_LONG_INT    = 3
CALC_LONG_LONG   = 4
CALC_LONG_FLOAT  = 5
CALC_FLOAT_INT   = 6
CALC_FLOAT_LONG  = 7
CALC_FLOAT_FLOAT = 8

mem = v.byteArray(64)
v.setRAMPointer(mem)

class TestVM_Sub_IntInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushW(rhs)
        v.VM_Sub()
        res = v.VM_PopW()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-21098, 25404), 19034, "")

    def test0001(self):
        self.assertEquals(self.calculate(-25148, 22711), 17677, "")

    def test0002(self):
        self.assertEquals(self.calculate(-1508, 30710), -32218, "")

    def test0003(self):
        self.assertEquals(self.calculate(12673, -2789), 15462, "")

    def test0004(self):
        self.assertEquals(self.calculate(22442, -7910), 30352, "")

    def test0005(self):
        self.assertEquals(self.calculate(-3071, -6980), 3909, "")

    def test0006(self):
        self.assertEquals(self.calculate(6553, 21737), -15184, "")

    def test0007(self):
        self.assertEquals(self.calculate(8839, 27698), -18859, "")

    def test0008(self):
        self.assertEquals(self.calculate(-27927, -6235), -21692, "")

    def test0009(self):
        self.assertEquals(self.calculate(-1111, 7211), -8322, "")

    def test0010(self):
        self.assertEquals(self.calculate(-13258, 32117), 20161, "")

    def test0011(self):
        self.assertEquals(self.calculate(12362, -2287), 14649, "")

    def test0012(self):
        self.assertEquals(self.calculate(-13104, -26318), 13214, "")

    def test0013(self):
        self.assertEquals(self.calculate(-28322, 32144), 5070, "")

    def test0014(self):
        self.assertEquals(self.calculate(-28250, 6461), 30825, "")

    def test0015(self):
        self.assertEquals(self.calculate(13039, 7845), 5194, "")

    def test0016(self):
        self.assertEquals(self.calculate(3414, 26242), -22828, "")

    def test0017(self):
        self.assertEquals(self.calculate(14300, -26927), -24309, "")

    def test0018(self):
        self.assertEquals(self.calculate(4357, -29122), -32057, "")

    def test0019(self):
        self.assertEquals(self.calculate(9553, 23406), -13853, "")

    def test0020(self):
        self.assertEquals(self.calculate(-32493, 7937), 25106, "")

    def test0021(self):
        self.assertEquals(self.calculate(3552, 18045), -14493, "")

    def test0022(self):
        self.assertEquals(self.calculate(28701, -9517), -27318, "")

    def test0023(self):
        self.assertEquals(self.calculate(-16925, 11526), -28451, "")

    def test0024(self):
        self.assertEquals(self.calculate(-9157, -16477), 7320, "")

    def test0025(self):
        self.assertEquals(self.calculate(32224, -31364), -1948, "")

    def test0026(self):
        self.assertEquals(self.calculate(3801, 15288), -11487, "")

    def test0027(self):
        self.assertEquals(self.calculate(-7230, -1616), -5614, "")

    def test0028(self):
        self.assertEquals(self.calculate(19657, 7092), 12565, "")

    def test0029(self):
        self.assertEquals(self.calculate(-29341, 5721), 30474, "")

    def test0030(self):
        self.assertEquals(self.calculate(-5189, 21305), -26494, "")

    def test0031(self):
        self.assertEquals(self.calculate(11201, 9422), 1779, "")

    def test0032(self):
        self.assertEquals(self.calculate(-29495, -21085), -8410, "")

    def test0033(self):
        self.assertEquals(self.calculate(9103, 18398), -9295, "")

    def test0034(self):
        self.assertEquals(self.calculate(26469, 12673), 13796, "")

    def test0035(self):
        self.assertEquals(self.calculate(-18586, 14500), 32450, "")

    def test0036(self):
        self.assertEquals(self.calculate(16444, -29473), -19619, "")

    def test0037(self):
        self.assertEquals(self.calculate(22052, -18190), -25294, "")

    def test0038(self):
        self.assertEquals(self.calculate(-18510, 16203), 30823, "")

    def test0039(self):
        self.assertEquals(self.calculate(15277, -9479), 24756, "")

    def test0040(self):
        self.assertEquals(self.calculate(-27668, -28641), 973, "")

    def test0041(self):
        self.assertEquals(self.calculate(19611, -12979), 32590, "")

    def test0042(self):
        self.assertEquals(self.calculate(-16747, -18960), 2213, "")

    def test0043(self):
        self.assertEquals(self.calculate(13191, -1079), 14270, "")

    def test0044(self):
        self.assertEquals(self.calculate(-10043, -21357), 11314, "")

    def test0045(self):
        self.assertEquals(self.calculate(-12763, -21343), 8580, "")

    def test0046(self):
        self.assertEquals(self.calculate(12939, -9764), 22703, "")

    def test0047(self):
        self.assertEquals(self.calculate(351, 31479), -31128, "")

    def test0048(self):
        self.assertEquals(self.calculate(27972, 2105), 25867, "")

    def test0049(self):
        self.assertEquals(self.calculate(25423, 15424), 9999, "")

    def test0050(self):
        self.assertEquals(self.calculate(20311, -16551), -28674, "")

    def test0051(self):
        self.assertEquals(self.calculate(-18686, -12500), -6186, "")

    def test0052(self):
        self.assertEquals(self.calculate(-12163, 8297), -20460, "")

    def test0053(self):
        self.assertEquals(self.calculate(-2511, -5547), 3036, "")

    def test0054(self):
        self.assertEquals(self.calculate(-31574, -27213), -4361, "")

    def test0055(self):
        self.assertEquals(self.calculate(11586, -15626), 27212, "")

    def test0056(self):
        self.assertEquals(self.calculate(-3746, -19942), 16196, "")

    def test0057(self):
        self.assertEquals(self.calculate(-3103, -5636), 2533, "")

    def test0058(self):
        self.assertEquals(self.calculate(14931, -19161), -31444, "")

    def test0059(self):
        self.assertEquals(self.calculate(12574, -7103), 19677, "")

    def test0060(self):
        self.assertEquals(self.calculate(-32694, 11914), 20928, "")

    def test0061(self):
        self.assertEquals(self.calculate(20739, 8207), 12532, "")

    def test0062(self):
        self.assertEquals(self.calculate(28142, -25689), -11705, "")

    def test0063(self):
        self.assertEquals(self.calculate(17630, 27427), -9797, "")

    def test0064(self):
        self.assertEquals(self.calculate(15753, -21308), -28475, "")

    def test0065(self):
        self.assertEquals(self.calculate(18828, -12689), 31517, "")

    def test0066(self):
        self.assertEquals(self.calculate(-26477, 18068), 20991, "")

    def test0067(self):
        self.assertEquals(self.calculate(28465, -9228), -27843, "")

    def test0068(self):
        self.assertEquals(self.calculate(20739, 8000), 12739, "")

    def test0069(self):
        self.assertEquals(self.calculate(2895, 23859), -20964, "")

    def test0070(self):
        self.assertEquals(self.calculate(24565, 28631), -4066, "")

    def test0071(self):
        self.assertEquals(self.calculate(-17753, 31619), 16164, "")

    def test0072(self):
        self.assertEquals(self.calculate(-23935, -22892), -1043, "")

    def test0073(self):
        self.assertEquals(self.calculate(-26569, -3764), -22805, "")

    def test0074(self):
        self.assertEquals(self.calculate(-24478, -21970), -2508, "")

    def test0075(self):
        self.assertEquals(self.calculate(6898, 1117), 5781, "")

    def test0076(self):
        self.assertEquals(self.calculate(-19272, -6947), -12325, "")

    def test0077(self):
        self.assertEquals(self.calculate(-15199, 26302), 24035, "")

    def test0078(self):
        self.assertEquals(self.calculate(-27053, 2439), -29492, "")

    def test0079(self):
        self.assertEquals(self.calculate(-3938, -18765), 14827, "")

    def test0080(self):
        self.assertEquals(self.calculate(-25581, 9947), 30008, "")

    def test0081(self):
        self.assertEquals(self.calculate(24066, 775), 23291, "")

    def test0082(self):
        self.assertEquals(self.calculate(-16065, 24682), 24789, "")

    def test0083(self):
        self.assertEquals(self.calculate(17467, 28190), -10723, "")

    def test0084(self):
        self.assertEquals(self.calculate(1461, 29820), -28359, "")

    def test0085(self):
        self.assertEquals(self.calculate(11094, 18240), -7146, "")

    def test0086(self):
        self.assertEquals(self.calculate(-26266, 31872), 7398, "")

    def test0087(self):
        self.assertEquals(self.calculate(-25868, -22832), -3036, "")

    def test0088(self):
        self.assertEquals(self.calculate(-3220, 3894), -7114, "")

    def test0089(self):
        self.assertEquals(self.calculate(-18537, 17365), 29634, "")

    def test0090(self):
        self.assertEquals(self.calculate(10332, 1196), 9136, "")

    def test0091(self):
        self.assertEquals(self.calculate(-20990, -3890), -17100, "")

    def test0092(self):
        self.assertEquals(self.calculate(-32345, -31119), -1226, "")

    def test0093(self):
        self.assertEquals(self.calculate(7817, 25002), -17185, "")

    def test0094(self):
        self.assertEquals(self.calculate(4408, -30497), -30631, "")

    def test0095(self):
        self.assertEquals(self.calculate(-2221, 18745), -20966, "")

    def test0096(self):
        self.assertEquals(self.calculate(21781, 31917), -10136, "")

    def test0097(self):
        self.assertEquals(self.calculate(13477, -2313), 15790, "")

    def test0098(self):
        self.assertEquals(self.calculate(22606, 3991), 18615, "")

    def test0099(self):
        self.assertEquals(self.calculate(19741, -25569), -20226, "")

    def test0100(self):
        self.assertEquals(self.calculate(15283, -6020), 21303, "")

    def test0101(self):
        self.assertEquals(self.calculate(-15234, -29735), 14501, "")

    def test0102(self):
        self.assertEquals(self.calculate(4935, -22706), 27641, "")

    def test0103(self):
        self.assertEquals(self.calculate(-4906, -10287), 5381, "")

    def test0104(self):
        self.assertEquals(self.calculate(25702, 3822), 21880, "")

    def test0105(self):
        self.assertEquals(self.calculate(-2544, -2106), -438, "")

    def test0106(self):
        self.assertEquals(self.calculate(-3102, 4645), -7747, "")

    def test0107(self):
        self.assertEquals(self.calculate(29934, 30602), -668, "")

    def test0108(self):
        self.assertEquals(self.calculate(-28282, 26855), 10399, "")

    def test0109(self):
        self.assertEquals(self.calculate(-13560, -22606), 9046, "")

    def test0110(self):
        self.assertEquals(self.calculate(21863, 32170), -10307, "")

    def test0111(self):
        self.assertEquals(self.calculate(-30020, 6595), 28921, "")

    def test0112(self):
        self.assertEquals(self.calculate(8893, -19032), 27925, "")

    def test0113(self):
        self.assertEquals(self.calculate(20790, 16962), 3828, "")

    def test0114(self):
        self.assertEquals(self.calculate(24078, -4946), 29024, "")

    def test0115(self):
        self.assertEquals(self.calculate(-18028, -15739), -2289, "")

    def test0116(self):
        self.assertEquals(self.calculate(14847, -5551), 20398, "")

    def test0117(self):
        self.assertEquals(self.calculate(-31774, -25571), -6203, "")

    def test0118(self):
        self.assertEquals(self.calculate(1460, 29289), -27829, "")

    def test0119(self):
        self.assertEquals(self.calculate(-15614, 31956), 17966, "")

    def test0120(self):
        self.assertEquals(self.calculate(7223, 2571), 4652, "")

    def test0121(self):
        self.assertEquals(self.calculate(-1304, 27446), -28750, "")

    def test0122(self):
        self.assertEquals(self.calculate(-17838, 30472), 17226, "")

    def test0123(self):
        self.assertEquals(self.calculate(30537, 1814), 28723, "")

    def test0124(self):
        self.assertEquals(self.calculate(13167, 5663), 7504, "")

    def test0125(self):
        self.assertEquals(self.calculate(-29112, 16626), 19798, "")

    def test0126(self):
        self.assertEquals(self.calculate(15491, -27584), -22461, "")

    def test0127(self):
        self.assertEquals(self.calculate(20560, 14390), 6170, "")

    def test0128(self):
        self.assertEquals(self.calculate(29533, 3311), 26222, "")

    def test0129(self):
        self.assertEquals(self.calculate(32610, 24719), 7891, "")

    def test0130(self):
        self.assertEquals(self.calculate(22896, 11636), 11260, "")

    def test0131(self):
        self.assertEquals(self.calculate(358, 6165), -5807, "")

    def test0132(self):
        self.assertEquals(self.calculate(-18887, -7880), -11007, "")

    def test0133(self):
        self.assertEquals(self.calculate(-16736, 10410), -27146, "")

    def test0134(self):
        self.assertEquals(self.calculate(14108, 3240), 10868, "")

    def test0135(self):
        self.assertEquals(self.calculate(10308, 6562), 3746, "")

    def test0136(self):
        self.assertEquals(self.calculate(5108, -14551), 19659, "")

    def test0137(self):
        self.assertEquals(self.calculate(26139, -14872), -24525, "")

    def test0138(self):
        self.assertEquals(self.calculate(27838, -23379), -14319, "")

    def test0139(self):
        self.assertEquals(self.calculate(3562, -24808), 28370, "")

    def test0140(self):
        self.assertEquals(self.calculate(-4018, -27180), 23162, "")

    def test0141(self):
        self.assertEquals(self.calculate(-7997, 28129), 29410, "")

    def test0142(self):
        self.assertEquals(self.calculate(-6357, -15680), 9323, "")

    def test0143(self):
        self.assertEquals(self.calculate(26847, -19137), -19552, "")

    def test0144(self):
        self.assertEquals(self.calculate(-27194, -7209), -19985, "")

    def test0145(self):
        self.assertEquals(self.calculate(28928, 20927), 8001, "")

    def test0146(self):
        self.assertEquals(self.calculate(-11266, 5154), -16420, "")

    def test0147(self):
        self.assertEquals(self.calculate(16946, 26240), -9294, "")

    def test0148(self):
        self.assertEquals(self.calculate(-4995, 22753), -27748, "")

    def test0149(self):
        self.assertEquals(self.calculate(32035, 22137), 9898, "")

    def test0150(self):
        self.assertEquals(self.calculate(-4459, -591), -3868, "")

    def test0151(self):
        self.assertEquals(self.calculate(4399, -22777), 27176, "")

    def test0152(self):
        self.assertEquals(self.calculate(20187, 1027), 19160, "")

    def test0153(self):
        self.assertEquals(self.calculate(-11036, 28072), 26428, "")

    def test0154(self):
        self.assertEquals(self.calculate(-18269, -25536), 7267, "")

    def test0155(self):
        self.assertEquals(self.calculate(17214, 16574), 640, "")

    def test0156(self):
        self.assertEquals(self.calculate(-13448, -19403), 5955, "")

    def test0157(self):
        self.assertEquals(self.calculate(22025, -3787), 25812, "")

    def test0158(self):
        self.assertEquals(self.calculate(-1157, -31268), 30111, "")

    def test0159(self):
        self.assertEquals(self.calculate(-5329, -29323), 23994, "")

    def test0160(self):
        self.assertEquals(self.calculate(13808, 13966), -158, "")

    def test0161(self):
        self.assertEquals(self.calculate(-4920, 31083), 29533, "")

    def test0162(self):
        self.assertEquals(self.calculate(-27566, 14530), 23440, "")

    def test0163(self):
        self.assertEquals(self.calculate(-11882, -31655), 19773, "")

    def test0164(self):
        self.assertEquals(self.calculate(31541, -31463), -2532, "")

    def test0165(self):
        self.assertEquals(self.calculate(1304, -6847), 8151, "")

    def test0166(self):
        self.assertEquals(self.calculate(7798, 19079), -11281, "")

    def test0167(self):
        self.assertEquals(self.calculate(-16813, 10695), -27508, "")

    def test0168(self):
        self.assertEquals(self.calculate(22486, -5902), 28388, "")

    def test0169(self):
        self.assertEquals(self.calculate(-1811, -17572), 15761, "")

    def test0170(self):
        self.assertEquals(self.calculate(-25964, -4852), -21112, "")

    def test0171(self):
        self.assertEquals(self.calculate(-21924, 24200), 19412, "")

    def test0172(self):
        self.assertEquals(self.calculate(-5676, 27301), 32559, "")

    def test0173(self):
        self.assertEquals(self.calculate(19028, 25896), -6868, "")

    def test0174(self):
        self.assertEquals(self.calculate(-4191, 5191), -9382, "")

    def test0175(self):
        self.assertEquals(self.calculate(14983, -25727), -24826, "")

    def test0176(self):
        self.assertEquals(self.calculate(-20220, 26763), 18553, "")

    def test0177(self):
        self.assertEquals(self.calculate(-9978, 20232), -30210, "")

    def test0178(self):
        self.assertEquals(self.calculate(-16544, 9725), -26269, "")

    def test0179(self):
        self.assertEquals(self.calculate(21810, 5446), 16364, "")

    def test0180(self):
        self.assertEquals(self.calculate(-256, -4537), 4281, "")

    def test0181(self):
        self.assertEquals(self.calculate(28217, -14465), -22854, "")

    def test0182(self):
        self.assertEquals(self.calculate(-12250, 500), -12750, "")

    def test0183(self):
        self.assertEquals(self.calculate(22780, -23867), -18889, "")

    def test0184(self):
        self.assertEquals(self.calculate(15009, -21574), -28953, "")

    def test0185(self):
        self.assertEquals(self.calculate(-14811, -14899), 88, "")

    def test0186(self):
        self.assertEquals(self.calculate(17238, -31932), -16366, "")

    def test0187(self):
        self.assertEquals(self.calculate(27388, -15087), -23061, "")

    def test0188(self):
        self.assertEquals(self.calculate(-31421, -22076), -9345, "")

    def test0189(self):
        self.assertEquals(self.calculate(8024, 20248), -12224, "")

    def test0190(self):
        self.assertEquals(self.calculate(-20062, -20222), 160, "")

    def test0191(self):
        self.assertEquals(self.calculate(-14359, 30464), 20713, "")

    def test0192(self):
        self.assertEquals(self.calculate(8245, 4735), 3510, "")

    def test0193(self):
        self.assertEquals(self.calculate(-1987, -18410), 16423, "")

    def test0194(self):
        self.assertEquals(self.calculate(-514, 4275), -4789, "")

    def test0195(self):
        self.assertEquals(self.calculate(14699, -11360), 26059, "")

    def test0196(self):
        self.assertEquals(self.calculate(23462, -8737), 32199, "")

    def test0197(self):
        self.assertEquals(self.calculate(11032, -18305), 29337, "")

    def test0198(self):
        self.assertEquals(self.calculate(22234, -26181), -17121, "")

    def test0199(self):
        self.assertEquals(self.calculate(-13280, -12242), -1038, "")

    def test0200(self):
        self.assertEquals(self.calculate(30895, 4931), 25964, "")

    def test0201(self):
        self.assertEquals(self.calculate(-25440, 2631), -28071, "")

    def test0202(self):
        self.assertEquals(self.calculate(-5570, -32268), 26698, "")

    def test0203(self):
        self.assertEquals(self.calculate(-7058, -10959), 3901, "")

    def test0204(self):
        self.assertEquals(self.calculate(1223, 404), 819, "")

    def test0205(self):
        self.assertEquals(self.calculate(3895, -11570), 15465, "")

    def test0206(self):
        self.assertEquals(self.calculate(-26882, 18353), 20301, "")

    def test0207(self):
        self.assertEquals(self.calculate(8012, 2929), 5083, "")

    def test0208(self):
        self.assertEquals(self.calculate(-30294, 6544), 28698, "")

    def test0209(self):
        self.assertEquals(self.calculate(26462, -22812), -16262, "")

    def test0210(self):
        self.assertEquals(self.calculate(-15812, 5529), -21341, "")

    def test0211(self):
        self.assertEquals(self.calculate(-21580, 9614), -31194, "")

    def test0212(self):
        self.assertEquals(self.calculate(20376, -20205), -24955, "")

    def test0213(self):
        self.assertEquals(self.calculate(-21213, -30075), 8862, "")

    def test0214(self):
        self.assertEquals(self.calculate(28925, 6307), 22618, "")

    def test0215(self):
        self.assertEquals(self.calculate(27885, -25975), -11676, "")

    def test0216(self):
        self.assertEquals(self.calculate(17560, 24445), -6885, "")

    def test0217(self):
        self.assertEquals(self.calculate(-889, 23067), -23956, "")

    def test0218(self):
        self.assertEquals(self.calculate(1253, -24407), 25660, "")

    def test0219(self):
        self.assertEquals(self.calculate(11421, 24984), -13563, "")

    def test0220(self):
        self.assertEquals(self.calculate(-32724, 16638), 16174, "")

    def test0221(self):
        self.assertEquals(self.calculate(8286, -11853), 20139, "")

    def test0222(self):
        self.assertEquals(self.calculate(-29831, 21316), 14389, "")

    def test0223(self):
        self.assertEquals(self.calculate(-30518, -4816), -25702, "")

    def test0224(self):
        self.assertEquals(self.calculate(7595, -28423), -29518, "")

    def test0225(self):
        self.assertEquals(self.calculate(2220, -8336), 10556, "")

    def test0226(self):
        self.assertEquals(self.calculate(-5686, -14927), 9241, "")

    def test0227(self):
        self.assertEquals(self.calculate(1312, -4052), 5364, "")

    def test0228(self):
        self.assertEquals(self.calculate(-18477, 28647), 18412, "")

    def test0229(self):
        self.assertEquals(self.calculate(31964, 10229), 21735, "")

    def test0230(self):
        self.assertEquals(self.calculate(-24110, -23241), -869, "")

    def test0231(self):
        self.assertEquals(self.calculate(18174, -2743), 20917, "")

    def test0232(self):
        self.assertEquals(self.calculate(14663, 18579), -3916, "")

    def test0233(self):
        self.assertEquals(self.calculate(8398, 27717), -19319, "")

    def test0234(self):
        self.assertEquals(self.calculate(8283, 7235), 1048, "")

    def test0235(self):
        self.assertEquals(self.calculate(22228, 25701), -3473, "")

    def test0236(self):
        self.assertEquals(self.calculate(-13215, -22579), 9364, "")

    def test0237(self):
        self.assertEquals(self.calculate(-23986, 2179), -26165, "")

    def test0238(self):
        self.assertEquals(self.calculate(13932, -3212), 17144, "")

    def test0239(self):
        self.assertEquals(self.calculate(-26259, -29013), 2754, "")

    def test0240(self):
        self.assertEquals(self.calculate(-297, 13536), -13833, "")

    def test0241(self):
        self.assertEquals(self.calculate(20568, -17687), -27281, "")

    def test0242(self):
        self.assertEquals(self.calculate(24608, -21378), -19550, "")

    def test0243(self):
        self.assertEquals(self.calculate(24337, -18107), -23092, "")

    def test0244(self):
        self.assertEquals(self.calculate(-30105, -30981), 876, "")

    def test0245(self):
        self.assertEquals(self.calculate(28070, -7021), -30445, "")

    def test0246(self):
        self.assertEquals(self.calculate(-26812, -8771), -18041, "")

    def test0247(self):
        self.assertEquals(self.calculate(337, 19589), -19252, "")

    def test0248(self):
        self.assertEquals(self.calculate(13572, -11610), 25182, "")

    def test0249(self):
        self.assertEquals(self.calculate(8584, 4442), 4142, "")

    def test0250(self):
        self.assertEquals(self.calculate(3703, -6355), 10058, "")

    def test0251(self):
        self.assertEquals(self.calculate(8898, -859), 9757, "")

    def test0252(self):
        self.assertEquals(self.calculate(7423, 22695), -15272, "")

    def test0253(self):
        self.assertEquals(self.calculate(-13608, -22165), 8557, "")

    def test0254(self):
        self.assertEquals(self.calculate(-17547, 19717), 28272, "")

    def test0255(self):
        self.assertEquals(self.calculate(27092, 9855), 17237, "")

    def test0256(self):
        self.assertEquals(self.calculate(30192, -22137), -13207, "")

    def test0257(self):
        self.assertEquals(self.calculate(19626, 9860), 9766, "")

    def test0258(self):
        self.assertEquals(self.calculate(-8844, -7901), -943, "")

    def test0259(self):
        self.assertEquals(self.calculate(-5393, -9405), 4012, "")

    def test0260(self):
        self.assertEquals(self.calculate(21574, 12669), 8905, "")

    def test0261(self):
        self.assertEquals(self.calculate(23540, -14940), -27056, "")

    def test0262(self):
        self.assertEquals(self.calculate(9156, -28447), -27933, "")

    def test0263(self):
        self.assertEquals(self.calculate(30707, 20115), 10592, "")

    def test0264(self):
        self.assertEquals(self.calculate(-4164, 6368), -10532, "")

    def test0265(self):
        self.assertEquals(self.calculate(1800, -5094), 6894, "")

    def test0266(self):
        self.assertEquals(self.calculate(-16516, -30157), 13641, "")

    def test0267(self):
        self.assertEquals(self.calculate(13301, -31207), -21028, "")

    def test0268(self):
        self.assertEquals(self.calculate(-20100, 3578), -23678, "")

    def test0269(self):
        self.assertEquals(self.calculate(6290, 23328), -17038, "")

    def test0270(self):
        self.assertEquals(self.calculate(-3503, -20702), 17199, "")

    def test0271(self):
        self.assertEquals(self.calculate(-12248, 31860), 21428, "")

    def test0272(self):
        self.assertEquals(self.calculate(21094, -23791), -20651, "")

    def test0273(self):
        self.assertEquals(self.calculate(25858, 18011), 7847, "")

    def test0274(self):
        self.assertEquals(self.calculate(-468, -7651), 7183, "")

    def test0275(self):
        self.assertEquals(self.calculate(14849, 27721), -12872, "")

    def test0276(self):
        self.assertEquals(self.calculate(24710, 30917), -6207, "")

    def test0277(self):
        self.assertEquals(self.calculate(28209, -18769), -18558, "")

    def test0278(self):
        self.assertEquals(self.calculate(6705, -4384), 11089, "")

    def test0279(self):
        self.assertEquals(self.calculate(13413, 20303), -6890, "")

    def test0280(self):
        self.assertEquals(self.calculate(6631, 15846), -9215, "")

    def test0281(self):
        self.assertEquals(self.calculate(-17476, -24017), 6541, "")

    def test0282(self):
        self.assertEquals(self.calculate(16652, 2584), 14068, "")

    def test0283(self):
        self.assertEquals(self.calculate(9744, 15536), -5792, "")

    def test0284(self):
        self.assertEquals(self.calculate(2061, -12787), 14848, "")

    def test0285(self):
        self.assertEquals(self.calculate(12892, -15369), 28261, "")

    def test0286(self):
        self.assertEquals(self.calculate(-4263, 9408), -13671, "")

    def test0287(self):
        self.assertEquals(self.calculate(-3640, -13455), 9815, "")

    def test0288(self):
        self.assertEquals(self.calculate(22907, -1340), 24247, "")

    def test0289(self):
        self.assertEquals(self.calculate(13251, -25053), -27232, "")

    def test0290(self):
        self.assertEquals(self.calculate(-11351, 3137), -14488, "")

    def test0291(self):
        self.assertEquals(self.calculate(22894, 29268), -6374, "")

    def test0292(self):
        self.assertEquals(self.calculate(-4889, 21535), -26424, "")

    def test0293(self):
        self.assertEquals(self.calculate(-6387, -5297), -1090, "")

    def test0294(self):
        self.assertEquals(self.calculate(-10139, 16360), -26499, "")

    def test0295(self):
        self.assertEquals(self.calculate(-8438, -30337), 21899, "")

    def test0296(self):
        self.assertEquals(self.calculate(2839, 4566), -1727, "")

    def test0297(self):
        self.assertEquals(self.calculate(-27949, 31631), 5956, "")

    def test0298(self):
        self.assertEquals(self.calculate(3239, 25301), -22062, "")

    def test0299(self):
        self.assertEquals(self.calculate(21847, -17400), -26289, "")

    def test0300(self):
        self.assertEquals(self.calculate(-27493, 4429), -31922, "")

    def test0301(self):
        self.assertEquals(self.calculate(20912, -14615), -30009, "")

    def test0302(self):
        self.assertEquals(self.calculate(-20434, -9621), -10813, "")

    def test0303(self):
        self.assertEquals(self.calculate(-6334, -3145), -3189, "")

    def test0304(self):
        self.assertEquals(self.calculate(-32530, 31131), 1875, "")

    def test0305(self):
        self.assertEquals(self.calculate(-18420, -11839), -6581, "")

    def test0306(self):
        self.assertEquals(self.calculate(20482, 28882), -8400, "")

    def test0307(self):
        self.assertEquals(self.calculate(-3205, -26026), 22821, "")

    def test0308(self):
        self.assertEquals(self.calculate(-7832, -25763), 17931, "")

    def test0309(self):
        self.assertEquals(self.calculate(-32622, 29456), 3458, "")

    def test0310(self):
        self.assertEquals(self.calculate(20248, 12396), 7852, "")

    def test0311(self):
        self.assertEquals(self.calculate(-24103, 13056), 28377, "")

    def test0312(self):
        self.assertEquals(self.calculate(-24695, -5938), -18757, "")

    def test0313(self):
        self.assertEquals(self.calculate(-20252, -13207), -7045, "")

    def test0314(self):
        self.assertEquals(self.calculate(13777, 27029), -13252, "")

    def test0315(self):
        self.assertEquals(self.calculate(-23547, -24251), 704, "")

    def test0316(self):
        self.assertEquals(self.calculate(-14452, 4309), -18761, "")

    def test0317(self):
        self.assertEquals(self.calculate(-19865, 13539), 32132, "")

    def test0318(self):
        self.assertEquals(self.calculate(9590, -23651), -32295, "")

    def test0319(self):
        self.assertEquals(self.calculate(-566, 4855), -5421, "")

    def test0320(self):
        self.assertEquals(self.calculate(18414, -781), 19195, "")

    def test0321(self):
        self.assertEquals(self.calculate(-14458, -23562), 9104, "")

    def test0322(self):
        self.assertEquals(self.calculate(25631, 2395), 23236, "")

    def test0323(self):
        self.assertEquals(self.calculate(10172, -24043), -31321, "")

    def test0324(self):
        self.assertEquals(self.calculate(-24206, -21540), -2666, "")

    def test0325(self):
        self.assertEquals(self.calculate(6954, -24279), 31233, "")

    def test0326(self):
        self.assertEquals(self.calculate(7242, 17194), -9952, "")

    def test0327(self):
        self.assertEquals(self.calculate(-11047, -9725), -1322, "")

    def test0328(self):
        self.assertEquals(self.calculate(18082, 10872), 7210, "")

    def test0329(self):
        self.assertEquals(self.calculate(5182, -1938), 7120, "")

    def test0330(self):
        self.assertEquals(self.calculate(-2209, 20054), -22263, "")

    def test0331(self):
        self.assertEquals(self.calculate(31381, -17167), -16988, "")

    def test0332(self):
        self.assertEquals(self.calculate(-18810, 18639), 28087, "")

    def test0333(self):
        self.assertEquals(self.calculate(-17146, 13296), -30442, "")

    def test0334(self):
        self.assertEquals(self.calculate(-3400, 9642), -13042, "")

    def test0335(self):
        self.assertEquals(self.calculate(-28402, -18679), -9723, "")

    def test0336(self):
        self.assertEquals(self.calculate(-16472, -24941), 8469, "")

    def test0337(self):
        self.assertEquals(self.calculate(25415, 26662), -1247, "")

    def test0338(self):
        self.assertEquals(self.calculate(-11571, -5583), -5988, "")

    def test0339(self):
        self.assertEquals(self.calculate(-24258, 28362), 12916, "")

    def test0340(self):
        self.assertEquals(self.calculate(9980, 5188), 4792, "")

    def test0341(self):
        self.assertEquals(self.calculate(-17383, 7385), -24768, "")

    def test0342(self):
        self.assertEquals(self.calculate(-8535, 21680), -30215, "")

    def test0343(self):
        self.assertEquals(self.calculate(-27891, 13010), 24635, "")

    def test0344(self):
        self.assertEquals(self.calculate(2028, 4587), -2559, "")

    def test0345(self):
        self.assertEquals(self.calculate(-3228, -16518), 13290, "")

    def test0346(self):
        self.assertEquals(self.calculate(-31973, -20947), -11026, "")

    def test0347(self):
        self.assertEquals(self.calculate(23134, 12341), 10793, "")

    def test0348(self):
        self.assertEquals(self.calculate(-23340, -19275), -4065, "")

    def test0349(self):
        self.assertEquals(self.calculate(27143, 26119), 1024, "")

    def test0350(self):
        self.assertEquals(self.calculate(-4341, 24392), -28733, "")

    def test0351(self):
        self.assertEquals(self.calculate(-13201, 7001), -20202, "")

    def test0352(self):
        self.assertEquals(self.calculate(-5720, -6151), 431, "")

    def test0353(self):
        self.assertEquals(self.calculate(-18429, 2688), -21117, "")

    def test0354(self):
        self.assertEquals(self.calculate(25214, -13476), -26846, "")

    def test0355(self):
        self.assertEquals(self.calculate(-13932, 14735), -28667, "")

    def test0356(self):
        self.assertEquals(self.calculate(-28914, 21124), 15498, "")

    def test0357(self):
        self.assertEquals(self.calculate(16997, 28773), -11776, "")

    def test0358(self):
        self.assertEquals(self.calculate(-18732, -5978), -12754, "")

    def test0359(self):
        self.assertEquals(self.calculate(-5255, 13267), -18522, "")

    def test0360(self):
        self.assertEquals(self.calculate(-19505, -18909), -596, "")

    def test0361(self):
        self.assertEquals(self.calculate(-28382, 4292), -32674, "")

    def test0362(self):
        self.assertEquals(self.calculate(-12138, -1042), -11096, "")

    def test0363(self):
        self.assertEquals(self.calculate(-5760, -9733), 3973, "")

    def test0364(self):
        self.assertEquals(self.calculate(3562, -11050), 14612, "")

    def test0365(self):
        self.assertEquals(self.calculate(-30352, -13203), -17149, "")

    def test0366(self):
        self.assertEquals(self.calculate(-11403, -26331), 14928, "")

    def test0367(self):
        self.assertEquals(self.calculate(-29120, 24887), 11529, "")

    def test0368(self):
        self.assertEquals(self.calculate(-3871, 13583), -17454, "")

    def test0369(self):
        self.assertEquals(self.calculate(17976, 4), 17972, "")

    def test0370(self):
        self.assertEquals(self.calculate(13279, 24538), -11259, "")

    def test0371(self):
        self.assertEquals(self.calculate(-3083, -27284), 24201, "")

    def test0372(self):
        self.assertEquals(self.calculate(-28786, 17008), 19742, "")

    def test0373(self):
        self.assertEquals(self.calculate(19314, 10917), 8397, "")

    def test0374(self):
        self.assertEquals(self.calculate(17341, 6866), 10475, "")

    def test0375(self):
        self.assertEquals(self.calculate(-1594, 15725), -17319, "")

    def test0376(self):
        self.assertEquals(self.calculate(-18983, -19824), 841, "")

    def test0377(self):
        self.assertEquals(self.calculate(-8450, 7487), -15937, "")

    def test0378(self):
        self.assertEquals(self.calculate(-24914, 26102), 14520, "")

    def test0379(self):
        self.assertEquals(self.calculate(-10940, 11352), -22292, "")

    def test0380(self):
        self.assertEquals(self.calculate(23378, 26880), -3502, "")

    def test0381(self):
        self.assertEquals(self.calculate(7854, -7693), 15547, "")

    def test0382(self):
        self.assertEquals(self.calculate(25982, 23594), 2388, "")

    def test0383(self):
        self.assertEquals(self.calculate(-24472, -8191), -16281, "")

    def test0384(self):
        self.assertEquals(self.calculate(-21607, 5098), -26705, "")

    def test0385(self):
        self.assertEquals(self.calculate(-32162, 31722), 1652, "")

    def test0386(self):
        self.assertEquals(self.calculate(4417, 11121), -6704, "")

    def test0387(self):
        self.assertEquals(self.calculate(-21654, 24475), 19407, "")

    def test0388(self):
        self.assertEquals(self.calculate(5480, -3112), 8592, "")

    def test0389(self):
        self.assertEquals(self.calculate(-28662, -28941), 279, "")

    def test0390(self):
        self.assertEquals(self.calculate(18945, 16203), 2742, "")

    def test0391(self):
        self.assertEquals(self.calculate(-28649, 6800), 30087, "")

    def test0392(self):
        self.assertEquals(self.calculate(-15413, -16686), 1273, "")

    def test0393(self):
        self.assertEquals(self.calculate(22175, -32198), -11163, "")

    def test0394(self):
        self.assertEquals(self.calculate(-9739, 9254), -18993, "")

    def test0395(self):
        self.assertEquals(self.calculate(28196, -12428), -24912, "")

    def test0396(self):
        self.assertEquals(self.calculate(31562, 22253), 9309, "")

    def test0397(self):
        self.assertEquals(self.calculate(31349, -24765), -9422, "")

    def test0398(self):
        self.assertEquals(self.calculate(-17318, -30389), 13071, "")

    def test0399(self):
        self.assertEquals(self.calculate(-7349, 29431), 28756, "")

    def test0400(self):
        self.assertEquals(self.calculate(10427, -3505), 13932, "")

    def test0401(self):
        self.assertEquals(self.calculate(32598, 26143), 6455, "")

    def test0402(self):
        self.assertEquals(self.calculate(28618, 25724), 2894, "")

    def test0403(self):
        self.assertEquals(self.calculate(-18321, -27005), 8684, "")

    def test0404(self):
        self.assertEquals(self.calculate(-8534, 11267), -19801, "")

    def test0405(self):
        self.assertEquals(self.calculate(-29197, 20395), 15944, "")

    def test0406(self):
        self.assertEquals(self.calculate(-6568, -15718), 9150, "")

    def test0407(self):
        self.assertEquals(self.calculate(-4494, -1780), -2714, "")

    def test0408(self):
        self.assertEquals(self.calculate(8808, -29571), -27157, "")

    def test0409(self):
        self.assertEquals(self.calculate(27299, -21546), -16691, "")

    def test0410(self):
        self.assertEquals(self.calculate(17464, 16364), 1100, "")

    def test0411(self):
        self.assertEquals(self.calculate(-113, 18209), -18322, "")

    def test0412(self):
        self.assertEquals(self.calculate(1676, -31248), -32612, "")

    def test0413(self):
        self.assertEquals(self.calculate(9842, -1748), 11590, "")

    def test0414(self):
        self.assertEquals(self.calculate(13846, -16386), 30232, "")

    def test0415(self):
        self.assertEquals(self.calculate(18455, 27746), -9291, "")

    def test0416(self):
        self.assertEquals(self.calculate(-16324, -7333), -8991, "")

    def test0417(self):
        self.assertEquals(self.calculate(-1191, 18824), -20015, "")

    def test0418(self):
        self.assertEquals(self.calculate(12251, -16897), 29148, "")

    def test0419(self):
        self.assertEquals(self.calculate(-19819, -1516), -18303, "")

    def test0420(self):
        self.assertEquals(self.calculate(-28212, -21567), -6645, "")

    def test0421(self):
        self.assertEquals(self.calculate(-28723, -2107), -26616, "")

    def test0422(self):
        self.assertEquals(self.calculate(-13719, -11537), -2182, "")

    def test0423(self):
        self.assertEquals(self.calculate(-26233, -23088), -3145, "")

    def test0424(self):
        self.assertEquals(self.calculate(21563, -7566), 29129, "")

    def test0425(self):
        self.assertEquals(self.calculate(-3991, -25431), 21440, "")

    def test0426(self):
        self.assertEquals(self.calculate(-9392, -23852), 14460, "")

    def test0427(self):
        self.assertEquals(self.calculate(-2474, -22465), 19991, "")

    def test0428(self):
        self.assertEquals(self.calculate(-7021, -7605), 584, "")

    def test0429(self):
        self.assertEquals(self.calculate(5602, -9252), 14854, "")

    def test0430(self):
        self.assertEquals(self.calculate(27223, -17101), -21212, "")

    def test0431(self):
        self.assertEquals(self.calculate(32357, 3904), 28453, "")

    def test0432(self):
        self.assertEquals(self.calculate(-9143, 1451), -10594, "")

    def test0433(self):
        self.assertEquals(self.calculate(-19195, -5692), -13503, "")

    def test0434(self):
        self.assertEquals(self.calculate(18361, -3659), 22020, "")

    def test0435(self):
        self.assertEquals(self.calculate(-13658, 5476), -19134, "")

    def test0436(self):
        self.assertEquals(self.calculate(-11187, 17842), -29029, "")

    def test0437(self):
        self.assertEquals(self.calculate(-27462, 26273), 11801, "")

    def test0438(self):
        self.assertEquals(self.calculate(-2654, 22482), -25136, "")

    def test0439(self):
        self.assertEquals(self.calculate(-5076, 15795), -20871, "")

    def test0440(self):
        self.assertEquals(self.calculate(-22689, -27392), 4703, "")

    def test0441(self):
        self.assertEquals(self.calculate(-21034, 13317), 31185, "")

    def test0442(self):
        self.assertEquals(self.calculate(-16821, -27), -16794, "")

    def test0443(self):
        self.assertEquals(self.calculate(19427, -3139), 22566, "")

    def test0444(self):
        self.assertEquals(self.calculate(-30299, 20926), 14311, "")

    def test0445(self):
        self.assertEquals(self.calculate(12950, 21052), -8102, "")

    def test0446(self):
        self.assertEquals(self.calculate(-31775, 5921), 27840, "")

    def test0447(self):
        self.assertEquals(self.calculate(21519, 23429), -1910, "")

    def test0448(self):
        self.assertEquals(self.calculate(-14364, 5243), -19607, "")

    def test0449(self):
        self.assertEquals(self.calculate(-19039, 31798), 14699, "")

    def test0450(self):
        self.assertEquals(self.calculate(-3562, -15732), 12170, "")

    def test0451(self):
        self.assertEquals(self.calculate(5658, 13299), -7641, "")

    def test0452(self):
        self.assertEquals(self.calculate(-3551, -5424), 1873, "")

    def test0453(self):
        self.assertEquals(self.calculate(4091, -15769), 19860, "")

    def test0454(self):
        self.assertEquals(self.calculate(-11799, 3943), -15742, "")

    def test0455(self):
        self.assertEquals(self.calculate(17083, 721), 16362, "")

    def test0456(self):
        self.assertEquals(self.calculate(29355, 6655), 22700, "")

    def test0457(self):
        self.assertEquals(self.calculate(5587, -6742), 12329, "")

    def test0458(self):
        self.assertEquals(self.calculate(2551, -8368), 10919, "")

    def test0459(self):
        self.assertEquals(self.calculate(-3874, 10930), -14804, "")

    def test0460(self):
        self.assertEquals(self.calculate(2655, -14983), 17638, "")

    def test0461(self):
        self.assertEquals(self.calculate(-3496, 21919), -25415, "")

    def test0462(self):
        self.assertEquals(self.calculate(28897, -26130), -10509, "")

    def test0463(self):
        self.assertEquals(self.calculate(-19203, 28171), 18162, "")

    def test0464(self):
        self.assertEquals(self.calculate(-13530, -27374), 13844, "")

    def test0465(self):
        self.assertEquals(self.calculate(-32258, 5120), 28158, "")

    def test0466(self):
        self.assertEquals(self.calculate(-10860, -5150), -5710, "")

    def test0467(self):
        self.assertEquals(self.calculate(7306, -31311), -26919, "")

    def test0468(self):
        self.assertEquals(self.calculate(-24768, -6912), -17856, "")

    def test0469(self):
        self.assertEquals(self.calculate(-1591, 10812), -12403, "")

    def test0470(self):
        self.assertEquals(self.calculate(23215, -25375), -16946, "")

    def test0471(self):
        self.assertEquals(self.calculate(-27448, -16513), -10935, "")

    def test0472(self):
        self.assertEquals(self.calculate(20209, 1758), 18451, "")

    def test0473(self):
        self.assertEquals(self.calculate(13326, 1440), 11886, "")

    def test0474(self):
        self.assertEquals(self.calculate(6505, -5063), 11568, "")

    def test0475(self):
        self.assertEquals(self.calculate(19066, -9257), 28323, "")

    def test0476(self):
        self.assertEquals(self.calculate(-28858, 28853), 7825, "")

    def test0477(self):
        self.assertEquals(self.calculate(-2181, 14097), -16278, "")

    def test0478(self):
        self.assertEquals(self.calculate(17009, 14002), 3007, "")

    def test0479(self):
        self.assertEquals(self.calculate(7414, 3785), 3629, "")

    def test0480(self):
        self.assertEquals(self.calculate(16247, 12241), 4006, "")

    def test0481(self):
        self.assertEquals(self.calculate(9160, -1965), 11125, "")

    def test0482(self):
        self.assertEquals(self.calculate(11126, -28474), -25936, "")

    def test0483(self):
        self.assertEquals(self.calculate(-11799, -28724), 16925, "")

    def test0484(self):
        self.assertEquals(self.calculate(-5717, -31049), 25332, "")

    def test0485(self):
        self.assertEquals(self.calculate(20797, -874), 21671, "")

    def test0486(self):
        self.assertEquals(self.calculate(14884, -7910), 22794, "")

    def test0487(self):
        self.assertEquals(self.calculate(25583, -20579), -19374, "")

    def test0488(self):
        self.assertEquals(self.calculate(-15138, 4315), -19453, "")

    def test0489(self):
        self.assertEquals(self.calculate(23689, 30566), -6877, "")

    def test0490(self):
        self.assertEquals(self.calculate(1410, 29636), -28226, "")

    def test0491(self):
        self.assertEquals(self.calculate(607, 3006), -2399, "")

    def test0492(self):
        self.assertEquals(self.calculate(11871, -17534), 29405, "")

    def test0493(self):
        self.assertEquals(self.calculate(16457, -1732), 18189, "")

    def test0494(self):
        self.assertEquals(self.calculate(-50, 8692), -8742, "")

    def test0495(self):
        self.assertEquals(self.calculate(-10943, 21507), -32450, "")

    def test0496(self):
        self.assertEquals(self.calculate(16079, -31121), -18336, "")

    def test0497(self):
        self.assertEquals(self.calculate(10027, -18284), 28311, "")

    def test0498(self):
        self.assertEquals(self.calculate(21224, 24970), -3746, "")

    def test0499(self):
        self.assertEquals(self.calculate(-12539, 3472), -16011, "")

    def test0500(self):
        self.assertEquals(self.calculate(16414, -8698), 25112, "")

    def test0501(self):
        self.assertEquals(self.calculate(-28942, -31651), 2709, "")

    def test0502(self):
        self.assertEquals(self.calculate(10932, -13936), 24868, "")

    def test0503(self):
        self.assertEquals(self.calculate(-3661, -24445), 20784, "")

    def test0504(self):
        self.assertEquals(self.calculate(-1913, -30773), 28860, "")

    def test0505(self):
        self.assertEquals(self.calculate(-31876, 22952), 10708, "")

    def test0506(self):
        self.assertEquals(self.calculate(-16432, 27403), 21701, "")

    def test0507(self):
        self.assertEquals(self.calculate(-21215, 19580), 24741, "")

    def test0508(self):
        self.assertEquals(self.calculate(19805, -8781), 28586, "")

    def test0509(self):
        self.assertEquals(self.calculate(-2512, 22562), -25074, "")

    def test0510(self):
        self.assertEquals(self.calculate(8452, 10682), -2230, "")

    def test0511(self):
        self.assertEquals(self.calculate(-20760, -6992), -13768, "")

    def test0512(self):
        self.assertEquals(self.calculate(26033, 15863), 10170, "")

    def test0513(self):
        self.assertEquals(self.calculate(11749, -6883), 18632, "")

    def test0514(self):
        self.assertEquals(self.calculate(6975, 7430), -455, "")

    def test0515(self):
        self.assertEquals(self.calculate(-7051, 9040), -16091, "")

    def test0516(self):
        self.assertEquals(self.calculate(23588, 30379), -6791, "")

    def test0517(self):
        self.assertEquals(self.calculate(-4289, -1717), -2572, "")

    def test0518(self):
        self.assertEquals(self.calculate(3943, 21057), -17114, "")

    def test0519(self):
        self.assertEquals(self.calculate(9682, 367), 9315, "")

    def test0520(self):
        self.assertEquals(self.calculate(-2056, 24954), -27010, "")

    def test0521(self):
        self.assertEquals(self.calculate(16768, 28676), -11908, "")

    def test0522(self):
        self.assertEquals(self.calculate(-11992, 25028), 28516, "")

    def test0523(self):
        self.assertEquals(self.calculate(-16633, -24669), 8036, "")

    def test0524(self):
        self.assertEquals(self.calculate(-15732, -29786), 14054, "")

    def test0525(self):
        self.assertEquals(self.calculate(-5225, 4820), -10045, "")

    def test0526(self):
        self.assertEquals(self.calculate(-8382, -25704), 17322, "")

    def test0527(self):
        self.assertEquals(self.calculate(21022, -11650), 32672, "")

    def test0528(self):
        self.assertEquals(self.calculate(-22209, -23217), 1008, "")

    def test0529(self):
        self.assertEquals(self.calculate(-30297, 28511), 6728, "")

    def test0530(self):
        self.assertEquals(self.calculate(-270, 9364), -9634, "")

    def test0531(self):
        self.assertEquals(self.calculate(-30019, -12393), -17626, "")

    def test0532(self):
        self.assertEquals(self.calculate(-21645, -13478), -8167, "")

    def test0533(self):
        self.assertEquals(self.calculate(-28315, -17993), -10322, "")

    def test0534(self):
        self.assertEquals(self.calculate(5205, -27019), 32224, "")

    def test0535(self):
        self.assertEquals(self.calculate(9430, 21623), -12193, "")

    def test0536(self):
        self.assertEquals(self.calculate(28725, 18606), 10119, "")

    def test0537(self):
        self.assertEquals(self.calculate(16036, -31801), -17699, "")

    def test0538(self):
        self.assertEquals(self.calculate(3533, -13353), 16886, "")

    def test0539(self):
        self.assertEquals(self.calculate(10384, 23079), -12695, "")

    def test0540(self):
        self.assertEquals(self.calculate(27346, 28440), -1094, "")

    def test0541(self):
        self.assertEquals(self.calculate(22720, 30222), -7502, "")

    def test0542(self):
        self.assertEquals(self.calculate(-15498, -7229), -8269, "")

    def test0543(self):
        self.assertEquals(self.calculate(17979, 7532), 10447, "")

    def test0544(self):
        self.assertEquals(self.calculate(-9706, -23674), 13968, "")

    def test0545(self):
        self.assertEquals(self.calculate(-22466, 8148), -30614, "")

    def test0546(self):
        self.assertEquals(self.calculate(14716, -2579), 17295, "")

    def test0547(self):
        self.assertEquals(self.calculate(-17200, 27203), 21133, "")

    def test0548(self):
        self.assertEquals(self.calculate(-29547, -16681), -12866, "")

    def test0549(self):
        self.assertEquals(self.calculate(-13993, -19018), 5025, "")

    def test0550(self):
        self.assertEquals(self.calculate(-7514, -27374), 19860, "")

    def test0551(self):
        self.assertEquals(self.calculate(25735, -17981), -21820, "")

    def test0552(self):
        self.assertEquals(self.calculate(31451, -32396), -1689, "")

    def test0553(self):
        self.assertEquals(self.calculate(10479, 24597), -14118, "")

    def test0554(self):
        self.assertEquals(self.calculate(28612, -11644), -25280, "")

    def test0555(self):
        self.assertEquals(self.calculate(15240, -12476), 27716, "")

    def test0556(self):
        self.assertEquals(self.calculate(25243, 7343), 17900, "")

    def test0557(self):
        self.assertEquals(self.calculate(-15929, 15712), -31641, "")

    def test0558(self):
        self.assertEquals(self.calculate(-22235, -11138), -11097, "")

    def test0559(self):
        self.assertEquals(self.calculate(-30919, 18384), 16233, "")

    def test0560(self):
        self.assertEquals(self.calculate(-25196, -9928), -15268, "")

    def test0561(self):
        self.assertEquals(self.calculate(-28860, -13385), -15475, "")

    def test0562(self):
        self.assertEquals(self.calculate(6421, 32196), -25775, "")

    def test0563(self):
        self.assertEquals(self.calculate(-316, 10443), -10759, "")

    def test0564(self):
        self.assertEquals(self.calculate(12355, 21945), -9590, "")

    def test0565(self):
        self.assertEquals(self.calculate(-30813, -29759), -1054, "")

    def test0566(self):
        self.assertEquals(self.calculate(26437, 23820), 2617, "")

    def test0567(self):
        self.assertEquals(self.calculate(29787, -16271), -19478, "")

    def test0568(self):
        self.assertEquals(self.calculate(-21543, 9179), -30722, "")

    def test0569(self):
        self.assertEquals(self.calculate(5125, 14454), -9329, "")

    def test0570(self):
        self.assertEquals(self.calculate(5707, -12807), 18514, "")

    def test0571(self):
        self.assertEquals(self.calculate(29347, -3736), -32453, "")

    def test0572(self):
        self.assertEquals(self.calculate(5659, 8254), -2595, "")

    def test0573(self):
        self.assertEquals(self.calculate(-23680, 2653), -26333, "")

    def test0574(self):
        self.assertEquals(self.calculate(32046, 26466), 5580, "")

    def test0575(self):
        self.assertEquals(self.calculate(-13667, 12988), -26655, "")

    def test0576(self):
        self.assertEquals(self.calculate(-2050, 731), -2781, "")

    def test0577(self):
        self.assertEquals(self.calculate(9804, -21284), 31088, "")

    def test0578(self):
        self.assertEquals(self.calculate(27530, -19608), -18398, "")

    def test0579(self):
        self.assertEquals(self.calculate(-11676, 15668), -27344, "")

    def test0580(self):
        self.assertEquals(self.calculate(-13687, -26327), 12640, "")

    def test0581(self):
        self.assertEquals(self.calculate(-28852, 20518), 16166, "")

    def test0582(self):
        self.assertEquals(self.calculate(-18199, 15298), 32039, "")

    def test0583(self):
        self.assertEquals(self.calculate(23336, 15804), 7532, "")

    def test0584(self):
        self.assertEquals(self.calculate(-1002, 32265), 32269, "")

    def test0585(self):
        self.assertEquals(self.calculate(10178, -28763), -26595, "")

    def test0586(self):
        self.assertEquals(self.calculate(5451, -26551), 32002, "")

    def test0587(self):
        self.assertEquals(self.calculate(-31586, -19539), -12047, "")

    def test0588(self):
        self.assertEquals(self.calculate(25976, -21939), -17621, "")

    def test0589(self):
        self.assertEquals(self.calculate(7720, 20990), -13270, "")

    def test0590(self):
        self.assertEquals(self.calculate(5605, 13793), -8188, "")

    def test0591(self):
        self.assertEquals(self.calculate(-10317, 13007), -23324, "")

    def test0592(self):
        self.assertEquals(self.calculate(4299, 7466), -3167, "")

    def test0593(self):
        self.assertEquals(self.calculate(-15936, -11701), -4235, "")

    def test0594(self):
        self.assertEquals(self.calculate(10415, -25887), -29234, "")

    def test0595(self):
        self.assertEquals(self.calculate(6152, -9989), 16141, "")

    def test0596(self):
        self.assertEquals(self.calculate(-30666, -1911), -28755, "")

    def test0597(self):
        self.assertEquals(self.calculate(-3981, 2581), -6562, "")

    def test0598(self):
        self.assertEquals(self.calculate(-30436, 12485), 22615, "")

    def test0599(self):
        self.assertEquals(self.calculate(-8334, -28428), 20094, "")

    def test0600(self):
        self.assertEquals(self.calculate(-17962, -1132), -16830, "")

    def test0601(self):
        self.assertEquals(self.calculate(1099, -19338), 20437, "")

    def test0602(self):
        self.assertEquals(self.calculate(14300, -4180), 18480, "")

    def test0603(self):
        self.assertEquals(self.calculate(10823, -9208), 20031, "")

    def test0604(self):
        self.assertEquals(self.calculate(-6367, -28766), 22399, "")

    def test0605(self):
        self.assertEquals(self.calculate(-17137, -31998), 14861, "")

    def test0606(self):
        self.assertEquals(self.calculate(20672, -11058), 31730, "")

    def test0607(self):
        self.assertEquals(self.calculate(-4088, 2726), -6814, "")

    def test0608(self):
        self.assertEquals(self.calculate(20603, 29226), -8623, "")

    def test0609(self):
        self.assertEquals(self.calculate(8500, 18511), -10011, "")

    def test0610(self):
        self.assertEquals(self.calculate(-21118, -5065), -16053, "")

    def test0611(self):
        self.assertEquals(self.calculate(17885, -7410), 25295, "")

    def test0612(self):
        self.assertEquals(self.calculate(14974, -8276), 23250, "")

    def test0613(self):
        self.assertEquals(self.calculate(18404, 5671), 12733, "")

    def test0614(self):
        self.assertEquals(self.calculate(20300, 5112), 15188, "")

    def test0615(self):
        self.assertEquals(self.calculate(-29542, -18493), -11049, "")

    def test0616(self):
        self.assertEquals(self.calculate(14466, -20222), -30848, "")

    def test0617(self):
        self.assertEquals(self.calculate(-15731, 21652), 28153, "")

    def test0618(self):
        self.assertEquals(self.calculate(15335, -29296), -20905, "")

    def test0619(self):
        self.assertEquals(self.calculate(-5694, 29662), 30180, "")

    def test0620(self):
        self.assertEquals(self.calculate(-5140, 16110), -21250, "")

    def test0621(self):
        self.assertEquals(self.calculate(-22102, 7186), -29288, "")

    def test0622(self):
        self.assertEquals(self.calculate(-24198, -7569), -16629, "")

    def test0623(self):
        self.assertEquals(self.calculate(22216, 17257), 4959, "")

    def test0624(self):
        self.assertEquals(self.calculate(-5304, -32658), 27354, "")

    def test0625(self):
        self.assertEquals(self.calculate(-17308, -1773), -15535, "")

    def test0626(self):
        self.assertEquals(self.calculate(-6789, -27103), 20314, "")

    def test0627(self):
        self.assertEquals(self.calculate(8868, 10239), -1371, "")

    def test0628(self):
        self.assertEquals(self.calculate(-10755, 969), -11724, "")

    def test0629(self):
        self.assertEquals(self.calculate(2681, 21568), -18887, "")

    def test0630(self):
        self.assertEquals(self.calculate(12439, -13759), 26198, "")

    def test0631(self):
        self.assertEquals(self.calculate(-13847, 23556), 28133, "")

    def test0632(self):
        self.assertEquals(self.calculate(5845, 6150), -305, "")

    def test0633(self):
        self.assertEquals(self.calculate(-2487, -270), -2217, "")

    def test0634(self):
        self.assertEquals(self.calculate(32363, 10852), 21511, "")

    def test0635(self):
        self.assertEquals(self.calculate(-10350, -30620), 20270, "")

    def test0636(self):
        self.assertEquals(self.calculate(4180, -9814), 13994, "")

    def test0637(self):
        self.assertEquals(self.calculate(26341, -32211), -6984, "")

    def test0638(self):
        self.assertEquals(self.calculate(5654, -4656), 10310, "")

    def test0639(self):
        self.assertEquals(self.calculate(21276, 11266), 10010, "")

    def test0640(self):
        self.assertEquals(self.calculate(-8536, -9821), 1285, "")

    def test0641(self):
        self.assertEquals(self.calculate(-15130, 11213), -26343, "")

    def test0642(self):
        self.assertEquals(self.calculate(-5564, 24749), -30313, "")

    def test0643(self):
        self.assertEquals(self.calculate(14482, -5812), 20294, "")

    def test0644(self):
        self.assertEquals(self.calculate(9561, -23879), -32096, "")

    def test0645(self):
        self.assertEquals(self.calculate(29627, -17243), -18666, "")

    def test0646(self):
        self.assertEquals(self.calculate(-13792, 32655), 19089, "")

    def test0647(self):
        self.assertEquals(self.calculate(-15406, -4932), -10474, "")

    def test0648(self):
        self.assertEquals(self.calculate(20982, 32692), -11710, "")

    def test0649(self):
        self.assertEquals(self.calculate(13450, 14658), -1208, "")

    def test0650(self):
        self.assertEquals(self.calculate(20121, 22510), -2389, "")

    def test0651(self):
        self.assertEquals(self.calculate(-21780, -27188), 5408, "")

    def test0652(self):
        self.assertEquals(self.calculate(2736, -32589), -30211, "")

    def test0653(self):
        self.assertEquals(self.calculate(9103, 268), 8835, "")

    def test0654(self):
        self.assertEquals(self.calculate(32124, 13524), 18600, "")

    def test0655(self):
        self.assertEquals(self.calculate(-23457, 17233), 24846, "")

    def test0656(self):
        self.assertEquals(self.calculate(21670, 841), 20829, "")

    def test0657(self):
        self.assertEquals(self.calculate(-31902, 30805), 2829, "")

    def test0658(self):
        self.assertEquals(self.calculate(-8853, -25264), 16411, "")

    def test0659(self):
        self.assertEquals(self.calculate(12259, -1714), 13973, "")

    def test0660(self):
        self.assertEquals(self.calculate(19746, 24481), -4735, "")

    def test0661(self):
        self.assertEquals(self.calculate(12180, -8110), 20290, "")

    def test0662(self):
        self.assertEquals(self.calculate(-21030, -17258), -3772, "")

    def test0663(self):
        self.assertEquals(self.calculate(9108, 23912), -14804, "")

    def test0664(self):
        self.assertEquals(self.calculate(-25034, 3302), -28336, "")

    def test0665(self):
        self.assertEquals(self.calculate(22069, 1046), 21023, "")

    def test0666(self):
        self.assertEquals(self.calculate(-8767, -13472), 4705, "")

    def test0667(self):
        self.assertEquals(self.calculate(-30019, -154), -29865, "")

    def test0668(self):
        self.assertEquals(self.calculate(-30370, 20011), 15155, "")

    def test0669(self):
        self.assertEquals(self.calculate(-1935, -11255), 9320, "")

    def test0670(self):
        self.assertEquals(self.calculate(-29457, 28526), 7553, "")

    def test0671(self):
        self.assertEquals(self.calculate(-28536, -30440), 1904, "")

    def test0672(self):
        self.assertEquals(self.calculate(5774, -30558), -29204, "")

    def test0673(self):
        self.assertEquals(self.calculate(28140, 3762), 24378, "")

    def test0674(self):
        self.assertEquals(self.calculate(-10240, 20959), -31199, "")

    def test0675(self):
        self.assertEquals(self.calculate(16651, 32249), -15598, "")

    def test0676(self):
        self.assertEquals(self.calculate(1104, -10469), 11573, "")

    def test0677(self):
        self.assertEquals(self.calculate(28986, -10335), -26215, "")

    def test0678(self):
        self.assertEquals(self.calculate(10407, -4557), 14964, "")

    def test0679(self):
        self.assertEquals(self.calculate(21258, 9396), 11862, "")

    def test0680(self):
        self.assertEquals(self.calculate(577, -18512), 19089, "")

    def test0681(self):
        self.assertEquals(self.calculate(-5345, 32485), 27706, "")

    def test0682(self):
        self.assertEquals(self.calculate(-6401, 16403), -22804, "")

    def test0683(self):
        self.assertEquals(self.calculate(3932, -25961), 29893, "")

    def test0684(self):
        self.assertEquals(self.calculate(-24813, 21064), 19659, "")

    def test0685(self):
        self.assertEquals(self.calculate(-7472, -6038), -1434, "")

    def test0686(self):
        self.assertEquals(self.calculate(-24550, -24490), -60, "")

    def test0687(self):
        self.assertEquals(self.calculate(16592, -12290), 28882, "")

    def test0688(self):
        self.assertEquals(self.calculate(27943, 26532), 1411, "")

    def test0689(self):
        self.assertEquals(self.calculate(18442, 23372), -4930, "")

    def test0690(self):
        self.assertEquals(self.calculate(29998, -21552), -13986, "")

    def test0691(self):
        self.assertEquals(self.calculate(23007, 4404), 18603, "")

    def test0692(self):
        self.assertEquals(self.calculate(-12372, -1422), -10950, "")

    def test0693(self):
        self.assertEquals(self.calculate(27043, -11611), -26882, "")

    def test0694(self):
        self.assertEquals(self.calculate(-20756, 27859), 16921, "")

    def test0695(self):
        self.assertEquals(self.calculate(-14078, 15474), -29552, "")

    def test0696(self):
        self.assertEquals(self.calculate(25523, 8313), 17210, "")

    def test0697(self):
        self.assertEquals(self.calculate(2053, 32432), -30379, "")

    def test0698(self):
        self.assertEquals(self.calculate(3637, 26628), -22991, "")

    def test0699(self):
        self.assertEquals(self.calculate(28002, -12522), -25012, "")

    def test0700(self):
        self.assertEquals(self.calculate(-4806, -15561), 10755, "")

    def test0701(self):
        self.assertEquals(self.calculate(-5315, 8412), -13727, "")

    def test0702(self):
        self.assertEquals(self.calculate(21005, -16434), -28097, "")

    def test0703(self):
        self.assertEquals(self.calculate(-14823, -8578), -6245, "")

    def test0704(self):
        self.assertEquals(self.calculate(18162, 2726), 15436, "")

    def test0705(self):
        self.assertEquals(self.calculate(-30914, 3827), 30795, "")

    def test0706(self):
        self.assertEquals(self.calculate(7998, 3776), 4222, "")

    def test0707(self):
        self.assertEquals(self.calculate(15414, 4244), 11170, "")

    def test0708(self):
        self.assertEquals(self.calculate(18078, 2325), 15753, "")

    def test0709(self):
        self.assertEquals(self.calculate(-9230, -27467), 18237, "")

    def test0710(self):
        self.assertEquals(self.calculate(-7401, 2130), -9531, "")

    def test0711(self):
        self.assertEquals(self.calculate(-21813, -7201), -14612, "")

    def test0712(self):
        self.assertEquals(self.calculate(3274, 32262), -28988, "")

    def test0713(self):
        self.assertEquals(self.calculate(20313, 12404), 7909, "")

    def test0714(self):
        self.assertEquals(self.calculate(-19721, -21978), 2257, "")

    def test0715(self):
        self.assertEquals(self.calculate(-15981, 16510), -32491, "")

    def test0716(self):
        self.assertEquals(self.calculate(19192, -24527), -21817, "")

    def test0717(self):
        self.assertEquals(self.calculate(604, 27401), -26797, "")

    def test0718(self):
        self.assertEquals(self.calculate(21011, 25122), -4111, "")

    def test0719(self):
        self.assertEquals(self.calculate(-10696, 20657), -31353, "")

    def test0720(self):
        self.assertEquals(self.calculate(29544, -28047), -7945, "")

    def test0721(self):
        self.assertEquals(self.calculate(-27576, -4251), -23325, "")

    def test0722(self):
        self.assertEquals(self.calculate(11337, -19025), 30362, "")

    def test0723(self):
        self.assertEquals(self.calculate(32659, -28578), -4299, "")

    def test0724(self):
        self.assertEquals(self.calculate(-139, 12742), -12881, "")

    def test0725(self):
        self.assertEquals(self.calculate(31463, 20636), 10827, "")

    def test0726(self):
        self.assertEquals(self.calculate(-24809, 14648), 26079, "")

    def test0727(self):
        self.assertEquals(self.calculate(-2565, 29310), -31875, "")

    def test0728(self):
        self.assertEquals(self.calculate(23673, -5599), 29272, "")

    def test0729(self):
        self.assertEquals(self.calculate(21568, -22064), -21904, "")

    def test0730(self):
        self.assertEquals(self.calculate(435, 150), 285, "")

    def test0731(self):
        self.assertEquals(self.calculate(-1380, -29073), 27693, "")

    def test0732(self):
        self.assertEquals(self.calculate(-4372, -9472), 5100, "")

    def test0733(self):
        self.assertEquals(self.calculate(16590, -25842), -23104, "")

    def test0734(self):
        self.assertEquals(self.calculate(22759, 32231), -9472, "")

    def test0735(self):
        self.assertEquals(self.calculate(5627, 4345), 1282, "")

    def test0736(self):
        self.assertEquals(self.calculate(20071, -20450), -25015, "")

    def test0737(self):
        self.assertEquals(self.calculate(-20219, -825), -19394, "")

    def test0738(self):
        self.assertEquals(self.calculate(-3213, 31800), 30523, "")

    def test0739(self):
        self.assertEquals(self.calculate(-13568, 525), -14093, "")

    def test0740(self):
        self.assertEquals(self.calculate(-9303, 32175), 24058, "")

    def test0741(self):
        self.assertEquals(self.calculate(-23248, 4364), -27612, "")

    def test0742(self):
        self.assertEquals(self.calculate(8721, -11883), 20604, "")

    def test0743(self):
        self.assertEquals(self.calculate(-7220, 22886), -30106, "")

    def test0744(self):
        self.assertEquals(self.calculate(-25083, 11126), 29327, "")

    def test0745(self):
        self.assertEquals(self.calculate(-11901, 10412), -22313, "")

    def test0746(self):
        self.assertEquals(self.calculate(-23605, 995), -24600, "")

    def test0747(self):
        self.assertEquals(self.calculate(-24944, -4603), -20341, "")

    def test0748(self):
        self.assertEquals(self.calculate(-16634, 16703), 32199, "")

    def test0749(self):
        self.assertEquals(self.calculate(-32277, -15828), -16449, "")

    def test0750(self):
        self.assertEquals(self.calculate(-24660, -4861), -19799, "")

    def test0751(self):
        self.assertEquals(self.calculate(-179, -20898), 20719, "")

    def test0752(self):
        self.assertEquals(self.calculate(6609, 287), 6322, "")

    def test0753(self):
        self.assertEquals(self.calculate(13997, 18718), -4721, "")

    def test0754(self):
        self.assertEquals(self.calculate(20242, 29319), -9077, "")

    def test0755(self):
        self.assertEquals(self.calculate(-263, 16630), -16893, "")

    def test0756(self):
        self.assertEquals(self.calculate(-6231, -2599), -3632, "")

    def test0757(self):
        self.assertEquals(self.calculate(-20788, -5054), -15734, "")

    def test0758(self):
        self.assertEquals(self.calculate(-15203, 20980), 29353, "")

    def test0759(self):
        self.assertEquals(self.calculate(-30554, 6636), 28346, "")

    def test0760(self):
        self.assertEquals(self.calculate(-31035, 11321), 23180, "")

    def test0761(self):
        self.assertEquals(self.calculate(20415, 3099), 17316, "")

    def test0762(self):
        self.assertEquals(self.calculate(24641, -2617), 27258, "")

    def test0763(self):
        self.assertEquals(self.calculate(17127, 21239), -4112, "")

    def test0764(self):
        self.assertEquals(self.calculate(-31044, 16004), 18488, "")

    def test0765(self):
        self.assertEquals(self.calculate(5663, 25485), -19822, "")

    def test0766(self):
        self.assertEquals(self.calculate(-12038, 25239), 28259, "")

    def test0767(self):
        self.assertEquals(self.calculate(-19744, 31936), 13856, "")

    def test0768(self):
        self.assertEquals(self.calculate(31393, -5396), -28747, "")

    def test0769(self):
        self.assertEquals(self.calculate(11704, 20971), -9267, "")

    def test0770(self):
        self.assertEquals(self.calculate(1678, 29210), -27532, "")

    def test0771(self):
        self.assertEquals(self.calculate(-1658, -2768), 1110, "")

    def test0772(self):
        self.assertEquals(self.calculate(17450, 15672), 1778, "")

    def test0773(self):
        self.assertEquals(self.calculate(-17179, 23742), 24615, "")

    def test0774(self):
        self.assertEquals(self.calculate(-11084, 16331), -27415, "")

    def test0775(self):
        self.assertEquals(self.calculate(-19060, -29089), 10029, "")

    def test0776(self):
        self.assertEquals(self.calculate(19320, 29533), -10213, "")

    def test0777(self):
        self.assertEquals(self.calculate(14074, 26540), -12466, "")

    def test0778(self):
        self.assertEquals(self.calculate(3646, -19792), 23438, "")

    def test0779(self):
        self.assertEquals(self.calculate(30579, 20592), 9987, "")

    def test0780(self):
        self.assertEquals(self.calculate(-6649, -13088), 6439, "")

    def test0781(self):
        self.assertEquals(self.calculate(-2849, 14210), -17059, "")

    def test0782(self):
        self.assertEquals(self.calculate(31819, 11642), 20177, "")

    def test0783(self):
        self.assertEquals(self.calculate(-15362, -12626), -2736, "")

    def test0784(self):
        self.assertEquals(self.calculate(15497, 9815), 5682, "")

    def test0785(self):
        self.assertEquals(self.calculate(-4529, -6782), 2253, "")

    def test0786(self):
        self.assertEquals(self.calculate(-25033, -10448), -14585, "")

    def test0787(self):
        self.assertEquals(self.calculate(13102, -20450), -31984, "")

    def test0788(self):
        self.assertEquals(self.calculate(-1402, -23306), 21904, "")

    def test0789(self):
        self.assertEquals(self.calculate(10597, -23555), -31384, "")

    def test0790(self):
        self.assertEquals(self.calculate(-27999, -25501), -2498, "")

    def test0791(self):
        self.assertEquals(self.calculate(-7699, -20288), 12589, "")

    def test0792(self):
        self.assertEquals(self.calculate(-30977, -8627), -22350, "")

    def test0793(self):
        self.assertEquals(self.calculate(12995, -8075), 21070, "")

    def test0794(self):
        self.assertEquals(self.calculate(-4633, -30354), 25721, "")

    def test0795(self):
        self.assertEquals(self.calculate(10915, -1456), 12371, "")

    def test0796(self):
        self.assertEquals(self.calculate(-20296, 17605), 27635, "")

    def test0797(self):
        self.assertEquals(self.calculate(30615, -14265), -20656, "")

    def test0798(self):
        self.assertEquals(self.calculate(4014, 17510), -13496, "")

    def test0799(self):
        self.assertEquals(self.calculate(31, 22830), -22799, "")

    def test0800(self):
        self.assertEquals(self.calculate(28544, -9280), -27712, "")

    def test0801(self):
        self.assertEquals(self.calculate(22625, 912), 21713, "")

    def test0802(self):
        self.assertEquals(self.calculate(-15809, -19532), 3723, "")

    def test0803(self):
        self.assertEquals(self.calculate(-22849, -26388), 3539, "")

    def test0804(self):
        self.assertEquals(self.calculate(-6757, 7746), -14503, "")

    def test0805(self):
        self.assertEquals(self.calculate(-27415, -7488), -19927, "")

    def test0806(self):
        self.assertEquals(self.calculate(12006, -3627), 15633, "")

    def test0807(self):
        self.assertEquals(self.calculate(1129, -7669), 8798, "")

    def test0808(self):
        self.assertEquals(self.calculate(15122, 6645), 8477, "")

    def test0809(self):
        self.assertEquals(self.calculate(-24925, -31977), 7052, "")

    def test0810(self):
        self.assertEquals(self.calculate(26175, -9439), -29922, "")

    def test0811(self):
        self.assertEquals(self.calculate(-28966, 23257), 13313, "")

    def test0812(self):
        self.assertEquals(self.calculate(923, 31106), -30183, "")

    def test0813(self):
        self.assertEquals(self.calculate(17569, 2147), 15422, "")

    def test0814(self):
        self.assertEquals(self.calculate(13790, 30987), -17197, "")

    def test0815(self):
        self.assertEquals(self.calculate(-2139, 12308), -14447, "")

    def test0816(self):
        self.assertEquals(self.calculate(-17653, -5214), -12439, "")

    def test0817(self):
        self.assertEquals(self.calculate(-28569, -27483), -1086, "")

    def test0818(self):
        self.assertEquals(self.calculate(-9446, 511), -9957, "")

    def test0819(self):
        self.assertEquals(self.calculate(-26470, 4108), -30578, "")

    def test0820(self):
        self.assertEquals(self.calculate(10139, -8543), 18682, "")

    def test0821(self):
        self.assertEquals(self.calculate(14720, -10834), 25554, "")

    def test0822(self):
        self.assertEquals(self.calculate(13885, -9302), 23187, "")

    def test0823(self):
        self.assertEquals(self.calculate(-24622, 18865), 22049, "")

    def test0824(self):
        self.assertEquals(self.calculate(-28555, -12278), -16277, "")

    def test0825(self):
        self.assertEquals(self.calculate(21768, -1566), 23334, "")

    def test0826(self):
        self.assertEquals(self.calculate(-20231, 11725), -31956, "")

    def test0827(self):
        self.assertEquals(self.calculate(-1219, 8592), -9811, "")

    def test0828(self):
        self.assertEquals(self.calculate(23159, 14968), 8191, "")

    def test0829(self):
        self.assertEquals(self.calculate(16457, -17570), -31509, "")

    def test0830(self):
        self.assertEquals(self.calculate(17243, -27420), -20873, "")

    def test0831(self):
        self.assertEquals(self.calculate(2630, 10325), -7695, "")

    def test0832(self):
        self.assertEquals(self.calculate(-4126, 5079), -9205, "")

    def test0833(self):
        self.assertEquals(self.calculate(8585, -4516), 13101, "")

    def test0834(self):
        self.assertEquals(self.calculate(31518, 17464), 14054, "")

    def test0835(self):
        self.assertEquals(self.calculate(-7242, -15018), 7776, "")

    def test0836(self):
        self.assertEquals(self.calculate(-8018, -23368), 15350, "")

    def test0837(self):
        self.assertEquals(self.calculate(-29373, 18318), 17845, "")

    def test0838(self):
        self.assertEquals(self.calculate(-13193, 28430), 23913, "")

    def test0839(self):
        self.assertEquals(self.calculate(-25141, 8564), 31831, "")

    def test0840(self):
        self.assertEquals(self.calculate(20789, 22105), -1316, "")

    def test0841(self):
        self.assertEquals(self.calculate(14937, 22886), -7949, "")

    def test0842(self):
        self.assertEquals(self.calculate(-29609, 2614), -32223, "")

    def test0843(self):
        self.assertEquals(self.calculate(-9251, 7866), -17117, "")

    def test0844(self):
        self.assertEquals(self.calculate(6246, 3034), 3212, "")

    def test0845(self):
        self.assertEquals(self.calculate(-24027, -30711), 6684, "")

    def test0846(self):
        self.assertEquals(self.calculate(-3306, 23150), -26456, "")

    def test0847(self):
        self.assertEquals(self.calculate(29753, 26768), 2985, "")

    def test0848(self):
        self.assertEquals(self.calculate(-32073, -22403), -9670, "")

    def test0849(self):
        self.assertEquals(self.calculate(15231, 16794), -1563, "")

    def test0850(self):
        self.assertEquals(self.calculate(21086, 23750), -2664, "")

    def test0851(self):
        self.assertEquals(self.calculate(-1269, -4089), 2820, "")

    def test0852(self):
        self.assertEquals(self.calculate(29105, 29873), -768, "")

    def test0853(self):
        self.assertEquals(self.calculate(2626, -12468), 15094, "")

    def test0854(self):
        self.assertEquals(self.calculate(25846, 14914), 10932, "")

    def test0855(self):
        self.assertEquals(self.calculate(-14587, -5884), -8703, "")

    def test0856(self):
        self.assertEquals(self.calculate(2323, -9302), 11625, "")

    def test0857(self):
        self.assertEquals(self.calculate(17107, 22157), -5050, "")

    def test0858(self):
        self.assertEquals(self.calculate(13490, -22426), -29620, "")

    def test0859(self):
        self.assertEquals(self.calculate(-31410, -29059), -2351, "")

    def test0860(self):
        self.assertEquals(self.calculate(-11018, -14460), 3442, "")

    def test0861(self):
        self.assertEquals(self.calculate(-27476, -3), -27473, "")

    def test0862(self):
        self.assertEquals(self.calculate(17328, -31171), -17037, "")

    def test0863(self):
        self.assertEquals(self.calculate(16360, 19646), -3286, "")

    def test0864(self):
        self.assertEquals(self.calculate(-19111, 26706), 19719, "")

    def test0865(self):
        self.assertEquals(self.calculate(-32457, -1812), -30645, "")

    def test0866(self):
        self.assertEquals(self.calculate(16736, -14861), 31597, "")

    def test0867(self):
        self.assertEquals(self.calculate(1316, -3298), 4614, "")

    def test0868(self):
        self.assertEquals(self.calculate(22644, 4736), 17908, "")

    def test0869(self):
        self.assertEquals(self.calculate(29165, -22754), -13617, "")

    def test0870(self):
        self.assertEquals(self.calculate(-5492, 20950), -26442, "")

    def test0871(self):
        self.assertEquals(self.calculate(29431, 19715), 9716, "")

    def test0872(self):
        self.assertEquals(self.calculate(-9814, -20892), 11078, "")

    def test0873(self):
        self.assertEquals(self.calculate(22921, -15392), -27223, "")

    def test0874(self):
        self.assertEquals(self.calculate(31425, 15060), 16365, "")

    def test0875(self):
        self.assertEquals(self.calculate(-27916, -25790), -2126, "")

    def test0876(self):
        self.assertEquals(self.calculate(28183, 13832), 14351, "")

    def test0877(self):
        self.assertEquals(self.calculate(-3496, 29326), 32714, "")

    def test0878(self):
        self.assertEquals(self.calculate(11308, -14896), 26204, "")

    def test0879(self):
        self.assertEquals(self.calculate(-10058, 22809), 32669, "")

    def test0880(self):
        self.assertEquals(self.calculate(-13985, 2556), -16541, "")

    def test0881(self):
        self.assertEquals(self.calculate(9570, -13818), 23388, "")

    def test0882(self):
        self.assertEquals(self.calculate(30517, 23426), 7091, "")

    def test0883(self):
        self.assertEquals(self.calculate(10341, -11732), 22073, "")

    def test0884(self):
        self.assertEquals(self.calculate(-8060, -12147), 4087, "")

    def test0885(self):
        self.assertEquals(self.calculate(-2151, -6185), 4034, "")

    def test0886(self):
        self.assertEquals(self.calculate(6887, -8853), 15740, "")

    def test0887(self):
        self.assertEquals(self.calculate(7278, -31166), -27092, "")

    def test0888(self):
        self.assertEquals(self.calculate(-20766, 24293), 20477, "")

    def test0889(self):
        self.assertEquals(self.calculate(-9141, -10947), 1806, "")

    def test0890(self):
        self.assertEquals(self.calculate(6231, -753), 6984, "")

    def test0891(self):
        self.assertEquals(self.calculate(30886, -23830), -10820, "")

    def test0892(self):
        self.assertEquals(self.calculate(18224, -9536), 27760, "")

    def test0893(self):
        self.assertEquals(self.calculate(-29714, 21845), 13977, "")

    def test0894(self):
        self.assertEquals(self.calculate(18460, -9542), 28002, "")

    def test0895(self):
        self.assertEquals(self.calculate(-13689, 15103), -28792, "")

    def test0896(self):
        self.assertEquals(self.calculate(-19115, -23097), 3982, "")

    def test0897(self):
        self.assertEquals(self.calculate(-4222, 24263), -28485, "")

    def test0898(self):
        self.assertEquals(self.calculate(4669, 23921), -19252, "")

    def test0899(self):
        self.assertEquals(self.calculate(7433, 17973), -10540, "")

    def test0900(self):
        self.assertEquals(self.calculate(-13035, 782), -13817, "")

    def test0901(self):
        self.assertEquals(self.calculate(-24269, 16267), 25000, "")

    def test0902(self):
        self.assertEquals(self.calculate(-15923, -22450), 6527, "")

    def test0903(self):
        self.assertEquals(self.calculate(-14461, 23454), 27621, "")

    def test0904(self):
        self.assertEquals(self.calculate(-4800, 31899), 28837, "")

    def test0905(self):
        self.assertEquals(self.calculate(25799, 18309), 7490, "")

    def test0906(self):
        self.assertEquals(self.calculate(-8078, -100), -7978, "")

    def test0907(self):
        self.assertEquals(self.calculate(32523, 21564), 10959, "")

    def test0908(self):
        self.assertEquals(self.calculate(24056, 23284), 772, "")

    def test0909(self):
        self.assertEquals(self.calculate(-26340, -27266), 926, "")

    def test0910(self):
        self.assertEquals(self.calculate(-6602, -28), -6574, "")

    def test0911(self):
        self.assertEquals(self.calculate(6443, -7327), 13770, "")

    def test0912(self):
        self.assertEquals(self.calculate(-13339, 5378), -18717, "")

    def test0913(self):
        self.assertEquals(self.calculate(19123, 1966), 17157, "")

    def test0914(self):
        self.assertEquals(self.calculate(28741, -31475), -5320, "")

    def test0915(self):
        self.assertEquals(self.calculate(-17406, 21633), 26497, "")

    def test0916(self):
        self.assertEquals(self.calculate(-2788, 30743), 32005, "")

    def test0917(self):
        self.assertEquals(self.calculate(15308, 29905), -14597, "")

    def test0918(self):
        self.assertEquals(self.calculate(-29856, -10072), -19784, "")

    def test0919(self):
        self.assertEquals(self.calculate(6514, -14240), 20754, "")

    def test0920(self):
        self.assertEquals(self.calculate(24382, -10539), -30615, "")

    def test0921(self):
        self.assertEquals(self.calculate(10089, 17083), -6994, "")

    def test0922(self):
        self.assertEquals(self.calculate(8947, -21308), 30255, "")

    def test0923(self):
        self.assertEquals(self.calculate(9024, -29530), -26982, "")

    def test0924(self):
        self.assertEquals(self.calculate(3945, -29933), -31658, "")

    def test0925(self):
        self.assertEquals(self.calculate(30968, -2468), -32100, "")

    def test0926(self):
        self.assertEquals(self.calculate(27693, -15068), -22775, "")

    def test0927(self):
        self.assertEquals(self.calculate(-9449, 22782), -32231, "")

    def test0928(self):
        self.assertEquals(self.calculate(5888, -17607), 23495, "")

    def test0929(self):
        self.assertEquals(self.calculate(-11850, 26061), 27625, "")

    def test0930(self):
        self.assertEquals(self.calculate(13844, 662), 13182, "")

    def test0931(self):
        self.assertEquals(self.calculate(-4218, -3531), -687, "")

    def test0932(self):
        self.assertEquals(self.calculate(-7046, -10984), 3938, "")

    def test0933(self):
        self.assertEquals(self.calculate(-20940, 11184), -32124, "")

    def test0934(self):
        self.assertEquals(self.calculate(-4106, -32385), 28279, "")

    def test0935(self):
        self.assertEquals(self.calculate(16339, -3646), 19985, "")

    def test0936(self):
        self.assertEquals(self.calculate(-23203, -5299), -17904, "")

    def test0937(self):
        self.assertEquals(self.calculate(-6184, 2642), -8826, "")

    def test0938(self):
        self.assertEquals(self.calculate(27004, 8310), 18694, "")

    def test0939(self):
        self.assertEquals(self.calculate(-3707, -24546), 20839, "")

    def test0940(self):
        self.assertEquals(self.calculate(17839, 21408), -3569, "")

    def test0941(self):
        self.assertEquals(self.calculate(25786, 2222), 23564, "")

    def test0942(self):
        self.assertEquals(self.calculate(-26314, -13154), -13160, "")

    def test0943(self):
        self.assertEquals(self.calculate(16374, 2446), 13928, "")

    def test0944(self):
        self.assertEquals(self.calculate(-12846, 5802), -18648, "")

    def test0945(self):
        self.assertEquals(self.calculate(-12263, 14546), -26809, "")

    def test0946(self):
        self.assertEquals(self.calculate(19063, -8707), 27770, "")

    def test0947(self):
        self.assertEquals(self.calculate(-25220, -32276), 7056, "")

    def test0948(self):
        self.assertEquals(self.calculate(-31777, -20051), -11726, "")

    def test0949(self):
        self.assertEquals(self.calculate(-3714, -29487), 25773, "")

    def test0950(self):
        self.assertEquals(self.calculate(3671, 8656), -4985, "")

    def test0951(self):
        self.assertEquals(self.calculate(-4039, -9129), 5090, "")

    def test0952(self):
        self.assertEquals(self.calculate(-6275, 26453), -32728, "")

    def test0953(self):
        self.assertEquals(self.calculate(24960, 21451), 3509, "")

    def test0954(self):
        self.assertEquals(self.calculate(5098, -30800), -29638, "")

    def test0955(self):
        self.assertEquals(self.calculate(6030, -14927), 20957, "")

    def test0956(self):
        self.assertEquals(self.calculate(12498, 32199), -19701, "")

    def test0957(self):
        self.assertEquals(self.calculate(-25269, -29369), 4100, "")

    def test0958(self):
        self.assertEquals(self.calculate(-27690, 17480), 20366, "")

    def test0959(self):
        self.assertEquals(self.calculate(-31281, 18433), 15822, "")

    def test0960(self):
        self.assertEquals(self.calculate(26149, -6199), 32348, "")

    def test0961(self):
        self.assertEquals(self.calculate(27585, 29944), -2359, "")

    def test0962(self):
        self.assertEquals(self.calculate(23389, 24304), -915, "")

    def test0963(self):
        self.assertEquals(self.calculate(732, 10305), -9573, "")

    def test0964(self):
        self.assertEquals(self.calculate(-21503, -25858), 4355, "")

    def test0965(self):
        self.assertEquals(self.calculate(-7744, -12333), 4589, "")

    def test0966(self):
        self.assertEquals(self.calculate(-20446, 20551), 24539, "")

    def test0967(self):
        self.assertEquals(self.calculate(18887, 6991), 11896, "")

    def test0968(self):
        self.assertEquals(self.calculate(3918, 22180), -18262, "")

    def test0969(self):
        self.assertEquals(self.calculate(-7513, -22583), 15070, "")

    def test0970(self):
        self.assertEquals(self.calculate(26101, -22554), -16881, "")

    def test0971(self):
        self.assertEquals(self.calculate(-27887, 30319), 7330, "")

    def test0972(self):
        self.assertEquals(self.calculate(13590, -10832), 24422, "")

    def test0973(self):
        self.assertEquals(self.calculate(1782, -24564), 26346, "")

    def test0974(self):
        self.assertEquals(self.calculate(-4348, 21015), -25363, "")

    def test0975(self):
        self.assertEquals(self.calculate(-19604, 24978), 20954, "")

    def test0976(self):
        self.assertEquals(self.calculate(-26072, 8247), 31217, "")

    def test0977(self):
        self.assertEquals(self.calculate(-16381, -30641), 14260, "")

    def test0978(self):
        self.assertEquals(self.calculate(-10487, 32735), 22314, "")

    def test0979(self):
        self.assertEquals(self.calculate(17258, 14901), 2357, "")

    def test0980(self):
        self.assertEquals(self.calculate(15719, 2497), 13222, "")

    def test0981(self):
        self.assertEquals(self.calculate(563, 21413), -20850, "")

    def test0982(self):
        self.assertEquals(self.calculate(18301, 1645), 16656, "")

    def test0983(self):
        self.assertEquals(self.calculate(83, -19245), 19328, "")

    def test0984(self):
        self.assertEquals(self.calculate(29435, 28401), 1034, "")

    def test0985(self):
        self.assertEquals(self.calculate(-3982, -25302), 21320, "")

    def test0986(self):
        self.assertEquals(self.calculate(32646, 2370), 30276, "")

    def test0987(self):
        self.assertEquals(self.calculate(27854, -15694), -21988, "")

    def test0988(self):
        self.assertEquals(self.calculate(39, -28372), 28411, "")

    def test0989(self):
        self.assertEquals(self.calculate(-27077, 7208), 31251, "")

    def test0990(self):
        self.assertEquals(self.calculate(15686, 30292), -14606, "")

    def test0991(self):
        self.assertEquals(self.calculate(1021, 6688), -5667, "")

    def test0992(self):
        self.assertEquals(self.calculate(-6707, 7047), -13754, "")

    def test0993(self):
        self.assertEquals(self.calculate(-22573, 25855), 17108, "")

    def test0994(self):
        self.assertEquals(self.calculate(30655, 6114), 24541, "")

    def test0995(self):
        self.assertEquals(self.calculate(23374, 14534), 8840, "")

    def test0996(self):
        self.assertEquals(self.calculate(-28134, -16528), -11606, "")

    def test0997(self):
        self.assertEquals(self.calculate(-24202, -11632), -12570, "")

    def test0998(self):
        self.assertEquals(self.calculate(-15138, 13532), -28670, "")

    def test0999(self):
        self.assertEquals(self.calculate(22603, -6579), 29182, "")

    def test1000(self):
        self.assertEquals(self.calculate(-27999, -17179), -10820, "")

    def test1001(self):
        self.assertEquals(self.calculate(-11387, -13648), 2261, "")

    def test1002(self):
        self.assertEquals(self.calculate(29443, -17174), -18919, "")

    def test1003(self):
        self.assertEquals(self.calculate(18366, -5100), 23466, "")

    def test1004(self):
        self.assertEquals(self.calculate(11379, 29257), -17878, "")

    def test1005(self):
        self.assertEquals(self.calculate(23184, 4514), 18670, "")

    def test1006(self):
        self.assertEquals(self.calculate(18969, -8048), 27017, "")

    def test1007(self):
        self.assertEquals(self.calculate(28873, -25082), -11581, "")

    def test1008(self):
        self.assertEquals(self.calculate(-6789, 22031), -28820, "")

    def test1009(self):
        self.assertEquals(self.calculate(26491, -11150), -27895, "")

    def test1010(self):
        self.assertEquals(self.calculate(-18658, -15677), -2981, "")

    def test1011(self):
        self.assertEquals(self.calculate(7560, 25375), -17815, "")

    def test1012(self):
        self.assertEquals(self.calculate(5025, -23769), 28794, "")

    def test1013(self):
        self.assertEquals(self.calculate(-19998, -24865), 4867, "")

    def test1014(self):
        self.assertEquals(self.calculate(5519, 6690), -1171, "")

    def test1015(self):
        self.assertEquals(self.calculate(-10539, 15644), -26183, "")

    def test1016(self):
        self.assertEquals(self.calculate(-24195, 13636), 27705, "")

    def test1017(self):
        self.assertEquals(self.calculate(6967, -17941), 24908, "")

    def test1018(self):
        self.assertEquals(self.calculate(-19807, 31844), 13885, "")

    def test1019(self):
        self.assertEquals(self.calculate(-3606, 3499), -7105, "")

    def test1020(self):
        self.assertEquals(self.calculate(23760, 18793), 4967, "")

    def test1021(self):
        self.assertEquals(self.calculate(30459, 10828), 19631, "")

    def test1022(self):
        self.assertEquals(self.calculate(2165, -5845), 8010, "")

    def test1023(self):
        self.assertEquals(self.calculate(20677, 21489), -812, "")


class TestVM_Sub_IntLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushL(rhs)
        v.VM_Sub()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(23920, 235896028), -235872108)

    def test0001(self):
        self.assertEquals(self.calculate(30205, -1894310897), 1894341102)

    def test0002(self):
        self.assertEquals(self.calculate(-14572, -1950817515), 1950802943)

    def test0003(self):
        self.assertEquals(self.calculate(8015, -42094374), 42102389)

    def test0004(self):
        self.assertEquals(self.calculate(-26322, -1833906218), 1833879896)

    def test0005(self):
        self.assertEquals(self.calculate(30096, -755959699), 755989795)

    def test0006(self):
        self.assertEquals(self.calculate(-22390, 1695839074), -1695861464)

    def test0007(self):
        self.assertEquals(self.calculate(26690, 889449186), -889422496)

    def test0008(self):
        self.assertEquals(self.calculate(10732, 1815390156), -1815379424)

    def test0009(self):
        self.assertEquals(self.calculate(18519, -1685266270), 1685284789)

    def test0010(self):
        self.assertEquals(self.calculate(-7807, -2144122013), 2144114206)

    def test0011(self):
        self.assertEquals(self.calculate(-16412, -1257815588), 1257799176)

    def test0012(self):
        self.assertEquals(self.calculate(-22743, 389589433), -389612176)

    def test0013(self):
        self.assertEquals(self.calculate(9009, -765962266), 765971275)

    def test0014(self):
        self.assertEquals(self.calculate(12533, 1374839030), -1374826497)

    def test0015(self):
        self.assertEquals(self.calculate(-17450, 643363069), -643380519)

    def test0016(self):
        self.assertEquals(self.calculate(22632, -382086002), 382108634)

    def test0017(self):
        self.assertEquals(self.calculate(-16985, 2120109744), -2120126729)

    def test0018(self):
        self.assertEquals(self.calculate(1770, 1346931113), -1346929343)

    def test0019(self):
        self.assertEquals(self.calculate(-12685, -1419806982), 1419794297)

    def test0020(self):
        self.assertEquals(self.calculate(-3971, 1254985788), -1254989759)

    def test0021(self):
        self.assertEquals(self.calculate(32227, 547203036), -547170809)

    def test0022(self):
        self.assertEquals(self.calculate(-25985, 400952624), -400978609)

    def test0023(self):
        self.assertEquals(self.calculate(-25805, -213891625), 213865820)

    def test0024(self):
        self.assertEquals(self.calculate(7728, -192980154), 192987882)

    def test0025(self):
        self.assertEquals(self.calculate(-31908, 416369004), -416400912)

    def test0026(self):
        self.assertEquals(self.calculate(-14284, -1153180453), 1153166169)

    def test0027(self):
        self.assertEquals(self.calculate(-1601, 1902179180), -1902180781)

    def test0028(self):
        self.assertEquals(self.calculate(1992, -715901633), 715903625)

    def test0029(self):
        self.assertEquals(self.calculate(-3723, -1198152171), 1198148448)

    def test0030(self):
        self.assertEquals(self.calculate(31861, -1715733933), 1715765794)

    def test0031(self):
        self.assertEquals(self.calculate(-26585, -529584673), 529558088)

    def test0032(self):
        self.assertEquals(self.calculate(1911, -1320880872), 1320882783)

    def test0033(self):
        self.assertEquals(self.calculate(29538, 1453295940), -1453266402)

    def test0034(self):
        self.assertEquals(self.calculate(5695, 218386706), -218381011)

    def test0035(self):
        self.assertEquals(self.calculate(21501, -40937756), 40959257)

    def test0036(self):
        self.assertEquals(self.calculate(15003, 739590888), -739575885)

    def test0037(self):
        self.assertEquals(self.calculate(25314, 1843477105), -1843451791)

    def test0038(self):
        self.assertEquals(self.calculate(9783, -1566162253), 1566172036)

    def test0039(self):
        self.assertEquals(self.calculate(-9530, -1561448493), 1561438963)

    def test0040(self):
        self.assertEquals(self.calculate(21303, 654776058), -654754755)

    def test0041(self):
        self.assertEquals(self.calculate(12742, 289196922), -289184180)

    def test0042(self):
        self.assertEquals(self.calculate(32722, 2093036276), -2093003554)

    def test0043(self):
        self.assertEquals(self.calculate(-457, 1827460075), -1827460532)

    def test0044(self):
        self.assertEquals(self.calculate(18652, 1608795852), -1608777200)

    def test0045(self):
        self.assertEquals(self.calculate(-30630, -38851562), 38820932)

    def test0046(self):
        self.assertEquals(self.calculate(-13693, 455753268), -455766961)

    def test0047(self):
        self.assertEquals(self.calculate(17780, 2002691395), -2002673615)

    def test0048(self):
        self.assertEquals(self.calculate(23200, -1788288380), 1788311580)

    def test0049(self):
        self.assertEquals(self.calculate(7044, -247979318), 247986362)

    def test0050(self):
        self.assertEquals(self.calculate(-23759, -946633530), 946609771)

    def test0051(self):
        self.assertEquals(self.calculate(-18893, 1562042812), -1562061705)

    def test0052(self):
        self.assertEquals(self.calculate(-28864, -2127052435), 2127023571)

    def test0053(self):
        self.assertEquals(self.calculate(-15959, -355559023), 355543064)

    def test0054(self):
        self.assertEquals(self.calculate(-4573, -1244177485), 1244172912)

    def test0055(self):
        self.assertEquals(self.calculate(30680, -935194790), 935225470)

    def test0056(self):
        self.assertEquals(self.calculate(-5439, 815831788), -815837227)

    def test0057(self):
        self.assertEquals(self.calculate(-24075, 273917641), -273941716)

    def test0058(self):
        self.assertEquals(self.calculate(22300, 227268523), -227246223)

    def test0059(self):
        self.assertEquals(self.calculate(9309, 700584887), -700575578)

    def test0060(self):
        self.assertEquals(self.calculate(-31757, 828466395), -828498152)

    def test0061(self):
        self.assertEquals(self.calculate(-3594, -2114018877), 2114015283)

    def test0062(self):
        self.assertEquals(self.calculate(-22029, 213535255), -213557284)

    def test0063(self):
        self.assertEquals(self.calculate(-23932, 168554370), -168578302)

    def test0064(self):
        self.assertEquals(self.calculate(20610, 924026048), -924005438)

    def test0065(self):
        self.assertEquals(self.calculate(4166, 1302404161), -1302399995)

    def test0066(self):
        self.assertEquals(self.calculate(4609, -1795528089), 1795532698)

    def test0067(self):
        self.assertEquals(self.calculate(15277, -759644389), 759659666)

    def test0068(self):
        self.assertEquals(self.calculate(23814, 1444435736), -1444411922)

    def test0069(self):
        self.assertEquals(self.calculate(-3436, 1369589531), -1369592967)

    def test0070(self):
        self.assertEquals(self.calculate(18938, 1383690521), -1383671583)

    def test0071(self):
        self.assertEquals(self.calculate(-9677, -1347344930), 1347335253)

    def test0072(self):
        self.assertEquals(self.calculate(25912, 279771828), -279745916)

    def test0073(self):
        self.assertEquals(self.calculate(-25061, -1806263674), 1806238613)

    def test0074(self):
        self.assertEquals(self.calculate(24312, -1482054651), 1482078963)

    def test0075(self):
        self.assertEquals(self.calculate(-24339, -2129715398), 2129691059)

    def test0076(self):
        self.assertEquals(self.calculate(30115, -23635819), 23665934)

    def test0077(self):
        self.assertEquals(self.calculate(-31704, -490503978), 490472274)

    def test0078(self):
        self.assertEquals(self.calculate(-29825, -1228502402), 1228472577)

    def test0079(self):
        self.assertEquals(self.calculate(-12586, 1343415696), -1343428282)

    def test0080(self):
        self.assertEquals(self.calculate(8033, 126241133), -126233100)

    def test0081(self):
        self.assertEquals(self.calculate(-32598, 2118784800), -2118817398)

    def test0082(self):
        self.assertEquals(self.calculate(-17399, 1343065500), -1343082899)

    def test0083(self):
        self.assertEquals(self.calculate(-27604, 476354444), -476382048)

    def test0084(self):
        self.assertEquals(self.calculate(-16523, 209322475), -209338998)

    def test0085(self):
        self.assertEquals(self.calculate(4855, 345730487), -345725632)

    def test0086(self):
        self.assertEquals(self.calculate(-7229, 1535219381), -1535226610)

    def test0087(self):
        self.assertEquals(self.calculate(-6111, 1108151803), -1108157914)

    def test0088(self):
        self.assertEquals(self.calculate(-30357, 1252788238), -1252818595)

    def test0089(self):
        self.assertEquals(self.calculate(-18253, 496558307), -496576560)

    def test0090(self):
        self.assertEquals(self.calculate(5700, 1693761360), -1693755660)

    def test0091(self):
        self.assertEquals(self.calculate(4483, 950113785), -950109302)

    def test0092(self):
        self.assertEquals(self.calculate(3661, 100230450), -100226789)

    def test0093(self):
        self.assertEquals(self.calculate(-14297, 1417593837), -1417608134)

    def test0094(self):
        self.assertEquals(self.calculate(-3911, -11288953), 11285042)

    def test0095(self):
        self.assertEquals(self.calculate(3881, 1452411032), -1452407151)

    def test0096(self):
        self.assertEquals(self.calculate(27979, 1802857973), -1802829994)

    def test0097(self):
        self.assertEquals(self.calculate(-29970, 2095047735), -2095077705)

    def test0098(self):
        self.assertEquals(self.calculate(-19396, -884155005), 884135609)

    def test0099(self):
        self.assertEquals(self.calculate(20505, 55789971), -55769466)

    def test0100(self):
        self.assertEquals(self.calculate(-23017, -1960075582), 1960052565)

    def test0101(self):
        self.assertEquals(self.calculate(-7966, -1945377498), 1945369532)

    def test0102(self):
        self.assertEquals(self.calculate(27779, 1753397646), -1753369867)

    def test0103(self):
        self.assertEquals(self.calculate(10008, 448579672), -448569664)

    def test0104(self):
        self.assertEquals(self.calculate(-3128, -2045236420), 2045233292)

    def test0105(self):
        self.assertEquals(self.calculate(24440, 994928930), -994904490)

    def test0106(self):
        self.assertEquals(self.calculate(17665, -2055064314), 2055081979)

    def test0107(self):
        self.assertEquals(self.calculate(31884, -1875023543), 1875055427)

    def test0108(self):
        self.assertEquals(self.calculate(17488, -744518799), 744536287)

    def test0109(self):
        self.assertEquals(self.calculate(-16403, 1154667222), -1154683625)

    def test0110(self):
        self.assertEquals(self.calculate(18861, -540827601), 540846462)

    def test0111(self):
        self.assertEquals(self.calculate(-13426, 1025240947), -1025254373)

    def test0112(self):
        self.assertEquals(self.calculate(-10948, 369345186), -369356134)

    def test0113(self):
        self.assertEquals(self.calculate(14022, 1661996313), -1661982291)

    def test0114(self):
        self.assertEquals(self.calculate(25925, -577714173), 577740098)

    def test0115(self):
        self.assertEquals(self.calculate(-10035, 872407775), -872417810)

    def test0116(self):
        self.assertEquals(self.calculate(-30079, 122023753), -122053832)

    def test0117(self):
        self.assertEquals(self.calculate(-29779, 1165935776), -1165965555)

    def test0118(self):
        self.assertEquals(self.calculate(-18042, -1845944122), 1845926080)

    def test0119(self):
        self.assertEquals(self.calculate(13450, 2092824517), -2092811067)

    def test0120(self):
        self.assertEquals(self.calculate(6209, -1090917166), 1090923375)

    def test0121(self):
        self.assertEquals(self.calculate(19595, -253183033), 253202628)

    def test0122(self):
        self.assertEquals(self.calculate(9511, 1036773478), -1036763967)

    def test0123(self):
        self.assertEquals(self.calculate(2509, -314549554), 314552063)

    def test0124(self):
        self.assertEquals(self.calculate(-24751, -1554931329), 1554906578)

    def test0125(self):
        self.assertEquals(self.calculate(-14838, -1183471485), 1183456647)

    def test0126(self):
        self.assertEquals(self.calculate(-19121, 470663943), -470683064)

    def test0127(self):
        self.assertEquals(self.calculate(28367, -396122858), 396151225)

    def test0128(self):
        self.assertEquals(self.calculate(-19873, -1433470346), 1433450473)

    def test0129(self):
        self.assertEquals(self.calculate(-9148, 186843477), -186852625)

    def test0130(self):
        self.assertEquals(self.calculate(-2681, -2082887573), 2082884892)

    def test0131(self):
        self.assertEquals(self.calculate(22650, 1869794053), -1869771403)

    def test0132(self):
        self.assertEquals(self.calculate(-12941, -95874355), 95861414)

    def test0133(self):
        self.assertEquals(self.calculate(-29892, -691865205), 691835313)

    def test0134(self):
        self.assertEquals(self.calculate(-5269, 1872017771), -1872023040)

    def test0135(self):
        self.assertEquals(self.calculate(-20285, -232181512), 232161227)

    def test0136(self):
        self.assertEquals(self.calculate(-23969, -686142582), 686118613)

    def test0137(self):
        self.assertEquals(self.calculate(27771, -1280823369), 1280851140)

    def test0138(self):
        self.assertEquals(self.calculate(-20979, -117716618), 117695639)

    def test0139(self):
        self.assertEquals(self.calculate(25150, 470128442), -470103292)

    def test0140(self):
        self.assertEquals(self.calculate(27983, -1380047986), 1380075969)

    def test0141(self):
        self.assertEquals(self.calculate(11663, -1588186463), 1588198126)

    def test0142(self):
        self.assertEquals(self.calculate(25284, 799324374), -799299090)

    def test0143(self):
        self.assertEquals(self.calculate(5911, 2096942184), -2096936273)

    def test0144(self):
        self.assertEquals(self.calculate(-17480, -1214786248), 1214768768)

    def test0145(self):
        self.assertEquals(self.calculate(15962, -775703862), 775719824)

    def test0146(self):
        self.assertEquals(self.calculate(2116, 856493917), -856491801)

    def test0147(self):
        self.assertEquals(self.calculate(-9310, -384062896), 384053586)

    def test0148(self):
        self.assertEquals(self.calculate(-11661, 528707401), -528719062)

    def test0149(self):
        self.assertEquals(self.calculate(8750, 279469854), -279461104)

    def test0150(self):
        self.assertEquals(self.calculate(-9605, -1852785601), 1852775996)

    def test0151(self):
        self.assertEquals(self.calculate(30268, -2119362241), 2119392509)

    def test0152(self):
        self.assertEquals(self.calculate(4341, -1301214403), 1301218744)

    def test0153(self):
        self.assertEquals(self.calculate(-19532, -1362419646), 1362400114)

    def test0154(self):
        self.assertEquals(self.calculate(-13315, 1065130678), -1065143993)

    def test0155(self):
        self.assertEquals(self.calculate(31831, 522090006), -522058175)

    def test0156(self):
        self.assertEquals(self.calculate(25623, -753712510), 753738133)

    def test0157(self):
        self.assertEquals(self.calculate(-4872, 1134027124), -1134031996)

    def test0158(self):
        self.assertEquals(self.calculate(3139, 247788606), -247785467)

    def test0159(self):
        self.assertEquals(self.calculate(11237, 1888778949), -1888767712)

    def test0160(self):
        self.assertEquals(self.calculate(-19484, 873573052), -873592536)

    def test0161(self):
        self.assertEquals(self.calculate(17276, 961728408), -961711132)

    def test0162(self):
        self.assertEquals(self.calculate(-30069, -518764310), 518734241)

    def test0163(self):
        self.assertEquals(self.calculate(-2788, 1197912767), -1197915555)

    def test0164(self):
        self.assertEquals(self.calculate(-10259, 175416816), -175427075)

    def test0165(self):
        self.assertEquals(self.calculate(-15747, 587973521), -587989268)

    def test0166(self):
        self.assertEquals(self.calculate(29435, -1515483305), 1515512740)

    def test0167(self):
        self.assertEquals(self.calculate(26035, 222671731), -222645696)

    def test0168(self):
        self.assertEquals(self.calculate(21049, -699764125), 699785174)

    def test0169(self):
        self.assertEquals(self.calculate(2793, -1559551526), 1559554319)

    def test0170(self):
        self.assertEquals(self.calculate(4205, -623775898), 623780103)

    def test0171(self):
        self.assertEquals(self.calculate(14948, 2011294887), -2011279939)

    def test0172(self):
        self.assertEquals(self.calculate(8880, -805663120), 805672000)

    def test0173(self):
        self.assertEquals(self.calculate(31543, -626944841), 626976384)

    def test0174(self):
        self.assertEquals(self.calculate(3793, -1276089358), 1276093151)

    def test0175(self):
        self.assertEquals(self.calculate(-27370, -1875176371), 1875149001)

    def test0176(self):
        self.assertEquals(self.calculate(-5186, 708753134), -708758320)

    def test0177(self):
        self.assertEquals(self.calculate(27455, -1289308629), 1289336084)

    def test0178(self):
        self.assertEquals(self.calculate(32016, -1350164214), 1350196230)

    def test0179(self):
        self.assertEquals(self.calculate(10120, -1882138114), 1882148234)

    def test0180(self):
        self.assertEquals(self.calculate(17588, 1646240688), -1646223100)

    def test0181(self):
        self.assertEquals(self.calculate(-13110, -1671353109), 1671339999)

    def test0182(self):
        self.assertEquals(self.calculate(-10529, 2015553158), -2015563687)

    def test0183(self):
        self.assertEquals(self.calculate(-24394, 1491896709), -1491921103)

    def test0184(self):
        self.assertEquals(self.calculate(-4454, 890570450), -890574904)

    def test0185(self):
        self.assertEquals(self.calculate(16833, -84940215), 84957048)

    def test0186(self):
        self.assertEquals(self.calculate(16712, 602088805), -602072093)

    def test0187(self):
        self.assertEquals(self.calculate(-1973, -592229662), 592227689)

    def test0188(self):
        self.assertEquals(self.calculate(-3446, 1991975105), -1991978551)

    def test0189(self):
        self.assertEquals(self.calculate(-13503, -1917841774), 1917828271)

    def test0190(self):
        self.assertEquals(self.calculate(-8437, -1023314033), 1023305596)

    def test0191(self):
        self.assertEquals(self.calculate(-22773, 1450465471), -1450488244)

    def test0192(self):
        self.assertEquals(self.calculate(-17333, -27248579), 27231246)

    def test0193(self):
        self.assertEquals(self.calculate(9492, -749992411), 750001903)

    def test0194(self):
        self.assertEquals(self.calculate(-30592, -1223179655), 1223149063)

    def test0195(self):
        self.assertEquals(self.calculate(13431, -476346228), 476359659)

    def test0196(self):
        self.assertEquals(self.calculate(8386, -40189312), 40197698)

    def test0197(self):
        self.assertEquals(self.calculate(-29309, 1772947464), -1772976773)

    def test0198(self):
        self.assertEquals(self.calculate(6337, -759596733), 759603070)

    def test0199(self):
        self.assertEquals(self.calculate(5865, 240137947), -240132082)

    def test0200(self):
        self.assertEquals(self.calculate(13809, -2121208966), 2121222775)

    def test0201(self):
        self.assertEquals(self.calculate(28345, -188461946), 188490291)

    def test0202(self):
        self.assertEquals(self.calculate(-571, 738785502), -738786073)

    def test0203(self):
        self.assertEquals(self.calculate(19279, -2013891341), 2013910620)

    def test0204(self):
        self.assertEquals(self.calculate(10616, 459328831), -459318215)

    def test0205(self):
        self.assertEquals(self.calculate(7062, 857433055), -857425993)

    def test0206(self):
        self.assertEquals(self.calculate(29039, 2013335048), -2013306009)

    def test0207(self):
        self.assertEquals(self.calculate(24826, 1482971070), -1482946244)

    def test0208(self):
        self.assertEquals(self.calculate(31899, 440311267), -440279368)

    def test0209(self):
        self.assertEquals(self.calculate(-3723, 326033139), -326036862)

    def test0210(self):
        self.assertEquals(self.calculate(-31938, -902565294), 902533356)

    def test0211(self):
        self.assertEquals(self.calculate(10774, 852703096), -852692322)

    def test0212(self):
        self.assertEquals(self.calculate(-9750, 517939970), -517949720)

    def test0213(self):
        self.assertEquals(self.calculate(13582, -2143181326), 2143194908)

    def test0214(self):
        self.assertEquals(self.calculate(26489, 473591132), -473564643)

    def test0215(self):
        self.assertEquals(self.calculate(-23241, -222853162), 222829921)

    def test0216(self):
        self.assertEquals(self.calculate(-10974, -686144854), 686133880)

    def test0217(self):
        self.assertEquals(self.calculate(29911, 1620127760), -1620097849)

    def test0218(self):
        self.assertEquals(self.calculate(-2059, 305664918), -305666977)

    def test0219(self):
        self.assertEquals(self.calculate(28473, -408973605), 409002078)

    def test0220(self):
        self.assertEquals(self.calculate(22472, -1921807971), 1921830443)

    def test0221(self):
        self.assertEquals(self.calculate(10060, 830791092), -830781032)

    def test0222(self):
        self.assertEquals(self.calculate(-30336, 2064737610), -2064767946)

    def test0223(self):
        self.assertEquals(self.calculate(-2391, 1181288229), -1181290620)

    def test0224(self):
        self.assertEquals(self.calculate(-16938, -232024299), 232007361)

    def test0225(self):
        self.assertEquals(self.calculate(-7897, 2071967106), -2071975003)

    def test0226(self):
        self.assertEquals(self.calculate(-8312, 1977217966), -1977226278)

    def test0227(self):
        self.assertEquals(self.calculate(-22085, 1447340653), -1447362738)

    def test0228(self):
        self.assertEquals(self.calculate(-1322, 272952630), -272953952)

    def test0229(self):
        self.assertEquals(self.calculate(5808, 664151092), -664145284)

    def test0230(self):
        self.assertEquals(self.calculate(2066, 1665753298), -1665751232)

    def test0231(self):
        self.assertEquals(self.calculate(12033, -1598428337), 1598440370)

    def test0232(self):
        self.assertEquals(self.calculate(-6730, -386427059), 386420329)

    def test0233(self):
        self.assertEquals(self.calculate(18886, 971954371), -971935485)

    def test0234(self):
        self.assertEquals(self.calculate(17669, 317878196), -317860527)

    def test0235(self):
        self.assertEquals(self.calculate(-11997, -855779260), 855767263)

    def test0236(self):
        self.assertEquals(self.calculate(-9680, 771071362), -771081042)

    def test0237(self):
        self.assertEquals(self.calculate(17821, 468754079), -468736258)

    def test0238(self):
        self.assertEquals(self.calculate(15257, -596917481), 596932738)

    def test0239(self):
        self.assertEquals(self.calculate(-29004, 1013236046), -1013265050)

    def test0240(self):
        self.assertEquals(self.calculate(-21836, -1812924303), 1812902467)

    def test0241(self):
        self.assertEquals(self.calculate(-26578, -1616882577), 1616855999)

    def test0242(self):
        self.assertEquals(self.calculate(-26577, 923972138), -923998715)

    def test0243(self):
        self.assertEquals(self.calculate(28881, -630495373), 630524254)

    def test0244(self):
        self.assertEquals(self.calculate(-17936, 171418316), -171436252)

    def test0245(self):
        self.assertEquals(self.calculate(30846, 171603101), -171572255)

    def test0246(self):
        self.assertEquals(self.calculate(-24066, 1730985476), -1731009542)

    def test0247(self):
        self.assertEquals(self.calculate(20831, 315252415), -315231584)

    def test0248(self):
        self.assertEquals(self.calculate(-15144, -1713090841), 1713075697)

    def test0249(self):
        self.assertEquals(self.calculate(-32711, -9848586), 9815875)

    def test0250(self):
        self.assertEquals(self.calculate(21585, 32196889), -32175304)

    def test0251(self):
        self.assertEquals(self.calculate(11847, 976321365), -976309518)

    def test0252(self):
        self.assertEquals(self.calculate(19380, -897761865), 897781245)

    def test0253(self):
        self.assertEquals(self.calculate(-14737, -140533120), 140518383)

    def test0254(self):
        self.assertEquals(self.calculate(-30480, -279039801), 279009321)

    def test0255(self):
        self.assertEquals(self.calculate(26072, -1270556777), 1270582849)

    def test0256(self):
        self.assertEquals(self.calculate(3565, 1016981127), -1016977562)

    def test0257(self):
        self.assertEquals(self.calculate(-3402, 2072718843), -2072722245)

    def test0258(self):
        self.assertEquals(self.calculate(-5186, -1584733532), 1584728346)

    def test0259(self):
        self.assertEquals(self.calculate(-14946, 1627829924), -1627844870)

    def test0260(self):
        self.assertEquals(self.calculate(7826, 1194402970), -1194395144)

    def test0261(self):
        self.assertEquals(self.calculate(22070, 1874812071), -1874790001)

    def test0262(self):
        self.assertEquals(self.calculate(21136, -1422931089), 1422952225)

    def test0263(self):
        self.assertEquals(self.calculate(-12407, 2119728631), -2119741038)

    def test0264(self):
        self.assertEquals(self.calculate(-5775, -1275399454), 1275393679)

    def test0265(self):
        self.assertEquals(self.calculate(-32279, 362248901), -362281180)

    def test0266(self):
        self.assertEquals(self.calculate(27582, 1212874436), -1212846854)

    def test0267(self):
        self.assertEquals(self.calculate(-22686, -1275083332), 1275060646)

    def test0268(self):
        self.assertEquals(self.calculate(10705, -2007567206), 2007577911)

    def test0269(self):
        self.assertEquals(self.calculate(17258, 1184783109), -1184765851)

    def test0270(self):
        self.assertEquals(self.calculate(-15055, 775896710), -775911765)

    def test0271(self):
        self.assertEquals(self.calculate(11006, 1906414663), -1906403657)

    def test0272(self):
        self.assertEquals(self.calculate(17413, 308588914), -308571501)

    def test0273(self):
        self.assertEquals(self.calculate(7817, -93366553), 93374370)

    def test0274(self):
        self.assertEquals(self.calculate(-12859, -1081059443), 1081046584)

    def test0275(self):
        self.assertEquals(self.calculate(23158, -547266310), 547289468)

    def test0276(self):
        self.assertEquals(self.calculate(13680, 724049901), -724036221)

    def test0277(self):
        self.assertEquals(self.calculate(3991, -1479271537), 1479275528)

    def test0278(self):
        self.assertEquals(self.calculate(-18597, -1492121697), 1492103100)

    def test0279(self):
        self.assertEquals(self.calculate(-15834, -308980974), 308965140)

    def test0280(self):
        self.assertEquals(self.calculate(-31289, 1418087315), -1418118604)

    def test0281(self):
        self.assertEquals(self.calculate(-1544, 2053089076), -2053090620)

    def test0282(self):
        self.assertEquals(self.calculate(-8770, -328488556), 328479786)

    def test0283(self):
        self.assertEquals(self.calculate(-9407, 1611079315), -1611088722)

    def test0284(self):
        self.assertEquals(self.calculate(-3501, -876956165), 876952664)

    def test0285(self):
        self.assertEquals(self.calculate(-6421, 1055195864), -1055202285)

    def test0286(self):
        self.assertEquals(self.calculate(-9108, 1064502591), -1064511699)

    def test0287(self):
        self.assertEquals(self.calculate(22554, -1390681462), 1390704016)

    def test0288(self):
        self.assertEquals(self.calculate(-2270, 262154131), -262156401)

    def test0289(self):
        self.assertEquals(self.calculate(11950, -269517825), 269529775)

    def test0290(self):
        self.assertEquals(self.calculate(6851, 1398691473), -1398684622)

    def test0291(self):
        self.assertEquals(self.calculate(8694, -1970299203), 1970307897)

    def test0292(self):
        self.assertEquals(self.calculate(-28751, -1280719878), 1280691127)

    def test0293(self):
        self.assertEquals(self.calculate(-32378, -292891431), 292859053)

    def test0294(self):
        self.assertEquals(self.calculate(28808, 1523718397), -1523689589)

    def test0295(self):
        self.assertEquals(self.calculate(-20765, 356793602), -356814367)

    def test0296(self):
        self.assertEquals(self.calculate(-17469, 851990143), -852007612)

    def test0297(self):
        self.assertEquals(self.calculate(-501, 1493224864), -1493225365)

    def test0298(self):
        self.assertEquals(self.calculate(-29937, 1012594163), -1012624100)

    def test0299(self):
        self.assertEquals(self.calculate(1858, -1970135950), 1970137808)

    def test0300(self):
        self.assertEquals(self.calculate(26166, 904058147), -904031981)

    def test0301(self):
        self.assertEquals(self.calculate(28220, 1293217213), -1293188993)

    def test0302(self):
        self.assertEquals(self.calculate(-28385, 1255134545), -1255162930)

    def test0303(self):
        self.assertEquals(self.calculate(-5208, 851727795), -851733003)

    def test0304(self):
        self.assertEquals(self.calculate(-22822, -687516747), 687493925)

    def test0305(self):
        self.assertEquals(self.calculate(3665, 1006561339), -1006557674)

    def test0306(self):
        self.assertEquals(self.calculate(-18969, -679254653), 679235684)

    def test0307(self):
        self.assertEquals(self.calculate(4896, -389947479), 389952375)

    def test0308(self):
        self.assertEquals(self.calculate(2659, 1382890957), -1382888298)

    def test0309(self):
        self.assertEquals(self.calculate(-20445, 837773043), -837793488)

    def test0310(self):
        self.assertEquals(self.calculate(-22356, -954932016), 954909660)

    def test0311(self):
        self.assertEquals(self.calculate(-26790, -1856982925), 1856956135)

    def test0312(self):
        self.assertEquals(self.calculate(6847, 2017604687), -2017597840)

    def test0313(self):
        self.assertEquals(self.calculate(-27956, -1079743210), 1079715254)

    def test0314(self):
        self.assertEquals(self.calculate(18096, 891539706), -891521610)

    def test0315(self):
        self.assertEquals(self.calculate(21245, 1687235518), -1687214273)

    def test0316(self):
        self.assertEquals(self.calculate(-32579, -299236311), 299203732)

    def test0317(self):
        self.assertEquals(self.calculate(-20893, 2076357376), -2076378269)

    def test0318(self):
        self.assertEquals(self.calculate(-15096, -1429959211), 1429944115)

    def test0319(self):
        self.assertEquals(self.calculate(-22121, 637593667), -637615788)

    def test0320(self):
        self.assertEquals(self.calculate(-25289, 845139974), -845165263)

    def test0321(self):
        self.assertEquals(self.calculate(-7057, -1450653494), 1450646437)

    def test0322(self):
        self.assertEquals(self.calculate(30595, -1904253623), 1904284218)

    def test0323(self):
        self.assertEquals(self.calculate(2155, -652509862), 652512017)

    def test0324(self):
        self.assertEquals(self.calculate(-23954, -55976391), 55952437)

    def test0325(self):
        self.assertEquals(self.calculate(32032, 163354210), -163322178)

    def test0326(self):
        self.assertEquals(self.calculate(-31001, -500118854), 500087853)

    def test0327(self):
        self.assertEquals(self.calculate(-15693, 489124737), -489140430)

    def test0328(self):
        self.assertEquals(self.calculate(-7561, 1642993268), -1643000829)

    def test0329(self):
        self.assertEquals(self.calculate(-21102, 814168771), -814189873)

    def test0330(self):
        self.assertEquals(self.calculate(-7184, -136598244), 136591060)

    def test0331(self):
        self.assertEquals(self.calculate(-8456, 767215413), -767223869)

    def test0332(self):
        self.assertEquals(self.calculate(-413, 366963765), -366964178)

    def test0333(self):
        self.assertEquals(self.calculate(5614, 1299828885), -1299823271)

    def test0334(self):
        self.assertEquals(self.calculate(6225, 232235868), -232229643)

    def test0335(self):
        self.assertEquals(self.calculate(-27305, 1408635813), -1408663118)

    def test0336(self):
        self.assertEquals(self.calculate(-21398, 2100414128), -2100435526)

    def test0337(self):
        self.assertEquals(self.calculate(-28995, 234757267), -234786262)

    def test0338(self):
        self.assertEquals(self.calculate(-23528, -2116575411), 2116551883)

    def test0339(self):
        self.assertEquals(self.calculate(-12794, 1774617875), -1774630669)

    def test0340(self):
        self.assertEquals(self.calculate(27234, 1081180244), -1081153010)

    def test0341(self):
        self.assertEquals(self.calculate(6984, 2112353344), -2112346360)

    def test0342(self):
        self.assertEquals(self.calculate(2703, -1538128503), 1538131206)

    def test0343(self):
        self.assertEquals(self.calculate(-20910, 263405641), -263426551)

    def test0344(self):
        self.assertEquals(self.calculate(-30794, 684995455), -685026249)

    def test0345(self):
        self.assertEquals(self.calculate(-24141, 1512642165), -1512666306)

    def test0346(self):
        self.assertEquals(self.calculate(13769, 287028312), -287014543)

    def test0347(self):
        self.assertEquals(self.calculate(-4389, 402195244), -402199633)

    def test0348(self):
        self.assertEquals(self.calculate(23834, -9451679), 9475513)

    def test0349(self):
        self.assertEquals(self.calculate(-32716, -1438436265), 1438403549)

    def test0350(self):
        self.assertEquals(self.calculate(-28395, 197938135), -197966530)

    def test0351(self):
        self.assertEquals(self.calculate(1235, 1546690765), -1546689530)

    def test0352(self):
        self.assertEquals(self.calculate(-31611, -134692760), 134661149)

    def test0353(self):
        self.assertEquals(self.calculate(-8167, -223092384), 223084217)

    def test0354(self):
        self.assertEquals(self.calculate(-27868, 24056560), -24084428)

    def test0355(self):
        self.assertEquals(self.calculate(-8113, -1985125959), 1985117846)

    def test0356(self):
        self.assertEquals(self.calculate(-10442, -391578213), 391567771)

    def test0357(self):
        self.assertEquals(self.calculate(-1089, -2121980576), 2121979487)

    def test0358(self):
        self.assertEquals(self.calculate(-7001, 1054050337), -1054057338)

    def test0359(self):
        self.assertEquals(self.calculate(-8447, 742944936), -742953383)

    def test0360(self):
        self.assertEquals(self.calculate(15388, -545372335), 545387723)

    def test0361(self):
        self.assertEquals(self.calculate(7055, 226177661), -226170606)

    def test0362(self):
        self.assertEquals(self.calculate(-23055, -452737817), 452714762)

    def test0363(self):
        self.assertEquals(self.calculate(10726, 1308903170), -1308892444)

    def test0364(self):
        self.assertEquals(self.calculate(-15519, 1406438156), -1406453675)

    def test0365(self):
        self.assertEquals(self.calculate(14594, 601092608), -601078014)

    def test0366(self):
        self.assertEquals(self.calculate(19969, 676390711), -676370742)

    def test0367(self):
        self.assertEquals(self.calculate(25561, 795204735), -795179174)

    def test0368(self):
        self.assertEquals(self.calculate(-5489, -160587467), 160581978)

    def test0369(self):
        self.assertEquals(self.calculate(6366, -2041550119), 2041556485)

    def test0370(self):
        self.assertEquals(self.calculate(27997, -1655582200), 1655610197)

    def test0371(self):
        self.assertEquals(self.calculate(-29036, -1755013003), 1754983967)

    def test0372(self):
        self.assertEquals(self.calculate(-18439, -208906713), 208888274)

    def test0373(self):
        self.assertEquals(self.calculate(-5863, -233125872), 233120009)

    def test0374(self):
        self.assertEquals(self.calculate(-951, 883156650), -883157601)

    def test0375(self):
        self.assertEquals(self.calculate(21192, 1459440700), -1459419508)

    def test0376(self):
        self.assertEquals(self.calculate(-8181, -1431984072), 1431975891)

    def test0377(self):
        self.assertEquals(self.calculate(-30476, 1955398452), -1955428928)

    def test0378(self):
        self.assertEquals(self.calculate(7465, 634671122), -634663657)

    def test0379(self):
        self.assertEquals(self.calculate(-32517, -1136975410), 1136942893)

    def test0380(self):
        self.assertEquals(self.calculate(18659, -28844087), 28862746)

    def test0381(self):
        self.assertEquals(self.calculate(8978, 847772247), -847763269)

    def test0382(self):
        self.assertEquals(self.calculate(29825, -1522204693), 1522234518)

    def test0383(self):
        self.assertEquals(self.calculate(-7009, 1088427414), -1088434423)

    def test0384(self):
        self.assertEquals(self.calculate(23037, -1584682196), 1584705233)

    def test0385(self):
        self.assertEquals(self.calculate(-26683, 1765797571), -1765824254)

    def test0386(self):
        self.assertEquals(self.calculate(31843, 1092690097), -1092658254)

    def test0387(self):
        self.assertEquals(self.calculate(27303, -1977841957), 1977869260)

    def test0388(self):
        self.assertEquals(self.calculate(-31824, -1355085671), 1355053847)

    def test0389(self):
        self.assertEquals(self.calculate(3635, 590535598), -590531963)

    def test0390(self):
        self.assertEquals(self.calculate(-19642, -1742778023), 1742758381)

    def test0391(self):
        self.assertEquals(self.calculate(6597, 2004355590), -2004348993)

    def test0392(self):
        self.assertEquals(self.calculate(-25659, 1090834964), -1090860623)

    def test0393(self):
        self.assertEquals(self.calculate(-10576, 211880756), -211891332)

    def test0394(self):
        self.assertEquals(self.calculate(-19808, 1908431912), -1908451720)

    def test0395(self):
        self.assertEquals(self.calculate(4777, 193906515), -193901738)

    def test0396(self):
        self.assertEquals(self.calculate(-5948, -755910998), 755905050)

    def test0397(self):
        self.assertEquals(self.calculate(-17766, 469156579), -469174345)

    def test0398(self):
        self.assertEquals(self.calculate(26504, -453697396), 453723900)

    def test0399(self):
        self.assertEquals(self.calculate(-25660, -886595920), 886570260)

    def test0400(self):
        self.assertEquals(self.calculate(-4258, 1280307217), -1280311475)

    def test0401(self):
        self.assertEquals(self.calculate(-28309, 99166896), -99195205)

    def test0402(self):
        self.assertEquals(self.calculate(-22911, -1660168656), 1660145745)

    def test0403(self):
        self.assertEquals(self.calculate(18152, 766338126), -766319974)

    def test0404(self):
        self.assertEquals(self.calculate(4697, -1733369054), 1733373751)

    def test0405(self):
        self.assertEquals(self.calculate(-11397, -405642810), 405631413)

    def test0406(self):
        self.assertEquals(self.calculate(-7497, -2100330706), 2100323209)

    def test0407(self):
        self.assertEquals(self.calculate(22882, 1587755832), -1587732950)

    def test0408(self):
        self.assertEquals(self.calculate(-23523, -47201849), 47178326)

    def test0409(self):
        self.assertEquals(self.calculate(-11885, -80449197), 80437312)

    def test0410(self):
        self.assertEquals(self.calculate(14189, 1225615509), -1225601320)

    def test0411(self):
        self.assertEquals(self.calculate(30848, 1355561375), -1355530527)

    def test0412(self):
        self.assertEquals(self.calculate(-5574, -235287088), 235281514)

    def test0413(self):
        self.assertEquals(self.calculate(995, -152948632), 152949627)

    def test0414(self):
        self.assertEquals(self.calculate(4666, -53508054), 53512720)

    def test0415(self):
        self.assertEquals(self.calculate(-7712, 2063392155), -2063399867)

    def test0416(self):
        self.assertEquals(self.calculate(1466, 1750002608), -1750001142)

    def test0417(self):
        self.assertEquals(self.calculate(30457, 1170013427), -1169982970)

    def test0418(self):
        self.assertEquals(self.calculate(1644, 455421601), -455419957)

    def test0419(self):
        self.assertEquals(self.calculate(-13221, 319808805), -319822026)

    def test0420(self):
        self.assertEquals(self.calculate(-582, -472227809), 472227227)

    def test0421(self):
        self.assertEquals(self.calculate(-21521, 199773849), -199795370)

    def test0422(self):
        self.assertEquals(self.calculate(11934, -150716004), 150727938)

    def test0423(self):
        self.assertEquals(self.calculate(-30489, -2028332992), 2028302503)

    def test0424(self):
        self.assertEquals(self.calculate(-16950, -1477959290), 1477942340)

    def test0425(self):
        self.assertEquals(self.calculate(-4739, -450445982), 450441243)

    def test0426(self):
        self.assertEquals(self.calculate(-24009, -1211758526), 1211734517)

    def test0427(self):
        self.assertEquals(self.calculate(32214, 1150468536), -1150436322)

    def test0428(self):
        self.assertEquals(self.calculate(32698, 645601468), -645568770)

    def test0429(self):
        self.assertEquals(self.calculate(27912, -885330356), 885358268)

    def test0430(self):
        self.assertEquals(self.calculate(-18072, 1401249359), -1401267431)

    def test0431(self):
        self.assertEquals(self.calculate(-11167, -585753313), 585742146)

    def test0432(self):
        self.assertEquals(self.calculate(16677, -947825437), 947842114)

    def test0433(self):
        self.assertEquals(self.calculate(-20229, -1808760364), 1808740135)

    def test0434(self):
        self.assertEquals(self.calculate(24833, 260919951), -260895118)

    def test0435(self):
        self.assertEquals(self.calculate(-26541, -1324809398), 1324782857)

    def test0436(self):
        self.assertEquals(self.calculate(-16821, -676075770), 676058949)

    def test0437(self):
        self.assertEquals(self.calculate(-16447, 134597601), -134614048)

    def test0438(self):
        self.assertEquals(self.calculate(12441, -1709877781), 1709890222)

    def test0439(self):
        self.assertEquals(self.calculate(31271, 1808116034), -1808084763)

    def test0440(self):
        self.assertEquals(self.calculate(24776, 619769029), -619744253)

    def test0441(self):
        self.assertEquals(self.calculate(-25555, 702332341), -702357896)

    def test0442(self):
        self.assertEquals(self.calculate(22779, -401134323), 401157102)

    def test0443(self):
        self.assertEquals(self.calculate(23566, 928582487), -928558921)

    def test0444(self):
        self.assertEquals(self.calculate(17413, -1000043377), 1000060790)

    def test0445(self):
        self.assertEquals(self.calculate(28709, -1726869542), 1726898251)

    def test0446(self):
        self.assertEquals(self.calculate(-7772, -546447153), 546439381)

    def test0447(self):
        self.assertEquals(self.calculate(3041, -686320162), 686323203)

    def test0448(self):
        self.assertEquals(self.calculate(16842, 1391208543), -1391191701)

    def test0449(self):
        self.assertEquals(self.calculate(-23512, -1291770551), 1291747039)

    def test0450(self):
        self.assertEquals(self.calculate(7461, -2046940874), 2046948335)

    def test0451(self):
        self.assertEquals(self.calculate(15285, -1293565786), 1293581071)

    def test0452(self):
        self.assertEquals(self.calculate(-3929, 987421780), -987425709)

    def test0453(self):
        self.assertEquals(self.calculate(-16936, 454422421), -454439357)

    def test0454(self):
        self.assertEquals(self.calculate(-7902, -1223530765), 1223522863)

    def test0455(self):
        self.assertEquals(self.calculate(30865, -945888318), 945919183)

    def test0456(self):
        self.assertEquals(self.calculate(6554, -1681869702), 1681876256)

    def test0457(self):
        self.assertEquals(self.calculate(-31543, -1219141559), 1219110016)

    def test0458(self):
        self.assertEquals(self.calculate(-7465, -888623162), 888615697)

    def test0459(self):
        self.assertEquals(self.calculate(-21355, 796119334), -796140689)

    def test0460(self):
        self.assertEquals(self.calculate(-19084, 981696664), -981715748)

    def test0461(self):
        self.assertEquals(self.calculate(3151, -2065520433), 2065523584)

    def test0462(self):
        self.assertEquals(self.calculate(-22573, -1942496731), 1942474158)

    def test0463(self):
        self.assertEquals(self.calculate(3937, 713822120), -713818183)

    def test0464(self):
        self.assertEquals(self.calculate(13762, 1937905033), -1937891271)

    def test0465(self):
        self.assertEquals(self.calculate(-4669, -2088114630), 2088109961)

    def test0466(self):
        self.assertEquals(self.calculate(5984, 53013897), -53007913)

    def test0467(self):
        self.assertEquals(self.calculate(20196, -1658479939), 1658500135)

    def test0468(self):
        self.assertEquals(self.calculate(28021, 806447844), -806419823)

    def test0469(self):
        self.assertEquals(self.calculate(-25586, -1966293644), 1966268058)

    def test0470(self):
        self.assertEquals(self.calculate(32356, -465608605), 465640961)

    def test0471(self):
        self.assertEquals(self.calculate(8797, 671412144), -671403347)

    def test0472(self):
        self.assertEquals(self.calculate(-23683, -1500044244), 1500020561)

    def test0473(self):
        self.assertEquals(self.calculate(-17443, -1795144750), 1795127307)

    def test0474(self):
        self.assertEquals(self.calculate(5714, -1339657019), 1339662733)

    def test0475(self):
        self.assertEquals(self.calculate(29063, 1456866416), -1456837353)

    def test0476(self):
        self.assertEquals(self.calculate(-18458, -1833736045), 1833717587)

    def test0477(self):
        self.assertEquals(self.calculate(-18247, 535713529), -535731776)

    def test0478(self):
        self.assertEquals(self.calculate(-17410, 796672698), -796690108)

    def test0479(self):
        self.assertEquals(self.calculate(-17297, 216755459), -216772756)

    def test0480(self):
        self.assertEquals(self.calculate(18704, -1077580045), 1077598749)

    def test0481(self):
        self.assertEquals(self.calculate(-19550, 643053140), -643072690)

    def test0482(self):
        self.assertEquals(self.calculate(3248, 37263899), -37260651)

    def test0483(self):
        self.assertEquals(self.calculate(-1835, 368152245), -368154080)

    def test0484(self):
        self.assertEquals(self.calculate(-32145, 739075683), -739107828)

    def test0485(self):
        self.assertEquals(self.calculate(16652, 1300640970), -1300624318)

    def test0486(self):
        self.assertEquals(self.calculate(27595, 2034206130), -2034178535)

    def test0487(self):
        self.assertEquals(self.calculate(-28850, 1027306962), -1027335812)

    def test0488(self):
        self.assertEquals(self.calculate(13176, 1022098115), -1022084939)

    def test0489(self):
        self.assertEquals(self.calculate(-18413, 41866220), -41884633)

    def test0490(self):
        self.assertEquals(self.calculate(14622, -748815961), 748830583)

    def test0491(self):
        self.assertEquals(self.calculate(26213, 438443752), -438417539)

    def test0492(self):
        self.assertEquals(self.calculate(31355, -869916930), 869948285)

    def test0493(self):
        self.assertEquals(self.calculate(-27636, -149183773), 149156137)

    def test0494(self):
        self.assertEquals(self.calculate(-9040, 788508634), -788517674)

    def test0495(self):
        self.assertEquals(self.calculate(3806, 1036459096), -1036455290)

    def test0496(self):
        self.assertEquals(self.calculate(27012, -36282726), 36309738)

    def test0497(self):
        self.assertEquals(self.calculate(6957, -1247800984), 1247807941)

    def test0498(self):
        self.assertEquals(self.calculate(11694, -1027651496), 1027663190)

    def test0499(self):
        self.assertEquals(self.calculate(27507, -1403193100), 1403220607)

    def test0500(self):
        self.assertEquals(self.calculate(8136, 62271417), -62263281)

    def test0501(self):
        self.assertEquals(self.calculate(994, 1797790317), -1797789323)

    def test0502(self):
        self.assertEquals(self.calculate(21614, 1590598833), -1590577219)

    def test0503(self):
        self.assertEquals(self.calculate(2440, 734690953), -734688513)

    def test0504(self):
        self.assertEquals(self.calculate(29297, 1122406752), -1122377455)

    def test0505(self):
        self.assertEquals(self.calculate(-23025, -1391945201), 1391922176)

    def test0506(self):
        self.assertEquals(self.calculate(6212, -1846895164), 1846901376)

    def test0507(self):
        self.assertEquals(self.calculate(-10495, 1907833332), -1907843827)

    def test0508(self):
        self.assertEquals(self.calculate(28586, 285493124), -285464538)

    def test0509(self):
        self.assertEquals(self.calculate(-488, -1945256225), 1945255737)

    def test0510(self):
        self.assertEquals(self.calculate(-19950, 1650589083), -1650609033)

    def test0511(self):
        self.assertEquals(self.calculate(7475, -1044425382), 1044432857)

    def test0512(self):
        self.assertEquals(self.calculate(19780, -2092088212), 2092107992)

    def test0513(self):
        self.assertEquals(self.calculate(-13256, -1169894225), 1169880969)

    def test0514(self):
        self.assertEquals(self.calculate(13477, -783733297), 783746774)

    def test0515(self):
        self.assertEquals(self.calculate(-12521, 1797994379), -1798006900)

    def test0516(self):
        self.assertEquals(self.calculate(-31522, -873188421), 873156899)

    def test0517(self):
        self.assertEquals(self.calculate(29479, -1760720070), 1760749549)

    def test0518(self):
        self.assertEquals(self.calculate(31929, 1910736595), -1910704666)

    def test0519(self):
        self.assertEquals(self.calculate(-24701, -831151849), 831127148)

    def test0520(self):
        self.assertEquals(self.calculate(-25582, -1782095677), 1782070095)

    def test0521(self):
        self.assertEquals(self.calculate(18270, -1207439899), 1207458169)

    def test0522(self):
        self.assertEquals(self.calculate(-11044, -1606207194), 1606196150)

    def test0523(self):
        self.assertEquals(self.calculate(2695, 90866307), -90863612)

    def test0524(self):
        self.assertEquals(self.calculate(-6383, -1545250500), 1545244117)

    def test0525(self):
        self.assertEquals(self.calculate(-27252, 214737038), -214764290)

    def test0526(self):
        self.assertEquals(self.calculate(-4405, 1476541837), -1476546242)

    def test0527(self):
        self.assertEquals(self.calculate(25204, 784626612), -784601408)

    def test0528(self):
        self.assertEquals(self.calculate(-31687, -202360998), 202329311)

    def test0529(self):
        self.assertEquals(self.calculate(-20501, -7029905), 7009404)

    def test0530(self):
        self.assertEquals(self.calculate(26033, -972805336), 972831369)

    def test0531(self):
        self.assertEquals(self.calculate(-4087, 1938193864), -1938197951)

    def test0532(self):
        self.assertEquals(self.calculate(-19426, -514509287), 514489861)

    def test0533(self):
        self.assertEquals(self.calculate(-17267, 417166667), -417183934)

    def test0534(self):
        self.assertEquals(self.calculate(16962, 655184893), -655167931)

    def test0535(self):
        self.assertEquals(self.calculate(8003, 1858197504), -1858189501)

    def test0536(self):
        self.assertEquals(self.calculate(-6286, -520055131), 520048845)

    def test0537(self):
        self.assertEquals(self.calculate(-30504, 1786819461), -1786849965)

    def test0538(self):
        self.assertEquals(self.calculate(-8832, -499565962), 499557130)

    def test0539(self):
        self.assertEquals(self.calculate(-3676, -814405671), 814401995)

    def test0540(self):
        self.assertEquals(self.calculate(-31358, 1386710560), -1386741918)

    def test0541(self):
        self.assertEquals(self.calculate(-23827, 163056803), -163080630)

    def test0542(self):
        self.assertEquals(self.calculate(22221, -1373726551), 1373748772)

    def test0543(self):
        self.assertEquals(self.calculate(13778, -806296285), 806310063)

    def test0544(self):
        self.assertEquals(self.calculate(-2218, -1012768074), 1012765856)

    def test0545(self):
        self.assertEquals(self.calculate(-22419, -323326851), 323304432)

    def test0546(self):
        self.assertEquals(self.calculate(-13194, -852583363), 852570169)

    def test0547(self):
        self.assertEquals(self.calculate(-7394, 1461725368), -1461732762)

    def test0548(self):
        self.assertEquals(self.calculate(17281, -223707639), 223724920)

    def test0549(self):
        self.assertEquals(self.calculate(-678, -1952625357), 1952624679)

    def test0550(self):
        self.assertEquals(self.calculate(-6536, 1589942892), -1589949428)

    def test0551(self):
        self.assertEquals(self.calculate(23134, 1482017172), -1481994038)

    def test0552(self):
        self.assertEquals(self.calculate(-22769, -1747258450), 1747235681)

    def test0553(self):
        self.assertEquals(self.calculate(9306, -531846126), 531855432)

    def test0554(self):
        self.assertEquals(self.calculate(1769, 1380510586), -1380508817)

    def test0555(self):
        self.assertEquals(self.calculate(-21904, -66827644), 66805740)

    def test0556(self):
        self.assertEquals(self.calculate(-9924, 1830212985), -1830222909)

    def test0557(self):
        self.assertEquals(self.calculate(-18858, -1525545603), 1525526745)

    def test0558(self):
        self.assertEquals(self.calculate(-2790, -1490553821), 1490551031)

    def test0559(self):
        self.assertEquals(self.calculate(-23061, -1555646088), 1555623027)

    def test0560(self):
        self.assertEquals(self.calculate(-27654, -1199134651), 1199106997)

    def test0561(self):
        self.assertEquals(self.calculate(24272, -375661094), 375685366)

    def test0562(self):
        self.assertEquals(self.calculate(17547, 345003731), -344986184)

    def test0563(self):
        self.assertEquals(self.calculate(-14466, -1960200549), 1960186083)

    def test0564(self):
        self.assertEquals(self.calculate(-18539, -1128557423), 1128538884)

    def test0565(self):
        self.assertEquals(self.calculate(-31844, -1380860536), 1380828692)

    def test0566(self):
        self.assertEquals(self.calculate(25808, 592779077), -592753269)

    def test0567(self):
        self.assertEquals(self.calculate(-25587, 854017053), -854042640)

    def test0568(self):
        self.assertEquals(self.calculate(9935, -1628917644), 1628927579)

    def test0569(self):
        self.assertEquals(self.calculate(-22708, -267030432), 267007724)

    def test0570(self):
        self.assertEquals(self.calculate(32754, 229965971), -229933217)

    def test0571(self):
        self.assertEquals(self.calculate(26773, -964950031), 964976804)

    def test0572(self):
        self.assertEquals(self.calculate(19756, 564523961), -564504205)

    def test0573(self):
        self.assertEquals(self.calculate(11342, 411190897), -411179555)

    def test0574(self):
        self.assertEquals(self.calculate(22968, -1177779266), 1177802234)

    def test0575(self):
        self.assertEquals(self.calculate(-27459, 609134051), -609161510)

    def test0576(self):
        self.assertEquals(self.calculate(-29820, -1311066241), 1311036421)

    def test0577(self):
        self.assertEquals(self.calculate(-16831, -476406200), 476389369)

    def test0578(self):
        self.assertEquals(self.calculate(-3934, -1800957407), 1800953473)

    def test0579(self):
        self.assertEquals(self.calculate(27583, 628574929), -628547346)

    def test0580(self):
        self.assertEquals(self.calculate(19542, -1305218122), 1305237664)

    def test0581(self):
        self.assertEquals(self.calculate(-22131, -806102389), 806080258)

    def test0582(self):
        self.assertEquals(self.calculate(5026, 872678570), -872673544)

    def test0583(self):
        self.assertEquals(self.calculate(-13954, -1933463310), 1933449356)

    def test0584(self):
        self.assertEquals(self.calculate(24979, -2121000550), 2121025529)

    def test0585(self):
        self.assertEquals(self.calculate(-25646, 1671100827), -1671126473)

    def test0586(self):
        self.assertEquals(self.calculate(-17422, 879275820), -879293242)

    def test0587(self):
        self.assertEquals(self.calculate(-1424, 2065410555), -2065411979)

    def test0588(self):
        self.assertEquals(self.calculate(-13728, -2119253778), 2119240050)

    def test0589(self):
        self.assertEquals(self.calculate(-8550, 851331005), -851339555)

    def test0590(self):
        self.assertEquals(self.calculate(18272, -1786556257), 1786574529)

    def test0591(self):
        self.assertEquals(self.calculate(12868, -513469394), 513482262)

    def test0592(self):
        self.assertEquals(self.calculate(-9038, 2025479502), -2025488540)

    def test0593(self):
        self.assertEquals(self.calculate(-4132, -526325233), 526321101)

    def test0594(self):
        self.assertEquals(self.calculate(-21644, -92834819), 92813175)

    def test0595(self):
        self.assertEquals(self.calculate(-26833, 1806624304), -1806651137)

    def test0596(self):
        self.assertEquals(self.calculate(-7426, 377076299), -377083725)

    def test0597(self):
        self.assertEquals(self.calculate(-18837, 669874827), -669893664)

    def test0598(self):
        self.assertEquals(self.calculate(-25706, -255337044), 255311338)

    def test0599(self):
        self.assertEquals(self.calculate(14019, -1325248634), 1325262653)

    def test0600(self):
        self.assertEquals(self.calculate(29826, 1058260193), -1058230367)

    def test0601(self):
        self.assertEquals(self.calculate(-2008, 1512287293), -1512289301)

    def test0602(self):
        self.assertEquals(self.calculate(-9848, -1129448322), 1129438474)

    def test0603(self):
        self.assertEquals(self.calculate(345, -1251837002), 1251837347)

    def test0604(self):
        self.assertEquals(self.calculate(10908, 441743331), -441732423)

    def test0605(self):
        self.assertEquals(self.calculate(-27157, -41060181), 41033024)

    def test0606(self):
        self.assertEquals(self.calculate(32521, -657464223), 657496744)

    def test0607(self):
        self.assertEquals(self.calculate(-24602, 788841781), -788866383)

    def test0608(self):
        self.assertEquals(self.calculate(-473, 149605037), -149605510)

    def test0609(self):
        self.assertEquals(self.calculate(-10205, 133719129), -133729334)

    def test0610(self):
        self.assertEquals(self.calculate(-1075, -2133440130), 2133439055)

    def test0611(self):
        self.assertEquals(self.calculate(26906, 1890027835), -1890000929)

    def test0612(self):
        self.assertEquals(self.calculate(17252, -1304859688), 1304876940)

    def test0613(self):
        self.assertEquals(self.calculate(-428, 1106979316), -1106979744)

    def test0614(self):
        self.assertEquals(self.calculate(-32417, 1125921449), -1125953866)

    def test0615(self):
        self.assertEquals(self.calculate(12177, -1241771769), 1241783946)

    def test0616(self):
        self.assertEquals(self.calculate(-12010, 1543751592), -1543763602)

    def test0617(self):
        self.assertEquals(self.calculate(-22624, 513204591), -513227215)

    def test0618(self):
        self.assertEquals(self.calculate(-31220, -757788112), 757756892)

    def test0619(self):
        self.assertEquals(self.calculate(1933, 230881641), -230879708)

    def test0620(self):
        self.assertEquals(self.calculate(-18152, 948509004), -948527156)

    def test0621(self):
        self.assertEquals(self.calculate(11705, -201064909), 201076614)

    def test0622(self):
        self.assertEquals(self.calculate(1633, -221809086), 221810719)

    def test0623(self):
        self.assertEquals(self.calculate(28031, -1691541121), 1691569152)

    def test0624(self):
        self.assertEquals(self.calculate(28487, -1505324017), 1505352504)

    def test0625(self):
        self.assertEquals(self.calculate(19505, -1203115971), 1203135476)

    def test0626(self):
        self.assertEquals(self.calculate(-14664, 525646905), -525661569)

    def test0627(self):
        self.assertEquals(self.calculate(-26254, 186487736), -186513990)

    def test0628(self):
        self.assertEquals(self.calculate(18504, -16124523), 16143027)

    def test0629(self):
        self.assertEquals(self.calculate(-17672, 865379345), -865397017)

    def test0630(self):
        self.assertEquals(self.calculate(665, -374679142), 374679807)

    def test0631(self):
        self.assertEquals(self.calculate(21168, 794003893), -793982725)

    def test0632(self):
        self.assertEquals(self.calculate(-20421, 1520032263), -1520052684)

    def test0633(self):
        self.assertEquals(self.calculate(18893, -559014635), 559033528)

    def test0634(self):
        self.assertEquals(self.calculate(21825, -725627134), 725648959)

    def test0635(self):
        self.assertEquals(self.calculate(-529, -59621709), 59621180)

    def test0636(self):
        self.assertEquals(self.calculate(-13467, 1320214868), -1320228335)

    def test0637(self):
        self.assertEquals(self.calculate(-15319, 1011351104), -1011366423)

    def test0638(self):
        self.assertEquals(self.calculate(4848, -342316713), 342321561)

    def test0639(self):
        self.assertEquals(self.calculate(23553, -1748961078), 1748984631)

    def test0640(self):
        self.assertEquals(self.calculate(-16961, 980446894), -980463855)

    def test0641(self):
        self.assertEquals(self.calculate(-9547, 1179194251), -1179203798)

    def test0642(self):
        self.assertEquals(self.calculate(22240, 692845549), -692823309)

    def test0643(self):
        self.assertEquals(self.calculate(-10348, -1073588950), 1073578602)

    def test0644(self):
        self.assertEquals(self.calculate(-2175, 1642185108), -1642187283)

    def test0645(self):
        self.assertEquals(self.calculate(22967, -468550125), 468573092)

    def test0646(self):
        self.assertEquals(self.calculate(11305, 1123137503), -1123126198)

    def test0647(self):
        self.assertEquals(self.calculate(2027, 1270970670), -1270968643)

    def test0648(self):
        self.assertEquals(self.calculate(-11395, -1114681740), 1114670345)

    def test0649(self):
        self.assertEquals(self.calculate(-2821, 1470155642), -1470158463)

    def test0650(self):
        self.assertEquals(self.calculate(24679, -1197503797), 1197528476)

    def test0651(self):
        self.assertEquals(self.calculate(-14184, -834795986), 834781802)

    def test0652(self):
        self.assertEquals(self.calculate(2312, -1756569582), 1756571894)

    def test0653(self):
        self.assertEquals(self.calculate(-18760, -612603398), 612584638)

    def test0654(self):
        self.assertEquals(self.calculate(9048, 901298229), -901289181)

    def test0655(self):
        self.assertEquals(self.calculate(-23321, 873042408), -873065729)

    def test0656(self):
        self.assertEquals(self.calculate(6252, -2061070602), 2061076854)

    def test0657(self):
        self.assertEquals(self.calculate(27288, -1405654687), 1405681975)

    def test0658(self):
        self.assertEquals(self.calculate(5121, 1586678126), -1586673005)

    def test0659(self):
        self.assertEquals(self.calculate(9642, -1103822171), 1103831813)

    def test0660(self):
        self.assertEquals(self.calculate(-1700, 638829839), -638831539)

    def test0661(self):
        self.assertEquals(self.calculate(-15685, 2117267207), -2117282892)

    def test0662(self):
        self.assertEquals(self.calculate(14449, -1773718635), 1773733084)

    def test0663(self):
        self.assertEquals(self.calculate(-30217, 578146776), -578176993)

    def test0664(self):
        self.assertEquals(self.calculate(-20709, -470364275), 470343566)

    def test0665(self):
        self.assertEquals(self.calculate(17465, 1128887998), -1128870533)

    def test0666(self):
        self.assertEquals(self.calculate(-26659, 1376212075), -1376238734)

    def test0667(self):
        self.assertEquals(self.calculate(-29895, 1312208826), -1312238721)

    def test0668(self):
        self.assertEquals(self.calculate(-20001, -1431326897), 1431306896)

    def test0669(self):
        self.assertEquals(self.calculate(18192, 810924415), -810906223)

    def test0670(self):
        self.assertEquals(self.calculate(28204, 1450724848), -1450696644)

    def test0671(self):
        self.assertEquals(self.calculate(-7935, 328168537), -328176472)

    def test0672(self):
        self.assertEquals(self.calculate(-3193, -611076053), 611072860)

    def test0673(self):
        self.assertEquals(self.calculate(16370, -365873304), 365889674)

    def test0674(self):
        self.assertEquals(self.calculate(-13188, -451082602), 451069414)

    def test0675(self):
        self.assertEquals(self.calculate(22059, -761154259), 761176318)

    def test0676(self):
        self.assertEquals(self.calculate(-22494, 1848984108), -1849006602)

    def test0677(self):
        self.assertEquals(self.calculate(6998, -1607263671), 1607270669)

    def test0678(self):
        self.assertEquals(self.calculate(8958, 154574911), -154565953)

    def test0679(self):
        self.assertEquals(self.calculate(28483, -519729266), 519757749)

    def test0680(self):
        self.assertEquals(self.calculate(-28221, -1455100311), 1455072090)

    def test0681(self):
        self.assertEquals(self.calculate(-2547, -736406939), 736404392)

    def test0682(self):
        self.assertEquals(self.calculate(3433, 1030867019), -1030863586)

    def test0683(self):
        self.assertEquals(self.calculate(12010, 1579348218), -1579336208)

    def test0684(self):
        self.assertEquals(self.calculate(18432, 1236030855), -1236012423)

    def test0685(self):
        self.assertEquals(self.calculate(24680, -1927418122), 1927442802)

    def test0686(self):
        self.assertEquals(self.calculate(4466, -1443962535), 1443967001)

    def test0687(self):
        self.assertEquals(self.calculate(10759, -1268854856), 1268865615)

    def test0688(self):
        self.assertEquals(self.calculate(-31508, -193667830), 193636322)

    def test0689(self):
        self.assertEquals(self.calculate(4666, 87398072), -87393406)

    def test0690(self):
        self.assertEquals(self.calculate(-2100, 1133632717), -1133634817)

    def test0691(self):
        self.assertEquals(self.calculate(-17923, -107620725), 107602802)

    def test0692(self):
        self.assertEquals(self.calculate(-26790, -904747), 877957)

    def test0693(self):
        self.assertEquals(self.calculate(-23416, 164540639), -164564055)

    def test0694(self):
        self.assertEquals(self.calculate(30092, -2107156763), 2107186855)

    def test0695(self):
        self.assertEquals(self.calculate(-6902, -993377728), 993370826)

    def test0696(self):
        self.assertEquals(self.calculate(-14044, 162967951), -162981995)

    def test0697(self):
        self.assertEquals(self.calculate(29325, 407912800), -407883475)

    def test0698(self):
        self.assertEquals(self.calculate(7425, 472378070), -472370645)

    def test0699(self):
        self.assertEquals(self.calculate(27756, 1632403533), -1632375777)

    def test0700(self):
        self.assertEquals(self.calculate(18567, 830693139), -830674572)

    def test0701(self):
        self.assertEquals(self.calculate(-13532, 1526331503), -1526345035)

    def test0702(self):
        self.assertEquals(self.calculate(-28908, -1490832543), 1490803635)

    def test0703(self):
        self.assertEquals(self.calculate(-22748, 2075660966), -2075683714)

    def test0704(self):
        self.assertEquals(self.calculate(-13794, 475760970), -475774764)

    def test0705(self):
        self.assertEquals(self.calculate(4929, 1702291040), -1702286111)

    def test0706(self):
        self.assertEquals(self.calculate(10238, 1101200671), -1101190433)

    def test0707(self):
        self.assertEquals(self.calculate(-24125, 903270064), -903294189)

    def test0708(self):
        self.assertEquals(self.calculate(31605, -1284485732), 1284517337)

    def test0709(self):
        self.assertEquals(self.calculate(23685, -1739545652), 1739569337)

    def test0710(self):
        self.assertEquals(self.calculate(-3190, -537530592), 537527402)

    def test0711(self):
        self.assertEquals(self.calculate(-8228, -1241711570), 1241703342)

    def test0712(self):
        self.assertEquals(self.calculate(-4292, 1832398011), -1832402303)

    def test0713(self):
        self.assertEquals(self.calculate(21731, 1583473467), -1583451736)

    def test0714(self):
        self.assertEquals(self.calculate(-1901, -1291879069), 1291877168)

    def test0715(self):
        self.assertEquals(self.calculate(-12642, 1670916614), -1670929256)

    def test0716(self):
        self.assertEquals(self.calculate(5144, 2059553148), -2059548004)

    def test0717(self):
        self.assertEquals(self.calculate(30652, -973660499), 973691151)

    def test0718(self):
        self.assertEquals(self.calculate(32304, -2011348654), 2011380958)

    def test0719(self):
        self.assertEquals(self.calculate(27749, -1665944259), 1665972008)

    def test0720(self):
        self.assertEquals(self.calculate(14903, 1843406211), -1843391308)

    def test0721(self):
        self.assertEquals(self.calculate(-27420, 1673690135), -1673717555)

    def test0722(self):
        self.assertEquals(self.calculate(10534, -1605780730), 1605791264)

    def test0723(self):
        self.assertEquals(self.calculate(-4759, -1001645729), 1001640970)

    def test0724(self):
        self.assertEquals(self.calculate(20215, 1099478836), -1099458621)

    def test0725(self):
        self.assertEquals(self.calculate(5105, -1492681329), 1492686434)

    def test0726(self):
        self.assertEquals(self.calculate(-20972, 819442192), -819463164)

    def test0727(self):
        self.assertEquals(self.calculate(-31382, -241817336), 241785954)

    def test0728(self):
        self.assertEquals(self.calculate(8806, -1992247394), 1992256200)

    def test0729(self):
        self.assertEquals(self.calculate(24261, -1831525088), 1831549349)

    def test0730(self):
        self.assertEquals(self.calculate(-16542, 568601359), -568617901)

    def test0731(self):
        self.assertEquals(self.calculate(-26867, 1227552157), -1227579024)

    def test0732(self):
        self.assertEquals(self.calculate(-30773, 1388178408), -1388209181)

    def test0733(self):
        self.assertEquals(self.calculate(-3075, 2022117513), -2022120588)

    def test0734(self):
        self.assertEquals(self.calculate(-16029, 1815173741), -1815189770)

    def test0735(self):
        self.assertEquals(self.calculate(-12687, -149573504), 149560817)

    def test0736(self):
        self.assertEquals(self.calculate(10074, -1219923992), 1219934066)

    def test0737(self):
        self.assertEquals(self.calculate(22307, -812160259), 812182566)

    def test0738(self):
        self.assertEquals(self.calculate(-28852, 905525189), -905554041)

    def test0739(self):
        self.assertEquals(self.calculate(-32236, 589410889), -589443125)

    def test0740(self):
        self.assertEquals(self.calculate(-27079, -151563519), 151536440)

    def test0741(self):
        self.assertEquals(self.calculate(18307, 1547640136), -1547621829)

    def test0742(self):
        self.assertEquals(self.calculate(-22293, -1917799538), 1917777245)

    def test0743(self):
        self.assertEquals(self.calculate(17148, -2119027993), 2119045141)

    def test0744(self):
        self.assertEquals(self.calculate(25171, 2113370877), -2113345706)

    def test0745(self):
        self.assertEquals(self.calculate(-12277, -276878466), 276866189)

    def test0746(self):
        self.assertEquals(self.calculate(31964, -1618535199), 1618567163)

    def test0747(self):
        self.assertEquals(self.calculate(-7605, -1388187078), 1388179473)

    def test0748(self):
        self.assertEquals(self.calculate(19242, -517726650), 517745892)

    def test0749(self):
        self.assertEquals(self.calculate(-13960, -775467083), 775453123)

    def test0750(self):
        self.assertEquals(self.calculate(31670, -123066047), 123097717)

    def test0751(self):
        self.assertEquals(self.calculate(3390, -1401276467), 1401279857)

    def test0752(self):
        self.assertEquals(self.calculate(-30008, -1356852973), 1356822965)

    def test0753(self):
        self.assertEquals(self.calculate(-28924, 1603284370), -1603313294)

    def test0754(self):
        self.assertEquals(self.calculate(-18445, -1857918160), 1857899715)

    def test0755(self):
        self.assertEquals(self.calculate(21210, -1180890363), 1180911573)

    def test0756(self):
        self.assertEquals(self.calculate(-18335, -1988992805), 1988974470)

    def test0757(self):
        self.assertEquals(self.calculate(-15836, -1457379306), 1457363470)

    def test0758(self):
        self.assertEquals(self.calculate(-8030, -768824906), 768816876)

    def test0759(self):
        self.assertEquals(self.calculate(10109, -418111037), 418121146)

    def test0760(self):
        self.assertEquals(self.calculate(-25593, 1008831920), -1008857513)

    def test0761(self):
        self.assertEquals(self.calculate(9252, 125640002), -125630750)

    def test0762(self):
        self.assertEquals(self.calculate(8948, -44346030), 44354978)

    def test0763(self):
        self.assertEquals(self.calculate(30422, 1933015409), -1932984987)

    def test0764(self):
        self.assertEquals(self.calculate(13392, 1873689055), -1873675663)

    def test0765(self):
        self.assertEquals(self.calculate(-20873, 862973396), -862994269)

    def test0766(self):
        self.assertEquals(self.calculate(-22075, -993540967), 993518892)

    def test0767(self):
        self.assertEquals(self.calculate(-13286, -172274034), 172260748)

    def test0768(self):
        self.assertEquals(self.calculate(30360, -873213745), 873244105)

    def test0769(self):
        self.assertEquals(self.calculate(-28824, -1071151805), 1071122981)

    def test0770(self):
        self.assertEquals(self.calculate(-3197, -1912410246), 1912407049)

    def test0771(self):
        self.assertEquals(self.calculate(-11973, -2076196594), 2076184621)

    def test0772(self):
        self.assertEquals(self.calculate(-3972, 1213673822), -1213677794)

    def test0773(self):
        self.assertEquals(self.calculate(-28810, 668968188), -668996998)

    def test0774(self):
        self.assertEquals(self.calculate(25398, -897321443), 897346841)

    def test0775(self):
        self.assertEquals(self.calculate(4004, 1856165762), -1856161758)

    def test0776(self):
        self.assertEquals(self.calculate(13469, -1979249258), 1979262727)

    def test0777(self):
        self.assertEquals(self.calculate(11782, 375728459), -375716677)

    def test0778(self):
        self.assertEquals(self.calculate(602, 254513738), -254513136)

    def test0779(self):
        self.assertEquals(self.calculate(-3355, 1589583435), -1589586790)

    def test0780(self):
        self.assertEquals(self.calculate(-20913, -822763080), 822742167)

    def test0781(self):
        self.assertEquals(self.calculate(31838, -1126468933), 1126500771)

    def test0782(self):
        self.assertEquals(self.calculate(-9422, -887294317), 887284895)

    def test0783(self):
        self.assertEquals(self.calculate(29221, 2073239907), -2073210686)

    def test0784(self):
        self.assertEquals(self.calculate(-21741, 1081130292), -1081152033)

    def test0785(self):
        self.assertEquals(self.calculate(23153, 1917802498), -1917779345)

    def test0786(self):
        self.assertEquals(self.calculate(-6915, -1254310959), 1254304044)

    def test0787(self):
        self.assertEquals(self.calculate(18117, -675661398), 675679515)

    def test0788(self):
        self.assertEquals(self.calculate(-3233, -1749037942), 1749034709)

    def test0789(self):
        self.assertEquals(self.calculate(-7581, -1709421878), 1709414297)

    def test0790(self):
        self.assertEquals(self.calculate(17854, 1092477901), -1092460047)

    def test0791(self):
        self.assertEquals(self.calculate(-16174, -916002145), 915985971)

    def test0792(self):
        self.assertEquals(self.calculate(5527, 1301498001), -1301492474)

    def test0793(self):
        self.assertEquals(self.calculate(-24792, -1080515235), 1080490443)

    def test0794(self):
        self.assertEquals(self.calculate(11585, -1082120916), 1082132501)

    def test0795(self):
        self.assertEquals(self.calculate(25115, -405314083), 405339198)

    def test0796(self):
        self.assertEquals(self.calculate(-15394, -482881543), 482866149)

    def test0797(self):
        self.assertEquals(self.calculate(-25079, 96548291), -96573370)

    def test0798(self):
        self.assertEquals(self.calculate(-7605, -885256285), 885248680)

    def test0799(self):
        self.assertEquals(self.calculate(-27651, -236827499), 236799848)

    def test0800(self):
        self.assertEquals(self.calculate(-2143, -2134220834), 2134218691)

    def test0801(self):
        self.assertEquals(self.calculate(32327, 318658755), -318626428)

    def test0802(self):
        self.assertEquals(self.calculate(12469, 1597627805), -1597615336)

    def test0803(self):
        self.assertEquals(self.calculate(979, -1556617352), 1556618331)

    def test0804(self):
        self.assertEquals(self.calculate(28003, -804363078), 804391081)

    def test0805(self):
        self.assertEquals(self.calculate(-10164, -95849979), 95839815)

    def test0806(self):
        self.assertEquals(self.calculate(17910, 2109053155), -2109035245)

    def test0807(self):
        self.assertEquals(self.calculate(-10967, -1780528113), 1780517146)

    def test0808(self):
        self.assertEquals(self.calculate(15905, 80090246), -80074341)

    def test0809(self):
        self.assertEquals(self.calculate(-25458, -1651078381), 1651052923)

    def test0810(self):
        self.assertEquals(self.calculate(9829, -1835930116), 1835939945)

    def test0811(self):
        self.assertEquals(self.calculate(30129, 1241514966), -1241484837)

    def test0812(self):
        self.assertEquals(self.calculate(-24133, -1575543770), 1575519637)

    def test0813(self):
        self.assertEquals(self.calculate(-19937, 2035240186), -2035260123)

    def test0814(self):
        self.assertEquals(self.calculate(-1419, -1820897972), 1820896553)

    def test0815(self):
        self.assertEquals(self.calculate(-3306, -339527179), 339523873)

    def test0816(self):
        self.assertEquals(self.calculate(-18378, 1347851287), -1347869665)

    def test0817(self):
        self.assertEquals(self.calculate(19296, -1921078707), 1921098003)

    def test0818(self):
        self.assertEquals(self.calculate(-11444, -251530403), 251518959)

    def test0819(self):
        self.assertEquals(self.calculate(30403, 236682468), -236652065)

    def test0820(self):
        self.assertEquals(self.calculate(-18029, -2006507114), 2006489085)

    def test0821(self):
        self.assertEquals(self.calculate(25807, 185261667), -185235860)

    def test0822(self):
        self.assertEquals(self.calculate(-514, -74525761), 74525247)

    def test0823(self):
        self.assertEquals(self.calculate(-11808, -710670036), 710658228)

    def test0824(self):
        self.assertEquals(self.calculate(-24873, 254857010), -254881883)

    def test0825(self):
        self.assertEquals(self.calculate(10015, -1423306576), 1423316591)

    def test0826(self):
        self.assertEquals(self.calculate(-27666, -883735048), 883707382)

    def test0827(self):
        self.assertEquals(self.calculate(28434, 1112210715), -1112182281)

    def test0828(self):
        self.assertEquals(self.calculate(-5494, -899161487), 899155993)

    def test0829(self):
        self.assertEquals(self.calculate(-9305, -822457502), 822448197)

    def test0830(self):
        self.assertEquals(self.calculate(9165, 2021754746), -2021745581)

    def test0831(self):
        self.assertEquals(self.calculate(-9275, -1221813120), 1221803845)

    def test0832(self):
        self.assertEquals(self.calculate(-27961, -185583523), 185555562)

    def test0833(self):
        self.assertEquals(self.calculate(-9556, 431941820), -431951376)

    def test0834(self):
        self.assertEquals(self.calculate(-26351, -650492547), 650466196)

    def test0835(self):
        self.assertEquals(self.calculate(-26561, -1256107948), 1256081387)

    def test0836(self):
        self.assertEquals(self.calculate(2051, -1002917124), 1002919175)

    def test0837(self):
        self.assertEquals(self.calculate(22221, -636834208), 636856429)

    def test0838(self):
        self.assertEquals(self.calculate(4264, 947435189), -947430925)

    def test0839(self):
        self.assertEquals(self.calculate(12200, -2052226666), 2052238866)

    def test0840(self):
        self.assertEquals(self.calculate(2713, -1485197436), 1485200149)

    def test0841(self):
        self.assertEquals(self.calculate(166, -1645879975), 1645880141)

    def test0842(self):
        self.assertEquals(self.calculate(29022, 377709956), -377680934)

    def test0843(self):
        self.assertEquals(self.calculate(19102, 1546934571), -1546915469)

    def test0844(self):
        self.assertEquals(self.calculate(-2064, 799058757), -799060821)

    def test0845(self):
        self.assertEquals(self.calculate(-95, -296714921), 296714826)

    def test0846(self):
        self.assertEquals(self.calculate(24284, 1049141774), -1049117490)

    def test0847(self):
        self.assertEquals(self.calculate(30496, -39741172), 39771668)

    def test0848(self):
        self.assertEquals(self.calculate(-2472, -1930339472), 1930337000)

    def test0849(self):
        self.assertEquals(self.calculate(-24026, -1059227642), 1059203616)

    def test0850(self):
        self.assertEquals(self.calculate(-17425, -1860781455), 1860764030)

    def test0851(self):
        self.assertEquals(self.calculate(-26653, -622013195), 621986542)

    def test0852(self):
        self.assertEquals(self.calculate(-10565, -1758560907), 1758550342)

    def test0853(self):
        self.assertEquals(self.calculate(16378, 2049429347), -2049412969)

    def test0854(self):
        self.assertEquals(self.calculate(1067, 557048944), -557047877)

    def test0855(self):
        self.assertEquals(self.calculate(5825, -1150116854), 1150122679)

    def test0856(self):
        self.assertEquals(self.calculate(2430, 221662121), -221659691)

    def test0857(self):
        self.assertEquals(self.calculate(-17127, -1330284712), 1330267585)

    def test0858(self):
        self.assertEquals(self.calculate(4495, 828219637), -828215142)

    def test0859(self):
        self.assertEquals(self.calculate(-11985, -1082993646), 1082981661)

    def test0860(self):
        self.assertEquals(self.calculate(24312, 251751430), -251727118)

    def test0861(self):
        self.assertEquals(self.calculate(-17439, 972206555), -972223994)

    def test0862(self):
        self.assertEquals(self.calculate(-10054, -271231458), 271221404)

    def test0863(self):
        self.assertEquals(self.calculate(1383, -1579789667), 1579791050)

    def test0864(self):
        self.assertEquals(self.calculate(-2125, 1710378289), -1710380414)

    def test0865(self):
        self.assertEquals(self.calculate(29204, 2116236556), -2116207352)

    def test0866(self):
        self.assertEquals(self.calculate(31424, -1516099301), 1516130725)

    def test0867(self):
        self.assertEquals(self.calculate(16919, -664792193), 664809112)

    def test0868(self):
        self.assertEquals(self.calculate(879, -1976277751), 1976278630)

    def test0869(self):
        self.assertEquals(self.calculate(3338, -1663723032), 1663726370)

    def test0870(self):
        self.assertEquals(self.calculate(-27912, 1384057251), -1384085163)

    def test0871(self):
        self.assertEquals(self.calculate(15280, -372117510), 372132790)

    def test0872(self):
        self.assertEquals(self.calculate(-31885, -326822361), 326790476)

    def test0873(self):
        self.assertEquals(self.calculate(-6587, -2070617443), 2070610856)

    def test0874(self):
        self.assertEquals(self.calculate(-19592, 811994196), -812013788)

    def test0875(self):
        self.assertEquals(self.calculate(2733, 1230365368), -1230362635)

    def test0876(self):
        self.assertEquals(self.calculate(26820, -205684356), 205711176)

    def test0877(self):
        self.assertEquals(self.calculate(-19611, -785426968), 785407357)

    def test0878(self):
        self.assertEquals(self.calculate(-21578, -1342528886), 1342507308)

    def test0879(self):
        self.assertEquals(self.calculate(-28888, -1963355269), 1963326381)

    def test0880(self):
        self.assertEquals(self.calculate(-22052, 1121235775), -1121257827)

    def test0881(self):
        self.assertEquals(self.calculate(5473, -742179576), 742185049)

    def test0882(self):
        self.assertEquals(self.calculate(-7616, 2019321997), -2019329613)

    def test0883(self):
        self.assertEquals(self.calculate(6909, 166877231), -166870322)

    def test0884(self):
        self.assertEquals(self.calculate(-32472, 2081817310), -2081849782)

    def test0885(self):
        self.assertEquals(self.calculate(3489, 61913604), -61910115)

    def test0886(self):
        self.assertEquals(self.calculate(10501, 113575150), -113564649)

    def test0887(self):
        self.assertEquals(self.calculate(24476, -947972250), 947996726)

    def test0888(self):
        self.assertEquals(self.calculate(811, 1118293167), -1118292356)

    def test0889(self):
        self.assertEquals(self.calculate(-31091, 1097030431), -1097061522)

    def test0890(self):
        self.assertEquals(self.calculate(8283, -908343388), 908351671)

    def test0891(self):
        self.assertEquals(self.calculate(-19529, -1040394972), 1040375443)

    def test0892(self):
        self.assertEquals(self.calculate(-26029, 1487361569), -1487387598)

    def test0893(self):
        self.assertEquals(self.calculate(4717, 905196639), -905191922)

    def test0894(self):
        self.assertEquals(self.calculate(16530, 2052531956), -2052515426)

    def test0895(self):
        self.assertEquals(self.calculate(-13669, 1356271193), -1356284862)

    def test0896(self):
        self.assertEquals(self.calculate(-7034, -242926100), 242919066)

    def test0897(self):
        self.assertEquals(self.calculate(-3595, -1275167240), 1275163645)

    def test0898(self):
        self.assertEquals(self.calculate(4019, -690481821), 690485840)

    def test0899(self):
        self.assertEquals(self.calculate(4158, 178591627), -178587469)

    def test0900(self):
        self.assertEquals(self.calculate(-10167, 292010299), -292020466)

    def test0901(self):
        self.assertEquals(self.calculate(9964, 106234481), -106224517)

    def test0902(self):
        self.assertEquals(self.calculate(-24202, -197980892), 197956690)

    def test0903(self):
        self.assertEquals(self.calculate(19332, -1083344813), 1083364145)

    def test0904(self):
        self.assertEquals(self.calculate(10022, -953633935), 953643957)

    def test0905(self):
        self.assertEquals(self.calculate(-27346, 1388992857), -1389020203)

    def test0906(self):
        self.assertEquals(self.calculate(-10576, -1364368270), 1364357694)

    def test0907(self):
        self.assertEquals(self.calculate(-22354, 1962955569), -1962977923)

    def test0908(self):
        self.assertEquals(self.calculate(-25146, -1649192236), 1649167090)

    def test0909(self):
        self.assertEquals(self.calculate(30841, -766086316), 766117157)

    def test0910(self):
        self.assertEquals(self.calculate(27513, -1185156684), 1185184197)

    def test0911(self):
        self.assertEquals(self.calculate(-28830, 1776507611), -1776536441)

    def test0912(self):
        self.assertEquals(self.calculate(-7429, 725041197), -725048626)

    def test0913(self):
        self.assertEquals(self.calculate(-32693, 867054634), -867087327)

    def test0914(self):
        self.assertEquals(self.calculate(17748, -166390520), 166408268)

    def test0915(self):
        self.assertEquals(self.calculate(-1296, -1819753429), 1819752133)

    def test0916(self):
        self.assertEquals(self.calculate(844, -1823175471), 1823176315)

    def test0917(self):
        self.assertEquals(self.calculate(13323, -400697526), 400710849)

    def test0918(self):
        self.assertEquals(self.calculate(2909, 283081155), -283078246)

    def test0919(self):
        self.assertEquals(self.calculate(-27860, 1356935205), -1356963065)

    def test0920(self):
        self.assertEquals(self.calculate(7991, 1599969376), -1599961385)

    def test0921(self):
        self.assertEquals(self.calculate(-13108, 960289006), -960302114)

    def test0922(self):
        self.assertEquals(self.calculate(-2647, -970779541), 970776894)

    def test0923(self):
        self.assertEquals(self.calculate(-10759, 1678619657), -1678630416)

    def test0924(self):
        self.assertEquals(self.calculate(3154, -1337644055), 1337647209)

    def test0925(self):
        self.assertEquals(self.calculate(-7180, 377211521), -377218701)

    def test0926(self):
        self.assertEquals(self.calculate(-20698, -1601325920), 1601305222)

    def test0927(self):
        self.assertEquals(self.calculate(-12780, -1722806240), 1722793460)

    def test0928(self):
        self.assertEquals(self.calculate(7469, -1184967554), 1184975023)

    def test0929(self):
        self.assertEquals(self.calculate(-25561, -1925874098), 1925848537)

    def test0930(self):
        self.assertEquals(self.calculate(11533, -1662387241), 1662398774)

    def test0931(self):
        self.assertEquals(self.calculate(-17100, -93975662), 93958562)

    def test0932(self):
        self.assertEquals(self.calculate(15206, -1345803632), 1345818838)

    def test0933(self):
        self.assertEquals(self.calculate(-29306, -2009317286), 2009287980)

    def test0934(self):
        self.assertEquals(self.calculate(-8239, -600072028), 600063789)

    def test0935(self):
        self.assertEquals(self.calculate(-17141, -1888798812), 1888781671)

    def test0936(self):
        self.assertEquals(self.calculate(-13932, 1540378296), -1540392228)

    def test0937(self):
        self.assertEquals(self.calculate(-1567, 380391638), -380393205)

    def test0938(self):
        self.assertEquals(self.calculate(-5354, 298161946), -298167300)

    def test0939(self):
        self.assertEquals(self.calculate(3657, 902597947), -902594290)

    def test0940(self):
        self.assertEquals(self.calculate(31278, -1905412142), 1905443420)

    def test0941(self):
        self.assertEquals(self.calculate(6793, -60621371), 60628164)

    def test0942(self):
        self.assertEquals(self.calculate(-26838, 1173826961), -1173853799)

    def test0943(self):
        self.assertEquals(self.calculate(8662, -1670926869), 1670935531)

    def test0944(self):
        self.assertEquals(self.calculate(373, -91325278), 91325651)

    def test0945(self):
        self.assertEquals(self.calculate(18176, 1942186106), -1942167930)

    def test0946(self):
        self.assertEquals(self.calculate(30949, 787944982), -787914033)

    def test0947(self):
        self.assertEquals(self.calculate(-20173, -302232375), 302212202)

    def test0948(self):
        self.assertEquals(self.calculate(9353, -389001996), 389011349)

    def test0949(self):
        self.assertEquals(self.calculate(6011, -1127513681), 1127519692)

    def test0950(self):
        self.assertEquals(self.calculate(7895, -1043644934), 1043652829)

    def test0951(self):
        self.assertEquals(self.calculate(7628, -1299039791), 1299047419)

    def test0952(self):
        self.assertEquals(self.calculate(-30759, 2059891056), -2059921815)

    def test0953(self):
        self.assertEquals(self.calculate(15855, 873146900), -873131045)

    def test0954(self):
        self.assertEquals(self.calculate(29448, 1122680792), -1122651344)

    def test0955(self):
        self.assertEquals(self.calculate(-22696, -1509261896), 1509239200)

    def test0956(self):
        self.assertEquals(self.calculate(-16109, -836848100), 836831991)

    def test0957(self):
        self.assertEquals(self.calculate(-19882, 1528538471), -1528558353)

    def test0958(self):
        self.assertEquals(self.calculate(-32398, -1943897910), 1943865512)

    def test0959(self):
        self.assertEquals(self.calculate(-14673, 970416511), -970431184)

    def test0960(self):
        self.assertEquals(self.calculate(-13673, -49585180), 49571507)

    def test0961(self):
        self.assertEquals(self.calculate(23208, -1836950273), 1836973481)

    def test0962(self):
        self.assertEquals(self.calculate(22261, 783428443), -783406182)

    def test0963(self):
        self.assertEquals(self.calculate(-2124, -282101119), 282098995)

    def test0964(self):
        self.assertEquals(self.calculate(4309, -1675306172), 1675310481)

    def test0965(self):
        self.assertEquals(self.calculate(-11500, 1318678809), -1318690309)

    def test0966(self):
        self.assertEquals(self.calculate(22385, 971717193), -971694808)

    def test0967(self):
        self.assertEquals(self.calculate(20749, -141994801), 142015550)

    def test0968(self):
        self.assertEquals(self.calculate(27875, -1943733107), 1943760982)

    def test0969(self):
        self.assertEquals(self.calculate(-26916, -221314867), 221287951)

    def test0970(self):
        self.assertEquals(self.calculate(-30122, 944003242), -944033364)

    def test0971(self):
        self.assertEquals(self.calculate(21035, 1057540329), -1057519294)

    def test0972(self):
        self.assertEquals(self.calculate(-8784, -2007393428), 2007384644)

    def test0973(self):
        self.assertEquals(self.calculate(-15984, 1941659753), -1941675737)

    def test0974(self):
        self.assertEquals(self.calculate(-25432, -2097859727), 2097834295)

    def test0975(self):
        self.assertEquals(self.calculate(24667, -586842651), 586867318)

    def test0976(self):
        self.assertEquals(self.calculate(13907, -1162115551), 1162129458)

    def test0977(self):
        self.assertEquals(self.calculate(6276, -2028040842), 2028047118)

    def test0978(self):
        self.assertEquals(self.calculate(-1910, 1882807950), -1882809860)

    def test0979(self):
        self.assertEquals(self.calculate(-24392, -1813474112), 1813449720)

    def test0980(self):
        self.assertEquals(self.calculate(-21012, 1605168413), -1605189425)

    def test0981(self):
        self.assertEquals(self.calculate(10741, -1955298421), 1955309162)

    def test0982(self):
        self.assertEquals(self.calculate(-29771, -1779795469), 1779765698)

    def test0983(self):
        self.assertEquals(self.calculate(-16526, -1153544150), 1153527624)

    def test0984(self):
        self.assertEquals(self.calculate(20628, -1055895941), 1055916569)

    def test0985(self):
        self.assertEquals(self.calculate(-2346, 1280265892), -1280268238)

    def test0986(self):
        self.assertEquals(self.calculate(-12590, -1299323479), 1299310889)

    def test0987(self):
        self.assertEquals(self.calculate(10726, 1637927555), -1637916829)

    def test0988(self):
        self.assertEquals(self.calculate(-3043, -1487174054), 1487171011)

    def test0989(self):
        self.assertEquals(self.calculate(7659, -999910967), 999918626)

    def test0990(self):
        self.assertEquals(self.calculate(23711, -1032234031), 1032257742)

    def test0991(self):
        self.assertEquals(self.calculate(16077, 1760877310), -1760861233)

    def test0992(self):
        self.assertEquals(self.calculate(-18289, -1998644036), 1998625747)

    def test0993(self):
        self.assertEquals(self.calculate(6086, -712598572), 712604658)

    def test0994(self):
        self.assertEquals(self.calculate(-16998, -638934904), 638917906)

    def test0995(self):
        self.assertEquals(self.calculate(16773, 190305186), -190288413)

    def test0996(self):
        self.assertEquals(self.calculate(7639, 1357951968), -1357944329)

    def test0997(self):
        self.assertEquals(self.calculate(26084, -1824465485), 1824491569)

    def test0998(self):
        self.assertEquals(self.calculate(4240, -1170843007), 1170847247)

    def test0999(self):
        self.assertEquals(self.calculate(7606, -313956924), 313964530)

    def test1000(self):
        self.assertEquals(self.calculate(-8341, -98658316), 98649975)

    def test1001(self):
        self.assertEquals(self.calculate(-27088, 1377399133), -1377426221)

    def test1002(self):
        self.assertEquals(self.calculate(10998, 765580057), -765569059)

    def test1003(self):
        self.assertEquals(self.calculate(-11114, 1144904446), -1144915560)

    def test1004(self):
        self.assertEquals(self.calculate(14256, -1027593352), 1027607608)

    def test1005(self):
        self.assertEquals(self.calculate(14402, 2102368328), -2102353926)

    def test1006(self):
        self.assertEquals(self.calculate(21750, 761994329), -761972579)

    def test1007(self):
        self.assertEquals(self.calculate(-13976, 753807743), -753821719)

    def test1008(self):
        self.assertEquals(self.calculate(22966, -1993783927), 1993806893)

    def test1009(self):
        self.assertEquals(self.calculate(-29201, -947027562), 946998361)

    def test1010(self):
        self.assertEquals(self.calculate(16489, 290436620), -290420131)

    def test1011(self):
        self.assertEquals(self.calculate(-2229, 1377910130), -1377912359)

    def test1012(self):
        self.assertEquals(self.calculate(24382, -1058003455), 1058027837)

    def test1013(self):
        self.assertEquals(self.calculate(1431, -1585575002), 1585576433)

    def test1014(self):
        self.assertEquals(self.calculate(8560, -1100353727), 1100362287)

    def test1015(self):
        self.assertEquals(self.calculate(20062, -273790360), 273810422)

    def test1016(self):
        self.assertEquals(self.calculate(-5087, 2056091327), -2056096414)

    def test1017(self):
        self.assertEquals(self.calculate(-21487, 1772657232), -1772678719)

    def test1018(self):
        self.assertEquals(self.calculate(26305, 2091573452), -2091547147)

    def test1019(self):
        self.assertEquals(self.calculate(-27074, 619460342), -619487416)

    def test1020(self):
        self.assertEquals(self.calculate(6383, 1275844160), -1275837777)

    def test1021(self):
        self.assertEquals(self.calculate(-30059, 841500116), -841530175)

    def test1022(self):
        self.assertEquals(self.calculate(-3128, -1047974818), 1047971690)

    def test1023(self):
        self.assertEquals(self.calculate(7151, 905580482), -905573331)


class TestVM_Sub_IntFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushF(rhs)
        v.VM_Sub()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-983, -144770.0), 143787.00, "")

    def test0001(self):
        self.assertEquals(self.calculate(20205, -82685.0), 102890.00, "")

    def test0002(self):
        self.assertEquals(self.calculate(14883, -15970.0), 30853.00, "")

    def test0003(self):
        self.assertEquals(self.calculate(-27344, 31764.0), -59108.00, "")

    def test0004(self):
        self.assertEquals(self.calculate(14282, 147336.0), -133054.00, "")

    def test0005(self):
        self.assertEquals(self.calculate(69, -85330.0), 85399.00, "")

    def test0006(self):
        self.assertEquals(self.calculate(-22722, 163763.0), -186485.00, "")

    def test0007(self):
        self.assertEquals(self.calculate(5100, 103046.0), -97946.00, "")

    def test0008(self):
        self.assertEquals(self.calculate(-16676, -99539.0), 82863.00, "")

    def test0009(self):
        self.assertEquals(self.calculate(-9984, -156055.0), 146071.00, "")

    def test0010(self):
        self.assertEquals(self.calculate(17723, -120849.0), 138572.00, "")

    def test0011(self):
        self.assertEquals(self.calculate(-24710, 145293.0), -170003.00, "")

    def test0012(self):
        self.assertEquals(self.calculate(7480, -82173.0), 89653.00, "")

    def test0013(self):
        self.assertEquals(self.calculate(-2120, -40239.0), 38119.00, "")

    def test0014(self):
        self.assertEquals(self.calculate(-30590, -1468.0), -29122.00, "")

    def test0015(self):
        self.assertEquals(self.calculate(3262, -24394.0), 27656.00, "")

    def test0016(self):
        self.assertEquals(self.calculate(-22708, 96623.0), -119331.00, "")

    def test0017(self):
        self.assertEquals(self.calculate(-15038, 80550.0), -95588.00, "")

    def test0018(self):
        self.assertEquals(self.calculate(-32227, 171901.0), -204128.00, "")

    def test0019(self):
        self.assertEquals(self.calculate(22282, 33554.0), -11272.00, "")

    def test0020(self):
        self.assertEquals(self.calculate(-15944, 158556.0), -174500.00, "")

    def test0021(self):
        self.assertEquals(self.calculate(-18122, 101158.0), -119280.00, "")

    def test0022(self):
        self.assertEquals(self.calculate(30744, 156560.0), -125816.00, "")

    def test0023(self):
        self.assertEquals(self.calculate(5937, 146737.0), -140800.00, "")

    def test0024(self):
        self.assertEquals(self.calculate(15528, 45579.0), -30051.00, "")

    def test0025(self):
        self.assertEquals(self.calculate(-16796, 157832.0), -174628.00, "")

    def test0026(self):
        self.assertEquals(self.calculate(6792, -90235.0), 97027.00, "")

    def test0027(self):
        self.assertEquals(self.calculate(-31113, -179116.0), 148003.00, "")

    def test0028(self):
        self.assertEquals(self.calculate(17583, -66496.0), 84079.00, "")

    def test0029(self):
        self.assertEquals(self.calculate(31574, 190596.0), -159022.00, "")

    def test0030(self):
        self.assertEquals(self.calculate(14376, -144925.0), 159301.00, "")

    def test0031(self):
        self.assertEquals(self.calculate(26223, -186093.0), 212316.00, "")

    def test0032(self):
        self.assertEquals(self.calculate(-6584, 937.0), -7521.00, "")

    def test0033(self):
        self.assertEquals(self.calculate(424, -175443.0), 175867.00, "")

    def test0034(self):
        self.assertEquals(self.calculate(14691, 173469.0), -158778.00, "")

    def test0035(self):
        self.assertEquals(self.calculate(-10865, -5463.0), -5402.00, "")

    def test0036(self):
        self.assertEquals(self.calculate(2156, -90688.0), 92844.00, "")

    def test0037(self):
        self.assertEquals(self.calculate(-1635, 112707.0), -114342.00, "")

    def test0038(self):
        self.assertEquals(self.calculate(-2283, -8006.0), 5723.00, "")

    def test0039(self):
        self.assertEquals(self.calculate(-13797, -39605.0), 25808.00, "")

    def test0040(self):
        self.assertEquals(self.calculate(24004, 180787.0), -156783.00, "")

    def test0041(self):
        self.assertEquals(self.calculate(10242, 194094.0), -183852.00, "")

    def test0042(self):
        self.assertEquals(self.calculate(25108, 71087.0), -45979.00, "")

    def test0043(self):
        self.assertEquals(self.calculate(6632, -184737.0), 191369.00, "")

    def test0044(self):
        self.assertEquals(self.calculate(25579, 44427.0), -18848.00, "")

    def test0045(self):
        self.assertEquals(self.calculate(13053, -155334.0), 168387.00, "")

    def test0046(self):
        self.assertEquals(self.calculate(7796, 82466.0), -74670.00, "")

    def test0047(self):
        self.assertEquals(self.calculate(-16765, 63306.0), -80071.00, "")

    def test0048(self):
        self.assertEquals(self.calculate(-6815, 193611.0), -200426.00, "")

    def test0049(self):
        self.assertEquals(self.calculate(6739, 64704.0), -57965.00, "")

    def test0050(self):
        self.assertEquals(self.calculate(2491, -171789.0), 174280.00, "")

    def test0051(self):
        self.assertEquals(self.calculate(5597, 34642.0), -29045.00, "")

    def test0052(self):
        self.assertEquals(self.calculate(-218, 141778.0), -141996.00, "")

    def test0053(self):
        self.assertEquals(self.calculate(10771, -23393.0), 34164.00, "")

    def test0054(self):
        self.assertEquals(self.calculate(15775, 27104.0), -11329.00, "")

    def test0055(self):
        self.assertEquals(self.calculate(-722, -183875.0), 183153.00, "")

    def test0056(self):
        self.assertEquals(self.calculate(-7109, -98435.0), 91326.00, "")

    def test0057(self):
        self.assertEquals(self.calculate(-17155, 78137.0), -95292.00, "")

    def test0058(self):
        self.assertEquals(self.calculate(4624, -33138.0), 37762.00, "")

    def test0059(self):
        self.assertEquals(self.calculate(9675, 72467.0), -62792.00, "")

    def test0060(self):
        self.assertEquals(self.calculate(-2952, 151586.0), -154538.00, "")

    def test0061(self):
        self.assertEquals(self.calculate(18551, -140277.0), 158828.00, "")

    def test0062(self):
        self.assertEquals(self.calculate(-5798, 183774.0), -189572.00, "")

    def test0063(self):
        self.assertEquals(self.calculate(11633, -180345.0), 191978.00, "")

    def test0064(self):
        self.assertEquals(self.calculate(5177, 148752.0), -143575.00, "")

    def test0065(self):
        self.assertEquals(self.calculate(22567, -103829.0), 126396.00, "")

    def test0066(self):
        self.assertEquals(self.calculate(4366, 149393.0), -145027.00, "")

    def test0067(self):
        self.assertEquals(self.calculate(9534, 28142.0), -18608.00, "")

    def test0068(self):
        self.assertEquals(self.calculate(30489, 57454.0), -26965.00, "")

    def test0069(self):
        self.assertEquals(self.calculate(7812, -82596.0), 90408.00, "")

    def test0070(self):
        self.assertEquals(self.calculate(14860, -190235.0), 205095.00, "")

    def test0071(self):
        self.assertEquals(self.calculate(32448, 60855.0), -28407.00, "")

    def test0072(self):
        self.assertEquals(self.calculate(-21958, -50248.0), 28290.00, "")

    def test0073(self):
        self.assertEquals(self.calculate(-31843, -121066.0), 89223.00, "")

    def test0074(self):
        self.assertEquals(self.calculate(-3512, 193569.0), -197081.00, "")

    def test0075(self):
        self.assertEquals(self.calculate(-22005, 173865.0), -195870.00, "")

    def test0076(self):
        self.assertEquals(self.calculate(-17641, -8028.0), -9613.00, "")

    def test0077(self):
        self.assertEquals(self.calculate(-6777, -35259.0), 28482.00, "")

    def test0078(self):
        self.assertEquals(self.calculate(18033, -54651.0), 72684.00, "")

    def test0079(self):
        self.assertEquals(self.calculate(-25288, -197481.0), 172193.00, "")

    def test0080(self):
        self.assertEquals(self.calculate(-24161, -40324.0), 16163.00, "")

    def test0081(self):
        self.assertEquals(self.calculate(-3266, -193867.0), 190601.00, "")

    def test0082(self):
        self.assertEquals(self.calculate(-23080, -4813.0), -18267.00, "")

    def test0083(self):
        self.assertEquals(self.calculate(-2277, 126563.0), -128840.00, "")

    def test0084(self):
        self.assertEquals(self.calculate(15382, 38379.0), -22997.00, "")

    def test0085(self):
        self.assertEquals(self.calculate(-16311, -198299.0), 181988.00, "")

    def test0086(self):
        self.assertEquals(self.calculate(11815, 156460.0), -144645.00, "")

    def test0087(self):
        self.assertEquals(self.calculate(-24198, -8805.0), -15393.00, "")

    def test0088(self):
        self.assertEquals(self.calculate(23379, 63110.0), -39731.00, "")

    def test0089(self):
        self.assertEquals(self.calculate(5906, 124178.0), -118272.00, "")

    def test0090(self):
        self.assertEquals(self.calculate(24375, 179294.0), -154919.00, "")

    def test0091(self):
        self.assertEquals(self.calculate(28810, -138960.0), 167770.00, "")

    def test0092(self):
        self.assertEquals(self.calculate(3753, 48266.0), -44513.00, "")

    def test0093(self):
        self.assertEquals(self.calculate(-23098, 184474.0), -207572.00, "")

    def test0094(self):
        self.assertEquals(self.calculate(-26431, -109765.0), 83334.00, "")

    def test0095(self):
        self.assertEquals(self.calculate(-2093, -8828.0), 6735.00, "")

    def test0096(self):
        self.assertEquals(self.calculate(-2311, 139156.0), -141467.00, "")

    def test0097(self):
        self.assertEquals(self.calculate(22298, -7011.0), 29309.00, "")

    def test0098(self):
        self.assertEquals(self.calculate(-7012, -98741.0), 91729.00, "")

    def test0099(self):
        self.assertEquals(self.calculate(-16244, 117980.0), -134224.00, "")

    def test0100(self):
        self.assertEquals(self.calculate(-13078, 46350.0), -59428.00, "")

    def test0101(self):
        self.assertEquals(self.calculate(-10604, -158937.0), 148333.00, "")

    def test0102(self):
        self.assertEquals(self.calculate(-22135, -189757.0), 167622.00, "")

    def test0103(self):
        self.assertEquals(self.calculate(19574, 75998.0), -56424.00, "")

    def test0104(self):
        self.assertEquals(self.calculate(12335, 35825.0), -23490.00, "")

    def test0105(self):
        self.assertEquals(self.calculate(25589, 197878.0), -172289.00, "")

    def test0106(self):
        self.assertEquals(self.calculate(-15541, -110149.0), 94608.00, "")

    def test0107(self):
        self.assertEquals(self.calculate(-31786, -143810.0), 112024.00, "")

    def test0108(self):
        self.assertEquals(self.calculate(28487, 5332.0), 23155.00, "")

    def test0109(self):
        self.assertEquals(self.calculate(-7870, 185313.0), -193183.00, "")

    def test0110(self):
        self.assertEquals(self.calculate(-1963, -173783.0), 171820.00, "")

    def test0111(self):
        self.assertEquals(self.calculate(-14000, -161585.0), 147585.00, "")

    def test0112(self):
        self.assertEquals(self.calculate(14554, -182750.0), 197304.00, "")

    def test0113(self):
        self.assertEquals(self.calculate(1418, 140452.0), -139034.00, "")

    def test0114(self):
        self.assertEquals(self.calculate(13657, -55343.0), 69000.00, "")

    def test0115(self):
        self.assertEquals(self.calculate(9600, -147973.0), 157573.00, "")

    def test0116(self):
        self.assertEquals(self.calculate(-29473, 3247.0), -32720.00, "")

    def test0117(self):
        self.assertEquals(self.calculate(21565, 145154.0), -123589.00, "")

    def test0118(self):
        self.assertEquals(self.calculate(-2738, 142696.0), -145434.00, "")

    def test0119(self):
        self.assertEquals(self.calculate(17455, -90326.0), 107781.00, "")

    def test0120(self):
        self.assertEquals(self.calculate(430, -169498.0), 169928.00, "")

    def test0121(self):
        self.assertEquals(self.calculate(-10736, -133218.0), 122482.00, "")

    def test0122(self):
        self.assertEquals(self.calculate(32572, -89086.0), 121658.00, "")

    def test0123(self):
        self.assertEquals(self.calculate(8681, -127308.0), 135989.00, "")

    def test0124(self):
        self.assertEquals(self.calculate(-29392, 22433.0), -51825.00, "")

    def test0125(self):
        self.assertEquals(self.calculate(26811, -175872.0), 202683.00, "")

    def test0126(self):
        self.assertEquals(self.calculate(-29506, -103322.0), 73816.00, "")

    def test0127(self):
        self.assertEquals(self.calculate(-13816, 83365.0), -97181.00, "")

    def test0128(self):
        self.assertEquals(self.calculate(13064, -45868.0), 58932.00, "")

    def test0129(self):
        self.assertEquals(self.calculate(14991, 191499.0), -176508.00, "")

    def test0130(self):
        self.assertEquals(self.calculate(-11601, -79332.0), 67731.00, "")

    def test0131(self):
        self.assertEquals(self.calculate(-15645, 193502.0), -209147.00, "")

    def test0132(self):
        self.assertEquals(self.calculate(-19607, -7959.0), -11648.00, "")

    def test0133(self):
        self.assertEquals(self.calculate(-14152, -168182.0), 154030.00, "")

    def test0134(self):
        self.assertEquals(self.calculate(-4712, -6566.0), 1854.00, "")

    def test0135(self):
        self.assertEquals(self.calculate(1167, 116995.0), -115828.00, "")

    def test0136(self):
        self.assertEquals(self.calculate(-18012, -144684.0), 126672.00, "")

    def test0137(self):
        self.assertEquals(self.calculate(-30329, -119284.0), 88955.00, "")

    def test0138(self):
        self.assertEquals(self.calculate(-27561, -70010.0), 42449.00, "")

    def test0139(self):
        self.assertEquals(self.calculate(24531, 137025.0), -112494.00, "")

    def test0140(self):
        self.assertEquals(self.calculate(3021, 192166.0), -189145.00, "")

    def test0141(self):
        self.assertEquals(self.calculate(1533, -88288.0), 89821.00, "")

    def test0142(self):
        self.assertEquals(self.calculate(19027, 132493.0), -113466.00, "")

    def test0143(self):
        self.assertEquals(self.calculate(-209, -137722.0), 137513.00, "")

    def test0144(self):
        self.assertEquals(self.calculate(4147, -21395.0), 25542.00, "")

    def test0145(self):
        self.assertEquals(self.calculate(-17347, 90037.0), -107384.00, "")

    def test0146(self):
        self.assertEquals(self.calculate(-9261, 77160.0), -86421.00, "")

    def test0147(self):
        self.assertEquals(self.calculate(25244, 121342.0), -96098.00, "")

    def test0148(self):
        self.assertEquals(self.calculate(-19308, -142735.0), 123427.00, "")

    def test0149(self):
        self.assertEquals(self.calculate(32540, 186651.0), -154111.00, "")

    def test0150(self):
        self.assertEquals(self.calculate(802, 6101.0), -5299.00, "")

    def test0151(self):
        self.assertEquals(self.calculate(-5097, 86586.0), -91683.00, "")

    def test0152(self):
        self.assertEquals(self.calculate(-9774, -83906.0), 74132.00, "")

    def test0153(self):
        self.assertEquals(self.calculate(-30013, -192889.0), 162876.00, "")

    def test0154(self):
        self.assertEquals(self.calculate(-5609, -179285.0), 173676.00, "")

    def test0155(self):
        self.assertEquals(self.calculate(-26840, 94160.0), -121000.00, "")

    def test0156(self):
        self.assertEquals(self.calculate(-10805, -126943.0), 116138.00, "")

    def test0157(self):
        self.assertEquals(self.calculate(11748, 52230.0), -40482.00, "")

    def test0158(self):
        self.assertEquals(self.calculate(-29367, -35796.0), 6429.00, "")

    def test0159(self):
        self.assertEquals(self.calculate(-27591, -128005.0), 100414.00, "")

    def test0160(self):
        self.assertEquals(self.calculate(-12174, 17727.0), -29901.00, "")

    def test0161(self):
        self.assertEquals(self.calculate(10305, 154612.0), -144307.00, "")

    def test0162(self):
        self.assertEquals(self.calculate(-24146, -193902.0), 169756.00, "")

    def test0163(self):
        self.assertEquals(self.calculate(-27850, 67596.0), -95446.00, "")

    def test0164(self):
        self.assertEquals(self.calculate(4078, -173757.0), 177835.00, "")

    def test0165(self):
        self.assertEquals(self.calculate(-8324, -31923.0), 23599.00, "")

    def test0166(self):
        self.assertEquals(self.calculate(11943, 135029.0), -123086.00, "")

    def test0167(self):
        self.assertEquals(self.calculate(9247, 112306.0), -103059.00, "")

    def test0168(self):
        self.assertEquals(self.calculate(30448, 175505.0), -145057.00, "")

    def test0169(self):
        self.assertEquals(self.calculate(-25000, 14954.0), -39954.00, "")

    def test0170(self):
        self.assertEquals(self.calculate(-17210, -20233.0), 3023.00, "")

    def test0171(self):
        self.assertEquals(self.calculate(20968, -104615.0), 125583.00, "")

    def test0172(self):
        self.assertEquals(self.calculate(4227, 52747.0), -48520.00, "")

    def test0173(self):
        self.assertEquals(self.calculate(15050, -73226.0), 88276.00, "")

    def test0174(self):
        self.assertEquals(self.calculate(-22215, 120874.0), -143089.00, "")

    def test0175(self):
        self.assertEquals(self.calculate(-28514, -26646.0), -1868.00, "")

    def test0176(self):
        self.assertEquals(self.calculate(24134, 48983.0), -24849.00, "")

    def test0177(self):
        self.assertEquals(self.calculate(15092, -139433.0), 154525.00, "")

    def test0178(self):
        self.assertEquals(self.calculate(25960, -88475.0), 114435.00, "")

    def test0179(self):
        self.assertEquals(self.calculate(22031, -1630.0), 23661.00, "")

    def test0180(self):
        self.assertEquals(self.calculate(511, 78293.0), -77782.00, "")

    def test0181(self):
        self.assertEquals(self.calculate(-12170, -48054.0), 35884.00, "")

    def test0182(self):
        self.assertEquals(self.calculate(22009, 194423.0), -172414.00, "")

    def test0183(self):
        self.assertEquals(self.calculate(24421, 44869.0), -20448.00, "")

    def test0184(self):
        self.assertEquals(self.calculate(-13826, -120047.0), 106221.00, "")

    def test0185(self):
        self.assertEquals(self.calculate(-25987, 9780.0), -35767.00, "")

    def test0186(self):
        self.assertEquals(self.calculate(-6617, -120561.0), 113944.00, "")

    def test0187(self):
        self.assertEquals(self.calculate(-28186, -177025.0), 148839.00, "")

    def test0188(self):
        self.assertEquals(self.calculate(18764, -189841.0), 208605.00, "")

    def test0189(self):
        self.assertEquals(self.calculate(-22825, 122523.0), -145348.00, "")

    def test0190(self):
        self.assertEquals(self.calculate(-15273, 175815.0), -191088.00, "")

    def test0191(self):
        self.assertEquals(self.calculate(18714, 104329.0), -85615.00, "")

    def test0192(self):
        self.assertEquals(self.calculate(-20657, 100987.0), -121644.00, "")

    def test0193(self):
        self.assertEquals(self.calculate(4046, -120003.0), 124049.00, "")

    def test0194(self):
        self.assertEquals(self.calculate(-17803, -99195.0), 81392.00, "")

    def test0195(self):
        self.assertEquals(self.calculate(-17781, -67579.0), 49798.00, "")

    def test0196(self):
        self.assertEquals(self.calculate(4599, 122963.0), -118364.00, "")

    def test0197(self):
        self.assertEquals(self.calculate(11279, -41498.0), 52777.00, "")

    def test0198(self):
        self.assertEquals(self.calculate(-5496, -143554.0), 138058.00, "")

    def test0199(self):
        self.assertEquals(self.calculate(20583, -167318.0), 187901.00, "")

    def test0200(self):
        self.assertEquals(self.calculate(24205, 37732.0), -13527.00, "")

    def test0201(self):
        self.assertEquals(self.calculate(-3015, -65533.0), 62518.00, "")

    def test0202(self):
        self.assertEquals(self.calculate(-15096, -149319.0), 134223.00, "")

    def test0203(self):
        self.assertEquals(self.calculate(15385, 160379.0), -144994.00, "")

    def test0204(self):
        self.assertEquals(self.calculate(2242, -193830.0), 196072.00, "")

    def test0205(self):
        self.assertEquals(self.calculate(-32702, 79998.0), -112700.00, "")

    def test0206(self):
        self.assertEquals(self.calculate(-18332, -31113.0), 12781.00, "")

    def test0207(self):
        self.assertEquals(self.calculate(-25, 56050.0), -56075.00, "")

    def test0208(self):
        self.assertEquals(self.calculate(-19906, 137466.0), -157372.00, "")

    def test0209(self):
        self.assertEquals(self.calculate(21713, 199514.0), -177801.00, "")

    def test0210(self):
        self.assertEquals(self.calculate(-20958, -131011.0), 110053.00, "")

    def test0211(self):
        self.assertEquals(self.calculate(-8881, 52337.0), -61218.00, "")

    def test0212(self):
        self.assertEquals(self.calculate(15423, -14131.0), 29554.00, "")

    def test0213(self):
        self.assertEquals(self.calculate(23042, 24755.0), -1713.00, "")

    def test0214(self):
        self.assertEquals(self.calculate(31792, 187792.0), -156000.00, "")

    def test0215(self):
        self.assertEquals(self.calculate(19688, 47921.0), -28233.00, "")

    def test0216(self):
        self.assertEquals(self.calculate(27722, -5126.0), 32848.00, "")

    def test0217(self):
        self.assertEquals(self.calculate(9326, 62343.0), -53017.00, "")

    def test0218(self):
        self.assertEquals(self.calculate(20941, 125451.0), -104510.00, "")

    def test0219(self):
        self.assertEquals(self.calculate(-9797, -13348.0), 3551.00, "")

    def test0220(self):
        self.assertEquals(self.calculate(21800, 136517.0), -114717.00, "")

    def test0221(self):
        self.assertEquals(self.calculate(31847, 92993.0), -61146.00, "")

    def test0222(self):
        self.assertEquals(self.calculate(-9582, -15887.0), 6305.00, "")

    def test0223(self):
        self.assertEquals(self.calculate(7503, 127231.0), -119728.00, "")

    def test0224(self):
        self.assertEquals(self.calculate(32025, 183580.0), -151555.00, "")

    def test0225(self):
        self.assertEquals(self.calculate(23599, 26752.0), -3153.00, "")

    def test0226(self):
        self.assertEquals(self.calculate(-30240, 194702.0), -224942.00, "")

    def test0227(self):
        self.assertEquals(self.calculate(-14618, -136387.0), 121769.00, "")

    def test0228(self):
        self.assertEquals(self.calculate(745, -134460.0), 135205.00, "")

    def test0229(self):
        self.assertEquals(self.calculate(-11880, -129114.0), 117234.00, "")

    def test0230(self):
        self.assertEquals(self.calculate(16441, 36569.0), -20128.00, "")

    def test0231(self):
        self.assertEquals(self.calculate(11790, 87612.0), -75822.00, "")

    def test0232(self):
        self.assertEquals(self.calculate(-27303, 88815.0), -116118.00, "")

    def test0233(self):
        self.assertEquals(self.calculate(-2815, -177124.0), 174309.00, "")

    def test0234(self):
        self.assertEquals(self.calculate(32749, 129310.0), -96561.00, "")

    def test0235(self):
        self.assertEquals(self.calculate(3460, 93450.0), -89990.00, "")

    def test0236(self):
        self.assertEquals(self.calculate(-21929, -173965.0), 152036.00, "")

    def test0237(self):
        self.assertEquals(self.calculate(-15188, -44871.0), 29683.00, "")

    def test0238(self):
        self.assertEquals(self.calculate(31738, -117750.0), 149488.00, "")

    def test0239(self):
        self.assertEquals(self.calculate(-6763, 88658.0), -95421.00, "")

    def test0240(self):
        self.assertEquals(self.calculate(-1882, -179316.0), 177434.00, "")

    def test0241(self):
        self.assertEquals(self.calculate(-5959, -170794.0), 164835.00, "")

    def test0242(self):
        self.assertEquals(self.calculate(11920, 110081.0), -98161.00, "")

    def test0243(self):
        self.assertEquals(self.calculate(-11578, -78165.0), 66587.00, "")

    def test0244(self):
        self.assertEquals(self.calculate(20476, 130237.0), -109761.00, "")

    def test0245(self):
        self.assertEquals(self.calculate(15607, 66326.0), -50719.00, "")

    def test0246(self):
        self.assertEquals(self.calculate(-9340, -44109.0), 34769.00, "")

    def test0247(self):
        self.assertEquals(self.calculate(25315, -45432.0), 70747.00, "")

    def test0248(self):
        self.assertEquals(self.calculate(-10294, -189607.0), 179313.00, "")

    def test0249(self):
        self.assertEquals(self.calculate(-1239, -129023.0), 127784.00, "")

    def test0250(self):
        self.assertEquals(self.calculate(-22297, 154166.0), -176463.00, "")

    def test0251(self):
        self.assertEquals(self.calculate(-1588, 65288.0), -66876.00, "")

    def test0252(self):
        self.assertEquals(self.calculate(-31272, 106909.0), -138181.00, "")

    def test0253(self):
        self.assertEquals(self.calculate(-16268, 55216.0), -71484.00, "")

    def test0254(self):
        self.assertEquals(self.calculate(-19820, 110306.0), -130126.00, "")

    def test0255(self):
        self.assertEquals(self.calculate(-15284, 169976.0), -185260.00, "")

    def test0256(self):
        self.assertEquals(self.calculate(9537, -193624.0), 203161.00, "")

    def test0257(self):
        self.assertEquals(self.calculate(18371, -153272.0), 171643.00, "")

    def test0258(self):
        self.assertEquals(self.calculate(15427, 61781.0), -46354.00, "")

    def test0259(self):
        self.assertEquals(self.calculate(22226, -87376.0), 109602.00, "")

    def test0260(self):
        self.assertEquals(self.calculate(-14746, -122932.0), 108186.00, "")

    def test0261(self):
        self.assertEquals(self.calculate(4363, -178243.0), 182606.00, "")

    def test0262(self):
        self.assertEquals(self.calculate(-17059, 129204.0), -146263.00, "")

    def test0263(self):
        self.assertEquals(self.calculate(-13020, 191853.0), -204873.00, "")

    def test0264(self):
        self.assertEquals(self.calculate(-24046, 10241.0), -34287.00, "")

    def test0265(self):
        self.assertEquals(self.calculate(-19637, 19929.0), -39566.00, "")

    def test0266(self):
        self.assertEquals(self.calculate(8974, 4757.0), 4217.00, "")

    def test0267(self):
        self.assertEquals(self.calculate(-10298, 7530.0), -17828.00, "")

    def test0268(self):
        self.assertEquals(self.calculate(-11683, -94972.0), 83289.00, "")

    def test0269(self):
        self.assertEquals(self.calculate(-20574, 162804.0), -183378.00, "")

    def test0270(self):
        self.assertEquals(self.calculate(-17850, 80670.0), -98520.00, "")

    def test0271(self):
        self.assertEquals(self.calculate(25022, -116813.0), 141835.00, "")

    def test0272(self):
        self.assertEquals(self.calculate(23542, -27562.0), 51104.00, "")

    def test0273(self):
        self.assertEquals(self.calculate(-30538, 167835.0), -198373.00, "")

    def test0274(self):
        self.assertEquals(self.calculate(-3527, -120843.0), 117316.00, "")

    def test0275(self):
        self.assertEquals(self.calculate(3575, -95509.0), 99084.00, "")

    def test0276(self):
        self.assertEquals(self.calculate(14324, -40296.0), 54620.00, "")

    def test0277(self):
        self.assertEquals(self.calculate(30078, 186296.0), -156218.00, "")

    def test0278(self):
        self.assertEquals(self.calculate(15927, -26721.0), 42648.00, "")

    def test0279(self):
        self.assertEquals(self.calculate(12982, 10788.0), 2194.00, "")

    def test0280(self):
        self.assertEquals(self.calculate(-7419, 143127.0), -150546.00, "")

    def test0281(self):
        self.assertEquals(self.calculate(17508, 82683.0), -65175.00, "")

    def test0282(self):
        self.assertEquals(self.calculate(7342, 110805.0), -103463.00, "")

    def test0283(self):
        self.assertEquals(self.calculate(14997, 149445.0), -134448.00, "")

    def test0284(self):
        self.assertEquals(self.calculate(30083, 33183.0), -3100.00, "")

    def test0285(self):
        self.assertEquals(self.calculate(12377, -145640.0), 158017.00, "")

    def test0286(self):
        self.assertEquals(self.calculate(14195, -47873.0), 62068.00, "")

    def test0287(self):
        self.assertEquals(self.calculate(13372, -50486.0), 63858.00, "")

    def test0288(self):
        self.assertEquals(self.calculate(-11118, -78710.0), 67592.00, "")

    def test0289(self):
        self.assertEquals(self.calculate(31354, 25668.0), 5686.00, "")

    def test0290(self):
        self.assertEquals(self.calculate(20353, -2942.0), 23295.00, "")

    def test0291(self):
        self.assertEquals(self.calculate(-17231, 77132.0), -94363.00, "")

    def test0292(self):
        self.assertEquals(self.calculate(14056, -34573.0), 48629.00, "")

    def test0293(self):
        self.assertEquals(self.calculate(22424, -180732.0), 203156.00, "")

    def test0294(self):
        self.assertEquals(self.calculate(-6910, -5604.0), -1306.00, "")

    def test0295(self):
        self.assertEquals(self.calculate(25665, 90665.0), -65000.00, "")

    def test0296(self):
        self.assertEquals(self.calculate(-15522, -60884.0), 45362.00, "")

    def test0297(self):
        self.assertEquals(self.calculate(-5800, -83631.0), 77831.00, "")

    def test0298(self):
        self.assertEquals(self.calculate(11061, -139687.0), 150748.00, "")

    def test0299(self):
        self.assertEquals(self.calculate(5130, 194134.0), -189004.00, "")

    def test0300(self):
        self.assertEquals(self.calculate(22851, -13970.0), 36821.00, "")

    def test0301(self):
        self.assertEquals(self.calculate(2734, 90786.0), -88052.00, "")

    def test0302(self):
        self.assertEquals(self.calculate(6599, 184115.0), -177516.00, "")

    def test0303(self):
        self.assertEquals(self.calculate(-7325, 199538.0), -206863.00, "")

    def test0304(self):
        self.assertEquals(self.calculate(-24891, -149249.0), 124358.00, "")

    def test0305(self):
        self.assertEquals(self.calculate(-15746, 133806.0), -149552.00, "")

    def test0306(self):
        self.assertEquals(self.calculate(-30850, 42861.0), -73711.00, "")

    def test0307(self):
        self.assertEquals(self.calculate(-6867, 178204.0), -185071.00, "")

    def test0308(self):
        self.assertEquals(self.calculate(-29446, -111497.0), 82051.00, "")

    def test0309(self):
        self.assertEquals(self.calculate(29281, -167528.0), 196809.00, "")

    def test0310(self):
        self.assertEquals(self.calculate(-5392, 98014.0), -103406.00, "")

    def test0311(self):
        self.assertEquals(self.calculate(-7038, -192698.0), 185660.00, "")

    def test0312(self):
        self.assertEquals(self.calculate(-5789, 67526.0), -73315.00, "")

    def test0313(self):
        self.assertEquals(self.calculate(-15359, -198174.0), 182815.00, "")

    def test0314(self):
        self.assertEquals(self.calculate(5992, 49110.0), -43118.00, "")

    def test0315(self):
        self.assertEquals(self.calculate(-31505, 93194.0), -124699.00, "")

    def test0316(self):
        self.assertEquals(self.calculate(1037, 43900.0), -42863.00, "")

    def test0317(self):
        self.assertEquals(self.calculate(30437, 85756.0), -55319.00, "")

    def test0318(self):
        self.assertEquals(self.calculate(-19835, 144079.0), -163914.00, "")

    def test0319(self):
        self.assertEquals(self.calculate(-18267, -393.0), -17874.00, "")

    def test0320(self):
        self.assertEquals(self.calculate(29250, -103809.0), 133059.00, "")

    def test0321(self):
        self.assertEquals(self.calculate(-2404, 155850.0), -158254.00, "")

    def test0322(self):
        self.assertEquals(self.calculate(3033, -148135.0), 151168.00, "")

    def test0323(self):
        self.assertEquals(self.calculate(22801, 133715.0), -110914.00, "")

    def test0324(self):
        self.assertEquals(self.calculate(31779, 53904.0), -22125.00, "")

    def test0325(self):
        self.assertEquals(self.calculate(-19987, -46964.0), 26977.00, "")

    def test0326(self):
        self.assertEquals(self.calculate(-21034, 168391.0), -189425.00, "")

    def test0327(self):
        self.assertEquals(self.calculate(-15238, -196164.0), 180926.00, "")

    def test0328(self):
        self.assertEquals(self.calculate(-22777, 20167.0), -42944.00, "")

    def test0329(self):
        self.assertEquals(self.calculate(-17126, 44552.0), -61678.00, "")

    def test0330(self):
        self.assertEquals(self.calculate(-18988, -15380.0), -3608.00, "")

    def test0331(self):
        self.assertEquals(self.calculate(31422, 57833.0), -26411.00, "")

    def test0332(self):
        self.assertEquals(self.calculate(17778, 187468.0), -169690.00, "")

    def test0333(self):
        self.assertEquals(self.calculate(-31979, 155457.0), -187436.00, "")

    def test0334(self):
        self.assertEquals(self.calculate(3088, -123313.0), 126401.00, "")

    def test0335(self):
        self.assertEquals(self.calculate(18626, 121695.0), -103069.00, "")

    def test0336(self):
        self.assertEquals(self.calculate(-318, 87840.0), -88158.00, "")

    def test0337(self):
        self.assertEquals(self.calculate(10626, -84576.0), 95202.00, "")

    def test0338(self):
        self.assertEquals(self.calculate(6107, -64002.0), 70109.00, "")

    def test0339(self):
        self.assertEquals(self.calculate(24064, -58182.0), 82246.00, "")

    def test0340(self):
        self.assertEquals(self.calculate(9162, -81158.0), 90320.00, "")

    def test0341(self):
        self.assertEquals(self.calculate(2628, 166995.0), -164367.00, "")

    def test0342(self):
        self.assertEquals(self.calculate(25179, -143305.0), 168484.00, "")

    def test0343(self):
        self.assertEquals(self.calculate(-6773, 55107.0), -61880.00, "")

    def test0344(self):
        self.assertEquals(self.calculate(-10394, -40899.0), 30505.00, "")

    def test0345(self):
        self.assertEquals(self.calculate(11742, 57127.0), -45385.00, "")

    def test0346(self):
        self.assertEquals(self.calculate(-7210, -152228.0), 145018.00, "")

    def test0347(self):
        self.assertEquals(self.calculate(11195, -156956.0), 168151.00, "")

    def test0348(self):
        self.assertEquals(self.calculate(-18995, 23576.0), -42571.00, "")

    def test0349(self):
        self.assertEquals(self.calculate(-11365, 193015.0), -204380.00, "")

    def test0350(self):
        self.assertEquals(self.calculate(-15761, 186727.0), -202488.00, "")

    def test0351(self):
        self.assertEquals(self.calculate(12755, -73362.0), 86117.00, "")

    def test0352(self):
        self.assertEquals(self.calculate(2445, -24931.0), 27376.00, "")

    def test0353(self):
        self.assertEquals(self.calculate(21424, 67895.0), -46471.00, "")

    def test0354(self):
        self.assertEquals(self.calculate(25907, 195079.0), -169172.00, "")

    def test0355(self):
        self.assertEquals(self.calculate(-27183, 179596.0), -206779.00, "")

    def test0356(self):
        self.assertEquals(self.calculate(-31946, -24454.0), -7492.00, "")

    def test0357(self):
        self.assertEquals(self.calculate(7354, 41714.0), -34360.00, "")

    def test0358(self):
        self.assertEquals(self.calculate(17006, -26138.0), 43144.00, "")

    def test0359(self):
        self.assertEquals(self.calculate(-6315, 109423.0), -115738.00, "")

    def test0360(self):
        self.assertEquals(self.calculate(-17301, 26965.0), -44266.00, "")

    def test0361(self):
        self.assertEquals(self.calculate(29335, -193928.0), 223263.00, "")

    def test0362(self):
        self.assertEquals(self.calculate(-12590, -146969.0), 134379.00, "")

    def test0363(self):
        self.assertEquals(self.calculate(25430, -132897.0), 158327.00, "")

    def test0364(self):
        self.assertEquals(self.calculate(30700, 189645.0), -158945.00, "")

    def test0365(self):
        self.assertEquals(self.calculate(31837, -135222.0), 167059.00, "")

    def test0366(self):
        self.assertEquals(self.calculate(-29960, -6307.0), -23653.00, "")

    def test0367(self):
        self.assertEquals(self.calculate(27020, -152010.0), 179030.00, "")

    def test0368(self):
        self.assertEquals(self.calculate(11182, -29091.0), 40273.00, "")

    def test0369(self):
        self.assertEquals(self.calculate(-22025, 30878.0), -52903.00, "")

    def test0370(self):
        self.assertEquals(self.calculate(-13706, 172328.0), -186034.00, "")

    def test0371(self):
        self.assertEquals(self.calculate(6846, 120645.0), -113799.00, "")

    def test0372(self):
        self.assertEquals(self.calculate(8848, 32346.0), -23498.00, "")

    def test0373(self):
        self.assertEquals(self.calculate(18467, 53837.0), -35370.00, "")

    def test0374(self):
        self.assertEquals(self.calculate(16843, -107773.0), 124616.00, "")

    def test0375(self):
        self.assertEquals(self.calculate(17204, 124517.0), -107313.00, "")

    def test0376(self):
        self.assertEquals(self.calculate(-23369, 121107.0), -144476.00, "")

    def test0377(self):
        self.assertEquals(self.calculate(-20579, 86282.0), -106861.00, "")

    def test0378(self):
        self.assertEquals(self.calculate(21576, -101158.0), 122734.00, "")

    def test0379(self):
        self.assertEquals(self.calculate(-9402, 148460.0), -157862.00, "")

    def test0380(self):
        self.assertEquals(self.calculate(-16504, -31487.0), 14983.00, "")

    def test0381(self):
        self.assertEquals(self.calculate(30987, 159646.0), -128659.00, "")

    def test0382(self):
        self.assertEquals(self.calculate(-12046, 197772.0), -209818.00, "")

    def test0383(self):
        self.assertEquals(self.calculate(9850, -71627.0), 81477.00, "")

    def test0384(self):
        self.assertEquals(self.calculate(-8432, 67264.0), -75696.00, "")

    def test0385(self):
        self.assertEquals(self.calculate(-30348, -121559.0), 91211.00, "")

    def test0386(self):
        self.assertEquals(self.calculate(6317, 194406.0), -188089.00, "")

    def test0387(self):
        self.assertEquals(self.calculate(-24541, -40177.0), 15636.00, "")

    def test0388(self):
        self.assertEquals(self.calculate(10730, -97148.0), 107878.00, "")

    def test0389(self):
        self.assertEquals(self.calculate(26412, 124095.0), -97683.00, "")

    def test0390(self):
        self.assertEquals(self.calculate(10656, 193760.0), -183104.00, "")

    def test0391(self):
        self.assertEquals(self.calculate(-11592, 144803.0), -156395.00, "")

    def test0392(self):
        self.assertEquals(self.calculate(4321, 32487.0), -28166.00, "")

    def test0393(self):
        self.assertEquals(self.calculate(-12710, 161839.0), -174549.00, "")

    def test0394(self):
        self.assertEquals(self.calculate(28390, 187595.0), -159205.00, "")

    def test0395(self):
        self.assertEquals(self.calculate(-8291, 194057.0), -202348.00, "")

    def test0396(self):
        self.assertEquals(self.calculate(-28770, 20688.0), -49458.00, "")

    def test0397(self):
        self.assertEquals(self.calculate(29979, 126331.0), -96352.00, "")

    def test0398(self):
        self.assertEquals(self.calculate(-12849, -134783.0), 121934.00, "")

    def test0399(self):
        self.assertEquals(self.calculate(4913, -147498.0), 152411.00, "")

    def test0400(self):
        self.assertEquals(self.calculate(28904, 121122.0), -92218.00, "")

    def test0401(self):
        self.assertEquals(self.calculate(6492, 34487.0), -27995.00, "")

    def test0402(self):
        self.assertEquals(self.calculate(-23196, 88491.0), -111687.00, "")

    def test0403(self):
        self.assertEquals(self.calculate(3306, 159945.0), -156639.00, "")

    def test0404(self):
        self.assertEquals(self.calculate(-8361, 116690.0), -125051.00, "")

    def test0405(self):
        self.assertEquals(self.calculate(-4111, 16344.0), -20455.00, "")

    def test0406(self):
        self.assertEquals(self.calculate(-8255, 84390.0), -92645.00, "")

    def test0407(self):
        self.assertEquals(self.calculate(-29917, -44790.0), 14873.00, "")

    def test0408(self):
        self.assertEquals(self.calculate(-1106, -17100.0), 15994.00, "")

    def test0409(self):
        self.assertEquals(self.calculate(844, -108619.0), 109463.00, "")

    def test0410(self):
        self.assertEquals(self.calculate(-31598, -77193.0), 45595.00, "")

    def test0411(self):
        self.assertEquals(self.calculate(17832, 25075.0), -7243.00, "")

    def test0412(self):
        self.assertEquals(self.calculate(30922, 63592.0), -32670.00, "")

    def test0413(self):
        self.assertEquals(self.calculate(6301, 47582.0), -41281.00, "")

    def test0414(self):
        self.assertEquals(self.calculate(7509, -173282.0), 180791.00, "")

    def test0415(self):
        self.assertEquals(self.calculate(22600, -91194.0), 113794.00, "")

    def test0416(self):
        self.assertEquals(self.calculate(-9247, 108771.0), -118018.00, "")

    def test0417(self):
        self.assertEquals(self.calculate(27878, -16300.0), 44178.00, "")

    def test0418(self):
        self.assertEquals(self.calculate(3024, 11651.0), -8627.00, "")

    def test0419(self):
        self.assertEquals(self.calculate(31839, -120642.0), 152481.00, "")

    def test0420(self):
        self.assertEquals(self.calculate(-16959, -695.0), -16264.00, "")

    def test0421(self):
        self.assertEquals(self.calculate(-19907, -169009.0), 149102.00, "")

    def test0422(self):
        self.assertEquals(self.calculate(-3758, -47250.0), 43492.00, "")

    def test0423(self):
        self.assertEquals(self.calculate(-32084, 8956.0), -41040.00, "")

    def test0424(self):
        self.assertEquals(self.calculate(-20091, 14184.0), -34275.00, "")

    def test0425(self):
        self.assertEquals(self.calculate(6028, 130133.0), -124105.00, "")

    def test0426(self):
        self.assertEquals(self.calculate(-513, -102285.0), 101772.00, "")

    def test0427(self):
        self.assertEquals(self.calculate(-11821, 61922.0), -73743.00, "")

    def test0428(self):
        self.assertEquals(self.calculate(-25663, 166985.0), -192648.00, "")

    def test0429(self):
        self.assertEquals(self.calculate(-7177, 187476.0), -194653.00, "")

    def test0430(self):
        self.assertEquals(self.calculate(-31040, -152409.0), 121369.00, "")

    def test0431(self):
        self.assertEquals(self.calculate(12782, -60392.0), 73174.00, "")

    def test0432(self):
        self.assertEquals(self.calculate(20932, -169557.0), 190489.00, "")

    def test0433(self):
        self.assertEquals(self.calculate(722, 23879.0), -23157.00, "")

    def test0434(self):
        self.assertEquals(self.calculate(-11910, 74352.0), -86262.00, "")

    def test0435(self):
        self.assertEquals(self.calculate(19064, 126254.0), -107190.00, "")

    def test0436(self):
        self.assertEquals(self.calculate(-12232, 166261.0), -178493.00, "")

    def test0437(self):
        self.assertEquals(self.calculate(-21275, -165455.0), 144180.00, "")

    def test0438(self):
        self.assertEquals(self.calculate(-15190, -150797.0), 135607.00, "")

    def test0439(self):
        self.assertEquals(self.calculate(-13420, 27460.0), -40880.00, "")

    def test0440(self):
        self.assertEquals(self.calculate(22645, 103396.0), -80751.00, "")

    def test0441(self):
        self.assertEquals(self.calculate(-28778, -158211.0), 129433.00, "")

    def test0442(self):
        self.assertEquals(self.calculate(-22888, 2025.0), -24913.00, "")

    def test0443(self):
        self.assertEquals(self.calculate(-1420, -87688.0), 86268.00, "")

    def test0444(self):
        self.assertEquals(self.calculate(17048, -91130.0), 108178.00, "")

    def test0445(self):
        self.assertEquals(self.calculate(17642, -46816.0), 64458.00, "")

    def test0446(self):
        self.assertEquals(self.calculate(26050, 102331.0), -76281.00, "")

    def test0447(self):
        self.assertEquals(self.calculate(-2627, -144757.0), 142130.00, "")

    def test0448(self):
        self.assertEquals(self.calculate(-31512, 8701.0), -40213.00, "")

    def test0449(self):
        self.assertEquals(self.calculate(15930, -13507.0), 29437.00, "")

    def test0450(self):
        self.assertEquals(self.calculate(23927, 960.0), 22967.00, "")

    def test0451(self):
        self.assertEquals(self.calculate(-4877, -142272.0), 137395.00, "")

    def test0452(self):
        self.assertEquals(self.calculate(1534, 76489.0), -74955.00, "")

    def test0453(self):
        self.assertEquals(self.calculate(2438, 101583.0), -99145.00, "")

    def test0454(self):
        self.assertEquals(self.calculate(27048, 72780.0), -45732.00, "")

    def test0455(self):
        self.assertEquals(self.calculate(2832, 150369.0), -147537.00, "")

    def test0456(self):
        self.assertEquals(self.calculate(-20639, -151530.0), 130891.00, "")

    def test0457(self):
        self.assertEquals(self.calculate(29554, -191944.0), 221498.00, "")

    def test0458(self):
        self.assertEquals(self.calculate(12364, 168378.0), -156014.00, "")

    def test0459(self):
        self.assertEquals(self.calculate(-7315, 83042.0), -90357.00, "")

    def test0460(self):
        self.assertEquals(self.calculate(-9467, 175109.0), -184576.00, "")

    def test0461(self):
        self.assertEquals(self.calculate(19889, -51427.0), 71316.00, "")

    def test0462(self):
        self.assertEquals(self.calculate(1252, -95222.0), 96474.00, "")

    def test0463(self):
        self.assertEquals(self.calculate(-15093, 42002.0), -57095.00, "")

    def test0464(self):
        self.assertEquals(self.calculate(21473, -85528.0), 107001.00, "")

    def test0465(self):
        self.assertEquals(self.calculate(21823, -39218.0), 61041.00, "")

    def test0466(self):
        self.assertEquals(self.calculate(-31409, 12944.0), -44353.00, "")

    def test0467(self):
        self.assertEquals(self.calculate(-32359, 5647.0), -38006.00, "")

    def test0468(self):
        self.assertEquals(self.calculate(-27075, -107883.0), 80808.00, "")

    def test0469(self):
        self.assertEquals(self.calculate(3733, -34115.0), 37848.00, "")

    def test0470(self):
        self.assertEquals(self.calculate(25028, -25419.0), 50447.00, "")

    def test0471(self):
        self.assertEquals(self.calculate(25823, 164753.0), -138930.00, "")

    def test0472(self):
        self.assertEquals(self.calculate(-26640, -67098.0), 40458.00, "")

    def test0473(self):
        self.assertEquals(self.calculate(-6377, 145832.0), -152209.00, "")

    def test0474(self):
        self.assertEquals(self.calculate(-22623, 166869.0), -189492.00, "")

    def test0475(self):
        self.assertEquals(self.calculate(-27823, 111943.0), -139766.00, "")

    def test0476(self):
        self.assertEquals(self.calculate(27780, -32731.0), 60511.00, "")

    def test0477(self):
        self.assertEquals(self.calculate(13911, -194613.0), 208524.00, "")

    def test0478(self):
        self.assertEquals(self.calculate(-10217, 186074.0), -196291.00, "")

    def test0479(self):
        self.assertEquals(self.calculate(18575, 110663.0), -92088.00, "")

    def test0480(self):
        self.assertEquals(self.calculate(-25786, -42025.0), 16239.00, "")

    def test0481(self):
        self.assertEquals(self.calculate(-21450, 160215.0), -181665.00, "")

    def test0482(self):
        self.assertEquals(self.calculate(16377, 98394.0), -82017.00, "")

    def test0483(self):
        self.assertEquals(self.calculate(-23654, 108599.0), -132253.00, "")

    def test0484(self):
        self.assertEquals(self.calculate(31030, -101900.0), 132930.00, "")

    def test0485(self):
        self.assertEquals(self.calculate(-5294, 171832.0), -177126.00, "")

    def test0486(self):
        self.assertEquals(self.calculate(-26073, 138706.0), -164779.00, "")

    def test0487(self):
        self.assertEquals(self.calculate(31119, 122624.0), -91505.00, "")

    def test0488(self):
        self.assertEquals(self.calculate(14888, -185251.0), 200139.00, "")

    def test0489(self):
        self.assertEquals(self.calculate(6976, 68679.0), -61703.00, "")

    def test0490(self):
        self.assertEquals(self.calculate(2761, 87675.0), -84914.00, "")

    def test0491(self):
        self.assertEquals(self.calculate(-22806, 88195.0), -111001.00, "")

    def test0492(self):
        self.assertEquals(self.calculate(27193, -173877.0), 201070.00, "")

    def test0493(self):
        self.assertEquals(self.calculate(15605, -119220.0), 134825.00, "")

    def test0494(self):
        self.assertEquals(self.calculate(9020, -142791.0), 151811.00, "")

    def test0495(self):
        self.assertEquals(self.calculate(-22477, -68590.0), 46113.00, "")

    def test0496(self):
        self.assertEquals(self.calculate(-31617, 70994.0), -102611.00, "")

    def test0497(self):
        self.assertEquals(self.calculate(-30567, -160679.0), 130112.00, "")

    def test0498(self):
        self.assertEquals(self.calculate(2458, -149128.0), 151586.00, "")

    def test0499(self):
        self.assertEquals(self.calculate(-6882, 176899.0), -183781.00, "")

    def test0500(self):
        self.assertEquals(self.calculate(-20328, 14485.0), -34813.00, "")

    def test0501(self):
        self.assertEquals(self.calculate(-15164, -47331.0), 32167.00, "")

    def test0502(self):
        self.assertEquals(self.calculate(20350, -57257.0), 77607.00, "")

    def test0503(self):
        self.assertEquals(self.calculate(19498, -57837.0), 77335.00, "")

    def test0504(self):
        self.assertEquals(self.calculate(18296, -199064.0), 217360.00, "")

    def test0505(self):
        self.assertEquals(self.calculate(-10681, 150708.0), -161389.00, "")

    def test0506(self):
        self.assertEquals(self.calculate(-6363, -191680.0), 185317.00, "")

    def test0507(self):
        self.assertEquals(self.calculate(-8284, -106772.0), 98488.00, "")

    def test0508(self):
        self.assertEquals(self.calculate(6465, 29987.0), -23522.00, "")

    def test0509(self):
        self.assertEquals(self.calculate(14141, -103106.0), 117247.00, "")

    def test0510(self):
        self.assertEquals(self.calculate(-30161, -31021.0), 860.00, "")

    def test0511(self):
        self.assertEquals(self.calculate(19940, 105281.0), -85341.00, "")

    def test0512(self):
        self.assertEquals(self.calculate(14750, -185209.0), 199959.00, "")

    def test0513(self):
        self.assertEquals(self.calculate(-28724, -138791.0), 110067.00, "")

    def test0514(self):
        self.assertEquals(self.calculate(-28145, -18062.0), -10083.00, "")

    def test0515(self):
        self.assertEquals(self.calculate(23416, -131837.0), 155253.00, "")

    def test0516(self):
        self.assertEquals(self.calculate(-4730, 112473.0), -117203.00, "")

    def test0517(self):
        self.assertEquals(self.calculate(24029, 191249.0), -167220.00, "")

    def test0518(self):
        self.assertEquals(self.calculate(-14898, -58904.0), 44006.00, "")

    def test0519(self):
        self.assertEquals(self.calculate(-25081, 853.0), -25934.00, "")

    def test0520(self):
        self.assertEquals(self.calculate(-869, 2319.0), -3188.00, "")

    def test0521(self):
        self.assertEquals(self.calculate(-19763, 137145.0), -156908.00, "")

    def test0522(self):
        self.assertEquals(self.calculate(-6135, -79785.0), 73650.00, "")

    def test0523(self):
        self.assertEquals(self.calculate(-12692, -191574.0), 178882.00, "")

    def test0524(self):
        self.assertEquals(self.calculate(-9247, -87390.0), 78143.00, "")

    def test0525(self):
        self.assertEquals(self.calculate(-27519, 20626.0), -48145.00, "")

    def test0526(self):
        self.assertEquals(self.calculate(-11760, 63770.0), -75530.00, "")

    def test0527(self):
        self.assertEquals(self.calculate(15379, 46302.0), -30923.00, "")

    def test0528(self):
        self.assertEquals(self.calculate(14120, -88618.0), 102738.00, "")

    def test0529(self):
        self.assertEquals(self.calculate(-5153, -63299.0), 58146.00, "")

    def test0530(self):
        self.assertEquals(self.calculate(22450, -164697.0), 187147.00, "")

    def test0531(self):
        self.assertEquals(self.calculate(19919, -136387.0), 156306.00, "")

    def test0532(self):
        self.assertEquals(self.calculate(-886, 96867.0), -97753.00, "")

    def test0533(self):
        self.assertEquals(self.calculate(26953, 20705.0), 6248.00, "")

    def test0534(self):
        self.assertEquals(self.calculate(27773, 148647.0), -120874.00, "")

    def test0535(self):
        self.assertEquals(self.calculate(-31758, -147837.0), 116079.00, "")

    def test0536(self):
        self.assertEquals(self.calculate(8924, 193864.0), -184940.00, "")

    def test0537(self):
        self.assertEquals(self.calculate(18133, -175811.0), 193944.00, "")

    def test0538(self):
        self.assertEquals(self.calculate(26724, -57885.0), 84609.00, "")

    def test0539(self):
        self.assertEquals(self.calculate(-5982, 138805.0), -144787.00, "")

    def test0540(self):
        self.assertEquals(self.calculate(-28713, -143206.0), 114493.00, "")

    def test0541(self):
        self.assertEquals(self.calculate(-24481, 120370.0), -144851.00, "")

    def test0542(self):
        self.assertEquals(self.calculate(19538, -120045.0), 139583.00, "")

    def test0543(self):
        self.assertEquals(self.calculate(21800, 18470.0), 3330.00, "")

    def test0544(self):
        self.assertEquals(self.calculate(-7465, -198840.0), 191375.00, "")

    def test0545(self):
        self.assertEquals(self.calculate(24124, 1733.0), 22391.00, "")

    def test0546(self):
        self.assertEquals(self.calculate(-28555, -124433.0), 95878.00, "")

    def test0547(self):
        self.assertEquals(self.calculate(25442, -192704.0), 218146.00, "")

    def test0548(self):
        self.assertEquals(self.calculate(8771, 109663.0), -100892.00, "")

    def test0549(self):
        self.assertEquals(self.calculate(-7660, 11524.0), -19184.00, "")

    def test0550(self):
        self.assertEquals(self.calculate(9093, 167701.0), -158608.00, "")

    def test0551(self):
        self.assertEquals(self.calculate(31120, -181774.0), 212894.00, "")

    def test0552(self):
        self.assertEquals(self.calculate(-20647, 173716.0), -194363.00, "")

    def test0553(self):
        self.assertEquals(self.calculate(-17371, 81349.0), -98720.00, "")

    def test0554(self):
        self.assertEquals(self.calculate(-3233, 175808.0), -179041.00, "")

    def test0555(self):
        self.assertEquals(self.calculate(30568, -146170.0), 176738.00, "")

    def test0556(self):
        self.assertEquals(self.calculate(-13353, 163344.0), -176697.00, "")

    def test0557(self):
        self.assertEquals(self.calculate(30012, -371.0), 30383.00, "")

    def test0558(self):
        self.assertEquals(self.calculate(28007, -54612.0), 82619.00, "")

    def test0559(self):
        self.assertEquals(self.calculate(-4637, 24558.0), -29195.00, "")

    def test0560(self):
        self.assertEquals(self.calculate(-23725, 141147.0), -164872.00, "")

    def test0561(self):
        self.assertEquals(self.calculate(31408, -166071.0), 197479.00, "")

    def test0562(self):
        self.assertEquals(self.calculate(-10804, -152874.0), 142070.00, "")

    def test0563(self):
        self.assertEquals(self.calculate(386, 39428.0), -39042.00, "")

    def test0564(self):
        self.assertEquals(self.calculate(-5248, -11777.0), 6529.00, "")

    def test0565(self):
        self.assertEquals(self.calculate(-16252, 18086.0), -34338.00, "")

    def test0566(self):
        self.assertEquals(self.calculate(-7277, 13143.0), -20420.00, "")

    def test0567(self):
        self.assertEquals(self.calculate(-30040, 147582.0), -177622.00, "")

    def test0568(self):
        self.assertEquals(self.calculate(-11284, 82712.0), -93996.00, "")

    def test0569(self):
        self.assertEquals(self.calculate(-1664, 34018.0), -35682.00, "")

    def test0570(self):
        self.assertEquals(self.calculate(23797, -152286.0), 176083.00, "")

    def test0571(self):
        self.assertEquals(self.calculate(-21571, 84829.0), -106400.00, "")

    def test0572(self):
        self.assertEquals(self.calculate(-22027, -72213.0), 50186.00, "")

    def test0573(self):
        self.assertEquals(self.calculate(31671, -168488.0), 200159.00, "")

    def test0574(self):
        self.assertEquals(self.calculate(13723, 27199.0), -13476.00, "")

    def test0575(self):
        self.assertEquals(self.calculate(5753, 74497.0), -68744.00, "")

    def test0576(self):
        self.assertEquals(self.calculate(-14315, -155812.0), 141497.00, "")

    def test0577(self):
        self.assertEquals(self.calculate(-17235, 183534.0), -200769.00, "")

    def test0578(self):
        self.assertEquals(self.calculate(-2824, -133489.0), 130665.00, "")

    def test0579(self):
        self.assertEquals(self.calculate(-3643, -72197.0), 68554.00, "")

    def test0580(self):
        self.assertEquals(self.calculate(28142, -139992.0), 168134.00, "")

    def test0581(self):
        self.assertEquals(self.calculate(7160, 59013.0), -51853.00, "")

    def test0582(self):
        self.assertEquals(self.calculate(30613, -152718.0), 183331.00, "")

    def test0583(self):
        self.assertEquals(self.calculate(21095, 177590.0), -156495.00, "")

    def test0584(self):
        self.assertEquals(self.calculate(5234, -42588.0), 47822.00, "")

    def test0585(self):
        self.assertEquals(self.calculate(28556, -196629.0), 225185.00, "")

    def test0586(self):
        self.assertEquals(self.calculate(13812, -18982.0), 32794.00, "")

    def test0587(self):
        self.assertEquals(self.calculate(-19385, 169173.0), -188558.00, "")

    def test0588(self):
        self.assertEquals(self.calculate(27573, 157479.0), -129906.00, "")

    def test0589(self):
        self.assertEquals(self.calculate(-5015, -31906.0), 26891.00, "")

    def test0590(self):
        self.assertEquals(self.calculate(-16618, 104492.0), -121110.00, "")

    def test0591(self):
        self.assertEquals(self.calculate(23490, 36716.0), -13226.00, "")

    def test0592(self):
        self.assertEquals(self.calculate(1213, -14190.0), 15403.00, "")

    def test0593(self):
        self.assertEquals(self.calculate(-8747, -140472.0), 131725.00, "")

    def test0594(self):
        self.assertEquals(self.calculate(1465, -145129.0), 146594.00, "")

    def test0595(self):
        self.assertEquals(self.calculate(27535, -174901.0), 202436.00, "")

    def test0596(self):
        self.assertEquals(self.calculate(-24416, 129769.0), -154185.00, "")

    def test0597(self):
        self.assertEquals(self.calculate(-22334, -109105.0), 86771.00, "")

    def test0598(self):
        self.assertEquals(self.calculate(12175, 186630.0), -174455.00, "")

    def test0599(self):
        self.assertEquals(self.calculate(1090, 46760.0), -45670.00, "")

    def test0600(self):
        self.assertEquals(self.calculate(-7976, 186049.0), -194025.00, "")

    def test0601(self):
        self.assertEquals(self.calculate(-26215, 77654.0), -103869.00, "")

    def test0602(self):
        self.assertEquals(self.calculate(-11174, -138391.0), 127217.00, "")

    def test0603(self):
        self.assertEquals(self.calculate(-1596, 134377.0), -135973.00, "")

    def test0604(self):
        self.assertEquals(self.calculate(-8282, -51031.0), 42749.00, "")

    def test0605(self):
        self.assertEquals(self.calculate(16248, 51094.0), -34846.00, "")

    def test0606(self):
        self.assertEquals(self.calculate(4901, 11272.0), -6371.00, "")

    def test0607(self):
        self.assertEquals(self.calculate(27190, -120721.0), 147911.00, "")

    def test0608(self):
        self.assertEquals(self.calculate(-5234, -102299.0), 97065.00, "")

    def test0609(self):
        self.assertEquals(self.calculate(-785, 149361.0), -150146.00, "")

    def test0610(self):
        self.assertEquals(self.calculate(2707, -33671.0), 36378.00, "")

    def test0611(self):
        self.assertEquals(self.calculate(-12810, -131095.0), 118285.00, "")

    def test0612(self):
        self.assertEquals(self.calculate(-23079, 148463.0), -171542.00, "")

    def test0613(self):
        self.assertEquals(self.calculate(-12085, 31748.0), -43833.00, "")

    def test0614(self):
        self.assertEquals(self.calculate(-21444, 193827.0), -215271.00, "")

    def test0615(self):
        self.assertEquals(self.calculate(15773, 78148.0), -62375.00, "")

    def test0616(self):
        self.assertEquals(self.calculate(6882, -179824.0), 186706.00, "")

    def test0617(self):
        self.assertEquals(self.calculate(-9250, 172127.0), -181377.00, "")

    def test0618(self):
        self.assertEquals(self.calculate(-24920, 194224.0), -219144.00, "")

    def test0619(self):
        self.assertEquals(self.calculate(-813, 148187.0), -149000.00, "")

    def test0620(self):
        self.assertEquals(self.calculate(-27289, 85644.0), -112933.00, "")

    def test0621(self):
        self.assertEquals(self.calculate(-32550, -134613.0), 102063.00, "")

    def test0622(self):
        self.assertEquals(self.calculate(-12420, 77221.0), -89641.00, "")

    def test0623(self):
        self.assertEquals(self.calculate(25209, -157695.0), 182904.00, "")

    def test0624(self):
        self.assertEquals(self.calculate(-5165, -125937.0), 120772.00, "")

    def test0625(self):
        self.assertEquals(self.calculate(28878, 183600.0), -154722.00, "")

    def test0626(self):
        self.assertEquals(self.calculate(20833, -157414.0), 178247.00, "")

    def test0627(self):
        self.assertEquals(self.calculate(-3302, -100608.0), 97306.00, "")

    def test0628(self):
        self.assertEquals(self.calculate(23015, 150893.0), -127878.00, "")

    def test0629(self):
        self.assertEquals(self.calculate(13147, 77402.0), -64255.00, "")

    def test0630(self):
        self.assertEquals(self.calculate(-29373, 41650.0), -71023.00, "")

    def test0631(self):
        self.assertEquals(self.calculate(-5188, -189736.0), 184548.00, "")

    def test0632(self):
        self.assertEquals(self.calculate(5647, -156285.0), 161932.00, "")

    def test0633(self):
        self.assertEquals(self.calculate(-13333, 45021.0), -58354.00, "")

    def test0634(self):
        self.assertEquals(self.calculate(1162, -195462.0), 196624.00, "")

    def test0635(self):
        self.assertEquals(self.calculate(-30115, 3374.0), -33489.00, "")

    def test0636(self):
        self.assertEquals(self.calculate(2054, 133061.0), -131007.00, "")

    def test0637(self):
        self.assertEquals(self.calculate(-10531, 187191.0), -197722.00, "")

    def test0638(self):
        self.assertEquals(self.calculate(24719, 188631.0), -163912.00, "")

    def test0639(self):
        self.assertEquals(self.calculate(-8396, 57117.0), -65513.00, "")

    def test0640(self):
        self.assertEquals(self.calculate(27577, 45603.0), -18026.00, "")

    def test0641(self):
        self.assertEquals(self.calculate(-4249, 80997.0), -85246.00, "")

    def test0642(self):
        self.assertEquals(self.calculate(6139, -163778.0), 169917.00, "")

    def test0643(self):
        self.assertEquals(self.calculate(19060, 135664.0), -116604.00, "")

    def test0644(self):
        self.assertEquals(self.calculate(13414, 128794.0), -115380.00, "")

    def test0645(self):
        self.assertEquals(self.calculate(32326, 189112.0), -156786.00, "")

    def test0646(self):
        self.assertEquals(self.calculate(14947, 68950.0), -54003.00, "")

    def test0647(self):
        self.assertEquals(self.calculate(-12543, -157730.0), 145187.00, "")

    def test0648(self):
        self.assertEquals(self.calculate(-19228, -181851.0), 162623.00, "")

    def test0649(self):
        self.assertEquals(self.calculate(30630, 6399.0), 24231.00, "")

    def test0650(self):
        self.assertEquals(self.calculate(14965, 46311.0), -31346.00, "")

    def test0651(self):
        self.assertEquals(self.calculate(-21515, 157065.0), -178580.00, "")

    def test0652(self):
        self.assertEquals(self.calculate(3123, 122876.0), -119753.00, "")

    def test0653(self):
        self.assertEquals(self.calculate(-27497, 82412.0), -109909.00, "")

    def test0654(self):
        self.assertEquals(self.calculate(19644, -73755.0), 93399.00, "")

    def test0655(self):
        self.assertEquals(self.calculate(-31865, 124760.0), -156625.00, "")

    def test0656(self):
        self.assertEquals(self.calculate(-11298, 198247.0), -209545.00, "")

    def test0657(self):
        self.assertEquals(self.calculate(-31651, -17894.0), -13757.00, "")

    def test0658(self):
        self.assertEquals(self.calculate(-31242, 43450.0), -74692.00, "")

    def test0659(self):
        self.assertEquals(self.calculate(1756, 109014.0), -107258.00, "")

    def test0660(self):
        self.assertEquals(self.calculate(17655, -159665.0), 177320.00, "")

    def test0661(self):
        self.assertEquals(self.calculate(30290, -160024.0), 190314.00, "")

    def test0662(self):
        self.assertEquals(self.calculate(-23504, 27002.0), -50506.00, "")

    def test0663(self):
        self.assertEquals(self.calculate(-14746, 65229.0), -79975.00, "")

    def test0664(self):
        self.assertEquals(self.calculate(22075, 29771.0), -7696.00, "")

    def test0665(self):
        self.assertEquals(self.calculate(-22480, 165835.0), -188315.00, "")

    def test0666(self):
        self.assertEquals(self.calculate(-591, -33712.0), 33121.00, "")

    def test0667(self):
        self.assertEquals(self.calculate(6738, 132659.0), -125921.00, "")

    def test0668(self):
        self.assertEquals(self.calculate(-20430, -28596.0), 8166.00, "")

    def test0669(self):
        self.assertEquals(self.calculate(-10251, 153384.0), -163635.00, "")

    def test0670(self):
        self.assertEquals(self.calculate(18125, -149217.0), 167342.00, "")

    def test0671(self):
        self.assertEquals(self.calculate(-10282, 193501.0), -203783.00, "")

    def test0672(self):
        self.assertEquals(self.calculate(-209, -165802.0), 165593.00, "")

    def test0673(self):
        self.assertEquals(self.calculate(20901, -104992.0), 125893.00, "")

    def test0674(self):
        self.assertEquals(self.calculate(-14339, 6832.0), -21171.00, "")

    def test0675(self):
        self.assertEquals(self.calculate(27924, 28068.0), -144.00, "")

    def test0676(self):
        self.assertEquals(self.calculate(8058, -80838.0), 88896.00, "")

    def test0677(self):
        self.assertEquals(self.calculate(-12499, -105976.0), 93477.00, "")

    def test0678(self):
        self.assertEquals(self.calculate(29689, -31440.0), 61129.00, "")

    def test0679(self):
        self.assertEquals(self.calculate(9798, 74990.0), -65192.00, "")

    def test0680(self):
        self.assertEquals(self.calculate(-19894, -129701.0), 109807.00, "")

    def test0681(self):
        self.assertEquals(self.calculate(13025, 116926.0), -103901.00, "")

    def test0682(self):
        self.assertEquals(self.calculate(-31298, -159712.0), 128414.00, "")

    def test0683(self):
        self.assertEquals(self.calculate(-6392, 40463.0), -46855.00, "")

    def test0684(self):
        self.assertEquals(self.calculate(22955, 135016.0), -112061.00, "")

    def test0685(self):
        self.assertEquals(self.calculate(-32525, 40182.0), -72707.00, "")

    def test0686(self):
        self.assertEquals(self.calculate(-15816, -53980.0), 38164.00, "")

    def test0687(self):
        self.assertEquals(self.calculate(-24939, 193355.0), -218294.00, "")

    def test0688(self):
        self.assertEquals(self.calculate(-15314, -145661.0), 130347.00, "")

    def test0689(self):
        self.assertEquals(self.calculate(-6360, 77745.0), -84105.00, "")

    def test0690(self):
        self.assertEquals(self.calculate(-6385, -142274.0), 135889.00, "")

    def test0691(self):
        self.assertEquals(self.calculate(2182, 124922.0), -122740.00, "")

    def test0692(self):
        self.assertEquals(self.calculate(-32196, -194174.0), 161978.00, "")

    def test0693(self):
        self.assertEquals(self.calculate(-28080, 156176.0), -184256.00, "")

    def test0694(self):
        self.assertEquals(self.calculate(-31399, -12299.0), -19100.00, "")

    def test0695(self):
        self.assertEquals(self.calculate(11066, -117443.0), 128509.00, "")

    def test0696(self):
        self.assertEquals(self.calculate(32240, 126658.0), -94418.00, "")

    def test0697(self):
        self.assertEquals(self.calculate(-17566, 11844.0), -29410.00, "")

    def test0698(self):
        self.assertEquals(self.calculate(-3905, 146627.0), -150532.00, "")

    def test0699(self):
        self.assertEquals(self.calculate(29851, -7488.0), 37339.00, "")

    def test0700(self):
        self.assertEquals(self.calculate(-15939, 138936.0), -154875.00, "")

    def test0701(self):
        self.assertEquals(self.calculate(-28331, -116998.0), 88667.00, "")

    def test0702(self):
        self.assertEquals(self.calculate(-9175, 152107.0), -161282.00, "")

    def test0703(self):
        self.assertEquals(self.calculate(-15488, 194915.0), -210403.00, "")

    def test0704(self):
        self.assertEquals(self.calculate(-31645, -194396.0), 162751.00, "")

    def test0705(self):
        self.assertEquals(self.calculate(-23160, -1978.0), -21182.00, "")

    def test0706(self):
        self.assertEquals(self.calculate(-22951, -192345.0), 169394.00, "")

    def test0707(self):
        self.assertEquals(self.calculate(14111, -49811.0), 63922.00, "")

    def test0708(self):
        self.assertEquals(self.calculate(29012, -42435.0), 71447.00, "")

    def test0709(self):
        self.assertEquals(self.calculate(-447, -67501.0), 67054.00, "")

    def test0710(self):
        self.assertEquals(self.calculate(-18201, -166114.0), 147913.00, "")

    def test0711(self):
        self.assertEquals(self.calculate(-4260, -48244.0), 43984.00, "")

    def test0712(self):
        self.assertEquals(self.calculate(-22894, -170656.0), 147762.00, "")

    def test0713(self):
        self.assertEquals(self.calculate(29524, 78765.0), -49241.00, "")

    def test0714(self):
        self.assertEquals(self.calculate(32564, -126229.0), 158793.00, "")

    def test0715(self):
        self.assertEquals(self.calculate(16274, 110721.0), -94447.00, "")

    def test0716(self):
        self.assertEquals(self.calculate(-25985, 3412.0), -29397.00, "")

    def test0717(self):
        self.assertEquals(self.calculate(-16552, 132554.0), -149106.00, "")

    def test0718(self):
        self.assertEquals(self.calculate(21625, 189444.0), -167819.00, "")

    def test0719(self):
        self.assertEquals(self.calculate(23159, 127713.0), -104554.00, "")

    def test0720(self):
        self.assertEquals(self.calculate(-8977, -141789.0), 132812.00, "")

    def test0721(self):
        self.assertEquals(self.calculate(-7541, -39259.0), 31718.00, "")

    def test0722(self):
        self.assertEquals(self.calculate(-18470, -145358.0), 126888.00, "")

    def test0723(self):
        self.assertEquals(self.calculate(19036, -49656.0), 68692.00, "")

    def test0724(self):
        self.assertEquals(self.calculate(1012, -16013.0), 17025.00, "")

    def test0725(self):
        self.assertEquals(self.calculate(-24620, 193761.0), -218381.00, "")

    def test0726(self):
        self.assertEquals(self.calculate(17020, 120476.0), -103456.00, "")

    def test0727(self):
        self.assertEquals(self.calculate(11272, 167155.0), -155883.00, "")

    def test0728(self):
        self.assertEquals(self.calculate(21167, 53866.0), -32699.00, "")

    def test0729(self):
        self.assertEquals(self.calculate(17270, 11062.0), 6208.00, "")

    def test0730(self):
        self.assertEquals(self.calculate(3297, -117087.0), 120384.00, "")

    def test0731(self):
        self.assertEquals(self.calculate(18832, -9794.0), 28626.00, "")

    def test0732(self):
        self.assertEquals(self.calculate(27473, 17030.0), 10443.00, "")

    def test0733(self):
        self.assertEquals(self.calculate(-6486, -59949.0), 53463.00, "")

    def test0734(self):
        self.assertEquals(self.calculate(-2955, 39930.0), -42885.00, "")

    def test0735(self):
        self.assertEquals(self.calculate(-13991, -102296.0), 88305.00, "")

    def test0736(self):
        self.assertEquals(self.calculate(-25445, 92393.0), -117838.00, "")

    def test0737(self):
        self.assertEquals(self.calculate(-6325, 156571.0), -162896.00, "")

    def test0738(self):
        self.assertEquals(self.calculate(16713, 23548.0), -6835.00, "")

    def test0739(self):
        self.assertEquals(self.calculate(-9015, -93316.0), 84301.00, "")

    def test0740(self):
        self.assertEquals(self.calculate(26686, 125407.0), -98721.00, "")

    def test0741(self):
        self.assertEquals(self.calculate(891, -34522.0), 35413.00, "")

    def test0742(self):
        self.assertEquals(self.calculate(23749, 88204.0), -64455.00, "")

    def test0743(self):
        self.assertEquals(self.calculate(-20148, -175728.0), 155580.00, "")

    def test0744(self):
        self.assertEquals(self.calculate(-31433, -41792.0), 10359.00, "")

    def test0745(self):
        self.assertEquals(self.calculate(5080, -52164.0), 57244.00, "")

    def test0746(self):
        self.assertEquals(self.calculate(2790, -144409.0), 147199.00, "")

    def test0747(self):
        self.assertEquals(self.calculate(-22547, 24957.0), -47504.00, "")

    def test0748(self):
        self.assertEquals(self.calculate(-10138, 90239.0), -100377.00, "")

    def test0749(self):
        self.assertEquals(self.calculate(3838, 51741.0), -47903.00, "")

    def test0750(self):
        self.assertEquals(self.calculate(-27859, -176556.0), 148697.00, "")

    def test0751(self):
        self.assertEquals(self.calculate(6422, -50114.0), 56536.00, "")

    def test0752(self):
        self.assertEquals(self.calculate(-18688, -192531.0), 173843.00, "")

    def test0753(self):
        self.assertEquals(self.calculate(-14585, -55621.0), 41036.00, "")

    def test0754(self):
        self.assertEquals(self.calculate(-5497, -88086.0), 82589.00, "")

    def test0755(self):
        self.assertEquals(self.calculate(-24916, -126934.0), 102018.00, "")

    def test0756(self):
        self.assertEquals(self.calculate(-28113, -118303.0), 90190.00, "")

    def test0757(self):
        self.assertEquals(self.calculate(16088, 32028.0), -15940.00, "")

    def test0758(self):
        self.assertEquals(self.calculate(15959, -132288.0), 148247.00, "")

    def test0759(self):
        self.assertEquals(self.calculate(11485, -113305.0), 124790.00, "")

    def test0760(self):
        self.assertEquals(self.calculate(29778, 11726.0), 18052.00, "")

    def test0761(self):
        self.assertEquals(self.calculate(14150, -84572.0), 98722.00, "")

    def test0762(self):
        self.assertEquals(self.calculate(-16378, 60109.0), -76487.00, "")

    def test0763(self):
        self.assertEquals(self.calculate(8062, 95261.0), -87199.00, "")

    def test0764(self):
        self.assertEquals(self.calculate(15062, -151373.0), 166435.00, "")

    def test0765(self):
        self.assertEquals(self.calculate(-7294, 78236.0), -85530.00, "")

    def test0766(self):
        self.assertEquals(self.calculate(-17892, -106806.0), 88914.00, "")

    def test0767(self):
        self.assertEquals(self.calculate(-3541, 5567.0), -9108.00, "")

    def test0768(self):
        self.assertEquals(self.calculate(2162, -59544.0), 61706.00, "")

    def test0769(self):
        self.assertEquals(self.calculate(12185, 65580.0), -53395.00, "")

    def test0770(self):
        self.assertEquals(self.calculate(7355, -85550.0), 92905.00, "")

    def test0771(self):
        self.assertEquals(self.calculate(15563, 186634.0), -171071.00, "")

    def test0772(self):
        self.assertEquals(self.calculate(32692, -130046.0), 162738.00, "")

    def test0773(self):
        self.assertEquals(self.calculate(10582, -39095.0), 49677.00, "")

    def test0774(self):
        self.assertEquals(self.calculate(4049, -171525.0), 175574.00, "")

    def test0775(self):
        self.assertEquals(self.calculate(17281, -60659.0), 77940.00, "")

    def test0776(self):
        self.assertEquals(self.calculate(8150, 190573.0), -182423.00, "")

    def test0777(self):
        self.assertEquals(self.calculate(-8282, 87547.0), -95829.00, "")

    def test0778(self):
        self.assertEquals(self.calculate(17735, 31701.0), -13966.00, "")

    def test0779(self):
        self.assertEquals(self.calculate(19910, 108474.0), -88564.00, "")

    def test0780(self):
        self.assertEquals(self.calculate(358, -56062.0), 56420.00, "")

    def test0781(self):
        self.assertEquals(self.calculate(-7778, -87650.0), 79872.00, "")

    def test0782(self):
        self.assertEquals(self.calculate(17680, -188993.0), 206673.00, "")

    def test0783(self):
        self.assertEquals(self.calculate(5620, 7433.0), -1813.00, "")

    def test0784(self):
        self.assertEquals(self.calculate(25262, -140620.0), 165882.00, "")

    def test0785(self):
        self.assertEquals(self.calculate(-23764, -162010.0), 138246.00, "")

    def test0786(self):
        self.assertEquals(self.calculate(-28787, -139204.0), 110417.00, "")

    def test0787(self):
        self.assertEquals(self.calculate(-5375, 39449.0), -44824.00, "")

    def test0788(self):
        self.assertEquals(self.calculate(26372, 61127.0), -34755.00, "")

    def test0789(self):
        self.assertEquals(self.calculate(-28450, 65229.0), -93679.00, "")

    def test0790(self):
        self.assertEquals(self.calculate(3027, 101864.0), -98837.00, "")

    def test0791(self):
        self.assertEquals(self.calculate(10658, -82615.0), 93273.00, "")

    def test0792(self):
        self.assertEquals(self.calculate(430, 41094.0), -40664.00, "")

    def test0793(self):
        self.assertEquals(self.calculate(-26863, 118397.0), -145260.00, "")

    def test0794(self):
        self.assertEquals(self.calculate(14406, -156427.0), 170833.00, "")

    def test0795(self):
        self.assertEquals(self.calculate(17579, -82325.0), 99904.00, "")

    def test0796(self):
        self.assertEquals(self.calculate(-3355, -166894.0), 163539.00, "")

    def test0797(self):
        self.assertEquals(self.calculate(10582, -46763.0), 57345.00, "")

    def test0798(self):
        self.assertEquals(self.calculate(31100, -195041.0), 226141.00, "")

    def test0799(self):
        self.assertEquals(self.calculate(19705, 151605.0), -131900.00, "")

    def test0800(self):
        self.assertEquals(self.calculate(17099, -119314.0), 136413.00, "")

    def test0801(self):
        self.assertEquals(self.calculate(10632, -630.0), 11262.00, "")

    def test0802(self):
        self.assertEquals(self.calculate(-15884, 31551.0), -47435.00, "")

    def test0803(self):
        self.assertEquals(self.calculate(-2957, -134487.0), 131530.00, "")

    def test0804(self):
        self.assertEquals(self.calculate(-28555, 56338.0), -84893.00, "")

    def test0805(self):
        self.assertEquals(self.calculate(-30140, -85158.0), 55018.00, "")

    def test0806(self):
        self.assertEquals(self.calculate(-27827, 167360.0), -195187.00, "")

    def test0807(self):
        self.assertEquals(self.calculate(1073, -17594.0), 18667.00, "")

    def test0808(self):
        self.assertEquals(self.calculate(-25775, 173582.0), -199357.00, "")

    def test0809(self):
        self.assertEquals(self.calculate(16703, 16513.0), 190.00, "")

    def test0810(self):
        self.assertEquals(self.calculate(29086, 6450.0), 22636.00, "")

    def test0811(self):
        self.assertEquals(self.calculate(-29158, -59713.0), 30555.00, "")

    def test0812(self):
        self.assertEquals(self.calculate(4261, -129022.0), 133283.00, "")

    def test0813(self):
        self.assertEquals(self.calculate(-16765, -127274.0), 110509.00, "")

    def test0814(self):
        self.assertEquals(self.calculate(22321, -22664.0), 44985.00, "")

    def test0815(self):
        self.assertEquals(self.calculate(-13750, -88901.0), 75151.00, "")

    def test0816(self):
        self.assertEquals(self.calculate(29589, -76249.0), 105838.00, "")

    def test0817(self):
        self.assertEquals(self.calculate(25598, -108557.0), 134155.00, "")

    def test0818(self):
        self.assertEquals(self.calculate(-9402, -129907.0), 120505.00, "")

    def test0819(self):
        self.assertEquals(self.calculate(5597, -139272.0), 144869.00, "")

    def test0820(self):
        self.assertEquals(self.calculate(-3122, 47301.0), -50423.00, "")

    def test0821(self):
        self.assertEquals(self.calculate(29194, -59172.0), 88366.00, "")

    def test0822(self):
        self.assertEquals(self.calculate(12749, -187932.0), 200681.00, "")

    def test0823(self):
        self.assertEquals(self.calculate(-2941, -29506.0), 26565.00, "")

    def test0824(self):
        self.assertEquals(self.calculate(13432, 118554.0), -105122.00, "")

    def test0825(self):
        self.assertEquals(self.calculate(-12781, -69008.0), 56227.00, "")

    def test0826(self):
        self.assertEquals(self.calculate(-25844, -145214.0), 119370.00, "")

    def test0827(self):
        self.assertEquals(self.calculate(14795, 183538.0), -168743.00, "")

    def test0828(self):
        self.assertEquals(self.calculate(-1676, 36025.0), -37701.00, "")

    def test0829(self):
        self.assertEquals(self.calculate(-19902, 9038.0), -28940.00, "")

    def test0830(self):
        self.assertEquals(self.calculate(8905, -189010.0), 197915.00, "")

    def test0831(self):
        self.assertEquals(self.calculate(-3149, 60821.0), -63970.00, "")

    def test0832(self):
        self.assertEquals(self.calculate(23774, -198660.0), 222434.00, "")

    def test0833(self):
        self.assertEquals(self.calculate(-16859, 93817.0), -110676.00, "")

    def test0834(self):
        self.assertEquals(self.calculate(-6653, -114798.0), 108145.00, "")

    def test0835(self):
        self.assertEquals(self.calculate(-22270, 98068.0), -120338.00, "")

    def test0836(self):
        self.assertEquals(self.calculate(-21937, 45421.0), -67358.00, "")

    def test0837(self):
        self.assertEquals(self.calculate(-4348, 111889.0), -116237.00, "")

    def test0838(self):
        self.assertEquals(self.calculate(975, 169380.0), -168405.00, "")

    def test0839(self):
        self.assertEquals(self.calculate(-24487, -184202.0), 159715.00, "")

    def test0840(self):
        self.assertEquals(self.calculate(31838, -91334.0), 123172.00, "")

    def test0841(self):
        self.assertEquals(self.calculate(21924, 19790.0), 2134.00, "")

    def test0842(self):
        self.assertEquals(self.calculate(-3203, -192073.0), 188870.00, "")

    def test0843(self):
        self.assertEquals(self.calculate(29705, 97229.0), -67524.00, "")

    def test0844(self):
        self.assertEquals(self.calculate(10383, 114503.0), -104120.00, "")

    def test0845(self):
        self.assertEquals(self.calculate(-6028, -155272.0), 149244.00, "")

    def test0846(self):
        self.assertEquals(self.calculate(13844, 128142.0), -114298.00, "")

    def test0847(self):
        self.assertEquals(self.calculate(5129, 53938.0), -48809.00, "")

    def test0848(self):
        self.assertEquals(self.calculate(-9411, -79332.0), 69921.00, "")

    def test0849(self):
        self.assertEquals(self.calculate(26195, -17655.0), 43850.00, "")

    def test0850(self):
        self.assertEquals(self.calculate(-26104, -63758.0), 37654.00, "")

    def test0851(self):
        self.assertEquals(self.calculate(-31087, 23351.0), -54438.00, "")

    def test0852(self):
        self.assertEquals(self.calculate(-14538, 117963.0), -132501.00, "")

    def test0853(self):
        self.assertEquals(self.calculate(22771, 127159.0), -104388.00, "")

    def test0854(self):
        self.assertEquals(self.calculate(-13824, -133921.0), 120097.00, "")

    def test0855(self):
        self.assertEquals(self.calculate(-18506, -33410.0), 14904.00, "")

    def test0856(self):
        self.assertEquals(self.calculate(-32542, 74334.0), -106876.00, "")

    def test0857(self):
        self.assertEquals(self.calculate(-19467, -167829.0), 148362.00, "")

    def test0858(self):
        self.assertEquals(self.calculate(-32270, 65213.0), -97483.00, "")

    def test0859(self):
        self.assertEquals(self.calculate(-6810, 76228.0), -83038.00, "")

    def test0860(self):
        self.assertEquals(self.calculate(16297, -70180.0), 86477.00, "")

    def test0861(self):
        self.assertEquals(self.calculate(-15962, 112633.0), -128595.00, "")

    def test0862(self):
        self.assertEquals(self.calculate(-21899, 198483.0), -220382.00, "")

    def test0863(self):
        self.assertEquals(self.calculate(30943, 73126.0), -42183.00, "")

    def test0864(self):
        self.assertEquals(self.calculate(-5959, 37503.0), -43462.00, "")

    def test0865(self):
        self.assertEquals(self.calculate(-16845, 33515.0), -50360.00, "")

    def test0866(self):
        self.assertEquals(self.calculate(5909, -41459.0), 47368.00, "")

    def test0867(self):
        self.assertEquals(self.calculate(-28178, 25500.0), -53678.00, "")

    def test0868(self):
        self.assertEquals(self.calculate(18036, -159665.0), 177701.00, "")

    def test0869(self):
        self.assertEquals(self.calculate(-24056, -182918.0), 158862.00, "")

    def test0870(self):
        self.assertEquals(self.calculate(-20493, -152836.0), 132343.00, "")

    def test0871(self):
        self.assertEquals(self.calculate(955, 19585.0), -18630.00, "")

    def test0872(self):
        self.assertEquals(self.calculate(-21232, 180401.0), -201633.00, "")

    def test0873(self):
        self.assertEquals(self.calculate(16597, -159718.0), 176315.00, "")

    def test0874(self):
        self.assertEquals(self.calculate(-20250, 45028.0), -65278.00, "")

    def test0875(self):
        self.assertEquals(self.calculate(14314, -55572.0), 69886.00, "")

    def test0876(self):
        self.assertEquals(self.calculate(30539, 24779.0), 5760.00, "")

    def test0877(self):
        self.assertEquals(self.calculate(7739, 158979.0), -151240.00, "")

    def test0878(self):
        self.assertEquals(self.calculate(-3549, -147457.0), 143908.00, "")

    def test0879(self):
        self.assertEquals(self.calculate(19909, 9466.0), 10443.00, "")

    def test0880(self):
        self.assertEquals(self.calculate(23421, 155074.0), -131653.00, "")

    def test0881(self):
        self.assertEquals(self.calculate(18500, 9637.0), 8863.00, "")

    def test0882(self):
        self.assertEquals(self.calculate(4044, 52339.0), -48295.00, "")

    def test0883(self):
        self.assertEquals(self.calculate(10241, 60736.0), -50495.00, "")

    def test0884(self):
        self.assertEquals(self.calculate(-16149, 159013.0), -175162.00, "")

    def test0885(self):
        self.assertEquals(self.calculate(-8735, -189491.0), 180756.00, "")

    def test0886(self):
        self.assertEquals(self.calculate(20826, 143495.0), -122669.00, "")

    def test0887(self):
        self.assertEquals(self.calculate(-1827, -143729.0), 141902.00, "")

    def test0888(self):
        self.assertEquals(self.calculate(31662, -40508.0), 72170.00, "")

    def test0889(self):
        self.assertEquals(self.calculate(-2418, 60344.0), -62762.00, "")

    def test0890(self):
        self.assertEquals(self.calculate(-31654, -145632.0), 113978.00, "")

    def test0891(self):
        self.assertEquals(self.calculate(-11906, -72742.0), 60836.00, "")

    def test0892(self):
        self.assertEquals(self.calculate(-13373, 172533.0), -185906.00, "")

    def test0893(self):
        self.assertEquals(self.calculate(11720, -59307.0), 71027.00, "")

    def test0894(self):
        self.assertEquals(self.calculate(-25806, -112415.0), 86609.00, "")

    def test0895(self):
        self.assertEquals(self.calculate(-19878, -1495.0), -18383.00, "")

    def test0896(self):
        self.assertEquals(self.calculate(-9361, 63769.0), -73130.00, "")

    def test0897(self):
        self.assertEquals(self.calculate(2587, 111073.0), -108486.00, "")

    def test0898(self):
        self.assertEquals(self.calculate(-15717, -147519.0), 131802.00, "")

    def test0899(self):
        self.assertEquals(self.calculate(15077, -75489.0), 90566.00, "")

    def test0900(self):
        self.assertEquals(self.calculate(-7809, -160835.0), 153026.00, "")

    def test0901(self):
        self.assertEquals(self.calculate(6529, 30252.0), -23723.00, "")

    def test0902(self):
        self.assertEquals(self.calculate(29650, -63526.0), 93176.00, "")

    def test0903(self):
        self.assertEquals(self.calculate(-7126, -157880.0), 150754.00, "")

    def test0904(self):
        self.assertEquals(self.calculate(-11481, -74415.0), 62934.00, "")

    def test0905(self):
        self.assertEquals(self.calculate(-22337, 132125.0), -154462.00, "")

    def test0906(self):
        self.assertEquals(self.calculate(28496, 198986.0), -170490.00, "")

    def test0907(self):
        self.assertEquals(self.calculate(-26366, 150437.0), -176803.00, "")

    def test0908(self):
        self.assertEquals(self.calculate(-24927, 122494.0), -147421.00, "")

    def test0909(self):
        self.assertEquals(self.calculate(13595, 59907.0), -46312.00, "")

    def test0910(self):
        self.assertEquals(self.calculate(-11923, -167549.0), 155626.00, "")

    def test0911(self):
        self.assertEquals(self.calculate(-23554, 34167.0), -57721.00, "")

    def test0912(self):
        self.assertEquals(self.calculate(-5142, 75818.0), -80960.00, "")

    def test0913(self):
        self.assertEquals(self.calculate(-4150, -68745.0), 64595.00, "")

    def test0914(self):
        self.assertEquals(self.calculate(-19399, -115975.0), 96576.00, "")

    def test0915(self):
        self.assertEquals(self.calculate(15802, -197147.0), 212949.00, "")

    def test0916(self):
        self.assertEquals(self.calculate(-13812, 128951.0), -142763.00, "")

    def test0917(self):
        self.assertEquals(self.calculate(-25797, 7530.0), -33327.00, "")

    def test0918(self):
        self.assertEquals(self.calculate(-10177, 124582.0), -134759.00, "")

    def test0919(self):
        self.assertEquals(self.calculate(241, -125333.0), 125574.00, "")

    def test0920(self):
        self.assertEquals(self.calculate(-15118, -91759.0), 76641.00, "")

    def test0921(self):
        self.assertEquals(self.calculate(19399, -15142.0), 34541.00, "")

    def test0922(self):
        self.assertEquals(self.calculate(-16081, 153069.0), -169150.00, "")

    def test0923(self):
        self.assertEquals(self.calculate(-7972, -27226.0), 19254.00, "")

    def test0924(self):
        self.assertEquals(self.calculate(-28252, 161748.0), -190000.00, "")

    def test0925(self):
        self.assertEquals(self.calculate(-8039, 187941.0), -195980.00, "")

    def test0926(self):
        self.assertEquals(self.calculate(-2464, 44511.0), -46975.00, "")

    def test0927(self):
        self.assertEquals(self.calculate(-22900, -55663.0), 32763.00, "")

    def test0928(self):
        self.assertEquals(self.calculate(10952, -30615.0), 41567.00, "")

    def test0929(self):
        self.assertEquals(self.calculate(-1998, -169801.0), 167803.00, "")

    def test0930(self):
        self.assertEquals(self.calculate(5654, 92543.0), -86889.00, "")

    def test0931(self):
        self.assertEquals(self.calculate(-24631, 120004.0), -144635.00, "")

    def test0932(self):
        self.assertEquals(self.calculate(18982, -113312.0), 132294.00, "")

    def test0933(self):
        self.assertEquals(self.calculate(-26030, -6102.0), -19928.00, "")

    def test0934(self):
        self.assertEquals(self.calculate(-18996, 191248.0), -210244.00, "")

    def test0935(self):
        self.assertEquals(self.calculate(-658, -192010.0), 191352.00, "")

    def test0936(self):
        self.assertEquals(self.calculate(-7355, 35455.0), -42810.00, "")

    def test0937(self):
        self.assertEquals(self.calculate(-13339, 79277.0), -92616.00, "")

    def test0938(self):
        self.assertEquals(self.calculate(-8719, -169799.0), 161080.00, "")

    def test0939(self):
        self.assertEquals(self.calculate(7345, -93013.0), 100358.00, "")

    def test0940(self):
        self.assertEquals(self.calculate(-22478, -80100.0), 57622.00, "")

    def test0941(self):
        self.assertEquals(self.calculate(5215, -106668.0), 111883.00, "")

    def test0942(self):
        self.assertEquals(self.calculate(20405, -120917.0), 141322.00, "")

    def test0943(self):
        self.assertEquals(self.calculate(7032, -52593.0), 59625.00, "")

    def test0944(self):
        self.assertEquals(self.calculate(11089, 31203.0), -20114.00, "")

    def test0945(self):
        self.assertEquals(self.calculate(-10744, 156690.0), -167434.00, "")

    def test0946(self):
        self.assertEquals(self.calculate(-26555, 948.0), -27503.00, "")

    def test0947(self):
        self.assertEquals(self.calculate(-17022, -25073.0), 8051.00, "")

    def test0948(self):
        self.assertEquals(self.calculate(-29775, -44008.0), 14233.00, "")

    def test0949(self):
        self.assertEquals(self.calculate(-13038, -118730.0), 105692.00, "")

    def test0950(self):
        self.assertEquals(self.calculate(-28694, -120605.0), 91911.00, "")

    def test0951(self):
        self.assertEquals(self.calculate(20863, -84460.0), 105323.00, "")

    def test0952(self):
        self.assertEquals(self.calculate(-32521, 27420.0), -59941.00, "")

    def test0953(self):
        self.assertEquals(self.calculate(-17656, -101186.0), 83530.00, "")

    def test0954(self):
        self.assertEquals(self.calculate(-30598, 141404.0), -172002.00, "")

    def test0955(self):
        self.assertEquals(self.calculate(25214, -184247.0), 209461.00, "")

    def test0956(self):
        self.assertEquals(self.calculate(-22230, -135059.0), 112829.00, "")

    def test0957(self):
        self.assertEquals(self.calculate(8281, 71763.0), -63482.00, "")

    def test0958(self):
        self.assertEquals(self.calculate(-27577, -190931.0), 163354.00, "")

    def test0959(self):
        self.assertEquals(self.calculate(7014, -32668.0), 39682.00, "")

    def test0960(self):
        self.assertEquals(self.calculate(-9805, -136474.0), 126669.00, "")

    def test0961(self):
        self.assertEquals(self.calculate(-11123, 96933.0), -108056.00, "")

    def test0962(self):
        self.assertEquals(self.calculate(9668, -182485.0), 192153.00, "")

    def test0963(self):
        self.assertEquals(self.calculate(-14779, 44789.0), -59568.00, "")

    def test0964(self):
        self.assertEquals(self.calculate(-14445, -91464.0), 77019.00, "")

    def test0965(self):
        self.assertEquals(self.calculate(29201, -5604.0), 34805.00, "")

    def test0966(self):
        self.assertEquals(self.calculate(8770, 181087.0), -172317.00, "")

    def test0967(self):
        self.assertEquals(self.calculate(-28371, 59173.0), -87544.00, "")

    def test0968(self):
        self.assertEquals(self.calculate(-5391, -124103.0), 118712.00, "")

    def test0969(self):
        self.assertEquals(self.calculate(9551, 32032.0), -22481.00, "")

    def test0970(self):
        self.assertEquals(self.calculate(-20687, 21725.0), -42412.00, "")

    def test0971(self):
        self.assertEquals(self.calculate(-28139, 194235.0), -222374.00, "")

    def test0972(self):
        self.assertEquals(self.calculate(21155, -142266.0), 163421.00, "")

    def test0973(self):
        self.assertEquals(self.calculate(-16225, 181514.0), -197739.00, "")

    def test0974(self):
        self.assertEquals(self.calculate(10958, -54193.0), 65151.00, "")

    def test0975(self):
        self.assertEquals(self.calculate(25815, 80306.0), -54491.00, "")

    def test0976(self):
        self.assertEquals(self.calculate(-21306, 98550.0), -119856.00, "")

    def test0977(self):
        self.assertEquals(self.calculate(-20718, -187911.0), 167193.00, "")

    def test0978(self):
        self.assertEquals(self.calculate(28377, -142136.0), 170513.00, "")

    def test0979(self):
        self.assertEquals(self.calculate(-30790, -58996.0), 28206.00, "")

    def test0980(self):
        self.assertEquals(self.calculate(27891, 96817.0), -68926.00, "")

    def test0981(self):
        self.assertEquals(self.calculate(19896, 96375.0), -76479.00, "")

    def test0982(self):
        self.assertEquals(self.calculate(-19877, 161414.0), -181291.00, "")

    def test0983(self):
        self.assertEquals(self.calculate(12842, 25515.0), -12673.00, "")

    def test0984(self):
        self.assertEquals(self.calculate(-27341, -195926.0), 168585.00, "")

    def test0985(self):
        self.assertEquals(self.calculate(14512, 70031.0), -55519.00, "")

    def test0986(self):
        self.assertEquals(self.calculate(6219, -69261.0), 75480.00, "")

    def test0987(self):
        self.assertEquals(self.calculate(-15693, -75062.0), 59369.00, "")

    def test0988(self):
        self.assertEquals(self.calculate(-10291, -137993.0), 127702.00, "")

    def test0989(self):
        self.assertEquals(self.calculate(2107, 122142.0), -120035.00, "")

    def test0990(self):
        self.assertEquals(self.calculate(1242, -165842.0), 167084.00, "")

    def test0991(self):
        self.assertEquals(self.calculate(-9105, -100503.0), 91398.00, "")

    def test0992(self):
        self.assertEquals(self.calculate(28206, -137618.0), 165824.00, "")

    def test0993(self):
        self.assertEquals(self.calculate(-19955, 134434.0), -154389.00, "")

    def test0994(self):
        self.assertEquals(self.calculate(-9181, 76616.0), -85797.00, "")

    def test0995(self):
        self.assertEquals(self.calculate(20083, -13955.0), 34038.00, "")

    def test0996(self):
        self.assertEquals(self.calculate(-13054, 3107.0), -16161.00, "")

    def test0997(self):
        self.assertEquals(self.calculate(-10672, 147048.0), -157720.00, "")

    def test0998(self):
        self.assertEquals(self.calculate(-12938, -184935.0), 171997.00, "")

    def test0999(self):
        self.assertEquals(self.calculate(4704, 197073.0), -192369.00, "")

    def test1000(self):
        self.assertEquals(self.calculate(-25088, -166494.0), 141406.00, "")

    def test1001(self):
        self.assertEquals(self.calculate(26696, 90140.0), -63444.00, "")

    def test1002(self):
        self.assertEquals(self.calculate(15665, -187687.0), 203352.00, "")

    def test1003(self):
        self.assertEquals(self.calculate(-26103, -179820.0), 153717.00, "")

    def test1004(self):
        self.assertEquals(self.calculate(-21773, -17776.0), -3997.00, "")

    def test1005(self):
        self.assertEquals(self.calculate(-27255, 191501.0), -218756.00, "")

    def test1006(self):
        self.assertEquals(self.calculate(-8092, -119470.0), 111378.00, "")

    def test1007(self):
        self.assertEquals(self.calculate(-22646, -89490.0), 66844.00, "")

    def test1008(self):
        self.assertEquals(self.calculate(18946, -49584.0), 68530.00, "")

    def test1009(self):
        self.assertEquals(self.calculate(-12163, 140743.0), -152906.00, "")

    def test1010(self):
        self.assertEquals(self.calculate(-27962, -192473.0), 164511.00, "")

    def test1011(self):
        self.assertEquals(self.calculate(17189, 15045.0), 2144.00, "")

    def test1012(self):
        self.assertEquals(self.calculate(32389, 172899.0), -140510.00, "")

    def test1013(self):
        self.assertEquals(self.calculate(-24036, -76490.0), 52454.00, "")

    def test1014(self):
        self.assertEquals(self.calculate(-11184, -154602.0), 143418.00, "")

    def test1015(self):
        self.assertEquals(self.calculate(-25609, -94752.0), 69143.00, "")

    def test1016(self):
        self.assertEquals(self.calculate(-10979, -109174.0), 98195.00, "")

    def test1017(self):
        self.assertEquals(self.calculate(-9245, -32743.0), 23498.00, "")

    def test1018(self):
        self.assertEquals(self.calculate(16886, -79246.0), 96132.00, "")

    def test1019(self):
        self.assertEquals(self.calculate(29653, -90824.0), 120477.00, "")

    def test1020(self):
        self.assertEquals(self.calculate(-23842, 76643.0), -100485.00, "")

    def test1021(self):
        self.assertEquals(self.calculate(-3030, 188059.0), -191089.00, "")

    def test1022(self):
        self.assertEquals(self.calculate(18605, 70895.0), -52290.00, "")

    def test1023(self):
        self.assertEquals(self.calculate(7103, 76896.0), -69793.00, "")



class TestVM_Sub_LongInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushW(rhs)
        v.VM_Sub()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-1927789072, 23125), -1927812197)

    def test0001(self):
        self.assertEquals(self.calculate(-2092096508, -27615), -2092068893)

    def test0002(self):
        self.assertEquals(self.calculate(-344997155, -23679), -344973476)

    def test0003(self):
        self.assertEquals(self.calculate(1346410253, -7407), 1346417660)

    def test0004(self):
        self.assertEquals(self.calculate(1974288833, 8596), 1974280237)

    def test0005(self):
        self.assertEquals(self.calculate(1869446980, 29911), 1869417069)

    def test0006(self):
        self.assertEquals(self.calculate(1563365183, -679), 1563365862)

    def test0007(self):
        self.assertEquals(self.calculate(-220704132, 25223), -220729355)

    def test0008(self):
        self.assertEquals(self.calculate(-676251796, -6836), -676244960)

    def test0009(self):
        self.assertEquals(self.calculate(2058539319, 29441), 2058509878)

    def test0010(self):
        self.assertEquals(self.calculate(1210743938, 23584), 1210720354)

    def test0011(self):
        self.assertEquals(self.calculate(911724540, 11654), 911712886)

    def test0012(self):
        self.assertEquals(self.calculate(-202968427, -20227), -202948200)

    def test0013(self):
        self.assertEquals(self.calculate(1787750641, -18256), 1787768897)

    def test0014(self):
        self.assertEquals(self.calculate(568728560, -24999), 568753559)

    def test0015(self):
        self.assertEquals(self.calculate(-785460444, -23647), -785436797)

    def test0016(self):
        self.assertEquals(self.calculate(-307586419, 32318), -307618737)

    def test0017(self):
        self.assertEquals(self.calculate(2146093219, 4883), 2146088336)

    def test0018(self):
        self.assertEquals(self.calculate(-995771146, -2848), -995768298)

    def test0019(self):
        self.assertEquals(self.calculate(-513760988, -28541), -513732447)

    def test0020(self):
        self.assertEquals(self.calculate(-1944686794, 11856), -1944698650)

    def test0021(self):
        self.assertEquals(self.calculate(830180328, -131), 830180459)

    def test0022(self):
        self.assertEquals(self.calculate(-853519230, 18094), -853537324)

    def test0023(self):
        self.assertEquals(self.calculate(2000429382, 8271), 2000421111)

    def test0024(self):
        self.assertEquals(self.calculate(-67366563, 9321), -67375884)

    def test0025(self):
        self.assertEquals(self.calculate(1259890464, 7763), 1259882701)

    def test0026(self):
        self.assertEquals(self.calculate(-66291250, -30785), -66260465)

    def test0027(self):
        self.assertEquals(self.calculate(-256158614, -7529), -256151085)

    def test0028(self):
        self.assertEquals(self.calculate(1837786778, -10806), 1837797584)

    def test0029(self):
        self.assertEquals(self.calculate(851840251, 8640), 851831611)

    def test0030(self):
        self.assertEquals(self.calculate(-1529546320, -16628), -1529529692)

    def test0031(self):
        self.assertEquals(self.calculate(923719110, 11158), 923707952)

    def test0032(self):
        self.assertEquals(self.calculate(1568261086, 4488), 1568256598)

    def test0033(self):
        self.assertEquals(self.calculate(1460642671, 29125), 1460613546)

    def test0034(self):
        self.assertEquals(self.calculate(669729287, 13874), 669715413)

    def test0035(self):
        self.assertEquals(self.calculate(632253906, 27461), 632226445)

    def test0036(self):
        self.assertEquals(self.calculate(-1204016698, -27534), -1203989164)

    def test0037(self):
        self.assertEquals(self.calculate(1125945735, -18868), 1125964603)

    def test0038(self):
        self.assertEquals(self.calculate(-162408953, 13678), -162422631)

    def test0039(self):
        self.assertEquals(self.calculate(3108658, -11538), 3120196)

    def test0040(self):
        self.assertEquals(self.calculate(985691137, 29870), 985661267)

    def test0041(self):
        self.assertEquals(self.calculate(-1602210355, -12059), -1602198296)

    def test0042(self):
        self.assertEquals(self.calculate(-1151851985, -9308), -1151842677)

    def test0043(self):
        self.assertEquals(self.calculate(1152760955, -19062), 1152780017)

    def test0044(self):
        self.assertEquals(self.calculate(971800468, -4967), 971805435)

    def test0045(self):
        self.assertEquals(self.calculate(1676105023, -20027), 1676125050)

    def test0046(self):
        self.assertEquals(self.calculate(236951540, 21283), 236930257)

    def test0047(self):
        self.assertEquals(self.calculate(117891618, 7626), 117883992)

    def test0048(self):
        self.assertEquals(self.calculate(-916636700, -10061), -916626639)

    def test0049(self):
        self.assertEquals(self.calculate(826570233, -24743), 826594976)

    def test0050(self):
        self.assertEquals(self.calculate(-1471004988, 27707), -1471032695)

    def test0051(self):
        self.assertEquals(self.calculate(786199961, -18634), 786218595)

    def test0052(self):
        self.assertEquals(self.calculate(-500757395, 12199), -500769594)

    def test0053(self):
        self.assertEquals(self.calculate(-2117197791, 13125), -2117210916)

    def test0054(self):
        self.assertEquals(self.calculate(2090012511, 1255), 2090011256)

    def test0055(self):
        self.assertEquals(self.calculate(1273053968, -22058), 1273076026)

    def test0056(self):
        self.assertEquals(self.calculate(-1131208480, 2412), -1131210892)

    def test0057(self):
        self.assertEquals(self.calculate(1251386083, -4620), 1251390703)

    def test0058(self):
        self.assertEquals(self.calculate(-1036946837, -22973), -1036923864)

    def test0059(self):
        self.assertEquals(self.calculate(-598959819, -25010), -598934809)

    def test0060(self):
        self.assertEquals(self.calculate(1410279245, 11409), 1410267836)

    def test0061(self):
        self.assertEquals(self.calculate(-2021452752, -15417), -2021437335)

    def test0062(self):
        self.assertEquals(self.calculate(60161406, 1802), 60159604)

    def test0063(self):
        self.assertEquals(self.calculate(-554600047, 4011), -554604058)

    def test0064(self):
        self.assertEquals(self.calculate(-1296237169, -8733), -1296228436)

    def test0065(self):
        self.assertEquals(self.calculate(1264646610, -15169), 1264661779)

    def test0066(self):
        self.assertEquals(self.calculate(1886106097, -6095), 1886112192)

    def test0067(self):
        self.assertEquals(self.calculate(-523079881, 22401), -523102282)

    def test0068(self):
        self.assertEquals(self.calculate(1234602148, 16153), 1234585995)

    def test0069(self):
        self.assertEquals(self.calculate(-1572118312, 23668), -1572141980)

    def test0070(self):
        self.assertEquals(self.calculate(1441086526, 20082), 1441066444)

    def test0071(self):
        self.assertEquals(self.calculate(-1910070064, 16971), -1910087035)

    def test0072(self):
        self.assertEquals(self.calculate(385180951, 16847), 385164104)

    def test0073(self):
        self.assertEquals(self.calculate(-1152480484, 30760), -1152511244)

    def test0074(self):
        self.assertEquals(self.calculate(2011184238, -20206), 2011204444)

    def test0075(self):
        self.assertEquals(self.calculate(-1682701458, 3990), -1682705448)

    def test0076(self):
        self.assertEquals(self.calculate(-1096736071, -9462), -1096726609)

    def test0077(self):
        self.assertEquals(self.calculate(690558942, 8292), 690550650)

    def test0078(self):
        self.assertEquals(self.calculate(439768197, 7553), 439760644)

    def test0079(self):
        self.assertEquals(self.calculate(-2103528430, 4191), -2103532621)

    def test0080(self):
        self.assertEquals(self.calculate(-680305891, -29446), -680276445)

    def test0081(self):
        self.assertEquals(self.calculate(1248686179, 23579), 1248662600)

    def test0082(self):
        self.assertEquals(self.calculate(410544500, -6807), 410551307)

    def test0083(self):
        self.assertEquals(self.calculate(-1256129967, -23741), -1256106226)

    def test0084(self):
        self.assertEquals(self.calculate(-439998758, -10444), -439988314)

    def test0085(self):
        self.assertEquals(self.calculate(1125058070, -19029), 1125077099)

    def test0086(self):
        self.assertEquals(self.calculate(1254968609, -13210), 1254981819)

    def test0087(self):
        self.assertEquals(self.calculate(811174247, 13806), 811160441)

    def test0088(self):
        self.assertEquals(self.calculate(951243075, 6149), 951236926)

    def test0089(self):
        self.assertEquals(self.calculate(300248981, 26517), 300222464)

    def test0090(self):
        self.assertEquals(self.calculate(1579758895, 32441), 1579726454)

    def test0091(self):
        self.assertEquals(self.calculate(327021457, -15263), 327036720)

    def test0092(self):
        self.assertEquals(self.calculate(-793038918, -29919), -793008999)

    def test0093(self):
        self.assertEquals(self.calculate(41356983, 11764), 41345219)

    def test0094(self):
        self.assertEquals(self.calculate(-141889643, 8387), -141898030)

    def test0095(self):
        self.assertEquals(self.calculate(1994819577, -16382), 1994835959)

    def test0096(self):
        self.assertEquals(self.calculate(143414634, 18274), 143396360)

    def test0097(self):
        self.assertEquals(self.calculate(-1749911949, -22148), -1749889801)

    def test0098(self):
        self.assertEquals(self.calculate(363763882, 15787), 363748095)

    def test0099(self):
        self.assertEquals(self.calculate(1005880569, 25859), 1005854710)

    def test0100(self):
        self.assertEquals(self.calculate(-51088878, -15687), -51073191)

    def test0101(self):
        self.assertEquals(self.calculate(-475433295, 23431), -475456726)

    def test0102(self):
        self.assertEquals(self.calculate(-361555184, 4916), -361560100)

    def test0103(self):
        self.assertEquals(self.calculate(94187979, 13727), 94174252)

    def test0104(self):
        self.assertEquals(self.calculate(243616966, -4659), 243621625)

    def test0105(self):
        self.assertEquals(self.calculate(-1268396779, -11396), -1268385383)

    def test0106(self):
        self.assertEquals(self.calculate(1378694527, 10005), 1378684522)

    def test0107(self):
        self.assertEquals(self.calculate(1447912885, 19478), 1447893407)

    def test0108(self):
        self.assertEquals(self.calculate(-1163279516, -27702), -1163251814)

    def test0109(self):
        self.assertEquals(self.calculate(-593140913, 6683), -593147596)

    def test0110(self):
        self.assertEquals(self.calculate(365939040, 6401), 365932639)

    def test0111(self):
        self.assertEquals(self.calculate(1848053756, -13730), 1848067486)

    def test0112(self):
        self.assertEquals(self.calculate(1771352479, -7833), 1771360312)

    def test0113(self):
        self.assertEquals(self.calculate(-1882718411, 29856), -1882748267)

    def test0114(self):
        self.assertEquals(self.calculate(2133656092, -14693), 2133670785)

    def test0115(self):
        self.assertEquals(self.calculate(495907394, 22146), 495885248)

    def test0116(self):
        self.assertEquals(self.calculate(1316729324, 16410), 1316712914)

    def test0117(self):
        self.assertEquals(self.calculate(1713152550, 10759), 1713141791)

    def test0118(self):
        self.assertEquals(self.calculate(-1085789429, -4740), -1085784689)

    def test0119(self):
        self.assertEquals(self.calculate(-532379403, 11499), -532390902)

    def test0120(self):
        self.assertEquals(self.calculate(2056311880, -13473), 2056325353)

    def test0121(self):
        self.assertEquals(self.calculate(-1034004460, -25643), -1033978817)

    def test0122(self):
        self.assertEquals(self.calculate(1309607109, 9725), 1309597384)

    def test0123(self):
        self.assertEquals(self.calculate(934304378, 25672), 934278706)

    def test0124(self):
        self.assertEquals(self.calculate(871580947, 15034), 871565913)

    def test0125(self):
        self.assertEquals(self.calculate(-859770575, -2494), -859768081)

    def test0126(self):
        self.assertEquals(self.calculate(-558433340, -18217), -558415123)

    def test0127(self):
        self.assertEquals(self.calculate(706468257, -14297), 706482554)

    def test0128(self):
        self.assertEquals(self.calculate(-1280630654, 16832), -1280647486)

    def test0129(self):
        self.assertEquals(self.calculate(1994620088, -6019), 1994626107)

    def test0130(self):
        self.assertEquals(self.calculate(1324860310, -19449), 1324879759)

    def test0131(self):
        self.assertEquals(self.calculate(1631826898, -23919), 1631850817)

    def test0132(self):
        self.assertEquals(self.calculate(-1206632934, -30825), -1206602109)

    def test0133(self):
        self.assertEquals(self.calculate(-1240676625, 3114), -1240679739)

    def test0134(self):
        self.assertEquals(self.calculate(-1031654881, 13080), -1031667961)

    def test0135(self):
        self.assertEquals(self.calculate(2080899717, 6038), 2080893679)

    def test0136(self):
        self.assertEquals(self.calculate(-1097805463, 17025), -1097822488)

    def test0137(self):
        self.assertEquals(self.calculate(-1870707404, 31123), -1870738527)

    def test0138(self):
        self.assertEquals(self.calculate(1200172212, -25347), 1200197559)

    def test0139(self):
        self.assertEquals(self.calculate(1411738152, 14262), 1411723890)

    def test0140(self):
        self.assertEquals(self.calculate(1296422670, -32650), 1296455320)

    def test0141(self):
        self.assertEquals(self.calculate(1019270347, -25653), 1019296000)

    def test0142(self):
        self.assertEquals(self.calculate(1389988756, -16293), 1390005049)

    def test0143(self):
        self.assertEquals(self.calculate(2074766478, 15918), 2074750560)

    def test0144(self):
        self.assertEquals(self.calculate(477366805, -7651), 477374456)

    def test0145(self):
        self.assertEquals(self.calculate(-32227473, 27894), -32255367)

    def test0146(self):
        self.assertEquals(self.calculate(-345945684, -5329), -345940355)

    def test0147(self):
        self.assertEquals(self.calculate(1838115204, 29689), 1838085515)

    def test0148(self):
        self.assertEquals(self.calculate(1362134706, 10735), 1362123971)

    def test0149(self):
        self.assertEquals(self.calculate(1512775407, -15206), 1512790613)

    def test0150(self):
        self.assertEquals(self.calculate(31955996, -23544), 31979540)

    def test0151(self):
        self.assertEquals(self.calculate(-1824954724, -13032), -1824941692)

    def test0152(self):
        self.assertEquals(self.calculate(502462128, 23948), 502438180)

    def test0153(self):
        self.assertEquals(self.calculate(-558264339, 28698), -558293037)

    def test0154(self):
        self.assertEquals(self.calculate(-1091628612, -23059), -1091605553)

    def test0155(self):
        self.assertEquals(self.calculate(223612081, -12304), 223624385)

    def test0156(self):
        self.assertEquals(self.calculate(-801933749, 17773), -801951522)

    def test0157(self):
        self.assertEquals(self.calculate(-504878593, -13675), -504864918)

    def test0158(self):
        self.assertEquals(self.calculate(-879736872, -3420), -879733452)

    def test0159(self):
        self.assertEquals(self.calculate(2044182610, 29625), 2044152985)

    def test0160(self):
        self.assertEquals(self.calculate(-649191845, -12619), -649179226)

    def test0161(self):
        self.assertEquals(self.calculate(-794852239, 29725), -794881964)

    def test0162(self):
        self.assertEquals(self.calculate(1615479331, 19528), 1615459803)

    def test0163(self):
        self.assertEquals(self.calculate(1043397725, 15494), 1043382231)

    def test0164(self):
        self.assertEquals(self.calculate(1321058488, -15953), 1321074441)

    def test0165(self):
        self.assertEquals(self.calculate(-232726037, 23882), -232749919)

    def test0166(self):
        self.assertEquals(self.calculate(-1564406657, 3449), -1564410106)

    def test0167(self):
        self.assertEquals(self.calculate(-1232490897, -11007), -1232479890)

    def test0168(self):
        self.assertEquals(self.calculate(1700050361, -13569), 1700063930)

    def test0169(self):
        self.assertEquals(self.calculate(-2112969077, -5232), -2112963845)

    def test0170(self):
        self.assertEquals(self.calculate(1257640868, 16562), 1257624306)

    def test0171(self):
        self.assertEquals(self.calculate(1681198535, 18072), 1681180463)

    def test0172(self):
        self.assertEquals(self.calculate(1336808084, -25368), 1336833452)

    def test0173(self):
        self.assertEquals(self.calculate(70995062, -2556), 70997618)

    def test0174(self):
        self.assertEquals(self.calculate(1887448871, 11241), 1887437630)

    def test0175(self):
        self.assertEquals(self.calculate(-1843979187, -3223), -1843975964)

    def test0176(self):
        self.assertEquals(self.calculate(-664215188, -15110), -664200078)

    def test0177(self):
        self.assertEquals(self.calculate(716186009, 28817), 716157192)

    def test0178(self):
        self.assertEquals(self.calculate(383999882, -29906), 384029788)

    def test0179(self):
        self.assertEquals(self.calculate(1865218051, 21446), 1865196605)

    def test0180(self):
        self.assertEquals(self.calculate(-1863293272, 11858), -1863305130)

    def test0181(self):
        self.assertEquals(self.calculate(-549725408, 15799), -549741207)

    def test0182(self):
        self.assertEquals(self.calculate(164011651, -3150), 164014801)

    def test0183(self):
        self.assertEquals(self.calculate(328924303, -2078), 328926381)

    def test0184(self):
        self.assertEquals(self.calculate(-1753571710, 10692), -1753582402)

    def test0185(self):
        self.assertEquals(self.calculate(484376515, -24830), 484401345)

    def test0186(self):
        self.assertEquals(self.calculate(-1846665605, -30081), -1846635524)

    def test0187(self):
        self.assertEquals(self.calculate(2005959030, 28651), 2005930379)

    def test0188(self):
        self.assertEquals(self.calculate(1356667170, 32217), 1356634953)

    def test0189(self):
        self.assertEquals(self.calculate(710749670, -13134), 710762804)

    def test0190(self):
        self.assertEquals(self.calculate(-411655028, -29680), -411625348)

    def test0191(self):
        self.assertEquals(self.calculate(550396439, 20686), 550375753)

    def test0192(self):
        self.assertEquals(self.calculate(-1586361772, -23033), -1586338739)

    def test0193(self):
        self.assertEquals(self.calculate(836347402, -13701), 836361103)

    def test0194(self):
        self.assertEquals(self.calculate(803886673, -29237), 803915910)

    def test0195(self):
        self.assertEquals(self.calculate(1579220855, -28472), 1579249327)

    def test0196(self):
        self.assertEquals(self.calculate(-421218956, 8536), -421227492)

    def test0197(self):
        self.assertEquals(self.calculate(1512893428, -31486), 1512924914)

    def test0198(self):
        self.assertEquals(self.calculate(823282929, 6727), 823276202)

    def test0199(self):
        self.assertEquals(self.calculate(1842971217, -17095), 1842988312)

    def test0200(self):
        self.assertEquals(self.calculate(679377127, 19088), 679358039)

    def test0201(self):
        self.assertEquals(self.calculate(1187954168, -29437), 1187983605)

    def test0202(self):
        self.assertEquals(self.calculate(1339059705, -31499), 1339091204)

    def test0203(self):
        self.assertEquals(self.calculate(-2024522650, 11553), -2024534203)

    def test0204(self):
        self.assertEquals(self.calculate(1253997520, -21203), 1254018723)

    def test0205(self):
        self.assertEquals(self.calculate(1434933289, -18690), 1434951979)

    def test0206(self):
        self.assertEquals(self.calculate(134867845, -3778), 134871623)

    def test0207(self):
        self.assertEquals(self.calculate(1797912503, -17444), 1797929947)

    def test0208(self):
        self.assertEquals(self.calculate(1724832453, 11709), 1724820744)

    def test0209(self):
        self.assertEquals(self.calculate(460172877, 570), 460172307)

    def test0210(self):
        self.assertEquals(self.calculate(-1852820654, 16154), -1852836808)

    def test0211(self):
        self.assertEquals(self.calculate(1525287802, 10393), 1525277409)

    def test0212(self):
        self.assertEquals(self.calculate(-300560011, 28328), -300588339)

    def test0213(self):
        self.assertEquals(self.calculate(1400681050, -7621), 1400688671)

    def test0214(self):
        self.assertEquals(self.calculate(-336672465, -32400), -336640065)

    def test0215(self):
        self.assertEquals(self.calculate(1740244695, 3494), 1740241201)

    def test0216(self):
        self.assertEquals(self.calculate(-2143199598, 7288), -2143206886)

    def test0217(self):
        self.assertEquals(self.calculate(1667870537, 11370), 1667859167)

    def test0218(self):
        self.assertEquals(self.calculate(1200477121, 5162), 1200471959)

    def test0219(self):
        self.assertEquals(self.calculate(2012259939, 32500), 2012227439)

    def test0220(self):
        self.assertEquals(self.calculate(-224317035, -4334), -224312701)

    def test0221(self):
        self.assertEquals(self.calculate(97992356, 17290), 97975066)

    def test0222(self):
        self.assertEquals(self.calculate(-28970847, 19037), -28989884)

    def test0223(self):
        self.assertEquals(self.calculate(1990335745, -30959), 1990366704)

    def test0224(self):
        self.assertEquals(self.calculate(1997873475, -32450), 1997905925)

    def test0225(self):
        self.assertEquals(self.calculate(-1039027479, -4771), -1039022708)

    def test0226(self):
        self.assertEquals(self.calculate(489825311, 17210), 489808101)

    def test0227(self):
        self.assertEquals(self.calculate(509535702, -20838), 509556540)

    def test0228(self):
        self.assertEquals(self.calculate(-1935211568, -8214), -1935203354)

    def test0229(self):
        self.assertEquals(self.calculate(35333866, 10421), 35323445)

    def test0230(self):
        self.assertEquals(self.calculate(943299829, 11210), 943288619)

    def test0231(self):
        self.assertEquals(self.calculate(1845613108, 4230), 1845608878)

    def test0232(self):
        self.assertEquals(self.calculate(822494862, -27444), 822522306)

    def test0233(self):
        self.assertEquals(self.calculate(-507124438, 9068), -507133506)

    def test0234(self):
        self.assertEquals(self.calculate(751884279, -17001), 751901280)

    def test0235(self):
        self.assertEquals(self.calculate(1598557545, -8568), 1598566113)

    def test0236(self):
        self.assertEquals(self.calculate(-2109599663, -22630), -2109577033)

    def test0237(self):
        self.assertEquals(self.calculate(-1343357484, -14298), -1343343186)

    def test0238(self):
        self.assertEquals(self.calculate(402201440, -29375), 402230815)

    def test0239(self):
        self.assertEquals(self.calculate(-1650908982, -20223), -1650888759)

    def test0240(self):
        self.assertEquals(self.calculate(1711921418, 23079), 1711898339)

    def test0241(self):
        self.assertEquals(self.calculate(2088616961, 29280), 2088587681)

    def test0242(self):
        self.assertEquals(self.calculate(1219899566, 6569), 1219892997)

    def test0243(self):
        self.assertEquals(self.calculate(1840682984, -3536), 1840686520)

    def test0244(self):
        self.assertEquals(self.calculate(-1053195718, -16857), -1053178861)

    def test0245(self):
        self.assertEquals(self.calculate(-1095031255, 20960), -1095052215)

    def test0246(self):
        self.assertEquals(self.calculate(1970675492, -27552), 1970703044)

    def test0247(self):
        self.assertEquals(self.calculate(-1215389075, 24118), -1215413193)

    def test0248(self):
        self.assertEquals(self.calculate(549993352, -11205), 550004557)

    def test0249(self):
        self.assertEquals(self.calculate(-1238507576, -12859), -1238494717)

    def test0250(self):
        self.assertEquals(self.calculate(611005007, -31468), 611036475)

    def test0251(self):
        self.assertEquals(self.calculate(-1374165103, 29354), -1374194457)

    def test0252(self):
        self.assertEquals(self.calculate(-296452795, 32191), -296484986)

    def test0253(self):
        self.assertEquals(self.calculate(1164444732, -21030), 1164465762)

    def test0254(self):
        self.assertEquals(self.calculate(-1092642796, 13807), -1092656603)

    def test0255(self):
        self.assertEquals(self.calculate(735633710, -31643), 735665353)

    def test0256(self):
        self.assertEquals(self.calculate(1069041340, -7132), 1069048472)

    def test0257(self):
        self.assertEquals(self.calculate(187490519, 20137), 187470382)

    def test0258(self):
        self.assertEquals(self.calculate(-1725945100, 24582), -1725969682)

    def test0259(self):
        self.assertEquals(self.calculate(1646164249, -23594), 1646187843)

    def test0260(self):
        self.assertEquals(self.calculate(-1705020224, -12757), -1705007467)

    def test0261(self):
        self.assertEquals(self.calculate(-1659356477, -18674), -1659337803)

    def test0262(self):
        self.assertEquals(self.calculate(-525589468, -11836), -525577632)

    def test0263(self):
        self.assertEquals(self.calculate(1134896230, -14342), 1134910572)

    def test0264(self):
        self.assertEquals(self.calculate(1028311872, 17382), 1028294490)

    def test0265(self):
        self.assertEquals(self.calculate(564847206, -17503), 564864709)

    def test0266(self):
        self.assertEquals(self.calculate(-902272592, -109), -902272483)

    def test0267(self):
        self.assertEquals(self.calculate(1565121590, 34), 1565121556)

    def test0268(self):
        self.assertEquals(self.calculate(1379326027, 9351), 1379316676)

    def test0269(self):
        self.assertEquals(self.calculate(736350538, 12672), 736337866)

    def test0270(self):
        self.assertEquals(self.calculate(559583174, 11336), 559571838)

    def test0271(self):
        self.assertEquals(self.calculate(2109136203, -30975), 2109167178)

    def test0272(self):
        self.assertEquals(self.calculate(-346779357, -17660), -346761697)

    def test0273(self):
        self.assertEquals(self.calculate(-257910295, 7014), -257917309)

    def test0274(self):
        self.assertEquals(self.calculate(-412325780, -6704), -412319076)

    def test0275(self):
        self.assertEquals(self.calculate(-719363819, 31952), -719395771)

    def test0276(self):
        self.assertEquals(self.calculate(-1589610954, -22021), -1589588933)

    def test0277(self):
        self.assertEquals(self.calculate(-1599044339, 12545), -1599056884)

    def test0278(self):
        self.assertEquals(self.calculate(-583268652, -16713), -583251939)

    def test0279(self):
        self.assertEquals(self.calculate(837755217, -27659), 837782876)

    def test0280(self):
        self.assertEquals(self.calculate(-1514988361, 19178), -1515007539)

    def test0281(self):
        self.assertEquals(self.calculate(993208049, 9652), 993198397)

    def test0282(self):
        self.assertEquals(self.calculate(-889881662, -7413), -889874249)

    def test0283(self):
        self.assertEquals(self.calculate(-66451835, 11676), -66463511)

    def test0284(self):
        self.assertEquals(self.calculate(1579581113, -15695), 1579596808)

    def test0285(self):
        self.assertEquals(self.calculate(719909608, 12733), 719896875)

    def test0286(self):
        self.assertEquals(self.calculate(-1731876395, -15273), -1731861122)

    def test0287(self):
        self.assertEquals(self.calculate(823584691, 32213), 823552478)

    def test0288(self):
        self.assertEquals(self.calculate(-2124733565, 15376), -2124748941)

    def test0289(self):
        self.assertEquals(self.calculate(-546402431, -29482), -546372949)

    def test0290(self):
        self.assertEquals(self.calculate(-172558040, 14646), -172572686)

    def test0291(self):
        self.assertEquals(self.calculate(-573712599, -3120), -573709479)

    def test0292(self):
        self.assertEquals(self.calculate(327412997, -28047), 327441044)

    def test0293(self):
        self.assertEquals(self.calculate(-1520556740, 3344), -1520560084)

    def test0294(self):
        self.assertEquals(self.calculate(1577958681, 27370), 1577931311)

    def test0295(self):
        self.assertEquals(self.calculate(-951919626, 4946), -951924572)

    def test0296(self):
        self.assertEquals(self.calculate(-1337060500, 31392), -1337091892)

    def test0297(self):
        self.assertEquals(self.calculate(-1551877952, 16199), -1551894151)

    def test0298(self):
        self.assertEquals(self.calculate(865956209, -19825), 865976034)

    def test0299(self):
        self.assertEquals(self.calculate(-168533244, 19711), -168552955)

    def test0300(self):
        self.assertEquals(self.calculate(-1261360933, 23862), -1261384795)

    def test0301(self):
        self.assertEquals(self.calculate(104366736, 31523), 104335213)

    def test0302(self):
        self.assertEquals(self.calculate(1482315536, 25100), 1482290436)

    def test0303(self):
        self.assertEquals(self.calculate(1148130857, 17052), 1148113805)

    def test0304(self):
        self.assertEquals(self.calculate(591269656, -27063), 591296719)

    def test0305(self):
        self.assertEquals(self.calculate(1028039718, 380), 1028039338)

    def test0306(self):
        self.assertEquals(self.calculate(-1272300981, 13225), -1272314206)

    def test0307(self):
        self.assertEquals(self.calculate(-388598943, 25382), -388624325)

    def test0308(self):
        self.assertEquals(self.calculate(-1694695706, -32629), -1694663077)

    def test0309(self):
        self.assertEquals(self.calculate(-235690595, 7001), -235697596)

    def test0310(self):
        self.assertEquals(self.calculate(-1829802181, -28979), -1829773202)

    def test0311(self):
        self.assertEquals(self.calculate(1282383430, 31140), 1282352290)

    def test0312(self):
        self.assertEquals(self.calculate(87544727, -2071), 87546798)

    def test0313(self):
        self.assertEquals(self.calculate(1914953825, 5490), 1914948335)

    def test0314(self):
        self.assertEquals(self.calculate(-1763837940, 31631), -1763869571)

    def test0315(self):
        self.assertEquals(self.calculate(67269027, 11012), 67258015)

    def test0316(self):
        self.assertEquals(self.calculate(-1892435092, 17068), -1892452160)

    def test0317(self):
        self.assertEquals(self.calculate(-1449345539, 9127), -1449354666)

    def test0318(self):
        self.assertEquals(self.calculate(120269387, 17874), 120251513)

    def test0319(self):
        self.assertEquals(self.calculate(-604895981, 22571), -604918552)

    def test0320(self):
        self.assertEquals(self.calculate(-1350944350, -10905), -1350933445)

    def test0321(self):
        self.assertEquals(self.calculate(-1967113516, -17953), -1967095563)

    def test0322(self):
        self.assertEquals(self.calculate(1194051380, -11616), 1194062996)

    def test0323(self):
        self.assertEquals(self.calculate(-1024495375, -16835), -1024478540)

    def test0324(self):
        self.assertEquals(self.calculate(-1810525118, 1249), -1810526367)

    def test0325(self):
        self.assertEquals(self.calculate(-322927720, -14798), -322912922)

    def test0326(self):
        self.assertEquals(self.calculate(1495296870, 15854), 1495281016)

    def test0327(self):
        self.assertEquals(self.calculate(2086192812, 13000), 2086179812)

    def test0328(self):
        self.assertEquals(self.calculate(97273879, 17606), 97256273)

    def test0329(self):
        self.assertEquals(self.calculate(-2114385753, -29601), -2114356152)

    def test0330(self):
        self.assertEquals(self.calculate(806906310, -27751), 806934061)

    def test0331(self):
        self.assertEquals(self.calculate(577772025, -15729), 577787754)

    def test0332(self):
        self.assertEquals(self.calculate(657515640, 941), 657514699)

    def test0333(self):
        self.assertEquals(self.calculate(-148957129, -1955), -148955174)

    def test0334(self):
        self.assertEquals(self.calculate(1705341414, -19573), 1705360987)

    def test0335(self):
        self.assertEquals(self.calculate(1402741590, -6561), 1402748151)

    def test0336(self):
        self.assertEquals(self.calculate(1865278518, -1254), 1865279772)

    def test0337(self):
        self.assertEquals(self.calculate(1755439803, 25730), 1755414073)

    def test0338(self):
        self.assertEquals(self.calculate(52232282, -3121), 52235403)

    def test0339(self):
        self.assertEquals(self.calculate(-1489286442, -21844), -1489264598)

    def test0340(self):
        self.assertEquals(self.calculate(-738322576, -28487), -738294089)

    def test0341(self):
        self.assertEquals(self.calculate(1723374290, 23005), 1723351285)

    def test0342(self):
        self.assertEquals(self.calculate(-1015010054, -7932), -1015002122)

    def test0343(self):
        self.assertEquals(self.calculate(-1000404744, 715), -1000405459)

    def test0344(self):
        self.assertEquals(self.calculate(179153630, -15628), 179169258)

    def test0345(self):
        self.assertEquals(self.calculate(731959644, 26385), 731933259)

    def test0346(self):
        self.assertEquals(self.calculate(1249908153, 12380), 1249895773)

    def test0347(self):
        self.assertEquals(self.calculate(-1888902758, 9968), -1888912726)

    def test0348(self):
        self.assertEquals(self.calculate(330039611, 21171), 330018440)

    def test0349(self):
        self.assertEquals(self.calculate(-223747639, 23022), -223770661)

    def test0350(self):
        self.assertEquals(self.calculate(97274164, -511), 97274675)

    def test0351(self):
        self.assertEquals(self.calculate(612212988, -4874), 612217862)

    def test0352(self):
        self.assertEquals(self.calculate(-723301209, 6186), -723307395)

    def test0353(self):
        self.assertEquals(self.calculate(1095333485, 4571), 1095328914)

    def test0354(self):
        self.assertEquals(self.calculate(-1508401772, -16492), -1508385280)

    def test0355(self):
        self.assertEquals(self.calculate(360489553, 31975), 360457578)

    def test0356(self):
        self.assertEquals(self.calculate(750779648, -19082), 750798730)

    def test0357(self):
        self.assertEquals(self.calculate(-161345887, 11967), -161357854)

    def test0358(self):
        self.assertEquals(self.calculate(301445494, -29225), 301474719)

    def test0359(self):
        self.assertEquals(self.calculate(-1301848829, 3747), -1301852576)

    def test0360(self):
        self.assertEquals(self.calculate(-67410069, 28641), -67438710)

    def test0361(self):
        self.assertEquals(self.calculate(2134842352, -2123), 2134844475)

    def test0362(self):
        self.assertEquals(self.calculate(838903416, 1983), 838901433)

    def test0363(self):
        self.assertEquals(self.calculate(1257766229, -20502), 1257786731)

    def test0364(self):
        self.assertEquals(self.calculate(765049075, -2198), 765051273)

    def test0365(self):
        self.assertEquals(self.calculate(1250073484, 14788), 1250058696)

    def test0366(self):
        self.assertEquals(self.calculate(-1514350801, 26779), -1514377580)

    def test0367(self):
        self.assertEquals(self.calculate(-1747009415, -16533), -1746992882)

    def test0368(self):
        self.assertEquals(self.calculate(580389813, 9262), 580380551)

    def test0369(self):
        self.assertEquals(self.calculate(-66631342, -7125), -66624217)

    def test0370(self):
        self.assertEquals(self.calculate(-389278496, 31531), -389310027)

    def test0371(self):
        self.assertEquals(self.calculate(-670302341, 13981), -670316322)

    def test0372(self):
        self.assertEquals(self.calculate(220796043, -27559), 220823602)

    def test0373(self):
        self.assertEquals(self.calculate(-499184638, 24089), -499208727)

    def test0374(self):
        self.assertEquals(self.calculate(-1448943788, -10779), -1448933009)

    def test0375(self):
        self.assertEquals(self.calculate(2065613341, -25755), 2065639096)

    def test0376(self):
        self.assertEquals(self.calculate(-818235565, 15441), -818251006)

    def test0377(self):
        self.assertEquals(self.calculate(871387102, -24380), 871411482)

    def test0378(self):
        self.assertEquals(self.calculate(1284138576, -26728), 1284165304)

    def test0379(self):
        self.assertEquals(self.calculate(-494937296, -2455), -494934841)

    def test0380(self):
        self.assertEquals(self.calculate(-1939730556, 9806), -1939740362)

    def test0381(self):
        self.assertEquals(self.calculate(892282534, 18947), 892263587)

    def test0382(self):
        self.assertEquals(self.calculate(1851478679, -5695), 1851484374)

    def test0383(self):
        self.assertEquals(self.calculate(1980126158, 21079), 1980105079)

    def test0384(self):
        self.assertEquals(self.calculate(-935323473, 29524), -935352997)

    def test0385(self):
        self.assertEquals(self.calculate(-1195339810, 2471), -1195342281)

    def test0386(self):
        self.assertEquals(self.calculate(-604934711, 26210), -604960921)

    def test0387(self):
        self.assertEquals(self.calculate(-1949633525, -6136), -1949627389)

    def test0388(self):
        self.assertEquals(self.calculate(1446105068, -17068), 1446122136)

    def test0389(self):
        self.assertEquals(self.calculate(45405508, -6944), 45412452)

    def test0390(self):
        self.assertEquals(self.calculate(-2050450521, -29177), -2050421344)

    def test0391(self):
        self.assertEquals(self.calculate(1667722763, -27582), 1667750345)

    def test0392(self):
        self.assertEquals(self.calculate(1511505990, 1705), 1511504285)

    def test0393(self):
        self.assertEquals(self.calculate(-1030481811, -30982), -1030450829)

    def test0394(self):
        self.assertEquals(self.calculate(1703599455, -29522), 1703628977)

    def test0395(self):
        self.assertEquals(self.calculate(268183033, 5718), 268177315)

    def test0396(self):
        self.assertEquals(self.calculate(1179196984, 7046), 1179189938)

    def test0397(self):
        self.assertEquals(self.calculate(-1398177532, 22132), -1398199664)

    def test0398(self):
        self.assertEquals(self.calculate(-1886863249, 13993), -1886877242)

    def test0399(self):
        self.assertEquals(self.calculate(-421273161, -6940), -421266221)

    def test0400(self):
        self.assertEquals(self.calculate(479108775, -21621), 479130396)

    def test0401(self):
        self.assertEquals(self.calculate(2087005092, 32644), 2086972448)

    def test0402(self):
        self.assertEquals(self.calculate(795481650, -5333), 795486983)

    def test0403(self):
        self.assertEquals(self.calculate(-568955571, 12599), -568968170)

    def test0404(self):
        self.assertEquals(self.calculate(608291619, -28143), 608319762)

    def test0405(self):
        self.assertEquals(self.calculate(1014105701, -12102), 1014117803)

    def test0406(self):
        self.assertEquals(self.calculate(-1684187304, 29129), -1684216433)

    def test0407(self):
        self.assertEquals(self.calculate(354783810, -10228), 354794038)

    def test0408(self):
        self.assertEquals(self.calculate(-1731417630, 29263), -1731446893)

    def test0409(self):
        self.assertEquals(self.calculate(-1185307066, 21448), -1185328514)

    def test0410(self):
        self.assertEquals(self.calculate(-173885651, -7493), -173878158)

    def test0411(self):
        self.assertEquals(self.calculate(1082685324, -14451), 1082699775)

    def test0412(self):
        self.assertEquals(self.calculate(1297532339, 1801), 1297530538)

    def test0413(self):
        self.assertEquals(self.calculate(530955956, -7573), 530963529)

    def test0414(self):
        self.assertEquals(self.calculate(-1010052341, -1012), -1010051329)

    def test0415(self):
        self.assertEquals(self.calculate(894053295, 16428), 894036867)

    def test0416(self):
        self.assertEquals(self.calculate(-1791319249, 21822), -1791341071)

    def test0417(self):
        self.assertEquals(self.calculate(-1843516465, 10128), -1843526593)

    def test0418(self):
        self.assertEquals(self.calculate(1863188873, 17753), 1863171120)

    def test0419(self):
        self.assertEquals(self.calculate(-1862530779, 2047), -1862532826)

    def test0420(self):
        self.assertEquals(self.calculate(-1800896190, 12325), -1800908515)

    def test0421(self):
        self.assertEquals(self.calculate(-625984451, -10489), -625973962)

    def test0422(self):
        self.assertEquals(self.calculate(1247225673, 29920), 1247195753)

    def test0423(self):
        self.assertEquals(self.calculate(-1149493833, 30358), -1149524191)

    def test0424(self):
        self.assertEquals(self.calculate(-2046764300, -2561), -2046761739)

    def test0425(self):
        self.assertEquals(self.calculate(-412352691, 17376), -412370067)

    def test0426(self):
        self.assertEquals(self.calculate(459106561, -32404), 459138965)

    def test0427(self):
        self.assertEquals(self.calculate(1131674574, 1148), 1131673426)

    def test0428(self):
        self.assertEquals(self.calculate(-481875414, -11333), -481864081)

    def test0429(self):
        self.assertEquals(self.calculate(75976844, -369), 75977213)

    def test0430(self):
        self.assertEquals(self.calculate(2022045560, -8661), 2022054221)

    def test0431(self):
        self.assertEquals(self.calculate(-43796156, -12862), -43783294)

    def test0432(self):
        self.assertEquals(self.calculate(-535540697, 27838), -535568535)

    def test0433(self):
        self.assertEquals(self.calculate(1047480266, -5953), 1047486219)

    def test0434(self):
        self.assertEquals(self.calculate(1770483585, 30350), 1770453235)

    def test0435(self):
        self.assertEquals(self.calculate(-1970618498, 12916), -1970631414)

    def test0436(self):
        self.assertEquals(self.calculate(-1123191860, 6384), -1123198244)

    def test0437(self):
        self.assertEquals(self.calculate(-1886820519, -6791), -1886813728)

    def test0438(self):
        self.assertEquals(self.calculate(149042005, -24879), 149066884)

    def test0439(self):
        self.assertEquals(self.calculate(-2041108604, -485), -2041108119)

    def test0440(self):
        self.assertEquals(self.calculate(151642529, 30256), 151612273)

    def test0441(self):
        self.assertEquals(self.calculate(-1747458802, 16938), -1747475740)

    def test0442(self):
        self.assertEquals(self.calculate(-9850484, -25386), -9825098)

    def test0443(self):
        self.assertEquals(self.calculate(1570838041, -8812), 1570846853)

    def test0444(self):
        self.assertEquals(self.calculate(-1273753513, -28815), -1273724698)

    def test0445(self):
        self.assertEquals(self.calculate(1930309020, 29718), 1930279302)

    def test0446(self):
        self.assertEquals(self.calculate(176765835, 4129), 176761706)

    def test0447(self):
        self.assertEquals(self.calculate(103108363, 24163), 103084200)

    def test0448(self):
        self.assertEquals(self.calculate(-1397575236, 13078), -1397588314)

    def test0449(self):
        self.assertEquals(self.calculate(208560268, 25972), 208534296)

    def test0450(self):
        self.assertEquals(self.calculate(207347715, 18662), 207329053)

    def test0451(self):
        self.assertEquals(self.calculate(-166205193, -13854), -166191339)

    def test0452(self):
        self.assertEquals(self.calculate(1586673499, 873), 1586672626)

    def test0453(self):
        self.assertEquals(self.calculate(11818785, -23662), 11842447)

    def test0454(self):
        self.assertEquals(self.calculate(-808485893, 22438), -808508331)

    def test0455(self):
        self.assertEquals(self.calculate(260290203, -24650), 260314853)

    def test0456(self):
        self.assertEquals(self.calculate(1294510719, -20972), 1294531691)

    def test0457(self):
        self.assertEquals(self.calculate(98485939, -29250), 98515189)

    def test0458(self):
        self.assertEquals(self.calculate(1185181329, -11377), 1185192706)

    def test0459(self):
        self.assertEquals(self.calculate(1599511239, 17813), 1599493426)

    def test0460(self):
        self.assertEquals(self.calculate(524075722, -26486), 524102208)

    def test0461(self):
        self.assertEquals(self.calculate(-1290786337, -16651), -1290769686)

    def test0462(self):
        self.assertEquals(self.calculate(-51200387, 12118), -51212505)

    def test0463(self):
        self.assertEquals(self.calculate(-791241321, -12779), -791228542)

    def test0464(self):
        self.assertEquals(self.calculate(1123783314, 11114), 1123772200)

    def test0465(self):
        self.assertEquals(self.calculate(347999445, 22725), 347976720)

    def test0466(self):
        self.assertEquals(self.calculate(1537088235, 27351), 1537060884)

    def test0467(self):
        self.assertEquals(self.calculate(2109996252, 3022), 2109993230)

    def test0468(self):
        self.assertEquals(self.calculate(307068530, -19799), 307088329)

    def test0469(self):
        self.assertEquals(self.calculate(-2064011389, -31826), -2063979563)

    def test0470(self):
        self.assertEquals(self.calculate(-1299394596, 15463), -1299410059)

    def test0471(self):
        self.assertEquals(self.calculate(-1020298731, 21757), -1020320488)

    def test0472(self):
        self.assertEquals(self.calculate(-715077991, 32573), -715110564)

    def test0473(self):
        self.assertEquals(self.calculate(-1992844893, 28855), -1992873748)

    def test0474(self):
        self.assertEquals(self.calculate(2017917975, -15278), 2017933253)

    def test0475(self):
        self.assertEquals(self.calculate(1542551867, -26872), 1542578739)

    def test0476(self):
        self.assertEquals(self.calculate(-1395976420, 19499), -1395995919)

    def test0477(self):
        self.assertEquals(self.calculate(2030216854, -12106), 2030228960)

    def test0478(self):
        self.assertEquals(self.calculate(-1371935816, 17476), -1371953292)

    def test0479(self):
        self.assertEquals(self.calculate(-630613003, -28631), -630584372)

    def test0480(self):
        self.assertEquals(self.calculate(-118017817, -26555), -117991262)

    def test0481(self):
        self.assertEquals(self.calculate(-784142264, -32681), -784109583)

    def test0482(self):
        self.assertEquals(self.calculate(-760248638, -20287), -760228351)

    def test0483(self):
        self.assertEquals(self.calculate(-1236621334, 25784), -1236647118)

    def test0484(self):
        self.assertEquals(self.calculate(-1791274292, 29039), -1791303331)

    def test0485(self):
        self.assertEquals(self.calculate(-1917580406, -20214), -1917560192)

    def test0486(self):
        self.assertEquals(self.calculate(-73470612, 14195), -73484807)

    def test0487(self):
        self.assertEquals(self.calculate(1716583204, 18660), 1716564544)

    def test0488(self):
        self.assertEquals(self.calculate(-263825345, -26945), -263798400)

    def test0489(self):
        self.assertEquals(self.calculate(-102780141, -10718), -102769423)

    def test0490(self):
        self.assertEquals(self.calculate(-1969527954, -487), -1969527467)

    def test0491(self):
        self.assertEquals(self.calculate(934176523, -16571), 934193094)

    def test0492(self):
        self.assertEquals(self.calculate(-1640055486, 27629), -1640083115)

    def test0493(self):
        self.assertEquals(self.calculate(79031903, 20267), 79011636)

    def test0494(self):
        self.assertEquals(self.calculate(-157812837, 26898), -157839735)

    def test0495(self):
        self.assertEquals(self.calculate(-337883503, -7803), -337875700)

    def test0496(self):
        self.assertEquals(self.calculate(1074729557, -11489), 1074741046)

    def test0497(self):
        self.assertEquals(self.calculate(1474089873, -3883), 1474093756)

    def test0498(self):
        self.assertEquals(self.calculate(815180105, 2708), 815177397)

    def test0499(self):
        self.assertEquals(self.calculate(-1736913644, 4), -1736913648)

    def test0500(self):
        self.assertEquals(self.calculate(2054157601, -9282), 2054166883)

    def test0501(self):
        self.assertEquals(self.calculate(614314416, 297), 614314119)

    def test0502(self):
        self.assertEquals(self.calculate(-179787357, 3186), -179790543)

    def test0503(self):
        self.assertEquals(self.calculate(-1613510909, 16959), -1613527868)

    def test0504(self):
        self.assertEquals(self.calculate(-1324657183, -1084), -1324656099)

    def test0505(self):
        self.assertEquals(self.calculate(-887820014, 22007), -887842021)

    def test0506(self):
        self.assertEquals(self.calculate(-511083699, -10475), -511073224)

    def test0507(self):
        self.assertEquals(self.calculate(-1660141928, 14691), -1660156619)

    def test0508(self):
        self.assertEquals(self.calculate(-371474596, -22877), -371451719)

    def test0509(self):
        self.assertEquals(self.calculate(-535682123, 24223), -535706346)

    def test0510(self):
        self.assertEquals(self.calculate(-2034649649, 10364), -2034660013)

    def test0511(self):
        self.assertEquals(self.calculate(1462643007, -9840), 1462652847)

    def test0512(self):
        self.assertEquals(self.calculate(593765229, -16), 593765245)

    def test0513(self):
        self.assertEquals(self.calculate(476031254, -20045), 476051299)

    def test0514(self):
        self.assertEquals(self.calculate(-1843436351, 28652), -1843465003)

    def test0515(self):
        self.assertEquals(self.calculate(-1988842466, -16170), -1988826296)

    def test0516(self):
        self.assertEquals(self.calculate(-1630408606, -4095), -1630404511)

    def test0517(self):
        self.assertEquals(self.calculate(944836319, 11164), 944825155)

    def test0518(self):
        self.assertEquals(self.calculate(-1946835723, -14504), -1946821219)

    def test0519(self):
        self.assertEquals(self.calculate(-1039412030, -15020), -1039397010)

    def test0520(self):
        self.assertEquals(self.calculate(520143033, 31994), 520111039)

    def test0521(self):
        self.assertEquals(self.calculate(-2072466069, -352), -2072465717)

    def test0522(self):
        self.assertEquals(self.calculate(1107284565, 10839), 1107273726)

    def test0523(self):
        self.assertEquals(self.calculate(1169841090, -4216), 1169845306)

    def test0524(self):
        self.assertEquals(self.calculate(-1222216869, -1905), -1222214964)

    def test0525(self):
        self.assertEquals(self.calculate(1702623501, -22566), 1702646067)

    def test0526(self):
        self.assertEquals(self.calculate(1904361602, -6973), 1904368575)

    def test0527(self):
        self.assertEquals(self.calculate(-600521392, 14516), -600535908)

    def test0528(self):
        self.assertEquals(self.calculate(1768549025, 10440), 1768538585)

    def test0529(self):
        self.assertEquals(self.calculate(-1681405732, -17724), -1681388008)

    def test0530(self):
        self.assertEquals(self.calculate(-909422792, -23673), -909399119)

    def test0531(self):
        self.assertEquals(self.calculate(-1466515672, -5641), -1466510031)

    def test0532(self):
        self.assertEquals(self.calculate(-496320834, -2544), -496318290)

    def test0533(self):
        self.assertEquals(self.calculate(-1607462243, 15651), -1607477894)

    def test0534(self):
        self.assertEquals(self.calculate(-1003995412, 32452), -1004027864)

    def test0535(self):
        self.assertEquals(self.calculate(-404139853, 22856), -404162709)

    def test0536(self):
        self.assertEquals(self.calculate(845997896, 18085), 845979811)

    def test0537(self):
        self.assertEquals(self.calculate(-1892172842, 5071), -1892177913)

    def test0538(self):
        self.assertEquals(self.calculate(-1766159132, 23255), -1766182387)

    def test0539(self):
        self.assertEquals(self.calculate(-250486353, -15282), -250471071)

    def test0540(self):
        self.assertEquals(self.calculate(1016802498, 25756), 1016776742)

    def test0541(self):
        self.assertEquals(self.calculate(-71427711, 11631), -71439342)

    def test0542(self):
        self.assertEquals(self.calculate(-1526081397, 4879), -1526086276)

    def test0543(self):
        self.assertEquals(self.calculate(-1871347365, 17001), -1871364366)

    def test0544(self):
        self.assertEquals(self.calculate(272597909, -23007), 272620916)

    def test0545(self):
        self.assertEquals(self.calculate(-2023613893, -13953), -2023599940)

    def test0546(self):
        self.assertEquals(self.calculate(1760097112, 21175), 1760075937)

    def test0547(self):
        self.assertEquals(self.calculate(1994860256, -29649), 1994889905)

    def test0548(self):
        self.assertEquals(self.calculate(1123170308, 5740), 1123164568)

    def test0549(self):
        self.assertEquals(self.calculate(1581828272, -20634), 1581848906)

    def test0550(self):
        self.assertEquals(self.calculate(1777889985, -14566), 1777904551)

    def test0551(self):
        self.assertEquals(self.calculate(-962539668, 4897), -962544565)

    def test0552(self):
        self.assertEquals(self.calculate(758624970, 10429), 758614541)

    def test0553(self):
        self.assertEquals(self.calculate(-2098137700, 31690), -2098169390)

    def test0554(self):
        self.assertEquals(self.calculate(547303769, 7256), 547296513)

    def test0555(self):
        self.assertEquals(self.calculate(776610695, 9823), 776600872)

    def test0556(self):
        self.assertEquals(self.calculate(-214222821, 1603), -214224424)

    def test0557(self):
        self.assertEquals(self.calculate(1525848598, -23900), 1525872498)

    def test0558(self):
        self.assertEquals(self.calculate(1607471829, -601), 1607472430)

    def test0559(self):
        self.assertEquals(self.calculate(594740018, -7219), 594747237)

    def test0560(self):
        self.assertEquals(self.calculate(313424304, 24451), 313399853)

    def test0561(self):
        self.assertEquals(self.calculate(-2053610911, -15842), -2053595069)

    def test0562(self):
        self.assertEquals(self.calculate(622414925, 19343), 622395582)

    def test0563(self):
        self.assertEquals(self.calculate(246423744, 20663), 246403081)

    def test0564(self):
        self.assertEquals(self.calculate(-1982326450, -32719), -1982293731)

    def test0565(self):
        self.assertEquals(self.calculate(-1162350542, 25233), -1162375775)

    def test0566(self):
        self.assertEquals(self.calculate(-73291813, -32183), -73259630)

    def test0567(self):
        self.assertEquals(self.calculate(1038620590, 31898), 1038588692)

    def test0568(self):
        self.assertEquals(self.calculate(-901640811, 14341), -901655152)

    def test0569(self):
        self.assertEquals(self.calculate(-672707654, 18132), -672725786)

    def test0570(self):
        self.assertEquals(self.calculate(-1983903495, 26412), -1983929907)

    def test0571(self):
        self.assertEquals(self.calculate(-1854761892, 4258), -1854766150)

    def test0572(self):
        self.assertEquals(self.calculate(1734781058, -17283), 1734798341)

    def test0573(self):
        self.assertEquals(self.calculate(666916778, -5778), 666922556)

    def test0574(self):
        self.assertEquals(self.calculate(930199273, -17688), 930216961)

    def test0575(self):
        self.assertEquals(self.calculate(-1961709713, 29752), -1961739465)

    def test0576(self):
        self.assertEquals(self.calculate(-879283646, -9137), -879274509)

    def test0577(self):
        self.assertEquals(self.calculate(1419203651, 8952), 1419194699)

    def test0578(self):
        self.assertEquals(self.calculate(-135687939, 20573), -135708512)

    def test0579(self):
        self.assertEquals(self.calculate(-305429622, -20688), -305408934)

    def test0580(self):
        self.assertEquals(self.calculate(-1092199992, 26211), -1092226203)

    def test0581(self):
        self.assertEquals(self.calculate(-380585306, 24008), -380609314)

    def test0582(self):
        self.assertEquals(self.calculate(402599150, 738), 402598412)

    def test0583(self):
        self.assertEquals(self.calculate(-695581007, -2695), -695578312)

    def test0584(self):
        self.assertEquals(self.calculate(1950774524, 26287), 1950748237)

    def test0585(self):
        self.assertEquals(self.calculate(1442178829, -705), 1442179534)

    def test0586(self):
        self.assertEquals(self.calculate(2053353024, 9377), 2053343647)

    def test0587(self):
        self.assertEquals(self.calculate(-446245356, -26466), -446218890)

    def test0588(self):
        self.assertEquals(self.calculate(1894242671, -24388), 1894267059)

    def test0589(self):
        self.assertEquals(self.calculate(-468608057, 8240), -468616297)

    def test0590(self):
        self.assertEquals(self.calculate(-750546947, 26306), -750573253)

    def test0591(self):
        self.assertEquals(self.calculate(-859478572, 30397), -859508969)

    def test0592(self):
        self.assertEquals(self.calculate(2104704512, -27891), 2104732403)

    def test0593(self):
        self.assertEquals(self.calculate(-336671353, -8585), -336662768)

    def test0594(self):
        self.assertEquals(self.calculate(1949067227, 2148), 1949065079)

    def test0595(self):
        self.assertEquals(self.calculate(-1551191000, -5420), -1551185580)

    def test0596(self):
        self.assertEquals(self.calculate(1732328014, -11783), 1732339797)

    def test0597(self):
        self.assertEquals(self.calculate(-1794126404, 31939), -1794158343)

    def test0598(self):
        self.assertEquals(self.calculate(-1719106659, -2604), -1719104055)

    def test0599(self):
        self.assertEquals(self.calculate(-507845851, 19673), -507865524)

    def test0600(self):
        self.assertEquals(self.calculate(865005048, -27785), 865032833)

    def test0601(self):
        self.assertEquals(self.calculate(-1046777319, -21681), -1046755638)

    def test0602(self):
        self.assertEquals(self.calculate(-82744918, -18152), -82726766)

    def test0603(self):
        self.assertEquals(self.calculate(1935349107, 27669), 1935321438)

    def test0604(self):
        self.assertEquals(self.calculate(-1530582422, 4317), -1530586739)

    def test0605(self):
        self.assertEquals(self.calculate(-1028064667, 20681), -1028085348)

    def test0606(self):
        self.assertEquals(self.calculate(1386295040, 10509), 1386284531)

    def test0607(self):
        self.assertEquals(self.calculate(2078732112, -22641), 2078754753)

    def test0608(self):
        self.assertEquals(self.calculate(134861808, 10635), 134851173)

    def test0609(self):
        self.assertEquals(self.calculate(1708695204, 22567), 1708672637)

    def test0610(self):
        self.assertEquals(self.calculate(-401765661, -19359), -401746302)

    def test0611(self):
        self.assertEquals(self.calculate(374370928, 139), 374370789)

    def test0612(self):
        self.assertEquals(self.calculate(1332996323, 25610), 1332970713)

    def test0613(self):
        self.assertEquals(self.calculate(1368914011, 3559), 1368910452)

    def test0614(self):
        self.assertEquals(self.calculate(-212737512, 2178), -212739690)

    def test0615(self):
        self.assertEquals(self.calculate(1325064929, 22823), 1325042106)

    def test0616(self):
        self.assertEquals(self.calculate(1138977446, -18138), 1138995584)

    def test0617(self):
        self.assertEquals(self.calculate(749107662, -2416), 749110078)

    def test0618(self):
        self.assertEquals(self.calculate(1073523310, -24395), 1073547705)

    def test0619(self):
        self.assertEquals(self.calculate(-1335479236, 4684), -1335483920)

    def test0620(self):
        self.assertEquals(self.calculate(-434916175, -5801), -434910374)

    def test0621(self):
        self.assertEquals(self.calculate(-111092527, 19867), -111112394)

    def test0622(self):
        self.assertEquals(self.calculate(1086700575, -24885), 1086725460)

    def test0623(self):
        self.assertEquals(self.calculate(496514210, 6340), 496507870)

    def test0624(self):
        self.assertEquals(self.calculate(382989349, 22522), 382966827)

    def test0625(self):
        self.assertEquals(self.calculate(1278832548, 27450), 1278805098)

    def test0626(self):
        self.assertEquals(self.calculate(1491123520, 19415), 1491104105)

    def test0627(self):
        self.assertEquals(self.calculate(-1152179901, -30199), -1152149702)

    def test0628(self):
        self.assertEquals(self.calculate(328224800, 23618), 328201182)

    def test0629(self):
        self.assertEquals(self.calculate(-793987170, 23798), -794010968)

    def test0630(self):
        self.assertEquals(self.calculate(-1606112056, -27796), -1606084260)

    def test0631(self):
        self.assertEquals(self.calculate(-1320508360, -5593), -1320502767)

    def test0632(self):
        self.assertEquals(self.calculate(161748166, 31060), 161717106)

    def test0633(self):
        self.assertEquals(self.calculate(-862579824, -10665), -862569159)

    def test0634(self):
        self.assertEquals(self.calculate(1361871777, 22127), 1361849650)

    def test0635(self):
        self.assertEquals(self.calculate(-564321, -6178), -558143)

    def test0636(self):
        self.assertEquals(self.calculate(-257629559, 16215), -257645774)

    def test0637(self):
        self.assertEquals(self.calculate(547039413, -21679), 547061092)

    def test0638(self):
        self.assertEquals(self.calculate(1731308702, -7287), 1731315989)

    def test0639(self):
        self.assertEquals(self.calculate(1493146874, -8844), 1493155718)

    def test0640(self):
        self.assertEquals(self.calculate(-1760655237, 21830), -1760677067)

    def test0641(self):
        self.assertEquals(self.calculate(-717140483, 7867), -717148350)

    def test0642(self):
        self.assertEquals(self.calculate(1011856491, -22511), 1011879002)

    def test0643(self):
        self.assertEquals(self.calculate(436830794, 29926), 436800868)

    def test0644(self):
        self.assertEquals(self.calculate(302312205, 12724), 302299481)

    def test0645(self):
        self.assertEquals(self.calculate(538349992, 17044), 538332948)

    def test0646(self):
        self.assertEquals(self.calculate(1278505126, -31491), 1278536617)

    def test0647(self):
        self.assertEquals(self.calculate(1230753344, 27849), 1230725495)

    def test0648(self):
        self.assertEquals(self.calculate(1272722539, -12693), 1272735232)

    def test0649(self):
        self.assertEquals(self.calculate(-1887938714, 8941), -1887947655)

    def test0650(self):
        self.assertEquals(self.calculate(1648213195, 10798), 1648202397)

    def test0651(self):
        self.assertEquals(self.calculate(-400545809, -16607), -400529202)

    def test0652(self):
        self.assertEquals(self.calculate(1716274333, 16088), 1716258245)

    def test0653(self):
        self.assertEquals(self.calculate(10560755, 9898), 10550857)

    def test0654(self):
        self.assertEquals(self.calculate(1769892540, 26345), 1769866195)

    def test0655(self):
        self.assertEquals(self.calculate(1013496312, -6305), 1013502617)

    def test0656(self):
        self.assertEquals(self.calculate(-1307055528, 6492), -1307062020)

    def test0657(self):
        self.assertEquals(self.calculate(-900981542, -31884), -900949658)

    def test0658(self):
        self.assertEquals(self.calculate(-786869730, 26126), -786895856)

    def test0659(self):
        self.assertEquals(self.calculate(183207995, -8222), 183216217)

    def test0660(self):
        self.assertEquals(self.calculate(-1755673651, -16358), -1755657293)

    def test0661(self):
        self.assertEquals(self.calculate(-504200641, -15204), -504185437)

    def test0662(self):
        self.assertEquals(self.calculate(1200891320, -3926), 1200895246)

    def test0663(self):
        self.assertEquals(self.calculate(592057976, -26249), 592084225)

    def test0664(self):
        self.assertEquals(self.calculate(-1521337419, 7958), -1521345377)

    def test0665(self):
        self.assertEquals(self.calculate(-249104386, -22298), -249082088)

    def test0666(self):
        self.assertEquals(self.calculate(554889638, 13051), 554876587)

    def test0667(self):
        self.assertEquals(self.calculate(1529972501, 4617), 1529967884)

    def test0668(self):
        self.assertEquals(self.calculate(-184701082, 3613), -184704695)

    def test0669(self):
        self.assertEquals(self.calculate(1424398500, -12989), 1424411489)

    def test0670(self):
        self.assertEquals(self.calculate(-1965306398, 15648), -1965322046)

    def test0671(self):
        self.assertEquals(self.calculate(289473690, 7264), 289466426)

    def test0672(self):
        self.assertEquals(self.calculate(-931275462, -16781), -931258681)

    def test0673(self):
        self.assertEquals(self.calculate(1112866636, 31143), 1112835493)

    def test0674(self):
        self.assertEquals(self.calculate(-1668437247, 24990), -1668462237)

    def test0675(self):
        self.assertEquals(self.calculate(113697117, 27389), 113669728)

    def test0676(self):
        self.assertEquals(self.calculate(280178159, 30629), 280147530)

    def test0677(self):
        self.assertEquals(self.calculate(265555786, 14351), 265541435)

    def test0678(self):
        self.assertEquals(self.calculate(-674440494, 26968), -674467462)

    def test0679(self):
        self.assertEquals(self.calculate(-2079503466, 12157), -2079515623)

    def test0680(self):
        self.assertEquals(self.calculate(-1031803546, -6426), -1031797120)

    def test0681(self):
        self.assertEquals(self.calculate(522340037, -23186), 522363223)

    def test0682(self):
        self.assertEquals(self.calculate(1701483569, 7992), 1701475577)

    def test0683(self):
        self.assertEquals(self.calculate(2094373751, 28095), 2094345656)

    def test0684(self):
        self.assertEquals(self.calculate(-1713536906, -9968), -1713526938)

    def test0685(self):
        self.assertEquals(self.calculate(-2007421584, 23563), -2007445147)

    def test0686(self):
        self.assertEquals(self.calculate(-588229501, -6570), -588222931)

    def test0687(self):
        self.assertEquals(self.calculate(-229095273, 25784), -229121057)

    def test0688(self):
        self.assertEquals(self.calculate(987436943, 30455), 987406488)

    def test0689(self):
        self.assertEquals(self.calculate(-1787912041, 22833), -1787934874)

    def test0690(self):
        self.assertEquals(self.calculate(-82835866, 27604), -82863470)

    def test0691(self):
        self.assertEquals(self.calculate(-1913048784, -13519), -1913035265)

    def test0692(self):
        self.assertEquals(self.calculate(-1813099775, -14361), -1813085414)

    def test0693(self):
        self.assertEquals(self.calculate(367797488, 31635), 367765853)

    def test0694(self):
        self.assertEquals(self.calculate(-1581295182, 11846), -1581307028)

    def test0695(self):
        self.assertEquals(self.calculate(-563554265, -31272), -563522993)

    def test0696(self):
        self.assertEquals(self.calculate(1352570290, -3279), 1352573569)

    def test0697(self):
        self.assertEquals(self.calculate(2099954734, 3291), 2099951443)

    def test0698(self):
        self.assertEquals(self.calculate(509393186, -18919), 509412105)

    def test0699(self):
        self.assertEquals(self.calculate(1372244666, 14376), 1372230290)

    def test0700(self):
        self.assertEquals(self.calculate(-996842851, -25008), -996817843)

    def test0701(self):
        self.assertEquals(self.calculate(871492197, 19260), 871472937)

    def test0702(self):
        self.assertEquals(self.calculate(-1768124406, 7448), -1768131854)

    def test0703(self):
        self.assertEquals(self.calculate(693097681, -25934), 693123615)

    def test0704(self):
        self.assertEquals(self.calculate(-674727450, -9824), -674717626)

    def test0705(self):
        self.assertEquals(self.calculate(1785054559, -16480), 1785071039)

    def test0706(self):
        self.assertEquals(self.calculate(175222069, 22398), 175199671)

    def test0707(self):
        self.assertEquals(self.calculate(-88633631, 19222), -88652853)

    def test0708(self):
        self.assertEquals(self.calculate(601741877, -5106), 601746983)

    def test0709(self):
        self.assertEquals(self.calculate(1425008609, 18089), 1424990520)

    def test0710(self):
        self.assertEquals(self.calculate(137434414, 23150), 137411264)

    def test0711(self):
        self.assertEquals(self.calculate(261254909, -9756), 261264665)

    def test0712(self):
        self.assertEquals(self.calculate(-1565933396, 16709), -1565950105)

    def test0713(self):
        self.assertEquals(self.calculate(2123099124, 13946), 2123085178)

    def test0714(self):
        self.assertEquals(self.calculate(1601361030, -832), 1601361862)

    def test0715(self):
        self.assertEquals(self.calculate(-532596882, 4240), -532601122)

    def test0716(self):
        self.assertEquals(self.calculate(-1166769276, 31797), -1166801073)

    def test0717(self):
        self.assertEquals(self.calculate(-996040124, -3222), -996036902)

    def test0718(self):
        self.assertEquals(self.calculate(-2115529276, -22952), -2115506324)

    def test0719(self):
        self.assertEquals(self.calculate(-492308722, 17869), -492326591)

    def test0720(self):
        self.assertEquals(self.calculate(-1802693679, 18965), -1802712644)

    def test0721(self):
        self.assertEquals(self.calculate(554404483, 20614), 554383869)

    def test0722(self):
        self.assertEquals(self.calculate(788470313, -23717), 788494030)

    def test0723(self):
        self.assertEquals(self.calculate(-1868714341, -21236), -1868693105)

    def test0724(self):
        self.assertEquals(self.calculate(1160473423, -16690), 1160490113)

    def test0725(self):
        self.assertEquals(self.calculate(-635065507, 21646), -635087153)

    def test0726(self):
        self.assertEquals(self.calculate(-692519676, 25087), -692544763)

    def test0727(self):
        self.assertEquals(self.calculate(-626243895, 25684), -626269579)

    def test0728(self):
        self.assertEquals(self.calculate(53565636, 14416), 53551220)

    def test0729(self):
        self.assertEquals(self.calculate(-1555810853, -23884), -1555786969)

    def test0730(self):
        self.assertEquals(self.calculate(1861083959, 31913), 1861052046)

    def test0731(self):
        self.assertEquals(self.calculate(1600146599, 23060), 1600123539)

    def test0732(self):
        self.assertEquals(self.calculate(19663587, -26119), 19689706)

    def test0733(self):
        self.assertEquals(self.calculate(-1800929552, 9844), -1800939396)

    def test0734(self):
        self.assertEquals(self.calculate(2000332376, 19479), 2000312897)

    def test0735(self):
        self.assertEquals(self.calculate(-258819521, 16865), -258836386)

    def test0736(self):
        self.assertEquals(self.calculate(-1756912946, -28761), -1756884185)

    def test0737(self):
        self.assertEquals(self.calculate(-491116329, 30826), -491147155)

    def test0738(self):
        self.assertEquals(self.calculate(1932721193, 3225), 1932717968)

    def test0739(self):
        self.assertEquals(self.calculate(300339146, 24217), 300314929)

    def test0740(self):
        self.assertEquals(self.calculate(-1944118765, 6116), -1944124881)

    def test0741(self):
        self.assertEquals(self.calculate(-1243250893, -25196), -1243225697)

    def test0742(self):
        self.assertEquals(self.calculate(1632824292, -11439), 1632835731)

    def test0743(self):
        self.assertEquals(self.calculate(1488798367, -23116), 1488821483)

    def test0744(self):
        self.assertEquals(self.calculate(-1138552499, 13270), -1138565769)

    def test0745(self):
        self.assertEquals(self.calculate(-261122855, 24411), -261147266)

    def test0746(self):
        self.assertEquals(self.calculate(-1448825437, -11769), -1448813668)

    def test0747(self):
        self.assertEquals(self.calculate(1245707611, 30255), 1245677356)

    def test0748(self):
        self.assertEquals(self.calculate(-2127151559, -8031), -2127143528)

    def test0749(self):
        self.assertEquals(self.calculate(450739295, 1070), 450738225)

    def test0750(self):
        self.assertEquals(self.calculate(-1984374799, 4471), -1984379270)

    def test0751(self):
        self.assertEquals(self.calculate(1081214736, 2377), 1081212359)

    def test0752(self):
        self.assertEquals(self.calculate(-80863631, 24998), -80888629)

    def test0753(self):
        self.assertEquals(self.calculate(70222211, 2566), 70219645)

    def test0754(self):
        self.assertEquals(self.calculate(1172506624, 9966), 1172496658)

    def test0755(self):
        self.assertEquals(self.calculate(1401748795, 972), 1401747823)

    def test0756(self):
        self.assertEquals(self.calculate(-877395929, -2167), -877393762)

    def test0757(self):
        self.assertEquals(self.calculate(-720289818, -5415), -720284403)

    def test0758(self):
        self.assertEquals(self.calculate(-1137772947, 11662), -1137784609)

    def test0759(self):
        self.assertEquals(self.calculate(-187225014, -26982), -187198032)

    def test0760(self):
        self.assertEquals(self.calculate(1391413812, 9414), 1391404398)

    def test0761(self):
        self.assertEquals(self.calculate(-458400425, -706), -458399719)

    def test0762(self):
        self.assertEquals(self.calculate(782928973, 28419), 782900554)

    def test0763(self):
        self.assertEquals(self.calculate(534048952, 31428), 534017524)

    def test0764(self):
        self.assertEquals(self.calculate(-457202711, -11942), -457190769)

    def test0765(self):
        self.assertEquals(self.calculate(-1420208163, -21102), -1420187061)

    def test0766(self):
        self.assertEquals(self.calculate(84658069, 26779), 84631290)

    def test0767(self):
        self.assertEquals(self.calculate(-128924337, -12942), -128911395)

    def test0768(self):
        self.assertEquals(self.calculate(-670231386, 2986), -670234372)

    def test0769(self):
        self.assertEquals(self.calculate(-346636849, -6217), -346630632)

    def test0770(self):
        self.assertEquals(self.calculate(1027622, -29528), 1057150)

    def test0771(self):
        self.assertEquals(self.calculate(-149889674, -27271), -149862403)

    def test0772(self):
        self.assertEquals(self.calculate(1865552182, 2870), 1865549312)

    def test0773(self):
        self.assertEquals(self.calculate(503004302, -3095), 503007397)

    def test0774(self):
        self.assertEquals(self.calculate(1107958608, 9052), 1107949556)

    def test0775(self):
        self.assertEquals(self.calculate(241621642, -1652), 241623294)

    def test0776(self):
        self.assertEquals(self.calculate(1065461211, 5889), 1065455322)

    def test0777(self):
        self.assertEquals(self.calculate(-835065763, -25920), -835039843)

    def test0778(self):
        self.assertEquals(self.calculate(1789754747, -31718), 1789786465)

    def test0779(self):
        self.assertEquals(self.calculate(-1136407824, -7086), -1136400738)

    def test0780(self):
        self.assertEquals(self.calculate(1857386204, -7320), 1857393524)

    def test0781(self):
        self.assertEquals(self.calculate(-1389112663, -2421), -1389110242)

    def test0782(self):
        self.assertEquals(self.calculate(-3308903, -4908), -3303995)

    def test0783(self):
        self.assertEquals(self.calculate(-41279436, 358), -41279794)

    def test0784(self):
        self.assertEquals(self.calculate(1112101790, -10149), 1112111939)

    def test0785(self):
        self.assertEquals(self.calculate(-2086210939, -2576), -2086208363)

    def test0786(self):
        self.assertEquals(self.calculate(44074357, 3553), 44070804)

    def test0787(self):
        self.assertEquals(self.calculate(1150302905, -20246), 1150323151)

    def test0788(self):
        self.assertEquals(self.calculate(314262485, 32293), 314230192)

    def test0789(self):
        self.assertEquals(self.calculate(1654817677, 22213), 1654795464)

    def test0790(self):
        self.assertEquals(self.calculate(-458358597, -20020), -458338577)

    def test0791(self):
        self.assertEquals(self.calculate(329068630, -16635), 329085265)

    def test0792(self):
        self.assertEquals(self.calculate(-1480095345, 21479), -1480116824)

    def test0793(self):
        self.assertEquals(self.calculate(1888361616, 27976), 1888333640)

    def test0794(self):
        self.assertEquals(self.calculate(176259934, -12155), 176272089)

    def test0795(self):
        self.assertEquals(self.calculate(534909337, 201), 534909136)

    def test0796(self):
        self.assertEquals(self.calculate(516681283, 4), 516681279)

    def test0797(self):
        self.assertEquals(self.calculate(675050163, 26167), 675023996)

    def test0798(self):
        self.assertEquals(self.calculate(-555165395, -9820), -555155575)

    def test0799(self):
        self.assertEquals(self.calculate(-1774347663, -21297), -1774326366)

    def test0800(self):
        self.assertEquals(self.calculate(-2097468201, 4938), -2097473139)

    def test0801(self):
        self.assertEquals(self.calculate(1248224663, 11477), 1248213186)

    def test0802(self):
        self.assertEquals(self.calculate(581673122, -23302), 581696424)

    def test0803(self):
        self.assertEquals(self.calculate(71188119, -17932), 71206051)

    def test0804(self):
        self.assertEquals(self.calculate(-592919253, 24646), -592943899)

    def test0805(self):
        self.assertEquals(self.calculate(-1028664432, 4948), -1028669380)

    def test0806(self):
        self.assertEquals(self.calculate(-1231257577, -4157), -1231253420)

    def test0807(self):
        self.assertEquals(self.calculate(-1844424927, -12106), -1844412821)

    def test0808(self):
        self.assertEquals(self.calculate(1145034168, 8005), 1145026163)

    def test0809(self):
        self.assertEquals(self.calculate(1006436438, -3039), 1006439477)

    def test0810(self):
        self.assertEquals(self.calculate(-846723106, 12197), -846735303)

    def test0811(self):
        self.assertEquals(self.calculate(-207439716, 16690), -207456406)

    def test0812(self):
        self.assertEquals(self.calculate(-1797445818, -29365), -1797416453)

    def test0813(self):
        self.assertEquals(self.calculate(-1594808520, 2393), -1594810913)

    def test0814(self):
        self.assertEquals(self.calculate(-1540651873, 5654), -1540657527)

    def test0815(self):
        self.assertEquals(self.calculate(-1046186268, 969), -1046187237)

    def test0816(self):
        self.assertEquals(self.calculate(-747483222, 4470), -747487692)

    def test0817(self):
        self.assertEquals(self.calculate(-465239400, 29816), -465269216)

    def test0818(self):
        self.assertEquals(self.calculate(1231742456, 5178), 1231737278)

    def test0819(self):
        self.assertEquals(self.calculate(-1408025195, -5206), -1408019989)

    def test0820(self):
        self.assertEquals(self.calculate(-156313977, 528), -156314505)

    def test0821(self):
        self.assertEquals(self.calculate(-1815891510, -31244), -1815860266)

    def test0822(self):
        self.assertEquals(self.calculate(-887607893, 21002), -887628895)

    def test0823(self):
        self.assertEquals(self.calculate(-1836107093, -21662), -1836085431)

    def test0824(self):
        self.assertEquals(self.calculate(135685632, -14083), 135699715)

    def test0825(self):
        self.assertEquals(self.calculate(748440400, 139), 748440261)

    def test0826(self):
        self.assertEquals(self.calculate(-937421045, -15375), -937405670)

    def test0827(self):
        self.assertEquals(self.calculate(-1469156888, 11004), -1469167892)

    def test0828(self):
        self.assertEquals(self.calculate(2058732892, -18736), 2058751628)

    def test0829(self):
        self.assertEquals(self.calculate(-1139195578, 18622), -1139214200)

    def test0830(self):
        self.assertEquals(self.calculate(-2077666859, -32372), -2077634487)

    def test0831(self):
        self.assertEquals(self.calculate(-1198181971, -17293), -1198164678)

    def test0832(self):
        self.assertEquals(self.calculate(352582224, -18415), 352600639)

    def test0833(self):
        self.assertEquals(self.calculate(-2018435462, -20405), -2018415057)

    def test0834(self):
        self.assertEquals(self.calculate(-1598988819, -21958), -1598966861)

    def test0835(self):
        self.assertEquals(self.calculate(1201666897, -27619), 1201694516)

    def test0836(self):
        self.assertEquals(self.calculate(2050738890, 18747), 2050720143)

    def test0837(self):
        self.assertEquals(self.calculate(1517765563, 17757), 1517747806)

    def test0838(self):
        self.assertEquals(self.calculate(-712831832, -7715), -712824117)

    def test0839(self):
        self.assertEquals(self.calculate(-2026775659, 31159), -2026806818)

    def test0840(self):
        self.assertEquals(self.calculate(-799132500, 4592), -799137092)

    def test0841(self):
        self.assertEquals(self.calculate(50833831, 22783), 50811048)

    def test0842(self):
        self.assertEquals(self.calculate(1506041956, 25039), 1506016917)

    def test0843(self):
        self.assertEquals(self.calculate(-222067601, 11864), -222079465)

    def test0844(self):
        self.assertEquals(self.calculate(-1626109565, -904), -1626108661)

    def test0845(self):
        self.assertEquals(self.calculate(-934447442, -18901), -934428541)

    def test0846(self):
        self.assertEquals(self.calculate(397671958, -17650), 397689608)

    def test0847(self):
        self.assertEquals(self.calculate(304016138, -32405), 304048543)

    def test0848(self):
        self.assertEquals(self.calculate(-919549137, 24421), -919573558)

    def test0849(self):
        self.assertEquals(self.calculate(-128039141, -31580), -128007561)

    def test0850(self):
        self.assertEquals(self.calculate(248096654, 12122), 248084532)

    def test0851(self):
        self.assertEquals(self.calculate(965505901, 13192), 965492709)

    def test0852(self):
        self.assertEquals(self.calculate(1953841730, 21149), 1953820581)

    def test0853(self):
        self.assertEquals(self.calculate(-384834916, -26894), -384808022)

    def test0854(self):
        self.assertEquals(self.calculate(-1447747437, 24277), -1447771714)

    def test0855(self):
        self.assertEquals(self.calculate(-725039278, 12562), -725051840)

    def test0856(self):
        self.assertEquals(self.calculate(1232223114, 19897), 1232203217)

    def test0857(self):
        self.assertEquals(self.calculate(-1675144829, -16616), -1675128213)

    def test0858(self):
        self.assertEquals(self.calculate(-1831379072, 251), -1831379323)

    def test0859(self):
        self.assertEquals(self.calculate(-1021151546, 12596), -1021164142)

    def test0860(self):
        self.assertEquals(self.calculate(644407127, -12453), 644419580)

    def test0861(self):
        self.assertEquals(self.calculate(161005799, -19901), 161025700)

    def test0862(self):
        self.assertEquals(self.calculate(1170996609, -22645), 1171019254)

    def test0863(self):
        self.assertEquals(self.calculate(1997297100, -29399), 1997326499)

    def test0864(self):
        self.assertEquals(self.calculate(-849519698, 31393), -849551091)

    def test0865(self):
        self.assertEquals(self.calculate(-1555755136, 3026), -1555758162)

    def test0866(self):
        self.assertEquals(self.calculate(700401640, -18101), 700419741)

    def test0867(self):
        self.assertEquals(self.calculate(-181415453, 5850), -181421303)

    def test0868(self):
        self.assertEquals(self.calculate(-462681949, -23705), -462658244)

    def test0869(self):
        self.assertEquals(self.calculate(-1144543038, 14284), -1144557322)

    def test0870(self):
        self.assertEquals(self.calculate(220454810, -27287), 220482097)

    def test0871(self):
        self.assertEquals(self.calculate(425841571, -30861), 425872432)

    def test0872(self):
        self.assertEquals(self.calculate(-264854235, 30297), -264884532)

    def test0873(self):
        self.assertEquals(self.calculate(911843097, 27104), 911815993)

    def test0874(self):
        self.assertEquals(self.calculate(-1992918255, -15355), -1992902900)

    def test0875(self):
        self.assertEquals(self.calculate(-802161935, 32035), -802193970)

    def test0876(self):
        self.assertEquals(self.calculate(-659944983, 6687), -659951670)

    def test0877(self):
        self.assertEquals(self.calculate(-1674406023, -20417), -1674385606)

    def test0878(self):
        self.assertEquals(self.calculate(159970828, 28165), 159942663)

    def test0879(self):
        self.assertEquals(self.calculate(-565619240, -13674), -565605566)

    def test0880(self):
        self.assertEquals(self.calculate(-1522605817, -13697), -1522592120)

    def test0881(self):
        self.assertEquals(self.calculate(-1778069626, -20634), -1778048992)

    def test0882(self):
        self.assertEquals(self.calculate(-1245040585, -20349), -1245020236)

    def test0883(self):
        self.assertEquals(self.calculate(-742727691, 30044), -742757735)

    def test0884(self):
        self.assertEquals(self.calculate(-113584021, 30811), -113614832)

    def test0885(self):
        self.assertEquals(self.calculate(-272820516, -14098), -272806418)

    def test0886(self):
        self.assertEquals(self.calculate(-1535790759, 30112), -1535820871)

    def test0887(self):
        self.assertEquals(self.calculate(432718583, 3741), 432714842)

    def test0888(self):
        self.assertEquals(self.calculate(1117274183, 14477), 1117259706)

    def test0889(self):
        self.assertEquals(self.calculate(-1698936661, -297), -1698936364)

    def test0890(self):
        self.assertEquals(self.calculate(-1630450433, -30130), -1630420303)

    def test0891(self):
        self.assertEquals(self.calculate(1328884454, 23855), 1328860599)

    def test0892(self):
        self.assertEquals(self.calculate(527819332, -28540), 527847872)

    def test0893(self):
        self.assertEquals(self.calculate(1505971418, 15029), 1505956389)

    def test0894(self):
        self.assertEquals(self.calculate(-1463949764, 17387), -1463967151)

    def test0895(self):
        self.assertEquals(self.calculate(-1544073397, 19612), -1544093009)

    def test0896(self):
        self.assertEquals(self.calculate(-1364202319, -26225), -1364176094)

    def test0897(self):
        self.assertEquals(self.calculate(1077365171, -29311), 1077394482)

    def test0898(self):
        self.assertEquals(self.calculate(1319226300, -3399), 1319229699)

    def test0899(self):
        self.assertEquals(self.calculate(-433055505, 6149), -433061654)

    def test0900(self):
        self.assertEquals(self.calculate(272913064, -16903), 272929967)

    def test0901(self):
        self.assertEquals(self.calculate(1953761809, -12067), 1953773876)

    def test0902(self):
        self.assertEquals(self.calculate(1274577935, -16276), 1274594211)

    def test0903(self):
        self.assertEquals(self.calculate(-1247838193, 24819), -1247863012)

    def test0904(self):
        self.assertEquals(self.calculate(1006179961, 5160), 1006174801)

    def test0905(self):
        self.assertEquals(self.calculate(1119294081, 13841), 1119280240)

    def test0906(self):
        self.assertEquals(self.calculate(2017068123, 21884), 2017046239)

    def test0907(self):
        self.assertEquals(self.calculate(-1301290982, -1729), -1301289253)

    def test0908(self):
        self.assertEquals(self.calculate(1440897899, 2012), 1440895887)

    def test0909(self):
        self.assertEquals(self.calculate(-682558926, -24758), -682534168)

    def test0910(self):
        self.assertEquals(self.calculate(-136461800, -9046), -136452754)

    def test0911(self):
        self.assertEquals(self.calculate(-809316313, -6304), -809310009)

    def test0912(self):
        self.assertEquals(self.calculate(-1032232176, 11917), -1032244093)

    def test0913(self):
        self.assertEquals(self.calculate(-1449662818, 5577), -1449668395)

    def test0914(self):
        self.assertEquals(self.calculate(-1587567631, 17900), -1587585531)

    def test0915(self):
        self.assertEquals(self.calculate(-1368445106, -18099), -1368427007)

    def test0916(self):
        self.assertEquals(self.calculate(2066472122, 31553), 2066440569)

    def test0917(self):
        self.assertEquals(self.calculate(1971556979, -9432), 1971566411)

    def test0918(self):
        self.assertEquals(self.calculate(-1899999404, -30227), -1899969177)

    def test0919(self):
        self.assertEquals(self.calculate(1528619656, -15755), 1528635411)

    def test0920(self):
        self.assertEquals(self.calculate(1301415829, 9935), 1301405894)

    def test0921(self):
        self.assertEquals(self.calculate(-1715334278, -30999), -1715303279)

    def test0922(self):
        self.assertEquals(self.calculate(1222394868, 10674), 1222384194)

    def test0923(self):
        self.assertEquals(self.calculate(-1033693092, 21878), -1033714970)

    def test0924(self):
        self.assertEquals(self.calculate(-1881347637, -6716), -1881340921)

    def test0925(self):
        self.assertEquals(self.calculate(-822019614, 7705), -822027319)

    def test0926(self):
        self.assertEquals(self.calculate(-13894284, -26727), -13867557)

    def test0927(self):
        self.assertEquals(self.calculate(-604845158, 26875), -604872033)

    def test0928(self):
        self.assertEquals(self.calculate(2020665639, 5937), 2020659702)

    def test0929(self):
        self.assertEquals(self.calculate(-783091586, -12178), -783079408)

    def test0930(self):
        self.assertEquals(self.calculate(-1530817289, -9555), -1530807734)

    def test0931(self):
        self.assertEquals(self.calculate(-1423760517, 4800), -1423765317)

    def test0932(self):
        self.assertEquals(self.calculate(-1781609809, 1936), -1781611745)

    def test0933(self):
        self.assertEquals(self.calculate(1057755334, 20684), 1057734650)

    def test0934(self):
        self.assertEquals(self.calculate(-831898676, 17902), -831916578)

    def test0935(self):
        self.assertEquals(self.calculate(-1113524867, 31088), -1113555955)

    def test0936(self):
        self.assertEquals(self.calculate(771556476, 2832), 771553644)

    def test0937(self):
        self.assertEquals(self.calculate(1305973501, -6551), 1305980052)

    def test0938(self):
        self.assertEquals(self.calculate(1244897222, 21818), 1244875404)

    def test0939(self):
        self.assertEquals(self.calculate(-1170625906, -5777), -1170620129)

    def test0940(self):
        self.assertEquals(self.calculate(-1175672919, -9335), -1175663584)

    def test0941(self):
        self.assertEquals(self.calculate(-267783449, 26161), -267809610)

    def test0942(self):
        self.assertEquals(self.calculate(379557351, -6049), 379563400)

    def test0943(self):
        self.assertEquals(self.calculate(-1781004191, 25670), -1781029861)

    def test0944(self):
        self.assertEquals(self.calculate(124789200, 10937), 124778263)

    def test0945(self):
        self.assertEquals(self.calculate(227731056, 5695), 227725361)

    def test0946(self):
        self.assertEquals(self.calculate(217690991, 15569), 217675422)

    def test0947(self):
        self.assertEquals(self.calculate(1170174112, -19102), 1170193214)

    def test0948(self):
        self.assertEquals(self.calculate(1569011849, 27485), 1568984364)

    def test0949(self):
        self.assertEquals(self.calculate(2033937008, -31622), 2033968630)

    def test0950(self):
        self.assertEquals(self.calculate(1527567928, 5485), 1527562443)

    def test0951(self):
        self.assertEquals(self.calculate(474412276, 15831), 474396445)

    def test0952(self):
        self.assertEquals(self.calculate(-33552176, -14165), -33538011)

    def test0953(self):
        self.assertEquals(self.calculate(-1016965319, -29262), -1016936057)

    def test0954(self):
        self.assertEquals(self.calculate(1601541124, -26187), 1601567311)

    def test0955(self):
        self.assertEquals(self.calculate(-1293424519, -28296), -1293396223)

    def test0956(self):
        self.assertEquals(self.calculate(-59001994, 21714), -59023708)

    def test0957(self):
        self.assertEquals(self.calculate(-723398727, 21253), -723419980)

    def test0958(self):
        self.assertEquals(self.calculate(2033544904, -252), 2033545156)

    def test0959(self):
        self.assertEquals(self.calculate(-1668508469, -28001), -1668480468)

    def test0960(self):
        self.assertEquals(self.calculate(1803760317, 2247), 1803758070)

    def test0961(self):
        self.assertEquals(self.calculate(-611332804, 7209), -611340013)

    def test0962(self):
        self.assertEquals(self.calculate(-1110037483, 15053), -1110052536)

    def test0963(self):
        self.assertEquals(self.calculate(-2020285833, 13325), -2020299158)

    def test0964(self):
        self.assertEquals(self.calculate(-1974874441, 16629), -1974891070)

    def test0965(self):
        self.assertEquals(self.calculate(-397749540, -18493), -397731047)

    def test0966(self):
        self.assertEquals(self.calculate(-104877211, -19697), -104857514)

    def test0967(self):
        self.assertEquals(self.calculate(-229935211, -31531), -229903680)

    def test0968(self):
        self.assertEquals(self.calculate(-704630524, -13521), -704617003)

    def test0969(self):
        self.assertEquals(self.calculate(186795683, 9678), 186786005)

    def test0970(self):
        self.assertEquals(self.calculate(1609558654, -24991), 1609583645)

    def test0971(self):
        self.assertEquals(self.calculate(361407812, 28100), 361379712)

    def test0972(self):
        self.assertEquals(self.calculate(-758020932, 29016), -758049948)

    def test0973(self):
        self.assertEquals(self.calculate(1348106495, 24177), 1348082318)

    def test0974(self):
        self.assertEquals(self.calculate(-1622426995, -16267), -1622410728)

    def test0975(self):
        self.assertEquals(self.calculate(2145126387, 5147), 2145121240)

    def test0976(self):
        self.assertEquals(self.calculate(1645074404, 10006), 1645064398)

    def test0977(self):
        self.assertEquals(self.calculate(2141137831, 28334), 2141109497)

    def test0978(self):
        self.assertEquals(self.calculate(1380555891, -9350), 1380565241)

    def test0979(self):
        self.assertEquals(self.calculate(-1736657685, -9407), -1736648278)

    def test0980(self):
        self.assertEquals(self.calculate(1843835621, -21742), 1843857363)

    def test0981(self):
        self.assertEquals(self.calculate(1345504269, -18061), 1345522330)

    def test0982(self):
        self.assertEquals(self.calculate(239894200, 16201), 239877999)

    def test0983(self):
        self.assertEquals(self.calculate(699972495, 28611), 699943884)

    def test0984(self):
        self.assertEquals(self.calculate(1524775246, -28166), 1524803412)

    def test0985(self):
        self.assertEquals(self.calculate(-179413463, 5106), -179418569)

    def test0986(self):
        self.assertEquals(self.calculate(-1644223201, 30494), -1644253695)

    def test0987(self):
        self.assertEquals(self.calculate(-1876288221, 14557), -1876302778)

    def test0988(self):
        self.assertEquals(self.calculate(-1657883002, -139), -1657882863)

    def test0989(self):
        self.assertEquals(self.calculate(-410855797, -3786), -410852011)

    def test0990(self):
        self.assertEquals(self.calculate(2058860833, -4355), 2058865188)

    def test0991(self):
        self.assertEquals(self.calculate(-1560461639, 24597), -1560486236)

    def test0992(self):
        self.assertEquals(self.calculate(2031499451, -14008), 2031513459)

    def test0993(self):
        self.assertEquals(self.calculate(106270683, 27160), 106243523)

    def test0994(self):
        self.assertEquals(self.calculate(-2132178833, -31213), -2132147620)

    def test0995(self):
        self.assertEquals(self.calculate(-966114410, 31761), -966146171)

    def test0996(self):
        self.assertEquals(self.calculate(186045859, 5206), 186040653)

    def test0997(self):
        self.assertEquals(self.calculate(-341441379, -22472), -341418907)

    def test0998(self):
        self.assertEquals(self.calculate(724224148, 7301), 724216847)

    def test0999(self):
        self.assertEquals(self.calculate(-949611145, -16549), -949594596)

    def test1000(self):
        self.assertEquals(self.calculate(1104761326, -30731), 1104792057)

    def test1001(self):
        self.assertEquals(self.calculate(259377376, -19518), 259396894)

    def test1002(self):
        self.assertEquals(self.calculate(1091560630, -9901), 1091570531)

    def test1003(self):
        self.assertEquals(self.calculate(1786012826, -25698), 1786038524)

    def test1004(self):
        self.assertEquals(self.calculate(1320109700, -2775), 1320112475)

    def test1005(self):
        self.assertEquals(self.calculate(-1227496124, -32168), -1227463956)

    def test1006(self):
        self.assertEquals(self.calculate(1290375979, 5526), 1290370453)

    def test1007(self):
        self.assertEquals(self.calculate(6373341, -31864), 6405205)

    def test1008(self):
        self.assertEquals(self.calculate(-1309185695, 22910), -1309208605)

    def test1009(self):
        self.assertEquals(self.calculate(-1912837223, 31306), -1912868529)

    def test1010(self):
        self.assertEquals(self.calculate(1150255798, -29809), 1150285607)

    def test1011(self):
        self.assertEquals(self.calculate(783923293, 29913), 783893380)

    def test1012(self):
        self.assertEquals(self.calculate(407313406, 5961), 407307445)

    def test1013(self):
        self.assertEquals(self.calculate(664565156, 2588), 664562568)

    def test1014(self):
        self.assertEquals(self.calculate(1606389135, 4552), 1606384583)

    def test1015(self):
        self.assertEquals(self.calculate(376780264, 17193), 376763071)

    def test1016(self):
        self.assertEquals(self.calculate(2145097839, -3640), 2145101479)

    def test1017(self):
        self.assertEquals(self.calculate(-1712247660, 16554), -1712264214)

    def test1018(self):
        self.assertEquals(self.calculate(-1515936517, -25932), -1515910585)

    def test1019(self):
        self.assertEquals(self.calculate(-898796755, 3107), -898799862)

    def test1020(self):
        self.assertEquals(self.calculate(346293201, -32216), 346325417)

    def test1021(self):
        self.assertEquals(self.calculate(1624142530, -24743), 1624167273)

    def test1022(self):
        self.assertEquals(self.calculate(-1465294347, -2508), -1465291839)

    def test1023(self):
        self.assertEquals(self.calculate(1043279635, -7771), 1043287406)




class TestVM_Sub_LongLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushL(rhs)
        v.VM_Sub()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-1683730384, 779374804), 1831862108)

    def test0001(self):
        self.assertEquals(self.calculate(10013296, 14515481), -4502185)

    def test0002(self):
        self.assertEquals(self.calculate(-448234249, -681842781), 233608532)

    def test0003(self):
        self.assertEquals(self.calculate(-1136701827, 1071196830), 2087068639)

    def test0004(self):
        self.assertEquals(self.calculate(2146185962, -1950217241), -198564093)

    def test0005(self):
        self.assertEquals(self.calculate(-1486827186, -183185917), -1303641269)

    def test0006(self):
        self.assertEquals(self.calculate(-1342743352, 1795646368), 1156577576)

    def test0007(self):
        self.assertEquals(self.calculate(-11568014, -1929093251), 1917525237)

    def test0008(self):
        self.assertEquals(self.calculate(976085670, 838419947), 137665723)

    def test0009(self):
        self.assertEquals(self.calculate(1683636344, 1629313803), 54322541)

    def test0010(self):
        self.assertEquals(self.calculate(-1252560221, 703109201), -1955669422)

    def test0011(self):
        self.assertEquals(self.calculate(-1032692462, -1012145189), -20547273)

    def test0012(self):
        self.assertEquals(self.calculate(-1149111327, -2016548402), 867437075)

    def test0013(self):
        self.assertEquals(self.calculate(-760185104, 257522776), -1017707880)

    def test0014(self):
        self.assertEquals(self.calculate(-1632718450, 1913801777), 748447069)

    def test0015(self):
        self.assertEquals(self.calculate(-499263800, -1031986552), 532722752)

    def test0016(self):
        self.assertEquals(self.calculate(-775593664, -1338748506), 563154842)

    def test0017(self):
        self.assertEquals(self.calculate(508265754, 2026115216), -1517849462)

    def test0018(self):
        self.assertEquals(self.calculate(1357888690, -2078785674), -858292932)

    def test0019(self):
        self.assertEquals(self.calculate(598149293, 866219025), -268069732)

    def test0020(self):
        self.assertEquals(self.calculate(1237956468, -863071944), 2101028412)

    def test0021(self):
        self.assertEquals(self.calculate(580620041, 1729727270), -1149107229)

    def test0022(self):
        self.assertEquals(self.calculate(204427838, -1105815929), 1310243767)

    def test0023(self):
        self.assertEquals(self.calculate(-199178383, 1651554874), -1850733257)

    def test0024(self):
        self.assertEquals(self.calculate(471159378, -1817187786), -2006620132)

    def test0025(self):
        self.assertEquals(self.calculate(-1019839716, 888300896), -1908140612)

    def test0026(self):
        self.assertEquals(self.calculate(1133386458, 2046115050), -912728592)

    def test0027(self):
        self.assertEquals(self.calculate(-821008040, -1094932590), 273924550)

    def test0028(self):
        self.assertEquals(self.calculate(85411791, -1903353400), 1988765191)

    def test0029(self):
        self.assertEquals(self.calculate(-1753754884, 406140325), 2135072087)

    def test0030(self):
        self.assertEquals(self.calculate(-1070472007, 945053169), -2015525176)

    def test0031(self):
        self.assertEquals(self.calculate(1571969599, -956077388), -1766920309)

    def test0032(self):
        self.assertEquals(self.calculate(908798809, -2083741057), -1302427430)

    def test0033(self):
        self.assertEquals(self.calculate(814329747, -898536174), 1712865921)

    def test0034(self):
        self.assertEquals(self.calculate(45077405, 875216944), -830139539)

    def test0035(self):
        self.assertEquals(self.calculate(1571739247, 269367143), 1302372104)

    def test0036(self):
        self.assertEquals(self.calculate(-825599187, -1596000860), 770401673)

    def test0037(self):
        self.assertEquals(self.calculate(-1998999126, 466601997), 1829366173)

    def test0038(self):
        self.assertEquals(self.calculate(1436613850, -165470330), 1602084180)

    def test0039(self):
        self.assertEquals(self.calculate(-512509244, -856430564), 343921320)

    def test0040(self):
        self.assertEquals(self.calculate(1527020197, -2079104710), -688842389)

    def test0041(self):
        self.assertEquals(self.calculate(471739291, -472098503), 943837794)

    def test0042(self):
        self.assertEquals(self.calculate(-1802507430, -773687877), -1028819553)

    def test0043(self):
        self.assertEquals(self.calculate(1838530980, 144577334), 1693953646)

    def test0044(self):
        self.assertEquals(self.calculate(503485587, -739592418), 1243078005)

    def test0045(self):
        self.assertEquals(self.calculate(2139078237, -931080324), -1224808735)

    def test0046(self):
        self.assertEquals(self.calculate(-431207678, 1198637024), -1629844702)

    def test0047(self):
        self.assertEquals(self.calculate(890035301, 576729295), 313306006)

    def test0048(self):
        self.assertEquals(self.calculate(-1784526853, -270545575), -1513981278)

    def test0049(self):
        self.assertEquals(self.calculate(649051346, 130422576), 518628770)

    def test0050(self):
        self.assertEquals(self.calculate(65184977, 119164396), -53979419)

    def test0051(self):
        self.assertEquals(self.calculate(1630457921, 1313308502), 317149419)

    def test0052(self):
        self.assertEquals(self.calculate(-969090962, -1403426422), 434335460)

    def test0053(self):
        self.assertEquals(self.calculate(-653714573, 1772903061), 1868349662)

    def test0054(self):
        self.assertEquals(self.calculate(83896347, 1180916679), -1097020332)

    def test0055(self):
        self.assertEquals(self.calculate(-1613320610, -47104442), -1566216168)

    def test0056(self):
        self.assertEquals(self.calculate(1973701030, 1140109339), 833591691)

    def test0057(self):
        self.assertEquals(self.calculate(-1765754703, -473185010), -1292569693)

    def test0058(self):
        self.assertEquals(self.calculate(-40164530, 1761111634), -1801276164)

    def test0059(self):
        self.assertEquals(self.calculate(1881258822, -1266461037), -1147247437)

    def test0060(self):
        self.assertEquals(self.calculate(-1609421973, 898330707), 1787214616)

    def test0061(self):
        self.assertEquals(self.calculate(-1323138249, -1678926077), 355787828)

    def test0062(self):
        self.assertEquals(self.calculate(-344722577, -1531433937), 1186711360)

    def test0063(self):
        self.assertEquals(self.calculate(-157603109, -190784752), 33181643)

    def test0064(self):
        self.assertEquals(self.calculate(-936984763, 1136801025), -2073785788)

    def test0065(self):
        self.assertEquals(self.calculate(-808922996, -366399123), -442523873)

    def test0066(self):
        self.assertEquals(self.calculate(542988572, 1354320080), -811331508)

    def test0067(self):
        self.assertEquals(self.calculate(-505155454, -1880098694), 1374943240)

    def test0068(self):
        self.assertEquals(self.calculate(2129341813, 1499820765), 629521048)

    def test0069(self):
        self.assertEquals(self.calculate(488605784, -1373838012), 1862443796)

    def test0070(self):
        self.assertEquals(self.calculate(-1871680436, -1887437762), 15757326)

    def test0071(self):
        self.assertEquals(self.calculate(686946823, -588456076), 1275402899)

    def test0072(self):
        self.assertEquals(self.calculate(-671923426, -230594630), -441328796)

    def test0073(self):
        self.assertEquals(self.calculate(1062269196, -1650248054), -1582450046)

    def test0074(self):
        self.assertEquals(self.calculate(12111182, -342566790), 354677972)

    def test0075(self):
        self.assertEquals(self.calculate(-1604129611, 1103142560), 1587695125)

    def test0076(self):
        self.assertEquals(self.calculate(-1217784939, -474482306), -743302633)

    def test0077(self):
        self.assertEquals(self.calculate(2087799005, 704454335), 1383344670)

    def test0078(self):
        self.assertEquals(self.calculate(-491423603, -970599313), 479175710)

    def test0079(self):
        self.assertEquals(self.calculate(1557874660, 563856219), 994018441)

    def test0080(self):
        self.assertEquals(self.calculate(-1124206230, -113955115), -1010251115)

    def test0081(self):
        self.assertEquals(self.calculate(-875222160, -1024541670), 149319510)

    def test0082(self):
        self.assertEquals(self.calculate(-2020431873, 655754941), 1618780482)

    def test0083(self):
        self.assertEquals(self.calculate(669796694, -862601606), 1532398300)

    def test0084(self):
        self.assertEquals(self.calculate(1616491090, -43479764), 1659970854)

    def test0085(self):
        self.assertEquals(self.calculate(1282094833, 602520139), 679574694)

    def test0086(self):
        self.assertEquals(self.calculate(-158034313, -8017674), -150016639)

    def test0087(self):
        self.assertEquals(self.calculate(-875882526, 1440171488), 1978913282)

    def test0088(self):
        self.assertEquals(self.calculate(-395806677, -1230941336), 835134659)

    def test0089(self):
        self.assertEquals(self.calculate(1548478815, -1921378002), -825110479)

    def test0090(self):
        self.assertEquals(self.calculate(-1039690269, 1849137885), 1406139142)

    def test0091(self):
        self.assertEquals(self.calculate(976166863, -1305760524), -2013039909)

    def test0092(self):
        self.assertEquals(self.calculate(707452428, 1947076253), -1239623825)

    def test0093(self):
        self.assertEquals(self.calculate(397368438, 1732846090), -1335477652)

    def test0094(self):
        self.assertEquals(self.calculate(-903553809, -375037064), -528516745)

    def test0095(self):
        self.assertEquals(self.calculate(-1394287309, 1660090995), 1240588992)

    def test0096(self):
        self.assertEquals(self.calculate(2051672143, 493285376), 1558386767)

    def test0097(self):
        self.assertEquals(self.calculate(-1152761492, 72504389), -1225265881)

    def test0098(self):
        self.assertEquals(self.calculate(909741660, -1847606120), -1537619516)

    def test0099(self):
        self.assertEquals(self.calculate(-22508510, 2079726594), -2102235104)

    def test0100(self):
        self.assertEquals(self.calculate(1487580481, -1217275010), -1590111805)

    def test0101(self):
        self.assertEquals(self.calculate(1587925749, -959850373), -1747191174)

    def test0102(self):
        self.assertEquals(self.calculate(-238957606, -895232671), 656275065)

    def test0103(self):
        self.assertEquals(self.calculate(-1141310350, -889245554), -252064796)

    def test0104(self):
        self.assertEquals(self.calculate(-1800895359, 519320082), 1974751855)

    def test0105(self):
        self.assertEquals(self.calculate(692150104, -1984065516), -1618751676)

    def test0106(self):
        self.assertEquals(self.calculate(1648536858, 1027623723), 620913135)

    def test0107(self):
        self.assertEquals(self.calculate(1628593457, -1922933188), -743440651)

    def test0108(self):
        self.assertEquals(self.calculate(-521679622, -742456335), 220776713)

    def test0109(self):
        self.assertEquals(self.calculate(208000900, 246679073), -38678173)

    def test0110(self):
        self.assertEquals(self.calculate(-754709674, 1374252029), -2128961703)

    def test0111(self):
        self.assertEquals(self.calculate(-41117908, -163581427), 122463519)

    def test0112(self):
        self.assertEquals(self.calculate(-1277483734, 2101127774), 916355788)

    def test0113(self):
        self.assertEquals(self.calculate(-794584335, -960706114), 166121779)

    def test0114(self):
        self.assertEquals(self.calculate(730900229, -82202476), 813102705)

    def test0115(self):
        self.assertEquals(self.calculate(1807567024, 14557358), 1793009666)

    def test0116(self):
        self.assertEquals(self.calculate(1457533066, -301424883), 1758957949)

    def test0117(self):
        self.assertEquals(self.calculate(1403171928, 1282139777), 121032151)

    def test0118(self):
        self.assertEquals(self.calculate(-2126994024, -1205692704), -921301320)

    def test0119(self):
        self.assertEquals(self.calculate(-62997001, -1869698703), 1806701702)

    def test0120(self):
        self.assertEquals(self.calculate(1442844802, -1417354945), -1434767549)

    def test0121(self):
        self.assertEquals(self.calculate(-1302236682, 1509176791), 1483553823)

    def test0122(self):
        self.assertEquals(self.calculate(-2022907355, -631142526), -1391764829)

    def test0123(self):
        self.assertEquals(self.calculate(356295134, 2082268990), -1725973856)

    def test0124(self):
        self.assertEquals(self.calculate(1271461755, -1252338907), -1771166634)

    def test0125(self):
        self.assertEquals(self.calculate(-693310864, 2097908399), 1503748033)

    def test0126(self):
        self.assertEquals(self.calculate(-688485713, 2141990808), 1464490775)

    def test0127(self):
        self.assertEquals(self.calculate(-210527403, -865194997), 654667594)

    def test0128(self):
        self.assertEquals(self.calculate(-2075117159, 474499004), 1745351133)

    def test0129(self):
        self.assertEquals(self.calculate(246150863, 1095064648), -848913785)

    def test0130(self):
        self.assertEquals(self.calculate(1923187042, -1563915205), -807865049)

    def test0131(self):
        self.assertEquals(self.calculate(449899673, 1605455950), -1155556277)

    def test0132(self):
        self.assertEquals(self.calculate(1375851362, -242326260), 1618177622)

    def test0133(self):
        self.assertEquals(self.calculate(-1493962055, -1994119174), 500157119)

    def test0134(self):
        self.assertEquals(self.calculate(292167542, -1215031507), 1507199049)

    def test0135(self):
        self.assertEquals(self.calculate(948871925, 123384008), 825487917)

    def test0136(self):
        self.assertEquals(self.calculate(-1166979577, 1851980336), 1276007383)

    def test0137(self):
        self.assertEquals(self.calculate(1633057181, 1745942824), -112885643)

    def test0138(self):
        self.assertEquals(self.calculate(-1053441669, -152324535), -901117134)

    def test0139(self):
        self.assertEquals(self.calculate(-925647937, -1516355947), 590708010)

    def test0140(self):
        self.assertEquals(self.calculate(-1994502781, -675855330), -1318647451)

    def test0141(self):
        self.assertEquals(self.calculate(-1399602897, -287792932), -1111809965)

    def test0142(self):
        self.assertEquals(self.calculate(1847675379, -784730037), -1662561880)

    def test0143(self):
        self.assertEquals(self.calculate(602999343, 1152458522), -549459179)

    def test0144(self):
        self.assertEquals(self.calculate(2119655573, 1817843435), 301812138)

    def test0145(self):
        self.assertEquals(self.calculate(917752577, -2086412426), -1290802293)

    def test0146(self):
        self.assertEquals(self.calculate(-169043314, -1162422271), 993378957)

    def test0147(self):
        self.assertEquals(self.calculate(70344058, -634545643), 704889701)

    def test0148(self):
        self.assertEquals(self.calculate(1403446500, -191740237), 1595186737)

    def test0149(self):
        self.assertEquals(self.calculate(1625279492, 1522634551), 102644941)

    def test0150(self):
        self.assertEquals(self.calculate(-1517571722, -876302838), -641268884)

    def test0151(self):
        self.assertEquals(self.calculate(719821844, -1588883211), -1986262241)

    def test0152(self):
        self.assertEquals(self.calculate(-1302910599, -1419909843), 116999244)

    def test0153(self):
        self.assertEquals(self.calculate(675138581, 69361737), 605776844)

    def test0154(self):
        self.assertEquals(self.calculate(375664181, -405427521), 781091702)

    def test0155(self):
        self.assertEquals(self.calculate(-1136496078, -1491112106), 354616028)

    def test0156(self):
        self.assertEquals(self.calculate(-409930280, 1345513720), -1755444000)

    def test0157(self):
        self.assertEquals(self.calculate(391235876, -524396782), 915632658)

    def test0158(self):
        self.assertEquals(self.calculate(-2090581259, 421233525), 1783152512)

    def test0159(self):
        self.assertEquals(self.calculate(47237298, -1194497527), 1241734825)

    def test0160(self):
        self.assertEquals(self.calculate(2003389990, -1966848262), -324729044)

    def test0161(self):
        self.assertEquals(self.calculate(-207754724, -609073253), 401318529)

    def test0162(self):
        self.assertEquals(self.calculate(826948175, -169100237), 996048412)

    def test0163(self):
        self.assertEquals(self.calculate(917629820, -1204793654), 2122423474)

    def test0164(self):
        self.assertEquals(self.calculate(-1909459915, 251509493), 2133997888)

    def test0165(self):
        self.assertEquals(self.calculate(1509487644, -2133590588), -651889064)

    def test0166(self):
        self.assertEquals(self.calculate(1871425230, 660385408), 1211039822)

    def test0167(self):
        self.assertEquals(self.calculate(1847786064, 2056228043), -208441979)

    def test0168(self):
        self.assertEquals(self.calculate(883325520, -1857156839), -1554484937)

    def test0169(self):
        self.assertEquals(self.calculate(-1001280458, -1248613059), 247332601)

    def test0170(self):
        self.assertEquals(self.calculate(-822828714, -238530424), -584298290)

    def test0171(self):
        self.assertEquals(self.calculate(2004605911, -1346252283), -944109102)

    def test0172(self):
        self.assertEquals(self.calculate(79407223, 682587586), -603180363)

    def test0173(self):
        self.assertEquals(self.calculate(-97378589, 1297494958), -1394873547)

    def test0174(self):
        self.assertEquals(self.calculate(-2013619847, 1836204172), 445143277)

    def test0175(self):
        self.assertEquals(self.calculate(-1493176254, 1709282577), 1092508465)

    def test0176(self):
        self.assertEquals(self.calculate(1074317509, -2106481593), -1114168194)

    def test0177(self):
        self.assertEquals(self.calculate(-1117684519, 1644109357), 1533173420)

    def test0178(self):
        self.assertEquals(self.calculate(-1220425533, 278099066), -1498524599)

    def test0179(self):
        self.assertEquals(self.calculate(2040601593, 1607345089), 433256504)

    def test0180(self):
        self.assertEquals(self.calculate(426703686, 2031944865), -1605241179)

    def test0181(self):
        self.assertEquals(self.calculate(-714704172, 1944278783), 1635984341)

    def test0182(self):
        self.assertEquals(self.calculate(174546511, 214717007), -40170496)

    def test0183(self):
        self.assertEquals(self.calculate(-1451521636, 1973772639), 869673021)

    def test0184(self):
        self.assertEquals(self.calculate(-1691126818, -1178741139), -512385679)

    def test0185(self):
        self.assertEquals(self.calculate(-766103260, 2123324395), 1405539641)

    def test0186(self):
        self.assertEquals(self.calculate(-1201200627, 278291322), -1479491949)

    def test0187(self):
        self.assertEquals(self.calculate(-1023940362, 989859995), -2013800357)

    def test0188(self):
        self.assertEquals(self.calculate(247590634, -1649745225), 1897335859)

    def test0189(self):
        self.assertEquals(self.calculate(-1329312206, -1203899533), -125412673)

    def test0190(self):
        self.assertEquals(self.calculate(2097353449, 41414631), 2055938818)

    def test0191(self):
        self.assertEquals(self.calculate(-1381798587, -94607007), -1287191580)

    def test0192(self):
        self.assertEquals(self.calculate(454349889, -2050625934), -1789991473)

    def test0193(self):
        self.assertEquals(self.calculate(204675496, 2068138148), -1863462652)

    def test0194(self):
        self.assertEquals(self.calculate(560700874, -854762425), 1415463299)

    def test0195(self):
        self.assertEquals(self.calculate(-1652275529, -1321294200), -330981329)

    def test0196(self):
        self.assertEquals(self.calculate(-1210458976, -706177830), -504281146)

    def test0197(self):
        self.assertEquals(self.calculate(1978235562, -252725258), -2064006476)

    def test0198(self):
        self.assertEquals(self.calculate(1432106104, -356141981), 1788248085)

    def test0199(self):
        self.assertEquals(self.calculate(1091972014, 1321972175), -230000161)

    def test0200(self):
        self.assertEquals(self.calculate(-1401878751, -1342591989), -59286762)

    def test0201(self):
        self.assertEquals(self.calculate(-666257323, -2105454443), 1439197120)

    def test0202(self):
        self.assertEquals(self.calculate(-506743512, -1984249507), 1477505995)

    def test0203(self):
        self.assertEquals(self.calculate(2108593456, 1752090357), 356503099)

    def test0204(self):
        self.assertEquals(self.calculate(-1814756480, 1773481025), 706729791)

    def test0205(self):
        self.assertEquals(self.calculate(-1253842675, -480843234), -772999441)

    def test0206(self):
        self.assertEquals(self.calculate(-2146876689, 869218469), 1278872138)

    def test0207(self):
        self.assertEquals(self.calculate(121798686, 1180086507), -1058287821)

    def test0208(self):
        self.assertEquals(self.calculate(650868865, -1744233992), -1899864439)

    def test0209(self):
        self.assertEquals(self.calculate(-2064100700, 1321867279), 908999317)

    def test0210(self):
        self.assertEquals(self.calculate(762725466, 1883137768), -1120412302)

    def test0211(self):
        self.assertEquals(self.calculate(-941904923, 1708864630), 1644197743)

    def test0212(self):
        self.assertEquals(self.calculate(-1748240112, 1123159773), 1423567411)

    def test0213(self):
        self.assertEquals(self.calculate(-548388868, 1103693531), -1652082399)

    def test0214(self):
        self.assertEquals(self.calculate(1132393722, -1298594179), -1863979395)

    def test0215(self):
        self.assertEquals(self.calculate(-948767725, -975574280), 26806555)

    def test0216(self):
        self.assertEquals(self.calculate(72677157, -363405945), 436083102)

    def test0217(self):
        self.assertEquals(self.calculate(-1108231915, 692456895), -1800688810)

    def test0218(self):
        self.assertEquals(self.calculate(1237033642, -511134891), 1748168533)

    def test0219(self):
        self.assertEquals(self.calculate(716201786, -1844535079), -1734230431)

    def test0220(self):
        self.assertEquals(self.calculate(362722822, -987550592), 1350273414)

    def test0221(self):
        self.assertEquals(self.calculate(-1394578391, 1707551531), 1192837374)

    def test0222(self):
        self.assertEquals(self.calculate(345706553, 1181491310), -835784757)

    def test0223(self):
        self.assertEquals(self.calculate(-351367605, -1278131596), 926763991)

    def test0224(self):
        self.assertEquals(self.calculate(-1448077137, -423907887), -1024169250)

    def test0225(self):
        self.assertEquals(self.calculate(-2107309112, -664364250), -1442944862)

    def test0226(self):
        self.assertEquals(self.calculate(-511199697, 863339666), -1374539363)

    def test0227(self):
        self.assertEquals(self.calculate(1827790681, 1269094606), 558696075)

    def test0228(self):
        self.assertEquals(self.calculate(-1540527385, -264905880), -1275621505)

    def test0229(self):
        self.assertEquals(self.calculate(-226235399, -1426787106), 1200551707)

    def test0230(self):
        self.assertEquals(self.calculate(1613210576, -2046112015), -635644705)

    def test0231(self):
        self.assertEquals(self.calculate(490412381, -1975124060), -1829430855)

    def test0232(self):
        self.assertEquals(self.calculate(332241398, -1396892783), 1729134181)

    def test0233(self):
        self.assertEquals(self.calculate(-377915301, -1066918223), 689002922)

    def test0234(self):
        self.assertEquals(self.calculate(-1255648555, 912920357), 2126398384)

    def test0235(self):
        self.assertEquals(self.calculate(607209350, 2100593811), -1493384461)

    def test0236(self):
        self.assertEquals(self.calculate(1568071447, 228291564), 1339779883)

    def test0237(self):
        self.assertEquals(self.calculate(-1035325926, 95454251), -1130780177)

    def test0238(self):
        self.assertEquals(self.calculate(-1439945936, 352382840), -1792328776)

    def test0239(self):
        self.assertEquals(self.calculate(1994675512, 1736701550), 257973962)

    def test0240(self):
        self.assertEquals(self.calculate(-622452606, -865547284), 243094678)

    def test0241(self):
        self.assertEquals(self.calculate(888312709, -1325955190), -2080699397)

    def test0242(self):
        self.assertEquals(self.calculate(-124909670, 433292465), -558202135)

    def test0243(self):
        self.assertEquals(self.calculate(-760319292, 926016471), -1686335763)

    def test0244(self):
        self.assertEquals(self.calculate(1913036113, -300145614), -2081785569)

    def test0245(self):
        self.assertEquals(self.calculate(-1859236040, 1006686576), 1429044680)

    def test0246(self):
        self.assertEquals(self.calculate(-546766727, -965650154), 418883427)

    def test0247(self):
        self.assertEquals(self.calculate(818940331, -1100941931), 1919882262)

    def test0248(self):
        self.assertEquals(self.calculate(1041021134, -1218663368), -2035282794)

    def test0249(self):
        self.assertEquals(self.calculate(-220768910, -1600139559), 1379370649)

    def test0250(self):
        self.assertEquals(self.calculate(1328791421, 83711417), 1245080004)

    def test0251(self):
        self.assertEquals(self.calculate(-586680156, 1598641394), 2109645746)

    def test0252(self):
        self.assertEquals(self.calculate(-1795091054, -1556919917), -238171137)

    def test0253(self):
        self.assertEquals(self.calculate(-395037567, 1606934482), -2001972049)

    def test0254(self):
        self.assertEquals(self.calculate(-1156210430, -1937403157), 781192727)

    def test0255(self):
        self.assertEquals(self.calculate(1268632802, -1930859001), -1095475493)

    def test0256(self):
        self.assertEquals(self.calculate(-514593232, -1627262591), 1112669359)

    def test0257(self):
        self.assertEquals(self.calculate(1162222896, 663342138), 498880758)

    def test0258(self):
        self.assertEquals(self.calculate(-2044540426, 158083179), 2092343691)

    def test0259(self):
        self.assertEquals(self.calculate(1380995080, -238980306), 1619975386)

    def test0260(self):
        self.assertEquals(self.calculate(-2145564793, -736825734), -1408739059)

    def test0261(self):
        self.assertEquals(self.calculate(946570066, 1037863660), -91293594)

    def test0262(self):
        self.assertEquals(self.calculate(-690619810, 1076480046), -1767099856)

    def test0263(self):
        self.assertEquals(self.calculate(379115259, 588611429), -209496170)

    def test0264(self):
        self.assertEquals(self.calculate(-539764895, 1178606047), -1718370942)

    def test0265(self):
        self.assertEquals(self.calculate(745302418, -225260916), 970563334)

    def test0266(self):
        self.assertEquals(self.calculate(-2048670155, -964356220), -1084313935)

    def test0267(self):
        self.assertEquals(self.calculate(-850204092, -1500123456), 649919364)

    def test0268(self):
        self.assertEquals(self.calculate(1430569414, -1510897973), -1353499909)

    def test0269(self):
        self.assertEquals(self.calculate(894275981, 108842670), 785433311)

    def test0270(self):
        self.assertEquals(self.calculate(73611022, 972859987), -899248965)

    def test0271(self):
        self.assertEquals(self.calculate(830754601, -818919558), 1649674159)

    def test0272(self):
        self.assertEquals(self.calculate(-1042210085, 664916247), -1707126332)

    def test0273(self):
        self.assertEquals(self.calculate(-1275269344, 1855150125), 1164547827)

    def test0274(self):
        self.assertEquals(self.calculate(1242738685, -601132836), 1843871521)

    def test0275(self):
        self.assertEquals(self.calculate(-1271690770, -521373899), -750316871)

    def test0276(self):
        self.assertEquals(self.calculate(795713347, 1695318505), -899605158)

    def test0277(self):
        self.assertEquals(self.calculate(-375314727, 365077844), -740392571)

    def test0278(self):
        self.assertEquals(self.calculate(-95572193, -905230703), 809658510)

    def test0279(self):
        self.assertEquals(self.calculate(1318525153, -1067382234), -1909059909)

    def test0280(self):
        self.assertEquals(self.calculate(16080140, -280632117), 296712257)

    def test0281(self):
        self.assertEquals(self.calculate(1494448057, -122344637), 1616792694)

    def test0282(self):
        self.assertEquals(self.calculate(-1281183171, -43454969), -1237728202)

    def test0283(self):
        self.assertEquals(self.calculate(-820561167, 810268516), -1630829683)

    def test0284(self):
        self.assertEquals(self.calculate(-725438973, -1647106356), 921667383)

    def test0285(self):
        self.assertEquals(self.calculate(1048496435, 1003931119), 44565316)

    def test0286(self):
        self.assertEquals(self.calculate(1233692999, 1793007668), -559314669)

    def test0287(self):
        self.assertEquals(self.calculate(965358838, 1317545220), -352186382)

    def test0288(self):
        self.assertEquals(self.calculate(-2127834177, -237333548), -1890500629)

    def test0289(self):
        self.assertEquals(self.calculate(-395499259, 1278426843), -1673926102)

    def test0290(self):
        self.assertEquals(self.calculate(711877631, -1931641610), -1651448055)

    def test0291(self):
        self.assertEquals(self.calculate(2008078358, -534052535), -1752836403)

    def test0292(self):
        self.assertEquals(self.calculate(-646888202, -217769830), -429118372)

    def test0293(self):
        self.assertEquals(self.calculate(-484560751, 1130290737), -1614851488)

    def test0294(self):
        self.assertEquals(self.calculate(-847860165, -610651588), -237208577)

    def test0295(self):
        self.assertEquals(self.calculate(-1348514007, 1224724315), 1721728974)

    def test0296(self):
        self.assertEquals(self.calculate(-116648765, -2045948909), 1929300144)

    def test0297(self):
        self.assertEquals(self.calculate(1393588165, -1759230014), -1142149117)

    def test0298(self):
        self.assertEquals(self.calculate(-2077326649, 53076138), -2130402787)

    def test0299(self):
        self.assertEquals(self.calculate(-1790381960, 811434712), 1693150624)

    def test0300(self):
        self.assertEquals(self.calculate(1305084779, -669910165), 1974994944)

    def test0301(self):
        self.assertEquals(self.calculate(-2038922978, 1708429254), 547615064)

    def test0302(self):
        self.assertEquals(self.calculate(1108530635, -12985863), 1121516498)

    def test0303(self):
        self.assertEquals(self.calculate(-665135122, 1961195901), 1668636273)

    def test0304(self):
        self.assertEquals(self.calculate(1903135892, 1675286990), 227848902)

    def test0305(self):
        self.assertEquals(self.calculate(-1058477962, -711599166), -346878796)

    def test0306(self):
        self.assertEquals(self.calculate(13472806, 1786747217), -1773274411)

    def test0307(self):
        self.assertEquals(self.calculate(2114863292, -1571938093), -608165911)

    def test0308(self):
        self.assertEquals(self.calculate(1928751750, -833024430), -1533191116)

    def test0309(self):
        self.assertEquals(self.calculate(-572029853, -1335507793), 763477940)

    def test0310(self):
        self.assertEquals(self.calculate(553010650, -747370299), 1300380949)

    def test0311(self):
        self.assertEquals(self.calculate(1506289633, -1854388828), -934288835)

    def test0312(self):
        self.assertEquals(self.calculate(-2069436822, -601251832), -1468184990)

    def test0313(self):
        self.assertEquals(self.calculate(-636580053, 1531656158), 2126731085)

    def test0314(self):
        self.assertEquals(self.calculate(-98758248, 1638473389), -1737231637)

    def test0315(self):
        self.assertEquals(self.calculate(-41008478, -307741701), 266733223)

    def test0316(self):
        self.assertEquals(self.calculate(-1507505425, 2138666447), 648795424)

    def test0317(self):
        self.assertEquals(self.calculate(1286616455, 2007198840), -720582385)

    def test0318(self):
        self.assertEquals(self.calculate(-1134175986, 2118339110), 1042452200)

    def test0319(self):
        self.assertEquals(self.calculate(1606665561, 2143786470), -537120909)

    def test0320(self):
        self.assertEquals(self.calculate(1499576659, -1531430985), -1263959652)

    def test0321(self):
        self.assertEquals(self.calculate(-1997274290, -2045585368), 48311078)

    def test0322(self):
        self.assertEquals(self.calculate(-2139078668, 1121464683), 1034423945)

    def test0323(self):
        self.assertEquals(self.calculate(-832011033, -1935041342), 1103030309)

    def test0324(self):
        self.assertEquals(self.calculate(1556892685, 1004870429), 552022256)

    def test0325(self):
        self.assertEquals(self.calculate(-180593593, 805856428), -986450021)

    def test0326(self):
        self.assertEquals(self.calculate(-1359889260, -1262955360), -96933900)

    def test0327(self):
        self.assertEquals(self.calculate(1006441961, -99777086), 1106219047)

    def test0328(self):
        self.assertEquals(self.calculate(-564246863, -1966711919), 1402465056)

    def test0329(self):
        self.assertEquals(self.calculate(-779228695, -343672432), -435556263)

    def test0330(self):
        self.assertEquals(self.calculate(1754952076, 1079907753), 675044323)

    def test0331(self):
        self.assertEquals(self.calculate(-429775153, -1661372131), 1231596978)

    def test0332(self):
        self.assertEquals(self.calculate(1940763978, 2084889421), -144125443)

    def test0333(self):
        self.assertEquals(self.calculate(778400791, -943733491), 1722134282)

    def test0334(self):
        self.assertEquals(self.calculate(-1926626768, 2056609942), 311730586)

    def test0335(self):
        self.assertEquals(self.calculate(838521350, -72680670), 911202020)

    def test0336(self):
        self.assertEquals(self.calculate(1274583713, 1004827852), 269755861)

    def test0337(self):
        self.assertEquals(self.calculate(1705961451, 321024288), 1384937163)

    def test0338(self):
        self.assertEquals(self.calculate(-283298357, 444184677), -727483034)

    def test0339(self):
        self.assertEquals(self.calculate(-1316066462, 789661383), -2105727845)

    def test0340(self):
        self.assertEquals(self.calculate(2059801567, -2019192462), -215973267)

    def test0341(self):
        self.assertEquals(self.calculate(-1761924786, -836956808), -924967978)

    def test0342(self):
        self.assertEquals(self.calculate(-321044042, 406176957), -727220999)

    def test0343(self):
        self.assertEquals(self.calculate(1361264776, 1153151140), 208113636)

    def test0344(self):
        self.assertEquals(self.calculate(1551517067, -1282095260), -1461354969)

    def test0345(self):
        self.assertEquals(self.calculate(-1858099157, -118290259), -1739808898)

    def test0346(self):
        self.assertEquals(self.calculate(16437307, 1430675611), -1414238304)

    def test0347(self):
        self.assertEquals(self.calculate(-1434874497, 739570649), 2120522150)

    def test0348(self):
        self.assertEquals(self.calculate(-2008414666, 1246717102), 1039835528)

    def test0349(self):
        self.assertEquals(self.calculate(1512008725, -268642660), 1780651385)

    def test0350(self):
        self.assertEquals(self.calculate(-299769908, -1842313499), 1542543591)

    def test0351(self):
        self.assertEquals(self.calculate(-204091102, -1025724494), 821633392)

    def test0352(self):
        self.assertEquals(self.calculate(855942455, -1074125744), 1930068199)

    def test0353(self):
        self.assertEquals(self.calculate(639164474, -1612035474), -2043767348)

    def test0354(self):
        self.assertEquals(self.calculate(482688882, -2066867476), -1745410938)

    def test0355(self):
        self.assertEquals(self.calculate(368107663, -563683094), 931790757)

    def test0356(self):
        self.assertEquals(self.calculate(-40463266, 709572429), -750035695)

    def test0357(self):
        self.assertEquals(self.calculate(830018326, 736577112), 93441214)

    def test0358(self):
        self.assertEquals(self.calculate(1682210809, 1127549030), 554661779)

    def test0359(self):
        self.assertEquals(self.calculate(102782315, 1110535778), -1007753463)

    def test0360(self):
        self.assertEquals(self.calculate(-1172477585, -234400819), -938076766)

    def test0361(self):
        self.assertEquals(self.calculate(1435833990, 1768364901), -332530911)

    def test0362(self):
        self.assertEquals(self.calculate(1895653172, -558269036), -1841045088)

    def test0363(self):
        self.assertEquals(self.calculate(1929128542, 1974327405), -45198863)

    def test0364(self):
        self.assertEquals(self.calculate(704323460, -1083508073), 1787831533)

    def test0365(self):
        self.assertEquals(self.calculate(1502680463, -2138469821), -653817012)

    def test0366(self):
        self.assertEquals(self.calculate(-2139531448, 1116666850), 1038768998)

    def test0367(self):
        self.assertEquals(self.calculate(1997315761, -992137369), -1305514166)

    def test0368(self):
        self.assertEquals(self.calculate(-1536136020, -152611795), -1383524225)

    def test0369(self):
        self.assertEquals(self.calculate(-1532294266, 852476078), 1910196952)

    def test0370(self):
        self.assertEquals(self.calculate(-1631787045, -655802039), -975985006)

    def test0371(self):
        self.assertEquals(self.calculate(-578016290, 2083300959), 1633650047)

    def test0372(self):
        self.assertEquals(self.calculate(-2115729440, 26143125), -2141872565)

    def test0373(self):
        self.assertEquals(self.calculate(-583677435, 1136827261), -1720504696)

    def test0374(self):
        self.assertEquals(self.calculate(2129745753, -431818232), -1733403311)

    def test0375(self):
        self.assertEquals(self.calculate(-998259688, -569450602), -428809086)

    def test0376(self):
        self.assertEquals(self.calculate(-1259883414, -603302229), -656581185)

    def test0377(self):
        self.assertEquals(self.calculate(-635855735, 329034828), -964890563)

    def test0378(self):
        self.assertEquals(self.calculate(1828590765, 265426403), 1563164362)

    def test0379(self):
        self.assertEquals(self.calculate(13750797, 1258892030), -1245141233)

    def test0380(self):
        self.assertEquals(self.calculate(802747239, 743471603), 59275636)

    def test0381(self):
        self.assertEquals(self.calculate(1980605250, -1141851985), -1172510061)

    def test0382(self):
        self.assertEquals(self.calculate(-24353984, -1971004133), 1946650149)

    def test0383(self):
        self.assertEquals(self.calculate(127265168, 1498429806), -1371164638)

    def test0384(self):
        self.assertEquals(self.calculate(-106150505, -157803479), 51652974)

    def test0385(self):
        self.assertEquals(self.calculate(-2117903460, 1834466834), 342597002)

    def test0386(self):
        self.assertEquals(self.calculate(-332866332, 887775641), -1220641973)

    def test0387(self):
        self.assertEquals(self.calculate(-1156211710, 172014433), -1328226143)

    def test0388(self):
        self.assertEquals(self.calculate(-989636213, 435191400), -1424827613)

    def test0389(self):
        self.assertEquals(self.calculate(1560563634, -462817655), 2023381289)

    def test0390(self):
        self.assertEquals(self.calculate(1728718692, -939234731), -1627013873)

    def test0391(self):
        self.assertEquals(self.calculate(1375329021, 1603893971), -228564950)

    def test0392(self):
        self.assertEquals(self.calculate(-615099121, 1095359170), -1710458291)

    def test0393(self):
        self.assertEquals(self.calculate(-1956862796, 2023810069), 314294431)

    def test0394(self):
        self.assertEquals(self.calculate(363451289, -1087946415), 1451397704)

    def test0395(self):
        self.assertEquals(self.calculate(1111521749, -1976823736), -1206621811)

    def test0396(self):
        self.assertEquals(self.calculate(569092812, -1392591940), 1961684752)

    def test0397(self):
        self.assertEquals(self.calculate(-1127386881, 311770730), -1439157611)

    def test0398(self):
        self.assertEquals(self.calculate(-1231726314, 543512329), -1775238643)

    def test0399(self):
        self.assertEquals(self.calculate(2035419748, -77783974), 2113203722)

    def test0400(self):
        self.assertEquals(self.calculate(1685896101, 324326170), 1361569931)

    def test0401(self):
        self.assertEquals(self.calculate(-1038564417, 1783989954), 1472412925)

    def test0402(self):
        self.assertEquals(self.calculate(687527168, -703745535), 1391272703)

    def test0403(self):
        self.assertEquals(self.calculate(-717460912, 1185683050), -1903143962)

    def test0404(self):
        self.assertEquals(self.calculate(224940905, -524570843), 749511748)

    def test0405(self):
        self.assertEquals(self.calculate(-915469107, 525753884), -1441222991)

    def test0406(self):
        self.assertEquals(self.calculate(335063960, 979320563), -644256603)

    def test0407(self):
        self.assertEquals(self.calculate(431110186, 1208208458), -777098272)

    def test0408(self):
        self.assertEquals(self.calculate(-1418670923, 1805744288), 1070552085)

    def test0409(self):
        self.assertEquals(self.calculate(-215997421, 558570816), -774568237)

    def test0410(self):
        self.assertEquals(self.calculate(2121977778, 1963923867), 158053911)

    def test0411(self):
        self.assertEquals(self.calculate(538605037, 1128468020), -589862983)

    def test0412(self):
        self.assertEquals(self.calculate(1649547271, -758529762), -1886890263)

    def test0413(self):
        self.assertEquals(self.calculate(836675890, -517006156), 1353682046)

    def test0414(self):
        self.assertEquals(self.calculate(-857751024, 826394409), -1684145433)

    def test0415(self):
        self.assertEquals(self.calculate(699157684, -1100459685), 1799617369)

    def test0416(self):
        self.assertEquals(self.calculate(2136958554, 1865088145), 271870409)

    def test0417(self):
        self.assertEquals(self.calculate(1971848806, 759496685), 1212352121)

    def test0418(self):
        self.assertEquals(self.calculate(1636483700, 1358485688), 277998012)

    def test0419(self):
        self.assertEquals(self.calculate(-1355853523, 1204971160), 1734142613)

    def test0420(self):
        self.assertEquals(self.calculate(-119916490, -1391636331), 1271719841)

    def test0421(self):
        self.assertEquals(self.calculate(824197588, 975726224), -151528636)

    def test0422(self):
        self.assertEquals(self.calculate(-1151951101, 602341918), -1754293019)

    def test0423(self):
        self.assertEquals(self.calculate(-1674665189, -1268308185), -406357004)

    def test0424(self):
        self.assertEquals(self.calculate(-721290687, 77041935), -798332622)

    def test0425(self):
        self.assertEquals(self.calculate(-1194676828, -1778990514), 584313686)

    def test0426(self):
        self.assertEquals(self.calculate(344881566, 211661384), 133220182)

    def test0427(self):
        self.assertEquals(self.calculate(-1916462449, -2034119226), 117656777)

    def test0428(self):
        self.assertEquals(self.calculate(-37071323, 1698481305), -1735552628)

    def test0429(self):
        self.assertEquals(self.calculate(-632448078, 1395069300), -2027517378)

    def test0430(self):
        self.assertEquals(self.calculate(745145661, 144903694), 600241967)

    def test0431(self):
        self.assertEquals(self.calculate(1507279119, 2043535651), -536256532)

    def test0432(self):
        self.assertEquals(self.calculate(-321137546, -240255734), -80881812)

    def test0433(self):
        self.assertEquals(self.calculate(282122398, 950042632), -667920234)

    def test0434(self):
        self.assertEquals(self.calculate(-1527691629, 1995300817), 771974850)

    def test0435(self):
        self.assertEquals(self.calculate(1885903902, 575022645), 1310881257)

    def test0436(self):
        self.assertEquals(self.calculate(-784145660, 962794396), -1746940056)

    def test0437(self):
        self.assertEquals(self.calculate(-1076108151, 1408708814), 1810150331)

    def test0438(self):
        self.assertEquals(self.calculate(898178956, -253171071), 1151350027)

    def test0439(self):
        self.assertEquals(self.calculate(-539637691, 741953836), -1281591527)

    def test0440(self):
        self.assertEquals(self.calculate(871640414, 309176135), 562464279)

    def test0441(self):
        self.assertEquals(self.calculate(963196998, 569491551), 393705447)

    def test0442(self):
        self.assertEquals(self.calculate(-1730153821, -2015257677), 285103856)

    def test0443(self):
        self.assertEquals(self.calculate(159422024, 1978127810), -1818705786)

    def test0444(self):
        self.assertEquals(self.calculate(2014856665, 1410512789), 604343876)

    def test0445(self):
        self.assertEquals(self.calculate(1650710310, -176124348), 1826834658)

    def test0446(self):
        self.assertEquals(self.calculate(1333487676, -1999487089), -961992531)

    def test0447(self):
        self.assertEquals(self.calculate(1210522452, 440400209), 770122243)

    def test0448(self):
        self.assertEquals(self.calculate(-2113999059, -460627606), -1653371453)

    def test0449(self):
        self.assertEquals(self.calculate(1116383144, 1551771667), -435388523)

    def test0450(self):
        self.assertEquals(self.calculate(1217795975, -2142488618), -934682703)

    def test0451(self):
        self.assertEquals(self.calculate(-884619921, -1775371670), 890751749)

    def test0452(self):
        self.assertEquals(self.calculate(-82362076, -2024144096), 1941782020)

    def test0453(self):
        self.assertEquals(self.calculate(-899446383, 31920310), -931366693)

    def test0454(self):
        self.assertEquals(self.calculate(564550166, 918832490), -354282324)

    def test0455(self):
        self.assertEquals(self.calculate(-1821615096, 152039183), -1973654279)

    def test0456(self):
        self.assertEquals(self.calculate(1804027482, -867282220), -1623657594)

    def test0457(self):
        self.assertEquals(self.calculate(129603844, -1848471611), 1978075455)

    def test0458(self):
        self.assertEquals(self.calculate(-1277152257, 755633742), -2032785999)

    def test0459(self):
        self.assertEquals(self.calculate(1289130963, 1315961361), -26830398)

    def test0460(self):
        self.assertEquals(self.calculate(-595181237, -129565412), -465615825)

    def test0461(self):
        self.assertEquals(self.calculate(-1783929431, -71780243), -1712149188)

    def test0462(self):
        self.assertEquals(self.calculate(1560810680, 1326437289), 234373391)

    def test0463(self):
        self.assertEquals(self.calculate(850500631, -1798942260), -1645524405)

    def test0464(self):
        self.assertEquals(self.calculate(1002329415, 1316865225), -314535810)

    def test0465(self):
        self.assertEquals(self.calculate(1943046763, 425436138), 1517610625)

    def test0466(self):
        self.assertEquals(self.calculate(115094443, -1973822490), 2088916933)

    def test0467(self):
        self.assertEquals(self.calculate(-1568224784, 2037909857), 688832655)

    def test0468(self):
        self.assertEquals(self.calculate(-1346765608, 2032340791), 915860897)

    def test0469(self):
        self.assertEquals(self.calculate(1058440398, -885291828), 1943732226)

    def test0470(self):
        self.assertEquals(self.calculate(-1243992392, 28993723), -1272986115)

    def test0471(self):
        self.assertEquals(self.calculate(-1191954004, -395978049), -795975955)

    def test0472(self):
        self.assertEquals(self.calculate(1662764031, 730278941), 932485090)

    def test0473(self):
        self.assertEquals(self.calculate(381284125, 983618604), -602334479)

    def test0474(self):
        self.assertEquals(self.calculate(-1841323587, 750433748), 1703209961)

    def test0475(self):
        self.assertEquals(self.calculate(695409533, -1539702375), -2059855388)

    def test0476(self):
        self.assertEquals(self.calculate(1492153536, 1893092895), -400939359)

    def test0477(self):
        self.assertEquals(self.calculate(1116399864, 1115535847), 864017)

    def test0478(self):
        self.assertEquals(self.calculate(-1553149194, 1860479259), 881338843)

    def test0479(self):
        self.assertEquals(self.calculate(-1639833228, -1308622437), -331210791)

    def test0480(self):
        self.assertEquals(self.calculate(1067072549, -2005051404), -1222843343)

    def test0481(self):
        self.assertEquals(self.calculate(-1339517732, -823552723), -515965009)

    def test0482(self):
        self.assertEquals(self.calculate(559900050, -953027819), 1512927869)

    def test0483(self):
        self.assertEquals(self.calculate(2008904418, -858713296), -1427349582)

    def test0484(self):
        self.assertEquals(self.calculate(-68074053, 69731959), -137806012)

    def test0485(self):
        self.assertEquals(self.calculate(-1926292973, 1713734101), 654940222)

    def test0486(self):
        self.assertEquals(self.calculate(682441994, 649302900), 33139094)

    def test0487(self):
        self.assertEquals(self.calculate(1926577205, -2011228067), -357162024)

    def test0488(self):
        self.assertEquals(self.calculate(1247098045, 1053981829), 193116216)

    def test0489(self):
        self.assertEquals(self.calculate(-583332564, 1964747943), 1746886789)

    def test0490(self):
        self.assertEquals(self.calculate(-1784838246, -379331833), -1405506413)

    def test0491(self):
        self.assertEquals(self.calculate(653275506, -641810137), 1295085643)

    def test0492(self):
        self.assertEquals(self.calculate(1519277503, 444940508), 1074336995)

    def test0493(self):
        self.assertEquals(self.calculate(857976627, 205006480), 652970147)

    def test0494(self):
        self.assertEquals(self.calculate(1726754276, 988448849), 738305427)

    def test0495(self):
        self.assertEquals(self.calculate(166647123, 1315048444), -1148401321)

    def test0496(self):
        self.assertEquals(self.calculate(-433510193, -453944537), 20434344)

    def test0497(self):
        self.assertEquals(self.calculate(759360060, 569259282), 190100778)

    def test0498(self):
        self.assertEquals(self.calculate(284798370, 1703037381), -1418239011)

    def test0499(self):
        self.assertEquals(self.calculate(-1477420331, -1753732680), 276312349)

    def test0500(self):
        self.assertEquals(self.calculate(-265945427, -1903977703), 1638032276)

    def test0501(self):
        self.assertEquals(self.calculate(656430212, -1123525982), 1779956194)

    def test0502(self):
        self.assertEquals(self.calculate(-675059981, -962090994), 287031013)

    def test0503(self):
        self.assertEquals(self.calculate(909497185, -80681942), 990179127)

    def test0504(self):
        self.assertEquals(self.calculate(299712319, 1550176233), -1250463914)

    def test0505(self):
        self.assertEquals(self.calculate(764273439, 850467033), -86193594)

    def test0506(self):
        self.assertEquals(self.calculate(1505116570, 1636207965), -131091395)

    def test0507(self):
        self.assertEquals(self.calculate(-262063677, -1203283751), 941220074)

    def test0508(self):
        self.assertEquals(self.calculate(-18452397, -561441314), 542988917)

    def test0509(self):
        self.assertEquals(self.calculate(-111513584, 1325279412), -1436792996)

    def test0510(self):
        self.assertEquals(self.calculate(-1215230923, 379389265), -1594620188)

    def test0511(self):
        self.assertEquals(self.calculate(-746904777, 862452350), -1609357127)

    def test0512(self):
        self.assertEquals(self.calculate(-123268328, 754246623), -877514951)

    def test0513(self):
        self.assertEquals(self.calculate(-1259744200, -619222659), -640521541)

    def test0514(self):
        self.assertEquals(self.calculate(-963127878, 1713821253), 1618018165)

    def test0515(self):
        self.assertEquals(self.calculate(-524926033, -1498632266), 973706233)

    def test0516(self):
        self.assertEquals(self.calculate(2120270920, -439460249), -1735236127)

    def test0517(self):
        self.assertEquals(self.calculate(742615473, 2070598623), -1327983150)

    def test0518(self):
        self.assertEquals(self.calculate(352849078, 936594765), -583745687)

    def test0519(self):
        self.assertEquals(self.calculate(2947262, -838924568), 841871830)

    def test0520(self):
        self.assertEquals(self.calculate(1589079209, -1602171117), -1103716970)

    def test0521(self):
        self.assertEquals(self.calculate(-2137906433, -2139451356), 1544923)

    def test0522(self):
        self.assertEquals(self.calculate(581675551, -311276020), 892951571)

    def test0523(self):
        self.assertEquals(self.calculate(-844238234, 534606093), -1378844327)

    def test0524(self):
        self.assertEquals(self.calculate(-1640157218, 110977049), -1751134267)

    def test0525(self):
        self.assertEquals(self.calculate(1674365612, -913751596), -1706850088)

    def test0526(self):
        self.assertEquals(self.calculate(1075193622, 1015897983), 59295639)

    def test0527(self):
        self.assertEquals(self.calculate(38148786, 1915028178), -1876879392)

    def test0528(self):
        self.assertEquals(self.calculate(22389255, 141650040), -119260785)

    def test0529(self):
        self.assertEquals(self.calculate(-1004331014, 1191398494), 2099237788)

    def test0530(self):
        self.assertEquals(self.calculate(1112131296, -1793449206), -1389386794)

    def test0531(self):
        self.assertEquals(self.calculate(-478926363, -674510553), 195584190)

    def test0532(self):
        self.assertEquals(self.calculate(-2095812683, 1979822856), 219331757)

    def test0533(self):
        self.assertEquals(self.calculate(-427750812, 1588911844), -2016662656)

    def test0534(self):
        self.assertEquals(self.calculate(-1840179284, 309735173), 2145052839)

    def test0535(self):
        self.assertEquals(self.calculate(-568983415, -338864268), -230119147)

    def test0536(self):
        self.assertEquals(self.calculate(122792352, 569986691), -447194339)

    def test0537(self):
        self.assertEquals(self.calculate(837086086, -1379365163), -2078516047)

    def test0538(self):
        self.assertEquals(self.calculate(-1773173147, 223738102), -1996911249)

    def test0539(self):
        self.assertEquals(self.calculate(428297892, -1637479060), 2065776952)

    def test0540(self):
        self.assertEquals(self.calculate(-1827297432, 1097815167), 1369854697)

    def test0541(self):
        self.assertEquals(self.calculate(-645600506, 756139490), -1401739996)

    def test0542(self):
        self.assertEquals(self.calculate(-2118937187, -1144695627), -974241560)

    def test0543(self):
        self.assertEquals(self.calculate(-490533440, -1367040364), 876506924)

    def test0544(self):
        self.assertEquals(self.calculate(35758063, -907952716), 943710779)

    def test0545(self):
        self.assertEquals(self.calculate(-871412538, -1120954656), 249542118)

    def test0546(self):
        self.assertEquals(self.calculate(1196529558, 1933607691), -737078133)

    def test0547(self):
        self.assertEquals(self.calculate(-841559106, -207641402), -633917704)

    def test0548(self):
        self.assertEquals(self.calculate(-1330828261, -1526055914), 195227653)

    def test0549(self):
        self.assertEquals(self.calculate(738017694, -116609600), 854627294)

    def test0550(self):
        self.assertEquals(self.calculate(-1381546211, -1402393038), 20846827)

    def test0551(self):
        self.assertEquals(self.calculate(767021610, 1638388331), -871366721)

    def test0552(self):
        self.assertEquals(self.calculate(-158513467, 245549000), -404062467)

    def test0553(self):
        self.assertEquals(self.calculate(1212759733, -1536864826), -1545342737)

    def test0554(self):
        self.assertEquals(self.calculate(-1378046324, -36957962), -1341088362)

    def test0555(self):
        self.assertEquals(self.calculate(-983530141, 909944092), -1893474233)

    def test0556(self):
        self.assertEquals(self.calculate(-474982515, 1497745474), -1972727989)

    def test0557(self):
        self.assertEquals(self.calculate(-1863039110, -547919636), -1315119474)

    def test0558(self):
        self.assertEquals(self.calculate(-1109275731, -1747817048), 638541317)

    def test0559(self):
        self.assertEquals(self.calculate(1137712721, 1070253967), 67458754)

    def test0560(self):
        self.assertEquals(self.calculate(1723608955, -1746557639), -824800702)

    def test0561(self):
        self.assertEquals(self.calculate(-603791213, 1821177427), 1869998656)

    def test0562(self):
        self.assertEquals(self.calculate(-1917801594, -117528293), -1800273301)

    def test0563(self):
        self.assertEquals(self.calculate(-220145343, -2125907651), 1905762308)

    def test0564(self):
        self.assertEquals(self.calculate(-1600193555, -1295871091), -304322464)

    def test0565(self):
        self.assertEquals(self.calculate(-750232139, 1150767976), -1901000115)

    def test0566(self):
        self.assertEquals(self.calculate(1175657140, 464093248), 711563892)

    def test0567(self):
        self.assertEquals(self.calculate(-828458971, -66386043), -762072928)

    def test0568(self):
        self.assertEquals(self.calculate(-2052893395, 1342745170), 899328731)

    def test0569(self):
        self.assertEquals(self.calculate(-663706849, 978116625), -1641823474)

    def test0570(self):
        self.assertEquals(self.calculate(-1734243860, 1332184657), 1228538779)

    def test0571(self):
        self.assertEquals(self.calculate(-507047484, -929978587), 422931103)

    def test0572(self):
        self.assertEquals(self.calculate(-1514699310, -707704686), -806994624)

    def test0573(self):
        self.assertEquals(self.calculate(-1404001172, 1633032287), 1257933837)

    def test0574(self):
        self.assertEquals(self.calculate(-422442987, -1174797008), 752354021)

    def test0575(self):
        self.assertEquals(self.calculate(-1914392288, -863715101), -1050677187)

    def test0576(self):
        self.assertEquals(self.calculate(1844223621, 589634970), 1254588651)

    def test0577(self):
        self.assertEquals(self.calculate(1803927873, -1481861000), -1009178423)

    def test0578(self):
        self.assertEquals(self.calculate(-1847056659, 1271751155), 1176159482)

    def test0579(self):
        self.assertEquals(self.calculate(-1648085886, -1650350636), 2264750)

    def test0580(self):
        self.assertEquals(self.calculate(-1269273494, 2118765313), 906928489)

    def test0581(self):
        self.assertEquals(self.calculate(-847392478, -406754958), -440637520)

    def test0582(self):
        self.assertEquals(self.calculate(-1139221181, 216948345), -1356169526)

    def test0583(self):
        self.assertEquals(self.calculate(-1401922218, -191090607), -1210831611)

    def test0584(self):
        self.assertEquals(self.calculate(1626214355, 1720856075), -94641720)

    def test0585(self):
        self.assertEquals(self.calculate(1486580786, -682158403), -2126228107)

    def test0586(self):
        self.assertEquals(self.calculate(2078617152, 545374616), 1533242536)

    def test0587(self):
        self.assertEquals(self.calculate(-787793010, 745912767), -1533705777)

    def test0588(self):
        self.assertEquals(self.calculate(-743001989, 1433427733), 2118537574)

    def test0589(self):
        self.assertEquals(self.calculate(1772734978, 1740297318), 32437660)

    def test0590(self):
        self.assertEquals(self.calculate(123477250, 373828838), -250351588)

    def test0591(self):
        self.assertEquals(self.calculate(-624846762, 839172013), -1464018775)

    def test0592(self):
        self.assertEquals(self.calculate(1574634189, -1818807992), -901525115)

    def test0593(self):
        self.assertEquals(self.calculate(806871499, 565576022), 241295477)

    def test0594(self):
        self.assertEquals(self.calculate(-24480459, -283785746), 259305287)

    def test0595(self):
        self.assertEquals(self.calculate(-245159088, 398395499), -643554587)

    def test0596(self):
        self.assertEquals(self.calculate(-430705864, 1328957307), -1759663171)

    def test0597(self):
        self.assertEquals(self.calculate(662264979, 481826966), 180438013)

    def test0598(self):
        self.assertEquals(self.calculate(1379893293, 531865816), 848027477)

    def test0599(self):
        self.assertEquals(self.calculate(-230230501, -1704284128), 1474053627)

    def test0600(self):
        self.assertEquals(self.calculate(1403960228, -356885687), 1760845915)

    def test0601(self):
        self.assertEquals(self.calculate(1580376361, -1003053964), -1711536971)

    def test0602(self):
        self.assertEquals(self.calculate(-1705701190, 2135049767), 454216339)

    def test0603(self):
        self.assertEquals(self.calculate(-637855428, -3734478), -634120950)

    def test0604(self):
        self.assertEquals(self.calculate(1809100529, -2016993906), -468872861)

    def test0605(self):
        self.assertEquals(self.calculate(1074697038, 601783576), 472913462)

    def test0606(self):
        self.assertEquals(self.calculate(-1390202245, 961360415), 1943404636)

    def test0607(self):
        self.assertEquals(self.calculate(-606127241, 1338911374), -1945038615)

    def test0608(self):
        self.assertEquals(self.calculate(-1552351918, 1780795051), 961820327)

    def test0609(self):
        self.assertEquals(self.calculate(-787156947, 1885757960), 1622052389)

    def test0610(self):
        self.assertEquals(self.calculate(-345151675, -554959114), 209807439)

    def test0611(self):
        self.assertEquals(self.calculate(1157400648, -555005481), 1712406129)

    def test0612(self):
        self.assertEquals(self.calculate(1965321817, -1338589419), -991056060)

    def test0613(self):
        self.assertEquals(self.calculate(-1474737210, 1563959848), 1256270238)

    def test0614(self):
        self.assertEquals(self.calculate(592173115, -371260909), 963434024)

    def test0615(self):
        self.assertEquals(self.calculate(1570386086, -1102198147), -1622383063)

    def test0616(self):
        self.assertEquals(self.calculate(-1535391550, 185524284), -1720915834)

    def test0617(self):
        self.assertEquals(self.calculate(-508751319, -39259945), -469491374)

    def test0618(self):
        self.assertEquals(self.calculate(1001564331, -1553654407), -1739748558)

    def test0619(self):
        self.assertEquals(self.calculate(862556349, 1539741118), -677184769)

    def test0620(self):
        self.assertEquals(self.calculate(-28182082, 1696658913), -1724840995)

    def test0621(self):
        self.assertEquals(self.calculate(1169086122, -173872178), 1342958300)

    def test0622(self):
        self.assertEquals(self.calculate(28360666, 1809027532), -1780666866)

    def test0623(self):
        self.assertEquals(self.calculate(-2046697565, 1729299139), 518970592)

    def test0624(self):
        self.assertEquals(self.calculate(994457275, -1212739103), -2087770918)

    def test0625(self):
        self.assertEquals(self.calculate(-1193589984, 367454387), -1561044371)

    def test0626(self):
        self.assertEquals(self.calculate(1277686629, 941651761), 336034868)

    def test0627(self):
        self.assertEquals(self.calculate(1485101403, 533129), 1484568274)

    def test0628(self):
        self.assertEquals(self.calculate(-871565025, 1451057428), 1972344843)

    def test0629(self):
        self.assertEquals(self.calculate(1922125296, 1239350549), 682774747)

    def test0630(self):
        self.assertEquals(self.calculate(725906085, -1591243), 727497328)

    def test0631(self):
        self.assertEquals(self.calculate(870497551, 1316708976), -446211425)

    def test0632(self):
        self.assertEquals(self.calculate(443931864, 321858133), 122073731)

    def test0633(self):
        self.assertEquals(self.calculate(2102823655, -1380660800), -811482841)

    def test0634(self):
        self.assertEquals(self.calculate(1396978057, 1089822787), 307155270)

    def test0635(self):
        self.assertEquals(self.calculate(-618317624, -1479567353), 861249729)

    def test0636(self):
        self.assertEquals(self.calculate(1554489490, -969967599), -1770510207)

    def test0637(self):
        self.assertEquals(self.calculate(1174337595, 195133084), 979204511)

    def test0638(self):
        self.assertEquals(self.calculate(-253300704, -580714619), 327413915)

    def test0639(self):
        self.assertEquals(self.calculate(1276219399, 1463460854), -187241455)

    def test0640(self):
        self.assertEquals(self.calculate(-936658567, -1439543351), 502884784)

    def test0641(self):
        self.assertEquals(self.calculate(1127364828, -356924263), 1484289091)

    def test0642(self):
        self.assertEquals(self.calculate(802368489, 85008743), 717359746)

    def test0643(self):
        self.assertEquals(self.calculate(1534512906, -472180956), 2006693862)

    def test0644(self):
        self.assertEquals(self.calculate(-1912775510, -1018709843), -894065667)

    def test0645(self):
        self.assertEquals(self.calculate(-1834786323, -1903468530), 68682207)

    def test0646(self):
        self.assertEquals(self.calculate(68316528, 1536054579), -1467738051)

    def test0647(self):
        self.assertEquals(self.calculate(-582427497, -786717706), 204290209)

    def test0648(self):
        self.assertEquals(self.calculate(623718028, -176887369), 800605397)

    def test0649(self):
        self.assertEquals(self.calculate(-317747701, 610320267), -928067968)

    def test0650(self):
        self.assertEquals(self.calculate(-282323152, 1508321364), -1790644516)

    def test0651(self):
        self.assertEquals(self.calculate(-873168196, 28406555), -901574751)

    def test0652(self):
        self.assertEquals(self.calculate(1701649467, -1352600638), -1240717191)

    def test0653(self):
        self.assertEquals(self.calculate(1138507179, 9060445), 1129446734)

    def test0654(self):
        self.assertEquals(self.calculate(-591408813, 983750802), -1575159615)

    def test0655(self):
        self.assertEquals(self.calculate(1716481726, 193143863), 1523337863)

    def test0656(self):
        self.assertEquals(self.calculate(925862112, 835553773), 90308339)

    def test0657(self):
        self.assertEquals(self.calculate(-2113154788, 1820156307), 361656201)

    def test0658(self):
        self.assertEquals(self.calculate(-147101197, -1093048896), 945947699)

    def test0659(self):
        self.assertEquals(self.calculate(-760582538, -673568830), -87013708)

    def test0660(self):
        self.assertEquals(self.calculate(-1938232720, 1426733795), 930000781)

    def test0661(self):
        self.assertEquals(self.calculate(1390864131, 20708606), 1370155525)

    def test0662(self):
        self.assertEquals(self.calculate(-213809121, -516597343), 302788222)

    def test0663(self):
        self.assertEquals(self.calculate(1837511543, -681052590), -1776403163)

    def test0664(self):
        self.assertEquals(self.calculate(612785437, 1789634899), -1176849462)

    def test0665(self):
        self.assertEquals(self.calculate(-1668025608, 1844690901), 782250787)

    def test0666(self):
        self.assertEquals(self.calculate(-902958275, 89721044), -992679319)

    def test0667(self):
        self.assertEquals(self.calculate(-1610864886, -528545845), -1082319041)

    def test0668(self):
        self.assertEquals(self.calculate(585530029, -380646360), 966176389)

    def test0669(self):
        self.assertEquals(self.calculate(379888249, 552149692), -172261443)

    def test0670(self):
        self.assertEquals(self.calculate(1729941816, 476740429), 1253201387)

    def test0671(self):
        self.assertEquals(self.calculate(560415173, -740090692), 1300505865)

    def test0672(self):
        self.assertEquals(self.calculate(67505402, 487349242), -419843840)

    def test0673(self):
        self.assertEquals(self.calculate(1508986796, -283458892), 1792445688)

    def test0674(self):
        self.assertEquals(self.calculate(-371380584, -319046321), -52334263)

    def test0675(self):
        self.assertEquals(self.calculate(-74324156, -1169720238), 1095396082)

    def test0676(self):
        self.assertEquals(self.calculate(1077835222, 263763220), 814072002)

    def test0677(self):
        self.assertEquals(self.calculate(-1703636258, 975409248), 1615921790)

    def test0678(self):
        self.assertEquals(self.calculate(1220531050, -896963892), 2117494942)

    def test0679(self):
        self.assertEquals(self.calculate(-179280417, 1716077661), -1895358078)

    def test0680(self):
        self.assertEquals(self.calculate(1195853607, 1542341693), -346488086)

    def test0681(self):
        self.assertEquals(self.calculate(-1109397762, -1589598720), 480200958)

    def test0682(self):
        self.assertEquals(self.calculate(194900887, 157060137), 37840750)

    def test0683(self):
        self.assertEquals(self.calculate(-630052817, -679662417), 49609600)

    def test0684(self):
        self.assertEquals(self.calculate(-1826645274, -344184183), -1482461091)

    def test0685(self):
        self.assertEquals(self.calculate(-1926101173, -1451876635), -474224538)

    def test0686(self):
        self.assertEquals(self.calculate(927319872, -1457814501), -1909832923)

    def test0687(self):
        self.assertEquals(self.calculate(2104091605, -234636880), -1956238811)

    def test0688(self):
        self.assertEquals(self.calculate(-1308387693, 694674289), -2003061982)

    def test0689(self):
        self.assertEquals(self.calculate(-487462835, -792534081), 305071246)

    def test0690(self):
        self.assertEquals(self.calculate(1688816718, -1157227364), -1448923214)

    def test0691(self):
        self.assertEquals(self.calculate(-255801193, -1716631505), 1460830312)

    def test0692(self):
        self.assertEquals(self.calculate(-470858597, -502382249), 31523652)

    def test0693(self):
        self.assertEquals(self.calculate(-1124558087, -317642365), -806915722)

    def test0694(self):
        self.assertEquals(self.calculate(-1596617897, 1810974879), 887374520)

    def test0695(self):
        self.assertEquals(self.calculate(1958887931, -786528601), -1549550764)

    def test0696(self):
        self.assertEquals(self.calculate(2050916750, 853958825), 1196957925)

    def test0697(self):
        self.assertEquals(self.calculate(1147824069, 1292197919), -144373850)

    def test0698(self):
        self.assertEquals(self.calculate(-17458922, -1229494662), 1212035740)

    def test0699(self):
        self.assertEquals(self.calculate(-1845616298, -1480699736), -364916562)

    def test0700(self):
        self.assertEquals(self.calculate(-591779701, -1370015120), 778235419)

    def test0701(self):
        self.assertEquals(self.calculate(-705184390, -1505102989), 799918599)

    def test0702(self):
        self.assertEquals(self.calculate(1666323826, 540800183), 1125523643)

    def test0703(self):
        self.assertEquals(self.calculate(312367965, 54005224), 258362741)

    def test0704(self):
        self.assertEquals(self.calculate(1405918675, 54172756), 1351745919)

    def test0705(self):
        self.assertEquals(self.calculate(-742906306, -818375301), 75468995)

    def test0706(self):
        self.assertEquals(self.calculate(248826166, 1036544829), -787718663)

    def test0707(self):
        self.assertEquals(self.calculate(-1425064282, 222259192), -1647323474)

    def test0708(self):
        self.assertEquals(self.calculate(-1186925627, -988598313), -198327314)

    def test0709(self):
        self.assertEquals(self.calculate(1983496434, -712086831), -1599384031)

    def test0710(self):
        self.assertEquals(self.calculate(-1618660261, -1979830459), 361170198)

    def test0711(self):
        self.assertEquals(self.calculate(2135938693, -2083940230), -75088373)

    def test0712(self):
        self.assertEquals(self.calculate(-1479596435, -1155670515), -323925920)

    def test0713(self):
        self.assertEquals(self.calculate(1581086440, 1544030487), 37055953)

    def test0714(self):
        self.assertEquals(self.calculate(-911036653, 1644881810), 1739048833)

    def test0715(self):
        self.assertEquals(self.calculate(-60680022, 1875911846), -1936591868)

    def test0716(self):
        self.assertEquals(self.calculate(-235992766, -1972318079), 1736325313)

    def test0717(self):
        self.assertEquals(self.calculate(-238020748, 1848984527), -2087005275)

    def test0718(self):
        self.assertEquals(self.calculate(-1552936817, 1887961089), 854069390)

    def test0719(self):
        self.assertEquals(self.calculate(-2047005916, -954053604), -1092952312)

    def test0720(self):
        self.assertEquals(self.calculate(-394504089, 276580395), -671084484)

    def test0721(self):
        self.assertEquals(self.calculate(-635633254, 489929132), -1125562386)

    def test0722(self):
        self.assertEquals(self.calculate(-452593608, 964266265), -1416859873)

    def test0723(self):
        self.assertEquals(self.calculate(-2059086902, 792070950), 1443809444)

    def test0724(self):
        self.assertEquals(self.calculate(-1584364793, -1388706810), -195657983)

    def test0725(self):
        self.assertEquals(self.calculate(-344334469, -109452550), -234881919)

    def test0726(self):
        self.assertEquals(self.calculate(-722952731, 2062493677), 1509520888)

    def test0727(self):
        self.assertEquals(self.calculate(141194676, 1338840907), -1197646231)

    def test0728(self):
        self.assertEquals(self.calculate(1474201232, 24392626), 1449808606)

    def test0729(self):
        self.assertEquals(self.calculate(2144590445, -1488264991), -662111860)

    def test0730(self):
        self.assertEquals(self.calculate(1489130765, -1199028352), -1606808179)

    def test0731(self):
        self.assertEquals(self.calculate(1023711899, -1146824508), -2124430889)

    def test0732(self):
        self.assertEquals(self.calculate(-1322054399, -101714436), -1220339963)

    def test0733(self):
        self.assertEquals(self.calculate(246471746, 1225473683), -979001937)

    def test0734(self):
        self.assertEquals(self.calculate(1184561174, 762884803), 421676371)

    def test0735(self):
        self.assertEquals(self.calculate(-1423099781, 1866731792), 1005135723)

    def test0736(self):
        self.assertEquals(self.calculate(-1928247441, -1480691283), -447556158)

    def test0737(self):
        self.assertEquals(self.calculate(-1015769674, -66445880), -949323794)

    def test0738(self):
        self.assertEquals(self.calculate(-115218296, 435653), -115653949)

    def test0739(self):
        self.assertEquals(self.calculate(-471568023, 2070981864), 1752417409)

    def test0740(self):
        self.assertEquals(self.calculate(-291782916, -127475783), -164307133)

    def test0741(self):
        self.assertEquals(self.calculate(-1840457185, -257395914), -1583061271)

    def test0742(self):
        self.assertEquals(self.calculate(-1049342491, 1949500644), 1296124161)

    def test0743(self):
        self.assertEquals(self.calculate(1348436517, -342578291), 1691014808)

    def test0744(self):
        self.assertEquals(self.calculate(-1756423334, -814468692), -941954642)

    def test0745(self):
        self.assertEquals(self.calculate(1156928437, -894978637), 2051907074)

    def test0746(self):
        self.assertEquals(self.calculate(-66738774, 952610975), -1019349749)

    def test0747(self):
        self.assertEquals(self.calculate(-518356825, -295913218), -222443607)

    def test0748(self):
        self.assertEquals(self.calculate(1699424500, -1350629950), -1244912846)

    def test0749(self):
        self.assertEquals(self.calculate(-933871413, -328039618), -605831795)

    def test0750(self):
        self.assertEquals(self.calculate(-994145911, -1061439892), 67293981)

    def test0751(self):
        self.assertEquals(self.calculate(-486188772, 1689649179), 2119129345)

    def test0752(self):
        self.assertEquals(self.calculate(-1647995240, -892801826), -755193414)

    def test0753(self):
        self.assertEquals(self.calculate(-1259544041, 201780369), -1461324410)

    def test0754(self):
        self.assertEquals(self.calculate(1568309707, 457234315), 1111075392)

    def test0755(self):
        self.assertEquals(self.calculate(-1473316511, 349893705), -1823210216)

    def test0756(self):
        self.assertEquals(self.calculate(-818976608, -2017639436), 1198662828)

    def test0757(self):
        self.assertEquals(self.calculate(1954644594, -1407820842), -932501860)

    def test0758(self):
        self.assertEquals(self.calculate(-1202569350, 1878213272), 1214184674)

    def test0759(self):
        self.assertEquals(self.calculate(-960602842, 2137396136), 1196968318)

    def test0760(self):
        self.assertEquals(self.calculate(1933607474, -1178279811), -1183080011)

    def test0761(self):
        self.assertEquals(self.calculate(-1670940814, -1646800579), -24140235)

    def test0762(self):
        self.assertEquals(self.calculate(-2049132183, 553518872), 1692316241)

    def test0763(self):
        self.assertEquals(self.calculate(-1819484133, -718578921), -1100905212)

    def test0764(self):
        self.assertEquals(self.calculate(-548564348, -1967987857), 1419423509)

    def test0765(self):
        self.assertEquals(self.calculate(193474623, 601556055), -408081432)

    def test0766(self):
        self.assertEquals(self.calculate(1830407691, 2106585448), -276177757)

    def test0767(self):
        self.assertEquals(self.calculate(1116513194, -977608850), 2094122044)

    def test0768(self):
        self.assertEquals(self.calculate(1194466056, -234229037), 1428695093)

    def test0769(self):
        self.assertEquals(self.calculate(1543753750, 1229149228), 314604522)

    def test0770(self):
        self.assertEquals(self.calculate(-1273729706, 676912187), -1950641893)

    def test0771(self):
        self.assertEquals(self.calculate(-1048496849, 1858686801), 1387783646)

    def test0772(self):
        self.assertEquals(self.calculate(-854598886, 1802590478), 1637777932)

    def test0773(self):
        self.assertEquals(self.calculate(-1198400741, 1550899507), 1545667048)

    def test0774(self):
        self.assertEquals(self.calculate(1925927627, -1242451499), -1126588170)

    def test0775(self):
        self.assertEquals(self.calculate(-1264613966, 926089008), 2104264322)

    def test0776(self):
        self.assertEquals(self.calculate(642980125, -327374606), 970354731)

    def test0777(self):
        self.assertEquals(self.calculate(150665092, -993366212), 1144031304)

    def test0778(self):
        self.assertEquals(self.calculate(-62212295, 621850305), -684062600)

    def test0779(self):
        self.assertEquals(self.calculate(-158006598, -674772601), 516766003)

    def test0780(self):
        self.assertEquals(self.calculate(1950944920, -1300979876), -1043042500)

    def test0781(self):
        self.assertEquals(self.calculate(544393882, -397944278), 942338160)

    def test0782(self):
        self.assertEquals(self.calculate(141078548, 1100969409), -959890861)

    def test0783(self):
        self.assertEquals(self.calculate(-1413320126, -2056988799), 643668673)

    def test0784(self):
        self.assertEquals(self.calculate(1438738232, -873182253), -1983046811)

    def test0785(self):
        self.assertEquals(self.calculate(-339232432, 2104653154), 1851081710)

    def test0786(self):
        self.assertEquals(self.calculate(-1112516762, -765972555), -346544207)

    def test0787(self):
        self.assertEquals(self.calculate(-318537196, -1391265842), 1072728646)

    def test0788(self):
        self.assertEquals(self.calculate(-1901322077, 1958870067), 434775152)

    def test0789(self):
        self.assertEquals(self.calculate(-1168076148, 1355046586), 1771844562)

    def test0790(self):
        self.assertEquals(self.calculate(-1310835420, -421113341), -889722079)

    def test0791(self):
        self.assertEquals(self.calculate(2113588585, 1772232440), 341356145)

    def test0792(self):
        self.assertEquals(self.calculate(1512260426, -987376081), -1795330789)

    def test0793(self):
        self.assertEquals(self.calculate(-1855061770, -945905394), -909156376)

    def test0794(self):
        self.assertEquals(self.calculate(1910355246, -56477691), 1966832937)

    def test0795(self):
        self.assertEquals(self.calculate(-373854526, -1066008092), 692153566)

    def test0796(self):
        self.assertEquals(self.calculate(132714778, -1988429170), 2121143948)

    def test0797(self):
        self.assertEquals(self.calculate(-29700092, 650247364), -679947456)

    def test0798(self):
        self.assertEquals(self.calculate(1932948861, 428470211), 1504478650)

    def test0799(self):
        self.assertEquals(self.calculate(-1767696086, 1357252940), 1170018270)

    def test0800(self):
        self.assertEquals(self.calculate(1922658899, 387344825), 1535314074)

    def test0801(self):
        self.assertEquals(self.calculate(-1641428628, -65771622), -1575657006)

    def test0802(self):
        self.assertEquals(self.calculate(-980917089, 1722515929), 1591534278)

    def test0803(self):
        self.assertEquals(self.calculate(250981388, 1838274640), -1587293252)

    def test0804(self):
        self.assertEquals(self.calculate(223144326, -892488801), 1115633127)

    def test0805(self):
        self.assertEquals(self.calculate(-1092481752, 582215995), -1674697747)

    def test0806(self):
        self.assertEquals(self.calculate(755827185, 2098600423), -1342773238)

    def test0807(self):
        self.assertEquals(self.calculate(-1405355177, 1766978915), 1122633204)

    def test0808(self):
        self.assertEquals(self.calculate(1768840126, -164425184), 1933265310)

    def test0809(self):
        self.assertEquals(self.calculate(1256009818, 1303557374), -47547556)

    def test0810(self):
        self.assertEquals(self.calculate(1761738504, 659796785), 1101941719)

    def test0811(self):
        self.assertEquals(self.calculate(-1729178664, -2070893741), 341715077)

    def test0812(self):
        self.assertEquals(self.calculate(-939964093, 702468908), -1642433001)

    def test0813(self):
        self.assertEquals(self.calculate(-169473372, -2060649523), 1891176151)

    def test0814(self):
        self.assertEquals(self.calculate(408336141, 1741204818), -1332868677)

    def test0815(self):
        self.assertEquals(self.calculate(-2097406684, -1458669332), -638737352)

    def test0816(self):
        self.assertEquals(self.calculate(-1495504869, -1667839747), 172334878)

    def test0817(self):
        self.assertEquals(self.calculate(-1724815505, 275570274), -2000385779)

    def test0818(self):
        self.assertEquals(self.calculate(-1875917921, -19202087), -1856715834)

    def test0819(self):
        self.assertEquals(self.calculate(1173781173, -736614830), 1910396003)

    def test0820(self):
        self.assertEquals(self.calculate(1065855026, -1157661819), -2071450451)

    def test0821(self):
        self.assertEquals(self.calculate(198389527, 532060223), -333670696)

    def test0822(self):
        self.assertEquals(self.calculate(72958661, 1883131274), -1810172613)

    def test0823(self):
        self.assertEquals(self.calculate(-907667101, -1601608902), 693941801)

    def test0824(self):
        self.assertEquals(self.calculate(15754952, 1337552893), -1321797941)

    def test0825(self):
        self.assertEquals(self.calculate(-889303294, -1860140774), 970837480)

    def test0826(self):
        self.assertEquals(self.calculate(1362364456, 913927754), 448436702)

    def test0827(self):
        self.assertEquals(self.calculate(1782233667, -1820631898), -692101731)

    def test0828(self):
        self.assertEquals(self.calculate(753429324, 1219570596), -466141272)

    def test0829(self):
        self.assertEquals(self.calculate(-641668430, -1839114415), 1197445985)

    def test0830(self):
        self.assertEquals(self.calculate(-1315528809, 1444880378), 1534558109)

    def test0831(self):
        self.assertEquals(self.calculate(-1047562240, 1822701598), 1424703458)

    def test0832(self):
        self.assertEquals(self.calculate(1296154017, 1628835797), -332681780)

    def test0833(self):
        self.assertEquals(self.calculate(-38197366, 1231492020), -1269689386)

    def test0834(self):
        self.assertEquals(self.calculate(1786661982, 654838531), 1131823451)

    def test0835(self):
        self.assertEquals(self.calculate(-689812813, 2123700591), 1481453892)

    def test0836(self):
        self.assertEquals(self.calculate(-310549814, -246142283), -64407531)

    def test0837(self):
        self.assertEquals(self.calculate(-1424610626, 106444267), -1531054893)

    def test0838(self):
        self.assertEquals(self.calculate(2064070215, 1743385301), 320684914)

    def test0839(self):
        self.assertEquals(self.calculate(-1163152845, -244778334), -918374511)

    def test0840(self):
        self.assertEquals(self.calculate(842121106, -878032278), 1720153384)

    def test0841(self):
        self.assertEquals(self.calculate(1180093019, -1173480551), -1941393726)

    def test0842(self):
        self.assertEquals(self.calculate(1715086314, -964760003), -1615120979)

    def test0843(self):
        self.assertEquals(self.calculate(-1755037393, 1429789645), 1110140258)

    def test0844(self):
        self.assertEquals(self.calculate(1126928019, -680807532), 1807735551)

    def test0845(self):
        self.assertEquals(self.calculate(546523373, -341106849), 887630222)

    def test0846(self):
        self.assertEquals(self.calculate(790846288, 179339866), 611506422)

    def test0847(self):
        self.assertEquals(self.calculate(-764524536, -1114883064), 350358528)

    def test0848(self):
        self.assertEquals(self.calculate(-157300904, -315077566), 157776662)

    def test0849(self):
        self.assertEquals(self.calculate(-1339269533, 1461821327), 1493876436)

    def test0850(self):
        self.assertEquals(self.calculate(-1007657879, 638597466), -1646255345)

    def test0851(self):
        self.assertEquals(self.calculate(-1104456431, 1215249222), 1975261643)

    def test0852(self):
        self.assertEquals(self.calculate(-2023535773, 1173137303), 1098294220)

    def test0853(self):
        self.assertEquals(self.calculate(793067593, 826865287), -33797694)

    def test0854(self):
        self.assertEquals(self.calculate(-1413816382, 56599015), -1470415397)

    def test0855(self):
        self.assertEquals(self.calculate(-349351784, 1091623640), -1440975424)

    def test0856(self):
        self.assertEquals(self.calculate(-139356924, 1531696903), -1671053827)

    def test0857(self):
        self.assertEquals(self.calculate(-1389820283, 1507695231), 1397451782)

    def test0858(self):
        self.assertEquals(self.calculate(751792338, 832323282), -80530944)

    def test0859(self):
        self.assertEquals(self.calculate(-718578055, -544132597), -174445458)

    def test0860(self):
        self.assertEquals(self.calculate(1613293765, 513468928), 1099824837)

    def test0861(self):
        self.assertEquals(self.calculate(-119271273, 464158379), -583429652)

    def test0862(self):
        self.assertEquals(self.calculate(1493297888, -1345901608), -1455767800)

    def test0863(self):
        self.assertEquals(self.calculate(-168739610, 2031923208), 2094304478)

    def test0864(self):
        self.assertEquals(self.calculate(-110654308, 198929586), -309583894)

    def test0865(self):
        self.assertEquals(self.calculate(682957288, -1074726657), 1757683945)

    def test0866(self):
        self.assertEquals(self.calculate(-1253346831, -2107515455), 854168624)

    def test0867(self):
        self.assertEquals(self.calculate(-543884733, 402935291), -946820024)

    def test0868(self):
        self.assertEquals(self.calculate(-291306951, 2102121284), 1901539061)

    def test0869(self):
        self.assertEquals(self.calculate(-1560557418, -621229635), -939327783)

    def test0870(self):
        self.assertEquals(self.calculate(-2084743584, 312676734), 1897546978)

    def test0871(self):
        self.assertEquals(self.calculate(-1978879331, -1873151), -1977006180)

    def test0872(self):
        self.assertEquals(self.calculate(-353121567, 2034339353), 1907506376)

    def test0873(self):
        self.assertEquals(self.calculate(-242378321, 608301148), -850679469)

    def test0874(self):
        self.assertEquals(self.calculate(1735161522, 1975986087), -240824565)

    def test0875(self):
        self.assertEquals(self.calculate(-1608004919, 1845441078), 841521299)

    def test0876(self):
        self.assertEquals(self.calculate(1264301489, -93066698), 1357368187)

    def test0877(self):
        self.assertEquals(self.calculate(1403593012, -423847039), 1827440051)

    def test0878(self):
        self.assertEquals(self.calculate(550484152, 1133841369), -583357217)

    def test0879(self):
        self.assertEquals(self.calculate(1410041677, -105356059), 1515397736)

    def test0880(self):
        self.assertEquals(self.calculate(-580442581, -608916865), 28474284)

    def test0881(self):
        self.assertEquals(self.calculate(549575461, -940026811), 1489602272)

    def test0882(self):
        self.assertEquals(self.calculate(513733316, 1044111004), -530377688)

    def test0883(self):
        self.assertEquals(self.calculate(-384989004, 1230546293), -1615535297)

    def test0884(self):
        self.assertEquals(self.calculate(-533893344, -1059141767), 525248423)

    def test0885(self):
        self.assertEquals(self.calculate(-414502319, -1474538653), 1060036334)

    def test0886(self):
        self.assertEquals(self.calculate(730272553, 1222509626), -492237073)

    def test0887(self):
        self.assertEquals(self.calculate(377496987, 1137992633), -760495646)

    def test0888(self):
        self.assertEquals(self.calculate(1454052116, -208916415), 1662968531)

    def test0889(self):
        self.assertEquals(self.calculate(-482036548, 1288046486), -1770083034)

    def test0890(self):
        self.assertEquals(self.calculate(231838254, -781936557), 1013774811)

    def test0891(self):
        self.assertEquals(self.calculate(-253754067, -1363314464), 1109560397)

    def test0892(self):
        self.assertEquals(self.calculate(1331123126, 1043055397), 288067729)

    def test0893(self):
        self.assertEquals(self.calculate(-1706735934, 1777083828), 811147534)

    def test0894(self):
        self.assertEquals(self.calculate(-1725691193, -2117472359), 391781166)

    def test0895(self):
        self.assertEquals(self.calculate(1405550256, -1968142310), -921274730)

    def test0896(self):
        self.assertEquals(self.calculate(1994581262, -1850644510), -449741524)

    def test0897(self):
        self.assertEquals(self.calculate(-182297559, -1541879491), 1359581932)

    def test0898(self):
        self.assertEquals(self.calculate(1591824185, 495328105), 1096496080)

    def test0899(self):
        self.assertEquals(self.calculate(-29121191, 1730777346), -1759898537)

    def test0900(self):
        self.assertEquals(self.calculate(-842484782, 392534360), -1235019142)

    def test0901(self):
        self.assertEquals(self.calculate(-1949595884, -1929070969), -20524915)

    def test0902(self):
        self.assertEquals(self.calculate(-1995155239, -1288264673), -706890566)

    def test0903(self):
        self.assertEquals(self.calculate(-670203506, -1146821490), 476617984)

    def test0904(self):
        self.assertEquals(self.calculate(-1764993536, -559934255), -1205059281)

    def test0905(self):
        self.assertEquals(self.calculate(2110970880, 111198542), 1999772338)

    def test0906(self):
        self.assertEquals(self.calculate(-1815010711, 360229906), 2119726679)

    def test0907(self):
        self.assertEquals(self.calculate(-305661393, -1633981252), 1328319859)

    def test0908(self):
        self.assertEquals(self.calculate(-468584223, -2116376799), 1647792576)

    def test0909(self):
        self.assertEquals(self.calculate(-1473538534, 225863542), -1699402076)

    def test0910(self):
        self.assertEquals(self.calculate(1179631058, 1757971109), -578340051)

    def test0911(self):
        self.assertEquals(self.calculate(-1888258925, 1459510767), 947197604)

    def test0912(self):
        self.assertEquals(self.calculate(-1209870191, -521783700), -688086491)

    def test0913(self):
        self.assertEquals(self.calculate(494663111, -1639131904), 2133795015)

    def test0914(self):
        self.assertEquals(self.calculate(-473463472, -491582123), 18118651)

    def test0915(self):
        self.assertEquals(self.calculate(-1671172604, -368376331), -1302796273)

    def test0916(self):
        self.assertEquals(self.calculate(1585023717, 1709576596), -124552879)

    def test0917(self):
        self.assertEquals(self.calculate(962860420, -1756429445), -1575677431)

    def test0918(self):
        self.assertEquals(self.calculate(763104870, 1352132772), -589027902)

    def test0919(self):
        self.assertEquals(self.calculate(-653981606, -1039753852), 385772246)

    def test0920(self):
        self.assertEquals(self.calculate(-305654109, -737766949), 432112840)

    def test0921(self):
        self.assertEquals(self.calculate(39792236, -427524916), 467317152)

    def test0922(self):
        self.assertEquals(self.calculate(1132415393, -1680474602), -1482077301)

    def test0923(self):
        self.assertEquals(self.calculate(-477195735, 1637968625), -2115164360)

    def test0924(self):
        self.assertEquals(self.calculate(-908985208, -381723400), -527261808)

    def test0925(self):
        self.assertEquals(self.calculate(-2131186420, 2050556380), 113224496)

    def test0926(self):
        self.assertEquals(self.calculate(1469718247, -1399044889), -1426204160)

    def test0927(self):
        self.assertEquals(self.calculate(358146085, -913856938), 1272003023)

    def test0928(self):
        self.assertEquals(self.calculate(-663279113, 706178399), -1369457512)

    def test0929(self):
        self.assertEquals(self.calculate(-1863548444, -1367569474), -495978970)

    def test0930(self):
        self.assertEquals(self.calculate(-559623808, 1385311449), -1944935257)

    def test0931(self):
        self.assertEquals(self.calculate(525758348, 343032303), 182726045)

    def test0932(self):
        self.assertEquals(self.calculate(17966656, -393661969), 411628625)

    def test0933(self):
        self.assertEquals(self.calculate(-975102275, -1068371139), 93268864)

    def test0934(self):
        self.assertEquals(self.calculate(-992797801, 1591694639), 1710474856)

    def test0935(self):
        self.assertEquals(self.calculate(-778928244, -1007964425), 229036181)

    def test0936(self):
        self.assertEquals(self.calculate(-288213311, 150954412), -439167723)

    def test0937(self):
        self.assertEquals(self.calculate(-1881419782, -573721123), -1307698659)

    def test0938(self):
        self.assertEquals(self.calculate(1860451927, 1445660300), 414791627)

    def test0939(self):
        self.assertEquals(self.calculate(2035442251, 1757753469), 277688782)

    def test0940(self):
        self.assertEquals(self.calculate(-563769346, -1310846234), 747076888)

    def test0941(self):
        self.assertEquals(self.calculate(1098207151, -250821195), 1349028346)

    def test0942(self):
        self.assertEquals(self.calculate(1130119359, 1623679878), -493560519)

    def test0943(self):
        self.assertEquals(self.calculate(1986296113, -333269913), -1975401270)

    def test0944(self):
        self.assertEquals(self.calculate(1641930282, -1126036941), -1527000073)

    def test0945(self):
        self.assertEquals(self.calculate(156651758, 624797641), -468145883)

    def test0946(self):
        self.assertEquals(self.calculate(282480832, -260032480), 542513312)

    def test0947(self):
        self.assertEquals(self.calculate(353051590, 997306440), -644254850)

    def test0948(self):
        self.assertEquals(self.calculate(1312773093, -1652954352), -1329239851)

    def test0949(self):
        self.assertEquals(self.calculate(-912809842, 119224066), -1032033908)

    def test0950(self):
        self.assertEquals(self.calculate(-1398092961, -1048064125), -350028836)

    def test0951(self):
        self.assertEquals(self.calculate(-529419472, -846237671), 316818199)

    def test0952(self):
        self.assertEquals(self.calculate(-438675902, -1777027395), 1338351493)

    def test0953(self):
        self.assertEquals(self.calculate(-765572267, 488044785), -1253617052)

    def test0954(self):
        self.assertEquals(self.calculate(-1835923335, 1943413422), 515630539)

    def test0955(self):
        self.assertEquals(self.calculate(1067005606, -2099442167), -1128519523)

    def test0956(self):
        self.assertEquals(self.calculate(-256752624, -1984032178), 1727279554)

    def test0957(self):
        self.assertEquals(self.calculate(-2133417436, -991871650), -1141545786)

    def test0958(self):
        self.assertEquals(self.calculate(-906990337, -2013176182), 1106185845)

    def test0959(self):
        self.assertEquals(self.calculate(787322239, 98928487), 688393752)

    def test0960(self):
        self.assertEquals(self.calculate(-100348461, 1306954669), -1407303130)

    def test0961(self):
        self.assertEquals(self.calculate(-2131833038, -2080302391), -51530647)

    def test0962(self):
        self.assertEquals(self.calculate(2038102666, 1211292820), 826809846)

    def test0963(self):
        self.assertEquals(self.calculate(236030815, 2038181100), -1802150285)

    def test0964(self):
        self.assertEquals(self.calculate(1788019241, 1635148445), 152870796)

    def test0965(self):
        self.assertEquals(self.calculate(1662746580, -2007714644), -624506072)

    def test0966(self):
        self.assertEquals(self.calculate(-896566583, 894157942), -1790724525)

    def test0967(self):
        self.assertEquals(self.calculate(-820934263, 1672742798), 1801290235)

    def test0968(self):
        self.assertEquals(self.calculate(-443581021, 1567513626), -2011094647)

    def test0969(self):
        self.assertEquals(self.calculate(1027002689, 1386802635), -359799946)

    def test0970(self):
        self.assertEquals(self.calculate(1427102044, 1612392550), -185290506)

    def test0971(self):
        self.assertEquals(self.calculate(-913163081, -453477746), -459685335)

    def test0972(self):
        self.assertEquals(self.calculate(-1549969887, 201083241), -1751053128)

    def test0973(self):
        self.assertEquals(self.calculate(1539059809, -1812316534), -943590953)

    def test0974(self):
        self.assertEquals(self.calculate(582219985, -319809498), 902029483)

    def test0975(self):
        self.assertEquals(self.calculate(1797380202, -1699524001), -798063093)

    def test0976(self):
        self.assertEquals(self.calculate(-1226793458, 924722768), 2143451070)

    def test0977(self):
        self.assertEquals(self.calculate(-1526989174, -501913384), -1025075790)

    def test0978(self):
        self.assertEquals(self.calculate(972468657, 56792762), 915675895)

    def test0979(self):
        self.assertEquals(self.calculate(1356259117, 1144494606), 211764511)

    def test0980(self):
        self.assertEquals(self.calculate(-1518847371, 479886868), -1998734239)

    def test0981(self):
        self.assertEquals(self.calculate(-1004330591, -1995196371), 990865780)

    def test0982(self):
        self.assertEquals(self.calculate(-380995830, -1054466713), 673470883)

    def test0983(self):
        self.assertEquals(self.calculate(848079217, 1002565902), -154486685)

    def test0984(self):
        self.assertEquals(self.calculate(-1728893228, 2135525979), 430548089)

    def test0985(self):
        self.assertEquals(self.calculate(-1016166005, -1733931255), 717765250)

    def test0986(self):
        self.assertEquals(self.calculate(-1761228177, 713400196), 1820338923)

    def test0987(self):
        self.assertEquals(self.calculate(-821752586, -674439523), -147313063)

    def test0988(self):
        self.assertEquals(self.calculate(105059155, 1127022708), -1021963553)

    def test0989(self):
        self.assertEquals(self.calculate(-18537595, 727501867), -746039462)

    def test0990(self):
        self.assertEquals(self.calculate(-1199987304, 1406578877), 1688401115)

    def test0991(self):
        self.assertEquals(self.calculate(775419129, -1962944316), -1556603851)

    def test0992(self):
        self.assertEquals(self.calculate(563713854, -145352089), 709065943)

    def test0993(self):
        self.assertEquals(self.calculate(-1828862980, 1446903347), 1019200969)

    def test0994(self):
        self.assertEquals(self.calculate(2039915549, 1331435797), 708479752)

    def test0995(self):
        self.assertEquals(self.calculate(-201916330, 859836806), -1061753136)

    def test0996(self):
        self.assertEquals(self.calculate(-1864862575, 928065657), 1502039064)

    def test0997(self):
        self.assertEquals(self.calculate(633119677, 1500259127), -867139450)

    def test0998(self):
        self.assertEquals(self.calculate(646910156, -1231954510), 1878864666)

    def test0999(self):
        self.assertEquals(self.calculate(-1874907929, -327658971), -1547248958)

    def test1000(self):
        self.assertEquals(self.calculate(-814772918, -863670735), 48897817)

    def test1001(self):
        self.assertEquals(self.calculate(1036424582, 345344156), 691080426)

    def test1002(self):
        self.assertEquals(self.calculate(-1123031170, 1608888236), 1563047890)

    def test1003(self):
        self.assertEquals(self.calculate(-1000375655, 1297044755), 1997546886)

    def test1004(self):
        self.assertEquals(self.calculate(296773575, -850823178), 1147596753)

    def test1005(self):
        self.assertEquals(self.calculate(7786837, 1736092958), -1728306121)

    def test1006(self):
        self.assertEquals(self.calculate(2064798726, -1758799207), -471369363)

    def test1007(self):
        self.assertEquals(self.calculate(-1654642356, -1692929818), 38287462)

    def test1008(self):
        self.assertEquals(self.calculate(359766443, 2084154469), -1724388026)

    def test1009(self):
        self.assertEquals(self.calculate(-1997038006, -261016746), -1736021260)

    def test1010(self):
        self.assertEquals(self.calculate(1451494874, -1678635033), -1164837389)

    def test1011(self):
        self.assertEquals(self.calculate(807793874, -1552449860), -1934723562)

    def test1012(self):
        self.assertEquals(self.calculate(-1147475494, 635074739), -1782550233)

    def test1013(self):
        self.assertEquals(self.calculate(-1641559780, 1479740345), 1173667171)

    def test1014(self):
        self.assertEquals(self.calculate(-1084225050, -1052961895), -31263155)

    def test1015(self):
        self.assertEquals(self.calculate(-436243580, -545789047), 109545467)

    def test1016(self):
        self.assertEquals(self.calculate(-1279664291, 1212835207), 1802467798)

    def test1017(self):
        self.assertEquals(self.calculate(923942378, -233918862), 1157861240)

    def test1018(self):
        self.assertEquals(self.calculate(209283990, 1208833021), -999549031)

    def test1019(self):
        self.assertEquals(self.calculate(-246794001, -496036329), 249242328)

    def test1020(self):
        self.assertEquals(self.calculate(-789537202, -1839152266), 1049615064)

    def test1021(self):
        self.assertEquals(self.calculate(-1724236227, -1782907893), 58671666)

    def test1022(self):
        self.assertEquals(self.calculate(1826639082, -984728691), -1483599523)

    def test1023(self):
        self.assertEquals(self.calculate(-1943002580, 1315059464), 1036905252)


class TestVM_Sub_LongFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushF(rhs)
        v.VM_Sub()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-1724397366, -24216.0), -1724373150.00)

    def test0001(self):
        self.assertEquals(self.calculate(-74877820, 62831.0), -74940651.00)

    def test0002(self):
        self.assertEquals(self.calculate(1036793281, 36300.0), 1036756981.00)

    def test0003(self):
        self.assertEquals(self.calculate(773635525, -112547.0), 773748072.00)

    def test0004(self):
        self.assertEquals(self.calculate(5442760, -32299.0), 5475059.00)

    def test0005(self):
        self.assertEquals(self.calculate(-1291053754, 111102.0), -1291164856.00)

    def test0006(self):
        self.assertEquals(self.calculate(-1212454997, 44761.0), -1212499758.00)

    def test0007(self):
        self.assertEquals(self.calculate(2065380819, -104069.0), 2065484888.00)

    def test0008(self):
        self.assertEquals(self.calculate(1057024846, -6208.0), 1057031054.00)

    def test0009(self):
        self.assertEquals(self.calculate(-1578354793, 133993.0), -1578488786.00)

    def test0010(self):
        self.assertEquals(self.calculate(-239916131, -63963.0), -239852168.00)

    def test0011(self):
        self.assertEquals(self.calculate(122883248, -46651.0), 122929899.00)

    def test0012(self):
        self.assertEquals(self.calculate(-121329478, 41437.0), -121370915.00)

    def test0013(self):
        self.assertEquals(self.calculate(911988560, -89258.0), 912077818.00)

    def test0014(self):
        self.assertEquals(self.calculate(1055257733, -21757.0), 1055279490.00)

    def test0015(self):
        self.assertEquals(self.calculate(2094666388, 139861.0), 2094526527.00)

    def test0016(self):
        self.assertEquals(self.calculate(-532242507, 154744.0), -532397251.00)

    def test0017(self):
        self.assertEquals(self.calculate(1763209201, 155098.0), 1763054103.00)

    def test0018(self):
        self.assertEquals(self.calculate(-911401678, 14852.0), -911416530.00)

    def test0019(self):
        self.assertEquals(self.calculate(-33144964, 198618.0), -33343582.00)

    def test0020(self):
        self.assertEquals(self.calculate(2046451400, 45693.0), 2046405707.00)

    def test0021(self):
        self.assertEquals(self.calculate(-1972503403, 76749.0), -1972580152.00)

    def test0022(self):
        self.assertEquals(self.calculate(-30079676, 145211.0), -30224887.00)

    def test0023(self):
        self.assertEquals(self.calculate(456972216, 102323.0), 456869893.00)

    def test0024(self):
        self.assertEquals(self.calculate(-1594820732, 34367.0), -1594855099.00)

    def test0025(self):
        self.assertEquals(self.calculate(-823690894, 13308.0), -823704202.00)

    def test0026(self):
        self.assertEquals(self.calculate(-539040902, 86714.0), -539127616.00)

    def test0027(self):
        self.assertEquals(self.calculate(2094676514, 89406.0), 2094587108.00)

    def test0028(self):
        self.assertEquals(self.calculate(1745123692, 129915.0), 1744993777.00)

    def test0029(self):
        self.assertEquals(self.calculate(-811707367, 11632.0), -811718999.00)

    def test0030(self):
        self.assertEquals(self.calculate(1773888779, -117433.0), 1774006212.00)

    def test0031(self):
        self.assertEquals(self.calculate(2093992065, -194976.0), 2094187041.00)

    def test0032(self):
        self.assertEquals(self.calculate(669480561, 73998.0), 669406563.00)

    def test0033(self):
        self.assertEquals(self.calculate(284536575, -146800.0), 284683375.00)

    def test0034(self):
        self.assertEquals(self.calculate(-841679260, 122940.0), -841802200.00)

    def test0035(self):
        self.assertEquals(self.calculate(-834700958, -196595.0), -834504363.00)

    def test0036(self):
        self.assertEquals(self.calculate(1885077576, -108026.0), 1885185602.00)

    def test0037(self):
        self.assertEquals(self.calculate(-998621751, -132474.0), -998489277.00)

    def test0038(self):
        self.assertEquals(self.calculate(-1965761102, -164337.0), -1965596765.00)

    def test0039(self):
        self.assertEquals(self.calculate(-1126525300, -8343.0), -1126516957.00)

    def test0040(self):
        self.assertEquals(self.calculate(-1076807846, 182046.0), -1076989892.00)

    def test0041(self):
        self.assertEquals(self.calculate(1498294351, 101530.0), 1498192821.00)

    def test0042(self):
        self.assertEquals(self.calculate(-952399410, 162187.0), -952561597.00)

    def test0043(self):
        self.assertEquals(self.calculate(-408164106, -82948.0), -408081158.00)

    def test0044(self):
        self.assertEquals(self.calculate(-2141598008, 79607.0), -2141677615.00)

    def test0045(self):
        self.assertEquals(self.calculate(-116305490, 98559.0), -116404049.00)

    def test0046(self):
        self.assertEquals(self.calculate(34945700, 67630.0), 34878070.00)

    def test0047(self):
        self.assertEquals(self.calculate(392158074, 148243.0), 392009831.00)

    def test0048(self):
        self.assertEquals(self.calculate(-1786745603, -143240.0), -1786602363.00)

    def test0049(self):
        self.assertEquals(self.calculate(839742383, -73264.0), 839815647.00)

    def test0050(self):
        self.assertEquals(self.calculate(-236684500, -112606.0), -236571894.00)

    def test0051(self):
        self.assertEquals(self.calculate(200392657, -194314.0), 200586971.00)

    def test0052(self):
        self.assertEquals(self.calculate(1873967980, -22958.0), 1873990938.00)

    def test0053(self):
        self.assertEquals(self.calculate(-2040888579, -168950.0), -2040719629.00)

    def test0054(self):
        self.assertEquals(self.calculate(1625490461, 11053.0), 1625479408.00)

    def test0055(self):
        self.assertEquals(self.calculate(533871149, 122527.0), 533748622.00)

    def test0056(self):
        self.assertEquals(self.calculate(-1566796369, -53573.0), -1566742796.00)

    def test0057(self):
        self.assertEquals(self.calculate(-2081100891, 33320.0), -2081134211.00)

    def test0058(self):
        self.assertEquals(self.calculate(1990802452, 114368.0), 1990688084.00)

    def test0059(self):
        self.assertEquals(self.calculate(125088222, 165191.0), 124923031.00)

    def test0060(self):
        self.assertEquals(self.calculate(-1285387583, -165707.0), -1285221876.00)

    def test0061(self):
        self.assertEquals(self.calculate(1816164849, -188473.0), 1816353322.00)

    def test0062(self):
        self.assertEquals(self.calculate(18251276, 193818.0), 18057458.00)

    def test0063(self):
        self.assertEquals(self.calculate(1043920166, -20897.0), 1043941063.00)

    def test0064(self):
        self.assertEquals(self.calculate(280612887, 43445.0), 280569442.00)

    def test0065(self):
        self.assertEquals(self.calculate(379598101, 34288.0), 379563813.00)

    def test0066(self):
        self.assertEquals(self.calculate(1908477171, -156295.0), 1908633466.00)

    def test0067(self):
        self.assertEquals(self.calculate(2064169108, -123690.0), 2064292798.00)

    def test0068(self):
        self.assertEquals(self.calculate(-1843609254, 124980.0), -1843734234.00)

    def test0069(self):
        self.assertEquals(self.calculate(124133671, 7773.0), 124125898.00)

    def test0070(self):
        self.assertEquals(self.calculate(1650618871, -150146.0), 1650769017.00)

    def test0071(self):
        self.assertEquals(self.calculate(-589964806, 49835.0), -590014641.00)

    def test0072(self):
        self.assertEquals(self.calculate(-955693521, 5052.0), -955698573.00)

    def test0073(self):
        self.assertEquals(self.calculate(798811278, -106555.0), 798917833.00)

    def test0074(self):
        self.assertEquals(self.calculate(829937171, 145143.0), 829792028.00)

    def test0075(self):
        self.assertEquals(self.calculate(1445729492, -123355.0), 1445852847.00)

    def test0076(self):
        self.assertEquals(self.calculate(1953034004, 105691.0), 1952928313.00)

    def test0077(self):
        self.assertEquals(self.calculate(-2007163540, -151498.0), -2007012042.00)

    def test0078(self):
        self.assertEquals(self.calculate(-89965360, 117136.0), -90082496.00)

    def test0079(self):
        self.assertEquals(self.calculate(863410016, -171467.0), 863581483.00)

    def test0080(self):
        self.assertEquals(self.calculate(-942184850, 83860.0), -942268710.00)

    def test0081(self):
        self.assertEquals(self.calculate(-356703655, 156102.0), -356859757.00)

    def test0082(self):
        self.assertEquals(self.calculate(-1224731144, -136966.0), -1224594178.00)

    def test0083(self):
        self.assertEquals(self.calculate(-1789769597, 112598.0), -1789882195.00)

    def test0084(self):
        self.assertEquals(self.calculate(-1080534469, 38841.0), -1080573310.00)

    def test0085(self):
        self.assertEquals(self.calculate(2016109431, -164036.0), 2016273467.00)

    def test0086(self):
        self.assertEquals(self.calculate(745447115, -93953.0), 745541068.00)

    def test0087(self):
        self.assertEquals(self.calculate(-1622749071, -709.0), -1622748362.00)

    def test0088(self):
        self.assertEquals(self.calculate(1954407927, 32389.0), 1954375538.00)

    def test0089(self):
        self.assertEquals(self.calculate(-474391885, 84496.0), -474476381.00)

    def test0090(self):
        self.assertEquals(self.calculate(1788067547, -71302.0), 1788138849.00)

    def test0091(self):
        self.assertEquals(self.calculate(953540745, -175326.0), 953716071.00)

    def test0092(self):
        self.assertEquals(self.calculate(1356318483, 52423.0), 1356266060.00)

    def test0093(self):
        self.assertEquals(self.calculate(-1688598521, 65162.0), -1688663683.00)

    def test0094(self):
        self.assertEquals(self.calculate(1176555814, -160631.0), 1176716445.00)

    def test0095(self):
        self.assertEquals(self.calculate(1775948273, -172735.0), 1776121008.00)

    def test0096(self):
        self.assertEquals(self.calculate(-1951578110, -10496.0), -1951567614.00)

    def test0097(self):
        self.assertEquals(self.calculate(-1813214769, 124128.0), -1813338897.00)

    def test0098(self):
        self.assertEquals(self.calculate(2084904373, 292.0), 2084904081.00)

    def test0099(self):
        self.assertEquals(self.calculate(1235303192, 73567.0), 1235229625.00)

    def test0100(self):
        self.assertEquals(self.calculate(284575008, 21555.0), 284553453.00)

    def test0101(self):
        self.assertEquals(self.calculate(1100658220, 169462.0), 1100488758.00)

    def test0102(self):
        self.assertEquals(self.calculate(-941526465, 96177.0), -941622642.00)

    def test0103(self):
        self.assertEquals(self.calculate(-2053542188, 81524.0), -2053623712.00)

    def test0104(self):
        self.assertEquals(self.calculate(-495239941, 74702.0), -495314643.00)

    def test0105(self):
        self.assertEquals(self.calculate(1486420599, 142453.0), 1486278146.00)

    def test0106(self):
        self.assertEquals(self.calculate(-119772599, -91225.0), -119681374.00)

    def test0107(self):
        self.assertEquals(self.calculate(812388397, 7593.0), 812380804.00)

    def test0108(self):
        self.assertEquals(self.calculate(767055337, 68695.0), 766986642.00)

    def test0109(self):
        self.assertEquals(self.calculate(75861972, 194208.0), 75667764.00)

    def test0110(self):
        self.assertEquals(self.calculate(-1246360554, -110939.0), -1246249615.00)

    def test0111(self):
        self.assertEquals(self.calculate(429770221, 101727.0), 429668494.00)

    def test0112(self):
        self.assertEquals(self.calculate(-566696215, -195629.0), -566500586.00)

    def test0113(self):
        self.assertEquals(self.calculate(-809110236, 176793.0), -809287029.00)

    def test0114(self):
        self.assertEquals(self.calculate(1317882564, 100072.0), 1317782492.00)

    def test0115(self):
        self.assertEquals(self.calculate(-100799815, 65806.0), -100865621.00)

    def test0116(self):
        self.assertEquals(self.calculate(-832403832, 106117.0), -832509949.00)

    def test0117(self):
        self.assertEquals(self.calculate(-1729127102, 19883.0), -1729146985.00)

    def test0118(self):
        self.assertEquals(self.calculate(2020689334, -114362.0), 2020803696.00)

    def test0119(self):
        self.assertEquals(self.calculate(-416488594, -131956.0), -416356638.00)

    def test0120(self):
        self.assertEquals(self.calculate(-1088609010, 6779.0), -1088615789.00)

    def test0121(self):
        self.assertEquals(self.calculate(2141405963, -38271.0), 2141444234.00)

    def test0122(self):
        self.assertEquals(self.calculate(-1663085213, 38467.0), -1663123680.00)

    def test0123(self):
        self.assertEquals(self.calculate(830130589, 145849.0), 829984740.00)

    def test0124(self):
        self.assertEquals(self.calculate(-1832852475, -83644.0), -1832768831.00)

    def test0125(self):
        self.assertEquals(self.calculate(1930000550, -124200.0), 1930124750.00)

    def test0126(self):
        self.assertEquals(self.calculate(1004371036, 23218.0), 1004347818.00)

    def test0127(self):
        self.assertEquals(self.calculate(-337462803, -77580.0), -337385223.00)

    def test0128(self):
        self.assertEquals(self.calculate(1562762155, -166512.0), 1562928667.00)

    def test0129(self):
        self.assertEquals(self.calculate(1657283521, -158331.0), 1657441852.00)

    def test0130(self):
        self.assertEquals(self.calculate(808083520, 14626.0), 808068894.00)

    def test0131(self):
        self.assertEquals(self.calculate(1748526264, 85504.0), 1748440760.00)

    def test0132(self):
        self.assertEquals(self.calculate(-1385003, 35361.0), -1420364.00)

    def test0133(self):
        self.assertEquals(self.calculate(166570965, 150696.0), 166420269.00)

    def test0134(self):
        self.assertEquals(self.calculate(357414260, 2646.0), 357411614.00)

    def test0135(self):
        self.assertEquals(self.calculate(1049624908, -79012.0), 1049703920.00)

    def test0136(self):
        self.assertEquals(self.calculate(-1969763078, -128833.0), -1969634245.00)

    def test0137(self):
        self.assertEquals(self.calculate(622762581, 190239.0), 622572342.00)

    def test0138(self):
        self.assertEquals(self.calculate(-1395450782, 36575.0), -1395487357.00)

    def test0139(self):
        self.assertEquals(self.calculate(1722952454, 49916.0), 1722902538.00)

    def test0140(self):
        self.assertEquals(self.calculate(-1721474069, -87576.0), -1721386493.00)

    def test0141(self):
        self.assertEquals(self.calculate(1534063925, -66401.0), 1534130326.00)

    def test0142(self):
        self.assertEquals(self.calculate(941093801, 72933.0), 941020868.00)

    def test0143(self):
        self.assertEquals(self.calculate(842809537, -8510.0), 842818047.00)

    def test0144(self):
        self.assertEquals(self.calculate(638964980, 124541.0), 638840439.00)

    def test0145(self):
        self.assertEquals(self.calculate(-134331626, -169207.0), -134162419.00)

    def test0146(self):
        self.assertEquals(self.calculate(34880026, 75727.0), 34804299.00)

    def test0147(self):
        self.assertEquals(self.calculate(-2118085488, -180408.0), -2117905080.00)

    def test0148(self):
        self.assertEquals(self.calculate(-767743054, -107342.0), -767635712.00)

    def test0149(self):
        self.assertEquals(self.calculate(1263619493, 107946.0), 1263511547.00)

    def test0150(self):
        self.assertEquals(self.calculate(1210082445, -50639.0), 1210133084.00)

    def test0151(self):
        self.assertEquals(self.calculate(-110943636, 56413.0), -111000049.00)

    def test0152(self):
        self.assertEquals(self.calculate(1866899362, 109876.0), 1866789486.00)

    def test0153(self):
        self.assertEquals(self.calculate(1909256903, 34517.0), 1909222386.00)

    def test0154(self):
        self.assertEquals(self.calculate(-417223903, 167392.0), -417391295.00)

    def test0155(self):
        self.assertEquals(self.calculate(1001002116, 33248.0), 1000968868.00)

    def test0156(self):
        self.assertEquals(self.calculate(-14279156, -152664.0), -14126492.00)

    def test0157(self):
        self.assertEquals(self.calculate(-1676746262, -193045.0), -1676553217.00)

    def test0158(self):
        self.assertEquals(self.calculate(-1625135109, 126173.0), -1625261282.00)

    def test0159(self):
        self.assertEquals(self.calculate(1430024630, 36357.0), 1429988273.00)

    def test0160(self):
        self.assertEquals(self.calculate(683535843, 79960.0), 683455883.00)

    def test0161(self):
        self.assertEquals(self.calculate(-1054575352, 32794.0), -1054608146.00)

    def test0162(self):
        self.assertEquals(self.calculate(-2001551506, -90258.0), -2001461248.00)

    def test0163(self):
        self.assertEquals(self.calculate(-1698859732, 65539.0), -1698925271.00)

    def test0164(self):
        self.assertEquals(self.calculate(-1102804949, -62645.0), -1102742304.00)

    def test0165(self):
        self.assertEquals(self.calculate(484669633, 37735.0), 484631898.00)

    def test0166(self):
        self.assertEquals(self.calculate(61249687, 143790.0), 61105897.00)

    def test0167(self):
        self.assertEquals(self.calculate(-1986489189, -124395.0), -1986364794.00)

    def test0168(self):
        self.assertEquals(self.calculate(742828156, 66253.0), 742761903.00)

    def test0169(self):
        self.assertEquals(self.calculate(1545979954, 135115.0), 1545844839.00)

    def test0170(self):
        self.assertEquals(self.calculate(-353793307, -150064.0), -353643243.00)

    def test0171(self):
        self.assertEquals(self.calculate(226522586, -143447.0), 226666033.00)

    def test0172(self):
        self.assertEquals(self.calculate(1576024401, 82653.0), 1575941748.00)

    def test0173(self):
        self.assertEquals(self.calculate(345307195, 17821.0), 345289374.00)

    def test0174(self):
        self.assertEquals(self.calculate(-411827354, 161817.0), -411989171.00)

    def test0175(self):
        self.assertEquals(self.calculate(-940716579, 70715.0), -940787294.00)

    def test0176(self):
        self.assertEquals(self.calculate(1178651226, -2491.0), 1178653717.00)

    def test0177(self):
        self.assertEquals(self.calculate(1800548448, 14864.0), 1800533584.00)

    def test0178(self):
        self.assertEquals(self.calculate(1379484248, 10076.0), 1379474172.00)

    def test0179(self):
        self.assertEquals(self.calculate(1480084142, 64998.0), 1480019144.00)

    def test0180(self):
        self.assertEquals(self.calculate(-1812457009, -181745.0), -1812275264.00)

    def test0181(self):
        self.assertEquals(self.calculate(-1859975193, -89675.0), -1859885518.00)

    def test0182(self):
        self.assertEquals(self.calculate(-445716878, -2172.0), -445714706.00)

    def test0183(self):
        self.assertEquals(self.calculate(-934612887, -142631.0), -934470256.00)

    def test0184(self):
        self.assertEquals(self.calculate(-1964744572, -127056.0), -1964617516.00)

    def test0185(self):
        self.assertEquals(self.calculate(526167598, 50289.0), 526117309.00)

    def test0186(self):
        self.assertEquals(self.calculate(838779627, 190901.0), 838588726.00)

    def test0187(self):
        self.assertEquals(self.calculate(1593095698, 88871.0), 1593006827.00)

    def test0188(self):
        self.assertEquals(self.calculate(-209960835, -143472.0), -209817363.00)

    def test0189(self):
        self.assertEquals(self.calculate(991173665, 89165.0), 991084500.00)

    def test0190(self):
        self.assertEquals(self.calculate(886286442, 21024.0), 886265418.00)

    def test0191(self):
        self.assertEquals(self.calculate(-1359474772, -190654.0), -1359284118.00)

    def test0192(self):
        self.assertEquals(self.calculate(-50411607, 186028.0), -50597635.00)

    def test0193(self):
        self.assertEquals(self.calculate(-995831456, -82220.0), -995749236.00)

    def test0194(self):
        self.assertEquals(self.calculate(-448436902, -36509.0), -448400393.00)

    def test0195(self):
        self.assertEquals(self.calculate(-427204772, 143428.0), -427348200.00)

    def test0196(self):
        self.assertEquals(self.calculate(758979573, 73390.0), 758906183.00)

    def test0197(self):
        self.assertEquals(self.calculate(-1607871328, 69046.0), -1607940374.00)

    def test0198(self):
        self.assertEquals(self.calculate(-1119398445, -199425.0), -1119199020.00)

    def test0199(self):
        self.assertEquals(self.calculate(-114213310, -95614.0), -114117696.00)

    def test0200(self):
        self.assertEquals(self.calculate(2041635542, 22499.0), 2041613043.00)

    def test0201(self):
        self.assertEquals(self.calculate(-753513548, 145500.0), -753659048.00)

    def test0202(self):
        self.assertEquals(self.calculate(-1561656841, 81202.0), -1561738043.00)

    def test0203(self):
        self.assertEquals(self.calculate(1732883311, 164172.0), 1732719139.00)

    def test0204(self):
        self.assertEquals(self.calculate(1634103987, -56177.0), 1634160164.00)

    def test0205(self):
        self.assertEquals(self.calculate(784493412, 91591.0), 784401821.00)

    def test0206(self):
        self.assertEquals(self.calculate(1005823665, -70027.0), 1005893692.00)

    def test0207(self):
        self.assertEquals(self.calculate(-1190106189, 154794.0), -1190260983.00)

    def test0208(self):
        self.assertEquals(self.calculate(1876574457, -127438.0), 1876701895.00)

    def test0209(self):
        self.assertEquals(self.calculate(864307341, 99857.0), 864207484.00)

    def test0210(self):
        self.assertEquals(self.calculate(-667990858, 160263.0), -668151121.00)

    def test0211(self):
        self.assertEquals(self.calculate(-1423502355, 137226.0), -1423639581.00)

    def test0212(self):
        self.assertEquals(self.calculate(1875067243, -35284.0), 1875102527.00)

    def test0213(self):
        self.assertEquals(self.calculate(-1677351542, 3241.0), -1677354783.00)

    def test0214(self):
        self.assertEquals(self.calculate(1295941534, 81383.0), 1295860151.00)

    def test0215(self):
        self.assertEquals(self.calculate(451960482, -45087.0), 452005569.00)

    def test0216(self):
        self.assertEquals(self.calculate(-1398944777, -175389.0), -1398769388.00)

    def test0217(self):
        self.assertEquals(self.calculate(-83464899, -84174.0), -83380725.00)

    def test0218(self):
        self.assertEquals(self.calculate(157948742, -17484.0), 157966226.00)

    def test0219(self):
        self.assertEquals(self.calculate(118838273, -100451.0), 118938724.00)

    def test0220(self):
        self.assertEquals(self.calculate(852261986, -102630.0), 852364616.00)

    def test0221(self):
        self.assertEquals(self.calculate(-74654948, 132429.0), -74787377.00)

    def test0222(self):
        self.assertEquals(self.calculate(1353402995, -101815.0), 1353504810.00)

    def test0223(self):
        self.assertEquals(self.calculate(567581170, 142153.0), 567439017.00)

    def test0224(self):
        self.assertEquals(self.calculate(-644454047, -76604.0), -644377443.00)

    def test0225(self):
        self.assertEquals(self.calculate(1444342802, 152925.0), 1444189877.00)

    def test0226(self):
        self.assertEquals(self.calculate(54548474, 100868.0), 54447606.00)

    def test0227(self):
        self.assertEquals(self.calculate(1306980692, 707.0), 1306979985.00)

    def test0228(self):
        self.assertEquals(self.calculate(-548563028, 9079.0), -548572107.00)

    def test0229(self):
        self.assertEquals(self.calculate(1579897762, 66082.0), 1579831680.00)

    def test0230(self):
        self.assertEquals(self.calculate(2068518668, 100481.0), 2068418187.00)

    def test0231(self):
        self.assertEquals(self.calculate(-1939348754, 83362.0), -1939432116.00)

    def test0232(self):
        self.assertEquals(self.calculate(1806251709, -111593.0), 1806363302.00)

    def test0233(self):
        self.assertEquals(self.calculate(969935235, 63005.0), 969872230.00)

    def test0234(self):
        self.assertEquals(self.calculate(-1834907251, -29662.0), -1834877589.00)

    def test0235(self):
        self.assertEquals(self.calculate(455743608, 65376.0), 455678232.00)

    def test0236(self):
        self.assertEquals(self.calculate(-1001750467, -30583.0), -1001719884.00)

    def test0237(self):
        self.assertEquals(self.calculate(-2001035117, -90082.0), -2000945035.00)

    def test0238(self):
        self.assertEquals(self.calculate(-2101196309, -100903.0), -2101095406.00)

    def test0239(self):
        self.assertEquals(self.calculate(-2085707774, -84505.0), -2085623269.00)

    def test0240(self):
        self.assertEquals(self.calculate(1832752683, 30396.0), 1832722287.00)

    def test0241(self):
        self.assertEquals(self.calculate(1574846075, -196342.0), 1575042417.00)

    def test0242(self):
        self.assertEquals(self.calculate(374810145, 122915.0), 374687230.00)

    def test0243(self):
        self.assertEquals(self.calculate(-1227073430, -42211.0), -1227031219.00)

    def test0244(self):
        self.assertEquals(self.calculate(2037644740, -139955.0), 2037784695.00)

    def test0245(self):
        self.assertEquals(self.calculate(1524928969, -147861.0), 1525076830.00)

    def test0246(self):
        self.assertEquals(self.calculate(1026922181, 124316.0), 1026797865.00)

    def test0247(self):
        self.assertEquals(self.calculate(-1985864707, 76477.0), -1985941184.00)

    def test0248(self):
        self.assertEquals(self.calculate(-1467101402, 94658.0), -1467196060.00)

    def test0249(self):
        self.assertEquals(self.calculate(1960365669, -38902.0), 1960404571.00)

    def test0250(self):
        self.assertEquals(self.calculate(2053923534, -3897.0), 2053927431.00)

    def test0251(self):
        self.assertEquals(self.calculate(519559012, 20403.0), 519538609.00)

    def test0252(self):
        self.assertEquals(self.calculate(-1749452853, 170223.0), -1749623076.00)

    def test0253(self):
        self.assertEquals(self.calculate(-1846683518, -100944.0), -1846582574.00)

    def test0254(self):
        self.assertEquals(self.calculate(1201966766, -149295.0), 1202116061.00)

    def test0255(self):
        self.assertEquals(self.calculate(1802033368, -6041.0), 1802039409.00)

    def test0256(self):
        self.assertEquals(self.calculate(1079536602, 127424.0), 1079409178.00)

    def test0257(self):
        self.assertEquals(self.calculate(453556012, 156046.0), 453399966.00)

    def test0258(self):
        self.assertEquals(self.calculate(-1345784136, 142250.0), -1345926386.00)

    def test0259(self):
        self.assertEquals(self.calculate(1403649172, 172387.0), 1403476785.00)

    def test0260(self):
        self.assertEquals(self.calculate(819328489, 135784.0), 819192705.00)

    def test0261(self):
        self.assertEquals(self.calculate(-1915971459, -144084.0), -1915827375.00)

    def test0262(self):
        self.assertEquals(self.calculate(-1312250635, -136492.0), -1312114143.00)

    def test0263(self):
        self.assertEquals(self.calculate(-485090179, -176635.0), -484913544.00)

    def test0264(self):
        self.assertEquals(self.calculate(-2004550237, 112391.0), -2004662628.00)

    def test0265(self):
        self.assertEquals(self.calculate(446545943, -12665.0), 446558608.00)

    def test0266(self):
        self.assertEquals(self.calculate(2145423465, 198565.0), 2145224900.00)

    def test0267(self):
        self.assertEquals(self.calculate(-2047439822, 66605.0), -2047506427.00)

    def test0268(self):
        self.assertEquals(self.calculate(-355762183, 45578.0), -355807761.00)

    def test0269(self):
        self.assertEquals(self.calculate(1578273736, 54757.0), 1578218979.00)

    def test0270(self):
        self.assertEquals(self.calculate(1100247869, 184461.0), 1100063408.00)

    def test0271(self):
        self.assertEquals(self.calculate(-978960670, 81382.0), -979042052.00)

    def test0272(self):
        self.assertEquals(self.calculate(-1436382842, -164672.0), -1436218170.00)

    def test0273(self):
        self.assertEquals(self.calculate(-1963510948, 2551.0), -1963513499.00)

    def test0274(self):
        self.assertEquals(self.calculate(2001918500, -137632.0), 2002056132.00)

    def test0275(self):
        self.assertEquals(self.calculate(-2102092168, -113804.0), -2101978364.00)

    def test0276(self):
        self.assertEquals(self.calculate(3936047, 138908.0), 3797139.00)

    def test0277(self):
        self.assertEquals(self.calculate(1875888487, -34386.0), 1875922873.00)

    def test0278(self):
        self.assertEquals(self.calculate(158964237, 127167.0), 158837070.00)

    def test0279(self):
        self.assertEquals(self.calculate(1334343955, -4480.0), 1334348435.00)

    def test0280(self):
        self.assertEquals(self.calculate(-369397832, -65203.0), -369332629.00)

    def test0281(self):
        self.assertEquals(self.calculate(1783920034, 77548.0), 1783842486.00)

    def test0282(self):
        self.assertEquals(self.calculate(1583520815, 120486.0), 1583400329.00)

    def test0283(self):
        self.assertEquals(self.calculate(-1734562117, -154294.0), -1734407823.00)

    def test0284(self):
        self.assertEquals(self.calculate(-1083974990, -16198.0), -1083958792.00)

    def test0285(self):
        self.assertEquals(self.calculate(282148137, 167075.0), 281981062.00)

    def test0286(self):
        self.assertEquals(self.calculate(-628869380, 6393.0), -628875773.00)

    def test0287(self):
        self.assertEquals(self.calculate(-1956850052, 42245.0), -1956892297.00)

    def test0288(self):
        self.assertEquals(self.calculate(1882680590, 170402.0), 1882510188.00)

    def test0289(self):
        self.assertEquals(self.calculate(851071496, 55018.0), 851016478.00)

    def test0290(self):
        self.assertEquals(self.calculate(632668112, 79540.0), 632588572.00)

    def test0291(self):
        self.assertEquals(self.calculate(-370881088, 194960.0), -371076048.00)

    def test0292(self):
        self.assertEquals(self.calculate(195895484, -186616.0), 196082100.00)

    def test0293(self):
        self.assertEquals(self.calculate(-1200909094, -188638.0), -1200720456.00)

    def test0294(self):
        self.assertEquals(self.calculate(1964646081, 41175.0), 1964604906.00)

    def test0295(self):
        self.assertEquals(self.calculate(677924964, 170480.0), 677754484.00)

    def test0296(self):
        self.assertEquals(self.calculate(-1714682213, 142664.0), -1714824877.00)

    def test0297(self):
        self.assertEquals(self.calculate(591776059, -77671.0), 591853730.00)

    def test0298(self):
        self.assertEquals(self.calculate(-133670657, -175712.0), -133494945.00)

    def test0299(self):
        self.assertEquals(self.calculate(1130184533, 62847.0), 1130121686.00)

    def test0300(self):
        self.assertEquals(self.calculate(714360295, 92520.0), 714267775.00)

    def test0301(self):
        self.assertEquals(self.calculate(-1911890285, -66211.0), -1911824074.00)

    def test0302(self):
        self.assertEquals(self.calculate(365638592, -67788.0), 365706380.00)

    def test0303(self):
        self.assertEquals(self.calculate(790332714, 190361.0), 790142353.00)

    def test0304(self):
        self.assertEquals(self.calculate(1883261572, 142591.0), 1883118981.00)

    def test0305(self):
        self.assertEquals(self.calculate(-1102000307, -188211.0), -1101812096.00)

    def test0306(self):
        self.assertEquals(self.calculate(2094038251, 153247.0), 2093885004.00)

    def test0307(self):
        self.assertEquals(self.calculate(-1931500212, 150628.0), -1931650840.00)

    def test0308(self):
        self.assertEquals(self.calculate(1983273631, 44679.0), 1983228952.00)

    def test0309(self):
        self.assertEquals(self.calculate(764026932, -28864.0), 764055796.00)

    def test0310(self):
        self.assertEquals(self.calculate(-1061012257, -176410.0), -1060835847.00)

    def test0311(self):
        self.assertEquals(self.calculate(2138643831, -192256.0), 2138836087.00)

    def test0312(self):
        self.assertEquals(self.calculate(-1642509586, 118952.0), -1642628538.00)

    def test0313(self):
        self.assertEquals(self.calculate(-1706063329, 59518.0), -1706122847.00)

    def test0314(self):
        self.assertEquals(self.calculate(-1057359168, 16155.0), -1057375323.00)

    def test0315(self):
        self.assertEquals(self.calculate(-1548672944, -56453.0), -1548616491.00)

    def test0316(self):
        self.assertEquals(self.calculate(-644286307, -69180.0), -644217127.00)

    def test0317(self):
        self.assertEquals(self.calculate(2024948116, -192038.0), 2025140154.00)

    def test0318(self):
        self.assertEquals(self.calculate(447613336, 138855.0), 447474481.00)

    def test0319(self):
        self.assertEquals(self.calculate(68864678, -129482.0), 68994160.00)

    def test0320(self):
        self.assertEquals(self.calculate(-605453456, 66498.0), -605519954.00)

    def test0321(self):
        self.assertEquals(self.calculate(123337110, -145181.0), 123482291.00)

    def test0322(self):
        self.assertEquals(self.calculate(-1191364453, 79732.0), -1191444185.00)

    def test0323(self):
        self.assertEquals(self.calculate(-1859716269, 162156.0), -1859878425.00)

    def test0324(self):
        self.assertEquals(self.calculate(484465987, -166541.0), 484632528.00)

    def test0325(self):
        self.assertEquals(self.calculate(-1823189127, -45505.0), -1823143622.00)

    def test0326(self):
        self.assertEquals(self.calculate(367712296, 2199.0), 367710097.00)

    def test0327(self):
        self.assertEquals(self.calculate(-434170574, 173656.0), -434344230.00)

    def test0328(self):
        self.assertEquals(self.calculate(1638079823, 6746.0), 1638073077.00)

    def test0329(self):
        self.assertEquals(self.calculate(-446939544, -42911.0), -446896633.00)

    def test0330(self):
        self.assertEquals(self.calculate(1872868315, -129528.0), 1872997843.00)

    def test0331(self):
        self.assertEquals(self.calculate(-705961566, -150285.0), -705811281.00)

    def test0332(self):
        self.assertEquals(self.calculate(-1050144131, 53446.0), -1050197577.00)

    def test0333(self):
        self.assertEquals(self.calculate(1420929030, -12093.0), 1420941123.00)

    def test0334(self):
        self.assertEquals(self.calculate(-1279214958, 2714.0), -1279217672.00)

    def test0335(self):
        self.assertEquals(self.calculate(231940649, -78081.0), 232018730.00)

    def test0336(self):
        self.assertEquals(self.calculate(-1466131465, -59513.0), -1466071952.00)

    def test0337(self):
        self.assertEquals(self.calculate(1039556732, -165004.0), 1039721736.00)

    def test0338(self):
        self.assertEquals(self.calculate(1315121688, 145817.0), 1314975871.00)

    def test0339(self):
        self.assertEquals(self.calculate(1187450794, -64339.0), 1187515133.00)

    def test0340(self):
        self.assertEquals(self.calculate(-92410545, -75694.0), -92334851.00)

    def test0341(self):
        self.assertEquals(self.calculate(-1754255270, 11342.0), -1754266612.00)

    def test0342(self):
        self.assertEquals(self.calculate(-233106497, -83838.0), -233022659.00)

    def test0343(self):
        self.assertEquals(self.calculate(-1079045867, 119250.0), -1079165117.00)

    def test0344(self):
        self.assertEquals(self.calculate(-1829327167, 19598.0), -1829346765.00)

    def test0345(self):
        self.assertEquals(self.calculate(1137442096, -62437.0), 1137504533.00)

    def test0346(self):
        self.assertEquals(self.calculate(-1527798436, 50004.0), -1527848440.00)

    def test0347(self):
        self.assertEquals(self.calculate(1728554198, 51084.0), 1728503114.00)

    def test0348(self):
        self.assertEquals(self.calculate(-1778327480, 112776.0), -1778440256.00)

    def test0349(self):
        self.assertEquals(self.calculate(920275607, -189608.0), 920465215.00)

    def test0350(self):
        self.assertEquals(self.calculate(836746778, 23670.0), 836723108.00)

    def test0351(self):
        self.assertEquals(self.calculate(-1429039373, -56430.0), -1428982943.00)

    def test0352(self):
        self.assertEquals(self.calculate(2009075565, 106105.0), 2008969460.00)

    def test0353(self):
        self.assertEquals(self.calculate(1735842996, 131928.0), 1735711068.00)

    def test0354(self):
        self.assertEquals(self.calculate(543506240, -176546.0), 543682786.00)

    def test0355(self):
        self.assertEquals(self.calculate(1250049339, 59320.0), 1249990019.00)

    def test0356(self):
        self.assertEquals(self.calculate(-1060130161, 21869.0), -1060152030.00)

    def test0357(self):
        self.assertEquals(self.calculate(-1442976429, -101772.0), -1442874657.00)

    def test0358(self):
        self.assertEquals(self.calculate(34826693, -70142.0), 34896835.00)

    def test0359(self):
        self.assertEquals(self.calculate(266660007, -177378.0), 266837385.00)

    def test0360(self):
        self.assertEquals(self.calculate(1987274133, 133994.0), 1987140139.00)

    def test0361(self):
        self.assertEquals(self.calculate(-1269405134, -111978.0), -1269293156.00)

    def test0362(self):
        self.assertEquals(self.calculate(-1867030437, 14159.0), -1867044596.00)

    def test0363(self):
        self.assertEquals(self.calculate(981639369, -108065.0), 981747434.00)

    def test0364(self):
        self.assertEquals(self.calculate(-267423670, 16715.0), -267440385.00)

    def test0365(self):
        self.assertEquals(self.calculate(1269381345, -134774.0), 1269516119.00)

    def test0366(self):
        self.assertEquals(self.calculate(2096397126, 76388.0), 2096320738.00)

    def test0367(self):
        self.assertEquals(self.calculate(1527194702, -38683.0), 1527233385.00)

    def test0368(self):
        self.assertEquals(self.calculate(-71133738, -124031.0), -71009707.00)

    def test0369(self):
        self.assertEquals(self.calculate(-809349496, 167330.0), -809516826.00)

    def test0370(self):
        self.assertEquals(self.calculate(-1453514863, -42410.0), -1453472453.00)

    def test0371(self):
        self.assertEquals(self.calculate(-279022031, -141586.0), -278880445.00)

    def test0372(self):
        self.assertEquals(self.calculate(1279607184, -181234.0), 1279788418.00)

    def test0373(self):
        self.assertEquals(self.calculate(546046220, 186901.0), 545859319.00)

    def test0374(self):
        self.assertEquals(self.calculate(684455214, 104153.0), 684351061.00)

    def test0375(self):
        self.assertEquals(self.calculate(-1199419258, 79496.0), -1199498754.00)

    def test0376(self):
        self.assertEquals(self.calculate(-1188864454, 91639.0), -1188956093.00)

    def test0377(self):
        self.assertEquals(self.calculate(-968860482, 159060.0), -969019542.00)

    def test0378(self):
        self.assertEquals(self.calculate(-663656292, 128057.0), -663784349.00)

    def test0379(self):
        self.assertEquals(self.calculate(642963256, 17443.0), 642945813.00)

    def test0380(self):
        self.assertEquals(self.calculate(1018637320, -152306.0), 1018789626.00)

    def test0381(self):
        self.assertEquals(self.calculate(328498133, -124125.0), 328622258.00)

    def test0382(self):
        self.assertEquals(self.calculate(-748749947, 27227.0), -748777174.00)

    def test0383(self):
        self.assertEquals(self.calculate(-751877955, -130009.0), -751747946.00)

    def test0384(self):
        self.assertEquals(self.calculate(1966001027, -146189.0), 1966147216.00)

    def test0385(self):
        self.assertEquals(self.calculate(-783911452, 196433.0), -784107885.00)

    def test0386(self):
        self.assertEquals(self.calculate(-474568743, 25613.0), -474594356.00)

    def test0387(self):
        self.assertEquals(self.calculate(490893949, 15161.0), 490878788.00)

    def test0388(self):
        self.assertEquals(self.calculate(1948493498, 99081.0), 1948394417.00)

    def test0389(self):
        self.assertEquals(self.calculate(1302183662, -67963.0), 1302251625.00)

    def test0390(self):
        self.assertEquals(self.calculate(1887239318, 158634.0), 1887080684.00)

    def test0391(self):
        self.assertEquals(self.calculate(-361245508, 48789.0), -361294297.00)

    def test0392(self):
        self.assertEquals(self.calculate(-844151854, -123761.0), -844028093.00)

    def test0393(self):
        self.assertEquals(self.calculate(117640321, -42607.0), 117682928.00)

    def test0394(self):
        self.assertEquals(self.calculate(-801875679, 189031.0), -802064710.00)

    def test0395(self):
        self.assertEquals(self.calculate(-1041812684, 56293.0), -1041868977.00)

    def test0396(self):
        self.assertEquals(self.calculate(-543815011, -87304.0), -543727707.00)

    def test0397(self):
        self.assertEquals(self.calculate(1385179196, 132640.0), 1385046556.00)

    def test0398(self):
        self.assertEquals(self.calculate(1162718837, -79803.0), 1162798640.00)

    def test0399(self):
        self.assertEquals(self.calculate(-1468390813, -24381.0), -1468366432.00)

    def test0400(self):
        self.assertEquals(self.calculate(-717619292, 41492.0), -717660784.00)

    def test0401(self):
        self.assertEquals(self.calculate(2144513193, -29896.0), 2144543089.00)

    def test0402(self):
        self.assertEquals(self.calculate(1005126564, 191726.0), 1004934838.00)

    def test0403(self):
        self.assertEquals(self.calculate(799100488, -76719.0), 799177207.00)

    def test0404(self):
        self.assertEquals(self.calculate(1717007414, 184736.0), 1716822678.00)

    def test0405(self):
        self.assertEquals(self.calculate(1462164940, -61715.0), 1462226655.00)

    def test0406(self):
        self.assertEquals(self.calculate(-2144921533, 72009.0), -2144993542.00)

    def test0407(self):
        self.assertEquals(self.calculate(531767366, 77255.0), 531690111.00)

    def test0408(self):
        self.assertEquals(self.calculate(699088115, 175350.0), 698912765.00)

    def test0409(self):
        self.assertEquals(self.calculate(1237232775, 146850.0), 1237085925.00)

    def test0410(self):
        self.assertEquals(self.calculate(-1317735412, -126020.0), -1317609392.00)

    def test0411(self):
        self.assertEquals(self.calculate(-1028890087, 86300.0), -1028976387.00)

    def test0412(self):
        self.assertEquals(self.calculate(-1119087645, -32802.0), -1119054843.00)

    def test0413(self):
        self.assertEquals(self.calculate(145019231, -92926.0), 145112157.00)

    def test0414(self):
        self.assertEquals(self.calculate(-1343338583, 151754.0), -1343490337.00)

    def test0415(self):
        self.assertEquals(self.calculate(1719344620, -111043.0), 1719455663.00)

    def test0416(self):
        self.assertEquals(self.calculate(-1280427197, -151050.0), -1280276147.00)

    def test0417(self):
        self.assertEquals(self.calculate(1782249113, -122529.0), 1782371642.00)

    def test0418(self):
        self.assertEquals(self.calculate(1345800646, -49242.0), 1345849888.00)

    def test0419(self):
        self.assertEquals(self.calculate(319169173, -86432.0), 319255605.00)

    def test0420(self):
        self.assertEquals(self.calculate(175614594, -988.0), 175615582.00)

    def test0421(self):
        self.assertEquals(self.calculate(163592438, 4101.0), 163588337.00)

    def test0422(self):
        self.assertEquals(self.calculate(-2068830487, 132420.0), -2068962907.00)

    def test0423(self):
        self.assertEquals(self.calculate(-780437673, 183800.0), -780621473.00)

    def test0424(self):
        self.assertEquals(self.calculate(-889600240, -71830.0), -889528410.00)

    def test0425(self):
        self.assertEquals(self.calculate(-1890004427, 165600.0), -1890170027.00)

    def test0426(self):
        self.assertEquals(self.calculate(751038696, 195643.0), 750843053.00)

    def test0427(self):
        self.assertEquals(self.calculate(-1534264563, -198257.0), -1534066306.00)

    def test0428(self):
        self.assertEquals(self.calculate(-1509247688, 195768.0), -1509443456.00)

    def test0429(self):
        self.assertEquals(self.calculate(-1209343181, 67668.0), -1209410849.00)

    def test0430(self):
        self.assertEquals(self.calculate(-363589704, 4650.0), -363594354.00)

    def test0431(self):
        self.assertEquals(self.calculate(2089869376, 191793.0), 2089677583.00)

    def test0432(self):
        self.assertEquals(self.calculate(769250803, -55081.0), 769305884.00)

    def test0433(self):
        self.assertEquals(self.calculate(1606202692, -103682.0), 1606306374.00)

    def test0434(self):
        self.assertEquals(self.calculate(483277764, 170216.0), 483107548.00)

    def test0435(self):
        self.assertEquals(self.calculate(-1791498834, -145674.0), -1791353160.00)

    def test0436(self):
        self.assertEquals(self.calculate(-477684133, 12750.0), -477696883.00)

    def test0437(self):
        self.assertEquals(self.calculate(2126565257, 42551.0), 2126522706.00)

    def test0438(self):
        self.assertEquals(self.calculate(270866438, -17489.0), 270883927.00)

    def test0439(self):
        self.assertEquals(self.calculate(-1103883781, -192906.0), -1103690875.00)

    def test0440(self):
        self.assertEquals(self.calculate(-1443180196, 20227.0), -1443200423.00)

    def test0441(self):
        self.assertEquals(self.calculate(799824292, 86444.0), 799737848.00)

    def test0442(self):
        self.assertEquals(self.calculate(-825395509, -81907.0), -825313602.00)

    def test0443(self):
        self.assertEquals(self.calculate(1579608403, 38430.0), 1579569973.00)

    def test0444(self):
        self.assertEquals(self.calculate(-1841216475, -4346.0), -1841212129.00)

    def test0445(self):
        self.assertEquals(self.calculate(1717079826, 59967.0), 1717019859.00)

    def test0446(self):
        self.assertEquals(self.calculate(831806853, 6641.0), 831800212.00)

    def test0447(self):
        self.assertEquals(self.calculate(2043265117, 184832.0), 2043080285.00)

    def test0448(self):
        self.assertEquals(self.calculate(348278327, -54641.0), 348332968.00)

    def test0449(self):
        self.assertEquals(self.calculate(-2077835427, -62939.0), -2077772488.00)

    def test0450(self):
        self.assertEquals(self.calculate(-1551954264, 50961.0), -1552005225.00)

    def test0451(self):
        self.assertEquals(self.calculate(75571641, -11317.0), 75582958.00)

    def test0452(self):
        self.assertEquals(self.calculate(-1930102217, -26012.0), -1930076205.00)

    def test0453(self):
        self.assertEquals(self.calculate(-2041245893, -6799.0), -2041239094.00)

    def test0454(self):
        self.assertEquals(self.calculate(356756145, -59630.0), 356815775.00)

    def test0455(self):
        self.assertEquals(self.calculate(-530946597, -153323.0), -530793274.00)

    def test0456(self):
        self.assertEquals(self.calculate(1863650852, -183040.0), 1863833892.00)

    def test0457(self):
        self.assertEquals(self.calculate(695617490, 139888.0), 695477602.00)

    def test0458(self):
        self.assertEquals(self.calculate(-49217246, -190425.0), -49026821.00)

    def test0459(self):
        self.assertEquals(self.calculate(980011044, -96400.0), 980107444.00)

    def test0460(self):
        self.assertEquals(self.calculate(-936790577, 16530.0), -936807107.00)

    def test0461(self):
        self.assertEquals(self.calculate(-185441918, -134466.0), -185307452.00)

    def test0462(self):
        self.assertEquals(self.calculate(-237080433, 58600.0), -237139033.00)

    def test0463(self):
        self.assertEquals(self.calculate(-2011051145, 113667.0), -2011164812.00)

    def test0464(self):
        self.assertEquals(self.calculate(-1751153574, -13348.0), -1751140226.00)

    def test0465(self):
        self.assertEquals(self.calculate(-1404398932, -115308.0), -1404283624.00)

    def test0466(self):
        self.assertEquals(self.calculate(-1423603874, 89359.0), -1423693233.00)

    def test0467(self):
        self.assertEquals(self.calculate(908847955, -194815.0), 909042770.00)

    def test0468(self):
        self.assertEquals(self.calculate(1554771562, -174288.0), 1554945850.00)

    def test0469(self):
        self.assertEquals(self.calculate(-47948074, -38419.0), -47909655.00)

    def test0470(self):
        self.assertEquals(self.calculate(1021141037, -118859.0), 1021259896.00)

    def test0471(self):
        self.assertEquals(self.calculate(-400987650, -178362.0), -400809288.00)

    def test0472(self):
        self.assertEquals(self.calculate(156353942, 32011.0), 156321931.00)

    def test0473(self):
        self.assertEquals(self.calculate(1054572942, 46543.0), 1054526399.00)

    def test0474(self):
        self.assertEquals(self.calculate(17150603, -96139.0), 17246742.00)

    def test0475(self):
        self.assertEquals(self.calculate(508151314, 41179.0), 508110135.00)

    def test0476(self):
        self.assertEquals(self.calculate(-925920232, -89334.0), -925830898.00)

    def test0477(self):
        self.assertEquals(self.calculate(-1855396387, 123228.0), -1855519615.00)

    def test0478(self):
        self.assertEquals(self.calculate(912575609, -39540.0), 912615149.00)

    def test0479(self):
        self.assertEquals(self.calculate(-1023744395, -177.0), -1023744218.00)

    def test0480(self):
        self.assertEquals(self.calculate(205972811, -164499.0), 206137310.00)

    def test0481(self):
        self.assertEquals(self.calculate(-1083488238, 135252.0), -1083623490.00)

    def test0482(self):
        self.assertEquals(self.calculate(1139826635, 18206.0), 1139808429.00)

    def test0483(self):
        self.assertEquals(self.calculate(2063912446, -59273.0), 2063971719.00)

    def test0484(self):
        self.assertEquals(self.calculate(-323156291, 45816.0), -323202107.00)

    def test0485(self):
        self.assertEquals(self.calculate(923307154, -30929.0), 923338083.00)

    def test0486(self):
        self.assertEquals(self.calculate(392232681, -140393.0), 392373074.00)

    def test0487(self):
        self.assertEquals(self.calculate(211485606, -89517.0), 211575123.00)

    def test0488(self):
        self.assertEquals(self.calculate(-928590351, 46993.0), -928637344.00)

    def test0489(self):
        self.assertEquals(self.calculate(2052909682, 103666.0), 2052806016.00)

    def test0490(self):
        self.assertEquals(self.calculate(131662320, 158446.0), 131503874.00)

    def test0491(self):
        self.assertEquals(self.calculate(-941840239, 15031.0), -941855270.00)

    def test0492(self):
        self.assertEquals(self.calculate(1656661720, 48055.0), 1656613665.00)

    def test0493(self):
        self.assertEquals(self.calculate(12574320, -84902.0), 12659222.00)

    def test0494(self):
        self.assertEquals(self.calculate(-1813477346, -62431.0), -1813414915.00)

    def test0495(self):
        self.assertEquals(self.calculate(-590715159, -62504.0), -590652655.00)

    def test0496(self):
        self.assertEquals(self.calculate(1549873698, -169108.0), 1550042806.00)

    def test0497(self):
        self.assertEquals(self.calculate(806203087, -107938.0), 806311025.00)

    def test0498(self):
        self.assertEquals(self.calculate(-1578246371, 82311.0), -1578328682.00)

    def test0499(self):
        self.assertEquals(self.calculate(1290452083, -110250.0), 1290562333.00)

    def test0500(self):
        self.assertEquals(self.calculate(-1643462192, 11210.0), -1643473402.00)

    def test0501(self):
        self.assertEquals(self.calculate(1602783631, -104655.0), 1602888286.00)

    def test0502(self):
        self.assertEquals(self.calculate(207755759, -139278.0), 207895037.00)

    def test0503(self):
        self.assertEquals(self.calculate(-371972806, -169120.0), -371803686.00)

    def test0504(self):
        self.assertEquals(self.calculate(-1059593321, -191748.0), -1059401573.00)

    def test0505(self):
        self.assertEquals(self.calculate(1742954039, -189951.0), 1743143990.00)

    def test0506(self):
        self.assertEquals(self.calculate(2055523291, 5447.0), 2055517844.00)

    def test0507(self):
        self.assertEquals(self.calculate(-3263499, 31310.0), -3294809.00)

    def test0508(self):
        self.assertEquals(self.calculate(-1319399250, -184174.0), -1319215076.00)

    def test0509(self):
        self.assertEquals(self.calculate(-819083587, 34168.0), -819117755.00)

    def test0510(self):
        self.assertEquals(self.calculate(-491439030, -26442.0), -491412588.00)

    def test0511(self):
        self.assertEquals(self.calculate(-1492155055, 131823.0), -1492286878.00)

    def test0512(self):
        self.assertEquals(self.calculate(939349608, 83805.0), 939265803.00)

    def test0513(self):
        self.assertEquals(self.calculate(-958206818, -134258.0), -958072560.00)

    def test0514(self):
        self.assertEquals(self.calculate(-163325469, -13735.0), -163311734.00)

    def test0515(self):
        self.assertEquals(self.calculate(-438934370, 10629.0), -438944999.00)

    def test0516(self):
        self.assertEquals(self.calculate(-615050155, -122974.0), -614927181.00)

    def test0517(self):
        self.assertEquals(self.calculate(-1312641504, -46587.0), -1312594917.00)

    def test0518(self):
        self.assertEquals(self.calculate(-969343913, -154403.0), -969189510.00)

    def test0519(self):
        self.assertEquals(self.calculate(371685629, -173073.0), 371858702.00)

    def test0520(self):
        self.assertEquals(self.calculate(540467612, -87985.0), 540555597.00)

    def test0521(self):
        self.assertEquals(self.calculate(-1348481544, 119997.0), -1348601541.00)

    def test0522(self):
        self.assertEquals(self.calculate(-947356866, 69966.0), -947426832.00)

    def test0523(self):
        self.assertEquals(self.calculate(-1230925518, 197597.0), -1231123115.00)

    def test0524(self):
        self.assertEquals(self.calculate(322702002, 59649.0), 322642353.00)

    def test0525(self):
        self.assertEquals(self.calculate(-1860547086, 91236.0), -1860638322.00)

    def test0526(self):
        self.assertEquals(self.calculate(914515334, -83779.0), 914599113.00)

    def test0527(self):
        self.assertEquals(self.calculate(-1654454524, 132269.0), -1654586793.00)

    def test0528(self):
        self.assertEquals(self.calculate(-932720926, 197177.0), -932918103.00)

    def test0529(self):
        self.assertEquals(self.calculate(-2078965082, -112611.0), -2078852471.00)

    def test0530(self):
        self.assertEquals(self.calculate(93408425, -15956.0), 93424381.00)

    def test0531(self):
        self.assertEquals(self.calculate(-375817609, -120869.0), -375696740.00)

    def test0532(self):
        self.assertEquals(self.calculate(-1477847619, -183551.0), -1477664068.00)

    def test0533(self):
        self.assertEquals(self.calculate(102544586, 122576.0), 102422010.00)

    def test0534(self):
        self.assertEquals(self.calculate(632359570, -129512.0), 632489082.00)

    def test0535(self):
        self.assertEquals(self.calculate(-2063357652, -67658.0), -2063289994.00)

    def test0536(self):
        self.assertEquals(self.calculate(-2038779556, -23291.0), -2038756265.00)

    def test0537(self):
        self.assertEquals(self.calculate(297378307, 135209.0), 297243098.00)

    def test0538(self):
        self.assertEquals(self.calculate(-1890431099, -74154.0), -1890356945.00)

    def test0539(self):
        self.assertEquals(self.calculate(2092092724, -93803.0), 2092186527.00)

    def test0540(self):
        self.assertEquals(self.calculate(669313339, -113050.0), 669426389.00)

    def test0541(self):
        self.assertEquals(self.calculate(1249516343, 20201.0), 1249496142.00)

    def test0542(self):
        self.assertEquals(self.calculate(1753242607, 74547.0), 1753168060.00)

    def test0543(self):
        self.assertEquals(self.calculate(1879426024, 2891.0), 1879423133.00)

    def test0544(self):
        self.assertEquals(self.calculate(1025295474, 115831.0), 1025179643.00)

    def test0545(self):
        self.assertEquals(self.calculate(-709621892, 105529.0), -709727421.00)

    def test0546(self):
        self.assertEquals(self.calculate(-1744783069, -133844.0), -1744649225.00)

    def test0547(self):
        self.assertEquals(self.calculate(1078524173, 52640.0), 1078471533.00)

    def test0548(self):
        self.assertEquals(self.calculate(-1884376298, 161866.0), -1884538164.00)

    def test0549(self):
        self.assertEquals(self.calculate(-2092347118, 184186.0), -2092531304.00)

    def test0550(self):
        self.assertEquals(self.calculate(614472322, -37285.0), 614509607.00)

    def test0551(self):
        self.assertEquals(self.calculate(-1470986743, -12950.0), -1470973793.00)

    def test0552(self):
        self.assertEquals(self.calculate(717069497, -137991.0), 717207488.00)

    def test0553(self):
        self.assertEquals(self.calculate(105312637, 148824.0), 105163813.00)

    def test0554(self):
        self.assertEquals(self.calculate(902097013, 1654.0), 902095359.00)

    def test0555(self):
        self.assertEquals(self.calculate(1572838213, -86331.0), 1572924544.00)

    def test0556(self):
        self.assertEquals(self.calculate(-657892001, 27658.0), -657919659.00)

    def test0557(self):
        self.assertEquals(self.calculate(1476606143, 163130.0), 1476443013.00)

    def test0558(self):
        self.assertEquals(self.calculate(1372267344, -71351.0), 1372338695.00)

    def test0559(self):
        self.assertEquals(self.calculate(-2085066409, 24974.0), -2085091383.00)

    def test0560(self):
        self.assertEquals(self.calculate(603554459, -100050.0), 603654509.00)

    def test0561(self):
        self.assertEquals(self.calculate(1841652615, -160507.0), 1841813122.00)

    def test0562(self):
        self.assertEquals(self.calculate(-361643828, 109064.0), -361752892.00)

    def test0563(self):
        self.assertEquals(self.calculate(243269997, 72305.0), 243197692.00)

    def test0564(self):
        self.assertEquals(self.calculate(-1067137880, 51265.0), -1067189145.00)

    def test0565(self):
        self.assertEquals(self.calculate(1986077170, 134437.0), 1985942733.00)

    def test0566(self):
        self.assertEquals(self.calculate(1602244680, 101439.0), 1602143241.00)

    def test0567(self):
        self.assertEquals(self.calculate(714993321, 130340.0), 714862981.00)

    def test0568(self):
        self.assertEquals(self.calculate(-678762269, -24420.0), -678737849.00)

    def test0569(self):
        self.assertEquals(self.calculate(-1650178576, 189497.0), -1650368073.00)

    def test0570(self):
        self.assertEquals(self.calculate(-652960390, -3939.0), -652956451.00)

    def test0571(self):
        self.assertEquals(self.calculate(435529080, -90052.0), 435619132.00)

    def test0572(self):
        self.assertEquals(self.calculate(-1083028390, -6599.0), -1083021791.00)

    def test0573(self):
        self.assertEquals(self.calculate(503614946, 97632.0), 503517314.00)

    def test0574(self):
        self.assertEquals(self.calculate(-766490228, -61967.0), -766428261.00)

    def test0575(self):
        self.assertEquals(self.calculate(-1242729442, -82003.0), -1242647439.00)

    def test0576(self):
        self.assertEquals(self.calculate(590172790, 191885.0), 589980905.00)

    def test0577(self):
        self.assertEquals(self.calculate(472239560, -3581.0), 472243141.00)

    def test0578(self):
        self.assertEquals(self.calculate(1678496792, 165071.0), 1678331721.00)

    def test0579(self):
        self.assertEquals(self.calculate(-781583339, -88620.0), -781494719.00)

    def test0580(self):
        self.assertEquals(self.calculate(-1029040821, 121817.0), -1029162638.00)

    def test0581(self):
        self.assertEquals(self.calculate(1658863368, -182968.0), 1659046336.00)

    def test0582(self):
        self.assertEquals(self.calculate(-2074039717, 98313.0), -2074138030.00)

    def test0583(self):
        self.assertEquals(self.calculate(-1081910434, 337.0), -1081910771.00)

    def test0584(self):
        self.assertEquals(self.calculate(1765513404, 20242.0), 1765493162.00)

    def test0585(self):
        self.assertEquals(self.calculate(674368400, 179440.0), 674188960.00)

    def test0586(self):
        self.assertEquals(self.calculate(209681767, 167709.0), 209514058.00)

    def test0587(self):
        self.assertEquals(self.calculate(-1949043870, 29335.0), -1949073205.00)

    def test0588(self):
        self.assertEquals(self.calculate(1602742294, 152810.0), 1602589484.00)

    def test0589(self):
        self.assertEquals(self.calculate(601367698, -126704.0), 601494402.00)

    def test0590(self):
        self.assertEquals(self.calculate(72479160, 157100.0), 72322060.00)

    def test0591(self):
        self.assertEquals(self.calculate(-91742929, 23841.0), -91766770.00)

    def test0592(self):
        self.assertEquals(self.calculate(-307483482, -195225.0), -307288257.00)

    def test0593(self):
        self.assertEquals(self.calculate(1634482635, 193368.0), 1634289267.00)

    def test0594(self):
        self.assertEquals(self.calculate(-519006045, -114873.0), -518891172.00)

    def test0595(self):
        self.assertEquals(self.calculate(-955267386, -43701.0), -955223685.00)

    def test0596(self):
        self.assertEquals(self.calculate(-1111583038, 27701.0), -1111610739.00)

    def test0597(self):
        self.assertEquals(self.calculate(-73258564, 31678.0), -73290242.00)

    def test0598(self):
        self.assertEquals(self.calculate(-593949679, -60399.0), -593889280.00)

    def test0599(self):
        self.assertEquals(self.calculate(2067674157, -39100.0), 2067713257.00)

    def test0600(self):
        self.assertEquals(self.calculate(1899087967, -157136.0), 1899245103.00)

    def test0601(self):
        self.assertEquals(self.calculate(-808372375, -82826.0), -808289549.00)

    def test0602(self):
        self.assertEquals(self.calculate(-307500137, 116468.0), -307616605.00)

    def test0603(self):
        self.assertEquals(self.calculate(698033114, 126721.0), 697906393.00)

    def test0604(self):
        self.assertEquals(self.calculate(-501094893, 103761.0), -501198654.00)

    def test0605(self):
        self.assertEquals(self.calculate(-248639593, 158596.0), -248798189.00)

    def test0606(self):
        self.assertEquals(self.calculate(1252182204, 61178.0), 1252121026.00)

    def test0607(self):
        self.assertEquals(self.calculate(-1341638228, -93297.0), -1341544931.00)

    def test0608(self):
        self.assertEquals(self.calculate(-1935509755, 168290.0), -1935678045.00)

    def test0609(self):
        self.assertEquals(self.calculate(680118988, -81145.0), 680200133.00)

    def test0610(self):
        self.assertEquals(self.calculate(-1894014534, -179501.0), -1893835033.00)

    def test0611(self):
        self.assertEquals(self.calculate(1299586819, -184935.0), 1299771754.00)

    def test0612(self):
        self.assertEquals(self.calculate(1784758504, -174223.0), 1784932727.00)

    def test0613(self):
        self.assertEquals(self.calculate(-698225134, 33762.0), -698258896.00)

    def test0614(self):
        self.assertEquals(self.calculate(523261710, -74590.0), 523336300.00)

    def test0615(self):
        self.assertEquals(self.calculate(-1019095586, -182517.0), -1018913069.00)

    def test0616(self):
        self.assertEquals(self.calculate(2122985542, 31377.0), 2122954165.00)

    def test0617(self):
        self.assertEquals(self.calculate(-1511570541, 11998.0), -1511582539.00)

    def test0618(self):
        self.assertEquals(self.calculate(922512719, -182681.0), 922695400.00)

    def test0619(self):
        self.assertEquals(self.calculate(-1780516160, 177408.0), -1780693568.00)

    def test0620(self):
        self.assertEquals(self.calculate(-466356828, -75454.0), -466281374.00)

    def test0621(self):
        self.assertEquals(self.calculate(1225186790, 116067.0), 1225070723.00)

    def test0622(self):
        self.assertEquals(self.calculate(-668204436, 130536.0), -668334972.00)

    def test0623(self):
        self.assertEquals(self.calculate(-524392763, -128227.0), -524264536.00)

    def test0624(self):
        self.assertEquals(self.calculate(1084878275, 172218.0), 1084706057.00)

    def test0625(self):
        self.assertEquals(self.calculate(284085907, 141677.0), 283944230.00)

    def test0626(self):
        self.assertEquals(self.calculate(785887791, -22468.0), 785910259.00)

    def test0627(self):
        self.assertEquals(self.calculate(-1386230006, 182086.0), -1386412092.00)

    def test0628(self):
        self.assertEquals(self.calculate(865382797, 131715.0), 865251082.00)

    def test0629(self):
        self.assertEquals(self.calculate(-2081517870, -88792.0), -2081429078.00)

    def test0630(self):
        self.assertEquals(self.calculate(-704319062, -198421.0), -704120641.00)

    def test0631(self):
        self.assertEquals(self.calculate(-1943873389, 6821.0), -1943880210.00)

    def test0632(self):
        self.assertEquals(self.calculate(-386865665, 86412.0), -386952077.00)

    def test0633(self):
        self.assertEquals(self.calculate(-1799013795, 111213.0), -1799125008.00)

    def test0634(self):
        self.assertEquals(self.calculate(-1097659036, -66311.0), -1097592725.00)

    def test0635(self):
        self.assertEquals(self.calculate(1486708339, -112352.0), 1486820691.00)

    def test0636(self):
        self.assertEquals(self.calculate(-617614592, 142533.0), -617757125.00)

    def test0637(self):
        self.assertEquals(self.calculate(-1593860634, -24638.0), -1593835996.00)

    def test0638(self):
        self.assertEquals(self.calculate(238824208, -159823.0), 238984031.00)

    def test0639(self):
        self.assertEquals(self.calculate(-1183601537, 23461.0), -1183624998.00)

    def test0640(self):
        self.assertEquals(self.calculate(1103058515, 91549.0), 1102966966.00)

    def test0641(self):
        self.assertEquals(self.calculate(-520302205, -36399.0), -520265806.00)

    def test0642(self):
        self.assertEquals(self.calculate(538877324, -181967.0), 539059291.00)

    def test0643(self):
        self.assertEquals(self.calculate(-1966066910, -145129.0), -1965921781.00)

    def test0644(self):
        self.assertEquals(self.calculate(552734871, -77826.0), 552812697.00)

    def test0645(self):
        self.assertEquals(self.calculate(-1294497074, 162475.0), -1294659549.00)

    def test0646(self):
        self.assertEquals(self.calculate(-1085891806, 67975.0), -1085959781.00)

    def test0647(self):
        self.assertEquals(self.calculate(1376107469, 72055.0), 1376035414.00)

    def test0648(self):
        self.assertEquals(self.calculate(1532679634, 49480.0), 1532630154.00)

    def test0649(self):
        self.assertEquals(self.calculate(763553769, -42631.0), 763596400.00)

    def test0650(self):
        self.assertEquals(self.calculate(-351310430, -190496.0), -351119934.00)

    def test0651(self):
        self.assertEquals(self.calculate(494624154, -185692.0), 494809846.00)

    def test0652(self):
        self.assertEquals(self.calculate(1665717818, 16130.0), 1665701688.00)

    def test0653(self):
        self.assertEquals(self.calculate(254298300, 63108.0), 254235192.00)

    def test0654(self):
        self.assertEquals(self.calculate(219963114, 195515.0), 219767599.00)

    def test0655(self):
        self.assertEquals(self.calculate(480577211, 154834.0), 480422377.00)

    def test0656(self):
        self.assertEquals(self.calculate(-850123458, -181648.0), -849941810.00)

    def test0657(self):
        self.assertEquals(self.calculate(-1972663431, -194158.0), -1972469273.00)

    def test0658(self):
        self.assertEquals(self.calculate(88706499, -112994.0), 88819493.00)

    def test0659(self):
        self.assertEquals(self.calculate(-1215223738, 183745.0), -1215407483.00)

    def test0660(self):
        self.assertEquals(self.calculate(10872638, 89280.0), 10783358.00)

    def test0661(self):
        self.assertEquals(self.calculate(260259605, 20412.0), 260239193.00)

    def test0662(self):
        self.assertEquals(self.calculate(1550151278, -106156.0), 1550257434.00)

    def test0663(self):
        self.assertEquals(self.calculate(213896154, 69360.0), 213826794.00)

    def test0664(self):
        self.assertEquals(self.calculate(884604323, 107553.0), 884496770.00)

    def test0665(self):
        self.assertEquals(self.calculate(1218700712, 152897.0), 1218547815.00)

    def test0666(self):
        self.assertEquals(self.calculate(496438827, -104194.0), 496543021.00)

    def test0667(self):
        self.assertEquals(self.calculate(-1717204592, 97172.0), -1717301764.00)

    def test0668(self):
        self.assertEquals(self.calculate(1145788011, -128255.0), 1145916266.00)

    def test0669(self):
        self.assertEquals(self.calculate(1019823565, -32360.0), 1019855925.00)

    def test0670(self):
        self.assertEquals(self.calculate(193858619, 46739.0), 193811880.00)

    def test0671(self):
        self.assertEquals(self.calculate(-117136386, 45582.0), -117181968.00)

    def test0672(self):
        self.assertEquals(self.calculate(-41022659, 24970.0), -41047629.00)

    def test0673(self):
        self.assertEquals(self.calculate(-36883201, -74675.0), -36808526.00)

    def test0674(self):
        self.assertEquals(self.calculate(-1902303533, -196846.0), -1902106687.00)

    def test0675(self):
        self.assertEquals(self.calculate(116289058, 163918.0), 116125140.00)

    def test0676(self):
        self.assertEquals(self.calculate(1280726218, -113526.0), 1280839744.00)

    def test0677(self):
        self.assertEquals(self.calculate(-917096446, -156395.0), -916940051.00)

    def test0678(self):
        self.assertEquals(self.calculate(-2095630703, -163844.0), -2095466859.00)

    def test0679(self):
        self.assertEquals(self.calculate(1473817587, 62310.0), 1473755277.00)

    def test0680(self):
        self.assertEquals(self.calculate(-2062446377, 116735.0), -2062563112.00)

    def test0681(self):
        self.assertEquals(self.calculate(-2123195908, -182209.0), -2123013699.00)

    def test0682(self):
        self.assertEquals(self.calculate(-1631781689, 116768.0), -1631898457.00)

    def test0683(self):
        self.assertEquals(self.calculate(-1509299755, 75007.0), -1509374762.00)

    def test0684(self):
        self.assertEquals(self.calculate(1333305206, -17631.0), 1333322837.00)

    def test0685(self):
        self.assertEquals(self.calculate(945450440, 85904.0), 945364536.00)

    def test0686(self):
        self.assertEquals(self.calculate(-1604699403, 128611.0), -1604828014.00)

    def test0687(self):
        self.assertEquals(self.calculate(1520815272, -96399.0), 1520911671.00)

    def test0688(self):
        self.assertEquals(self.calculate(-360402109, 10581.0), -360412690.00)

    def test0689(self):
        self.assertEquals(self.calculate(-1202707412, 70257.0), -1202777669.00)

    def test0690(self):
        self.assertEquals(self.calculate(-120695786, -111353.0), -120584433.00)

    def test0691(self):
        self.assertEquals(self.calculate(-1088564629, -80774.0), -1088483855.00)

    def test0692(self):
        self.assertEquals(self.calculate(2106562502, 37164.0), 2106525338.00)

    def test0693(self):
        self.assertEquals(self.calculate(-942041492, 194664.0), -942236156.00)

    def test0694(self):
        self.assertEquals(self.calculate(1340060522, 184467.0), 1339876055.00)

    def test0695(self):
        self.assertEquals(self.calculate(-1542646174, 7195.0), -1542653369.00)

    def test0696(self):
        self.assertEquals(self.calculate(751947456, 90696.0), 751856760.00)

    def test0697(self):
        self.assertEquals(self.calculate(-744404460, -59952.0), -744344508.00)

    def test0698(self):
        self.assertEquals(self.calculate(1784570920, -31089.0), 1784602009.00)

    def test0699(self):
        self.assertEquals(self.calculate(829770627, 12018.0), 829758609.00)

    def test0700(self):
        self.assertEquals(self.calculate(1831823580, -189964.0), 1832013544.00)

    def test0701(self):
        self.assertEquals(self.calculate(-1200037875, -68316.0), -1199969559.00)

    def test0702(self):
        self.assertEquals(self.calculate(898845328, -54763.0), 898900091.00)

    def test0703(self):
        self.assertEquals(self.calculate(-1437777212, -18245.0), -1437758967.00)

    def test0704(self):
        self.assertEquals(self.calculate(-1390138417, -125728.0), -1390012689.00)

    def test0705(self):
        self.assertEquals(self.calculate(142088663, -181623.0), 142270286.00)

    def test0706(self):
        self.assertEquals(self.calculate(-37070104, -188385.0), -36881719.00)

    def test0707(self):
        self.assertEquals(self.calculate(1457818876, -182970.0), 1458001846.00)

    def test0708(self):
        self.assertEquals(self.calculate(899191951, 80875.0), 899111076.00)

    def test0709(self):
        self.assertEquals(self.calculate(1800803624, 158851.0), 1800644773.00)

    def test0710(self):
        self.assertEquals(self.calculate(-53562945, 147046.0), -53709991.00)

    def test0711(self):
        self.assertEquals(self.calculate(-3625973, -171222.0), -3454751.00)

    def test0712(self):
        self.assertEquals(self.calculate(-342636897, 193008.0), -342829905.00)

    def test0713(self):
        self.assertEquals(self.calculate(-820662108, 36546.0), -820698654.00)

    def test0714(self):
        self.assertEquals(self.calculate(420709534, -65081.0), 420774615.00)

    def test0715(self):
        self.assertEquals(self.calculate(40258282, 111032.0), 40147250.00)

    def test0716(self):
        self.assertEquals(self.calculate(-834998007, 129780.0), -835127787.00)

    def test0717(self):
        self.assertEquals(self.calculate(-1873541500, -146195.0), -1873395305.00)

    def test0718(self):
        self.assertEquals(self.calculate(1824829096, -139781.0), 1824968877.00)

    def test0719(self):
        self.assertEquals(self.calculate(-195759180, -138408.0), -195620772.00)

    def test0720(self):
        self.assertEquals(self.calculate(2045334343, 29552.0), 2045304791.00)

    def test0721(self):
        self.assertEquals(self.calculate(1496537055, -199134.0), 1496736189.00)

    def test0722(self):
        self.assertEquals(self.calculate(-609474219, -97280.0), -609376939.00)

    def test0723(self):
        self.assertEquals(self.calculate(-1805854170, -47471.0), -1805806699.00)

    def test0724(self):
        self.assertEquals(self.calculate(-1695751199, -159218.0), -1695591981.00)

    def test0725(self):
        self.assertEquals(self.calculate(-1113188538, -46070.0), -1113142468.00)

    def test0726(self):
        self.assertEquals(self.calculate(1166581678, 199484.0), 1166382194.00)

    def test0727(self):
        self.assertEquals(self.calculate(-1621328970, -93640.0), -1621235330.00)

    def test0728(self):
        self.assertEquals(self.calculate(-40483305, -26348.0), -40456957.00)

    def test0729(self):
        self.assertEquals(self.calculate(292645128, -33966.0), 292679094.00)

    def test0730(self):
        self.assertEquals(self.calculate(1497048600, 58463.0), 1496990137.00)

    def test0731(self):
        self.assertEquals(self.calculate(-1640072782, -116450.0), -1639956332.00)

    def test0732(self):
        self.assertEquals(self.calculate(-203432885, 88722.0), -203521607.00)

    def test0733(self):
        self.assertEquals(self.calculate(1097484336, -67389.0), 1097551725.00)

    def test0734(self):
        self.assertEquals(self.calculate(1578598374, -46125.0), 1578644499.00)

    def test0735(self):
        self.assertEquals(self.calculate(-1340017027, 90237.0), -1340107264.00)

    def test0736(self):
        self.assertEquals(self.calculate(-789765964, -198067.0), -789567897.00)

    def test0737(self):
        self.assertEquals(self.calculate(1466462074, 150917.0), 1466311157.00)

    def test0738(self):
        self.assertEquals(self.calculate(1227243882, 44230.0), 1227199652.00)

    def test0739(self):
        self.assertEquals(self.calculate(-709450020, 158509.0), -709608529.00)

    def test0740(self):
        self.assertEquals(self.calculate(-1139503734, 150352.0), -1139654086.00)

    def test0741(self):
        self.assertEquals(self.calculate(1946121693, -69916.0), 1946191609.00)

    def test0742(self):
        self.assertEquals(self.calculate(-11319184, -26294.0), -11292890.00)

    def test0743(self):
        self.assertEquals(self.calculate(-734154365, 147164.0), -734301529.00)

    def test0744(self):
        self.assertEquals(self.calculate(-1619089067, -81825.0), -1619007242.00)

    def test0745(self):
        self.assertEquals(self.calculate(19812786, -57452.0), 19870238.00)

    def test0746(self):
        self.assertEquals(self.calculate(-690295812, -176203.0), -690119609.00)

    def test0747(self):
        self.assertEquals(self.calculate(1152877512, 48055.0), 1152829457.00)

    def test0748(self):
        self.assertEquals(self.calculate(-1697291263, 126078.0), -1697417341.00)

    def test0749(self):
        self.assertEquals(self.calculate(-509110061, 49492.0), -509159553.00)

    def test0750(self):
        self.assertEquals(self.calculate(1163433823, 71622.0), 1163362201.00)

    def test0751(self):
        self.assertEquals(self.calculate(1068167822, -149701.0), 1068317523.00)

    def test0752(self):
        self.assertEquals(self.calculate(-1646919266, -55073.0), -1646864193.00)

    def test0753(self):
        self.assertEquals(self.calculate(-1520197765, -48478.0), -1520149287.00)

    def test0754(self):
        self.assertEquals(self.calculate(650344797, -67411.0), 650412208.00)

    def test0755(self):
        self.assertEquals(self.calculate(1682495285, 100131.0), 1682395154.00)

    def test0756(self):
        self.assertEquals(self.calculate(-685743501, 192791.0), -685936292.00)

    def test0757(self):
        self.assertEquals(self.calculate(-617054485, -3762.0), -617050723.00)

    def test0758(self):
        self.assertEquals(self.calculate(351154484, -58619.0), 351213103.00)

    def test0759(self):
        self.assertEquals(self.calculate(-4874780, -186495.0), -4688285.00)

    def test0760(self):
        self.assertEquals(self.calculate(954471125, -153968.0), 954625093.00)

    def test0761(self):
        self.assertEquals(self.calculate(-927508220, 59509.0), -927567729.00)

    def test0762(self):
        self.assertEquals(self.calculate(158532060, 33117.0), 158498943.00)

    def test0763(self):
        self.assertEquals(self.calculate(-351134420, 29854.0), -351164274.00)

    def test0764(self):
        self.assertEquals(self.calculate(976856618, 102005.0), 976754613.00)

    def test0765(self):
        self.assertEquals(self.calculate(-1091489724, 89423.0), -1091579147.00)

    def test0766(self):
        self.assertEquals(self.calculate(1222428644, 56664.0), 1222371980.00)

    def test0767(self):
        self.assertEquals(self.calculate(-623905497, -80859.0), -623824638.00)

    def test0768(self):
        self.assertEquals(self.calculate(270089986, -158084.0), 270248070.00)

    def test0769(self):
        self.assertEquals(self.calculate(4060883, 25694.0), 4035189.00)

    def test0770(self):
        self.assertEquals(self.calculate(-1656936240, 22197.0), -1656958437.00)

    def test0771(self):
        self.assertEquals(self.calculate(789404657, -107303.0), 789511960.00)

    def test0772(self):
        self.assertEquals(self.calculate(-1801209459, -90191.0), -1801119268.00)

    def test0773(self):
        self.assertEquals(self.calculate(1841133465, 23501.0), 1841109964.00)

    def test0774(self):
        self.assertEquals(self.calculate(-970077024, 114288.0), -970191312.00)

    def test0775(self):
        self.assertEquals(self.calculate(-182121445, -162028.0), -181959417.00)

    def test0776(self):
        self.assertEquals(self.calculate(34375964, -95181.0), 34471145.00)

    def test0777(self):
        self.assertEquals(self.calculate(-492258849, -120023.0), -492138826.00)

    def test0778(self):
        self.assertEquals(self.calculate(226244205, 89390.0), 226154815.00)

    def test0779(self):
        self.assertEquals(self.calculate(-1588421609, -100290.0), -1588321319.00)

    def test0780(self):
        self.assertEquals(self.calculate(1263847890, 142698.0), 1263705192.00)

    def test0781(self):
        self.assertEquals(self.calculate(978292630, 152905.0), 978139725.00)

    def test0782(self):
        self.assertEquals(self.calculate(63354007, -109586.0), 63463593.00)

    def test0783(self):
        self.assertEquals(self.calculate(-907343245, 26162.0), -907369407.00)

    def test0784(self):
        self.assertEquals(self.calculate(-1794073264, -55492.0), -1794017772.00)

    def test0785(self):
        self.assertEquals(self.calculate(-191860404, 192468.0), -192052872.00)

    def test0786(self):
        self.assertEquals(self.calculate(1395422407, -93056.0), 1395515463.00)

    def test0787(self):
        self.assertEquals(self.calculate(-797258424, -32460.0), -797225964.00)

    def test0788(self):
        self.assertEquals(self.calculate(-2094331548, -159447.0), -2094172101.00)

    def test0789(self):
        self.assertEquals(self.calculate(1935050412, 6608.0), 1935043804.00)

    def test0790(self):
        self.assertEquals(self.calculate(159052726, 50683.0), 159002043.00)

    def test0791(self):
        self.assertEquals(self.calculate(-2011741098, 156025.0), -2011897123.00)

    def test0792(self):
        self.assertEquals(self.calculate(164972429, -128531.0), 165100960.00)

    def test0793(self):
        self.assertEquals(self.calculate(-923586384, 109353.0), -923695737.00)

    def test0794(self):
        self.assertEquals(self.calculate(1686114896, -2755.0), 1686117651.00)

    def test0795(self):
        self.assertEquals(self.calculate(-1217346729, -123703.0), -1217223026.00)

    def test0796(self):
        self.assertEquals(self.calculate(1876713830, -183586.0), 1876897416.00)

    def test0797(self):
        self.assertEquals(self.calculate(837992450, -187992.0), 838180442.00)

    def test0798(self):
        self.assertEquals(self.calculate(-13329037, -140960.0), -13188077.00)

    def test0799(self):
        self.assertEquals(self.calculate(917548478, 175375.0), 917373103.00)

    def test0800(self):
        self.assertEquals(self.calculate(-1760723079, -69085.0), -1760653994.00)

    def test0801(self):
        self.assertEquals(self.calculate(-1145624969, 177533.0), -1145802502.00)

    def test0802(self):
        self.assertEquals(self.calculate(1583883632, 178956.0), 1583704676.00)

    def test0803(self):
        self.assertEquals(self.calculate(-695937072, 140392.0), -696077464.00)

    def test0804(self):
        self.assertEquals(self.calculate(1832626689, 94331.0), 1832532358.00)

    def test0805(self):
        self.assertEquals(self.calculate(-831877940, 138090.0), -832016030.00)

    def test0806(self):
        self.assertEquals(self.calculate(-906810096, 182604.0), -906992700.00)

    def test0807(self):
        self.assertEquals(self.calculate(173465227, -1267.0), 173466494.00)

    def test0808(self):
        self.assertEquals(self.calculate(-893991689, -127683.0), -893864006.00)

    def test0809(self):
        self.assertEquals(self.calculate(-2136114040, -104433.0), -2136009607.00)

    def test0810(self):
        self.assertEquals(self.calculate(-1278333476, 144455.0), -1278477931.00)

    def test0811(self):
        self.assertEquals(self.calculate(1451936113, 61732.0), 1451874381.00)

    def test0812(self):
        self.assertEquals(self.calculate(-1240726279, 96718.0), -1240822997.00)

    def test0813(self):
        self.assertEquals(self.calculate(1071501270, -16466.0), 1071517736.00)

    def test0814(self):
        self.assertEquals(self.calculate(990533713, 69821.0), 990463892.00)

    def test0815(self):
        self.assertEquals(self.calculate(-1314031018, -64671.0), -1313966347.00)

    def test0816(self):
        self.assertEquals(self.calculate(-903905757, 35177.0), -903940934.00)

    def test0817(self):
        self.assertEquals(self.calculate(1111414210, 196845.0), 1111217365.00)

    def test0818(self):
        self.assertEquals(self.calculate(243700916, -115673.0), 243816589.00)

    def test0819(self):
        self.assertEquals(self.calculate(-901003296, -89999.0), -900913297.00)

    def test0820(self):
        self.assertEquals(self.calculate(1832362461, -150844.0), 1832513305.00)

    def test0821(self):
        self.assertEquals(self.calculate(736586077, -162829.0), 736748906.00)

    def test0822(self):
        self.assertEquals(self.calculate(-1155145013, 47126.0), -1155192139.00)

    def test0823(self):
        self.assertEquals(self.calculate(-2025016737, 131123.0), -2025147860.00)

    def test0824(self):
        self.assertEquals(self.calculate(310144283, -128491.0), 310272774.00)

    def test0825(self):
        self.assertEquals(self.calculate(-1493277488, 26111.0), -1493303599.00)

    def test0826(self):
        self.assertEquals(self.calculate(-1289627045, 82791.0), -1289709836.00)

    def test0827(self):
        self.assertEquals(self.calculate(-1080157518, 128560.0), -1080286078.00)

    def test0828(self):
        self.assertEquals(self.calculate(1149675987, 9928.0), 1149666059.00)

    def test0829(self):
        self.assertEquals(self.calculate(-1438172121, 83085.0), -1438255206.00)

    def test0830(self):
        self.assertEquals(self.calculate(-2003645985, -108521.0), -2003537464.00)

    def test0831(self):
        self.assertEquals(self.calculate(-1295888248, -175402.0), -1295712846.00)

    def test0832(self):
        self.assertEquals(self.calculate(-1959647098, -110776.0), -1959536322.00)

    def test0833(self):
        self.assertEquals(self.calculate(-1842858763, -23513.0), -1842835250.00)

    def test0834(self):
        self.assertEquals(self.calculate(2066065787, 88501.0), 2065977286.00)

    def test0835(self):
        self.assertEquals(self.calculate(1837792748, 111244.0), 1837681504.00)

    def test0836(self):
        self.assertEquals(self.calculate(828400696, -67010.0), 828467706.00)

    def test0837(self):
        self.assertEquals(self.calculate(1665916431, 62198.0), 1665854233.00)

    def test0838(self):
        self.assertEquals(self.calculate(2025823574, -71512.0), 2025895086.00)

    def test0839(self):
        self.assertEquals(self.calculate(-1191725916, 96091.0), -1191822007.00)

    def test0840(self):
        self.assertEquals(self.calculate(-314882323, 75022.0), -314957345.00)

    def test0841(self):
        self.assertEquals(self.calculate(-1625924568, 179342.0), -1626103910.00)

    def test0842(self):
        self.assertEquals(self.calculate(146500484, -62321.0), 146562805.00)

    def test0843(self):
        self.assertEquals(self.calculate(-1107761678, 139483.0), -1107901161.00)

    def test0844(self):
        self.assertEquals(self.calculate(944929402, 93899.0), 944835503.00)

    def test0845(self):
        self.assertEquals(self.calculate(-1694119652, -117570.0), -1694002082.00)

    def test0846(self):
        self.assertEquals(self.calculate(-1120403408, 176999.0), -1120580407.00)

    def test0847(self):
        self.assertEquals(self.calculate(584705706, 84658.0), 584621048.00)

    def test0848(self):
        self.assertEquals(self.calculate(428986558, 186788.0), 428799770.00)

    def test0849(self):
        self.assertEquals(self.calculate(2020599460, -53213.0), 2020652673.00)

    def test0850(self):
        self.assertEquals(self.calculate(1837162116, -65650.0), 1837227766.00)

    def test0851(self):
        self.assertEquals(self.calculate(-114658767, 193676.0), -114852443.00)

    def test0852(self):
        self.assertEquals(self.calculate(-259083867, -23049.0), -259060818.00)

    def test0853(self):
        self.assertEquals(self.calculate(1161444909, 32738.0), 1161412171.00)

    def test0854(self):
        self.assertEquals(self.calculate(2131885462, 95854.0), 2131789608.00)

    def test0855(self):
        self.assertEquals(self.calculate(969968538, -19544.0), 969988082.00)

    def test0856(self):
        self.assertEquals(self.calculate(-1841920394, -13116.0), -1841907278.00)

    def test0857(self):
        self.assertEquals(self.calculate(1094208231, 12331.0), 1094195900.00)

    def test0858(self):
        self.assertEquals(self.calculate(964613617, 46783.0), 964566834.00)

    def test0859(self):
        self.assertEquals(self.calculate(-124792596, 45567.0), -124838163.00)

    def test0860(self):
        self.assertEquals(self.calculate(-1431429132, -127267.0), -1431301865.00)

    def test0861(self):
        self.assertEquals(self.calculate(-2119792196, -51508.0), -2119740688.00)

    def test0862(self):
        self.assertEquals(self.calculate(-825015367, -65855.0), -824949512.00)

    def test0863(self):
        self.assertEquals(self.calculate(-1337725258, -18878.0), -1337706380.00)

    def test0864(self):
        self.assertEquals(self.calculate(-834210873, -76694.0), -834134179.00)

    def test0865(self):
        self.assertEquals(self.calculate(1400823272, -179981.0), 1401003253.00)

    def test0866(self):
        self.assertEquals(self.calculate(1242389301, -32647.0), 1242421948.00)

    def test0867(self):
        self.assertEquals(self.calculate(-1960034180, -139832.0), -1959894348.00)

    def test0868(self):
        self.assertEquals(self.calculate(1113257369, 40999.0), 1113216370.00)

    def test0869(self):
        self.assertEquals(self.calculate(-1574636471, -172404.0), -1574464067.00)

    def test0870(self):
        self.assertEquals(self.calculate(43621989, -172013.0), 43794002.00)

    def test0871(self):
        self.assertEquals(self.calculate(656669952, -129858.0), 656799810.00)

    def test0872(self):
        self.assertEquals(self.calculate(1436492315, -31825.0), 1436524140.00)

    def test0873(self):
        self.assertEquals(self.calculate(-1943798148, -5743.0), -1943792405.00)

    def test0874(self):
        self.assertEquals(self.calculate(677315006, 180151.0), 677134855.00)

    def test0875(self):
        self.assertEquals(self.calculate(-2125530938, -136767.0), -2125394171.00)

    def test0876(self):
        self.assertEquals(self.calculate(-972796829, 41450.0), -972838279.00)

    def test0877(self):
        self.assertEquals(self.calculate(-314484587, -143555.0), -314341032.00)

    def test0878(self):
        self.assertEquals(self.calculate(1052437820, 87214.0), 1052350606.00)

    def test0879(self):
        self.assertEquals(self.calculate(1578980406, -186943.0), 1579167349.00)

    def test0880(self):
        self.assertEquals(self.calculate(66423138, 106358.0), 66316780.00)

    def test0881(self):
        self.assertEquals(self.calculate(1669662786, 47494.0), 1669615292.00)

    def test0882(self):
        self.assertEquals(self.calculate(863317247, -60481.0), 863377728.00)

    def test0883(self):
        self.assertEquals(self.calculate(-41377851, 148070.0), -41525921.00)

    def test0884(self):
        self.assertEquals(self.calculate(720120037, -109561.0), 720229598.00)

    def test0885(self):
        self.assertEquals(self.calculate(1624926467, -148956.0), 1625075423.00)

    def test0886(self):
        self.assertEquals(self.calculate(1511949634, -14103.0), 1511963737.00)

    def test0887(self):
        self.assertEquals(self.calculate(383113248, 161085.0), 382952163.00)

    def test0888(self):
        self.assertEquals(self.calculate(-815869426, 82655.0), -815952081.00)

    def test0889(self):
        self.assertEquals(self.calculate(113575060, -6795.0), 113581855.00)

    def test0890(self):
        self.assertEquals(self.calculate(-225863229, -27769.0), -225835460.00)

    def test0891(self):
        self.assertEquals(self.calculate(1205943227, -32107.0), 1205975334.00)

    def test0892(self):
        self.assertEquals(self.calculate(2084401030, 140015.0), 2084261015.00)

    def test0893(self):
        self.assertEquals(self.calculate(-677134372, 11977.0), -677146349.00)

    def test0894(self):
        self.assertEquals(self.calculate(-1472091718, 30154.0), -1472121872.00)

    def test0895(self):
        self.assertEquals(self.calculate(-2133547783, -190247.0), -2133357536.00)

    def test0896(self):
        self.assertEquals(self.calculate(-1403907615, 94072.0), -1404001687.00)

    def test0897(self):
        self.assertEquals(self.calculate(1430596176, -3435.0), 1430599611.00)

    def test0898(self):
        self.assertEquals(self.calculate(312192945, 108182.0), 312084763.00)

    def test0899(self):
        self.assertEquals(self.calculate(445073418, -160209.0), 445233627.00)

    def test0900(self):
        self.assertEquals(self.calculate(814398512, -193889.0), 814592401.00)

    def test0901(self):
        self.assertEquals(self.calculate(-1450640084, 76619.0), -1450716703.00)

    def test0902(self):
        self.assertEquals(self.calculate(-1157531585, -50035.0), -1157481550.00)

    def test0903(self):
        self.assertEquals(self.calculate(1725428048, 2268.0), 1725425780.00)

    def test0904(self):
        self.assertEquals(self.calculate(-1372365193, 102732.0), -1372467925.00)

    def test0905(self):
        self.assertEquals(self.calculate(-634274549, 173525.0), -634448074.00)

    def test0906(self):
        self.assertEquals(self.calculate(1877244336, -62206.0), 1877306542.00)

    def test0907(self):
        self.assertEquals(self.calculate(2056793592, 22361.0), 2056771231.00)

    def test0908(self):
        self.assertEquals(self.calculate(657372386, -71806.0), 657444192.00)

    def test0909(self):
        self.assertEquals(self.calculate(-1510612143, -57079.0), -1510555064.00)

    def test0910(self):
        self.assertEquals(self.calculate(1561082491, -43284.0), 1561125775.00)

    def test0911(self):
        self.assertEquals(self.calculate(1102818583, 24460.0), 1102794123.00)

    def test0912(self):
        self.assertEquals(self.calculate(-268196345, -85873.0), -268110472.00)

    def test0913(self):
        self.assertEquals(self.calculate(1758369145, 141481.0), 1758227664.00)

    def test0914(self):
        self.assertEquals(self.calculate(1270755166, -90694.0), 1270845860.00)

    def test0915(self):
        self.assertEquals(self.calculate(-791303517, -142567.0), -791160950.00)

    def test0916(self):
        self.assertEquals(self.calculate(1126657917, 15075.0), 1126642842.00)

    def test0917(self):
        self.assertEquals(self.calculate(1733870029, -141367.0), 1734011396.00)

    def test0918(self):
        self.assertEquals(self.calculate(-586473834, 197637.0), -586671471.00)

    def test0919(self):
        self.assertEquals(self.calculate(-424489663, 91914.0), -424581577.00)

    def test0920(self):
        self.assertEquals(self.calculate(-2088538727, -169216.0), -2088369511.00)

    def test0921(self):
        self.assertEquals(self.calculate(-1116037209, -56670.0), -1115980539.00)

    def test0922(self):
        self.assertEquals(self.calculate(-1542092622, -195892.0), -1541896730.00)

    def test0923(self):
        self.assertEquals(self.calculate(1768369764, -198047.0), 1768567811.00)

    def test0924(self):
        self.assertEquals(self.calculate(-1348505372, -88252.0), -1348417120.00)

    def test0925(self):
        self.assertEquals(self.calculate(-1407331077, 146984.0), -1407478061.00)

    def test0926(self):
        self.assertEquals(self.calculate(-1850467, -61546.0), -1788921.00)

    def test0927(self):
        self.assertEquals(self.calculate(1068168573, -21010.0), 1068189583.00)

    def test0928(self):
        self.assertEquals(self.calculate(-191293363, 171540.0), -191464903.00)

    def test0929(self):
        self.assertEquals(self.calculate(2051295218, -31616.0), 2051326834.00)

    def test0930(self):
        self.assertEquals(self.calculate(1256146202, 197935.0), 1255948267.00)

    def test0931(self):
        self.assertEquals(self.calculate(-442663432, -30942.0), -442632490.00)

    def test0932(self):
        self.assertEquals(self.calculate(-1869197273, 182181.0), -1869379454.00)

    def test0933(self):
        self.assertEquals(self.calculate(-1674284660, 197573.0), -1674482233.00)

    def test0934(self):
        self.assertEquals(self.calculate(1714420971, -21408.0), 1714442379.00)

    def test0935(self):
        self.assertEquals(self.calculate(216912811, -112749.0), 217025560.00)

    def test0936(self):
        self.assertEquals(self.calculate(1428681699, -189212.0), 1428870911.00)

    def test0937(self):
        self.assertEquals(self.calculate(-1056002708, 126570.0), -1056129278.00)

    def test0938(self):
        self.assertEquals(self.calculate(-876991562, -63596.0), -876927966.00)

    def test0939(self):
        self.assertEquals(self.calculate(-140467014, -86824.0), -140380190.00)

    def test0940(self):
        self.assertEquals(self.calculate(-2103727507, 114578.0), -2103842085.00)

    def test0941(self):
        self.assertEquals(self.calculate(631799943, 9204.0), 631790739.00)

    def test0942(self):
        self.assertEquals(self.calculate(1298582414, -49839.0), 1298632253.00)

    def test0943(self):
        self.assertEquals(self.calculate(-839522468, 195947.0), -839718415.00)

    def test0944(self):
        self.assertEquals(self.calculate(1332875232, -99134.0), 1332974366.00)

    def test0945(self):
        self.assertEquals(self.calculate(1617401067, 93631.0), 1617307436.00)

    def test0946(self):
        self.assertEquals(self.calculate(676960566, -19674.0), 676980240.00)

    def test0947(self):
        self.assertEquals(self.calculate(-798645901, -2859.0), -798643042.00)

    def test0948(self):
        self.assertEquals(self.calculate(1083259, 84964.0), 998295.00)

    def test0949(self):
        self.assertEquals(self.calculate(-760761618, -153586.0), -760608032.00)

    def test0950(self):
        self.assertEquals(self.calculate(2089598983, -6821.0), 2089605804.00)

    def test0951(self):
        self.assertEquals(self.calculate(1992616050, 56529.0), 1992559521.00)

    def test0952(self):
        self.assertEquals(self.calculate(1193975841, -171128.0), 1194146969.00)

    def test0953(self):
        self.assertEquals(self.calculate(126919197, 172270.0), 126746927.00)

    def test0954(self):
        self.assertEquals(self.calculate(1264289685, 149586.0), 1264140099.00)

    def test0955(self):
        self.assertEquals(self.calculate(1729755743, 130837.0), 1729624906.00)

    def test0956(self):
        self.assertEquals(self.calculate(-762325971, 99453.0), -762425424.00)

    def test0957(self):
        self.assertEquals(self.calculate(-1876246694, 56053.0), -1876302747.00)

    def test0958(self):
        self.assertEquals(self.calculate(-7495873, -74705.0), -7421168.00)

    def test0959(self):
        self.assertEquals(self.calculate(2028885802, -58621.0), 2028944423.00)

    def test0960(self):
        self.assertEquals(self.calculate(-595675511, -98570.0), -595576941.00)

    def test0961(self):
        self.assertEquals(self.calculate(-1423218359, 186073.0), -1423404432.00)

    def test0962(self):
        self.assertEquals(self.calculate(1957243921, 11849.0), 1957232072.00)

    def test0963(self):
        self.assertEquals(self.calculate(-1071157511, 106538.0), -1071264049.00)

    def test0964(self):
        self.assertEquals(self.calculate(-1741944285, -16633.0), -1741927652.00)

    def test0965(self):
        self.assertEquals(self.calculate(-657743586, -186770.0), -657556816.00)

    def test0966(self):
        self.assertEquals(self.calculate(-1528731723, -23705.0), -1528708018.00)

    def test0967(self):
        self.assertEquals(self.calculate(1494707094, -93898.0), 1494800992.00)

    def test0968(self):
        self.assertEquals(self.calculate(-1418603659, 41406.0), -1418645065.00)

    def test0969(self):
        self.assertEquals(self.calculate(-1758057349, 140246.0), -1758197595.00)

    def test0970(self):
        self.assertEquals(self.calculate(-1318917556, -4301.0), -1318913255.00)

    def test0971(self):
        self.assertEquals(self.calculate(-16602300, 31130.0), -16633430.00)

    def test0972(self):
        self.assertEquals(self.calculate(-129698536, -154815.0), -129543721.00)

    def test0973(self):
        self.assertEquals(self.calculate(-1960012302, -196909.0), -1959815393.00)

    def test0974(self):
        self.assertEquals(self.calculate(-2052541095, -86603.0), -2052454492.00)

    def test0975(self):
        self.assertEquals(self.calculate(-1374209658, 119736.0), -1374329394.00)

    def test0976(self):
        self.assertEquals(self.calculate(106132591, -49202.0), 106181793.00)

    def test0977(self):
        self.assertEquals(self.calculate(533088910, -32140.0), 533121050.00)

    def test0978(self):
        self.assertEquals(self.calculate(1601284778, -164078.0), 1601448856.00)

    def test0979(self):
        self.assertEquals(self.calculate(1686252710, 138745.0), 1686113965.00)

    def test0980(self):
        self.assertEquals(self.calculate(936502014, -183479.0), 936685493.00)

    def test0981(self):
        self.assertEquals(self.calculate(-1628779624, -140091.0), -1628639533.00)

    def test0982(self):
        self.assertEquals(self.calculate(-1840659681, 77069.0), -1840736750.00)

    def test0983(self):
        self.assertEquals(self.calculate(2092452259, -14016.0), 2092466275.00)

    def test0984(self):
        self.assertEquals(self.calculate(192172254, 191048.0), 191981206.00)

    def test0985(self):
        self.assertEquals(self.calculate(-1622248675, -67458.0), -1622181217.00)

    def test0986(self):
        self.assertEquals(self.calculate(-1227395808, -169760.0), -1227226048.00)

    def test0987(self):
        self.assertEquals(self.calculate(-1722889946, -164431.0), -1722725515.00)

    def test0988(self):
        self.assertEquals(self.calculate(-620550583, 103210.0), -620653793.00)

    def test0989(self):
        self.assertEquals(self.calculate(-1136862032, -142510.0), -1136719522.00)

    def test0990(self):
        self.assertEquals(self.calculate(-1977504735, -169606.0), -1977335129.00)

    def test0991(self):
        self.assertEquals(self.calculate(-641503353, -174760.0), -641328593.00)

    def test0992(self):
        self.assertEquals(self.calculate(1159012254, 61183.0), 1158951071.00)

    def test0993(self):
        self.assertEquals(self.calculate(2127941414, -30779.0), 2127972193.00)

    def test0994(self):
        self.assertEquals(self.calculate(297261796, -101743.0), 297363539.00)

    def test0995(self):
        self.assertEquals(self.calculate(-1303992448, -69201.0), -1303923247.00)

    def test0996(self):
        self.assertEquals(self.calculate(100933270, 49562.0), 100883708.00)

    def test0997(self):
        self.assertEquals(self.calculate(263320325, 50047.0), 263270278.00)

    def test0998(self):
        self.assertEquals(self.calculate(1954470820, -162699.0), 1954633519.00)

    def test0999(self):
        self.assertEquals(self.calculate(803013419, -112294.0), 803125713.00)

    def test1000(self):
        self.assertEquals(self.calculate(-301504160, -64635.0), -301439525.00)

    def test1001(self):
        self.assertEquals(self.calculate(-277048431, 130396.0), -277178827.00)

    def test1002(self):
        self.assertEquals(self.calculate(1556433226, -56032.0), 1556489258.00)

    def test1003(self):
        self.assertEquals(self.calculate(1160836551, 6950.0), 1160829601.00)

    def test1004(self):
        self.assertEquals(self.calculate(-697475967, 158040.0), -697634007.00)

    def test1005(self):
        self.assertEquals(self.calculate(1569103588, -20811.0), 1569124399.00)

    def test1006(self):
        self.assertEquals(self.calculate(-1824816222, -168171.0), -1824648051.00)

    def test1007(self):
        self.assertEquals(self.calculate(-80170582, 126446.0), -80297028.00)

    def test1008(self):
        self.assertEquals(self.calculate(1945775217, -30802.0), 1945806019.00)

    def test1009(self):
        self.assertEquals(self.calculate(1686042972, 75157.0), 1685967815.00)

    def test1010(self):
        self.assertEquals(self.calculate(-1922559650, 16647.0), -1922576297.00)

    def test1011(self):
        self.assertEquals(self.calculate(-857532352, -66701.0), -857465651.00)

    def test1012(self):
        self.assertEquals(self.calculate(1887330870, 22399.0), 1887308471.00)

    def test1013(self):
        self.assertEquals(self.calculate(-1222433681, -87270.0), -1222346411.00)

    def test1014(self):
        self.assertEquals(self.calculate(-319511306, 118745.0), -319630051.00)

    def test1015(self):
        self.assertEquals(self.calculate(450950465, 161726.0), 450788739.00)

    def test1016(self):
        self.assertEquals(self.calculate(208381527, -121710.0), 208503237.00)

    def test1017(self):
        self.assertEquals(self.calculate(-2037124893, -126349.0), -2036998544.00)

    def test1018(self):
        self.assertEquals(self.calculate(1616296963, -179344.0), 1616476307.00)

    def test1019(self):
        self.assertEquals(self.calculate(879868012, -140185.0), 880008197.00)

    def test1020(self):
        self.assertEquals(self.calculate(561912154, -70950.0), 561983104.00)

    def test1021(self):
        self.assertEquals(self.calculate(-488169770, 43838.0), -488213608.00)

    def test1022(self):
        self.assertEquals(self.calculate(452911282, -133820.0), 453045102.00)

    def test1023(self):
        self.assertEquals(self.calculate(-29519204, 150804.0), -29670008.00)




class TestVM_Sub_FloatInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushW(rhs)
        v.VM_Sub()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(143949.0, 20448), 123501.00)

    def test0001(self):
        self.assertEquals(self.calculate(-77100.0, -18617), -58483.00)

    def test0002(self):
        self.assertEquals(self.calculate(63700.0, 17745), 45955.00)

    def test0003(self):
        self.assertEquals(self.calculate(-197702.0, 30805), -228507.00)

    def test0004(self):
        self.assertEquals(self.calculate(-179254.0, -30653), -148601.00)

    def test0005(self):
        self.assertEquals(self.calculate(167216.0, -29656), 196872.00)

    def test0006(self):
        self.assertEquals(self.calculate(185201.0, 3226), 181975.00)

    def test0007(self):
        self.assertEquals(self.calculate(35536.0, -11190), 46726.00)

    def test0008(self):
        self.assertEquals(self.calculate(139839.0, -13441), 153280.00)

    def test0009(self):
        self.assertEquals(self.calculate(186385.0, 32239), 154146.00)

    def test0010(self):
        self.assertEquals(self.calculate(125699.0, -27665), 153364.00)

    def test0011(self):
        self.assertEquals(self.calculate(22693.0, -23150), 45843.00)

    def test0012(self):
        self.assertEquals(self.calculate(-94450.0, -18456), -75994.00)

    def test0013(self):
        self.assertEquals(self.calculate(-84847.0, -27924), -56923.00)

    def test0014(self):
        self.assertEquals(self.calculate(71363.0, 16086), 55277.00)

    def test0015(self):
        self.assertEquals(self.calculate(-17334.0, 14713), -32047.00)

    def test0016(self):
        self.assertEquals(self.calculate(176087.0, 25821), 150266.00)

    def test0017(self):
        self.assertEquals(self.calculate(88916.0, -128), 89044.00)

    def test0018(self):
        self.assertEquals(self.calculate(-18944.0, 14893), -33837.00)

    def test0019(self):
        self.assertEquals(self.calculate(-185189.0, 12466), -197655.00)

    def test0020(self):
        self.assertEquals(self.calculate(8472.0, 6307), 2165.00)

    def test0021(self):
        self.assertEquals(self.calculate(177939.0, 31231), 146708.00)

    def test0022(self):
        self.assertEquals(self.calculate(-101381.0, -16861), -84520.00)

    def test0023(self):
        self.assertEquals(self.calculate(-28680.0, -23800), -4880.00)

    def test0024(self):
        self.assertEquals(self.calculate(66404.0, -30989), 97393.00)

    def test0025(self):
        self.assertEquals(self.calculate(-185216.0, -29574), -155642.00)

    def test0026(self):
        self.assertEquals(self.calculate(163416.0, 30117), 133299.00)

    def test0027(self):
        self.assertEquals(self.calculate(19746.0, 32297), -12551.00)

    def test0028(self):
        self.assertEquals(self.calculate(176505.0, 24329), 152176.00)

    def test0029(self):
        self.assertEquals(self.calculate(-70552.0, -12054), -58498.00)

    def test0030(self):
        self.assertEquals(self.calculate(-8978.0, -19287), 10309.00)

    def test0031(self):
        self.assertEquals(self.calculate(162837.0, -630), 163467.00)

    def test0032(self):
        self.assertEquals(self.calculate(93620.0, -19066), 112686.00)

    def test0033(self):
        self.assertEquals(self.calculate(-132571.0, 28537), -161108.00)

    def test0034(self):
        self.assertEquals(self.calculate(-92691.0, -15161), -77530.00)

    def test0035(self):
        self.assertEquals(self.calculate(-199878.0, 6615), -206493.00)

    def test0036(self):
        self.assertEquals(self.calculate(25640.0, 15303), 10337.00)

    def test0037(self):
        self.assertEquals(self.calculate(-40082.0, -27556), -12526.00)

    def test0038(self):
        self.assertEquals(self.calculate(2842.0, -5014), 7856.00)

    def test0039(self):
        self.assertEquals(self.calculate(162894.0, 2087), 160807.00)

    def test0040(self):
        self.assertEquals(self.calculate(2838.0, 23846), -21008.00)

    def test0041(self):
        self.assertEquals(self.calculate(-58005.0, 24110), -82115.00)

    def test0042(self):
        self.assertEquals(self.calculate(25761.0, 15442), 10319.00)

    def test0043(self):
        self.assertEquals(self.calculate(-112305.0, -23869), -88436.00)

    def test0044(self):
        self.assertEquals(self.calculate(-91029.0, -21205), -69824.00)

    def test0045(self):
        self.assertEquals(self.calculate(-2010.0, -18968), 16958.00)

    def test0046(self):
        self.assertEquals(self.calculate(138341.0, 18793), 119548.00)

    def test0047(self):
        self.assertEquals(self.calculate(69593.0, -24280), 93873.00)

    def test0048(self):
        self.assertEquals(self.calculate(-145758.0, -4853), -140905.00)

    def test0049(self):
        self.assertEquals(self.calculate(173249.0, 26806), 146443.00)

    def test0050(self):
        self.assertEquals(self.calculate(-134847.0, 27290), -162137.00)

    def test0051(self):
        self.assertEquals(self.calculate(-43404.0, 16164), -59568.00)

    def test0052(self):
        self.assertEquals(self.calculate(-25305.0, 18857), -44162.00)

    def test0053(self):
        self.assertEquals(self.calculate(192673.0, 18288), 174385.00)

    def test0054(self):
        self.assertEquals(self.calculate(-57878.0, -24734), -33144.00)

    def test0055(self):
        self.assertEquals(self.calculate(-165940.0, -10291), -155649.00)

    def test0056(self):
        self.assertEquals(self.calculate(-83887.0, 7612), -91499.00)

    def test0057(self):
        self.assertEquals(self.calculate(59020.0, -29190), 88210.00)

    def test0058(self):
        self.assertEquals(self.calculate(-196024.0, -6336), -189688.00)

    def test0059(self):
        self.assertEquals(self.calculate(94244.0, -15744), 109988.00)

    def test0060(self):
        self.assertEquals(self.calculate(192501.0, -17552), 210053.00)

    def test0061(self):
        self.assertEquals(self.calculate(191934.0, 12978), 178956.00)

    def test0062(self):
        self.assertEquals(self.calculate(-132018.0, 17224), -149242.00)

    def test0063(self):
        self.assertEquals(self.calculate(176116.0, -18580), 194696.00)

    def test0064(self):
        self.assertEquals(self.calculate(-19905.0, 6434), -26339.00)

    def test0065(self):
        self.assertEquals(self.calculate(-161013.0, -9727), -151286.00)

    def test0066(self):
        self.assertEquals(self.calculate(177.0, 4930), -4753.00)

    def test0067(self):
        self.assertEquals(self.calculate(45832.0, 1963), 43869.00)

    def test0068(self):
        self.assertEquals(self.calculate(185288.0, -10014), 195302.00)

    def test0069(self):
        self.assertEquals(self.calculate(158042.0, 24720), 133322.00)

    def test0070(self):
        self.assertEquals(self.calculate(98719.0, -27247), 125966.00)

    def test0071(self):
        self.assertEquals(self.calculate(-106024.0, -15289), -90735.00)

    def test0072(self):
        self.assertEquals(self.calculate(-97134.0, -4860), -92274.00)

    def test0073(self):
        self.assertEquals(self.calculate(174066.0, 7158), 166908.00)

    def test0074(self):
        self.assertEquals(self.calculate(-186636.0, 15303), -201939.00)

    def test0075(self):
        self.assertEquals(self.calculate(-111587.0, -27338), -84249.00)

    def test0076(self):
        self.assertEquals(self.calculate(-81622.0, 1484), -83106.00)

    def test0077(self):
        self.assertEquals(self.calculate(-179915.0, 32512), -212427.00)

    def test0078(self):
        self.assertEquals(self.calculate(-108742.0, -10064), -98678.00)

    def test0079(self):
        self.assertEquals(self.calculate(-74057.0, 10890), -84947.00)

    def test0080(self):
        self.assertEquals(self.calculate(-183414.0, 18260), -201674.00)

    def test0081(self):
        self.assertEquals(self.calculate(-159646.0, 1794), -161440.00)

    def test0082(self):
        self.assertEquals(self.calculate(170796.0, 31364), 139432.00)

    def test0083(self):
        self.assertEquals(self.calculate(-181335.0, 26212), -207547.00)

    def test0084(self):
        self.assertEquals(self.calculate(-183351.0, -28262), -155089.00)

    def test0085(self):
        self.assertEquals(self.calculate(-27884.0, -17265), -10619.00)

    def test0086(self):
        self.assertEquals(self.calculate(-146567.0, 15267), -161834.00)

    def test0087(self):
        self.assertEquals(self.calculate(21131.0, -22542), 43673.00)

    def test0088(self):
        self.assertEquals(self.calculate(143832.0, -15272), 159104.00)

    def test0089(self):
        self.assertEquals(self.calculate(-143723.0, -6146), -137577.00)

    def test0090(self):
        self.assertEquals(self.calculate(-141853.0, -15058), -126795.00)

    def test0091(self):
        self.assertEquals(self.calculate(191412.0, -23317), 214729.00)

    def test0092(self):
        self.assertEquals(self.calculate(-95693.0, 8471), -104164.00)

    def test0093(self):
        self.assertEquals(self.calculate(-85927.0, 20443), -106370.00)

    def test0094(self):
        self.assertEquals(self.calculate(-34162.0, 9528), -43690.00)

    def test0095(self):
        self.assertEquals(self.calculate(-168573.0, -25118), -143455.00)

    def test0096(self):
        self.assertEquals(self.calculate(120894.0, -23766), 144660.00)

    def test0097(self):
        self.assertEquals(self.calculate(-150195.0, 29609), -179804.00)

    def test0098(self):
        self.assertEquals(self.calculate(156972.0, 18291), 138681.00)

    def test0099(self):
        self.assertEquals(self.calculate(139756.0, -12292), 152048.00)

    def test0100(self):
        self.assertEquals(self.calculate(41000.0, 2494), 38506.00)

    def test0101(self):
        self.assertEquals(self.calculate(81177.0, -12934), 94111.00)

    def test0102(self):
        self.assertEquals(self.calculate(87094.0, 2945), 84149.00)

    def test0103(self):
        self.assertEquals(self.calculate(-190131.0, 5224), -195355.00)

    def test0104(self):
        self.assertEquals(self.calculate(197438.0, 2304), 195134.00)

    def test0105(self):
        self.assertEquals(self.calculate(48280.0, 23340), 24940.00)

    def test0106(self):
        self.assertEquals(self.calculate(-173822.0, -32014), -141808.00)

    def test0107(self):
        self.assertEquals(self.calculate(108005.0, 16555), 91450.00)

    def test0108(self):
        self.assertEquals(self.calculate(184058.0, -168), 184226.00)

    def test0109(self):
        self.assertEquals(self.calculate(195808.0, 16490), 179318.00)

    def test0110(self):
        self.assertEquals(self.calculate(121348.0, 31934), 89414.00)

    def test0111(self):
        self.assertEquals(self.calculate(107928.0, 30249), 77679.00)

    def test0112(self):
        self.assertEquals(self.calculate(-8965.0, 30757), -39722.00)

    def test0113(self):
        self.assertEquals(self.calculate(-186776.0, -4974), -181802.00)

    def test0114(self):
        self.assertEquals(self.calculate(41959.0, 25575), 16384.00)

    def test0115(self):
        self.assertEquals(self.calculate(61550.0, -19398), 80948.00)

    def test0116(self):
        self.assertEquals(self.calculate(-30791.0, 29162), -59953.00)

    def test0117(self):
        self.assertEquals(self.calculate(121923.0, -3620), 125543.00)

    def test0118(self):
        self.assertEquals(self.calculate(-173392.0, -236), -173156.00)

    def test0119(self):
        self.assertEquals(self.calculate(-58512.0, -28021), -30491.00)

    def test0120(self):
        self.assertEquals(self.calculate(23687.0, -14044), 37731.00)

    def test0121(self):
        self.assertEquals(self.calculate(129089.0, 5496), 123593.00)

    def test0122(self):
        self.assertEquals(self.calculate(53214.0, -28494), 81708.00)

    def test0123(self):
        self.assertEquals(self.calculate(-16721.0, 27607), -44328.00)

    def test0124(self):
        self.assertEquals(self.calculate(137333.0, -32188), 169521.00)

    def test0125(self):
        self.assertEquals(self.calculate(-148804.0, 13492), -162296.00)

    def test0126(self):
        self.assertEquals(self.calculate(87992.0, 17748), 70244.00)

    def test0127(self):
        self.assertEquals(self.calculate(-68169.0, 2203), -70372.00)

    def test0128(self):
        self.assertEquals(self.calculate(-133964.0, -29642), -104322.00)

    def test0129(self):
        self.assertEquals(self.calculate(-99271.0, 18398), -117669.00)

    def test0130(self):
        self.assertEquals(self.calculate(60896.0, 3826), 57070.00)

    def test0131(self):
        self.assertEquals(self.calculate(139323.0, 21022), 118301.00)

    def test0132(self):
        self.assertEquals(self.calculate(120828.0, 965), 119863.00)

    def test0133(self):
        self.assertEquals(self.calculate(110023.0, -32229), 142252.00)

    def test0134(self):
        self.assertEquals(self.calculate(196224.0, 3270), 192954.00)

    def test0135(self):
        self.assertEquals(self.calculate(183481.0, -12880), 196361.00)

    def test0136(self):
        self.assertEquals(self.calculate(96396.0, -7512), 103908.00)

    def test0137(self):
        self.assertEquals(self.calculate(135013.0, -18796), 153809.00)

    def test0138(self):
        self.assertEquals(self.calculate(-82733.0, -6078), -76655.00)

    def test0139(self):
        self.assertEquals(self.calculate(183180.0, 2272), 180908.00)

    def test0140(self):
        self.assertEquals(self.calculate(-156593.0, -13370), -143223.00)

    def test0141(self):
        self.assertEquals(self.calculate(-166251.0, 9963), -176214.00)

    def test0142(self):
        self.assertEquals(self.calculate(68486.0, -19190), 87676.00)

    def test0143(self):
        self.assertEquals(self.calculate(-39890.0, 368), -40258.00)

    def test0144(self):
        self.assertEquals(self.calculate(18206.0, -19872), 38078.00)

    def test0145(self):
        self.assertEquals(self.calculate(95545.0, 26871), 68674.00)

    def test0146(self):
        self.assertEquals(self.calculate(-185202.0, 18414), -203616.00)

    def test0147(self):
        self.assertEquals(self.calculate(105562.0, 20848), 84714.00)

    def test0148(self):
        self.assertEquals(self.calculate(-167280.0, -25467), -141813.00)

    def test0149(self):
        self.assertEquals(self.calculate(-16937.0, 23759), -40696.00)

    def test0150(self):
        self.assertEquals(self.calculate(-176139.0, 14934), -191073.00)

    def test0151(self):
        self.assertEquals(self.calculate(-165951.0, -28525), -137426.00)

    def test0152(self):
        self.assertEquals(self.calculate(143975.0, -10282), 154257.00)

    def test0153(self):
        self.assertEquals(self.calculate(98713.0, -12171), 110884.00)

    def test0154(self):
        self.assertEquals(self.calculate(85763.0, 20504), 65259.00)

    def test0155(self):
        self.assertEquals(self.calculate(102825.0, -28206), 131031.00)

    def test0156(self):
        self.assertEquals(self.calculate(-107632.0, 3130), -110762.00)

    def test0157(self):
        self.assertEquals(self.calculate(-91317.0, 20416), -111733.00)

    def test0158(self):
        self.assertEquals(self.calculate(77503.0, -12436), 89939.00)

    def test0159(self):
        self.assertEquals(self.calculate(-40698.0, -28754), -11944.00)

    def test0160(self):
        self.assertEquals(self.calculate(120254.0, -13631), 133885.00)

    def test0161(self):
        self.assertEquals(self.calculate(116653.0, 24994), 91659.00)

    def test0162(self):
        self.assertEquals(self.calculate(-181900.0, -1372), -180528.00)

    def test0163(self):
        self.assertEquals(self.calculate(190857.0, -8091), 198948.00)

    def test0164(self):
        self.assertEquals(self.calculate(-135804.0, -20243), -115561.00)

    def test0165(self):
        self.assertEquals(self.calculate(35434.0, -27292), 62726.00)

    def test0166(self):
        self.assertEquals(self.calculate(149959.0, -22491), 172450.00)

    def test0167(self):
        self.assertEquals(self.calculate(111647.0, -19830), 131477.00)

    def test0168(self):
        self.assertEquals(self.calculate(-142810.0, -27180), -115630.00)

    def test0169(self):
        self.assertEquals(self.calculate(-167959.0, -5547), -162412.00)

    def test0170(self):
        self.assertEquals(self.calculate(-112624.0, -10341), -102283.00)

    def test0171(self):
        self.assertEquals(self.calculate(12174.0, -27556), 39730.00)

    def test0172(self):
        self.assertEquals(self.calculate(116415.0, 29170), 87245.00)

    def test0173(self):
        self.assertEquals(self.calculate(22347.0, 32080), -9733.00)

    def test0174(self):
        self.assertEquals(self.calculate(-104811.0, -6062), -98749.00)

    def test0175(self):
        self.assertEquals(self.calculate(-97455.0, -32296), -65159.00)

    def test0176(self):
        self.assertEquals(self.calculate(110517.0, -17087), 127604.00)

    def test0177(self):
        self.assertEquals(self.calculate(84886.0, 9532), 75354.00)

    def test0178(self):
        self.assertEquals(self.calculate(-144517.0, -29775), -114742.00)

    def test0179(self):
        self.assertEquals(self.calculate(-174784.0, -27513), -147271.00)

    def test0180(self):
        self.assertEquals(self.calculate(-123601.0, -28051), -95550.00)

    def test0181(self):
        self.assertEquals(self.calculate(9265.0, -22618), 31883.00)

    def test0182(self):
        self.assertEquals(self.calculate(184147.0, 14557), 169590.00)

    def test0183(self):
        self.assertEquals(self.calculate(68203.0, 21379), 46824.00)

    def test0184(self):
        self.assertEquals(self.calculate(-101758.0, 28484), -130242.00)

    def test0185(self):
        self.assertEquals(self.calculate(119995.0, 10563), 109432.00)

    def test0186(self):
        self.assertEquals(self.calculate(-66472.0, 12764), -79236.00)

    def test0187(self):
        self.assertEquals(self.calculate(-190024.0, -15961), -174063.00)

    def test0188(self):
        self.assertEquals(self.calculate(197740.0, 25180), 172560.00)

    def test0189(self):
        self.assertEquals(self.calculate(191932.0, -27129), 219061.00)

    def test0190(self):
        self.assertEquals(self.calculate(-59805.0, -11279), -48526.00)

    def test0191(self):
        self.assertEquals(self.calculate(-108898.0, 29088), -137986.00)

    def test0192(self):
        self.assertEquals(self.calculate(-48046.0, 22255), -70301.00)

    def test0193(self):
        self.assertEquals(self.calculate(-9791.0, 6071), -15862.00)

    def test0194(self):
        self.assertEquals(self.calculate(-6161.0, -24727), 18566.00)

    def test0195(self):
        self.assertEquals(self.calculate(145034.0, 265), 144769.00)

    def test0196(self):
        self.assertEquals(self.calculate(-137497.0, 19913), -157410.00)

    def test0197(self):
        self.assertEquals(self.calculate(167341.0, 19455), 147886.00)

    def test0198(self):
        self.assertEquals(self.calculate(21998.0, 12921), 9077.00)

    def test0199(self):
        self.assertEquals(self.calculate(-18049.0, -2657), -15392.00)

    def test0200(self):
        self.assertEquals(self.calculate(22683.0, -27293), 49976.00)

    def test0201(self):
        self.assertEquals(self.calculate(-96694.0, -32424), -64270.00)

    def test0202(self):
        self.assertEquals(self.calculate(81388.0, 27900), 53488.00)

    def test0203(self):
        self.assertEquals(self.calculate(86347.0, -13013), 99360.00)

    def test0204(self):
        self.assertEquals(self.calculate(183285.0, 15507), 167778.00)

    def test0205(self):
        self.assertEquals(self.calculate(-8182.0, 21313), -29495.00)

    def test0206(self):
        self.assertEquals(self.calculate(-37633.0, -24478), -13155.00)

    def test0207(self):
        self.assertEquals(self.calculate(-9356.0, -28921), 19565.00)

    def test0208(self):
        self.assertEquals(self.calculate(-182221.0, -18941), -163280.00)

    def test0209(self):
        self.assertEquals(self.calculate(105043.0, 3983), 101060.00)

    def test0210(self):
        self.assertEquals(self.calculate(76174.0, 6019), 70155.00)

    def test0211(self):
        self.assertEquals(self.calculate(145227.0, 4809), 140418.00)

    def test0212(self):
        self.assertEquals(self.calculate(10656.0, -15493), 26149.00)

    def test0213(self):
        self.assertEquals(self.calculate(-183245.0, -5939), -177306.00)

    def test0214(self):
        self.assertEquals(self.calculate(-119829.0, 3035), -122864.00)

    def test0215(self):
        self.assertEquals(self.calculate(97890.0, -5633), 103523.00)

    def test0216(self):
        self.assertEquals(self.calculate(190410.0, -17648), 208058.00)

    def test0217(self):
        self.assertEquals(self.calculate(12214.0, -29098), 41312.00)

    def test0218(self):
        self.assertEquals(self.calculate(87151.0, -26223), 113374.00)

    def test0219(self):
        self.assertEquals(self.calculate(9438.0, -32086), 41524.00)

    def test0220(self):
        self.assertEquals(self.calculate(-140601.0, 11456), -152057.00)

    def test0221(self):
        self.assertEquals(self.calculate(-162698.0, -27946), -134752.00)

    def test0222(self):
        self.assertEquals(self.calculate(17471.0, 8225), 9246.00)

    def test0223(self):
        self.assertEquals(self.calculate(121105.0, -6724), 127829.00)

    def test0224(self):
        self.assertEquals(self.calculate(177218.0, -2660), 179878.00)

    def test0225(self):
        self.assertEquals(self.calculate(126043.0, -11116), 137159.00)

    def test0226(self):
        self.assertEquals(self.calculate(-192046.0, 8250), -200296.00)

    def test0227(self):
        self.assertEquals(self.calculate(31512.0, 3797), 27715.00)

    def test0228(self):
        self.assertEquals(self.calculate(148024.0, -21139), 169163.00)

    def test0229(self):
        self.assertEquals(self.calculate(160856.0, 20540), 140316.00)

    def test0230(self):
        self.assertEquals(self.calculate(-62064.0, -13883), -48181.00)

    def test0231(self):
        self.assertEquals(self.calculate(148980.0, -28115), 177095.00)

    def test0232(self):
        self.assertEquals(self.calculate(48150.0, -5936), 54086.00)

    def test0233(self):
        self.assertEquals(self.calculate(-94937.0, 5353), -100290.00)

    def test0234(self):
        self.assertEquals(self.calculate(113854.0, 21845), 92009.00)

    def test0235(self):
        self.assertEquals(self.calculate(196449.0, -9702), 206151.00)

    def test0236(self):
        self.assertEquals(self.calculate(-179171.0, -15008), -164163.00)

    def test0237(self):
        self.assertEquals(self.calculate(-173406.0, -16988), -156418.00)

    def test0238(self):
        self.assertEquals(self.calculate(71370.0, -12890), 84260.00)

    def test0239(self):
        self.assertEquals(self.calculate(-76372.0, -25836), -50536.00)

    def test0240(self):
        self.assertEquals(self.calculate(-144368.0, 2565), -146933.00)

    def test0241(self):
        self.assertEquals(self.calculate(40508.0, -22042), 62550.00)

    def test0242(self):
        self.assertEquals(self.calculate(-71672.0, -11772), -59900.00)

    def test0243(self):
        self.assertEquals(self.calculate(98459.0, -23395), 121854.00)

    def test0244(self):
        self.assertEquals(self.calculate(18180.0, 25404), -7224.00)

    def test0245(self):
        self.assertEquals(self.calculate(190806.0, 16697), 174109.00)

    def test0246(self):
        self.assertEquals(self.calculate(-60005.0, 21619), -81624.00)

    def test0247(self):
        self.assertEquals(self.calculate(-2280.0, 10258), -12538.00)

    def test0248(self):
        self.assertEquals(self.calculate(-171910.0, -31043), -140867.00)

    def test0249(self):
        self.assertEquals(self.calculate(6249.0, -25818), 32067.00)

    def test0250(self):
        self.assertEquals(self.calculate(191904.0, 11154), 180750.00)

    def test0251(self):
        self.assertEquals(self.calculate(-47292.0, 11589), -58881.00)

    def test0252(self):
        self.assertEquals(self.calculate(-129568.0, -9660), -119908.00)

    def test0253(self):
        self.assertEquals(self.calculate(19192.0, -32253), 51445.00)

    def test0254(self):
        self.assertEquals(self.calculate(180670.0, -23849), 204519.00)

    def test0255(self):
        self.assertEquals(self.calculate(-68111.0, -23656), -44455.00)

    def test0256(self):
        self.assertEquals(self.calculate(-169239.0, -1940), -167299.00)

    def test0257(self):
        self.assertEquals(self.calculate(139539.0, -17569), 157108.00)

    def test0258(self):
        self.assertEquals(self.calculate(42443.0, -32507), 74950.00)

    def test0259(self):
        self.assertEquals(self.calculate(95045.0, 24133), 70912.00)

    def test0260(self):
        self.assertEquals(self.calculate(-34665.0, -24413), -10252.00)

    def test0261(self):
        self.assertEquals(self.calculate(-25964.0, 20236), -46200.00)

    def test0262(self):
        self.assertEquals(self.calculate(-31177.0, -32175), 998.00)

    def test0263(self):
        self.assertEquals(self.calculate(65170.0, -993), 66163.00)

    def test0264(self):
        self.assertEquals(self.calculate(-157988.0, 32343), -190331.00)

    def test0265(self):
        self.assertEquals(self.calculate(94466.0, -25689), 120155.00)

    def test0266(self):
        self.assertEquals(self.calculate(87778.0, -27230), 115008.00)

    def test0267(self):
        self.assertEquals(self.calculate(-18647.0, 15022), -33669.00)

    def test0268(self):
        self.assertEquals(self.calculate(-144823.0, 11921), -156744.00)

    def test0269(self):
        self.assertEquals(self.calculate(53719.0, -8), 53727.00)

    def test0270(self):
        self.assertEquals(self.calculate(3707.0, 32427), -28720.00)

    def test0271(self):
        self.assertEquals(self.calculate(65158.0, -15628), 80786.00)

    def test0272(self):
        self.assertEquals(self.calculate(152239.0, 2006), 150233.00)

    def test0273(self):
        self.assertEquals(self.calculate(139721.0, 11310), 128411.00)

    def test0274(self):
        self.assertEquals(self.calculate(-26162.0, 8272), -34434.00)

    def test0275(self):
        self.assertEquals(self.calculate(192334.0, 2936), 189398.00)

    def test0276(self):
        self.assertEquals(self.calculate(132212.0, 15251), 116961.00)

    def test0277(self):
        self.assertEquals(self.calculate(-185141.0, 4831), -189972.00)

    def test0278(self):
        self.assertEquals(self.calculate(-1178.0, -25827), 24649.00)

    def test0279(self):
        self.assertEquals(self.calculate(-112877.0, -25062), -87815.00)

    def test0280(self):
        self.assertEquals(self.calculate(137673.0, -25608), 163281.00)

    def test0281(self):
        self.assertEquals(self.calculate(-65277.0, -20796), -44481.00)

    def test0282(self):
        self.assertEquals(self.calculate(-127814.0, 21842), -149656.00)

    def test0283(self):
        self.assertEquals(self.calculate(42112.0, 8809), 33303.00)

    def test0284(self):
        self.assertEquals(self.calculate(90091.0, -4523), 94614.00)

    def test0285(self):
        self.assertEquals(self.calculate(36336.0, -15289), 51625.00)

    def test0286(self):
        self.assertEquals(self.calculate(40310.0, 12807), 27503.00)

    def test0287(self):
        self.assertEquals(self.calculate(-130767.0, 2809), -133576.00)

    def test0288(self):
        self.assertEquals(self.calculate(152998.0, 6914), 146084.00)

    def test0289(self):
        self.assertEquals(self.calculate(176874.0, 5021), 171853.00)

    def test0290(self):
        self.assertEquals(self.calculate(56232.0, -30927), 87159.00)

    def test0291(self):
        self.assertEquals(self.calculate(-95593.0, -21517), -74076.00)

    def test0292(self):
        self.assertEquals(self.calculate(180415.0, 7864), 172551.00)

    def test0293(self):
        self.assertEquals(self.calculate(122461.0, -6081), 128542.00)

    def test0294(self):
        self.assertEquals(self.calculate(-159600.0, -6185), -153415.00)

    def test0295(self):
        self.assertEquals(self.calculate(-90405.0, 8520), -98925.00)

    def test0296(self):
        self.assertEquals(self.calculate(158727.0, 11601), 147126.00)

    def test0297(self):
        self.assertEquals(self.calculate(113742.0, 3774), 109968.00)

    def test0298(self):
        self.assertEquals(self.calculate(38128.0, 14000), 24128.00)

    def test0299(self):
        self.assertEquals(self.calculate(14715.0, -14585), 29300.00)

    def test0300(self):
        self.assertEquals(self.calculate(-20978.0, -3148), -17830.00)

    def test0301(self):
        self.assertEquals(self.calculate(172572.0, 27987), 144585.00)

    def test0302(self):
        self.assertEquals(self.calculate(84154.0, 3352), 80802.00)

    def test0303(self):
        self.assertEquals(self.calculate(-159484.0, 22375), -181859.00)

    def test0304(self):
        self.assertEquals(self.calculate(-175599.0, 18788), -194387.00)

    def test0305(self):
        self.assertEquals(self.calculate(70968.0, -15408), 86376.00)

    def test0306(self):
        self.assertEquals(self.calculate(-98678.0, 9437), -108115.00)

    def test0307(self):
        self.assertEquals(self.calculate(-7123.0, 28440), -35563.00)

    def test0308(self):
        self.assertEquals(self.calculate(-185295.0, -7523), -177772.00)

    def test0309(self):
        self.assertEquals(self.calculate(49723.0, -283), 50006.00)

    def test0310(self):
        self.assertEquals(self.calculate(5331.0, 14164), -8833.00)

    def test0311(self):
        self.assertEquals(self.calculate(-68262.0, 1346), -69608.00)

    def test0312(self):
        self.assertEquals(self.calculate(166409.0, -20821), 187230.00)

    def test0313(self):
        self.assertEquals(self.calculate(-42799.0, -14391), -28408.00)

    def test0314(self):
        self.assertEquals(self.calculate(-46475.0, 15884), -62359.00)

    def test0315(self):
        self.assertEquals(self.calculate(96405.0, -1777), 98182.00)

    def test0316(self):
        self.assertEquals(self.calculate(-86205.0, -30588), -55617.00)

    def test0317(self):
        self.assertEquals(self.calculate(-189459.0, -26110), -163349.00)

    def test0318(self):
        self.assertEquals(self.calculate(-152977.0, 8475), -161452.00)

    def test0319(self):
        self.assertEquals(self.calculate(-27438.0, 22053), -49491.00)

    def test0320(self):
        self.assertEquals(self.calculate(69444.0, -24032), 93476.00)

    def test0321(self):
        self.assertEquals(self.calculate(34212.0, -25594), 59806.00)

    def test0322(self):
        self.assertEquals(self.calculate(96000.0, 10369), 85631.00)

    def test0323(self):
        self.assertEquals(self.calculate(-105163.0, -4929), -100234.00)

    def test0324(self):
        self.assertEquals(self.calculate(101688.0, -4175), 105863.00)

    def test0325(self):
        self.assertEquals(self.calculate(4783.0, -32472), 37255.00)

    def test0326(self):
        self.assertEquals(self.calculate(101631.0, -27908), 129539.00)

    def test0327(self):
        self.assertEquals(self.calculate(120607.0, 13782), 106825.00)

    def test0328(self):
        self.assertEquals(self.calculate(138366.0, -15254), 153620.00)

    def test0329(self):
        self.assertEquals(self.calculate(-124811.0, -23177), -101634.00)

    def test0330(self):
        self.assertEquals(self.calculate(147733.0, -20008), 167741.00)

    def test0331(self):
        self.assertEquals(self.calculate(-47272.0, -20780), -26492.00)

    def test0332(self):
        self.assertEquals(self.calculate(-127394.0, -8446), -118948.00)

    def test0333(self):
        self.assertEquals(self.calculate(115887.0, 20175), 95712.00)

    def test0334(self):
        self.assertEquals(self.calculate(114987.0, 23864), 91123.00)

    def test0335(self):
        self.assertEquals(self.calculate(-15341.0, -6336), -9005.00)

    def test0336(self):
        self.assertEquals(self.calculate(-49917.0, 1973), -51890.00)

    def test0337(self):
        self.assertEquals(self.calculate(-172288.0, -26992), -145296.00)

    def test0338(self):
        self.assertEquals(self.calculate(138193.0, -3510), 141703.00)

    def test0339(self):
        self.assertEquals(self.calculate(-111031.0, 2771), -113802.00)

    def test0340(self):
        self.assertEquals(self.calculate(64648.0, -16344), 80992.00)

    def test0341(self):
        self.assertEquals(self.calculate(142889.0, -7725), 150614.00)

    def test0342(self):
        self.assertEquals(self.calculate(-198600.0, 11772), -210372.00)

    def test0343(self):
        self.assertEquals(self.calculate(-53387.0, 23902), -77289.00)

    def test0344(self):
        self.assertEquals(self.calculate(-103025.0, -26005), -77020.00)

    def test0345(self):
        self.assertEquals(self.calculate(-10846.0, 1611), -12457.00)

    def test0346(self):
        self.assertEquals(self.calculate(64963.0, -22700), 87663.00)

    def test0347(self):
        self.assertEquals(self.calculate(58093.0, 8772), 49321.00)

    def test0348(self):
        self.assertEquals(self.calculate(75653.0, -28721), 104374.00)

    def test0349(self):
        self.assertEquals(self.calculate(-188451.0, 19934), -208385.00)

    def test0350(self):
        self.assertEquals(self.calculate(-19990.0, -12499), -7491.00)

    def test0351(self):
        self.assertEquals(self.calculate(-95339.0, -2952), -92387.00)

    def test0352(self):
        self.assertEquals(self.calculate(182563.0, 31070), 151493.00)

    def test0353(self):
        self.assertEquals(self.calculate(132707.0, -24100), 156807.00)

    def test0354(self):
        self.assertEquals(self.calculate(67317.0, -10745), 78062.00)

    def test0355(self):
        self.assertEquals(self.calculate(-120872.0, 30694), -151566.00)

    def test0356(self):
        self.assertEquals(self.calculate(3446.0, -27126), 30572.00)

    def test0357(self):
        self.assertEquals(self.calculate(-87685.0, -475), -87210.00)

    def test0358(self):
        self.assertEquals(self.calculate(98844.0, -9470), 108314.00)

    def test0359(self):
        self.assertEquals(self.calculate(-174757.0, 27554), -202311.00)

    def test0360(self):
        self.assertEquals(self.calculate(14632.0, 14582), 50.00)

    def test0361(self):
        self.assertEquals(self.calculate(-73926.0, 13198), -87124.00)

    def test0362(self):
        self.assertEquals(self.calculate(-41344.0, 1897), -43241.00)

    def test0363(self):
        self.assertEquals(self.calculate(71232.0, -12532), 83764.00)

    def test0364(self):
        self.assertEquals(self.calculate(-193304.0, -5862), -187442.00)

    def test0365(self):
        self.assertEquals(self.calculate(-110126.0, -28705), -81421.00)

    def test0366(self):
        self.assertEquals(self.calculate(-60522.0, 14532), -75054.00)

    def test0367(self):
        self.assertEquals(self.calculate(-164003.0, 24506), -188509.00)

    def test0368(self):
        self.assertEquals(self.calculate(-18756.0, -25468), 6712.00)

    def test0369(self):
        self.assertEquals(self.calculate(50569.0, 20220), 30349.00)

    def test0370(self):
        self.assertEquals(self.calculate(-66119.0, -11866), -54253.00)

    def test0371(self):
        self.assertEquals(self.calculate(-163843.0, 22125), -185968.00)

    def test0372(self):
        self.assertEquals(self.calculate(-31822.0, 766), -32588.00)

    def test0373(self):
        self.assertEquals(self.calculate(-19904.0, -24952), 5048.00)

    def test0374(self):
        self.assertEquals(self.calculate(-52634.0, 23280), -75914.00)

    def test0375(self):
        self.assertEquals(self.calculate(-4559.0, 10769), -15328.00)

    def test0376(self):
        self.assertEquals(self.calculate(110090.0, 29634), 80456.00)

    def test0377(self):
        self.assertEquals(self.calculate(100358.0, 5759), 94599.00)

    def test0378(self):
        self.assertEquals(self.calculate(-45806.0, -30145), -15661.00)

    def test0379(self):
        self.assertEquals(self.calculate(142003.0, 31185), 110818.00)

    def test0380(self):
        self.assertEquals(self.calculate(-23962.0, 10525), -34487.00)

    def test0381(self):
        self.assertEquals(self.calculate(-54921.0, 18017), -72938.00)

    def test0382(self):
        self.assertEquals(self.calculate(-67333.0, 5879), -73212.00)

    def test0383(self):
        self.assertEquals(self.calculate(92362.0, 3136), 89226.00)

    def test0384(self):
        self.assertEquals(self.calculate(60796.0, -28724), 89520.00)

    def test0385(self):
        self.assertEquals(self.calculate(-127121.0, 22126), -149247.00)

    def test0386(self):
        self.assertEquals(self.calculate(101405.0, -18404), 119809.00)

    def test0387(self):
        self.assertEquals(self.calculate(116888.0, 18469), 98419.00)

    def test0388(self):
        self.assertEquals(self.calculate(-116882.0, -13670), -103212.00)

    def test0389(self):
        self.assertEquals(self.calculate(-83505.0, -6294), -77211.00)

    def test0390(self):
        self.assertEquals(self.calculate(-54185.0, -3427), -50758.00)

    def test0391(self):
        self.assertEquals(self.calculate(-192253.0, 4399), -196652.00)

    def test0392(self):
        self.assertEquals(self.calculate(-81468.0, 21031), -102499.00)

    def test0393(self):
        self.assertEquals(self.calculate(177544.0, 8697), 168847.00)

    def test0394(self):
        self.assertEquals(self.calculate(74620.0, -24851), 99471.00)

    def test0395(self):
        self.assertEquals(self.calculate(-104499.0, -29163), -75336.00)

    def test0396(self):
        self.assertEquals(self.calculate(99276.0, 8411), 90865.00)

    def test0397(self):
        self.assertEquals(self.calculate(157203.0, 396), 156807.00)

    def test0398(self):
        self.assertEquals(self.calculate(66678.0, -13674), 80352.00)

    def test0399(self):
        self.assertEquals(self.calculate(8193.0, -6657), 14850.00)

    def test0400(self):
        self.assertEquals(self.calculate(50614.0, 17955), 32659.00)

    def test0401(self):
        self.assertEquals(self.calculate(181783.0, -28129), 209912.00)

    def test0402(self):
        self.assertEquals(self.calculate(98879.0, -29677), 128556.00)

    def test0403(self):
        self.assertEquals(self.calculate(81851.0, -11332), 93183.00)

    def test0404(self):
        self.assertEquals(self.calculate(-63456.0, 10035), -73491.00)

    def test0405(self):
        self.assertEquals(self.calculate(-33685.0, 23953), -57638.00)

    def test0406(self):
        self.assertEquals(self.calculate(-182588.0, -15394), -167194.00)

    def test0407(self):
        self.assertEquals(self.calculate(-179767.0, 4679), -184446.00)

    def test0408(self):
        self.assertEquals(self.calculate(157649.0, 22245), 135404.00)

    def test0409(self):
        self.assertEquals(self.calculate(-177252.0, 5832), -183084.00)

    def test0410(self):
        self.assertEquals(self.calculate(122775.0, 17843), 104932.00)

    def test0411(self):
        self.assertEquals(self.calculate(124322.0, 28786), 95536.00)

    def test0412(self):
        self.assertEquals(self.calculate(105048.0, -3967), 109015.00)

    def test0413(self):
        self.assertEquals(self.calculate(115215.0, 28219), 86996.00)

    def test0414(self):
        self.assertEquals(self.calculate(-9865.0, -31807), 21942.00)

    def test0415(self):
        self.assertEquals(self.calculate(-279.0, -20097), 19818.00)

    def test0416(self):
        self.assertEquals(self.calculate(196853.0, 24633), 172220.00)

    def test0417(self):
        self.assertEquals(self.calculate(46622.0, 1096), 45526.00)

    def test0418(self):
        self.assertEquals(self.calculate(26861.0, 19501), 7360.00)

    def test0419(self):
        self.assertEquals(self.calculate(75572.0, 19700), 55872.00)

    def test0420(self):
        self.assertEquals(self.calculate(-104761.0, 2284), -107045.00)

    def test0421(self):
        self.assertEquals(self.calculate(-52234.0, -24014), -28220.00)

    def test0422(self):
        self.assertEquals(self.calculate(42111.0, -10459), 52570.00)

    def test0423(self):
        self.assertEquals(self.calculate(67359.0, 11751), 55608.00)

    def test0424(self):
        self.assertEquals(self.calculate(70650.0, 1988), 68662.00)

    def test0425(self):
        self.assertEquals(self.calculate(110676.0, 9343), 101333.00)

    def test0426(self):
        self.assertEquals(self.calculate(-136406.0, -20408), -115998.00)

    def test0427(self):
        self.assertEquals(self.calculate(-185485.0, 13656), -199141.00)

    def test0428(self):
        self.assertEquals(self.calculate(4975.0, -21634), 26609.00)

    def test0429(self):
        self.assertEquals(self.calculate(91142.0, 6877), 84265.00)

    def test0430(self):
        self.assertEquals(self.calculate(-171213.0, 16402), -187615.00)

    def test0431(self):
        self.assertEquals(self.calculate(-156391.0, -31448), -124943.00)

    def test0432(self):
        self.assertEquals(self.calculate(-173881.0, 22350), -196231.00)

    def test0433(self):
        self.assertEquals(self.calculate(-104186.0, 4042), -108228.00)

    def test0434(self):
        self.assertEquals(self.calculate(-168140.0, 1854), -169994.00)

    def test0435(self):
        self.assertEquals(self.calculate(89771.0, -29668), 119439.00)

    def test0436(self):
        self.assertEquals(self.calculate(-111490.0, 12510), -124000.00)

    def test0437(self):
        self.assertEquals(self.calculate(-21122.0, -14656), -6466.00)

    def test0438(self):
        self.assertEquals(self.calculate(-169253.0, -12612), -156641.00)

    def test0439(self):
        self.assertEquals(self.calculate(72009.0, 3297), 68712.00)

    def test0440(self):
        self.assertEquals(self.calculate(-151280.0, -13166), -138114.00)

    def test0441(self):
        self.assertEquals(self.calculate(-170345.0, 2425), -172770.00)

    def test0442(self):
        self.assertEquals(self.calculate(148236.0, -25112), 173348.00)

    def test0443(self):
        self.assertEquals(self.calculate(-61449.0, 3906), -65355.00)

    def test0444(self):
        self.assertEquals(self.calculate(155643.0, -15979), 171622.00)

    def test0445(self):
        self.assertEquals(self.calculate(22199.0, 2345), 19854.00)

    def test0446(self):
        self.assertEquals(self.calculate(-162411.0, 22444), -184855.00)

    def test0447(self):
        self.assertEquals(self.calculate(-149427.0, 6340), -155767.00)

    def test0448(self):
        self.assertEquals(self.calculate(-179856.0, -8932), -170924.00)

    def test0449(self):
        self.assertEquals(self.calculate(-4610.0, -27412), 22802.00)

    def test0450(self):
        self.assertEquals(self.calculate(-147204.0, -27677), -119527.00)

    def test0451(self):
        self.assertEquals(self.calculate(148077.0, -26152), 174229.00)

    def test0452(self):
        self.assertEquals(self.calculate(124357.0, -29482), 153839.00)

    def test0453(self):
        self.assertEquals(self.calculate(186626.0, 16703), 169923.00)

    def test0454(self):
        self.assertEquals(self.calculate(104870.0, -9753), 114623.00)

    def test0455(self):
        self.assertEquals(self.calculate(-196293.0, 1102), -197395.00)

    def test0456(self):
        self.assertEquals(self.calculate(71698.0, -12857), 84555.00)

    def test0457(self):
        self.assertEquals(self.calculate(191613.0, 14494), 177119.00)

    def test0458(self):
        self.assertEquals(self.calculate(122947.0, 12065), 110882.00)

    def test0459(self):
        self.assertEquals(self.calculate(-118091.0, 22438), -140529.00)

    def test0460(self):
        self.assertEquals(self.calculate(-20133.0, 22658), -42791.00)

    def test0461(self):
        self.assertEquals(self.calculate(-66331.0, -18463), -47868.00)

    def test0462(self):
        self.assertEquals(self.calculate(101251.0, -15069), 116320.00)

    def test0463(self):
        self.assertEquals(self.calculate(-31909.0, -14111), -17798.00)

    def test0464(self):
        self.assertEquals(self.calculate(-158137.0, 5190), -163327.00)

    def test0465(self):
        self.assertEquals(self.calculate(-158125.0, -28751), -129374.00)

    def test0466(self):
        self.assertEquals(self.calculate(60563.0, -31538), 92101.00)

    def test0467(self):
        self.assertEquals(self.calculate(-163557.0, 24035), -187592.00)

    def test0468(self):
        self.assertEquals(self.calculate(-121199.0, -5249), -115950.00)

    def test0469(self):
        self.assertEquals(self.calculate(191354.0, -28160), 219514.00)

    def test0470(self):
        self.assertEquals(self.calculate(-57286.0, -11202), -46084.00)

    def test0471(self):
        self.assertEquals(self.calculate(34959.0, 765), 34194.00)

    def test0472(self):
        self.assertEquals(self.calculate(132142.0, 7888), 124254.00)

    def test0473(self):
        self.assertEquals(self.calculate(-120252.0, -4847), -115405.00)

    def test0474(self):
        self.assertEquals(self.calculate(-164849.0, -29828), -135021.00)

    def test0475(self):
        self.assertEquals(self.calculate(-96896.0, -16259), -80637.00)

    def test0476(self):
        self.assertEquals(self.calculate(-48532.0, 15675), -64207.00)

    def test0477(self):
        self.assertEquals(self.calculate(136907.0, -25648), 162555.00)

    def test0478(self):
        self.assertEquals(self.calculate(-154473.0, 5584), -160057.00)

    def test0479(self):
        self.assertEquals(self.calculate(-145763.0, -18526), -127237.00)

    def test0480(self):
        self.assertEquals(self.calculate(23331.0, -20526), 43857.00)

    def test0481(self):
        self.assertEquals(self.calculate(-120511.0, 21324), -141835.00)

    def test0482(self):
        self.assertEquals(self.calculate(1332.0, 7681), -6349.00)

    def test0483(self):
        self.assertEquals(self.calculate(80950.0, -19706), 100656.00)

    def test0484(self):
        self.assertEquals(self.calculate(-54082.0, -12419), -41663.00)

    def test0485(self):
        self.assertEquals(self.calculate(-26131.0, 19613), -45744.00)

    def test0486(self):
        self.assertEquals(self.calculate(-93544.0, 31673), -125217.00)

    def test0487(self):
        self.assertEquals(self.calculate(66036.0, -16219), 82255.00)

    def test0488(self):
        self.assertEquals(self.calculate(111293.0, -19113), 130406.00)

    def test0489(self):
        self.assertEquals(self.calculate(29879.0, -16431), 46310.00)

    def test0490(self):
        self.assertEquals(self.calculate(181080.0, 17054), 164026.00)

    def test0491(self):
        self.assertEquals(self.calculate(106591.0, 31598), 74993.00)

    def test0492(self):
        self.assertEquals(self.calculate(-53582.0, 23973), -77555.00)

    def test0493(self):
        self.assertEquals(self.calculate(-27639.0, -30946), 3307.00)

    def test0494(self):
        self.assertEquals(self.calculate(-46511.0, -7981), -38530.00)

    def test0495(self):
        self.assertEquals(self.calculate(-164782.0, 9370), -174152.00)

    def test0496(self):
        self.assertEquals(self.calculate(-127776.0, 21964), -149740.00)

    def test0497(self):
        self.assertEquals(self.calculate(-168124.0, 1258), -169382.00)

    def test0498(self):
        self.assertEquals(self.calculate(-15200.0, 18064), -33264.00)

    def test0499(self):
        self.assertEquals(self.calculate(-180686.0, 19567), -200253.00)

    def test0500(self):
        self.assertEquals(self.calculate(-157745.0, -13603), -144142.00)

    def test0501(self):
        self.assertEquals(self.calculate(165698.0, 29438), 136260.00)

    def test0502(self):
        self.assertEquals(self.calculate(-148214.0, 22217), -170431.00)

    def test0503(self):
        self.assertEquals(self.calculate(127502.0, -15138), 142640.00)

    def test0504(self):
        self.assertEquals(self.calculate(-198711.0, 10352), -209063.00)

    def test0505(self):
        self.assertEquals(self.calculate(-151656.0, -21312), -130344.00)

    def test0506(self):
        self.assertEquals(self.calculate(192154.0, 2239), 189915.00)

    def test0507(self):
        self.assertEquals(self.calculate(28457.0, 23248), 5209.00)

    def test0508(self):
        self.assertEquals(self.calculate(52068.0, 28237), 23831.00)

    def test0509(self):
        self.assertEquals(self.calculate(148208.0, -28758), 176966.00)

    def test0510(self):
        self.assertEquals(self.calculate(-43323.0, 6085), -49408.00)

    def test0511(self):
        self.assertEquals(self.calculate(73658.0, 19266), 54392.00)

    def test0512(self):
        self.assertEquals(self.calculate(-54536.0, 20949), -75485.00)

    def test0513(self):
        self.assertEquals(self.calculate(725.0, 2827), -2102.00)

    def test0514(self):
        self.assertEquals(self.calculate(172484.0, -31795), 204279.00)

    def test0515(self):
        self.assertEquals(self.calculate(51141.0, -30410), 81551.00)

    def test0516(self):
        self.assertEquals(self.calculate(-56180.0, -12568), -43612.00)

    def test0517(self):
        self.assertEquals(self.calculate(-110485.0, -15087), -95398.00)

    def test0518(self):
        self.assertEquals(self.calculate(-72041.0, -16196), -55845.00)

    def test0519(self):
        self.assertEquals(self.calculate(46992.0, 30821), 16171.00)

    def test0520(self):
        self.assertEquals(self.calculate(-93685.0, -3505), -90180.00)

    def test0521(self):
        self.assertEquals(self.calculate(-29559.0, 1200), -30759.00)

    def test0522(self):
        self.assertEquals(self.calculate(-64059.0, 765), -64824.00)

    def test0523(self):
        self.assertEquals(self.calculate(10959.0, 26840), -15881.00)

    def test0524(self):
        self.assertEquals(self.calculate(-9534.0, 10483), -20017.00)

    def test0525(self):
        self.assertEquals(self.calculate(-131101.0, 12290), -143391.00)

    def test0526(self):
        self.assertEquals(self.calculate(-150616.0, -14628), -135988.00)

    def test0527(self):
        self.assertEquals(self.calculate(24897.0, -24994), 49891.00)

    def test0528(self):
        self.assertEquals(self.calculate(142446.0, 29192), 113254.00)

    def test0529(self):
        self.assertEquals(self.calculate(-104356.0, 32588), -136944.00)

    def test0530(self):
        self.assertEquals(self.calculate(149488.0, 30973), 118515.00)

    def test0531(self):
        self.assertEquals(self.calculate(-112127.0, -22311), -89816.00)

    def test0532(self):
        self.assertEquals(self.calculate(174732.0, 23691), 151041.00)

    def test0533(self):
        self.assertEquals(self.calculate(-127588.0, 25061), -152649.00)

    def test0534(self):
        self.assertEquals(self.calculate(48556.0, 4332), 44224.00)

    def test0535(self):
        self.assertEquals(self.calculate(173555.0, 32095), 141460.00)

    def test0536(self):
        self.assertEquals(self.calculate(-132544.0, -25412), -107132.00)

    def test0537(self):
        self.assertEquals(self.calculate(-188727.0, 6864), -195591.00)

    def test0538(self):
        self.assertEquals(self.calculate(-53645.0, -31974), -21671.00)

    def test0539(self):
        self.assertEquals(self.calculate(-155237.0, -15359), -139878.00)

    def test0540(self):
        self.assertEquals(self.calculate(-45911.0, 27354), -73265.00)

    def test0541(self):
        self.assertEquals(self.calculate(-16250.0, -10270), -5980.00)

    def test0542(self):
        self.assertEquals(self.calculate(124126.0, 9068), 115058.00)

    def test0543(self):
        self.assertEquals(self.calculate(117325.0, -7897), 125222.00)

    def test0544(self):
        self.assertEquals(self.calculate(-129331.0, -25600), -103731.00)

    def test0545(self):
        self.assertEquals(self.calculate(-38249.0, 7498), -45747.00)

    def test0546(self):
        self.assertEquals(self.calculate(119255.0, 11086), 108169.00)

    def test0547(self):
        self.assertEquals(self.calculate(-97689.0, -13771), -83918.00)

    def test0548(self):
        self.assertEquals(self.calculate(-86314.0, 9378), -95692.00)

    def test0549(self):
        self.assertEquals(self.calculate(96139.0, -358), 96497.00)

    def test0550(self):
        self.assertEquals(self.calculate(-159522.0, -25458), -134064.00)

    def test0551(self):
        self.assertEquals(self.calculate(160040.0, -31917), 191957.00)

    def test0552(self):
        self.assertEquals(self.calculate(-138634.0, -12148), -126486.00)

    def test0553(self):
        self.assertEquals(self.calculate(-144900.0, 3169), -148069.00)

    def test0554(self):
        self.assertEquals(self.calculate(-105565.0, -14064), -91501.00)

    def test0555(self):
        self.assertEquals(self.calculate(-187509.0, -1297), -186212.00)

    def test0556(self):
        self.assertEquals(self.calculate(3333.0, -31929), 35262.00)

    def test0557(self):
        self.assertEquals(self.calculate(-28259.0, 20225), -48484.00)

    def test0558(self):
        self.assertEquals(self.calculate(-9486.0, -17073), 7587.00)

    def test0559(self):
        self.assertEquals(self.calculate(10363.0, 8242), 2121.00)

    def test0560(self):
        self.assertEquals(self.calculate(-192892.0, -27495), -165397.00)

    def test0561(self):
        self.assertEquals(self.calculate(115643.0, 7610), 108033.00)

    def test0562(self):
        self.assertEquals(self.calculate(133709.0, 13707), 120002.00)

    def test0563(self):
        self.assertEquals(self.calculate(-116866.0, -3920), -112946.00)

    def test0564(self):
        self.assertEquals(self.calculate(-187643.0, -20538), -167105.00)

    def test0565(self):
        self.assertEquals(self.calculate(-149219.0, -9942), -139277.00)

    def test0566(self):
        self.assertEquals(self.calculate(-160296.0, -12135), -148161.00)

    def test0567(self):
        self.assertEquals(self.calculate(-121510.0, 26168), -147678.00)

    def test0568(self):
        self.assertEquals(self.calculate(-46781.0, -24828), -21953.00)

    def test0569(self):
        self.assertEquals(self.calculate(155044.0, -1115), 156159.00)

    def test0570(self):
        self.assertEquals(self.calculate(-73096.0, -13481), -59615.00)

    def test0571(self):
        self.assertEquals(self.calculate(192768.0, 21695), 171073.00)

    def test0572(self):
        self.assertEquals(self.calculate(-94493.0, -3468), -91025.00)

    def test0573(self):
        self.assertEquals(self.calculate(-177737.0, -4177), -173560.00)

    def test0574(self):
        self.assertEquals(self.calculate(66052.0, -27138), 93190.00)

    def test0575(self):
        self.assertEquals(self.calculate(-85656.0, 12049), -97705.00)

    def test0576(self):
        self.assertEquals(self.calculate(24264.0, 16001), 8263.00)

    def test0577(self):
        self.assertEquals(self.calculate(-94382.0, -14116), -80266.00)

    def test0578(self):
        self.assertEquals(self.calculate(-179763.0, 20312), -200075.00)

    def test0579(self):
        self.assertEquals(self.calculate(108918.0, -19407), 128325.00)

    def test0580(self):
        self.assertEquals(self.calculate(-20177.0, -3130), -17047.00)

    def test0581(self):
        self.assertEquals(self.calculate(-130924.0, 22814), -153738.00)

    def test0582(self):
        self.assertEquals(self.calculate(118631.0, 16859), 101772.00)

    def test0583(self):
        self.assertEquals(self.calculate(5499.0, 16255), -10756.00)

    def test0584(self):
        self.assertEquals(self.calculate(184923.0, 11871), 173052.00)

    def test0585(self):
        self.assertEquals(self.calculate(94445.0, 30026), 64419.00)

    def test0586(self):
        self.assertEquals(self.calculate(-161283.0, -2012), -159271.00)

    def test0587(self):
        self.assertEquals(self.calculate(-833.0, -9022), 8189.00)

    def test0588(self):
        self.assertEquals(self.calculate(-122853.0, -29148), -93705.00)

    def test0589(self):
        self.assertEquals(self.calculate(-44983.0, -27732), -17251.00)

    def test0590(self):
        self.assertEquals(self.calculate(-78728.0, 31324), -110052.00)

    def test0591(self):
        self.assertEquals(self.calculate(-25999.0, -16448), -9551.00)

    def test0592(self):
        self.assertEquals(self.calculate(-107616.0, 11745), -119361.00)

    def test0593(self):
        self.assertEquals(self.calculate(130011.0, -22814), 152825.00)

    def test0594(self):
        self.assertEquals(self.calculate(39646.0, 4692), 34954.00)

    def test0595(self):
        self.assertEquals(self.calculate(146311.0, -15967), 162278.00)

    def test0596(self):
        self.assertEquals(self.calculate(54390.0, 23639), 30751.00)

    def test0597(self):
        self.assertEquals(self.calculate(15566.0, 12504), 3062.00)

    def test0598(self):
        self.assertEquals(self.calculate(-97715.0, -12096), -85619.00)

    def test0599(self):
        self.assertEquals(self.calculate(-91203.0, -29075), -62128.00)

    def test0600(self):
        self.assertEquals(self.calculate(79914.0, 13184), 66730.00)

    def test0601(self):
        self.assertEquals(self.calculate(-198814.0, -4931), -193883.00)

    def test0602(self):
        self.assertEquals(self.calculate(50709.0, -114), 50823.00)

    def test0603(self):
        self.assertEquals(self.calculate(170927.0, -25211), 196138.00)

    def test0604(self):
        self.assertEquals(self.calculate(-82911.0, 23310), -106221.00)

    def test0605(self):
        self.assertEquals(self.calculate(-143885.0, -2770), -141115.00)

    def test0606(self):
        self.assertEquals(self.calculate(-85602.0, -6986), -78616.00)

    def test0607(self):
        self.assertEquals(self.calculate(-115776.0, -15327), -100449.00)

    def test0608(self):
        self.assertEquals(self.calculate(147248.0, 19056), 128192.00)

    def test0609(self):
        self.assertEquals(self.calculate(-174885.0, -10335), -164550.00)

    def test0610(self):
        self.assertEquals(self.calculate(-121142.0, -27125), -94017.00)

    def test0611(self):
        self.assertEquals(self.calculate(195871.0, -5267), 201138.00)

    def test0612(self):
        self.assertEquals(self.calculate(-65214.0, 6466), -71680.00)

    def test0613(self):
        self.assertEquals(self.calculate(-186181.0, -14220), -171961.00)

    def test0614(self):
        self.assertEquals(self.calculate(-169840.0, 8727), -178567.00)

    def test0615(self):
        self.assertEquals(self.calculate(37532.0, 25570), 11962.00)

    def test0616(self):
        self.assertEquals(self.calculate(40029.0, 25069), 14960.00)

    def test0617(self):
        self.assertEquals(self.calculate(-196729.0, -28523), -168206.00)

    def test0618(self):
        self.assertEquals(self.calculate(-80652.0, 31203), -111855.00)

    def test0619(self):
        self.assertEquals(self.calculate(107868.0, -26122), 133990.00)

    def test0620(self):
        self.assertEquals(self.calculate(-193180.0, -17437), -175743.00)

    def test0621(self):
        self.assertEquals(self.calculate(2538.0, 30525), -27987.00)

    def test0622(self):
        self.assertEquals(self.calculate(-64974.0, -2974), -62000.00)

    def test0623(self):
        self.assertEquals(self.calculate(163482.0, -2369), 165851.00)

    def test0624(self):
        self.assertEquals(self.calculate(165861.0, 27260), 138601.00)

    def test0625(self):
        self.assertEquals(self.calculate(-57361.0, -17878), -39483.00)

    def test0626(self):
        self.assertEquals(self.calculate(-59030.0, -13357), -45673.00)

    def test0627(self):
        self.assertEquals(self.calculate(180161.0, -5177), 185338.00)

    def test0628(self):
        self.assertEquals(self.calculate(-195245.0, -10918), -184327.00)

    def test0629(self):
        self.assertEquals(self.calculate(-170435.0, -31920), -138515.00)

    def test0630(self):
        self.assertEquals(self.calculate(-109216.0, -10874), -98342.00)

    def test0631(self):
        self.assertEquals(self.calculate(158501.0, -12239), 170740.00)

    def test0632(self):
        self.assertEquals(self.calculate(195272.0, -29040), 224312.00)

    def test0633(self):
        self.assertEquals(self.calculate(-31944.0, -6981), -24963.00)

    def test0634(self):
        self.assertEquals(self.calculate(-55001.0, -20979), -34022.00)

    def test0635(self):
        self.assertEquals(self.calculate(-69137.0, -21193), -47944.00)

    def test0636(self):
        self.assertEquals(self.calculate(-197605.0, -6265), -191340.00)

    def test0637(self):
        self.assertEquals(self.calculate(-2396.0, 16856), -19252.00)

    def test0638(self):
        self.assertEquals(self.calculate(133448.0, -6642), 140090.00)

    def test0639(self):
        self.assertEquals(self.calculate(26542.0, -4847), 31389.00)

    def test0640(self):
        self.assertEquals(self.calculate(-13882.0, -28688), 14806.00)

    def test0641(self):
        self.assertEquals(self.calculate(-2119.0, 29080), -31199.00)

    def test0642(self):
        self.assertEquals(self.calculate(-181566.0, -19016), -162550.00)

    def test0643(self):
        self.assertEquals(self.calculate(-161721.0, -29478), -132243.00)

    def test0644(self):
        self.assertEquals(self.calculate(52745.0, 10873), 41872.00)

    def test0645(self):
        self.assertEquals(self.calculate(16386.0, 15742), 644.00)

    def test0646(self):
        self.assertEquals(self.calculate(77918.0, -15395), 93313.00)

    def test0647(self):
        self.assertEquals(self.calculate(191464.0, 31874), 159590.00)

    def test0648(self):
        self.assertEquals(self.calculate(-48778.0, 4841), -53619.00)

    def test0649(self):
        self.assertEquals(self.calculate(-93618.0, -13499), -80119.00)

    def test0650(self):
        self.assertEquals(self.calculate(-150099.0, 29387), -179486.00)

    def test0651(self):
        self.assertEquals(self.calculate(36199.0, 13540), 22659.00)

    def test0652(self):
        self.assertEquals(self.calculate(131993.0, 30356), 101637.00)

    def test0653(self):
        self.assertEquals(self.calculate(52686.0, 14192), 38494.00)

    def test0654(self):
        self.assertEquals(self.calculate(-54440.0, -3590), -50850.00)

    def test0655(self):
        self.assertEquals(self.calculate(-197414.0, -12201), -185213.00)

    def test0656(self):
        self.assertEquals(self.calculate(134229.0, 16826), 117403.00)

    def test0657(self):
        self.assertEquals(self.calculate(16172.0, 12722), 3450.00)

    def test0658(self):
        self.assertEquals(self.calculate(16904.0, -17489), 34393.00)

    def test0659(self):
        self.assertEquals(self.calculate(-167749.0, 3016), -170765.00)

    def test0660(self):
        self.assertEquals(self.calculate(-87591.0, -3846), -83745.00)

    def test0661(self):
        self.assertEquals(self.calculate(-99965.0, -7770), -92195.00)

    def test0662(self):
        self.assertEquals(self.calculate(197393.0, -25757), 223150.00)

    def test0663(self):
        self.assertEquals(self.calculate(-32979.0, 19798), -52777.00)

    def test0664(self):
        self.assertEquals(self.calculate(2025.0, -3841), 5866.00)

    def test0665(self):
        self.assertEquals(self.calculate(75473.0, -21021), 96494.00)

    def test0666(self):
        self.assertEquals(self.calculate(64177.0, 29969), 34208.00)

    def test0667(self):
        self.assertEquals(self.calculate(-45064.0, 21061), -66125.00)

    def test0668(self):
        self.assertEquals(self.calculate(-76649.0, -22041), -54608.00)

    def test0669(self):
        self.assertEquals(self.calculate(-67056.0, 1237), -68293.00)

    def test0670(self):
        self.assertEquals(self.calculate(-121595.0, -28579), -93016.00)

    def test0671(self):
        self.assertEquals(self.calculate(-162149.0, 21497), -183646.00)

    def test0672(self):
        self.assertEquals(self.calculate(-195447.0, 21890), -217337.00)

    def test0673(self):
        self.assertEquals(self.calculate(67963.0, -20927), 88890.00)

    def test0674(self):
        self.assertEquals(self.calculate(-195215.0, -305), -194910.00)

    def test0675(self):
        self.assertEquals(self.calculate(21590.0, -17425), 39015.00)

    def test0676(self):
        self.assertEquals(self.calculate(-106604.0, 8126), -114730.00)

    def test0677(self):
        self.assertEquals(self.calculate(-62711.0, 32758), -95469.00)

    def test0678(self):
        self.assertEquals(self.calculate(142914.0, 20214), 122700.00)

    def test0679(self):
        self.assertEquals(self.calculate(21101.0, -25413), 46514.00)

    def test0680(self):
        self.assertEquals(self.calculate(-83758.0, -3482), -80276.00)

    def test0681(self):
        self.assertEquals(self.calculate(-52470.0, 14396), -66866.00)

    def test0682(self):
        self.assertEquals(self.calculate(101356.0, 13055), 88301.00)

    def test0683(self):
        self.assertEquals(self.calculate(-90263.0, -2941), -87322.00)

    def test0684(self):
        self.assertEquals(self.calculate(-58609.0, -9369), -49240.00)

    def test0685(self):
        self.assertEquals(self.calculate(-22957.0, -24465), 1508.00)

    def test0686(self):
        self.assertEquals(self.calculate(185140.0, -31108), 216248.00)

    def test0687(self):
        self.assertEquals(self.calculate(-159113.0, -7140), -151973.00)

    def test0688(self):
        self.assertEquals(self.calculate(160221.0, -20693), 180914.00)

    def test0689(self):
        self.assertEquals(self.calculate(-97778.0, -27258), -70520.00)

    def test0690(self):
        self.assertEquals(self.calculate(20166.0, -11309), 31475.00)

    def test0691(self):
        self.assertEquals(self.calculate(158532.0, -22728), 181260.00)

    def test0692(self):
        self.assertEquals(self.calculate(18166.0, -15108), 33274.00)

    def test0693(self):
        self.assertEquals(self.calculate(-199273.0, -12625), -186648.00)

    def test0694(self):
        self.assertEquals(self.calculate(-108813.0, -1918), -106895.00)

    def test0695(self):
        self.assertEquals(self.calculate(-157512.0, -31294), -126218.00)

    def test0696(self):
        self.assertEquals(self.calculate(-54449.0, 1467), -55916.00)

    def test0697(self):
        self.assertEquals(self.calculate(-35103.0, -32455), -2648.00)

    def test0698(self):
        self.assertEquals(self.calculate(160165.0, 7646), 152519.00)

    def test0699(self):
        self.assertEquals(self.calculate(134788.0, -16370), 151158.00)

    def test0700(self):
        self.assertEquals(self.calculate(-40652.0, -9476), -31176.00)

    def test0701(self):
        self.assertEquals(self.calculate(-2385.0, -27402), 25017.00)

    def test0702(self):
        self.assertEquals(self.calculate(-193551.0, 12071), -205622.00)

    def test0703(self):
        self.assertEquals(self.calculate(68890.0, 11957), 56933.00)

    def test0704(self):
        self.assertEquals(self.calculate(191330.0, -31916), 223246.00)

    def test0705(self):
        self.assertEquals(self.calculate(-66512.0, -4612), -61900.00)

    def test0706(self):
        self.assertEquals(self.calculate(161129.0, 25354), 135775.00)

    def test0707(self):
        self.assertEquals(self.calculate(189226.0, -12100), 201326.00)

    def test0708(self):
        self.assertEquals(self.calculate(24359.0, -17319), 41678.00)

    def test0709(self):
        self.assertEquals(self.calculate(180491.0, -947), 181438.00)

    def test0710(self):
        self.assertEquals(self.calculate(-64952.0, -24544), -40408.00)

    def test0711(self):
        self.assertEquals(self.calculate(163415.0, -1921), 165336.00)

    def test0712(self):
        self.assertEquals(self.calculate(32664.0, 15915), 16749.00)

    def test0713(self):
        self.assertEquals(self.calculate(-16669.0, -26324), 9655.00)

    def test0714(self):
        self.assertEquals(self.calculate(-153760.0, 7296), -161056.00)

    def test0715(self):
        self.assertEquals(self.calculate(-98734.0, 28224), -126958.00)

    def test0716(self):
        self.assertEquals(self.calculate(24138.0, -23805), 47943.00)

    def test0717(self):
        self.assertEquals(self.calculate(-183549.0, -8101), -175448.00)

    def test0718(self):
        self.assertEquals(self.calculate(199817.0, 26343), 173474.00)

    def test0719(self):
        self.assertEquals(self.calculate(-92553.0, 11752), -104305.00)

    def test0720(self):
        self.assertEquals(self.calculate(-178434.0, -32732), -145702.00)

    def test0721(self):
        self.assertEquals(self.calculate(-160414.0, -5318), -155096.00)

    def test0722(self):
        self.assertEquals(self.calculate(79537.0, 20064), 59473.00)

    def test0723(self):
        self.assertEquals(self.calculate(69536.0, -19054), 88590.00)

    def test0724(self):
        self.assertEquals(self.calculate(94211.0, -4324), 98535.00)

    def test0725(self):
        self.assertEquals(self.calculate(89762.0, -2083), 91845.00)

    def test0726(self):
        self.assertEquals(self.calculate(55199.0, 27531), 27668.00)

    def test0727(self):
        self.assertEquals(self.calculate(-116482.0, 27435), -143917.00)

    def test0728(self):
        self.assertEquals(self.calculate(-88389.0, -23214), -65175.00)

    def test0729(self):
        self.assertEquals(self.calculate(58674.0, 25380), 33294.00)

    def test0730(self):
        self.assertEquals(self.calculate(-12846.0, -28976), 16130.00)

    def test0731(self):
        self.assertEquals(self.calculate(-94363.0, 30216), -124579.00)

    def test0732(self):
        self.assertEquals(self.calculate(143456.0, -30666), 174122.00)

    def test0733(self):
        self.assertEquals(self.calculate(182167.0, -6341), 188508.00)

    def test0734(self):
        self.assertEquals(self.calculate(156438.0, -6), 156444.00)

    def test0735(self):
        self.assertEquals(self.calculate(-55524.0, -25886), -29638.00)

    def test0736(self):
        self.assertEquals(self.calculate(-126788.0, -11267), -115521.00)

    def test0737(self):
        self.assertEquals(self.calculate(136806.0, -6227), 143033.00)

    def test0738(self):
        self.assertEquals(self.calculate(-140865.0, -25812), -115053.00)

    def test0739(self):
        self.assertEquals(self.calculate(199361.0, 12251), 187110.00)

    def test0740(self):
        self.assertEquals(self.calculate(116502.0, 16043), 100459.00)

    def test0741(self):
        self.assertEquals(self.calculate(-130033.0, 28672), -158705.00)

    def test0742(self):
        self.assertEquals(self.calculate(-169359.0, 31221), -200580.00)

    def test0743(self):
        self.assertEquals(self.calculate(112932.0, -9740), 122672.00)

    def test0744(self):
        self.assertEquals(self.calculate(71418.0, 16512), 54906.00)

    def test0745(self):
        self.assertEquals(self.calculate(12256.0, 21228), -8972.00)

    def test0746(self):
        self.assertEquals(self.calculate(-135619.0, 25861), -161480.00)

    def test0747(self):
        self.assertEquals(self.calculate(104026.0, -22906), 126932.00)

    def test0748(self):
        self.assertEquals(self.calculate(-110587.0, 23758), -134345.00)

    def test0749(self):
        self.assertEquals(self.calculate(22578.0, 6297), 16281.00)

    def test0750(self):
        self.assertEquals(self.calculate(85617.0, -3713), 89330.00)

    def test0751(self):
        self.assertEquals(self.calculate(27871.0, -24538), 52409.00)

    def test0752(self):
        self.assertEquals(self.calculate(6317.0, 23748), -17431.00)

    def test0753(self):
        self.assertEquals(self.calculate(-48221.0, 12978), -61199.00)

    def test0754(self):
        self.assertEquals(self.calculate(101223.0, -10625), 111848.00)

    def test0755(self):
        self.assertEquals(self.calculate(-194189.0, 15569), -209758.00)

    def test0756(self):
        self.assertEquals(self.calculate(123263.0, 8620), 114643.00)

    def test0757(self):
        self.assertEquals(self.calculate(-169081.0, -7765), -161316.00)

    def test0758(self):
        self.assertEquals(self.calculate(-137002.0, 20383), -157385.00)

    def test0759(self):
        self.assertEquals(self.calculate(-112614.0, 30256), -142870.00)

    def test0760(self):
        self.assertEquals(self.calculate(15822.0, -18350), 34172.00)

    def test0761(self):
        self.assertEquals(self.calculate(-67023.0, 16043), -83066.00)

    def test0762(self):
        self.assertEquals(self.calculate(71585.0, 22753), 48832.00)

    def test0763(self):
        self.assertEquals(self.calculate(-129007.0, 11392), -140399.00)

    def test0764(self):
        self.assertEquals(self.calculate(-191537.0, 21238), -212775.00)

    def test0765(self):
        self.assertEquals(self.calculate(-83492.0, -7363), -76129.00)

    def test0766(self):
        self.assertEquals(self.calculate(59916.0, 22398), 37518.00)

    def test0767(self):
        self.assertEquals(self.calculate(150731.0, 29856), 120875.00)

    def test0768(self):
        self.assertEquals(self.calculate(-131170.0, 24553), -155723.00)

    def test0769(self):
        self.assertEquals(self.calculate(1824.0, 32124), -30300.00)

    def test0770(self):
        self.assertEquals(self.calculate(-25613.0, 14106), -39719.00)

    def test0771(self):
        self.assertEquals(self.calculate(-48057.0, -22293), -25764.00)

    def test0772(self):
        self.assertEquals(self.calculate(-38700.0, -26511), -12189.00)

    def test0773(self):
        self.assertEquals(self.calculate(42144.0, -4436), 46580.00)

    def test0774(self):
        self.assertEquals(self.calculate(-90858.0, -4697), -86161.00)

    def test0775(self):
        self.assertEquals(self.calculate(-4884.0, -13927), 9043.00)

    def test0776(self):
        self.assertEquals(self.calculate(-130789.0, 5520), -136309.00)

    def test0777(self):
        self.assertEquals(self.calculate(191962.0, -26132), 218094.00)

    def test0778(self):
        self.assertEquals(self.calculate(-176454.0, -26351), -150103.00)

    def test0779(self):
        self.assertEquals(self.calculate(-86895.0, 31108), -118003.00)

    def test0780(self):
        self.assertEquals(self.calculate(189647.0, -2959), 192606.00)

    def test0781(self):
        self.assertEquals(self.calculate(-159634.0, 24151), -183785.00)

    def test0782(self):
        self.assertEquals(self.calculate(5581.0, -7010), 12591.00)

    def test0783(self):
        self.assertEquals(self.calculate(-151364.0, -11640), -139724.00)

    def test0784(self):
        self.assertEquals(self.calculate(151754.0, -8823), 160577.00)

    def test0785(self):
        self.assertEquals(self.calculate(-14221.0, -4452), -9769.00)

    def test0786(self):
        self.assertEquals(self.calculate(-106073.0, 10492), -116565.00)

    def test0787(self):
        self.assertEquals(self.calculate(168011.0, -13323), 181334.00)

    def test0788(self):
        self.assertEquals(self.calculate(108386.0, -5187), 113573.00)

    def test0789(self):
        self.assertEquals(self.calculate(155451.0, 6988), 148463.00)

    def test0790(self):
        self.assertEquals(self.calculate(98041.0, -20375), 118416.00)

    def test0791(self):
        self.assertEquals(self.calculate(153117.0, 17412), 135705.00)

    def test0792(self):
        self.assertEquals(self.calculate(69993.0, -10931), 80924.00)

    def test0793(self):
        self.assertEquals(self.calculate(-174175.0, 30585), -204760.00)

    def test0794(self):
        self.assertEquals(self.calculate(-91899.0, 5256), -97155.00)

    def test0795(self):
        self.assertEquals(self.calculate(-89862.0, 3106), -92968.00)

    def test0796(self):
        self.assertEquals(self.calculate(-145180.0, -24308), -120872.00)

    def test0797(self):
        self.assertEquals(self.calculate(-127048.0, -27456), -99592.00)

    def test0798(self):
        self.assertEquals(self.calculate(-159808.0, 32332), -192140.00)

    def test0799(self):
        self.assertEquals(self.calculate(76816.0, 3170), 73646.00)

    def test0800(self):
        self.assertEquals(self.calculate(-157689.0, 30728), -188417.00)

    def test0801(self):
        self.assertEquals(self.calculate(153222.0, -15214), 168436.00)

    def test0802(self):
        self.assertEquals(self.calculate(-39152.0, -18148), -21004.00)

    def test0803(self):
        self.assertEquals(self.calculate(137216.0, 14913), 122303.00)

    def test0804(self):
        self.assertEquals(self.calculate(94396.0, -30311), 124707.00)

    def test0805(self):
        self.assertEquals(self.calculate(173104.0, -17348), 190452.00)

    def test0806(self):
        self.assertEquals(self.calculate(13827.0, 23022), -9195.00)

    def test0807(self):
        self.assertEquals(self.calculate(145244.0, -28956), 174200.00)

    def test0808(self):
        self.assertEquals(self.calculate(75732.0, 24371), 51361.00)

    def test0809(self):
        self.assertEquals(self.calculate(-8034.0, -22579), 14545.00)

    def test0810(self):
        self.assertEquals(self.calculate(-58112.0, 18949), -77061.00)

    def test0811(self):
        self.assertEquals(self.calculate(-58977.0, -2673), -56304.00)

    def test0812(self):
        self.assertEquals(self.calculate(-187874.0, -9650), -178224.00)

    def test0813(self):
        self.assertEquals(self.calculate(-38298.0, -18656), -19642.00)

    def test0814(self):
        self.assertEquals(self.calculate(2540.0, -31613), 34153.00)

    def test0815(self):
        self.assertEquals(self.calculate(29626.0, -8204), 37830.00)

    def test0816(self):
        self.assertEquals(self.calculate(-103401.0, -3485), -99916.00)

    def test0817(self):
        self.assertEquals(self.calculate(-124884.0, 24198), -149082.00)

    def test0818(self):
        self.assertEquals(self.calculate(-105221.0, 10648), -115869.00)

    def test0819(self):
        self.assertEquals(self.calculate(-198630.0, -7256), -191374.00)

    def test0820(self):
        self.assertEquals(self.calculate(121486.0, 18029), 103457.00)

    def test0821(self):
        self.assertEquals(self.calculate(-31012.0, -29178), -1834.00)

    def test0822(self):
        self.assertEquals(self.calculate(-74177.0, 28980), -103157.00)

    def test0823(self):
        self.assertEquals(self.calculate(88567.0, -13507), 102074.00)

    def test0824(self):
        self.assertEquals(self.calculate(94639.0, -8203), 102842.00)

    def test0825(self):
        self.assertEquals(self.calculate(1813.0, 7180), -5367.00)

    def test0826(self):
        self.assertEquals(self.calculate(-165689.0, -12119), -153570.00)

    def test0827(self):
        self.assertEquals(self.calculate(193222.0, 15479), 177743.00)

    def test0828(self):
        self.assertEquals(self.calculate(-16660.0, 13631), -30291.00)

    def test0829(self):
        self.assertEquals(self.calculate(33322.0, 19291), 14031.00)

    def test0830(self):
        self.assertEquals(self.calculate(-15231.0, -3949), -11282.00)

    def test0831(self):
        self.assertEquals(self.calculate(-100466.0, 32649), -133115.00)

    def test0832(self):
        self.assertEquals(self.calculate(123440.0, -63), 123503.00)

    def test0833(self):
        self.assertEquals(self.calculate(-116440.0, -20500), -95940.00)

    def test0834(self):
        self.assertEquals(self.calculate(-11204.0, 30239), -41443.00)

    def test0835(self):
        self.assertEquals(self.calculate(-168765.0, 26608), -195373.00)

    def test0836(self):
        self.assertEquals(self.calculate(-157120.0, 4460), -161580.00)

    def test0837(self):
        self.assertEquals(self.calculate(-57697.0, -7682), -50015.00)

    def test0838(self):
        self.assertEquals(self.calculate(159391.0, -19073), 178464.00)

    def test0839(self):
        self.assertEquals(self.calculate(117997.0, -25275), 143272.00)

    def test0840(self):
        self.assertEquals(self.calculate(20817.0, 29665), -8848.00)

    def test0841(self):
        self.assertEquals(self.calculate(6854.0, 25728), -18874.00)

    def test0842(self):
        self.assertEquals(self.calculate(-191964.0, 32011), -223975.00)

    def test0843(self):
        self.assertEquals(self.calculate(-85884.0, -1409), -84475.00)

    def test0844(self):
        self.assertEquals(self.calculate(90569.0, 24056), 66513.00)

    def test0845(self):
        self.assertEquals(self.calculate(-100139.0, -11910), -88229.00)

    def test0846(self):
        self.assertEquals(self.calculate(-8442.0, -27988), 19546.00)

    def test0847(self):
        self.assertEquals(self.calculate(41933.0, -14399), 56332.00)

    def test0848(self):
        self.assertEquals(self.calculate(-179321.0, -13935), -165386.00)

    def test0849(self):
        self.assertEquals(self.calculate(188557.0, 24445), 164112.00)

    def test0850(self):
        self.assertEquals(self.calculate(-45783.0, 11953), -57736.00)

    def test0851(self):
        self.assertEquals(self.calculate(127370.0, -31890), 159260.00)

    def test0852(self):
        self.assertEquals(self.calculate(-123413.0, -29753), -93660.00)

    def test0853(self):
        self.assertEquals(self.calculate(-148781.0, -3084), -145697.00)

    def test0854(self):
        self.assertEquals(self.calculate(143083.0, -29117), 172200.00)

    def test0855(self):
        self.assertEquals(self.calculate(-126702.0, -7996), -118706.00)

    def test0856(self):
        self.assertEquals(self.calculate(50617.0, 27449), 23168.00)

    def test0857(self):
        self.assertEquals(self.calculate(-100860.0, -13478), -87382.00)

    def test0858(self):
        self.assertEquals(self.calculate(127308.0, -26818), 154126.00)

    def test0859(self):
        self.assertEquals(self.calculate(-185449.0, 4269), -189718.00)

    def test0860(self):
        self.assertEquals(self.calculate(-108159.0, 11609), -119768.00)

    def test0861(self):
        self.assertEquals(self.calculate(53047.0, -16837), 69884.00)

    def test0862(self):
        self.assertEquals(self.calculate(-60321.0, 21439), -81760.00)

    def test0863(self):
        self.assertEquals(self.calculate(-419.0, -25074), 24655.00)

    def test0864(self):
        self.assertEquals(self.calculate(-12785.0, -11518), -1267.00)

    def test0865(self):
        self.assertEquals(self.calculate(-114589.0, 1534), -116123.00)

    def test0866(self):
        self.assertEquals(self.calculate(118562.0, -2299), 120861.00)

    def test0867(self):
        self.assertEquals(self.calculate(-6929.0, 24240), -31169.00)

    def test0868(self):
        self.assertEquals(self.calculate(-50352.0, -22784), -27568.00)

    def test0869(self):
        self.assertEquals(self.calculate(98401.0, 11485), 86916.00)

    def test0870(self):
        self.assertEquals(self.calculate(19169.0, -10216), 29385.00)

    def test0871(self):
        self.assertEquals(self.calculate(-115858.0, -31552), -84306.00)

    def test0872(self):
        self.assertEquals(self.calculate(-69379.0, -23514), -45865.00)

    def test0873(self):
        self.assertEquals(self.calculate(-107567.0, -1052), -106515.00)

    def test0874(self):
        self.assertEquals(self.calculate(28290.0, 26152), 2138.00)

    def test0875(self):
        self.assertEquals(self.calculate(-22376.0, 24998), -47374.00)

    def test0876(self):
        self.assertEquals(self.calculate(155474.0, 23258), 132216.00)

    def test0877(self):
        self.assertEquals(self.calculate(-94351.0, -17129), -77222.00)

    def test0878(self):
        self.assertEquals(self.calculate(74311.0, 8536), 65775.00)

    def test0879(self):
        self.assertEquals(self.calculate(-119070.0, 12803), -131873.00)

    def test0880(self):
        self.assertEquals(self.calculate(117654.0, -28967), 146621.00)

    def test0881(self):
        self.assertEquals(self.calculate(-154464.0, -13120), -141344.00)

    def test0882(self):
        self.assertEquals(self.calculate(-94624.0, 8861), -103485.00)

    def test0883(self):
        self.assertEquals(self.calculate(115775.0, 17923), 97852.00)

    def test0884(self):
        self.assertEquals(self.calculate(27983.0, 18239), 9744.00)

    def test0885(self):
        self.assertEquals(self.calculate(-195660.0, -31744), -163916.00)

    def test0886(self):
        self.assertEquals(self.calculate(33479.0, -4561), 38040.00)

    def test0887(self):
        self.assertEquals(self.calculate(-52014.0, 443), -52457.00)

    def test0888(self):
        self.assertEquals(self.calculate(195858.0, 4547), 191311.00)

    def test0889(self):
        self.assertEquals(self.calculate(156862.0, 9497), 147365.00)

    def test0890(self):
        self.assertEquals(self.calculate(27057.0, 17736), 9321.00)

    def test0891(self):
        self.assertEquals(self.calculate(-140753.0, -27116), -113637.00)

    def test0892(self):
        self.assertEquals(self.calculate(190068.0, -19707), 209775.00)

    def test0893(self):
        self.assertEquals(self.calculate(-191111.0, 25739), -216850.00)

    def test0894(self):
        self.assertEquals(self.calculate(179482.0, 17732), 161750.00)

    def test0895(self):
        self.assertEquals(self.calculate(49066.0, 21646), 27420.00)

    def test0896(self):
        self.assertEquals(self.calculate(-141712.0, -332), -141380.00)

    def test0897(self):
        self.assertEquals(self.calculate(-23518.0, -32163), 8645.00)

    def test0898(self):
        self.assertEquals(self.calculate(117489.0, 30042), 87447.00)

    def test0899(self):
        self.assertEquals(self.calculate(116206.0, -25175), 141381.00)

    def test0900(self):
        self.assertEquals(self.calculate(-4169.0, -13936), 9767.00)

    def test0901(self):
        self.assertEquals(self.calculate(-179754.0, 6222), -185976.00)

    def test0902(self):
        self.assertEquals(self.calculate(-181003.0, 11419), -192422.00)

    def test0903(self):
        self.assertEquals(self.calculate(-11425.0, -11855), 430.00)

    def test0904(self):
        self.assertEquals(self.calculate(-10293.0, -700), -9593.00)

    def test0905(self):
        self.assertEquals(self.calculate(-140672.0, -4468), -136204.00)

    def test0906(self):
        self.assertEquals(self.calculate(29940.0, 16378), 13562.00)

    def test0907(self):
        self.assertEquals(self.calculate(-85312.0, -3657), -81655.00)

    def test0908(self):
        self.assertEquals(self.calculate(-97198.0, -9654), -87544.00)

    def test0909(self):
        self.assertEquals(self.calculate(10949.0, 980), 9969.00)

    def test0910(self):
        self.assertEquals(self.calculate(13670.0, -19676), 33346.00)

    def test0911(self):
        self.assertEquals(self.calculate(2600.0, 22888), -20288.00)

    def test0912(self):
        self.assertEquals(self.calculate(-189391.0, 20811), -210202.00)

    def test0913(self):
        self.assertEquals(self.calculate(185973.0, -23435), 209408.00)

    def test0914(self):
        self.assertEquals(self.calculate(31929.0, -21429), 53358.00)

    def test0915(self):
        self.assertEquals(self.calculate(-67655.0, 15233), -82888.00)

    def test0916(self):
        self.assertEquals(self.calculate(177037.0, -3675), 180712.00)

    def test0917(self):
        self.assertEquals(self.calculate(50988.0, 24855), 26133.00)

    def test0918(self):
        self.assertEquals(self.calculate(-156356.0, 18154), -174510.00)

    def test0919(self):
        self.assertEquals(self.calculate(-105927.0, 2288), -108215.00)

    def test0920(self):
        self.assertEquals(self.calculate(47907.0, 32247), 15660.00)

    def test0921(self):
        self.assertEquals(self.calculate(60105.0, -28311), 88416.00)

    def test0922(self):
        self.assertEquals(self.calculate(-157095.0, 4307), -161402.00)

    def test0923(self):
        self.assertEquals(self.calculate(-38753.0, 21656), -60409.00)

    def test0924(self):
        self.assertEquals(self.calculate(23530.0, 25245), -1715.00)

    def test0925(self):
        self.assertEquals(self.calculate(199912.0, 11923), 187989.00)

    def test0926(self):
        self.assertEquals(self.calculate(-9215.0, 13055), -22270.00)

    def test0927(self):
        self.assertEquals(self.calculate(-152685.0, -11476), -141209.00)

    def test0928(self):
        self.assertEquals(self.calculate(83559.0, -3974), 87533.00)

    def test0929(self):
        self.assertEquals(self.calculate(194239.0, -1417), 195656.00)

    def test0930(self):
        self.assertEquals(self.calculate(-22945.0, -3087), -19858.00)

    def test0931(self):
        self.assertEquals(self.calculate(-122072.0, -15245), -106827.00)

    def test0932(self):
        self.assertEquals(self.calculate(139920.0, 19312), 120608.00)

    def test0933(self):
        self.assertEquals(self.calculate(58140.0, 6495), 51645.00)

    def test0934(self):
        self.assertEquals(self.calculate(147718.0, -12714), 160432.00)

    def test0935(self):
        self.assertEquals(self.calculate(-123795.0, 22327), -146122.00)

    def test0936(self):
        self.assertEquals(self.calculate(-69490.0, -764), -68726.00)

    def test0937(self):
        self.assertEquals(self.calculate(-166254.0, 21503), -187757.00)

    def test0938(self):
        self.assertEquals(self.calculate(38598.0, -8282), 46880.00)

    def test0939(self):
        self.assertEquals(self.calculate(165796.0, 29111), 136685.00)

    def test0940(self):
        self.assertEquals(self.calculate(-75214.0, 29692), -104906.00)

    def test0941(self):
        self.assertEquals(self.calculate(-180916.0, -22219), -158697.00)

    def test0942(self):
        self.assertEquals(self.calculate(-8388.0, 19797), -28185.00)

    def test0943(self):
        self.assertEquals(self.calculate(127948.0, 21822), 106126.00)

    def test0944(self):
        self.assertEquals(self.calculate(-154611.0, 55), -154666.00)

    def test0945(self):
        self.assertEquals(self.calculate(-199160.0, 11534), -210694.00)

    def test0946(self):
        self.assertEquals(self.calculate(97386.0, -23556), 120942.00)

    def test0947(self):
        self.assertEquals(self.calculate(-100196.0, 14743), -114939.00)

    def test0948(self):
        self.assertEquals(self.calculate(103097.0, -2591), 105688.00)

    def test0949(self):
        self.assertEquals(self.calculate(22352.0, -4934), 27286.00)

    def test0950(self):
        self.assertEquals(self.calculate(-172660.0, -25738), -146922.00)

    def test0951(self):
        self.assertEquals(self.calculate(168897.0, 14107), 154790.00)

    def test0952(self):
        self.assertEquals(self.calculate(-142522.0, 32378), -174900.00)

    def test0953(self):
        self.assertEquals(self.calculate(-164962.0, -17385), -147577.00)

    def test0954(self):
        self.assertEquals(self.calculate(113341.0, -16558), 129899.00)

    def test0955(self):
        self.assertEquals(self.calculate(-133273.0, -15460), -117813.00)

    def test0956(self):
        self.assertEquals(self.calculate(-175817.0, 3430), -179247.00)

    def test0957(self):
        self.assertEquals(self.calculate(-52223.0, 13236), -65459.00)

    def test0958(self):
        self.assertEquals(self.calculate(-109437.0, -740), -108697.00)

    def test0959(self):
        self.assertEquals(self.calculate(-5867.0, 2442), -8309.00)

    def test0960(self):
        self.assertEquals(self.calculate(82436.0, -26309), 108745.00)

    def test0961(self):
        self.assertEquals(self.calculate(-1065.0, -29473), 28408.00)

    def test0962(self):
        self.assertEquals(self.calculate(-87060.0, -20981), -66079.00)

    def test0963(self):
        self.assertEquals(self.calculate(-97350.0, -25492), -71858.00)

    def test0964(self):
        self.assertEquals(self.calculate(-3853.0, 13688), -17541.00)

    def test0965(self):
        self.assertEquals(self.calculate(-167231.0, -30154), -137077.00)

    def test0966(self):
        self.assertEquals(self.calculate(1830.0, 8059), -6229.00)

    def test0967(self):
        self.assertEquals(self.calculate(-80383.0, 3254), -83637.00)

    def test0968(self):
        self.assertEquals(self.calculate(-40273.0, -11943), -28330.00)

    def test0969(self):
        self.assertEquals(self.calculate(139505.0, -31838), 171343.00)

    def test0970(self):
        self.assertEquals(self.calculate(24500.0, -4995), 29495.00)

    def test0971(self):
        self.assertEquals(self.calculate(-106849.0, -8107), -98742.00)

    def test0972(self):
        self.assertEquals(self.calculate(-76457.0, -29697), -46760.00)

    def test0973(self):
        self.assertEquals(self.calculate(-110063.0, -6718), -103345.00)

    def test0974(self):
        self.assertEquals(self.calculate(-31542.0, -23003), -8539.00)

    def test0975(self):
        self.assertEquals(self.calculate(-32437.0, 8478), -40915.00)

    def test0976(self):
        self.assertEquals(self.calculate(-64388.0, -30760), -33628.00)

    def test0977(self):
        self.assertEquals(self.calculate(19267.0, -10618), 29885.00)

    def test0978(self):
        self.assertEquals(self.calculate(-92609.0, -32066), -60543.00)

    def test0979(self):
        self.assertEquals(self.calculate(165469.0, -8471), 173940.00)

    def test0980(self):
        self.assertEquals(self.calculate(-61852.0, -30966), -30886.00)

    def test0981(self):
        self.assertEquals(self.calculate(-57424.0, -12711), -44713.00)

    def test0982(self):
        self.assertEquals(self.calculate(106688.0, 21282), 85406.00)

    def test0983(self):
        self.assertEquals(self.calculate(136347.0, 6926), 129421.00)

    def test0984(self):
        self.assertEquals(self.calculate(-17289.0, -9674), -7615.00)

    def test0985(self):
        self.assertEquals(self.calculate(36312.0, 24462), 11850.00)

    def test0986(self):
        self.assertEquals(self.calculate(20192.0, 20628), -436.00)

    def test0987(self):
        self.assertEquals(self.calculate(-100245.0, -26054), -74191.00)

    def test0988(self):
        self.assertEquals(self.calculate(-1216.0, -11483), 10267.00)

    def test0989(self):
        self.assertEquals(self.calculate(70363.0, -9679), 80042.00)

    def test0990(self):
        self.assertEquals(self.calculate(-10026.0, 27042), -37068.00)

    def test0991(self):
        self.assertEquals(self.calculate(106675.0, 26847), 79828.00)

    def test0992(self):
        self.assertEquals(self.calculate(76979.0, 31064), 45915.00)

    def test0993(self):
        self.assertEquals(self.calculate(-4266.0, 17455), -21721.00)

    def test0994(self):
        self.assertEquals(self.calculate(-158360.0, 30355), -188715.00)

    def test0995(self):
        self.assertEquals(self.calculate(-173417.0, -24990), -148427.00)

    def test0996(self):
        self.assertEquals(self.calculate(-25692.0, -30487), 4795.00)

    def test0997(self):
        self.assertEquals(self.calculate(-133902.0, -16009), -117893.00)

    def test0998(self):
        self.assertEquals(self.calculate(118054.0, 8750), 109304.00)

    def test0999(self):
        self.assertEquals(self.calculate(-83175.0, -7204), -75971.00)

    def test1000(self):
        self.assertEquals(self.calculate(-90276.0, -17102), -73174.00)

    def test1001(self):
        self.assertEquals(self.calculate(-744.0, -12083), 11339.00)

    def test1002(self):
        self.assertEquals(self.calculate(-32453.0, 4465), -36918.00)

    def test1003(self):
        self.assertEquals(self.calculate(-117768.0, -10375), -107393.00)

    def test1004(self):
        self.assertEquals(self.calculate(78156.0, -9159), 87315.00)

    def test1005(self):
        self.assertEquals(self.calculate(88100.0, 31763), 56337.00)

    def test1006(self):
        self.assertEquals(self.calculate(33592.0, 30139), 3453.00)

    def test1007(self):
        self.assertEquals(self.calculate(-15219.0, -17843), 2624.00)

    def test1008(self):
        self.assertEquals(self.calculate(195439.0, 7220), 188219.00)

    def test1009(self):
        self.assertEquals(self.calculate(-199944.0, -30459), -169485.00)

    def test1010(self):
        self.assertEquals(self.calculate(7315.0, 1982), 5333.00)

    def test1011(self):
        self.assertEquals(self.calculate(36495.0, -24389), 60884.00)

    def test1012(self):
        self.assertEquals(self.calculate(109278.0, -14263), 123541.00)

    def test1013(self):
        self.assertEquals(self.calculate(188753.0, -14937), 203690.00)

    def test1014(self):
        self.assertEquals(self.calculate(-76680.0, -11749), -64931.00)

    def test1015(self):
        self.assertEquals(self.calculate(-171857.0, -14485), -157372.00)

    def test1016(self):
        self.assertEquals(self.calculate(-85793.0, -13742), -72051.00)

    def test1017(self):
        self.assertEquals(self.calculate(-191936.0, 14935), -206871.00)

    def test1018(self):
        self.assertEquals(self.calculate(86719.0, 13037), 73682.00)

    def test1019(self):
        self.assertEquals(self.calculate(-4990.0, 8588), -13578.00)

    def test1020(self):
        self.assertEquals(self.calculate(-196110.0, -28933), -167177.00)

    def test1021(self):
        self.assertEquals(self.calculate(74766.0, 8613), 66153.00)

    def test1022(self):
        self.assertEquals(self.calculate(63432.0, -22080), 85512.00)

    def test1023(self):
        self.assertEquals(self.calculate(51189.0, 22739), 28450.00)



class TestVM_Sub_FloatLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushL(rhs)
        v.VM_Sub()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-13365.0, -1924935048), 1924921683.00)

    def test0001(self):
        self.assertEquals(self.calculate(-135128.0, 1750074335), -1750209463.00)

    def test0002(self):
        self.assertEquals(self.calculate(-19836.0, -1420809775), 1420789939.00)

    def test0003(self):
        self.assertEquals(self.calculate(32034.0, -1029205941), 1029237975.00)

    def test0004(self):
        self.assertEquals(self.calculate(-191904.0, 828107887), -828299791.00)

    def test0005(self):
        self.assertEquals(self.calculate(-183231.0, 987905178), -988088409.00)

    def test0006(self):
        self.assertEquals(self.calculate(-71123.0, -1266302316), 1266231193.00)

    def test0007(self):
        self.assertEquals(self.calculate(-181931.0, 391878869), -392060800.00)

    def test0008(self):
        self.assertEquals(self.calculate(67930.0, -1409504081), 1409572011.00)

    def test0009(self):
        self.assertEquals(self.calculate(-48672.0, 1739472465), -1739521137.00)

    def test0010(self):
        self.assertEquals(self.calculate(183274.0, 2103308123), -2103124849.00)

    def test0011(self):
        self.assertEquals(self.calculate(-36117.0, -1057454772), 1057418655.00)

    def test0012(self):
        self.assertEquals(self.calculate(-152608.0, -1088461438), 1088308830.00)

    def test0013(self):
        self.assertEquals(self.calculate(104574.0, -1073168710), 1073273284.00)

    def test0014(self):
        self.assertEquals(self.calculate(177356.0, -1685247712), 1685425068.00)

    def test0015(self):
        self.assertEquals(self.calculate(190119.0, 2011244499), -2011054380.00)

    def test0016(self):
        self.assertEquals(self.calculate(-133258.0, -2147438001), 2147304743.00)

    def test0017(self):
        self.assertEquals(self.calculate(-54811.0, -1739351924), 1739297113.00)

    def test0018(self):
        self.assertEquals(self.calculate(-62895.0, 481732465), -481795360.00)

    def test0019(self):
        self.assertEquals(self.calculate(-30571.0, -1504242594), 1504212023.00)

    def test0020(self):
        self.assertEquals(self.calculate(53818.0, 1073853363), -1073799545.00)

    def test0021(self):
        self.assertEquals(self.calculate(182519.0, -461023230), 461205749.00)

    def test0022(self):
        self.assertEquals(self.calculate(124303.0, -372626161), 372750464.00)

    def test0023(self):
        self.assertEquals(self.calculate(-188953.0, 50345271), -50534224.00)

    def test0024(self):
        self.assertEquals(self.calculate(89969.0, 741653601), -741563632.00)

    def test0025(self):
        self.assertEquals(self.calculate(147803.0, -2043038164), 2043185967.00)

    def test0026(self):
        self.assertEquals(self.calculate(6808.0, -412561691), 412568499.00)

    def test0027(self):
        self.assertEquals(self.calculate(142973.0, -169041157), 169184130.00)

    def test0028(self):
        self.assertEquals(self.calculate(147216.0, -1125468907), 1125616123.00)

    def test0029(self):
        self.assertEquals(self.calculate(-166989.0, 1630302852), -1630469841.00)

    def test0030(self):
        self.assertEquals(self.calculate(135796.0, 2019346312), -2019210516.00)

    def test0031(self):
        self.assertEquals(self.calculate(-68691.0, 1435366712), -1435435403.00)

    def test0032(self):
        self.assertEquals(self.calculate(-84783.0, 72226257), -72311040.00)

    def test0033(self):
        self.assertEquals(self.calculate(-70122.0, 1350641269), -1350711391.00)

    def test0034(self):
        self.assertEquals(self.calculate(171002.0, 1868387384), -1868216382.00)

    def test0035(self):
        self.assertEquals(self.calculate(-2439.0, 413353208), -413355647.00)

    def test0036(self):
        self.assertEquals(self.calculate(-32604.0, 384158717), -384191321.00)

    def test0037(self):
        self.assertEquals(self.calculate(615.0, -424964295), 424964910.00)

    def test0038(self):
        self.assertEquals(self.calculate(116997.0, -333302227), 333419224.00)

    def test0039(self):
        self.assertEquals(self.calculate(-45739.0, 438894932), -438940671.00)

    def test0040(self):
        self.assertEquals(self.calculate(-31342.0, -1063715662), 1063684320.00)

    def test0041(self):
        self.assertEquals(self.calculate(-157289.0, -657192253), 657034964.00)

    def test0042(self):
        self.assertEquals(self.calculate(8804.0, 935562507), -935553703.00)

    def test0043(self):
        self.assertEquals(self.calculate(92840.0, 924552241), -924459401.00)

    def test0044(self):
        self.assertEquals(self.calculate(12434.0, -583495273), 583507707.00)

    def test0045(self):
        self.assertEquals(self.calculate(-160761.0, -527145172), 526984411.00)

    def test0046(self):
        self.assertEquals(self.calculate(153462.0, 57973401), -57819939.00)

    def test0047(self):
        self.assertEquals(self.calculate(131058.0, 581386734), -581255676.00)

    def test0048(self):
        self.assertEquals(self.calculate(136485.0, 606338835), -606202350.00)

    def test0049(self):
        self.assertEquals(self.calculate(-23576.0, 91987335), -92010911.00)

    def test0050(self):
        self.assertEquals(self.calculate(148612.0, 280333287), -280184675.00)

    def test0051(self):
        self.assertEquals(self.calculate(85131.0, -1119707764), 1119792895.00)

    def test0052(self):
        self.assertEquals(self.calculate(94532.0, -1943465597), 1943560129.00)

    def test0053(self):
        self.assertEquals(self.calculate(-116936.0, 1569917784), -1570034720.00)

    def test0054(self):
        self.assertEquals(self.calculate(-126085.0, 2009744737), -2009870822.00)

    def test0055(self):
        self.assertEquals(self.calculate(149117.0, 1803743465), -1803594348.00)

    def test0056(self):
        self.assertEquals(self.calculate(-77389.0, 209818678), -209896067.00)

    def test0057(self):
        self.assertEquals(self.calculate(-18577.0, 1955383837), -1955402414.00)

    def test0058(self):
        self.assertEquals(self.calculate(-14434.0, 1988266683), -1988281117.00)

    def test0059(self):
        self.assertEquals(self.calculate(-186467.0, -384463846), 384277379.00)

    def test0060(self):
        self.assertEquals(self.calculate(-42905.0, -364931852), 364888947.00)

    def test0061(self):
        self.assertEquals(self.calculate(7258.0, 1949160022), -1949152764.00)

    def test0062(self):
        self.assertEquals(self.calculate(47509.0, -889897564), 889945073.00)

    def test0063(self):
        self.assertEquals(self.calculate(-121055.0, 1462961669), -1463082724.00)

    def test0064(self):
        self.assertEquals(self.calculate(58215.0, -2016479), 2074694.00)

    def test0065(self):
        self.assertEquals(self.calculate(87244.0, -1068634539), 1068721783.00)

    def test0066(self):
        self.assertEquals(self.calculate(74023.0, 1536690238), -1536616215.00)

    def test0067(self):
        self.assertEquals(self.calculate(21317.0, 1352911063), -1352889746.00)

    def test0068(self):
        self.assertEquals(self.calculate(108851.0, -876241831), 876350682.00)

    def test0069(self):
        self.assertEquals(self.calculate(-158966.0, 1235530524), -1235689490.00)

    def test0070(self):
        self.assertEquals(self.calculate(149482.0, -1863520826), 1863670308.00)

    def test0071(self):
        self.assertEquals(self.calculate(-90804.0, -868103500), 868012696.00)

    def test0072(self):
        self.assertEquals(self.calculate(-237.0, 2041263995), -2041264232.00)

    def test0073(self):
        self.assertEquals(self.calculate(-115221.0, 943783282), -943898503.00)

    def test0074(self):
        self.assertEquals(self.calculate(-162516.0, 638346561), -638509077.00)

    def test0075(self):
        self.assertEquals(self.calculate(16410.0, -1685443580), 1685459990.00)

    def test0076(self):
        self.assertEquals(self.calculate(158253.0, -1277380008), 1277538261.00)

    def test0077(self):
        self.assertEquals(self.calculate(23344.0, -1824948169), 1824971513.00)

    def test0078(self):
        self.assertEquals(self.calculate(-28889.0, -1883274427), 1883245538.00)

    def test0079(self):
        self.assertEquals(self.calculate(-80099.0, 1546500763), -1546580862.00)

    def test0080(self):
        self.assertEquals(self.calculate(83589.0, 581954429), -581870840.00)

    def test0081(self):
        self.assertEquals(self.calculate(189382.0, -1204153550), 1204342932.00)

    def test0082(self):
        self.assertEquals(self.calculate(-188599.0, -612117159), 611928560.00)

    def test0083(self):
        self.assertEquals(self.calculate(-119194.0, -1930017898), 1929898704.00)

    def test0084(self):
        self.assertEquals(self.calculate(7113.0, -764410445), 764417558.00)

    def test0085(self):
        self.assertEquals(self.calculate(-127271.0, 359665540), -359792811.00)

    def test0086(self):
        self.assertEquals(self.calculate(-154176.0, 1180836896), -1180991072.00)

    def test0087(self):
        self.assertEquals(self.calculate(-60538.0, 214946028), -215006566.00)

    def test0088(self):
        self.assertEquals(self.calculate(80026.0, -639878464), 639958490.00)

    def test0089(self):
        self.assertEquals(self.calculate(-136626.0, -356853664), 356717038.00)

    def test0090(self):
        self.assertEquals(self.calculate(49108.0, -742954890), 743003998.00)

    def test0091(self):
        self.assertEquals(self.calculate(106028.0, 91258091), -91152063.00)

    def test0092(self):
        self.assertEquals(self.calculate(-31371.0, 968977630), -969009001.00)

    def test0093(self):
        self.assertEquals(self.calculate(186786.0, 2029858651), -2029671865.00)

    def test0094(self):
        self.assertEquals(self.calculate(33987.0, 1235863923), -1235829936.00)

    def test0095(self):
        self.assertEquals(self.calculate(168866.0, 342506647), -342337781.00)

    def test0096(self):
        self.assertEquals(self.calculate(136064.0, 1751981217), -1751845153.00)

    def test0097(self):
        self.assertEquals(self.calculate(106109.0, -622956314), 623062423.00)

    def test0098(self):
        self.assertEquals(self.calculate(196234.0, 735439904), -735243670.00)

    def test0099(self):
        self.assertEquals(self.calculate(91745.0, 154415944), -154324199.00)

    def test0100(self):
        self.assertEquals(self.calculate(-69026.0, 874589439), -874658465.00)

    def test0101(self):
        self.assertEquals(self.calculate(175825.0, -5926413), 6102238.00)

    def test0102(self):
        self.assertEquals(self.calculate(162066.0, 540815391), -540653325.00)

    def test0103(self):
        self.assertEquals(self.calculate(160742.0, -52430505), 52591247.00)

    def test0104(self):
        self.assertEquals(self.calculate(-128910.0, -1622678515), 1622549605.00)

    def test0105(self):
        self.assertEquals(self.calculate(-11757.0, -601666820), 601655063.00)

    def test0106(self):
        self.assertEquals(self.calculate(124224.0, -1646270579), 1646394803.00)

    def test0107(self):
        self.assertEquals(self.calculate(158368.0, 2046306958), -2046148590.00)

    def test0108(self):
        self.assertEquals(self.calculate(160042.0, 244541034), -244380992.00)

    def test0109(self):
        self.assertEquals(self.calculate(141551.0, 1244500523), -1244358972.00)

    def test0110(self):
        self.assertEquals(self.calculate(175512.0, 474138376), -473962864.00)

    def test0111(self):
        self.assertEquals(self.calculate(137873.0, 460058169), -459920296.00)

    def test0112(self):
        self.assertEquals(self.calculate(-24455.0, 1464124100), -1464148555.00)

    def test0113(self):
        self.assertEquals(self.calculate(49547.0, 1645658692), -1645609145.00)

    def test0114(self):
        self.assertEquals(self.calculate(77674.0, 1788505612), -1788427938.00)

    def test0115(self):
        self.assertEquals(self.calculate(143382.0, 982364005), -982220623.00)

    def test0116(self):
        self.assertEquals(self.calculate(157325.0, -923448385), 923605710.00)

    def test0117(self):
        self.assertEquals(self.calculate(-35831.0, -620070053), 620034222.00)

    def test0118(self):
        self.assertEquals(self.calculate(57304.0, 624286852), -624229548.00)

    def test0119(self):
        self.assertEquals(self.calculate(-95870.0, -1525207639), 1525111769.00)

    def test0120(self):
        self.assertEquals(self.calculate(-121698.0, 719752256), -719873954.00)

    def test0121(self):
        self.assertEquals(self.calculate(-127436.0, 2129117106), -2129244542.00)

    def test0122(self):
        self.assertEquals(self.calculate(-10645.0, 376718661), -376729306.00)

    def test0123(self):
        self.assertEquals(self.calculate(-183957.0, 911008250), -911192207.00)

    def test0124(self):
        self.assertEquals(self.calculate(194515.0, 1882306838), -1882112323.00)

    def test0125(self):
        self.assertEquals(self.calculate(190964.0, 131116652), -130925688.00)

    def test0126(self):
        self.assertEquals(self.calculate(-43418.0, -1908798472), 1908755054.00)

    def test0127(self):
        self.assertEquals(self.calculate(-81919.0, -460596968), 460515049.00)

    def test0128(self):
        self.assertEquals(self.calculate(14024.0, -245788396), 245802420.00)

    def test0129(self):
        self.assertEquals(self.calculate(-10256.0, 941232313), -941242569.00)

    def test0130(self):
        self.assertEquals(self.calculate(-48275.0, -1440702632), 1440654357.00)

    def test0131(self):
        self.assertEquals(self.calculate(96097.0, -175941220), 176037317.00)

    def test0132(self):
        self.assertEquals(self.calculate(-5315.0, 1282682485), -1282687800.00)

    def test0133(self):
        self.assertEquals(self.calculate(168398.0, 479703819), -479535421.00)

    def test0134(self):
        self.assertEquals(self.calculate(104883.0, -820339829), 820444712.00)

    def test0135(self):
        self.assertEquals(self.calculate(-197628.0, -1473523239), 1473325611.00)

    def test0136(self):
        self.assertEquals(self.calculate(-54437.0, -122489598), 122435161.00)

    def test0137(self):
        self.assertEquals(self.calculate(-30698.0, -1346294938), 1346264240.00)

    def test0138(self):
        self.assertEquals(self.calculate(-31963.0, 1400935624), -1400967587.00)

    def test0139(self):
        self.assertEquals(self.calculate(-72925.0, 2077635798), -2077708723.00)

    def test0140(self):
        self.assertEquals(self.calculate(134212.0, -375770233), 375904445.00)

    def test0141(self):
        self.assertEquals(self.calculate(194364.0, -1679825563), 1680019927.00)

    def test0142(self):
        self.assertEquals(self.calculate(30769.0, 1962123104), -1962092335.00)

    def test0143(self):
        self.assertEquals(self.calculate(-198452.0, 1941726758), -1941925210.00)

    def test0144(self):
        self.assertEquals(self.calculate(-80423.0, 862996062), -863076485.00)

    def test0145(self):
        self.assertEquals(self.calculate(-88022.0, 2050724863), -2050812885.00)

    def test0146(self):
        self.assertEquals(self.calculate(96786.0, -1723232298), 1723329084.00)

    def test0147(self):
        self.assertEquals(self.calculate(-145495.0, -711841201), 711695706.00)

    def test0148(self):
        self.assertEquals(self.calculate(-148288.0, -474749633), 474601345.00)

    def test0149(self):
        self.assertEquals(self.calculate(-129171.0, 1527273920), -1527403091.00)

    def test0150(self):
        self.assertEquals(self.calculate(-170873.0, 1519018877), -1519189750.00)

    def test0151(self):
        self.assertEquals(self.calculate(192772.0, 1815204311), -1815011539.00)

    def test0152(self):
        self.assertEquals(self.calculate(-96741.0, -1029426661), 1029329920.00)

    def test0153(self):
        self.assertEquals(self.calculate(77532.0, -84272636), 84350168.00)

    def test0154(self):
        self.assertEquals(self.calculate(103731.0, -1351652988), 1351756719.00)

    def test0155(self):
        self.assertEquals(self.calculate(-192123.0, 1481695571), -1481887694.00)

    def test0156(self):
        self.assertEquals(self.calculate(188750.0, -97209251), 97398001.00)

    def test0157(self):
        self.assertEquals(self.calculate(-21234.0, 484793899), -484815133.00)

    def test0158(self):
        self.assertEquals(self.calculate(53979.0, -732340608), 732394587.00)

    def test0159(self):
        self.assertEquals(self.calculate(38114.0, -2106469615), 2106507729.00)

    def test0160(self):
        self.assertEquals(self.calculate(46028.0, -1598821951), 1598867979.00)

    def test0161(self):
        self.assertEquals(self.calculate(50132.0, -463742957), 463793089.00)

    def test0162(self):
        self.assertEquals(self.calculate(119216.0, -3989114), 4108330.00)

    def test0163(self):
        self.assertEquals(self.calculate(132624.0, -351962364), 352094988.00)

    def test0164(self):
        self.assertEquals(self.calculate(57152.0, -1575847989), 1575905141.00)

    def test0165(self):
        self.assertEquals(self.calculate(-169887.0, -1282831597), 1282661710.00)

    def test0166(self):
        self.assertEquals(self.calculate(-156494.0, -615977635), 615821141.00)

    def test0167(self):
        self.assertEquals(self.calculate(149498.0, 108597305), -108447807.00)

    def test0168(self):
        self.assertEquals(self.calculate(1255.0, 2058076896), -2058075641.00)

    def test0169(self):
        self.assertEquals(self.calculate(-130639.0, -217445201), 217314562.00)

    def test0170(self):
        self.assertEquals(self.calculate(-50267.0, -1729514710), 1729464443.00)

    def test0171(self):
        self.assertEquals(self.calculate(54514.0, 1656872963), -1656818449.00)

    def test0172(self):
        self.assertEquals(self.calculate(-87164.0, 1055393309), -1055480473.00)

    def test0173(self):
        self.assertEquals(self.calculate(58436.0, -1567917328), 1567975764.00)

    def test0174(self):
        self.assertEquals(self.calculate(180584.0, -1590725075), 1590905659.00)

    def test0175(self):
        self.assertEquals(self.calculate(-74346.0, 392787964), -392862310.00)

    def test0176(self):
        self.assertEquals(self.calculate(156873.0, 1755879018), -1755722145.00)

    def test0177(self):
        self.assertEquals(self.calculate(-176612.0, 471613094), -471789706.00)

    def test0178(self):
        self.assertEquals(self.calculate(-168434.0, 51128508), -51296942.00)

    def test0179(self):
        self.assertEquals(self.calculate(-30718.0, 1684843491), -1684874209.00)

    def test0180(self):
        self.assertEquals(self.calculate(125954.0, 2095673915), -2095547961.00)

    def test0181(self):
        self.assertEquals(self.calculate(-62269.0, 1924930122), -1924992391.00)

    def test0182(self):
        self.assertEquals(self.calculate(7162.0, 1096810344), -1096803182.00)

    def test0183(self):
        self.assertEquals(self.calculate(85486.0, 655015338), -654929852.00)

    def test0184(self):
        self.assertEquals(self.calculate(-42978.0, 502137219), -502180197.00)

    def test0185(self):
        self.assertEquals(self.calculate(113935.0, 672572447), -672458512.00)

    def test0186(self):
        self.assertEquals(self.calculate(42896.0, -1307868761), 1307911657.00)

    def test0187(self):
        self.assertEquals(self.calculate(-37707.0, -739353817), 739316110.00)

    def test0188(self):
        self.assertEquals(self.calculate(66363.0, -778550453), 778616816.00)

    def test0189(self):
        self.assertEquals(self.calculate(-120772.0, -1597965960), 1597845188.00)

    def test0190(self):
        self.assertEquals(self.calculate(2167.0, -662313424), 662315591.00)

    def test0191(self):
        self.assertEquals(self.calculate(4670.0, -492549000), 492553670.00)

    def test0192(self):
        self.assertEquals(self.calculate(-79406.0, 1476891717), -1476971123.00)

    def test0193(self):
        self.assertEquals(self.calculate(94260.0, -1325675782), 1325770042.00)

    def test0194(self):
        self.assertEquals(self.calculate(6382.0, 1193454275), -1193447893.00)

    def test0195(self):
        self.assertEquals(self.calculate(181410.0, -533869348), 534050758.00)

    def test0196(self):
        self.assertEquals(self.calculate(48142.0, 1693962491), -1693914349.00)

    def test0197(self):
        self.assertEquals(self.calculate(-188854.0, -648995910), 648807056.00)

    def test0198(self):
        self.assertEquals(self.calculate(133793.0, 913664951), -913531158.00)

    def test0199(self):
        self.assertEquals(self.calculate(3308.0, 1219711095), -1219707787.00)

    def test0200(self):
        self.assertEquals(self.calculate(194479.0, -2126419040), 2126613519.00)

    def test0201(self):
        self.assertEquals(self.calculate(-34987.0, -1433748746), 1433713759.00)

    def test0202(self):
        self.assertEquals(self.calculate(68569.0, -151524445), 151593014.00)

    def test0203(self):
        self.assertEquals(self.calculate(-97321.0, -142168961), 142071640.00)

    def test0204(self):
        self.assertEquals(self.calculate(-188001.0, 1720474142), -1720662143.00)

    def test0205(self):
        self.assertEquals(self.calculate(173929.0, 747140244), -746966315.00)

    def test0206(self):
        self.assertEquals(self.calculate(-12721.0, -1871092689), 1871079968.00)

    def test0207(self):
        self.assertEquals(self.calculate(65179.0, 272647726), -272582547.00)

    def test0208(self):
        self.assertEquals(self.calculate(165933.0, -759292471), 759458404.00)

    def test0209(self):
        self.assertEquals(self.calculate(-10577.0, -1413163129), 1413152552.00)

    def test0210(self):
        self.assertEquals(self.calculate(30627.0, 129243443), -129212816.00)

    def test0211(self):
        self.assertEquals(self.calculate(192138.0, -1634313333), 1634505471.00)

    def test0212(self):
        self.assertEquals(self.calculate(112695.0, -1622418424), 1622531119.00)

    def test0213(self):
        self.assertEquals(self.calculate(68254.0, -1246781131), 1246849385.00)

    def test0214(self):
        self.assertEquals(self.calculate(-63144.0, -1166696174), 1166633030.00)

    def test0215(self):
        self.assertEquals(self.calculate(16234.0, -1280735099), 1280751333.00)

    def test0216(self):
        self.assertEquals(self.calculate(-108595.0, 876435980), -876544575.00)

    def test0217(self):
        self.assertEquals(self.calculate(-176929.0, 1710308306), -1710485235.00)

    def test0218(self):
        self.assertEquals(self.calculate(-71002.0, 1943088555), -1943159557.00)

    def test0219(self):
        self.assertEquals(self.calculate(-5779.0, -1427888894), 1427883115.00)

    def test0220(self):
        self.assertEquals(self.calculate(-72379.0, 29910494), -29982873.00)

    def test0221(self):
        self.assertEquals(self.calculate(-4186.0, 1278392175), -1278396361.00)

    def test0222(self):
        self.assertEquals(self.calculate(-5491.0, 35317347), -35322838.00)

    def test0223(self):
        self.assertEquals(self.calculate(-48865.0, 1801812405), -1801861270.00)

    def test0224(self):
        self.assertEquals(self.calculate(-85032.0, -1418439015), 1418353983.00)

    def test0225(self):
        self.assertEquals(self.calculate(-64157.0, -784365548), 784301391.00)

    def test0226(self):
        self.assertEquals(self.calculate(-197788.0, 1625082569), -1625280357.00)

    def test0227(self):
        self.assertEquals(self.calculate(116770.0, -922495716), 922612486.00)

    def test0228(self):
        self.assertEquals(self.calculate(-180023.0, -1068474393), 1068294370.00)

    def test0229(self):
        self.assertEquals(self.calculate(150066.0, -1470794189), 1470944255.00)

    def test0230(self):
        self.assertEquals(self.calculate(91962.0, -55573202), 55665164.00)

    def test0231(self):
        self.assertEquals(self.calculate(179673.0, 1881669452), -1881489779.00)

    def test0232(self):
        self.assertEquals(self.calculate(-46955.0, 638361699), -638408654.00)

    def test0233(self):
        self.assertEquals(self.calculate(178136.0, 1724881408), -1724703272.00)

    def test0234(self):
        self.assertEquals(self.calculate(18306.0, 362574067), -362555761.00)

    def test0235(self):
        self.assertEquals(self.calculate(62110.0, -1254501478), 1254563588.00)

    def test0236(self):
        self.assertEquals(self.calculate(-17122.0, 1616551986), -1616569108.00)

    def test0237(self):
        self.assertEquals(self.calculate(-101293.0, 918876717), -918978010.00)

    def test0238(self):
        self.assertEquals(self.calculate(178506.0, 68495606), -68317100.00)

    def test0239(self):
        self.assertEquals(self.calculate(-15168.0, 1783828128), -1783843296.00)

    def test0240(self):
        self.assertEquals(self.calculate(-130982.0, 566458921), -566589903.00)

    def test0241(self):
        self.assertEquals(self.calculate(-96733.0, 1534185583), -1534282316.00)

    def test0242(self):
        self.assertEquals(self.calculate(168509.0, -1429198044), 1429366553.00)

    def test0243(self):
        self.assertEquals(self.calculate(64013.0, -1241602141), 1241666154.00)

    def test0244(self):
        self.assertEquals(self.calculate(-176715.0, 918181921), -918358636.00)

    def test0245(self):
        self.assertEquals(self.calculate(160301.0, 1146503049), -1146342748.00)

    def test0246(self):
        self.assertEquals(self.calculate(-165884.0, 527661204), -527827088.00)

    def test0247(self):
        self.assertEquals(self.calculate(-85752.0, -276820948), 276735196.00)

    def test0248(self):
        self.assertEquals(self.calculate(135550.0, 2018295413), -2018159863.00)

    def test0249(self):
        self.assertEquals(self.calculate(-98643.0, -877961278), 877862635.00)

    def test0250(self):
        self.assertEquals(self.calculate(-35088.0, 860256921), -860292009.00)

    def test0251(self):
        self.assertEquals(self.calculate(-57156.0, -1409512634), 1409455478.00)

    def test0252(self):
        self.assertEquals(self.calculate(-126667.0, -73146442), 73019775.00)

    def test0253(self):
        self.assertEquals(self.calculate(-131114.0, -1574384243), 1574253129.00)

    def test0254(self):
        self.assertEquals(self.calculate(23936.0, 183100745), -183076809.00)

    def test0255(self):
        self.assertEquals(self.calculate(169889.0, -141834296), 142004185.00)

    def test0256(self):
        self.assertEquals(self.calculate(67473.0, -1818525684), 1818593157.00)

    def test0257(self):
        self.assertEquals(self.calculate(66873.0, -1666842678), 1666909551.00)

    def test0258(self):
        self.assertEquals(self.calculate(177209.0, -413549137), 413726346.00)

    def test0259(self):
        self.assertEquals(self.calculate(-81811.0, 1663483322), -1663565133.00)

    def test0260(self):
        self.assertEquals(self.calculate(-78640.0, 1057541905), -1057620545.00)

    def test0261(self):
        self.assertEquals(self.calculate(119241.0, -359293494), 359412735.00)

    def test0262(self):
        self.assertEquals(self.calculate(63804.0, 1098528457), -1098464653.00)

    def test0263(self):
        self.assertEquals(self.calculate(-141316.0, 1672093201), -1672234517.00)

    def test0264(self):
        self.assertEquals(self.calculate(-146096.0, -1846666022), 1846519926.00)

    def test0265(self):
        self.assertEquals(self.calculate(-168315.0, 1719561347), -1719729662.00)

    def test0266(self):
        self.assertEquals(self.calculate(188440.0, 1555617708), -1555429268.00)

    def test0267(self):
        self.assertEquals(self.calculate(-141367.0, 890097070), -890238437.00)

    def test0268(self):
        self.assertEquals(self.calculate(-193649.0, -936103809), 935910160.00)

    def test0269(self):
        self.assertEquals(self.calculate(84986.0, 1993433647), -1993348661.00)

    def test0270(self):
        self.assertEquals(self.calculate(67919.0, -479886148), 479954067.00)

    def test0271(self):
        self.assertEquals(self.calculate(133915.0, -1492053840), 1492187755.00)

    def test0272(self):
        self.assertEquals(self.calculate(-141872.0, -1554954887), 1554813015.00)

    def test0273(self):
        self.assertEquals(self.calculate(-194620.0, 737964847), -738159467.00)

    def test0274(self):
        self.assertEquals(self.calculate(-89152.0, -1988823340), 1988734188.00)

    def test0275(self):
        self.assertEquals(self.calculate(47942.0, -1411760606), 1411808548.00)

    def test0276(self):
        self.assertEquals(self.calculate(-123492.0, 789340568), -789464060.00)

    def test0277(self):
        self.assertEquals(self.calculate(70910.0, -1344379487), 1344450397.00)

    def test0278(self):
        self.assertEquals(self.calculate(-88273.0, -270734057), 270645784.00)

    def test0279(self):
        self.assertEquals(self.calculate(-187555.0, 1897719063), -1897906618.00)

    def test0280(self):
        self.assertEquals(self.calculate(-65737.0, -1663648973), 1663583236.00)

    def test0281(self):
        self.assertEquals(self.calculate(115050.0, 63150664), -63035614.00)

    def test0282(self):
        self.assertEquals(self.calculate(151411.0, -351947230), 352098641.00)

    def test0283(self):
        self.assertEquals(self.calculate(146217.0, 118936154), -118789937.00)

    def test0284(self):
        self.assertEquals(self.calculate(-76680.0, -578665347), 578588667.00)

    def test0285(self):
        self.assertEquals(self.calculate(-148231.0, -1999462432), 1999314201.00)

    def test0286(self):
        self.assertEquals(self.calculate(177934.0, -2102545183), 2102723117.00)

    def test0287(self):
        self.assertEquals(self.calculate(126490.0, -1406744040), 1406870530.00)

    def test0288(self):
        self.assertEquals(self.calculate(9321.0, -2134924170), 2134933491.00)

    def test0289(self):
        self.assertEquals(self.calculate(-42286.0, -778358040), 778315754.00)

    def test0290(self):
        self.assertEquals(self.calculate(177111.0, -455263339), 455440450.00)

    def test0291(self):
        self.assertEquals(self.calculate(-80096.0, 1363288691), -1363368787.00)

    def test0292(self):
        self.assertEquals(self.calculate(-155553.0, -738517957), 738362404.00)

    def test0293(self):
        self.assertEquals(self.calculate(-29816.0, -1053359282), 1053329466.00)

    def test0294(self):
        self.assertEquals(self.calculate(-77221.0, 215163519), -215240740.00)

    def test0295(self):
        self.assertEquals(self.calculate(136917.0, 2105417102), -2105280185.00)

    def test0296(self):
        self.assertEquals(self.calculate(182749.0, 5728961), -5546212.00)

    def test0297(self):
        self.assertEquals(self.calculate(175407.0, -545005182), 545180589.00)

    def test0298(self):
        self.assertEquals(self.calculate(-197464.0, -1290642120), 1290444656.00)

    def test0299(self):
        self.assertEquals(self.calculate(44769.0, 650786181), -650741412.00)

    def test0300(self):
        self.assertEquals(self.calculate(166349.0, 2062739435), -2062573086.00)

    def test0301(self):
        self.assertEquals(self.calculate(-55288.0, 1306014779), -1306070067.00)

    def test0302(self):
        self.assertEquals(self.calculate(164262.0, -1174275305), 1174439567.00)

    def test0303(self):
        self.assertEquals(self.calculate(139988.0, 679188436), -679048448.00)

    def test0304(self):
        self.assertEquals(self.calculate(121140.0, 284296213), -284175073.00)

    def test0305(self):
        self.assertEquals(self.calculate(114353.0, 485888848), -485774495.00)

    def test0306(self):
        self.assertEquals(self.calculate(113633.0, 909974428), -909860795.00)

    def test0307(self):
        self.assertEquals(self.calculate(-180288.0, -1595957302), 1595777014.00)

    def test0308(self):
        self.assertEquals(self.calculate(36138.0, -1971524743), 1971560881.00)

    def test0309(self):
        self.assertEquals(self.calculate(172885.0, -2046409926), 2046582811.00)

    def test0310(self):
        self.assertEquals(self.calculate(105497.0, -1157224746), 1157330243.00)

    def test0311(self):
        self.assertEquals(self.calculate(69091.0, 778239911), -778170820.00)

    def test0312(self):
        self.assertEquals(self.calculate(189893.0, -687384028), 687573921.00)

    def test0313(self):
        self.assertEquals(self.calculate(7535.0, -183345709), 183353244.00)

    def test0314(self):
        self.assertEquals(self.calculate(-121913.0, -1064524158), 1064402245.00)

    def test0315(self):
        self.assertEquals(self.calculate(-21185.0, 840516966), -840538151.00)

    def test0316(self):
        self.assertEquals(self.calculate(48769.0, -11966646), 12015415.00)

    def test0317(self):
        self.assertEquals(self.calculate(148337.0, 726962157), -726813820.00)

    def test0318(self):
        self.assertEquals(self.calculate(186449.0, 1322977974), -1322791525.00)

    def test0319(self):
        self.assertEquals(self.calculate(-61854.0, 107363000), -107424854.00)

    def test0320(self):
        self.assertEquals(self.calculate(-81699.0, 1437599857), -1437681556.00)

    def test0321(self):
        self.assertEquals(self.calculate(-7189.0, 2066490753), -2066497942.00)

    def test0322(self):
        self.assertEquals(self.calculate(68885.0, -1564586094), 1564654979.00)

    def test0323(self):
        self.assertEquals(self.calculate(-151502.0, 247682557), -247834059.00)

    def test0324(self):
        self.assertEquals(self.calculate(124350.0, 1069091361), -1068967011.00)

    def test0325(self):
        self.assertEquals(self.calculate(-35978.0, -853742375), 853706397.00)

    def test0326(self):
        self.assertEquals(self.calculate(-22525.0, 1823949409), -1823971934.00)

    def test0327(self):
        self.assertEquals(self.calculate(-31765.0, 1113948203), -1113979968.00)

    def test0328(self):
        self.assertEquals(self.calculate(26806.0, -803708036), 803734842.00)

    def test0329(self):
        self.assertEquals(self.calculate(61978.0, -1754868288), 1754930266.00)

    def test0330(self):
        self.assertEquals(self.calculate(83355.0, -1735211496), 1735294851.00)

    def test0331(self):
        self.assertEquals(self.calculate(92151.0, 1901829893), -1901737742.00)

    def test0332(self):
        self.assertEquals(self.calculate(-67828.0, 650706931), -650774759.00)

    def test0333(self):
        self.assertEquals(self.calculate(121616.0, 793822059), -793700443.00)

    def test0334(self):
        self.assertEquals(self.calculate(164145.0, 388697260), -388533115.00)

    def test0335(self):
        self.assertEquals(self.calculate(83596.0, 368701158), -368617562.00)

    def test0336(self):
        self.assertEquals(self.calculate(183015.0, 1744774636), -1744591621.00)

    def test0337(self):
        self.assertEquals(self.calculate(-197924.0, -295920637), 295722713.00)

    def test0338(self):
        self.assertEquals(self.calculate(40889.0, -1618606482), 1618647371.00)

    def test0339(self):
        self.assertEquals(self.calculate(-110832.0, 1866099991), -1866210823.00)

    def test0340(self):
        self.assertEquals(self.calculate(-61925.0, 1750992540), -1751054465.00)

    def test0341(self):
        self.assertEquals(self.calculate(-145267.0, -1138121207), 1137975940.00)

    def test0342(self):
        self.assertEquals(self.calculate(-55286.0, 1574307424), -1574362710.00)

    def test0343(self):
        self.assertEquals(self.calculate(-46047.0, 1756856781), -1756902828.00)

    def test0344(self):
        self.assertEquals(self.calculate(60979.0, -1996255168), 1996316147.00)

    def test0345(self):
        self.assertEquals(self.calculate(176417.0, 1410125585), -1409949168.00)

    def test0346(self):
        self.assertEquals(self.calculate(66862.0, -940295898), 940362760.00)

    def test0347(self):
        self.assertEquals(self.calculate(-5745.0, 793089447), -793095192.00)

    def test0348(self):
        self.assertEquals(self.calculate(-45974.0, -352947494), 352901520.00)

    def test0349(self):
        self.assertEquals(self.calculate(99396.0, 1538649159), -1538549763.00)

    def test0350(self):
        self.assertEquals(self.calculate(-131270.0, 947822479), -947953749.00)

    def test0351(self):
        self.assertEquals(self.calculate(37128.0, -2023167473), 2023204601.00)

    def test0352(self):
        self.assertEquals(self.calculate(108934.0, 914800122), -914691188.00)

    def test0353(self):
        self.assertEquals(self.calculate(-16529.0, 2107971535), -2107988064.00)

    def test0354(self):
        self.assertEquals(self.calculate(-186523.0, 1769749791), -1769936314.00)

    def test0355(self):
        self.assertEquals(self.calculate(-111103.0, -1572032552), 1571921449.00)

    def test0356(self):
        self.assertEquals(self.calculate(187865.0, 1902118791), -1901930926.00)

    def test0357(self):
        self.assertEquals(self.calculate(126584.0, -640414207), 640540791.00)

    def test0358(self):
        self.assertEquals(self.calculate(-180387.0, 347332697), -347513084.00)

    def test0359(self):
        self.assertEquals(self.calculate(-20676.0, 1275488779), -1275509455.00)

    def test0360(self):
        self.assertEquals(self.calculate(60140.0, 125808696), -125748556.00)

    def test0361(self):
        self.assertEquals(self.calculate(94954.0, 2147166244), -2147071290.00)

    def test0362(self):
        self.assertEquals(self.calculate(45162.0, 1464221496), -1464176334.00)

    def test0363(self):
        self.assertEquals(self.calculate(-65948.0, -1715950717), 1715884769.00)

    def test0364(self):
        self.assertEquals(self.calculate(94871.0, 1767355325), -1767260454.00)

    def test0365(self):
        self.assertEquals(self.calculate(74751.0, -133085978), 133160729.00)

    def test0366(self):
        self.assertEquals(self.calculate(-114186.0, -1900743582), 1900629396.00)

    def test0367(self):
        self.assertEquals(self.calculate(103239.0, -1883823357), 1883926596.00)

    def test0368(self):
        self.assertEquals(self.calculate(-112475.0, -1019313397), 1019200922.00)

    def test0369(self):
        self.assertEquals(self.calculate(-47669.0, 1397307012), -1397354681.00)

    def test0370(self):
        self.assertEquals(self.calculate(-92106.0, 216033415), -216125521.00)

    def test0371(self):
        self.assertEquals(self.calculate(-183273.0, 882668934), -882852207.00)

    def test0372(self):
        self.assertEquals(self.calculate(-32446.0, -2003835805), 2003803359.00)

    def test0373(self):
        self.assertEquals(self.calculate(57417.0, 855075608), -855018191.00)

    def test0374(self):
        self.assertEquals(self.calculate(61676.0, 457238961), -457177285.00)

    def test0375(self):
        self.assertEquals(self.calculate(-100823.0, 842615217), -842716040.00)

    def test0376(self):
        self.assertEquals(self.calculate(-22566.0, -420420661), 420398095.00)

    def test0377(self):
        self.assertEquals(self.calculate(-125203.0, -1910561129), 1910435926.00)

    def test0378(self):
        self.assertEquals(self.calculate(-189947.0, -1230043152), 1229853205.00)

    def test0379(self):
        self.assertEquals(self.calculate(-51941.0, -357405924), 357353983.00)

    def test0380(self):
        self.assertEquals(self.calculate(-167960.0, 1811095785), -1811263745.00)

    def test0381(self):
        self.assertEquals(self.calculate(-184830.0, 2004329306), -2004514136.00)

    def test0382(self):
        self.assertEquals(self.calculate(-3396.0, 2058818440), -2058821836.00)

    def test0383(self):
        self.assertEquals(self.calculate(-142830.0, -1223175911), 1223033081.00)

    def test0384(self):
        self.assertEquals(self.calculate(-3639.0, 521633709), -521637348.00)

    def test0385(self):
        self.assertEquals(self.calculate(9256.0, -973390684), 973399940.00)

    def test0386(self):
        self.assertEquals(self.calculate(146801.0, 1108918558), -1108771757.00)

    def test0387(self):
        self.assertEquals(self.calculate(-183493.0, 2029077133), -2029260626.00)

    def test0388(self):
        self.assertEquals(self.calculate(-61037.0, -1825115368), 1825054331.00)

    def test0389(self):
        self.assertEquals(self.calculate(-182128.0, 2097052641), -2097234769.00)

    def test0390(self):
        self.assertEquals(self.calculate(4062.0, 703541214), -703537152.00)

    def test0391(self):
        self.assertEquals(self.calculate(22791.0, -1839400180), 1839422971.00)

    def test0392(self):
        self.assertEquals(self.calculate(91875.0, 331831298), -331739423.00)

    def test0393(self):
        self.assertEquals(self.calculate(-69887.0, 625750101), -625819988.00)

    def test0394(self):
        self.assertEquals(self.calculate(180311.0, 790585261), -790404950.00)

    def test0395(self):
        self.assertEquals(self.calculate(-128756.0, 1636535299), -1636664055.00)

    def test0396(self):
        self.assertEquals(self.calculate(56824.0, 572346005), -572289181.00)

    def test0397(self):
        self.assertEquals(self.calculate(41482.0, -741123997), 741165479.00)

    def test0398(self):
        self.assertEquals(self.calculate(-139348.0, -1961002650), 1960863302.00)

    def test0399(self):
        self.assertEquals(self.calculate(-100074.0, 1527507315), -1527607389.00)

    def test0400(self):
        self.assertEquals(self.calculate(40364.0, 1838556037), -1838515673.00)

    def test0401(self):
        self.assertEquals(self.calculate(188408.0, 1839853445), -1839665037.00)

    def test0402(self):
        self.assertEquals(self.calculate(-117078.0, -281163596), 281046518.00)

    def test0403(self):
        self.assertEquals(self.calculate(62476.0, 1786287200), -1786224724.00)

    def test0404(self):
        self.assertEquals(self.calculate(41991.0, 505421712), -505379721.00)

    def test0405(self):
        self.assertEquals(self.calculate(6638.0, 862192667), -862186029.00)

    def test0406(self):
        self.assertEquals(self.calculate(-81616.0, -1959399766), 1959318150.00)

    def test0407(self):
        self.assertEquals(self.calculate(125528.0, 1261464302), -1261338774.00)

    def test0408(self):
        self.assertEquals(self.calculate(-86693.0, -1948935345), 1948848652.00)

    def test0409(self):
        self.assertEquals(self.calculate(-27631.0, 1260214582), -1260242213.00)

    def test0410(self):
        self.assertEquals(self.calculate(-80308.0, 990376634), -990456942.00)

    def test0411(self):
        self.assertEquals(self.calculate(75738.0, 810618039), -810542301.00)

    def test0412(self):
        self.assertEquals(self.calculate(-48939.0, -1399640072), 1399591133.00)

    def test0413(self):
        self.assertEquals(self.calculate(-194180.0, 622313147), -622507327.00)

    def test0414(self):
        self.assertEquals(self.calculate(-123053.0, 1600375031), -1600498084.00)

    def test0415(self):
        self.assertEquals(self.calculate(-54040.0, -858224286), 858170246.00)

    def test0416(self):
        self.assertEquals(self.calculate(-54818.0, 2014303992), -2014358810.00)

    def test0417(self):
        self.assertEquals(self.calculate(106149.0, 1567443210), -1567337061.00)

    def test0418(self):
        self.assertEquals(self.calculate(-175952.0, -1572352590), 1572176638.00)

    def test0419(self):
        self.assertEquals(self.calculate(-75703.0, 1003261177), -1003336880.00)

    def test0420(self):
        self.assertEquals(self.calculate(561.0, 592291847), -592291286.00)

    def test0421(self):
        self.assertEquals(self.calculate(-73698.0, -556798921), 556725223.00)

    def test0422(self):
        self.assertEquals(self.calculate(-133075.0, -1375537102), 1375404027.00)

    def test0423(self):
        self.assertEquals(self.calculate(-131326.0, 734719623), -734850949.00)

    def test0424(self):
        self.assertEquals(self.calculate(-112044.0, 1603376172), -1603488216.00)

    def test0425(self):
        self.assertEquals(self.calculate(120293.0, -1073582975), 1073703268.00)

    def test0426(self):
        self.assertEquals(self.calculate(80817.0, -922725339), 922806156.00)

    def test0427(self):
        self.assertEquals(self.calculate(139224.0, -463325676), 463464900.00)

    def test0428(self):
        self.assertEquals(self.calculate(-133029.0, 764711077), -764844106.00)

    def test0429(self):
        self.assertEquals(self.calculate(-155453.0, -389726875), 389571422.00)

    def test0430(self):
        self.assertEquals(self.calculate(-161184.0, -530817228), 530656044.00)

    def test0431(self):
        self.assertEquals(self.calculate(86877.0, 1665940458), -1665853581.00)

    def test0432(self):
        self.assertEquals(self.calculate(101.0, 687845360), -687845259.00)

    def test0433(self):
        self.assertEquals(self.calculate(-77645.0, -1995555646), 1995478001.00)

    def test0434(self):
        self.assertEquals(self.calculate(-120994.0, 920120808), -920241802.00)

    def test0435(self):
        self.assertEquals(self.calculate(-123355.0, 216171404), -216294759.00)

    def test0436(self):
        self.assertEquals(self.calculate(144259.0, -1559985560), 1560129819.00)

    def test0437(self):
        self.assertEquals(self.calculate(-162032.0, 1899535816), -1899697848.00)

    def test0438(self):
        self.assertEquals(self.calculate(157710.0, -646531912), 646689622.00)

    def test0439(self):
        self.assertEquals(self.calculate(172085.0, -439079276), 439251361.00)

    def test0440(self):
        self.assertEquals(self.calculate(40635.0, -716797986), 716838621.00)

    def test0441(self):
        self.assertEquals(self.calculate(110518.0, -717560842), 717671360.00)

    def test0442(self):
        self.assertEquals(self.calculate(35218.0, -982282186), 982317404.00)

    def test0443(self):
        self.assertEquals(self.calculate(-37021.0, 404191807), -404228828.00)

    def test0444(self):
        self.assertEquals(self.calculate(127047.0, 356213470), -356086423.00)

    def test0445(self):
        self.assertEquals(self.calculate(67642.0, 1343540703), -1343473061.00)

    def test0446(self):
        self.assertEquals(self.calculate(-4744.0, 557920807), -557925551.00)

    def test0447(self):
        self.assertEquals(self.calculate(-34739.0, -1455089586), 1455054847.00)

    def test0448(self):
        self.assertEquals(self.calculate(-57762.0, -1212547118), 1212489356.00)

    def test0449(self):
        self.assertEquals(self.calculate(126190.0, 72536560), -72410370.00)

    def test0450(self):
        self.assertEquals(self.calculate(20119.0, -1506443493), 1506463612.00)

    def test0451(self):
        self.assertEquals(self.calculate(-26744.0, -975834077), 975807333.00)

    def test0452(self):
        self.assertEquals(self.calculate(-26581.0, 110719440), -110746021.00)

    def test0453(self):
        self.assertEquals(self.calculate(107457.0, 1243052285), -1242944828.00)

    def test0454(self):
        self.assertEquals(self.calculate(52717.0, -1792430531), 1792483248.00)

    def test0455(self):
        self.assertEquals(self.calculate(-157307.0, 141668576), -141825883.00)

    def test0456(self):
        self.assertEquals(self.calculate(19185.0, 359469819), -359450634.00)

    def test0457(self):
        self.assertEquals(self.calculate(-70018.0, -983675769), 983605751.00)

    def test0458(self):
        self.assertEquals(self.calculate(-115653.0, 1227794157), -1227909810.00)

    def test0459(self):
        self.assertEquals(self.calculate(-45281.0, 1957074267), -1957119548.00)

    def test0460(self):
        self.assertEquals(self.calculate(150867.0, -533408926), 533559793.00)

    def test0461(self):
        self.assertEquals(self.calculate(-184678.0, 1588109261), -1588293939.00)

    def test0462(self):
        self.assertEquals(self.calculate(184210.0, 428489892), -428305682.00)

    def test0463(self):
        self.assertEquals(self.calculate(-96920.0, -1348561499), 1348464579.00)

    def test0464(self):
        self.assertEquals(self.calculate(-116755.0, 743219058), -743335813.00)

    def test0465(self):
        self.assertEquals(self.calculate(16258.0, 1880916234), -1880899976.00)

    def test0466(self):
        self.assertEquals(self.calculate(-27678.0, -128623062), 128595384.00)

    def test0467(self):
        self.assertEquals(self.calculate(-100551.0, -774945495), 774844944.00)

    def test0468(self):
        self.assertEquals(self.calculate(-186508.0, 1605662255), -1605848763.00)

    def test0469(self):
        self.assertEquals(self.calculate(136329.0, -725970331), 726106660.00)

    def test0470(self):
        self.assertEquals(self.calculate(170896.0, 179675233), -179504337.00)

    def test0471(self):
        self.assertEquals(self.calculate(-42877.0, -1793457982), 1793415105.00)

    def test0472(self):
        self.assertEquals(self.calculate(96073.0, 224959923), -224863850.00)

    def test0473(self):
        self.assertEquals(self.calculate(100416.0, 753406372), -753305956.00)

    def test0474(self):
        self.assertEquals(self.calculate(-6871.0, 586400390), -586407261.00)

    def test0475(self):
        self.assertEquals(self.calculate(46334.0, 1486643396), -1486597062.00)

    def test0476(self):
        self.assertEquals(self.calculate(120562.0, -1752592507), 1752713069.00)

    def test0477(self):
        self.assertEquals(self.calculate(63326.0, -788064204), 788127530.00)

    def test0478(self):
        self.assertEquals(self.calculate(58620.0, 1225786777), -1225728157.00)

    def test0479(self):
        self.assertEquals(self.calculate(76617.0, 1457687316), -1457610699.00)

    def test0480(self):
        self.assertEquals(self.calculate(-84113.0, -1907056216), 1906972103.00)

    def test0481(self):
        self.assertEquals(self.calculate(-69429.0, 1991903688), -1991973117.00)

    def test0482(self):
        self.assertEquals(self.calculate(-90119.0, 46559568), -46649687.00)

    def test0483(self):
        self.assertEquals(self.calculate(-24477.0, 59036716), -59061193.00)

    def test0484(self):
        self.assertEquals(self.calculate(-40554.0, -383727912), 383687358.00)

    def test0485(self):
        self.assertEquals(self.calculate(-179776.0, -428350253), 428170477.00)

    def test0486(self):
        self.assertEquals(self.calculate(198588.0, 1647562973), -1647364385.00)

    def test0487(self):
        self.assertEquals(self.calculate(-148680.0, 226089114), -226237794.00)

    def test0488(self):
        self.assertEquals(self.calculate(142151.0, 496454733), -496312582.00)

    def test0489(self):
        self.assertEquals(self.calculate(-172698.0, -1331270188), 1331097490.00)

    def test0490(self):
        self.assertEquals(self.calculate(60083.0, -163769621), 163829704.00)

    def test0491(self):
        self.assertEquals(self.calculate(95574.0, 1481861407), -1481765833.00)

    def test0492(self):
        self.assertEquals(self.calculate(-98494.0, -1695842018), 1695743524.00)

    def test0493(self):
        self.assertEquals(self.calculate(178427.0, 1477786563), -1477608136.00)

    def test0494(self):
        self.assertEquals(self.calculate(125000.0, -266395811), 266520811.00)

    def test0495(self):
        self.assertEquals(self.calculate(-74396.0, 2074297546), -2074371942.00)

    def test0496(self):
        self.assertEquals(self.calculate(15225.0, 1590494071), -1590478846.00)

    def test0497(self):
        self.assertEquals(self.calculate(-172829.0, 886764202), -886937031.00)

    def test0498(self):
        self.assertEquals(self.calculate(71680.0, -1273678341), 1273750021.00)

    def test0499(self):
        self.assertEquals(self.calculate(127443.0, -155201478), 155328921.00)

    def test0500(self):
        self.assertEquals(self.calculate(-68173.0, 1521030522), -1521098695.00)

    def test0501(self):
        self.assertEquals(self.calculate(-14078.0, 96401033), -96415111.00)

    def test0502(self):
        self.assertEquals(self.calculate(99845.0, -253687911), 253787756.00)

    def test0503(self):
        self.assertEquals(self.calculate(137756.0, -451649362), 451787118.00)

    def test0504(self):
        self.assertEquals(self.calculate(75510.0, -1611940846), 1612016356.00)

    def test0505(self):
        self.assertEquals(self.calculate(145630.0, -653496608), 653642238.00)

    def test0506(self):
        self.assertEquals(self.calculate(-139224.0, -1765877114), 1765737890.00)

    def test0507(self):
        self.assertEquals(self.calculate(107145.0, 1632066387), -1631959242.00)

    def test0508(self):
        self.assertEquals(self.calculate(191292.0, -1217432456), 1217623748.00)

    def test0509(self):
        self.assertEquals(self.calculate(142357.0, 1153006059), -1152863702.00)

    def test0510(self):
        self.assertEquals(self.calculate(6280.0, 1556680768), -1556674488.00)

    def test0511(self):
        self.assertEquals(self.calculate(-20961.0, -423144677), 423123716.00)

    def test0512(self):
        self.assertEquals(self.calculate(40923.0, -1203465821), 1203506744.00)

    def test0513(self):
        self.assertEquals(self.calculate(77391.0, 1643383068), -1643305677.00)

    def test0514(self):
        self.assertEquals(self.calculate(92982.0, 265653752), -265560770.00)

    def test0515(self):
        self.assertEquals(self.calculate(-80502.0, -1721198892), 1721118390.00)

    def test0516(self):
        self.assertEquals(self.calculate(107029.0, -891317867), 891424896.00)

    def test0517(self):
        self.assertEquals(self.calculate(-12934.0, -2066526302), 2066513368.00)

    def test0518(self):
        self.assertEquals(self.calculate(-65626.0, -900695267), 900629641.00)

    def test0519(self):
        self.assertEquals(self.calculate(-191966.0, -1809758653), 1809566687.00)

    def test0520(self):
        self.assertEquals(self.calculate(189976.0, -940587149), 940777125.00)

    def test0521(self):
        self.assertEquals(self.calculate(9873.0, 675402762), -675392889.00)

    def test0522(self):
        self.assertEquals(self.calculate(-76633.0, -1440198050), 1440121417.00)

    def test0523(self):
        self.assertEquals(self.calculate(-152387.0, -904840079), 904687692.00)

    def test0524(self):
        self.assertEquals(self.calculate(-11239.0, 1798971987), -1798983226.00)

    def test0525(self):
        self.assertEquals(self.calculate(-54571.0, -1362045280), 1361990709.00)

    def test0526(self):
        self.assertEquals(self.calculate(-106383.0, 1106523784), -1106630167.00)

    def test0527(self):
        self.assertEquals(self.calculate(187189.0, 835377448), -835190259.00)

    def test0528(self):
        self.assertEquals(self.calculate(190971.0, -216817288), 217008259.00)

    def test0529(self):
        self.assertEquals(self.calculate(-189354.0, 403336008), -403525362.00)

    def test0530(self):
        self.assertEquals(self.calculate(176616.0, -1362133293), 1362309909.00)

    def test0531(self):
        self.assertEquals(self.calculate(-130549.0, -1932763023), 1932632474.00)

    def test0532(self):
        self.assertEquals(self.calculate(-61928.0, 708452160), -708514088.00)

    def test0533(self):
        self.assertEquals(self.calculate(-141849.0, -1855835638), 1855693789.00)

    def test0534(self):
        self.assertEquals(self.calculate(-5524.0, -1368235930), 1368230406.00)

    def test0535(self):
        self.assertEquals(self.calculate(-10363.0, -1922023194), 1922012831.00)

    def test0536(self):
        self.assertEquals(self.calculate(-66377.0, 1044230233), -1044296610.00)

    def test0537(self):
        self.assertEquals(self.calculate(-112914.0, 1476110250), -1476223164.00)

    def test0538(self):
        self.assertEquals(self.calculate(-9282.0, 371975264), -371984546.00)

    def test0539(self):
        self.assertEquals(self.calculate(20031.0, -245513353), 245533384.00)

    def test0540(self):
        self.assertEquals(self.calculate(66247.0, 1993927069), -1993860822.00)

    def test0541(self):
        self.assertEquals(self.calculate(90700.0, 1671299086), -1671208386.00)

    def test0542(self):
        self.assertEquals(self.calculate(103107.0, 91208880), -91105773.00)

    def test0543(self):
        self.assertEquals(self.calculate(-32634.0, 379427851), -379460485.00)

    def test0544(self):
        self.assertEquals(self.calculate(108017.0, 101530589), -101422572.00)

    def test0545(self):
        self.assertEquals(self.calculate(-183984.0, 374570626), -374754610.00)

    def test0546(self):
        self.assertEquals(self.calculate(4322.0, 938434144), -938429822.00)

    def test0547(self):
        self.assertEquals(self.calculate(-190730.0, 1718106128), -1718296858.00)

    def test0548(self):
        self.assertEquals(self.calculate(-77182.0, -651253582), 651176400.00)

    def test0549(self):
        self.assertEquals(self.calculate(-126450.0, 1951736822), -1951863272.00)

    def test0550(self):
        self.assertEquals(self.calculate(-3749.0, 906726777), -906730526.00)

    def test0551(self):
        self.assertEquals(self.calculate(158670.0, -821526419), 821685089.00)

    def test0552(self):
        self.assertEquals(self.calculate(-36476.0, -1094184105), 1094147629.00)

    def test0553(self):
        self.assertEquals(self.calculate(-140651.0, 1037897484), -1038038135.00)

    def test0554(self):
        self.assertEquals(self.calculate(-137597.0, 617493146), -617630743.00)

    def test0555(self):
        self.assertEquals(self.calculate(140772.0, -2098782383), 2098923155.00)

    def test0556(self):
        self.assertEquals(self.calculate(-111743.0, -1302158776), 1302047033.00)

    def test0557(self):
        self.assertEquals(self.calculate(117895.0, -384516598), 384634493.00)

    def test0558(self):
        self.assertEquals(self.calculate(121741.0, 1517257037), -1517135296.00)

    def test0559(self):
        self.assertEquals(self.calculate(95252.0, 1170530690), -1170435438.00)

    def test0560(self):
        self.assertEquals(self.calculate(-146517.0, -643463737), 643317220.00)

    def test0561(self):
        self.assertEquals(self.calculate(-56564.0, -1615507038), 1615450474.00)

    def test0562(self):
        self.assertEquals(self.calculate(-70055.0, 993099893), -993169948.00)

    def test0563(self):
        self.assertEquals(self.calculate(5169.0, -1211273932), 1211279101.00)

    def test0564(self):
        self.assertEquals(self.calculate(-36342.0, -2113682968), 2113646626.00)

    def test0565(self):
        self.assertEquals(self.calculate(-163254.0, -418679608), 418516354.00)

    def test0566(self):
        self.assertEquals(self.calculate(-116074.0, -359887899), 359771825.00)

    def test0567(self):
        self.assertEquals(self.calculate(-115286.0, -10670946), 10555660.00)

    def test0568(self):
        self.assertEquals(self.calculate(-50088.0, 655791296), -655841384.00)

    def test0569(self):
        self.assertEquals(self.calculate(-195638.0, 1409497259), -1409692897.00)

    def test0570(self):
        self.assertEquals(self.calculate(62516.0, -571777808), 571840324.00)

    def test0571(self):
        self.assertEquals(self.calculate(-153384.0, 1064280637), -1064434021.00)

    def test0572(self):
        self.assertEquals(self.calculate(142142.0, 1619577005), -1619434863.00)

    def test0573(self):
        self.assertEquals(self.calculate(-45369.0, -911459834), 911414465.00)

    def test0574(self):
        self.assertEquals(self.calculate(62528.0, -1674044607), 1674107135.00)

    def test0575(self):
        self.assertEquals(self.calculate(56848.0, 635090323), -635033475.00)

    def test0576(self):
        self.assertEquals(self.calculate(87467.0, 270076176), -269988709.00)

    def test0577(self):
        self.assertEquals(self.calculate(-169581.0, 877888100), -878057681.00)

    def test0578(self):
        self.assertEquals(self.calculate(-115895.0, -1041705997), 1041590102.00)

    def test0579(self):
        self.assertEquals(self.calculate(-158493.0, -535518636), 535360143.00)

    def test0580(self):
        self.assertEquals(self.calculate(63986.0, -1297442064), 1297506050.00)

    def test0581(self):
        self.assertEquals(self.calculate(77892.0, 1567682643), -1567604751.00)

    def test0582(self):
        self.assertEquals(self.calculate(-199433.0, -571220415), 571020982.00)

    def test0583(self):
        self.assertEquals(self.calculate(176621.0, 483173564), -482996943.00)

    def test0584(self):
        self.assertEquals(self.calculate(-18173.0, -525922247), 525904074.00)

    def test0585(self):
        self.assertEquals(self.calculate(-94887.0, -1705774774), 1705679887.00)

    def test0586(self):
        self.assertEquals(self.calculate(87705.0, -777434210), 777521915.00)

    def test0587(self):
        self.assertEquals(self.calculate(-172563.0, -998451441), 998278878.00)

    def test0588(self):
        self.assertEquals(self.calculate(-163430.0, -644479771), 644316341.00)

    def test0589(self):
        self.assertEquals(self.calculate(114892.0, 673998140), -673883248.00)

    def test0590(self):
        self.assertEquals(self.calculate(-26710.0, -1476773674), 1476746964.00)

    def test0591(self):
        self.assertEquals(self.calculate(175142.0, 1297163755), -1296988613.00)

    def test0592(self):
        self.assertEquals(self.calculate(49558.0, 188236097), -188186539.00)

    def test0593(self):
        self.assertEquals(self.calculate(-19331.0, -456830677), 456811346.00)

    def test0594(self):
        self.assertEquals(self.calculate(180468.0, -210387894), 210568362.00)

    def test0595(self):
        self.assertEquals(self.calculate(-88701.0, 840085203), -840173904.00)

    def test0596(self):
        self.assertEquals(self.calculate(-18338.0, 775434978), -775453316.00)

    def test0597(self):
        self.assertEquals(self.calculate(170606.0, -823792760), 823963366.00)

    def test0598(self):
        self.assertEquals(self.calculate(169821.0, 252738352), -252568531.00)

    def test0599(self):
        self.assertEquals(self.calculate(-114059.0, 1176668256), -1176782315.00)

    def test0600(self):
        self.assertEquals(self.calculate(92457.0, -78516926), 78609383.00)

    def test0601(self):
        self.assertEquals(self.calculate(6068.0, -2044941932), 2044948000.00)

    def test0602(self):
        self.assertEquals(self.calculate(-69814.0, 1107234104), -1107303918.00)

    def test0603(self):
        self.assertEquals(self.calculate(113055.0, 1905466501), -1905353446.00)

    def test0604(self):
        self.assertEquals(self.calculate(75895.0, -1592839776), 1592915671.00)

    def test0605(self):
        self.assertEquals(self.calculate(-50052.0, -106409887), 106359835.00)

    def test0606(self):
        self.assertEquals(self.calculate(171735.0, 1593913545), -1593741810.00)

    def test0607(self):
        self.assertEquals(self.calculate(147724.0, 392014574), -391866850.00)

    def test0608(self):
        self.assertEquals(self.calculate(30454.0, -1146564098), 1146594552.00)

    def test0609(self):
        self.assertEquals(self.calculate(21753.0, -1722591964), 1722613717.00)

    def test0610(self):
        self.assertEquals(self.calculate(-69308.0, 1621395632), -1621464940.00)

    def test0611(self):
        self.assertEquals(self.calculate(-149182.0, 316799713), -316948895.00)

    def test0612(self):
        self.assertEquals(self.calculate(-32305.0, -328349005), 328316700.00)

    def test0613(self):
        self.assertEquals(self.calculate(165835.0, 1047818894), -1047653059.00)

    def test0614(self):
        self.assertEquals(self.calculate(-161916.0, -1697681058), 1697519142.00)

    def test0615(self):
        self.assertEquals(self.calculate(35789.0, 601063779), -601027990.00)

    def test0616(self):
        self.assertEquals(self.calculate(-26241.0, -316622652), 316596411.00)

    def test0617(self):
        self.assertEquals(self.calculate(160466.0, -1702242393), 1702402859.00)

    def test0618(self):
        self.assertEquals(self.calculate(-175793.0, 1243267267), -1243443060.00)

    def test0619(self):
        self.assertEquals(self.calculate(-190423.0, 2056356300), -2056546723.00)

    def test0620(self):
        self.assertEquals(self.calculate(-170973.0, -1460151989), 1459981016.00)

    def test0621(self):
        self.assertEquals(self.calculate(-119262.0, 1083228808), -1083348070.00)

    def test0622(self):
        self.assertEquals(self.calculate(-46713.0, 1315579122), -1315625835.00)

    def test0623(self):
        self.assertEquals(self.calculate(180911.0, -1742703218), 1742884129.00)

    def test0624(self):
        self.assertEquals(self.calculate(167972.0, -2112802038), 2112970010.00)

    def test0625(self):
        self.assertEquals(self.calculate(132604.0, -698612848), 698745452.00)

    def test0626(self):
        self.assertEquals(self.calculate(-193240.0, -554883750), 554690510.00)

    def test0627(self):
        self.assertEquals(self.calculate(12850.0, 328455060), -328442210.00)

    def test0628(self):
        self.assertEquals(self.calculate(166620.0, 843884100), -843717480.00)

    def test0629(self):
        self.assertEquals(self.calculate(-11414.0, 1260363573), -1260374987.00)

    def test0630(self):
        self.assertEquals(self.calculate(-184392.0, -766080620), 765896228.00)

    def test0631(self):
        self.assertEquals(self.calculate(-10332.0, 436349884), -436360216.00)

    def test0632(self):
        self.assertEquals(self.calculate(146794.0, -424088166), 424234960.00)

    def test0633(self):
        self.assertEquals(self.calculate(193066.0, 250315584), -250122518.00)

    def test0634(self):
        self.assertEquals(self.calculate(-186270.0, 2127475558), -2127661828.00)

    def test0635(self):
        self.assertEquals(self.calculate(-63757.0, -1266274078), 1266210321.00)

    def test0636(self):
        self.assertEquals(self.calculate(-83468.0, -461951461), 461867993.00)

    def test0637(self):
        self.assertEquals(self.calculate(-70228.0, -604627930), 604557702.00)

    def test0638(self):
        self.assertEquals(self.calculate(65049.0, -2065782201), 2065847250.00)

    def test0639(self):
        self.assertEquals(self.calculate(21979.0, -1633455750), 1633477729.00)

    def test0640(self):
        self.assertEquals(self.calculate(-137512.0, 520908822), -521046334.00)

    def test0641(self):
        self.assertEquals(self.calculate(-186737.0, -1721705271), 1721518534.00)

    def test0642(self):
        self.assertEquals(self.calculate(-78650.0, 2074066418), -2074145068.00)

    def test0643(self):
        self.assertEquals(self.calculate(-128022.0, -1849630409), 1849502387.00)

    def test0644(self):
        self.assertEquals(self.calculate(-183272.0, 929474642), -929657914.00)

    def test0645(self):
        self.assertEquals(self.calculate(32426.0, -660193835), 660226261.00)

    def test0646(self):
        self.assertEquals(self.calculate(197631.0, -1452026596), 1452224227.00)

    def test0647(self):
        self.assertEquals(self.calculate(-154555.0, 1263044889), -1263199444.00)

    def test0648(self):
        self.assertEquals(self.calculate(-36718.0, -369331524), 369294806.00)

    def test0649(self):
        self.assertEquals(self.calculate(74681.0, -2014349410), 2014424091.00)

    def test0650(self):
        self.assertEquals(self.calculate(26236.0, -2050508783), 2050535019.00)

    def test0651(self):
        self.assertEquals(self.calculate(55741.0, 248358900), -248303159.00)

    def test0652(self):
        self.assertEquals(self.calculate(-78102.0, 1818385047), -1818463149.00)

    def test0653(self):
        self.assertEquals(self.calculate(-52746.0, -258431327), 258378581.00)

    def test0654(self):
        self.assertEquals(self.calculate(24085.0, 226043558), -226019473.00)

    def test0655(self):
        self.assertEquals(self.calculate(111177.0, -2071721567), 2071832744.00)

    def test0656(self):
        self.assertEquals(self.calculate(15422.0, 474966511), -474951089.00)

    def test0657(self):
        self.assertEquals(self.calculate(-21567.0, 54442100), -54463667.00)

    def test0658(self):
        self.assertEquals(self.calculate(-193686.0, -1786634843), 1786441157.00)

    def test0659(self):
        self.assertEquals(self.calculate(2559.0, 1471825686), -1471823127.00)

    def test0660(self):
        self.assertEquals(self.calculate(-118821.0, 301233164), -301351985.00)

    def test0661(self):
        self.assertEquals(self.calculate(-100621.0, 174842927), -174943548.00)

    def test0662(self):
        self.assertEquals(self.calculate(117562.0, 956063998), -955946436.00)

    def test0663(self):
        self.assertEquals(self.calculate(18556.0, -1209074319), 1209092875.00)

    def test0664(self):
        self.assertEquals(self.calculate(50300.0, 1416755209), -1416704909.00)

    def test0665(self):
        self.assertEquals(self.calculate(114209.0, 1926578556), -1926464347.00)

    def test0666(self):
        self.assertEquals(self.calculate(-149597.0, 1599644631), -1599794228.00)

    def test0667(self):
        self.assertEquals(self.calculate(-59866.0, 1189154483), -1189214349.00)

    def test0668(self):
        self.assertEquals(self.calculate(-62517.0, 940771346), -940833863.00)

    def test0669(self):
        self.assertEquals(self.calculate(24520.0, 1645073186), -1645048666.00)

    def test0670(self):
        self.assertEquals(self.calculate(91562.0, 709398649), -709307087.00)

    def test0671(self):
        self.assertEquals(self.calculate(23587.0, -623492913), 623516500.00)

    def test0672(self):
        self.assertEquals(self.calculate(-143759.0, 1643503158), -1643646917.00)

    def test0673(self):
        self.assertEquals(self.calculate(-89853.0, 343546123), -343635976.00)

    def test0674(self):
        self.assertEquals(self.calculate(70516.0, 397584929), -397514413.00)

    def test0675(self):
        self.assertEquals(self.calculate(159640.0, -407764877), 407924517.00)

    def test0676(self):
        self.assertEquals(self.calculate(145710.0, 1132343650), -1132197940.00)

    def test0677(self):
        self.assertEquals(self.calculate(-37768.0, -1250739604), 1250701836.00)

    def test0678(self):
        self.assertEquals(self.calculate(49368.0, 590087490), -590038122.00)

    def test0679(self):
        self.assertEquals(self.calculate(153007.0, 1314101374), -1313948367.00)

    def test0680(self):
        self.assertEquals(self.calculate(-133527.0, -1048029450), 1047895923.00)

    def test0681(self):
        self.assertEquals(self.calculate(153987.0, -1640066297), 1640220284.00)

    def test0682(self):
        self.assertEquals(self.calculate(-197155.0, 173271374), -173468529.00)

    def test0683(self):
        self.assertEquals(self.calculate(104236.0, 599864543), -599760307.00)

    def test0684(self):
        self.assertEquals(self.calculate(-151745.0, -998491139), 998339394.00)

    def test0685(self):
        self.assertEquals(self.calculate(26190.0, -946314622), 946340812.00)

    def test0686(self):
        self.assertEquals(self.calculate(26221.0, 1014150157), -1014123936.00)

    def test0687(self):
        self.assertEquals(self.calculate(-85555.0, 1808810796), -1808896351.00)

    def test0688(self):
        self.assertEquals(self.calculate(-26511.0, -897267937), 897241426.00)

    def test0689(self):
        self.assertEquals(self.calculate(126124.0, -218117401), 218243525.00)

    def test0690(self):
        self.assertEquals(self.calculate(129912.0, 737113278), -736983366.00)

    def test0691(self):
        self.assertEquals(self.calculate(-191966.0, -867189624), 866997658.00)

    def test0692(self):
        self.assertEquals(self.calculate(50716.0, 1599462526), -1599411810.00)

    def test0693(self):
        self.assertEquals(self.calculate(-133853.0, -1911767601), 1911633748.00)

    def test0694(self):
        self.assertEquals(self.calculate(-83789.0, -1016940319), 1016856530.00)

    def test0695(self):
        self.assertEquals(self.calculate(-131443.0, 230502133), -230633576.00)

    def test0696(self):
        self.assertEquals(self.calculate(-154506.0, -830906254), 830751748.00)

    def test0697(self):
        self.assertEquals(self.calculate(82543.0, -1038605509), 1038688052.00)

    def test0698(self):
        self.assertEquals(self.calculate(158659.0, 500518246), -500359587.00)

    def test0699(self):
        self.assertEquals(self.calculate(-87299.0, 1414827245), -1414914544.00)

    def test0700(self):
        self.assertEquals(self.calculate(143670.0, 631934125), -631790455.00)

    def test0701(self):
        self.assertEquals(self.calculate(-84456.0, 1369469457), -1369553913.00)

    def test0702(self):
        self.assertEquals(self.calculate(171151.0, 1394569544), -1394398393.00)

    def test0703(self):
        self.assertEquals(self.calculate(-122335.0, 519203566), -519325901.00)

    def test0704(self):
        self.assertEquals(self.calculate(78641.0, 440513211), -440434570.00)

    def test0705(self):
        self.assertEquals(self.calculate(-194234.0, -1553998561), 1553804327.00)

    def test0706(self):
        self.assertEquals(self.calculate(-89675.0, -1904058360), 1903968685.00)

    def test0707(self):
        self.assertEquals(self.calculate(44818.0, 1951315498), -1951270680.00)

    def test0708(self):
        self.assertEquals(self.calculate(53535.0, -2135738911), 2135792446.00)

    def test0709(self):
        self.assertEquals(self.calculate(23104.0, 262548109), -262525005.00)

    def test0710(self):
        self.assertEquals(self.calculate(71449.0, -670830469), 670901918.00)

    def test0711(self):
        self.assertEquals(self.calculate(81607.0, 7508250), -7426643.00)

    def test0712(self):
        self.assertEquals(self.calculate(65874.0, -939302581), 939368455.00)

    def test0713(self):
        self.assertEquals(self.calculate(-81740.0, -1238488554), 1238406814.00)

    def test0714(self):
        self.assertEquals(self.calculate(-62297.0, 924294654), -924356951.00)

    def test0715(self):
        self.assertEquals(self.calculate(-165787.0, 2059853977), -2060019764.00)

    def test0716(self):
        self.assertEquals(self.calculate(143788.0, -2138089925), 2138233713.00)

    def test0717(self):
        self.assertEquals(self.calculate(-155558.0, -87254414), 87098856.00)

    def test0718(self):
        self.assertEquals(self.calculate(-176602.0, 525539013), -525715615.00)

    def test0719(self):
        self.assertEquals(self.calculate(15067.0, -1089500143), 1089515210.00)

    def test0720(self):
        self.assertEquals(self.calculate(172475.0, -1143347489), 1143519964.00)

    def test0721(self):
        self.assertEquals(self.calculate(150713.0, 573728171), -573577458.00)

    def test0722(self):
        self.assertEquals(self.calculate(92351.0, -1536584807), 1536677158.00)

    def test0723(self):
        self.assertEquals(self.calculate(-64293.0, -117025775), 116961482.00)

    def test0724(self):
        self.assertEquals(self.calculate(81756.0, 1775999584), -1775917828.00)

    def test0725(self):
        self.assertEquals(self.calculate(-174660.0, -1708290533), 1708115873.00)

    def test0726(self):
        self.assertEquals(self.calculate(87403.0, 1336746239), -1336658836.00)

    def test0727(self):
        self.assertEquals(self.calculate(190349.0, -1251267590), 1251457939.00)

    def test0728(self):
        self.assertEquals(self.calculate(-45300.0, 329841161), -329886461.00)

    def test0729(self):
        self.assertEquals(self.calculate(95162.0, -286106577), 286201739.00)

    def test0730(self):
        self.assertEquals(self.calculate(-164357.0, 518285501), -518449858.00)

    def test0731(self):
        self.assertEquals(self.calculate(196593.0, -1617396040), 1617592633.00)

    def test0732(self):
        self.assertEquals(self.calculate(-86900.0, -658682529), 658595629.00)

    def test0733(self):
        self.assertEquals(self.calculate(-189818.0, -765118683), 764928865.00)

    def test0734(self):
        self.assertEquals(self.calculate(83552.0, 2116069410), -2115985858.00)

    def test0735(self):
        self.assertEquals(self.calculate(159449.0, 1616982855), -1616823406.00)

    def test0736(self):
        self.assertEquals(self.calculate(95931.0, -2036195811), 2036291742.00)

    def test0737(self):
        self.assertEquals(self.calculate(57942.0, 1189484623), -1189426681.00)

    def test0738(self):
        self.assertEquals(self.calculate(-121947.0, -355680900), 355558953.00)

    def test0739(self):
        self.assertEquals(self.calculate(-114391.0, -1872307076), 1872192685.00)

    def test0740(self):
        self.assertEquals(self.calculate(-82629.0, 1588814593), -1588897222.00)

    def test0741(self):
        self.assertEquals(self.calculate(-197178.0, -1880828538), 1880631360.00)

    def test0742(self):
        self.assertEquals(self.calculate(-23247.0, -829539811), 829516564.00)

    def test0743(self):
        self.assertEquals(self.calculate(75340.0, 1350719534), -1350644194.00)

    def test0744(self):
        self.assertEquals(self.calculate(-76446.0, 293048317), -293124763.00)

    def test0745(self):
        self.assertEquals(self.calculate(-166675.0, 605784005), -605950680.00)

    def test0746(self):
        self.assertEquals(self.calculate(-41571.0, -782029000), 781987429.00)

    def test0747(self):
        self.assertEquals(self.calculate(113300.0, 765466998), -765353698.00)

    def test0748(self):
        self.assertEquals(self.calculate(72436.0, -167851227), 167923663.00)

    def test0749(self):
        self.assertEquals(self.calculate(60720.0, -586920660), 586981380.00)

    def test0750(self):
        self.assertEquals(self.calculate(107404.0, 333310715), -333203311.00)

    def test0751(self):
        self.assertEquals(self.calculate(-140714.0, 2004159711), -2004300425.00)

    def test0752(self):
        self.assertEquals(self.calculate(43207.0, -388059271), 388102478.00)

    def test0753(self):
        self.assertEquals(self.calculate(-25763.0, -1964112968), 1964087205.00)

    def test0754(self):
        self.assertEquals(self.calculate(100575.0, 1501692753), -1501592178.00)

    def test0755(self):
        self.assertEquals(self.calculate(9913.0, 1998536304), -1998526391.00)

    def test0756(self):
        self.assertEquals(self.calculate(141527.0, 1381191767), -1381050240.00)

    def test0757(self):
        self.assertEquals(self.calculate(-177765.0, -1211092812), 1210915047.00)

    def test0758(self):
        self.assertEquals(self.calculate(-180382.0, 147114992), -147295374.00)

    def test0759(self):
        self.assertEquals(self.calculate(-51993.0, 325475728), -325527721.00)

    def test0760(self):
        self.assertEquals(self.calculate(-59535.0, -1361576462), 1361516927.00)

    def test0761(self):
        self.assertEquals(self.calculate(88683.0, 538627885), -538539202.00)

    def test0762(self):
        self.assertEquals(self.calculate(-132922.0, -1502797462), 1502664540.00)

    def test0763(self):
        self.assertEquals(self.calculate(-19104.0, 1442360798), -1442379902.00)

    def test0764(self):
        self.assertEquals(self.calculate(179375.0, -564300398), 564479773.00)

    def test0765(self):
        self.assertEquals(self.calculate(-98656.0, -598112747), 598014091.00)

    def test0766(self):
        self.assertEquals(self.calculate(-185919.0, -1885746258), 1885560339.00)

    def test0767(self):
        self.assertEquals(self.calculate(-97348.0, -599502568), 599405220.00)

    def test0768(self):
        self.assertEquals(self.calculate(-60596.0, 1545055587), -1545116183.00)

    def test0769(self):
        self.assertEquals(self.calculate(-39609.0, -1280203774), 1280164165.00)

    def test0770(self):
        self.assertEquals(self.calculate(63099.0, 869115807), -869052708.00)

    def test0771(self):
        self.assertEquals(self.calculate(-143342.0, 616097707), -616241049.00)

    def test0772(self):
        self.assertEquals(self.calculate(-131418.0, 1695025046), -1695156464.00)

    def test0773(self):
        self.assertEquals(self.calculate(-157767.0, 746537102), -746694869.00)

    def test0774(self):
        self.assertEquals(self.calculate(-178111.0, 665281371), -665459482.00)

    def test0775(self):
        self.assertEquals(self.calculate(46666.0, 1687950369), -1687903703.00)

    def test0776(self):
        self.assertEquals(self.calculate(22535.0, -719742697), 719765232.00)

    def test0777(self):
        self.assertEquals(self.calculate(187015.0, -1715744657), 1715931672.00)

    def test0778(self):
        self.assertEquals(self.calculate(-441.0, 829607247), -829607688.00)

    def test0779(self):
        self.assertEquals(self.calculate(173480.0, 1168524700), -1168351220.00)

    def test0780(self):
        self.assertEquals(self.calculate(155491.0, -1218635791), 1218791282.00)

    def test0781(self):
        self.assertEquals(self.calculate(-191783.0, -633641776), 633449993.00)

    def test0782(self):
        self.assertEquals(self.calculate(-176782.0, -1155114808), 1154938026.00)

    def test0783(self):
        self.assertEquals(self.calculate(10972.0, -206161707), 206172679.00)

    def test0784(self):
        self.assertEquals(self.calculate(187560.0, 42961992), -42774432.00)

    def test0785(self):
        self.assertEquals(self.calculate(-2522.0, -223884265), 223881743.00)

    def test0786(self):
        self.assertEquals(self.calculate(104134.0, 954548179), -954444045.00)

    def test0787(self):
        self.assertEquals(self.calculate(-195369.0, 729994755), -730190124.00)

    def test0788(self):
        self.assertEquals(self.calculate(114909.0, -1764557535), 1764672444.00)

    def test0789(self):
        self.assertEquals(self.calculate(168978.0, 388082763), -387913785.00)

    def test0790(self):
        self.assertEquals(self.calculate(-16878.0, -115487320), 115470442.00)

    def test0791(self):
        self.assertEquals(self.calculate(101307.0, 530059491), -529958184.00)

    def test0792(self):
        self.assertEquals(self.calculate(92875.0, 1746221538), -1746128663.00)

    def test0793(self):
        self.assertEquals(self.calculate(47887.0, -214232489), 214280376.00)

    def test0794(self):
        self.assertEquals(self.calculate(-51586.0, 1880980938), -1881032524.00)

    def test0795(self):
        self.assertEquals(self.calculate(-34827.0, -382238147), 382203320.00)

    def test0796(self):
        self.assertEquals(self.calculate(21527.0, 657610576), -657589049.00)

    def test0797(self):
        self.assertEquals(self.calculate(-72942.0, 1503112951), -1503185893.00)

    def test0798(self):
        self.assertEquals(self.calculate(-81501.0, -1668905575), 1668824074.00)

    def test0799(self):
        self.assertEquals(self.calculate(188964.0, -839169404), 839358368.00)

    def test0800(self):
        self.assertEquals(self.calculate(155488.0, 1363889899), -1363734411.00)

    def test0801(self):
        self.assertEquals(self.calculate(174266.0, 1457526259), -1457351993.00)

    def test0802(self):
        self.assertEquals(self.calculate(93134.0, 1433050690), -1432957556.00)

    def test0803(self):
        self.assertEquals(self.calculate(-40881.0, -99542207), 99501326.00)

    def test0804(self):
        self.assertEquals(self.calculate(153854.0, -1920562623), 1920716477.00)

    def test0805(self):
        self.assertEquals(self.calculate(8336.0, 631038393), -631030057.00)

    def test0806(self):
        self.assertEquals(self.calculate(-133523.0, -1357482674), 1357349151.00)

    def test0807(self):
        self.assertEquals(self.calculate(42483.0, 1579965464), -1579922981.00)

    def test0808(self):
        self.assertEquals(self.calculate(152178.0, 1618047428), -1617895250.00)

    def test0809(self):
        self.assertEquals(self.calculate(-64550.0, -1202908356), 1202843806.00)

    def test0810(self):
        self.assertEquals(self.calculate(115067.0, -99952491), 100067558.00)

    def test0811(self):
        self.assertEquals(self.calculate(-109035.0, -1782474480), 1782365445.00)

    def test0812(self):
        self.assertEquals(self.calculate(-155714.0, 1750660346), -1750816060.00)

    def test0813(self):
        self.assertEquals(self.calculate(-26271.0, -734178901), 734152630.00)

    def test0814(self):
        self.assertEquals(self.calculate(138873.0, -716800569), 716939442.00)

    def test0815(self):
        self.assertEquals(self.calculate(-115494.0, 445795715), -445911209.00)

    def test0816(self):
        self.assertEquals(self.calculate(143632.0, -1647591609), 1647735241.00)

    def test0817(self):
        self.assertEquals(self.calculate(193071.0, 1664051953), -1663858882.00)

    def test0818(self):
        self.assertEquals(self.calculate(164665.0, 2103795617), -2103630952.00)

    def test0819(self):
        self.assertEquals(self.calculate(-60002.0, -196268862), 196208860.00)

    def test0820(self):
        self.assertEquals(self.calculate(-78595.0, 2036408795), -2036487390.00)

    def test0821(self):
        self.assertEquals(self.calculate(199156.0, -870768543), 870967699.00)

    def test0822(self):
        self.assertEquals(self.calculate(158896.0, -1363593295), 1363752191.00)

    def test0823(self):
        self.assertEquals(self.calculate(154158.0, -1346850338), 1347004496.00)

    def test0824(self):
        self.assertEquals(self.calculate(-178134.0, 34248808), -34426942.00)

    def test0825(self):
        self.assertEquals(self.calculate(137379.0, -1255976742), 1256114121.00)

    def test0826(self):
        self.assertEquals(self.calculate(149077.0, -1780679356), 1780828433.00)

    def test0827(self):
        self.assertEquals(self.calculate(-41747.0, 1075038746), -1075080493.00)

    def test0828(self):
        self.assertEquals(self.calculate(140905.0, -176757263), 176898168.00)

    def test0829(self):
        self.assertEquals(self.calculate(168826.0, 1371240591), -1371071765.00)

    def test0830(self):
        self.assertEquals(self.calculate(191564.0, 124542397), -124350833.00)

    def test0831(self):
        self.assertEquals(self.calculate(123063.0, -360270859), 360393922.00)

    def test0832(self):
        self.assertEquals(self.calculate(-118520.0, 709513737), -709632257.00)

    def test0833(self):
        self.assertEquals(self.calculate(-36138.0, -1641504845), 1641468707.00)

    def test0834(self):
        self.assertEquals(self.calculate(104088.0, 2068189084), -2068084996.00)

    def test0835(self):
        self.assertEquals(self.calculate(100113.0, -451504537), 451604650.00)

    def test0836(self):
        self.assertEquals(self.calculate(165839.0, -1072249799), 1072415638.00)

    def test0837(self):
        self.assertEquals(self.calculate(-12689.0, -541638905), 541626216.00)

    def test0838(self):
        self.assertEquals(self.calculate(125856.0, 1027300982), -1027175126.00)

    def test0839(self):
        self.assertEquals(self.calculate(168129.0, 144670538), -144502409.00)

    def test0840(self):
        self.assertEquals(self.calculate(189188.0, 1321077373), -1320888185.00)

    def test0841(self):
        self.assertEquals(self.calculate(55129.0, 1782989642), -1782934513.00)

    def test0842(self):
        self.assertEquals(self.calculate(-27724.0, 1145316711), -1145344435.00)

    def test0843(self):
        self.assertEquals(self.calculate(91586.0, 1599324236), -1599232650.00)

    def test0844(self):
        self.assertEquals(self.calculate(-172037.0, 1070542318), -1070714355.00)

    def test0845(self):
        self.assertEquals(self.calculate(-79508.0, 1337787014), -1337866522.00)

    def test0846(self):
        self.assertEquals(self.calculate(59301.0, -1575119566), 1575178867.00)

    def test0847(self):
        self.assertEquals(self.calculate(90552.0, 1226995497), -1226904945.00)

    def test0848(self):
        self.assertEquals(self.calculate(-191899.0, -1759623406), 1759431507.00)

    def test0849(self):
        self.assertEquals(self.calculate(-198940.0, -1073006096), 1072807156.00)

    def test0850(self):
        self.assertEquals(self.calculate(133085.0, 1987866991), -1987733906.00)

    def test0851(self):
        self.assertEquals(self.calculate(-34084.0, 543552381), -543586465.00)

    def test0852(self):
        self.assertEquals(self.calculate(-140415.0, 430367415), -430507830.00)

    def test0853(self):
        self.assertEquals(self.calculate(119236.0, -1872098037), 1872217273.00)

    def test0854(self):
        self.assertEquals(self.calculate(140933.0, 1809979618), -1809838685.00)

    def test0855(self):
        self.assertEquals(self.calculate(-173834.0, 1241863932), -1242037766.00)

    def test0856(self):
        self.assertEquals(self.calculate(-168053.0, -170279553), 170111500.00)

    def test0857(self):
        self.assertEquals(self.calculate(-75659.0, -126732817), 126657158.00)

    def test0858(self):
        self.assertEquals(self.calculate(-46473.0, -476077722), 476031249.00)

    def test0859(self):
        self.assertEquals(self.calculate(-135179.0, 1955190179), -1955325358.00)

    def test0860(self):
        self.assertEquals(self.calculate(199735.0, 1676515334), -1676315599.00)

    def test0861(self):
        self.assertEquals(self.calculate(129495.0, -291240905), 291370400.00)

    def test0862(self):
        self.assertEquals(self.calculate(42737.0, 1839124877), -1839082140.00)

    def test0863(self):
        self.assertEquals(self.calculate(189276.0, 1253460097), -1253270821.00)

    def test0864(self):
        self.assertEquals(self.calculate(79777.0, -152145258), 152225035.00)

    def test0865(self):
        self.assertEquals(self.calculate(-146038.0, -2090626777), 2090480739.00)

    def test0866(self):
        self.assertEquals(self.calculate(-193019.0, 1614591593), -1614784612.00)

    def test0867(self):
        self.assertEquals(self.calculate(-72466.0, 1876672659), -1876745125.00)

    def test0868(self):
        self.assertEquals(self.calculate(97264.0, -1966149324), 1966246588.00)

    def test0869(self):
        self.assertEquals(self.calculate(-91917.0, 1863890289), -1863982206.00)

    def test0870(self):
        self.assertEquals(self.calculate(47544.0, 971059182), -971011638.00)

    def test0871(self):
        self.assertEquals(self.calculate(-87772.0, 1800838411), -1800926183.00)

    def test0872(self):
        self.assertEquals(self.calculate(194353.0, -379746097), 379940450.00)

    def test0873(self):
        self.assertEquals(self.calculate(-159391.0, 813517712), -813677103.00)

    def test0874(self):
        self.assertEquals(self.calculate(46952.0, 1115214813), -1115167861.00)

    def test0875(self):
        self.assertEquals(self.calculate(104727.0, 646640594), -646535867.00)

    def test0876(self):
        self.assertEquals(self.calculate(40011.0, 2071643068), -2071603057.00)

    def test0877(self):
        self.assertEquals(self.calculate(189414.0, -984056479), 984245893.00)

    def test0878(self):
        self.assertEquals(self.calculate(134363.0, 1603837119), -1603702756.00)

    def test0879(self):
        self.assertEquals(self.calculate(10094.0, 360665013), -360654919.00)

    def test0880(self):
        self.assertEquals(self.calculate(100189.0, 697277162), -697176973.00)

    def test0881(self):
        self.assertEquals(self.calculate(122670.0, -2076596631), 2076719301.00)

    def test0882(self):
        self.assertEquals(self.calculate(-31485.0, -1095671615), 1095640130.00)

    def test0883(self):
        self.assertEquals(self.calculate(-44670.0, 1744567039), -1744611709.00)

    def test0884(self):
        self.assertEquals(self.calculate(-40244.0, -1493317666), 1493277422.00)

    def test0885(self):
        self.assertEquals(self.calculate(-155258.0, 551794718), -551949976.00)

    def test0886(self):
        self.assertEquals(self.calculate(-158622.0, 2128165690), -2128324312.00)

    def test0887(self):
        self.assertEquals(self.calculate(-94403.0, 2065057165), -2065151568.00)

    def test0888(self):
        self.assertEquals(self.calculate(73803.0, 1301685295), -1301611492.00)

    def test0889(self):
        self.assertEquals(self.calculate(88646.0, -629910256), 629998902.00)

    def test0890(self):
        self.assertEquals(self.calculate(183323.0, -1903515152), 1903698475.00)

    def test0891(self):
        self.assertEquals(self.calculate(-136050.0, -1897331168), 1897195118.00)

    def test0892(self):
        self.assertEquals(self.calculate(60584.0, 1838791453), -1838730869.00)

    def test0893(self):
        self.assertEquals(self.calculate(138056.0, -775000571), 775138627.00)

    def test0894(self):
        self.assertEquals(self.calculate(937.0, -1590481539), 1590482476.00)

    def test0895(self):
        self.assertEquals(self.calculate(184576.0, -681725887), 681910463.00)

    def test0896(self):
        self.assertEquals(self.calculate(113222.0, -489777742), 489890964.00)

    def test0897(self):
        self.assertEquals(self.calculate(-12733.0, -507201523), 507188790.00)

    def test0898(self):
        self.assertEquals(self.calculate(241.0, 131492234), -131491993.00)

    def test0899(self):
        self.assertEquals(self.calculate(54301.0, -219270470), 219324771.00)

    def test0900(self):
        self.assertEquals(self.calculate(175940.0, 1452618156), -1452442216.00)

    def test0901(self):
        self.assertEquals(self.calculate(31671.0, 769434229), -769402558.00)

    def test0902(self):
        self.assertEquals(self.calculate(-124739.0, -773633460), 773508721.00)

    def test0903(self):
        self.assertEquals(self.calculate(-103925.0, 1292194375), -1292298300.00)

    def test0904(self):
        self.assertEquals(self.calculate(52831.0, -1466734773), 1466787604.00)

    def test0905(self):
        self.assertEquals(self.calculate(-98282.0, 640767656), -640865938.00)

    def test0906(self):
        self.assertEquals(self.calculate(-43981.0, -600886032), 600842051.00)

    def test0907(self):
        self.assertEquals(self.calculate(-170826.0, 2130952972), -2131123798.00)

    def test0908(self):
        self.assertEquals(self.calculate(71450.0, -1613860770), 1613932220.00)

    def test0909(self):
        self.assertEquals(self.calculate(-78595.0, -1857824283), 1857745688.00)

    def test0910(self):
        self.assertEquals(self.calculate(173636.0, -1477830506), 1478004142.00)

    def test0911(self):
        self.assertEquals(self.calculate(197761.0, 1884352734), -1884154973.00)

    def test0912(self):
        self.assertEquals(self.calculate(-106702.0, -364409919), 364303217.00)

    def test0913(self):
        self.assertEquals(self.calculate(-42883.0, 1064666892), -1064709775.00)

    def test0914(self):
        self.assertEquals(self.calculate(-134025.0, -1688000187), 1687866162.00)

    def test0915(self):
        self.assertEquals(self.calculate(-117244.0, -1660012129), 1659894885.00)

    def test0916(self):
        self.assertEquals(self.calculate(-157998.0, 324093246), -324251244.00)

    def test0917(self):
        self.assertEquals(self.calculate(-22330.0, -525358691), 525336361.00)

    def test0918(self):
        self.assertEquals(self.calculate(73488.0, -651496796), 651570284.00)

    def test0919(self):
        self.assertEquals(self.calculate(-22523.0, 134904543), -134927066.00)

    def test0920(self):
        self.assertEquals(self.calculate(125176.0, 1378342484), -1378217308.00)

    def test0921(self):
        self.assertEquals(self.calculate(4873.0, 210891581), -210886708.00)

    def test0922(self):
        self.assertEquals(self.calculate(21999.0, -1907034021), 1907056020.00)

    def test0923(self):
        self.assertEquals(self.calculate(174477.0, -1700988048), 1701162525.00)

    def test0924(self):
        self.assertEquals(self.calculate(-252.0, 349446464), -349446716.00)

    def test0925(self):
        self.assertEquals(self.calculate(192236.0, -348599819), 348792055.00)

    def test0926(self):
        self.assertEquals(self.calculate(34052.0, 178883795), -178849743.00)

    def test0927(self):
        self.assertEquals(self.calculate(-81479.0, 21621501), -21702980.00)

    def test0928(self):
        self.assertEquals(self.calculate(-89113.0, 1374244082), -1374333195.00)

    def test0929(self):
        self.assertEquals(self.calculate(134816.0, -347313259), 347448075.00)

    def test0930(self):
        self.assertEquals(self.calculate(-88324.0, -186086747), 185998423.00)

    def test0931(self):
        self.assertEquals(self.calculate(83767.0, 1864972492), -1864888725.00)

    def test0932(self):
        self.assertEquals(self.calculate(21276.0, 1635086108), -1635064832.00)

    def test0933(self):
        self.assertEquals(self.calculate(-83635.0, -698578549), 698494914.00)

    def test0934(self):
        self.assertEquals(self.calculate(-185925.0, -16453976), 16268051.00)

    def test0935(self):
        self.assertEquals(self.calculate(130356.0, -490284146), 490414502.00)

    def test0936(self):
        self.assertEquals(self.calculate(-17954.0, -1950746040), 1950728086.00)

    def test0937(self):
        self.assertEquals(self.calculate(-184063.0, -359039161), 358855098.00)

    def test0938(self):
        self.assertEquals(self.calculate(40773.0, 1509671714), -1509630941.00)

    def test0939(self):
        self.assertEquals(self.calculate(-189225.0, -94825253), 94636028.00)

    def test0940(self):
        self.assertEquals(self.calculate(86999.0, -404902847), 404989846.00)

    def test0941(self):
        self.assertEquals(self.calculate(39507.0, 1481195098), -1481155591.00)

    def test0942(self):
        self.assertEquals(self.calculate(-172298.0, -2119677047), 2119504749.00)

    def test0943(self):
        self.assertEquals(self.calculate(-160654.0, 1114098894), -1114259548.00)

    def test0944(self):
        self.assertEquals(self.calculate(104249.0, -398983720), 399087969.00)

    def test0945(self):
        self.assertEquals(self.calculate(62725.0, 1574539081), -1574476356.00)

    def test0946(self):
        self.assertEquals(self.calculate(117968.0, -1885375662), 1885493630.00)

    def test0947(self):
        self.assertEquals(self.calculate(-98956.0, -1264761350), 1264662394.00)

    def test0948(self):
        self.assertEquals(self.calculate(6132.0, -159700701), 159706833.00)

    def test0949(self):
        self.assertEquals(self.calculate(9318.0, -613373105), 613382423.00)

    def test0950(self):
        self.assertEquals(self.calculate(-107553.0, -1154421332), 1154313779.00)

    def test0951(self):
        self.assertEquals(self.calculate(-143299.0, 343252442), -343395741.00)

    def test0952(self):
        self.assertEquals(self.calculate(-95034.0, -714659535), 714564501.00)

    def test0953(self):
        self.assertEquals(self.calculate(97393.0, 302997195), -302899802.00)

    def test0954(self):
        self.assertEquals(self.calculate(-110155.0, -47758177), 47648022.00)

    def test0955(self):
        self.assertEquals(self.calculate(86305.0, -328781680), 328867985.00)

    def test0956(self):
        self.assertEquals(self.calculate(65512.0, 378292226), -378226714.00)

    def test0957(self):
        self.assertEquals(self.calculate(92743.0, -743014292), 743107035.00)

    def test0958(self):
        self.assertEquals(self.calculate(-49215.0, -338443947), 338394732.00)

    def test0959(self):
        self.assertEquals(self.calculate(111001.0, 2130290956), -2130179955.00)

    def test0960(self):
        self.assertEquals(self.calculate(24737.0, 986559645), -986534908.00)

    def test0961(self):
        self.assertEquals(self.calculate(124029.0, -386235180), 386359209.00)

    def test0962(self):
        self.assertEquals(self.calculate(-128107.0, -1523054030), 1522925923.00)

    def test0963(self):
        self.assertEquals(self.calculate(-82441.0, -2016537518), 2016455077.00)

    def test0964(self):
        self.assertEquals(self.calculate(88403.0, -1989241017), 1989329420.00)

    def test0965(self):
        self.assertEquals(self.calculate(-70988.0, 1080293262), -1080364250.00)

    def test0966(self):
        self.assertEquals(self.calculate(86302.0, -1448311438), 1448397740.00)

    def test0967(self):
        self.assertEquals(self.calculate(130672.0, 765458372), -765327700.00)

    def test0968(self):
        self.assertEquals(self.calculate(-121156.0, -644512116), 644390960.00)

    def test0969(self):
        self.assertEquals(self.calculate(-33762.0, 383561929), -383595691.00)

    def test0970(self):
        self.assertEquals(self.calculate(-69201.0, 699416876), -699486077.00)

    def test0971(self):
        self.assertEquals(self.calculate(30356.0, -1593938039), 1593968395.00)

    def test0972(self):
        self.assertEquals(self.calculate(40300.0, 62233596), -62193296.00)

    def test0973(self):
        self.assertEquals(self.calculate(-153171.0, -1691040523), 1690887352.00)

    def test0974(self):
        self.assertEquals(self.calculate(148057.0, -1375788596), 1375936653.00)

    def test0975(self):
        self.assertEquals(self.calculate(46423.0, -1277561482), 1277607905.00)

    def test0976(self):
        self.assertEquals(self.calculate(-113002.0, -791578588), 791465586.00)

    def test0977(self):
        self.assertEquals(self.calculate(-123501.0, -719431135), 719307634.00)

    def test0978(self):
        self.assertEquals(self.calculate(56316.0, 2100340325), -2100284009.00)

    def test0979(self):
        self.assertEquals(self.calculate(-101583.0, -5849189), 5747606.00)

    def test0980(self):
        self.assertEquals(self.calculate(-134380.0, 9740345), -9874725.00)

    def test0981(self):
        self.assertEquals(self.calculate(191876.0, 973964619), -973772743.00)

    def test0982(self):
        self.assertEquals(self.calculate(81724.0, -931657830), 931739554.00)

    def test0983(self):
        self.assertEquals(self.calculate(-61418.0, 7161153), -7222571.00)

    def test0984(self):
        self.assertEquals(self.calculate(75447.0, 1179799232), -1179723785.00)

    def test0985(self):
        self.assertEquals(self.calculate(-1368.0, 1507440251), -1507441619.00)

    def test0986(self):
        self.assertEquals(self.calculate(115532.0, -1877028570), 1877144102.00)

    def test0987(self):
        self.assertEquals(self.calculate(189026.0, -1427685265), 1427874291.00)

    def test0988(self):
        self.assertEquals(self.calculate(-56950.0, 1023610317), -1023667267.00)

    def test0989(self):
        self.assertEquals(self.calculate(131550.0, -1328993053), 1329124603.00)

    def test0990(self):
        self.assertEquals(self.calculate(-184109.0, 506172234), -506356343.00)

    def test0991(self):
        self.assertEquals(self.calculate(-181989.0, 779176546), -779358535.00)

    def test0992(self):
        self.assertEquals(self.calculate(80296.0, -1784571289), 1784651585.00)

    def test0993(self):
        self.assertEquals(self.calculate(137444.0, -911249208), 911386652.00)

    def test0994(self):
        self.assertEquals(self.calculate(180375.0, -1582096526), 1582276901.00)

    def test0995(self):
        self.assertEquals(self.calculate(-16912.0, 1258044335), -1258061247.00)

    def test0996(self):
        self.assertEquals(self.calculate(-19096.0, -259301091), 259281995.00)

    def test0997(self):
        self.assertEquals(self.calculate(-82007.0, 1550783706), -1550865713.00)

    def test0998(self):
        self.assertEquals(self.calculate(189414.0, -865686610), 865876024.00)

    def test0999(self):
        self.assertEquals(self.calculate(55968.0, -51402669), 51458637.00)

    def test1000(self):
        self.assertEquals(self.calculate(-82665.0, 707635960), -707718625.00)

    def test1001(self):
        self.assertEquals(self.calculate(-178250.0, 80501537), -80679787.00)

    def test1002(self):
        self.assertEquals(self.calculate(-41475.0, 1694772088), -1694813563.00)

    def test1003(self):
        self.assertEquals(self.calculate(84631.0, 48600886), -48516255.00)

    def test1004(self):
        self.assertEquals(self.calculate(-56607.0, 861959575), -862016182.00)

    def test1005(self):
        self.assertEquals(self.calculate(88733.0, 1893824287), -1893735554.00)

    def test1006(self):
        self.assertEquals(self.calculate(157086.0, -1833172050), 1833329136.00)

    def test1007(self):
        self.assertEquals(self.calculate(-140578.0, -2072344485), 2072203907.00)

    def test1008(self):
        self.assertEquals(self.calculate(-40822.0, 553060349), -553101171.00)

    def test1009(self):
        self.assertEquals(self.calculate(-60285.0, 1144408494), -1144468779.00)

    def test1010(self):
        self.assertEquals(self.calculate(56538.0, -1598606741), 1598663279.00)

    def test1011(self):
        self.assertEquals(self.calculate(170639.0, 1519688680), -1519518041.00)

    def test1012(self):
        self.assertEquals(self.calculate(-81056.0, 36611335), -36692391.00)

    def test1013(self):
        self.assertEquals(self.calculate(-115028.0, -452063546), 451948518.00)

    def test1014(self):
        self.assertEquals(self.calculate(54847.0, -350020818), 350075665.00)

    def test1015(self):
        self.assertEquals(self.calculate(-99970.0, -567898863), 567798893.00)

    def test1016(self):
        self.assertEquals(self.calculate(24526.0, 47040785), -47016259.00)

    def test1017(self):
        self.assertEquals(self.calculate(-103722.0, -95247421), 95143699.00)

    def test1018(self):
        self.assertEquals(self.calculate(44878.0, -1000884165), 1000929043.00)

    def test1019(self):
        self.assertEquals(self.calculate(-28572.0, 1035227566), -1035256138.00)

    def test1020(self):
        self.assertEquals(self.calculate(128229.0, -2094586756), 2094714985.00)

    def test1021(self):
        self.assertEquals(self.calculate(154837.0, 377353001), -377198164.00)

    def test1022(self):
        self.assertEquals(self.calculate(-104216.0, 237332631), -237436847.00)

    def test1023(self):
        self.assertEquals(self.calculate(158054.0, -1016407676), 1016565730.00)



class TestVM_Sub_FloatFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushF(rhs)
        v.VM_Sub()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(101066.0, 133258.0), -32192.00)

    def test0001(self):
        self.assertEquals(self.calculate(49001.0, 173972.0), -124971.00)

    def test0002(self):
        self.assertEquals(self.calculate(-25069.0, -36035.0), 10966.00)

    def test0003(self):
        self.assertEquals(self.calculate(34698.0, -116785.0), 151483.00)

    def test0004(self):
        self.assertEquals(self.calculate(82910.0, 87207.0), -4297.00)

    def test0005(self):
        self.assertEquals(self.calculate(-45633.0, -1938.0), -43695.00)

    def test0006(self):
        self.assertEquals(self.calculate(167015.0, 46576.0), 120439.00)

    def test0007(self):
        self.assertEquals(self.calculate(144143.0, 53417.0), 90726.00)

    def test0008(self):
        self.assertEquals(self.calculate(-159795.0, -54909.0), -104886.00)

    def test0009(self):
        self.assertEquals(self.calculate(163076.0, 136223.0), 26853.00)

    def test0010(self):
        self.assertEquals(self.calculate(22886.0, 74415.0), -51529.00)

    def test0011(self):
        self.assertEquals(self.calculate(-69219.0, 12106.0), -81325.00)

    def test0012(self):
        self.assertEquals(self.calculate(-100115.0, -124810.0), 24695.00)

    def test0013(self):
        self.assertEquals(self.calculate(8824.0, 163867.0), -155043.00)

    def test0014(self):
        self.assertEquals(self.calculate(-9896.0, 11416.0), -21312.00)

    def test0015(self):
        self.assertEquals(self.calculate(-11260.0, 55258.0), -66518.00)

    def test0016(self):
        self.assertEquals(self.calculate(-88744.0, 112044.0), -200788.00)

    def test0017(self):
        self.assertEquals(self.calculate(-11491.0, 97531.0), -109022.00)

    def test0018(self):
        self.assertEquals(self.calculate(-58419.0, 120341.0), -178760.00)

    def test0019(self):
        self.assertEquals(self.calculate(123277.0, 13143.0), 110134.00)

    def test0020(self):
        self.assertEquals(self.calculate(-142514.0, 83945.0), -226459.00)

    def test0021(self):
        self.assertEquals(self.calculate(-116643.0, -131938.0), 15295.00)

    def test0022(self):
        self.assertEquals(self.calculate(-128777.0, -13175.0), -115602.00)

    def test0023(self):
        self.assertEquals(self.calculate(-113825.0, 102553.0), -216378.00)

    def test0024(self):
        self.assertEquals(self.calculate(20139.0, 178703.0), -158564.00)

    def test0025(self):
        self.assertEquals(self.calculate(-12612.0, -123446.0), 110834.00)

    def test0026(self):
        self.assertEquals(self.calculate(97872.0, 23657.0), 74215.00)

    def test0027(self):
        self.assertEquals(self.calculate(-113462.0, 60179.0), -173641.00)

    def test0028(self):
        self.assertEquals(self.calculate(-74931.0, 117880.0), -192811.00)

    def test0029(self):
        self.assertEquals(self.calculate(-133056.0, -6796.0), -126260.00)

    def test0030(self):
        self.assertEquals(self.calculate(-190045.0, 5095.0), -195140.00)

    def test0031(self):
        self.assertEquals(self.calculate(-89458.0, 190258.0), -279716.00)

    def test0032(self):
        self.assertEquals(self.calculate(160040.0, -99432.0), 259472.00)

    def test0033(self):
        self.assertEquals(self.calculate(131976.0, -179159.0), 311135.00)

    def test0034(self):
        self.assertEquals(self.calculate(59213.0, 139513.0), -80300.00)

    def test0035(self):
        self.assertEquals(self.calculate(-106248.0, 176133.0), -282381.00)

    def test0036(self):
        self.assertEquals(self.calculate(-89351.0, 114280.0), -203631.00)

    def test0037(self):
        self.assertEquals(self.calculate(-87787.0, -71041.0), -16746.00)

    def test0038(self):
        self.assertEquals(self.calculate(-103862.0, -30520.0), -73342.00)

    def test0039(self):
        self.assertEquals(self.calculate(-95757.0, -15241.0), -80516.00)

    def test0040(self):
        self.assertEquals(self.calculate(58199.0, -160261.0), 218460.00)

    def test0041(self):
        self.assertEquals(self.calculate(98332.0, 43316.0), 55016.00)

    def test0042(self):
        self.assertEquals(self.calculate(38396.0, 186964.0), -148568.00)

    def test0043(self):
        self.assertEquals(self.calculate(116863.0, -158984.0), 275847.00)

    def test0044(self):
        self.assertEquals(self.calculate(-81374.0, 187218.0), -268592.00)

    def test0045(self):
        self.assertEquals(self.calculate(33490.0, -9123.0), 42613.00)

    def test0046(self):
        self.assertEquals(self.calculate(-190976.0, -143938.0), -47038.00)

    def test0047(self):
        self.assertEquals(self.calculate(-83701.0, -9454.0), -74247.00)

    def test0048(self):
        self.assertEquals(self.calculate(31412.0, -187044.0), 218456.00)

    def test0049(self):
        self.assertEquals(self.calculate(118367.0, 158317.0), -39950.00)

    def test0050(self):
        self.assertEquals(self.calculate(-64637.0, -99933.0), 35296.00)

    def test0051(self):
        self.assertEquals(self.calculate(-47244.0, 102358.0), -149602.00)

    def test0052(self):
        self.assertEquals(self.calculate(160848.0, -59034.0), 219882.00)

    def test0053(self):
        self.assertEquals(self.calculate(141568.0, 85446.0), 56122.00)

    def test0054(self):
        self.assertEquals(self.calculate(-70362.0, 100546.0), -170908.00)

    def test0055(self):
        self.assertEquals(self.calculate(147369.0, -95189.0), 242558.00)

    def test0056(self):
        self.assertEquals(self.calculate(-114709.0, 171547.0), -286256.00)

    def test0057(self):
        self.assertEquals(self.calculate(-132737.0, -33030.0), -99707.00)

    def test0058(self):
        self.assertEquals(self.calculate(129045.0, 70694.0), 58351.00)

    def test0059(self):
        self.assertEquals(self.calculate(84202.0, 76410.0), 7792.00)

    def test0060(self):
        self.assertEquals(self.calculate(-9672.0, 162809.0), -172481.00)

    def test0061(self):
        self.assertEquals(self.calculate(46583.0, 187710.0), -141127.00)

    def test0062(self):
        self.assertEquals(self.calculate(179163.0, 6303.0), 172860.00)

    def test0063(self):
        self.assertEquals(self.calculate(190652.0, 44376.0), 146276.00)

    def test0064(self):
        self.assertEquals(self.calculate(177180.0, 139889.0), 37291.00)

    def test0065(self):
        self.assertEquals(self.calculate(62919.0, -13288.0), 76207.00)

    def test0066(self):
        self.assertEquals(self.calculate(-28362.0, 8880.0), -37242.00)

    def test0067(self):
        self.assertEquals(self.calculate(45179.0, 89869.0), -44690.00)

    def test0068(self):
        self.assertEquals(self.calculate(51952.0, -113783.0), 165735.00)

    def test0069(self):
        self.assertEquals(self.calculate(-174816.0, 110825.0), -285641.00)

    def test0070(self):
        self.assertEquals(self.calculate(182835.0, -109339.0), 292174.00)

    def test0071(self):
        self.assertEquals(self.calculate(-122840.0, -183717.0), 60877.00)

    def test0072(self):
        self.assertEquals(self.calculate(49512.0, -160688.0), 210200.00)

    def test0073(self):
        self.assertEquals(self.calculate(24106.0, -115403.0), 139509.00)

    def test0074(self):
        self.assertEquals(self.calculate(-185584.0, 150981.0), -336565.00)

    def test0075(self):
        self.assertEquals(self.calculate(-47097.0, 196255.0), -243352.00)

    def test0076(self):
        self.assertEquals(self.calculate(-30388.0, 39925.0), -70313.00)

    def test0077(self):
        self.assertEquals(self.calculate(-161259.0, 70414.0), -231673.00)

    def test0078(self):
        self.assertEquals(self.calculate(-113239.0, -31156.0), -82083.00)

    def test0079(self):
        self.assertEquals(self.calculate(31686.0, -198435.0), 230121.00)

    def test0080(self):
        self.assertEquals(self.calculate(197609.0, -198095.0), 395704.00)

    def test0081(self):
        self.assertEquals(self.calculate(3233.0, -151577.0), 154810.00)

    def test0082(self):
        self.assertEquals(self.calculate(-86067.0, 83081.0), -169148.00)

    def test0083(self):
        self.assertEquals(self.calculate(-99583.0, 127113.0), -226696.00)

    def test0084(self):
        self.assertEquals(self.calculate(-96289.0, -41580.0), -54709.00)

    def test0085(self):
        self.assertEquals(self.calculate(-29371.0, 29538.0), -58909.00)

    def test0086(self):
        self.assertEquals(self.calculate(152993.0, 144696.0), 8297.00)

    def test0087(self):
        self.assertEquals(self.calculate(180188.0, 60897.0), 119291.00)

    def test0088(self):
        self.assertEquals(self.calculate(-144212.0, -49160.0), -95052.00)

    def test0089(self):
        self.assertEquals(self.calculate(-76890.0, 40482.0), -117372.00)

    def test0090(self):
        self.assertEquals(self.calculate(-118997.0, 81446.0), -200443.00)

    def test0091(self):
        self.assertEquals(self.calculate(-40678.0, 90158.0), -130836.00)

    def test0092(self):
        self.assertEquals(self.calculate(-20063.0, -101379.0), 81316.00)

    def test0093(self):
        self.assertEquals(self.calculate(-151735.0, -22369.0), -129366.00)

    def test0094(self):
        self.assertEquals(self.calculate(-62764.0, -19550.0), -43214.00)

    def test0095(self):
        self.assertEquals(self.calculate(2369.0, 192858.0), -190489.00)

    def test0096(self):
        self.assertEquals(self.calculate(61329.0, 98579.0), -37250.00)

    def test0097(self):
        self.assertEquals(self.calculate(129182.0, 90484.0), 38698.00)

    def test0098(self):
        self.assertEquals(self.calculate(66556.0, 111587.0), -45031.00)

    def test0099(self):
        self.assertEquals(self.calculate(135292.0, 35971.0), 99321.00)

    def test0100(self):
        self.assertEquals(self.calculate(-169247.0, 91232.0), -260479.00)

    def test0101(self):
        self.assertEquals(self.calculate(-42135.0, -183413.0), 141278.00)

    def test0102(self):
        self.assertEquals(self.calculate(-164642.0, -190511.0), 25869.00)

    def test0103(self):
        self.assertEquals(self.calculate(-143294.0, 78903.0), -222197.00)

    def test0104(self):
        self.assertEquals(self.calculate(-91804.0, 72137.0), -163941.00)

    def test0105(self):
        self.assertEquals(self.calculate(195801.0, -139664.0), 335465.00)

    def test0106(self):
        self.assertEquals(self.calculate(-160114.0, 10433.0), -170547.00)

    def test0107(self):
        self.assertEquals(self.calculate(-137403.0, 164166.0), -301569.00)

    def test0108(self):
        self.assertEquals(self.calculate(31530.0, -8976.0), 40506.00)

    def test0109(self):
        self.assertEquals(self.calculate(-94633.0, 116774.0), -211407.00)

    def test0110(self):
        self.assertEquals(self.calculate(109315.0, 103152.0), 6163.00)

    def test0111(self):
        self.assertEquals(self.calculate(-159047.0, -161256.0), 2209.00)

    def test0112(self):
        self.assertEquals(self.calculate(-185067.0, 35942.0), -221009.00)

    def test0113(self):
        self.assertEquals(self.calculate(-137456.0, 33678.0), -171134.00)

    def test0114(self):
        self.assertEquals(self.calculate(52432.0, -167647.0), 220079.00)

    def test0115(self):
        self.assertEquals(self.calculate(-113440.0, 26840.0), -140280.00)

    def test0116(self):
        self.assertEquals(self.calculate(-10115.0, 156653.0), -166768.00)

    def test0117(self):
        self.assertEquals(self.calculate(7675.0, 100425.0), -92750.00)

    def test0118(self):
        self.assertEquals(self.calculate(-7368.0, 139053.0), -146421.00)

    def test0119(self):
        self.assertEquals(self.calculate(-81451.0, 18851.0), -100302.00)

    def test0120(self):
        self.assertEquals(self.calculate(-180108.0, 81709.0), -261817.00)

    def test0121(self):
        self.assertEquals(self.calculate(-177946.0, 52992.0), -230938.00)

    def test0122(self):
        self.assertEquals(self.calculate(946.0, 129573.0), -128627.00)

    def test0123(self):
        self.assertEquals(self.calculate(21382.0, 19895.0), 1487.00)

    def test0124(self):
        self.assertEquals(self.calculate(78640.0, 199358.0), -120718.00)

    def test0125(self):
        self.assertEquals(self.calculate(74844.0, 158907.0), -84063.00)

    def test0126(self):
        self.assertEquals(self.calculate(21441.0, 55435.0), -33994.00)

    def test0127(self):
        self.assertEquals(self.calculate(135278.0, -69121.0), 204399.00)

    def test0128(self):
        self.assertEquals(self.calculate(52992.0, -109193.0), 162185.00)

    def test0129(self):
        self.assertEquals(self.calculate(-65393.0, -144320.0), 78927.00)

    def test0130(self):
        self.assertEquals(self.calculate(57581.0, -69884.0), 127465.00)

    def test0131(self):
        self.assertEquals(self.calculate(83930.0, 43717.0), 40213.00)

    def test0132(self):
        self.assertEquals(self.calculate(-142352.0, 105789.0), -248141.00)

    def test0133(self):
        self.assertEquals(self.calculate(-10095.0, -121116.0), 111021.00)

    def test0134(self):
        self.assertEquals(self.calculate(86008.0, 112380.0), -26372.00)

    def test0135(self):
        self.assertEquals(self.calculate(-179635.0, -90150.0), -89485.00)

    def test0136(self):
        self.assertEquals(self.calculate(60083.0, 18310.0), 41773.00)

    def test0137(self):
        self.assertEquals(self.calculate(-30956.0, -127117.0), 96161.00)

    def test0138(self):
        self.assertEquals(self.calculate(-20107.0, 162789.0), -182896.00)

    def test0139(self):
        self.assertEquals(self.calculate(166776.0, -75216.0), 241992.00)

    def test0140(self):
        self.assertEquals(self.calculate(-153068.0, 78146.0), -231214.00)

    def test0141(self):
        self.assertEquals(self.calculate(-8032.0, 139382.0), -147414.00)

    def test0142(self):
        self.assertEquals(self.calculate(-163558.0, 17935.0), -181493.00)

    def test0143(self):
        self.assertEquals(self.calculate(135524.0, 110505.0), 25019.00)

    def test0144(self):
        self.assertEquals(self.calculate(106028.0, 192854.0), -86826.00)

    def test0145(self):
        self.assertEquals(self.calculate(81859.0, 95188.0), -13329.00)

    def test0146(self):
        self.assertEquals(self.calculate(104527.0, 187377.0), -82850.00)

    def test0147(self):
        self.assertEquals(self.calculate(-145010.0, 67438.0), -212448.00)

    def test0148(self):
        self.assertEquals(self.calculate(-48741.0, -150746.0), 102005.00)

    def test0149(self):
        self.assertEquals(self.calculate(154107.0, -124119.0), 278226.00)

    def test0150(self):
        self.assertEquals(self.calculate(-105138.0, 142177.0), -247315.00)

    def test0151(self):
        self.assertEquals(self.calculate(-36013.0, 137352.0), -173365.00)

    def test0152(self):
        self.assertEquals(self.calculate(-5018.0, 188227.0), -193245.00)

    def test0153(self):
        self.assertEquals(self.calculate(-85117.0, -182006.0), 96889.00)

    def test0154(self):
        self.assertEquals(self.calculate(-128774.0, 156558.0), -285332.00)

    def test0155(self):
        self.assertEquals(self.calculate(-147272.0, 72681.0), -219953.00)

    def test0156(self):
        self.assertEquals(self.calculate(-143535.0, -166427.0), 22892.00)

    def test0157(self):
        self.assertEquals(self.calculate(151448.0, -37217.0), 188665.00)

    def test0158(self):
        self.assertEquals(self.calculate(138669.0, 161576.0), -22907.00)

    def test0159(self):
        self.assertEquals(self.calculate(-154583.0, 59669.0), -214252.00)

    def test0160(self):
        self.assertEquals(self.calculate(174269.0, 92800.0), 81469.00)

    def test0161(self):
        self.assertEquals(self.calculate(95798.0, -4613.0), 100411.00)

    def test0162(self):
        self.assertEquals(self.calculate(-15326.0, 167083.0), -182409.00)

    def test0163(self):
        self.assertEquals(self.calculate(-179577.0, 181067.0), -360644.00)

    def test0164(self):
        self.assertEquals(self.calculate(-24284.0, 126485.0), -150769.00)

    def test0165(self):
        self.assertEquals(self.calculate(100003.0, 33918.0), 66085.00)

    def test0166(self):
        self.assertEquals(self.calculate(57458.0, -181270.0), 238728.00)

    def test0167(self):
        self.assertEquals(self.calculate(183835.0, -64286.0), 248121.00)

    def test0168(self):
        self.assertEquals(self.calculate(46590.0, 109847.0), -63257.00)

    def test0169(self):
        self.assertEquals(self.calculate(-147320.0, -39835.0), -107485.00)

    def test0170(self):
        self.assertEquals(self.calculate(92904.0, 140193.0), -47289.00)

    def test0171(self):
        self.assertEquals(self.calculate(71880.0, -78744.0), 150624.00)

    def test0172(self):
        self.assertEquals(self.calculate(72892.0, 11953.0), 60939.00)

    def test0173(self):
        self.assertEquals(self.calculate(-18248.0, 67279.0), -85527.00)

    def test0174(self):
        self.assertEquals(self.calculate(102908.0, 54391.0), 48517.00)

    def test0175(self):
        self.assertEquals(self.calculate(25783.0, 146125.0), -120342.00)

    def test0176(self):
        self.assertEquals(self.calculate(118702.0, -139968.0), 258670.00)

    def test0177(self):
        self.assertEquals(self.calculate(87980.0, 8896.0), 79084.00)

    def test0178(self):
        self.assertEquals(self.calculate(-46964.0, 46784.0), -93748.00)

    def test0179(self):
        self.assertEquals(self.calculate(23496.0, -22355.0), 45851.00)

    def test0180(self):
        self.assertEquals(self.calculate(95753.0, 156745.0), -60992.00)

    def test0181(self):
        self.assertEquals(self.calculate(18413.0, 172345.0), -153932.00)

    def test0182(self):
        self.assertEquals(self.calculate(128318.0, -74133.0), 202451.00)

    def test0183(self):
        self.assertEquals(self.calculate(25790.0, 118936.0), -93146.00)

    def test0184(self):
        self.assertEquals(self.calculate(141346.0, 184878.0), -43532.00)

    def test0185(self):
        self.assertEquals(self.calculate(-102974.0, -183215.0), 80241.00)

    def test0186(self):
        self.assertEquals(self.calculate(-62269.0, 105739.0), -168008.00)

    def test0187(self):
        self.assertEquals(self.calculate(14522.0, 170738.0), -156216.00)

    def test0188(self):
        self.assertEquals(self.calculate(89376.0, -174626.0), 264002.00)

    def test0189(self):
        self.assertEquals(self.calculate(-184557.0, -47201.0), -137356.00)

    def test0190(self):
        self.assertEquals(self.calculate(116995.0, -98950.0), 215945.00)

    def test0191(self):
        self.assertEquals(self.calculate(-67566.0, -100364.0), 32798.00)

    def test0192(self):
        self.assertEquals(self.calculate(100248.0, -86177.0), 186425.00)

    def test0193(self):
        self.assertEquals(self.calculate(-41672.0, -60648.0), 18976.00)

    def test0194(self):
        self.assertEquals(self.calculate(-17079.0, -5961.0), -11118.00)

    def test0195(self):
        self.assertEquals(self.calculate(-194551.0, -70038.0), -124513.00)

    def test0196(self):
        self.assertEquals(self.calculate(-119497.0, -192508.0), 73011.00)

    def test0197(self):
        self.assertEquals(self.calculate(-81370.0, 117822.0), -199192.00)

    def test0198(self):
        self.assertEquals(self.calculate(42431.0, -8778.0), 51209.00)

    def test0199(self):
        self.assertEquals(self.calculate(138956.0, 46884.0), 92072.00)

    def test0200(self):
        self.assertEquals(self.calculate(-183564.0, -25089.0), -158475.00)

    def test0201(self):
        self.assertEquals(self.calculate(-56664.0, 13270.0), -69934.00)

    def test0202(self):
        self.assertEquals(self.calculate(129501.0, -186156.0), 315657.00)

    def test0203(self):
        self.assertEquals(self.calculate(29276.0, 88749.0), -59473.00)

    def test0204(self):
        self.assertEquals(self.calculate(-139417.0, -27433.0), -111984.00)

    def test0205(self):
        self.assertEquals(self.calculate(-62282.0, 133710.0), -195992.00)

    def test0206(self):
        self.assertEquals(self.calculate(133615.0, 147647.0), -14032.00)

    def test0207(self):
        self.assertEquals(self.calculate(91197.0, -77918.0), 169115.00)

    def test0208(self):
        self.assertEquals(self.calculate(-198246.0, 197769.0), -396015.00)

    def test0209(self):
        self.assertEquals(self.calculate(146893.0, -47563.0), 194456.00)

    def test0210(self):
        self.assertEquals(self.calculate(-106889.0, -63503.0), -43386.00)

    def test0211(self):
        self.assertEquals(self.calculate(-158958.0, -27700.0), -131258.00)

    def test0212(self):
        self.assertEquals(self.calculate(-88982.0, 17364.0), -106346.00)

    def test0213(self):
        self.assertEquals(self.calculate(125551.0, -4549.0), 130100.00)

    def test0214(self):
        self.assertEquals(self.calculate(-155788.0, -92755.0), -63033.00)

    def test0215(self):
        self.assertEquals(self.calculate(-8423.0, -154343.0), 145920.00)

    def test0216(self):
        self.assertEquals(self.calculate(-12053.0, 66121.0), -78174.00)

    def test0217(self):
        self.assertEquals(self.calculate(117354.0, 168048.0), -50694.00)

    def test0218(self):
        self.assertEquals(self.calculate(40020.0, -173104.0), 213124.00)

    def test0219(self):
        self.assertEquals(self.calculate(37161.0, -118951.0), 156112.00)

    def test0220(self):
        self.assertEquals(self.calculate(-42055.0, 102870.0), -144925.00)

    def test0221(self):
        self.assertEquals(self.calculate(95112.0, -196866.0), 291978.00)

    def test0222(self):
        self.assertEquals(self.calculate(-108032.0, 85407.0), -193439.00)

    def test0223(self):
        self.assertEquals(self.calculate(126708.0, 84620.0), 42088.00)

    def test0224(self):
        self.assertEquals(self.calculate(-176958.0, 89634.0), -266592.00)

    def test0225(self):
        self.assertEquals(self.calculate(87122.0, -139076.0), 226198.00)

    def test0226(self):
        self.assertEquals(self.calculate(-100038.0, -29050.0), -70988.00)

    def test0227(self):
        self.assertEquals(self.calculate(49864.0, 136893.0), -87029.00)

    def test0228(self):
        self.assertEquals(self.calculate(-152170.0, -128358.0), -23812.00)

    def test0229(self):
        self.assertEquals(self.calculate(-118515.0, 7330.0), -125845.00)

    def test0230(self):
        self.assertEquals(self.calculate(-112877.0, -65359.0), -47518.00)

    def test0231(self):
        self.assertEquals(self.calculate(-20028.0, -175370.0), 155342.00)

    def test0232(self):
        self.assertEquals(self.calculate(112563.0, -196497.0), 309060.00)

    def test0233(self):
        self.assertEquals(self.calculate(133052.0, 169854.0), -36802.00)

    def test0234(self):
        self.assertEquals(self.calculate(180319.0, -172252.0), 352571.00)

    def test0235(self):
        self.assertEquals(self.calculate(134531.0, 120523.0), 14008.00)

    def test0236(self):
        self.assertEquals(self.calculate(112923.0, -100152.0), 213075.00)

    def test0237(self):
        self.assertEquals(self.calculate(-44919.0, -61952.0), 17033.00)

    def test0238(self):
        self.assertEquals(self.calculate(65326.0, 178163.0), -112837.00)

    def test0239(self):
        self.assertEquals(self.calculate(-78701.0, 64567.0), -143268.00)

    def test0240(self):
        self.assertEquals(self.calculate(-46906.0, -41938.0), -4968.00)

    def test0241(self):
        self.assertEquals(self.calculate(-69103.0, -99642.0), 30539.00)

    def test0242(self):
        self.assertEquals(self.calculate(61701.0, -180622.0), 242323.00)

    def test0243(self):
        self.assertEquals(self.calculate(70371.0, 128533.0), -58162.00)

    def test0244(self):
        self.assertEquals(self.calculate(47627.0, -48553.0), 96180.00)

    def test0245(self):
        self.assertEquals(self.calculate(-102000.0, 148858.0), -250858.00)

    def test0246(self):
        self.assertEquals(self.calculate(175446.0, 173701.0), 1745.00)

    def test0247(self):
        self.assertEquals(self.calculate(131539.0, -177548.0), 309087.00)

    def test0248(self):
        self.assertEquals(self.calculate(-726.0, 192076.0), -192802.00)

    def test0249(self):
        self.assertEquals(self.calculate(-191041.0, 170288.0), -361329.00)

    def test0250(self):
        self.assertEquals(self.calculate(-125585.0, 146871.0), -272456.00)

    def test0251(self):
        self.assertEquals(self.calculate(-75538.0, 61666.0), -137204.00)

    def test0252(self):
        self.assertEquals(self.calculate(45127.0, -158687.0), 203814.00)

    def test0253(self):
        self.assertEquals(self.calculate(-40758.0, 171057.0), -211815.00)

    def test0254(self):
        self.assertEquals(self.calculate(78853.0, 37625.0), 41228.00)

    def test0255(self):
        self.assertEquals(self.calculate(-145128.0, 72395.0), -217523.00)

    def test0256(self):
        self.assertEquals(self.calculate(-179558.0, 111801.0), -291359.00)

    def test0257(self):
        self.assertEquals(self.calculate(88926.0, -20915.0), 109841.00)

    def test0258(self):
        self.assertEquals(self.calculate(128582.0, -125663.0), 254245.00)

    def test0259(self):
        self.assertEquals(self.calculate(-14194.0, -12845.0), -1349.00)

    def test0260(self):
        self.assertEquals(self.calculate(197374.0, -67848.0), 265222.00)

    def test0261(self):
        self.assertEquals(self.calculate(-198137.0, 181313.0), -379450.00)

    def test0262(self):
        self.assertEquals(self.calculate(-60049.0, 105174.0), -165223.00)

    def test0263(self):
        self.assertEquals(self.calculate(-127748.0, -174262.0), 46514.00)

    def test0264(self):
        self.assertEquals(self.calculate(124410.0, 131017.0), -6607.00)

    def test0265(self):
        self.assertEquals(self.calculate(184040.0, 111550.0), 72490.00)

    def test0266(self):
        self.assertEquals(self.calculate(191889.0, 23174.0), 168715.00)

    def test0267(self):
        self.assertEquals(self.calculate(115951.0, -135112.0), 251063.00)

    def test0268(self):
        self.assertEquals(self.calculate(138897.0, -43163.0), 182060.00)

    def test0269(self):
        self.assertEquals(self.calculate(-34782.0, -150970.0), 116188.00)

    def test0270(self):
        self.assertEquals(self.calculate(-116474.0, 83610.0), -200084.00)

    def test0271(self):
        self.assertEquals(self.calculate(16421.0, -22267.0), 38688.00)

    def test0272(self):
        self.assertEquals(self.calculate(-35201.0, 159559.0), -194760.00)

    def test0273(self):
        self.assertEquals(self.calculate(-199460.0, -191684.0), -7776.00)

    def test0274(self):
        self.assertEquals(self.calculate(195529.0, -199907.0), 395436.00)

    def test0275(self):
        self.assertEquals(self.calculate(190542.0, 142401.0), 48141.00)

    def test0276(self):
        self.assertEquals(self.calculate(120821.0, 25009.0), 95812.00)

    def test0277(self):
        self.assertEquals(self.calculate(-31419.0, 68579.0), -99998.00)

    def test0278(self):
        self.assertEquals(self.calculate(177835.0, -106913.0), 284748.00)

    def test0279(self):
        self.assertEquals(self.calculate(-170871.0, -28267.0), -142604.00)

    def test0280(self):
        self.assertEquals(self.calculate(-152029.0, -164413.0), 12384.00)

    def test0281(self):
        self.assertEquals(self.calculate(-144732.0, -194159.0), 49427.00)

    def test0282(self):
        self.assertEquals(self.calculate(-15248.0, -79748.0), 64500.00)

    def test0283(self):
        self.assertEquals(self.calculate(93267.0, -100889.0), 194156.00)

    def test0284(self):
        self.assertEquals(self.calculate(-8578.0, -147490.0), 138912.00)

    def test0285(self):
        self.assertEquals(self.calculate(-17138.0, -140162.0), 123024.00)

    def test0286(self):
        self.assertEquals(self.calculate(98413.0, 93325.0), 5088.00)

    def test0287(self):
        self.assertEquals(self.calculate(121284.0, 70202.0), 51082.00)

    def test0288(self):
        self.assertEquals(self.calculate(195017.0, -76030.0), 271047.00)

    def test0289(self):
        self.assertEquals(self.calculate(-108727.0, 44582.0), -153309.00)

    def test0290(self):
        self.assertEquals(self.calculate(-143420.0, 173925.0), -317345.00)

    def test0291(self):
        self.assertEquals(self.calculate(131548.0, 96761.0), 34787.00)

    def test0292(self):
        self.assertEquals(self.calculate(113925.0, -84208.0), 198133.00)

    def test0293(self):
        self.assertEquals(self.calculate(-193085.0, -158670.0), -34415.00)

    def test0294(self):
        self.assertEquals(self.calculate(-160918.0, 68092.0), -229010.00)

    def test0295(self):
        self.assertEquals(self.calculate(-58575.0, 57098.0), -115673.00)

    def test0296(self):
        self.assertEquals(self.calculate(-151137.0, -100487.0), -50650.00)

    def test0297(self):
        self.assertEquals(self.calculate(-186159.0, -145741.0), -40418.00)

    def test0298(self):
        self.assertEquals(self.calculate(-164188.0, 38315.0), -202503.00)

    def test0299(self):
        self.assertEquals(self.calculate(166202.0, 153824.0), 12378.00)

    def test0300(self):
        self.assertEquals(self.calculate(-33300.0, -128554.0), 95254.00)

    def test0301(self):
        self.assertEquals(self.calculate(62871.0, -61444.0), 124315.00)

    def test0302(self):
        self.assertEquals(self.calculate(-35754.0, 137522.0), -173276.00)

    def test0303(self):
        self.assertEquals(self.calculate(31511.0, -129086.0), 160597.00)

    def test0304(self):
        self.assertEquals(self.calculate(-183426.0, -128815.0), -54611.00)

    def test0305(self):
        self.assertEquals(self.calculate(-133445.0, 66208.0), -199653.00)

    def test0306(self):
        self.assertEquals(self.calculate(36779.0, 80542.0), -43763.00)

    def test0307(self):
        self.assertEquals(self.calculate(62802.0, -126152.0), 188954.00)

    def test0308(self):
        self.assertEquals(self.calculate(175715.0, 167370.0), 8345.00)

    def test0309(self):
        self.assertEquals(self.calculate(-109048.0, -105811.0), -3237.00)

    def test0310(self):
        self.assertEquals(self.calculate(13616.0, 1786.0), 11830.00)

    def test0311(self):
        self.assertEquals(self.calculate(128419.0, -31247.0), 159666.00)

    def test0312(self):
        self.assertEquals(self.calculate(141109.0, 35851.0), 105258.00)

    def test0313(self):
        self.assertEquals(self.calculate(78741.0, -67169.0), 145910.00)

    def test0314(self):
        self.assertEquals(self.calculate(184950.0, 72614.0), 112336.00)

    def test0315(self):
        self.assertEquals(self.calculate(-150104.0, -157174.0), 7070.00)

    def test0316(self):
        self.assertEquals(self.calculate(-144359.0, 193909.0), -338268.00)

    def test0317(self):
        self.assertEquals(self.calculate(-170084.0, -33378.0), -136706.00)

    def test0318(self):
        self.assertEquals(self.calculate(156072.0, 31999.0), 124073.00)

    def test0319(self):
        self.assertEquals(self.calculate(-143081.0, -28784.0), -114297.00)

    def test0320(self):
        self.assertEquals(self.calculate(130352.0, 107782.0), 22570.00)

    def test0321(self):
        self.assertEquals(self.calculate(184954.0, -118224.0), 303178.00)

    def test0322(self):
        self.assertEquals(self.calculate(117793.0, -120170.0), 237963.00)

    def test0323(self):
        self.assertEquals(self.calculate(151784.0, 161855.0), -10071.00)

    def test0324(self):
        self.assertEquals(self.calculate(-145267.0, 129661.0), -274928.00)

    def test0325(self):
        self.assertEquals(self.calculate(168658.0, -41024.0), 209682.00)

    def test0326(self):
        self.assertEquals(self.calculate(-47963.0, -68117.0), 20154.00)

    def test0327(self):
        self.assertEquals(self.calculate(10286.0, 73484.0), -63198.00)

    def test0328(self):
        self.assertEquals(self.calculate(-22225.0, -110852.0), 88627.00)

    def test0329(self):
        self.assertEquals(self.calculate(30254.0, -74431.0), 104685.00)

    def test0330(self):
        self.assertEquals(self.calculate(122413.0, -10195.0), 132608.00)

    def test0331(self):
        self.assertEquals(self.calculate(67627.0, -80441.0), 148068.00)

    def test0332(self):
        self.assertEquals(self.calculate(-128714.0, 90647.0), -219361.00)

    def test0333(self):
        self.assertEquals(self.calculate(-187121.0, 34276.0), -221397.00)

    def test0334(self):
        self.assertEquals(self.calculate(57503.0, -48695.0), 106198.00)

    def test0335(self):
        self.assertEquals(self.calculate(164372.0, -8082.0), 172454.00)

    def test0336(self):
        self.assertEquals(self.calculate(-178662.0, -87669.0), -90993.00)

    def test0337(self):
        self.assertEquals(self.calculate(-168645.0, -181758.0), 13113.00)

    def test0338(self):
        self.assertEquals(self.calculate(118138.0, -170948.0), 289086.00)

    def test0339(self):
        self.assertEquals(self.calculate(-15758.0, -162618.0), 146860.00)

    def test0340(self):
        self.assertEquals(self.calculate(-118373.0, -133827.0), 15454.00)

    def test0341(self):
        self.assertEquals(self.calculate(-175285.0, -68937.0), -106348.00)

    def test0342(self):
        self.assertEquals(self.calculate(40766.0, 36223.0), 4543.00)

    def test0343(self):
        self.assertEquals(self.calculate(59663.0, 6204.0), 53459.00)

    def test0344(self):
        self.assertEquals(self.calculate(67377.0, 144048.0), -76671.00)

    def test0345(self):
        self.assertEquals(self.calculate(92051.0, -164557.0), 256608.00)

    def test0346(self):
        self.assertEquals(self.calculate(-177706.0, 52658.0), -230364.00)

    def test0347(self):
        self.assertEquals(self.calculate(-112063.0, -199178.0), 87115.00)

    def test0348(self):
        self.assertEquals(self.calculate(152949.0, -105212.0), 258161.00)

    def test0349(self):
        self.assertEquals(self.calculate(-4475.0, 158104.0), -162579.00)

    def test0350(self):
        self.assertEquals(self.calculate(-192699.0, -109649.0), -83050.00)

    def test0351(self):
        self.assertEquals(self.calculate(98321.0, 110420.0), -12099.00)

    def test0352(self):
        self.assertEquals(self.calculate(-184271.0, 159472.0), -343743.00)

    def test0353(self):
        self.assertEquals(self.calculate(163051.0, -37915.0), 200966.00)

    def test0354(self):
        self.assertEquals(self.calculate(64507.0, 98628.0), -34121.00)

    def test0355(self):
        self.assertEquals(self.calculate(112526.0, 186482.0), -73956.00)

    def test0356(self):
        self.assertEquals(self.calculate(-172590.0, -160062.0), -12528.00)

    def test0357(self):
        self.assertEquals(self.calculate(-92065.0, 124209.0), -216274.00)

    def test0358(self):
        self.assertEquals(self.calculate(-199314.0, 645.0), -199959.00)

    def test0359(self):
        self.assertEquals(self.calculate(15362.0, 96648.0), -81286.00)

    def test0360(self):
        self.assertEquals(self.calculate(66027.0, -116726.0), 182753.00)

    def test0361(self):
        self.assertEquals(self.calculate(-78447.0, 21954.0), -100401.00)

    def test0362(self):
        self.assertEquals(self.calculate(-46952.0, -190370.0), 143418.00)

    def test0363(self):
        self.assertEquals(self.calculate(18338.0, 137154.0), -118816.00)

    def test0364(self):
        self.assertEquals(self.calculate(-15409.0, -154018.0), 138609.00)

    def test0365(self):
        self.assertEquals(self.calculate(-123000.0, 181198.0), -304198.00)

    def test0366(self):
        self.assertEquals(self.calculate(134073.0, -177369.0), 311442.00)

    def test0367(self):
        self.assertEquals(self.calculate(87863.0, -75875.0), 163738.00)

    def test0368(self):
        self.assertEquals(self.calculate(1889.0, -57075.0), 58964.00)

    def test0369(self):
        self.assertEquals(self.calculate(-116301.0, 85201.0), -201502.00)

    def test0370(self):
        self.assertEquals(self.calculate(-134369.0, -72233.0), -62136.00)

    def test0371(self):
        self.assertEquals(self.calculate(-82058.0, -158180.0), 76122.00)

    def test0372(self):
        self.assertEquals(self.calculate(-34143.0, -137816.0), 103673.00)

    def test0373(self):
        self.assertEquals(self.calculate(-34917.0, -9368.0), -25549.00)

    def test0374(self):
        self.assertEquals(self.calculate(-52719.0, -37391.0), -15328.00)

    def test0375(self):
        self.assertEquals(self.calculate(96862.0, -111867.0), 208729.00)

    def test0376(self):
        self.assertEquals(self.calculate(30544.0, -21721.0), 52265.00)

    def test0377(self):
        self.assertEquals(self.calculate(-55337.0, 113540.0), -168877.00)

    def test0378(self):
        self.assertEquals(self.calculate(146364.0, 143660.0), 2704.00)

    def test0379(self):
        self.assertEquals(self.calculate(46683.0, 77751.0), -31068.00)

    def test0380(self):
        self.assertEquals(self.calculate(-195737.0, 49540.0), -245277.00)

    def test0381(self):
        self.assertEquals(self.calculate(48322.0, 20806.0), 27516.00)

    def test0382(self):
        self.assertEquals(self.calculate(-166051.0, 58570.0), -224621.00)

    def test0383(self):
        self.assertEquals(self.calculate(-17242.0, 162517.0), -179759.00)

    def test0384(self):
        self.assertEquals(self.calculate(185400.0, -23261.0), 208661.00)

    def test0385(self):
        self.assertEquals(self.calculate(59389.0, -63207.0), 122596.00)

    def test0386(self):
        self.assertEquals(self.calculate(1780.0, 22258.0), -20478.00)

    def test0387(self):
        self.assertEquals(self.calculate(-175056.0, 156644.0), -331700.00)

    def test0388(self):
        self.assertEquals(self.calculate(-193470.0, -90370.0), -103100.00)

    def test0389(self):
        self.assertEquals(self.calculate(52437.0, -103092.0), 155529.00)

    def test0390(self):
        self.assertEquals(self.calculate(33349.0, -53880.0), 87229.00)

    def test0391(self):
        self.assertEquals(self.calculate(193993.0, -49336.0), 243329.00)

    def test0392(self):
        self.assertEquals(self.calculate(185363.0, 72243.0), 113120.00)

    def test0393(self):
        self.assertEquals(self.calculate(117208.0, -17322.0), 134530.00)

    def test0394(self):
        self.assertEquals(self.calculate(-16682.0, 95582.0), -112264.00)

    def test0395(self):
        self.assertEquals(self.calculate(-96101.0, 95172.0), -191273.00)

    def test0396(self):
        self.assertEquals(self.calculate(-153901.0, -80445.0), -73456.00)

    def test0397(self):
        self.assertEquals(self.calculate(35096.0, -39628.0), 74724.00)

    def test0398(self):
        self.assertEquals(self.calculate(28264.0, -192870.0), 221134.00)

    def test0399(self):
        self.assertEquals(self.calculate(91066.0, -36280.0), 127346.00)

    def test0400(self):
        self.assertEquals(self.calculate(154006.0, -4913.0), 158919.00)

    def test0401(self):
        self.assertEquals(self.calculate(-185323.0, 94259.0), -279582.00)

    def test0402(self):
        self.assertEquals(self.calculate(-43987.0, 8826.0), -52813.00)

    def test0403(self):
        self.assertEquals(self.calculate(53151.0, -118091.0), 171242.00)

    def test0404(self):
        self.assertEquals(self.calculate(-48068.0, 92073.0), -140141.00)

    def test0405(self):
        self.assertEquals(self.calculate(172639.0, 155380.0), 17259.00)

    def test0406(self):
        self.assertEquals(self.calculate(33891.0, 59392.0), -25501.00)

    def test0407(self):
        self.assertEquals(self.calculate(62054.0, 106892.0), -44838.00)

    def test0408(self):
        self.assertEquals(self.calculate(190659.0, -67056.0), 257715.00)

    def test0409(self):
        self.assertEquals(self.calculate(-181401.0, 199532.0), -380933.00)

    def test0410(self):
        self.assertEquals(self.calculate(126421.0, -93538.0), 219959.00)

    def test0411(self):
        self.assertEquals(self.calculate(78064.0, -165998.0), 244062.00)

    def test0412(self):
        self.assertEquals(self.calculate(-199974.0, -17839.0), -182135.00)

    def test0413(self):
        self.assertEquals(self.calculate(-35903.0, 71778.0), -107681.00)

    def test0414(self):
        self.assertEquals(self.calculate(56086.0, 4006.0), 52080.00)

    def test0415(self):
        self.assertEquals(self.calculate(61194.0, -115414.0), 176608.00)

    def test0416(self):
        self.assertEquals(self.calculate(121399.0, -166087.0), 287486.00)

    def test0417(self):
        self.assertEquals(self.calculate(165551.0, -121482.0), 287033.00)

    def test0418(self):
        self.assertEquals(self.calculate(51529.0, -59117.0), 110646.00)

    def test0419(self):
        self.assertEquals(self.calculate(114351.0, -90021.0), 204372.00)

    def test0420(self):
        self.assertEquals(self.calculate(167592.0, -99392.0), 266984.00)

    def test0421(self):
        self.assertEquals(self.calculate(-64682.0, 96485.0), -161167.00)

    def test0422(self):
        self.assertEquals(self.calculate(68288.0, 95306.0), -27018.00)

    def test0423(self):
        self.assertEquals(self.calculate(123450.0, -145835.0), 269285.00)

    def test0424(self):
        self.assertEquals(self.calculate(147377.0, -142096.0), 289473.00)

    def test0425(self):
        self.assertEquals(self.calculate(119937.0, -59393.0), 179330.00)

    def test0426(self):
        self.assertEquals(self.calculate(-107993.0, 129221.0), -237214.00)

    def test0427(self):
        self.assertEquals(self.calculate(114813.0, -64607.0), 179420.00)

    def test0428(self):
        self.assertEquals(self.calculate(146307.0, 81178.0), 65129.00)

    def test0429(self):
        self.assertEquals(self.calculate(41306.0, 178914.0), -137608.00)

    def test0430(self):
        self.assertEquals(self.calculate(178535.0, -169271.0), 347806.00)

    def test0431(self):
        self.assertEquals(self.calculate(125950.0, 14034.0), 111916.00)

    def test0432(self):
        self.assertEquals(self.calculate(-142150.0, 150832.0), -292982.00)

    def test0433(self):
        self.assertEquals(self.calculate(140301.0, -38210.0), 178511.00)

    def test0434(self):
        self.assertEquals(self.calculate(-98066.0, 69173.0), -167239.00)

    def test0435(self):
        self.assertEquals(self.calculate(30627.0, -198582.0), 229209.00)

    def test0436(self):
        self.assertEquals(self.calculate(58489.0, -72301.0), 130790.00)

    def test0437(self):
        self.assertEquals(self.calculate(-194870.0, -133833.0), -61037.00)

    def test0438(self):
        self.assertEquals(self.calculate(-108030.0, -143072.0), 35042.00)

    def test0439(self):
        self.assertEquals(self.calculate(107004.0, -190906.0), 297910.00)

    def test0440(self):
        self.assertEquals(self.calculate(-53619.0, -109099.0), 55480.00)

    def test0441(self):
        self.assertEquals(self.calculate(-1807.0, -44372.0), 42565.00)

    def test0442(self):
        self.assertEquals(self.calculate(-81381.0, -115545.0), 34164.00)

    def test0443(self):
        self.assertEquals(self.calculate(-79657.0, -179293.0), 99636.00)

    def test0444(self):
        self.assertEquals(self.calculate(94524.0, 175781.0), -81257.00)

    def test0445(self):
        self.assertEquals(self.calculate(124368.0, 125378.0), -1010.00)

    def test0446(self):
        self.assertEquals(self.calculate(-85927.0, 145096.0), -231023.00)

    def test0447(self):
        self.assertEquals(self.calculate(174975.0, 115263.0), 59712.00)

    def test0448(self):
        self.assertEquals(self.calculate(-13170.0, 123131.0), -136301.00)

    def test0449(self):
        self.assertEquals(self.calculate(-691.0, 148806.0), -149497.00)

    def test0450(self):
        self.assertEquals(self.calculate(-178301.0, -107047.0), -71254.00)

    def test0451(self):
        self.assertEquals(self.calculate(-174643.0, -169254.0), -5389.00)

    def test0452(self):
        self.assertEquals(self.calculate(-134226.0, 20597.0), -154823.00)

    def test0453(self):
        self.assertEquals(self.calculate(181080.0, 11498.0), 169582.00)

    def test0454(self):
        self.assertEquals(self.calculate(-9212.0, 84430.0), -93642.00)

    def test0455(self):
        self.assertEquals(self.calculate(-145443.0, 2736.0), -148179.00)

    def test0456(self):
        self.assertEquals(self.calculate(-169538.0, -6632.0), -162906.00)

    def test0457(self):
        self.assertEquals(self.calculate(-172590.0, -75082.0), -97508.00)

    def test0458(self):
        self.assertEquals(self.calculate(154634.0, -23188.0), 177822.00)

    def test0459(self):
        self.assertEquals(self.calculate(-77258.0, 121797.0), -199055.00)

    def test0460(self):
        self.assertEquals(self.calculate(-165831.0, 95631.0), -261462.00)

    def test0461(self):
        self.assertEquals(self.calculate(-90130.0, -118055.0), 27925.00)

    def test0462(self):
        self.assertEquals(self.calculate(136247.0, 134222.0), 2025.00)

    def test0463(self):
        self.assertEquals(self.calculate(-192157.0, 64534.0), -256691.00)

    def test0464(self):
        self.assertEquals(self.calculate(180023.0, -40103.0), 220126.00)

    def test0465(self):
        self.assertEquals(self.calculate(-5148.0, -176503.0), 171355.00)

    def test0466(self):
        self.assertEquals(self.calculate(120190.0, 160739.0), -40549.00)

    def test0467(self):
        self.assertEquals(self.calculate(116162.0, -87402.0), 203564.00)

    def test0468(self):
        self.assertEquals(self.calculate(57624.0, 123425.0), -65801.00)

    def test0469(self):
        self.assertEquals(self.calculate(14969.0, 122422.0), -107453.00)

    def test0470(self):
        self.assertEquals(self.calculate(38967.0, -107532.0), 146499.00)

    def test0471(self):
        self.assertEquals(self.calculate(73841.0, -135434.0), 209275.00)

    def test0472(self):
        self.assertEquals(self.calculate(142253.0, -196331.0), 338584.00)

    def test0473(self):
        self.assertEquals(self.calculate(-3631.0, 181120.0), -184751.00)

    def test0474(self):
        self.assertEquals(self.calculate(184680.0, 13146.0), 171534.00)

    def test0475(self):
        self.assertEquals(self.calculate(7069.0, 9804.0), -2735.00)

    def test0476(self):
        self.assertEquals(self.calculate(-162392.0, -160630.0), -1762.00)

    def test0477(self):
        self.assertEquals(self.calculate(-122176.0, -109507.0), -12669.00)

    def test0478(self):
        self.assertEquals(self.calculate(-63508.0, 120985.0), -184493.00)

    def test0479(self):
        self.assertEquals(self.calculate(-73695.0, 180369.0), -254064.00)

    def test0480(self):
        self.assertEquals(self.calculate(27407.0, -16060.0), 43467.00)

    def test0481(self):
        self.assertEquals(self.calculate(106787.0, 171623.0), -64836.00)

    def test0482(self):
        self.assertEquals(self.calculate(-50035.0, -189640.0), 139605.00)

    def test0483(self):
        self.assertEquals(self.calculate(-181499.0, 64436.0), -245935.00)

    def test0484(self):
        self.assertEquals(self.calculate(14822.0, -38087.0), 52909.00)

    def test0485(self):
        self.assertEquals(self.calculate(-135163.0, -101919.0), -33244.00)

    def test0486(self):
        self.assertEquals(self.calculate(-128642.0, 47092.0), -175734.00)

    def test0487(self):
        self.assertEquals(self.calculate(115645.0, 45570.0), 70075.00)

    def test0488(self):
        self.assertEquals(self.calculate(25297.0, 191041.0), -165744.00)

    def test0489(self):
        self.assertEquals(self.calculate(21301.0, -143024.0), 164325.00)

    def test0490(self):
        self.assertEquals(self.calculate(66416.0, -106708.0), 173124.00)

    def test0491(self):
        self.assertEquals(self.calculate(30334.0, -36985.0), 67319.00)

    def test0492(self):
        self.assertEquals(self.calculate(-105576.0, -139288.0), 33712.00)

    def test0493(self):
        self.assertEquals(self.calculate(-158532.0, -195334.0), 36802.00)

    def test0494(self):
        self.assertEquals(self.calculate(-188385.0, -28862.0), -159523.00)

    def test0495(self):
        self.assertEquals(self.calculate(-60401.0, 40916.0), -101317.00)

    def test0496(self):
        self.assertEquals(self.calculate(108263.0, -39025.0), 147288.00)

    def test0497(self):
        self.assertEquals(self.calculate(-81797.0, -129758.0), 47961.00)

    def test0498(self):
        self.assertEquals(self.calculate(-76668.0, -93280.0), 16612.00)

    def test0499(self):
        self.assertEquals(self.calculate(12577.0, 46569.0), -33992.00)

    def test0500(self):
        self.assertEquals(self.calculate(64618.0, -123972.0), 188590.00)

    def test0501(self):
        self.assertEquals(self.calculate(60703.0, -85398.0), 146101.00)

    def test0502(self):
        self.assertEquals(self.calculate(162667.0, -198804.0), 361471.00)

    def test0503(self):
        self.assertEquals(self.calculate(-165987.0, 31822.0), -197809.00)

    def test0504(self):
        self.assertEquals(self.calculate(-168258.0, 183285.0), -351543.00)

    def test0505(self):
        self.assertEquals(self.calculate(190953.0, 153423.0), 37530.00)

    def test0506(self):
        self.assertEquals(self.calculate(19406.0, 179421.0), -160015.00)

    def test0507(self):
        self.assertEquals(self.calculate(-189639.0, 178716.0), -368355.00)

    def test0508(self):
        self.assertEquals(self.calculate(61058.0, -32204.0), 93262.00)

    def test0509(self):
        self.assertEquals(self.calculate(-26478.0, 42980.0), -69458.00)

    def test0510(self):
        self.assertEquals(self.calculate(178719.0, -161057.0), 339776.00)

    def test0511(self):
        self.assertEquals(self.calculate(72644.0, 160299.0), -87655.00)

    def test0512(self):
        self.assertEquals(self.calculate(179919.0, -109733.0), 289652.00)

    def test0513(self):
        self.assertEquals(self.calculate(76285.0, 131997.0), -55712.00)

    def test0514(self):
        self.assertEquals(self.calculate(144288.0, 45395.0), 98893.00)

    def test0515(self):
        self.assertEquals(self.calculate(190650.0, 127170.0), 63480.00)

    def test0516(self):
        self.assertEquals(self.calculate(-150582.0, 158298.0), -308880.00)

    def test0517(self):
        self.assertEquals(self.calculate(-41576.0, -119210.0), 77634.00)

    def test0518(self):
        self.assertEquals(self.calculate(13743.0, -87426.0), 101169.00)

    def test0519(self):
        self.assertEquals(self.calculate(-127299.0, -53308.0), -73991.00)

    def test0520(self):
        self.assertEquals(self.calculate(-79983.0, 68953.0), -148936.00)

    def test0521(self):
        self.assertEquals(self.calculate(-34738.0, 165999.0), -200737.00)

    def test0522(self):
        self.assertEquals(self.calculate(10698.0, 156789.0), -146091.00)

    def test0523(self):
        self.assertEquals(self.calculate(-115309.0, 90425.0), -205734.00)

    def test0524(self):
        self.assertEquals(self.calculate(55533.0, -85513.0), 141046.00)

    def test0525(self):
        self.assertEquals(self.calculate(-160703.0, 1973.0), -162676.00)

    def test0526(self):
        self.assertEquals(self.calculate(184955.0, -147566.0), 332521.00)

    def test0527(self):
        self.assertEquals(self.calculate(-88629.0, -185664.0), 97035.00)

    def test0528(self):
        self.assertEquals(self.calculate(-92758.0, 75591.0), -168349.00)

    def test0529(self):
        self.assertEquals(self.calculate(187696.0, 138015.0), 49681.00)

    def test0530(self):
        self.assertEquals(self.calculate(124271.0, 45022.0), 79249.00)

    def test0531(self):
        self.assertEquals(self.calculate(-20185.0, 12323.0), -32508.00)

    def test0532(self):
        self.assertEquals(self.calculate(176890.0, -30108.0), 206998.00)

    def test0533(self):
        self.assertEquals(self.calculate(-164365.0, 184986.0), -349351.00)

    def test0534(self):
        self.assertEquals(self.calculate(-3267.0, 140064.0), -143331.00)

    def test0535(self):
        self.assertEquals(self.calculate(-152614.0, 39989.0), -192603.00)

    def test0536(self):
        self.assertEquals(self.calculate(50500.0, -101230.0), 151730.00)

    def test0537(self):
        self.assertEquals(self.calculate(-118622.0, -182340.0), 63718.00)

    def test0538(self):
        self.assertEquals(self.calculate(-159941.0, 42412.0), -202353.00)

    def test0539(self):
        self.assertEquals(self.calculate(-64580.0, -98869.0), 34289.00)

    def test0540(self):
        self.assertEquals(self.calculate(169332.0, -132417.0), 301749.00)

    def test0541(self):
        self.assertEquals(self.calculate(-161581.0, 134388.0), -295969.00)

    def test0542(self):
        self.assertEquals(self.calculate(23097.0, -191596.0), 214693.00)

    def test0543(self):
        self.assertEquals(self.calculate(187206.0, -145257.0), 332463.00)

    def test0544(self):
        self.assertEquals(self.calculate(-46408.0, -18980.0), -27428.00)

    def test0545(self):
        self.assertEquals(self.calculate(-143374.0, 29442.0), -172816.00)

    def test0546(self):
        self.assertEquals(self.calculate(-169495.0, -86903.0), -82592.00)

    def test0547(self):
        self.assertEquals(self.calculate(17368.0, 193946.0), -176578.00)

    def test0548(self):
        self.assertEquals(self.calculate(-105134.0, -177550.0), 72416.00)

    def test0549(self):
        self.assertEquals(self.calculate(165767.0, 60677.0), 105090.00)

    def test0550(self):
        self.assertEquals(self.calculate(148740.0, 162198.0), -13458.00)

    def test0551(self):
        self.assertEquals(self.calculate(117412.0, -176719.0), 294131.00)

    def test0552(self):
        self.assertEquals(self.calculate(71758.0, 196877.0), -125119.00)

    def test0553(self):
        self.assertEquals(self.calculate(-112079.0, 149133.0), -261212.00)

    def test0554(self):
        self.assertEquals(self.calculate(-195926.0, -105375.0), -90551.00)

    def test0555(self):
        self.assertEquals(self.calculate(-29488.0, 132581.0), -162069.00)

    def test0556(self):
        self.assertEquals(self.calculate(-37776.0, -3559.0), -34217.00)

    def test0557(self):
        self.assertEquals(self.calculate(-24453.0, -12510.0), -11943.00)

    def test0558(self):
        self.assertEquals(self.calculate(-135917.0, 179911.0), -315828.00)

    def test0559(self):
        self.assertEquals(self.calculate(29858.0, 190381.0), -160523.00)

    def test0560(self):
        self.assertEquals(self.calculate(-132332.0, 71014.0), -203346.00)

    def test0561(self):
        self.assertEquals(self.calculate(-174576.0, 266.0), -174842.00)

    def test0562(self):
        self.assertEquals(self.calculate(-147860.0, -121361.0), -26499.00)

    def test0563(self):
        self.assertEquals(self.calculate(11103.0, 72105.0), -61002.00)

    def test0564(self):
        self.assertEquals(self.calculate(-51419.0, -168864.0), 117445.00)

    def test0565(self):
        self.assertEquals(self.calculate(-56370.0, -70968.0), 14598.00)

    def test0566(self):
        self.assertEquals(self.calculate(-41605.0, 152317.0), -193922.00)

    def test0567(self):
        self.assertEquals(self.calculate(-176802.0, -175864.0), -938.00)

    def test0568(self):
        self.assertEquals(self.calculate(129978.0, 80767.0), 49211.00)

    def test0569(self):
        self.assertEquals(self.calculate(-38742.0, -95409.0), 56667.00)

    def test0570(self):
        self.assertEquals(self.calculate(-32056.0, 112571.0), -144627.00)

    def test0571(self):
        self.assertEquals(self.calculate(-78285.0, 7462.0), -85747.00)

    def test0572(self):
        self.assertEquals(self.calculate(51838.0, -93783.0), 145621.00)

    def test0573(self):
        self.assertEquals(self.calculate(-72734.0, -198284.0), 125550.00)

    def test0574(self):
        self.assertEquals(self.calculate(55476.0, -195248.0), 250724.00)

    def test0575(self):
        self.assertEquals(self.calculate(-157146.0, -111096.0), -46050.00)

    def test0576(self):
        self.assertEquals(self.calculate(154121.0, 9278.0), 144843.00)

    def test0577(self):
        self.assertEquals(self.calculate(-117982.0, 148595.0), -266577.00)

    def test0578(self):
        self.assertEquals(self.calculate(-164090.0, 142931.0), -307021.00)

    def test0579(self):
        self.assertEquals(self.calculate(131509.0, -150108.0), 281617.00)

    def test0580(self):
        self.assertEquals(self.calculate(163850.0, -33735.0), 197585.00)

    def test0581(self):
        self.assertEquals(self.calculate(-52242.0, 42039.0), -94281.00)

    def test0582(self):
        self.assertEquals(self.calculate(66886.0, 180731.0), -113845.00)

    def test0583(self):
        self.assertEquals(self.calculate(-92987.0, -112534.0), 19547.00)

    def test0584(self):
        self.assertEquals(self.calculate(23551.0, 145526.0), -121975.00)

    def test0585(self):
        self.assertEquals(self.calculate(-101769.0, 93161.0), -194930.00)

    def test0586(self):
        self.assertEquals(self.calculate(-10900.0, 171282.0), -182182.00)

    def test0587(self):
        self.assertEquals(self.calculate(-92738.0, -155967.0), 63229.00)

    def test0588(self):
        self.assertEquals(self.calculate(-115280.0, -80261.0), -35019.00)

    def test0589(self):
        self.assertEquals(self.calculate(-113931.0, 91227.0), -205158.00)

    def test0590(self):
        self.assertEquals(self.calculate(20936.0, 132850.0), -111914.00)

    def test0591(self):
        self.assertEquals(self.calculate(124398.0, -72335.0), 196733.00)

    def test0592(self):
        self.assertEquals(self.calculate(78684.0, 196260.0), -117576.00)

    def test0593(self):
        self.assertEquals(self.calculate(171631.0, 147285.0), 24346.00)

    def test0594(self):
        self.assertEquals(self.calculate(96371.0, 130742.0), -34371.00)

    def test0595(self):
        self.assertEquals(self.calculate(-146750.0, 181802.0), -328552.00)

    def test0596(self):
        self.assertEquals(self.calculate(-129876.0, -195183.0), 65307.00)

    def test0597(self):
        self.assertEquals(self.calculate(125918.0, -33344.0), 159262.00)

    def test0598(self):
        self.assertEquals(self.calculate(-10173.0, -92943.0), 82770.00)

    def test0599(self):
        self.assertEquals(self.calculate(-176658.0, -112184.0), -64474.00)

    def test0600(self):
        self.assertEquals(self.calculate(182219.0, -61994.0), 244213.00)

    def test0601(self):
        self.assertEquals(self.calculate(-125374.0, 8596.0), -133970.00)

    def test0602(self):
        self.assertEquals(self.calculate(179577.0, -38945.0), 218522.00)

    def test0603(self):
        self.assertEquals(self.calculate(-72821.0, -12497.0), -60324.00)

    def test0604(self):
        self.assertEquals(self.calculate(-89249.0, -97593.0), 8344.00)

    def test0605(self):
        self.assertEquals(self.calculate(-60045.0, 38486.0), -98531.00)

    def test0606(self):
        self.assertEquals(self.calculate(-116957.0, 34495.0), -151452.00)

    def test0607(self):
        self.assertEquals(self.calculate(8423.0, 168464.0), -160041.00)

    def test0608(self):
        self.assertEquals(self.calculate(-152347.0, 84008.0), -236355.00)

    def test0609(self):
        self.assertEquals(self.calculate(163983.0, 148563.0), 15420.00)

    def test0610(self):
        self.assertEquals(self.calculate(40739.0, 26762.0), 13977.00)

    def test0611(self):
        self.assertEquals(self.calculate(-91268.0, 101767.0), -193035.00)

    def test0612(self):
        self.assertEquals(self.calculate(-97108.0, 33043.0), -130151.00)

    def test0613(self):
        self.assertEquals(self.calculate(-49043.0, -193955.0), 144912.00)

    def test0614(self):
        self.assertEquals(self.calculate(77575.0, 67242.0), 10333.00)

    def test0615(self):
        self.assertEquals(self.calculate(-196893.0, -80526.0), -116367.00)

    def test0616(self):
        self.assertEquals(self.calculate(-68430.0, -44812.0), -23618.00)

    def test0617(self):
        self.assertEquals(self.calculate(173982.0, -117844.0), 291826.00)

    def test0618(self):
        self.assertEquals(self.calculate(64863.0, 74091.0), -9228.00)

    def test0619(self):
        self.assertEquals(self.calculate(73825.0, 199767.0), -125942.00)

    def test0620(self):
        self.assertEquals(self.calculate(-53737.0, 81160.0), -134897.00)

    def test0621(self):
        self.assertEquals(self.calculate(-2113.0, -23093.0), 20980.00)

    def test0622(self):
        self.assertEquals(self.calculate(187513.0, -95940.0), 283453.00)

    def test0623(self):
        self.assertEquals(self.calculate(-133404.0, 31911.0), -165315.00)

    def test0624(self):
        self.assertEquals(self.calculate(-68364.0, -119012.0), 50648.00)

    def test0625(self):
        self.assertEquals(self.calculate(-173715.0, -195347.0), 21632.00)

    def test0626(self):
        self.assertEquals(self.calculate(-112165.0, -27672.0), -84493.00)

    def test0627(self):
        self.assertEquals(self.calculate(-122555.0, 122921.0), -245476.00)

    def test0628(self):
        self.assertEquals(self.calculate(153017.0, -135894.0), 288911.00)

    def test0629(self):
        self.assertEquals(self.calculate(2143.0, -188594.0), 190737.00)

    def test0630(self):
        self.assertEquals(self.calculate(153545.0, -57560.0), 211105.00)

    def test0631(self):
        self.assertEquals(self.calculate(157896.0, 31193.0), 126703.00)

    def test0632(self):
        self.assertEquals(self.calculate(-95344.0, 97591.0), -192935.00)

    def test0633(self):
        self.assertEquals(self.calculate(-155714.0, 168002.0), -323716.00)

    def test0634(self):
        self.assertEquals(self.calculate(-135607.0, 58266.0), -193873.00)

    def test0635(self):
        self.assertEquals(self.calculate(90639.0, 149008.0), -58369.00)

    def test0636(self):
        self.assertEquals(self.calculate(103627.0, -91742.0), 195369.00)

    def test0637(self):
        self.assertEquals(self.calculate(-54796.0, -164739.0), 109943.00)

    def test0638(self):
        self.assertEquals(self.calculate(6411.0, 168598.0), -162187.00)

    def test0639(self):
        self.assertEquals(self.calculate(-46176.0, 17499.0), -63675.00)

    def test0640(self):
        self.assertEquals(self.calculate(63548.0, -124405.0), 187953.00)

    def test0641(self):
        self.assertEquals(self.calculate(-68986.0, -102234.0), 33248.00)

    def test0642(self):
        self.assertEquals(self.calculate(89669.0, -106061.0), 195730.00)

    def test0643(self):
        self.assertEquals(self.calculate(-102230.0, -39169.0), -63061.00)

    def test0644(self):
        self.assertEquals(self.calculate(-11654.0, 52090.0), -63744.00)

    def test0645(self):
        self.assertEquals(self.calculate(-2985.0, 3581.0), -6566.00)

    def test0646(self):
        self.assertEquals(self.calculate(-123862.0, 150735.0), -274597.00)

    def test0647(self):
        self.assertEquals(self.calculate(190893.0, -20974.0), 211867.00)

    def test0648(self):
        self.assertEquals(self.calculate(161884.0, -150655.0), 312539.00)

    def test0649(self):
        self.assertEquals(self.calculate(67930.0, -14860.0), 82790.00)

    def test0650(self):
        self.assertEquals(self.calculate(-141546.0, 59621.0), -201167.00)

    def test0651(self):
        self.assertEquals(self.calculate(-171128.0, -15594.0), -155534.00)

    def test0652(self):
        self.assertEquals(self.calculate(-179527.0, 33458.0), -212985.00)

    def test0653(self):
        self.assertEquals(self.calculate(60862.0, -109069.0), 169931.00)

    def test0654(self):
        self.assertEquals(self.calculate(-129455.0, -127336.0), -2119.00)

    def test0655(self):
        self.assertEquals(self.calculate(-74213.0, 8623.0), -82836.00)

    def test0656(self):
        self.assertEquals(self.calculate(-155939.0, 128706.0), -284645.00)

    def test0657(self):
        self.assertEquals(self.calculate(-177347.0, 16358.0), -193705.00)

    def test0658(self):
        self.assertEquals(self.calculate(152041.0, 79536.0), 72505.00)

    def test0659(self):
        self.assertEquals(self.calculate(177833.0, -49870.0), 227703.00)

    def test0660(self):
        self.assertEquals(self.calculate(-198215.0, -38089.0), -160126.00)

    def test0661(self):
        self.assertEquals(self.calculate(-157513.0, -13632.0), -143881.00)

    def test0662(self):
        self.assertEquals(self.calculate(-59165.0, -113372.0), 54207.00)

    def test0663(self):
        self.assertEquals(self.calculate(157604.0, -118750.0), 276354.00)

    def test0664(self):
        self.assertEquals(self.calculate(-54094.0, -140749.0), 86655.00)

    def test0665(self):
        self.assertEquals(self.calculate(-16396.0, -183436.0), 167040.00)

    def test0666(self):
        self.assertEquals(self.calculate(164017.0, -198096.0), 362113.00)

    def test0667(self):
        self.assertEquals(self.calculate(-26479.0, 114274.0), -140753.00)

    def test0668(self):
        self.assertEquals(self.calculate(194736.0, -181589.0), 376325.00)

    def test0669(self):
        self.assertEquals(self.calculate(47111.0, 79640.0), -32529.00)

    def test0670(self):
        self.assertEquals(self.calculate(-184036.0, 142415.0), -326451.00)

    def test0671(self):
        self.assertEquals(self.calculate(72448.0, 22792.0), 49656.00)

    def test0672(self):
        self.assertEquals(self.calculate(147289.0, 167992.0), -20703.00)

    def test0673(self):
        self.assertEquals(self.calculate(30286.0, -18353.0), 48639.00)

    def test0674(self):
        self.assertEquals(self.calculate(-154569.0, -87204.0), -67365.00)

    def test0675(self):
        self.assertEquals(self.calculate(-25798.0, -199396.0), 173598.00)

    def test0676(self):
        self.assertEquals(self.calculate(-170191.0, -116147.0), -54044.00)

    def test0677(self):
        self.assertEquals(self.calculate(67533.0, 50865.0), 16668.00)

    def test0678(self):
        self.assertEquals(self.calculate(59250.0, 131094.0), -71844.00)

    def test0679(self):
        self.assertEquals(self.calculate(-101157.0, -178902.0), 77745.00)

    def test0680(self):
        self.assertEquals(self.calculate(107794.0, -43412.0), 151206.00)

    def test0681(self):
        self.assertEquals(self.calculate(68031.0, -114666.0), 182697.00)

    def test0682(self):
        self.assertEquals(self.calculate(135729.0, 31577.0), 104152.00)

    def test0683(self):
        self.assertEquals(self.calculate(-147858.0, -187484.0), 39626.00)

    def test0684(self):
        self.assertEquals(self.calculate(149588.0, 148971.0), 617.00)

    def test0685(self):
        self.assertEquals(self.calculate(15713.0, 122194.0), -106481.00)

    def test0686(self):
        self.assertEquals(self.calculate(105672.0, 1432.0), 104240.00)

    def test0687(self):
        self.assertEquals(self.calculate(88977.0, -1435.0), 90412.00)

    def test0688(self):
        self.assertEquals(self.calculate(-30022.0, -98919.0), 68897.00)

    def test0689(self):
        self.assertEquals(self.calculate(-12266.0, 149137.0), -161403.00)

    def test0690(self):
        self.assertEquals(self.calculate(103307.0, -81639.0), 184946.00)

    def test0691(self):
        self.assertEquals(self.calculate(-82031.0, -3894.0), -78137.00)

    def test0692(self):
        self.assertEquals(self.calculate(77375.0, 83460.0), -6085.00)

    def test0693(self):
        self.assertEquals(self.calculate(-52147.0, 93323.0), -145470.00)

    def test0694(self):
        self.assertEquals(self.calculate(17166.0, -52442.0), 69608.00)

    def test0695(self):
        self.assertEquals(self.calculate(-114359.0, -87839.0), -26520.00)

    def test0696(self):
        self.assertEquals(self.calculate(66273.0, -27431.0), 93704.00)

    def test0697(self):
        self.assertEquals(self.calculate(77106.0, 102002.0), -24896.00)

    def test0698(self):
        self.assertEquals(self.calculate(-114683.0, 157508.0), -272191.00)

    def test0699(self):
        self.assertEquals(self.calculate(109925.0, 105583.0), 4342.00)

    def test0700(self):
        self.assertEquals(self.calculate(124409.0, -71944.0), 196353.00)

    def test0701(self):
        self.assertEquals(self.calculate(-72241.0, -142669.0), 70428.00)

    def test0702(self):
        self.assertEquals(self.calculate(141673.0, -102216.0), 243889.00)

    def test0703(self):
        self.assertEquals(self.calculate(-60966.0, 124758.0), -185724.00)

    def test0704(self):
        self.assertEquals(self.calculate(-97272.0, 105888.0), -203160.00)

    def test0705(self):
        self.assertEquals(self.calculate(134382.0, 284.0), 134098.00)

    def test0706(self):
        self.assertEquals(self.calculate(-151527.0, -19465.0), -132062.00)

    def test0707(self):
        self.assertEquals(self.calculate(-104748.0, -171941.0), 67193.00)

    def test0708(self):
        self.assertEquals(self.calculate(98374.0, 129292.0), -30918.00)

    def test0709(self):
        self.assertEquals(self.calculate(-28003.0, 119164.0), -147167.00)

    def test0710(self):
        self.assertEquals(self.calculate(-153691.0, -32501.0), -121190.00)

    def test0711(self):
        self.assertEquals(self.calculate(-109021.0, -64069.0), -44952.00)

    def test0712(self):
        self.assertEquals(self.calculate(152670.0, 99215.0), 53455.00)

    def test0713(self):
        self.assertEquals(self.calculate(-50561.0, -22364.0), -28197.00)

    def test0714(self):
        self.assertEquals(self.calculate(184193.0, 189244.0), -5051.00)

    def test0715(self):
        self.assertEquals(self.calculate(-98465.0, -82380.0), -16085.00)

    def test0716(self):
        self.assertEquals(self.calculate(-167319.0, 26140.0), -193459.00)

    def test0717(self):
        self.assertEquals(self.calculate(186177.0, -161421.0), 347598.00)

    def test0718(self):
        self.assertEquals(self.calculate(-128681.0, -132999.0), 4318.00)

    def test0719(self):
        self.assertEquals(self.calculate(-102670.0, 79215.0), -181885.00)

    def test0720(self):
        self.assertEquals(self.calculate(-192817.0, -89362.0), -103455.00)

    def test0721(self):
        self.assertEquals(self.calculate(28704.0, -62319.0), 91023.00)

    def test0722(self):
        self.assertEquals(self.calculate(-84630.0, -82751.0), -1879.00)

    def test0723(self):
        self.assertEquals(self.calculate(175994.0, 116121.0), 59873.00)

    def test0724(self):
        self.assertEquals(self.calculate(-156578.0, -154975.0), -1603.00)

    def test0725(self):
        self.assertEquals(self.calculate(-130031.0, 128543.0), -258574.00)

    def test0726(self):
        self.assertEquals(self.calculate(-62877.0, -103581.0), 40704.00)

    def test0727(self):
        self.assertEquals(self.calculate(-154897.0, 169712.0), -324609.00)

    def test0728(self):
        self.assertEquals(self.calculate(-184525.0, 72233.0), -256758.00)

    def test0729(self):
        self.assertEquals(self.calculate(47940.0, -134969.0), 182909.00)

    def test0730(self):
        self.assertEquals(self.calculate(9277.0, 133494.0), -124217.00)

    def test0731(self):
        self.assertEquals(self.calculate(175777.0, 174346.0), 1431.00)

    def test0732(self):
        self.assertEquals(self.calculate(-127259.0, 187615.0), -314874.00)

    def test0733(self):
        self.assertEquals(self.calculate(18577.0, -6833.0), 25410.00)

    def test0734(self):
        self.assertEquals(self.calculate(125474.0, -39079.0), 164553.00)

    def test0735(self):
        self.assertEquals(self.calculate(-118348.0, 60287.0), -178635.00)

    def test0736(self):
        self.assertEquals(self.calculate(-1228.0, 109798.0), -111026.00)

    def test0737(self):
        self.assertEquals(self.calculate(124522.0, 37151.0), 87371.00)

    def test0738(self):
        self.assertEquals(self.calculate(-43991.0, -139746.0), 95755.00)

    def test0739(self):
        self.assertEquals(self.calculate(-132741.0, 68913.0), -201654.00)

    def test0740(self):
        self.assertEquals(self.calculate(119867.0, 40513.0), 79354.00)

    def test0741(self):
        self.assertEquals(self.calculate(18111.0, 142777.0), -124666.00)

    def test0742(self):
        self.assertEquals(self.calculate(7345.0, 35737.0), -28392.00)

    def test0743(self):
        self.assertEquals(self.calculate(-31284.0, -168847.0), 137563.00)

    def test0744(self):
        self.assertEquals(self.calculate(142372.0, 64034.0), 78338.00)

    def test0745(self):
        self.assertEquals(self.calculate(-111534.0, -165060.0), 53526.00)

    def test0746(self):
        self.assertEquals(self.calculate(-46341.0, -133813.0), 87472.00)

    def test0747(self):
        self.assertEquals(self.calculate(-122509.0, -12430.0), -110079.00)

    def test0748(self):
        self.assertEquals(self.calculate(-591.0, -137026.0), 136435.00)

    def test0749(self):
        self.assertEquals(self.calculate(-139158.0, -138254.0), -904.00)

    def test0750(self):
        self.assertEquals(self.calculate(20169.0, -134868.0), 155037.00)

    def test0751(self):
        self.assertEquals(self.calculate(-23655.0, -148890.0), 125235.00)

    def test0752(self):
        self.assertEquals(self.calculate(6107.0, 122023.0), -115916.00)

    def test0753(self):
        self.assertEquals(self.calculate(30567.0, -133162.0), 163729.00)

    def test0754(self):
        self.assertEquals(self.calculate(7719.0, -146164.0), 153883.00)

    def test0755(self):
        self.assertEquals(self.calculate(-23415.0, 76246.0), -99661.00)

    def test0756(self):
        self.assertEquals(self.calculate(-108733.0, 143288.0), -252021.00)

    def test0757(self):
        self.assertEquals(self.calculate(-129558.0, 161067.0), -290625.00)

    def test0758(self):
        self.assertEquals(self.calculate(-39325.0, 90054.0), -129379.00)

    def test0759(self):
        self.assertEquals(self.calculate(132853.0, 164803.0), -31950.00)

    def test0760(self):
        self.assertEquals(self.calculate(-84363.0, 286.0), -84649.00)

    def test0761(self):
        self.assertEquals(self.calculate(176755.0, -123639.0), 300394.00)

    def test0762(self):
        self.assertEquals(self.calculate(186115.0, -117907.0), 304022.00)

    def test0763(self):
        self.assertEquals(self.calculate(-42623.0, -184491.0), 141868.00)

    def test0764(self):
        self.assertEquals(self.calculate(-137824.0, 187808.0), -325632.00)

    def test0765(self):
        self.assertEquals(self.calculate(-142160.0, 23096.0), -165256.00)

    def test0766(self):
        self.assertEquals(self.calculate(-74489.0, 134034.0), -208523.00)

    def test0767(self):
        self.assertEquals(self.calculate(-154719.0, 137532.0), -292251.00)

    def test0768(self):
        self.assertEquals(self.calculate(169495.0, -17724.0), 187219.00)

    def test0769(self):
        self.assertEquals(self.calculate(98802.0, -191632.0), 290434.00)

    def test0770(self):
        self.assertEquals(self.calculate(-169711.0, 38072.0), -207783.00)

    def test0771(self):
        self.assertEquals(self.calculate(-86404.0, 153006.0), -239410.00)

    def test0772(self):
        self.assertEquals(self.calculate(61086.0, 53037.0), 8049.00)

    def test0773(self):
        self.assertEquals(self.calculate(-15569.0, -45054.0), 29485.00)

    def test0774(self):
        self.assertEquals(self.calculate(-21704.0, 42115.0), -63819.00)

    def test0775(self):
        self.assertEquals(self.calculate(-104603.0, 16725.0), -121328.00)

    def test0776(self):
        self.assertEquals(self.calculate(17925.0, 48784.0), -30859.00)

    def test0777(self):
        self.assertEquals(self.calculate(-83056.0, -112462.0), 29406.00)

    def test0778(self):
        self.assertEquals(self.calculate(44584.0, 169313.0), -124729.00)

    def test0779(self):
        self.assertEquals(self.calculate(122438.0, -27646.0), 150084.00)

    def test0780(self):
        self.assertEquals(self.calculate(53673.0, 75303.0), -21630.00)

    def test0781(self):
        self.assertEquals(self.calculate(-37471.0, -37502.0), 31.00)

    def test0782(self):
        self.assertEquals(self.calculate(-14206.0, -3329.0), -10877.00)

    def test0783(self):
        self.assertEquals(self.calculate(-78550.0, 144088.0), -222638.00)

    def test0784(self):
        self.assertEquals(self.calculate(-63131.0, -194002.0), 130871.00)

    def test0785(self):
        self.assertEquals(self.calculate(61502.0, -117888.0), 179390.00)

    def test0786(self):
        self.assertEquals(self.calculate(110709.0, 6694.0), 104015.00)

    def test0787(self):
        self.assertEquals(self.calculate(128593.0, 173207.0), -44614.00)

    def test0788(self):
        self.assertEquals(self.calculate(-190809.0, 74082.0), -264891.00)

    def test0789(self):
        self.assertEquals(self.calculate(14290.0, -115903.0), 130193.00)

    def test0790(self):
        self.assertEquals(self.calculate(32247.0, 177791.0), -145544.00)

    def test0791(self):
        self.assertEquals(self.calculate(168392.0, -76821.0), 245213.00)

    def test0792(self):
        self.assertEquals(self.calculate(-107226.0, 65252.0), -172478.00)

    def test0793(self):
        self.assertEquals(self.calculate(120650.0, -148289.0), 268939.00)

    def test0794(self):
        self.assertEquals(self.calculate(176939.0, -37462.0), 214401.00)

    def test0795(self):
        self.assertEquals(self.calculate(-102772.0, 191617.0), -294389.00)

    def test0796(self):
        self.assertEquals(self.calculate(113203.0, -170022.0), 283225.00)

    def test0797(self):
        self.assertEquals(self.calculate(-106475.0, 55662.0), -162137.00)

    def test0798(self):
        self.assertEquals(self.calculate(164194.0, -13532.0), 177726.00)

    def test0799(self):
        self.assertEquals(self.calculate(-169857.0, -33642.0), -136215.00)

    def test0800(self):
        self.assertEquals(self.calculate(-83173.0, -29967.0), -53206.00)

    def test0801(self):
        self.assertEquals(self.calculate(-57947.0, 57855.0), -115802.00)

    def test0802(self):
        self.assertEquals(self.calculate(130731.0, -14493.0), 145224.00)

    def test0803(self):
        self.assertEquals(self.calculate(-77529.0, 19138.0), -96667.00)

    def test0804(self):
        self.assertEquals(self.calculate(-25209.0, 173243.0), -198452.00)

    def test0805(self):
        self.assertEquals(self.calculate(115680.0, -160987.0), 276667.00)

    def test0806(self):
        self.assertEquals(self.calculate(-42259.0, 171310.0), -213569.00)

    def test0807(self):
        self.assertEquals(self.calculate(-6691.0, -84427.0), 77736.00)

    def test0808(self):
        self.assertEquals(self.calculate(-47430.0, 179390.0), -226820.00)

    def test0809(self):
        self.assertEquals(self.calculate(-19340.0, -46490.0), 27150.00)

    def test0810(self):
        self.assertEquals(self.calculate(-178536.0, 117478.0), -296014.00)

    def test0811(self):
        self.assertEquals(self.calculate(-39765.0, -167699.0), 127934.00)

    def test0812(self):
        self.assertEquals(self.calculate(-167430.0, -97413.0), -70017.00)

    def test0813(self):
        self.assertEquals(self.calculate(-130189.0, 39323.0), -169512.00)

    def test0814(self):
        self.assertEquals(self.calculate(190848.0, 120644.0), 70204.00)

    def test0815(self):
        self.assertEquals(self.calculate(89491.0, 45986.0), 43505.00)

    def test0816(self):
        self.assertEquals(self.calculate(93567.0, 37546.0), 56021.00)

    def test0817(self):
        self.assertEquals(self.calculate(-30207.0, -36914.0), 6707.00)

    def test0818(self):
        self.assertEquals(self.calculate(-67469.0, -115997.0), 48528.00)

    def test0819(self):
        self.assertEquals(self.calculate(-131009.0, 81884.0), -212893.00)

    def test0820(self):
        self.assertEquals(self.calculate(27674.0, -29216.0), 56890.00)

    def test0821(self):
        self.assertEquals(self.calculate(-178651.0, 192248.0), -370899.00)

    def test0822(self):
        self.assertEquals(self.calculate(-115506.0, 137098.0), -252604.00)

    def test0823(self):
        self.assertEquals(self.calculate(-117128.0, 198762.0), -315890.00)

    def test0824(self):
        self.assertEquals(self.calculate(-27135.0, -173869.0), 146734.00)

    def test0825(self):
        self.assertEquals(self.calculate(-57932.0, 165484.0), -223416.00)

    def test0826(self):
        self.assertEquals(self.calculate(-187797.0, 47195.0), -234992.00)

    def test0827(self):
        self.assertEquals(self.calculate(90582.0, -42165.0), 132747.00)

    def test0828(self):
        self.assertEquals(self.calculate(178828.0, 155732.0), 23096.00)

    def test0829(self):
        self.assertEquals(self.calculate(141367.0, 28145.0), 113222.00)

    def test0830(self):
        self.assertEquals(self.calculate(117984.0, 63119.0), 54865.00)

    def test0831(self):
        self.assertEquals(self.calculate(-84013.0, -111459.0), 27446.00)

    def test0832(self):
        self.assertEquals(self.calculate(-192499.0, 51180.0), -243679.00)

    def test0833(self):
        self.assertEquals(self.calculate(-194240.0, -30221.0), -164019.00)

    def test0834(self):
        self.assertEquals(self.calculate(171581.0, -136548.0), 308129.00)

    def test0835(self):
        self.assertEquals(self.calculate(46168.0, -45162.0), 91330.00)

    def test0836(self):
        self.assertEquals(self.calculate(175298.0, 181665.0), -6367.00)

    def test0837(self):
        self.assertEquals(self.calculate(170684.0, -173207.0), 343891.00)

    def test0838(self):
        self.assertEquals(self.calculate(110.0, 62954.0), -62844.00)

    def test0839(self):
        self.assertEquals(self.calculate(-189450.0, 132427.0), -321877.00)

    def test0840(self):
        self.assertEquals(self.calculate(169406.0, 98505.0), 70901.00)

    def test0841(self):
        self.assertEquals(self.calculate(-107301.0, 89896.0), -197197.00)

    def test0842(self):
        self.assertEquals(self.calculate(102589.0, 100402.0), 2187.00)

    def test0843(self):
        self.assertEquals(self.calculate(-183291.0, -43323.0), -139968.00)

    def test0844(self):
        self.assertEquals(self.calculate(-30420.0, 77057.0), -107477.00)

    def test0845(self):
        self.assertEquals(self.calculate(-55260.0, 191921.0), -247181.00)

    def test0846(self):
        self.assertEquals(self.calculate(-62624.0, 100704.0), -163328.00)

    def test0847(self):
        self.assertEquals(self.calculate(160092.0, 154993.0), 5099.00)

    def test0848(self):
        self.assertEquals(self.calculate(-24924.0, -29081.0), 4157.00)

    def test0849(self):
        self.assertEquals(self.calculate(14333.0, -191907.0), 206240.00)

    def test0850(self):
        self.assertEquals(self.calculate(138636.0, -56114.0), 194750.00)

    def test0851(self):
        self.assertEquals(self.calculate(192331.0, 10444.0), 181887.00)

    def test0852(self):
        self.assertEquals(self.calculate(109627.0, -72738.0), 182365.00)

    def test0853(self):
        self.assertEquals(self.calculate(-56663.0, 108097.0), -164760.00)

    def test0854(self):
        self.assertEquals(self.calculate(-168838.0, -26666.0), -142172.00)

    def test0855(self):
        self.assertEquals(self.calculate(-29527.0, -66910.0), 37383.00)

    def test0856(self):
        self.assertEquals(self.calculate(122244.0, -156432.0), 278676.00)

    def test0857(self):
        self.assertEquals(self.calculate(-11835.0, 6062.0), -17897.00)

    def test0858(self):
        self.assertEquals(self.calculate(-184609.0, -190959.0), 6350.00)

    def test0859(self):
        self.assertEquals(self.calculate(-33868.0, 61012.0), -94880.00)

    def test0860(self):
        self.assertEquals(self.calculate(129298.0, -109808.0), 239106.00)

    def test0861(self):
        self.assertEquals(self.calculate(-137007.0, 56652.0), -193659.00)

    def test0862(self):
        self.assertEquals(self.calculate(8086.0, -90852.0), 98938.00)

    def test0863(self):
        self.assertEquals(self.calculate(55911.0, 134966.0), -79055.00)

    def test0864(self):
        self.assertEquals(self.calculate(-141545.0, -137883.0), -3662.00)

    def test0865(self):
        self.assertEquals(self.calculate(187272.0, 194261.0), -6989.00)

    def test0866(self):
        self.assertEquals(self.calculate(-62231.0, -45856.0), -16375.00)

    def test0867(self):
        self.assertEquals(self.calculate(90856.0, 80366.0), 10490.00)

    def test0868(self):
        self.assertEquals(self.calculate(187179.0, -139123.0), 326302.00)

    def test0869(self):
        self.assertEquals(self.calculate(-53045.0, -70255.0), 17210.00)

    def test0870(self):
        self.assertEquals(self.calculate(175725.0, 82858.0), 92867.00)

    def test0871(self):
        self.assertEquals(self.calculate(-61750.0, 193672.0), -255422.00)

    def test0872(self):
        self.assertEquals(self.calculate(56271.0, 183284.0), -127013.00)

    def test0873(self):
        self.assertEquals(self.calculate(6734.0, -108674.0), 115408.00)

    def test0874(self):
        self.assertEquals(self.calculate(193201.0, 65067.0), 128134.00)

    def test0875(self):
        self.assertEquals(self.calculate(-79516.0, -24293.0), -55223.00)

    def test0876(self):
        self.assertEquals(self.calculate(-44911.0, 167475.0), -212386.00)

    def test0877(self):
        self.assertEquals(self.calculate(-15656.0, -20578.0), 4922.00)

    def test0878(self):
        self.assertEquals(self.calculate(32587.0, -13400.0), 45987.00)

    def test0879(self):
        self.assertEquals(self.calculate(-45725.0, -180004.0), 134279.00)

    def test0880(self):
        self.assertEquals(self.calculate(-195364.0, -126081.0), -69283.00)

    def test0881(self):
        self.assertEquals(self.calculate(-177656.0, 193360.0), -371016.00)

    def test0882(self):
        self.assertEquals(self.calculate(185420.0, 148607.0), 36813.00)

    def test0883(self):
        self.assertEquals(self.calculate(93233.0, 146156.0), -52923.00)

    def test0884(self):
        self.assertEquals(self.calculate(-153520.0, -124959.0), -28561.00)

    def test0885(self):
        self.assertEquals(self.calculate(163084.0, 431.0), 162653.00)

    def test0886(self):
        self.assertEquals(self.calculate(27659.0, 19521.0), 8138.00)

    def test0887(self):
        self.assertEquals(self.calculate(-116050.0, -33464.0), -82586.00)

    def test0888(self):
        self.assertEquals(self.calculate(-136553.0, -57449.0), -79104.00)

    def test0889(self):
        self.assertEquals(self.calculate(122419.0, 157244.0), -34825.00)

    def test0890(self):
        self.assertEquals(self.calculate(-27025.0, -22430.0), -4595.00)

    def test0891(self):
        self.assertEquals(self.calculate(166243.0, -85955.0), 252198.00)

    def test0892(self):
        self.assertEquals(self.calculate(138939.0, 158994.0), -20055.00)

    def test0893(self):
        self.assertEquals(self.calculate(60656.0, -41000.0), 101656.00)

    def test0894(self):
        self.assertEquals(self.calculate(-153170.0, -34706.0), -118464.00)

    def test0895(self):
        self.assertEquals(self.calculate(-153411.0, -33659.0), -119752.00)

    def test0896(self):
        self.assertEquals(self.calculate(-99732.0, 194793.0), -294525.00)

    def test0897(self):
        self.assertEquals(self.calculate(-183938.0, -156292.0), -27646.00)

    def test0898(self):
        self.assertEquals(self.calculate(92919.0, 75774.0), 17145.00)

    def test0899(self):
        self.assertEquals(self.calculate(152549.0, -7710.0), 160259.00)

    def test0900(self):
        self.assertEquals(self.calculate(60445.0, 86090.0), -25645.00)

    def test0901(self):
        self.assertEquals(self.calculate(-58723.0, -68356.0), 9633.00)

    def test0902(self):
        self.assertEquals(self.calculate(15083.0, 87043.0), -71960.00)

    def test0903(self):
        self.assertEquals(self.calculate(128240.0, 23881.0), 104359.00)

    def test0904(self):
        self.assertEquals(self.calculate(116441.0, 22817.0), 93624.00)

    def test0905(self):
        self.assertEquals(self.calculate(-50440.0, -14566.0), -35874.00)

    def test0906(self):
        self.assertEquals(self.calculate(27246.0, 44997.0), -17751.00)

    def test0907(self):
        self.assertEquals(self.calculate(-71661.0, -47029.0), -24632.00)

    def test0908(self):
        self.assertEquals(self.calculate(158706.0, 193859.0), -35153.00)

    def test0909(self):
        self.assertEquals(self.calculate(45075.0, -91837.0), 136912.00)

    def test0910(self):
        self.assertEquals(self.calculate(-29309.0, 49145.0), -78454.00)

    def test0911(self):
        self.assertEquals(self.calculate(96990.0, -31821.0), 128811.00)

    def test0912(self):
        self.assertEquals(self.calculate(-15823.0, 716.0), -16539.00)

    def test0913(self):
        self.assertEquals(self.calculate(55350.0, 137858.0), -82508.00)

    def test0914(self):
        self.assertEquals(self.calculate(45760.0, -46330.0), 92090.00)

    def test0915(self):
        self.assertEquals(self.calculate(133546.0, 121621.0), 11925.00)

    def test0916(self):
        self.assertEquals(self.calculate(-123887.0, 144795.0), -268682.00)

    def test0917(self):
        self.assertEquals(self.calculate(-188827.0, 65703.0), -254530.00)

    def test0918(self):
        self.assertEquals(self.calculate(72711.0, -146330.0), 219041.00)

    def test0919(self):
        self.assertEquals(self.calculate(-155211.0, 4034.0), -159245.00)

    def test0920(self):
        self.assertEquals(self.calculate(-161150.0, -78876.0), -82274.00)

    def test0921(self):
        self.assertEquals(self.calculate(148937.0, -35170.0), 184107.00)

    def test0922(self):
        self.assertEquals(self.calculate(185366.0, 88870.0), 96496.00)

    def test0923(self):
        self.assertEquals(self.calculate(-187427.0, -34033.0), -153394.00)

    def test0924(self):
        self.assertEquals(self.calculate(56940.0, -164324.0), 221264.00)

    def test0925(self):
        self.assertEquals(self.calculate(-59830.0, -180951.0), 121121.00)

    def test0926(self):
        self.assertEquals(self.calculate(57999.0, -41812.0), 99811.00)

    def test0927(self):
        self.assertEquals(self.calculate(-107417.0, -170597.0), 63180.00)

    def test0928(self):
        self.assertEquals(self.calculate(-141474.0, -115939.0), -25535.00)

    def test0929(self):
        self.assertEquals(self.calculate(-99212.0, -135601.0), 36389.00)

    def test0930(self):
        self.assertEquals(self.calculate(-150475.0, -52788.0), -97687.00)

    def test0931(self):
        self.assertEquals(self.calculate(181700.0, 193036.0), -11336.00)

    def test0932(self):
        self.assertEquals(self.calculate(-103670.0, -24748.0), -78922.00)

    def test0933(self):
        self.assertEquals(self.calculate(-181635.0, 180302.0), -361937.00)

    def test0934(self):
        self.assertEquals(self.calculate(-80649.0, -174941.0), 94292.00)

    def test0935(self):
        self.assertEquals(self.calculate(-93991.0, 144536.0), -238527.00)

    def test0936(self):
        self.assertEquals(self.calculate(-136022.0, -65414.0), -70608.00)

    def test0937(self):
        self.assertEquals(self.calculate(-191960.0, 168687.0), -360647.00)

    def test0938(self):
        self.assertEquals(self.calculate(153340.0, -15158.0), 168498.00)

    def test0939(self):
        self.assertEquals(self.calculate(46486.0, 107007.0), -60521.00)

    def test0940(self):
        self.assertEquals(self.calculate(960.0, 108077.0), -107117.00)

    def test0941(self):
        self.assertEquals(self.calculate(42134.0, -28157.0), 70291.00)

    def test0942(self):
        self.assertEquals(self.calculate(-52031.0, 98465.0), -150496.00)

    def test0943(self):
        self.assertEquals(self.calculate(153322.0, 28486.0), 124836.00)

    def test0944(self):
        self.assertEquals(self.calculate(-100840.0, 163621.0), -264461.00)

    def test0945(self):
        self.assertEquals(self.calculate(-121076.0, 168439.0), -289515.00)

    def test0946(self):
        self.assertEquals(self.calculate(-169149.0, 179873.0), -349022.00)

    def test0947(self):
        self.assertEquals(self.calculate(-57988.0, -175155.0), 117167.00)

    def test0948(self):
        self.assertEquals(self.calculate(-180173.0, -24886.0), -155287.00)

    def test0949(self):
        self.assertEquals(self.calculate(-80039.0, 187484.0), -267523.00)

    def test0950(self):
        self.assertEquals(self.calculate(9296.0, -26553.0), 35849.00)

    def test0951(self):
        self.assertEquals(self.calculate(167178.0, -170491.0), 337669.00)

    def test0952(self):
        self.assertEquals(self.calculate(-153559.0, -150623.0), -2936.00)

    def test0953(self):
        self.assertEquals(self.calculate(-94733.0, 115965.0), -210698.00)

    def test0954(self):
        self.assertEquals(self.calculate(99924.0, 119381.0), -19457.00)

    def test0955(self):
        self.assertEquals(self.calculate(-51009.0, -105632.0), 54623.00)

    def test0956(self):
        self.assertEquals(self.calculate(-18961.0, -186885.0), 167924.00)

    def test0957(self):
        self.assertEquals(self.calculate(82691.0, -180929.0), 263620.00)

    def test0958(self):
        self.assertEquals(self.calculate(71781.0, 157476.0), -85695.00)

    def test0959(self):
        self.assertEquals(self.calculate(-99297.0, 90675.0), -189972.00)

    def test0960(self):
        self.assertEquals(self.calculate(-98469.0, 73760.0), -172229.00)

    def test0961(self):
        self.assertEquals(self.calculate(-154725.0, 67478.0), -222203.00)

    def test0962(self):
        self.assertEquals(self.calculate(78587.0, 153837.0), -75250.00)

    def test0963(self):
        self.assertEquals(self.calculate(-56598.0, -102824.0), 46226.00)

    def test0964(self):
        self.assertEquals(self.calculate(8653.0, -179014.0), 187667.00)

    def test0965(self):
        self.assertEquals(self.calculate(9711.0, -170916.0), 180627.00)

    def test0966(self):
        self.assertEquals(self.calculate(-1632.0, 133272.0), -134904.00)

    def test0967(self):
        self.assertEquals(self.calculate(-161812.0, -48657.0), -113155.00)

    def test0968(self):
        self.assertEquals(self.calculate(-79444.0, -44460.0), -34984.00)

    def test0969(self):
        self.assertEquals(self.calculate(43068.0, -107555.0), 150623.00)

    def test0970(self):
        self.assertEquals(self.calculate(-96470.0, -182235.0), 85765.00)

    def test0971(self):
        self.assertEquals(self.calculate(-30608.0, -113454.0), 82846.00)

    def test0972(self):
        self.assertEquals(self.calculate(-167085.0, 74973.0), -242058.00)

    def test0973(self):
        self.assertEquals(self.calculate(-105193.0, 59861.0), -165054.00)

    def test0974(self):
        self.assertEquals(self.calculate(94563.0, 53121.0), 41442.00)

    def test0975(self):
        self.assertEquals(self.calculate(115065.0, 3564.0), 111501.00)

    def test0976(self):
        self.assertEquals(self.calculate(-145274.0, -144029.0), -1245.00)

    def test0977(self):
        self.assertEquals(self.calculate(48400.0, 46342.0), 2058.00)

    def test0978(self):
        self.assertEquals(self.calculate(-199139.0, 144250.0), -343389.00)

    def test0979(self):
        self.assertEquals(self.calculate(184804.0, -150265.0), 335069.00)

    def test0980(self):
        self.assertEquals(self.calculate(-101612.0, -117253.0), 15641.00)

    def test0981(self):
        self.assertEquals(self.calculate(-163739.0, -190776.0), 27037.00)

    def test0982(self):
        self.assertEquals(self.calculate(83956.0, -171057.0), 255013.00)

    def test0983(self):
        self.assertEquals(self.calculate(-78801.0, -45135.0), -33666.00)

    def test0984(self):
        self.assertEquals(self.calculate(-41245.0, -196636.0), 155391.00)

    def test0985(self):
        self.assertEquals(self.calculate(-182938.0, -169288.0), -13650.00)

    def test0986(self):
        self.assertEquals(self.calculate(-89055.0, -54273.0), -34782.00)

    def test0987(self):
        self.assertEquals(self.calculate(109455.0, 83560.0), 25895.00)

    def test0988(self):
        self.assertEquals(self.calculate(-70858.0, -8588.0), -62270.00)

    def test0989(self):
        self.assertEquals(self.calculate(-172786.0, -119555.0), -53231.00)

    def test0990(self):
        self.assertEquals(self.calculate(-80807.0, 164399.0), -245206.00)

    def test0991(self):
        self.assertEquals(self.calculate(185851.0, -69399.0), 255250.00)

    def test0992(self):
        self.assertEquals(self.calculate(63730.0, -193333.0), 257063.00)

    def test0993(self):
        self.assertEquals(self.calculate(35954.0, 80601.0), -44647.00)

    def test0994(self):
        self.assertEquals(self.calculate(-141811.0, 152379.0), -294190.00)

    def test0995(self):
        self.assertEquals(self.calculate(-121703.0, -55931.0), -65772.00)

    def test0996(self):
        self.assertEquals(self.calculate(-24577.0, -104841.0), 80264.00)

    def test0997(self):
        self.assertEquals(self.calculate(151105.0, 67525.0), 83580.00)

    def test0998(self):
        self.assertEquals(self.calculate(-177007.0, 19734.0), -196741.00)

    def test0999(self):
        self.assertEquals(self.calculate(-158513.0, 99793.0), -258306.00)

    def test1000(self):
        self.assertEquals(self.calculate(-156346.0, -31853.0), -124493.00)

    def test1001(self):
        self.assertEquals(self.calculate(100276.0, 9041.0), 91235.00)

    def test1002(self):
        self.assertEquals(self.calculate(139035.0, 108882.0), 30153.00)

    def test1003(self):
        self.assertEquals(self.calculate(56416.0, 100768.0), -44352.00)

    def test1004(self):
        self.assertEquals(self.calculate(125310.0, 162211.0), -36901.00)

    def test1005(self):
        self.assertEquals(self.calculate(-143400.0, 106962.0), -250362.00)

    def test1006(self):
        self.assertEquals(self.calculate(19658.0, 20278.0), -620.00)

    def test1007(self):
        self.assertEquals(self.calculate(53322.0, 45167.0), 8155.00)

    def test1008(self):
        self.assertEquals(self.calculate(-78376.0, -181589.0), 103213.00)

    def test1009(self):
        self.assertEquals(self.calculate(-170049.0, 174039.0), -344088.00)

    def test1010(self):
        self.assertEquals(self.calculate(-48005.0, 30237.0), -78242.00)

    def test1011(self):
        self.assertEquals(self.calculate(60380.0, 196275.0), -135895.00)

    def test1012(self):
        self.assertEquals(self.calculate(-6407.0, -26581.0), 20174.00)

    def test1013(self):
        self.assertEquals(self.calculate(-113702.0, 22245.0), -135947.00)

    def test1014(self):
        self.assertEquals(self.calculate(-145835.0, 72343.0), -218178.00)

    def test1015(self):
        self.assertEquals(self.calculate(59396.0, -29035.0), 88431.00)

    def test1016(self):
        self.assertEquals(self.calculate(135739.0, 41237.0), 94502.00)

    def test1017(self):
        self.assertEquals(self.calculate(66246.0, 171375.0), -105129.00)

    def test1018(self):
        self.assertEquals(self.calculate(17412.0, 122158.0), -104746.00)

    def test1019(self):
        self.assertEquals(self.calculate(7839.0, -23952.0), 31791.00)

    def test1020(self):
        self.assertEquals(self.calculate(-167670.0, -62440.0), -105230.00)

    def test1021(self):
        self.assertEquals(self.calculate(158037.0, -69536.0), 227573.00)

    def test1022(self):
        self.assertEquals(self.calculate(-178630.0, 188297.0), -366927.00)

    def test1023(self):
        self.assertEquals(self.calculate(-57011.0, 12023.0), -69034.00)


#
unittest.main()

