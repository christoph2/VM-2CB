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

class TestVM_Mul_IntInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushW(rhs)
        v.VM_Mul()
        res = v.VM_PopW()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-3112, -25218), 31824, "")

    def test0001(self):
        self.assertEquals(self.calculate(-20994, -17873), 32162, "")

    def test0002(self):
        self.assertEquals(self.calculate(-31667, 32469), -1519, "")

    def test0003(self):
        self.assertEquals(self.calculate(-28182, 18162), -5324, "")

    def test0004(self):
        self.assertEquals(self.calculate(7590, -13616), 4832, "")

    def test0005(self):
        self.assertEquals(self.calculate(13954, 14418), -6748, "")

    def test0006(self):
        self.assertEquals(self.calculate(-20017, -23276), 20268, "")

    def test0007(self):
        self.assertEquals(self.calculate(-15740, 28142), 2744, "")

    def test0008(self):
        self.assertEquals(self.calculate(7916, -17856), 13056, "")

    def test0009(self):
        self.assertEquals(self.calculate(-7598, -16649), 14622, "")

    def test0010(self):
        self.assertEquals(self.calculate(-32449, -13363), 29811, "")

    def test0011(self):
        self.assertEquals(self.calculate(14154, 15038), -13076, "")

    def test0012(self):
        self.assertEquals(self.calculate(8849, 9002), 32458, "")

    def test0013(self):
        self.assertEquals(self.calculate(4579, -27600), -26992, "")

    def test0014(self):
        self.assertEquals(self.calculate(-4177, -619), 29659, "")

    def test0015(self):
        self.assertEquals(self.calculate(-22795, -26514), 13638, "")

    def test0016(self):
        self.assertEquals(self.calculate(-30738, 1983), -4974, "")

    def test0017(self):
        self.assertEquals(self.calculate(1223, 6276), 7836, "")

    def test0018(self):
        self.assertEquals(self.calculate(558, 29467), -6950, "")

    def test0019(self):
        self.assertEquals(self.calculate(25013, 5628), 1836, "")

    def test0020(self):
        self.assertEquals(self.calculate(-14370, -4618), -27308, "")

    def test0021(self):
        self.assertEquals(self.calculate(12867, -25523), -3545, "")

    def test0022(self):
        self.assertEquals(self.calculate(433, -19986), -3186, "")

    def test0023(self):
        self.assertEquals(self.calculate(1948, -5454), -7560, "")

    def test0024(self):
        self.assertEquals(self.calculate(-1572, 32585), 25532, "")

    def test0025(self):
        self.assertEquals(self.calculate(-14544, 16364), 28736, "")

    def test0026(self):
        self.assertEquals(self.calculate(-24045, 17435), 9217, "")

    def test0027(self):
        self.assertEquals(self.calculate(3049, 4611), -31301, "")

    def test0028(self):
        self.assertEquals(self.calculate(-29830, 2537), 15370, "")

    def test0029(self):
        self.assertEquals(self.calculate(8819, 9498), 7854, "")

    def test0030(self):
        self.assertEquals(self.calculate(-19226, -12076), -20872, "")

    def test0031(self):
        self.assertEquals(self.calculate(-23057, -32572), -29956, "")

    def test0032(self):
        self.assertEquals(self.calculate(-30961, -1563), 26475, "")

    def test0033(self):
        self.assertEquals(self.calculate(12891, -11693), -1663, "")

    def test0034(self):
        self.assertEquals(self.calculate(-16036, 6863), -20124, "")

    def test0035(self):
        self.assertEquals(self.calculate(9888, 28441), 9632, "")

    def test0036(self):
        self.assertEquals(self.calculate(13673, -8741), 21971, "")

    def test0037(self):
        self.assertEquals(self.calculate(27417, 13835), -8173, "")

    def test0038(self):
        self.assertEquals(self.calculate(23870, -19863), 23150, "")

    def test0039(self):
        self.assertEquals(self.calculate(23345, -17586), -27666, "")

    def test0040(self):
        self.assertEquals(self.calculate(-16201, 8930), 28558, "")

    def test0041(self):
        self.assertEquals(self.calculate(-25779, -5103), 19485, "")

    def test0042(self):
        self.assertEquals(self.calculate(-15752, -23988), -21600, "")

    def test0043(self):
        self.assertEquals(self.calculate(22953, -21248), 13568, "")

    def test0044(self):
        self.assertEquals(self.calculate(31972, -17462), 6120, "")

    def test0045(self):
        self.assertEquals(self.calculate(-11292, 27923), -12820, "")

    def test0046(self):
        self.assertEquals(self.calculate(-4386, -24585), 23090, "")

    def test0047(self):
        self.assertEquals(self.calculate(25879, 2840), 30504, "")

    def test0048(self):
        self.assertEquals(self.calculate(-9220, 23187), -5708, "")

    def test0049(self):
        self.assertEquals(self.calculate(3767, -27776), 28800, "")

    def test0050(self):
        self.assertEquals(self.calculate(6142, -9364), 26920, "")

    def test0051(self):
        self.assertEquals(self.calculate(-29303, 28824), -1704, "")

    def test0052(self):
        self.assertEquals(self.calculate(-12620, -13000), 23392, "")

    def test0053(self):
        self.assertEquals(self.calculate(-22151, -25905), -11561, "")

    def test0054(self):
        self.assertEquals(self.calculate(5724, -31881), 30916, "")

    def test0055(self):
        self.assertEquals(self.calculate(11330, -28293), -23114, "")

    def test0056(self):
        self.assertEquals(self.calculate(-15784, -1436), -9632, "")

    def test0057(self):
        self.assertEquals(self.calculate(-27086, -1237), 16486, "")

    def test0058(self):
        self.assertEquals(self.calculate(14080, 31708), 17408, "")

    def test0059(self):
        self.assertEquals(self.calculate(-28146, -8759), -15618, "")

    def test0060(self):
        self.assertEquals(self.calculate(-21534, -10712), -14512, "")

    def test0061(self):
        self.assertEquals(self.calculate(-3240, -5921), -18008, "")

    def test0062(self):
        self.assertEquals(self.calculate(-16248, 5065), 17096, "")

    def test0063(self):
        self.assertEquals(self.calculate(28716, -24431), 2284, "")

    def test0064(self):
        self.assertEquals(self.calculate(-11112, -6375), -5416, "")

    def test0065(self):
        self.assertEquals(self.calculate(-29949, -6650), -3054, "")

    def test0066(self):
        self.assertEquals(self.calculate(5089, -22191), -11471, "")

    def test0067(self):
        self.assertEquals(self.calculate(-12749, -29755), 24127, "")

    def test0068(self):
        self.assertEquals(self.calculate(18097, 22956), 2028, "")

    def test0069(self):
        self.assertEquals(self.calculate(23784, -20957), 25528, "")

    def test0070(self):
        self.assertEquals(self.calculate(16927, -13050), 24506, "")

    def test0071(self):
        self.assertEquals(self.calculate(-28904, -12536), -8000, "")

    def test0072(self):
        self.assertEquals(self.calculate(-27004, -8757), 20140, "")

    def test0073(self):
        self.assertEquals(self.calculate(15701, 24550), -23202, "")

    def test0074(self):
        self.assertEquals(self.calculate(27217, -3116), -4588, "")

    def test0075(self):
        self.assertEquals(self.calculate(-12759, 12812), -21524, "")

    def test0076(self):
        self.assertEquals(self.calculate(-24091, 21930), -29934, "")

    def test0077(self):
        self.assertEquals(self.calculate(19325, 29352), 13320, "")

    def test0078(self):
        self.assertEquals(self.calculate(-4943, -1978), 12390, "")

    def test0079(self):
        self.assertEquals(self.calculate(3171, 683), 3105, "")

    def test0080(self):
        self.assertEquals(self.calculate(17977, 15053), 9637, "")

    def test0081(self):
        self.assertEquals(self.calculate(17727, 20431), 28401, "")

    def test0082(self):
        self.assertEquals(self.calculate(2952, -12044), 32160, "")

    def test0083(self):
        self.assertEquals(self.calculate(-7990, -8288), 29760, "")

    def test0084(self):
        self.assertEquals(self.calculate(-28605, 20467), -25447, "")

    def test0085(self):
        self.assertEquals(self.calculate(1716, -12403), 15652, "")

    def test0086(self):
        self.assertEquals(self.calculate(-31997, 5841), 14195, "")

    def test0087(self):
        self.assertEquals(self.calculate(3597, 25290), 4162, "")

    def test0088(self):
        self.assertEquals(self.calculate(-26835, -985), 21467, "")

    def test0089(self):
        self.assertEquals(self.calculate(15022, 26737), -26930, "")

    def test0090(self):
        self.assertEquals(self.calculate(1844, 30804), -17136, "")

    def test0091(self):
        self.assertEquals(self.calculate(28220, -6402), 18312, "")

    def test0092(self):
        self.assertEquals(self.calculate(-7590, 1690), 17956, "")

    def test0093(self):
        self.assertEquals(self.calculate(4188, 1288), 20192, "")

    def test0094(self):
        self.assertEquals(self.calculate(18051, -14496), 17952, "")

    def test0095(self):
        self.assertEquals(self.calculate(10893, -25047), -10603, "")

    def test0096(self):
        self.assertEquals(self.calculate(-24396, 10720), 29056, "")

    def test0097(self):
        self.assertEquals(self.calculate(22126, 16778), -31412, "")

    def test0098(self):
        self.assertEquals(self.calculate(5242, -30427), 16290, "")

    def test0099(self):
        self.assertEquals(self.calculate(-21339, -11132), -22252, "")

    def test0100(self):
        self.assertEquals(self.calculate(26194, 1784), 2928, "")

    def test0101(self):
        self.assertEquals(self.calculate(-24434, -28784), -24096, "")

    def test0102(self):
        self.assertEquals(self.calculate(-27391, -16193), -5185, "")

    def test0103(self):
        self.assertEquals(self.calculate(-29667, -26111), -483, "")

    def test0104(self):
        self.assertEquals(self.calculate(30684, -13652), 8144, "")

    def test0105(self):
        self.assertEquals(self.calculate(-26648, 5279), 31000, "")

    def test0106(self):
        self.assertEquals(self.calculate(31996, -25868), -18384, "")

    def test0107(self):
        self.assertEquals(self.calculate(15804, -15076), 27792, "")

    def test0108(self):
        self.assertEquals(self.calculate(30898, 1868), -19752, "")

    def test0109(self):
        self.assertEquals(self.calculate(-21975, 4739), -2821, "")

    def test0110(self):
        self.assertEquals(self.calculate(5439, 31169), -13441, "")

    def test0111(self):
        self.assertEquals(self.calculate(12016, -29828), 3136, "")

    def test0112(self):
        self.assertEquals(self.calculate(-11330, 25660), -10104, "")

    def test0113(self):
        self.assertEquals(self.calculate(-31827, -24886), -21374, "")

    def test0114(self):
        self.assertEquals(self.calculate(8487, 15465), -17153, "")

    def test0115(self):
        self.assertEquals(self.calculate(5398, 4008), 8304, "")

    def test0116(self):
        self.assertEquals(self.calculate(22733, 4769), 17133, "")

    def test0117(self):
        self.assertEquals(self.calculate(8069, -5268), 25372, "")

    def test0118(self):
        self.assertEquals(self.calculate(-20138, 14642), -14132, "")

    def test0119(self):
        self.assertEquals(self.calculate(21271, 6194), 25214, "")

    def test0120(self):
        self.assertEquals(self.calculate(-9712, 24496), -9472, "")

    def test0121(self):
        self.assertEquals(self.calculate(-24276, -19552), 32640, "")

    def test0122(self):
        self.assertEquals(self.calculate(17893, -31304), 13720, "")

    def test0123(self):
        self.assertEquals(self.calculate(26135, -14317), -29771, "")

    def test0124(self):
        self.assertEquals(self.calculate(-2930, -3662), -18244, "")

    def test0125(self):
        self.assertEquals(self.calculate(12319, -23408), -4752, "")

    def test0126(self):
        self.assertEquals(self.calculate(-20453, -21768), -30680, "")

    def test0127(self):
        self.assertEquals(self.calculate(13818, -6531), -2286, "")

    def test0128(self):
        self.assertEquals(self.calculate(-20501, 8112), 26256, "")

    def test0129(self):
        self.assertEquals(self.calculate(-8053, -2388), 28516, "")

    def test0130(self):
        self.assertEquals(self.calculate(10312, -4712), -27968, "")

    def test0131(self):
        self.assertEquals(self.calculate(-744, -24262), 28528, "")

    def test0132(self):
        self.assertEquals(self.calculate(3064, 27618), 14576, "")

    def test0133(self):
        self.assertEquals(self.calculate(10618, 10944), 8064, "")

    def test0134(self):
        self.assertEquals(self.calculate(-14737, -22361), 19049, "")

    def test0135(self):
        self.assertEquals(self.calculate(-12460, 2427), -28324, "")

    def test0136(self):
        self.assertEquals(self.calculate(-7269, 21488), -23984, "")

    def test0137(self):
        self.assertEquals(self.calculate(-4431, -19672), 3752, "")

    def test0138(self):
        self.assertEquals(self.calculate(12955, -32249), 6205, "")

    def test0139(self):
        self.assertEquals(self.calculate(14759, 2756), -22052, "")

    def test0140(self):
        self.assertEquals(self.calculate(2668, -32108), -8592, "")

    def test0141(self):
        self.assertEquals(self.calculate(-9644, -15541), -3428, "")

    def test0142(self):
        self.assertEquals(self.calculate(23708, -11259), -244, "")

    def test0143(self):
        self.assertEquals(self.calculate(25374, -8749), -26694, "")

    def test0144(self):
        self.assertEquals(self.calculate(27436, -8165), -12892, "")

    def test0145(self):
        self.assertEquals(self.calculate(13359, -24352), 2336, "")

    def test0146(self):
        self.assertEquals(self.calculate(-25982, -7090), -9316, "")

    def test0147(self):
        self.assertEquals(self.calculate(-29313, 13430), 1162, "")

    def test0148(self):
        self.assertEquals(self.calculate(-1164, -13557), -13828, "")

    def test0149(self):
        self.assertEquals(self.calculate(-27624, -1358), 26800, "")

    def test0150(self):
        self.assertEquals(self.calculate(12551, 32492), -23436, "")

    def test0151(self):
        self.assertEquals(self.calculate(-8709, 9366), 23826, "")

    def test0152(self):
        self.assertEquals(self.calculate(25881, 1075), -30725, "")

    def test0153(self):
        self.assertEquals(self.calculate(16803, -24761), 28981, "")

    def test0154(self):
        self.assertEquals(self.calculate(-7492, -30532), 25104, "")

    def test0155(self):
        self.assertEquals(self.calculate(19042, 27580), -27144, "")

    def test0156(self):
        self.assertEquals(self.calculate(861, 3215), 15603, "")

    def test0157(self):
        self.assertEquals(self.calculate(-23553, 30872), -6296, "")

    def test0158(self):
        self.assertEquals(self.calculate(-7264, -17161), 8032, "")

    def test0159(self):
        self.assertEquals(self.calculate(-28553, 6129), -20217, "")

    def test0160(self):
        self.assertEquals(self.calculate(27871, -15938), -4990, "")

    def test0161(self):
        self.assertEquals(self.calculate(30263, -11042), 4018, "")

    def test0162(self):
        self.assertEquals(self.calculate(-24954, -4483), -1170, "")

    def test0163(self):
        self.assertEquals(self.calculate(32003, -12451), -10473, "")

    def test0164(self):
        self.assertEquals(self.calculate(16941, 3193), 25413, "")

    def test0165(self):
        self.assertEquals(self.calculate(-22777, 8939), 16749, "")

    def test0166(self):
        self.assertEquals(self.calculate(7273, -27528), 1336, "")

    def test0167(self):
        self.assertEquals(self.calculate(-24097, 25243), 24581, "")

    def test0168(self):
        self.assertEquals(self.calculate(-26911, 5693), 18845, "")

    def test0169(self):
        self.assertEquals(self.calculate(-16975, 31477), -7067, "")

    def test0170(self):
        self.assertEquals(self.calculate(3151, 2), 6302, "")

    def test0171(self):
        self.assertEquals(self.calculate(-5437, 8387), 12937, "")

    def test0172(self):
        self.assertEquals(self.calculate(8573, 16045), -6279, "")

    def test0173(self):
        self.assertEquals(self.calculate(25373, 30547), -25241, "")

    def test0174(self):
        self.assertEquals(self.calculate(24496, -25538), 27808, "")

    def test0175(self):
        self.assertEquals(self.calculate(2823, -6437), -18179, "")

    def test0176(self):
        self.assertEquals(self.calculate(-13954, -27389), -19846, "")

    def test0177(self):
        self.assertEquals(self.calculate(19834, 3569), 8666, "")

    def test0178(self):
        self.assertEquals(self.calculate(16309, 805), 21545, "")

    def test0179(self):
        self.assertEquals(self.calculate(-31444, -28600), 13408, "")

    def test0180(self):
        self.assertEquals(self.calculate(-757, -17534), -30570, "")

    def test0181(self):
        self.assertEquals(self.calculate(-975, -30791), 5737, "")

    def test0182(self):
        self.assertEquals(self.calculate(15482, -31343), -23782, "")

    def test0183(self):
        self.assertEquals(self.calculate(3420, -29131), -13300, "")

    def test0184(self):
        self.assertEquals(self.calculate(-18318, -3860), -5864, "")

    def test0185(self):
        self.assertEquals(self.calculate(-1144, 20393), 1224, "")

    def test0186(self):
        self.assertEquals(self.calculate(-25320, -32265), -21976, "")

    def test0187(self):
        self.assertEquals(self.calculate(6998, -22524), -8872, "")

    def test0188(self):
        self.assertEquals(self.calculate(4839, 27618), 15598, "")

    def test0189(self):
        self.assertEquals(self.calculate(-18127, -20246), -2358, "")

    def test0190(self):
        self.assertEquals(self.calculate(6038, 2073), -602, "")

    def test0191(self):
        self.assertEquals(self.calculate(31763, 16553), -22389, "")

    def test0192(self):
        self.assertEquals(self.calculate(14496, 15789), 25632, "")

    def test0193(self):
        self.assertEquals(self.calculate(-2446, -28792), -25968, "")

    def test0194(self):
        self.assertEquals(self.calculate(6133, -30253), -9233, "")

    def test0195(self):
        self.assertEquals(self.calculate(2047, 21284), -13092, "")

    def test0196(self):
        self.assertEquals(self.calculate(12061, -10556), 20532, "")

    def test0197(self):
        self.assertEquals(self.calculate(-1561, -9241), 7281, "")

    def test0198(self):
        self.assertEquals(self.calculate(-1066, 22835), -28254, "")

    def test0199(self):
        self.assertEquals(self.calculate(13602, -18928), 32288, "")

    def test0200(self):
        self.assertEquals(self.calculate(6920, -10545), -29832, "")

    def test0201(self):
        self.assertEquals(self.calculate(11954, 26312), 26384, "")

    def test0202(self):
        self.assertEquals(self.calculate(14834, -26229), 6246, "")

    def test0203(self):
        self.assertEquals(self.calculate(-23609, 3226), -9802, "")

    def test0204(self):
        self.assertEquals(self.calculate(25772, 22621), -19844, "")

    def test0205(self):
        self.assertEquals(self.calculate(19318, -21346), -9516, "")

    def test0206(self):
        self.assertEquals(self.calculate(25127, -24429), -17307, "")

    def test0207(self):
        self.assertEquals(self.calculate(26501, 21574), -3490, "")

    def test0208(self):
        self.assertEquals(self.calculate(15125, -565), -25945, "")

    def test0209(self):
        self.assertEquals(self.calculate(30370, 16803), -21722, "")

    def test0210(self):
        self.assertEquals(self.calculate(-588, -14525), 21020, "")

    def test0211(self):
        self.assertEquals(self.calculate(-4511, -16742), 25690, "")

    def test0212(self):
        self.assertEquals(self.calculate(31679, -19336), 19848, "")

    def test0213(self):
        self.assertEquals(self.calculate(-19200, -5872), 20480, "")

    def test0214(self):
        self.assertEquals(self.calculate(32151, 19533), -26005, "")

    def test0215(self):
        self.assertEquals(self.calculate(30088, -26829), -24040, "")

    def test0216(self):
        self.assertEquals(self.calculate(21306, 23695), 21862, "")

    def test0217(self):
        self.assertEquals(self.calculate(-15122, -26851), -20234, "")

    def test0218(self):
        self.assertEquals(self.calculate(-28078, -27909), 14950, "")

    def test0219(self):
        self.assertEquals(self.calculate(-13934, 22234), -19884, "")

    def test0220(self):
        self.assertEquals(self.calculate(20529, -14213), -12405, "")

    def test0221(self):
        self.assertEquals(self.calculate(-17189, 32336), -12688, "")

    def test0222(self):
        self.assertEquals(self.calculate(-2031, -14267), 9365, "")

    def test0223(self):
        self.assertEquals(self.calculate(20905, -7765), 5347, "")

    def test0224(self):
        self.assertEquals(self.calculate(26170, 8520), 14928, "")

    def test0225(self):
        self.assertEquals(self.calculate(-23554, 27258), 21260, "")

    def test0226(self):
        self.assertEquals(self.calculate(3951, 2227), 17053, "")

    def test0227(self):
        self.assertEquals(self.calculate(-2567, 7153), -11671, "")

    def test0228(self):
        self.assertEquals(self.calculate(-16626, -25428), -6808, "")

    def test0229(self):
        self.assertEquals(self.calculate(-10388, -17273), -5644, "")

    def test0230(self):
        self.assertEquals(self.calculate(-23494, 9155), 1582, "")

    def test0231(self):
        self.assertEquals(self.calculate(-4347, 13541), -11399, "")

    def test0232(self):
        self.assertEquals(self.calculate(26, 16845), -20782, "")

    def test0233(self):
        self.assertEquals(self.calculate(-22271, -10431), -16319, "")

    def test0234(self):
        self.assertEquals(self.calculate(26133, -30026), -6930, "")

    def test0235(self):
        self.assertEquals(self.calculate(-9898, -13093), 29842, "")

    def test0236(self):
        self.assertEquals(self.calculate(30444, -14725), -21660, "")

    def test0237(self):
        self.assertEquals(self.calculate(26638, -16645), 27066, "")

    def test0238(self):
        self.assertEquals(self.calculate(1199, -26226), 12306, "")

    def test0239(self):
        self.assertEquals(self.calculate(-30292, -25057), -11308, "")

    def test0240(self):
        self.assertEquals(self.calculate(14460, -29850), -10904, "")

    def test0241(self):
        self.assertEquals(self.calculate(8140, 8187), -7932, "")

    def test0242(self):
        self.assertEquals(self.calculate(-28082, 17381), 18886, "")

    def test0243(self):
        self.assertEquals(self.calculate(22815, -21379), 22563, "")

    def test0244(self):
        self.assertEquals(self.calculate(-1963, 21910), -17714, "")

    def test0245(self):
        self.assertEquals(self.calculate(-31207, 16433), -5431, "")

    def test0246(self):
        self.assertEquals(self.calculate(-19030, 22997), 16498, "")

    def test0247(self):
        self.assertEquals(self.calculate(20155, 162), -11690, "")

    def test0248(self):
        self.assertEquals(self.calculate(6233, 19612), 16956, "")

    def test0249(self):
        self.assertEquals(self.calculate(-24596, 16549), 4892, "")

    def test0250(self):
        self.assertEquals(self.calculate(13666, -3480), 21456, "")

    def test0251(self):
        self.assertEquals(self.calculate(-26198, -5567), 26666, "")

    def test0252(self):
        self.assertEquals(self.calculate(28773, 10761), -31347, "")

    def test0253(self):
        self.assertEquals(self.calculate(245, 31130), 24674, "")

    def test0254(self):
        self.assertEquals(self.calculate(-14705, -5832), -27064, "")

    def test0255(self):
        self.assertEquals(self.calculate(-4378, -23807), 24806, "")

    def test0256(self):
        self.assertEquals(self.calculate(-18826, 24526), -25356, "")

    def test0257(self):
        self.assertEquals(self.calculate(14255, -23436), 22348, "")

    def test0258(self):
        self.assertEquals(self.calculate(24493, -18957), 8759, "")

    def test0259(self):
        self.assertEquals(self.calculate(9911, 28302), 7042, "")

    def test0260(self):
        self.assertEquals(self.calculate(-32111, -29695), -12655, "")

    def test0261(self):
        self.assertEquals(self.calculate(23678, 5971), 20186, "")

    def test0262(self):
        self.assertEquals(self.calculate(-4103, 9622), -26394, "")

    def test0263(self):
        self.assertEquals(self.calculate(-24469, 12958), -6134, "")

    def test0264(self):
        self.assertEquals(self.calculate(-4592, -30145), 13808, "")

    def test0265(self):
        self.assertEquals(self.calculate(787, -2988), 7740, "")

    def test0266(self):
        self.assertEquals(self.calculate(-25884, 32424), -8800, "")

    def test0267(self):
        self.assertEquals(self.calculate(-4378, -8227), -26994, "")

    def test0268(self):
        self.assertEquals(self.calculate(26392, 1145), 6744, "")

    def test0269(self):
        self.assertEquals(self.calculate(2578, -28562), 29628, "")

    def test0270(self):
        self.assertEquals(self.calculate(-3245, -4015), -12989, "")

    def test0271(self):
        self.assertEquals(self.calculate(2827, -16992), 1504, "")

    def test0272(self):
        self.assertEquals(self.calculate(-26251, 21903), -28325, "")

    def test0273(self):
        self.assertEquals(self.calculate(-32290, -16658), -32668, "")

    def test0274(self):
        self.assertEquals(self.calculate(19592, 9108), -10592, "")

    def test0275(self):
        self.assertEquals(self.calculate(-11163, -31792), 16656, "")

    def test0276(self):
        self.assertEquals(self.calculate(21556, -343), 11860, "")

    def test0277(self):
        self.assertEquals(self.calculate(21653, -8360), -8648, "")

    def test0278(self):
        self.assertEquals(self.calculate(-11185, 19872), 29792, "")

    def test0279(self):
        self.assertEquals(self.calculate(11828, 1067), -27972, "")

    def test0280(self):
        self.assertEquals(self.calculate(18823, 7567), 23913, "")

    def test0281(self):
        self.assertEquals(self.calculate(26061, -5182), 21594, "")

    def test0282(self):
        self.assertEquals(self.calculate(-12331, 16661), 8569, "")

    def test0283(self):
        self.assertEquals(self.calculate(-29712, -19645), 28624, "")

    def test0284(self):
        self.assertEquals(self.calculate(27370, -23286), -220, "")

    def test0285(self):
        self.assertEquals(self.calculate(15557, 5235), -20353, "")

    def test0286(self):
        self.assertEquals(self.calculate(-20174, -28417), -24370, "")

    def test0287(self):
        self.assertEquals(self.calculate(-15737, 5576), 3192, "")

    def test0288(self):
        self.assertEquals(self.calculate(-16469, -11630), -27258, "")

    def test0289(self):
        self.assertEquals(self.calculate(-14732, 17837), 24676, "")

    def test0290(self):
        self.assertEquals(self.calculate(10288, -3110), -14112, "")

    def test0291(self):
        self.assertEquals(self.calculate(2202, 2778), 22308, "")

    def test0292(self):
        self.assertEquals(self.calculate(-16363, -7843), 15521, "")

    def test0293(self):
        self.assertEquals(self.calculate(-16376, -12102), 1488, "")

    def test0294(self):
        self.assertEquals(self.calculate(22325, -26168), -12696, "")

    def test0295(self):
        self.assertEquals(self.calculate(23747, 4140), 8580, "")

    def test0296(self):
        self.assertEquals(self.calculate(-2415, 5647), -6017, "")

    def test0297(self):
        self.assertEquals(self.calculate(17690, 4035), 10446, "")

    def test0298(self):
        self.assertEquals(self.calculate(-17412, -27519), 27132, "")

    def test0299(self):
        self.assertEquals(self.calculate(-5199, 19364), -10140, "")

    def test0300(self):
        self.assertEquals(self.calculate(15760, -8347), -17968, "")

    def test0301(self):
        self.assertEquals(self.calculate(16288, -1333), -19488, "")

    def test0302(self):
        self.assertEquals(self.calculate(-943, -15753), -21593, "")

    def test0303(self):
        self.assertEquals(self.calculate(9083, -1426), 23770, "")

    def test0304(self):
        self.assertEquals(self.calculate(-13136, -27203), -29200, "")

    def test0305(self):
        self.assertEquals(self.calculate(15713, 24926), 19102, "")

    def test0306(self):
        self.assertEquals(self.calculate(-17504, -30990), 7488, "")

    def test0307(self):
        self.assertEquals(self.calculate(14395, -7913), -6067, "")

    def test0308(self):
        self.assertEquals(self.calculate(5675, 10058), -2706, "")

    def test0309(self):
        self.assertEquals(self.calculate(455, -14677), 6637, "")

    def test0310(self):
        self.assertEquals(self.calculate(26977, 20448), 9184, "")

    def test0311(self):
        self.assertEquals(self.calculate(16916, 18416), 32448, "")

    def test0312(self):
        self.assertEquals(self.calculate(-9987, 13299), 24359, "")

    def test0313(self):
        self.assertEquals(self.calculate(-18647, 474), 8682, "")

    def test0314(self):
        self.assertEquals(self.calculate(2182, -13161), -12534, "")

    def test0315(self):
        self.assertEquals(self.calculate(-3872, -3004), 31616, "")

    def test0316(self):
        self.assertEquals(self.calculate(-28615, 3620), 26116, "")

    def test0317(self):
        self.assertEquals(self.calculate(24592, 496), 7936, "")

    def test0318(self):
        self.assertEquals(self.calculate(-12267, -31032), -29080, "")

    def test0319(self):
        self.assertEquals(self.calculate(22700, -29539), 29052, "")

    def test0320(self):
        self.assertEquals(self.calculate(1869, -26112), 20992, "")

    def test0321(self):
        self.assertEquals(self.calculate(-9501, -11488), 30048, "")

    def test0322(self):
        self.assertEquals(self.calculate(11750, 14330), 15516, "")

    def test0323(self):
        self.assertEquals(self.calculate(16069, 30790), -32290, "")

    def test0324(self):
        self.assertEquals(self.calculate(11662, 4248), -5040, "")

    def test0325(self):
        self.assertEquals(self.calculate(24151, -29230), 20062, "")

    def test0326(self):
        self.assertEquals(self.calculate(-15228, 6850), 21512, "")

    def test0327(self):
        self.assertEquals(self.calculate(26597, 2896), 20112, "")

    def test0328(self):
        self.assertEquals(self.calculate(29046, -2025), -32358, "")

    def test0329(self):
        self.assertEquals(self.calculate(8915, 23456), -15136, "")

    def test0330(self):
        self.assertEquals(self.calculate(3080, -6700), 7840, "")

    def test0331(self):
        self.assertEquals(self.calculate(-28107, 19308), 13660, "")

    def test0332(self):
        self.assertEquals(self.calculate(25512, -1401), -25192, "")

    def test0333(self):
        self.assertEquals(self.calculate(5910, -13533), -26110, "")

    def test0334(self):
        self.assertEquals(self.calculate(2795, -7444), -31068, "")

    def test0335(self):
        self.assertEquals(self.calculate(-14017, -15145), 16361, "")

    def test0336(self):
        self.assertEquals(self.calculate(-22815, 2941), 9949, "")

    def test0337(self):
        self.assertEquals(self.calculate(29182, -31583), -22338, "")

    def test0338(self):
        self.assertEquals(self.calculate(5189, -11396), -20372, "")

    def test0339(self):
        self.assertEquals(self.calculate(-11446, 1313), -20854, "")

    def test0340(self):
        self.assertEquals(self.calculate(4544, 28801), -3648, "")

    def test0341(self):
        self.assertEquals(self.calculate(28420, -17616), -17216, "")

    def test0342(self):
        self.assertEquals(self.calculate(18223, 15525), -6837, "")

    def test0343(self):
        self.assertEquals(self.calculate(22264, 8446), 18960, "")

    def test0344(self):
        self.assertEquals(self.calculate(-2722, -546), -21116, "")

    def test0345(self):
        self.assertEquals(self.calculate(15798, -5590), 31708, "")

    def test0346(self):
        self.assertEquals(self.calculate(32632, 5569), -3720, "")

    def test0347(self):
        self.assertEquals(self.calculate(-30717, -3923), -17913, "")

    def test0348(self):
        self.assertEquals(self.calculate(5928, -23141), -13000, "")

    def test0349(self):
        self.assertEquals(self.calculate(-31979, -18028), -2780, "")

    def test0350(self):
        self.assertEquals(self.calculate(1449, -7081), 28783, "")

    def test0351(self):
        self.assertEquals(self.calculate(8982, -3069), 24898, "")

    def test0352(self):
        self.assertEquals(self.calculate(13516, -29017), -26348, "")

    def test0353(self):
        self.assertEquals(self.calculate(-4107, 31411), -30129, "")

    def test0354(self):
        self.assertEquals(self.calculate(-9350, -15694), 3796, "")

    def test0355(self):
        self.assertEquals(self.calculate(-9590, 12268), -13000, "")

    def test0356(self):
        self.assertEquals(self.calculate(1840, 2276), -6464, "")

    def test0357(self):
        self.assertEquals(self.calculate(10664, 24484), 1952, "")

    def test0358(self):
        self.assertEquals(self.calculate(25173, 3344), 30288, "")

    def test0359(self):
        self.assertEquals(self.calculate(31392, -22211), -10208, "")

    def test0360(self):
        self.assertEquals(self.calculate(12864, -7157), 10432, "")

    def test0361(self):
        self.assertEquals(self.calculate(-11480, -28476), 10912, "")

    def test0362(self):
        self.assertEquals(self.calculate(22960, -18538), 23840, "")

    def test0363(self):
        self.assertEquals(self.calculate(2308, -27123), -13004, "")

    def test0364(self):
        self.assertEquals(self.calculate(27258, -1195), -1918, "")

    def test0365(self):
        self.assertEquals(self.calculate(-13657, -4022), 9286, "")

    def test0366(self):
        self.assertEquals(self.calculate(-10472, -16286), 22320, "")

    def test0367(self):
        self.assertEquals(self.calculate(-10328, -18004), 19680, "")

    def test0368(self):
        self.assertEquals(self.calculate(20922, -16479), 11258, "")

    def test0369(self):
        self.assertEquals(self.calculate(22752, 14151), -14816, "")

    def test0370(self):
        self.assertEquals(self.calculate(11639, 604), 17604, "")

    def test0371(self):
        self.assertEquals(self.calculate(8826, -16188), -6808, "")

    def test0372(self):
        self.assertEquals(self.calculate(1150, -19281), -21982, "")

    def test0373(self):
        self.assertEquals(self.calculate(-18116, -13182), -8072, "")

    def test0374(self):
        self.assertEquals(self.calculate(21363, 24526), -11382, "")

    def test0375(self):
        self.assertEquals(self.calculate(10087, 30809), -1329, "")

    def test0376(self):
        self.assertEquals(self.calculate(1674, 18674), -396, "")

    def test0377(self):
        self.assertEquals(self.calculate(-18126, 7384), -17872, "")

    def test0378(self):
        self.assertEquals(self.calculate(26612, 15490), -1560, "")

    def test0379(self):
        self.assertEquals(self.calculate(-10475, -11472), -23824, "")

    def test0380(self):
        self.assertEquals(self.calculate(-22453, 19396), -11668, "")

    def test0381(self):
        self.assertEquals(self.calculate(13713, -4978), 25198, "")

    def test0382(self):
        self.assertEquals(self.calculate(29435, -2024), -4216, "")

    def test0383(self):
        self.assertEquals(self.calculate(-17706, -4828), 25624, "")

    def test0384(self):
        self.assertEquals(self.calculate(9841, -2783), 6545, "")

    def test0385(self):
        self.assertEquals(self.calculate(16695, -18075), 31155, "")

    def test0386(self):
        self.assertEquals(self.calculate(511, -15331), 30179, "")

    def test0387(self):
        self.assertEquals(self.calculate(24089, -21195), 24621, "")

    def test0388(self):
        self.assertEquals(self.calculate(26006, -18215), -5082, "")

    def test0389(self):
        self.assertEquals(self.calculate(-11480, 24336), 2688, "")

    def test0390(self):
        self.assertEquals(self.calculate(-25583, -15790), -8334, "")

    def test0391(self):
        self.assertEquals(self.calculate(-10394, 3810), -17396, "")

    def test0392(self):
        self.assertEquals(self.calculate(-11863, 32566), 4262, "")

    def test0393(self):
        self.assertEquals(self.calculate(-24874, 752), -27488, "")

    def test0394(self):
        self.assertEquals(self.calculate(18119, -7436), 9132, "")

    def test0395(self):
        self.assertEquals(self.calculate(-19306, -24532), -13880, "")

    def test0396(self):
        self.assertEquals(self.calculate(8307, 3421), -24377, "")

    def test0397(self):
        self.assertEquals(self.calculate(-30628, 56), -11232, "")

    def test0398(self):
        self.assertEquals(self.calculate(-3901, -17750), -28802, "")

    def test0399(self):
        self.assertEquals(self.calculate(-18273, 20921), -17945, "")

    def test0400(self):
        self.assertEquals(self.calculate(-16431, 11499), 219, "")

    def test0401(self):
        self.assertEquals(self.calculate(32682, -6315), -13966, "")

    def test0402(self):
        self.assertEquals(self.calculate(-1030, -2748), 12392, "")

    def test0403(self):
        self.assertEquals(self.calculate(23501, 25202), 23370, "")

    def test0404(self):
        self.assertEquals(self.calculate(498, -28870), -24876, "")

    def test0405(self):
        self.assertEquals(self.calculate(-19068, 15903), -3332, "")

    def test0406(self):
        self.assertEquals(self.calculate(15906, -18164), 31640, "")

    def test0407(self):
        self.assertEquals(self.calculate(-17150, -9869), -26138, "")

    def test0408(self):
        self.assertEquals(self.calculate(11957, -25876), -3876, "")

    def test0409(self):
        self.assertEquals(self.calculate(-23296, 8856), -2048, "")

    def test0410(self):
        self.assertEquals(self.calculate(16180, 1132), 31216, "")

    def test0411(self):
        self.assertEquals(self.calculate(14698, -22632), 15600, "")

    def test0412(self):
        self.assertEquals(self.calculate(6843, -13247), -12933, "")

    def test0413(self):
        self.assertEquals(self.calculate(19374, -16091), 7718, "")

    def test0414(self):
        self.assertEquals(self.calculate(1082, -9880), -7792, "")

    def test0415(self):
        self.assertEquals(self.calculate(25458, 29586), -4860, "")

    def test0416(self):
        self.assertEquals(self.calculate(16352, -31631), -20000, "")

    def test0417(self):
        self.assertEquals(self.calculate(28297, -12208), -9520, "")

    def test0418(self):
        self.assertEquals(self.calculate(5878, 17983), -5494, "")

    def test0419(self):
        self.assertEquals(self.calculate(-20630, 23996), 21464, "")

    def test0420(self):
        self.assertEquals(self.calculate(-10724, 21782), -19864, "")

    def test0421(self):
        self.assertEquals(self.calculate(15043, 27477), 959, "")

    def test0422(self):
        self.assertEquals(self.calculate(18361, 24729), 15761, "")

    def test0423(self):
        self.assertEquals(self.calculate(24995, -25693), -9271, "")

    def test0424(self):
        self.assertEquals(self.calculate(-9318, -10659), -32014, "")

    def test0425(self):
        self.assertEquals(self.calculate(-21531, 2116), -12076, "")

    def test0426(self):
        self.assertEquals(self.calculate(-4841, -22274), 21714, "")

    def test0427(self):
        self.assertEquals(self.calculate(8561, 14954), 29386, "")

    def test0428(self):
        self.assertEquals(self.calculate(-4619, -29706), -20370, "")

    def test0429(self):
        self.assertEquals(self.calculate(-25782, 30186), -15452, "")

    def test0430(self):
        self.assertEquals(self.calculate(27248, -15848), -9600, "")

    def test0431(self):
        self.assertEquals(self.calculate(3847, -14561), 17113, "")

    def test0432(self):
        self.assertEquals(self.calculate(-29703, 13545), -1631, "")

    def test0433(self):
        self.assertEquals(self.calculate(-2599, 7631), 24439, "")

    def test0434(self):
        self.assertEquals(self.calculate(5656, -5232), 30080, "")

    def test0435(self):
        self.assertEquals(self.calculate(35, 480), 16800, "")

    def test0436(self):
        self.assertEquals(self.calculate(-13195, -14713), 20403, "")

    def test0437(self):
        self.assertEquals(self.calculate(1740, -1100), -13456, "")

    def test0438(self):
        self.assertEquals(self.calculate(2590, -28797), -4262, "")

    def test0439(self):
        self.assertEquals(self.calculate(-2890, -21660), 10520, "")

    def test0440(self):
        self.assertEquals(self.calculate(-20666, -23713), -25350, "")

    def test0441(self):
        self.assertEquals(self.calculate(25905, -31348), -13364, "")

    def test0442(self):
        self.assertEquals(self.calculate(822, 6201), -14586, "")

    def test0443(self):
        self.assertEquals(self.calculate(-15322, -19588), -27544, "")

    def test0444(self):
        self.assertEquals(self.calculate(-6559, -7483), -5467, "")

    def test0445(self):
        self.assertEquals(self.calculate(13956, 17004), 1968, "")

    def test0446(self):
        self.assertEquals(self.calculate(-21444, -32680), 13472, "")

    def test0447(self):
        self.assertEquals(self.calculate(-3489, -13378), 14210, "")

    def test0448(self):
        self.assertEquals(self.calculate(15391, 17865), -28841, "")

    def test0449(self):
        self.assertEquals(self.calculate(21599, 31403), -24203, "")

    def test0450(self):
        self.assertEquals(self.calculate(-13409, -15579), -29957, "")

    def test0451(self):
        self.assertEquals(self.calculate(4267, 18059), -12583, "")

    def test0452(self):
        self.assertEquals(self.calculate(-16658, -9098), -30284, "")

    def test0453(self):
        self.assertEquals(self.calculate(-26122, 28749), -4354, "")

    def test0454(self):
        self.assertEquals(self.calculate(-15423, 28560), -13424, "")

    def test0455(self):
        self.assertEquals(self.calculate(13024, -10650), -31424, "")

    def test0456(self):
        self.assertEquals(self.calculate(12252, 10094), 5256, "")

    def test0457(self):
        self.assertEquals(self.calculate(27578, 10894), 17708, "")

    def test0458(self):
        self.assertEquals(self.calculate(14687, -21829), -411, "")

    def test0459(self):
        self.assertEquals(self.calculate(30382, 19072), -23808, "")

    def test0460(self):
        self.assertEquals(self.calculate(-1799, -32739), -19403, "")

    def test0461(self):
        self.assertEquals(self.calculate(25776, -27088), 256, "")

    def test0462(self):
        self.assertEquals(self.calculate(29224, 5150), -32592, "")

    def test0463(self):
        self.assertEquals(self.calculate(10593, 6863), 20335, "")

    def test0464(self):
        self.assertEquals(self.calculate(-632, -24048), -6016, "")

    def test0465(self):
        self.assertEquals(self.calculate(31415, 19852), 10004, "")

    def test0466(self):
        self.assertEquals(self.calculate(24167, 24607), 3705, "")

    def test0467(self):
        self.assertEquals(self.calculate(7105, -30288), 23984, "")

    def test0468(self):
        self.assertEquals(self.calculate(-22536, 21954), -24080, "")

    def test0469(self):
        self.assertEquals(self.calculate(1125, -23859), 28385, "")

    def test0470(self):
        self.assertEquals(self.calculate(29187, 28763), -10479, "")

    def test0471(self):
        self.assertEquals(self.calculate(31012, 17536), 8704, "")

    def test0472(self):
        self.assertEquals(self.calculate(4712, 10809), 10536, "")

    def test0473(self):
        self.assertEquals(self.calculate(-5540, -18523), -11956, "")

    def test0474(self):
        self.assertEquals(self.calculate(-11691, -4660), 19644, "")

    def test0475(self):
        self.assertEquals(self.calculate(-1986, -5378), -1660, "")

    def test0476(self):
        self.assertEquals(self.calculate(54, -4971), -6290, "")

    def test0477(self):
        self.assertEquals(self.calculate(3394, -3671), -7534, "")

    def test0478(self):
        self.assertEquals(self.calculate(12965, 6300), 21644, "")

    def test0479(self):
        self.assertEquals(self.calculate(20351, 17431), -8087, "")

    def test0480(self):
        self.assertEquals(self.calculate(25665, -22992), -3536, "")

    def test0481(self):
        self.assertEquals(self.calculate(25827, 21305), 3979, "")

    def test0482(self):
        self.assertEquals(self.calculate(-2246, 21637), 31010, "")

    def test0483(self):
        self.assertEquals(self.calculate(16728, 29909), 15928, "")

    def test0484(self):
        self.assertEquals(self.calculate(29412, -23195), 18420, "")

    def test0485(self):
        self.assertEquals(self.calculate(24097, 4318), -20322, "")

    def test0486(self):
        self.assertEquals(self.calculate(-13701, -1220), 3540, "")

    def test0487(self):
        self.assertEquals(self.calculate(23997, -17015), -19675, "")

    def test0488(self):
        self.assertEquals(self.calculate(18232, -14192), -12416, "")

    def test0489(self):
        self.assertEquals(self.calculate(19355, 17019), 18809, "")

    def test0490(self):
        self.assertEquals(self.calculate(-29519, -7546), -6490, "")

    def test0491(self):
        self.assertEquals(self.calculate(14386, -4424), -8208, "")

    def test0492(self):
        self.assertEquals(self.calculate(-8, 20686), 31120, "")

    def test0493(self):
        self.assertEquals(self.calculate(-5367, -26802), -5186, "")

    def test0494(self):
        self.assertEquals(self.calculate(8831, -4698), -3750, "")

    def test0495(self):
        self.assertEquals(self.calculate(-28820, 4582), 1800, "")

    def test0496(self):
        self.assertEquals(self.calculate(-31682, 18500), -28552, "")

    def test0497(self):
        self.assertEquals(self.calculate(-9888, -5884), -14976, "")

    def test0498(self):
        self.assertEquals(self.calculate(5453, -24762), -23026, "")

    def test0499(self):
        self.assertEquals(self.calculate(-14912, -31706), 23168, "")

    def test0500(self):
        self.assertEquals(self.calculate(-13935, -19083), -23483, "")

    def test0501(self):
        self.assertEquals(self.calculate(13950, -12072), 23120, "")

    def test0502(self):
        self.assertEquals(self.calculate(-12151, -17500), -21820, "")

    def test0503(self):
        self.assertEquals(self.calculate(11323, -5657), -25539, "")

    def test0504(self):
        self.assertEquals(self.calculate(-16712, -29270), -464, "")

    def test0505(self):
        self.assertEquals(self.calculate(-7586, 30997), -74, "")

    def test0506(self):
        self.assertEquals(self.calculate(-11608, -29579), 9928, "")

    def test0507(self):
        self.assertEquals(self.calculate(-4314, -87), -17898, "")

    def test0508(self):
        self.assertEquals(self.calculate(26520, -20344), -30528, "")

    def test0509(self):
        self.assertEquals(self.calculate(31093, -5379), -1375, "")

    def test0510(self):
        self.assertEquals(self.calculate(4226, -17274), 7180, "")

    def test0511(self):
        self.assertEquals(self.calculate(-5829, 29386), 20110, "")

    def test0512(self):
        self.assertEquals(self.calculate(-25106, 21749), 15558, "")

    def test0513(self):
        self.assertEquals(self.calculate(10288, -29618), 32416, "")

    def test0514(self):
        self.assertEquals(self.calculate(25598, 14583), 2578, "")

    def test0515(self):
        self.assertEquals(self.calculate(11616, 14887), -22112, "")

    def test0516(self):
        self.assertEquals(self.calculate(27285, -3460), 31276, "")

    def test0517(self):
        self.assertEquals(self.calculate(14617, -12618), -19002, "")

    def test0518(self):
        self.assertEquals(self.calculate(-7396, -14476), -21328, "")

    def test0519(self):
        self.assertEquals(self.calculate(-5563, 21857), -21211, "")

    def test0520(self):
        self.assertEquals(self.calculate(16254, -29455), -21090, "")

    def test0521(self):
        self.assertEquals(self.calculate(14552, -29106), 8656, "")

    def test0522(self):
        self.assertEquals(self.calculate(-22629, 7172), -28052, "")

    def test0523(self):
        self.assertEquals(self.calculate(11639, 4631), 29617, "")

    def test0524(self):
        self.assertEquals(self.calculate(17875, 23802), 1038, "")

    def test0525(self):
        self.assertEquals(self.calculate(20742, -5683), 22478, "")

    def test0526(self):
        self.assertEquals(self.calculate(-26663, 7605), -3731, "")

    def test0527(self):
        self.assertEquals(self.calculate(-30878, -6725), -29034, "")

    def test0528(self):
        self.assertEquals(self.calculate(-10313, -7370), -14950, "")

    def test0529(self):
        self.assertEquals(self.calculate(26587, -22637), 32705, "")

    def test0530(self):
        self.assertEquals(self.calculate(-26037, 20721), -20325, "")

    def test0531(self):
        self.assertEquals(self.calculate(32485, 20172), -7044, "")

    def test0532(self):
        self.assertEquals(self.calculate(687, 21261), -8221, "")

    def test0533(self):
        self.assertEquals(self.calculate(-4040, -27605), -18072, "")

    def test0534(self):
        self.assertEquals(self.calculate(5524, 3848), 22688, "")

    def test0535(self):
        self.assertEquals(self.calculate(-9747, -1871), 17629, "")

    def test0536(self):
        self.assertEquals(self.calculate(12557, 23329), -3667, "")

    def test0537(self):
        self.assertEquals(self.calculate(-9257, -22651), 30643, "")

    def test0538(self):
        self.assertEquals(self.calculate(3784, -13582), -14064, "")

    def test0539(self):
        self.assertEquals(self.calculate(4467, -7461), 29537, "")

    def test0540(self):
        self.assertEquals(self.calculate(-22720, 21273), 5440, "")

    def test0541(self):
        self.assertEquals(self.calculate(-8774, -5695), 29498, "")

    def test0542(self):
        self.assertEquals(self.calculate(-9947, 24144), 29072, "")

    def test0543(self):
        self.assertEquals(self.calculate(-9113, -6494), 814, "")

    def test0544(self):
        self.assertEquals(self.calculate(11839, 16931), -28515, "")

    def test0545(self):
        self.assertEquals(self.calculate(2509, 24480), 13088, "")

    def test0546(self):
        self.assertEquals(self.calculate(5350, -30990), 9580, "")

    def test0547(self):
        self.assertEquals(self.calculate(27347, 25258), -18914, "")

    def test0548(self):
        self.assertEquals(self.calculate(11031, 18166), -19942, "")

    def test0549(self):
        self.assertEquals(self.calculate(-5273, -9570), -110, "")

    def test0550(self):
        self.assertEquals(self.calculate(15193, 26838), -15258, "")

    def test0551(self):
        self.assertEquals(self.calculate(26372, -20831), -32380, "")

    def test0552(self):
        self.assertEquals(self.calculate(-15781, 30576), 21712, "")

    def test0553(self):
        self.assertEquals(self.calculate(12991, -32365), 25261, "")

    def test0554(self):
        self.assertEquals(self.calculate(2888, -14236), -22496, "")

    def test0555(self):
        self.assertEquals(self.calculate(-8077, -23929), 8869, "")

    def test0556(self):
        self.assertEquals(self.calculate(2687, -25166), 12110, "")

    def test0557(self):
        self.assertEquals(self.calculate(27147, -21057), -29387, "")

    def test0558(self):
        self.assertEquals(self.calculate(24287, -5409), 31297, "")

    def test0559(self):
        self.assertEquals(self.calculate(11058, -4107), 1242, "")

    def test0560(self):
        self.assertEquals(self.calculate(-923, 4559), -13653, "")

    def test0561(self):
        self.assertEquals(self.calculate(28841, -1632), -13664, "")

    def test0562(self):
        self.assertEquals(self.calculate(13167, -4490), -6358, "")

    def test0563(self):
        self.assertEquals(self.calculate(-8304, 16885), -31536, "")

    def test0564(self):
        self.assertEquals(self.calculate(22206, 7034), 24716, "")

    def test0565(self):
        self.assertEquals(self.calculate(-4638, 6274), -828, "")

    def test0566(self):
        self.assertEquals(self.calculate(-12344, 9851), -31464, "")

    def test0567(self):
        self.assertEquals(self.calculate(26949, 12948), 21988, "")

    def test0568(self):
        self.assertEquals(self.calculate(10992, 22333), -13520, "")

    def test0569(self):
        self.assertEquals(self.calculate(-24238, 12967), 16510, "")

    def test0570(self):
        self.assertEquals(self.calculate(20693, 25199), -27045, "")

    def test0571(self):
        self.assertEquals(self.calculate(9730, 10793), 27218, "")

    def test0572(self):
        self.assertEquals(self.calculate(-28664, 9546), -13744, "")

    def test0573(self):
        self.assertEquals(self.calculate(32333, 30266), 7026, "")

    def test0574(self):
        self.assertEquals(self.calculate(137, 74), 10138, "")

    def test0575(self):
        self.assertEquals(self.calculate(17920, -602), 25600, "")

    def test0576(self):
        self.assertEquals(self.calculate(-5625, 23366), 31466, "")

    def test0577(self):
        self.assertEquals(self.calculate(29888, -9173), -25536, "")

    def test0578(self):
        self.assertEquals(self.calculate(-25228, 32075), -15108, "")

    def test0579(self):
        self.assertEquals(self.calculate(27435, -13997), -32271, "")

    def test0580(self):
        self.assertEquals(self.calculate(-21799, 5373), -13195, "")

    def test0581(self):
        self.assertEquals(self.calculate(-20742, 30062), 29036, "")

    def test0582(self):
        self.assertEquals(self.calculate(18422, 24376), 2000, "")

    def test0583(self):
        self.assertEquals(self.calculate(21790, 5034), -16404, "")

    def test0584(self):
        self.assertEquals(self.calculate(-30239, -17759), 12417, "")

    def test0585(self):
        self.assertEquals(self.calculate(-19586, -21097), 1362, "")

    def test0586(self):
        self.assertEquals(self.calculate(8573, -10151), 7285, "")

    def test0587(self):
        self.assertEquals(self.calculate(24252, -6791), -3364, "")

    def test0588(self):
        self.assertEquals(self.calculate(-8744, -8963), -8584, "")

    def test0589(self):
        self.assertEquals(self.calculate(3838, 4540), -8056, "")

    def test0590(self):
        self.assertEquals(self.calculate(-24085, 17707), -30343, "")

    def test0591(self):
        self.assertEquals(self.calculate(11349, 17409), -16299, "")

    def test0592(self):
        self.assertEquals(self.calculate(28668, 31729), -32708, "")

    def test0593(self):
        self.assertEquals(self.calculate(12055, -17672), 21576, "")

    def test0594(self):
        self.assertEquals(self.calculate(14403, 2712), 1480, "")

    def test0595(self):
        self.assertEquals(self.calculate(6026, 2995), 25470, "")

    def test0596(self):
        self.assertEquals(self.calculate(-13565, 27038), -31014, "")

    def test0597(self):
        self.assertEquals(self.calculate(-30591, 23565), 19085, "")

    def test0598(self):
        self.assertEquals(self.calculate(-11995, 31206), 25662, "")

    def test0599(self):
        self.assertEquals(self.calculate(29391, -20290), -31326, "")

    def test0600(self):
        self.assertEquals(self.calculate(-29318, 24501), 19778, "")

    def test0601(self):
        self.assertEquals(self.calculate(-28431, 9350), -15834, "")

    def test0602(self):
        self.assertEquals(self.calculate(-4253, 4612), -19572, "")

    def test0603(self):
        self.assertEquals(self.calculate(28194, -10845), 27046, "")

    def test0604(self):
        self.assertEquals(self.calculate(12466, 22178), -25436, "")

    def test0605(self):
        self.assertEquals(self.calculate(-30511, 26338), 3714, "")

    def test0606(self):
        self.assertEquals(self.calculate(10484, 19909), -6204, "")

    def test0607(self):
        self.assertEquals(self.calculate(5227, -31057), -2267, "")

    def test0608(self):
        self.assertEquals(self.calculate(-22208, 6945), -28352, "")

    def test0609(self):
        self.assertEquals(self.calculate(-26676, -22706), 21544, "")

    def test0610(self):
        self.assertEquals(self.calculate(9759, 11836), -32444, "")

    def test0611(self):
        self.assertEquals(self.calculate(7296, 7019), 27008, "")

    def test0612(self):
        self.assertEquals(self.calculate(-14346, 31778), -18772, "")

    def test0613(self):
        self.assertEquals(self.calculate(19744, 8098), -20928, "")

    def test0614(self):
        self.assertEquals(self.calculate(30487, 12969), 7215, "")

    def test0615(self):
        self.assertEquals(self.calculate(-3575, -31098), 26294, "")

    def test0616(self):
        self.assertEquals(self.calculate(6073, 14370), -24942, "")

    def test0617(self):
        self.assertEquals(self.calculate(-4176, -13778), -3680, "")

    def test0618(self):
        self.assertEquals(self.calculate(2313, 7326), -28786, "")

    def test0619(self):
        self.assertEquals(self.calculate(-991, 25698), 26786, "")

    def test0620(self):
        self.assertEquals(self.calculate(19108, 31210), -16920, "")

    def test0621(self):
        self.assertEquals(self.calculate(31437, 24874), -11614, "")

    def test0622(self):
        self.assertEquals(self.calculate(28304, 24180), -1728, "")

    def test0623(self):
        self.assertEquals(self.calculate(7129, -13005), 20795, "")

    def test0624(self):
        self.assertEquals(self.calculate(-6207, 15915), -21653, "")

    def test0625(self):
        self.assertEquals(self.calculate(6685, 5908), -23228, "")

    def test0626(self):
        self.assertEquals(self.calculate(28325, 15502), 2950, "")

    def test0627(self):
        self.assertEquals(self.calculate(-29765, -31079), 25795, "")

    def test0628(self):
        self.assertEquals(self.calculate(28018, 9577), 24002, "")

    def test0629(self):
        self.assertEquals(self.calculate(5919, 773), -12133, "")

    def test0630(self):
        self.assertEquals(self.calculate(8915, 10803), -29175, "")

    def test0631(self):
        self.assertEquals(self.calculate(-30245, 881), 27307, "")

    def test0632(self):
        self.assertEquals(self.calculate(-23079, 27008), -4736, "")

    def test0633(self):
        self.assertEquals(self.calculate(-17392, 24916), -15040, "")

    def test0634(self):
        self.assertEquals(self.calculate(5875, -26198), 30814, "")

    def test0635(self):
        self.assertEquals(self.calculate(8049, 16423), 2615, "")

    def test0636(self):
        self.assertEquals(self.calculate(5327, -1154), 13026, "")

    def test0637(self):
        self.assertEquals(self.calculate(-9398, 17039), -28074, "")

    def test0638(self):
        self.assertEquals(self.calculate(-29222, -12569), 27574, "")

    def test0639(self):
        self.assertEquals(self.calculate(-21880, -3610), 15920, "")

    def test0640(self):
        self.assertEquals(self.calculate(8441, -22638), 15618, "")

    def test0641(self):
        self.assertEquals(self.calculate(23309, -6440), -32520, "")

    def test0642(self):
        self.assertEquals(self.calculate(-30544, -13243), 6000, "")

    def test0643(self):
        self.assertEquals(self.calculate(-10631, 31151), -12873, "")

    def test0644(self):
        self.assertEquals(self.calculate(-8191, -30006), 19146, "")

    def test0645(self):
        self.assertEquals(self.calculate(-11984, -19827), -26768, "")

    def test0646(self):
        self.assertEquals(self.calculate(-32489, -29816), 4408, "")

    def test0647(self):
        self.assertEquals(self.calculate(26905, -27742), -9006, "")

    def test0648(self):
        self.assertEquals(self.calculate(2783, -19347), 27891, "")

    def test0649(self):
        self.assertEquals(self.calculate(-3381, 15070), -30198, "")

    def test0650(self):
        self.assertEquals(self.calculate(-4041, 31096), -26424, "")

    def test0651(self):
        self.assertEquals(self.calculate(-4294, 23595), 1726, "")

    def test0652(self):
        self.assertEquals(self.calculate(12502, -9967), -23498, "")

    def test0653(self):
        self.assertEquals(self.calculate(-16432, -31793), -30416, "")

    def test0654(self):
        self.assertEquals(self.calculate(-13635, 31479), -20901, "")

    def test0655(self):
        self.assertEquals(self.calculate(-4934, -28840), 17904, "")

    def test0656(self):
        self.assertEquals(self.calculate(7498, -12453), 16206, "")

    def test0657(self):
        self.assertEquals(self.calculate(-13494, 19793), -27542, "")

    def test0658(self):
        self.assertEquals(self.calculate(25067, 6784), -11392, "")

    def test0659(self):
        self.assertEquals(self.calculate(11449, 17568), 6048, "")

    def test0660(self):
        self.assertEquals(self.calculate(1189, -12216), 24168, "")

    def test0661(self):
        self.assertEquals(self.calculate(5658, -361), -10922, "")

    def test0662(self):
        self.assertEquals(self.calculate(-11804, 1408), 26112, "")

    def test0663(self):
        self.assertEquals(self.calculate(-22697, 13306), -16394, "")

    def test0664(self):
        self.assertEquals(self.calculate(15057, 15205), 24437, "")

    def test0665(self):
        self.assertEquals(self.calculate(19193, -24817), 2967, "")

    def test0666(self):
        self.assertEquals(self.calculate(-25404, -988), -1136, "")

    def test0667(self):
        self.assertEquals(self.calculate(9516, -28324), 18384, "")

    def test0668(self):
        self.assertEquals(self.calculate(27552, 24144), 25088, "")

    def test0669(self):
        self.assertEquals(self.calculate(-29872, -22926), -5728, "")

    def test0670(self):
        self.assertEquals(self.calculate(28833, -2423), -983, "")

    def test0671(self):
        self.assertEquals(self.calculate(-4145, 10855), 29257, "")

    def test0672(self):
        self.assertEquals(self.calculate(12470, -13510), 23356, "")

    def test0673(self):
        self.assertEquals(self.calculate(16048, 2001), -592, "")

    def test0674(self):
        self.assertEquals(self.calculate(-2941, -27574), 27102, "")

    def test0675(self):
        self.assertEquals(self.calculate(14346, 20177), -13270, "")

    def test0676(self):
        self.assertEquals(self.calculate(1400, -16342), -6736, "")

    def test0677(self):
        self.assertEquals(self.calculate(-17582, 24824), 14192, "")

    def test0678(self):
        self.assertEquals(self.calculate(27409, 3433), -14599, "")

    def test0679(self):
        self.assertEquals(self.calculate(28801, 17913), 12921, "")

    def test0680(self):
        self.assertEquals(self.calculate(3898, 14795), -770, "")

    def test0681(self):
        self.assertEquals(self.calculate(-6772, -15915), -30340, "")

    def test0682(self):
        self.assertEquals(self.calculate(-11302, -3264), -7040, "")

    def test0683(self):
        self.assertEquals(self.calculate(-3323, 14336), 6144, "")

    def test0684(self):
        self.assertEquals(self.calculate(-1841, 4695), 7257, "")

    def test0685(self):
        self.assertEquals(self.calculate(-5686, -31412), 23032, "")

    def test0686(self):
        self.assertEquals(self.calculate(-30746, 31862), 3076, "")

    def test0687(self):
        self.assertEquals(self.calculate(1609, 27954), 20290, "")

    def test0688(self):
        self.assertEquals(self.calculate(-18090, -17727), 13782, "")

    def test0689(self):
        self.assertEquals(self.calculate(17104, -17985), 10544, "")

    def test0690(self):
        self.assertEquals(self.calculate(-23315, -18899), 31657, "")

    def test0691(self):
        self.assertEquals(self.calculate(-18594, -23076), 10952, "")

    def test0692(self):
        self.assertEquals(self.calculate(21199, -9889), 12753, "")

    def test0693(self):
        self.assertEquals(self.calculate(-32429, 27494), 14354, "")

    def test0694(self):
        self.assertEquals(self.calculate(-3061, -11617), -26411, "")

    def test0695(self):
        self.assertEquals(self.calculate(-10928, 21869), 25360, "")

    def test0696(self):
        self.assertEquals(self.calculate(22388, 20662), 27768, "")

    def test0697(self):
        self.assertEquals(self.calculate(-15759, -26488), 25608, "")

    def test0698(self):
        self.assertEquals(self.calculate(-17242, -3790), 7788, "")

    def test0699(self):
        self.assertEquals(self.calculate(-4502, 1933), 13922, "")

    def test0700(self):
        self.assertEquals(self.calculate(20783, -14397), 24525, "")

    def test0701(self):
        self.assertEquals(self.calculate(31263, 23123), 32269, "")

    def test0702(self):
        self.assertEquals(self.calculate(-27515, 1568), -20832, "")

    def test0703(self):
        self.assertEquals(self.calculate(-7973, 24717), -1889, "")

    def test0704(self):
        self.assertEquals(self.calculate(-6800, 15859), 31056, "")

    def test0705(self):
        self.assertEquals(self.calculate(-4418, -32568), -31632, "")

    def test0706(self):
        self.assertEquals(self.calculate(-26730, -29593), 1370, "")

    def test0707(self):
        self.assertEquals(self.calculate(-17942, -10328), -30832, "")

    def test0708(self):
        self.assertEquals(self.calculate(18090, -30052), -19560, "")

    def test0709(self):
        self.assertEquals(self.calculate(-23958, 13834), -19420, "")

    def test0710(self):
        self.assertEquals(self.calculate(13659, 18122), -1074, "")

    def test0711(self):
        self.assertEquals(self.calculate(-20991, 1815), -22249, "")

    def test0712(self):
        self.assertEquals(self.calculate(-16397, -15455), -12077, "")

    def test0713(self):
        self.assertEquals(self.calculate(-4199, -26207), 8249, "")

    def test0714(self):
        self.assertEquals(self.calculate(1522, -21688), 21008, "")

    def test0715(self):
        self.assertEquals(self.calculate(15653, 2050), -23990, "")

    def test0716(self):
        self.assertEquals(self.calculate(6260, -1065), 17772, "")

    def test0717(self):
        self.assertEquals(self.calculate(-11561, 5228), -16716, "")

    def test0718(self):
        self.assertEquals(self.calculate(-8697, 5978), -20618, "")

    def test0719(self):
        self.assertEquals(self.calculate(12832, -26637), 29792, "")

    def test0720(self):
        self.assertEquals(self.calculate(5109, 29497), -32627, "")

    def test0721(self):
        self.assertEquals(self.calculate(-22947, -15099), -12079, "")

    def test0722(self):
        self.assertEquals(self.calculate(26045, -9367), 27013, "")

    def test0723(self):
        self.assertEquals(self.calculate(-10112, -15946), 27392, "")

    def test0724(self):
        self.assertEquals(self.calculate(-31836, 1808), -18880, "")

    def test0725(self):
        self.assertEquals(self.calculate(-472, 27083), -3656, "")

    def test0726(self):
        self.assertEquals(self.calculate(12918, 24155), 17394, "")

    def test0727(self):
        self.assertEquals(self.calculate(3541, -29516), 13764, "")

    def test0728(self):
        self.assertEquals(self.calculate(-32216, 2603), 27832, "")

    def test0729(self):
        self.assertEquals(self.calculate(-3251, 7009), 20269, "")

    def test0730(self):
        self.assertEquals(self.calculate(32224, 16235), -17248, "")

    def test0731(self):
        self.assertEquals(self.calculate(7114, 7245), 29634, "")

    def test0732(self):
        self.assertEquals(self.calculate(14117, -30343), -8835, "")

    def test0733(self):
        self.assertEquals(self.calculate(9552, -5010), -14240, "")

    def test0734(self):
        self.assertEquals(self.calculate(-31007, -6999), 28297, "")

    def test0735(self):
        self.assertEquals(self.calculate(-24611, -31230), -4678, "")

    def test0736(self):
        self.assertEquals(self.calculate(-3509, 5017), 24531, "")

    def test0737(self):
        self.assertEquals(self.calculate(16425, 23778), 24626, "")

    def test0738(self):
        self.assertEquals(self.calculate(-2460, 3559), 26684, "")

    def test0739(self):
        self.assertEquals(self.calculate(-27100, 22640), 4032, "")

    def test0740(self):
        self.assertEquals(self.calculate(19140, 9709), -29836, "")

    def test0741(self):
        self.assertEquals(self.calculate(23349, -1588), 15164, "")

    def test0742(self):
        self.assertEquals(self.calculate(25862, 11821), -10738, "")

    def test0743(self):
        self.assertEquals(self.calculate(-12835, 9305), -23083, "")

    def test0744(self):
        self.assertEquals(self.calculate(-13243, 8790), -14034, "")

    def test0745(self):
        self.assertEquals(self.calculate(-16568, 19711), -5960, "")

    def test0746(self):
        self.assertEquals(self.calculate(20522, 23699), 8222, "")

    def test0747(self):
        self.assertEquals(self.calculate(19652, 19565), -8332, "")

    def test0748(self):
        self.assertEquals(self.calculate(14378, 9897), 20410, "")

    def test0749(self):
        self.assertEquals(self.calculate(30610, 18294), -25780, "")

    def test0750(self):
        self.assertEquals(self.calculate(19827, -20880), 3152, "")

    def test0751(self):
        self.assertEquals(self.calculate(11632, -28884), 24384, "")

    def test0752(self):
        self.assertEquals(self.calculate(-24305, -29001), 29625, "")

    def test0753(self):
        self.assertEquals(self.calculate(-30186, 25815), -28550, "")

    def test0754(self):
        self.assertEquals(self.calculate(-25919, -3046), -21606, "")

    def test0755(self):
        self.assertEquals(self.calculate(28671, -3114), -21462, "")

    def test0756(self):
        self.assertEquals(self.calculate(-21098, 27408), -29856, "")

    def test0757(self):
        self.assertEquals(self.calculate(12996, 4313), 18468, "")

    def test0758(self):
        self.assertEquals(self.calculate(-12883, 30312), 19528, "")

    def test0759(self):
        self.assertEquals(self.calculate(28773, -24052), 11964, "")

    def test0760(self):
        self.assertEquals(self.calculate(-9879, -2418), 32318, "")

    def test0761(self):
        self.assertEquals(self.calculate(-25750, -31905), -5546, "")

    def test0762(self):
        self.assertEquals(self.calculate(-23096, -5744), 18560, "")

    def test0763(self):
        self.assertEquals(self.calculate(-24812, -24508), -16048, "")

    def test0764(self):
        self.assertEquals(self.calculate(26606, 2129), 21070, "")

    def test0765(self):
        self.assertEquals(self.calculate(32303, 17245), 9235, "")

    def test0766(self):
        self.assertEquals(self.calculate(17368, 20917), 20408, "")

    def test0767(self):
        self.assertEquals(self.calculate(-2401, 15434), -29194, "")

    def test0768(self):
        self.assertEquals(self.calculate(20765, 32584), 13096, "")

    def test0769(self):
        self.assertEquals(self.calculate(30387, 14781), 32039, "")

    def test0770(self):
        self.assertEquals(self.calculate(4152, -1646), -18448, "")

    def test0771(self):
        self.assertEquals(self.calculate(-1457, 23013), 24491, "")

    def test0772(self):
        self.assertEquals(self.calculate(-25142, -19620), -3432, "")

    def test0773(self):
        self.assertEquals(self.calculate(-1292, -919), 7700, "")

    def test0774(self):
        self.assertEquals(self.calculate(5643, -9646), 28038, "")

    def test0775(self):
        self.assertEquals(self.calculate(8548, 30136), -19488, "")

    def test0776(self):
        self.assertEquals(self.calculate(13501, 7066), -22350, "")

    def test0777(self):
        self.assertEquals(self.calculate(12108, -21153), -5836, "")

    def test0778(self):
        self.assertEquals(self.calculate(768, 17258), 15872, "")

    def test0779(self):
        self.assertEquals(self.calculate(15302, -7422), 2444, "")

    def test0780(self):
        self.assertEquals(self.calculate(18629, -30571), 681, "")

    def test0781(self):
        self.assertEquals(self.calculate(18544, 9505), -31120, "")

    def test0782(self):
        self.assertEquals(self.calculate(15362, 18636), 24984, "")

    def test0783(self):
        self.assertEquals(self.calculate(-32047, -11066), 16806, "")

    def test0784(self):
        self.assertEquals(self.calculate(-30733, -2060), 2204, "")

    def test0785(self):
        self.assertEquals(self.calculate(-15314, -10693), -21862, "")

    def test0786(self):
        self.assertEquals(self.calculate(-16823, 22063), 30055, "")

    def test0787(self):
        self.assertEquals(self.calculate(-27704, 6296), 32448, "")

    def test0788(self):
        self.assertEquals(self.calculate(1239, 31945), -3889, "")

    def test0789(self):
        self.assertEquals(self.calculate(-14437, -13705), 5901, "")

    def test0790(self):
        self.assertEquals(self.calculate(-25903, 5358), 16974, "")

    def test0791(self):
        self.assertEquals(self.calculate(-31439, 30733), -17539, "")

    def test0792(self):
        self.assertEquals(self.calculate(-19574, 13491), -28290, "")

    def test0793(self):
        self.assertEquals(self.calculate(27592, 14006), -12240, "")

    def test0794(self):
        self.assertEquals(self.calculate(14322, -23866), 26924, "")

    def test0795(self):
        self.assertEquals(self.calculate(-14190, 13762), 14500, "")

    def test0796(self):
        self.assertEquals(self.calculate(13847, -23443), -15413, "")

    def test0797(self):
        self.assertEquals(self.calculate(18953, -12968), -22504, "")

    def test0798(self):
        self.assertEquals(self.calculate(31920, 1020), -12992, "")

    def test0799(self):
        self.assertEquals(self.calculate(-8792, 16715), -26568, "")

    def test0800(self):
        self.assertEquals(self.calculate(22149, 18715), 3335, "")

    def test0801(self):
        self.assertEquals(self.calculate(-7732, 5672), -12320, "")

    def test0802(self):
        self.assertEquals(self.calculate(-15091, 13551), -25821, "")

    def test0803(self):
        self.assertEquals(self.calculate(-21141, -22161), -11163, "")

    def test0804(self):
        self.assertEquals(self.calculate(2224, -23734), -27936, "")

    def test0805(self):
        self.assertEquals(self.calculate(-18133, 4870), -30718, "")

    def test0806(self):
        self.assertEquals(self.calculate(-15074, -28699), 5590, "")

    def test0807(self):
        self.assertEquals(self.calculate(5616, -23768), 15744, "")

    def test0808(self):
        self.assertEquals(self.calculate(-23371, 6468), 27924, "")

    def test0809(self):
        self.assertEquals(self.calculate(-23809, 25686), 23978, "")

    def test0810(self):
        self.assertEquals(self.calculate(-4415, 1371), -23653, "")

    def test0811(self):
        self.assertEquals(self.calculate(-31343, -3465), 10343, "")

    def test0812(self):
        self.assertEquals(self.calculate(17919, -21255), 26887, "")

    def test0813(self):
        self.assertEquals(self.calculate(-31925, -863), 26155, "")

    def test0814(self):
        self.assertEquals(self.calculate(7783, 14650), -11690, "")

    def test0815(self):
        self.assertEquals(self.calculate(-28421, -14175), 17883, "")

    def test0816(self):
        self.assertEquals(self.calculate(6620, 17761), 6236, "")

    def test0817(self):
        self.assertEquals(self.calculate(27085, -28617), 2827, "")

    def test0818(self):
        self.assertEquals(self.calculate(2484, -16794), 30136, "")

    def test0819(self):
        self.assertEquals(self.calculate(-17659, -2810), 11038, "")

    def test0820(self):
        self.assertEquals(self.calculate(32468, -1936), -9024, "")

    def test0821(self):
        self.assertEquals(self.calculate(19975, 19411), 23749, "")

    def test0822(self):
        self.assertEquals(self.calculate(-2672, 31179), -14032, "")

    def test0823(self):
        self.assertEquals(self.calculate(2309, 16895), 16635, "")

    def test0824(self):
        self.assertEquals(self.calculate(29924, 11514), 22184, "")

    def test0825(self):
        self.assertEquals(self.calculate(-1366, -12037), -6994, "")

    def test0826(self):
        self.assertEquals(self.calculate(15658, -22197), -23218, "")

    def test0827(self):
        self.assertEquals(self.calculate(-24471, -16969), 12303, "")

    def test0828(self):
        self.assertEquals(self.calculate(25766, 16275), -23214, "")

    def test0829(self):
        self.assertEquals(self.calculate(-26005, 8791), -20387, "")

    def test0830(self):
        self.assertEquals(self.calculate(-28059, 1834), -14446, "")

    def test0831(self):
        self.assertEquals(self.calculate(14424, -2842), 32528, "")

    def test0832(self):
        self.assertEquals(self.calculate(7818, 5178), -19644, "")

    def test0833(self):
        self.assertEquals(self.calculate(-11174, 17097), -4438, "")

    def test0834(self):
        self.assertEquals(self.calculate(-12439, 323), -20101, "")

    def test0835(self):
        self.assertEquals(self.calculate(-13867, 10197), 24889, "")

    def test0836(self):
        self.assertEquals(self.calculate(19820, -26065), 11988, "")

    def test0837(self):
        self.assertEquals(self.calculate(-13826, 12079), -18526, "")

    def test0838(self):
        self.assertEquals(self.calculate(-6859, -15685), -26697, "")

    def test0839(self):
        self.assertEquals(self.calculate(5410, 30649), 5010, "")

    def test0840(self):
        self.assertEquals(self.calculate(-18544, -11568), 17664, "")

    def test0841(self):
        self.assertEquals(self.calculate(5917, -19833), 23115, "")

    def test0842(self):
        self.assertEquals(self.calculate(-26260, 30610), -19560, "")

    def test0843(self):
        self.assertEquals(self.calculate(-20292, 17209), -29220, "")

    def test0844(self):
        self.assertEquals(self.calculate(-27213, -12329), 30293, "")

    def test0845(self):
        self.assertEquals(self.calculate(-26482, 16275), -29814, "")

    def test0846(self):
        self.assertEquals(self.calculate(13678, -12986), -19948, "")

    def test0847(self):
        self.assertEquals(self.calculate(32527, 32205), 4611, "")

    def test0848(self):
        self.assertEquals(self.calculate(-22624, 26572), -3200, "")

    def test0849(self):
        self.assertEquals(self.calculate(-9941, -28675), -23425, "")

    def test0850(self):
        self.assertEquals(self.calculate(-24259, -6465), 6787, "")

    def test0851(self):
        self.assertEquals(self.calculate(23541, -11555), 23681, "")

    def test0852(self):
        self.assertEquals(self.calculate(23912, -31447), -600, "")

    def test0853(self):
        self.assertEquals(self.calculate(8105, 31492), -20060, "")

    def test0854(self):
        self.assertEquals(self.calculate(2711, 6735), -25959, "")

    def test0855(self):
        self.assertEquals(self.calculate(11195, 9305), -32765, "")

    def test0856(self):
        self.assertEquals(self.calculate(6764, -5220), 15824, "")

    def test0857(self):
        self.assertEquals(self.calculate(-8984, -10288), 21632, "")

    def test0858(self):
        self.assertEquals(self.calculate(-29201, 14421), 26715, "")

    def test0859(self):
        self.assertEquals(self.calculate(-24934, -3586), 22220, "")

    def test0860(self):
        self.assertEquals(self.calculate(933, -27635), -27807, "")

    def test0861(self):
        self.assertEquals(self.calculate(-20756, -25479), 32140, "")

    def test0862(self):
        self.assertEquals(self.calculate(-13140, -27063), 9484, "")

    def test0863(self):
        self.assertEquals(self.calculate(2514, 31259), 7462, "")

    def test0864(self):
        self.assertEquals(self.calculate(14661, 3552), -25248, "")

    def test0865(self):
        self.assertEquals(self.calculate(4796, 22112), 11904, "")

    def test0866(self):
        self.assertEquals(self.calculate(-14710, 30523), -6194, "")

    def test0867(self):
        self.assertEquals(self.calculate(8234, -32233), 14278, "")

    def test0868(self):
        self.assertEquals(self.calculate(16594, 7722), 15988, "")

    def test0869(self):
        self.assertEquals(self.calculate(19228, 18512), 22720, "")

    def test0870(self):
        self.assertEquals(self.calculate(-32361, 27694), -734, "")

    def test0871(self):
        self.assertEquals(self.calculate(18175, 16552), 22360, "")

    def test0872(self):
        self.assertEquals(self.calculate(-6848, -7344), 25600, "")

    def test0873(self):
        self.assertEquals(self.calculate(3502, -1768), -31152, "")

    def test0874(self):
        self.assertEquals(self.calculate(14234, 29044), 11208, "")

    def test0875(self):
        self.assertEquals(self.calculate(16569, 2395), -32061, "")

    def test0876(self):
        self.assertEquals(self.calculate(16091, 26259), 22977, "")

    def test0877(self):
        self.assertEquals(self.calculate(32471, -872), -3160, "")

    def test0878(self):
        self.assertEquals(self.calculate(-18851, -510), -19782, "")

    def test0879(self):
        self.assertEquals(self.calculate(14744, 17067), -22392, "")

    def test0880(self):
        self.assertEquals(self.calculate(-5502, -4120), -7216, "")

    def test0881(self):
        self.assertEquals(self.calculate(28906, -14768), 17696, "")

    def test0882(self):
        self.assertEquals(self.calculate(-17063, 3901), 21813, "")

    def test0883(self):
        self.assertEquals(self.calculate(21366, 30294), 28068, "")

    def test0884(self):
        self.assertEquals(self.calculate(-21303, -29855), -25815, "")

    def test0885(self):
        self.assertEquals(self.calculate(-9795, -19021), -8153, "")

    def test0886(self):
        self.assertEquals(self.calculate(-25752, -4812), -9952, "")

    def test0887(self):
        self.assertEquals(self.calculate(-9509, 11490), -9898, "")

    def test0888(self):
        self.assertEquals(self.calculate(-20127, -14403), 23453, "")

    def test0889(self):
        self.assertEquals(self.calculate(-9173, 31295), -21355, "")

    def test0890(self):
        self.assertEquals(self.calculate(-15938, 27446), 18452, "")

    def test0891(self):
        self.assertEquals(self.calculate(-5546, 1438), 20244, "")

    def test0892(self):
        self.assertEquals(self.calculate(-30319, -26253), 29987, "")

    def test0893(self):
        self.assertEquals(self.calculate(-10571, -13340), -16332, "")

    def test0894(self):
        self.assertEquals(self.calculate(28972, 4096), -16384, "")

    def test0895(self):
        self.assertEquals(self.calculate(10047, 25173), 9707, "")

    def test0896(self):
        self.assertEquals(self.calculate(22285, -10117), -13505, "")

    def test0897(self):
        self.assertEquals(self.calculate(27404, 7579), 11332, "")

    def test0898(self):
        self.assertEquals(self.calculate(-5654, 622), 22156, "")

    def test0899(self):
        self.assertEquals(self.calculate(6082, 29206), 28332, "")

    def test0900(self):
        self.assertEquals(self.calculate(5047, 24935), 17825, "")

    def test0901(self):
        self.assertEquals(self.calculate(-30055, -10179), 7797, "")

    def test0902(self):
        self.assertEquals(self.calculate(-27367, -11324), -15836, "")

    def test0903(self):
        self.assertEquals(self.calculate(8058, -9019), 4322, "")

    def test0904(self):
        self.assertEquals(self.calculate(12099, -13131), -12705, "")

    def test0905(self):
        self.assertEquals(self.calculate(3183, 4004), 30748, "")

    def test0906(self):
        self.assertEquals(self.calculate(24065, -18111), -26815, "")

    def test0907(self):
        self.assertEquals(self.calculate(-3242, -4949), -11662, "")

    def test0908(self):
        self.assertEquals(self.calculate(19917, 2399), 5139, "")

    def test0909(self):
        self.assertEquals(self.calculate(5153, 26192), 28752, "")

    def test0910(self):
        self.assertEquals(self.calculate(9662, -8228), -3768, "")

    def test0911(self):
        self.assertEquals(self.calculate(-19589, 16017), 29355, "")

    def test0912(self):
        self.assertEquals(self.calculate(2442, 19406), 6924, "")

    def test0913(self):
        self.assertEquals(self.calculate(-19982, -20423), -286, "")

    def test0914(self):
        self.assertEquals(self.calculate(16654, -30711), -18050, "")

    def test0915(self):
        self.assertEquals(self.calculate(-1062, -22576), -10464, "")

    def test0916(self):
        self.assertEquals(self.calculate(2964, -24172), -14960, "")

    def test0917(self):
        self.assertEquals(self.calculate(-22581, 16689), -22309, "")

    def test0918(self):
        self.assertEquals(self.calculate(18613, 3012), 29076, "")

    def test0919(self):
        self.assertEquals(self.calculate(29066, -12273), -14570, "")

    def test0920(self):
        self.assertEquals(self.calculate(6568, -30990), 12496, "")

    def test0921(self):
        self.assertEquals(self.calculate(24751, 29382), -19110, "")

    def test0922(self):
        self.assertEquals(self.calculate(31162, 31150), -22932, "")

    def test0923(self):
        self.assertEquals(self.calculate(-9302, 12689), -2742, "")

    def test0924(self):
        self.assertEquals(self.calculate(29549, 9369), 20517, "")

    def test0925(self):
        self.assertEquals(self.calculate(11655, -18886), 19094, "")

    def test0926(self):
        self.assertEquals(self.calculate(-32035, 23630), 19286, "")

    def test0927(self):
        self.assertEquals(self.calculate(18723, 15682), 12806, "")

    def test0928(self):
        self.assertEquals(self.calculate(-15907, 29185), 11229, "")

    def test0929(self):
        self.assertEquals(self.calculate(21017, 12115), 13595, "")

    def test0930(self):
        self.assertEquals(self.calculate(-1769, 15472), 24080, "")

    def test0931(self):
        self.assertEquals(self.calculate(9674, -4332), -30264, "")

    def test0932(self):
        self.assertEquals(self.calculate(27798, -24115), 18974, "")

    def test0933(self):
        self.assertEquals(self.calculate(18074, 13519), 24198, "")

    def test0934(self):
        self.assertEquals(self.calculate(-18145, 17181), 5507, "")

    def test0935(self):
        self.assertEquals(self.calculate(-9991, 7738), 22122, "")

    def test0936(self):
        self.assertEquals(self.calculate(21663, -9270), -13706, "")

    def test0937(self):
        self.assertEquals(self.calculate(-1183, 30552), -32680, "")

    def test0938(self):
        self.assertEquals(self.calculate(60, -15214), 4664, "")

    def test0939(self):
        self.assertEquals(self.calculate(-23046, 29286), 30108, "")

    def test0940(self):
        self.assertEquals(self.calculate(7313, -23550), 7458, "")

    def test0941(self):
        self.assertEquals(self.calculate(21249, -29202), -18450, "")

    def test0942(self):
        self.assertEquals(self.calculate(28096, -24522), 9856, "")

    def test0943(self):
        self.assertEquals(self.calculate(25972, -28789), -7684, "")

    def test0944(self):
        self.assertEquals(self.calculate(-12634, 4572), -25432, "")

    def test0945(self):
        self.assertEquals(self.calculate(11017, -2467), 18501, "")

    def test0946(self):
        self.assertEquals(self.calculate(5968, -7472), -28416, "")

    def test0947(self):
        self.assertEquals(self.calculate(-29773, -14208), -20096, "")

    def test0948(self):
        self.assertEquals(self.calculate(30922, -164), -24936, "")

    def test0949(self):
        self.assertEquals(self.calculate(412, 11685), 30092, "")

    def test0950(self):
        self.assertEquals(self.calculate(-24822, -20543), -17270, "")

    def test0951(self):
        self.assertEquals(self.calculate(-3113, -23830), -3962, "")

    def test0952(self):
        self.assertEquals(self.calculate(9318, 11164), 20520, "")

    def test0953(self):
        self.assertEquals(self.calculate(-3, -19885), -5881, "")

    def test0954(self):
        self.assertEquals(self.calculate(-26856, -5750), 19184, "")

    def test0955(self):
        self.assertEquals(self.calculate(12445, -9545), 29243, "")

    def test0956(self):
        self.assertEquals(self.calculate(31555, 19850), -26338, "")

    def test0957(self):
        self.assertEquals(self.calculate(-16843, -16949), -2809, "")

    def test0958(self):
        self.assertEquals(self.calculate(-10804, 32655), -24332, "")

    def test0959(self):
        self.assertEquals(self.calculate(-3486, 10085), -29014, "")

    def test0960(self):
        self.assertEquals(self.calculate(2262, -31236), -8024, "")

    def test0961(self):
        self.assertEquals(self.calculate(4681, 1079), 4527, "")

    def test0962(self):
        self.assertEquals(self.calculate(-3883, -29443), 32385, "")

    def test0963(self):
        self.assertEquals(self.calculate(31476, -7645), 14172, "")

    def test0964(self):
        self.assertEquals(self.calculate(20906, -27343), -27766, "")

    def test0965(self):
        self.assertEquals(self.calculate(-21459, -8989), 22503, "")

    def test0966(self):
        self.assertEquals(self.calculate(14830, -3765), 1722, "")

    def test0967(self):
        self.assertEquals(self.calculate(-30235, 24748), -31268, "")

    def test0968(self):
        self.assertEquals(self.calculate(-21293, -32564), 14372, "")

    def test0969(self):
        self.assertEquals(self.calculate(-25746, -25515), -23674, "")

    def test0970(self):
        self.assertEquals(self.calculate(-22184, -4520), 1600, "")

    def test0971(self):
        self.assertEquals(self.calculate(-14107, 21557), -17559, "")

    def test0972(self):
        self.assertEquals(self.calculate(-22064, 12301), -24688, "")

    def test0973(self):
        self.assertEquals(self.calculate(-7323, 8080), 9168, "")

    def test0974(self):
        self.assertEquals(self.calculate(-18930, 29353), 27454, "")

    def test0975(self):
        self.assertEquals(self.calculate(12166, -19326), 23052, "")

    def test0976(self):
        self.assertEquals(self.calculate(20981, -23424), -4480, "")

    def test0977(self):
        self.assertEquals(self.calculate(16306, -25109), -23962, "")

    def test0978(self):
        self.assertEquals(self.calculate(13088, 17837), 11424, "")

    def test0979(self):
        self.assertEquals(self.calculate(-10489, 14107), 11965, "")

    def test0980(self):
        self.assertEquals(self.calculate(-26630, -7315), 25458, "")

    def test0981(self):
        self.assertEquals(self.calculate(-21707, -24689), -29285, "")

    def test0982(self):
        self.assertEquals(self.calculate(2877, 29361), -4307, "")

    def test0983(self):
        self.assertEquals(self.calculate(8913, 25506), -9406, "")

    def test0984(self):
        self.assertEquals(self.calculate(14946, 8926), -23300, "")

    def test0985(self):
        self.assertEquals(self.calculate(29446, 7905), -13242, "")

    def test0986(self):
        self.assertEquals(self.calculate(-3521, -1859), -8061, "")

    def test0987(self):
        self.assertEquals(self.calculate(28019, 4733), -30937, "")

    def test0988(self):
        self.assertEquals(self.calculate(20451, -14998), -15618, "")

    def test0989(self):
        self.assertEquals(self.calculate(-26633, -22570), 10618, "")

    def test0990(self):
        self.assertEquals(self.calculate(20696, 18010), 31728, "")

    def test0991(self):
        self.assertEquals(self.calculate(-28936, 29431), 24904, "")

    def test0992(self):
        self.assertEquals(self.calculate(9899, 25627), -8183, "")

    def test0993(self):
        self.assertEquals(self.calculate(-30188, 20947), 8828, "")

    def test0994(self):
        self.assertEquals(self.calculate(5186, -19108), -3656, "")

    def test0995(self):
        self.assertEquals(self.calculate(-15319, 31171), -13253, "")

    def test0996(self):
        self.assertEquals(self.calculate(-20683, -6358), -28238, "")

    def test0997(self):
        self.assertEquals(self.calculate(30518, 1245), -15970, "")

    def test0998(self):
        self.assertEquals(self.calculate(-6023, 31767), 32479, "")

    def test0999(self):
        self.assertEquals(self.calculate(5061, 9154), -5558, "")

    def test1000(self):
        self.assertEquals(self.calculate(21263, 2708), -25940, "")

    def test1001(self):
        self.assertEquals(self.calculate(3186, 9115), 7942, "")

    def test1002(self):
        self.assertEquals(self.calculate(12366, -7964), 17784, "")

    def test1003(self):
        self.assertEquals(self.calculate(-26540, -2670), 17384, "")

    def test1004(self):
        self.assertEquals(self.calculate(-22501, -16180), 13700, "")

    def test1005(self):
        self.assertEquals(self.calculate(-10337, -13116), -13892, "")

    def test1006(self):
        self.assertEquals(self.calculate(23833, 21689), 31505, "")

    def test1007(self):
        self.assertEquals(self.calculate(24160, -9228), 4992, "")

    def test1008(self):
        self.assertEquals(self.calculate(8019, 13699), 13945, "")

    def test1009(self):
        self.assertEquals(self.calculate(-30786, -26915), -31994, "")

    def test1010(self):
        self.assertEquals(self.calculate(22031, -1741), -17411, "")

    def test1011(self):
        self.assertEquals(self.calculate(-6528, -8857), 15744, "")

    def test1012(self):
        self.assertEquals(self.calculate(-20479, 14107), -14565, "")

    def test1013(self):
        self.assertEquals(self.calculate(17941, 16979), 8911, "")

    def test1014(self):
        self.assertEquals(self.calculate(-19763, -12370), 19030, "")

    def test1015(self):
        self.assertEquals(self.calculate(10275, 24970), -6690, "")

    def test1016(self):
        self.assertEquals(self.calculate(-6067, -29851), 30049, "")

    def test1017(self):
        self.assertEquals(self.calculate(-22457, 31653), -27965, "")

    def test1018(self):
        self.assertEquals(self.calculate(589, -20170), -18114, "")

    def test1019(self):
        self.assertEquals(self.calculate(25949, -3087), -19571, "")

    def test1020(self):
        self.assertEquals(self.calculate(18820, 26779), 8940, "")

    def test1021(self):
        self.assertEquals(self.calculate(13471, 20553), -20137, "")

    def test1022(self):
        self.assertEquals(self.calculate(-21985, 10596), 27420, "")

    def test1023(self):
        self.assertEquals(self.calculate(-26626, -13261), -20582, "")


class TestVM_Mul_IntLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushL(rhs)
        v.VM_Mul()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(2842, -352810436), -1959879144)

    def test0001(self):
        self.assertEquals(self.calculate(26809, 1877992075), 1482894963)

    def test0002(self):
        self.assertEquals(self.calculate(-5932, 264213790), 346860760)

    def test0003(self):
        self.assertEquals(self.calculate(28233, -1033644348), 1421899236)

    def test0004(self):
        self.assertEquals(self.calculate(11572, -1049812857), 2028099180)

    def test0005(self):
        self.assertEquals(self.calculate(-10544, 56946897), 847339472)

    def test0006(self):
        self.assertEquals(self.calculate(-30486, 570399939), 1110041150)

    def test0007(self):
        self.assertEquals(self.calculate(5690, -253515594), 605281596)

    def test0008(self):
        self.assertEquals(self.calculate(27951, 1107035754), 1811959670)

    def test0009(self):
        self.assertEquals(self.calculate(24831, 1746510785), 1324514623)

    def test0010(self):
        self.assertEquals(self.calculate(17338, -607522482), -1964983124)

    def test0011(self):
        self.assertEquals(self.calculate(7155, -900055063), -1737999061)

    def test0012(self):
        self.assertEquals(self.calculate(-5081, -454044981), 605110509)

    def test0013(self):
        self.assertEquals(self.calculate(9186, 1497628640), 436437952)

    def test0014(self):
        self.assertEquals(self.calculate(-22948, -2118229892), -1300294512)

    def test0015(self):
        self.assertEquals(self.calculate(-3947, -43950771), 1675001297)

    def test0016(self):
        self.assertEquals(self.calculate(-27529, 533779518), -1333231406)

    def test0017(self):
        self.assertEquals(self.calculate(-30516, 489885392), 1438535104)

    def test0018(self):
        self.assertEquals(self.calculate(22637, 1464920214), -43608098)

    def test0019(self):
        self.assertEquals(self.calculate(-15193, -778308025), 788857937)

    def test0020(self):
        self.assertEquals(self.calculate(-13858, 483318899), -1979287878)

    def test0021(self):
        self.assertEquals(self.calculate(-12264, -986752523), -1684898056)

    def test0022(self):
        self.assertEquals(self.calculate(156, 1596130529), -111740644)

    def test0023(self):
        self.assertEquals(self.calculate(-3374, -481228454), 167165908)

    def test0024(self):
        self.assertEquals(self.calculate(25461, 1534769329), 1149426661)

    def test0025(self):
        self.assertEquals(self.calculate(-9381, 372779351), -939712787)

    def test0026(self):
        self.assertEquals(self.calculate(17917, 341632880), 707914160)

    def test0027(self):
        self.assertEquals(self.calculate(-17888, -725668270), 1362845248)

    def test0028(self):
        self.assertEquals(self.calculate(12458, -1691455159), -1038816646)

    def test0029(self):
        self.assertEquals(self.calculate(2274, 1465213252), -999686648)

    def test0030(self):
        self.assertEquals(self.calculate(-14324, -1058213326), 908094040)

    def test0031(self):
        self.assertEquals(self.calculate(4292, 872058791), 1959816156)

    def test0032(self):
        self.assertEquals(self.calculate(-27928, 2107263461), -2012049016)

    def test0033(self):
        self.assertEquals(self.calculate(14593, 1596725087), 811613791)

    def test0034(self):
        self.assertEquals(self.calculate(3653, -998402873), -738460765)

    def test0035(self):
        self.assertEquals(self.calculate(-16500, 287665491), -541739420)

    def test0036(self):
        self.assertEquals(self.calculate(4168, 670650570), -752133936)

    def test0037(self):
        self.assertEquals(self.calculate(25078, -1298872654), -96444148)

    def test0038(self):
        self.assertEquals(self.calculate(-29107, 1944540799), -670009805)

    def test0039(self):
        self.assertEquals(self.calculate(18038, 721417014), -830808348)

    def test0040(self):
        self.assertEquals(self.calculate(12947, 2049564434), 1402772310)

    def test0041(self):
        self.assertEquals(self.calculate(-8820, -1052508626), 1701754664)

    def test0042(self):
        self.assertEquals(self.calculate(-6373, -1772817316), -1894200908)

    def test0043(self):
        self.assertEquals(self.calculate(-28996, 433096783), 410053636)

    def test0044(self):
        self.assertEquals(self.calculate(-2494, 1601200824), 924730224)

    def test0045(self):
        self.assertEquals(self.calculate(5348, 1476388585), 1576262532)

    def test0046(self):
        self.assertEquals(self.calculate(12801, -668376581), -313759749)

    def test0047(self):
        self.assertEquals(self.calculate(-24243, 1247419200), -318934464)

    def test0048(self):
        self.assertEquals(self.calculate(29587, 1287430287), -865046755)

    def test0049(self):
        self.assertEquals(self.calculate(5451, -411092307), 1108763055)

    def test0050(self):
        self.assertEquals(self.calculate(-13616, 1630090759), 1075211184)

    def test0051(self):
        self.assertEquals(self.calculate(-10686, -359291930), -307198644)

    def test0052(self):
        self.assertEquals(self.calculate(24574, 332738282), -907189716)

    def test0053(self):
        self.assertEquals(self.calculate(30806, 1640449065), 1088691654)

    def test0054(self):
        self.assertEquals(self.calculate(-32705, 1746773877), -879643189)

    def test0055(self):
        self.assertEquals(self.calculate(-19968, 1631090190), -871908352)

    def test0056(self):
        self.assertEquals(self.calculate(-25693, 627453884), 2134587572)

    def test0057(self):
        self.assertEquals(self.calculate(-14697, -1010479652), -977464124)

    def test0058(self):
        self.assertEquals(self.calculate(-29345, 1399244006), -928006310)

    def test0059(self):
        self.assertEquals(self.calculate(-12090, -1736593019), 1609456862)

    def test0060(self):
        self.assertEquals(self.calculate(-29939, -1534576422), 418332946)

    def test0061(self):
        self.assertEquals(self.calculate(-12052, 1217711609), 42938764)

    def test0062(self):
        self.assertEquals(self.calculate(22744, 56536120), 1662291776)

    def test0063(self):
        self.assertEquals(self.calculate(3362, -1433805347), -1500270502)

    def test0064(self):
        self.assertEquals(self.calculate(-22846, 1944383563), 1459862230)

    def test0065(self):
        self.assertEquals(self.calculate(191, -1992241824), 1733900960)

    def test0066(self):
        self.assertEquals(self.calculate(-27446, -688908338), 1332207756)

    def test0067(self):
        self.assertEquals(self.calculate(11025, -287335558), 1811337498)

    def test0068(self):
        self.assertEquals(self.calculate(-4136, -1228879963), 1701215800)

    def test0069(self):
        self.assertEquals(self.calculate(-2322, -319456385), -1251616238)

    def test0070(self):
        self.assertEquals(self.calculate(18055, 1830629943), -2044689151)

    def test0071(self):
        self.assertEquals(self.calculate(14, -1661512340), -1786336280)

    def test0072(self):
        self.assertEquals(self.calculate(8027, -297768616), 2108103240)

    def test0073(self):
        self.assertEquals(self.calculate(-28771, 268990049), 418367613)

    def test0074(self):
        self.assertEquals(self.calculate(22859, 1828682405), -1065596073)

    def test0075(self):
        self.assertEquals(self.calculate(31918, -1560903306), 708912692)

    def test0076(self):
        self.assertEquals(self.calculate(-28070, 1445015439), 87770694)

    def test0077(self):
        self.assertEquals(self.calculate(-4186, 1487366621), 1585903694)

    def test0078(self):
        self.assertEquals(self.calculate(-837, 533724684), -50961724)

    def test0079(self):
        self.assertEquals(self.calculate(7480, 1630424313), -2133259400)

    def test0080(self):
        self.assertEquals(self.calculate(9830, -1893704063), -722678426)

    def test0081(self):
        self.assertEquals(self.calculate(10087, 2099486075), -967698051)

    def test0082(self):
        self.assertEquals(self.calculate(-1806, -1120305594), 342306348)

    def test0083(self):
        self.assertEquals(self.calculate(7860, -703590671), 1695203188)

    def test0084(self):
        self.assertEquals(self.calculate(3482, -1887846163), 2114590610)

    def test0085(self):
        self.assertEquals(self.calculate(12569, 1585694275), 1943089035)

    def test0086(self):
        self.assertEquals(self.calculate(-11930, 1163615614), -599974348)

    def test0087(self):
        self.assertEquals(self.calculate(-27943, -1574600975), 1430064201)

    def test0088(self):
        self.assertEquals(self.calculate(28573, -2114639091), 17172985)

    def test0089(self):
        self.assertEquals(self.calculate(-30996, 807333336), -1624616160)

    def test0090(self):
        self.assertEquals(self.calculate(1561, 1653971134), 573595278)

    def test0091(self):
        self.assertEquals(self.calculate(26971, -1462351436), -395901188)

    def test0092(self):
        self.assertEquals(self.calculate(-21305, -1246290871), 739182783)

    def test0093(self):
        self.assertEquals(self.calculate(29941, -1627699069), 56082783)

    def test0094(self):
        self.assertEquals(self.calculate(-21731, -970314035), 1899838521)

    def test0095(self):
        self.assertEquals(self.calculate(13961, 615949179), 741961427)

    def test0096(self):
        self.assertEquals(self.calculate(5465, -1580825375), -2031442119)

    def test0097(self):
        self.assertEquals(self.calculate(12225, 333158951), 1239179367)

    def test0098(self):
        self.assertEquals(self.calculate(-9192, 1502090672), 1102399616)

    def test0099(self):
        self.assertEquals(self.calculate(-23070, -838810717), -1759394586)

    def test0100(self):
        self.assertEquals(self.calculate(-7303, -1245553202), -465698722)

    def test0101(self):
        self.assertEquals(self.calculate(-14485, -904878518), -1074854162)

    def test0102(self):
        self.assertEquals(self.calculate(-25452, 360542041), 1829084020)

    def test0103(self):
        self.assertEquals(self.calculate(29143, 1567833999), 1524138009)

    def test0104(self):
        self.assertEquals(self.calculate(32740, 1630421557), -2146745804)

    def test0105(self):
        self.assertEquals(self.calculate(29834, 752940775), 556123270)

    def test0106(self):
        self.assertEquals(self.calculate(-18590, 1736929648), 41975008)

    def test0107(self):
        self.assertEquals(self.calculate(-19130, -946111261), 116237586)

    def test0108(self):
        self.assertEquals(self.calculate(15992, -1411220584), 1813561152)

    def test0109(self):
        self.assertEquals(self.calculate(-11681, -1041378853), 998999621)

    def test0110(self):
        self.assertEquals(self.calculate(-7207, 1481894417), 1570601833)

    def test0111(self):
        self.assertEquals(self.calculate(10910, 241902507), 2046431626)

    def test0112(self):
        self.assertEquals(self.calculate(-20145, -2044555580), -1164209540)

    def test0113(self):
        self.assertEquals(self.calculate(-12932, -1598446435), -568298228)

    def test0114(self):
        self.assertEquals(self.calculate(24428, 270100982), 957021640)

    def test0115(self):
        self.assertEquals(self.calculate(4780, 233213041), -1933160980)

    def test0116(self):
        self.assertEquals(self.calculate(-26658, 1479371089), -684778690)

    def test0117(self):
        self.assertEquals(self.calculate(2003, -33963278), 691030902)

    def test0118(self):
        self.assertEquals(self.calculate(-30972, 1544792912), 609606976)

    def test0119(self):
        self.assertEquals(self.calculate(19114, 15744633), 295204442)

    def test0120(self):
        self.assertEquals(self.calculate(-5916, -817574876), 639791120)

    def test0121(self):
        self.assertEquals(self.calculate(-26865, 2061407047), -392003031)

    def test0122(self):
        self.assertEquals(self.calculate(-21393, 1405778102), -449929494)

    def test0123(self):
        self.assertEquals(self.calculate(31619, 821998611), 1926973113)

    def test0124(self):
        self.assertEquals(self.calculate(16912, -1288819095), 450492560)

    def test0125(self):
        self.assertEquals(self.calculate(4944, -1291735007), 278494544)

    def test0126(self):
        self.assertEquals(self.calculate(-26253, 907016340), -601284996)

    def test0127(self):
        self.assertEquals(self.calculate(-29416, -1359018905), -655481688)

    def test0128(self):
        self.assertEquals(self.calculate(-7054, -200223374), -668560188)

    def test0129(self):
        self.assertEquals(self.calculate(-22347, 509751594), -1165602126)

    def test0130(self):
        self.assertEquals(self.calculate(23170, -1846544648), 2024708592)

    def test0131(self):
        self.assertEquals(self.calculate(-28680, 1774260615), 978084808)

    def test0132(self):
        self.assertEquals(self.calculate(-18832, 573128939), 88635600)

    def test0133(self):
        self.assertEquals(self.calculate(-18910, 1119509604), -32809656)

    def test0134(self):
        self.assertEquals(self.calculate(1333, 46694741), 2114547609)

    def test0135(self):
        self.assertEquals(self.calculate(-22594, -111604957), 456595706)

    def test0136(self):
        self.assertEquals(self.calculate(31422, -1338928243), 1696380070)

    def test0137(self):
        self.assertEquals(self.calculate(-18849, -190126071), 1683587415)

    def test0138(self):
        self.assertEquals(self.calculate(17695, -1179592651), 649099115)

    def test0139(self):
        self.assertEquals(self.calculate(-19714, 1354468628), -182853160)

    def test0140(self):
        self.assertEquals(self.calculate(573, -554764838), -52672270)

    def test0141(self):
        self.assertEquals(self.calculate(-206, 1778318781), -1261448726)

    def test0142(self):
        self.assertEquals(self.calculate(-4501, 1954895948), 1401327556)

    def test0143(self):
        self.assertEquals(self.calculate(17134, 1161728908), -2110307288)

    def test0144(self):
        self.assertEquals(self.calculate(-2860, 1087361225), -296781196)

    def test0145(self):
        self.assertEquals(self.calculate(2112, 1947115034), 2023249536)

    def test0146(self):
        self.assertEquals(self.calculate(-11727, -1575269681), 533208991)

    def test0147(self):
        self.assertEquals(self.calculate(-19872, 1880827189), -992490016)

    def test0148(self):
        self.assertEquals(self.calculate(8304, -1593313792), 1916510208)

    def test0149(self):
        self.assertEquals(self.calculate(-8622, -1910727598), -1201197500)

    def test0150(self):
        self.assertEquals(self.calculate(-13376, -605864626), -558050176)

    def test0151(self):
        self.assertEquals(self.calculate(-6711, 789885813), -934047779)

    def test0152(self):
        self.assertEquals(self.calculate(32344, -1543519473), 1106013992)

    def test0153(self):
        self.assertEquals(self.calculate(-29319, -1418951456), 1184509408)

    def test0154(self):
        self.assertEquals(self.calculate(15506, -1965207327), 288152658)

    def test0155(self):
        self.assertEquals(self.calculate(31730, 518490505), 1978979970)

    def test0156(self):
        self.assertEquals(self.calculate(20560, 423426953), -240555312)

    def test0157(self):
        self.assertEquals(self.calculate(-1350, 1517305157), 337438242)

    def test0158(self):
        self.assertEquals(self.calculate(-24388, -1328737981), -266367692)

    def test0159(self):
        self.assertEquals(self.calculate(29468, -1154760076), 555966640)

    def test0160(self):
        self.assertEquals(self.calculate(19193, -1973836073), 2070768927)

    def test0161(self):
        self.assertEquals(self.calculate(6536, -1541385773), 1495864088)

    def test0162(self):
        self.assertEquals(self.calculate(-12531, 59753529), -1447162395)

    def test0163(self):
        self.assertEquals(self.calculate(-2246, -1271052289), -1369810746)

    def test0164(self):
        self.assertEquals(self.calculate(-27617, 474328313), 125232679)

    def test0165(self):
        self.assertEquals(self.calculate(24265, -68769203), 2057567349)

    def test0166(self):
        self.assertEquals(self.calculate(-3858, 168150894), -186087356)

    def test0167(self):
        self.assertEquals(self.calculate(32340, -1076788345), 259758668)

    def test0168(self):
        self.assertEquals(self.calculate(-22535, -1171691060), -1400898708)

    def test0169(self):
        self.assertEquals(self.calculate(27721, -1674453663), -1818424151)

    def test0170(self):
        self.assertEquals(self.calculate(30689, -1899229445), 1548736411)

    def test0171(self):
        self.assertEquals(self.calculate(2126, 1088740784), -324465760)

    def test0172(self):
        self.assertEquals(self.calculate(10909, 862012718), 2013329718)

    def test0173(self):
        self.assertEquals(self.calculate(-10311, -1687417193), 46160927)

    def test0174(self):
        self.assertEquals(self.calculate(19299, -1479880381), 1321045481)

    def test0175(self):
        self.assertEquals(self.calculate(2375, -645578318), 54819422)

    def test0176(self):
        self.assertEquals(self.calculate(-23408, 867900293), -614748464)

    def test0177(self):
        self.assertEquals(self.calculate(-21095, -323726188), 5935220)

    def test0178(self):
        self.assertEquals(self.calculate(560, -312903897), 867476816)

    def test0179(self):
        self.assertEquals(self.calculate(-17269, 130628495), -965649755)

    def test0180(self):
        self.assertEquals(self.calculate(15661, -1075995923), -2015447895)

    def test0181(self):
        self.assertEquals(self.calculate(-9966, 973924808), 491452432)

    def test0182(self):
        self.assertEquals(self.calculate(15134, -1292057395), 989482758)

    def test0183(self):
        self.assertEquals(self.calculate(28551, -496472180), -1385134380)

    def test0184(self):
        self.assertEquals(self.calculate(13508, 778821082), 1940267752)

    def test0185(self):
        self.assertEquals(self.calculate(4782, -1937555603), -1146436074)

    def test0186(self):
        self.assertEquals(self.calculate(-30431, -475314902), -1142070166)

    def test0187(self):
        self.assertEquals(self.calculate(-30864, -791583281), 1652405136)

    def test0188(self):
        self.assertEquals(self.calculate(-27568, -795155496), -666365056)

    def test0189(self):
        self.assertEquals(self.calculate(-27114, 1628588971), -1002589518)

    def test0190(self):
        self.assertEquals(self.calculate(-3412, 1052851592), -1736972448)

    def test0191(self):
        self.assertEquals(self.calculate(-22137, -1271785128), -3246744)

    def test0192(self):
        self.assertEquals(self.calculate(32640, 122101674), -331011328)

    def test0193(self):
        self.assertEquals(self.calculate(26090, -1274109758), 1523284820)

    def test0194(self):
        self.assertEquals(self.calculate(23806, -1825193572), 1625958600)

    def test0195(self):
        self.assertEquals(self.calculate(-772, -473263091), 286886092)

    def test0196(self):
        self.assertEquals(self.calculate(-20345, -1355092776), -32545304)

    def test0197(self):
        self.assertEquals(self.calculate(-1869, 659752423), -421664635)

    def test0198(self):
        self.assertEquals(self.calculate(-22378, -2029277767), 488649318)

    def test0199(self):
        self.assertEquals(self.calculate(26080, -1117953227), -1982154912)

    def test0200(self):
        self.assertEquals(self.calculate(-1846, 487746928), 1562303072)

    def test0201(self):
        self.assertEquals(self.calculate(-21941, -917277075), -240446481)

    def test0202(self):
        self.assertEquals(self.calculate(3721, 926485328), -1406833200)

    def test0203(self):
        self.assertEquals(self.calculate(-10616, 1869008875), 1350690520)

    def test0204(self):
        self.assertEquals(self.calculate(-12279, 903522546), -452816766)

    def test0205(self):
        self.assertEquals(self.calculate(-22713, 1423141464), 111797864)

    def test0206(self):
        self.assertEquals(self.calculate(25017, -2115617707), 473812589)

    def test0207(self):
        self.assertEquals(self.calculate(13742, 423529019), 455093018)

    def test0208(self):
        self.assertEquals(self.calculate(-7633, -1996361648), -315507024)

    def test0209(self):
        self.assertEquals(self.calculate(-708, 13313268), -835859152)

    def test0210(self):
        self.assertEquals(self.calculate(-12669, 2021786174), 1175914938)

    def test0211(self):
        self.assertEquals(self.calculate(-9257, -594853290), 408832058)

    def test0212(self):
        self.assertEquals(self.calculate(2494, 22536335), 371044642)

    def test0213(self):
        self.assertEquals(self.calculate(25866, 1647851418), 69332484)

    def test0214(self):
        self.assertEquals(self.calculate(-26319, -955579200), -1439520576)

    def test0215(self):
        self.assertEquals(self.calculate(4691, -1583145821), -538591527)

    def test0216(self):
        self.assertEquals(self.calculate(12087, 1356263016), -739094440)

    def test0217(self):
        self.assertEquals(self.calculate(11718, 663315345), -1161593050)

    def test0218(self):
        self.assertEquals(self.calculate(18287, -711555763), 1530668899)

    def test0219(self):
        self.assertEquals(self.calculate(12942, 1097914684), 1460025160)

    def test0220(self):
        self.assertEquals(self.calculate(-12402, -1585413720), -59325648)

    def test0221(self):
        self.assertEquals(self.calculate(-24898, 2028191707), -1986621814)

    def test0222(self):
        self.assertEquals(self.calculate(-29492, 1844138712), -168025056)

    def test0223(self):
        self.assertEquals(self.calculate(-17354, 1246060384), 1028431424)

    def test0224(self):
        self.assertEquals(self.calculate(329, -1700435509), -1097533981)

    def test0225(self):
        self.assertEquals(self.calculate(32463, 1361670647), 110803129)

    def test0226(self):
        self.assertEquals(self.calculate(2429, -1389982171), -422398703)

    def test0227(self):
        self.assertEquals(self.calculate(-25921, -1696363589), -434585979)

    def test0228(self):
        self.assertEquals(self.calculate(9667, -2647390), 177484646)

    def test0229(self):
        self.assertEquals(self.calculate(-23617, -520045386), -1694585398)

    def test0230(self):
        self.assertEquals(self.calculate(-26570, 639997064), -946465616)

    def test0231(self):
        self.assertEquals(self.calculate(16672, 1051739998), -1742222912)

    def test0232(self):
        self.assertEquals(self.calculate(30087, -26042384), -1853159536)

    def test0233(self):
        self.assertEquals(self.calculate(-30054, -220270022), 1450638052)

    def test0234(self):
        self.assertEquals(self.calculate(-30181, 1420343149), 692001407)

    def test0235(self):
        self.assertEquals(self.calculate(7703, -949625975), -639580337)

    def test0236(self):
        self.assertEquals(self.calculate(-5624, 1011764577), 667686152)

    def test0237(self):
        self.assertEquals(self.calculate(-4552, 1546333305), 542193784)

    def test0238(self):
        self.assertEquals(self.calculate(8213, -870533150), 1431786890)

    def test0239(self):
        self.assertEquals(self.calculate(-279, -1645411378), -491726210)

    def test0240(self):
        self.assertEquals(self.calculate(-8478, -827391963), 947467946)

    def test0241(self):
        self.assertEquals(self.calculate(-1208, -391514631), 503271688)

    def test0242(self):
        self.assertEquals(self.calculate(-20216, -780301063), -848588600)

    def test0243(self):
        self.assertEquals(self.calculate(-4002, 1274730600), 949286448)

    def test0244(self):
        self.assertEquals(self.calculate(26188, -1254788808), 385477792)

    def test0245(self):
        self.assertEquals(self.calculate(1517, -1768611701), 1370609583)

    def test0246(self):
        self.assertEquals(self.calculate(8039, 577969215), -860094887)

    def test0247(self):
        self.assertEquals(self.calculate(15511, -1787123463), -353106209)

    def test0248(self):
        self.assertEquals(self.calculate(27728, -987926806), 66937120)

    def test0249(self):
        self.assertEquals(self.calculate(-1927, 801426853), 1838680829)

    def test0250(self):
        self.assertEquals(self.calculate(9531, -691145188), 1175045236)

    def test0251(self):
        self.assertEquals(self.calculate(-25278, 1631275014), 611205004)

    def test0252(self):
        self.assertEquals(self.calculate(6049, 40553479), 494858599)

    def test0253(self):
        self.assertEquals(self.calculate(595, -748424502), 1364020094)

    def test0254(self):
        self.assertEquals(self.calculate(28671, 244637860), 330489692)

    def test0255(self):
        self.assertEquals(self.calculate(-16990, -113313744), 1055161952)

    def test0256(self):
        self.assertEquals(self.calculate(15420, -802710061), 306606452)

    def test0257(self):
        self.assertEquals(self.calculate(-23654, 1707667842), 992284212)

    def test0258(self):
        self.assertEquals(self.calculate(-24290, -1920051655), -995167314)

    def test0259(self):
        self.assertEquals(self.calculate(-7029, -46881711), -1180935173)

    def test0260(self):
        self.assertEquals(self.calculate(12113, 349892512), -884723296)

    def test0261(self):
        self.assertEquals(self.calculate(-13077, 1951251231), -111642251)

    def test0262(self):
        self.assertEquals(self.calculate(-1939, -1090331502), 1028872746)

    def test0263(self):
        self.assertEquals(self.calculate(32616, 1364704531), -1838072648)

    def test0264(self):
        self.assertEquals(self.calculate(-9837, -101756897), 255215821)

    def test0265(self):
        self.assertEquals(self.calculate(-73, 2097937035), 1469419101)

    def test0266(self):
        self.assertEquals(self.calculate(-27618, -2113424885), -37078710)

    def test0267(self):
        self.assertEquals(self.calculate(-18483, 997815250), -29696726)

    def test0268(self):
        self.assertEquals(self.calculate(22044, -383432408), 111636576)

    def test0269(self):
        self.assertEquals(self.calculate(14882, 62801272), -1694340624)

    def test0270(self):
        self.assertEquals(self.calculate(-31876, 1714641623), 1837434148)

    def test0271(self):
        self.assertEquals(self.calculate(16072, -1455589725), 448801112)

    def test0272(self):
        self.assertEquals(self.calculate(17138, -242342504), -32458320)

    def test0273(self):
        self.assertEquals(self.calculate(13297, 1978758194), 578050322)

    def test0274(self):
        self.assertEquals(self.calculate(-12693, 1944347859), -725291471)

    def test0275(self):
        self.assertEquals(self.calculate(-25798, 819675548), -1865789096)

    def test0276(self):
        self.assertEquals(self.calculate(-3552, -1364444988), 1785487488)

    def test0277(self):
        self.assertEquals(self.calculate(25189, -928379749), 1139429159)

    def test0278(self):
        self.assertEquals(self.calculate(19305, -1340380121), 1139722495)

    def test0279(self):
        self.assertEquals(self.calculate(-12802, -331262324), 1687550696)

    def test0280(self):
        self.assertEquals(self.calculate(-27158, -105581184), -1664358656)

    def test0281(self):
        self.assertEquals(self.calculate(-23967, -1077310124), -1451641644)

    def test0282(self):
        self.assertEquals(self.calculate(-28544, 1459540370), 62449920)

    def test0283(self):
        self.assertEquals(self.calculate(-3207, -1787527565), -1180439205)

    def test0284(self):
        self.assertEquals(self.calculate(7701, -1130572086), -636925294)

    def test0285(self):
        self.assertEquals(self.calculate(29729, 207826295), -1990014889)

    def test0286(self):
        self.assertEquals(self.calculate(21398, -1417150121), -1709179398)

    def test0287(self):
        self.assertEquals(self.calculate(11696, 1706528545), 844837808)

    def test0288(self):
        self.assertEquals(self.calculate(18113, 1210854246), 2099944422)

    def test0289(self):
        self.assertEquals(self.calculate(15646, -591408758), -1821872084)

    def test0290(self):
        self.assertEquals(self.calculate(24346, -1278417162), 1283768060)

    def test0291(self):
        self.assertEquals(self.calculate(-22659, -1395467878), 357414450)

    def test0292(self):
        self.assertEquals(self.calculate(-27738, 1964282415), 689489786)

    def test0293(self):
        self.assertEquals(self.calculate(27156, -1205839518), -947286104)

    def test0294(self):
        self.assertEquals(self.calculate(23700, -231822935), -940387916)

    def test0295(self):
        self.assertEquals(self.calculate(8071, 536612992), 1676424064)

    def test0296(self):
        self.assertEquals(self.calculate(-23580, -1994053314), -1524812488)

    def test0297(self):
        self.assertEquals(self.calculate(-23990, -1078061184), -1605252352)

    def test0298(self):
        self.assertEquals(self.calculate(-21889, 6156231), -1609754183)

    def test0299(self):
        self.assertEquals(self.calculate(-21367, -412220303), -1066709895)

    def test0300(self):
        self.assertEquals(self.calculate(7017, 2128949891), 945129659)

    def test0301(self):
        self.assertEquals(self.calculate(-9751, 1732380978), -340541310)

    def test0302(self):
        self.assertEquals(self.calculate(-2447, 621377282), -91786270)

    def test0303(self):
        self.assertEquals(self.calculate(15380, -421951769), 77377036)

    def test0304(self):
        self.assertEquals(self.calculate(31711, 60941372), -223435708)

    def test0305(self):
        self.assertEquals(self.calculate(6017, -24806179), 1065076317)

    def test0306(self):
        self.assertEquals(self.calculate(5272, 1427470681), 842727640)

    def test0307(self):
        self.assertEquals(self.calculate(32677, -1164499359), 1064688517)

    def test0308(self):
        self.assertEquals(self.calculate(-8996, 1207911365), -103380660)

    def test0309(self):
        self.assertEquals(self.calculate(-1761, -464177962), 1373604842)

    def test0310(self):
        self.assertEquals(self.calculate(27084, -472970589), 1952011492)

    def test0311(self):
        self.assertEquals(self.calculate(-24238, -205399959), 617110178)

    def test0312(self):
        self.assertEquals(self.calculate(7716, 1510729056), 244154752)

    def test0313(self):
        self.assertEquals(self.calculate(-1523, 456404846), 680121494)

    def test0314(self):
        self.assertEquals(self.calculate(-19291, 1264512272), 1708002128)

    def test0315(self):
        self.assertEquals(self.calculate(-32337, 1781805776), -1267102672)

    def test0316(self):
        self.assertEquals(self.calculate(-6566, -888094376), -1337915152)

    def test0317(self):
        self.assertEquals(self.calculate(-5085, 1247670177), -736153853)

    def test0318(self):
        self.assertEquals(self.calculate(16588, -436079821), -967144284)

    def test0319(self):
        self.assertEquals(self.calculate(-22057, -519316169), -121038799)

    def test0320(self):
        self.assertEquals(self.calculate(27538, -903726503), -1779926590)

    def test0321(self):
        self.assertEquals(self.calculate(26696, -694103263), -1291794104)

    def test0322(self):
        self.assertEquals(self.calculate(10818, 1459922918), 851379532)

    def test0323(self):
        self.assertEquals(self.calculate(-4961, -484091550), 691461086)

    def test0324(self):
        self.assertEquals(self.calculate(-5581, -1860670436), -829218412)

    def test0325(self):
        self.assertEquals(self.calculate(-29087, -399545367), -605413047)

    def test0326(self):
        self.assertEquals(self.calculate(-27692, 1072648712), 205686432)

    def test0327(self):
        self.assertEquals(self.calculate(3994, -754769478), 517746660)

    def test0328(self):
        self.assertEquals(self.calculate(26907, 1795823030), 1828188210)

    def test0329(self):
        self.assertEquals(self.calculate(962, -323221794), -1701720516)

    def test0330(self):
        self.assertEquals(self.calculate(-28238, -1100645907), 1655768010)

    def test0331(self):
        self.assertEquals(self.calculate(4227, 1038825657), 1659475627)

    def test0332(self):
        self.assertEquals(self.calculate(-21588, -701657325), -971320892)

    def test0333(self):
        self.assertEquals(self.calculate(9753, -734466439), 754270161)

    def test0334(self):
        self.assertEquals(self.calculate(-15736, 118563789), -1703977240)

    def test0335(self):
        self.assertEquals(self.calculate(10711, 9269317), 499406579)

    def test0336(self):
        self.assertEquals(self.calculate(-9589, -369475271), -449645581)

    def test0337(self):
        self.assertEquals(self.calculate(-24463, -246697534), 532723362)

    def test0338(self):
        self.assertEquals(self.calculate(25686, -1969015983), 1390338358)

    def test0339(self):
        self.assertEquals(self.calculate(-17355, 1045136699), -700520137)

    def test0340(self):
        self.assertEquals(self.calculate(-28109, -1156015765), -1275423151)

    def test0341(self):
        self.assertEquals(self.calculate(27999, 1162287883), -68765675)

    def test0342(self):
        self.assertEquals(self.calculate(-14429, 1379385051), -268451215)

    def test0343(self):
        self.assertEquals(self.calculate(-18827, -539777742), 502926298)

    def test0344(self):
        self.assertEquals(self.calculate(-1015, -1844318826), -622132666)

    def test0345(self):
        self.assertEquals(self.calculate(-8686, -782128349), -1071422858)

    def test0346(self):
        self.assertEquals(self.calculate(-14159, 153168569), 244716009)

    def test0347(self):
        self.assertEquals(self.calculate(22751, -1580669409), -48554751)

    def test0348(self):
        self.assertEquals(self.calculate(-27754, -1915764440), -1568856720)

    def test0349(self):
        self.assertEquals(self.calculate(11724, 2043062839), -163885356)

    def test0350(self):
        self.assertEquals(self.calculate(23763, -423520973), -1020506871)

    def test0351(self):
        self.assertEquals(self.calculate(1094, -327630277), -1945237470)

    def test0352(self):
        self.assertEquals(self.calculate(437, -1908062630), -599713886)

    def test0353(self):
        self.assertEquals(self.calculate(4075, 654331342), -774472166)

    def test0354(self):
        self.assertEquals(self.calculate(-30299, -1050714089), 1288584659)

    def test0355(self):
        self.assertEquals(self.calculate(8603, 480804982), 311754098)

    def test0356(self):
        self.assertEquals(self.calculate(22732, -1025754051), -63637348)

    def test0357(self):
        self.assertEquals(self.calculate(16712, 297019705), -1188884216)

    def test0358(self):
        self.assertEquals(self.calculate(23040, -1529502233), 475215360)

    def test0359(self):
        self.assertEquals(self.calculate(-22133, -1938489872), -2126950064)

    def test0360(self):
        self.assertEquals(self.calculate(-13528, -545269133), 1941983992)

    def test0361(self):
        self.assertEquals(self.calculate(11634, -968163955), 2079764938)

    def test0362(self):
        self.assertEquals(self.calculate(-26371, 2021173330), 182257930)

    def test0363(self):
        self.assertEquals(self.calculate(22585, -174964855), -211337855)

    def test0364(self):
        self.assertEquals(self.calculate(-29552, 833211197), -9785776)

    def test0365(self):
        self.assertEquals(self.calculate(16676, 2105258037), 220347508)

    def test0366(self):
        self.assertEquals(self.calculate(24390, 1716480964), 1924477848)

    def test0367(self):
        self.assertEquals(self.calculate(-4672, 868619227), 555066176)

    def test0368(self):
        self.assertEquals(self.calculate(6190, 1799856233), -35083554)

    def test0369(self):
        self.assertEquals(self.calculate(-449, -1386493258), -234785078)

    def test0370(self):
        self.assertEquals(self.calculate(14493, 884379101), 1123899529)

    def test0371(self):
        self.assertEquals(self.calculate(9217, -1987111736), -1468320568)

    def test0372(self):
        self.assertEquals(self.calculate(-4687, 1911324778), 922544970)

    def test0373(self):
        self.assertEquals(self.calculate(-4526, 1386241255), 819299326)

    def test0374(self):
        self.assertEquals(self.calculate(-25338, -1800227156), 1602995208)

    def test0375(self):
        self.assertEquals(self.calculate(-27467, -1211439680), 1502048448)

    def test0376(self):
        self.assertEquals(self.calculate(-15734, -168657357), -634933890)

    def test0377(self):
        self.assertEquals(self.calculate(-32418, 323961135), -977035710)

    def test0378(self):
        self.assertEquals(self.calculate(4823, -364778922), 1607850554)

    def test0379(self):
        self.assertEquals(self.calculate(16452, -1498606362), -1959588584)

    def test0380(self):
        self.assertEquals(self.calculate(-6318, 1976658477), 1236639082)

    def test0381(self):
        self.assertEquals(self.calculate(-29366, 154116604), 1107336920)

    def test0382(self):
        self.assertEquals(self.calculate(-23475, -1221556436), -1459300292)

    def test0383(self):
        self.assertEquals(self.calculate(7683, 1379147653), 307098767)

    def test0384(self):
        self.assertEquals(self.calculate(-22746, -474942548), 1200447368)

    def test0385(self):
        self.assertEquals(self.calculate(-11606, -763997365), 2140919246)

    def test0386(self):
        self.assertEquals(self.calculate(2503, 36630908), 1492849508)

    def test0387(self):
        self.assertEquals(self.calculate(-13515, -2137111205), -597130025)

    def test0388(self):
        self.assertEquals(self.calculate(-784, 430607473), 1706157552)

    def test0389(self):
        self.assertEquals(self.calculate(21785, 1075036142), -794311618)

    def test0390(self):
        self.assertEquals(self.calculate(7200, 1035764477), 1441008544)

    def test0391(self):
        self.assertEquals(self.calculate(-9793, 1589205186), 1875094206)

    def test0392(self):
        self.assertEquals(self.calculate(1817, -694347627), 1090746765)

    def test0393(self):
        self.assertEquals(self.calculate(639, -1508552763), -1892541253)

    def test0394(self):
        self.assertEquals(self.calculate(23237, 1637910380), -1876677092)

    def test0395(self):
        self.assertEquals(self.calculate(-32041, 613054757), -2002024429)

    def test0396(self):
        self.assertEquals(self.calculate(15279, 2058642128), 1947565104)

    def test0397(self):
        self.assertEquals(self.calculate(-24303, -1418194942), -720874974)

    def test0398(self):
        self.assertEquals(self.calculate(-15577, -923355023), -744281033)

    def test0399(self):
        self.assertEquals(self.calculate(1059, 1192039460), -350596884)

    def test0400(self):
        self.assertEquals(self.calculate(-375, 936309686), 1071186022)

    def test0401(self):
        self.assertEquals(self.calculate(-1992, -1309818355), 2113014488)

    def test0402(self):
        self.assertEquals(self.calculate(13061, -1015230314), -1359088402)

    def test0403(self):
        self.assertEquals(self.calculate(4500, 1438611650), 1236709928)

    def test0404(self):
        self.assertEquals(self.calculate(-6179, -506904389), 1131060847)

    def test0405(self):
        self.assertEquals(self.calculate(-6714, 189222253), 872112974)

    def test0406(self):
        self.assertEquals(self.calculate(-4369, 1414873719), -1125339367)

    def test0407(self):
        self.assertEquals(self.calculate(21481, -163239872), -1862376896)

    def test0408(self):
        self.assertEquals(self.calculate(1401, 872586085), -1572574275)

    def test0409(self):
        self.assertEquals(self.calculate(9991, 1005990640), 629011600)

    def test0410(self):
        self.assertEquals(self.calculate(27718, -1121290747), -1553571490)

    def test0411(self):
        self.assertEquals(self.calculate(18277, 996351870), -338207050)

    def test0412(self):
        self.assertEquals(self.calculate(-17091, -1467155430), 1134380082)

    def test0413(self):
        self.assertEquals(self.calculate(12451, 434579530), -709064930)

    def test0414(self):
        self.assertEquals(self.calculate(-12132, 1048463929), 1728744124)

    def test0415(self):
        self.assertEquals(self.calculate(-11761, -1139411898), 325368858)

    def test0416(self):
        self.assertEquals(self.calculate(-23810, 174238077), 329794566)

    def test0417(self):
        self.assertEquals(self.calculate(-554, -186110767), 26149814)

    def test0418(self):
        self.assertEquals(self.calculate(-15693, -2093074734), -1288079146)

    def test0419(self):
        self.assertEquals(self.calculate(-18604, -1288967988), 1158035184)

    def test0420(self):
        self.assertEquals(self.calculate(-10746, -96069320), 1568761680)

    def test0421(self):
        self.assertEquals(self.calculate(-8188, -372535180), 891273680)

    def test0422(self):
        self.assertEquals(self.calculate(29047, 1301282257), -1661453017)

    def test0423(self):
        self.assertEquals(self.calculate(-20392, -1086839798), 805913456)

    def test0424(self):
        self.assertEquals(self.calculate(17933, 663966183), 1256215227)

    def test0425(self):
        self.assertEquals(self.calculate(-12350, -727883564), -4535128)

    def test0426(self):
        self.assertEquals(self.calculate(16226, 136812317), -581436390)

    def test0427(self):
        self.assertEquals(self.calculate(7798, 1217984529), 1670665686)

    def test0428(self):
        self.assertEquals(self.calculate(19923, -1694904767), -554791789)

    def test0429(self):
        self.assertEquals(self.calculate(-6530, -1514629143), -781378898)

    def test0430(self):
        self.assertEquals(self.calculate(5614, -345732036), 385567688)

    def test0431(self):
        self.assertEquals(self.calculate(28867, -1040696142), 1520704406)

    def test0432(self):
        self.assertEquals(self.calculate(-27481, -1386425890), -284999726)

    def test0433(self):
        self.assertEquals(self.calculate(11687, 846342091), -109665171)

    def test0434(self):
        self.assertEquals(self.calculate(-7366, 1769747316), -732986296)

    def test0435(self):
        self.assertEquals(self.calculate(-20594, 1605359463), 1885463586)

    def test0436(self):
        self.assertEquals(self.calculate(2381, -937842525), 379941895)

    def test0437(self):
        self.assertEquals(self.calculate(4631, 77854023), -235272351)

    def test0438(self):
        self.assertEquals(self.calculate(-30815, -155312049), 1347222191)

    def test0439(self):
        self.assertEquals(self.calculate(1194, -729097368), 1336103696)

    def test0440(self):
        self.assertEquals(self.calculate(-5324, 1614270590), -147061864)

    def test0441(self):
        self.assertEquals(self.calculate(4262, 1278401537), -1766147930)

    def test0442(self):
        self.assertEquals(self.calculate(-29949, -507477923), -1432944617)

    def test0443(self):
        self.assertEquals(self.calculate(21210, 812403895), -322178602)

    def test0444(self):
        self.assertEquals(self.calculate(4684, 1590079757), 460290524)

    def test0445(self):
        self.assertEquals(self.calculate(11392, -353927487), 1032359040)

    def test0446(self):
        self.assertEquals(self.calculate(14676, -972076355), 1688771332)

    def test0447(self):
        self.assertEquals(self.calculate(-30027, 632524520), -468379128)

    def test0448(self):
        self.assertEquals(self.calculate(-7169, 861656114), -1049709618)

    def test0449(self):
        self.assertEquals(self.calculate(18914, -1709129785), 1738083502)

    def test0450(self):
        self.assertEquals(self.calculate(16361, 984716531), 524836395)

    def test0451(self):
        self.assertEquals(self.calculate(10268, -1981087155), -837793684)

    def test0452(self):
        self.assertEquals(self.calculate(21652, -1832995170), 1781361496)

    def test0453(self):
        self.assertEquals(self.calculate(3133, 1330649847), -1487273765)

    def test0454(self):
        self.assertEquals(self.calculate(-16946, -1338186176), -524384384)

    def test0455(self):
        self.assertEquals(self.calculate(28373, -1939687466), 958458126)

    def test0456(self):
        self.assertEquals(self.calculate(2004, 511894937), -659729996)

    def test0457(self):
        self.assertEquals(self.calculate(30849, 1577381895), -1325384825)

    def test0458(self):
        self.assertEquals(self.calculate(7386, -744931278), -209313132)

    def test0459(self):
        self.assertEquals(self.calculate(31243, -162147356), 2091565772)

    def test0460(self):
        self.assertEquals(self.calculate(-11132, -1704624257), 711715196)

    def test0461(self):
        self.assertEquals(self.calculate(-19612, 1174305586), -866511480)

    def test0462(self):
        self.assertEquals(self.calculate(15207, 794406887), -1197473039)

    def test0463(self):
        self.assertEquals(self.calculate(26899, -1626412408), -330485736)

    def test0464(self):
        self.assertEquals(self.calculate(-31812, -515164253), -1189985100)

    def test0465(self):
        self.assertEquals(self.calculate(-8441, -1131211787), 846395059)

    def test0466(self):
        self.assertEquals(self.calculate(-21139, 805960377), 938853829)

    def test0467(self):
        self.assertEquals(self.calculate(-29506, 940353218), -573318148)

    def test0468(self):
        self.assertEquals(self.calculate(-4699, 162940564), -1153531548)

    def test0469(self):
        self.assertEquals(self.calculate(-14449, -1842893494), -829140394)

    def test0470(self):
        self.assertEquals(self.calculate(-6418, -559211531), -1573053498)

    def test0471(self):
        self.assertEquals(self.calculate(1610, 438784999), 2069211846)

    def test0472(self):
        self.assertEquals(self.calculate(600, -2128882793), -1724388888)

    def test0473(self):
        self.assertEquals(self.calculate(-13041, -1910128188), -828617092)

    def test0474(self):
        self.assertEquals(self.calculate(22118, 1334036676), -202123752)

    def test0475(self):
        self.assertEquals(self.calculate(7874, -78492675), 423967674)

    def test0476(self):
        self.assertEquals(self.calculate(-1231, 887218771), -1244613917)

    def test0477(self):
        self.assertEquals(self.calculate(12059, 1616776206), 1847711610)

    def test0478(self):
        self.assertEquals(self.calculate(23314, 626337062), -466542932)

    def test0479(self):
        self.assertEquals(self.calculate(-23723, 316836016), -108039568)

    def test0480(self):
        self.assertEquals(self.calculate(7462, 2141097874), -406005332)

    def test0481(self):
        self.assertEquals(self.calculate(16961, 1396782233), -216150823)

    def test0482(self):
        self.assertEquals(self.calculate(-32365, -1253349533), -1308475175)

    def test0483(self):
        self.assertEquals(self.calculate(-30476, 1893369283), 563353052)

    def test0484(self):
        self.assertEquals(self.calculate(-27037, 1225814822), 1907280818)

    def test0485(self):
        self.assertEquals(self.calculate(17367, -1784463475), 1706837611)

    def test0486(self):
        self.assertEquals(self.calculate(9784, 125918876), -665331168)

    def test0487(self):
        self.assertEquals(self.calculate(21156, 900508626), -1314433400)

    def test0488(self):
        self.assertEquals(self.calculate(-14943, 1238935097), -2098108711)

    def test0489(self):
        self.assertEquals(self.calculate(925, -1355293448), 484011032)

    def test0490(self):
        self.assertEquals(self.calculate(-14996, -572704552), -1657130208)

    def test0491(self):
        self.assertEquals(self.calculate(27645, 1392560055), 1530846427)

    def test0492(self):
        self.assertEquals(self.calculate(31354, 1194194623), -746676986)

    def test0493(self):
        self.assertEquals(self.calculate(-14004, -460481327), 1834592012)

    def test0494(self):
        self.assertEquals(self.calculate(-27859, 101551720), 1254080584)

    def test0495(self):
        self.assertEquals(self.calculate(19922, 759827128), 1811292912)

    def test0496(self):
        self.assertEquals(self.calculate(9411, -98346805), -2123813215)

    def test0497(self):
        self.assertEquals(self.calculate(23142, 1261617383), -838200822)

    def test0498(self):
        self.assertEquals(self.calculate(27089, 712402760), 990304712)

    def test0499(self):
        self.assertEquals(self.calculate(-8075, 996256974), -301319642)

    def test0500(self):
        self.assertEquals(self.calculate(21222, 114068147), -1607339310)

    def test0501(self):
        self.assertEquals(self.calculate(-9069, -2056192456), -1138615768)

    def test0502(self):
        self.assertEquals(self.calculate(-12711, 1132981134), -297850786)

    def test0503(self):
        self.assertEquals(self.calculate(-20484, 1868428410), -433975784)

    def test0504(self):
        self.assertEquals(self.calculate(-28435, -1008979503), -49369475)

    def test0505(self):
        self.assertEquals(self.calculate(280, 869860429), -1252215752)

    def test0506(self):
        self.assertEquals(self.calculate(-10849, 722431565), 655266515)

    def test0507(self):
        self.assertEquals(self.calculate(-23318, 1723873451), -682207154)

    def test0508(self):
        self.assertEquals(self.calculate(-29521, -374337181), -142932307)

    def test0509(self):
        self.assertEquals(self.calculate(6503, 1152150334), 2010657778)

    def test0510(self):
        self.assertEquals(self.calculate(-11159, 845383957), -1891394147)

    def test0511(self):
        self.assertEquals(self.calculate(20358, 127859742), 218446260)

    def test0512(self):
        self.assertEquals(self.calculate(-19545, -1875027907), -1535494453)

    def test0513(self):
        self.assertEquals(self.calculate(-24975, -347458187), 1934282405)

    def test0514(self):
        self.assertEquals(self.calculate(20074, 352484357), 1959845906)

    def test0515(self):
        self.assertEquals(self.calculate(14258, 269406588), 1498369080)

    def test0516(self):
        self.assertEquals(self.calculate(-31164, -1849185879), -1842444572)

    def test0517(self):
        self.assertEquals(self.calculate(-4382, 1316013057), 1371862754)

    def test0518(self):
        self.assertEquals(self.calculate(17350, -258244348), -888548072)

    def test0519(self):
        self.assertEquals(self.calculate(150, -862666744), -550992720)

    def test0520(self):
        self.assertEquals(self.calculate(31935, -1032253056), -1127346560)

    def test0521(self):
        self.assertEquals(self.calculate(-1611, -310215479), 1540930333)

    def test0522(self):
        self.assertEquals(self.calculate(23465, 1585240756), -1037411116)

    def test0523(self):
        self.assertEquals(self.calculate(-27061, 1875619022), 1797149786)

    def test0524(self):
        self.assertEquals(self.calculate(4126, -121218505), -1931345294)

    def test0525(self):
        self.assertEquals(self.calculate(-2625, -432008440), 150788856)

    def test0526(self):
        self.assertEquals(self.calculate(-30263, -12683850), 1599263206)

    def test0527(self):
        self.assertEquals(self.calculate(2077, 462956305), -512428819)

    def test0528(self):
        self.assertEquals(self.calculate(32599, 1654285853), 455153371)

    def test0529(self):
        self.assertEquals(self.calculate(-9369, -1390112365), 1621906213)

    def test0530(self):
        self.assertEquals(self.calculate(15365, -675945900), -677831772)

    def test0531(self):
        self.assertEquals(self.calculate(-12710, 487034036), -1154724024)

    def test0532(self):
        self.assertEquals(self.calculate(22239, -1297017409), 630201185)

    def test0533(self):
        self.assertEquals(self.calculate(31020, 323984910), -211564440)

    def test0534(self):
        self.assertEquals(self.calculate(8052, 2098095719), 1760354220)

    def test0535(self):
        self.assertEquals(self.calculate(19327, -522686539), -199659061)

    def test0536(self):
        self.assertEquals(self.calculate(-19208, -90983981), -431382424)

    def test0537(self):
        self.assertEquals(self.calculate(-27840, 943640928), 1351514112)

    def test0538(self):
        self.assertEquals(self.calculate(5699, -1754254131), 1189572519)

    def test0539(self):
        self.assertEquals(self.calculate(2753, -612997091), 341155805)

    def test0540(self):
        self.assertEquals(self.calculate(29381, 1550787335), -1625353629)

    def test0541(self):
        self.assertEquals(self.calculate(-2063, 1039501369), -1302643543)

    def test0542(self):
        self.assertEquals(self.calculate(-5693, -1987975592), 306220296)

    def test0543(self):
        self.assertEquals(self.calculate(20908, 51734165), -673836772)

    def test0544(self):
        self.assertEquals(self.calculate(-11858, 369920212), -1352264680)

    def test0545(self):
        self.assertEquals(self.calculate(-15060, -1424034747), 1191580892)

    def test0546(self):
        self.assertEquals(self.calculate(26562, 385021044), 611838952)

    def test0547(self):
        self.assertEquals(self.calculate(-32495, -295912706), -748394274)

    def test0548(self):
        self.assertEquals(self.calculate(-3596, 646261491), -379014500)

    def test0549(self):
        self.assertEquals(self.calculate(14789, 523538310), -1217968098)

    def test0550(self):
        self.assertEquals(self.calculate(-32762, 236327080), 1278239728)

    def test0551(self):
        self.assertEquals(self.calculate(10453, 1080840383), -2034432277)

    def test0552(self):
        self.assertEquals(self.calculate(19845, -1311254252), 1366215524)

    def test0553(self):
        self.assertEquals(self.calculate(14234, -1647975089), 1833953926)

    def test0554(self):
        self.assertEquals(self.calculate(-6150, -1974952866), -207387188)

    def test0555(self):
        self.assertEquals(self.calculate(-22805, 1310453817), -516851117)

    def test0556(self):
        self.assertEquals(self.calculate(2668, 1847800340), -691148688)

    def test0557(self):
        self.assertEquals(self.calculate(-27003, 39867231), 1501952603)

    def test0558(self):
        self.assertEquals(self.calculate(-29773, -956202688), 1979391936)

    def test0559(self):
        self.assertEquals(self.calculate(11681, -1181975730), 1661354510)

    def test0560(self):
        self.assertEquals(self.calculate(-5927, 969668436), -558578124)

    def test0561(self):
        self.assertEquals(self.calculate(-6163, -1670671344), 1310884560)

    def test0562(self):
        self.assertEquals(self.calculate(-18925, 1953547660), 189018468)

    def test0563(self):
        self.assertEquals(self.calculate(15035, 72506002), -793953114)

    def test0564(self):
        self.assertEquals(self.calculate(21729, 669264322), -314811518)

    def test0565(self):
        self.assertEquals(self.calculate(8625, -1925229068), -757145164)

    def test0566(self):
        self.assertEquals(self.calculate(6309, 825456061), -1993041199)

    def test0567(self):
        self.assertEquals(self.calculate(-31137, -1405267766), -1304381706)

    def test0568(self):
        self.assertEquals(self.calculate(19813, -1481616257), 838568219)

    def test0569(self):
        self.assertEquals(self.calculate(-3960, -1987042489), 308170168)

    def test0570(self):
        self.assertEquals(self.calculate(-32206, -63451445), -887195226)

    def test0571(self):
        self.assertEquals(self.calculate(-23028, -1841902323), -1770321252)

    def test0572(self):
        self.assertEquals(self.calculate(-12378, -810620589), 818047186)

    def test0573(self):
        self.assertEquals(self.calculate(-22210, 1560743496), 567999856)

    def test0574(self):
        self.assertEquals(self.calculate(-20805, -27042325), -25144151)

    def test0575(self):
        self.assertEquals(self.calculate(-31586, -935263158), 437046700)

    def test0576(self):
        self.assertEquals(self.calculate(26688, 1307566541), -273433792)

    def test0577(self):
        self.assertEquals(self.calculate(30414, 428365597), 1675458390)

    def test0578(self):
        self.assertEquals(self.calculate(-23864, 1062776752), -322526848)

    def test0579(self):
        self.assertEquals(self.calculate(-3533, 1415258925), -767849481)

    def test0580(self):
        self.assertEquals(self.calculate(23430, -761501226), -679577596)

    def test0581(self):
        self.assertEquals(self.calculate(5052, -1485503655), -1456598948)

    def test0582(self):
        self.assertEquals(self.calculate(-9117, 1511764752), -209191120)

    def test0583(self):
        self.assertEquals(self.calculate(29649, -277091107), 798205805)

    def test0584(self):
        self.assertEquals(self.calculate(-5193, 933229358), -1536946206)

    def test0585(self):
        self.assertEquals(self.calculate(-29608, 1987432755), 1437912456)

    def test0586(self):
        self.assertEquals(self.calculate(-26090, -1192401426), 1305079412)

    def test0587(self):
        self.assertEquals(self.calculate(-25776, -1968330425), -763632848)

    def test0588(self):
        self.assertEquals(self.calculate(-16866, -1802863677), -1269679398)

    def test0589(self):
        self.assertEquals(self.calculate(-28244, 2009316269), -1725819588)

    def test0590(self):
        self.assertEquals(self.calculate(15016, -1574160842), 1900793712)

    def test0591(self):
        self.assertEquals(self.calculate(-12189, -824666392), 1635179448)

    def test0592(self):
        self.assertEquals(self.calculate(-7802, -382432942), -1260457236)

    def test0593(self):
        self.assertEquals(self.calculate(-32174, -1968230942), 864515684)

    def test0594(self):
        self.assertEquals(self.calculate(-9516, 1712495169), -998107180)

    def test0595(self):
        self.assertEquals(self.calculate(-21357, -125236776), -1082800376)

    def test0596(self):
        self.assertEquals(self.calculate(-24692, -1471488240), -1435702080)

    def test0597(self):
        self.assertEquals(self.calculate(-7116, 1405843373), -1002609884)

    def test0598(self):
        self.assertEquals(self.calculate(-29078, -90882695), 1282118170)

    def test0599(self):
        self.assertEquals(self.calculate(-29179, -1637486246), -1299995966)

    def test0600(self):
        self.assertEquals(self.calculate(32470, -707220316), 1746471192)

    def test0601(self):
        self.assertEquals(self.calculate(-5064, 763285370), 193452720)

    def test0602(self):
        self.assertEquals(self.calculate(26667, -2096864889), -916768339)

    def test0603(self):
        self.assertEquals(self.calculate(1813, -119966161), 1544682203)

    def test0604(self):
        self.assertEquals(self.calculate(30924, -873922939), -1258739204)

    def test0605(self):
        self.assertEquals(self.calculate(-21015, 1567931702), 904377382)

    def test0606(self):
        self.assertEquals(self.calculate(399, 633150997), -775822661)

    def test0607(self):
        self.assertEquals(self.calculate(26937, 2124612133), 237807421)

    def test0608(self):
        self.assertEquals(self.calculate(-21507, 2002640761), -862802539)

    def test0609(self):
        self.assertEquals(self.calculate(21774, -1366547258), 333430996)

    def test0610(self):
        self.assertEquals(self.calculate(18387, -1878741430), 3288318)

    def test0611(self):
        self.assertEquals(self.calculate(-31020, -1756773515), 569383652)

    def test0612(self):
        self.assertEquals(self.calculate(-9761, -391731582), 1171078462)

    def test0613(self):
        self.assertEquals(self.calculate(-23570, 3896065), -1635938834)

    def test0614(self):
        self.assertEquals(self.calculate(12407, 1134351986), -702738690)

    def test0615(self):
        self.assertEquals(self.calculate(23028, 1223270094), -1226769832)

    def test0616(self):
        self.assertEquals(self.calculate(-28682, 1096813608), 1827538544)

    def test0617(self):
        self.assertEquals(self.calculate(20290, 1443371012), -1384157944)

    def test0618(self):
        self.assertEquals(self.calculate(29014, -340717250), 1444423892)

    def test0619(self):
        self.assertEquals(self.calculate(-26285, 1708276201), 1843136395)

    def test0620(self):
        self.assertEquals(self.calculate(31334, -718220798), 898146508)

    def test0621(self):
        self.assertEquals(self.calculate(27071, -796756215), 338264247)

    def test0622(self):
        self.assertEquals(self.calculate(-13885, 1455888038), 1405654642)

    def test0623(self):
        self.assertEquals(self.calculate(31053, 376366435), 700893639)

    def test0624(self):
        self.assertEquals(self.calculate(-21001, -500509376), 1412432064)

    def test0625(self):
        self.assertEquals(self.calculate(24857, -996548682), -2134192442)

    def test0626(self):
        self.assertEquals(self.calculate(-8168, 101198354), -1954434640)

    def test0627(self):
        self.assertEquals(self.calculate(22445, 1948542868), -607302908)

    def test0628(self):
        self.assertEquals(self.calculate(4898, -644423198), 416138756)

    def test0629(self):
        self.assertEquals(self.calculate(-22467, -935813955), 1067213065)

    def test0630(self):
        self.assertEquals(self.calculate(-30170, -91105051), -139680770)

    def test0631(self):
        self.assertEquals(self.calculate(18788, -1841610602), 76546200)

    def test0632(self):
        self.assertEquals(self.calculate(-10947, -1887887691), -676074975)

    def test0633(self):
        self.assertEquals(self.calculate(-3957, 1073880728), -1623384952)

    def test0634(self):
        self.assertEquals(self.calculate(-26194, -779019839), 256039470)

    def test0635(self):
        self.assertEquals(self.calculate(-21223, 1351116447), -1542686585)

    def test0636(self):
        self.assertEquals(self.calculate(-22971, -1166060595), -2133097407)

    def test0637(self):
        self.assertEquals(self.calculate(-10751, 1262825166), -241737010)

    def test0638(self):
        self.assertEquals(self.calculate(14111, 1832341613), 469379123)

    def test0639(self):
        self.assertEquals(self.calculate(-30746, -1130782480), -722131040)

    def test0640(self):
        self.assertEquals(self.calculate(-2895, 1859705441), 2041737489)

    def test0641(self):
        self.assertEquals(self.calculate(5200, 866136808), -1509291904)

    def test0642(self):
        self.assertEquals(self.calculate(-14866, 400434246), -30828780)

    def test0643(self):
        self.assertEquals(self.calculate(7484, 1187438873), 505190108)

    def test0644(self):
        self.assertEquals(self.calculate(16565, 704947548), -559945204)

    def test0645(self):
        self.assertEquals(self.calculate(-11880, -1284745056), -1542504704)

    def test0646(self):
        self.assertEquals(self.calculate(-12576, 1454366089), -2137188896)

    def test0647(self):
        self.assertEquals(self.calculate(30735, 1099272455), 1926154089)

    def test0648(self):
        self.assertEquals(self.calculate(-26963, -908929315), 377729369)

    def test0649(self):
        self.assertEquals(self.calculate(-22738, -575414187), 1297400390)

    def test0650(self):
        self.assertEquals(self.calculate(-4298, -601423478), -652203748)

    def test0651(self):
        self.assertEquals(self.calculate(14627, 261677297), 737962483)

    def test0652(self):
        self.assertEquals(self.calculate(2492, 999390579), -599708812)

    def test0653(self):
        self.assertEquals(self.calculate(-8898, 1347317531), -1177667702)

    def test0654(self):
        self.assertEquals(self.calculate(-337, 1767858496), 1232140992)

    def test0655(self):
        self.assertEquals(self.calculate(-2098, 1274427006), 2016766820)

    def test0656(self):
        self.assertEquals(self.calculate(-3021, 1359870468), 2115018444)

    def test0657(self):
        self.assertEquals(self.calculate(9533, 823117128), -129668568)

    def test0658(self):
        self.assertEquals(self.calculate(23951, -261853953), -1011776143)

    def test0659(self):
        self.assertEquals(self.calculate(20139, -2132612858), 982612738)

    def test0660(self):
        self.assertEquals(self.calculate(-17241, 1966075975), -1233984943)

    def test0661(self):
        self.assertEquals(self.calculate(1723, -24710364), 373715788)

    def test0662(self):
        self.assertEquals(self.calculate(-442, 1616740270), -1634628204)

    def test0663(self):
        self.assertEquals(self.calculate(10818, 1110125617), 610365090)

    def test0664(self):
        self.assertEquals(self.calculate(10153, 2073309258), 674178778)

    def test0665(self):
        self.assertEquals(self.calculate(3147, -725916003), 464940031)

    def test0666(self):
        self.assertEquals(self.calculate(12166, 1240518025), -372785994)

    def test0667(self):
        self.assertEquals(self.calculate(2597, -292779503), -139157899)

    def test0668(self):
        self.assertEquals(self.calculate(-2380, -2125916134), 208924232)

    def test0669(self):
        self.assertEquals(self.calculate(19613, -1138385026), -1905510330)

    def test0670(self):
        self.assertEquals(self.calculate(6750, -1096562595), -1568865242)

    def test0671(self):
        self.assertEquals(self.calculate(13897, 756353606), 1261089270)

    def test0672(self):
        self.assertEquals(self.calculate(4647, -1199741621), -331762579)

    def test0673(self):
        self.assertEquals(self.calculate(-12703, 1588886506), -1573961814)

    def test0674(self):
        self.assertEquals(self.calculate(-24030, 1673970275), 1157986086)

    def test0675(self):
        self.assertEquals(self.calculate(-16113, 400088563), 118895677)

    def test0676(self):
        self.assertEquals(self.calculate(-5773, 708716972), 1680753732)

    def test0677(self):
        self.assertEquals(self.calculate(-12769, -1580210987), -42263605)

    def test0678(self):
        self.assertEquals(self.calculate(-10608, 918898615), 1899254000)

    def test0679(self):
        self.assertEquals(self.calculate(11726, 725993095), 369851298)

    def test0680(self):
        self.assertEquals(self.calculate(-14907, -148887471), -1032561835)

    def test0681(self):
        self.assertEquals(self.calculate(-9528, 344045347), -1004019368)

    def test0682(self):
        self.assertEquals(self.calculate(-24506, 1721000880), 1731281440)

    def test0683(self):
        self.assertEquals(self.calculate(-27963, -941125542), 1428908354)

    def test0684(self):
        self.assertEquals(self.calculate(4990, 861054076), 1692543240)

    def test0685(self):
        self.assertEquals(self.calculate(18758, 1979107660), -1595820344)

    def test0686(self):
        self.assertEquals(self.calculate(-28982, -741997145), -339994682)

    def test0687(self):
        self.assertEquals(self.calculate(23924, 1775478947), -668229412)

    def test0688(self):
        self.assertEquals(self.calculate(11385, -1957916044), 6105300)

    def test0689(self):
        self.assertEquals(self.calculate(-17367, 262336075), 969686531)

    def test0690(self):
        self.assertEquals(self.calculate(-9159, 1490484173), -1938473819)

    def test0691(self):
        self.assertEquals(self.calculate(-28253, -434156295), -208794741)

    def test0692(self):
        self.assertEquals(self.calculate(11365, -1629162372), 173655276)

    def test0693(self):
        self.assertEquals(self.calculate(1530, -1830447162), -265480868)

    def test0694(self):
        self.assertEquals(self.calculate(16809, -1218491458), 1076117102)

    def test0695(self):
        self.assertEquals(self.calculate(17599, -1391247017), 1052302313)

    def test0696(self):
        self.assertEquals(self.calculate(-13529, 1406730209), -652908985)

    def test0697(self):
        self.assertEquals(self.calculate(14049, 443620682), 429414922)

    def test0698(self):
        self.assertEquals(self.calculate(-31587, -1115977128), 1572943864)

    def test0699(self):
        self.assertEquals(self.calculate(27266, -1893139409), -1422162466)

    def test0700(self):
        self.assertEquals(self.calculate(7071, -997358991), 10874671)

    def test0701(self):
        self.assertEquals(self.calculate(20139, 2134226516), 1450074652)

    def test0702(self):
        self.assertEquals(self.calculate(23231, 1185795551), -703791263)

    def test0703(self):
        self.assertEquals(self.calculate(-26533, 1347689091), 1663054993)

    def test0704(self):
        self.assertEquals(self.calculate(20514, -1736855517), 1194611878)

    def test0705(self):
        self.assertEquals(self.calculate(-24825, 1870561988), 485052252)

    def test0706(self):
        self.assertEquals(self.calculate(16694, 899432024), -87458160)

    def test0707(self):
        self.assertEquals(self.calculate(-6062, 1381747094), -964656628)

    def test0708(self):
        self.assertEquals(self.calculate(28934, -487044380), -354392744)

    def test0709(self):
        self.assertEquals(self.calculate(13544, 1237824800), 1841734912)

    def test0710(self):
        self.assertEquals(self.calculate(-28231, 445523945), -1922248607)

    def test0711(self):
        self.assertEquals(self.calculate(16745, 1755165379), -216935173)

    def test0712(self):
        self.assertEquals(self.calculate(-6789, -1161850332), -2053018804)

    def test0713(self):
        self.assertEquals(self.calculate(6, -1346196145), 512757722)

    def test0714(self):
        self.assertEquals(self.calculate(16626, 1996911439), 552386734)

    def test0715(self):
        self.assertEquals(self.calculate(10295, 1478403582), -1199220334)

    def test0716(self):
        self.assertEquals(self.calculate(-30141, 1311849855), -997552579)

    def test0717(self):
        self.assertEquals(self.calculate(28603, 1180847801), 166836259)

    def test0718(self):
        self.assertEquals(self.calculate(-32325, 1631485287), 141525309)

    def test0719(self):
        self.assertEquals(self.calculate(-28421, -400545922), -2042652534)

    def test0720(self):
        self.assertEquals(self.calculate(30997, 2076431844), -1222029388)

    def test0721(self):
        self.assertEquals(self.calculate(-20350, -686747119), -519709534)

    def test0722(self):
        self.assertEquals(self.calculate(28050, -229836216), -159947504)

    def test0723(self):
        self.assertEquals(self.calculate(-4550, -33665785), -1439500906)

    def test0724(self):
        self.assertEquals(self.calculate(15303, 1398852405), 521350451)

    def test0725(self):
        self.assertEquals(self.calculate(14054, 1495362290), 546644332)

    def test0726(self):
        self.assertEquals(self.calculate(10993, -423619163), -1100909995)

    def test0727(self):
        self.assertEquals(self.calculate(29637, 1209777963), -197497577)

    def test0728(self):
        self.assertEquals(self.calculate(-32687, 1995656476), -59939364)

    def test0729(self):
        self.assertEquals(self.calculate(3794, -238881830), -79563564)

    def test0730(self):
        self.assertEquals(self.calculate(6200, 511661641), -1678657544)

    def test0731(self):
        self.assertEquals(self.calculate(-20608, 1004938417), 561403776)

    def test0732(self):
        self.assertEquals(self.calculate(-6895, 1146935572), -1085977004)

    def test0733(self):
        self.assertEquals(self.calculate(26735, 627789223), -787315863)

    def test0734(self):
        self.assertEquals(self.calculate(-30104, 1355323677), 1525339592)

    def test0735(self):
        self.assertEquals(self.calculate(-9659, 379538860), 1936222044)

    def test0736(self):
        self.assertEquals(self.calculate(29469, -874387683), -1821821623)

    def test0737(self):
        self.assertEquals(self.calculate(3544, 239469338), -1724190736)

    def test0738(self):
        self.assertEquals(self.calculate(-6905, 601854236), 1724842948)

    def test0739(self):
        self.assertEquals(self.calculate(2860, 1406148820), 1496236144)

    def test0740(self):
        self.assertEquals(self.calculate(-24028, 1995885660), 464188656)

    def test0741(self):
        self.assertEquals(self.calculate(29619, -1012018214), -390721682)

    def test0742(self):
        self.assertEquals(self.calculate(-30586, 1196938241), 748191878)

    def test0743(self):
        self.assertEquals(self.calculate(-3968, -833878710), 1705903360)

    def test0744(self):
        self.assertEquals(self.calculate(-1816, 19464852), -988432864)

    def test0745(self):
        self.assertEquals(self.calculate(25952, -1807355236), 854754944)

    def test0746(self):
        self.assertEquals(self.calculate(2889, 584423308), 476789484)

    def test0747(self):
        self.assertEquals(self.calculate(-17761, 1323616893), 1891341731)

    def test0748(self):
        self.assertEquals(self.calculate(-25241, -431352295), 21182735)

    def test0749(self):
        self.assertEquals(self.calculate(29770, 709912455), -1440278266)

    def test0750(self):
        self.assertEquals(self.calculate(-30654, 541385170), 132630564)

    def test0751(self):
        self.assertEquals(self.calculate(-9557, -415527809), -1645478187)

    def test0752(self):
        self.assertEquals(self.calculate(-8981, -1118479241), -866441923)

    def test0753(self):
        self.assertEquals(self.calculate(27087, 1527591819), 164671589)

    def test0754(self):
        self.assertEquals(self.calculate(26032, -360196782), -729021856)

    def test0755(self):
        self.assertEquals(self.calculate(-16411, -415081213), 79655087)

    def test0756(self):
        self.assertEquals(self.calculate(7817, -1525589674), 1589699334)

    def test0757(self):
        self.assertEquals(self.calculate(25620, 1348687767), 368694220)

    def test0758(self):
        self.assertEquals(self.calculate(19008, 1158748640), 901855232)

    def test0759(self):
        self.assertEquals(self.calculate(1301, 794817549), -1029487087)

    def test0760(self):
        self.assertEquals(self.calculate(13050, 874951983), 2100305382)

    def test0761(self):
        self.assertEquals(self.calculate(-18092, 832154936), -1486729632)

    def test0762(self):
        self.assertEquals(self.calculate(15944, -2070450492), -144007392)

    def test0763(self):
        self.assertEquals(self.calculate(-26115, 701810529), -1156512803)

    def test0764(self):
        self.assertEquals(self.calculate(25904, 1350428925), -997752720)

    def test0765(self):
        self.assertEquals(self.calculate(-18224, 176249796), 659255104)

    def test0766(self):
        self.assertEquals(self.calculate(-248, 1349920755), 227101848)

    def test0767(self):
        self.assertEquals(self.calculate(-22877, -738827041), 1449907197)

    def test0768(self):
        self.assertEquals(self.calculate(-3006, -884771028), 1036953944)

    def test0769(self):
        self.assertEquals(self.calculate(27188, 850911750), 1894802744)

    def test0770(self):
        self.assertEquals(self.calculate(-24804, -383845794), -1031420856)

    def test0771(self):
        self.assertEquals(self.calculate(22135, 672803440), 1852529168)

    def test0772(self):
        self.assertEquals(self.calculate(-26605, -925247838), 1761156614)

    def test0773(self):
        self.assertEquals(self.calculate(-4331, 1227920750), -955255802)

    def test0774(self):
        self.assertEquals(self.calculate(-8480, -1886149341), 88201376)

    def test0775(self):
        self.assertEquals(self.calculate(22795, 1645430250), -366847218)

    def test0776(self):
        self.assertEquals(self.calculate(14179, 1444273424), -51188432)

    def test0777(self):
        self.assertEquals(self.calculate(3135, -755689223), 1736233287)

    def test0778(self):
        self.assertEquals(self.calculate(-28240, -489201480), -1859996032)

    def test0779(self):
        self.assertEquals(self.calculate(26176, -1162109963), 1862966080)

    def test0780(self):
        self.assertEquals(self.calculate(-20186, 82978125), 40814190)

    def test0781(self):
        self.assertEquals(self.calculate(-26239, 238074572), -1956246324)

    def test0782(self):
        self.assertEquals(self.calculate(7551, 1164312448), -74760064)

    def test0783(self):
        self.assertEquals(self.calculate(19072, -715036342), -651949824)

    def test0784(self):
        self.assertEquals(self.calculate(29749, -1332984630), 473286098)

    def test0785(self):
        self.assertEquals(self.calculate(-9680, -1384748828), -224275776)

    def test0786(self):
        self.assertEquals(self.calculate(-8355, 1371122681), -1052221323)

    def test0787(self):
        self.assertEquals(self.calculate(32553, 1941590511), -142823353)

    def test0788(self):
        self.assertEquals(self.calculate(30428, -2038632802), 693756872)

    def test0789(self):
        self.assertEquals(self.calculate(-16739, 1965362892), 1240038172)

    def test0790(self):
        self.assertEquals(self.calculate(22232, -1851885289), 442754408)

    def test0791(self):
        self.assertEquals(self.calculate(-30346, 295656567), 192499162)

    def test0792(self):
        self.assertEquals(self.calculate(-29153, 1087520300), 969273172)

    def test0793(self):
        self.assertEquals(self.calculate(28142, -1259821379), 1061780662)

    def test0794(self):
        self.assertEquals(self.calculate(22390, 692218313), -1768943194)

    def test0795(self):
        self.assertEquals(self.calculate(-6952, 2136607810), -1700585552)

    def test0796(self):
        self.assertEquals(self.calculate(-9823, 1597496191), 1605415391)

    def test0797(self):
        self.assertEquals(self.calculate(-24962, -2126104040), -1101830192)

    def test0798(self):
        self.assertEquals(self.calculate(-13107, -1459076167), -1378048219)

    def test0799(self):
        self.assertEquals(self.calculate(29890, -387145151), -1126667966)

    def test0800(self):
        self.assertEquals(self.calculate(12652, 386425709), 1385287420)

    def test0801(self):
        self.assertEquals(self.calculate(7723, 847991296), -788347392)

    def test0802(self):
        self.assertEquals(self.calculate(-9621, -1696728297), -947746659)

    def test0803(self):
        self.assertEquals(self.calculate(23111, 614440339), 1168794053)

    def test0804(self):
        self.assertEquals(self.calculate(4707, -221308419), 1978324695)

    def test0805(self):
        self.assertEquals(self.calculate(-24064, -1990001258), -1495077888)

    def test0806(self):
        self.assertEquals(self.calculate(-10662, -682548040), 1652603056)

    def test0807(self):
        self.assertEquals(self.calculate(-28048, 438974755), 1307309392)

    def test0808(self):
        self.assertEquals(self.calculate(-11380, 563308590), 1934418728)

    def test0809(self):
        self.assertEquals(self.calculate(-22022, -1532369453), 282049294)

    def test0810(self):
        self.assertEquals(self.calculate(-28628, 1624578108), 1778772560)

    def test0811(self):
        self.assertEquals(self.calculate(-30624, 1208840575), -1210644576)

    def test0812(self):
        self.assertEquals(self.calculate(9344, -199530498), -397166848)

    def test0813(self):
        self.assertEquals(self.calculate(-7787, 1764139651), -2050049729)

    def test0814(self):
        self.assertEquals(self.calculate(-31346, 1519959367), -574103454)

    def test0815(self):
        self.assertEquals(self.calculate(-9952, 1596391510), -204279616)

    def test0816(self):
        self.assertEquals(self.calculate(6558, -1067311063), 1370741326)

    def test0817(self):
        self.assertEquals(self.calculate(21984, 1284795545), 1240322784)

    def test0818(self):
        self.assertEquals(self.calculate(310, 777211557), 417414094)

    def test0819(self):
        self.assertEquals(self.calculate(24858, -674171798), 399834308)

    def test0820(self):
        self.assertEquals(self.calculate(18682, -1647108119), -2128170614)

    def test0821(self):
        self.assertEquals(self.calculate(-5911, 899770886), -1376194698)

    def test0822(self):
        self.assertEquals(self.calculate(29132, -1064712310), 1054796792)

    def test0823(self):
        self.assertEquals(self.calculate(29331, 1084281988), -1157836852)

    def test0824(self):
        self.assertEquals(self.calculate(17077, 983527661), -1915227759)

    def test0825(self):
        self.assertEquals(self.calculate(-23593, 675418035), -809031595)

    def test0826(self):
        self.assertEquals(self.calculate(20252, 1351698096), -1531704512)

    def test0827(self):
        self.assertEquals(self.calculate(12095, 1352356485), 1516222907)

    def test0828(self):
        self.assertEquals(self.calculate(22678, 1508669461), -103443378)

    def test0829(self):
        self.assertEquals(self.calculate(27829, -1196695446), 338846450)

    def test0830(self):
        self.assertEquals(self.calculate(-1270, 1272783537), -1527388694)

    def test0831(self):
        self.assertEquals(self.calculate(-9841, -226150648), 755467640)

    def test0832(self):
        self.assertEquals(self.calculate(28521, -2040228681), -1145284593)

    def test0833(self):
        self.assertEquals(self.calculate(-24224, 1418396716), 496319616)

    def test0834(self):
        self.assertEquals(self.calculate(-22576, 1819648478), 978146912)

    def test0835(self):
        self.assertEquals(self.calculate(30051, 1083004820), -1884323268)

    def test0836(self):
        self.assertEquals(self.calculate(13594, 1352470849), -1266272870)

    def test0837(self):
        self.assertEquals(self.calculate(6729, -286906995), 2138113845)

    def test0838(self):
        self.assertEquals(self.calculate(-27585, 1972221149), 630343267)

    def test0839(self):
        self.assertEquals(self.calculate(11916, 1083665739), -2005713148)

    def test0840(self):
        self.assertEquals(self.calculate(7015, 2017418688), 274856000)

    def test0841(self):
        self.assertEquals(self.calculate(32679, -1029394795), -1408643533)

    def test0842(self):
        self.assertEquals(self.calculate(30783, 832666985), -377023273)

    def test0843(self):
        self.assertEquals(self.calculate(1407, 542052761), -1835943961)

    def test0844(self):
        self.assertEquals(self.calculate(-29974, 427529895), 1401338534)

    def test0845(self):
        self.assertEquals(self.calculate(20984, -301250886), 743267888)

    def test0846(self):
        self.assertEquals(self.calculate(-4062, -1412374402), -1011486532)

    def test0847(self):
        self.assertEquals(self.calculate(23084, 1840474108), -312182960)

    def test0848(self):
        self.assertEquals(self.calculate(-31143, -1013471852), -1160771468)

    def test0849(self):
        self.assertEquals(self.calculate(25838, -1290288171), -929610746)

    def test0850(self):
        self.assertEquals(self.calculate(12201, 1136828114), 1990420130)

    def test0851(self):
        self.assertEquals(self.calculate(15071, -1531272999), -956086521)

    def test0852(self):
        self.assertEquals(self.calculate(-14791, -1168249949), 931563851)

    def test0853(self):
        self.assertEquals(self.calculate(-30942, -709640718), 1830279204)

    def test0854(self):
        self.assertEquals(self.calculate(-19272, -60603432), -281763008)

    def test0855(self):
        self.assertEquals(self.calculate(32283, 237685674), -1899944210)

    def test0856(self):
        self.assertEquals(self.calculate(-30793, -1393125716), 386820340)

    def test0857(self):
        self.assertEquals(self.calculate(16518, 351065156), 688397208)

    def test0858(self):
        self.assertEquals(self.calculate(-27131, -1160287616), 1947997312)

    def test0859(self):
        self.assertEquals(self.calculate(-9334, 1790264187), 1391827278)

    def test0860(self):
        self.assertEquals(self.calculate(-21773, -1892755837), 761633881)

    def test0861(self):
        self.assertEquals(self.calculate(59, -235158806), -989467666)

    def test0862(self):
        self.assertEquals(self.calculate(-2427, 201922805), -440375991)

    def test0863(self):
        self.assertEquals(self.calculate(-7702, 780232612), -692330520)

    def test0864(self):
        self.assertEquals(self.calculate(-2186, -812000667), 1211964814)

    def test0865(self):
        self.assertEquals(self.calculate(14100, -63243729), 1616618668)

    def test0866(self):
        self.assertEquals(self.calculate(-10871, -2110564609), 232569207)

    def test0867(self):
        self.assertEquals(self.calculate(-18206, -711864313), -2009616850)

    def test0868(self):
        self.assertEquals(self.calculate(-14151, -38884046), 492321058)

    def test0869(self):
        self.assertEquals(self.calculate(3195, 865772625), 184598251)

    def test0870(self):
        self.assertEquals(self.calculate(-30581, 1940185585), -2137147941)

    def test0871(self):
        self.assertEquals(self.calculate(-9338, -2009512867), 119035822)

    def test0872(self):
        self.assertEquals(self.calculate(5027, 1490512049), -1913861197)

    def test0873(self):
        self.assertEquals(self.calculate(-1221, -1432792718), 1388219206)

    def test0874(self):
        self.assertEquals(self.calculate(-31596, 398051673), -1176417420)

    def test0875(self):
        self.assertEquals(self.calculate(8913, -1480665010), 1267266478)

    def test0876(self):
        self.assertEquals(self.calculate(-4202, -690756226), -840230444)

    def test0877(self):
        self.assertEquals(self.calculate(8237, 1858556071), 1662913883)

    def test0878(self):
        self.assertEquals(self.calculate(-1547, 810521321), 253966845)

    def test0879(self):
        self.assertEquals(self.calculate(9706, 1512343016), -1396904432)

    def test0880(self):
        self.assertEquals(self.calculate(11674, 2107729049), -238720758)

    def test0881(self):
        self.assertEquals(self.calculate(-27843, -1517824113), -1701414381)

    def test0882(self):
        self.assertEquals(self.calculate(-16481, -1315637856), 2032594528)

    def test0883(self):
        self.assertEquals(self.calculate(-18107, -849838142), -848584374)

    def test0884(self):
        self.assertEquals(self.calculate(-11767, 1921325258), 473535258)

    def test0885(self):
        self.assertEquals(self.calculate(-27378, -417800662), 1048614988)

    def test0886(self):
        self.assertEquals(self.calculate(7114, -807942177), -1034405130)

    def test0887(self):
        self.assertEquals(self.calculate(11668, -186287627), -350580060)

    def test0888(self):
        self.assertEquals(self.calculate(-10159, -2001334710), -815860374)

    def test0889(self):
        self.assertEquals(self.calculate(6797, -79139037), -1037122489)

    def test0890(self):
        self.assertEquals(self.calculate(23830, 1376575508), -1165851208)

    def test0891(self):
        self.assertEquals(self.calculate(21013, 1020139351), 6408227)

    def test0892(self):
        self.assertEquals(self.calculate(29879, -802449623), -1884839345)

    def test0893(self):
        self.assertEquals(self.calculate(13495, 1264213288), 948221848)

    def test0894(self):
        self.assertEquals(self.calculate(-32130, -1928132884), 301285416)

    def test0895(self):
        self.assertEquals(self.calculate(8534, -1641192156), -45507048)

    def test0896(self):
        self.assertEquals(self.calculate(14539, 1400711236), -1794257428)

    def test0897(self):
        self.assertEquals(self.calculate(-32648, 728708242), -1042832272)

    def test0898(self):
        self.assertEquals(self.calculate(-17504, 158453659), 976026080)

    def test0899(self):
        self.assertEquals(self.calculate(30661, -1966827759), 729884437)

    def test0900(self):
        self.assertEquals(self.calculate(19653, -1136171360), 359233824)

    def test0901(self):
        self.assertEquals(self.calculate(-15584, -6976631), 1349635104)

    def test0902(self):
        self.assertEquals(self.calculate(18253, -1615684478), -1843322598)

    def test0903(self):
        self.assertEquals(self.calculate(-32220, -1656814724), 421885296)

    def test0904(self):
        self.assertEquals(self.calculate(-27003, -115360696), 1233584488)

    def test0905(self):
        self.assertEquals(self.calculate(12923, 267371671), 2090398349)

    def test0906(self):
        self.assertEquals(self.calculate(-18650, 1350962581), -1173977314)

    def test0907(self):
        self.assertEquals(self.calculate(9909, 292716925), 1429085025)

    def test0908(self):
        self.assertEquals(self.calculate(29765, 534424906), -1401537294)

    def test0909(self):
        self.assertEquals(self.calculate(841, -1027718617), -1022930401)

    def test0910(self):
        self.assertEquals(self.calculate(27466, 1435078993), 964746346)

    def test0911(self):
        self.assertEquals(self.calculate(21128, 2050680422), -854126032)

    def test0912(self):
        self.assertEquals(self.calculate(28948, 59972758), 924611000)

    def test0913(self):
        self.assertEquals(self.calculate(8739, -1835498378), 1282525218)

    def test0914(self):
        self.assertEquals(self.calculate(-8999, -816935526), -1381212278)

    def test0915(self):
        self.assertEquals(self.calculate(6007, 1693415636), 1865168524)

    def test0916(self):
        self.assertEquals(self.calculate(-31744, -263574205), 303270912)

    def test0917(self):
        self.assertEquals(self.calculate(-11623, 1074715661), -1655231035)

    def test0918(self):
        self.assertEquals(self.calculate(1755, 1117623240), -1371268072)

    def test0919(self):
        self.assertEquals(self.calculate(17517, 1599831537), -412572771)

    def test0920(self):
        self.assertEquals(self.calculate(-7455, -1770365574), -359146438)

    def test0921(self):
        self.assertEquals(self.calculate(-20153, -1462624365), -91724603)

    def test0922(self):
        self.assertEquals(self.calculate(3681, 310623810), 944943874)

    def test0923(self):
        self.assertEquals(self.calculate(-28466, 805616250), -1841779156)

    def test0924(self):
        self.assertEquals(self.calculate(30537, 44463177), 562370513)

    def test0925(self):
        self.assertEquals(self.calculate(-31344, -1870721653), 1005966640)

    def test0926(self):
        self.assertEquals(self.calculate(27208, -133901809), -1068152264)

    def test0927(self):
        self.assertEquals(self.calculate(25650, -1643050543), -2027319598)

    def test0928(self):
        self.assertEquals(self.calculate(-26542, -466176228), -551336200)

    def test0929(self):
        self.assertEquals(self.calculate(30383, -393805497), 786471305)

    def test0930(self):
        self.assertEquals(self.calculate(3850, 608484532), 1908271880)

    def test0931(self):
        self.assertEquals(self.calculate(-15460, -894417417), -2101426300)

    def test0932(self):
        self.assertEquals(self.calculate(10215, 478041132), -187652172)

    def test0933(self):
        self.assertEquals(self.calculate(6595, -762707324), -648098164)

    def test0934(self):
        self.assertEquals(self.calculate(143, -743754204), 1017331228)

    def test0935(self):
        self.assertEquals(self.calculate(-24403, -557524110), -1195537398)

    def test0936(self):
        self.assertEquals(self.calculate(-21815, 2109632785), -1064628135)

    def test0937(self):
        self.assertEquals(self.calculate(9632, 617044085), -866110944)

    def test0938(self):
        self.assertEquals(self.calculate(22901, -1217103070), 1460344970)

    def test0939(self):
        self.assertEquals(self.calculate(15836, 575240091), -123553740)

    def test0940(self):
        self.assertEquals(self.calculate(-14542, -84826070), 885095988)

    def test0941(self):
        self.assertEquals(self.calculate(-913, 1612900292), 595815932)

    def test0942(self):
        self.assertEquals(self.calculate(-15125, 835550151), -1902249043)

    def test0943(self):
        self.assertEquals(self.calculate(31498, -1542037483), 688510930)

    def test0944(self):
        self.assertEquals(self.calculate(20993, 1174393338), 927065594)

    def test0945(self):
        self.assertEquals(self.calculate(11034, -1269416235), -850384734)

    def test0946(self):
        self.assertEquals(self.calculate(-7186, 630308480), 1793760000)

    def test0947(self):
        self.assertEquals(self.calculate(22583, -993969743), -1319617273)

    def test0948(self):
        self.assertEquals(self.calculate(-1811, 1865446227), 1816144855)

    def test0949(self):
        self.assertEquals(self.calculate(-15220, 1236699826), -2024660648)

    def test0950(self):
        self.assertEquals(self.calculate(22813, -1298813681), 1142870451)

    def test0951(self):
        self.assertEquals(self.calculate(-23154, -1956866637), 1680107594)

    def test0952(self):
        self.assertEquals(self.calculate(14442, -1575565237), 423581454)

    def test0953(self):
        self.assertEquals(self.calculate(-14746, -2112033344), 1235827328)

    def test0954(self):
        self.assertEquals(self.calculate(16056, 1715122133), -1329334504)

    def test0955(self):
        self.assertEquals(self.calculate(11443, -55735367), -2124644773)

    def test0956(self):
        self.assertEquals(self.calculate(10380, 32223681), -525640308)

    def test0957(self):
        self.assertEquals(self.calculate(-7873, -518758840), -325551176)

    def test0958(self):
        self.assertEquals(self.calculate(-14032, -336537389), 2123584144)

    def test0959(self):
        self.assertEquals(self.calculate(-28618, -1432638117), -520175310)

    def test0960(self):
        self.assertEquals(self.calculate(-32721, 667467699), -301878819)

    def test0961(self):
        self.assertEquals(self.calculate(-30477, 1963179544), 1366438088)

    def test0962(self):
        self.assertEquals(self.calculate(17113, 25045787), -888176669)

    def test0963(self):
        self.assertEquals(self.calculate(-18229, -624423916), 960230364)

    def test0964(self):
        self.assertEquals(self.calculate(-22704, 413409668), -1549560512)

    def test0965(self):
        self.assertEquals(self.calculate(-13019, -1817748722), 810758)

    def test0966(self):
        self.assertEquals(self.calculate(-17748, -419740135), 2074624716)

    def test0967(self):
        self.assertEquals(self.calculate(27403, -2009464772), 412554900)

    def test0968(self):
        self.assertEquals(self.calculate(-23941, -1875570119), -858860701)

    def test0969(self):
        self.assertEquals(self.calculate(22871, 83485841), -1855777209)

    def test0970(self):
        self.assertEquals(self.calculate(21658, -1185419396), 1501216920)

    def test0971(self):
        self.assertEquals(self.calculate(-5994, -1212760565), -2092805518)

    def test0972(self):
        self.assertEquals(self.calculate(32194, -2045688838), 122066292)

    def test0973(self):
        self.assertEquals(self.calculate(6465, 149271932), -1324601220)

    def test0974(self):
        self.assertEquals(self.calculate(-16256, -473331511), -2104351616)

    def test0975(self):
        self.assertEquals(self.calculate(26979, -649840475), 10327247)

    def test0976(self):
        self.assertEquals(self.calculate(-13231, -1264141793), 1257412559)

    def test0977(self):
        self.assertEquals(self.calculate(-20400, -900244127), -299966896)

    def test0978(self):
        self.assertEquals(self.calculate(13408, 2120273560), 239360256)

    def test0979(self):
        self.assertEquals(self.calculate(-1435, 147601358), -1354551226)

    def test0980(self):
        self.assertEquals(self.calculate(4013, -9981229), -1399966313)

    def test0981(self):
        self.assertEquals(self.calculate(-4401, -348696445), 1309729773)

    def test0982(self):
        self.assertEquals(self.calculate(-13776, -903575906), 846457248)

    def test0983(self):
        self.assertEquals(self.calculate(27347, -584518039), 1053463179)

    def test0984(self):
        self.assertEquals(self.calculate(31139, -114331290), 365849074)

    def test0985(self):
        self.assertEquals(self.calculate(27733, -715932762), 670520862)

    def test0986(self):
        self.assertEquals(self.calculate(25616, -764431916), -932057792)

    def test0987(self):
        self.assertEquals(self.calculate(-6941, -591466297), -621167499)

    def test0988(self):
        self.assertEquals(self.calculate(5546, 1556466772), -719547448)

    def test0989(self):
        self.assertEquals(self.calculate(4543, 469528166), -1532287974)

    def test0990(self):
        self.assertEquals(self.calculate(-26255, -1635769134), 1740620466)

    def test0991(self):
        self.assertEquals(self.calculate(-679, 831113569), -1685397575)

    def test0992(self):
        self.assertEquals(self.calculate(-29120, 1347395819), -1640000320)

    def test0993(self):
        self.assertEquals(self.calculate(-15919, 1358846931), -2028991933)

    def test0994(self):
        self.assertEquals(self.calculate(-3255, 35461779), 536026347)

    def test0995(self):
        self.assertEquals(self.calculate(24085, 1078770893), 1939784401)

    def test0996(self):
        self.assertEquals(self.calculate(13640, 2140090624), -2056599552)

    def test0997(self):
        self.assertEquals(self.calculate(26044, 1611488183), -822178460)

    def test0998(self):
        self.assertEquals(self.calculate(18969, -1286616794), -1829789514)

    def test0999(self):
        self.assertEquals(self.calculate(-15130, 1195950570), -34906052)

    def test1000(self):
        self.assertEquals(self.calculate(14776, 1704693044), -1438772896)

    def test1001(self):
        self.assertEquals(self.calculate(-11230, -147981472), -320412992)

    def test1002(self):
        self.assertEquals(self.calculate(10329, 1631409704), 1674130408)

    def test1003(self):
        self.assertEquals(self.calculate(-13486, -2093512127), -2010459182)

    def test1004(self):
        self.assertEquals(self.calculate(-1124, -911943153), -1473079772)

    def test1005(self):
        self.assertEquals(self.calculate(-23493, -1901540974), 947256486)

    def test1006(self):
        self.assertEquals(self.calculate(-22290, -1618576353), 341621970)

    def test1007(self):
        self.assertEquals(self.calculate(-32129, 110981383), -897998727)

    def test1008(self):
        self.assertEquals(self.calculate(30903, -1054099203), -1795697445)

    def test1009(self):
        self.assertEquals(self.calculate(11212, -1345800697), -897303916)

    def test1010(self):
        self.assertEquals(self.calculate(26740, 1783991384), -272148512)

    def test1011(self):
        self.assertEquals(self.calculate(-32675, -1083730728), -1103818120)

    def test1012(self):
        self.assertEquals(self.calculate(21256, 236200040), -148718784)

    def test1013(self):
        self.assertEquals(self.calculate(31636, -1779193045), -1004757540)

    def test1014(self):
        self.assertEquals(self.calculate(11299, 1437084322), -1655591898)

    def test1015(self):
        self.assertEquals(self.calculate(2207, -477337002), -1215775894)

    def test1016(self):
        self.assertEquals(self.calculate(-26273, 633504109), -1055183757)

    def test1017(self):
        self.assertEquals(self.calculate(21015, 749843002), -284321994)

    def test1018(self):
        self.assertEquals(self.calculate(-27919, -1477599216), -68366576)

    def test1019(self):
        self.assertEquals(self.calculate(-18949, 1783140581), -223151737)

    def test1020(self):
        self.assertEquals(self.calculate(29467, 186275328), 6885888)

    def test1021(self):
        self.assertEquals(self.calculate(-6896, -774965891), 1225468112)

    def test1022(self):
        self.assertEquals(self.calculate(-14358, -65848745), 563475590)

    def test1023(self):
        self.assertEquals(self.calculate(21383, -206774782), -1943815922)


class TestVM_Mul_IntFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushF(rhs)
        v.VM_Mul()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(4001, 7862.0), 31455862.00, "")

    def test0001(self):
        self.assertEquals(self.calculate(-27363, -49660.0), 1358846580.00, "")

    def test0002(self):
        self.assertEquals(self.calculate(-28018, -159495.0), 4468730910.00, "")

    def test0003(self):
        self.assertEquals(self.calculate(27427, -3719.0), -102001013.00, "")

    def test0004(self):
        self.assertEquals(self.calculate(31656, 166359.0), 5266260504.00, "")

    def test0005(self):
        self.assertEquals(self.calculate(5000, -173045.0), -865225000.00, "")

    def test0006(self):
        self.assertEquals(self.calculate(120, -113483.0), -13617960.00, "")

    def test0007(self):
        self.assertEquals(self.calculate(5470, 142161.0), 777620670.00, "")

    def test0008(self):
        self.assertEquals(self.calculate(-15921, -150547.0), 2396858787.00, "")

    def test0009(self):
        self.assertEquals(self.calculate(-19290, 151503.0), -2922492870.00, "")

    def test0010(self):
        self.assertEquals(self.calculate(-32625, -197522.0), 6444155250.00, "")

    def test0011(self):
        self.assertEquals(self.calculate(-29651, -129702.0), 3845794002.00, "")

    def test0012(self):
        self.assertEquals(self.calculate(18239, 64333.0), 1173369587.00, "")

    def test0013(self):
        self.assertEquals(self.calculate(29698, -40279.0), -1196205742.00, "")

    def test0014(self):
        self.assertEquals(self.calculate(-6374, -126018.0), 803238732.00, "")

    def test0015(self):
        self.assertEquals(self.calculate(9362, -46360.0), -434022320.00, "")

    def test0016(self):
        self.assertEquals(self.calculate(-27827, -186103.0), 5178688181.00, "")

    def test0017(self):
        self.assertEquals(self.calculate(-4690, 149972.0), -703368680.00, "")

    def test0018(self):
        self.assertEquals(self.calculate(2569, -129556.0), -332829364.00, "")

    def test0019(self):
        self.assertEquals(self.calculate(7997, -66345.0), -530560965.00, "")

    def test0020(self):
        self.assertEquals(self.calculate(-2721, 156325.0), -425360325.00, "")

    def test0021(self):
        self.assertEquals(self.calculate(22699, 16989.0), 385633311.00, "")

    def test0022(self):
        self.assertEquals(self.calculate(10812, -35844.0), -387545328.00, "")

    def test0023(self):
        self.assertEquals(self.calculate(-15992, 57182.0), -914454544.00, "")

    def test0024(self):
        self.assertEquals(self.calculate(-4055, 2218.0), -8993990.00, "")

    def test0025(self):
        self.assertEquals(self.calculate(17111, -121459.0), -2078284949.00, "")

    def test0026(self):
        self.assertEquals(self.calculate(25213, 130742.0), 3296398046.00, "")

    def test0027(self):
        self.assertEquals(self.calculate(-12089, 108559.0), -1312369751.00, "")

    def test0028(self):
        self.assertEquals(self.calculate(-23894, -148517.0), 3548665198.00, "")

    def test0029(self):
        self.assertEquals(self.calculate(6175, 176560.0), 1090258000.00, "")

    def test0030(self):
        self.assertEquals(self.calculate(-27870, -71451.0), 1991339370.00, "")

    def test0031(self):
        self.assertEquals(self.calculate(21156, -69357.0), -1467316692.00, "")

    def test0032(self):
        self.assertEquals(self.calculate(6494, -156891.0), -1018850154.00, "")

    def test0033(self):
        self.assertEquals(self.calculate(32586, 54931.0), 1789981566.00, "")

    def test0034(self):
        self.assertEquals(self.calculate(29641, 33140.0), 982302740.00, "")

    def test0035(self):
        self.assertEquals(self.calculate(11693, -94242.0), -1101971706.00, "")

    def test0036(self):
        self.assertEquals(self.calculate(14093, 184313.0), 2597523109.00, "")

    def test0037(self):
        self.assertEquals(self.calculate(-19436, 48062.0), -934133032.00, "")

    def test0038(self):
        self.assertEquals(self.calculate(-6349, 52567.0), -333747883.00, "")

    def test0039(self):
        self.assertEquals(self.calculate(-15883, -125286.0), 1989917538.00, "")

    def test0040(self):
        self.assertEquals(self.calculate(-15412, 161854.0), -2494493848.00, "")

    def test0041(self):
        self.assertEquals(self.calculate(-14155, 173810.0), -2460280550.00, "")

    def test0042(self):
        self.assertEquals(self.calculate(-15224, -199424.0), 3036030976.00, "")

    def test0043(self):
        self.assertEquals(self.calculate(31671, -1815.0), -57482865.00, "")

    def test0044(self):
        self.assertEquals(self.calculate(-22063, 77871.0), -1718067873.00, "")

    def test0045(self):
        self.assertEquals(self.calculate(31049, 164683.0), 5113242467.00, "")

    def test0046(self):
        self.assertEquals(self.calculate(-15257, -147657.0), 2252802849.00, "")

    def test0047(self):
        self.assertEquals(self.calculate(3450, -187436.0), -646654200.00, "")

    def test0048(self):
        self.assertEquals(self.calculate(10318, 128551.0), 1326389218.00, "")

    def test0049(self):
        self.assertEquals(self.calculate(-28832, 10868.0), -313346176.00, "")

    def test0050(self):
        self.assertEquals(self.calculate(29442, 51631.0), 1520119902.00, "")

    def test0051(self):
        self.assertEquals(self.calculate(-16299, -159076.0), 2592779724.00, "")

    def test0052(self):
        self.assertEquals(self.calculate(9020, 81728.0), 737186560.00, "")

    def test0053(self):
        self.assertEquals(self.calculate(-14761, -130328.0), 1923771608.00, "")

    def test0054(self):
        self.assertEquals(self.calculate(23075, 86225.0), 1989641875.00, "")

    def test0055(self):
        self.assertEquals(self.calculate(7184, -182462.0), -1310807008.00, "")

    def test0056(self):
        self.assertEquals(self.calculate(25938, -58806.0), -1525310028.00, "")

    def test0057(self):
        self.assertEquals(self.calculate(-12318, -137919.0), 1698886242.00, "")

    def test0058(self):
        self.assertEquals(self.calculate(-32252, 92957.0), -2998049164.00, "")

    def test0059(self):
        self.assertEquals(self.calculate(-30414, -126713.0), 3853849182.00, "")

    def test0060(self):
        self.assertEquals(self.calculate(-12836, -113689.0), 1459312004.00, "")

    def test0061(self):
        self.assertEquals(self.calculate(24013, 117234.0), 2815140042.00, "")

    def test0062(self):
        self.assertEquals(self.calculate(29118, 32204.0), 937716072.00, "")

    def test0063(self):
        self.assertEquals(self.calculate(-14720, -60119.0), 884951680.00, "")

    def test0064(self):
        self.assertEquals(self.calculate(-26807, 3457.0), -92671799.00, "")

    def test0065(self):
        self.assertEquals(self.calculate(14235, -1977.0), -28142595.00, "")

    def test0066(self):
        self.assertEquals(self.calculate(10664, 151020.0), 1610477280.00, "")

    def test0067(self):
        self.assertEquals(self.calculate(11295, -15117.0), -170746515.00, "")

    def test0068(self):
        self.assertEquals(self.calculate(-8251, 2837.0), -23408087.00, "")

    def test0069(self):
        self.assertEquals(self.calculate(-13946, 174106.0), -2428082276.00, "")

    def test0070(self):
        self.assertEquals(self.calculate(-16037, 123437.0), -1979559169.00, "")

    def test0071(self):
        self.assertEquals(self.calculate(-11705, -25907.0), 303241435.00, "")

    def test0072(self):
        self.assertEquals(self.calculate(-363, 35206.0), -12779778.00, "")

    def test0073(self):
        self.assertEquals(self.calculate(8448, 4422.0), 37357056.00, "")

    def test0074(self):
        self.assertEquals(self.calculate(-5014, 117455.0), -588919370.00, "")

    def test0075(self):
        self.assertEquals(self.calculate(-27579, 51417.0), -1418029443.00, "")

    def test0076(self):
        self.assertEquals(self.calculate(-25579, -144600.0), 3698723400.00, "")

    def test0077(self):
        self.assertEquals(self.calculate(-23012, -91133.0), 2097152596.00, "")

    def test0078(self):
        self.assertEquals(self.calculate(-16795, 18078.0), -303620010.00, "")

    def test0079(self):
        self.assertEquals(self.calculate(26750, 107687.0), 2880627250.00, "")

    def test0080(self):
        self.assertEquals(self.calculate(-13689, -33357.0), 456623973.00, "")

    def test0081(self):
        self.assertEquals(self.calculate(18625, 190062.0), 3539904750.00, "")

    def test0082(self):
        self.assertEquals(self.calculate(-2562, 185008.0), -473990496.00, "")

    def test0083(self):
        self.assertEquals(self.calculate(-23026, -81314.0), 1872336164.00, "")

    def test0084(self):
        self.assertEquals(self.calculate(-1747, 169296.0), -295760112.00, "")

    def test0085(self):
        self.assertEquals(self.calculate(-26685, -104767.0), 2795707395.00, "")

    def test0086(self):
        self.assertEquals(self.calculate(-2489, 139257.0), -346610673.00, "")

    def test0087(self):
        self.assertEquals(self.calculate(-13144, -47857.0), 629032408.00, "")

    def test0088(self):
        self.assertEquals(self.calculate(-9674, -181321.0), 1754099354.00, "")

    def test0089(self):
        self.assertEquals(self.calculate(29461, -120629.0), -3553850969.00, "")

    def test0090(self):
        self.assertEquals(self.calculate(2600, -125860.0), -327236000.00, "")

    def test0091(self):
        self.assertEquals(self.calculate(-13691, -185213.0), 2535751183.00, "")

    def test0092(self):
        self.assertEquals(self.calculate(-21989, 141475.0), -3110893775.00, "")

    def test0093(self):
        self.assertEquals(self.calculate(-121, -129927.0), 15721167.00, "")

    def test0094(self):
        self.assertEquals(self.calculate(-7439, -46165.0), 343421435.00, "")

    def test0095(self):
        self.assertEquals(self.calculate(20004, 135664.0), 2713822656.00, "")

    def test0096(self):
        self.assertEquals(self.calculate(14866, 154948.0), 2303456968.00, "")

    def test0097(self):
        self.assertEquals(self.calculate(550, 63440.0), 34892000.00, "")

    def test0098(self):
        self.assertEquals(self.calculate(-7440, -118797.0), 883849680.00, "")

    def test0099(self):
        self.assertEquals(self.calculate(-14918, 81381.0), -1214041758.00, "")

    def test0100(self):
        self.assertEquals(self.calculate(18224, 41795.0), 761672080.00, "")

    def test0101(self):
        self.assertEquals(self.calculate(-26251, -115540.0), 3033040540.00, "")

    def test0102(self):
        self.assertEquals(self.calculate(-18370, -71477.0), 1313032490.00, "")

    def test0103(self):
        self.assertEquals(self.calculate(-25629, -33752.0), 865030008.00, "")

    def test0104(self):
        self.assertEquals(self.calculate(-22413, -23999.0), 537889587.00, "")

    def test0105(self):
        self.assertEquals(self.calculate(-16720, 5934.0), -99216480.00, "")

    def test0106(self):
        self.assertEquals(self.calculate(4208, -52633.0), -221479664.00, "")

    def test0107(self):
        self.assertEquals(self.calculate(-27575, -48121.0), 1326936575.00, "")

    def test0108(self):
        self.assertEquals(self.calculate(-3350, -48343.0), 161949050.00, "")

    def test0109(self):
        self.assertEquals(self.calculate(15454, 50043.0), 773364522.00, "")

    def test0110(self):
        self.assertEquals(self.calculate(-8930, 166960.0), -1490952800.00, "")

    def test0111(self):
        self.assertEquals(self.calculate(-26869, -127946.0), 3437781074.00, "")

    def test0112(self):
        self.assertEquals(self.calculate(-32432, 137081.0), -4445810992.00, "")

    def test0113(self):
        self.assertEquals(self.calculate(27109, 111039.0), 3010156251.00, "")

    def test0114(self):
        self.assertEquals(self.calculate(4030, -30341.0), -122274230.00, "")

    def test0115(self):
        self.assertEquals(self.calculate(-4280, -46417.0), 198664760.00, "")

    def test0116(self):
        self.assertEquals(self.calculate(-11464, -112799.0), 1293127736.00, "")

    def test0117(self):
        self.assertEquals(self.calculate(-22492, -43746.0), 983935032.00, "")

    def test0118(self):
        self.assertEquals(self.calculate(-23569, -5156.0), 121521764.00, "")

    def test0119(self):
        self.assertEquals(self.calculate(-23138, -145276.0), 3361396088.00, "")

    def test0120(self):
        self.assertEquals(self.calculate(16467, 14182.0), 233534994.00, "")

    def test0121(self):
        self.assertEquals(self.calculate(27255, -72513.0), -1976341815.00, "")

    def test0122(self):
        self.assertEquals(self.calculate(11442, -177723.0), -2033506566.00, "")

    def test0123(self):
        self.assertEquals(self.calculate(8816, 83740.0), 738251840.00, "")

    def test0124(self):
        self.assertEquals(self.calculate(18924, 144628.0), 2736940272.00, "")

    def test0125(self):
        self.assertEquals(self.calculate(20460, 149153.0), 3051670380.00, "")

    def test0126(self):
        self.assertEquals(self.calculate(-10332, -150169.0), 1551546108.00, "")

    def test0127(self):
        self.assertEquals(self.calculate(-28491, -2142.0), 61027722.00, "")

    def test0128(self):
        self.assertEquals(self.calculate(-22008, -51397.0), 1131145176.00, "")

    def test0129(self):
        self.assertEquals(self.calculate(29621, -48724.0), -1443253604.00, "")

    def test0130(self):
        self.assertEquals(self.calculate(9640, -62586.0), -603329040.00, "")

    def test0131(self):
        self.assertEquals(self.calculate(25433, 101748.0), 2587756884.00, "")

    def test0132(self):
        self.assertEquals(self.calculate(-25126, -82103.0), 2062919978.00, "")

    def test0133(self):
        self.assertEquals(self.calculate(31685, 69028.0), 2187152180.00, "")

    def test0134(self):
        self.assertEquals(self.calculate(29648, 18405.0), 545671440.00, "")

    def test0135(self):
        self.assertEquals(self.calculate(-27531, 183607.0), -5054884317.00, "")

    def test0136(self):
        self.assertEquals(self.calculate(-5631, -137986.0), 776999166.00, "")

    def test0137(self):
        self.assertEquals(self.calculate(3728, -103111.0), -384397808.00, "")

    def test0138(self):
        self.assertEquals(self.calculate(-30842, -34623.0), 1067842566.00, "")

    def test0139(self):
        self.assertEquals(self.calculate(-1332, 10310.0), -13732920.00, "")

    def test0140(self):
        self.assertEquals(self.calculate(22511, -195277.0), -4395880547.00, "")

    def test0141(self):
        self.assertEquals(self.calculate(-24735, -151478.0), 3746808330.00, "")

    def test0142(self):
        self.assertEquals(self.calculate(-25680, -188959.0), 4852467120.00, "")

    def test0143(self):
        self.assertEquals(self.calculate(-7621, -121437.0), 925471377.00, "")

    def test0144(self):
        self.assertEquals(self.calculate(-28236, 168910.0), -4769342760.00, "")

    def test0145(self):
        self.assertEquals(self.calculate(12541, -137694.0), -1726820454.00, "")

    def test0146(self):
        self.assertEquals(self.calculate(27362, 30188.0), 826004056.00, "")

    def test0147(self):
        self.assertEquals(self.calculate(22223, -191036.0), -4245393028.00, "")

    def test0148(self):
        self.assertEquals(self.calculate(27079, 80240.0), 2172818960.00, "")

    def test0149(self):
        self.assertEquals(self.calculate(18010, 89293.0), 1608166930.00, "")

    def test0150(self):
        self.assertEquals(self.calculate(2725, -139452.0), -380006700.00, "")

    def test0151(self):
        self.assertEquals(self.calculate(1510, -87666.0), -132375660.00, "")

    def test0152(self):
        self.assertEquals(self.calculate(3130, -136948.0), -428647240.00, "")

    def test0153(self):
        self.assertEquals(self.calculate(19876, -182036.0), -3618147536.00, "")

    def test0154(self):
        self.assertEquals(self.calculate(23117, -91603.0), -2117586551.00, "")

    def test0155(self):
        self.assertEquals(self.calculate(-5895, -199142.0), 1173942090.00, "")

    def test0156(self):
        self.assertEquals(self.calculate(-23228, -79741.0), 1852223948.00, "")

    def test0157(self):
        self.assertEquals(self.calculate(1715, -63824.0), -109458160.00, "")

    def test0158(self):
        self.assertEquals(self.calculate(25357, -197161.0), -4999411477.00, "")

    def test0159(self):
        self.assertEquals(self.calculate(5012, -139598.0), -699665176.00, "")

    def test0160(self):
        self.assertEquals(self.calculate(-17879, -79835.0), 1427369965.00, "")

    def test0161(self):
        self.assertEquals(self.calculate(-19840, 169726.0), -3367363840.00, "")

    def test0162(self):
        self.assertEquals(self.calculate(-14390, 159431.0), -2294212090.00, "")

    def test0163(self):
        self.assertEquals(self.calculate(21997, -27516.0), -605269452.00, "")

    def test0164(self):
        self.assertEquals(self.calculate(10391, 400.0), 4156400.00, "")

    def test0165(self):
        self.assertEquals(self.calculate(11265, -181865.0), -2048709225.00, "")

    def test0166(self):
        self.assertEquals(self.calculate(-21268, -35820.0), 761819760.00, "")

    def test0167(self):
        self.assertEquals(self.calculate(-17455, -146090.0), 2550000950.00, "")

    def test0168(self):
        self.assertEquals(self.calculate(23470, 127798.0), 2999419060.00, "")

    def test0169(self):
        self.assertEquals(self.calculate(12529, -50265.0), -629770185.00, "")

    def test0170(self):
        self.assertEquals(self.calculate(28131, 158043.0), 4445907633.00, "")

    def test0171(self):
        self.assertEquals(self.calculate(18466, -134448.0), -2482716768.00, "")

    def test0172(self):
        self.assertEquals(self.calculate(2277, 136983.0), 311910291.00, "")

    def test0173(self):
        self.assertEquals(self.calculate(-32026, 74319.0), -2380140294.00, "")

    def test0174(self):
        self.assertEquals(self.calculate(-12632, -59772.0), 755039904.00, "")

    def test0175(self):
        self.assertEquals(self.calculate(-23571, 85885.0), -2024395335.00, "")

    def test0176(self):
        self.assertEquals(self.calculate(23425, 173032.0), 4053274600.00, "")

    def test0177(self):
        self.assertEquals(self.calculate(4610, 73148.0), 337212280.00, "")

    def test0178(self):
        self.assertEquals(self.calculate(3839, 13548.0), 52010772.00, "")

    def test0179(self):
        self.assertEquals(self.calculate(-26799, 176417.0), -4727799183.00, "")

    def test0180(self):
        self.assertEquals(self.calculate(-3772, 87621.0), -330506412.00, "")

    def test0181(self):
        self.assertEquals(self.calculate(-18537, -32222.0), 597299214.00, "")

    def test0182(self):
        self.assertEquals(self.calculate(-9173, -75263.0), 690387499.00, "")

    def test0183(self):
        self.assertEquals(self.calculate(-9693, 131505.0), -1274677965.00, "")

    def test0184(self):
        self.assertEquals(self.calculate(26598, -122651.0), -3262271298.00, "")

    def test0185(self):
        self.assertEquals(self.calculate(-10743, -1285.0), 13804755.00, "")

    def test0186(self):
        self.assertEquals(self.calculate(-22148, -68648.0), 1520415904.00, "")

    def test0187(self):
        self.assertEquals(self.calculate(21719, 37948.0), 824192612.00, "")

    def test0188(self):
        self.assertEquals(self.calculate(10961, 11952.0), 131005872.00, "")

    def test0189(self):
        self.assertEquals(self.calculate(-17267, -167104.0), 2885384768.00, "")

    def test0190(self):
        self.assertEquals(self.calculate(-26854, -81752.0), 2195368208.00, "")

    def test0191(self):
        self.assertEquals(self.calculate(-24587, 32936.0), -809797432.00, "")

    def test0192(self):
        self.assertEquals(self.calculate(17071, -38116.0), -650678236.00, "")

    def test0193(self):
        self.assertEquals(self.calculate(-24931, 108652.0), -2708803012.00, "")

    def test0194(self):
        self.assertEquals(self.calculate(4849, 123208.0), 597435592.00, "")

    def test0195(self):
        self.assertEquals(self.calculate(-10348, -48984.0), 506886432.00, "")

    def test0196(self):
        self.assertEquals(self.calculate(-27707, -46800.0), 1296687600.00, "")

    def test0197(self):
        self.assertEquals(self.calculate(-359, -87152.0), 31287568.00, "")

    def test0198(self):
        self.assertEquals(self.calculate(31929, 44048.0), 1406408592.00, "")

    def test0199(self):
        self.assertEquals(self.calculate(15650, 76714.0), 1200574100.00, "")

    def test0200(self):
        self.assertEquals(self.calculate(-3799, 192095.0), -729768905.00, "")

    def test0201(self):
        self.assertEquals(self.calculate(-5344, 114000.0), -609216000.00, "")

    def test0202(self):
        self.assertEquals(self.calculate(-8096, 35894.0), -290597824.00, "")

    def test0203(self):
        self.assertEquals(self.calculate(20507, 117088.0), 2401123616.00, "")

    def test0204(self):
        self.assertEquals(self.calculate(-30163, 44951.0), -1355857013.00, "")

    def test0205(self):
        self.assertEquals(self.calculate(10430, -49345.0), -514668350.00, "")

    def test0206(self):
        self.assertEquals(self.calculate(32172, -40112.0), -1290483264.00, "")

    def test0207(self):
        self.assertEquals(self.calculate(-20084, 201.0), -4036884.00, "")

    def test0208(self):
        self.assertEquals(self.calculate(32353, -187309.0), -6060008077.00, "")

    def test0209(self):
        self.assertEquals(self.calculate(-16624, -23437.0), 389616688.00, "")

    def test0210(self):
        self.assertEquals(self.calculate(4488, 33855.0), 151941240.00, "")

    def test0211(self):
        self.assertEquals(self.calculate(28975, -66907.0), -1938630325.00, "")

    def test0212(self):
        self.assertEquals(self.calculate(28270, -154675.0), -4372662250.00, "")

    def test0213(self):
        self.assertEquals(self.calculate(-30768, 120622.0), -3711297696.00, "")

    def test0214(self):
        self.assertEquals(self.calculate(4467, -46918.0), -209582706.00, "")

    def test0215(self):
        self.assertEquals(self.calculate(13226, 163400.0), 2161128400.00, "")

    def test0216(self):
        self.assertEquals(self.calculate(-32163, 53015.0), -1705121445.00, "")

    def test0217(self):
        self.assertEquals(self.calculate(-19218, 53774.0), -1033428732.00, "")

    def test0218(self):
        self.assertEquals(self.calculate(-1660, -13995.0), 23231700.00, "")

    def test0219(self):
        self.assertEquals(self.calculate(-3322, -159785.0), 530805770.00, "")

    def test0220(self):
        self.assertEquals(self.calculate(32080, -150400.0), -4824832000.00, "")

    def test0221(self):
        self.assertEquals(self.calculate(-26076, 197989.0), -5162761164.00, "")

    def test0222(self):
        self.assertEquals(self.calculate(28088, 2861.0), 80359768.00, "")

    def test0223(self):
        self.assertEquals(self.calculate(11455, -1145.0), -13115975.00, "")

    def test0224(self):
        self.assertEquals(self.calculate(-1945, -2307.0), 4487115.00, "")

    def test0225(self):
        self.assertEquals(self.calculate(-4480, -68188.0), 305482240.00, "")

    def test0226(self):
        self.assertEquals(self.calculate(-18209, -53950.0), 982375550.00, "")

    def test0227(self):
        self.assertEquals(self.calculate(5037, -143317.0), -721887729.00, "")

    def test0228(self):
        self.assertEquals(self.calculate(27212, 77579.0), 2111079748.00, "")

    def test0229(self):
        self.assertEquals(self.calculate(29553, 70174.0), 2073852222.00, "")

    def test0230(self):
        self.assertEquals(self.calculate(15112, -185963.0), -2810272856.00, "")

    def test0231(self):
        self.assertEquals(self.calculate(-8599, -5148.0), 44267652.00, "")

    def test0232(self):
        self.assertEquals(self.calculate(4255, -54935.0), -233748425.00, "")

    def test0233(self):
        self.assertEquals(self.calculate(18229, 146043.0), 2662217847.00, "")

    def test0234(self):
        self.assertEquals(self.calculate(16299, -130542.0), -2127704058.00, "")

    def test0235(self):
        self.assertEquals(self.calculate(-28359, -105789.0), 3000070251.00, "")

    def test0236(self):
        self.assertEquals(self.calculate(6869, 109509.0), 752217321.00, "")

    def test0237(self):
        self.assertEquals(self.calculate(-5044, -191105.0), 963933620.00, "")

    def test0238(self):
        self.assertEquals(self.calculate(-28247, -73744.0), 2083046768.00, "")

    def test0239(self):
        self.assertEquals(self.calculate(-30669, -182557.0), 5598840633.00, "")

    def test0240(self):
        self.assertEquals(self.calculate(-13130, 126526.0), -1661286380.00, "")

    def test0241(self):
        self.assertEquals(self.calculate(18131, -58843.0), -1066882433.00, "")

    def test0242(self):
        self.assertEquals(self.calculate(29176, -146200.0), -4265531200.00, "")

    def test0243(self):
        self.assertEquals(self.calculate(14088, 36428.0), 513197664.00, "")

    def test0244(self):
        self.assertEquals(self.calculate(-14534, 94281.0), -1370280054.00, "")

    def test0245(self):
        self.assertEquals(self.calculate(24243, -72585.0), -1759678155.00, "")

    def test0246(self):
        self.assertEquals(self.calculate(-23267, -21362.0), 497029654.00, "")

    def test0247(self):
        self.assertEquals(self.calculate(10221, -156754.0), -1602182634.00, "")

    def test0248(self):
        self.assertEquals(self.calculate(-19391, -158001.0), 3063797391.00, "")

    def test0249(self):
        self.assertEquals(self.calculate(-12888, 153101.0), -1973165688.00, "")

    def test0250(self):
        self.assertEquals(self.calculate(25210, -6992.0), -176268320.00, "")

    def test0251(self):
        self.assertEquals(self.calculate(17114, 18440.0), 315582160.00, "")

    def test0252(self):
        self.assertEquals(self.calculate(-7260, 99865.0), -725019900.00, "")

    def test0253(self):
        self.assertEquals(self.calculate(5555, -20032.0), -111277760.00, "")

    def test0254(self):
        self.assertEquals(self.calculate(-18004, -178156.0), 3207520624.00, "")

    def test0255(self):
        self.assertEquals(self.calculate(-31719, 76509.0), -2426788971.00, "")

    def test0256(self):
        self.assertEquals(self.calculate(-9246, -89861.0), 830854806.00, "")

    def test0257(self):
        self.assertEquals(self.calculate(-6944, 186431.0), -1294576864.00, "")

    def test0258(self):
        self.assertEquals(self.calculate(18690, 176827.0), 3304896630.00, "")

    def test0259(self):
        self.assertEquals(self.calculate(13467, 39226.0), 528256542.00, "")

    def test0260(self):
        self.assertEquals(self.calculate(-13528, -90648.0), 1226286144.00, "")

    def test0261(self):
        self.assertEquals(self.calculate(-31335, 138936.0), -4353559560.00, "")

    def test0262(self):
        self.assertEquals(self.calculate(-8803, 192875.0), -1697878625.00, "")

    def test0263(self):
        self.assertEquals(self.calculate(-12098, -108126.0), 1308108348.00, "")

    def test0264(self):
        self.assertEquals(self.calculate(9680, -35860.0), -347124800.00, "")

    def test0265(self):
        self.assertEquals(self.calculate(25518, 198914.0), 5075887452.00, "")

    def test0266(self):
        self.assertEquals(self.calculate(-24914, -192679.0), 4800404606.00, "")

    def test0267(self):
        self.assertEquals(self.calculate(-26866, 174831.0), -4697009646.00, "")

    def test0268(self):
        self.assertEquals(self.calculate(29293, -141218.0), -4136698874.00, "")

    def test0269(self):
        self.assertEquals(self.calculate(-15431, -92092.0), 1421071652.00, "")

    def test0270(self):
        self.assertEquals(self.calculate(-4055, 57286.0), -232294730.00, "")

    def test0271(self):
        self.assertEquals(self.calculate(-23410, 117404.0), -2748427640.00, "")

    def test0272(self):
        self.assertEquals(self.calculate(-2802, 180878.0), -506820156.00, "")

    def test0273(self):
        self.assertEquals(self.calculate(-8558, 5917.0), -50637686.00, "")

    def test0274(self):
        self.assertEquals(self.calculate(20918, -151294.0), -3164767892.00, "")

    def test0275(self):
        self.assertEquals(self.calculate(-23208, -3005.0), 69740040.00, "")

    def test0276(self):
        self.assertEquals(self.calculate(5728, -104915.0), -600953120.00, "")

    def test0277(self):
        self.assertEquals(self.calculate(-16763, 138473.0), -2321222899.00, "")

    def test0278(self):
        self.assertEquals(self.calculate(25220, -33251.0), -838590220.00, "")

    def test0279(self):
        self.assertEquals(self.calculate(-3558, 111426.0), -396453708.00, "")

    def test0280(self):
        self.assertEquals(self.calculate(30348, -131653.0), -3995405244.00, "")

    def test0281(self):
        self.assertEquals(self.calculate(-20865, -73179.0), 1526879835.00, "")

    def test0282(self):
        self.assertEquals(self.calculate(30666, -197919.0), -6069384054.00, "")

    def test0283(self):
        self.assertEquals(self.calculate(17514, 82322.0), 1441787508.00, "")

    def test0284(self):
        self.assertEquals(self.calculate(18330, -47231.0), -865744230.00, "")

    def test0285(self):
        self.assertEquals(self.calculate(-3214, -15272.0), 49084208.00, "")

    def test0286(self):
        self.assertEquals(self.calculate(17820, 69260.0), 1234213200.00, "")

    def test0287(self):
        self.assertEquals(self.calculate(-1637, -27401.0), 44855437.00, "")

    def test0288(self):
        self.assertEquals(self.calculate(18170, 150419.0), 2733113230.00, "")

    def test0289(self):
        self.assertEquals(self.calculate(-26705, -35218.0), 940496690.00, "")

    def test0290(self):
        self.assertEquals(self.calculate(-13618, 160170.0), -2181195060.00, "")

    def test0291(self):
        self.assertEquals(self.calculate(-20123, -90615.0), 1823445645.00, "")

    def test0292(self):
        self.assertEquals(self.calculate(16044, 150415.0), 2413258260.00, "")

    def test0293(self):
        self.assertEquals(self.calculate(-27903, 78285.0), -2184386355.00, "")

    def test0294(self):
        self.assertEquals(self.calculate(-21454, 61462.0), -1318605748.00, "")

    def test0295(self):
        self.assertEquals(self.calculate(5339, -89582.0), -478278298.00, "")

    def test0296(self):
        self.assertEquals(self.calculate(22837, 56478.0), 1289788086.00, "")

    def test0297(self):
        self.assertEquals(self.calculate(-2759, 24809.0), -68448031.00, "")

    def test0298(self):
        self.assertEquals(self.calculate(976, -6916.0), -6750016.00, "")

    def test0299(self):
        self.assertEquals(self.calculate(-25224, -143849.0), 3628447176.00, "")

    def test0300(self):
        self.assertEquals(self.calculate(2221, 8453.0), 18774113.00, "")

    def test0301(self):
        self.assertEquals(self.calculate(12982, -177858.0), -2308952556.00, "")

    def test0302(self):
        self.assertEquals(self.calculate(-16717, -56980.0), 952534660.00, "")

    def test0303(self):
        self.assertEquals(self.calculate(20074, -63910.0), -1282929340.00, "")

    def test0304(self):
        self.assertEquals(self.calculate(12775, -195854.0), -2502034850.00, "")

    def test0305(self):
        self.assertEquals(self.calculate(11322, 79420.0), 899193240.00, "")

    def test0306(self):
        self.assertEquals(self.calculate(8589, 63097.0), 541940133.00, "")

    def test0307(self):
        self.assertEquals(self.calculate(-6446, -97840.0), 630676640.00, "")

    def test0308(self):
        self.assertEquals(self.calculate(-9833, 158399.0), -1557537367.00, "")

    def test0309(self):
        self.assertEquals(self.calculate(-22093, 197012.0), -4352586116.00, "")

    def test0310(self):
        self.assertEquals(self.calculate(28479, -182089.0), -5185712631.00, "")

    def test0311(self):
        self.assertEquals(self.calculate(-32141, 31119.0), -1000195779.00, "")

    def test0312(self):
        self.assertEquals(self.calculate(-28503, -150385.0), 4286423655.00, "")

    def test0313(self):
        self.assertEquals(self.calculate(-6392, -46073.0), 294498616.00, "")

    def test0314(self):
        self.assertEquals(self.calculate(-22975, -133811.0), 3074307725.00, "")

    def test0315(self):
        self.assertEquals(self.calculate(-24387, -170015.0), 4146155805.00, "")

    def test0316(self):
        self.assertEquals(self.calculate(-21488, -132343.0), 2843786384.00, "")

    def test0317(self):
        self.assertEquals(self.calculate(-8953, -52663.0), 471491839.00, "")

    def test0318(self):
        self.assertEquals(self.calculate(-6677, 47961.0), -320235597.00, "")

    def test0319(self):
        self.assertEquals(self.calculate(19121, 73653.0), 1408319013.00, "")

    def test0320(self):
        self.assertEquals(self.calculate(14496, -186272.0), -2700198912.00, "")

    def test0321(self):
        self.assertEquals(self.calculate(-6149, -189075.0), 1162622175.00, "")

    def test0322(self):
        self.assertEquals(self.calculate(19259, -159472.0), -3071271248.00, "")

    def test0323(self):
        self.assertEquals(self.calculate(25884, 118712.0), 3072741408.00, "")

    def test0324(self):
        self.assertEquals(self.calculate(30031, 16546.0), 496892926.00, "")

    def test0325(self):
        self.assertEquals(self.calculate(-7370, 13399.0), -98750630.00, "")

    def test0326(self):
        self.assertEquals(self.calculate(549, 164959.0), 90562491.00, "")

    def test0327(self):
        self.assertEquals(self.calculate(-21586, 13951.0), -301146286.00, "")

    def test0328(self):
        self.assertEquals(self.calculate(-19715, 69967.0), -1379399405.00, "")

    def test0329(self):
        self.assertEquals(self.calculate(32145, 119617.0), 3845088465.00, "")

    def test0330(self):
        self.assertEquals(self.calculate(5976, 46055.0), 275224680.00, "")

    def test0331(self):
        self.assertEquals(self.calculate(-17065, 136218.0), -2324560170.00, "")

    def test0332(self):
        self.assertEquals(self.calculate(12701, 86557.0), 1099360457.00, "")

    def test0333(self):
        self.assertEquals(self.calculate(21965, 126664.0), 2782174760.00, "")

    def test0334(self):
        self.assertEquals(self.calculate(30109, -116075.0), -3494902175.00, "")

    def test0335(self):
        self.assertEquals(self.calculate(21885, 152472.0), 3336849720.00, "")

    def test0336(self):
        self.assertEquals(self.calculate(19010, -143731.0), -2732326310.00, "")

    def test0337(self):
        self.assertEquals(self.calculate(9831, -29962.0), -294556422.00, "")

    def test0338(self):
        self.assertEquals(self.calculate(-1950, 122888.0), -239631600.00, "")

    def test0339(self):
        self.assertEquals(self.calculate(20943, -30798.0), -645002514.00, "")

    def test0340(self):
        self.assertEquals(self.calculate(-26734, 130945.0), -3500683630.00, "")

    def test0341(self):
        self.assertEquals(self.calculate(28926, -29432.0), -851350032.00, "")

    def test0342(self):
        self.assertEquals(self.calculate(19199, 9557.0), 183484843.00, "")

    def test0343(self):
        self.assertEquals(self.calculate(2916, 41429.0), 120806964.00, "")

    def test0344(self):
        self.assertEquals(self.calculate(-12682, 58827.0), -746044014.00, "")

    def test0345(self):
        self.assertEquals(self.calculate(4380, -92056.0), -403205280.00, "")

    def test0346(self):
        self.assertEquals(self.calculate(-30976, -138826.0), 4300274176.00, "")

    def test0347(self):
        self.assertEquals(self.calculate(31249, 33662.0), 1051903838.00, "")

    def test0348(self):
        self.assertEquals(self.calculate(19177, 82709.0), 1586110493.00, "")

    def test0349(self):
        self.assertEquals(self.calculate(10466, 165722.0), 1734446452.00, "")

    def test0350(self):
        self.assertEquals(self.calculate(24617, 72301.0), 1779833717.00, "")

    def test0351(self):
        self.assertEquals(self.calculate(-5351, 103763.0), -555235813.00, "")

    def test0352(self):
        self.assertEquals(self.calculate(-10508, -143131.0), 1504020548.00, "")

    def test0353(self):
        self.assertEquals(self.calculate(-21861, -18116.0), 396033876.00, "")

    def test0354(self):
        self.assertEquals(self.calculate(-1876, 169084.0), -317201584.00, "")

    def test0355(self):
        self.assertEquals(self.calculate(14205, 93479.0), 1327869195.00, "")

    def test0356(self):
        self.assertEquals(self.calculate(-16364, 164907.0), -2698538148.00, "")

    def test0357(self):
        self.assertEquals(self.calculate(-193, 142.0), -27406.00, "")

    def test0358(self):
        self.assertEquals(self.calculate(4499, 196274.0), 883036726.00, "")

    def test0359(self):
        self.assertEquals(self.calculate(-16493, -124980.0), 2061295140.00, "")

    def test0360(self):
        self.assertEquals(self.calculate(16129, -43329.0), -698853441.00, "")

    def test0361(self):
        self.assertEquals(self.calculate(27595, -171703.0), -4738144285.00, "")

    def test0362(self):
        self.assertEquals(self.calculate(-31226, -89159.0), 2784078934.00, "")

    def test0363(self):
        self.assertEquals(self.calculate(28652, -51380.0), -1472139760.00, "")

    def test0364(self):
        self.assertEquals(self.calculate(22681, 195358.0), 4430914798.00, "")

    def test0365(self):
        self.assertEquals(self.calculate(-21319, -79499.0), 1694839181.00, "")

    def test0366(self):
        self.assertEquals(self.calculate(20025, 109715.0), 2197042875.00, "")

    def test0367(self):
        self.assertEquals(self.calculate(-23804, -167716.0), 3992311664.00, "")

    def test0368(self):
        self.assertEquals(self.calculate(-16318, 187562.0), -3060636716.00, "")

    def test0369(self):
        self.assertEquals(self.calculate(-28343, -89929.0), 2548857647.00, "")

    def test0370(self):
        self.assertEquals(self.calculate(32240, -85418.0), -2753876320.00, "")

    def test0371(self):
        self.assertEquals(self.calculate(6053, 152078.0), 920528134.00, "")

    def test0372(self):
        self.assertEquals(self.calculate(25055, 2847.0), 71331585.00, "")

    def test0373(self):
        self.assertEquals(self.calculate(11580, -140738.0), -1629746040.00, "")

    def test0374(self):
        self.assertEquals(self.calculate(30255, -186106.0), -5630637030.00, "")

    def test0375(self):
        self.assertEquals(self.calculate(24489, 65546.0), 1605155994.00, "")

    def test0376(self):
        self.assertEquals(self.calculate(-29584, 40147.0), -1187708848.00, "")

    def test0377(self):
        self.assertEquals(self.calculate(-27286, 57695.0), -1574265770.00, "")

    def test0378(self):
        self.assertEquals(self.calculate(7934, 17235.0), 136742490.00, "")

    def test0379(self):
        self.assertEquals(self.calculate(7934, -50764.0), -402761576.00, "")

    def test0380(self):
        self.assertEquals(self.calculate(-22371, 32829.0), -734417559.00, "")

    def test0381(self):
        self.assertEquals(self.calculate(-16084, -27568.0), 443403712.00, "")

    def test0382(self):
        self.assertEquals(self.calculate(-12565, 182154.0), -2288765010.00, "")

    def test0383(self):
        self.assertEquals(self.calculate(4340, 94993.0), 412269620.00, "")

    def test0384(self):
        self.assertEquals(self.calculate(10801, 76330.0), 824440330.00, "")

    def test0385(self):
        self.assertEquals(self.calculate(15686, 154645.0), 2425761470.00, "")

    def test0386(self):
        self.assertEquals(self.calculate(19319, -32856.0), -634745064.00, "")

    def test0387(self):
        self.assertEquals(self.calculate(30557, 64125.0), 1959467625.00, "")

    def test0388(self):
        self.assertEquals(self.calculate(-20438, -159464.0), 3259125232.00, "")

    def test0389(self):
        self.assertEquals(self.calculate(21280, -59550.0), -1267224000.00, "")

    def test0390(self):
        self.assertEquals(self.calculate(18610, 161605.0), 3007469050.00, "")

    def test0391(self):
        self.assertEquals(self.calculate(13933, -41210.0), -574178930.00, "")

    def test0392(self):
        self.assertEquals(self.calculate(-8434, 152690.0), -1287787460.00, "")

    def test0393(self):
        self.assertEquals(self.calculate(23994, -68364.0), -1640325816.00, "")

    def test0394(self):
        self.assertEquals(self.calculate(20266, -139720.0), -2831565520.00, "")

    def test0395(self):
        self.assertEquals(self.calculate(15482, -171137.0), -2649543034.00, "")

    def test0396(self):
        self.assertEquals(self.calculate(-23324, -90185.0), 2103474940.00, "")

    def test0397(self):
        self.assertEquals(self.calculate(27016, -160228.0), -4328719648.00, "")

    def test0398(self):
        self.assertEquals(self.calculate(11477, -85475.0), -980996575.00, "")

    def test0399(self):
        self.assertEquals(self.calculate(32701, -20908.0), -683712508.00, "")

    def test0400(self):
        self.assertEquals(self.calculate(12155, -172359.0), -2095023645.00, "")

    def test0401(self):
        self.assertEquals(self.calculate(-12729, -26699.0), 339851571.00, "")

    def test0402(self):
        self.assertEquals(self.calculate(23977, -101229.0), -2427167733.00, "")

    def test0403(self):
        self.assertEquals(self.calculate(-2200, 171823.0), -378010600.00, "")

    def test0404(self):
        self.assertEquals(self.calculate(30845, -75701.0), -2334997345.00, "")

    def test0405(self):
        self.assertEquals(self.calculate(-9202, 5305.0), -48816610.00, "")

    def test0406(self):
        self.assertEquals(self.calculate(-31884, -98559.0), 3142455156.00, "")

    def test0407(self):
        self.assertEquals(self.calculate(-19589, -134684.0), 2638324876.00, "")

    def test0408(self):
        self.assertEquals(self.calculate(-24623, 42849.0), -1055070927.00, "")

    def test0409(self):
        self.assertEquals(self.calculate(21236, -139884.0), -2970576624.00, "")

    def test0410(self):
        self.assertEquals(self.calculate(-1884, 101514.0), -191252376.00, "")

    def test0411(self):
        self.assertEquals(self.calculate(11605, 199809.0), 2318783445.00, "")

    def test0412(self):
        self.assertEquals(self.calculate(-27927, 42887.0), -1197705249.00, "")

    def test0413(self):
        self.assertEquals(self.calculate(-7340, 136933.0), -1005088220.00, "")

    def test0414(self):
        self.assertEquals(self.calculate(-5039, 192206.0), -968526034.00, "")

    def test0415(self):
        self.assertEquals(self.calculate(-36, 3627.0), -130572.00, "")

    def test0416(self):
        self.assertEquals(self.calculate(1988, 107475.0), 213660300.00, "")

    def test0417(self):
        self.assertEquals(self.calculate(-1013, -109413.0), 110835369.00, "")

    def test0418(self):
        self.assertEquals(self.calculate(-7513, 65355.0), -491012115.00, "")

    def test0419(self):
        self.assertEquals(self.calculate(-9448, -195713.0), 1849096424.00, "")

    def test0420(self):
        self.assertEquals(self.calculate(5447, 71279.0), 388256713.00, "")

    def test0421(self):
        self.assertEquals(self.calculate(-13301, 23021.0), -306202321.00, "")

    def test0422(self):
        self.assertEquals(self.calculate(-23623, 72615.0), -1715384145.00, "")

    def test0423(self):
        self.assertEquals(self.calculate(32361, -64126.0), -2075181486.00, "")

    def test0424(self):
        self.assertEquals(self.calculate(-21188, 199371.0), -4224272748.00, "")

    def test0425(self):
        self.assertEquals(self.calculate(30942, 114175.0), 3532802850.00, "")

    def test0426(self):
        self.assertEquals(self.calculate(-9743, -120526.0), 1174284818.00, "")

    def test0427(self):
        self.assertEquals(self.calculate(-8543, 88669.0), -757499267.00, "")

    def test0428(self):
        self.assertEquals(self.calculate(-12225, 174750.0), -2136318750.00, "")

    def test0429(self):
        self.assertEquals(self.calculate(15193, 38756.0), 588819908.00, "")

    def test0430(self):
        self.assertEquals(self.calculate(5700, -161215.0), -918925500.00, "")

    def test0431(self):
        self.assertEquals(self.calculate(11378, 81095.0), 922698910.00, "")

    def test0432(self):
        self.assertEquals(self.calculate(26149, 73469.0), 1921140881.00, "")

    def test0433(self):
        self.assertEquals(self.calculate(-1557, 113824.0), -177223968.00, "")

    def test0434(self):
        self.assertEquals(self.calculate(18160, 101411.0), 1841623760.00, "")

    def test0435(self):
        self.assertEquals(self.calculate(22706, 99751.0), 2264946206.00, "")

    def test0436(self):
        self.assertEquals(self.calculate(22683, -101079.0), -2292774957.00, "")

    def test0437(self):
        self.assertEquals(self.calculate(-1518, 180571.0), -274106778.00, "")

    def test0438(self):
        self.assertEquals(self.calculate(-20523, -150726.0), 3093349698.00, "")

    def test0439(self):
        self.assertEquals(self.calculate(4887, 23048.0), 112635576.00, "")

    def test0440(self):
        self.assertEquals(self.calculate(-28846, -194634.0), 5614412364.00, "")

    def test0441(self):
        self.assertEquals(self.calculate(-12057, 91957.0), -1108725549.00, "")

    def test0442(self):
        self.assertEquals(self.calculate(28233, 101549.0), 2867032917.00, "")

    def test0443(self):
        self.assertEquals(self.calculate(-4924, 10528.0), -51839872.00, "")

    def test0444(self):
        self.assertEquals(self.calculate(-22743, -17463.0), 397161009.00, "")

    def test0445(self):
        self.assertEquals(self.calculate(29497, -184667.0), -5447122499.00, "")

    def test0446(self):
        self.assertEquals(self.calculate(24080, -87199.0), -2099751920.00, "")

    def test0447(self):
        self.assertEquals(self.calculate(4961, -14427.0), -71572347.00, "")

    def test0448(self):
        self.assertEquals(self.calculate(8864, 171771.0), 1522578144.00, "")

    def test0449(self):
        self.assertEquals(self.calculate(-9256, 17264.0), -159795584.00, "")

    def test0450(self):
        self.assertEquals(self.calculate(-26987, 155456.0), -4195291072.00, "")

    def test0451(self):
        self.assertEquals(self.calculate(1069, 1505.0), 1608845.00, "")

    def test0452(self):
        self.assertEquals(self.calculate(-22013, 126676.0), -2788518788.00, "")

    def test0453(self):
        self.assertEquals(self.calculate(-604, 194217.0), -117307068.00, "")

    def test0454(self):
        self.assertEquals(self.calculate(-8613, -164399.0), 1415968587.00, "")

    def test0455(self):
        self.assertEquals(self.calculate(-25456, 109650.0), -2791250400.00, "")

    def test0456(self):
        self.assertEquals(self.calculate(14353, -142526.0), -2045675678.00, "")

    def test0457(self):
        self.assertEquals(self.calculate(29610, 70587.0), 2090081070.00, "")

    def test0458(self):
        self.assertEquals(self.calculate(936, 74041.0), 69302376.00, "")

    def test0459(self):
        self.assertEquals(self.calculate(23114, 196538.0), 4542779332.00, "")

    def test0460(self):
        self.assertEquals(self.calculate(-20987, 96242.0), -2019830854.00, "")

    def test0461(self):
        self.assertEquals(self.calculate(147, -151932.0), -22334004.00, "")

    def test0462(self):
        self.assertEquals(self.calculate(9147, -103506.0), -946769382.00, "")

    def test0463(self):
        self.assertEquals(self.calculate(-31183, 79923.0), -2492238909.00, "")

    def test0464(self):
        self.assertEquals(self.calculate(14089, 37827.0), 532944603.00, "")

    def test0465(self):
        self.assertEquals(self.calculate(-27160, 57778.0), -1569250480.00, "")

    def test0466(self):
        self.assertEquals(self.calculate(15324, 123499.0), 1892498676.00, "")

    def test0467(self):
        self.assertEquals(self.calculate(22705, 176441.0), 4006092905.00, "")

    def test0468(self):
        self.assertEquals(self.calculate(-32475, 115310.0), -3744692250.00, "")

    def test0469(self):
        self.assertEquals(self.calculate(32657, 63256.0), 2065751192.00, "")

    def test0470(self):
        self.assertEquals(self.calculate(-5140, 157476.0), -809426640.00, "")

    def test0471(self):
        self.assertEquals(self.calculate(5892, 36371.0), 214297932.00, "")

    def test0472(self):
        self.assertEquals(self.calculate(-7159, -122466.0), 876734094.00, "")

    def test0473(self):
        self.assertEquals(self.calculate(15399, -37446.0), -576630954.00, "")

    def test0474(self):
        self.assertEquals(self.calculate(25391, -70172.0), -1781737252.00, "")

    def test0475(self):
        self.assertEquals(self.calculate(8746, 42051.0), 367778046.00, "")

    def test0476(self):
        self.assertEquals(self.calculate(14565, -163254.0), -2377794510.00, "")

    def test0477(self):
        self.assertEquals(self.calculate(-4908, 192385.0), -944225580.00, "")

    def test0478(self):
        self.assertEquals(self.calculate(23664, -164925.0), -3902785200.00, "")

    def test0479(self):
        self.assertEquals(self.calculate(-4638, -122620.0), 568711560.00, "")

    def test0480(self):
        self.assertEquals(self.calculate(10279, -55245.0), -567863355.00, "")

    def test0481(self):
        self.assertEquals(self.calculate(21931, 81407.0), 1785336917.00, "")

    def test0482(self):
        self.assertEquals(self.calculate(994, 44523.0), 44255862.00, "")

    def test0483(self):
        self.assertEquals(self.calculate(19705, -9973.0), -196517965.00, "")

    def test0484(self):
        self.assertEquals(self.calculate(31900, -119441.0), -3810167900.00, "")

    def test0485(self):
        self.assertEquals(self.calculate(9668, 190301.0), 1839830068.00, "")

    def test0486(self):
        self.assertEquals(self.calculate(7592, -186627.0), -1416872184.00, "")

    def test0487(self):
        self.assertEquals(self.calculate(23462, 20004.0), 469333848.00, "")

    def test0488(self):
        self.assertEquals(self.calculate(-6164, -36697.0), 226200308.00, "")

    def test0489(self):
        self.assertEquals(self.calculate(-21105, -137626.0), 2904596730.00, "")

    def test0490(self):
        self.assertEquals(self.calculate(-11643, -180681.0), 2103668883.00, "")

    def test0491(self):
        self.assertEquals(self.calculate(8828, -2109.0), -18618252.00, "")

    def test0492(self):
        self.assertEquals(self.calculate(8834, 115498.0), 1020309332.00, "")

    def test0493(self):
        self.assertEquals(self.calculate(-10427, 76372.0), -796330844.00, "")

    def test0494(self):
        self.assertEquals(self.calculate(-7061, 173399.0), -1224370339.00, "")

    def test0495(self):
        self.assertEquals(self.calculate(-4060, -33619.0), 136493140.00, "")

    def test0496(self):
        self.assertEquals(self.calculate(-26872, 50378.0), -1353757616.00, "")

    def test0497(self):
        self.assertEquals(self.calculate(516, 144758.0), 74695128.00, "")

    def test0498(self):
        self.assertEquals(self.calculate(8272, -9133.0), -75548176.00, "")

    def test0499(self):
        self.assertEquals(self.calculate(-2016, -95186.0), 191894976.00, "")

    def test0500(self):
        self.assertEquals(self.calculate(10457, 77152.0), 806778464.00, "")

    def test0501(self):
        self.assertEquals(self.calculate(9234, -100456.0), -927610704.00, "")

    def test0502(self):
        self.assertEquals(self.calculate(-20220, 148391.0), -3000466020.00, "")

    def test0503(self):
        self.assertEquals(self.calculate(1848, -114191.0), -211024968.00, "")

    def test0504(self):
        self.assertEquals(self.calculate(-19468, -70242.0), 1367471256.00, "")

    def test0505(self):
        self.assertEquals(self.calculate(30700, -173874.0), -5337931800.00, "")

    def test0506(self):
        self.assertEquals(self.calculate(22569, 176977.0), 3994193913.00, "")

    def test0507(self):
        self.assertEquals(self.calculate(-19064, 43045.0), -820609880.00, "")

    def test0508(self):
        self.assertEquals(self.calculate(-19858, 120943.0), -2401686094.00, "")

    def test0509(self):
        self.assertEquals(self.calculate(31017, 6383.0), 197981511.00, "")

    def test0510(self):
        self.assertEquals(self.calculate(-6205, 41989.0), -260541745.00, "")

    def test0511(self):
        self.assertEquals(self.calculate(18290, 83347.0), 1524416630.00, "")

    def test0512(self):
        self.assertEquals(self.calculate(8927, -122.0), -1089094.00, "")

    def test0513(self):
        self.assertEquals(self.calculate(4117, -164157.0), -675834369.00, "")

    def test0514(self):
        self.assertEquals(self.calculate(-12568, -157975.0), 1985429800.00, "")

    def test0515(self):
        self.assertEquals(self.calculate(3939, -122867.0), -483973113.00, "")

    def test0516(self):
        self.assertEquals(self.calculate(-19167, 20912.0), -400820304.00, "")

    def test0517(self):
        self.assertEquals(self.calculate(22075, -114128.0), -2519375600.00, "")

    def test0518(self):
        self.assertEquals(self.calculate(18286, 168486.0), 3080934996.00, "")

    def test0519(self):
        self.assertEquals(self.calculate(26773, -51584.0), -1381058432.00, "")

    def test0520(self):
        self.assertEquals(self.calculate(27421, -141975.0), -3893096475.00, "")

    def test0521(self):
        self.assertEquals(self.calculate(-14453, 131472.0), -1900164816.00, "")

    def test0522(self):
        self.assertEquals(self.calculate(-6916, -131331.0), 908285196.00, "")

    def test0523(self):
        self.assertEquals(self.calculate(13275, -79724.0), -1058336100.00, "")

    def test0524(self):
        self.assertEquals(self.calculate(-31274, 91739.0), -2869045486.00, "")

    def test0525(self):
        self.assertEquals(self.calculate(-26556, 183208.0), -4865271648.00, "")

    def test0526(self):
        self.assertEquals(self.calculate(-18235, -33684.0), 614227740.00, "")

    def test0527(self):
        self.assertEquals(self.calculate(6635, -50593.0), -335684555.00, "")

    def test0528(self):
        self.assertEquals(self.calculate(17318, -34715.0), -601194370.00, "")

    def test0529(self):
        self.assertEquals(self.calculate(-5890, -79250.0), 466782500.00, "")

    def test0530(self):
        self.assertEquals(self.calculate(-13089, 143311.0), -1875797679.00, "")

    def test0531(self):
        self.assertEquals(self.calculate(20575, 24270.0), 499355250.00, "")

    def test0532(self):
        self.assertEquals(self.calculate(-22209, -34226.0), 760125234.00, "")

    def test0533(self):
        self.assertEquals(self.calculate(9067, -144800.0), -1312901600.00, "")

    def test0534(self):
        self.assertEquals(self.calculate(-19287, -18265.0), 352277055.00, "")

    def test0535(self):
        self.assertEquals(self.calculate(7051, -108206.0), -762960506.00, "")

    def test0536(self):
        self.assertEquals(self.calculate(3457, -77970.0), -269542290.00, "")

    def test0537(self):
        self.assertEquals(self.calculate(11203, -79672.0), -892565416.00, "")

    def test0538(self):
        self.assertEquals(self.calculate(-28534, -73557.0), 2098875438.00, "")

    def test0539(self):
        self.assertEquals(self.calculate(-7655, -10715.0), 82023325.00, "")

    def test0540(self):
        self.assertEquals(self.calculate(6960, -38988.0), -271356480.00, "")

    def test0541(self):
        self.assertEquals(self.calculate(-22692, 106862.0), -2424912504.00, "")

    def test0542(self):
        self.assertEquals(self.calculate(-2227, 152584.0), -339804568.00, "")

    def test0543(self):
        self.assertEquals(self.calculate(32726, 35831.0), 1172605306.00, "")

    def test0544(self):
        self.assertEquals(self.calculate(4863, 3724.0), 18109812.00, "")

    def test0545(self):
        self.assertEquals(self.calculate(9133, 94784.0), 865662272.00, "")

    def test0546(self):
        self.assertEquals(self.calculate(16280, -45178.0), -735497840.00, "")

    def test0547(self):
        self.assertEquals(self.calculate(-17077, 65867.0), -1124810759.00, "")

    def test0548(self):
        self.assertEquals(self.calculate(-3154, -4067.0), 12827318.00, "")

    def test0549(self):
        self.assertEquals(self.calculate(28183, 22815.0), 642995145.00, "")

    def test0550(self):
        self.assertEquals(self.calculate(-763, 21277.0), -16234351.00, "")

    def test0551(self):
        self.assertEquals(self.calculate(12009, 82088.0), 985794792.00, "")

    def test0552(self):
        self.assertEquals(self.calculate(18198, 80796.0), 1470325608.00, "")

    def test0553(self):
        self.assertEquals(self.calculate(-11952, -33177.0), 396531504.00, "")

    def test0554(self):
        self.assertEquals(self.calculate(22164, 186056.0), 4123745184.00, "")

    def test0555(self):
        self.assertEquals(self.calculate(-30478, -103308.0), 3148621224.00, "")

    def test0556(self):
        self.assertEquals(self.calculate(-1452, 156551.0), -227312052.00, "")

    def test0557(self):
        self.assertEquals(self.calculate(-5681, -60097.0), 341411057.00, "")

    def test0558(self):
        self.assertEquals(self.calculate(-11997, -178961.0), 2146995117.00, "")

    def test0559(self):
        self.assertEquals(self.calculate(1484, 120727.0), 179158868.00, "")

    def test0560(self):
        self.assertEquals(self.calculate(-24653, -192698.0), 4750583794.00, "")

    def test0561(self):
        self.assertEquals(self.calculate(-11917, 134559.0), -1603539603.00, "")

    def test0562(self):
        self.assertEquals(self.calculate(12735, 118471.0), 1508728185.00, "")

    def test0563(self):
        self.assertEquals(self.calculate(-12794, -5507.0), 70456558.00, "")

    def test0564(self):
        self.assertEquals(self.calculate(17538, -50004.0), -876970152.00, "")

    def test0565(self):
        self.assertEquals(self.calculate(18144, 184816.0), 3353301504.00, "")

    def test0566(self):
        self.assertEquals(self.calculate(8007, -81801.0), -654980607.00, "")

    def test0567(self):
        self.assertEquals(self.calculate(-7955, 129178.0), -1027610990.00, "")

    def test0568(self):
        self.assertEquals(self.calculate(16962, 168978.0), 2866204836.00, "")

    def test0569(self):
        self.assertEquals(self.calculate(10251, -145683.0), -1493396433.00, "")

    def test0570(self):
        self.assertEquals(self.calculate(-10704, -74644.0), 798989376.00, "")

    def test0571(self):
        self.assertEquals(self.calculate(-2698, 40953.0), -110491194.00, "")

    def test0572(self):
        self.assertEquals(self.calculate(-21495, -130445.0), 2803915275.00, "")

    def test0573(self):
        self.assertEquals(self.calculate(-12895, -174073.0), 2244671335.00, "")

    def test0574(self):
        self.assertEquals(self.calculate(-27851, 32570.0), -907107070.00, "")

    def test0575(self):
        self.assertEquals(self.calculate(-9804, -43466.0), 426140664.00, "")

    def test0576(self):
        self.assertEquals(self.calculate(-3987, 135744.0), -541211328.00, "")

    def test0577(self):
        self.assertEquals(self.calculate(-27809, -86970.0), 2418548730.00, "")

    def test0578(self):
        self.assertEquals(self.calculate(-10875, -54918.0), 597233250.00, "")

    def test0579(self):
        self.assertEquals(self.calculate(-16018, -44195.0), 707915510.00, "")

    def test0580(self):
        self.assertEquals(self.calculate(11792, 49125.0), 579282000.00, "")

    def test0581(self):
        self.assertEquals(self.calculate(17451, -164096.0), -2863639296.00, "")

    def test0582(self):
        self.assertEquals(self.calculate(-26371, -62941.0), 1659817111.00, "")

    def test0583(self):
        self.assertEquals(self.calculate(-23544, 65225.0), -1535657400.00, "")

    def test0584(self):
        self.assertEquals(self.calculate(1203, -98560.0), -118567680.00, "")

    def test0585(self):
        self.assertEquals(self.calculate(-21616, 8667.0), -187345872.00, "")

    def test0586(self):
        self.assertEquals(self.calculate(12130, -153331.0), -1859905030.00, "")

    def test0587(self):
        self.assertEquals(self.calculate(-7797, -54790.0), 427197630.00, "")

    def test0588(self):
        self.assertEquals(self.calculate(-6322, -98318.0), 621566396.00, "")

    def test0589(self):
        self.assertEquals(self.calculate(-11568, 151587.0), -1753558416.00, "")

    def test0590(self):
        self.assertEquals(self.calculate(-21043, -90105.0), 1896079515.00, "")

    def test0591(self):
        self.assertEquals(self.calculate(-23276, 191637.0), -4460542812.00, "")

    def test0592(self):
        self.assertEquals(self.calculate(15410, -159246.0), -2453980860.00, "")

    def test0593(self):
        self.assertEquals(self.calculate(-24340, -167312.0), 4072374080.00, "")

    def test0594(self):
        self.assertEquals(self.calculate(-19713, -113603.0), 2239455939.00, "")

    def test0595(self):
        self.assertEquals(self.calculate(-15797, -20072.0), 317077384.00, "")

    def test0596(self):
        self.assertEquals(self.calculate(-16508, 37248.0), -614889984.00, "")

    def test0597(self):
        self.assertEquals(self.calculate(31022, 29196.0), 905718312.00, "")

    def test0598(self):
        self.assertEquals(self.calculate(9359, -50576.0), -473340784.00, "")

    def test0599(self):
        self.assertEquals(self.calculate(-7548, -151861.0), 1146246828.00, "")

    def test0600(self):
        self.assertEquals(self.calculate(-13092, 121151.0), -1586108892.00, "")

    def test0601(self):
        self.assertEquals(self.calculate(27483, 43936.0), 1207493088.00, "")

    def test0602(self):
        self.assertEquals(self.calculate(-18738, -7129.0), 133583202.00, "")

    def test0603(self):
        self.assertEquals(self.calculate(-11185, -188528.0), 2108685680.00, "")

    def test0604(self):
        self.assertEquals(self.calculate(1692, -154246.0), -260984232.00, "")

    def test0605(self):
        self.assertEquals(self.calculate(-142, 134317.0), -19073014.00, "")

    def test0606(self):
        self.assertEquals(self.calculate(5833, -126028.0), -735121324.00, "")

    def test0607(self):
        self.assertEquals(self.calculate(-32058, -29887.0), 958117446.00, "")

    def test0608(self):
        self.assertEquals(self.calculate(-15458, -42276.0), 653502408.00, "")

    def test0609(self):
        self.assertEquals(self.calculate(-4271, -4305.0), 18386655.00, "")

    def test0610(self):
        self.assertEquals(self.calculate(13345, -78917.0), -1053147365.00, "")

    def test0611(self):
        self.assertEquals(self.calculate(486, -103305.0), -50206230.00, "")

    def test0612(self):
        self.assertEquals(self.calculate(2629, 153990.0), 404839710.00, "")

    def test0613(self):
        self.assertEquals(self.calculate(16794, -75502.0), -1267980588.00, "")

    def test0614(self):
        self.assertEquals(self.calculate(19703, 8555.0), 168559165.00, "")

    def test0615(self):
        self.assertEquals(self.calculate(-32054, 109927.0), -3523600058.00, "")

    def test0616(self):
        self.assertEquals(self.calculate(-21924, -135418.0), 2968904232.00, "")

    def test0617(self):
        self.assertEquals(self.calculate(3078, -195281.0), -601074918.00, "")

    def test0618(self):
        self.assertEquals(self.calculate(-28354, -83202.0), 2359109508.00, "")

    def test0619(self):
        self.assertEquals(self.calculate(-4215, 189850.0), -800217750.00, "")

    def test0620(self):
        self.assertEquals(self.calculate(16044, 167796.0), 2692119024.00, "")

    def test0621(self):
        self.assertEquals(self.calculate(12619, -21145.0), -266828755.00, "")

    def test0622(self):
        self.assertEquals(self.calculate(-13175, -53646.0), 706786050.00, "")

    def test0623(self):
        self.assertEquals(self.calculate(-6566, 152619.0), -1002096354.00, "")

    def test0624(self):
        self.assertEquals(self.calculate(-3448, -80715.0), 278305320.00, "")

    def test0625(self):
        self.assertEquals(self.calculate(-11905, -54085.0), 643881925.00, "")

    def test0626(self):
        self.assertEquals(self.calculate(-14428, 79163.0), -1142163764.00, "")

    def test0627(self):
        self.assertEquals(self.calculate(22330, 86992.0), 1942531360.00, "")

    def test0628(self):
        self.assertEquals(self.calculate(4431, 150147.0), 665301357.00, "")

    def test0629(self):
        self.assertEquals(self.calculate(-4156, 35848.0), -148984288.00, "")

    def test0630(self):
        self.assertEquals(self.calculate(26489, -106782.0), -2828548398.00, "")

    def test0631(self):
        self.assertEquals(self.calculate(7287, 45556.0), 331966572.00, "")

    def test0632(self):
        self.assertEquals(self.calculate(-15637, 127874.0), -1999565738.00, "")

    def test0633(self):
        self.assertEquals(self.calculate(-30148, -118860.0), 3583391280.00, "")

    def test0634(self):
        self.assertEquals(self.calculate(-12812, 174633.0), -2237397996.00, "")

    def test0635(self):
        self.assertEquals(self.calculate(-17065, -135233.0), 2307751145.00, "")

    def test0636(self):
        self.assertEquals(self.calculate(-10420, -168098.0), 1751581160.00, "")

    def test0637(self):
        self.assertEquals(self.calculate(-17704, 55062.0), -974817648.00, "")

    def test0638(self):
        self.assertEquals(self.calculate(22828, -33805.0), -771700540.00, "")

    def test0639(self):
        self.assertEquals(self.calculate(11536, 90733.0), 1046695888.00, "")

    def test0640(self):
        self.assertEquals(self.calculate(25757, -77604.0), -1998846228.00, "")

    def test0641(self):
        self.assertEquals(self.calculate(-1360, 31469.0), -42797840.00, "")

    def test0642(self):
        self.assertEquals(self.calculate(25852, -29065.0), -751388380.00, "")

    def test0643(self):
        self.assertEquals(self.calculate(32173, -73160.0), -2353776680.00, "")

    def test0644(self):
        self.assertEquals(self.calculate(-15664, 182259.0), -2854904976.00, "")

    def test0645(self):
        self.assertEquals(self.calculate(30301, -103112.0), -3124396712.00, "")

    def test0646(self):
        self.assertEquals(self.calculate(25917, 132100.0), 3423635700.00, "")

    def test0647(self):
        self.assertEquals(self.calculate(-31770, 4189.0), -133084530.00, "")

    def test0648(self):
        self.assertEquals(self.calculate(-7307, 60367.0), -441101669.00, "")

    def test0649(self):
        self.assertEquals(self.calculate(-18658, 89611.0), -1671962038.00, "")

    def test0650(self):
        self.assertEquals(self.calculate(27896, 21560.0), 601437760.00, "")

    def test0651(self):
        self.assertEquals(self.calculate(-30318, -197386.0), 5984348748.00, "")

    def test0652(self):
        self.assertEquals(self.calculate(1409, -189841.0), -267485969.00, "")

    def test0653(self):
        self.assertEquals(self.calculate(23637, -195486.0), -4620702582.00, "")

    def test0654(self):
        self.assertEquals(self.calculate(-14025, -182546.0), 2560207650.00, "")

    def test0655(self):
        self.assertEquals(self.calculate(-10395, 73760.0), -766735200.00, "")

    def test0656(self):
        self.assertEquals(self.calculate(24162, 10604.0), 256213848.00, "")

    def test0657(self):
        self.assertEquals(self.calculate(15769, -172427.0), -2719001363.00, "")

    def test0658(self):
        self.assertEquals(self.calculate(3809, 16659.0), 63454131.00, "")

    def test0659(self):
        self.assertEquals(self.calculate(28195, 30551.0), 861385445.00, "")

    def test0660(self):
        self.assertEquals(self.calculate(4995, 34270.0), 171178650.00, "")

    def test0661(self):
        self.assertEquals(self.calculate(31609, -86460.0), -2732914140.00, "")

    def test0662(self):
        self.assertEquals(self.calculate(-5190, -52307.0), 271473330.00, "")

    def test0663(self):
        self.assertEquals(self.calculate(13376, 102332.0), 1368792832.00, "")

    def test0664(self):
        self.assertEquals(self.calculate(-31938, -174731.0), 5580558678.00, "")

    def test0665(self):
        self.assertEquals(self.calculate(-2785, 79533.0), -221499405.00, "")

    def test0666(self):
        self.assertEquals(self.calculate(-30873, -112634.0), 3477349482.00, "")

    def test0667(self):
        self.assertEquals(self.calculate(20348, -193558.0), -3938518184.00, "")

    def test0668(self):
        self.assertEquals(self.calculate(-2875, 27732.0), -79729500.00, "")

    def test0669(self):
        self.assertEquals(self.calculate(13743, 115592.0), 1588580856.00, "")

    def test0670(self):
        self.assertEquals(self.calculate(12416, 38414.0), 476948224.00, "")

    def test0671(self):
        self.assertEquals(self.calculate(4672, 56592.0), 264397824.00, "")

    def test0672(self):
        self.assertEquals(self.calculate(-16135, 29606.0), -477692810.00, "")

    def test0673(self):
        self.assertEquals(self.calculate(20879, -14013.0), -292577427.00, "")

    def test0674(self):
        self.assertEquals(self.calculate(-9667, 27965.0), -270337655.00, "")

    def test0675(self):
        self.assertEquals(self.calculate(-29171, -104004.0), 3033900684.00, "")

    def test0676(self):
        self.assertEquals(self.calculate(-7077, -47459.0), 335867343.00, "")

    def test0677(self):
        self.assertEquals(self.calculate(9867, -92093.0), -908681631.00, "")

    def test0678(self):
        self.assertEquals(self.calculate(-31831, -96769.0), 3080254039.00, "")

    def test0679(self):
        self.assertEquals(self.calculate(2743, -187437.0), -514139691.00, "")

    def test0680(self):
        self.assertEquals(self.calculate(23006, 75819.0), 1744291914.00, "")

    def test0681(self):
        self.assertEquals(self.calculate(9354, 64157.0), 600124578.00, "")

    def test0682(self):
        self.assertEquals(self.calculate(8500, 171108.0), 1454418000.00, "")

    def test0683(self):
        self.assertEquals(self.calculate(-8762, -122991.0), 1077647142.00, "")

    def test0684(self):
        self.assertEquals(self.calculate(-26417, -82502.0), 2179455334.00, "")

    def test0685(self):
        self.assertEquals(self.calculate(-27886, 149589.0), -4171438854.00, "")

    def test0686(self):
        self.assertEquals(self.calculate(28494, 74834.0), 2132319996.00, "")

    def test0687(self):
        self.assertEquals(self.calculate(-26576, 105787.0), -2811395312.00, "")

    def test0688(self):
        self.assertEquals(self.calculate(11467, -153005.0), -1754508335.00, "")

    def test0689(self):
        self.assertEquals(self.calculate(-17560, -48591.0), 853257960.00, "")

    def test0690(self):
        self.assertEquals(self.calculate(-13762, 192217.0), -2645290354.00, "")

    def test0691(self):
        self.assertEquals(self.calculate(943, -1154.0), -1088222.00, "")

    def test0692(self):
        self.assertEquals(self.calculate(-10516, 43743.0), -460001388.00, "")

    def test0693(self):
        self.assertEquals(self.calculate(9216, 171206.0), 1577834496.00, "")

    def test0694(self):
        self.assertEquals(self.calculate(15337, -194900.0), -2989181300.00, "")

    def test0695(self):
        self.assertEquals(self.calculate(-1609, -49430.0), 79532870.00, "")

    def test0696(self):
        self.assertEquals(self.calculate(30736, -163931.0), -5038583216.00, "")

    def test0697(self):
        self.assertEquals(self.calculate(-22170, 93366.0), -2069924220.00, "")

    def test0698(self):
        self.assertEquals(self.calculate(12076, 61078.0), 737577928.00, "")

    def test0699(self):
        self.assertEquals(self.calculate(-21081, -75422.0), 1589971182.00, "")

    def test0700(self):
        self.assertEquals(self.calculate(-23743, 51224.0), -1216211432.00, "")

    def test0701(self):
        self.assertEquals(self.calculate(-20041, -7426.0), 148824466.00, "")

    def test0702(self):
        self.assertEquals(self.calculate(9383, 191174.0), 1793785642.00, "")

    def test0703(self):
        self.assertEquals(self.calculate(31947, -126715.0), -4048164105.00, "")

    def test0704(self):
        self.assertEquals(self.calculate(-10643, 136703.0), -1454930029.00, "")

    def test0705(self):
        self.assertEquals(self.calculate(-14012, -50084.0), 701777008.00, "")

    def test0706(self):
        self.assertEquals(self.calculate(5845, 37553.0), 219497285.00, "")

    def test0707(self):
        self.assertEquals(self.calculate(235, 74742.0), 17564370.00, "")

    def test0708(self):
        self.assertEquals(self.calculate(-12556, -74279.0), 932647124.00, "")

    def test0709(self):
        self.assertEquals(self.calculate(16283, -152566.0), -2484232178.00, "")

    def test0710(self):
        self.assertEquals(self.calculate(16137, -141548.0), -2284160076.00, "")

    def test0711(self):
        self.assertEquals(self.calculate(-8220, 57072.0), -469131840.00, "")

    def test0712(self):
        self.assertEquals(self.calculate(20234, -31512.0), -637613808.00, "")

    def test0713(self):
        self.assertEquals(self.calculate(-9447, 9050.0), -85495350.00, "")

    def test0714(self):
        self.assertEquals(self.calculate(2266, -127691.0), -289347806.00, "")

    def test0715(self):
        self.assertEquals(self.calculate(-14299, -113539.0), 1623494161.00, "")

    def test0716(self):
        self.assertEquals(self.calculate(21035, 190554.0), 4008303390.00, "")

    def test0717(self):
        self.assertEquals(self.calculate(-13015, 189072.0), -2460772080.00, "")

    def test0718(self):
        self.assertEquals(self.calculate(-24666, -47299.0), 1166677134.00, "")

    def test0719(self):
        self.assertEquals(self.calculate(23924, -174798.0), -4181867352.00, "")

    def test0720(self):
        self.assertEquals(self.calculate(12718, -102393.0), -1302234174.00, "")

    def test0721(self):
        self.assertEquals(self.calculate(6372, 51033.0), 325182276.00, "")

    def test0722(self):
        self.assertEquals(self.calculate(-20356, -52449.0), 1067651844.00, "")

    def test0723(self):
        self.assertEquals(self.calculate(22131, 64424.0), 1425767544.00, "")

    def test0724(self):
        self.assertEquals(self.calculate(4614, -40471.0), -186733194.00, "")

    def test0725(self):
        self.assertEquals(self.calculate(2822, -12011.0), -33895042.00, "")

    def test0726(self):
        self.assertEquals(self.calculate(-31407, 128405.0), -4032815835.00, "")

    def test0727(self):
        self.assertEquals(self.calculate(-23276, -118085.0), 2748546460.00, "")

    def test0728(self):
        self.assertEquals(self.calculate(5692, -109297.0), -622118524.00, "")

    def test0729(self):
        self.assertEquals(self.calculate(16313, 124449.0), 2030136537.00, "")

    def test0730(self):
        self.assertEquals(self.calculate(-7208, 144575.0), -1042096600.00, "")

    def test0731(self):
        self.assertEquals(self.calculate(-17990, 54873.0), -987165270.00, "")

    def test0732(self):
        self.assertEquals(self.calculate(6362, 148131.0), 942409422.00, "")

    def test0733(self):
        self.assertEquals(self.calculate(9597, 6498.0), 62361306.00, "")

    def test0734(self):
        self.assertEquals(self.calculate(-5584, -67807.0), 378634288.00, "")

    def test0735(self):
        self.assertEquals(self.calculate(59, -4187.0), -247033.00, "")

    def test0736(self):
        self.assertEquals(self.calculate(-2078, -188801.0), 392328478.00, "")

    def test0737(self):
        self.assertEquals(self.calculate(22208, -65192.0), -1447783936.00, "")

    def test0738(self):
        self.assertEquals(self.calculate(3467, -98398.0), -341145866.00, "")

    def test0739(self):
        self.assertEquals(self.calculate(27222, -175257.0), -4770846054.00, "")

    def test0740(self):
        self.assertEquals(self.calculate(16287, 33050.0), 538285350.00, "")

    def test0741(self):
        self.assertEquals(self.calculate(5664, -188009.0), -1064882976.00, "")

    def test0742(self):
        self.assertEquals(self.calculate(23725, 85770.0), 2034893250.00, "")

    def test0743(self):
        self.assertEquals(self.calculate(30929, 155095.0), 4796933255.00, "")

    def test0744(self):
        self.assertEquals(self.calculate(-14931, -75901.0), 1133277831.00, "")

    def test0745(self):
        self.assertEquals(self.calculate(-28455, -37838.0), 1076680290.00, "")

    def test0746(self):
        self.assertEquals(self.calculate(-29654, -73581.0), 2181970974.00, "")

    def test0747(self):
        self.assertEquals(self.calculate(13239, -2579.0), -34143381.00, "")

    def test0748(self):
        self.assertEquals(self.calculate(21348, 182145.0), 3888431460.00, "")

    def test0749(self):
        self.assertEquals(self.calculate(2637, 170532.0), 449692884.00, "")

    def test0750(self):
        self.assertEquals(self.calculate(12059, 167542.0), 2020388978.00, "")

    def test0751(self):
        self.assertEquals(self.calculate(214, 116224.0), 24871936.00, "")

    def test0752(self):
        self.assertEquals(self.calculate(-12546, 86613.0), -1086646698.00, "")

    def test0753(self):
        self.assertEquals(self.calculate(32132, 55354.0), 1778634728.00, "")

    def test0754(self):
        self.assertEquals(self.calculate(1900, -173863.0), -330339700.00, "")

    def test0755(self):
        self.assertEquals(self.calculate(-17478, -9197.0), 160745166.00, "")

    def test0756(self):
        self.assertEquals(self.calculate(-21385, -145867.0), 3119365795.00, "")

    def test0757(self):
        self.assertEquals(self.calculate(30057, 47092.0), 1415444244.00, "")

    def test0758(self):
        self.assertEquals(self.calculate(-10259, 147521.0), -1513417939.00, "")

    def test0759(self):
        self.assertEquals(self.calculate(31797, 149593.0), 4756608621.00, "")

    def test0760(self):
        self.assertEquals(self.calculate(-4211, 167685.0), -706121535.00, "")

    def test0761(self):
        self.assertEquals(self.calculate(26348, -197524.0), -5204362352.00, "")

    def test0762(self):
        self.assertEquals(self.calculate(19276, -148278.0), -2858206728.00, "")

    def test0763(self):
        self.assertEquals(self.calculate(30802, 46307.0), 1426348214.00, "")

    def test0764(self):
        self.assertEquals(self.calculate(-16170, -154630.0), 2500367100.00, "")

    def test0765(self):
        self.assertEquals(self.calculate(13243, 59445.0), 787230135.00, "")

    def test0766(self):
        self.assertEquals(self.calculate(9386, 44496.0), 417639456.00, "")

    def test0767(self):
        self.assertEquals(self.calculate(-30743, 65513.0), -2014066159.00, "")

    def test0768(self):
        self.assertEquals(self.calculate(-4457, -74456.0), 331850392.00, "")

    def test0769(self):
        self.assertEquals(self.calculate(-12470, 87013.0), -1085052110.00, "")

    def test0770(self):
        self.assertEquals(self.calculate(10317, 172413.0), 1778784921.00, "")

    def test0771(self):
        self.assertEquals(self.calculate(31487, 71279.0), 2244361873.00, "")

    def test0772(self):
        self.assertEquals(self.calculate(-17164, -34710.0), 595762440.00, "")

    def test0773(self):
        self.assertEquals(self.calculate(14896, 111679.0), 1663570384.00, "")

    def test0774(self):
        self.assertEquals(self.calculate(23457, -153583.0), -3602596431.00, "")

    def test0775(self):
        self.assertEquals(self.calculate(15411, 188375.0), 2903047125.00, "")

    def test0776(self):
        self.assertEquals(self.calculate(-29469, -24767.0), 729858723.00, "")

    def test0777(self):
        self.assertEquals(self.calculate(1033, -133482.0), -137886906.00, "")

    def test0778(self):
        self.assertEquals(self.calculate(10019, -8203.0), -82185857.00, "")

    def test0779(self):
        self.assertEquals(self.calculate(7789, 103152.0), 803450928.00, "")

    def test0780(self):
        self.assertEquals(self.calculate(12050, -45402.0), -547094100.00, "")

    def test0781(self):
        self.assertEquals(self.calculate(28143, 113945.0), 3206754135.00, "")

    def test0782(self):
        self.assertEquals(self.calculate(3444, 128100.0), 441176400.00, "")

    def test0783(self):
        self.assertEquals(self.calculate(-4906, -39083.0), 191741198.00, "")

    def test0784(self):
        self.assertEquals(self.calculate(-17174, -61437.0), 1055119038.00, "")

    def test0785(self):
        self.assertEquals(self.calculate(23582, 32046.0), 755708772.00, "")

    def test0786(self):
        self.assertEquals(self.calculate(3880, 24395.0), 94652600.00, "")

    def test0787(self):
        self.assertEquals(self.calculate(-4898, -55025.0), 269512450.00, "")

    def test0788(self):
        self.assertEquals(self.calculate(25093, 104560.0), 2623724080.00, "")

    def test0789(self):
        self.assertEquals(self.calculate(28783, -148481.0), -4273728623.00, "")

    def test0790(self):
        self.assertEquals(self.calculate(-16308, -112507.0), 1834764156.00, "")

    def test0791(self):
        self.assertEquals(self.calculate(-17212, -145402.0), 2502659224.00, "")

    def test0792(self):
        self.assertEquals(self.calculate(-6536, 91979.0), -601174744.00, "")

    def test0793(self):
        self.assertEquals(self.calculate(29422, 145644.0), 4285137768.00, "")

    def test0794(self):
        self.assertEquals(self.calculate(-25314, 189419.0), -4794952566.00, "")

    def test0795(self):
        self.assertEquals(self.calculate(29318, 137991.0), 4045620138.00, "")

    def test0796(self):
        self.assertEquals(self.calculate(-23318, -109045.0), 2542711310.00, "")

    def test0797(self):
        self.assertEquals(self.calculate(26512, 190316.0), 5045657792.00, "")

    def test0798(self):
        self.assertEquals(self.calculate(-22086, -160484.0), 3544449624.00, "")

    def test0799(self):
        self.assertEquals(self.calculate(-25743, 35415.0), -911688345.00, "")

    def test0800(self):
        self.assertEquals(self.calculate(23485, -181243.0), -4256491855.00, "")

    def test0801(self):
        self.assertEquals(self.calculate(-13100, -195156.0), 2556543600.00, "")

    def test0802(self):
        self.assertEquals(self.calculate(-3572, -44877.0), 160300644.00, "")

    def test0803(self):
        self.assertEquals(self.calculate(17071, 168254.0), 2872264034.00, "")

    def test0804(self):
        self.assertEquals(self.calculate(2663, 132710.0), 353406730.00, "")

    def test0805(self):
        self.assertEquals(self.calculate(-11124, 159526.0), -1774567224.00, "")

    def test0806(self):
        self.assertEquals(self.calculate(8894, -55609.0), -494586446.00, "")

    def test0807(self):
        self.assertEquals(self.calculate(6668, 67450.0), 449756600.00, "")

    def test0808(self):
        self.assertEquals(self.calculate(5078, -131650.0), -668518700.00, "")

    def test0809(self):
        self.assertEquals(self.calculate(-31557, -188348.0), 5943697836.00, "")

    def test0810(self):
        self.assertEquals(self.calculate(-2238, -32654.0), 73079652.00, "")

    def test0811(self):
        self.assertEquals(self.calculate(-29942, -54532.0), 1632797144.00, "")

    def test0812(self):
        self.assertEquals(self.calculate(29036, 44072.0), 1279674592.00, "")

    def test0813(self):
        self.assertEquals(self.calculate(4377, -111315.0), -487225755.00, "")

    def test0814(self):
        self.assertEquals(self.calculate(-13743, -13873.0), 190656639.00, "")

    def test0815(self):
        self.assertEquals(self.calculate(-2507, 173465.0), -434876755.00, "")

    def test0816(self):
        self.assertEquals(self.calculate(31701, -99994.0), -3169909794.00, "")

    def test0817(self):
        self.assertEquals(self.calculate(-9847, 193081.0), -1901268607.00, "")

    def test0818(self):
        self.assertEquals(self.calculate(-17411, -82288.0), 1432716368.00, "")

    def test0819(self):
        self.assertEquals(self.calculate(15250, 51983.0), 792740750.00, "")

    def test0820(self):
        self.assertEquals(self.calculate(-21426, -183107.0), 3923250582.00, "")

    def test0821(self):
        self.assertEquals(self.calculate(-30280, 120366.0), -3644682480.00, "")

    def test0822(self):
        self.assertEquals(self.calculate(-13618, 150045.0), -2043312810.00, "")

    def test0823(self):
        self.assertEquals(self.calculate(-25694, -21286.0), 546922484.00, "")

    def test0824(self):
        self.assertEquals(self.calculate(21333, -54872.0), -1170584376.00, "")

    def test0825(self):
        self.assertEquals(self.calculate(-10589, 15247.0), -161450483.00, "")

    def test0826(self):
        self.assertEquals(self.calculate(21926, -146617.0), -3214724342.00, "")

    def test0827(self):
        self.assertEquals(self.calculate(-4983, -14261.0), 71062563.00, "")

    def test0828(self):
        self.assertEquals(self.calculate(9778, -185339.0), -1812244742.00, "")

    def test0829(self):
        self.assertEquals(self.calculate(12418, -101010.0), -1254342180.00, "")

    def test0830(self):
        self.assertEquals(self.calculate(-18264, -130703.0), 2387159592.00, "")

    def test0831(self):
        self.assertEquals(self.calculate(29980, -89972.0), -2697360560.00, "")

    def test0832(self):
        self.assertEquals(self.calculate(-13067, -38437.0), 502256279.00, "")

    def test0833(self):
        self.assertEquals(self.calculate(26088, -126357.0), -3296401416.00, "")

    def test0834(self):
        self.assertEquals(self.calculate(-5215, -31108.0), 162228220.00, "")

    def test0835(self):
        self.assertEquals(self.calculate(-24286, -103247.0), 2507456642.00, "")

    def test0836(self):
        self.assertEquals(self.calculate(-13410, -31171.0), 418003110.00, "")

    def test0837(self):
        self.assertEquals(self.calculate(-14913, 11304.0), -168576552.00, "")

    def test0838(self):
        self.assertEquals(self.calculate(-11126, -195401.0), 2174031526.00, "")

    def test0839(self):
        self.assertEquals(self.calculate(19997, 123682.0), 2473268954.00, "")

    def test0840(self):
        self.assertEquals(self.calculate(-6734, -146093.0), 983790262.00, "")

    def test0841(self):
        self.assertEquals(self.calculate(-27232, -171531.0), 4671132192.00, "")

    def test0842(self):
        self.assertEquals(self.calculate(10567, 112821.0), 1192179507.00, "")

    def test0843(self):
        self.assertEquals(self.calculate(-16544, 77028.0), -1274351232.00, "")

    def test0844(self):
        self.assertEquals(self.calculate(23354, -115709.0), -2702267986.00, "")

    def test0845(self):
        self.assertEquals(self.calculate(-11514, -55790.0), 642366060.00, "")

    def test0846(self):
        self.assertEquals(self.calculate(8054, 63750.0), 513442500.00, "")

    def test0847(self):
        self.assertEquals(self.calculate(9145, -55762.0), -509943490.00, "")

    def test0848(self):
        self.assertEquals(self.calculate(-15395, -42926.0), 660845770.00, "")

    def test0849(self):
        self.assertEquals(self.calculate(32155, 164017.0), 5273966635.00, "")

    def test0850(self):
        self.assertEquals(self.calculate(2105, 161265.0), 339462825.00, "")

    def test0851(self):
        self.assertEquals(self.calculate(12912, 166680.0), 2152172160.00, "")

    def test0852(self):
        self.assertEquals(self.calculate(20206, -88354.0), -1785280924.00, "")

    def test0853(self):
        self.assertEquals(self.calculate(-18348, -198398.0), 3640206504.00, "")

    def test0854(self):
        self.assertEquals(self.calculate(32328, -108775.0), -3516478200.00, "")

    def test0855(self):
        self.assertEquals(self.calculate(32592, 62014.0), 2021160288.00, "")

    def test0856(self):
        self.assertEquals(self.calculate(-10116, 180231.0), -1823216796.00, "")

    def test0857(self):
        self.assertEquals(self.calculate(29181, -177307.0), -5173995567.00, "")

    def test0858(self):
        self.assertEquals(self.calculate(19121, 196440.0), 3756129240.00, "")

    def test0859(self):
        self.assertEquals(self.calculate(15439, -70687.0), -1091336593.00, "")

    def test0860(self):
        self.assertEquals(self.calculate(-22422, -49715.0), 1114709730.00, "")

    def test0861(self):
        self.assertEquals(self.calculate(26405, -105050.0), -2773845250.00, "")

    def test0862(self):
        self.assertEquals(self.calculate(26763, -174951.0), -4682213613.00, "")

    def test0863(self):
        self.assertEquals(self.calculate(-2291, 8637.0), -19787367.00, "")

    def test0864(self):
        self.assertEquals(self.calculate(-16883, 190300.0), -3212834900.00, "")

    def test0865(self):
        self.assertEquals(self.calculate(576, -109665.0), -63167040.00, "")

    def test0866(self):
        self.assertEquals(self.calculate(-8143, -93050.0), 757706150.00, "")

    def test0867(self):
        self.assertEquals(self.calculate(8408, -120002.0), -1008976816.00, "")

    def test0868(self):
        self.assertEquals(self.calculate(1864, -34885.0), -65025640.00, "")

    def test0869(self):
        self.assertEquals(self.calculate(3635, -1976.0), -7182760.00, "")

    def test0870(self):
        self.assertEquals(self.calculate(24910, 184217.0), 4588845470.00, "")

    def test0871(self):
        self.assertEquals(self.calculate(14562, -25482.0), -371068884.00, "")

    def test0872(self):
        self.assertEquals(self.calculate(4788, -112660.0), -539416080.00, "")

    def test0873(self):
        self.assertEquals(self.calculate(32599, 23375.0), 762001625.00, "")

    def test0874(self):
        self.assertEquals(self.calculate(-26603, -155084.0), 4125699652.00, "")

    def test0875(self):
        self.assertEquals(self.calculate(19258, -106042.0), -2042156836.00, "")

    def test0876(self):
        self.assertEquals(self.calculate(27278, 105727.0), 2884021106.00, "")

    def test0877(self):
        self.assertEquals(self.calculate(-26248, 139652.0), -3665585696.00, "")

    def test0878(self):
        self.assertEquals(self.calculate(24006, 180555.0), 4334403330.00, "")

    def test0879(self):
        self.assertEquals(self.calculate(-5224, 188821.0), -986400904.00, "")

    def test0880(self):
        self.assertEquals(self.calculate(24855, 185294.0), 4605482370.00, "")

    def test0881(self):
        self.assertEquals(self.calculate(-16744, 80284.0), -1344275296.00, "")

    def test0882(self):
        self.assertEquals(self.calculate(-8660, -58425.0), 505960500.00, "")

    def test0883(self):
        self.assertEquals(self.calculate(-4673, -23390.0), 109301470.00, "")

    def test0884(self):
        self.assertEquals(self.calculate(-14690, 38105.0), -559762450.00, "")

    def test0885(self):
        self.assertEquals(self.calculate(-16343, 68486.0), -1119266698.00, "")

    def test0886(self):
        self.assertEquals(self.calculate(6793, -19907.0), -135228251.00, "")

    def test0887(self):
        self.assertEquals(self.calculate(2705, -168130.0), -454791650.00, "")

    def test0888(self):
        self.assertEquals(self.calculate(-2366, -165373.0), 391272518.00, "")

    def test0889(self):
        self.assertEquals(self.calculate(-24143, 156398.0), -3775916914.00, "")

    def test0890(self):
        self.assertEquals(self.calculate(16642, 44920.0), 747558640.00, "")

    def test0891(self):
        self.assertEquals(self.calculate(26231, 37573.0), 985577363.00, "")

    def test0892(self):
        self.assertEquals(self.calculate(-30419, 100381.0), -3053489639.00, "")

    def test0893(self):
        self.assertEquals(self.calculate(15454, 103337.0), 1596969998.00, "")

    def test0894(self):
        self.assertEquals(self.calculate(24946, 181407.0), 4525379022.00, "")

    def test0895(self):
        self.assertEquals(self.calculate(18809, 71042.0), 1336228978.00, "")

    def test0896(self):
        self.assertEquals(self.calculate(-17594, -175890.0), 3094608660.00, "")

    def test0897(self):
        self.assertEquals(self.calculate(22098, 13196.0), 291605208.00, "")

    def test0898(self):
        self.assertEquals(self.calculate(4703, 45387.0), 213455061.00, "")

    def test0899(self):
        self.assertEquals(self.calculate(27515, -87885.0), -2418155775.00, "")

    def test0900(self):
        self.assertEquals(self.calculate(25344, -178148.0), -4514982912.00, "")

    def test0901(self):
        self.assertEquals(self.calculate(738, 71535.0), 52792830.00, "")

    def test0902(self):
        self.assertEquals(self.calculate(28476, 10430.0), 297004680.00, "")

    def test0903(self):
        self.assertEquals(self.calculate(-12193, -150693.0), 1837399749.00, "")

    def test0904(self):
        self.assertEquals(self.calculate(-30421, 120685.0), -3671358385.00, "")

    def test0905(self):
        self.assertEquals(self.calculate(11813, -196994.0), -2327090122.00, "")

    def test0906(self):
        self.assertEquals(self.calculate(18657, 140359.0), 2618677863.00, "")

    def test0907(self):
        self.assertEquals(self.calculate(1843, -93822.0), -172913946.00, "")

    def test0908(self):
        self.assertEquals(self.calculate(-3509, -106360.0), 373217240.00, "")

    def test0909(self):
        self.assertEquals(self.calculate(6171, -188729.0), -1164646659.00, "")

    def test0910(self):
        self.assertEquals(self.calculate(-8151, 36343.0), -296231793.00, "")

    def test0911(self):
        self.assertEquals(self.calculate(26516, -93929.0), -2490621364.00, "")

    def test0912(self):
        self.assertEquals(self.calculate(-14196, -88711.0), 1259341356.00, "")

    def test0913(self):
        self.assertEquals(self.calculate(25248, 86265.0), 2178018720.00, "")

    def test0914(self):
        self.assertEquals(self.calculate(-31902, 143935.0), -4591814370.00, "")

    def test0915(self):
        self.assertEquals(self.calculate(-30301, -28392.0), 860305992.00, "")

    def test0916(self):
        self.assertEquals(self.calculate(14361, 130668.0), 1876523148.00, "")

    def test0917(self):
        self.assertEquals(self.calculate(20721, 120018.0), 2486892978.00, "")

    def test0918(self):
        self.assertEquals(self.calculate(20259, -123995.0), -2512014705.00, "")

    def test0919(self):
        self.assertEquals(self.calculate(-31701, 44396.0), -1407397596.00, "")

    def test0920(self):
        self.assertEquals(self.calculate(25514, 134444.0), 3430204216.00, "")

    def test0921(self):
        self.assertEquals(self.calculate(-11446, 35966.0), -411666836.00, "")

    def test0922(self):
        self.assertEquals(self.calculate(21124, 58774.0), 1241541976.00, "")

    def test0923(self):
        self.assertEquals(self.calculate(22749, -191724.0), -4361529276.00, "")

    def test0924(self):
        self.assertEquals(self.calculate(-23631, 93247.0), -2203519857.00, "")

    def test0925(self):
        self.assertEquals(self.calculate(4814, 199319.0), 959521666.00, "")

    def test0926(self):
        self.assertEquals(self.calculate(22744, -182575.0), -4152485800.00, "")

    def test0927(self):
        self.assertEquals(self.calculate(-18659, -49416.0), 922053144.00, "")

    def test0928(self):
        self.assertEquals(self.calculate(-25378, 168385.0), -4273274530.00, "")

    def test0929(self):
        self.assertEquals(self.calculate(16633, -1600.0), -26612800.00, "")

    def test0930(self):
        self.assertEquals(self.calculate(28940, 95415.0), 2761310100.00, "")

    def test0931(self):
        self.assertEquals(self.calculate(-14595, 155385.0), -2267844075.00, "")

    def test0932(self):
        self.assertEquals(self.calculate(25464, 50745.0), 1292170680.00, "")

    def test0933(self):
        self.assertEquals(self.calculate(-31432, 109726.0), -3448907632.00, "")

    def test0934(self):
        self.assertEquals(self.calculate(-4692, 139941.0), -656603172.00, "")

    def test0935(self):
        self.assertEquals(self.calculate(-31929, 39959.0), -1275850911.00, "")

    def test0936(self):
        self.assertEquals(self.calculate(-10936, -126140.0), 1379467040.00, "")

    def test0937(self):
        self.assertEquals(self.calculate(-27863, -91443.0), 2547876309.00, "")

    def test0938(self):
        self.assertEquals(self.calculate(29163, -185219.0), -5401541697.00, "")

    def test0939(self):
        self.assertEquals(self.calculate(19704, 82714.0), 1629796656.00, "")

    def test0940(self):
        self.assertEquals(self.calculate(-5653, -158431.0), 895610443.00, "")

    def test0941(self):
        self.assertEquals(self.calculate(-29759, -168707.0), 5020551613.00, "")

    def test0942(self):
        self.assertEquals(self.calculate(30469, 175676.0), 5352672044.00, "")

    def test0943(self):
        self.assertEquals(self.calculate(-17059, 173919.0), -2966884221.00, "")

    def test0944(self):
        self.assertEquals(self.calculate(5001, 60297.0), 301545297.00, "")

    def test0945(self):
        self.assertEquals(self.calculate(29584, -144724.0), -4281514816.00, "")

    def test0946(self):
        self.assertEquals(self.calculate(-17559, -137276.0), 2410429284.00, "")

    def test0947(self):
        self.assertEquals(self.calculate(1797, 188759.0), 339199923.00, "")

    def test0948(self):
        self.assertEquals(self.calculate(11087, -142058.0), -1574997046.00, "")

    def test0949(self):
        self.assertEquals(self.calculate(-16223, 59622.0), -967247706.00, "")

    def test0950(self):
        self.assertEquals(self.calculate(-14391, 185209.0), -2665342719.00, "")

    def test0951(self):
        self.assertEquals(self.calculate(-26873, -84492.0), 2270553516.00, "")

    def test0952(self):
        self.assertEquals(self.calculate(-9077, -145594.0), 1321556738.00, "")

    def test0953(self):
        self.assertEquals(self.calculate(25339, -170411.0), -4318044329.00, "")

    def test0954(self):
        self.assertEquals(self.calculate(21914, -149504.0), -3276230656.00, "")

    def test0955(self):
        self.assertEquals(self.calculate(-25397, -946.0), 24025562.00, "")

    def test0956(self):
        self.assertEquals(self.calculate(15617, 51996.0), 812021532.00, "")

    def test0957(self):
        self.assertEquals(self.calculate(-8605, 11899.0), -102390895.00, "")

    def test0958(self):
        self.assertEquals(self.calculate(-17087, 49724.0), -849633988.00, "")

    def test0959(self):
        self.assertEquals(self.calculate(32619, 169216.0), 5519656704.00, "")

    def test0960(self):
        self.assertEquals(self.calculate(19057, -109190.0), -2080833830.00, "")

    def test0961(self):
        self.assertEquals(self.calculate(11906, 81868.0), 974720408.00, "")

    def test0962(self):
        self.assertEquals(self.calculate(-27774, 81149.0), -2253832326.00, "")

    def test0963(self):
        self.assertEquals(self.calculate(25259, -131118.0), -3311909562.00, "")

    def test0964(self):
        self.assertEquals(self.calculate(29851, 79420.0), 2370766420.00, "")

    def test0965(self):
        self.assertEquals(self.calculate(19020, -81349.0), -1547257980.00, "")

    def test0966(self):
        self.assertEquals(self.calculate(-3308, 3766.0), -12457928.00, "")

    def test0967(self):
        self.assertEquals(self.calculate(4688, -167076.0), -783252288.00, "")

    def test0968(self):
        self.assertEquals(self.calculate(10315, 182727.0), 1884829005.00, "")

    def test0969(self):
        self.assertEquals(self.calculate(-7361, 164381.0), -1210008541.00, "")

    def test0970(self):
        self.assertEquals(self.calculate(18430, -69244.0), -1276166920.00, "")

    def test0971(self):
        self.assertEquals(self.calculate(18397, -154753.0), -2846990941.00, "")

    def test0972(self):
        self.assertEquals(self.calculate(-16085, 10008.0), -160978680.00, "")

    def test0973(self):
        self.assertEquals(self.calculate(-305, 12833.0), -3914065.00, "")

    def test0974(self):
        self.assertEquals(self.calculate(482, -100495.0), -48438590.00, "")

    def test0975(self):
        self.assertEquals(self.calculate(-11469, 18210.0), -208850490.00, "")

    def test0976(self):
        self.assertEquals(self.calculate(21927, -33509.0), -734751843.00, "")

    def test0977(self):
        self.assertEquals(self.calculate(9050, 7953.0), 71974650.00, "")

    def test0978(self):
        self.assertEquals(self.calculate(-14995, 70852.0), -1062425740.00, "")

    def test0979(self):
        self.assertEquals(self.calculate(17473, 148368.0), 2592434064.00, "")

    def test0980(self):
        self.assertEquals(self.calculate(-20267, -107043.0), 2169440481.00, "")

    def test0981(self):
        self.assertEquals(self.calculate(13367, -140680.0), -1880469560.00, "")

    def test0982(self):
        self.assertEquals(self.calculate(-10891, 126430.0), -1376949130.00, "")

    def test0983(self):
        self.assertEquals(self.calculate(22012, 83065.0), 1828426780.00, "")

    def test0984(self):
        self.assertEquals(self.calculate(-7764, 159557.0), -1238800548.00, "")

    def test0985(self):
        self.assertEquals(self.calculate(-18542, -159105.0), 2950124910.00, "")

    def test0986(self):
        self.assertEquals(self.calculate(959, -134037.0), -128541483.00, "")

    def test0987(self):
        self.assertEquals(self.calculate(17941, 59284.0), 1063614244.00, "")

    def test0988(self):
        self.assertEquals(self.calculate(-26788, -112527.0), 3014373276.00, "")

    def test0989(self):
        self.assertEquals(self.calculate(28583, 153852.0), 4397551716.00, "")

    def test0990(self):
        self.assertEquals(self.calculate(-19905, -34849.0), 693669345.00, "")

    def test0991(self):
        self.assertEquals(self.calculate(3916, -33186.0), -129956376.00, "")

    def test0992(self):
        self.assertEquals(self.calculate(2272, -112435.0), -255452320.00, "")

    def test0993(self):
        self.assertEquals(self.calculate(20109, -63665.0), -1280239485.00, "")

    def test0994(self):
        self.assertEquals(self.calculate(14147, -154885.0), -2191158095.00, "")

    def test0995(self):
        self.assertEquals(self.calculate(-24882, -99618.0), 2478695076.00, "")

    def test0996(self):
        self.assertEquals(self.calculate(-2462, -153440.0), 377769280.00, "")

    def test0997(self):
        self.assertEquals(self.calculate(-30401, 193118.0), -5870980318.00, "")

    def test0998(self):
        self.assertEquals(self.calculate(4329, 31106.0), 134657874.00, "")

    def test0999(self):
        self.assertEquals(self.calculate(-20054, -114186.0), 2289886044.00, "")

    def test1000(self):
        self.assertEquals(self.calculate(-15477, -50548.0), 782331396.00, "")

    def test1001(self):
        self.assertEquals(self.calculate(16670, 67700.0), 1128559000.00, "")

    def test1002(self):
        self.assertEquals(self.calculate(-27266, -9901.0), 269960666.00, "")

    def test1003(self):
        self.assertEquals(self.calculate(3999, -38252.0), -152969748.00, "")

    def test1004(self):
        self.assertEquals(self.calculate(24375, -10769.0), -262494375.00, "")

    def test1005(self):
        self.assertEquals(self.calculate(-6940, -43484.0), 301778960.00, "")

    def test1006(self):
        self.assertEquals(self.calculate(6892, 107741.0), 742550972.00, "")

    def test1007(self):
        self.assertEquals(self.calculate(-25244, -79315.0), 2002227860.00, "")

    def test1008(self):
        self.assertEquals(self.calculate(7457, 52664.0), 392715448.00, "")

    def test1009(self):
        self.assertEquals(self.calculate(3169, -56117.0), -177834773.00, "")

    def test1010(self):
        self.assertEquals(self.calculate(32048, 100854.0), 3232168992.00, "")

    def test1011(self):
        self.assertEquals(self.calculate(25229, 59269.0), 1495297601.00, "")

    def test1012(self):
        self.assertEquals(self.calculate(13484, 19962.0), 269167608.00, "")

    def test1013(self):
        self.assertEquals(self.calculate(-31905, 123497.0), -3940171785.00, "")

    def test1014(self):
        self.assertEquals(self.calculate(-5876, -77722.0), 456694472.00, "")

    def test1015(self):
        self.assertEquals(self.calculate(-26737, -144254.0), 3856919198.00, "")

    def test1016(self):
        self.assertEquals(self.calculate(-21767, -181497.0), 3950645199.00, "")

    def test1017(self):
        self.assertEquals(self.calculate(-18531, 143994.0), -2668352814.00, "")

    def test1018(self):
        self.assertEquals(self.calculate(-2966, 77670.0), -230369220.00, "")

    def test1019(self):
        self.assertEquals(self.calculate(20530, 184171.0), 3781030630.00, "")

    def test1020(self):
        self.assertEquals(self.calculate(5486, 109591.0), 601216226.00, "")

    def test1021(self):
        self.assertEquals(self.calculate(4510, 45980.0), 207369800.00, "")

    def test1022(self):
        self.assertEquals(self.calculate(27742, -31095.0), -862637490.00, "")

    def test1023(self):
        self.assertEquals(self.calculate(-29288, 4774.0), -139820912.00, "")



class TestVM_Mul_LongInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushW(rhs)
        v.VM_Mul()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(2048016, 5462), -1698638496)

    def test0001(self):
        self.assertEquals(self.calculate(-862247677, 20332), 836733508)

    def test0002(self):
        self.assertEquals(self.calculate(-1437228181, 11803), 1516598857)

    def test0003(self):
        self.assertEquals(self.calculate(2111549679, 20557), -2107709469)

    def test0004(self):
        self.assertEquals(self.calculate(1366492295, 6014), 1812224882)

    def test0005(self):
        self.assertEquals(self.calculate(-404888968, -30183), 1581764024)

    def test0006(self):
        self.assertEquals(self.calculate(51707704, 28394), -690267856)

    def test0007(self):
        self.assertEquals(self.calculate(-337100572, -16652), -123530928)

    def test0008(self):
        self.assertEquals(self.calculate(1139973141, -12776), -62748680)

    def test0009(self):
        self.assertEquals(self.calculate(-2054486545, 24926), -1236550462)

    def test0010(self):
        self.assertEquals(self.calculate(230378018, 19644), -1349744392)

    def test0011(self):
        self.assertEquals(self.calculate(-865465795, 362), 233994818)

    def test0012(self):
        self.assertEquals(self.calculate(-991648865, 24031), -1835316607)

    def test0013(self):
        self.assertEquals(self.calculate(1028167840, 12702), -1207643456)

    def test0014(self):
        self.assertEquals(self.calculate(749231883, -15755), -1578187257)

    def test0015(self):
        self.assertEquals(self.calculate(1288605571, 27472), 1451792880)

    def test0016(self):
        self.assertEquals(self.calculate(1196377684, 15257), -476683212)

    def test0017(self):
        self.assertEquals(self.calculate(182915507, -7376), -565048688)

    def test0018(self):
        self.assertEquals(self.calculate(599590157, -881), 42049091)

    def test0019(self):
        self.assertEquals(self.calculate(-2026259671, 29386), 1759899738)

    def test0020(self):
        self.assertEquals(self.calculate(1179071027, 10705), -953538909)

    def test0021(self):
        self.assertEquals(self.calculate(241531549, -9543), 1461865845)

    def test0022(self):
        self.assertEquals(self.calculate(366319304, 12063), -611583432)

    def test0023(self):
        self.assertEquals(self.calculate(-850001270, 9216), 408643584)

    def test0024(self):
        self.assertEquals(self.calculate(1086216166, -9831), -1302430090)

    def test0025(self):
        self.assertEquals(self.calculate(1316857191, 12455), -1023789519)

    def test0026(self):
        self.assertEquals(self.calculate(-636734811, -22326), -600359374)

    def test0027(self):
        self.assertEquals(self.calculate(-145211697, -27844), 1710265732)

    def test0028(self):
        self.assertEquals(self.calculate(1418057775, -29261), -109507619)

    def test0029(self):
        self.assertEquals(self.calculate(2077935600, -12408), -336246912)

    def test0030(self):
        self.assertEquals(self.calculate(183331152, 24367), 464192944)

    def test0031(self):
        self.assertEquals(self.calculate(552929515, 13096), -149932616)

    def test0032(self):
        self.assertEquals(self.calculate(1857412585, -11799), 1607021073)

    def test0033(self):
        self.assertEquals(self.calculate(-839183043, -30282), -1180582306)

    def test0034(self):
        self.assertEquals(self.calculate(-16765891, -30944), -887311712)

    def test0035(self):
        self.assertEquals(self.calculate(544829465, -8797), 318698731)

    def test0036(self):
        self.assertEquals(self.calculate(-1020265743, 26602), -1210951862)

    def test0037(self):
        self.assertEquals(self.calculate(669179343, -31945), -881879943)

    def test0038(self):
        self.assertEquals(self.calculate(-1155726301, -2843), 79892303)

    def test0039(self):
        self.assertEquals(self.calculate(1359559670, -12054), 1462939356)

    def test0040(self):
        self.assertEquals(self.calculate(747610910, 19882), -881698836)

    def test0041(self):
        self.assertEquals(self.calculate(769088203, -4766), -1867272010)

    def test0042(self):
        self.assertEquals(self.calculate(1754049180, -29160), 691439264)

    def test0043(self):
        self.assertEquals(self.calculate(1281890446, 14079), 283011442)

    def test0044(self):
        self.assertEquals(self.calculate(661109487, -25480), -207993848)

    def test0045(self):
        self.assertEquals(self.calculate(-702650238, 1910), -2032158228)

    def test0046(self):
        self.assertEquals(self.calculate(-2105307379, 24842), -229145726)

    def test0047(self):
        self.assertEquals(self.calculate(898821088, 32445), -577739680)

    def test0048(self):
        self.assertEquals(self.calculate(1283745688, -15890), -1919293616)

    def test0049(self):
        self.assertEquals(self.calculate(-449511858, 13166), 191811460)

    def test0050(self):
        self.assertEquals(self.calculate(1770889664, 18149), 636235968)

    def test0051(self):
        self.assertEquals(self.calculate(1069369625, -18462), 1262642962)

    def test0052(self):
        self.assertEquals(self.calculate(879148154, -24556), -1856439928)

    def test0053(self):
        self.assertEquals(self.calculate(1354467744, 31837), 717913888)

    def test0054(self):
        self.assertEquals(self.calculate(1791314952, 9724), -1640759328)

    def test0055(self):
        self.assertEquals(self.calculate(684805084, -2874), -1034789848)

    def test0056(self):
        self.assertEquals(self.calculate(-655070844, 18502), 276953624)

    def test0057(self):
        self.assertEquals(self.calculate(-44069630, 28569), -599841742)

    def test0058(self):
        self.assertEquals(self.calculate(1730367380, 298), 253403720)

    def test0059(self):
        self.assertEquals(self.calculate(-467681801, 10608), -481318128)

    def test0060(self):
        self.assertEquals(self.calculate(624679036, 8025), 822429468)

    def test0061(self):
        self.assertEquals(self.calculate(-826845011, 14703), 1950218243)

    def test0062(self):
        self.assertEquals(self.calculate(1249708012, -17174), -533819976)

    def test0063(self):
        self.assertEquals(self.calculate(1487144216, 21422), 1830960720)

    def test0064(self):
        self.assertEquals(self.calculate(1361445011, 14824), 9519160)

    def test0065(self):
        self.assertEquals(self.calculate(-2054604778, 25042), -1999611892)

    def test0066(self):
        self.assertEquals(self.calculate(-2122255430, 23785), 905227338)

    def test0067(self):
        self.assertEquals(self.calculate(-557105719, 29200), 1849122448)

    def test0068(self):
        self.assertEquals(self.calculate(1564497592, 27053), 1745621592)

    def test0069(self):
        self.assertEquals(self.calculate(-1432908380, 27013), -908797388)

    def test0070(self):
        self.assertEquals(self.calculate(927227158, 1292), -318387448)

    def test0071(self):
        self.assertEquals(self.calculate(255296558, -20675), 258470134)

    def test0072(self):
        self.assertEquals(self.calculate(11230216, -15911), 1704659656)

    def test0073(self):
        self.assertEquals(self.calculate(900398888, -2079), 676452904)

    def test0074(self):
        self.assertEquals(self.calculate(-2034424984, -22026), 850898416)

    def test0075(self):
        self.assertEquals(self.calculate(-1811972802, -16194), -129010684)

    def test0076(self):
        self.assertEquals(self.calculate(621249686, 13702), -261983100)

    def test0077(self):
        self.assertEquals(self.calculate(-1561517469, -31559), -524950133)

    def test0078(self):
        self.assertEquals(self.calculate(1929395143, 5641), 270873599)

    def test0079(self):
        self.assertEquals(self.calculate(-1490878245, -5662), 1741886550)

    def test0080(self):
        self.assertEquals(self.calculate(-470473072, -19955), -508357296)

    def test0081(self):
        self.assertEquals(self.calculate(1871558306, -926), 2103796228)

    def test0082(self):
        self.assertEquals(self.calculate(1195444943, 27796), -1574333524)

    def test0083(self):
        self.assertEquals(self.calculate(479815858, -3751), -197986334)

    def test0084(self):
        self.assertEquals(self.calculate(744985189, -23647), 1291083909)

    def test0085(self):
        self.assertEquals(self.calculate(1857125332, -4252), 1947945680)

    def test0086(self):
        self.assertEquals(self.calculate(-127786211, 22873), 2018724373)

    def test0087(self):
        self.assertEquals(self.calculate(-157082367, -14180), -1660062564)

    def test0088(self):
        self.assertEquals(self.calculate(369809863, 25188), -1013235780)

    def test0089(self):
        self.assertEquals(self.calculate(2021475125, 4072), -2005597432)

    def test0090(self):
        self.assertEquals(self.calculate(408407188, -26043), -1809372188)

    def test0091(self):
        self.assertEquals(self.calculate(227440668, 217), 2109984700)

    def test0092(self):
        self.assertEquals(self.calculate(902902321, -23444), -2043178836)

    def test0093(self):
        self.assertEquals(self.calculate(-1300446382, -10168), -1265492208)

    def test0094(self):
        self.assertEquals(self.calculate(-1115896955, 18187), -1097446985)

    def test0095(self):
        self.assertEquals(self.calculate(-1508560220, -22201), -609529988)

    def test0096(self):
        self.assertEquals(self.calculate(1570382210, 22229), -1468035798)

    def test0097(self):
        self.assertEquals(self.calculate(-1472370753, -26841), 1909290777)

    def test0098(self):
        self.assertEquals(self.calculate(-1963377030, 5620), -407925176)

    def test0099(self):
        self.assertEquals(self.calculate(-2133859025, 7912), 423834776)

    def test0100(self):
        self.assertEquals(self.calculate(-1082438538, -10326), 1755439196)

    def test0101(self):
        self.assertEquals(self.calculate(1533381475, -9284), 1902972340)

    def test0102(self):
        self.assertEquals(self.calculate(-1217657311, -23674), -1001310138)

    def test0103(self):
        self.assertEquals(self.calculate(1703373786, -14452), 1594585400)

    def test0104(self):
        self.assertEquals(self.calculate(1216619353, -25870), -422317022)

    def test0105(self):
        self.assertEquals(self.calculate(-782240983, -22358), 237068602)

    def test0106(self):
        self.assertEquals(self.calculate(1598006745, 16458), 1910255802)

    def test0107(self):
        self.assertEquals(self.calculate(-519599563, -21118), -737869846)

    def test0108(self):
        self.assertEquals(self.calculate(-598990791, 17461), -732835891)

    def test0109(self):
        self.assertEquals(self.calculate(489373993, 22190), 1531580382)

    def test0110(self):
        self.assertEquals(self.calculate(-1670595838, -8314), -590438132)

    def test0111(self):
        self.assertEquals(self.calculate(-1886362800, -25101), 1873171696)

    def test0112(self):
        self.assertEquals(self.calculate(-1686906295, -25774), 368909922)

    def test0113(self):
        self.assertEquals(self.calculate(-1874103082, 1053), -2040556482)

    def test0114(self):
        self.assertEquals(self.calculate(-685396872, -31241), 2071707592)

    def test0115(self):
        self.assertEquals(self.calculate(-803128095, 26008), -1329534312)

    def test0116(self):
        self.assertEquals(self.calculate(664831940, -20452), 723622256)

    def test0117(self):
        self.assertEquals(self.calculate(1081454119, 23577), -1777072689)

    def test0118(self):
        self.assertEquals(self.calculate(219944496, 17957), -1826597648)

    def test0119(self):
        self.assertEquals(self.calculate(-1746204894, -30110), -760279292)

    def test0120(self):
        self.assertEquals(self.calculate(1649160126, 15511), -702500590)

    def test0121(self):
        self.assertEquals(self.calculate(415515307, 17733), -1830940905)

    def test0122(self):
        self.assertEquals(self.calculate(-855387272, -20395), -533743912)

    def test0123(self):
        self.assertEquals(self.calculate(-84220485, 24157), 1300242159)

    def test0124(self):
        self.assertEquals(self.calculate(-926252989, -6608), 351354512)

    def test0125(self):
        self.assertEquals(self.calculate(1084347585, -22589), -129108477)

    def test0126(self):
        self.assertEquals(self.calculate(-1866325414, 8761), 63543818)

    def test0127(self):
        self.assertEquals(self.calculate(514814613, -5899), -349523815)

    def test0128(self):
        self.assertEquals(self.calculate(165010685, 32424), -1222800376)

    def test0129(self):
        self.assertEquals(self.calculate(847589487, -13886), -1417225442)

    def test0130(self):
        self.assertEquals(self.calculate(1211364331, 1221), 1607098327)

    def test0131(self):
        self.assertEquals(self.calculate(993077911, -19018), -1384510886)

    def test0132(self):
        self.assertEquals(self.calculate(241458507, 25085), 1082760735)

    def test0133(self):
        self.assertEquals(self.calculate(38744432, 26088), 1447427456)

    def test0134(self):
        self.assertEquals(self.calculate(416081876, 16126), 997416024)

    def test0135(self):
        self.assertEquals(self.calculate(310563619, -6625), -194641091)

    def test0136(self):
        self.assertEquals(self.calculate(1243187586, -11719), -386252302)

    def test0137(self):
        self.assertEquals(self.calculate(706904862, 1182), -1957075836)

    def test0138(self):
        self.assertEquals(self.calculate(-1624771550, -28884), -1206193192)

    def test0139(self):
        self.assertEquals(self.calculate(-1575654863, -26733), 1237180707)

    def test0140(self):
        self.assertEquals(self.calculate(-1846055832, 8522), 377404944)

    def test0141(self):
        self.assertEquals(self.calculate(-1768548090, -16885), -973109438)

    def test0142(self):
        self.assertEquals(self.calculate(1402097882, -26791), 179614154)

    def test0143(self):
        self.assertEquals(self.calculate(1314565936, -23201), -681512240)

    def test0144(self):
        self.assertEquals(self.calculate(-411342910, -16213), -981610858)

    def test0145(self):
        self.assertEquals(self.calculate(1870111111, -15121), 114567433)

    def test0146(self):
        self.assertEquals(self.calculate(-928525492, -9495), -1218312148)

    def test0147(self):
        self.assertEquals(self.calculate(-1101529906, 7742), 1760517604)

    def test0148(self):
        self.assertEquals(self.calculate(936828648, -24502), -1870303472)

    def test0149(self):
        self.assertEquals(self.calculate(715066626, -29563), 314366474)

    def test0150(self):
        self.assertEquals(self.calculate(-720602440, 13180), -1367467744)

    def test0151(self):
        self.assertEquals(self.calculate(-799947500, 30796), 749199856)

    def test0152(self):
        self.assertEquals(self.calculate(-218293845, 30017), 1593748331)

    def test0153(self):
        self.assertEquals(self.calculate(-1941090106, 16055), 81047946)

    def test0154(self):
        self.assertEquals(self.calculate(-1979062821, 31970), -1475149994)

    def test0155(self):
        self.assertEquals(self.calculate(1742740017, 2402), -1531592766)

    def test0156(self):
        self.assertEquals(self.calculate(-472813408, 26100), -988907392)

    def test0157(self):
        self.assertEquals(self.calculate(2103930556, 3140), 682244592)

    def test0158(self):
        self.assertEquals(self.calculate(-703205475, -26415), -560933075)

    def test0159(self):
        self.assertEquals(self.calculate(-1646384708, -26157), -1152269836)

    def test0160(self):
        self.assertEquals(self.calculate(-984517342, -6176), -1294586944)

    def test0161(self):
        self.assertEquals(self.calculate(-689059304, -12040), -1602795712)

    def test0162(self):
        self.assertEquals(self.calculate(1474921137, 12600), -317163592)

    def test0163(self):
        self.assertEquals(self.calculate(-525208735, -15030), -262602998)

    def test0164(self):
        self.assertEquals(self.calculate(421240481, -16936), -188107560)

    def test0165(self):
        self.assertEquals(self.calculate(136157658, 28872), 1248825936)

    def test0166(self):
        self.assertEquals(self.calculate(1367494367, 15548), 1714302916)

    def test0167(self):
        self.assertEquals(self.calculate(-795384987, 31315), -965518401)

    def test0168(self):
        self.assertEquals(self.calculate(-1411745548, 16200), 422973600)

    def test0169(self):
        self.assertEquals(self.calculate(-438874131, -2972), -1336140652)

    def test0170(self):
        self.assertEquals(self.calculate(-73084177, -20397), 344306557)

    def test0171(self):
        self.assertEquals(self.calculate(786892765, -16804), 1258281324)

    def test0172(self):
        self.assertEquals(self.calculate(-716478307, -29184), 1802114560)

    def test0173(self):
        self.assertEquals(self.calculate(2066191731, -15694), 190058486)

    def test0174(self):
        self.assertEquals(self.calculate(1476983457, 28433), -1119587407)

    def test0175(self):
        self.assertEquals(self.calculate(964671492, 3751), 2120303260)

    def test0176(self):
        self.assertEquals(self.calculate(1860204519, 18410), -1704023514)

    def test0177(self):
        self.assertEquals(self.calculate(2042792232, -29029), 397753144)

    def test0178(self):
        self.assertEquals(self.calculate(222686640, 21808), -1257766656)

    def test0179(self):
        self.assertEquals(self.calculate(-1024360510, -31549), -2079172410)

    def test0180(self):
        self.assertEquals(self.calculate(973258243, -31091), -1527432793)

    def test0181(self):
        self.assertEquals(self.calculate(1275069810, 22615), -706672194)

    def test0182(self):
        self.assertEquals(self.calculate(-1598012653, -25037), 1822430921)

    def test0183(self):
        self.assertEquals(self.calculate(-283144685, 1906), 1492109686)

    def test0184(self):
        self.assertEquals(self.calculate(1775607456, 30696), 911483136)

    def test0185(self):
        self.assertEquals(self.calculate(1625917946, -17732), 1338439576)

    def test0186(self):
        self.assertEquals(self.calculate(1425859034, -22606), 760233876)

    def test0187(self):
        self.assertEquals(self.calculate(-498229080, 30532), 843891872)

    def test0188(self):
        self.assertEquals(self.calculate(-966552007, -15693), -1723843621)

    def test0189(self):
        self.assertEquals(self.calculate(-1695407188, 25712), 1608436544)

    def test0190(self):
        self.assertEquals(self.calculate(-1219710509, -14126), -1778141418)

    def test0191(self):
        self.assertEquals(self.calculate(662630843, -26254), -2092603322)

    def test0192(self):
        self.assertEquals(self.calculate(-1099587513, 16438), -1797157126)

    def test0193(self):
        self.assertEquals(self.calculate(1833295401, 7360), -1733092672)

    def test0194(self):
        self.assertEquals(self.calculate(-1289445275, 29621), 485672553)

    def test0195(self):
        self.assertEquals(self.calculate(-561471157, 446), -1308032854)

    def test0196(self):
        self.assertEquals(self.calculate(1175620513, -5520), 270352496)

    def test0197(self):
        self.assertEquals(self.calculate(1938853457, 15037), 301427661)

    def test0198(self):
        self.assertEquals(self.calculate(1937854785, -6854), -2017817158)

    def test0199(self):
        self.assertEquals(self.calculate(1687407392, -31329), 1966262496)

    def test0200(self):
        self.assertEquals(self.calculate(-1503615774, 3213), 720726138)

    def test0201(self):
        self.assertEquals(self.calculate(-1100256134, 13640), -877935536)

    def test0202(self):
        self.assertEquals(self.calculate(-1661710928, 457), 807317296)

    def test0203(self):
        self.assertEquals(self.calculate(-1213718315, 26556), -2068983956)

    def test0204(self):
        self.assertEquals(self.calculate(-1154682074, -9529), -740729206)

    def test0205(self):
        self.assertEquals(self.calculate(1849799518, -7432), 480296720)

    def test0206(self):
        self.assertEquals(self.calculate(-573928450, -24138), -2079570796)

    def test0207(self):
        self.assertEquals(self.calculate(1279894036, 3276), 1044781040)

    def test0208(self):
        self.assertEquals(self.calculate(-974483127, 11180), 1610670092)

    def test0209(self):
        self.assertEquals(self.calculate(-1161763504, 28118), 1055047904)

    def test0210(self):
        self.assertEquals(self.calculate(-477128173, -13416), 1650297928)

    def test0211(self):
        self.assertEquals(self.calculate(-296171687, 7296), -500078464)

    def test0212(self):
        self.assertEquals(self.calculate(-640312262, 19612), 680291160)

    def test0213(self):
        self.assertEquals(self.calculate(-949133465, -22838), -389869242)

    def test0214(self):
        self.assertEquals(self.calculate(-2052890584, 3037), 1663810184)

    def test0215(self):
        self.assertEquals(self.calculate(890684154, 1193), 1729273610)

    def test0216(self):
        self.assertEquals(self.calculate(1072578286, 19673), -341704770)

    def test0217(self):
        self.assertEquals(self.calculate(1173548669, 30906), -1303650606)

    def test0218(self):
        self.assertEquals(self.calculate(865211419, 12821), -1024922569)

    def test0219(self):
        self.assertEquals(self.calculate(-1343024468, -29490), 1898124904)

    def test0220(self):
        self.assertEquals(self.calculate(-720371304, -12296), 1462989632)

    def test0221(self):
        self.assertEquals(self.calculate(-474918016, -9159), -1027762304)

    def test0222(self):
        self.assertEquals(self.calculate(1412654110, -22450), -46255836)

    def test0223(self):
        self.assertEquals(self.calculate(-410859721, 28848), 1628505552)

    def test0224(self):
        self.assertEquals(self.calculate(2011894308, 25887), 1134519900)

    def test0225(self):
        self.assertEquals(self.calculate(-2115425868, -30010), 18696504)

    def test0226(self):
        self.assertEquals(self.calculate(283923125, -24964), -1160854100)

    def test0227(self):
        self.assertEquals(self.calculate(-1859933447, 17528), -2111682376)

    def test0228(self):
        self.assertEquals(self.calculate(1215262382, -9544), -2052474608)

    def test0229(self):
        self.assertEquals(self.calculate(-12053560, -29534), -492444528)

    def test0230(self):
        self.assertEquals(self.calculate(983355209, -25732), -2043897252)

    def test0231(self):
        self.assertEquals(self.calculate(1577567865, 2297), -1279011919)

    def test0232(self):
        self.assertEquals(self.calculate(-1888941872, 24488), 389216384)

    def test0233(self):
        self.assertEquals(self.calculate(650506183, -20530), -1838613726)

    def test0234(self):
        self.assertEquals(self.calculate(-170402364, 16752), 1572850112)

    def test0235(self):
        self.assertEquals(self.calculate(-626353876, -1315), -978373892)

    def test0236(self):
        self.assertEquals(self.calculate(-1403579746, 20377), -557260178)

    def test0237(self):
        self.assertEquals(self.calculate(1415071283, 7584), -1222662432)

    def test0238(self):
        self.assertEquals(self.calculate(1247392008, 12779), 1798834776)

    def test0239(self):
        self.assertEquals(self.calculate(1894416972, -14464), 1044265472)

    def test0240(self):
        self.assertEquals(self.calculate(-1124711181, 12782), -802775830)

    def test0241(self):
        self.assertEquals(self.calculate(706128885, 27473), -888418427)

    def test0242(self):
        self.assertEquals(self.calculate(1811493913, 8392), -2127309944)

    def test0243(self):
        self.assertEquals(self.calculate(1136985855, 287), -102574111)

    def test0244(self):
        self.assertEquals(self.calculate(-58153585, 20842), -856241098)

    def test0245(self):
        self.assertEquals(self.calculate(-467850131, -10618), -1644470514)

    def test0246(self):
        self.assertEquals(self.calculate(1068484604, 18269), -481129844)

    def test0247(self):
        self.assertEquals(self.calculate(2024415101, -31246), 1404089642)

    def test0248(self):
        self.assertEquals(self.calculate(1567403019, 27269), -2001604681)

    def test0249(self):
        self.assertEquals(self.calculate(1363323596, 21099), 1368570692)

    def test0250(self):
        self.assertEquals(self.calculate(-1159794106, 10865), 271084774)

    def test0251(self):
        self.assertEquals(self.calculate(-2119411262, -23894), -746692908)

    def test0252(self):
        self.assertEquals(self.calculate(307211654, 16410), -948363364)

    def test0253(self):
        self.assertEquals(self.calculate(533081582, 3636), 1254381656)

    def test0254(self):
        self.assertEquals(self.calculate(2060653429, -30139), -806596471)

    def test0255(self):
        self.assertEquals(self.calculate(-1838136483, 4266), 1120046018)

    def test0256(self):
        self.assertEquals(self.calculate(404332211, -14608), -904906288)

    def test0257(self):
        self.assertEquals(self.calculate(215903762, -7179), 510086458)

    def test0258(self):
        self.assertEquals(self.calculate(1442887426, 4062), -1621634628)

    def test0259(self):
        self.assertEquals(self.calculate(1074602561, 13111), 1621446391)

    def test0260(self):
        self.assertEquals(self.calculate(-1419099606, 26818), 291976148)

    def test0261(self):
        self.assertEquals(self.calculate(1823756089, 27336), -1783923064)

    def test0262(self):
        self.assertEquals(self.calculate(-1622604710, 1450), 865248708)

    def test0263(self):
        self.assertEquals(self.calculate(2145515653, 22148), -637480300)

    def test0264(self):
        self.assertEquals(self.calculate(539418178, 20222), -1102536324)

    def test0265(self):
        self.assertEquals(self.calculate(-1806248909, 29755), -2010512447)

    def test0266(self):
        self.assertEquals(self.calculate(1907668779, -12861), -1674971967)

    def test0267(self):
        self.assertEquals(self.calculate(995507914, 10801), -2117130070)

    def test0268(self):
        self.assertEquals(self.calculate(-481654661, -824), 1746449432)

    def test0269(self):
        self.assertEquals(self.calculate(-1172506486, 17172), 525306056)

    def test0270(self):
        self.assertEquals(self.calculate(709869768, -21849), -817655176)

    def test0271(self):
        self.assertEquals(self.calculate(2067544782, 16485), -1384729786)

    def test0272(self):
        self.assertEquals(self.calculate(2135590879, 15302), -1594524806)

    def test0273(self):
        self.assertEquals(self.calculate(642738571, -16980), -189036444)

    def test0274(self):
        self.assertEquals(self.calculate(-852996492, -19386), 565904312)

    def test0275(self):
        self.assertEquals(self.calculate(-708716434, -27226), -1774428844)

    def test0276(self):
        self.assertEquals(self.calculate(1503358592, -3869), -1108673664)

    def test0277(self):
        self.assertEquals(self.calculate(-817442596, -14259), -627264980)

    def test0278(self):
        self.assertEquals(self.calculate(-1356263834, -29635), 574764622)

    def test0279(self):
        self.assertEquals(self.calculate(-119125379, 3801), -1823999499)

    def test0280(self):
        self.assertEquals(self.calculate(-1960160651, 21968), 532928528)

    def test0281(self):
        self.assertEquals(self.calculate(-302563369, 32590), 704715906)

    def test0282(self):
        self.assertEquals(self.calculate(1064293355, -16956), 1294450412)

    def test0283(self):
        self.assertEquals(self.calculate(1974377598, 224), -121049536)

    def test0284(self):
        self.assertEquals(self.calculate(-1368843907, -31148), 609667844)

    def test0285(self):
        self.assertEquals(self.calculate(1696390292, -18803), 1495446916)

    def test0286(self):
        self.assertEquals(self.calculate(942622781, -5379), 1988437577)

    def test0287(self):
        self.assertEquals(self.calculate(500421583, 2312), 1628497272)

    def test0288(self):
        self.assertEquals(self.calculate(727315792, 28091), -131514000)

    def test0289(self):
        self.assertEquals(self.calculate(-816586290, 824), 1442762512)

    def test0290(self):
        self.assertEquals(self.calculate(1026041155, -2090), -1237333246)

    def test0291(self):
        self.assertEquals(self.calculate(-628455999, -10470), 44412058)

    def test0292(self):
        self.assertEquals(self.calculate(319783766, -15293), 1514616706)

    def test0293(self):
        self.assertEquals(self.calculate(-1895220043, 8099), 825987647)

    def test0294(self):
        self.assertEquals(self.calculate(1957291784, -32391), -625919288)

    def test0295(self):
        self.assertEquals(self.calculate(-773023958, 28808), 131247696)

    def test0296(self):
        self.assertEquals(self.calculate(57990786, -26772), -2046128936)

    def test0297(self):
        self.assertEquals(self.calculate(-1440170729, -30731), -1751312381)

    def test0298(self):
        self.assertEquals(self.calculate(-481581820, 6104), -1817798816)

    def test0299(self):
        self.assertEquals(self.calculate(-971969068, 6548), 688075408)

    def test0300(self):
        self.assertEquals(self.calculate(1762233720, -13200), 57771136)

    def test0301(self):
        self.assertEquals(self.calculate(1684638588, 16861), 2072503820)

    def test0302(self):
        self.assertEquals(self.calculate(1269770683, -1293), -1135986047)

    def test0303(self):
        self.assertEquals(self.calculate(-392369367, -17856), 1055757376)

    def test0304(self):
        self.assertEquals(self.calculate(1817869388, -28315), -2083645956)

    def test0305(self):
        self.assertEquals(self.calculate(-1191910836, -13019), -229666564)

    def test0306(self):
        self.assertEquals(self.calculate(-910655528, 8791), 246293096)

    def test0307(self):
        self.assertEquals(self.calculate(-818142003, 23127), -1839164501)

    def test0308(self):
        self.assertEquals(self.calculate(-1550652356, 18294), 624789416)

    def test0309(self):
        self.assertEquals(self.calculate(1123760139, -19039), -2037185045)

    def test0310(self):
        self.assertEquals(self.calculate(553053607, 6213), 148223491)

    def test0311(self):
        self.assertEquals(self.calculate(-890137355, -4327), -961329427)

    def test0312(self):
        self.assertEquals(self.calculate(318232393, 24550), 59736726)

    def test0313(self):
        self.assertEquals(self.calculate(-1190764332, -2829), 1417935164)

    def test0314(self):
        self.assertEquals(self.calculate(562615071, -3478), 1729870038)

    def test0315(self):
        self.assertEquals(self.calculate(1517992731, 2802), 1398009222)

    def test0316(self):
        self.assertEquals(self.calculate(-161353965, 7329), -1447203085)

    def test0317(self):
        self.assertEquals(self.calculate(878044664, -21916), -1773370144)

    def test0318(self):
        self.assertEquals(self.calculate(-44265743, 29422), -1011599858)

    def test0319(self):
        self.assertEquals(self.calculate(-960131062, -4402), 249115660)

    def test0320(self):
        self.assertEquals(self.calculate(-846413266, -28270), 840223804)

    def test0321(self):
        self.assertEquals(self.calculate(744362422, -32313), -766084486)

    def test0322(self):
        self.assertEquals(self.calculate(1264610856, -29723), 1525301704)

    def test0323(self):
        self.assertEquals(self.calculate(1447607139, 2354), 1758139478)

    def test0324(self):
        self.assertEquals(self.calculate(1519524947, -24986), 660570898)

    def test0325(self):
        self.assertEquals(self.calculate(646625238, -538), 7972932)

    def test0326(self):
        self.assertEquals(self.calculate(1432750039, -11796), -23150284)

    def test0327(self):
        self.assertEquals(self.calculate(70512137, -31448), -1262559640)

    def test0328(self):
        self.assertEquals(self.calculate(1302869862, -16010), 1709666052)

    def test0329(self):
        self.assertEquals(self.calculate(-435109232, 25290), -206264928)

    def test0330(self):
        self.assertEquals(self.calculate(1548231881, 17784), -1279562952)

    def test0331(self):
        self.assertEquals(self.calculate(100300523, -18593), -871817675)

    def test0332(self):
        self.assertEquals(self.calculate(-1091174200, -4459), -652188568)

    def test0333(self):
        self.assertEquals(self.calculate(-1924874670, -14732), 1879550248)

    def test0334(self):
        self.assertEquals(self.calculate(-1577888948, 23937), 14652748)

    def test0335(self):
        self.assertEquals(self.calculate(-1803727054, -13655), -1744520190)

    def test0336(self):
        self.assertEquals(self.calculate(-1264815889, 1898), 266161142)

    def test0337(self):
        self.assertEquals(self.calculate(-1314792292, 1165), 1570304492)

    def test0338(self):
        self.assertEquals(self.calculate(1647465994, -30859), 374773906)

    def test0339(self):
        self.assertEquals(self.calculate(-1456848803, 5254), -651889490)

    def test0340(self):
        self.assertEquals(self.calculate(-2075687776, -5240), 1746752768)

    def test0341(self):
        self.assertEquals(self.calculate(598930499, -13594), 1396789810)

    def test0342(self):
        self.assertEquals(self.calculate(348594269, -7709), 1336307575)

    def test0343(self):
        self.assertEquals(self.calculate(-661058358, -1631), 149390602)

    def test0344(self):
        self.assertEquals(self.calculate(-719165655, -18501), -524899853)

    def test0345(self):
        self.assertEquals(self.calculate(398805021, 5068), -1785749988)

    def test0346(self):
        self.assertEquals(self.calculate(771978861, -9654), -915665534)

    def test0347(self):
        self.assertEquals(self.calculate(-954925234, -27472), 45784480)

    def test0348(self):
        self.assertEquals(self.calculate(-679123316, -24127), -91989108)

    def test0349(self):
        self.assertEquals(self.calculate(-1149477042, -22495), 1782937870)

    def test0350(self):
        self.assertEquals(self.calculate(801410872, 30728), -1589200448)

    def test0351(self):
        self.assertEquals(self.calculate(531060888, 15139), -447994680)

    def test0352(self):
        self.assertEquals(self.calculate(1183840033, -6638), 1460012626)

    def test0353(self):
        self.assertEquals(self.calculate(1799493750, 20594), 1796457612)

    def test0354(self):
        self.assertEquals(self.calculate(-502955866, -19506), 951818132)

    def test0355(self):
        self.assertEquals(self.calculate(-1899571488, -28753), -720108768)

    def test0356(self):
        self.assertEquals(self.calculate(-2077658586, 25870), -1806877676)

    def test0357(self):
        self.assertEquals(self.calculate(-1733828282, 6958), 585948308)

    def test0358(self):
        self.assertEquals(self.calculate(-1765861987, -31864), -940191128)

    def test0359(self):
        self.assertEquals(self.calculate(518542884, 28613), -2044467788)

    def test0360(self):
        self.assertEquals(self.calculate(-1791954892, -26510), -1909074136)

    def test0361(self):
        self.assertEquals(self.calculate(-234352147, 9285), 1588734177)

    def test0362(self):
        self.assertEquals(self.calculate(-14151819, -1279), 920307317)

    def test0363(self):
        self.assertEquals(self.calculate(-740394283, 24325), -1293061847)

    def test0364(self):
        self.assertEquals(self.calculate(1079600261, -19005), -744187313)

    def test0365(self):
        self.assertEquals(self.calculate(1622719667, 7275), -1579519279)

    def test0366(self):
        self.assertEquals(self.calculate(477337794, -29290), -1105437780)

    def test0367(self):
        self.assertEquals(self.calculate(227073023, 12147), 887006349)

    def test0368(self):
        self.assertEquals(self.calculate(328621910, -5032), -63042160)

    def test0369(self):
        self.assertEquals(self.calculate(-1768094836, 8168), -2118571296)

    def test0370(self):
        self.assertEquals(self.calculate(-1115066942, -12234), 912836332)

    def test0371(self):
        self.assertEquals(self.calculate(63811093, -30759), 34644685)

    def test0372(self):
        self.assertEquals(self.calculate(486125352, 29056), -1289208832)

    def test0373(self):
        self.assertEquals(self.calculate(1416497178, -15649), -438123866)

    def test0374(self):
        self.assertEquals(self.calculate(2073144288, 17446), 155648832)

    def test0375(self):
        self.assertEquals(self.calculate(1772927240, -26304), -323220992)

    def test0376(self):
        self.assertEquals(self.calculate(-174343395, -16849), -245768109)

    def test0377(self):
        self.assertEquals(self.calculate(1964890915, -22676), 124340164)

    def test0378(self):
        self.assertEquals(self.calculate(183628076, -8415), 957967020)

    def test0379(self):
        self.assertEquals(self.calculate(-1540720715, -13021), -67809601)

    def test0380(self):
        self.assertEquals(self.calculate(1818195400, -10069), 2036100248)

    def test0381(self):
        self.assertEquals(self.calculate(1367236551, -27591), -725917873)

    def test0382(self):
        self.assertEquals(self.calculate(-1812779346, -19925), -1046490310)

    def test0383(self):
        self.assertEquals(self.calculate(1724759212, 23530), 438278456)

    def test0384(self):
        self.assertEquals(self.calculate(1733491622, -10378), 1441949828)

    def test0385(self):
        self.assertEquals(self.calculate(892490066, 9303), 663300830)

    def test0386(self):
        self.assertEquals(self.calculate(-2056606946, 15931), -1794722838)

    def test0387(self):
        self.assertEquals(self.calculate(-1034753550, 13188), -1218718008)

    def test0388(self):
        self.assertEquals(self.calculate(260597313, 19587), 1898422083)

    def test0389(self):
        self.assertEquals(self.calculate(749748389, 13373), 1931537233)

    def test0390(self):
        self.assertEquals(self.calculate(-818651235, -30402), -700633850)

    def test0391(self):
        self.assertEquals(self.calculate(-920787641, -12965), -1997317315)

    def test0392(self):
        self.assertEquals(self.calculate(-43105444, 27731), -1356159276)

    def test0393(self):
        self.assertEquals(self.calculate(-1252860315, -26228), -774439876)

    def test0394(self):
        self.assertEquals(self.calculate(2117103356, -7028), -1235672624)

    def test0395(self):
        self.assertEquals(self.calculate(-1238888985, -25161), -1186882783)

    def test0396(self):
        self.assertEquals(self.calculate(-1419792854, -15371), 907127858)

    def test0397(self):
        self.assertEquals(self.calculate(-1985839716, -26641), -651278172)

    def test0398(self):
        self.assertEquals(self.calculate(1738200869, -31733), 1936806551)

    def test0399(self):
        self.assertEquals(self.calculate(-658902633, -5944), -492923400)

    def test0400(self):
        self.assertEquals(self.calculate(1391888870, -22924), -348413896)

    def test0401(self):
        self.assertEquals(self.calculate(1652115576, -25763), -327681128)

    def test0402(self):
        self.assertEquals(self.calculate(1724088391, -2419), -156573413)

    def test0403(self):
        self.assertEquals(self.calculate(1612093272, 24178), 362919216)

    def test0404(self):
        self.assertEquals(self.calculate(-1447843776, -28836), -1353959680)

    def test0405(self):
        self.assertEquals(self.calculate(2100040277, 28319), -1371543349)

    def test0406(self):
        self.assertEquals(self.calculate(674949457, 20845), -991430531)

    def test0407(self):
        self.assertEquals(self.calculate(-1876377757, 15862), 1019379746)

    def test0408(self):
        self.assertEquals(self.calculate(-438737044, 24295), 992344692)

    def test0409(self):
        self.assertEquals(self.calculate(-408448202, -13970), -1990154444)

    def test0410(self):
        self.assertEquals(self.calculate(-2092923776, -27105), 770902912)

    def test0411(self):
        self.assertEquals(self.calculate(-1637867825, 23532), 730856404)

    def test0412(self):
        self.assertEquals(self.calculate(245385597, -12448), -838164000)

    def test0413(self):
        self.assertEquals(self.calculate(2005025378, 29888), -1480183424)

    def test0414(self):
        self.assertEquals(self.calculate(1491915378, -24397), 1588356534)

    def test0415(self):
        self.assertEquals(self.calculate(-1546252896, 26488), -338574592)

    def test0416(self):
        self.assertEquals(self.calculate(-250884262, 26866), -1452895468)

    def test0417(self):
        self.assertEquals(self.calculate(2050092131, 3228), -847204268)

    def test0418(self):
        self.assertEquals(self.calculate(-691622014, -12794), 979417356)

    def test0419(self):
        self.assertEquals(self.calculate(-1610043118, -9966), -308103868)

    def test0420(self):
        self.assertEquals(self.calculate(-2047163034, 2167), 498922090)

    def test0421(self):
        self.assertEquals(self.calculate(-1733000859, 15462), 641677886)

    def test0422(self):
        self.assertEquals(self.calculate(2020450569, -9534), -47402286)

    def test0423(self):
        self.assertEquals(self.calculate(-756419537, -30097), -1662831007)

    def test0424(self):
        self.assertEquals(self.calculate(127633504, -28709), -623162848)

    def test0425(self):
        self.assertEquals(self.calculate(-638559641, 20848), 1707222032)

    def test0426(self):
        self.assertEquals(self.calculate(2030994818, -7684), 1746972152)

    def test0427(self):
        self.assertEquals(self.calculate(-331510214, -14098), 706578924)

    def test0428(self):
        self.assertEquals(self.calculate(-769669596, 12672), 617608704)

    def test0429(self):
        self.assertEquals(self.calculate(-1719788849, -1890), -889318462)

    def test0430(self):
        self.assertEquals(self.calculate(-930708244, 23488), 908301568)

    def test0431(self):
        self.assertEquals(self.calculate(-1858808992, 23881), -1730533792)

    def test0432(self):
        self.assertEquals(self.calculate(1723158837, 4028), 216645100)

    def test0433(self):
        self.assertEquals(self.calculate(1586109433, 2659), -192902325)

    def test0434(self):
        self.assertEquals(self.calculate(65761294, 2477), -318032010)

    def test0435(self):
        self.assertEquals(self.calculate(1690977198, 19432), -1725870160)

    def test0436(self):
        self.assertEquals(self.calculate(-1082676825, -21744), 1009133424)

    def test0437(self):
        self.assertEquals(self.calculate(-1429297580, 16932), 1274088400)

    def test0438(self):
        self.assertEquals(self.calculate(2115103163, -24569), -1160297443)

    def test0439(self):
        self.assertEquals(self.calculate(-566608949, -20253), -621570815)

    def test0440(self):
        self.assertEquals(self.calculate(-1325941104, 19452), -927742528)

    def test0441(self):
        self.assertEquals(self.calculate(-1571913709, -10862), 1631705558)

    def test0442(self):
        self.assertEquals(self.calculate(-2036425194, 13676), -1583005880)

    def test0443(self):
        self.assertEquals(self.calculate(-395797629, -25984), -2041081984)

    def test0444(self):
        self.assertEquals(self.calculate(-810093666, -19206), -2007564212)

    def test0445(self):
        self.assertEquals(self.calculate(-871222696, 3513), 1706351000)

    def test0446(self):
        self.assertEquals(self.calculate(844889382, -4339), 1927042286)

    def test0447(self):
        self.assertEquals(self.calculate(221306907, 27620), 758309132)

    def test0448(self):
        self.assertEquals(self.calculate(-417498398, 21251), 1143977638)

    def test0449(self):
        self.assertEquals(self.calculate(1901127277, 9468), -334878900)

    def test0450(self):
        self.assertEquals(self.calculate(2147184247, 18816), -1338561920)

    def test0451(self):
        self.assertEquals(self.calculate(116391262, -31978), 1776869396)

    def test0452(self):
        self.assertEquals(self.calculate(-632142351, 4977), 2038547041)

    def test0453(self):
        self.assertEquals(self.calculate(-1825119448, 24061), 1841563272)

    def test0454(self):
        self.assertEquals(self.calculate(2061773960, -31850), -1745637456)

    def test0455(self):
        self.assertEquals(self.calculate(1422644100, -9202), -110689992)

    def test0456(self):
        self.assertEquals(self.calculate(58986505, 9020), -517669604)

    def test0457(self):
        self.assertEquals(self.calculate(1915850553, 13219), -1793684405)

    def test0458(self):
        self.assertEquals(self.calculate(127850166, -19906), 1930202132)

    def test0459(self):
        self.assertEquals(self.calculate(-56676636, -25136), -1305219776)

    def test0460(self):
        self.assertEquals(self.calculate(57018852, 18154), 33120872)

    def test0461(self):
        self.assertEquals(self.calculate(-1368571337, -24091), 2083115571)

    def test0462(self):
        self.assertEquals(self.calculate(2032918114, -80), 575308128)

    def test0463(self):
        self.assertEquals(self.calculate(963795318, 8802), 765979436)

    def test0464(self):
        self.assertEquals(self.calculate(1589405917, -19630), -1395712566)

    def test0465(self):
        self.assertEquals(self.calculate(652632345, -1260), -1978001164)

    def test0466(self):
        self.assertEquals(self.calculate(687597711, 27926), -945103030)

    def test0467(self):
        self.assertEquals(self.calculate(2131600850, 16702), 1013480156)

    def test0468(self):
        self.assertEquals(self.calculate(1575101703, -7734), -1309319546)

    def test0469(self):
        self.assertEquals(self.calculate(-1664692279, -10182), 1955834762)

    def test0470(self):
        self.assertEquals(self.calculate(-2099080764, 3246), -1798028488)

    def test0471(self):
        self.assertEquals(self.calculate(619885489, -26721), 1728709103)

    def test0472(self):
        self.assertEquals(self.calculate(1467678358, -23534), -215482740)

    def test0473(self):
        self.assertEquals(self.calculate(1215296374, -17077), -334204526)

    def test0474(self):
        self.assertEquals(self.calculate(455783305, 31871), 690318583)

    def test0475(self):
        self.assertEquals(self.calculate(-1822109156, -26164), -473028016)

    def test0476(self):
        self.assertEquals(self.calculate(369282109, 7816), 90941032)

    def test0477(self):
        self.assertEquals(self.calculate(-737624265, -21466), -1701947862)

    def test0478(self):
        self.assertEquals(self.calculate(1831459712, -3522), 639772928)

    def test0479(self):
        self.assertEquals(self.calculate(-449884538, -3460), 1822340328)

    def test0480(self):
        self.assertEquals(self.calculate(-1257164811, 1646), 880957766)

    def test0481(self):
        self.assertEquals(self.calculate(-1904164070, -27038), 1015147508)

    def test0482(self):
        self.assertEquals(self.calculate(-692874725, 24372), 1068610172)

    def test0483(self):
        self.assertEquals(self.calculate(177654913, -721), 759826607)

    def test0484(self):
        self.assertEquals(self.calculate(1897585808, 21528), 1793322368)

    def test0485(self):
        self.assertEquals(self.calculate(518627787, -10655), 1643839467)

    def test0486(self):
        self.assertEquals(self.calculate(185296110, 1435), -388054502)

    def test0487(self):
        self.assertEquals(self.calculate(-1231145620, 9886), 831717544)

    def test0488(self):
        self.assertEquals(self.calculate(1141115099, -2644), -2041279964)

    def test0489(self):
        self.assertEquals(self.calculate(162447077, 22667), 1400921687)

    def test0490(self):
        self.assertEquals(self.calculate(926189280, -3689), 2081713696)

    def test0491(self):
        self.assertEquals(self.calculate(-504786225, -6369), -1947037679)

    def test0492(self):
        self.assertEquals(self.calculate(-2112019456, 13924), -117829632)

    def test0493(self):
        self.assertEquals(self.calculate(-1738453997, 19660), 1344160548)

    def test0494(self):
        self.assertEquals(self.calculate(-318293454, 32476), 1088069368)

    def test0495(self):
        self.assertEquals(self.calculate(1308884159, -5604), 817314532)

    def test0496(self):
        self.assertEquals(self.calculate(-2019563998, 20952), 112914096)

    def test0497(self):
        self.assertEquals(self.calculate(1690961576, 28333), -345854072)

    def test0498(self):
        self.assertEquals(self.calculate(-498511078, -29889), 756060518)

    def test0499(self):
        self.assertEquals(self.calculate(1597788038, -28247), -1202363018)

    def test0500(self):
        self.assertEquals(self.calculate(-619699869, 29720), -660341432)

    def test0501(self):
        self.assertEquals(self.calculate(1024145237, -6748), -329680012)

    def test0502(self):
        self.assertEquals(self.calculate(1353734549, 23232), -2084466240)

    def test0503(self):
        self.assertEquals(self.calculate(-163739944, -6472), -1132004544)

    def test0504(self):
        self.assertEquals(self.calculate(1464250634, -9308), -1313671064)

    def test0505(self):
        self.assertEquals(self.calculate(-165248113, 11601), -1487944897)

    def test0506(self):
        self.assertEquals(self.calculate(1179956643, 19052), 675135172)

    def test0507(self):
        self.assertEquals(self.calculate(-1038904595, -23859), 968466889)

    def test0508(self):
        self.assertEquals(self.calculate(1367082158, -1076), -2101586776)

    def test0509(self):
        self.assertEquals(self.calculate(-201426533, 17591), 53877197)

    def test0510(self):
        self.assertEquals(self.calculate(-1854989378, -4867), 212046534)

    def test0511(self):
        self.assertEquals(self.calculate(729462038, -10051), -313769666)

    def test0512(self):
        self.assertEquals(self.calculate(1480355011, 26234), 539068142)

    def test0513(self):
        self.assertEquals(self.calculate(-2088157002, -700), 1421020760)

    def test0514(self):
        self.assertEquals(self.calculate(-1888485519, -11894), -1032195094)

    def test0515(self):
        self.assertEquals(self.calculate(-1943827813, -1298), 1942698522)

    def test0516(self):
        self.assertEquals(self.calculate(1453781042, 28713), -372090878)

    def test0517(self):
        self.assertEquals(self.calculate(-32999707, 31735), 726318579)

    def test0518(self):
        self.assertEquals(self.calculate(1075749823, -990), 159564638)

    def test0519(self):
        self.assertEquals(self.calculate(1639200683, 4579), -1702905951)

    def test0520(self):
        self.assertEquals(self.calculate(1785276714, 12468), -1985425016)

    def test0521(self):
        self.assertEquals(self.calculate(245959190, -28255), -319828522)

    def test0522(self):
        self.assertEquals(self.calculate(668521151, 27241), 523339351)

    def test0523(self):
        self.assertEquals(self.calculate(1310965943, -32575), 144230903)

    def test0524(self):
        self.assertEquals(self.calculate(-1994044919, -28793), -587460161)

    def test0525(self):
        self.assertEquals(self.calculate(839572922, -29018), -1672547684)

    def test0526(self):
        self.assertEquals(self.calculate(2017595159, 30034), -1240573858)

    def test0527(self):
        self.assertEquals(self.calculate(1202309248, -7964), -1708748288)

    def test0528(self):
        self.assertEquals(self.calculate(-1108853665, 10251), 1919512597)

    def test0529(self):
        self.assertEquals(self.calculate(592251590, 31754), -1304800324)

    def test0530(self):
        self.assertEquals(self.calculate(77363053, -476), 1829892436)

    def test0531(self):
        self.assertEquals(self.calculate(-405812548, 10354), -1305106504)

    def test0532(self):
        self.assertEquals(self.calculate(1019973276, 6851), -74876716)

    def test0533(self):
        self.assertEquals(self.calculate(-2023713395, 1822), -2123865722)

    def test0534(self):
        self.assertEquals(self.calculate(2080458876, 2244), -79733008)

    def test0535(self):
        self.assertEquals(self.calculate(-327424943, 8111), -1453923745)

    def test0536(self):
        self.assertEquals(self.calculate(771027152, 2191), 1398342704)

    def test0537(self):
        self.assertEquals(self.calculate(-397938631, 30582), -2116863674)

    def test0538(self):
        self.assertEquals(self.calculate(-448565134, -24808), -256419664)

    def test0539(self):
        self.assertEquals(self.calculate(-1414975837, 20331), -182793439)

    def test0540(self):
        self.assertEquals(self.calculate(2106093920, -15917), -477179360)

    def test0541(self):
        self.assertEquals(self.calculate(-117132219, -31891), -1157951391)

    def test0542(self):
        self.assertEquals(self.calculate(492790874, 6518), -624620676)

    def test0543(self):
        self.assertEquals(self.calculate(1978571248, 2208), 703575552)

    def test0544(self):
        self.assertEquals(self.calculate(493376105, 19196), 444823900)

    def test0545(self):
        self.assertEquals(self.calculate(-1532341396, -26448), 53836352)

    def test0546(self):
        self.assertEquals(self.calculate(298097182, 28353), -546237282)

    def test0547(self):
        self.assertEquals(self.calculate(-410949471, -24701), 1855162723)

    def test0548(self):
        self.assertEquals(self.calculate(-966830093, -12275), 844752727)

    def test0549(self):
        self.assertEquals(self.calculate(753038351, 3000), -37744696)

    def test0550(self):
        self.assertEquals(self.calculate(1065612368, 9605), 299728272)

    def test0551(self):
        self.assertEquals(self.calculate(1587394404, 18436), -703922800)

    def test0552(self):
        self.assertEquals(self.calculate(551081686, -30327), -936542586)

    def test0553(self):
        self.assertEquals(self.calculate(-246329033, -1955), 536922363)

    def test0554(self):
        self.assertEquals(self.calculate(-2017509515, -10393), -53949677)

    def test0555(self):
        self.assertEquals(self.calculate(-1875159831, 20084), 1858172820)

    def test0556(self):
        self.assertEquals(self.calculate(-1291017463, 23888), -1959970864)

    def test0557(self):
        self.assertEquals(self.calculate(3804961, 17790), -1029220546)

    def test0558(self):
        self.assertEquals(self.calculate(1347695859, -30291), 608883511)

    def test0559(self):
        self.assertEquals(self.calculate(-1211638186, -5750), 482615388)

    def test0560(self):
        self.assertEquals(self.calculate(-175470285, -27795), -1886276681)

    def test0561(self):
        self.assertEquals(self.calculate(-947986797, 27509), 872622639)

    def test0562(self):
        self.assertEquals(self.calculate(-1108953299, 23619), -1657398073)

    def test0563(self):
        self.assertEquals(self.calculate(-1095312895, 19484), 616047644)

    def test0564(self):
        self.assertEquals(self.calculate(-875915980, -30776), 1975450784)

    def test0565(self):
        self.assertEquals(self.calculate(-424184148, -10007), 1383080588)

    def test0566(self):
        self.assertEquals(self.calculate(-1115070707, 6984), -878110040)

    def test0567(self):
        self.assertEquals(self.calculate(-1716123995, -8798), 1648862570)

    def test0568(self):
        self.assertEquals(self.calculate(1608841162, 22704), -1567110432)

    def test0569(self):
        self.assertEquals(self.calculate(-537488745, 3760), 1971915216)

    def test0570(self):
        self.assertEquals(self.calculate(-2107832183, 15748), 1661012900)

    def test0571(self):
        self.assertEquals(self.calculate(-935117848, -4683), -1709759736)

    def test0572(self):
        self.assertEquals(self.calculate(-88141154, -10915), -11978394)

    def test0573(self):
        self.assertEquals(self.calculate(-918052708, 19122), -1472543624)

    def test0574(self):
        self.assertEquals(self.calculate(-1259448896, -2397), -463005376)

    def test0575(self):
        self.assertEquals(self.calculate(-1452021710, 7768), -720523984)

    def test0576(self):
        self.assertEquals(self.calculate(-1243454460, 3161), -664472220)

    def test0577(self):
        self.assertEquals(self.calculate(286712557, -12080), -1744047984)

    def test0578(self):
        self.assertEquals(self.calculate(-318215763, -18258), -1107350634)

    def test0579(self):
        self.assertEquals(self.calculate(-699274188, 15267), 1469669660)

    def test0580(self):
        self.assertEquals(self.calculate(391269715, -10024), -782481912)

    def test0581(self):
        self.assertEquals(self.calculate(-1392346994, -20312), -1007502032)

    def test0582(self):
        self.assertEquals(self.calculate(-1223572537, 1247), -1081563559)

    def test0583(self):
        self.assertEquals(self.calculate(768765462, 26039), -958701638)

    def test0584(self):
        self.assertEquals(self.calculate(1953231926, 15024), 2139889952)

    def test0585(self):
        self.assertEquals(self.calculate(-148108943, -28696), -1883394712)

    def test0586(self):
        self.assertEquals(self.calculate(-365511920, 31692), -276971328)

    def test0587(self):
        self.assertEquals(self.calculate(-274718582, -11435), 1785891794)

    def test0588(self):
        self.assertEquals(self.calculate(832920582, 22021), -2061184994)

    def test0589(self):
        self.assertEquals(self.calculate(-567329581, -24894), 1250120166)

    def test0590(self):
        self.assertEquals(self.calculate(-1506351034, -2438), 286782812)

    def test0591(self):
        self.assertEquals(self.calculate(759808263, 7432), -986983624)

    def test0592(self):
        self.assertEquals(self.calculate(183263999, -12913), 38961009)

    def test0593(self):
        self.assertEquals(self.calculate(756131362, 6554), -707313036)

    def test0594(self):
        self.assertEquals(self.calculate(145424194, 10190), 108819740)

    def test0595(self):
        self.assertEquals(self.calculate(1052196879, -7349), -1653730971)

    def test0596(self):
        self.assertEquals(self.calculate(-949635322, -18293), -1463766974)

    def test0597(self):
        self.assertEquals(self.calculate(-622992578, -8321), -104284734)

    def test0598(self):
        self.assertEquals(self.calculate(-906077431, 24169), 1052812465)

    def test0599(self):
        self.assertEquals(self.calculate(-876922382, 15799), 1067783678)

    def test0600(self):
        self.assertEquals(self.calculate(294632592, 32740), -225484736)

    def test0601(self):
        self.assertEquals(self.calculate(-1521062026, 13435), -13924942)

    def test0602(self):
        self.assertEquals(self.calculate(-512751989, -13564), 1415926572)

    def test0603(self):
        self.assertEquals(self.calculate(-1628994908, -31400), 1674583136)

    def test0604(self):
        self.assertEquals(self.calculate(-2103656144, -19962), 1288693536)

    def test0605(self):
        self.assertEquals(self.calculate(-1108478116, -8620), -1220873680)

    def test0606(self):
        self.assertEquals(self.calculate(1200518558, 20630), 1916422804)

    def test0607(self):
        self.assertEquals(self.calculate(65838536, 11372), 1391521888)

    def test0608(self):
        self.assertEquals(self.calculate(-1757170667, -18937), -1865688429)

    def test0609(self):
        self.assertEquals(self.calculate(-1131235921, 8676), -602579236)

    def test0610(self):
        self.assertEquals(self.calculate(81141677, -26219), -1444817743)

    def test0611(self):
        self.assertEquals(self.calculate(1175603160, 26160), 1812826240)

    def test0612(self):
        self.assertEquals(self.calculate(-1740683785, -16199), 876334975)

    def test0613(self):
        self.assertEquals(self.calculate(2077374674, 27825), 1280434482)

    def test0614(self):
        self.assertEquals(self.calculate(1339092590, 20942), 1435544196)

    def test0615(self):
        self.assertEquals(self.calculate(-840952262, 5259), 1248369022)

    def test0616(self):
        self.assertEquals(self.calculate(907307265, 27831), 1155759031)

    def test0617(self):
        self.assertEquals(self.calculate(-1059895236, 12608), -1515877632)

    def test0618(self):
        self.assertEquals(self.calculate(-1997083695, -30537), 704158311)

    def test0619(self):
        self.assertEquals(self.calculate(2105326396, 26057), -1127371236)

    def test0620(self):
        self.assertEquals(self.calculate(-797279262, 16443), -1422717674)

    def test0621(self):
        self.assertEquals(self.calculate(1539611033, -4019), 1351131909)

    def test0622(self):
        self.assertEquals(self.calculate(-1755420017, 20988), -525851708)

    def test0623(self):
        self.assertEquals(self.calculate(1484350381, -31933), -501637817)

    def test0624(self):
        self.assertEquals(self.calculate(839851211, 3296), -2104314464)

    def test0625(self):
        self.assertEquals(self.calculate(-1431741289, -14886), 1273105302)

    def test0626(self):
        self.assertEquals(self.calculate(-1612816794, -29505), -2078132710)

    def test0627(self):
        self.assertEquals(self.calculate(1040528776, -23891), -2278168)

    def test0628(self):
        self.assertEquals(self.calculate(-1198041259, -4719), 1379739685)

    def test0629(self):
        self.assertEquals(self.calculate(-337764522, 12108), -843966584)

    def test0630(self):
        self.assertEquals(self.calculate(1152663663, 8637), -178134797)

    def test0631(self):
        self.assertEquals(self.calculate(747337293, 17017), 40551525)

    def test0632(self):
        self.assertEquals(self.calculate(1412618277, 22319), -1127595573)

    def test0633(self):
        self.assertEquals(self.calculate(-148495071, -14765), 2096402355)

    def test0634(self):
        self.assertEquals(self.calculate(-934310413, 4499), 1310434697)

    def test0635(self):
        self.assertEquals(self.calculate(-92569119, -19338), -899739210)

    def test0636(self):
        self.assertEquals(self.calculate(-996440319, 6323), 224886195)

    def test0637(self):
        self.assertEquals(self.calculate(1281459626, 854), -850139876)

    def test0638(self):
        self.assertEquals(self.calculate(-1225784719, 20145), -1666179551)

    def test0639(self):
        self.assertEquals(self.calculate(-224456314, 8529), 1167511910)

    def test0640(self):
        self.assertEquals(self.calculate(-1531333462, 23852), -963850440)

    def test0641(self):
        self.assertEquals(self.calculate(297147032, -16111), 1552702488)

    def test0642(self):
        self.assertEquals(self.calculate(589016340, -7123), 619658372)

    def test0643(self):
        self.assertEquals(self.calculate(282007190, -9639), 446993958)

    def test0644(self):
        self.assertEquals(self.calculate(-1898785057, 5802), -159786474)

    def test0645(self):
        self.assertEquals(self.calculate(-1219598550, -1477), 1755761326)

    def test0646(self):
        self.assertEquals(self.calculate(1304708918, -28094), -1241438228)

    def test0647(self):
        self.assertEquals(self.calculate(-1192569653, -23094), 1873264430)

    def test0648(self):
        self.assertEquals(self.calculate(-793709734, 11687), 1043698102)

    def test0649(self):
        self.assertEquals(self.calculate(-469261341, -24364), -119629828)

    def test0650(self):
        self.assertEquals(self.calculate(-1145729029, 7193), 813335427)

    def test0651(self):
        self.assertEquals(self.calculate(-1890623780, -17709), 1786447700)

    def test0652(self):
        self.assertEquals(self.calculate(-1369026428, 27902), 863736568)

    def test0653(self):
        self.assertEquals(self.calculate(-1030410279, -4372), -466953716)

    def test0654(self):
        self.assertEquals(self.calculate(-937470872, 12141), -170522552)

    def test0655(self):
        self.assertEquals(self.calculate(1537384283, -3325), -791658735)

    def test0656(self):
        self.assertEquals(self.calculate(341560827, 5610), 600825454)

    def test0657(self):
        self.assertEquals(self.calculate(-1939745736, 5190), 122971984)

    def test0658(self):
        self.assertEquals(self.calculate(-1202521122, 3761), -81377154)

    def test0659(self):
        self.assertEquals(self.calculate(779377748, -1060), -1506692048)

    def test0660(self):
        self.assertEquals(self.calculate(-1029700689, 24913), 906393951)

    def test0661(self):
        self.assertEquals(self.calculate(-806316611, -29552), -210069936)

    def test0662(self):
        self.assertEquals(self.calculate(-582128598, 4439), 1501465670)

    def test0663(self):
        self.assertEquals(self.calculate(-366335823, 14817), 840772753)

    def test0664(self):
        self.assertEquals(self.calculate(-276246390, 8603), -1430778482)

    def test0665(self):
        self.assertEquals(self.calculate(221110083, 22218), -818762530)

    def test0666(self):
        self.assertEquals(self.calculate(-1497275053, 13555), -1842869815)

    def test0667(self):
        self.assertEquals(self.calculate(1588987698, 22301), -1760506198)

    def test0668(self):
        self.assertEquals(self.calculate(-1375377154, -26324), -1146103384)

    def test0669(self):
        self.assertEquals(self.calculate(646709637, 31408), 955936112)

    def test0670(self):
        self.assertEquals(self.calculate(-1551572221, -9753), 1314087605)

    def test0671(self):
        self.assertEquals(self.calculate(1486117158, 26752), -1906048256)

    def test0672(self):
        self.assertEquals(self.calculate(1371530818, 8664), -1231500880)

    def test0673(self):
        self.assertEquals(self.calculate(636104194, -1689), -638159666)

    def test0674(self):
        self.assertEquals(self.calculate(855334500, -22233), 1463248188)

    def test0675(self):
        self.assertEquals(self.calculate(-2022798425, -5428), 1813442324)

    def test0676(self):
        self.assertEquals(self.calculate(1073690007, -28069), 380709549)

    def test0677(self):
        self.assertEquals(self.calculate(1940206241, -28231), -244463783)

    def test0678(self):
        self.assertEquals(self.calculate(-257008264, -21618), -1683029872)

    def test0679(self):
        self.assertEquals(self.calculate(1892556935, -4735), -1955307769)

    def test0680(self):
        self.assertEquals(self.calculate(-606798893, 11953), 1132594915)

    def test0681(self):
        self.assertEquals(self.calculate(-314199313, 4864), 742898944)

    def test0682(self):
        self.assertEquals(self.calculate(-2118114088, 23159), -582676376)

    def test0683(self):
        self.assertEquals(self.calculate(-302296623, 10888), -1460682488)

    def test0684(self):
        self.assertEquals(self.calculate(-519985507, 1493), 1050718625)

    def test0685(self):
        self.assertEquals(self.calculate(571218245, 12880), 12017552)

    def test0686(self):
        self.assertEquals(self.calculate(-315681223, -17217), 1949986951)

    def test0687(self):
        self.assertEquals(self.calculate(-1443126404, 20171), 1985637204)

    def test0688(self):
        self.assertEquals(self.calculate(-1909844409, 22987), 1562270029)

    def test0689(self):
        self.assertEquals(self.calculate(335296525, 1101), -205713431)

    def test0690(self):
        self.assertEquals(self.calculate(1857678955, -28190), 566498678)

    def test0691(self):
        self.assertEquals(self.calculate(245836636, 27485), 836383852)

    def test0692(self):
        self.assertEquals(self.calculate(1203431982, -4576), -756676160)

    def test0693(self):
        self.assertEquals(self.calculate(-1137754157, 5810), -396983626)

    def test0694(self):
        self.assertEquals(self.calculate(1637634605, -28063), -789852915)

    def test0695(self):
        self.assertEquals(self.calculate(1218144966, -12615), 494238998)

    def test0696(self):
        self.assertEquals(self.calculate(-1963732078, -26518), 2063747700)

    def test0697(self):
        self.assertEquals(self.calculate(-1420223532, 27773), 1111492228)

    def test0698(self):
        self.assertEquals(self.calculate(1404553952, -19513), -874949600)

    def test0699(self):
        self.assertEquals(self.calculate(-1167060989, 16113), -1486893869)

    def test0700(self):
        self.assertEquals(self.calculate(-345936903, 20611), -459796373)

    def test0701(self):
        self.assertEquals(self.calculate(2088733328, -15990), -1180221024)

    def test0702(self):
        self.assertEquals(self.calculate(-802414392, 3649), 1157579464)

    def test0703(self):
        self.assertEquals(self.calculate(-250420469, -12678), 849874238)

    def test0704(self):
        self.assertEquals(self.calculate(135529257, -3997), -544560933)

    def test0705(self):
        self.assertEquals(self.calculate(1450281860, 14516), -1638205232)

    def test0706(self):
        self.assertEquals(self.calculate(-456761129, -15909), -471863571)

    def test0707(self):
        self.assertEquals(self.calculate(1555429508, 4261), 550595860)

    def test0708(self):
        self.assertEquals(self.calculate(503262949, -13775), -369906731)

    def test0709(self):
        self.assertEquals(self.calculate(2063342873, 10861), -1172406875)

    def test0710(self):
        self.assertEquals(self.calculate(996822581, 13061), 1453856265)

    def test0711(self):
        self.assertEquals(self.calculate(-973320099, 679), 540616363)

    def test0712(self):
        self.assertEquals(self.calculate(392616057, 3656), 885227528)

    def test0713(self):
        self.assertEquals(self.calculate(-685630658, -6544), -1473798368)

    def test0714(self):
        self.assertEquals(self.calculate(-1855530185, 23087), -621570791)

    def test0715(self):
        self.assertEquals(self.calculate(684181988, 4872), 440023840)

    def test0716(self):
        self.assertEquals(self.calculate(1478994175, -27352), 848286424)

    def test0717(self):
        self.assertEquals(self.calculate(-1325396071, -28839), -2111642831)

    def test0718(self):
        self.assertEquals(self.calculate(363447423, 23018), -763509994)

    def test0719(self):
        self.assertEquals(self.calculate(-74535303, -1339), 1018522909)

    def test0720(self):
        self.assertEquals(self.calculate(-1521453708, -21309), -2051053732)

    def test0721(self):
        self.assertEquals(self.calculate(-1227219907, -10803), -907387431)

    def test0722(self):
        self.assertEquals(self.calculate(-908540316, 8873), 175390724)

    def test0723(self):
        self.assertEquals(self.calculate(1561912186, 31625), -945989046)

    def test0724(self):
        self.assertEquals(self.calculate(549892037, 5064), 1514467560)

    def test0725(self):
        self.assertEquals(self.calculate(-739551946, -6359), -178364506)

    def test0726(self):
        self.assertEquals(self.calculate(1405687760, -14766), 1191477408)

    def test0727(self):
        self.assertEquals(self.calculate(-89770580, -29663), -15008980)

    def test0728(self):
        self.assertEquals(self.calculate(1618140971, 3572), -1026432004)

    def test0729(self):
        self.assertEquals(self.calculate(1149375300, -12009), 1176911644)

    def test0730(self):
        self.assertEquals(self.calculate(1114034411, 4708), 718938572)

    def test0731(self):
        self.assertEquals(self.calculate(2123499277, 25452), -564854660)

    def test0732(self):
        self.assertEquals(self.calculate(-1886190575, 11481), -128885143)

    def test0733(self):
        self.assertEquals(self.calculate(153902807, -1872), -343245872)

    def test0734(self):
        self.assertEquals(self.calculate(-129188133, 27372), -1379491868)

    def test0735(self):
        self.assertEquals(self.calculate(-445893102, 22073), 1866601986)

    def test0736(self):
        self.assertEquals(self.calculate(-1011388363, 3673), 317253741)

    def test0737(self):
        self.assertEquals(self.calculate(246918505, -1532), -322027612)

    def test0738(self):
        self.assertEquals(self.calculate(-1646774546, -6022), -203170452)

    def test0739(self):
        self.assertEquals(self.calculate(-1178091352, 20871), 743162008)

    def test0740(self):
        self.assertEquals(self.calculate(-994433334, 16787), 985501694)

    def test0741(self):
        self.assertEquals(self.calculate(-55994225, -23678), -1313634914)

    def test0742(self):
        self.assertEquals(self.calculate(743552152, -2296), -2093724480)

    def test0743(self):
        self.assertEquals(self.calculate(-757825017, -6171), -681205437)

    def test0744(self):
        self.assertEquals(self.calculate(-402430745, -3681), -416144775)

    def test0745(self):
        self.assertEquals(self.calculate(-1658430991, -16730), 61747270)

    def test0746(self):
        self.assertEquals(self.calculate(677370350, 9491), -644050262)

    def test0747(self):
        self.assertEquals(self.calculate(-1845646680, 14549), -178012728)

    def test0748(self):
        self.assertEquals(self.calculate(627565227, 12198), 1408917474)

    def test0749(self):
        self.assertEquals(self.calculate(1004965461, -19520), -1810157888)

    def test0750(self):
        self.assertEquals(self.calculate(393479255, 18419), 1884569493)

    def test0751(self):
        self.assertEquals(self.calculate(-1110154541, -18416), 561698096)

    def test0752(self):
        self.assertEquals(self.calculate(-1917763590, -29163), -1324553342)

    def test0753(self):
        self.assertEquals(self.calculate(1706201364, -6922), 834222392)

    def test0754(self):
        self.assertEquals(self.calculate(-167717089, -11124), 1669091572)

    def test0755(self):
        self.assertEquals(self.calculate(-407627060, 29276), 2024307024)

    def test0756(self):
        self.assertEquals(self.calculate(-620286780, 11067), -1356055252)

    def test0757(self):
        self.assertEquals(self.calculate(-236702324, -8044), 1362982128)

    def test0758(self):
        self.assertEquals(self.calculate(-605188418, -27699), -143366106)

    def test0759(self):
        self.assertEquals(self.calculate(-984492593, -23582), 2006093246)

    def test0760(self):
        self.assertEquals(self.calculate(1175132884, 16395), -919656676)

    def test0761(self):
        self.assertEquals(self.calculate(-514731629, 4679), 1047360965)

    def test0762(self):
        self.assertEquals(self.calculate(1000699910, 167), -386839574)

    def test0763(self):
        self.assertEquals(self.calculate(-767929108, 27863), 718332468)

    def test0764(self):
        self.assertEquals(self.calculate(1591361168, 14948), 2137854016)

    def test0765(self):
        self.assertEquals(self.calculate(-342641308, -11519), -189718172)

    def test0766(self):
        self.assertEquals(self.calculate(2136135155, 11393), 1703121779)

    def test0767(self):
        self.assertEquals(self.calculate(-1487015173, 21963), -382925815)

    def test0768(self):
        self.assertEquals(self.calculate(-521979665, -27711), -871356113)

    def test0769(self):
        self.assertEquals(self.calculate(1135820675, -8948), -1430777564)

    def test0770(self):
        self.assertEquals(self.calculate(-1546365166, 31922), -1009696124)

    def test0771(self):
        self.assertEquals(self.calculate(-1720030928, -31608), 1041539456)

    def test0772(self):
        self.assertEquals(self.calculate(1832471893, -13715), 1796603697)

    def test0773(self):
        self.assertEquals(self.calculate(-139028582, 18540), -609532680)

    def test0774(self):
        self.assertEquals(self.calculate(-1680428017, 24668), -2068949660)

    def test0775(self):
        self.assertEquals(self.calculate(-262364033, 4760), 982686056)

    def test0776(self):
        self.assertEquals(self.calculate(-479355404, -11519), -1633043980)

    def test0777(self):
        self.assertEquals(self.calculate(716985129, -1808), 771010160)

    def test0778(self):
        self.assertEquals(self.calculate(1112375763, 1958), 483324882)

    def test0779(self):
        self.assertEquals(self.calculate(-394733198, 18686), -1525690596)

    def test0780(self):
        self.assertEquals(self.calculate(-1086770006, 17166), 1844010828)

    def test0781(self):
        self.assertEquals(self.calculate(478536171, -6001), 1637558853)

    def test0782(self):
        self.assertEquals(self.calculate(520478382, 21175), 243657314)

    def test0783(self):
        self.assertEquals(self.calculate(-1483854441, 32187), -786560947)

    def test0784(self):
        self.assertEquals(self.calculate(841981580, -770), 214245096)

    def test0785(self):
        self.assertEquals(self.calculate(1644904056, 21016), -888124608)

    def test0786(self):
        self.assertEquals(self.calculate(1511911479, -12094), -1381647954)

    def test0787(self):
        self.assertEquals(self.calculate(-250546983, -23142), -47569014)

    def test0788(self):
        self.assertEquals(self.calculate(-106857108, -26178), 1281663528)

    def test0789(self):
        self.assertEquals(self.calculate(1149767392, -14572), 256985472)

    def test0790(self):
        self.assertEquals(self.calculate(2071291936, 22449), 1116724768)

    def test0791(self):
        self.assertEquals(self.calculate(708029722, -11527), -1020743094)

    def test0792(self):
        self.assertEquals(self.calculate(1924793780, -111), 1096255220)

    def test0793(self):
        self.assertEquals(self.calculate(-1038894948, 3761), 1136339932)

    def test0794(self):
        self.assertEquals(self.calculate(-1739214835, -18734), 828811434)

    def test0795(self):
        self.assertEquals(self.calculate(-1292390448, 10202), 582248224)

    def test0796(self):
        self.assertEquals(self.calculate(-1127132845, -30740), 562478468)

    def test0797(self):
        self.assertEquals(self.calculate(-2038545395, -30993), 1668503075)

    def test0798(self):
        self.assertEquals(self.calculate(-825967826, -3022), 698771196)

    def test0799(self):
        self.assertEquals(self.calculate(-627365062, -8005), 1240552286)

    def test0800(self):
        self.assertEquals(self.calculate(-326767859, 26253), -1586912215)

    def test0801(self):
        self.assertEquals(self.calculate(1715267979, 16621), -523831889)

    def test0802(self):
        self.assertEquals(self.calculate(158525372, 4237), 1657102988)

    def test0803(self):
        self.assertEquals(self.calculate(-1252450203, 9250), -1637580438)

    def test0804(self):
        self.assertEquals(self.calculate(1788873090, -31403), -2104380886)

    def test0805(self):
        self.assertEquals(self.calculate(-190581350, 30508), 1129892984)

    def test0806(self):
        self.assertEquals(self.calculate(1591526002, 20078), 102385916)

    def test0807(self):
        self.assertEquals(self.calculate(325782842, 1457), -2075769062)

    def test0808(self):
        self.assertEquals(self.calculate(-1270183271, -3598), 274206114)

    def test0809(self):
        self.assertEquals(self.calculate(890939115, -6177), -1477807179)

    def test0810(self):
        self.assertEquals(self.calculate(998951379, 32569), 470195451)

    def test0811(self):
        self.assertEquals(self.calculate(1060346437, -16696), 311081960)

    def test0812(self):
        self.assertEquals(self.calculate(757769826, -12343), 1285808370)

    def test0813(self):
        self.assertEquals(self.calculate(745280453, -13339), 1553327673)

    def test0814(self):
        self.assertEquals(self.calculate(-826871988, 7620), -47525328)

    def test0815(self):
        self.assertEquals(self.calculate(922031403, -5444), 1277811092)

    def test0816(self):
        self.assertEquals(self.calculate(-459861147, -8901), 120236359)

    def test0817(self):
        self.assertEquals(self.calculate(-117192565, 31067), 1310850153)

    def test0818(self):
        self.assertEquals(self.calculate(-2082215997, 12074), 2062603006)

    def test0819(self):
        self.assertEquals(self.calculate(-1837742480, 14186), 236665440)

    def test0820(self):
        self.assertEquals(self.calculate(615047062, 12764), -739517720)

    def test0821(self):
        self.assertEquals(self.calculate(-1272660815, 5035), 244002107)

    def test0822(self):
        self.assertEquals(self.calculate(-1851893, -13944), 52992216)

    def test0823(self):
        self.assertEquals(self.calculate(-1556216082, 22726), -1805964268)

    def test0824(self):
        self.assertEquals(self.calculate(353922952, 5240), -869603392)

    def test0825(self):
        self.assertEquals(self.calculate(-1731727476, -8515), 1036730972)

    def test0826(self):
        self.assertEquals(self.calculate(87403509, -6528), 660543616)

    def test0827(self):
        self.assertEquals(self.calculate(-1236400372, 524), 666266768)

    def test0828(self):
        self.assertEquals(self.calculate(-1648312188, 15543), -236417444)

    def test0829(self):
        self.assertEquals(self.calculate(-1431481100, 22696), -1762418656)

    def test0830(self):
        self.assertEquals(self.calculate(-1417234397, 22559), 345789501)

    def test0831(self):
        self.assertEquals(self.calculate(1539121832, 16783), 1148388312)

    def test0832(self):
        self.assertEquals(self.calculate(-2054316163, -20502), 1140669250)

    def test0833(self):
        self.assertEquals(self.calculate(-1417439525, -18872), 862396312)

    def test0834(self):
        self.assertEquals(self.calculate(-1492885931, 32321), -1903572587)

    def test0835(self):
        self.assertEquals(self.calculate(1603900067, -30089), -1496578107)

    def test0836(self):
        self.assertEquals(self.calculate(-422825071, 19019), -1531247237)

    def test0837(self):
        self.assertEquals(self.calculate(-1377757406, 22542), -498928676)

    def test0838(self):
        self.assertEquals(self.calculate(-1920043366, -22474), -481815428)

    def test0839(self):
        self.assertEquals(self.calculate(1127709738, 3975), -1299648474)

    def test0840(self):
        self.assertEquals(self.calculate(-829340958, -24777), 1457372302)

    def test0841(self):
        self.assertEquals(self.calculate(984645304, 2316), -189110112)

    def test0842(self):
        self.assertEquals(self.calculate(-1839497675, 32588), -691682628)

    def test0843(self):
        self.assertEquals(self.calculate(746544951, 23950), -197276798)

    def test0844(self):
        self.assertEquals(self.calculate(953264227, -15741), 1283535017)

    def test0845(self):
        self.assertEquals(self.calculate(-761148515, -17566), 101622042)

    def test0846(self):
        self.assertEquals(self.calculate(-1680222362, 15539), 130909266)

    def test0847(self):
        self.assertEquals(self.calculate(1019062049, -17570), 798456094)

    def test0848(self):
        self.assertEquals(self.calculate(-1383936250, 25594), 130907612)

    def test0849(self):
        self.assertEquals(self.calculate(-814195839, -14653), -1007519421)

    def test0850(self):
        self.assertEquals(self.calculate(-398607635, -11147), -2011844015)

    def test0851(self):
        self.assertEquals(self.calculate(-402616001, -3361), 277681121)

    def test0852(self):
        self.assertEquals(self.calculate(-528157107, 18650), -1770035822)

    def test0853(self):
        self.assertEquals(self.calculate(471160100, 18104), 77400544)

    def test0854(self):
        self.assertEquals(self.calculate(2123302806, 24317), -1742499010)

    def test0855(self):
        self.assertEquals(self.calculate(1451879349, 21255), 355541235)

    def test0856(self):
        self.assertEquals(self.calculate(-130264870, 19163), -889704834)

    def test0857(self):
        self.assertEquals(self.calculate(-874996183, -16170), 1066006086)

    def test0858(self):
        self.assertEquals(self.calculate(461142169, 17742), -328336482)

    def test0859(self):
        self.assertEquals(self.calculate(1841882188, 3516), -752909360)

    def test0860(self):
        self.assertEquals(self.calculate(-499948330, 19665), -303768906)

    def test0861(self):
        self.assertEquals(self.calculate(-631865658, 14172), 206706984)

    def test0862(self):
        self.assertEquals(self.calculate(-1342979808, -6636), -43133312)

    def test0863(self):
        self.assertEquals(self.calculate(-1759053015, -1773), 654738699)

    def test0864(self):
        self.assertEquals(self.calculate(-466217622, 24204), -1452236296)

    def test0865(self):
        self.assertEquals(self.calculate(-996302461, 27901), -806624649)

    def test0866(self):
        self.assertEquals(self.calculate(-919183272, 4209), 923141848)

    def test0867(self):
        self.assertEquals(self.calculate(1774884391, 29210), -177168906)

    def test0868(self):
        self.assertEquals(self.calculate(2092317787, -2829), -702085535)

    def test0869(self):
        self.assertEquals(self.calculate(2013785878, -30456), 270286512)

    def test0870(self):
        self.assertEquals(self.calculate(1310421939, -13018), 537297810)

    def test0871(self):
        self.assertEquals(self.calculate(410235248, 30938), 229742944)

    def test0872(self):
        self.assertEquals(self.calculate(-1395553949, -7846), 1644646350)

    def test0873(self):
        self.assertEquals(self.calculate(1462955274, -16630), 2043525220)

    def test0874(self):
        self.assertEquals(self.calculate(1578784488, -10774), -1753581552)

    def test0875(self):
        self.assertEquals(self.calculate(-947002554, -22731), -61032578)

    def test0876(self):
        self.assertEquals(self.calculate(480057629, 19734), -1240604290)

    def test0877(self):
        self.assertEquals(self.calculate(866604683, -8600), -1032015240)

    def test0878(self):
        self.assertEquals(self.calculate(808613493, 10715), 1344541463)

    def test0879(self):
        self.assertEquals(self.calculate(751908830, 8267), 1212620298)

    def test0880(self):
        self.assertEquals(self.calculate(-1383558590, 29149), 393569530)

    def test0881(self):
        self.assertEquals(self.calculate(-1276718618, 2994), 25351148)

    def test0882(self):
        self.assertEquals(self.calculate(-1457143428, 31328), 1818076800)

    def test0883(self):
        self.assertEquals(self.calculate(137884877, 20588), -199534980)

    def test0884(self):
        self.assertEquals(self.calculate(-1301447974, 23221), -1533509598)

    def test0885(self):
        self.assertEquals(self.calculate(-204565870, 21757), -1153514934)

    def test0886(self):
        self.assertEquals(self.calculate(-875061763, 15607), 907066139)

    def test0887(self):
        self.assertEquals(self.calculate(-248067530, 8241), 79918166)

    def test0888(self):
        self.assertEquals(self.calculate(1389386474, -5566), 1910985812)

    def test0889(self):
        self.assertEquals(self.calculate(2089109273, 4038), 507475030)

    def test0890(self):
        self.assertEquals(self.calculate(-520972892, 23036), -992915088)

    def test0891(self):
        self.assertEquals(self.calculate(79174771, 25924), -467604084)

    def test0892(self):
        self.assertEquals(self.calculate(1206357241, -15057), -704282953)

    def test0893(self):
        self.assertEquals(self.calculate(-347457657, 24759), 115364225)

    def test0894(self):
        self.assertEquals(self.calculate(1958783952, -23772), 1823316288)

    def test0895(self):
        self.assertEquals(self.calculate(1447543712, -12190), -1832197312)

    def test0896(self):
        self.assertEquals(self.calculate(-529548171, 5915), -1246272681)

    def test0897(self):
        self.assertEquals(self.calculate(2121668827, 25368), -2035350136)

    def test0898(self):
        self.assertEquals(self.calculate(975588429, -1650), 891828150)

    def test0899(self):
        self.assertEquals(self.calculate(-778580914, -6601), -1663239998)

    def test0900(self):
        self.assertEquals(self.calculate(-1269976577, 14256), -1498929072)

    def test0901(self):
        self.assertEquals(self.calculate(-1398416380, -17868), -1215850288)

    def test0902(self):
        self.assertEquals(self.calculate(1633669000, -19686), 307178448)

    def test0903(self):
        self.assertEquals(self.calculate(-1950327118, 172), -448815208)

    def test0904(self):
        self.assertEquals(self.calculate(-445599038, -14625), 1420542718)

    def test0905(self):
        self.assertEquals(self.calculate(1021476332, -15949), -715065340)

    def test0906(self):
        self.assertEquals(self.calculate(697082711, 972), -1040437676)

    def test0907(self):
        self.assertEquals(self.calculate(-2119111812, 9066), -478972584)

    def test0908(self):
        self.assertEquals(self.calculate(995882784, -30519), 2136868896)

    def test0909(self):
        self.assertEquals(self.calculate(-239923176, -8193), -1404440600)

    def test0910(self):
        self.assertEquals(self.calculate(570905354, -2505), 106197798)

    def test0911(self):
        self.assertEquals(self.calculate(441124836, -22854), -1178758232)

    def test0912(self):
        self.assertEquals(self.calculate(-972816630, 31945), 1756108506)

    def test0913(self):
        self.assertEquals(self.calculate(-608818738, -21451), -1224798298)

    def test0914(self):
        self.assertEquals(self.calculate(1136740878, 31946), 375600908)

    def test0915(self):
        self.assertEquals(self.calculate(1243094820, -11739), 1608779828)

    def test0916(self):
        self.assertEquals(self.calculate(-1696035600, -11385), -807656816)

    def test0917(self):
        self.assertEquals(self.calculate(-1305859352, 27456), 712618496)

    def test0918(self):
        self.assertEquals(self.calculate(1714825130, 5869), 1200313442)

    def test0919(self):
        self.assertEquals(self.calculate(461527169, -24581), -1790712453)

    def test0920(self):
        self.assertEquals(self.calculate(-420949974, 5910), -1028281956)

    def test0921(self):
        self.assertEquals(self.calculate(-729163003, 14415), -1099714933)

    def test0922(self):
        self.assertEquals(self.calculate(1121449113, 2037), -530758291)

    def test0923(self):
        self.assertEquals(self.calculate(-292442837, 32107), -663658503)

    def test0924(self):
        self.assertEquals(self.calculate(-686834786, 6975), -1784097310)

    def test0925(self):
        self.assertEquals(self.calculate(1748756621, -19906), -39363546)

    def test0926(self):
        self.assertEquals(self.calculate(1176133594, -26860), -1463872760)

    def test0927(self):
        self.assertEquals(self.calculate(-1149031349, 5083), 629175593)

    def test0928(self):
        self.assertEquals(self.calculate(2025778152, -30984), -58197824)

    def test0929(self):
        self.assertEquals(self.calculate(-1140776207, 2657), 1204528977)

    def test0930(self):
        self.assertEquals(self.calculate(2108988270, 32248), -153401200)

    def test0931(self):
        self.assertEquals(self.calculate(1810440541, 24620), -124478468)

    def test0932(self):
        self.assertEquals(self.calculate(16653533, -1566), -309628902)

    def test0933(self):
        self.assertEquals(self.calculate(755688344, 14992), -844073600)

    def test0934(self):
        self.assertEquals(self.calculate(-1983499317, -27163), 1722186647)

    def test0935(self):
        self.assertEquals(self.calculate(-4569700, -29509), 1703291124)

    def test0936(self):
        self.assertEquals(self.calculate(488846040, 14513), -663394472)

    def test0937(self):
        self.assertEquals(self.calculate(-988071281, -5630), 858663710)

    def test0938(self):
        self.assertEquals(self.calculate(1781121761, 26708), -857777708)

    def test0939(self):
        self.assertEquals(self.calculate(2130715798, -13968), -2009872480)

    def test0940(self):
        self.assertEquals(self.calculate(-415730837, 12172), -804273276)

    def test0941(self):
        self.assertEquals(self.calculate(411516592, 20629), -1974567824)

    def test0942(self):
        self.assertEquals(self.calculate(645589208, 1125), 438385976)

    def test0943(self):
        self.assertEquals(self.calculate(-844245572, -22821), -695091244)

    def test0944(self):
        self.assertEquals(self.calculate(-131924249, 21526), -828001318)

    def test0945(self):
        self.assertEquals(self.calculate(70618667, -19485), -1615191775)

    def test0946(self):
        self.assertEquals(self.calculate(-530637067, -9581), -1207539537)

    def test0947(self):
        self.assertEquals(self.calculate(-2004071636, -10940), -1264348240)

    def test0948(self):
        self.assertEquals(self.calculate(73275580, -14363), -190168020)

    def test0949(self):
        self.assertEquals(self.calculate(-2050247546, 30482), 423426924)

    def test0950(self):
        self.assertEquals(self.calculate(1782695323, 4706), 1293060950)

    def test0951(self):
        self.assertEquals(self.calculate(-2090673519, -8421), 490757195)

    def test0952(self):
        self.assertEquals(self.calculate(-721297421, -7343), 792286435)

    def test0953(self):
        self.assertEquals(self.calculate(-886512123, 4721), -1925586379)

    def test0954(self):
        self.assertEquals(self.calculate(-1485753917, 27632), 1240147920)

    def test0955(self):
        self.assertEquals(self.calculate(-1919947589, 5310), 1330663114)

    def test0956(self):
        self.assertEquals(self.calculate(362734079, -16604), -1292498724)

    def test0957(self):
        self.assertEquals(self.calculate(-1441664638, 19547), -938249930)

    def test0958(self):
        self.assertEquals(self.calculate(1562192679, -25239), -381248001)

    def test0959(self):
        self.assertEquals(self.calculate(1610989156, 17292), 66603696)

    def test0960(self):
        self.assertEquals(self.calculate(1839552153, 17398), -1567931898)

    def test0961(self):
        self.assertEquals(self.calculate(-1063445727, 20062), -1745615842)

    def test0962(self):
        self.assertEquals(self.calculate(1254894912, -11129), 1508170944)

    def test0963(self):
        self.assertEquals(self.calculate(-1933276253, 17622), -513538494)

    def test0964(self):
        self.assertEquals(self.calculate(1387052967, 7871), -312963175)

    def test0965(self):
        self.assertEquals(self.calculate(481006, -3838), -1846101028)

    def test0966(self):
        self.assertEquals(self.calculate(1847896592, -26902), 2132333216)

    def test0967(self):
        self.assertEquals(self.calculate(-845607228, -10316), 205585872)

    def test0968(self):
        self.assertEquals(self.calculate(680559636, -32091), 69421284)

    def test0969(self):
        self.assertEquals(self.calculate(2015169275, 5395), 1276012449)

    def test0970(self):
        self.assertEquals(self.calculate(-1014484291, 2374), 1090946222)

    def test0971(self):
        self.assertEquals(self.calculate(-893536940, 20494), 1594501784)

    def test0972(self):
        self.assertEquals(self.calculate(-784932289, 13552), 1231611664)

    def test0973(self):
        self.assertEquals(self.calculate(279889649, -29494), -138164694)

    def test0974(self):
        self.assertEquals(self.calculate(1251345159, -155), -684971325)

    def test0975(self):
        self.assertEquals(self.calculate(583416026, -31339), 940258)

    def test0976(self):
        self.assertEquals(self.calculate(308519564, -163), 1250918620)

    def test0977(self):
        self.assertEquals(self.calculate(277856026, 31869), -1228871758)

    def test0978(self):
        self.assertEquals(self.calculate(-521366919, 27647), -320964217)

    def test0979(self):
        self.assertEquals(self.calculate(-862493203, -2512), 1919408752)

    def test0980(self):
        self.assertEquals(self.calculate(-717465503, 12085), 968366869)

    def test0981(self):
        self.assertEquals(self.calculate(-1056245969, 29305), 541180727)

    def test0982(self):
        self.assertEquals(self.calculate(295530781, -28067), -1080581751)

    def test0983(self):
        self.assertEquals(self.calculate(-965819013, -9770), 8607698)

    def test0984(self):
        self.assertEquals(self.calculate(92879921, -18129), -192907777)

    def test0985(self):
        self.assertEquals(self.calculate(2006239485, -11433), 2084295931)

    def test0986(self):
        self.assertEquals(self.calculate(-1045602363, -28547), -1212050639)

    def test0987(self):
        self.assertEquals(self.calculate(-109382263, 2567), -1611394881)

    def test0988(self):
        self.assertEquals(self.calculate(229763342, -5184), -1387223936)

    def test0989(self):
        self.assertEquals(self.calculate(-639237060, 16847), -1743738748)

    def test0990(self):
        self.assertEquals(self.calculate(-652077281, -1527), -710404585)

    def test0991(self):
        self.assertEquals(self.calculate(771747621, -18110), -525835126)

    def test0992(self):
        self.assertEquals(self.calculate(-1356841073, 11587), -2137209491)

    def test0993(self):
        self.assertEquals(self.calculate(1173267512, -15567), -2054416712)

    def test0994(self):
        self.assertEquals(self.calculate(-1148350823, -16046), 1027606018)

    def test0995(self):
        self.assertEquals(self.calculate(-366672003, -3099), -1849796143)

    def test0996(self):
        self.assertEquals(self.calculate(2133569463, -22889), -1493283087)

    def test0997(self):
        self.assertEquals(self.calculate(-1023436353, -32227), 1229482147)

    def test0998(self):
        self.assertEquals(self.calculate(-1353982679, 953), -1855304287)

    def test0999(self):
        self.assertEquals(self.calculate(2034513984, -10849), -605278272)

    def test1000(self):
        self.assertEquals(self.calculate(-1370432240, 25110), -275570848)

    def test1001(self):
        self.assertEquals(self.calculate(1845665323, 11485), 1802628895)

    def test1002(self):
        self.assertEquals(self.calculate(-1340505781, 15553), -1115157109)

    def test1003(self):
        self.assertEquals(self.calculate(401551760, 28690), 1417706528)

    def test1004(self):
        self.assertEquals(self.calculate(333428012, 22704), -1877758400)

    def test1005(self):
        self.assertEquals(self.calculate(-1141502527, 30448), -1593582864)

    def test1006(self):
        self.assertEquals(self.calculate(-732854836, 7503), -1051695628)

    def test1007(self):
        self.assertEquals(self.calculate(1594383955, -22315), 831124239)

    def test1008(self):
        self.assertEquals(self.calculate(1051801211, 6276), -260333716)

    def test1009(self):
        self.assertEquals(self.calculate(-965259048, -5990), 875717104)

    def test1010(self):
        self.assertEquals(self.calculate(-727456182, -19557), 1928867022)

    def test1011(self):
        self.assertEquals(self.calculate(-974796847, -15505), 235198111)

    def test1012(self):
        self.assertEquals(self.calculate(-1214682479, -3167), -1391286223)

    def test1013(self):
        self.assertEquals(self.calculate(-1425019887, -19805), 288760019)

    def test1014(self):
        self.assertEquals(self.calculate(398213392, 19639), -622640528)

    def test1015(self):
        self.assertEquals(self.calculate(1345321457, -27239), -550197751)

    def test1016(self):
        self.assertEquals(self.calculate(-1081034718, -15020), -2129881816)

    def test1017(self):
        self.assertEquals(self.calculate(882028369, 7417), 769221065)

    def test1018(self):
        self.assertEquals(self.calculate(1175802094, -2858), -1777959180)

    def test1019(self):
        self.assertEquals(self.calculate(127787753, 22072), -1262229256)

    def test1020(self):
        self.assertEquals(self.calculate(2098927718, -30774), -388429188)

    def test1021(self):
        self.assertEquals(self.calculate(1388108919, -20890), 2023864682)

    def test1022(self):
        self.assertEquals(self.calculate(-310862244, -21874), 867495688)

    def test1023(self):
        self.assertEquals(self.calculate(-1879629366, -18064), 1908392544)




class TestVM_Mul_LongLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushL(rhs)
        v.VM_Mul()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(1922350315, 663751467), -1270229895)

    def test0001(self):
        self.assertEquals(self.calculate(699765920, 240624405), 1273434400)

    def test0002(self):
        self.assertEquals(self.calculate(990585996, 981974838), -1032705656)

    def test0003(self):
        self.assertEquals(self.calculate(-1599597508, 346661871), 224991236)

    def test0004(self):
        self.assertEquals(self.calculate(1005266326, -1063308835), -1805965186)

    def test0005(self):
        self.assertEquals(self.calculate(-1031035112, 287114009), 676370776)

    def test0006(self):
        self.assertEquals(self.calculate(1726731734, -1150891461), 1415128146)

    def test0007(self):
        self.assertEquals(self.calculate(-1524201052, 10543636), -217741104)

    def test0008(self):
        self.assertEquals(self.calculate(637273845, -1855412844), -21500252)

    def test0009(self):
        self.assertEquals(self.calculate(285444749, 90542949), 697671841)

    def test0010(self):
        self.assertEquals(self.calculate(59492939, 876926263), 172285213)

    def test0011(self):
        self.assertEquals(self.calculate(1366973355, 2143175151), 7077797)

    def test0012(self):
        self.assertEquals(self.calculate(1647916282, 2131821308), -1386997224)

    def test0013(self):
        self.assertEquals(self.calculate(-348444807, 1343151155), -1420633829)

    def test0014(self):
        self.assertEquals(self.calculate(-1334315646, -1444166572), -274065752)

    def test0015(self):
        self.assertEquals(self.calculate(-689963555, 363819468), -996157156)

    def test0016(self):
        self.assertEquals(self.calculate(1003179519, -1063798886), -1904790426)

    def test0017(self):
        self.assertEquals(self.calculate(-2030186750, 1249086258), -1092713372)

    def test0018(self):
        self.assertEquals(self.calculate(1958279756, 1741559715), -311676316)

    def test0019(self):
        self.assertEquals(self.calculate(634209155, 1853641668), 2071931212)

    def test0020(self):
        self.assertEquals(self.calculate(383265503, -622787463), -1059668121)

    def test0021(self):
        self.assertEquals(self.calculate(1562533331, 835041080), -2030740696)

    def test0022(self):
        self.assertEquals(self.calculate(1221684493, 1771250622), -1597065562)

    def test0023(self):
        self.assertEquals(self.calculate(-1563798117, 656081021), 556059823)

    def test0024(self):
        self.assertEquals(self.calculate(-1251918791, -395036782), 1194891138)

    def test0025(self):
        self.assertEquals(self.calculate(939545638, 62271046), -1539713436)

    def test0026(self):
        self.assertEquals(self.calculate(1995464882, 779429890), -1437167260)

    def test0027(self):
        self.assertEquals(self.calculate(-2093891683, -1417645098), -1305889730)

    def test0028(self):
        self.assertEquals(self.calculate(1253310872, -61555619), 2054173752)

    def test0029(self):
        self.assertEquals(self.calculate(1072510844, -1367636253), -889775372)

    def test0030(self):
        self.assertEquals(self.calculate(1863880478, 345887900), 652349000)

    def test0031(self):
        self.assertEquals(self.calculate(-1603950933, 255586980), 1192586124)

    def test0032(self):
        self.assertEquals(self.calculate(751227636, -576597930), -442163720)

    def test0033(self):
        self.assertEquals(self.calculate(1136925415, -184034683), 52146179)

    def test0034(self):
        self.assertEquals(self.calculate(-1889570321, -58403066), -2010618726)

    def test0035(self):
        self.assertEquals(self.calculate(-1053016491, 158453670), -2080627170)

    def test0036(self):
        self.assertEquals(self.calculate(-1758099567, -966053703), 515188681)

    def test0037(self):
        self.assertEquals(self.calculate(-2056121764, -1928544738), -716280120)

    def test0038(self):
        self.assertEquals(self.calculate(-887813712, 148968781), -758162960)

    def test0039(self):
        self.assertEquals(self.calculate(1936654215, 1918127791), -1324888247)

    def test0040(self):
        self.assertEquals(self.calculate(1131179737, -1674973519), 1774674441)

    def test0041(self):
        self.assertEquals(self.calculate(-1495449624, 243421159), -64142760)

    def test0042(self):
        self.assertEquals(self.calculate(1628689133, 1792607036), -385665396)

    def test0043(self):
        self.assertEquals(self.calculate(-82066253, 1313493609), 1227031403)

    def test0044(self):
        self.assertEquals(self.calculate(-1100017381, 1783892062), 808263658)

    def test0045(self):
        self.assertEquals(self.calculate(2054944706, -1438340629), -370966250)

    def test0046(self):
        self.assertEquals(self.calculate(630701862, 758735205), -1849569282)

    def test0047(self):
        self.assertEquals(self.calculate(-1277580497, -1139320681), -847961927)

    def test0048(self):
        self.assertEquals(self.calculate(977328745, -520134508), 1845273780)

    def test0049(self):
        self.assertEquals(self.calculate(-1001395216, -15663490), -1167179744)

    def test0050(self):
        self.assertEquals(self.calculate(1480812073, 330966323), -1745139925)

    def test0051(self):
        self.assertEquals(self.calculate(-696689534, -1469458369), 1866298366)

    def test0052(self):
        self.assertEquals(self.calculate(-262860181, 160865215), 1599178453)

    def test0053(self):
        self.assertEquals(self.calculate(1501812527, -740360786), 2064102642)

    def test0054(self):
        self.assertEquals(self.calculate(-1486226345, 1563309039), 1541007929)

    def test0055(self):
        self.assertEquals(self.calculate(1527890374, -50359334), -1415727972)

    def test0056(self):
        self.assertEquals(self.calculate(-655201938, 1090790294), -701771660)

    def test0057(self):
        self.assertEquals(self.calculate(1081409213, -670368845), 854813991)

    def test0058(self):
        self.assertEquals(self.calculate(-153506931, -1684183226), -1476156530)

    def test0059(self):
        self.assertEquals(self.calculate(-1778807225, -2059851311), -111835401)

    def test0060(self):
        self.assertEquals(self.calculate(359764503, 336945745), 180291399)

    def test0061(self):
        self.assertEquals(self.calculate(937557968, -1908273663), -411082800)

    def test0062(self):
        self.assertEquals(self.calculate(1160274781, -1939088759), -887529787)

    def test0063(self):
        self.assertEquals(self.calculate(385747717, 1624292771), 99857711)

    def test0064(self):
        self.assertEquals(self.calculate(-1590661367, 414016688), -1648305616)

    def test0065(self):
        self.assertEquals(self.calculate(182432501, -891641570), -1402663498)

    def test0066(self):
        self.assertEquals(self.calculate(-1069409443, 1542441834), -1578822782)

    def test0067(self):
        self.assertEquals(self.calculate(-1044138937, 1117403785), -917925889)

    def test0068(self):
        self.assertEquals(self.calculate(-1862688947, 640496645), -138100607)

    def test0069(self):
        self.assertEquals(self.calculate(-1647125642, 1448959493), -544105138)

    def test0070(self):
        self.assertEquals(self.calculate(285997726, 56229922), 958613756)

    def test0071(self):
        self.assertEquals(self.calculate(1169118879, -1993327686), 1596691590)

    def test0072(self):
        self.assertEquals(self.calculate(-978745356, -1460923684), 1043332528)

    def test0073(self):
        self.assertEquals(self.calculate(-1076337633, 382552038), 922848474)

    def test0074(self):
        self.assertEquals(self.calculate(-13861175, -904607005), -499972549)

    def test0075(self):
        self.assertEquals(self.calculate(-1973513060, -1683634084), -626833392)

    def test0076(self):
        self.assertEquals(self.calculate(-1987622281, 1146080495), -883009255)

    def test0077(self):
        self.assertEquals(self.calculate(1657962141, -1895118781), -182203625)

    def test0078(self):
        self.assertEquals(self.calculate(518323531, -2095028449), -368846571)

    def test0079(self):
        self.assertEquals(self.calculate(813453968, -406335699), 713880400)

    def test0080(self):
        self.assertEquals(self.calculate(1509222534, 828395444), -1405822920)

    def test0081(self):
        self.assertEquals(self.calculate(1623106975, 316472916), 1770396204)

    def test0082(self):
        self.assertEquals(self.calculate(970966364, 1448593982), -1875876792)

    def test0083(self):
        self.assertEquals(self.calculate(-1297570964, 1250993492), 1969896304)

    def test0084(self):
        self.assertEquals(self.calculate(2108614244, 2024548708), -966262000)

    def test0085(self):
        self.assertEquals(self.calculate(-1786625666, -159585415), 163028622)

    def test0086(self):
        self.assertEquals(self.calculate(-1272832031, 1707078038), 971013846)

    def test0087(self):
        self.assertEquals(self.calculate(-790617921, -1337284883), 2079337171)

    def test0088(self):
        self.assertEquals(self.calculate(977140124, 850233190), 163493928)

    def test0089(self):
        self.assertEquals(self.calculate(-1910991712, -1247314494), -1013792448)

    def test0090(self):
        self.assertEquals(self.calculate(1631096874, -412517722), 110853948)

    def test0091(self):
        self.assertEquals(self.calculate(-459839950, 1898214209), 2120313010)

    def test0092(self):
        self.assertEquals(self.calculate(-751085819, -434786559), 86032901)

    def test0093(self):
        self.assertEquals(self.calculate(1433233512, -1983678079), -239942552)

    def test0094(self):
        self.assertEquals(self.calculate(1986148519, 250931654), 380882986)

    def test0095(self):
        self.assertEquals(self.calculate(1276041534, -1724418208), 652167488)

    def test0096(self):
        self.assertEquals(self.calculate(-1723986247, -111472914), 155373054)

    def test0097(self):
        self.assertEquals(self.calculate(-876456413, -2118458500), 1022411252)

    def test0098(self):
        self.assertEquals(self.calculate(-2088206546, 960403225), 1719438718)

    def test0099(self):
        self.assertEquals(self.calculate(1550539579, -9447660), -1248416356)

    def test0100(self):
        self.assertEquals(self.calculate(-1635145037, -1899658539), 1996025071)

    def test0101(self):
        self.assertEquals(self.calculate(302265827, 349598186), 459568254)

    def test0102(self):
        self.assertEquals(self.calculate(-1678594577, -1806930746), -838378790)

    def test0103(self):
        self.assertEquals(self.calculate(-1127615454, 418693222), -1879521908)

    def test0104(self):
        self.assertEquals(self.calculate(1442965258, -383128154), -1564863876)

    def test0105(self):
        self.assertEquals(self.calculate(-1971996695, 117863970), 1423823602)

    def test0106(self):
        self.assertEquals(self.calculate(-1004351105, -738583307), -951950709)

    def test0107(self):
        self.assertEquals(self.calculate(-1113089870, -107704811), -296074598)

    def test0108(self):
        self.assertEquals(self.calculate(2042270915, -114219454), 948063302)

    def test0109(self):
        self.assertEquals(self.calculate(330702437, 855188478), -1089013962)

    def test0110(self):
        self.assertEquals(self.calculate(-2077507481, 1555897663), -1952775079)

    def test0111(self):
        self.assertEquals(self.calculate(-584698872, -431532057), 660581176)

    def test0112(self):
        self.assertEquals(self.calculate(-1377653, -1715894330), -78637950)

    def test0113(self):
        self.assertEquals(self.calculate(1830773731, 1768921525), 1414613631)

    def test0114(self):
        self.assertEquals(self.calculate(-1693296678, -1585875447), -2010279254)

    def test0115(self):
        self.assertEquals(self.calculate(-1816068373, 1768102447), -1305236699)

    def test0116(self):
        self.assertEquals(self.calculate(-507255282, -1149018230), 1495479692)

    def test0117(self):
        self.assertEquals(self.calculate(-2044669372, 1645005101), 1007442420)

    def test0118(self):
        self.assertEquals(self.calculate(-285007097, -475434863), 347662071)

    def test0119(self):
        self.assertEquals(self.calculate(582324053, -1203891567), 998254885)

    def test0120(self):
        self.assertEquals(self.calculate(1707941139, 1311004484), -1610011124)

    def test0121(self):
        self.assertEquals(self.calculate(-1407000038, -296651383), -969219606)

    def test0122(self):
        self.assertEquals(self.calculate(-2080517058, 883763875), -1252634758)

    def test0123(self):
        self.assertEquals(self.calculate(115496099, 1180371044), 1795106732)

    def test0124(self):
        self.assertEquals(self.calculate(-1822194108, 1024559141), 1262127060)

    def test0125(self):
        self.assertEquals(self.calculate(314668285, 1825124544), -307483200)

    def test0126(self):
        self.assertEquals(self.calculate(-948659795, -1879858957), -1242497225)

    def test0127(self):
        self.assertEquals(self.calculate(-1902223831, -508482442), 411529958)

    def test0128(self):
        self.assertEquals(self.calculate(427869551, 1900629921), 311454671)

    def test0129(self):
        self.assertEquals(self.calculate(-1349339454, -964888130), -1801562628)

    def test0130(self):
        self.assertEquals(self.calculate(2009247130, 1488628284), 1791816728)

    def test0131(self):
        self.assertEquals(self.calculate(1673696880, 1861929253), 1016966704)

    def test0132(self):
        self.assertEquals(self.calculate(-619344085, -439804753), -14118299)

    def test0133(self):
        self.assertEquals(self.calculate(1606698256, 52035597), 278364624)

    def test0134(self):
        self.assertEquals(self.calculate(947778264, -348863439), -639050920)

    def test0135(self):
        self.assertEquals(self.calculate(-1081511591, -1186435843), 2024706293)

    def test0136(self):
        self.assertEquals(self.calculate(618249506, 1149544797), -1367529638)

    def test0137(self):
        self.assertEquals(self.calculate(-1639733283, 237516144), -1881001552)

    def test0138(self):
        self.assertEquals(self.calculate(-1603681743, -648331000), 1845985928)

    def test0139(self):
        self.assertEquals(self.calculate(-370019633, 887129626), -389348602)

    def test0140(self):
        self.assertEquals(self.calculate(-1391252485, 1489731765), 479500407)

    def test0141(self):
        self.assertEquals(self.calculate(101878125, -1053414055), -2003308571)

    def test0142(self):
        self.assertEquals(self.calculate(549835009, -1856723744), -1940945696)

    def test0143(self):
        self.assertEquals(self.calculate(-1052334755, 84939375), -334348973)

    def test0144(self):
        self.assertEquals(self.calculate(174764470, 348809365), -639148306)

    def test0145(self):
        self.assertEquals(self.calculate(1566387643, 1107100912), -1461662896)

    def test0146(self):
        self.assertEquals(self.calculate(409591888, -446920805), -903544720)

    def test0147(self):
        self.assertEquals(self.calculate(-344561973, 345691120), 131575632)

    def test0148(self):
        self.assertEquals(self.calculate(-1114713162, -501882354), 2124693492)

    def test0149(self):
        self.assertEquals(self.calculate(-1323554464, 1686537319), -269867616)

    def test0150(self):
        self.assertEquals(self.calculate(-1277299164, -493045353), 1153184572)

    def test0151(self):
        self.assertEquals(self.calculate(505131772, 1780870987), -459099180)

    def test0152(self):
        self.assertEquals(self.calculate(2041074550, -1222527807), 785114102)

    def test0153(self):
        self.assertEquals(self.calculate(-1651109768, -1763408840), -734954944)

    def test0154(self):
        self.assertEquals(self.calculate(180893364, -1878326908), -248583984)

    def test0155(self):
        self.assertEquals(self.calculate(1842518609, 1492468873), 1043798361)

    def test0156(self):
        self.assertEquals(self.calculate(701181647, -1049335885), 1035142077)

    def test0157(self):
        self.assertEquals(self.calculate(1753748605, -1977575736), 1475428264)

    def test0158(self):
        self.assertEquals(self.calculate(1781899142, 678515440), 428112288)

    def test0159(self):
        self.assertEquals(self.calculate(727050279, 2049967354), -959098346)

    def test0160(self):
        self.assertEquals(self.calculate(2003845245, 1485825744), -487083120)

    def test0161(self):
        self.assertEquals(self.calculate(1526856631, 607490790), -1103526806)

    def test0162(self):
        self.assertEquals(self.calculate(-744499153, 1743696384), 151170560)

    def test0163(self):
        self.assertEquals(self.calculate(-1146767346, -855012137), -413975614)

    def test0164(self):
        self.assertEquals(self.calculate(-1367044915, -1790157701), -1708830081)

    def test0165(self):
        self.assertEquals(self.calculate(271771027, 614956395), 239319921)

    def test0166(self):
        self.assertEquals(self.calculate(-1559059110, 1043400027), -954889986)

    def test0167(self):
        self.assertEquals(self.calculate(1697565735, -2107859228), 733078716)

    def test0168(self):
        self.assertEquals(self.calculate(357471920, 882359089), 502097840)

    def test0169(self):
        self.assertEquals(self.calculate(594056604, 1282108397), 1452193132)

    def test0170(self):
        self.assertEquals(self.calculate(-316417680, 36820520), -2083677824)

    def test0171(self):
        self.assertEquals(self.calculate(626076625, 676727811), -1640542349)

    def test0172(self):
        self.assertEquals(self.calculate(-1874647655, -1582761970), -713013666)

    def test0173(self):
        self.assertEquals(self.calculate(1922857765, -1011398145), -9488677)

    def test0174(self):
        self.assertEquals(self.calculate(198930351, 1029769724), 1732122436)

    def test0175(self):
        self.assertEquals(self.calculate(1060648153, 816425529), -102965679)

    def test0176(self):
        self.assertEquals(self.calculate(1737386482, -128633777), 2144459182)

    def test0177(self):
        self.assertEquals(self.calculate(25152949, 815857530), -2047913150)

    def test0178(self):
        self.assertEquals(self.calculate(-749473605, -221882920), 610481352)

    def test0179(self):
        self.assertEquals(self.calculate(510483891, -851888555), 1609490031)

    def test0180(self):
        self.assertEquals(self.calculate(1450215882, 2034408628), 1529608712)

    def test0181(self):
        self.assertEquals(self.calculate(315104917, -1940193570), 340024118)

    def test0182(self):
        self.assertEquals(self.calculate(-789318949, 788291395), -1601448879)

    def test0183(self):
        self.assertEquals(self.calculate(1774888731, 362252880), 357942896)

    def test0184(self):
        self.assertEquals(self.calculate(-997045990, -7625033), -149480042)

    def test0185(self):
        self.assertEquals(self.calculate(-134655373, 1011412616), -1418545384)

    def test0186(self):
        self.assertEquals(self.calculate(1447792202, -1938308078), -2035898060)

    def test0187(self):
        self.assertEquals(self.calculate(-1670961261, 26075167), -1844090163)

    def test0188(self):
        self.assertEquals(self.calculate(1036372342, -1958138726), -1404995332)

    def test0189(self):
        self.assertEquals(self.calculate(-609121855, -212916174), 1539444658)

    def test0190(self):
        self.assertEquals(self.calculate(-1723608483, -2026797406), -875246374)

    def test0191(self):
        self.assertEquals(self.calculate(2137152227, 1097341103), -604411603)

    def test0192(self):
        self.assertEquals(self.calculate(-2027168037, -891716726), -1487119602)

    def test0193(self):
        self.assertEquals(self.calculate(1640250770, -1194541771), 527272250)

    def test0194(self):
        self.assertEquals(self.calculate(-1982012729, -1820532559), -1249186921)

    def test0195(self):
        self.assertEquals(self.calculate(707891948, -295663243), 1355313628)

    def test0196(self):
        self.assertEquals(self.calculate(-2026050822, -1205181470), 799678132)

    def test0197(self):
        self.assertEquals(self.calculate(1664135000, 325498750), 73282896)

    def test0198(self):
        self.assertEquals(self.calculate(553959051, 1805612927), 121775093)

    def test0199(self):
        self.assertEquals(self.calculate(-910290608, -1204798069), -1823246736)

    def test0200(self):
        self.assertEquals(self.calculate(589607749, 980550067), 773234239)

    def test0201(self):
        self.assertEquals(self.calculate(-1034792242, -566681833), -2125831550)

    def test0202(self):
        self.assertEquals(self.calculate(-1608717280, -1480126868), -1912775296)

    def test0203(self):
        self.assertEquals(self.calculate(141860146, 258372074), -1008287308)

    def test0204(self):
        self.assertEquals(self.calculate(-1720435288, -230064562), 1554741552)

    def test0205(self):
        self.assertEquals(self.calculate(1735866032, -1398860140), 1190051264)

    def test0206(self):
        self.assertEquals(self.calculate(380933514, -1574498096), -669507552)

    def test0207(self):
        self.assertEquals(self.calculate(-555718296, 1100958343), 1181197784)

    def test0208(self):
        self.assertEquals(self.calculate(1232408745, 478215595), -1826019869)

    def test0209(self):
        self.assertEquals(self.calculate(1520863478, -1124523867), 498796174)

    def test0210(self):
        self.assertEquals(self.calculate(989193357, -2079687677), 1830287783)

    def test0211(self):
        self.assertEquals(self.calculate(148532154, 1124908914), -1571045676)

    def test0212(self):
        self.assertEquals(self.calculate(1457584727, -34579197), 1814333957)

    def test0213(self):
        self.assertEquals(self.calculate(300654239, -2012694850), 1016906754)

    def test0214(self):
        self.assertEquals(self.calculate(-759758014, -2133435950), 862887460)

    def test0215(self):
        self.assertEquals(self.calculate(245499845, 2059516732), -2027177684)

    def test0216(self):
        self.assertEquals(self.calculate(-1925840554, 1946393145), -371849178)

    def test0217(self):
        self.assertEquals(self.calculate(1168281454, 873765140), 621015704)

    def test0218(self):
        self.assertEquals(self.calculate(-693910142, -181013460), 1246747224)

    def test0219(self):
        self.assertEquals(self.calculate(515961613, -327493349), -1668176033)

    def test0220(self):
        self.assertEquals(self.calculate(1861558071, -891507063), 900273775)

    def test0221(self):
        self.assertEquals(self.calculate(-1695886364, 997378320), -158121408)

    def test0222(self):
        self.assertEquals(self.calculate(-1560268954, -1091011773), 1587702194)

    def test0223(self):
        self.assertEquals(self.calculate(-594708740, 1003532804), -1884220432)

    def test0224(self):
        self.assertEquals(self.calculate(-581967460, -700597213), 365324372)

    def test0225(self):
        self.assertEquals(self.calculate(-2053861509, -1314648069), -1562582375)

    def test0226(self):
        self.assertEquals(self.calculate(1083632569, 411203050), 262210586)

    def test0227(self):
        self.assertEquals(self.calculate(-89248912, -1771011398), 899313504)

    def test0228(self):
        self.assertEquals(self.calculate(-1109576442, -205245304), 383869744)

    def test0229(self):
        self.assertEquals(self.calculate(963096660, 599680480), 2107862400)

    def test0230(self):
        self.assertEquals(self.calculate(1081415936, -1644239830), -1418061312)

    def test0231(self):
        self.assertEquals(self.calculate(-92268426, 304737233), 1341016662)

    def test0232(self):
        self.assertEquals(self.calculate(-369953317, 542392029), -635090929)

    def test0233(self):
        self.assertEquals(self.calculate(-1983619812, 1582237852), 439721232)

    def test0234(self):
        self.assertEquals(self.calculate(-1474132559, -366419478), -1263090486)

    def test0235(self):
        self.assertEquals(self.calculate(51278563, -1787247347), 1066173575)

    def test0236(self):
        self.assertEquals(self.calculate(1578719234, -164683983), 685774434)

    def test0237(self):
        self.assertEquals(self.calculate(1143557465, 535449330), 2130066466)

    def test0238(self):
        self.assertEquals(self.calculate(33691738, -362890161), 1569954758)

    def test0239(self):
        self.assertEquals(self.calculate(1487763216, -1975027629), -1250092496)

    def test0240(self):
        self.assertEquals(self.calculate(1025878455, 2056866666), -22027578)

    def test0241(self):
        self.assertEquals(self.calculate(944122580, 1677842816), -1741218304)

    def test0242(self):
        self.assertEquals(self.calculate(932363727, 244492537), -329746857)

    def test0243(self):
        self.assertEquals(self.calculate(-1362723571, 452577925), 1601190337)

    def test0244(self):
        self.assertEquals(self.calculate(-996674411, 200075843), 967914751)

    def test0245(self):
        self.assertEquals(self.calculate(1521890138, 1867628249), 1678267210)

    def test0246(self):
        self.assertEquals(self.calculate(437927612, 750480900), -760102160)

    def test0247(self):
        self.assertEquals(self.calculate(-327007602, -1437774040), 2006595632)

    def test0248(self):
        self.assertEquals(self.calculate(-1595611174, 926188741), -973417790)

    def test0249(self):
        self.assertEquals(self.calculate(-578093816, 759377604), 955853344)

    def test0250(self):
        self.assertEquals(self.calculate(-1454158983, -2040853423), -1528328887)

    def test0251(self):
        self.assertEquals(self.calculate(1437993651, -1530398688), 239320672)

    def test0252(self):
        self.assertEquals(self.calculate(323450820, -545313176), -758521952)

    def test0253(self):
        self.assertEquals(self.calculate(1816340583, -1641479585), -1111765959)

    def test0254(self):
        self.assertEquals(self.calculate(-1714626163, -996364226), -2137288666)

    def test0255(self):
        self.assertEquals(self.calculate(846609613, -739094478), 1054994442)

    def test0256(self):
        self.assertEquals(self.calculate(-506207808, -347377833), 19134528)

    def test0257(self):
        self.assertEquals(self.calculate(-542708854, -343489707), 1611813586)

    def test0258(self):
        self.assertEquals(self.calculate(-302639350, -290177319), -835325062)

    def test0259(self):
        self.assertEquals(self.calculate(827395276, 1105036603), 1366290180)

    def test0260(self):
        self.assertEquals(self.calculate(1253995178, -65450547), -1382484958)

    def test0261(self):
        self.assertEquals(self.calculate(-711385036, 1045145934), 841360344)

    def test0262(self):
        self.assertEquals(self.calculate(-4207695, -2059077482), -1212624458)

    def test0263(self):
        self.assertEquals(self.calculate(-1245225747, 1854290438), -406331506)

    def test0264(self):
        self.assertEquals(self.calculate(-731547760, -710135373), 328542640)

    def test0265(self):
        self.assertEquals(self.calculate(196317975, 1234583018), 984280582)

    def test0266(self):
        self.assertEquals(self.calculate(-1939125750, -1890558442), 797444316)

    def test0267(self):
        self.assertEquals(self.calculate(-1882845752, 1941106633), 913213960)

    def test0268(self):
        self.assertEquals(self.calculate(153867022, -61268693), -1457321638)

    def test0269(self):
        self.assertEquals(self.calculate(-1725542343, 719501634), 1479270322)

    def test0270(self):
        self.assertEquals(self.calculate(-761493821, -922269379), -1676757129)

    def test0271(self):
        self.assertEquals(self.calculate(1612445154, 1794605583), -1517409218)

    def test0272(self):
        self.assertEquals(self.calculate(2129246722, -607453420), 907970088)

    def test0273(self):
        self.assertEquals(self.calculate(-1031403110, -1442683173), 665948862)

    def test0274(self):
        self.assertEquals(self.calculate(-2091509534, 669507392), -1222568320)

    def test0275(self):
        self.assertEquals(self.calculate(1072445143, -221191464), 1147671400)

    def test0276(self):
        self.assertEquals(self.calculate(-1973355831, 1886770326), -228694586)

    def test0277(self):
        self.assertEquals(self.calculate(-1818285890, 1236023126), 1457553876)

    def test0278(self):
        self.assertEquals(self.calculate(730315884, -1910915919), 365205164)

    def test0279(self):
        self.assertEquals(self.calculate(-985981824, 1232586753), -1291903872)

    def test0280(self):
        self.assertEquals(self.calculate(-1107137544, -1399716892), 1960579296)

    def test0281(self):
        self.assertEquals(self.calculate(1325734840, 2051550815), -1180673720)

    def test0282(self):
        self.assertEquals(self.calculate(-1877692698, -538822244), 681036328)

    def test0283(self):
        self.assertEquals(self.calculate(-325631972, 957407016), -163944352)

    def test0284(self):
        self.assertEquals(self.calculate(279235323, -1338360944), -463993296)

    def test0285(self):
        self.assertEquals(self.calculate(-150757462, 242136251), -487249618)

    def test0286(self):
        self.assertEquals(self.calculate(1023238408, -2115805800), 1422492864)

    def test0287(self):
        self.assertEquals(self.calculate(-399682519, 2004049644), -1944345652)

    def test0288(self):
        self.assertEquals(self.calculate(1730265912, -1404848062), -1834183568)

    def test0289(self):
        self.assertEquals(self.calculate(769675726, 757088501), 1809959462)

    def test0290(self):
        self.assertEquals(self.calculate(91676098, -1028248529), 450629278)

    def test0291(self):
        self.assertEquals(self.calculate(1740553321, 1641963959), -1698007025)

    def test0292(self):
        self.assertEquals(self.calculate(1318425975, 98979319), 1815216337)

    def test0293(self):
        self.assertEquals(self.calculate(1514922313, 239480226), 311715122)

    def test0294(self):
        self.assertEquals(self.calculate(1835445730, -2105102739), 657696058)

    def test0295(self):
        self.assertEquals(self.calculate(869611750, 835030516), -1500583624)

    def test0296(self):
        self.assertEquals(self.calculate(-2102691435, -1182100447), 834064437)

    def test0297(self):
        self.assertEquals(self.calculate(-1490518018, 100582807), -1218054958)

    def test0298(self):
        self.assertEquals(self.calculate(-534766172, 644977321), -1283516092)

    def test0299(self):
        self.assertEquals(self.calculate(-1396166404, 1011619802), -1179624808)

    def test0300(self):
        self.assertEquals(self.calculate(-214086661, 822977026), -1756467722)

    def test0301(self):
        self.assertEquals(self.calculate(1585929986, 2103498266), 1575703092)

    def test0302(self):
        self.assertEquals(self.calculate(1911731700, 1020382451), 1318397596)

    def test0303(self):
        self.assertEquals(self.calculate(-194908109, 390368080), -292372240)

    def test0304(self):
        self.assertEquals(self.calculate(1190555721, 879243637), 197610077)

    def test0305(self):
        self.assertEquals(self.calculate(-2130260412, -452475699), 3882100)

    def test0306(self):
        self.assertEquals(self.calculate(-1654444466, -682771679), 739373582)

    def test0307(self):
        self.assertEquals(self.calculate(-1049276238, 2125077313), -1333771470)

    def test0308(self):
        self.assertEquals(self.calculate(-1419635075, -798355816), -12963784)

    def test0309(self):
        self.assertEquals(self.calculate(906337272, -1386604705), -95934200)

    def test0310(self):
        self.assertEquals(self.calculate(342506722, -1635040942), 238215780)

    def test0311(self):
        self.assertEquals(self.calculate(-518362175, -74583557), 681924411)

    def test0312(self):
        self.assertEquals(self.calculate(952529671, -1829437827), 1068702827)

    def test0313(self):
        self.assertEquals(self.calculate(1461889763, -1227160880), -1548640656)

    def test0314(self):
        self.assertEquals(self.calculate(-1218915846, -530216645), 1635331742)

    def test0315(self):
        self.assertEquals(self.calculate(-1840925110, -1107460146), 313091468)

    def test0316(self):
        self.assertEquals(self.calculate(-1185457837, 526066291), -1449449911)

    def test0317(self):
        self.assertEquals(self.calculate(1110818090, -1753951631), -873663606)

    def test0318(self):
        self.assertEquals(self.calculate(-201965421, 866336901), -1246933921)

    def test0319(self):
        self.assertEquals(self.calculate(915393812, -2084276602), 387747960)

    def test0320(self):
        self.assertEquals(self.calculate(1568245998, 662087263), -560454574)

    def test0321(self):
        self.assertEquals(self.calculate(129917419, -1590865646), -911393402)

    def test0322(self):
        self.assertEquals(self.calculate(-382097920, 1021563758), -325626880)

    def test0323(self):
        self.assertEquals(self.calculate(-1436191428, 1163311691), 823062676)

    def test0324(self):
        self.assertEquals(self.calculate(161974730, -679666516), -1119573064)

    def test0325(self):
        self.assertEquals(self.calculate(-580979065, -484726786), 1279765234)

    def test0326(self):
        self.assertEquals(self.calculate(-1093687909, 1359215398), -436040190)

    def test0327(self):
        self.assertEquals(self.calculate(-874496049, -1305667833), -566208599)

    def test0328(self):
        self.assertEquals(self.calculate(705200757, 372433956), 104631412)

    def test0329(self):
        self.assertEquals(self.calculate(-343444959, 956748297), 1764234537)

    def test0330(self):
        self.assertEquals(self.calculate(-1795183721, 1740016422), -1367837334)

    def test0331(self):
        self.assertEquals(self.calculate(437739487, -1648388733), 1059314205)

    def test0332(self):
        self.assertEquals(self.calculate(-1758271228, -628551944), 1563685856)

    def test0333(self):
        self.assertEquals(self.calculate(2022300652, 150379744), 795623040)

    def test0334(self):
        self.assertEquals(self.calculate(-447025788, -1065165147), 1251708436)

    def test0335(self):
        self.assertEquals(self.calculate(307529151, 1985238607), -105943055)

    def test0336(self):
        self.assertEquals(self.calculate(-161914063, 1753172460), -1258329556)

    def test0337(self):
        self.assertEquals(self.calculate(439512987, -773031314), -1195388262)

    def test0338(self):
        self.assertEquals(self.calculate(879334158, 946274418), -1851425732)

    def test0339(self):
        self.assertEquals(self.calculate(-1620764097, 176971963), 690342917)

    def test0340(self):
        self.assertEquals(self.calculate(-213095581, 1099684714), -1891424258)

    def test0341(self):
        self.assertEquals(self.calculate(754014492, -1567176041), -518805628)

    def test0342(self):
        self.assertEquals(self.calculate(-750072211, 1143676744), 475546024)

    def test0343(self):
        self.assertEquals(self.calculate(-1115604812, 1101034087), -289539988)

    def test0344(self):
        self.assertEquals(self.calculate(-2067347478, 692382090), 323206692)

    def test0345(self):
        self.assertEquals(self.calculate(51382148, -1513719453), -1495774196)

    def test0346(self):
        self.assertEquals(self.calculate(519372886, -1081205974), 1156522012)

    def test0347(self):
        self.assertEquals(self.calculate(-563557861, 527355953), -757162197)

    def test0348(self):
        self.assertEquals(self.calculate(-1744733307, 1647213076), -1327429532)

    def test0349(self):
        self.assertEquals(self.calculate(-746954693, 1147589878), -1832168270)

    def test0350(self):
        self.assertEquals(self.calculate(480127350, 1374954246), 634919620)

    def test0351(self):
        self.assertEquals(self.calculate(-148554705, 2067647312), -1366355024)

    def test0352(self):
        self.assertEquals(self.calculate(-2067210599, -291828226), -146956082)

    def test0353(self):
        self.assertEquals(self.calculate(1139852628, -1605492219), -310312284)

    def test0354(self):
        self.assertEquals(self.calculate(-118542103, -894192501), 1697538691)

    def test0355(self):
        self.assertEquals(self.calculate(-1129225825, 943651248), -1368865712)

    def test0356(self):
        self.assertEquals(self.calculate(-863633013, 68121019), -810124407)

    def test0357(self):
        self.assertEquals(self.calculate(-488814282, 1889596308), -1775463112)

    def test0358(self):
        self.assertEquals(self.calculate(-473759506, -570282043), 2014800166)

    def test0359(self):
        self.assertEquals(self.calculate(533591079, 1152798204), 820384100)

    def test0360(self):
        self.assertEquals(self.calculate(2043226823, -1945403658), -1259729606)

    def test0361(self):
        self.assertEquals(self.calculate(537320313, -1145409818), -1855902538)

    def test0362(self):
        self.assertEquals(self.calculate(-1560922177, -1774328732), 609673884)

    def test0363(self):
        self.assertEquals(self.calculate(-1621528770, 518415892), 1258513624)

    def test0364(self):
        self.assertEquals(self.calculate(-1529053226, -1408558114), 2128899476)

    def test0365(self):
        self.assertEquals(self.calculate(898396515, -1618138227), 99423367)

    def test0366(self):
        self.assertEquals(self.calculate(568431561, -2032190628), 473395004)

    def test0367(self):
        self.assertEquals(self.calculate(-1189370563, -80958879), -1263526371)

    def test0368(self):
        self.assertEquals(self.calculate(1835589000, 1431702864), 397746816)

    def test0369(self):
        self.assertEquals(self.calculate(1384023457, -748446976), -81036544)

    def test0370(self):
        self.assertEquals(self.calculate(2093636968, 1053631837), -1857292600)

    def test0371(self):
        self.assertEquals(self.calculate(-72770777, 122395266), 1491288014)

    def test0372(self):
        self.assertEquals(self.calculate(408062060, 1316121405), -221796932)

    def test0373(self):
        self.assertEquals(self.calculate(-315819251, -521479433), -32420981)

    def test0374(self):
        self.assertEquals(self.calculate(-69354644, -1191067899), 563494172)

    def test0375(self):
        self.assertEquals(self.calculate(257380911, 1517172101), -493654677)

    def test0376(self):
        self.assertEquals(self.calculate(1519918327, -1715475688), 1545761832)

    def test0377(self):
        self.assertEquals(self.calculate(-193561139, -431051382), 1566136706)

    def test0378(self):
        self.assertEquals(self.calculate(-1382349406, 1445097044), -1093831384)

    def test0379(self):
        self.assertEquals(self.calculate(1967226340, -911658190), 308478600)

    def test0380(self):
        self.assertEquals(self.calculate(1678980857, 1562417456), -1818943568)

    def test0381(self):
        self.assertEquals(self.calculate(-1437692185, -291253308), -486355492)

    def test0382(self):
        self.assertEquals(self.calculate(1162636310, 1706863617), -1408027626)

    def test0383(self):
        self.assertEquals(self.calculate(-1237661483, -720128025), -1788183757)

    def test0384(self):
        self.assertEquals(self.calculate(1291352347, 1295465659), -1716532551)

    def test0385(self):
        self.assertEquals(self.calculate(-748636976, -718876312), -1178123136)

    def test0386(self):
        self.assertEquals(self.calculate(557103617, -539170711), 520958569)

    def test0387(self):
        self.assertEquals(self.calculate(-1042920051, -1951562646), -1174286238)

    def test0388(self):
        self.assertEquals(self.calculate(-763280232, 1122743983), -190188568)

    def test0389(self):
        self.assertEquals(self.calculate(-2028650303, 305784011), 142556427)

    def test0390(self):
        self.assertEquals(self.calculate(1989630141, 1657756981), -1553659871)

    def test0391(self):
        self.assertEquals(self.calculate(885130615, 74585932), 1662341204)

    def test0392(self):
        self.assertEquals(self.calculate(391223746, 1484212966), -1292879796)

    def test0393(self):
        self.assertEquals(self.calculate(1889927021, 1346676525), -4062935)

    def test0394(self):
        self.assertEquals(self.calculate(-985107940, -1164685507), -1381378900)

    def test0395(self):
        self.assertEquals(self.calculate(770494921, 635926907), 1498401939)

    def test0396(self):
        self.assertEquals(self.calculate(-1591041291, -2094522437), -1188514825)

    def test0397(self):
        self.assertEquals(self.calculate(745335638, 890871773), -912813250)

    def test0398(self):
        self.assertEquals(self.calculate(1189689097, -742390940), 545168004)

    def test0399(self):
        self.assertEquals(self.calculate(-1227953976, -278612378), -1777406032)

    def test0400(self):
        self.assertEquals(self.calculate(1368949345, -671517799), -1911521543)

    def test0401(self):
        self.assertEquals(self.calculate(2038060853, -863807171), 1452749985)

    def test0402(self):
        self.assertEquals(self.calculate(-854410784, 1748849630), 853594176)

    def test0403(self):
        self.assertEquals(self.calculate(-80581861, -1970604753), -1454341899)

    def test0404(self):
        self.assertEquals(self.calculate(-1599454227, 1947444051), -284496681)

    def test0405(self):
        self.assertEquals(self.calculate(1552138172, 292673450), 864040664)

    def test0406(self):
        self.assertEquals(self.calculate(1240692401, -1129547625), 2032794215)

    def test0407(self):
        self.assertEquals(self.calculate(-1587606411, -1690263605), -212104249)

    def test0408(self):
        self.assertEquals(self.calculate(1641028879, -813508024), -1645940168)

    def test0409(self):
        self.assertEquals(self.calculate(-2020894540, 733335335), -1174286484)

    def test0410(self):
        self.assertEquals(self.calculate(-803134667, 1734941559), 31126691)

    def test0411(self):
        self.assertEquals(self.calculate(1436904726, 1986840976), 956015200)

    def test0412(self):
        self.assertEquals(self.calculate(-1567177299, 1110907717), -878213471)

    def test0413(self):
        self.assertEquals(self.calculate(734666700, -1259034991), -1668658548)

    def test0414(self):
        self.assertEquals(self.calculate(1686304251, -1393254571), -847343273)

    def test0415(self):
        self.assertEquals(self.calculate(362312857, 1495928969), 1744434657)

    def test0416(self):
        self.assertEquals(self.calculate(-711254728, 669810664), -5160256)

    def test0417(self):
        self.assertEquals(self.calculate(-1337787445, 252414712), -1822926168)

    def test0418(self):
        self.assertEquals(self.calculate(-1701619506, -1297062303), -1864975858)

    def test0419(self):
        self.assertEquals(self.calculate(-1664244622, 1771518164), -1753014680)

    def test0420(self):
        self.assertEquals(self.calculate(-1869387141, -555630043), -602236473)

    def test0421(self):
        self.assertEquals(self.calculate(1486098456, -359944559), 2077584792)

    def test0422(self):
        self.assertEquals(self.calculate(-1367945733, -1879611362), -1480123542)

    def test0423(self):
        self.assertEquals(self.calculate(-1487812415, 1298744989), 1580590173)

    def test0424(self):
        self.assertEquals(self.calculate(1496188836, -175644160), -1640314880)

    def test0425(self):
        self.assertEquals(self.calculate(-1054011531, 1217225617), 1123090501)

    def test0426(self):
        self.assertEquals(self.calculate(289538568, -974422709), 1319927896)

    def test0427(self):
        self.assertEquals(self.calculate(-2130551344, -2096258181), -1318157584)

    def test0428(self):
        self.assertEquals(self.calculate(-1852483757, 981003163), -109244351)

    def test0429(self):
        self.assertEquals(self.calculate(-1237709087, -1429681593), 1671408231)

    def test0430(self):
        self.assertEquals(self.calculate(-318664295, -718410755), -1877387467)

    def test0431(self):
        self.assertEquals(self.calculate(-841019537, 224032912), 1824175728)

    def test0432(self):
        self.assertEquals(self.calculate(1764773166, 35337434), -492236500)

    def test0433(self):
        self.assertEquals(self.calculate(690049516, -2067233738), -1952122936)

    def test0434(self):
        self.assertEquals(self.calculate(1726017293, 1903966048), 1862365152)

    def test0435(self):
        self.assertEquals(self.calculate(-573173770, 1024471743), -281807734)

    def test0436(self):
        self.assertEquals(self.calculate(-1418278400, -854690226), 189631488)

    def test0437(self):
        self.assertEquals(self.calculate(1522433661, -1676950727), -366845739)

    def test0438(self):
        self.assertEquals(self.calculate(-1436486691, 1951107750), 1410483022)

    def test0439(self):
        self.assertEquals(self.calculate(1375850741, -1920085120), -2011993728)

    def test0440(self):
        self.assertEquals(self.calculate(-64006320, -1392878529), 388447408)

    def test0441(self):
        self.assertEquals(self.calculate(-1545388753, -444426178), -1170556574)

    def test0442(self):
        self.assertEquals(self.calculate(956522130, -849814136), -1633794160)

    def test0443(self):
        self.assertEquals(self.calculate(442084078, 1768763528), 889548400)

    def test0444(self):
        self.assertEquals(self.calculate(-1056574300, 1018742980), -1248891504)

    def test0445(self):
        self.assertEquals(self.calculate(-673133040, 824457739), 1066957488)

    def test0446(self):
        self.assertEquals(self.calculate(1143411556, 1784464125), 1463808468)

    def test0447(self):
        self.assertEquals(self.calculate(1568824972, 2033901606), -1949529912)

    def test0448(self):
        self.assertEquals(self.calculate(1414088554, -1400235546), -1728871620)

    def test0449(self):
        self.assertEquals(self.calculate(-1721536303, 1035826198), 1425499638)

    def test0450(self):
        self.assertEquals(self.calculate(-441959328, 950929533), 1850243808)

    def test0451(self):
        self.assertEquals(self.calculate(-87189519, -1312890179), 264892141)

    def test0452(self):
        self.assertEquals(self.calculate(711158093, -1596578251), -1366017295)

    def test0453(self):
        self.assertEquals(self.calculate(1991779476, 1733847522), 1953562280)

    def test0454(self):
        self.assertEquals(self.calculate(-704440902, -1975938722), 1859802188)

    def test0455(self):
        self.assertEquals(self.calculate(-1267629855, 1023071086), -1380396114)

    def test0456(self):
        self.assertEquals(self.calculate(-562135842, 333421104), 238482848)

    def test0457(self):
        self.assertEquals(self.calculate(-36201008, -1523717765), 46867184)

    def test0458(self):
        self.assertEquals(self.calculate(124395091, 1241040819), -1204963063)

    def test0459(self):
        self.assertEquals(self.calculate(1334896049, 430255971), -1287040397)

    def test0460(self):
        self.assertEquals(self.calculate(1492901701, -2136962015), 1102152677)

    def test0461(self):
        self.assertEquals(self.calculate(1994761267, -398846587), 122977663)

    def test0462(self):
        self.assertEquals(self.calculate(153373574, -151237616), 1956151392)

    def test0463(self):
        self.assertEquals(self.calculate(1219213020, 659963872), -903338880)

    def test0464(self):
        self.assertEquals(self.calculate(2031688853, 1980399734), 732933294)

    def test0465(self):
        self.assertEquals(self.calculate(-283667231, 1626028027), -2019143781)

    def test0466(self):
        self.assertEquals(self.calculate(150173869, 115506286), 1573627478)

    def test0467(self):
        self.assertEquals(self.calculate(-437488357, 1195410676), -712930884)

    def test0468(self):
        self.assertEquals(self.calculate(914670113, -1841858227), -1396245267)

    def test0469(self):
        self.assertEquals(self.calculate(1312407611, -708792947), 1610006399)

    def test0470(self):
        self.assertEquals(self.calculate(1749200232, 529603594), 762979856)

    def test0471(self):
        self.assertEquals(self.calculate(326480770, -1829693779), 1700362970)

    def test0472(self):
        self.assertEquals(self.calculate(-1090398767, 1455102854), -1842481562)

    def test0473(self):
        self.assertEquals(self.calculate(-1490855189, -1109105554), 419486970)

    def test0474(self):
        self.assertEquals(self.calculate(-444103089, 424030198), -495087382)

    def test0475(self):
        self.assertEquals(self.calculate(-985658258, -1546986829), 1328176362)

    def test0476(self):
        self.assertEquals(self.calculate(-1799439356, 1876078543), -1610038468)

    def test0477(self):
        self.assertEquals(self.calculate(1194108029, -956082299), 1049554929)

    def test0478(self):
        self.assertEquals(self.calculate(766914838, -1920091673), 268251354)

    def test0479(self):
        self.assertEquals(self.calculate(-547024478, 2355083), 276615414)

    def test0480(self):
        self.assertEquals(self.calculate(853867603, 942500127), -1748002547)

    def test0481(self):
        self.assertEquals(self.calculate(-216307679, 1481683992), -233244904)

    def test0482(self):
        self.assertEquals(self.calculate(1909503099, -650445312), 972032512)

    def test0483(self):
        self.assertEquals(self.calculate(218687669, 229429887), 1357638603)

    def test0484(self):
        self.assertEquals(self.calculate(691719165, 1240934267), -1167159921)

    def test0485(self):
        self.assertEquals(self.calculate(-178228887, 169481014), -1989363930)

    def test0486(self):
        self.assertEquals(self.calculate(-545025114, -1325241859), -907804402)

    def test0487(self):
        self.assertEquals(self.calculate(-1237320817, 1772166304), -1016079008)

    def test0488(self):
        self.assertEquals(self.calculate(-1836305943, -1992355543), -1055164591)

    def test0489(self):
        self.assertEquals(self.calculate(-116120049, -1889624266), 1751472170)

    def test0490(self):
        self.assertEquals(self.calculate(-939002132, -1587829934), 1453939608)

    def test0491(self):
        self.assertEquals(self.calculate(1018256624, 1743225598), -1245964768)

    def test0492(self):
        self.assertEquals(self.calculate(969607126, 1211760417), -1633669994)

    def test0493(self):
        self.assertEquals(self.calculate(-149842787, 143556899), -94343561)

    def test0494(self):
        self.assertEquals(self.calculate(-440047564, -141809279), -1902520780)

    def test0495(self):
        self.assertEquals(self.calculate(952864683, -1137242059), -321098137)

    def test0496(self):
        self.assertEquals(self.calculate(-1971986363, -912980748), -2063346236)

    def test0497(self):
        self.assertEquals(self.calculate(1690494833, 1189396994), -2087882526)

    def test0498(self):
        self.assertEquals(self.calculate(1597415302, -198890259), 1331345166)

    def test0499(self):
        self.assertEquals(self.calculate(-1893729665, 1644235430), -1492884390)

    def test0500(self):
        self.assertEquals(self.calculate(290408848, 1104335546), -2045537632)

    def test0501(self):
        self.assertEquals(self.calculate(1291793931, 314690622), -1993680214)

    def test0502(self):
        self.assertEquals(self.calculate(-511645826, -1582968300), -835882536)

    def test0503(self):
        self.assertEquals(self.calculate(-578186327, 1473979911), 994123679)

    def test0504(self):
        self.assertEquals(self.calculate(-553703071, -1821351054), -938414030)

    def test0505(self):
        self.assertEquals(self.calculate(1389246159, -872408909), 794016445)

    def test0506(self):
        self.assertEquals(self.calculate(2014443329, 857495548), 1255308028)

    def test0507(self):
        self.assertEquals(self.calculate(1046971076, 2104832445), 1510411956)

    def test0508(self):
        self.assertEquals(self.calculate(-218951147, -1703149002), -1986659730)

    def test0509(self):
        self.assertEquals(self.calculate(1705448788, -1892689738), 355731896)

    def test0510(self):
        self.assertEquals(self.calculate(-1107050346, 1032238398), 949400148)

    def test0511(self):
        self.assertEquals(self.calculate(1636474605, 589122183), -370978565)

    def test0512(self):
        self.assertEquals(self.calculate(1177939928, 398657396), 1669830112)

    def test0513(self):
        self.assertEquals(self.calculate(-1448891803, -236200198), 391052450)

    def test0514(self):
        self.assertEquals(self.calculate(82004513, 837513749), -84752715)

    def test0515(self):
        self.assertEquals(self.calculate(-580860806, -1501060266), -1276006660)

    def test0516(self):
        self.assertEquals(self.calculate(254729272, 482363615), -1312713528)

    def test0517(self):
        self.assertEquals(self.calculate(-781717017, -2039612020), 675583316)

    def test0518(self):
        self.assertEquals(self.calculate(414301766, 975371149), 12611214)

    def test0519(self):
        self.assertEquals(self.calculate(2137477784, -1035121730), -610675504)

    def test0520(self):
        self.assertEquals(self.calculate(-1987717318, 924360326), 978613340)

    def test0521(self):
        self.assertEquals(self.calculate(-1944462257, 1582495284), -498947572)

    def test0522(self):
        self.assertEquals(self.calculate(2146265891, -1139731635), -357576057)

    def test0523(self):
        self.assertEquals(self.calculate(749790084, -275459432), 1744395872)

    def test0524(self):
        self.assertEquals(self.calculate(-124995232, -287923509), 1529200416)

    def test0525(self):
        self.assertEquals(self.calculate(866640569, 1182117142), 422674662)

    def test0526(self):
        self.assertEquals(self.calculate(-2076476257, 1715098084), 762268828)

    def test0527(self):
        self.assertEquals(self.calculate(450227580, -1589197559), 2100151644)

    def test0528(self):
        self.assertEquals(self.calculate(186763835, -446939693), -1371685471)

    def test0529(self):
        self.assertEquals(self.calculate(662862070, -1579878603), -227515154)

    def test0530(self):
        self.assertEquals(self.calculate(-493569721, 384099676), -1804920700)

    def test0531(self):
        self.assertEquals(self.calculate(-1946549841, 854696252), -848923644)

    def test0532(self):
        self.assertEquals(self.calculate(-1435576685, -1737794128), 1738009616)

    def test0533(self):
        self.assertEquals(self.calculate(1578058566, 437734533), -1926186146)

    def test0534(self):
        self.assertEquals(self.calculate(-42902937, -1191221753), 750224081)

    def test0535(self):
        self.assertEquals(self.calculate(-1021033994, -1408126262), -640739300)

    def test0536(self):
        self.assertEquals(self.calculate(-181543214, 1710381262), -1945797380)

    def test0537(self):
        self.assertEquals(self.calculate(1219953721, -1214950872), 807398120)

    def test0538(self):
        self.assertEquals(self.calculate(-2123716752, -1928864323), -497463888)

    def test0539(self):
        self.assertEquals(self.calculate(37556949, -570234102), 39207762)

    def test0540(self):
        self.assertEquals(self.calculate(-449239380, 1822496355), 1889057924)

    def test0541(self):
        self.assertEquals(self.calculate(-671782722, 514548997), 1158152630)

    def test0542(self):
        self.assertEquals(self.calculate(-109447196, 1965106543), -182816804)

    def test0543(self):
        self.assertEquals(self.calculate(1864717067, -2067680479), -1272224405)

    def test0544(self):
        self.assertEquals(self.calculate(-1590139108, -583741428), -2145675952)

    def test0545(self):
        self.assertEquals(self.calculate(667434980, -1807753722), 523581272)

    def test0546(self):
        self.assertEquals(self.calculate(54592743, 1995605198), 1094127074)

    def test0547(self):
        self.assertEquals(self.calculate(1063214057, 890088841), 1123656881)

    def test0548(self):
        self.assertEquals(self.calculate(-27360916, -150334241), 950480148)

    def test0549(self):
        self.assertEquals(self.calculate(-1754523478, -481767690), 730365788)

    def test0550(self):
        self.assertEquals(self.calculate(1682355896, 1829773529), -1706565128)

    def test0551(self):
        self.assertEquals(self.calculate(1193507, 119633053), 993398647)

    def test0552(self):
        self.assertEquals(self.calculate(449397209, 950916012), -668788532)

    def test0553(self):
        self.assertEquals(self.calculate(-1455775319, -1827739233), 1523267831)

    def test0554(self):
        self.assertEquals(self.calculate(1176719928, -495665812), 1543112608)

    def test0555(self):
        self.assertEquals(self.calculate(1942541305, 1995552041), -596508703)

    def test0556(self):
        self.assertEquals(self.calculate(-735232370, -1743659394), 569503204)

    def test0557(self):
        self.assertEquals(self.calculate(-2035302818, -1635783743), 1390464734)

    def test0558(self):
        self.assertEquals(self.calculate(1330630695, -984431081), -1968710271)

    def test0559(self):
        self.assertEquals(self.calculate(-356268467, -1712415525), -2098753569)

    def test0560(self):
        self.assertEquals(self.calculate(-2076454885, -1799798236), 59980236)

    def test0561(self):
        self.assertEquals(self.calculate(-1744792422, -1708529379), 804978546)

    def test0562(self):
        self.assertEquals(self.calculate(-2076860664, 659803007), -481477384)

    def test0563(self):
        self.assertEquals(self.calculate(-1450414227, -1574473929), 1159148395)

    def test0564(self):
        self.assertEquals(self.calculate(1501922983, 1656824658), 1611986558)

    def test0565(self):
        self.assertEquals(self.calculate(-289198875, -1558266525), 2138402191)

    def test0566(self):
        self.assertEquals(self.calculate(2089627453, 1780345357), -62773223)

    def test0567(self):
        self.assertEquals(self.calculate(988559845, 1569559510), -86514578)

    def test0568(self):
        self.assertEquals(self.calculate(1681421992, 470024844), 2054042592)

    def test0569(self):
        self.assertEquals(self.calculate(1066270490, 1679345409), -1286916838)

    def test0570(self):
        self.assertEquals(self.calculate(-883251384, 208338628), 1194427168)

    def test0571(self):
        self.assertEquals(self.calculate(-1849467783, -1132925417), -314716961)

    def test0572(self):
        self.assertEquals(self.calculate(-34953738, -1564336596), -1808573880)

    def test0573(self):
        self.assertEquals(self.calculate(-1484758439, 20905006), -1536210946)

    def test0574(self):
        self.assertEquals(self.calculate(618971306, -526498940), -1924409944)

    def test0575(self):
        self.assertEquals(self.calculate(616411298, 1498121532), 984584184)

    def test0576(self):
        self.assertEquals(self.calculate(83572226, 1780866980), -1488693432)

    def test0577(self):
        self.assertEquals(self.calculate(1622647677, -106956355), 624642121)

    def test0578(self):
        self.assertEquals(self.calculate(1486738185, 1878614288), -2120967792)

    def test0579(self):
        self.assertEquals(self.calculate(1248577949, 718788029), -1255245335)

    def test0580(self):
        self.assertEquals(self.calculate(1835395771, -115676377), -218207363)

    def test0581(self):
        self.assertEquals(self.calculate(1654177593, -2050486091), 1132118861)

    def test0582(self):
        self.assertEquals(self.calculate(1852163321, -946774101), -1575225005)

    def test0583(self):
        self.assertEquals(self.calculate(-1987226221, 2031715547), 1650655425)

    def test0584(self):
        self.assertEquals(self.calculate(-1717991733, 470071486), -1476398422)

    def test0585(self):
        self.assertEquals(self.calculate(951952901, 1854517752), 372197848)

    def test0586(self):
        self.assertEquals(self.calculate(-981135752, 1590423372), 1697272736)

    def test0587(self):
        self.assertEquals(self.calculate(-798650622, -539658287), 319663778)

    def test0588(self):
        self.assertEquals(self.calculate(-1222197657, 1980049540), -1346550500)

    def test0589(self):
        self.assertEquals(self.calculate(250855218, 700244367), -1392914)

    def test0590(self):
        self.assertEquals(self.calculate(1902970884, 202583058), 2136424520)

    def test0591(self):
        self.assertEquals(self.calculate(-1804735612, 121004208), -1917097280)

    def test0592(self):
        self.assertEquals(self.calculate(664799001, 229455085), 1098688037)

    def test0593(self):
        self.assertEquals(self.calculate(-2131501089, -217323505), -591317487)

    def test0594(self):
        self.assertEquals(self.calculate(1387324378, 281037494), 1864302844)

    def test0595(self):
        self.assertEquals(self.calculate(1880152982, -2104181613), -643285214)

    def test0596(self):
        self.assertEquals(self.calculate(1805879220, 1538690001), 556303860)

    def test0597(self):
        self.assertEquals(self.calculate(-413855786, 639391280), 1923931168)

    def test0598(self):
        self.assertEquals(self.calculate(1220045755, 1850623500), 51654340)

    def test0599(self):
        self.assertEquals(self.calculate(766303205, -1601831330), -1516309482)

    def test0600(self):
        self.assertEquals(self.calculate(1233513583, 1449267869), 1312804371)

    def test0601(self):
        self.assertEquals(self.calculate(-8832736, -450376762), 200183488)

    def test0602(self):
        self.assertEquals(self.calculate(55098771, -1623171634), -1020857526)

    def test0603(self):
        self.assertEquals(self.calculate(-1429481651, -772128548), -617462228)

    def test0604(self):
        self.assertEquals(self.calculate(1252268024, -1881235686), -794986704)

    def test0605(self):
        self.assertEquals(self.calculate(1308002537, 234250478), 1399892126)

    def test0606(self):
        self.assertEquals(self.calculate(1062526487, -2136975484), -845392676)

    def test0607(self):
        self.assertEquals(self.calculate(-1247476707, -6734755), 37636745)

    def test0608(self):
        self.assertEquals(self.calculate(-2085419411, -1312018080), 590956000)

    def test0609(self):
        self.assertEquals(self.calculate(-445844786, -1326161106), 1741769476)

    def test0610(self):
        self.assertEquals(self.calculate(-1362496782, -1882483851), -1397555558)

    def test0611(self):
        self.assertEquals(self.calculate(-312350721, 368154856), -1802983656)

    def test0612(self):
        self.assertEquals(self.calculate(1927084975, 551637604), -1145086372)

    def test0613(self):
        self.assertEquals(self.calculate(1974858764, 2064265553), 1589674956)

    def test0614(self):
        self.assertEquals(self.calculate(1176895216, -60595603), 1083534384)

    def test0615(self):
        self.assertEquals(self.calculate(36173898, 1449591603), -1482337090)

    def test0616(self):
        self.assertEquals(self.calculate(-2117056821, -751112389), -1206528567)

    def test0617(self):
        self.assertEquals(self.calculate(-1479544966, 1643039991), 2044806838)

    def test0618(self):
        self.assertEquals(self.calculate(-389397934, 1520167271), -1151119106)

    def test0619(self):
        self.assertEquals(self.calculate(1355299075, 1776565159), -647175691)

    def test0620(self):
        self.assertEquals(self.calculate(-942363307, 1490444469), 661417241)

    def test0621(self):
        self.assertEquals(self.calculate(-1485285785, -1030579641), 722988177)

    def test0622(self):
        self.assertEquals(self.calculate(1168942147, 671039686), -531313710)

    def test0623(self):
        self.assertEquals(self.calculate(-1511411658, 1649259661), 1574569406)

    def test0624(self):
        self.assertEquals(self.calculate(2063893461, -277132051), 1822967857)

    def test0625(self):
        self.assertEquals(self.calculate(606669189, -1876873663), -1740222267)

    def test0626(self):
        self.assertEquals(self.calculate(-470677557, -415885073), 1367494277)

    def test0627(self):
        self.assertEquals(self.calculate(-1391734995, 1958216642), -1833400550)

    def test0628(self):
        self.assertEquals(self.calculate(-1642998516, -421989845), -226221820)

    def test0629(self):
        self.assertEquals(self.calculate(77937969, -1980304546), -1814562050)

    def test0630(self):
        self.assertEquals(self.calculate(-1686159942, 895068713), 1577608906)

    def test0631(self):
        self.assertEquals(self.calculate(-1610121985, -328093768), 1684219976)

    def test0632(self):
        self.assertEquals(self.calculate(-894391298, 1981273492), -1257257768)

    def test0633(self):
        self.assertEquals(self.calculate(22625093, -505109993), 83492147)

    def test0634(self):
        self.assertEquals(self.calculate(-259092108, 850769402), 924127048)

    def test0635(self):
        self.assertEquals(self.calculate(1159909937, -1088373400), -1603039000)

    def test0636(self):
        self.assertEquals(self.calculate(925166359, 421418882), 1482044078)

    def test0637(self):
        self.assertEquals(self.calculate(1366805255, 2073686581), -806836621)

    def test0638(self):
        self.assertEquals(self.calculate(-562543152, 1990324198), -250877728)

    def test0639(self):
        self.assertEquals(self.calculate(392608946, -923512362), -79819060)

    def test0640(self):
        self.assertEquals(self.calculate(-1391914374, -670447619), -1516365678)

    def test0641(self):
        self.assertEquals(self.calculate(-1155209885, -138655269), -1750239567)

    def test0642(self):
        self.assertEquals(self.calculate(685338554, -374089344), 628786944)

    def test0643(self):
        self.assertEquals(self.calculate(-1389573544, -2015752577), 322515368)

    def test0644(self):
        self.assertEquals(self.calculate(-824829463, 2013186672), 1917530096)

    def test0645(self):
        self.assertEquals(self.calculate(311903904, 1582487869), 136934432)

    def test0646(self):
        self.assertEquals(self.calculate(2072199599, 1358211205), -1726482453)

    def test0647(self):
        self.assertEquals(self.calculate(1893046070, -476282797), 1740834434)

    def test0648(self):
        self.assertEquals(self.calculate(-874188699, 1750871573), 1229315657)

    def test0649(self):
        self.assertEquals(self.calculate(1105514787, 452992145), 175786195)

    def test0650(self):
        self.assertEquals(self.calculate(419201934, -1595232716), -1266598696)

    def test0651(self):
        self.assertEquals(self.calculate(1051457441, 137265683), -2123291917)

    def test0652(self):
        self.assertEquals(self.calculate(1296879240, -1284906438), 528669392)

    def test0653(self):
        self.assertEquals(self.calculate(-1433187545, -1003365519), -1966765769)

    def test0654(self):
        self.assertEquals(self.calculate(2112274497, -272898845), 1162960291)

    def test0655(self):
        self.assertEquals(self.calculate(-1592390359, -109142643), -1704631147)

    def test0656(self):
        self.assertEquals(self.calculate(-983650851, -2093322924), -1909840508)

    def test0657(self):
        self.assertEquals(self.calculate(888668440, 1624481437), 1938652088)

    def test0658(self):
        self.assertEquals(self.calculate(256811673, -716214335), 486534233)

    def test0659(self):
        self.assertEquals(self.calculate(-871767380, 1726205039), -546416492)

    def test0660(self):
        self.assertEquals(self.calculate(1198496315, -1380877401), -1162676867)

    def test0661(self):
        self.assertEquals(self.calculate(-15308316, -352615186), -268697096)

    def test0662(self):
        self.assertEquals(self.calculate(-202842974, 380858497), -98300510)

    def test0663(self):
        self.assertEquals(self.calculate(316100054, -706431527), -1826535322)

    def test0664(self):
        self.assertEquals(self.calculate(-1040263747, 1121328111), 1668446835)

    def test0665(self):
        self.assertEquals(self.calculate(1651877189, -365135119), -1884325899)

    def test0666(self):
        self.assertEquals(self.calculate(-1222699445, -586416930), 455092490)

    def test0667(self):
        self.assertEquals(self.calculate(1475619950, 841401380), 1689155448)

    def test0668(self):
        self.assertEquals(self.calculate(-1795802539, -212391390), -1339510454)

    def test0669(self):
        self.assertEquals(self.calculate(-388993848, 200202538), -1739104048)

    def test0670(self):
        self.assertEquals(self.calculate(240744157, 1368358525), 1554173929)

    def test0671(self):
        self.assertEquals(self.calculate(-1783877937, 1003920739), 1347751181)

    def test0672(self):
        self.assertEquals(self.calculate(1152824713, 1669874452), -1684993612)

    def test0673(self):
        self.assertEquals(self.calculate(-1630154156, 659189204), 736620944)

    def test0674(self):
        self.assertEquals(self.calculate(550590952, 969260832), 600265984)

    def test0675(self):
        self.assertEquals(self.calculate(-1121734222, 610706745), -211400030)

    def test0676(self):
        self.assertEquals(self.calculate(616994625, -1359565353), -1653214057)

    def test0677(self):
        self.assertEquals(self.calculate(-356835209, 1635794862), -357738014)

    def test0678(self):
        self.assertEquals(self.calculate(-733658502, 475623393), 219960122)

    def test0679(self):
        self.assertEquals(self.calculate(68057781, -750355352), 1708098952)

    def test0680(self):
        self.assertEquals(self.calculate(-1859190005, -438804152), 229115416)

    def test0681(self):
        self.assertEquals(self.calculate(1997729512, 2098510864), 1254182528)

    def test0682(self):
        self.assertEquals(self.calculate(-1558087919, 1035624404), 306178324)

    def test0683(self):
        self.assertEquals(self.calculate(-1818787724, 927052738), 1360294888)

    def test0684(self):
        self.assertEquals(self.calculate(-1662939395, 14308471), -1288275045)

    def test0685(self):
        self.assertEquals(self.calculate(-1093858475, -1353200520), -905442344)

    def test0686(self):
        self.assertEquals(self.calculate(-1290165925, -1468272572), -657642452)

    def test0687(self):
        self.assertEquals(self.calculate(-1791077034, -1101432602), -857277628)

    def test0688(self):
        self.assertEquals(self.calculate(786472764, -984638357), -932241900)

    def test0689(self):
        self.assertEquals(self.calculate(-1020559358, -1911170668), 1355920168)

    def test0690(self):
        self.assertEquals(self.calculate(1019660989, 1488938627), -1987834697)

    def test0691(self):
        self.assertEquals(self.calculate(-1911408948, -12355581), -1085651868)

    def test0692(self):
        self.assertEquals(self.calculate(1388595325, -2103406909), -1277653705)

    def test0693(self):
        self.assertEquals(self.calculate(353380466, 91454509), -324774902)

    def test0694(self):
        self.assertEquals(self.calculate(839990438, 1980384450), 1739066828)

    def test0695(self):
        self.assertEquals(self.calculate(-186617823, 1034145305), -970424007)

    def test0696(self):
        self.assertEquals(self.calculate(285058059, -1169578220), -1896415780)

    def test0697(self):
        self.assertEquals(self.calculate(-2029331430, 39176119), 1115524246)

    def test0698(self):
        self.assertEquals(self.calculate(-1573542287, -1426205237), -877395813)

    def test0699(self):
        self.assertEquals(self.calculate(-540316810, 467302577), 176200854)

    def test0700(self):
        self.assertEquals(self.calculate(-1201194283, 1198340992), 501055872)

    def test0701(self):
        self.assertEquals(self.calculate(-1820043175, -745314234), 808407126)

    def test0702(self):
        self.assertEquals(self.calculate(1889058244, -1040954500), -328968464)

    def test0703(self):
        self.assertEquals(self.calculate(433237949, 1861679399), -240805173)

    def test0704(self):
        self.assertEquals(self.calculate(1016752103, -474118113), -395293447)

    def test0705(self):
        self.assertEquals(self.calculate(-632950501, -887773246), 964711286)

    def test0706(self):
        self.assertEquals(self.calculate(936339116, -1318133332), -763484272)

    def test0707(self):
        self.assertEquals(self.calculate(492849186, 1576082681), 1552670994)

    def test0708(self):
        self.assertEquals(self.calculate(1542588630, -2044621315), 1420204414)

    def test0709(self):
        self.assertEquals(self.calculate(-194277723, 899292946), 773325466)

    def test0710(self):
        self.assertEquals(self.calculate(-1872745827, 1913230060), 1517933244)

    def test0711(self):
        self.assertEquals(self.calculate(-644424878, -2145159026), 1689393020)

    def test0712(self):
        self.assertEquals(self.calculate(1635763364, -748539263), -2003689820)

    def test0713(self):
        self.assertEquals(self.calculate(-1725990975, 95440387), 2072720707)

    def test0714(self):
        self.assertEquals(self.calculate(673334053, 1054986203), 52386727)

    def test0715(self):
        self.assertEquals(self.calculate(-1534629404, 1487861510), -615549096)

    def test0716(self):
        self.assertEquals(self.calculate(244601499, -884131764), -2017890812)

    def test0717(self):
        self.assertEquals(self.calculate(156042885, 1975000902), 1467081566)

    def test0718(self):
        self.assertEquals(self.calculate(1302817179, -254562101), 119295465)

    def test0719(self):
        self.assertEquals(self.calculate(-1724125686, 1927009097), 769072858)

    def test0720(self):
        self.assertEquals(self.calculate(735205365, -606998873), -1979570477)

    def test0721(self):
        self.assertEquals(self.calculate(1367259881, -946650252), -1960661868)

    def test0722(self):
        self.assertEquals(self.calculate(372950116, 1066474689), 141360996)

    def test0723(self):
        self.assertEquals(self.calculate(-787882078, -1896479472), 61350944)

    def test0724(self):
        self.assertEquals(self.calculate(-1577678136, 1424200358), 1348210096)

    def test0725(self):
        self.assertEquals(self.calculate(-875192734, -1565557109), 435108662)

    def test0726(self):
        self.assertEquals(self.calculate(-81588959, -551024136), 1368580344)

    def test0727(self):
        self.assertEquals(self.calculate(462370227, -1698964308), 2115954756)

    def test0728(self):
        self.assertEquals(self.calculate(-1748747907, 1871371727), 1303209235)

    def test0729(self):
        self.assertEquals(self.calculate(190411422, 787002424), -1554503024)

    def test0730(self):
        self.assertEquals(self.calculate(558254081, -63369104), -143093648)

    def test0731(self):
        self.assertEquals(self.calculate(-2122549949, -561785735), 1614276779)

    def test0732(self):
        self.assertEquals(self.calculate(-962040758, -281130976), -2089920192)

    def test0733(self):
        self.assertEquals(self.calculate(-146642722, 1378033751), -955817102)

    def test0734(self):
        self.assertEquals(self.calculate(-435905978, -462817333), 1966464898)

    def test0735(self):
        self.assertEquals(self.calculate(-1689451500, -1320943495), 1354165620)

    def test0736(self):
        self.assertEquals(self.calculate(-1794980645, -2115010875), 729433735)

    def test0737(self):
        self.assertEquals(self.calculate(421029317, -1819184828), 855375188)

    def test0738(self):
        self.assertEquals(self.calculate(408692662, 1736661320), 1876652336)

    def test0739(self):
        self.assertEquals(self.calculate(951643299, 1602873430), -993118526)

    def test0740(self):
        self.assertEquals(self.calculate(-1121981874, 921643278), -1491644860)

    def test0741(self):
        self.assertEquals(self.calculate(-1043789320, 1500300896), -1783001856)

    def test0742(self):
        self.assertEquals(self.calculate(-734325133, 2005887852), 982288772)

    def test0743(self):
        self.assertEquals(self.calculate(1039749973, 210408141), -1174391535)

    def test0744(self):
        self.assertEquals(self.calculate(311639308, 1777327865), -1436890964)

    def test0745(self):
        self.assertEquals(self.calculate(818471719, -759463268), -1455343164)

    def test0746(self):
        self.assertEquals(self.calculate(-1324532396, -563781939), -1371343804)

    def test0747(self):
        self.assertEquals(self.calculate(-780520549, -1379339007), -722105701)

    def test0748(self):
        self.assertEquals(self.calculate(-890872527, 167512801), -916991471)

    def test0749(self):
        self.assertEquals(self.calculate(-389982073, 168168774), -813232150)

    def test0750(self):
        self.assertEquals(self.calculate(557477801, -1332262789), 1932144179)

    def test0751(self):
        self.assertEquals(self.calculate(-1850988704, -1628976813), 760947744)

    def test0752(self):
        self.assertEquals(self.calculate(673725151, 2052024720), -2020109200)

    def test0753(self):
        self.assertEquals(self.calculate(-2076237385, 188213223), 1739885857)

    def test0754(self):
        self.assertEquals(self.calculate(-954685466, -1500282104), 1673654576)

    def test0755(self):
        self.assertEquals(self.calculate(-927408295, 29394725), 1547712221)

    def test0756(self):
        self.assertEquals(self.calculate(-1569675274, -1820826553), 204123450)

    def test0757(self):
        self.assertEquals(self.calculate(777953950, 983300025), 317978158)

    def test0758(self):
        self.assertEquals(self.calculate(-1226324165, -400050014), 668695382)

    def test0759(self):
        self.assertEquals(self.calculate(-750807528, -653722845), 1117457736)

    def test0760(self):
        self.assertEquals(self.calculate(1667627059, 907183088), -1825519408)

    def test0761(self):
        self.assertEquals(self.calculate(200847025, -1748208151), 691659801)

    def test0762(self):
        self.assertEquals(self.calculate(-1227208452, 407270215), 1513845220)

    def test0763(self):
        self.assertEquals(self.calculate(-1029503482, 1110705613), -790499122)

    def test0764(self):
        self.assertEquals(self.calculate(-378586816, 1580220337), 16602432)

    def test0765(self):
        self.assertEquals(self.calculate(2127745093, -1207211257), 533170403)

    def test0766(self):
        self.assertEquals(self.calculate(1682210229, -557571281), -94973125)

    def test0767(self):
        self.assertEquals(self.calculate(1678675569, -193421024), 576642848)

    def test0768(self):
        self.assertEquals(self.calculate(-841295071, -639995725), 1124050963)

    def test0769(self):
        self.assertEquals(self.calculate(12485411, 1960515511), -1326914811)

    def test0770(self):
        self.assertEquals(self.calculate(-1032306061, -540976356), 1249453460)

    def test0771(self):
        self.assertEquals(self.calculate(-1735561373, -1564708698), 1059424818)

    def test0772(self):
        self.assertEquals(self.calculate(-785478174, 1638117279), -1211261602)

    def test0773(self):
        self.assertEquals(self.calculate(-2083064613, 1743045877), -264502889)

    def test0774(self):
        self.assertEquals(self.calculate(-861035839, -1638512899), -1930387779)

    def test0775(self):
        self.assertEquals(self.calculate(149519042, 1485187240), 1173544784)

    def test0776(self):
        self.assertEquals(self.calculate(55106197, -1859157154), 49643958)

    def test0777(self):
        self.assertEquals(self.calculate(316608899, -1889385006), 2077928566)

    def test0778(self):
        self.assertEquals(self.calculate(1652236102, -38660815), -540165530)

    def test0779(self):
        self.assertEquals(self.calculate(1456110266, 1181403423), 702867078)

    def test0780(self):
        self.assertEquals(self.calculate(-58114661, 360633945), -1904214813)

    def test0781(self):
        self.assertEquals(self.calculate(2040065434, -118191831), -143820886)

    def test0782(self):
        self.assertEquals(self.calculate(1622725728, -2113711231), -417455008)

    def test0783(self):
        self.assertEquals(self.calculate(-782716183, 803757129), 2092875889)

    def test0784(self):
        self.assertEquals(self.calculate(1220132633, 1829167073), -665994247)

    def test0785(self):
        self.assertEquals(self.calculate(131784447, -1824443683), -1824567261)

    def test0786(self):
        self.assertEquals(self.calculate(-1956792327, -217475424), -685776480)

    def test0787(self):
        self.assertEquals(self.calculate(-1675124506, -842147681), 1921842906)

    def test0788(self):
        self.assertEquals(self.calculate(-851450586, 1626667589), 1614274366)

    def test0789(self):
        self.assertEquals(self.calculate(-822443618, -1140200180), 877353320)

    def test0790(self):
        self.assertEquals(self.calculate(-2065150980, -285626815), -759393540)

    def test0791(self):
        self.assertEquals(self.calculate(1842450266, -1654167799), 205602858)

    def test0792(self):
        self.assertEquals(self.calculate(-485063692, -2002104116), 1060464240)

    def test0793(self):
        self.assertEquals(self.calculate(-2126193658, -1484884648), 489578512)

    def test0794(self):
        self.assertEquals(self.calculate(-1620293290, -1491081326), -1655149300)

    def test0795(self):
        self.assertEquals(self.calculate(-416989929, 1569072568), -643679352)

    def test0796(self):
        self.assertEquals(self.calculate(-1707852341, -589669139), -1687148305)

    def test0797(self):
        self.assertEquals(self.calculate(-186181324, -1329826909), 27748380)

    def test0798(self):
        self.assertEquals(self.calculate(341952791, -1082481927), -1303173793)

    def test0799(self):
        self.assertEquals(self.calculate(-1770027982, 768516079), -563906386)

    def test0800(self):
        self.assertEquals(self.calculate(-1189942499, -1456171937), -2066349117)

    def test0801(self):
        self.assertEquals(self.calculate(-178241092, 1100054502), 747852520)

    def test0802(self):
        self.assertEquals(self.calculate(1007165112, 1744449341), -750577192)

    def test0803(self):
        self.assertEquals(self.calculate(-787158000, 165118501), -1453965744)

    def test0804(self):
        self.assertEquals(self.calculate(-921605288, -1273194191), -2095242280)

    def test0805(self):
        self.assertEquals(self.calculate(1284226878, 661833853), 692113734)

    def test0806(self):
        self.assertEquals(self.calculate(1332734328, 1270814369), -335928200)

    def test0807(self):
        self.assertEquals(self.calculate(425551646, 963187103), -299234910)

    def test0808(self):
        self.assertEquals(self.calculate(-608767758, 1057513490), 583512324)

    def test0809(self):
        self.assertEquals(self.calculate(51524295, 1847920593), -637409929)

    def test0810(self):
        self.assertEquals(self.calculate(-617321761, -814241104), -2119528624)

    def test0811(self):
        self.assertEquals(self.calculate(-75565458, -1302863646), 1494732060)

    def test0812(self):
        self.assertEquals(self.calculate(-33856646, -645782517), 834563646)

    def test0813(self):
        self.assertEquals(self.calculate(84480324, -1801367795), 965598324)

    def test0814(self):
        self.assertEquals(self.calculate(-263098523, 930062071), 555602035)

    def test0815(self):
        self.assertEquals(self.calculate(1049254765, 1850008492), -755297220)

    def test0816(self):
        self.assertEquals(self.calculate(1465317168, 268206038), 1251176992)

    def test0817(self):
        self.assertEquals(self.calculate(-1150156230, -2055954144), 1173274944)

    def test0818(self):
        self.assertEquals(self.calculate(1675655769, 1561344659), 808348443)

    def test0819(self):
        self.assertEquals(self.calculate(-1276069521, -2028593837), 345485821)

    def test0820(self):
        self.assertEquals(self.calculate(716689444, 1335875880), -561837664)

    def test0821(self):
        self.assertEquals(self.calculate(-2058939464, 1354676460), 373452192)

    def test0822(self):
        self.assertEquals(self.calculate(-1461650904, -90036207), -1151935320)

    def test0823(self):
        self.assertEquals(self.calculate(-528450491, -681356245), -536181865)

    def test0824(self):
        self.assertEquals(self.calculate(-1179409111, -911689015), -403409103)

    def test0825(self):
        self.assertEquals(self.calculate(591214249, 1233999684), 1978332132)

    def test0826(self):
        self.assertEquals(self.calculate(-1663016514, -473413816), 816263024)

    def test0827(self):
        self.assertEquals(self.calculate(-1619651491, -2104322947), -143149719)

    def test0828(self):
        self.assertEquals(self.calculate(-472764719, 359343659), 765190939)

    def test0829(self):
        self.assertEquals(self.calculate(1047453221, -363017069), -637859009)

    def test0830(self):
        self.assertEquals(self.calculate(1085124087, 833199224), 1182470088)

    def test0831(self):
        self.assertEquals(self.calculate(1669077098, -97539103), 1406550826)

    def test0832(self):
        self.assertEquals(self.calculate(-72163374, -2105191532), 1846836072)

    def test0833(self):
        self.assertEquals(self.calculate(-1666936852, 1042385450), 503370936)

    def test0834(self):
        self.assertEquals(self.calculate(-1444781245, -729257793), -271366403)

    def test0835(self):
        self.assertEquals(self.calculate(336548281, -960047863), -1096889215)

    def test0836(self):
        self.assertEquals(self.calculate(438641191, 2041126904), -841298232)

    def test0837(self):
        self.assertEquals(self.calculate(-908758328, -1172155823), -908238520)

    def test0838(self):
        self.assertEquals(self.calculate(-364331788, 442483455), 1680940812)

    def test0839(self):
        self.assertEquals(self.calculate(-428456923, -81052771), 1366512049)

    def test0840(self):
        self.assertEquals(self.calculate(-1701552846, 1984264843), -848138714)

    def test0841(self):
        self.assertEquals(self.calculate(1918506445, 1351672811), 760662575)

    def test0842(self):
        self.assertEquals(self.calculate(-1892689960, 642300465), -272940968)

    def test0843(self):
        self.assertEquals(self.calculate(828607296, 1833564494), -737825408)

    def test0844(self):
        self.assertEquals(self.calculate(-824192317, 22060816), -1848358608)

    def test0845(self):
        self.assertEquals(self.calculate(-1148400295, -595168203), -1714890899)

    def test0846(self):
        self.assertEquals(self.calculate(-1075345659, -1921747133), -929060529)

    def test0847(self):
        self.assertEquals(self.calculate(-389730789, -678008854), -895811154)

    def test0848(self):
        self.assertEquals(self.calculate(-1585861979, -615622243), 2033648689)

    def test0849(self):
        self.assertEquals(self.calculate(-1760475948, 435932947), 1556842428)

    def test0850(self):
        self.assertEquals(self.calculate(991700172, -945943), 2036088236)

    def test0851(self):
        self.assertEquals(self.calculate(2043017213, -4009801), -692333093)

    def test0852(self):
        self.assertEquals(self.calculate(-403037070, -115566650), -714117588)

    def test0853(self):
        self.assertEquals(self.calculate(1083489800, -449437746), 946070128)

    def test0854(self):
        self.assertEquals(self.calculate(-1362588890, -164536773), 295044546)

    def test0855(self):
        self.assertEquals(self.calculate(237038430, 1347336400), 982436960)

    def test0856(self):
        self.assertEquals(self.calculate(1037469629, -769656503), -971601435)

    def test0857(self):
        self.assertEquals(self.calculate(176220085, 1150954797), -129659951)

    def test0858(self):
        self.assertEquals(self.calculate(365371687, -734673629), 1607437141)

    def test0859(self):
        self.assertEquals(self.calculate(-59414609, 1724988278), -857595990)

    def test0860(self):
        self.assertEquals(self.calculate(704539851, -316186365), 1730228577)

    def test0861(self):
        self.assertEquals(self.calculate(-1230829344, 1925599998), 198872640)

    def test0862(self):
        self.assertEquals(self.calculate(-1402536528, -251931004), -1195643200)

    def test0863(self):
        self.assertEquals(self.calculate(-446974336, -1877766846), 816418048)

    def test0864(self):
        self.assertEquals(self.calculate(1122749325, -339228857), -2076504293)

    def test0865(self):
        self.assertEquals(self.calculate(-2059846836, 1620585415), -510469100)

    def test0866(self):
        self.assertEquals(self.calculate(75810452, -987002592), -575011200)

    def test0867(self):
        self.assertEquals(self.calculate(-1901825841, -829968788), 20269396)

    def test0868(self):
        self.assertEquals(self.calculate(1814106816, 171315074), 1298449792)

    def test0869(self):
        self.assertEquals(self.calculate(-965977726, -239219726), -194989340)

    def test0870(self):
        self.assertEquals(self.calculate(-1827239963, -1266750517), 944961943)

    def test0871(self):
        self.assertEquals(self.calculate(1657227945, 1257970216), -1167338392)

    def test0872(self):
        self.assertEquals(self.calculate(1356632063, 911311945), 584289207)

    def test0873(self):
        self.assertEquals(self.calculate(918135015, 1418072940), -500496780)

    def test0874(self):
        self.assertEquals(self.calculate(1845030334, 1694330423), -1016547374)

    def test0875(self):
        self.assertEquals(self.calculate(-1138267815, 1450332237), -1201111099)

    def test0876(self):
        self.assertEquals(self.calculate(-11353399, -1338045281), -1795201321)

    def test0877(self):
        self.assertEquals(self.calculate(1052588580, -44894263), 154362436)

    def test0878(self):
        self.assertEquals(self.calculate(-504026173, 1674986941), -456204809)

    def test0879(self):
        self.assertEquals(self.calculate(1504016118, -114614947), -1863838370)

    def test0880(self):
        self.assertEquals(self.calculate(561517705, -2084742572), 1992550132)

    def test0881(self):
        self.assertEquals(self.calculate(-542108297, -1021288012), 1406217900)

    def test0882(self):
        self.assertEquals(self.calculate(1086958642, 476877574), 1873985324)

    def test0883(self):
        self.assertEquals(self.calculate(-294068689, 2031174195), -1552195235)

    def test0884(self):
        self.assertEquals(self.calculate(1551869969, -2111144790), 1995953994)

    def test0885(self):
        self.assertEquals(self.calculate(-1901848364, -229575940), -1287595856)

    def test0886(self):
        self.assertEquals(self.calculate(-1471363704, 1870364364), -960604064)

    def test0887(self):
        self.assertEquals(self.calculate(1665263024, -594594445), -931684848)

    def test0888(self):
        self.assertEquals(self.calculate(-2051825004, 481645732), -1156532528)

    def test0889(self):
        self.assertEquals(self.calculate(-2023444026, 970334700), 2101504136)

    def test0890(self):
        self.assertEquals(self.calculate(-1562766149, -1464870651), -307631449)

    def test0891(self):
        self.assertEquals(self.calculate(541968010, -1648667200), -1240548992)

    def test0892(self):
        self.assertEquals(self.calculate(-2124843452, -815746415), -848870268)

    def test0893(self):
        self.assertEquals(self.calculate(1553417594, -1320221316), -1740175080)

    def test0894(self):
        self.assertEquals(self.calculate(755123567, 699529240), 876153448)

    def test0895(self):
        self.assertEquals(self.calculate(2087460468, 1923022199), 603114476)

    def test0896(self):
        self.assertEquals(self.calculate(-234379270, -957523021), -763211314)

    def test0897(self):
        self.assertEquals(self.calculate(-1415704198, 1730740117), 662221314)

    def test0898(self):
        self.assertEquals(self.calculate(613625821, 568206835), -62431289)

    def test0899(self):
        self.assertEquals(self.calculate(1688525457, -235367464), -770593448)

    def test0900(self):
        self.assertEquals(self.calculate(-468384928, 1493298789), -389180192)

    def test0901(self):
        self.assertEquals(self.calculate(429760377, 1547734605), 2099123557)

    def test0902(self):
        self.assertEquals(self.calculate(897101259, 549476289), 189465355)

    def test0903(self):
        self.assertEquals(self.calculate(-1861092733, -821967128), 1200576696)

    def test0904(self):
        self.assertEquals(self.calculate(437600763, 567174671), 1921179573)

    def test0905(self):
        self.assertEquals(self.calculate(-1014916627, -521114342), -1209824494)

    def test0906(self):
        self.assertEquals(self.calculate(-1567238765, 1939145122), -801785338)

    def test0907(self):
        self.assertEquals(self.calculate(-533081748, 904648017), -1481760980)

    def test0908(self):
        self.assertEquals(self.calculate(-1556213453, 736527366), -651906254)

    def test0909(self):
        self.assertEquals(self.calculate(-180346898, 1572654361), 899462206)

    def test0910(self):
        self.assertEquals(self.calculate(-1476243198, 389498141), 1032238906)

    def test0911(self):
        self.assertEquals(self.calculate(1133116775, 1734680698), -636312810)

    def test0912(self):
        self.assertEquals(self.calculate(1944896495, -1808923757), -1204662467)

    def test0913(self):
        self.assertEquals(self.calculate(-1767173641, -259963424), -1895937248)

    def test0914(self):
        self.assertEquals(self.calculate(2020615140, 1267702106), 893116968)

    def test0915(self):
        self.assertEquals(self.calculate(575957216, -1882195710), 1271574976)

    def test0916(self):
        self.assertEquals(self.calculate(1569034727, -721708183), -1801669441)

    def test0917(self):
        self.assertEquals(self.calculate(-230573719, 1688135063), 577587695)

    def test0918(self):
        self.assertEquals(self.calculate(1502606476, -1161963901), 1853041572)

    def test0919(self):
        self.assertEquals(self.calculate(-1999307007, 785383193), -425859559)

    def test0920(self):
        self.assertEquals(self.calculate(-791170906, -1087643119), -836286714)

    def test0921(self):
        self.assertEquals(self.calculate(-97273714, 224469187), 809849898)

    def test0922(self):
        self.assertEquals(self.calculate(52255863, 866801332), 700120492)

    def test0923(self):
        self.assertEquals(self.calculate(2013572875, -576251244), -1951838116)

    def test0924(self):
        self.assertEquals(self.calculate(92164861, -728658193), -1203449805)

    def test0925(self):
        self.assertEquals(self.calculate(344232822, 1228914608), -181114080)

    def test0926(self):
        self.assertEquals(self.calculate(1690894407, -1182873230), 615243422)

    def test0927(self):
        self.assertEquals(self.calculate(-1605972584, -402851808), 698675968)

    def test0928(self):
        self.assertEquals(self.calculate(923497798, -1821814677), -500833214)

    def test0929(self):
        self.assertEquals(self.calculate(-771102630, -194802693), -206721474)

    def test0930(self):
        self.assertEquals(self.calculate(1027557648, -2113039127), 715571088)

    def test0931(self):
        self.assertEquals(self.calculate(1074601859, 271323255), 848680421)

    def test0932(self):
        self.assertEquals(self.calculate(-1547150313, 683577517), 1397042059)

    def test0933(self):
        self.assertEquals(self.calculate(-582962767, -340261591), -452138407)

    def test0934(self):
        self.assertEquals(self.calculate(-324392259, -1851973102), -2138236086)

    def test0935(self):
        self.assertEquals(self.calculate(-1266293773, -1828660825), -896487803)

    def test0936(self):
        self.assertEquals(self.calculate(-1155992509, 1632865509), -1751112721)

    def test0937(self):
        self.assertEquals(self.calculate(-866742783, 719947054), 406653230)

    def test0938(self):
        self.assertEquals(self.calculate(1193886448, 1488748938), -818346656)

    def test0939(self):
        self.assertEquals(self.calculate(1323204856, 986426364), -1210803168)

    def test0940(self):
        self.assertEquals(self.calculate(-699013969, 1866378597), -556827637)

    def test0941(self):
        self.assertEquals(self.calculate(-2055837830, 1172004040), 957263696)

    def test0942(self):
        self.assertEquals(self.calculate(-933157666, 1593213905), 1048621886)

    def test0943(self):
        self.assertEquals(self.calculate(1476707005, 546030401), 1445619965)

    def test0944(self):
        self.assertEquals(self.calculate(1616094843, -2034438007), -1658099757)

    def test0945(self):
        self.assertEquals(self.calculate(-1364047725, -1930905804), 391107292)

    def test0946(self):
        self.assertEquals(self.calculate(-43390964, 695190149), 1930602044)

    def test0947(self):
        self.assertEquals(self.calculate(1230021548, -130873672), -787502176)

    def test0948(self):
        self.assertEquals(self.calculate(211655461, -1950706879), -2080595099)

    def test0949(self):
        self.assertEquals(self.calculate(387682383, -591329089), -912121103)

    def test0950(self):
        self.assertEquals(self.calculate(-979368080, -1052275346), -1897143776)

    def test0951(self):
        self.assertEquals(self.calculate(1872901322, -1794644646), 1539653892)

    def test0952(self):
        self.assertEquals(self.calculate(1703832499, 91200715), -2094171407)

    def test0953(self):
        self.assertEquals(self.calculate(-1972126136, 767716877), -1640785496)

    def test0954(self):
        self.assertEquals(self.calculate(-853282089, -431665391), 1430681927)

    def test0955(self):
        self.assertEquals(self.calculate(-909372632, 575815433), -1011645336)

    def test0956(self):
        self.assertEquals(self.calculate(-936712548, 576836623), 1519956772)

    def test0957(self):
        self.assertEquals(self.calculate(686197372, 258255631), -1066208956)

    def test0958(self):
        self.assertEquals(self.calculate(-749415076, 1493048645), -481235508)

    def test0959(self):
        self.assertEquals(self.calculate(-1419897808, -1933496199), 460360368)

    def test0960(self):
        self.assertEquals(self.calculate(125797537, 1523461822), -838378114)

    def test0961(self):
        self.assertEquals(self.calculate(-1263097015, 1968762645), -1694682115)

    def test0962(self):
        self.assertEquals(self.calculate(-526292577, -2094925441), 1783500001)

    def test0963(self):
        self.assertEquals(self.calculate(1873836672, 207376276), 232018432)

    def test0964(self):
        self.assertEquals(self.calculate(1674923390, 1176632859), -1684000694)

    def test0965(self):
        self.assertEquals(self.calculate(487473266, 1680292446), 1060339164)

    def test0966(self):
        self.assertEquals(self.calculate(-1873237319, 633563550), 1017790254)

    def test0967(self):
        self.assertEquals(self.calculate(-482088215, 1920048541), 2056320485)

    def test0968(self):
        self.assertEquals(self.calculate(-764051235, -1737269729), -1127038781)

    def test0969(self):
        self.assertEquals(self.calculate(-1358025562, 1921559757), 1485392110)

    def test0970(self):
        self.assertEquals(self.calculate(-434818806, -730777964), 1778546120)

    def test0971(self):
        self.assertEquals(self.calculate(-760356201, -604883214), 904531134)

    def test0972(self):
        self.assertEquals(self.calculate(-1154115919, 2131482208), 1219197024)

    def test0973(self):
        self.assertEquals(self.calculate(-1815649624, -2042824574), 1110628688)

    def test0974(self):
        self.assertEquals(self.calculate(-1334562930, -650423679), 1971417742)

    def test0975(self):
        self.assertEquals(self.calculate(577416682, -366895803), 43213330)

    def test0976(self):
        self.assertEquals(self.calculate(-187674147, 2121444811), 585974591)

    def test0977(self):
        self.assertEquals(self.calculate(-1821385979, -727911901), -2141082705)

    def test0978(self):
        self.assertEquals(self.calculate(1362610644, 1402311531), 798627740)

    def test0979(self):
        self.assertEquals(self.calculate(-1409602116, -1910511377), 45486724)

    def test0980(self):
        self.assertEquals(self.calculate(449114490, -2014661380), -483689448)

    def test0981(self):
        self.assertEquals(self.calculate(-39844167, -1795703936), 627801984)

    def test0982(self):
        self.assertEquals(self.calculate(1883688485, 293841437), -1361515471)

    def test0983(self):
        self.assertEquals(self.calculate(1407523546, -2001936122), 779107100)

    def test0984(self):
        self.assertEquals(self.calculate(1166267037, 2001101681), 999337549)

    def test0985(self):
        self.assertEquals(self.calculate(276122604, 2064997461), 1016530268)

    def test0986(self):
        self.assertEquals(self.calculate(457063715, 526323839), 1420788829)

    def test0987(self):
        self.assertEquals(self.calculate(610250579, 767742005), -1171735505)

    def test0988(self):
        self.assertEquals(self.calculate(-94456221, 661329509), 996898575)

    def test0989(self):
        self.assertEquals(self.calculate(-1496861327, 231881924), 320824964)

    def test0990(self):
        self.assertEquals(self.calculate(1242478161, -1481944235), -82195483)

    def test0991(self):
        self.assertEquals(self.calculate(-2002865477, 1948063156), 258867836)

    def test0992(self):
        self.assertEquals(self.calculate(-1519998694, -1183451769), -1948578122)

    def test0993(self):
        self.assertEquals(self.calculate(1066883942, 238999521), -1199702362)

    def test0994(self):
        self.assertEquals(self.calculate(1912797987, -1316964560), 1184177040)

    def test0995(self):
        self.assertEquals(self.calculate(-857094080, 908529866), 1320944256)

    def test0996(self):
        self.assertEquals(self.calculate(-1027776173, 1846342018), 1722715942)

    def test0997(self):
        self.assertEquals(self.calculate(-709065924, -505633907), 1140030476)

    def test0998(self):
        self.assertEquals(self.calculate(-1822571394, 926840801), -1002158914)

    def test0999(self):
        self.assertEquals(self.calculate(1665649220, -2017281382), 95229160)

    def test1000(self):
        self.assertEquals(self.calculate(745888004, -350700684), -510508592)

    def test1001(self):
        self.assertEquals(self.calculate(-1932882659, -608383369), -536809861)

    def test1002(self):
        self.assertEquals(self.calculate(1954677607, 2003671628), 545257620)

    def test1003(self):
        self.assertEquals(self.calculate(402516292, 2023958634), 31536680)

    def test1004(self):
        self.assertEquals(self.calculate(1999635159, -929336999), 1360978879)

    def test1005(self):
        self.assertEquals(self.calculate(503231698, 1263818760), 1493554832)

    def test1006(self):
        self.assertEquals(self.calculate(-1493027347, 1229167192), 1866079096)

    def test1007(self):
        self.assertEquals(self.calculate(902845076, -666694066), 1186545944)

    def test1008(self):
        self.assertEquals(self.calculate(652020554, 1845803718), -1571651780)

    def test1009(self):
        self.assertEquals(self.calculate(-576014950, -22848717), 1151200174)

    def test1010(self):
        self.assertEquals(self.calculate(-865213602, -1832594065), -1043674174)

    def test1011(self):
        self.assertEquals(self.calculate(8775607, -265567590), 1172509206)

    def test1012(self):
        self.assertEquals(self.calculate(1675458941, 1676493550), -1057870794)

    def test1013(self):
        self.assertEquals(self.calculate(-2125210280, 646451863), -725106968)

    def test1014(self):
        self.assertEquals(self.calculate(-592783543, 1304195581), -1938162651)

    def test1015(self):
        self.assertEquals(self.calculate(-984825741, 2050335161), 2135844379)

    def test1016(self):
        self.assertEquals(self.calculate(-316043479, -67039387), -336469459)

    def test1017(self):
        self.assertEquals(self.calculate(1635323043, -2135743537), -1282113331)

    def test1018(self):
        self.assertEquals(self.calculate(1383798514, -654654218), 405623948)

    def test1019(self):
        self.assertEquals(self.calculate(-715871325, -905422357), 1065171361)

    def test1020(self):
        self.assertEquals(self.calculate(578467557, -46943543), 639882189)

    def test1021(self):
        self.assertEquals(self.calculate(-1421722266, 581990853), -618760834)

    def test1022(self):
        self.assertEquals(self.calculate(1735124309, -279937445), -473277641)

    def test1023(self):
        self.assertEquals(self.calculate(255085312, 1553407931), -1387804416)


class TestVM_Mul_LongFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushF(rhs)
        v.VM_Mul()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(1273191300, -140930.0), -179430849909000.00)

    def test0001(self):
        self.assertEquals(self.calculate(-19328649, 14714.0), -284401741386.00)

    def test0002(self):
        self.assertEquals(self.calculate(1296761214, 159505.0), 206839897439070.00)

    def test0003(self):
        self.assertEquals(self.calculate(-1771457337, 54504.0), -96551510695848.00)

    def test0004(self):
        self.assertEquals(self.calculate(-1713068461, -56795.0), 97293723242495.00)

    def test0005(self):
        self.assertEquals(self.calculate(1707413716, -80625.0), -137660230852500.00)

    def test0006(self):
        self.assertEquals(self.calculate(-1318224291, 10967.0), -14456965799397.00)

    def test0007(self):
        self.assertEquals(self.calculate(-289751593, 146838.0), -42546544412934.00)

    def test0008(self):
        self.assertEquals(self.calculate(1494671355, 76457.0), 114278087789235.00)

    def test0009(self):
        self.assertEquals(self.calculate(-2053341100, 106418.0), -218512453179800.00)

    def test0010(self):
        self.assertEquals(self.calculate(938317623, 190159.0), 178429540872057.00)

    def test0011(self):
        self.assertEquals(self.calculate(572080118, -163054.0), -93279951560372.00)

    def test0012(self):
        self.assertEquals(self.calculate(-1748446114, -186521.0), 326121917629394.00)

    def test0013(self):
        self.assertEquals(self.calculate(30009554, 45227.0), 1357242098758.00)

    def test0014(self):
        self.assertEquals(self.calculate(-1116971329, 19841.0), -22161828138689.00)

    def test0015(self):
        self.assertEquals(self.calculate(-1845006008, 126199.0), -232837913203592.00)

    def test0016(self):
        self.assertEquals(self.calculate(-60707543, -20650.0), 1253610762950.00)

    def test0017(self):
        self.assertEquals(self.calculate(-587952088, 120018.0), -70564833697584.00)

    def test0018(self):
        self.assertEquals(self.calculate(453700170, 121037.0), 54914507476290.00)

    def test0019(self):
        self.assertEquals(self.calculate(-566727834, 93338.0), -52897242569892.00)

    def test0020(self):
        self.assertEquals(self.calculate(1575248782, 193588.0), 304949261209816.00)

    def test0021(self):
        self.assertEquals(self.calculate(-392549565, -163919.0), 64346332145235.00)

    def test0022(self):
        self.assertEquals(self.calculate(-1170171694, -40713.0), 47641200177822.00)

    def test0023(self):
        self.assertEquals(self.calculate(875767429, -157587.0), -138009561833823.00)

    def test0024(self):
        self.assertEquals(self.calculate(-994708732, 187127.0), -186136860892964.00)

    def test0025(self):
        self.assertEquals(self.calculate(594509236, -76599.0), -45538812968364.00)

    def test0026(self):
        self.assertEquals(self.calculate(2141013278, 78238.0), 167508596844164.00)

    def test0027(self):
        self.assertEquals(self.calculate(87744739, -27452.0), -2408768575028.00)

    def test0028(self):
        self.assertEquals(self.calculate(-87759180, 7627.0), -669339265860.00)

    def test0029(self):
        self.assertEquals(self.calculate(814781775, 23896.0), 19470025295400.00)

    def test0030(self):
        self.assertEquals(self.calculate(-345449758, 166592.0), -57549166084736.00)

    def test0031(self):
        self.assertEquals(self.calculate(1070017549, 154881.0), 165725388006669.00)

    def test0032(self):
        self.assertEquals(self.calculate(-81771306, -36918.0), 3018833074908.00)

    def test0033(self):
        self.assertEquals(self.calculate(-1776168282, -45055.0), 80025261945510.00)

    def test0034(self):
        self.assertEquals(self.calculate(-1387777537, 15179.0), -21065075234123.00)

    def test0035(self):
        self.assertEquals(self.calculate(-1245064533, 174643.0), -217441805236719.00)

    def test0036(self):
        self.assertEquals(self.calculate(-589140190, 110336.0), -65003372003840.00)

    def test0037(self):
        self.assertEquals(self.calculate(429122404, 7586.0), 3255322556744.00)

    def test0038(self):
        self.assertEquals(self.calculate(-1871689803, -169378.0), 317023075452534.00)

    def test0039(self):
        self.assertEquals(self.calculate(-624395860, 39897.0), -24911521626420.00)

    def test0040(self):
        self.assertEquals(self.calculate(1015738805, 141442.0), 143668128056810.00)

    def test0041(self):
        self.assertEquals(self.calculate(896378052, 189773.0), 170108352062196.00)

    def test0042(self):
        self.assertEquals(self.calculate(1184397136, -68114.0), -80674026521504.00)

    def test0043(self):
        self.assertEquals(self.calculate(247601520, -118500.0), -29340780120000.00)

    def test0044(self):
        self.assertEquals(self.calculate(-614576342, -119291.0), 73313426413522.00)

    def test0045(self):
        self.assertEquals(self.calculate(-1050482946, 278.0), -292034258988.00)

    def test0046(self):
        self.assertEquals(self.calculate(1679715583, -37536.0), -63049804123488.00)

    def test0047(self):
        self.assertEquals(self.calculate(1734319674, -147036.0), -255007427586264.00)

    def test0048(self):
        self.assertEquals(self.calculate(-1550020359, -138619.0), 214862272144221.00)

    def test0049(self):
        self.assertEquals(self.calculate(197345550, -48181.0), -9508305944550.00)

    def test0050(self):
        self.assertEquals(self.calculate(1590163264, -188757.0), -300154447222848.00)

    def test0051(self):
        self.assertEquals(self.calculate(-397522044, 93782.0), -37280412330408.00)

    def test0052(self):
        self.assertEquals(self.calculate(845354513, -89537.0), -75690507030481.00)

    def test0053(self):
        self.assertEquals(self.calculate(-1473760685, 40941.0), -60337236204585.00)

    def test0054(self):
        self.assertEquals(self.calculate(1581218732, 57427.0), 90804648122564.00)

    def test0055(self):
        self.assertEquals(self.calculate(1012929806, 87456.0), 88586789113536.00)

    def test0056(self):
        self.assertEquals(self.calculate(622883096, -127829.0), -79622523278584.00)

    def test0057(self):
        self.assertEquals(self.calculate(124001799, 102915.0), 12761645144085.00)

    def test0058(self):
        self.assertEquals(self.calculate(1613096008, 187225.0), 302011900097800.00)

    def test0059(self):
        self.assertEquals(self.calculate(-1995515941, -51528.0), 102824945407848.00)

    def test0060(self):
        self.assertEquals(self.calculate(-1959146736, -44449.0), 87082113268464.00)

    def test0061(self):
        self.assertEquals(self.calculate(2011842, 33059.0), 66509484678.00)

    def test0062(self):
        self.assertEquals(self.calculate(-2082856217, 143300.0), -298473295896100.00)

    def test0063(self):
        self.assertEquals(self.calculate(313874053, 164125.0), 51514578948625.00)

    def test0064(self):
        self.assertEquals(self.calculate(-1490143094, -78988.0), 117703422708872.00)

    def test0065(self):
        self.assertEquals(self.calculate(-1174350225, -197417.0), 231836698368825.00)

    def test0066(self):
        self.assertEquals(self.calculate(335162585, 17330.0), 5808367598050.00)

    def test0067(self):
        self.assertEquals(self.calculate(197963424, -78956.0), -15630400105344.00)

    def test0068(self):
        self.assertEquals(self.calculate(117075585, 26546.0), 3107888479410.00)

    def test0069(self):
        self.assertEquals(self.calculate(-262240563, -148980.0), 39068599075740.00)

    def test0070(self):
        self.assertEquals(self.calculate(-1915261391, -148725.0), 284847250376475.00)

    def test0071(self):
        self.assertEquals(self.calculate(-552227499, -81310.0), 44901617943690.00)

    def test0072(self):
        self.assertEquals(self.calculate(913408568, 114025.0), 104151411966200.00)

    def test0073(self):
        self.assertEquals(self.calculate(504159557, 163225.0), 82291443691325.00)

    def test0074(self):
        self.assertEquals(self.calculate(1637730808, 159362.0), 260992057024496.00)

    def test0075(self):
        self.assertEquals(self.calculate(1483826753, -101029.0), -149909533028837.00)

    def test0076(self):
        self.assertEquals(self.calculate(-845048456, 110338.0), -93240956538128.00)

    def test0077(self):
        self.assertEquals(self.calculate(1760964026, 27408.0), 48264502024608.00)

    def test0078(self):
        self.assertEquals(self.calculate(1787144300, 165488.0), 295750935918400.00)

    def test0079(self):
        self.assertEquals(self.calculate(2025450984, 25092.0), 50822616090528.00)

    def test0080(self):
        self.assertEquals(self.calculate(-1037774790, -81931.0), 85025926319490.00)

    def test0081(self):
        self.assertEquals(self.calculate(1626193943, 196241.0), 319125925568263.00)

    def test0082(self):
        self.assertEquals(self.calculate(-965605084, 167264.0), -161510968770176.00)

    def test0083(self):
        self.assertEquals(self.calculate(1050462227, 160744.0), 168855500216888.00)

    def test0084(self):
        self.assertEquals(self.calculate(1058689287, 184582.0), 195414985973034.00)

    def test0085(self):
        self.assertEquals(self.calculate(1977402623, -52638.0), -104086519269474.00)

    def test0086(self):
        self.assertEquals(self.calculate(710594834, 65506.0), 46548225196004.00)

    def test0087(self):
        self.assertEquals(self.calculate(1409445715, -198197.0), -279347912375855.00)

    def test0088(self):
        self.assertEquals(self.calculate(-1904985067, 149278.0), -284372360831626.00)

    def test0089(self):
        self.assertEquals(self.calculate(1549010266, -7958.0), -12327023696828.00)

    def test0090(self):
        self.assertEquals(self.calculate(620268855, 133531.0), 82825120477005.00)

    def test0091(self):
        self.assertEquals(self.calculate(-1287347032, -16311.0), 20997917438952.00)

    def test0092(self):
        self.assertEquals(self.calculate(-316384295, 157385.0), -49794142268575.00)

    def test0093(self):
        self.assertEquals(self.calculate(843268270, -131577.0), -110954709161790.00)

    def test0094(self):
        self.assertEquals(self.calculate(933824788, 99802.0), 93197581491976.00)

    def test0095(self):
        self.assertEquals(self.calculate(789551757, 186789.0), 147479583138273.00)

    def test0096(self):
        self.assertEquals(self.calculate(-569264965, 163499.0), -93074252512535.00)

    def test0097(self):
        self.assertEquals(self.calculate(-1182888856, -136130.0), 161026659967280.00)

    def test0098(self):
        self.assertEquals(self.calculate(-166497903, 131669.0), -21922612390107.00)

    def test0099(self):
        self.assertEquals(self.calculate(232169469, -112623.0), -26147622107187.00)

    def test0100(self):
        self.assertEquals(self.calculate(-1416079313, 97634.0), -138257487645442.00)

    def test0101(self):
        self.assertEquals(self.calculate(1149478862, 152986.0), 175854173181932.00)

    def test0102(self):
        self.assertEquals(self.calculate(2112044735, 29538.0), 62385577382430.00)

    def test0103(self):
        self.assertEquals(self.calculate(542304049, 92438.0), 50129501681462.00)

    def test0104(self):
        self.assertEquals(self.calculate(1888200894, 169979.0), 320954499761226.00)

    def test0105(self):
        self.assertEquals(self.calculate(-1587101877, -7686.0), 12198465026622.00)

    def test0106(self):
        self.assertEquals(self.calculate(1903439687, -92559.0), -176180473989033.00)

    def test0107(self):
        self.assertEquals(self.calculate(1330450112, 113398.0), 150870381800576.00)

    def test0108(self):
        self.assertEquals(self.calculate(2052643179, 172743.0), 354579740669997.00)

    def test0109(self):
        self.assertEquals(self.calculate(784945021, 193489.0), 151878227168269.00)

    def test0110(self):
        self.assertEquals(self.calculate(-980327115, 94290.0), -92435043673350.00)

    def test0111(self):
        self.assertEquals(self.calculate(-944008707, 58549.0), -55270765786143.00)

    def test0112(self):
        self.assertEquals(self.calculate(-295887954, 193608.0), -57286274998032.00)

    def test0113(self):
        self.assertEquals(self.calculate(1265975309, 105217.0), 133202124087053.00)

    def test0114(self):
        self.assertEquals(self.calculate(-1729966432, -17534.0), 30333231418688.00)

    def test0115(self):
        self.assertEquals(self.calculate(-1498019130, -178001.0), 266648903159130.00)

    def test0116(self):
        self.assertEquals(self.calculate(548696270, 160344.0), 87980154716880.00)

    def test0117(self):
        self.assertEquals(self.calculate(1558396985, 76554.0), 119301522789690.00)

    def test0118(self):
        self.assertEquals(self.calculate(-221448858, -108724.0), 24076805637192.00)

    def test0119(self):
        self.assertEquals(self.calculate(756298788, -162057.0), -122563512686916.00)

    def test0120(self):
        self.assertEquals(self.calculate(-1498948767, 151585.0), -227218148845695.00)

    def test0121(self):
        self.assertEquals(self.calculate(-555304316, 148135.0), -82260004850660.00)

    def test0122(self):
        self.assertEquals(self.calculate(-1981818907, 87032.0), -172481663114024.00)

    def test0123(self):
        self.assertEquals(self.calculate(-237738043, -45997.0), 10935236763871.00)

    def test0124(self):
        self.assertEquals(self.calculate(-1416822524, 103652.0), -146856488257648.00)

    def test0125(self):
        self.assertEquals(self.calculate(-874440248, 67023.0), -58607608741704.00)

    def test0126(self):
        self.assertEquals(self.calculate(936784331, -17271.0), -16179202180701.00)

    def test0127(self):
        self.assertEquals(self.calculate(1996084428, 67588.0), 134911354319664.00)

    def test0128(self):
        self.assertEquals(self.calculate(-1816385651, 84343.0), -153199414962293.00)

    def test0129(self):
        self.assertEquals(self.calculate(-1517631932, 65844.0), -99926956930608.00)

    def test0130(self):
        self.assertEquals(self.calculate(1170054386, -153428.0), -179519104335208.00)

    def test0131(self):
        self.assertEquals(self.calculate(350606389, 129681.0), 45466987131909.00)

    def test0132(self):
        self.assertEquals(self.calculate(1488729285, 136874.0), 203768332155090.00)

    def test0133(self):
        self.assertEquals(self.calculate(1759319105, 113583.0), 199828741903215.00)

    def test0134(self):
        self.assertEquals(self.calculate(914052870, 117040.0), 106980747904800.00)

    def test0135(self):
        self.assertEquals(self.calculate(366398938, 43735.0), 16024457553430.00)

    def test0136(self):
        self.assertEquals(self.calculate(821740407, 153228.0), 125913639083796.00)

    def test0137(self):
        self.assertEquals(self.calculate(1136500535, 87343.0), 99265366228505.00)

    def test0138(self):
        self.assertEquals(self.calculate(379023159, -185524.0), -70317892550316.00)

    def test0139(self):
        self.assertEquals(self.calculate(-2000121148, 147675.0), -295367890530900.00)

    def test0140(self):
        self.assertEquals(self.calculate(2020763695, 70520.0), 142504255771400.00)

    def test0141(self):
        self.assertEquals(self.calculate(1120286149, 118708.0), 132986928175492.00)

    def test0142(self):
        self.assertEquals(self.calculate(-490984908, -177521.0), 87160131853068.00)

    def test0143(self):
        self.assertEquals(self.calculate(709832241, 38791.0), 27535102460631.00)

    def test0144(self):
        self.assertEquals(self.calculate(-1885513112, 162945.0), -307234934034840.00)

    def test0145(self):
        self.assertEquals(self.calculate(-1151161316, -140299.0), 161506781473484.00)

    def test0146(self):
        self.assertEquals(self.calculate(1350781395, 134122.0), 181169502260190.00)

    def test0147(self):
        self.assertEquals(self.calculate(166509949, -31893.0), -5310501803457.00)

    def test0148(self):
        self.assertEquals(self.calculate(914225895, 103491.0), 94614152099445.00)

    def test0149(self):
        self.assertEquals(self.calculate(-1794118139, -88040.0), 157954160957560.00)

    def test0150(self):
        self.assertEquals(self.calculate(-1122026340, -62089.0), 69665493424260.00)

    def test0151(self):
        self.assertEquals(self.calculate(-1740515982, 138887.0), -241735043192034.00)

    def test0152(self):
        self.assertEquals(self.calculate(1495114904, -62019.0), -92725531231176.00)

    def test0153(self):
        self.assertEquals(self.calculate(-1343075977, 92226.0), -123866525054802.00)

    def test0154(self):
        self.assertEquals(self.calculate(1523095587, -119679.0), -182282556756573.00)

    def test0155(self):
        self.assertEquals(self.calculate(-1917136045, 51983.0), -99658483027235.00)

    def test0156(self):
        self.assertEquals(self.calculate(547660143, -130636.0), -71544130440948.00)

    def test0157(self):
        self.assertEquals(self.calculate(-1829409440, 96048.0), -175711117893120.00)

    def test0158(self):
        self.assertEquals(self.calculate(-932339990, -150685.0), 140489651393150.00)

    def test0159(self):
        self.assertEquals(self.calculate(460832408, -193058.0), -88967383023664.00)

    def test0160(self):
        self.assertEquals(self.calculate(-856022410, -145231.0), 124320990626710.00)

    def test0161(self):
        self.assertEquals(self.calculate(523617593, -149540.0), -78301774857220.00)

    def test0162(self):
        self.assertEquals(self.calculate(1893258273, -197796.0), -374478913366308.00)

    def test0163(self):
        self.assertEquals(self.calculate(583173839, -72391.0), -42216537379049.00)

    def test0164(self):
        self.assertEquals(self.calculate(-1084281309, -69330.0), 75173223152970.00)

    def test0165(self):
        self.assertEquals(self.calculate(1911384938, 179064.0), 342260232538032.00)

    def test0166(self):
        self.assertEquals(self.calculate(-718343240, -45556.0), 32724844641440.00)

    def test0167(self):
        self.assertEquals(self.calculate(-1908198743, -173880.0), 331797597432840.00)

    def test0168(self):
        self.assertEquals(self.calculate(-1045734808, -83176.0), 86980038390208.00)

    def test0169(self):
        self.assertEquals(self.calculate(-140654258, -153807.0), 21633609460206.00)

    def test0170(self):
        self.assertEquals(self.calculate(-1374602148, -8203.0), 11275861420044.00)

    def test0171(self):
        self.assertEquals(self.calculate(2023662076, -187849.0), -380142897314524.00)

    def test0172(self):
        self.assertEquals(self.calculate(1927237904, 117586.0), 226616196179744.00)

    def test0173(self):
        self.assertEquals(self.calculate(-1488080336, -109136.0), 162403135549696.00)

    def test0174(self):
        self.assertEquals(self.calculate(-1573446547, -16574.0), 26078303069978.00)

    def test0175(self):
        self.assertEquals(self.calculate(-864952280, 45356.0), -39230775611680.00)

    def test0176(self):
        self.assertEquals(self.calculate(1299717321, 77694.0), 100980237537774.00)

    def test0177(self):
        self.assertEquals(self.calculate(467531707, 131790.0), 61616003665530.00)

    def test0178(self):
        self.assertEquals(self.calculate(317904992, -4134.0), -1314219236928.00)

    def test0179(self):
        self.assertEquals(self.calculate(1667821697, -160500.0), -267685382368500.00)

    def test0180(self):
        self.assertEquals(self.calculate(1885488048, 125321.0), 236291247663408.00)

    def test0181(self):
        self.assertEquals(self.calculate(-1562466504, -164965.0), 257752286832360.00)

    def test0182(self):
        self.assertEquals(self.calculate(1570708974, 80679.0), 126723229313346.00)

    def test0183(self):
        self.assertEquals(self.calculate(601616005, 116039.0), 69810919604195.00)

    def test0184(self):
        self.assertEquals(self.calculate(-1398702970, -98324.0), 137526070822280.00)

    def test0185(self):
        self.assertEquals(self.calculate(-1121390946, -48776.0), 54696964782096.00)

    def test0186(self):
        self.assertEquals(self.calculate(587168515, -141763.0), -83238770191945.00)

    def test0187(self):
        self.assertEquals(self.calculate(-423973313, 52964.0), -22455322549732.00)

    def test0188(self):
        self.assertEquals(self.calculate(-1186742719, 164978.0), -195786440295182.00)

    def test0189(self):
        self.assertEquals(self.calculate(-1066903001, -30117.0), 32131917681117.00)

    def test0190(self):
        self.assertEquals(self.calculate(-1374308305, -128797.0), 177006786759085.00)

    def test0191(self):
        self.assertEquals(self.calculate(-1490792010, -196901.0), 293538437561010.00)

    def test0192(self):
        self.assertEquals(self.calculate(473362986, 89247.0), 42246226411542.00)

    def test0193(self):
        self.assertEquals(self.calculate(1198624141, 138308.0), 165779307693428.00)

    def test0194(self):
        self.assertEquals(self.calculate(-1252095448, 143377.0), -179521689047896.00)

    def test0195(self):
        self.assertEquals(self.calculate(112799337, 72602.0), 8189457464874.00)

    def test0196(self):
        self.assertEquals(self.calculate(-1543430639, 60280.0), -93037998918920.00)

    def test0197(self):
        self.assertEquals(self.calculate(-1763137150, -108708.0), 191667113302200.00)

    def test0198(self):
        self.assertEquals(self.calculate(1206020474, -88959.0), -107286375346566.00)

    def test0199(self):
        self.assertEquals(self.calculate(-325106984, 67419.0), -21918387754296.00)

    def test0200(self):
        self.assertEquals(self.calculate(-7606134, 8051.0), -61236984834.00)

    def test0201(self):
        self.assertEquals(self.calculate(-794874643, -46499.0), 36960876024857.00)

    def test0202(self):
        self.assertEquals(self.calculate(1356784257, -153108.0), -207734524020756.00)

    def test0203(self):
        self.assertEquals(self.calculate(-486844933, -107397.0), 52285685269401.00)

    def test0204(self):
        self.assertEquals(self.calculate(-1431611721, -73086.0), 104630774241006.00)

    def test0205(self):
        self.assertEquals(self.calculate(1506389234, 180208.0), 271463391080672.00)

    def test0206(self):
        self.assertEquals(self.calculate(-136228066, 183682.0), -25022643619012.00)

    def test0207(self):
        self.assertEquals(self.calculate(443744746, -102219.0), -45359144191374.00)

    def test0208(self):
        self.assertEquals(self.calculate(1550064617, 96442.0), 149491331792714.00)

    def test0209(self):
        self.assertEquals(self.calculate(2066934998, 83452.0), 172489859453096.00)

    def test0210(self):
        self.assertEquals(self.calculate(777524354, -38907.0), -30251140041078.00)

    def test0211(self):
        self.assertEquals(self.calculate(-161633102, -142462.0), 23026574977124.00)

    def test0212(self):
        self.assertEquals(self.calculate(1048414298, 164812.0), 172791257281976.00)

    def test0213(self):
        self.assertEquals(self.calculate(1339257679, -56830.0), -76110013897570.00)

    def test0214(self):
        self.assertEquals(self.calculate(463606036, 113177.0), 52469540336372.00)

    def test0215(self):
        self.assertEquals(self.calculate(247695280, 46444.0), 11503959584320.00)

    def test0216(self):
        self.assertEquals(self.calculate(1403435800, 71370.0), 100163213046000.00)

    def test0217(self):
        self.assertEquals(self.calculate(-1301692381, 103864.0), -135198977460184.00)

    def test0218(self):
        self.assertEquals(self.calculate(-422207468, 130877.0), -55257246789436.00)

    def test0219(self):
        self.assertEquals(self.calculate(78541616, -113252.0), -8894995095232.00)

    def test0220(self):
        self.assertEquals(self.calculate(446777924, -170945.0), -76374452218180.00)

    def test0221(self):
        self.assertEquals(self.calculate(51535925, -13511.0), -696301882675.00)

    def test0222(self):
        self.assertEquals(self.calculate(2013691998, 24958.0), 50257724886084.00)

    def test0223(self):
        self.assertEquals(self.calculate(2055126770, -167159.0), -343532935746430.00)

    def test0224(self):
        self.assertEquals(self.calculate(223142100, -58787.0), -13117854632700.00)

    def test0225(self):
        self.assertEquals(self.calculate(-993585328, 67718.0), -67283611241504.00)

    def test0226(self):
        self.assertEquals(self.calculate(-147172369, -38653.0), 5688653578957.00)

    def test0227(self):
        self.assertEquals(self.calculate(812378603, -160270.0), -130199918702810.00)

    def test0228(self):
        self.assertEquals(self.calculate(-827982825, 130805.0), -108304293424125.00)

    def test0229(self):
        self.assertEquals(self.calculate(-1028883996, 186484.0), -191870403110064.00)

    def test0230(self):
        self.assertEquals(self.calculate(-1702041053, -184725.0), 314409533515425.00)

    def test0231(self):
        self.assertEquals(self.calculate(683103644, -167276.0), -114266845153744.00)

    def test0232(self):
        self.assertEquals(self.calculate(1839562080, 92043.0), 169318812529440.00)

    def test0233(self):
        self.assertEquals(self.calculate(1997541812, 77679.0), 155167050414348.00)

    def test0234(self):
        self.assertEquals(self.calculate(-3606408, 181404.0), -654216836832.00)

    def test0235(self):
        self.assertEquals(self.calculate(350308275, -84461.0), -29587387214775.00)

    def test0236(self):
        self.assertEquals(self.calculate(-364679313, 50551.0), -18434903951463.00)

    def test0237(self):
        self.assertEquals(self.calculate(-255431514, 115667.0), -29544996929838.00)

    def test0238(self):
        self.assertEquals(self.calculate(16319674, 123202.0), 2010616476148.00)

    def test0239(self):
        self.assertEquals(self.calculate(-451689827, 163389.0), -73801149143703.00)

    def test0240(self):
        self.assertEquals(self.calculate(830179495, -188327.0), -156345213754865.00)

    def test0241(self):
        self.assertEquals(self.calculate(841579508, 71717.0), 60355557575236.00)

    def test0242(self):
        self.assertEquals(self.calculate(1927960590, -52179.0), -100599055625610.00)

    def test0243(self):
        self.assertEquals(self.calculate(1411954142, -128061.0), -180816259378662.00)

    def test0244(self):
        self.assertEquals(self.calculate(-1579154609, 170785.0), -269695919898065.00)

    def test0245(self):
        self.assertEquals(self.calculate(-1082090094, -127967.0), 138471823058898.00)

    def test0246(self):
        self.assertEquals(self.calculate(-789245222, 190854.0), -150630607599588.00)

    def test0247(self):
        self.assertEquals(self.calculate(-1503642605, 60658.0), -91207953134090.00)

    def test0248(self):
        self.assertEquals(self.calculate(1049139553, -108488.0), -113819051825864.00)

    def test0249(self):
        self.assertEquals(self.calculate(425867327, -148187.0), -63108001586149.00)

    def test0250(self):
        self.assertEquals(self.calculate(-1912046109, -101789.0), 194625261389001.00)

    def test0251(self):
        self.assertEquals(self.calculate(-1919672286, 128407.0), -246499359228402.00)

    def test0252(self):
        self.assertEquals(self.calculate(-732446504, -106972.0), 78351267425888.00)

    def test0253(self):
        self.assertEquals(self.calculate(-1219515155, 123593.0), -150723536551915.00)

    def test0254(self):
        self.assertEquals(self.calculate(257725427, -189308.0), -48789485134516.00)

    def test0255(self):
        self.assertEquals(self.calculate(-489098462, -171547.0), 83903373860714.00)

    def test0256(self):
        self.assertEquals(self.calculate(-2018271830, -32632.0), 65860246356560.00)

    def test0257(self):
        self.assertEquals(self.calculate(9970561, 44950.0), 448176716950.00)

    def test0258(self):
        self.assertEquals(self.calculate(-1877136880, -173700.0), 326058676056000.00)

    def test0259(self):
        self.assertEquals(self.calculate(357572877, 31243.0), 11171649396111.00)

    def test0260(self):
        self.assertEquals(self.calculate(-972834930, 168596.0), -164016077858280.00)

    def test0261(self):
        self.assertEquals(self.calculate(-1401007391, -129160.0), 180954114621560.00)

    def test0262(self):
        self.assertEquals(self.calculate(-2076207267, 167213.0), -347168845736871.00)

    def test0263(self):
        self.assertEquals(self.calculate(179196310, 136836.0), 24520506275160.00)

    def test0264(self):
        self.assertEquals(self.calculate(2105030821, -105976.0), -223082746286296.00)

    def test0265(self):
        self.assertEquals(self.calculate(-71017919, 37668.0), -2675102972892.00)

    def test0266(self):
        self.assertEquals(self.calculate(-216492887, -21953.0), 4752668348311.00)

    def test0267(self):
        self.assertEquals(self.calculate(2129047183, 135091.0), 287615112998653.00)

    def test0268(self):
        self.assertEquals(self.calculate(1975765445, -106422.0), -210264910187790.00)

    def test0269(self):
        self.assertEquals(self.calculate(-477136386, -41018.0), 19571180280948.00)

    def test0270(self):
        self.assertEquals(self.calculate(-1296294634, 49832.0), -64596954201488.00)

    def test0271(self):
        self.assertEquals(self.calculate(-267807896, -43568.0), 11667854412928.00)

    def test0272(self):
        self.assertEquals(self.calculate(-61260972, 64611.0), -3958132661892.00)

    def test0273(self):
        self.assertEquals(self.calculate(1267766616, 24351.0), 30871384866216.00)

    def test0274(self):
        self.assertEquals(self.calculate(1771498437, -30821.0), -54599353326777.00)

    def test0275(self):
        self.assertEquals(self.calculate(164587730, -44727.0), -7361515399710.00)

    def test0276(self):
        self.assertEquals(self.calculate(1719229044, 74816.0), 128625840155904.00)

    def test0277(self):
        self.assertEquals(self.calculate(-281319001, 67572.0), -19009287535572.00)

    def test0278(self):
        self.assertEquals(self.calculate(-586281247, -39448.0), 23127622631656.00)

    def test0279(self):
        self.assertEquals(self.calculate(15682365, 103031.0), 1615769748315.00)

    def test0280(self):
        self.assertEquals(self.calculate(-342616389, 102385.0), -35078778987765.00)

    def test0281(self):
        self.assertEquals(self.calculate(-1695945009, 182966.0), -310300274516694.00)

    def test0282(self):
        self.assertEquals(self.calculate(380599872, 159723.0), 60790553355456.00)

    def test0283(self):
        self.assertEquals(self.calculate(2066405796, 24190.0), 49986356205240.00)

    def test0284(self):
        self.assertEquals(self.calculate(-1969526304, 125802.0), -247770348095808.00)

    def test0285(self):
        self.assertEquals(self.calculate(-1745432139, -191623.0), 334464942771597.00)

    def test0286(self):
        self.assertEquals(self.calculate(-1091500803, 15880.0), -17333032751640.00)

    def test0287(self):
        self.assertEquals(self.calculate(411202299, -195656.0), -80454197013144.00)

    def test0288(self):
        self.assertEquals(self.calculate(-2133699293, -194081.0), 414110492484733.00)

    def test0289(self):
        self.assertEquals(self.calculate(-556810740, 92843.0), -51695979533820.00)

    def test0290(self):
        self.assertEquals(self.calculate(748671316, -54760.0), -40997241264160.00)

    def test0291(self):
        self.assertEquals(self.calculate(-31576236, -45675.0), 1442244579300.00)

    def test0292(self):
        self.assertEquals(self.calculate(-1921583263, 30521.0), -58648642770023.00)

    def test0293(self):
        self.assertEquals(self.calculate(-399978799, 37769.0), -15106799259431.00)

    def test0294(self):
        self.assertEquals(self.calculate(1163743556, 78924.0), 91847296413744.00)

    def test0295(self):
        self.assertEquals(self.calculate(1377909960, -53226.0), -73340635530960.00)

    def test0296(self):
        self.assertEquals(self.calculate(-1393631216, -189124.0), 263569110094784.00)

    def test0297(self):
        self.assertEquals(self.calculate(371634154, 193834.0), 72035334606436.00)

    def test0298(self):
        self.assertEquals(self.calculate(-812950814, 158381.0), -128755962872134.00)

    def test0299(self):
        self.assertEquals(self.calculate(1094332443, 105103.0), 115017622756629.00)

    def test0300(self):
        self.assertEquals(self.calculate(1090462505, 65282.0), 71187573251410.00)

    def test0301(self):
        self.assertEquals(self.calculate(673858955, -77063.0), -51929592649165.00)

    def test0302(self):
        self.assertEquals(self.calculate(-2121271781, -54780.0), 116203268163180.00)

    def test0303(self):
        self.assertEquals(self.calculate(1779376789, -57366.0), -102075728877774.00)

    def test0304(self):
        self.assertEquals(self.calculate(680467909, -11466.0), -7802245044594.00)

    def test0305(self):
        self.assertEquals(self.calculate(1975516593, 195244.0), 385707761683692.00)

    def test0306(self):
        self.assertEquals(self.calculate(-1832710879, -92672.0), 169840982578688.00)

    def test0307(self):
        self.assertEquals(self.calculate(1598769464, 144884.0), 231636115022176.00)

    def test0308(self):
        self.assertEquals(self.calculate(-1310213868, 39816.0), -52167475368288.00)

    def test0309(self):
        self.assertEquals(self.calculate(-1710470128, 129643.0), -221750478804304.00)

    def test0310(self):
        self.assertEquals(self.calculate(735120980, 98236.0), 72215344591280.00)

    def test0311(self):
        self.assertEquals(self.calculate(-1302387948, 44862.0), -58427728123176.00)

    def test0312(self):
        self.assertEquals(self.calculate(1782506656, 198298.0), 353467504871488.00)

    def test0313(self):
        self.assertEquals(self.calculate(-1219463078, 142775.0), -174108840961450.00)

    def test0314(self):
        self.assertEquals(self.calculate(-1831020865, -189731.0), 347401419737315.00)

    def test0315(self):
        self.assertEquals(self.calculate(-1094860143, -193444.0), 211794125502492.00)

    def test0316(self):
        self.assertEquals(self.calculate(139046408, -58846.0), -8182324925168.00)

    def test0317(self):
        self.assertEquals(self.calculate(1452763812, -174330.0), -253260315345960.00)

    def test0318(self):
        self.assertEquals(self.calculate(-505479374, 159219.0), -80481920448906.00)

    def test0319(self):
        self.assertEquals(self.calculate(618036487, 73943.0), 45699471958241.00)

    def test0320(self):
        self.assertEquals(self.calculate(-445062835, -64601.0), 28751504203835.00)

    def test0321(self):
        self.assertEquals(self.calculate(-1988264945, -166739.0), 331521308664355.00)

    def test0322(self):
        self.assertEquals(self.calculate(58245147, 101867.0), 5933258389449.00)

    def test0323(self):
        self.assertEquals(self.calculate(-1862030792, 48368.0), -90062705347456.00)

    def test0324(self):
        self.assertEquals(self.calculate(2010584098, 14924.0), 30005957078552.00)

    def test0325(self):
        self.assertEquals(self.calculate(-676120013, -149874.0), 101332810828362.00)

    def test0326(self):
        self.assertEquals(self.calculate(-802275380, 14764.0), -11844793710320.00)

    def test0327(self):
        self.assertEquals(self.calculate(-1246644871, -43907.0), 54736436350997.00)

    def test0328(self):
        self.assertEquals(self.calculate(-2036179527, 54449.0), -110867939065623.00)

    def test0329(self):
        self.assertEquals(self.calculate(1684098353, 30873.0), 51993168452169.00)

    def test0330(self):
        self.assertEquals(self.calculate(118717543, -65820.0), -7813988680260.00)

    def test0331(self):
        self.assertEquals(self.calculate(1613405434, 46954.0), 75755838748036.00)

    def test0332(self):
        self.assertEquals(self.calculate(1932961926, 39350.0), 76062051788100.00)

    def test0333(self):
        self.assertEquals(self.calculate(122572302, -115543.0), -14162371489986.00)

    def test0334(self):
        self.assertEquals(self.calculate(-442356243, -132257.0), 58504709630451.00)

    def test0335(self):
        self.assertEquals(self.calculate(30596327, 73304.0), 2242833154408.00)

    def test0336(self):
        self.assertEquals(self.calculate(-1766172765, 26342.0), -46524522975630.00)

    def test0337(self):
        self.assertEquals(self.calculate(71722169, -62680.0), -4495545552920.00)

    def test0338(self):
        self.assertEquals(self.calculate(-1074475479, 77428.0), -83194487388012.00)

    def test0339(self):
        self.assertEquals(self.calculate(-1020030672, -48591.0), 49564310383152.00)

    def test0340(self):
        self.assertEquals(self.calculate(1595265160, 23657.0), 37739187890120.00)

    def test0341(self):
        self.assertEquals(self.calculate(1249972922, 113599.0), 141995673966278.00)

    def test0342(self):
        self.assertEquals(self.calculate(763256024, 30260.0), 23096127286240.00)

    def test0343(self):
        self.assertEquals(self.calculate(-2060995809, 102208.0), -210650259646272.00)

    def test0344(self):
        self.assertEquals(self.calculate(702004763, -80484.0), -56500151345292.00)

    def test0345(self):
        self.assertEquals(self.calculate(710469624, -190141.0), -135089404776984.00)

    def test0346(self):
        self.assertEquals(self.calculate(-797165792, -182694.0), 145637407203648.00)

    def test0347(self):
        self.assertEquals(self.calculate(-1384528734, 67787.0), -93853049291658.00)

    def test0348(self):
        self.assertEquals(self.calculate(137355284, 152781.0), 20985277644804.00)

    def test0349(self):
        self.assertEquals(self.calculate(2003097501, -9943.0), -19916798452443.00)

    def test0350(self):
        self.assertEquals(self.calculate(-916303552, -32908.0), 30153717289216.00)

    def test0351(self):
        self.assertEquals(self.calculate(254795007, -146052.0), -37213320362364.00)

    def test0352(self):
        self.assertEquals(self.calculate(1840744678, -18945.0), -34872907924710.00)

    def test0353(self):
        self.assertEquals(self.calculate(-1157386108, 98658.0), -114185398643064.00)

    def test0354(self):
        self.assertEquals(self.calculate(600891541, -52424.0), -31501138145384.00)

    def test0355(self):
        self.assertEquals(self.calculate(1288727301, 36418.0), 46932870847818.00)

    def test0356(self):
        self.assertEquals(self.calculate(1671162813, 75024.0), 125377318882512.00)

    def test0357(self):
        self.assertEquals(self.calculate(-1791401530, -197109.0), 353101364176770.00)

    def test0358(self):
        self.assertEquals(self.calculate(-1896572091, -52593.0), 99746415981963.00)

    def test0359(self):
        self.assertEquals(self.calculate(765962175, 97224.0), 74469906502200.00)

    def test0360(self):
        self.assertEquals(self.calculate(-2068986968, -51246.0), 106027306162128.00)

    def test0361(self):
        self.assertEquals(self.calculate(-1788148807, -79470.0), 142104185692290.00)

    def test0362(self):
        self.assertEquals(self.calculate(439952740, -80519.0), -35424554672060.00)

    def test0363(self):
        self.assertEquals(self.calculate(-1379192459, -105903.0), 146060618985477.00)

    def test0364(self):
        self.assertEquals(self.calculate(459082541, -95340.0), -43768929458940.00)

    def test0365(self):
        self.assertEquals(self.calculate(1576223857, 156350.0), 246442600041950.00)

    def test0366(self):
        self.assertEquals(self.calculate(97372849, -134333.0), -13080386924717.00)

    def test0367(self):
        self.assertEquals(self.calculate(1800239536, 144420.0), 259990593789120.00)

    def test0368(self):
        self.assertEquals(self.calculate(-353313303, 118811.0), -41977506842733.00)

    def test0369(self):
        self.assertEquals(self.calculate(1673169550, 67873.0), 113563036867150.00)

    def test0370(self):
        self.assertEquals(self.calculate(-1329905223, 165703.0), -220369285166769.00)

    def test0371(self):
        self.assertEquals(self.calculate(341167464, 190045.0), 64837170695880.00)

    def test0372(self):
        self.assertEquals(self.calculate(-1912934842, -74476.0), 142467735292792.00)

    def test0373(self):
        self.assertEquals(self.calculate(508445170, -4307.0), -2189873347190.00)

    def test0374(self):
        self.assertEquals(self.calculate(-1998218774, -2792.0), 5579026817008.00)

    def test0375(self):
        self.assertEquals(self.calculate(790673299, -153551.0), -121408675734749.00)

    def test0376(self):
        self.assertEquals(self.calculate(-1243879373, 137616.0), -171177703794768.00)

    def test0377(self):
        self.assertEquals(self.calculate(505990267, 188659.0), 95459617781953.00)

    def test0378(self):
        self.assertEquals(self.calculate(-237652076, 182797.0), -43442086536572.00)

    def test0379(self):
        self.assertEquals(self.calculate(19561088, 60274.0), 1179025018112.00)

    def test0380(self):
        self.assertEquals(self.calculate(-842608211, 181341.0), -152799415590951.00)

    def test0381(self):
        self.assertEquals(self.calculate(-118188380, -38656.0), 4568690017280.00)

    def test0382(self):
        self.assertEquals(self.calculate(1095484171, -165744.0), -181569928438224.00)

    def test0383(self):
        self.assertEquals(self.calculate(-303831565, -138446.0), 42064264847990.00)

    def test0384(self):
        self.assertEquals(self.calculate(1848454627, -182817.0), -337928929544259.00)

    def test0385(self):
        self.assertEquals(self.calculate(177548662, -156350.0), -27759733303700.00)

    def test0386(self):
        self.assertEquals(self.calculate(-821254476, -12995.0), 10672201915620.00)

    def test0387(self):
        self.assertEquals(self.calculate(-1338711680, -91122.0), 121986085704960.00)

    def test0388(self):
        self.assertEquals(self.calculate(1966411831, -77431.0), -152261234486161.00)

    def test0389(self):
        self.assertEquals(self.calculate(810424905, -84222.0), -68255606348910.00)

    def test0390(self):
        self.assertEquals(self.calculate(-1546847269, -167056.0), 258410117370064.00)

    def test0391(self):
        self.assertEquals(self.calculate(494610461, 83524.0), 41311844144564.00)

    def test0392(self):
        self.assertEquals(self.calculate(-1870325662, -184361.0), 344815109371982.00)

    def test0393(self):
        self.assertEquals(self.calculate(-1382048890, 104919.0), -145003187489910.00)

    def test0394(self):
        self.assertEquals(self.calculate(-1782917096, 168343.0), -300141612691928.00)

    def test0395(self):
        self.assertEquals(self.calculate(-506547205, 15096.0), -7646836606680.00)

    def test0396(self):
        self.assertEquals(self.calculate(1601811102, 28930.0), 46340395180860.00)

    def test0397(self):
        self.assertEquals(self.calculate(1724775073, -160289.0), -276462471676097.00)

    def test0398(self):
        self.assertEquals(self.calculate(1199175353, 154994.0), 185864984662882.00)

    def test0399(self):
        self.assertEquals(self.calculate(430433152, -166138.0), -71511303006976.00)

    def test0400(self):
        self.assertEquals(self.calculate(-1273992697, 198455.0), -252830220683135.00)

    def test0401(self):
        self.assertEquals(self.calculate(1835531041, 9857.0), 18092829471137.00)

    def test0402(self):
        self.assertEquals(self.calculate(1705891151, 173027.0), 295165228184077.00)

    def test0403(self):
        self.assertEquals(self.calculate(1029351415, -47745.0), -49146383309175.00)

    def test0404(self):
        self.assertEquals(self.calculate(1413354287, 49680.0), 70215440978160.00)

    def test0405(self):
        self.assertEquals(self.calculate(601668632, -146326.0), -88039764246032.00)

    def test0406(self):
        self.assertEquals(self.calculate(1469653767, 189224.0), 278093764406808.00)

    def test0407(self):
        self.assertEquals(self.calculate(-1692639495, 184357.0), -312049939379715.00)

    def test0408(self):
        self.assertEquals(self.calculate(1858170232, 189925.0), 352912981312600.00)

    def test0409(self):
        self.assertEquals(self.calculate(1686439548, 70807.0), 119411725075236.00)

    def test0410(self):
        self.assertEquals(self.calculate(529431981, -185191.0), -98046037993371.00)

    def test0411(self):
        self.assertEquals(self.calculate(2015059775, 98028.0), 197532279623700.00)

    def test0412(self):
        self.assertEquals(self.calculate(699905722, -154466.0), -108111637254452.00)

    def test0413(self):
        self.assertEquals(self.calculate(876410430, -107666.0), -94359605356380.00)

    def test0414(self):
        self.assertEquals(self.calculate(1542013270, 166947.0), 257434489386690.00)

    def test0415(self):
        self.assertEquals(self.calculate(1220274143, 123858.0), 151140714803694.00)

    def test0416(self):
        self.assertEquals(self.calculate(-3737970, 73550.0), -274927693500.00)

    def test0417(self):
        self.assertEquals(self.calculate(-890191926, 16775.0), -14932969558650.00)

    def test0418(self):
        self.assertEquals(self.calculate(-724478774, 92440.0), -66970817868560.00)

    def test0419(self):
        self.assertEquals(self.calculate(693763358, -74847.0), -51926106056226.00)

    def test0420(self):
        self.assertEquals(self.calculate(-2027055282, -151020.0), 306125888687640.00)

    def test0421(self):
        self.assertEquals(self.calculate(757858958, -85026.0), -64437715762908.00)

    def test0422(self):
        self.assertEquals(self.calculate(494966242, -14118.0), -6987933404556.00)

    def test0423(self):
        self.assertEquals(self.calculate(-2025022453, -152259.0), 308327893671327.00)

    def test0424(self):
        self.assertEquals(self.calculate(-1596013426, -103829.0), 165712478008154.00)

    def test0425(self):
        self.assertEquals(self.calculate(-196745048, 164607.0), -32385612116136.00)

    def test0426(self):
        self.assertEquals(self.calculate(-202761926, -160836.0), 32611417130136.00)

    def test0427(self):
        self.assertEquals(self.calculate(-1808128945, -143669.0), 259772077399205.00)

    def test0428(self):
        self.assertEquals(self.calculate(1466617162, -50014.0), -73351390740268.00)

    def test0429(self):
        self.assertEquals(self.calculate(342631517, 58602.0), 20078892159234.00)

    def test0430(self):
        self.assertEquals(self.calculate(744659274, -74768.0), -55676684598432.00)

    def test0431(self):
        self.assertEquals(self.calculate(-480055062, -108432.0), 52053330482784.00)

    def test0432(self):
        self.assertEquals(self.calculate(-1724934648, 132160.0), -227967363079680.00)

    def test0433(self):
        self.assertEquals(self.calculate(-410398753, -115648.0), 47461794986944.00)

    def test0434(self):
        self.assertEquals(self.calculate(1300310381, -78817.0), -102486563299277.00)

    def test0435(self):
        self.assertEquals(self.calculate(-2133220417, 49191.0), -104935245532647.00)

    def test0436(self):
        self.assertEquals(self.calculate(-808642822, -122807.0), 99306999041354.00)

    def test0437(self):
        self.assertEquals(self.calculate(-1698425030, 91365.0), -155176602865950.00)

    def test0438(self):
        self.assertEquals(self.calculate(-1720510481, -33024.0), 56818138124544.00)

    def test0439(self):
        self.assertEquals(self.calculate(-894363641, 164023.0), -146696207487743.00)

    def test0440(self):
        self.assertEquals(self.calculate(1406927110, -163617.0), -230197192956870.00)

    def test0441(self):
        self.assertEquals(self.calculate(1541701658, -179385.0), -276558151920330.00)

    def test0442(self):
        self.assertEquals(self.calculate(1768568854, -55688.0), -98488062341552.00)

    def test0443(self):
        self.assertEquals(self.calculate(-1885378061, 182200.0), -343515882714200.00)

    def test0444(self):
        self.assertEquals(self.calculate(-1965960018, 197859.0), -388982883201462.00)

    def test0445(self):
        self.assertEquals(self.calculate(939058207, -39175.0), -36787605259225.00)

    def test0446(self):
        self.assertEquals(self.calculate(1075037044, 97776.0), 105112822014144.00)

    def test0447(self):
        self.assertEquals(self.calculate(1570608737, 30793.0), 48363754838441.00)

    def test0448(self):
        self.assertEquals(self.calculate(-895016713, 181964.0), -162860821164332.00)

    def test0449(self):
        self.assertEquals(self.calculate(664807703, 179609.0), 119405446728127.00)

    def test0450(self):
        self.assertEquals(self.calculate(84957029, -110618.0), -9397776633922.00)

    def test0451(self):
        self.assertEquals(self.calculate(-44638684, -26717.0), 1192611720428.00)

    def test0452(self):
        self.assertEquals(self.calculate(421642580, 52319.0), 22059918143020.00)

    def test0453(self):
        self.assertEquals(self.calculate(-1676431445, -3318.0), 5562399534510.00)

    def test0454(self):
        self.assertEquals(self.calculate(1404737223, 150983.0), 212091440140209.00)

    def test0455(self):
        self.assertEquals(self.calculate(-350438188, 97976.0), -34334531907488.00)

    def test0456(self):
        self.assertEquals(self.calculate(1777765027, -157013.0), -279132220184351.00)

    def test0457(self):
        self.assertEquals(self.calculate(785233262, -126236.0), -99124706061832.00)

    def test0458(self):
        self.assertEquals(self.calculate(-770967071, -68476.0), 52792741153796.00)

    def test0459(self):
        self.assertEquals(self.calculate(1737507434, -114023.0), -198115810146982.00)

    def test0460(self):
        self.assertEquals(self.calculate(-2129810878, -34835.0), 74191961935130.00)

    def test0461(self):
        self.assertEquals(self.calculate(1482831107, 109852.0), 162891962766164.00)

    def test0462(self):
        self.assertEquals(self.calculate(1484355464, 195655.0), 290421568308920.00)

    def test0463(self):
        self.assertEquals(self.calculate(-2076366493, 107954.0), -224152068385322.00)

    def test0464(self):
        self.assertEquals(self.calculate(-1359688848, -20413.0), 27755328454224.00)

    def test0465(self):
        self.assertEquals(self.calculate(686079813, -49387.0), -33883423724631.00)

    def test0466(self):
        self.assertEquals(self.calculate(62274184, -193361.0), -12041398492424.00)

    def test0467(self):
        self.assertEquals(self.calculate(1221704078, 101779.0), 124343819354762.00)

    def test0468(self):
        self.assertEquals(self.calculate(414040697, -167186.0), -69221807968642.00)

    def test0469(self):
        self.assertEquals(self.calculate(-1729981355, 41081.0), -71069364044755.00)

    def test0470(self):
        self.assertEquals(self.calculate(812295735, 20377.0), 16552150192095.00)

    def test0471(self):
        self.assertEquals(self.calculate(-977349372, 15347.0), -14999380812084.00)

    def test0472(self):
        self.assertEquals(self.calculate(-2084892781, 68223.0), -142237640198163.00)

    def test0473(self):
        self.assertEquals(self.calculate(895288242, -13297.0), -11904647753874.00)

    def test0474(self):
        self.assertEquals(self.calculate(1547472098, -176494.0), -273119540464412.00)

    def test0475(self):
        self.assertEquals(self.calculate(1521133137, -155975.0), -237258741043575.00)

    def test0476(self):
        self.assertEquals(self.calculate(1076540651, 188772.0), 203220731770572.00)

    def test0477(self):
        self.assertEquals(self.calculate(1816392481, -30155.0), -54773315264555.00)

    def test0478(self):
        self.assertEquals(self.calculate(1940834547, -61733.0), -119813539089951.00)

    def test0479(self):
        self.assertEquals(self.calculate(-2097503017, 50641.0), -106219650283897.00)

    def test0480(self):
        self.assertEquals(self.calculate(1474206340, 193914.0), 285869248214760.00)

    def test0481(self):
        self.assertEquals(self.calculate(178800562, 93431.0), 16705515308222.00)

    def test0482(self):
        self.assertEquals(self.calculate(488423826, -145871.0), -71246871922446.00)

    def test0483(self):
        self.assertEquals(self.calculate(740092361, 75034.0), 55532090215274.00)

    def test0484(self):
        self.assertEquals(self.calculate(-260462827, -55118.0), 14356190098586.00)

    def test0485(self):
        self.assertEquals(self.calculate(1262483492, 173456.0), 218985336588352.00)

    def test0486(self):
        self.assertEquals(self.calculate(1093642499, -190475.0), -208311554997025.00)

    def test0487(self):
        self.assertEquals(self.calculate(1160583034, 62898.0), 72998351672532.00)

    def test0488(self):
        self.assertEquals(self.calculate(-1242382036, 129785.0), -161242552542260.00)

    def test0489(self):
        self.assertEquals(self.calculate(-486443670, -178424.0), 86793225376080.00)

    def test0490(self):
        self.assertEquals(self.calculate(-345448313, 198755.0), -68659579450315.00)

    def test0491(self):
        self.assertEquals(self.calculate(1251085821, 105293.0), 131730579350553.00)

    def test0492(self):
        self.assertEquals(self.calculate(-749679208, 99267.0), -74418405940536.00)

    def test0493(self):
        self.assertEquals(self.calculate(-228943782, -49237.0), 11272504994334.00)

    def test0494(self):
        self.assertEquals(self.calculate(247581774, 3111.0), 770226898914.00)

    def test0495(self):
        self.assertEquals(self.calculate(1333341009, 10268.0), 13690745480412.00)

    def test0496(self):
        self.assertEquals(self.calculate(-1505478630, 22437.0), -33778424021310.00)

    def test0497(self):
        self.assertEquals(self.calculate(1631418067, 149381.0), 243702862266527.00)

    def test0498(self):
        self.assertEquals(self.calculate(-553559711, -19924.0), 11029123681964.00)

    def test0499(self):
        self.assertEquals(self.calculate(-1785843122, -96022.0), 171480228260684.00)

    def test0500(self):
        self.assertEquals(self.calculate(1810794000, -130853.0), -236947827282000.00)

    def test0501(self):
        self.assertEquals(self.calculate(-36825194, -172805.0), 6363577649170.00)

    def test0502(self):
        self.assertEquals(self.calculate(-1482838198, -46295.0), 68647994376410.00)

    def test0503(self):
        self.assertEquals(self.calculate(2098830863, 39165.0), 82200710749395.00)

    def test0504(self):
        self.assertEquals(self.calculate(-1006369546, -180547.0), 181697002421662.00)

    def test0505(self):
        self.assertEquals(self.calculate(1594061492, 36457.0), 58114699813844.00)

    def test0506(self):
        self.assertEquals(self.calculate(-1772094160, -111971.0), 198423155189360.00)

    def test0507(self):
        self.assertEquals(self.calculate(-123465005, -79737.0), 9844729103685.00)

    def test0508(self):
        self.assertEquals(self.calculate(-22838524, 178792.0), -4083345383008.00)

    def test0509(self):
        self.assertEquals(self.calculate(1849503444, -152397.0), -281858776355268.00)

    def test0510(self):
        self.assertEquals(self.calculate(1992720004, 129824.0), 258702881799296.00)

    def test0511(self):
        self.assertEquals(self.calculate(778018046, -78547.0), -61110983459162.00)

    def test0512(self):
        self.assertEquals(self.calculate(-1700100201, -36233.0), 61599730582833.00)

    def test0513(self):
        self.assertEquals(self.calculate(-818973807, -6045.0), 4950696663315.00)

    def test0514(self):
        self.assertEquals(self.calculate(133743196, 140939.0), 18849632301044.00)

    def test0515(self):
        self.assertEquals(self.calculate(192974569, 192822.0), 37209742343718.00)

    def test0516(self):
        self.assertEquals(self.calculate(-726962912, 67355.0), -48964586937760.00)

    def test0517(self):
        self.assertEquals(self.calculate(344299038, -10447.0), -3596892049986.00)

    def test0518(self):
        self.assertEquals(self.calculate(-316705574, -41503.0), 13144231437722.00)

    def test0519(self):
        self.assertEquals(self.calculate(794681912, -52260.0), -41530076721120.00)

    def test0520(self):
        self.assertEquals(self.calculate(1450921761, -163335.0), -236986305832935.00)

    def test0521(self):
        self.assertEquals(self.calculate(-873188955, -198181.0), 173049460290855.00)

    def test0522(self):
        self.assertEquals(self.calculate(433641218, -13757.0), -5965602236026.00)

    def test0523(self):
        self.assertEquals(self.calculate(-1142867220, 79570.0), -90937944695400.00)

    def test0524(self):
        self.assertEquals(self.calculate(-1235870142, -61754.0), 76319924749068.00)

    def test0525(self):
        self.assertEquals(self.calculate(-1894279825, 137645.0), -260738146512125.00)

    def test0526(self):
        self.assertEquals(self.calculate(-781092954, 323.0), -252293024142.00)

    def test0527(self):
        self.assertEquals(self.calculate(-1155673067, 114460.0), -132278339248820.00)

    def test0528(self):
        self.assertEquals(self.calculate(-282192225, -67825.0), 19139687660625.00)

    def test0529(self):
        self.assertEquals(self.calculate(-1421195544, -116744.0), 165916052588736.00)

    def test0530(self):
        self.assertEquals(self.calculate(-970905258, 47575.0), -46190817649350.00)

    def test0531(self):
        self.assertEquals(self.calculate(1713060873, 77311.0), 132438449152503.00)

    def test0532(self):
        self.assertEquals(self.calculate(-10328243, 53399.0), -551517847957.00)

    def test0533(self):
        self.assertEquals(self.calculate(976867243, 81228.0), 79348972414404.00)

    def test0534(self):
        self.assertEquals(self.calculate(-814516173, 28373.0), -23110267376529.00)

    def test0535(self):
        self.assertEquals(self.calculate(-1910766716, -158525.0), 302904293653900.00)

    def test0536(self):
        self.assertEquals(self.calculate(-1782700673, 117905.0), -210189322850065.00)

    def test0537(self):
        self.assertEquals(self.calculate(-676700696, 192576.0), -130316313232896.00)

    def test0538(self):
        self.assertEquals(self.calculate(-631495032, -11857.0), 7487636594424.00)

    def test0539(self):
        self.assertEquals(self.calculate(1353307492, 11207.0), 15166517062844.00)

    def test0540(self):
        self.assertEquals(self.calculate(1944359126, -199095.0), -387112180190970.00)

    def test0541(self):
        self.assertEquals(self.calculate(952228076, 162122.0), 154377120137272.00)

    def test0542(self):
        self.assertEquals(self.calculate(-227956753, -23103.0), 5266484864559.00)

    def test0543(self):
        self.assertEquals(self.calculate(-255434820, 44087.0), -11261354909340.00)

    def test0544(self):
        self.assertEquals(self.calculate(-1478978330, 155054.0), -229321505979820.00)

    def test0545(self):
        self.assertEquals(self.calculate(-289252527, -84828.0), 24536713360356.00)

    def test0546(self):
        self.assertEquals(self.calculate(1362075162, -63828.0), -86938533440136.00)

    def test0547(self):
        self.assertEquals(self.calculate(-381178111, 144269.0), -54992184895859.00)

    def test0548(self):
        self.assertEquals(self.calculate(-1644890533, -128588.0), 211513183857404.00)

    def test0549(self):
        self.assertEquals(self.calculate(-826892607, -138547.0), 114563490022029.00)

    def test0550(self):
        self.assertEquals(self.calculate(-1484427590, -68889.0), 102260732247510.00)

    def test0551(self):
        self.assertEquals(self.calculate(1925103541, 112025.0), 215659724180525.00)

    def test0552(self):
        self.assertEquals(self.calculate(-1287117116, 36484.0), -46959180860144.00)

    def test0553(self):
        self.assertEquals(self.calculate(-1872970872, 102237.0), -191486923040664.00)

    def test0554(self):
        self.assertEquals(self.calculate(-1712138710, 65321.0), -111838612675910.00)

    def test0555(self):
        self.assertEquals(self.calculate(1763926031, 185744.0), 327638676702064.00)

    def test0556(self):
        self.assertEquals(self.calculate(278508398, -152269.0), -42408195255062.00)

    def test0557(self):
        self.assertEquals(self.calculate(-8805195, -186412.0), 1641394010340.00)

    def test0558(self):
        self.assertEquals(self.calculate(779384099, 167507.0), 130552292271193.00)

    def test0559(self):
        self.assertEquals(self.calculate(353903872, -160965.0), -56966136756480.00)

    def test0560(self):
        self.assertEquals(self.calculate(896708029, 136200.0), 122131633549800.00)

    def test0561(self):
        self.assertEquals(self.calculate(-101150948, 179597.0), -18166406807956.00)

    def test0562(self):
        self.assertEquals(self.calculate(-545441189, -95296.0), 51978363546944.00)

    def test0563(self):
        self.assertEquals(self.calculate(-1167703938, -36835.0), 43012374556230.00)

    def test0564(self):
        self.assertEquals(self.calculate(1641330226, 159743.0), 262191014291918.00)

    def test0565(self):
        self.assertEquals(self.calculate(-1845643490, -148865.0), 274751718138850.00)

    def test0566(self):
        self.assertEquals(self.calculate(-2056035722, -79485.0), 163423999363170.00)

    def test0567(self):
        self.assertEquals(self.calculate(-829977130, -16248.0), 13485468408240.00)

    def test0568(self):
        self.assertEquals(self.calculate(834121482, 141731.0), 118220871765342.00)

    def test0569(self):
        self.assertEquals(self.calculate(-1684519481, -127345.0), 214515133307945.00)

    def test0570(self):
        self.assertEquals(self.calculate(-1444359003, -150099.0), 216796841991297.00)

    def test0571(self):
        self.assertEquals(self.calculate(-1461852824, 37177.0), -54347302437848.00)

    def test0572(self):
        self.assertEquals(self.calculate(988408098, 97458.0), 96328276414884.00)

    def test0573(self):
        self.assertEquals(self.calculate(1475791, 171200.0), 252655419200.00)

    def test0574(self):
        self.assertEquals(self.calculate(-1639076929, -107384.0), 176010636943736.00)

    def test0575(self):
        self.assertEquals(self.calculate(-2147328792, 132142.0), -283752321232464.00)

    def test0576(self):
        self.assertEquals(self.calculate(502206893, -123629.0), -62087335974697.00)

    def test0577(self):
        self.assertEquals(self.calculate(-148979468, -53080.0), 7907830161440.00)

    def test0578(self):
        self.assertEquals(self.calculate(2008896572, 166135.0), 333748031989220.00)

    def test0579(self):
        self.assertEquals(self.calculate(-1998760379, -197004.0), 393763789704516.00)

    def test0580(self):
        self.assertEquals(self.calculate(-132466272, 31776.0), -4209248259072.00)

    def test0581(self):
        self.assertEquals(self.calculate(-950085502, 156692.0), -148870797479384.00)

    def test0582(self):
        self.assertEquals(self.calculate(-192713494, 97412.0), -18772606877528.00)

    def test0583(self):
        self.assertEquals(self.calculate(902346474, 100184.0), 90400679151216.00)

    def test0584(self):
        self.assertEquals(self.calculate(-576832851, -114276.0), 65918150880876.00)

    def test0585(self):
        self.assertEquals(self.calculate(94788284, -95216.0), -9025361249344.00)

    def test0586(self):
        self.assertEquals(self.calculate(-1843174830, 10317.0), -19016034721110.00)

    def test0587(self):
        self.assertEquals(self.calculate(993597204, 70330.0), 69879691357320.00)

    def test0588(self):
        self.assertEquals(self.calculate(-737688668, -111224.0), 82048684409632.00)

    def test0589(self):
        self.assertEquals(self.calculate(1911519325, 32261.0), 61667524943825.00)

    def test0590(self):
        self.assertEquals(self.calculate(1670816475, -56641.0), -94636715960475.00)

    def test0591(self):
        self.assertEquals(self.calculate(1244874809, -149861.0), -186558183751549.00)

    def test0592(self):
        self.assertEquals(self.calculate(1276765720, 185865.0), 237306060547800.00)

    def test0593(self):
        self.assertEquals(self.calculate(2089389286, -193247.0), -403768211351642.00)

    def test0594(self):
        self.assertEquals(self.calculate(-1776403395, 122404.0), -217438881161580.00)

    def test0595(self):
        self.assertEquals(self.calculate(-1524757625, -89776.0), 136886640542000.00)

    def test0596(self):
        self.assertEquals(self.calculate(-363634343, -103604.0), 37673972472172.00)

    def test0597(self):
        self.assertEquals(self.calculate(1438712583, -177772.0), -255762813305076.00)

    def test0598(self):
        self.assertEquals(self.calculate(1803111777, -168266.0), -303402406268682.00)

    def test0599(self):
        self.assertEquals(self.calculate(1831646455, -166900.0), -305701793339500.00)

    def test0600(self):
        self.assertEquals(self.calculate(-146984394, -46455.0), 6828160023270.00)

    def test0601(self):
        self.assertEquals(self.calculate(-2094325030, 105522.0), -220997365815660.00)

    def test0602(self):
        self.assertEquals(self.calculate(1290355150, -186266.0), -240349292369900.00)

    def test0603(self):
        self.assertEquals(self.calculate(-1555907935, -180594.0), 280987637613390.00)

    def test0604(self):
        self.assertEquals(self.calculate(541558846, 171514.0), 92884923912844.00)

    def test0605(self):
        self.assertEquals(self.calculate(-63657617, 114509.0), -7289370065053.00)

    def test0606(self):
        self.assertEquals(self.calculate(577163788, -193789.0), -111847993312732.00)

    def test0607(self):
        self.assertEquals(self.calculate(647919836, -95078.0), -61602922167208.00)

    def test0608(self):
        self.assertEquals(self.calculate(-946709564, 58415.0), -55302039181060.00)

    def test0609(self):
        self.assertEquals(self.calculate(-1709209228, 175074.0), -299238096382872.00)

    def test0610(self):
        self.assertEquals(self.calculate(-1030169152, -79680.0), 82083878031360.00)

    def test0611(self):
        self.assertEquals(self.calculate(980925736, 92449.0), 90685603367464.00)

    def test0612(self):
        self.assertEquals(self.calculate(517745075, -154088.0), -79778303116600.00)

    def test0613(self):
        self.assertEquals(self.calculate(873117855, 25936.0), 22645184687280.00)

    def test0614(self):
        self.assertEquals(self.calculate(-1110947751, 45606.0), -50665883132106.00)

    def test0615(self):
        self.assertEquals(self.calculate(-2079499287, -58090.0), 120798113581830.00)

    def test0616(self):
        self.assertEquals(self.calculate(84061763, 118393.0), 9952324306859.00)

    def test0617(self):
        self.assertEquals(self.calculate(-1820594610, 150027.0), -273138347554470.00)

    def test0618(self):
        self.assertEquals(self.calculate(-750433133, -129666.0), 97305662623578.00)

    def test0619(self):
        self.assertEquals(self.calculate(-1388258730, -153715.0), 213396190681950.00)

    def test0620(self):
        self.assertEquals(self.calculate(-1382367058, -129211.0), 178617029931238.00)

    def test0621(self):
        self.assertEquals(self.calculate(-215293427, -194518.0), 41878446833186.00)

    def test0622(self):
        self.assertEquals(self.calculate(823410440, 73250.0), 60314814730000.00)

    def test0623(self):
        self.assertEquals(self.calculate(175863030, 50576.0), 8894448605280.00)

    def test0624(self):
        self.assertEquals(self.calculate(42925169, -18003.0), -772781817507.00)

    def test0625(self):
        self.assertEquals(self.calculate(86953830, 183553.0), 15960636357990.00)

    def test0626(self):
        self.assertEquals(self.calculate(-210116206, -34987.0), 7351335699322.00)

    def test0627(self):
        self.assertEquals(self.calculate(578699078, -45537.0), -26352219914886.00)

    def test0628(self):
        self.assertEquals(self.calculate(689413144, 154205.0), 106310953870520.00)

    def test0629(self):
        self.assertEquals(self.calculate(1017981367, -64548.0), -65708661277116.00)

    def test0630(self):
        self.assertEquals(self.calculate(-33536934, -12298.0), 412437214332.00)

    def test0631(self):
        self.assertEquals(self.calculate(1429284425, -117472.0), -167900899973600.00)

    def test0632(self):
        self.assertEquals(self.calculate(806932557, 96795.0), 78107036854815.00)

    def test0633(self):
        self.assertEquals(self.calculate(778160034, -196952.0), -153260175016368.00)

    def test0634(self):
        self.assertEquals(self.calculate(-645917039, 191512.0), -123700863972968.00)

    def test0635(self):
        self.assertEquals(self.calculate(505207713, -159930.0), -80797869540090.00)

    def test0636(self):
        self.assertEquals(self.calculate(-1055275397, -197271.0), 208175232841587.00)

    def test0637(self):
        self.assertEquals(self.calculate(-1433675319, -57215.0), 82027733376585.00)

    def test0638(self):
        self.assertEquals(self.calculate(-2079455424, -49482.0), 102895613290368.00)

    def test0639(self):
        self.assertEquals(self.calculate(1807761093, -2098.0), -3792682773114.00)

    def test0640(self):
        self.assertEquals(self.calculate(-1638347793, -173689.0), 284562989818377.00)

    def test0641(self):
        self.assertEquals(self.calculate(189279153, 74433.0), 14088615195249.00)

    def test0642(self):
        self.assertEquals(self.calculate(-1537938395, 182295.0), -280358479716525.00)

    def test0643(self):
        self.assertEquals(self.calculate(-1754475853, 35117.0), -61611928529801.00)

    def test0644(self):
        self.assertEquals(self.calculate(1388682338, 34902.0), 48467790960876.00)

    def test0645(self):
        self.assertEquals(self.calculate(17176336, 150829.0), 2590689582544.00)

    def test0646(self):
        self.assertEquals(self.calculate(-2107778754, -60249.0), 126991562149746.00)

    def test0647(self):
        self.assertEquals(self.calculate(531661339, -10180.0), -5412312431020.00)

    def test0648(self):
        self.assertEquals(self.calculate(338529722, 150291.0), 50877970449102.00)

    def test0649(self):
        self.assertEquals(self.calculate(1366662926, 163592.0), 223575121390192.00)

    def test0650(self):
        self.assertEquals(self.calculate(979438622, -78214.0), -76605812381108.00)

    def test0651(self):
        self.assertEquals(self.calculate(-1915816989, 165981.0), -317989219651209.00)

    def test0652(self):
        self.assertEquals(self.calculate(-1009170531, -169320.0), 170872754308920.00)

    def test0653(self):
        self.assertEquals(self.calculate(-342151691, 84091.0), -28771877847881.00)

    def test0654(self):
        self.assertEquals(self.calculate(-2089793858, 70603.0), -147545715756374.00)

    def test0655(self):
        self.assertEquals(self.calculate(1923614955, -14129.0), -27178755699195.00)

    def test0656(self):
        self.assertEquals(self.calculate(-670387841, -22942.0), 15380037848222.00)

    def test0657(self):
        self.assertEquals(self.calculate(-1974242184, -69811.0), 137823821107224.00)

    def test0658(self):
        self.assertEquals(self.calculate(-2002626063, 160431.0), -321283301913153.00)

    def test0659(self):
        self.assertEquals(self.calculate(1205701965, 161575.0), 194811294994875.00)

    def test0660(self):
        self.assertEquals(self.calculate(988726344, -19316.0), -19098238060704.00)

    def test0661(self):
        self.assertEquals(self.calculate(2018466599, -114584.0), -231283976779816.00)

    def test0662(self):
        self.assertEquals(self.calculate(-774115866, -24555.0), 19008415089630.00)

    def test0663(self):
        self.assertEquals(self.calculate(533842644, 196746.0), 105031404836424.00)

    def test0664(self):
        self.assertEquals(self.calculate(-1028623173, -165142.0), 169868888035566.00)

    def test0665(self):
        self.assertEquals(self.calculate(1341228739, -22689.0), -30431138859171.00)

    def test0666(self):
        self.assertEquals(self.calculate(-1144795737, 195738.0), -224080027968906.00)

    def test0667(self):
        self.assertEquals(self.calculate(729086250, -15254.0), -11121481657500.00)

    def test0668(self):
        self.assertEquals(self.calculate(-920861918, 189489.0), -174493203979902.00)

    def test0669(self):
        self.assertEquals(self.calculate(2054508974, -165672.0), -340374610740528.00)

    def test0670(self):
        self.assertEquals(self.calculate(-447347492, -89673.0), 40114991650116.00)

    def test0671(self):
        self.assertEquals(self.calculate(-1882431637, -60389.0), 113678164126793.00)

    def test0672(self):
        self.assertEquals(self.calculate(-1475256010, 168024.0), -247878415824240.00)

    def test0673(self):
        self.assertEquals(self.calculate(-182372524, 185731.0), -33872231255044.00)

    def test0674(self):
        self.assertEquals(self.calculate(1139801304, -127660.0), -145507034468640.00)

    def test0675(self):
        self.assertEquals(self.calculate(-325235054, 24960.0), -8117866947840.00)

    def test0676(self):
        self.assertEquals(self.calculate(-1788271929, 188875.0), -337759860589875.00)

    def test0677(self):
        self.assertEquals(self.calculate(-1986570472, 67402.0), -133898822953744.00)

    def test0678(self):
        self.assertEquals(self.calculate(-1580560100, 184416.0), -291480571401600.00)

    def test0679(self):
        self.assertEquals(self.calculate(2006472148, 8291.0), 16635660579068.00)

    def test0680(self):
        self.assertEquals(self.calculate(2109963827, -172373.0), -363700794751471.00)

    def test0681(self):
        self.assertEquals(self.calculate(-868707781, 171044.0), -148587253693364.00)

    def test0682(self):
        self.assertEquals(self.calculate(1358489282, -99538.0), -135221306151716.00)

    def test0683(self):
        self.assertEquals(self.calculate(-1396178020, -26093.0), 36430473075860.00)

    def test0684(self):
        self.assertEquals(self.calculate(2097746311, -46592.0), -97738196122112.00)

    def test0685(self):
        self.assertEquals(self.calculate(-402599733, 137249.0), -55256410754517.00)

    def test0686(self):
        self.assertEquals(self.calculate(1764467392, -192099.0), -338952421535808.00)

    def test0687(self):
        self.assertEquals(self.calculate(-93010980, -164032.0), 15256777071360.00)

    def test0688(self):
        self.assertEquals(self.calculate(2083089271, 168527.0), 351056785573817.00)

    def test0689(self):
        self.assertEquals(self.calculate(1297465757, 170223.0), 220858513553811.00)

    def test0690(self):
        self.assertEquals(self.calculate(1970943482, 58939.0), 116165437885598.00)

    def test0691(self):
        self.assertEquals(self.calculate(1177410137, 193044.0), 227291962487028.00)

    def test0692(self):
        self.assertEquals(self.calculate(1544011899, -132787.0), -205024708032513.00)

    def test0693(self):
        self.assertEquals(self.calculate(1907883986, -149593.0), -285406089117698.00)

    def test0694(self):
        self.assertEquals(self.calculate(-347964550, -10794.0), 3755929352700.00)

    def test0695(self):
        self.assertEquals(self.calculate(-1062161354, 15858.0), -16843754751732.00)

    def test0696(self):
        self.assertEquals(self.calculate(-2046056704, 90145.0), -184441781582080.00)

    def test0697(self):
        self.assertEquals(self.calculate(-1079989715, -133223.0), 143879469801445.00)

    def test0698(self):
        self.assertEquals(self.calculate(167211284, 11323.0), 1893333368732.00)

    def test0699(self):
        self.assertEquals(self.calculate(712621898, 137594.0), 98052497433412.00)

    def test0700(self):
        self.assertEquals(self.calculate(-1777071980, -150971.0), 268286333892580.00)

    def test0701(self):
        self.assertEquals(self.calculate(-1153353988, 47286.0), -54537496676568.00)

    def test0702(self):
        self.assertEquals(self.calculate(57269862, 131055.0), 7505501764410.00)

    def test0703(self):
        self.assertEquals(self.calculate(1469601151, 163702.0), 240576647621002.00)

    def test0704(self):
        self.assertEquals(self.calculate(2132894105, -174657.0), -372524885696985.00)

    def test0705(self):
        self.assertEquals(self.calculate(480456392, -147377.0), -70808221683784.00)

    def test0706(self):
        self.assertEquals(self.calculate(1278326902, -83692.0), -106985735082184.00)

    def test0707(self):
        self.assertEquals(self.calculate(-1138427113, -17453.0), 19868968403189.00)

    def test0708(self):
        self.assertEquals(self.calculate(-1968103229, -151240.0), 297655932353960.00)

    def test0709(self):
        self.assertEquals(self.calculate(-1424201978, -166956.0), 237779065438968.00)

    def test0710(self):
        self.assertEquals(self.calculate(-624888245, -75856.0), 47401522712720.00)

    def test0711(self):
        self.assertEquals(self.calculate(606311396, 168558.0), 102198636286968.00)

    def test0712(self):
        self.assertEquals(self.calculate(1411224844, -66534.0), -93894433770696.00)

    def test0713(self):
        self.assertEquals(self.calculate(-892053723, 25843.0), -23053344363489.00)

    def test0714(self):
        self.assertEquals(self.calculate(-282904437, 157923.0), -44677117404351.00)

    def test0715(self):
        self.assertEquals(self.calculate(-2017922710, -101357.0), 204530592117470.00)

    def test0716(self):
        self.assertEquals(self.calculate(-486696032, -130011.0), 63275837816352.00)

    def test0717(self):
        self.assertEquals(self.calculate(1576865377, 176007.0), 277539344409639.00)

    def test0718(self):
        self.assertEquals(self.calculate(82190260, 3209.0), 263748544340.00)

    def test0719(self):
        self.assertEquals(self.calculate(-2064709071, -169731.0), 350445135329901.00)

    def test0720(self):
        self.assertEquals(self.calculate(-854485252, 97605.0), -83402033021460.00)

    def test0721(self):
        self.assertEquals(self.calculate(1662528067, 26121.0), 43426895638107.00)

    def test0722(self):
        self.assertEquals(self.calculate(1632573170, 186254.0), 304073283205180.00)

    def test0723(self):
        self.assertEquals(self.calculate(193110511, 110993.0), 21433914947423.00)

    def test0724(self):
        self.assertEquals(self.calculate(-1759869746, 84329.0), -148408055810434.00)

    def test0725(self):
        self.assertEquals(self.calculate(1832367236, -181114.0), -331867359580904.00)

    def test0726(self):
        self.assertEquals(self.calculate(2038309265, -109588.0), -223374235732820.00)

    def test0727(self):
        self.assertEquals(self.calculate(616257774, -6927.0), -4268817600498.00)

    def test0728(self):
        self.assertEquals(self.calculate(-82943641, -81083.0), 6725319243203.00)

    def test0729(self):
        self.assertEquals(self.calculate(-805535459, 69475.0), -55964576014025.00)

    def test0730(self):
        self.assertEquals(self.calculate(2090466573, 113810.0), 237916000673130.00)

    def test0731(self):
        self.assertEquals(self.calculate(-178040107, -125449.0), 22334953383043.00)

    def test0732(self):
        self.assertEquals(self.calculate(-432215787, -148993.0), 64397126752491.00)

    def test0733(self):
        self.assertEquals(self.calculate(558445082, -161555.0), -90219595222510.00)

    def test0734(self):
        self.assertEquals(self.calculate(824314467, -170836.0), -140822586284412.00)

    def test0735(self):
        self.assertEquals(self.calculate(-1709382981, 191917.0), -328059653564577.00)

    def test0736(self):
        self.assertEquals(self.calculate(758519412, -134534.0), -102046650574008.00)

    def test0737(self):
        self.assertEquals(self.calculate(-1411711186, -191431.0), 270245284047166.00)

    def test0738(self):
        self.assertEquals(self.calculate(3155086, 13200.0), 41647135200.00)

    def test0739(self):
        self.assertEquals(self.calculate(736019656, 86883.0), 63947595772248.00)

    def test0740(self):
        self.assertEquals(self.calculate(1083054789, 52454.0), 56810555902206.00)

    def test0741(self):
        self.assertEquals(self.calculate(-21016702, 190832.0), -4010659276064.00)

    def test0742(self):
        self.assertEquals(self.calculate(280855788, 61762.0), 17346215178456.00)

    def test0743(self):
        self.assertEquals(self.calculate(371907620, 170336.0), 63349256360320.00)

    def test0744(self):
        self.assertEquals(self.calculate(559488702, 29503.0), 16506595175106.00)

    def test0745(self):
        self.assertEquals(self.calculate(82509571, -79795.0), -6583851217945.00)

    def test0746(self):
        self.assertEquals(self.calculate(-236127245, 139869.0), -33026881630905.00)

    def test0747(self):
        self.assertEquals(self.calculate(807323416, 95921.0), 77439269386136.00)

    def test0748(self):
        self.assertEquals(self.calculate(-55900658, -6135.0), 342950536830.00)

    def test0749(self):
        self.assertEquals(self.calculate(1436639050, -183979.0), -264311415779950.00)

    def test0750(self):
        self.assertEquals(self.calculate(-750638008, 111320.0), -83561023050560.00)

    def test0751(self):
        self.assertEquals(self.calculate(1099764715, -20476.0), -22518782304340.00)

    def test0752(self):
        self.assertEquals(self.calculate(-601623502, 196489.0), -118212400284478.00)

    def test0753(self):
        self.assertEquals(self.calculate(-155611879, -114494.0), 17816626474226.00)

    def test0754(self):
        self.assertEquals(self.calculate(-335064582, -99069.0), 33194513074158.00)

    def test0755(self):
        self.assertEquals(self.calculate(1240973582, -19806.0), -24578722765092.00)

    def test0756(self):
        self.assertEquals(self.calculate(2062387382, 180461.0), 372180489343102.00)

    def test0757(self):
        self.assertEquals(self.calculate(1215501797, -101387.0), -123236080692439.00)

    def test0758(self):
        self.assertEquals(self.calculate(263815439, 159243.0), 42010761952677.00)

    def test0759(self):
        self.assertEquals(self.calculate(583177050, -150110.0), -87540706975500.00)

    def test0760(self):
        self.assertEquals(self.calculate(1953580305, 72527.0), 141687318780735.00)

    def test0761(self):
        self.assertEquals(self.calculate(-1178158490, -181093.0), 213356255429570.00)

    def test0762(self):
        self.assertEquals(self.calculate(-1414947169, 51047.0), -72228808135943.00)

    def test0763(self):
        self.assertEquals(self.calculate(-438769412, 138146.0), -60614239190152.00)

    def test0764(self):
        self.assertEquals(self.calculate(1178234535, -23525.0), -27717967435875.00)

    def test0765(self):
        self.assertEquals(self.calculate(-1371304485, -24859.0), 34089258192615.00)

    def test0766(self):
        self.assertEquals(self.calculate(567969727, 60349.0), 34276405054723.00)

    def test0767(self):
        self.assertEquals(self.calculate(2090478414, 8623.0), 18026195363922.00)

    def test0768(self):
        self.assertEquals(self.calculate(-341223243, 59550.0), -20319844120650.00)

    def test0769(self):
        self.assertEquals(self.calculate(-1243334375, -163091.0), 202776646553125.00)

    def test0770(self):
        self.assertEquals(self.calculate(2116582400, 3620.0), 7662028288000.00)

    def test0771(self):
        self.assertEquals(self.calculate(-773709530, 54817.0), -42412435306010.00)

    def test0772(self):
        self.assertEquals(self.calculate(-1003153162, -85517.0), 85786648954754.00)

    def test0773(self):
        self.assertEquals(self.calculate(-1309966197, 40877.0), -53547488234769.00)

    def test0774(self):
        self.assertEquals(self.calculate(121627940, 41290.0), 5022017642600.00)

    def test0775(self):
        self.assertEquals(self.calculate(-1713652610, 60749.0), -104102682404890.00)

    def test0776(self):
        self.assertEquals(self.calculate(-102399676, -20335.0), 2082297411460.00)

    def test0777(self):
        self.assertEquals(self.calculate(13605383, -174038.0), -2367853646554.00)

    def test0778(self):
        self.assertEquals(self.calculate(2124037731, 115998.0), 246384128720538.00)

    def test0779(self):
        self.assertEquals(self.calculate(1721458283, -189472.0), -326168143796576.00)

    def test0780(self):
        self.assertEquals(self.calculate(1077072676, -108412.0), -116767602950512.00)

    def test0781(self):
        self.assertEquals(self.calculate(1515109085, -90275.0), -136776472648375.00)

    def test0782(self):
        self.assertEquals(self.calculate(1818352262, -34980.0), -63605962124760.00)

    def test0783(self):
        self.assertEquals(self.calculate(1017973553, -109879.0), -111853916030087.00)

    def test0784(self):
        self.assertEquals(self.calculate(-1602034854, -99219.0), 158952296179026.00)

    def test0785(self):
        self.assertEquals(self.calculate(-1975033517, -172376.0), 340448377526392.00)

    def test0786(self):
        self.assertEquals(self.calculate(1745003149, -126233.0), -220276982507717.00)

    def test0787(self):
        self.assertEquals(self.calculate(-1190666749, -116772.0), 139036537614228.00)

    def test0788(self):
        self.assertEquals(self.calculate(98671673, 83307.0), 8220041062611.00)

    def test0789(self):
        self.assertEquals(self.calculate(-68510692, 79421.0), -5441187669332.00)

    def test0790(self):
        self.assertEquals(self.calculate(1144030809, -146278.0), -167346538678902.00)

    def test0791(self):
        self.assertEquals(self.calculate(-1459718581, 84251.0), -122982750167831.00)

    def test0792(self):
        self.assertEquals(self.calculate(-1584174923, -132177.0), 209391488797371.00)

    def test0793(self):
        self.assertEquals(self.calculate(-586552159, 106575.0), -62511796345425.00)

    def test0794(self):
        self.assertEquals(self.calculate(637074514, -61132.0), -38945639189848.00)

    def test0795(self):
        self.assertEquals(self.calculate(-2111903017, 95064.0), -200765948408088.00)

    def test0796(self):
        self.assertEquals(self.calculate(-1002271651, -142840.0), 143164482628840.00)

    def test0797(self):
        self.assertEquals(self.calculate(-777128097, -35660.0), 27712387939020.00)

    def test0798(self):
        self.assertEquals(self.calculate(-61813036, 146561.0), -9059380369196.00)

    def test0799(self):
        self.assertEquals(self.calculate(-1578278323, 22772.0), -35940553971356.00)

    def test0800(self):
        self.assertEquals(self.calculate(-2025273890, 57774.0), -117008173720860.00)

    def test0801(self):
        self.assertEquals(self.calculate(-1049749870, 199380.0), -209299129080600.00)

    def test0802(self):
        self.assertEquals(self.calculate(-624021812, -45641.0), 28480979521492.00)

    def test0803(self):
        self.assertEquals(self.calculate(1099440469, 117458.0), 129138078607802.00)

    def test0804(self):
        self.assertEquals(self.calculate(376172916, 78812.0), 29646939855792.00)

    def test0805(self):
        self.assertEquals(self.calculate(-11249591, 82349.0), -926392569259.00)

    def test0806(self):
        self.assertEquals(self.calculate(1634755312, 99679.0), 162950774744848.00)

    def test0807(self):
        self.assertEquals(self.calculate(135637583, -70052.0), -9501683964316.00)

    def test0808(self):
        self.assertEquals(self.calculate(687087383, 186139.0), 127893758384237.00)

    def test0809(self):
        self.assertEquals(self.calculate(322940741, -89207.0), -28808574682387.00)

    def test0810(self):
        self.assertEquals(self.calculate(-360140063, 59149.0), -21301924586387.00)

    def test0811(self):
        self.assertEquals(self.calculate(61853298, 34540.0), 2136412912920.00)

    def test0812(self):
        self.assertEquals(self.calculate(-869049586, 57995.0), -50400530740070.00)

    def test0813(self):
        self.assertEquals(self.calculate(-376486291, -131470.0), 49496652677770.00)

    def test0814(self):
        self.assertEquals(self.calculate(-1191856734, 156060.0), -186001161908040.00)

    def test0815(self):
        self.assertEquals(self.calculate(599211800, 83060.0), 49770532108000.00)

    def test0816(self):
        self.assertEquals(self.calculate(202779879, 172143.0), 34907136710697.00)

    def test0817(self):
        self.assertEquals(self.calculate(1841347591, 14331.0), 26388352326621.00)

    def test0818(self):
        self.assertEquals(self.calculate(765267650, 102962.0), 78793487779300.00)

    def test0819(self):
        self.assertEquals(self.calculate(-69279669, 108566.0), -7521416544654.00)

    def test0820(self):
        self.assertEquals(self.calculate(-936501707, 126567.0), -118530211549869.00)

    def test0821(self):
        self.assertEquals(self.calculate(-1519088438, -150736.0), 228981314790368.00)

    def test0822(self):
        self.assertEquals(self.calculate(-879185739, 118197.0), -103917116792583.00)

    def test0823(self):
        self.assertEquals(self.calculate(1890178577, 129272.0), 244347165005944.00)

    def test0824(self):
        self.assertEquals(self.calculate(-1200952549, 164206.0), -197203614261094.00)

    def test0825(self):
        self.assertEquals(self.calculate(1921821076, 189736.0), 364638643675936.00)

    def test0826(self):
        self.assertEquals(self.calculate(-1189759756, 63452.0), -75492636037712.00)

    def test0827(self):
        self.assertEquals(self.calculate(-671334295, -165679.0), 111225994661305.00)

    def test0828(self):
        self.assertEquals(self.calculate(1183259143, -19411.0), -22968243224773.00)

    def test0829(self):
        self.assertEquals(self.calculate(-5036539, -40549.0), 204226619911.00)

    def test0830(self):
        self.assertEquals(self.calculate(-1935815206, -17625.0), 34118743005750.00)

    def test0831(self):
        self.assertEquals(self.calculate(-1145565580, 36384.0), -41680258062720.00)

    def test0832(self):
        self.assertEquals(self.calculate(-1823774282, -44049.0), 80335433347818.00)

    def test0833(self):
        self.assertEquals(self.calculate(1178473303, 133249.0), 157030389151447.00)

    def test0834(self):
        self.assertEquals(self.calculate(-163752457, 175399.0), -28722017205343.00)

    def test0835(self):
        self.assertEquals(self.calculate(-2075951231, -56818.0), 117951397042958.00)

    def test0836(self):
        self.assertEquals(self.calculate(856877669, -136253.0), -116752153034257.00)

    def test0837(self):
        self.assertEquals(self.calculate(891922403, 177127.0), 157983539476181.00)

    def test0838(self):
        self.assertEquals(self.calculate(-1192416081, 103676.0), -123624929613756.00)

    def test0839(self):
        self.assertEquals(self.calculate(268909600, 86323.0), 23213083400800.00)

    def test0840(self):
        self.assertEquals(self.calculate(-745612055, -159795.0), 119145078328725.00)

    def test0841(self):
        self.assertEquals(self.calculate(-1546124403, -61283.0), 94751141789049.00)

    def test0842(self):
        self.assertEquals(self.calculate(-2067279193, -137069.0), 283359891705317.00)

    def test0843(self):
        self.assertEquals(self.calculate(-188923911, -111090.0), 20987557272990.00)

    def test0844(self):
        self.assertEquals(self.calculate(-1993840956, 161428.0), -321861757845168.00)

    def test0845(self):
        self.assertEquals(self.calculate(1935195216, 44374.0), 85872352514784.00)

    def test0846(self):
        self.assertEquals(self.calculate(426806727, -192952.0), -82353211588104.00)

    def test0847(self):
        self.assertEquals(self.calculate(-839862262, -12382.0), 10399174528084.00)

    def test0848(self):
        self.assertEquals(self.calculate(-1506957266, 100624.0), -151636067933984.00)

    def test0849(self):
        self.assertEquals(self.calculate(-505819659, 175075.0), -88556376799425.00)

    def test0850(self):
        self.assertEquals(self.calculate(-2065674651, 127628.0), -263637924357828.00)

    def test0851(self):
        self.assertEquals(self.calculate(-1189061919, 76257.0), -90674294757183.00)

    def test0852(self):
        self.assertEquals(self.calculate(1769014972, -57015.0), -100860388628580.00)

    def test0853(self):
        self.assertEquals(self.calculate(1274393924, -132367.0), -168687700538108.00)

    def test0854(self):
        self.assertEquals(self.calculate(1168594579, 38697.0), 45221104423563.00)

    def test0855(self):
        self.assertEquals(self.calculate(2023962368, -62180.0), -125849980042240.00)

    def test0856(self):
        self.assertEquals(self.calculate(2093286191, -44927.0), -94045068703057.00)

    def test0857(self):
        self.assertEquals(self.calculate(10248454, -192209.0), -1969845094886.00)

    def test0858(self):
        self.assertEquals(self.calculate(-1304166259, -19567.0), 25518621189853.00)

    def test0859(self):
        self.assertEquals(self.calculate(1618742023, 20475.0), 33143742920925.00)

    def test0860(self):
        self.assertEquals(self.calculate(-580969232, 75317.0), -43756859646544.00)

    def test0861(self):
        self.assertEquals(self.calculate(2073922914, -18552.0), -38475417900528.00)

    def test0862(self):
        self.assertEquals(self.calculate(473582592, -152117.0), -72039963147264.00)

    def test0863(self):
        self.assertEquals(self.calculate(-214264424, -37423.0), 8018417539352.00)

    def test0864(self):
        self.assertEquals(self.calculate(1412908770, 189371.0), 267563946683670.00)

    def test0865(self):
        self.assertEquals(self.calculate(1840632266, -82971.0), -152719099742286.00)

    def test0866(self):
        self.assertEquals(self.calculate(-1536429925, 121781.0), -187107972696425.00)

    def test0867(self):
        self.assertEquals(self.calculate(-1805449487, 191640.0), -345996339688680.00)

    def test0868(self):
        self.assertEquals(self.calculate(-1762127429, -145388.0), 256192182647452.00)

    def test0869(self):
        self.assertEquals(self.calculate(-1547838052, 84836.0), -131312388979472.00)

    def test0870(self):
        self.assertEquals(self.calculate(1611614940, 166381.0), 268142105332140.00)

    def test0871(self):
        self.assertEquals(self.calculate(-1099205368, 134362.0), -147691431655216.00)

    def test0872(self):
        self.assertEquals(self.calculate(-1889597916, 53646.0), -101369369801736.00)

    def test0873(self):
        self.assertEquals(self.calculate(1321083074, -17789.0), -23500746803386.00)

    def test0874(self):
        self.assertEquals(self.calculate(664582813, 135418.0), 89996475370834.00)

    def test0875(self):
        self.assertEquals(self.calculate(397451229, 110602.0), 43958900829858.00)

    def test0876(self):
        self.assertEquals(self.calculate(1484880855, 98842.0), 146768593469910.00)

    def test0877(self):
        self.assertEquals(self.calculate(-1762796286, -195722.0), 345018014688492.00)

    def test0878(self):
        self.assertEquals(self.calculate(-1895461041, 89123.0), -168929174357043.00)

    def test0879(self):
        self.assertEquals(self.calculate(-1563875226, -57466.0), 89869653737316.00)

    def test0880(self):
        self.assertEquals(self.calculate(954246404, 94277.0), 89963488229908.00)

    def test0881(self):
        self.assertEquals(self.calculate(-844722472, -50671.0), 42802932378712.00)

    def test0882(self):
        self.assertEquals(self.calculate(-690541793, -40636.0), 28060856300348.00)

    def test0883(self):
        self.assertEquals(self.calculate(1005281521, -58247.0), -58554632753687.00)

    def test0884(self):
        self.assertEquals(self.calculate(-951516417, -74988.0), 71352313077996.00)

    def test0885(self):
        self.assertEquals(self.calculate(2130184390, -193198.0), -411547363779220.00)

    def test0886(self):
        self.assertEquals(self.calculate(1541216972, -189755.0), -292453626521860.00)

    def test0887(self):
        self.assertEquals(self.calculate(-688752201, -17656.0), 12160608860856.00)

    def test0888(self):
        self.assertEquals(self.calculate(1923523670, -153905.0), -296039910431350.00)

    def test0889(self):
        self.assertEquals(self.calculate(-1621504699, 133470.0), -216422232175530.00)

    def test0890(self):
        self.assertEquals(self.calculate(-1149798321, 188428.0), -216654198029388.00)

    def test0891(self):
        self.assertEquals(self.calculate(-1764028875, 176320.0), -311033571240000.00)

    def test0892(self):
        self.assertEquals(self.calculate(-32268362, 190069.0), -6133215296978.00)

    def test0893(self):
        self.assertEquals(self.calculate(-521959128, -125443.0), 65476118893704.00)

    def test0894(self):
        self.assertEquals(self.calculate(-892377289, -96453.0), 86072466655917.00)

    def test0895(self):
        self.assertEquals(self.calculate(-1592773020, 17993.0), -28658764948860.00)

    def test0896(self):
        self.assertEquals(self.calculate(1977181231, 172305.0), 340678212007455.00)

    def test0897(self):
        self.assertEquals(self.calculate(1577093882, -135592.0), -213841313648144.00)

    def test0898(self):
        self.assertEquals(self.calculate(484319575, 191379.0), 92688595943925.00)

    def test0899(self):
        self.assertEquals(self.calculate(1571253767, -97081.0), -152538886954127.00)

    def test0900(self):
        self.assertEquals(self.calculate(-884751653, 105127.0), -93011287024931.00)

    def test0901(self):
        self.assertEquals(self.calculate(-731640256, -197904.0), 144794533223424.00)

    def test0902(self):
        self.assertEquals(self.calculate(-1606814866, -62284.0), 100078857113944.00)

    def test0903(self):
        self.assertEquals(self.calculate(1022827432, -76500.0), -78246298548000.00)

    def test0904(self):
        self.assertEquals(self.calculate(-1352375792, 166680.0), -225413997010560.00)

    def test0905(self):
        self.assertEquals(self.calculate(-1542527859, -151680.0), 233970625653120.00)

    def test0906(self):
        self.assertEquals(self.calculate(876570301, 91324.0), 80051906168524.00)

    def test0907(self):
        self.assertEquals(self.calculate(64559221, 14017.0), 904926600757.00)

    def test0908(self):
        self.assertEquals(self.calculate(-761101988, 181996.0), -138517517408048.00)

    def test0909(self):
        self.assertEquals(self.calculate(-2092853012, 130593.0), -273311953396116.00)

    def test0910(self):
        self.assertEquals(self.calculate(-1962352121, -137502.0), 269827341341742.00)

    def test0911(self):
        self.assertEquals(self.calculate(1915872845, -97078.0), -185989104046910.00)

    def test0912(self):
        self.assertEquals(self.calculate(1834928707, -51770.0), -94994259161390.00)

    def test0913(self):
        self.assertEquals(self.calculate(-830971994, 102375.0), -85070757885750.00)

    def test0914(self):
        self.assertEquals(self.calculate(-662600519, -32946.0), 21830036698974.00)

    def test0915(self):
        self.assertEquals(self.calculate(-818067304, -166181.0), 135947242646024.00)

    def test0916(self):
        self.assertEquals(self.calculate(-341780540, 169980.0), -58095856189200.00)

    def test0917(self):
        self.assertEquals(self.calculate(-1136300611, -68223.0), 77521836584253.00)

    def test0918(self):
        self.assertEquals(self.calculate(-882775284, 72933.0), -64383449787972.00)

    def test0919(self):
        self.assertEquals(self.calculate(1929104571, -4284.0), -8264283982164.00)

    def test0920(self):
        self.assertEquals(self.calculate(633622360, 6448.0), 4085596977280.00)

    def test0921(self):
        self.assertEquals(self.calculate(-1687408714, 167331.0), -282355787522334.00)

    def test0922(self):
        self.assertEquals(self.calculate(782129794, -157836.0), -123448238165784.00)

    def test0923(self):
        self.assertEquals(self.calculate(-501497395, 84914.0), -42584149799030.00)

    def test0924(self):
        self.assertEquals(self.calculate(-922618621, -45975.0), 42417391100475.00)

    def test0925(self):
        self.assertEquals(self.calculate(-1835664343, -22092.0), 40553496665556.00)

    def test0926(self):
        self.assertEquals(self.calculate(-1400153281, -197859.0), 277032928025379.00)

    def test0927(self):
        self.assertEquals(self.calculate(521480179, -96402.0), -50271732215958.00)

    def test0928(self):
        self.assertEquals(self.calculate(-644439878, -126475.0), 81505533570050.00)

    def test0929(self):
        self.assertEquals(self.calculate(-1729791128, 22767.0), -39382154611176.00)

    def test0930(self):
        self.assertEquals(self.calculate(1796747822, -16898.0), -30361444696156.00)

    def test0931(self):
        self.assertEquals(self.calculate(-1747861799, 144816.0), -253118354283984.00)

    def test0932(self):
        self.assertEquals(self.calculate(-100589898, 151138.0), -15202956003924.00)

    def test0933(self):
        self.assertEquals(self.calculate(-632556811, -129364.0), 81830079298204.00)

    def test0934(self):
        self.assertEquals(self.calculate(-1365137050, 171377.0), -233953092217850.00)

    def test0935(self):
        self.assertEquals(self.calculate(2052664250, -10015.0), -20557432463750.00)

    def test0936(self):
        self.assertEquals(self.calculate(-680830220, 198226.0), -134958251189720.00)

    def test0937(self):
        self.assertEquals(self.calculate(-550269712, 76649.0), -42177623155088.00)

    def test0938(self):
        self.assertEquals(self.calculate(-1600908266, -63345.0), 101409534109770.00)

    def test0939(self):
        self.assertEquals(self.calculate(1815686558, -109163.0), -198205791730954.00)

    def test0940(self):
        self.assertEquals(self.calculate(1875166506, -91941.0), -172404683728146.00)

    def test0941(self):
        self.assertEquals(self.calculate(-1167522585, 140702.0), -164272762754670.00)

    def test0942(self):
        self.assertEquals(self.calculate(954170933, -109766.0), -104735526631678.00)

    def test0943(self):
        self.assertEquals(self.calculate(1930562461, 112567.0), 217317624547387.00)

    def test0944(self):
        self.assertEquals(self.calculate(440093565, 185913.0), 81819114949845.00)

    def test0945(self):
        self.assertEquals(self.calculate(-824425268, 144310.0), -118972810425080.00)

    def test0946(self):
        self.assertEquals(self.calculate(1567007999, 29818.0), 46725044514182.00)

    def test0947(self):
        self.assertEquals(self.calculate(-2033569726, 21907.0), -44549411987482.00)

    def test0948(self):
        self.assertEquals(self.calculate(-750593301, 48055.0), -36069761079555.00)

    def test0949(self):
        self.assertEquals(self.calculate(884496743, -71184.0), -62962016153712.00)

    def test0950(self):
        self.assertEquals(self.calculate(-2103259791, -20572.0), 43268260420452.00)

    def test0951(self):
        self.assertEquals(self.calculate(-1950933334, -100148.0), 195382071533432.00)

    def test0952(self):
        self.assertEquals(self.calculate(41873912, 76249.0), 3192843916088.00)

    def test0953(self):
        self.assertEquals(self.calculate(-1771317863, -177718.0), 314795067976634.00)

    def test0954(self):
        self.assertEquals(self.calculate(1821267010, 124057.0), 225940921459570.00)

    def test0955(self):
        self.assertEquals(self.calculate(-1853960685, -23566.0), 43690437502710.00)

    def test0956(self):
        self.assertEquals(self.calculate(256293248, -147286.0), -37748407324928.00)

    def test0957(self):
        self.assertEquals(self.calculate(1942133212, -81380.0), -158050800792560.00)

    def test0958(self):
        self.assertEquals(self.calculate(-682490313, -176307.0), 120327819614091.00)

    def test0959(self):
        self.assertEquals(self.calculate(1424939418, -92350.0), -131593155252300.00)

    def test0960(self):
        self.assertEquals(self.calculate(-2107855266, -187151.0), 394487220887166.00)

    def test0961(self):
        self.assertEquals(self.calculate(-1808313611, -20952.0), 37887786777672.00)

    def test0962(self):
        self.assertEquals(self.calculate(-2025771373, -53709.0), 108802154672457.00)

    def test0963(self):
        self.assertEquals(self.calculate(1117700654, 7902.0), 8832070567908.00)

    def test0964(self):
        self.assertEquals(self.calculate(1348590757, -141016.0), -190172874189112.00)

    def test0965(self):
        self.assertEquals(self.calculate(-293321208, 153395.0), -44994006701160.00)

    def test0966(self):
        self.assertEquals(self.calculate(1364039281, -89708.0), -122365235819948.00)

    def test0967(self):
        self.assertEquals(self.calculate(1555296908, -180699.0), -281040595978692.00)

    def test0968(self):
        self.assertEquals(self.calculate(-31713010, 103646.0), -3286926634460.00)

    def test0969(self):
        self.assertEquals(self.calculate(860547154, 78631.0), 67665683266174.00)

    def test0970(self):
        self.assertEquals(self.calculate(1014519138, -165087.0), -167483920935006.00)

    def test0971(self):
        self.assertEquals(self.calculate(2147073245, -154469.0), -331656257081905.00)

    def test0972(self):
        self.assertEquals(self.calculate(508927239, 90161.0), 45885388795479.00)

    def test0973(self):
        self.assertEquals(self.calculate(-1618270223, -51377.0), 83141869247071.00)

    def test0974(self):
        self.assertEquals(self.calculate(-1198081925, -5313.0), 6365409267525.00)

    def test0975(self):
        self.assertEquals(self.calculate(-1041094322, -141752.0), 147577202332144.00)

    def test0976(self):
        self.assertEquals(self.calculate(-18562402, -151359.0), 2809586604318.00)

    def test0977(self):
        self.assertEquals(self.calculate(1707631843, -160558.0), -274173953448394.00)

    def test0978(self):
        self.assertEquals(self.calculate(-1155043269, -51158.0), 59089703555502.00)

    def test0979(self):
        self.assertEquals(self.calculate(-1268763973, -124585.0), 158068959576205.00)

    def test0980(self):
        self.assertEquals(self.calculate(-1585646152, -117400.0), 186154858244800.00)

    def test0981(self):
        self.assertEquals(self.calculate(-522688451, 189956.0), -99287807398156.00)

    def test0982(self):
        self.assertEquals(self.calculate(932574531, 83901.0), 78243935725431.00)

    def test0983(self):
        self.assertEquals(self.calculate(-1193764390, 4099.0), -4893240234610.00)

    def test0984(self):
        self.assertEquals(self.calculate(1877906018, 9692.0), 18200665126456.00)

    def test0985(self):
        self.assertEquals(self.calculate(1363507394, -15035.0), -20500333668790.00)

    def test0986(self):
        self.assertEquals(self.calculate(-833252763, 106375.0), -88637262664125.00)

    def test0987(self):
        self.assertEquals(self.calculate(1374825880, 65081.0), 89475043096280.00)

    def test0988(self):
        self.assertEquals(self.calculate(-37032198, -136684.0), 5061708951432.00)

    def test0989(self):
        self.assertEquals(self.calculate(-1366906987, 79951.0), -109285580517637.00)

    def test0990(self):
        self.assertEquals(self.calculate(-388565521, -139519.0), 54212272924399.00)

    def test0991(self):
        self.assertEquals(self.calculate(-248247540, 196091.0), -48679108366140.00)

    def test0992(self):
        self.assertEquals(self.calculate(274160307, -70285.0), -19269357177495.00)

    def test0993(self):
        self.assertEquals(self.calculate(-1817090267, 15840.0), -28782709829280.00)

    def test0994(self):
        self.assertEquals(self.calculate(922900291, 13387.0), 12354866195617.00)

    def test0995(self):
        self.assertEquals(self.calculate(688319175, -57909.0), -39859875105075.00)

    def test0996(self):
        self.assertEquals(self.calculate(375826205, 146620.0), 55103638177100.00)

    def test0997(self):
        self.assertEquals(self.calculate(-1090899141, 49703.0), -54220960005123.00)

    def test0998(self):
        self.assertEquals(self.calculate(1462193920, -77078.0), -112702982965760.00)

    def test0999(self):
        self.assertEquals(self.calculate(-326864006, -48286.0), 15782955393716.00)

    def test1000(self):
        self.assertEquals(self.calculate(199809637, -87251.0), -17433590637887.00)

    def test1001(self):
        self.assertEquals(self.calculate(-1984624867, -168962.0), 335326186778054.00)

    def test1002(self):
        self.assertEquals(self.calculate(-2016665128, -12324.0), 24853381037472.00)

    def test1003(self):
        self.assertEquals(self.calculate(890796271, -87388.0), -77844904530148.00)

    def test1004(self):
        self.assertEquals(self.calculate(1590237056, 167928.0), 267045328339968.00)

    def test1005(self):
        self.assertEquals(self.calculate(-274790601, -182540.0), 50160276306540.00)

    def test1006(self):
        self.assertEquals(self.calculate(-111745314, 84438.0), -9435550823532.00)

    def test1007(self):
        self.assertEquals(self.calculate(-852198089, -163685.0), 139492044197965.00)

    def test1008(self):
        self.assertEquals(self.calculate(-1860373192, -115421.0), 214726134193832.00)

    def test1009(self):
        self.assertEquals(self.calculate(-1091271865, -145969.0), 159291862862185.00)

    def test1010(self):
        self.assertEquals(self.calculate(-1467817032, 113836.0), -167090419654752.00)

    def test1011(self):
        self.assertEquals(self.calculate(-835349197, 23748.0), -19837872730356.00)

    def test1012(self):
        self.assertEquals(self.calculate(523270876, -251.0), -131340989876.00)

    def test1013(self):
        self.assertEquals(self.calculate(984390763, 57744.0), 56842660218672.00)

    def test1014(self):
        self.assertEquals(self.calculate(311310315, 13578.0), 4226971457070.00)

    def test1015(self):
        self.assertEquals(self.calculate(-403784611, 191173.0), -77192715438703.00)

    def test1016(self):
        self.assertEquals(self.calculate(-1288401110, 185559.0), -239074421570490.00)

    def test1017(self):
        self.assertEquals(self.calculate(-353291199, 151517.0), -53529622598883.00)

    def test1018(self):
        self.assertEquals(self.calculate(1340958500, -100583.0), -134877628805500.00)

    def test1019(self):
        self.assertEquals(self.calculate(1511108070, 106618.0), 161111320207260.00)

    def test1020(self):
        self.assertEquals(self.calculate(1597306083, -69492.0), -110999994319836.00)

    def test1021(self):
        self.assertEquals(self.calculate(450225482, -107813.0), -48540159890866.00)

    def test1022(self):
        self.assertEquals(self.calculate(501524324, -63114.0), -31653206184936.00)

    def test1023(self):
        self.assertEquals(self.calculate(380062770, -64476.0), -24504927158520.00)




class TestVM_Mul_FloatInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushW(rhs)
        v.VM_Mul()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-99681.0, 1819), -181319739.00)

    def test0001(self):
        self.assertEquals(self.calculate(133586.0, -542), -72403612.00)

    def test0002(self):
        self.assertEquals(self.calculate(88483.0, -16847), -1490673101.00)

    def test0003(self):
        self.assertEquals(self.calculate(-193197.0, -15284), 2952822948.00)

    def test0004(self):
        self.assertEquals(self.calculate(74211.0, -2206), -163709466.00)

    def test0005(self):
        self.assertEquals(self.calculate(195989.0, 151), 29594339.00)

    def test0006(self):
        self.assertEquals(self.calculate(-165890.0, -28732), 4766351480.00)

    def test0007(self):
        self.assertEquals(self.calculate(154490.0, -13211), -2040967390.00)

    def test0008(self):
        self.assertEquals(self.calculate(110229.0, -24678), -2720231262.00)

    def test0009(self):
        self.assertEquals(self.calculate(60687.0, 1878), 113970186.00)

    def test0010(self):
        self.assertEquals(self.calculate(-122948.0, -29470), 3623277560.00)

    def test0011(self):
        self.assertEquals(self.calculate(-18096.0, 26649), -482240304.00)

    def test0012(self):
        self.assertEquals(self.calculate(-149695.0, -19709), 2950338755.00)

    def test0013(self):
        self.assertEquals(self.calculate(-86847.0, 25932), -2252116404.00)

    def test0014(self):
        self.assertEquals(self.calculate(37168.0, -5319), -197696592.00)

    def test0015(self):
        self.assertEquals(self.calculate(61806.0, -20437), -1263129222.00)

    def test0016(self):
        self.assertEquals(self.calculate(196357.0, 19312), 3792046384.00)

    def test0017(self):
        self.assertEquals(self.calculate(-139301.0, 17807), -2480532907.00)

    def test0018(self):
        self.assertEquals(self.calculate(115632.0, 13481), 1558834992.00)

    def test0019(self):
        self.assertEquals(self.calculate(-116808.0, 19588), -2288035104.00)

    def test0020(self):
        self.assertEquals(self.calculate(-37037.0, -30222), 1119332214.00)

    def test0021(self):
        self.assertEquals(self.calculate(-16213.0, 22019), -356994047.00)

    def test0022(self):
        self.assertEquals(self.calculate(-68456.0, 28911), -1979131416.00)

    def test0023(self):
        self.assertEquals(self.calculate(-77667.0, 27735), -2154094245.00)

    def test0024(self):
        self.assertEquals(self.calculate(74780.0, -22920), -1713957600.00)

    def test0025(self):
        self.assertEquals(self.calculate(115555.0, -7642), -883071310.00)

    def test0026(self):
        self.assertEquals(self.calculate(-151769.0, -24758), 3757496902.00)

    def test0027(self):
        self.assertEquals(self.calculate(-112713.0, 30429), -3429743877.00)

    def test0028(self):
        self.assertEquals(self.calculate(-92769.0, -25910), 2403644790.00)

    def test0029(self):
        self.assertEquals(self.calculate(141785.0, 7815), 1108049775.00)

    def test0030(self):
        self.assertEquals(self.calculate(-190086.0, 30328), -5764928208.00)

    def test0031(self):
        self.assertEquals(self.calculate(116784.0, -29561), -3452251824.00)

    def test0032(self):
        self.assertEquals(self.calculate(-3733.0, 15182), -56674406.00)

    def test0033(self):
        self.assertEquals(self.calculate(112043.0, -13117), -1469668031.00)

    def test0034(self):
        self.assertEquals(self.calculate(34539.0, -9298), -321143622.00)

    def test0035(self):
        self.assertEquals(self.calculate(169347.0, 9793), 1658415171.00)

    def test0036(self):
        self.assertEquals(self.calculate(31642.0, 7481), 236713802.00)

    def test0037(self):
        self.assertEquals(self.calculate(-51096.0, -31900), 1629962400.00)

    def test0038(self):
        self.assertEquals(self.calculate(-194573.0, -5876), 1143310948.00)

    def test0039(self):
        self.assertEquals(self.calculate(-193510.0, -20776), 4020363760.00)

    def test0040(self):
        self.assertEquals(self.calculate(-31876.0, 26353), -840028228.00)

    def test0041(self):
        self.assertEquals(self.calculate(97820.0, 28634), 2800977880.00)

    def test0042(self):
        self.assertEquals(self.calculate(-191316.0, -24145), 4619324820.00)

    def test0043(self):
        self.assertEquals(self.calculate(100630.0, 6809), 685189670.00)

    def test0044(self):
        self.assertEquals(self.calculate(87309.0, 28430), 2482194870.00)

    def test0045(self):
        self.assertEquals(self.calculate(-154798.0, 23592), -3651994416.00)

    def test0046(self):
        self.assertEquals(self.calculate(-50852.0, -27490), 1397921480.00)

    def test0047(self):
        self.assertEquals(self.calculate(-39483.0, 31385), -1239173955.00)

    def test0048(self):
        self.assertEquals(self.calculate(-61219.0, 5848), -358008712.00)

    def test0049(self):
        self.assertEquals(self.calculate(-61227.0, 27833), -1704131091.00)

    def test0050(self):
        self.assertEquals(self.calculate(-160697.0, -8198), 1317394006.00)

    def test0051(self):
        self.assertEquals(self.calculate(-178243.0, -17475), 3114796425.00)

    def test0052(self):
        self.assertEquals(self.calculate(-89236.0, 20906), -1865567816.00)

    def test0053(self):
        self.assertEquals(self.calculate(-106641.0, 19182), -2045587662.00)

    def test0054(self):
        self.assertEquals(self.calculate(87251.0, -17956), -1566678956.00)

    def test0055(self):
        self.assertEquals(self.calculate(-63392.0, -308), 19524736.00)

    def test0056(self):
        self.assertEquals(self.calculate(139048.0, 21150), 2940865200.00)

    def test0057(self):
        self.assertEquals(self.calculate(-58597.0, -26170), 1533483490.00)

    def test0058(self):
        self.assertEquals(self.calculate(153255.0, -28375), -4348610625.00)

    def test0059(self):
        self.assertEquals(self.calculate(94849.0, 18646), 1768554454.00)

    def test0060(self):
        self.assertEquals(self.calculate(-117258.0, -29405), 3447971490.00)

    def test0061(self):
        self.assertEquals(self.calculate(-11438.0, -1508), 17248504.00)

    def test0062(self):
        self.assertEquals(self.calculate(-161597.0, 27908), -4509849076.00)

    def test0063(self):
        self.assertEquals(self.calculate(-112495.0, -1179), 132631605.00)

    def test0064(self):
        self.assertEquals(self.calculate(-44992.0, 2122), -95473024.00)

    def test0065(self):
        self.assertEquals(self.calculate(-48805.0, 13506), -659160330.00)

    def test0066(self):
        self.assertEquals(self.calculate(141450.0, 13937), 1971388650.00)

    def test0067(self):
        self.assertEquals(self.calculate(45693.0, 10307), 470957751.00)

    def test0068(self):
        self.assertEquals(self.calculate(-12662.0, -25612), 324299144.00)

    def test0069(self):
        self.assertEquals(self.calculate(46024.0, 17449), 803072776.00)

    def test0070(self):
        self.assertEquals(self.calculate(-163234.0, -15355), 2506458070.00)

    def test0071(self):
        self.assertEquals(self.calculate(18794.0, -20744), -389862736.00)

    def test0072(self):
        self.assertEquals(self.calculate(196702.0, 12123), 2384618346.00)

    def test0073(self):
        self.assertEquals(self.calculate(52641.0, -30509), -1606024269.00)

    def test0074(self):
        self.assertEquals(self.calculate(-53800.0, 3684), -198199200.00)

    def test0075(self):
        self.assertEquals(self.calculate(166097.0, -10688), -1775244736.00)

    def test0076(self):
        self.assertEquals(self.calculate(164391.0, -13353), -2195113023.00)

    def test0077(self):
        self.assertEquals(self.calculate(-165427.0, -2668), 441359236.00)

    def test0078(self):
        self.assertEquals(self.calculate(38222.0, 6938), 265184236.00)

    def test0079(self):
        self.assertEquals(self.calculate(-186256.0, -24170), 4501807520.00)

    def test0080(self):
        self.assertEquals(self.calculate(19083.0, 19427), 370725441.00)

    def test0081(self):
        self.assertEquals(self.calculate(122059.0, -6241), -761770219.00)

    def test0082(self):
        self.assertEquals(self.calculate(68676.0, -23536), -1616358336.00)

    def test0083(self):
        self.assertEquals(self.calculate(-159779.0, 21832), -3488295128.00)

    def test0084(self):
        self.assertEquals(self.calculate(47670.0, 6076), 289642920.00)

    def test0085(self):
        self.assertEquals(self.calculate(-97504.0, 27395), -2671122080.00)

    def test0086(self):
        self.assertEquals(self.calculate(7255.0, -19113), -138664815.00)

    def test0087(self):
        self.assertEquals(self.calculate(-94942.0, -13510), 1282666420.00)

    def test0088(self):
        self.assertEquals(self.calculate(78322.0, 26227), 2054151094.00)

    def test0089(self):
        self.assertEquals(self.calculate(-64571.0, -25659), 1656827289.00)

    def test0090(self):
        self.assertEquals(self.calculate(143925.0, 25230), 3631227750.00)

    def test0091(self):
        self.assertEquals(self.calculate(197512.0, 13252), 2617429024.00)

    def test0092(self):
        self.assertEquals(self.calculate(-84537.0, 23764), -2008937268.00)

    def test0093(self):
        self.assertEquals(self.calculate(43212.0, -17643), -762389316.00)

    def test0094(self):
        self.assertEquals(self.calculate(18260.0, 171), 3122460.00)

    def test0095(self):
        self.assertEquals(self.calculate(96127.0, 14694), 1412490138.00)

    def test0096(self):
        self.assertEquals(self.calculate(147898.0, -26220), -3877885560.00)

    def test0097(self):
        self.assertEquals(self.calculate(133723.0, -3797), -507746231.00)

    def test0098(self):
        self.assertEquals(self.calculate(96377.0, -27864), -2685448728.00)

    def test0099(self):
        self.assertEquals(self.calculate(1104.0, -1945), -2147280.00)

    def test0100(self):
        self.assertEquals(self.calculate(-124495.0, -7783), 968944585.00)

    def test0101(self):
        self.assertEquals(self.calculate(6169.0, -17241), -106359729.00)

    def test0102(self):
        self.assertEquals(self.calculate(-160060.0, -8833), 1413809980.00)

    def test0103(self):
        self.assertEquals(self.calculate(105714.0, 29704), 3140128656.00)

    def test0104(self):
        self.assertEquals(self.calculate(-192066.0, -23305), 4476098130.00)

    def test0105(self):
        self.assertEquals(self.calculate(-184063.0, -6030), 1109899890.00)

    def test0106(self):
        self.assertEquals(self.calculate(25272.0, 27843), 703648296.00)

    def test0107(self):
        self.assertEquals(self.calculate(152286.0, -17975), -2737340850.00)

    def test0108(self):
        self.assertEquals(self.calculate(195401.0, 3913), 764604113.00)

    def test0109(self):
        self.assertEquals(self.calculate(-171367.0, 4107), -703804269.00)

    def test0110(self):
        self.assertEquals(self.calculate(118852.0, -6539), -777173228.00)

    def test0111(self):
        self.assertEquals(self.calculate(-13777.0, -14972), 206269244.00)

    def test0112(self):
        self.assertEquals(self.calculate(-110613.0, 23139), -2559474207.00)

    def test0113(self):
        self.assertEquals(self.calculate(-56448.0, -28249), 1594599552.00)

    def test0114(self):
        self.assertEquals(self.calculate(192945.0, -26290), -5072524050.00)

    def test0115(self):
        self.assertEquals(self.calculate(45132.0, -7087), -319850484.00)

    def test0116(self):
        self.assertEquals(self.calculate(93445.0, -3798), -354904110.00)

    def test0117(self):
        self.assertEquals(self.calculate(178300.0, 30843), 5499306900.00)

    def test0118(self):
        self.assertEquals(self.calculate(-4647.0, 18482), -85885854.00)

    def test0119(self):
        self.assertEquals(self.calculate(-80048.0, -6133), 490934384.00)

    def test0120(self):
        self.assertEquals(self.calculate(98757.0, -26550), -2621998350.00)

    def test0121(self):
        self.assertEquals(self.calculate(-145786.0, 1814), -264455804.00)

    def test0122(self):
        self.assertEquals(self.calculate(94226.0, -15821), -1490749546.00)

    def test0123(self):
        self.assertEquals(self.calculate(-84305.0, 18144), -1529629920.00)

    def test0124(self):
        self.assertEquals(self.calculate(-192732.0, -314), 60517848.00)

    def test0125(self):
        self.assertEquals(self.calculate(-178677.0, 9453), -1689033681.00)

    def test0126(self):
        self.assertEquals(self.calculate(186603.0, -2319), -432732357.00)

    def test0127(self):
        self.assertEquals(self.calculate(-127869.0, 18210), -2328494490.00)

    def test0128(self):
        self.assertEquals(self.calculate(60799.0, 24946), 1516691854.00)

    def test0129(self):
        self.assertEquals(self.calculate(-43678.0, -22138), 966943564.00)

    def test0130(self):
        self.assertEquals(self.calculate(53512.0, 430), 23010160.00)

    def test0131(self):
        self.assertEquals(self.calculate(52188.0, -15016), -783655008.00)

    def test0132(self):
        self.assertEquals(self.calculate(145995.0, 23483), 3428400585.00)

    def test0133(self):
        self.assertEquals(self.calculate(130192.0, -5015), -652912880.00)

    def test0134(self):
        self.assertEquals(self.calculate(119315.0, -6474), -772445310.00)

    def test0135(self):
        self.assertEquals(self.calculate(-82940.0, -29741), 2466718540.00)

    def test0136(self):
        self.assertEquals(self.calculate(189104.0, -24283), -4592012432.00)

    def test0137(self):
        self.assertEquals(self.calculate(-62552.0, -7217), 451437784.00)

    def test0138(self):
        self.assertEquals(self.calculate(-165907.0, -21727), 3604661389.00)

    def test0139(self):
        self.assertEquals(self.calculate(33914.0, -14440), -489718160.00)

    def test0140(self):
        self.assertEquals(self.calculate(127314.0, -29432), -3747105648.00)

    def test0141(self):
        self.assertEquals(self.calculate(66794.0, -32250), -2154106500.00)

    def test0142(self):
        self.assertEquals(self.calculate(178028.0, -24599), -4379310772.00)

    def test0143(self):
        self.assertEquals(self.calculate(-160734.0, 24675), -3966111450.00)

    def test0144(self):
        self.assertEquals(self.calculate(90532.0, 10364), 938273648.00)

    def test0145(self):
        self.assertEquals(self.calculate(-186060.0, 22791), -4240493460.00)

    def test0146(self):
        self.assertEquals(self.calculate(-130688.0, -31360), 4098375680.00)

    def test0147(self):
        self.assertEquals(self.calculate(163922.0, -10253), -1680692266.00)

    def test0148(self):
        self.assertEquals(self.calculate(-184973.0, -2169), 401206437.00)

    def test0149(self):
        self.assertEquals(self.calculate(-158723.0, 25612), -4065213476.00)

    def test0150(self):
        self.assertEquals(self.calculate(69455.0, -16126), -1120031330.00)

    def test0151(self):
        self.assertEquals(self.calculate(-160671.0, -6144), 987162624.00)

    def test0152(self):
        self.assertEquals(self.calculate(23594.0, 2915), 68776510.00)

    def test0153(self):
        self.assertEquals(self.calculate(4111.0, 14719), 60509809.00)

    def test0154(self):
        self.assertEquals(self.calculate(4220.0, 5348), 22568560.00)

    def test0155(self):
        self.assertEquals(self.calculate(-141304.0, -7987), 1128595048.00)

    def test0156(self):
        self.assertEquals(self.calculate(-122489.0, 31661), -3878124229.00)

    def test0157(self):
        self.assertEquals(self.calculate(-182525.0, 7458), -1361271450.00)

    def test0158(self):
        self.assertEquals(self.calculate(30896.0, -30030), -927806880.00)

    def test0159(self):
        self.assertEquals(self.calculate(16442.0, 12575), 206758150.00)

    def test0160(self):
        self.assertEquals(self.calculate(-157288.0, 19499), -3066958712.00)

    def test0161(self):
        self.assertEquals(self.calculate(-195580.0, 6248), -1221983840.00)

    def test0162(self):
        self.assertEquals(self.calculate(-145161.0, 1036), -150386796.00)

    def test0163(self):
        self.assertEquals(self.calculate(-10750.0, -7493), 80549750.00)

    def test0164(self):
        self.assertEquals(self.calculate(149664.0, -5756), -861465984.00)

    def test0165(self):
        self.assertEquals(self.calculate(-50654.0, 677), -34292758.00)

    def test0166(self):
        self.assertEquals(self.calculate(179650.0, 10053), 1806021450.00)

    def test0167(self):
        self.assertEquals(self.calculate(23082.0, 25670), 592514940.00)

    def test0168(self):
        self.assertEquals(self.calculate(-184130.0, -25264), 4651860320.00)

    def test0169(self):
        self.assertEquals(self.calculate(-61082.0, 25866), -1579947012.00)

    def test0170(self):
        self.assertEquals(self.calculate(15799.0, -27887), -440586713.00)

    def test0171(self):
        self.assertEquals(self.calculate(131759.0, -10992), -1448294928.00)

    def test0172(self):
        self.assertEquals(self.calculate(119327.0, 12893), 1538483011.00)

    def test0173(self):
        self.assertEquals(self.calculate(-107271.0, 7462), -800456202.00)

    def test0174(self):
        self.assertEquals(self.calculate(18990.0, -4895), -92956050.00)

    def test0175(self):
        self.assertEquals(self.calculate(76931.0, -10540), -810852740.00)

    def test0176(self):
        self.assertEquals(self.calculate(-111646.0, -10339), 1154307994.00)

    def test0177(self):
        self.assertEquals(self.calculate(-53035.0, -5121), 271592235.00)

    def test0178(self):
        self.assertEquals(self.calculate(23041.0, -10220), -235479020.00)

    def test0179(self):
        self.assertEquals(self.calculate(22266.0, -4964), -110528424.00)

    def test0180(self):
        self.assertEquals(self.calculate(-56518.0, -26264), 1484388752.00)

    def test0181(self):
        self.assertEquals(self.calculate(31109.0, 9579), 297993111.00)

    def test0182(self):
        self.assertEquals(self.calculate(72401.0, -19822), -1435132622.00)

    def test0183(self):
        self.assertEquals(self.calculate(-115012.0, 8066), -927686792.00)

    def test0184(self):
        self.assertEquals(self.calculate(-53484.0, -9302), 497508168.00)

    def test0185(self):
        self.assertEquals(self.calculate(-157585.0, -221), 34826285.00)

    def test0186(self):
        self.assertEquals(self.calculate(-148892.0, -10691), 1591804372.00)

    def test0187(self):
        self.assertEquals(self.calculate(-43276.0, -2333), 100962908.00)

    def test0188(self):
        self.assertEquals(self.calculate(53900.0, 26581), 1432715900.00)

    def test0189(self):
        self.assertEquals(self.calculate(-173192.0, 661), -114479912.00)

    def test0190(self):
        self.assertEquals(self.calculate(-84029.0, 30036), -2523895044.00)

    def test0191(self):
        self.assertEquals(self.calculate(-157364.0, 9170), -1443027880.00)

    def test0192(self):
        self.assertEquals(self.calculate(-167425.0, -29352), 4914258600.00)

    def test0193(self):
        self.assertEquals(self.calculate(-163571.0, -25681), 4200666851.00)

    def test0194(self):
        self.assertEquals(self.calculate(-135620.0, -14836), 2012058320.00)

    def test0195(self):
        self.assertEquals(self.calculate(-38201.0, 7254), -277110054.00)

    def test0196(self):
        self.assertEquals(self.calculate(-71074.0, 24542), -1744298108.00)

    def test0197(self):
        self.assertEquals(self.calculate(-42503.0, 24258), -1031037774.00)

    def test0198(self):
        self.assertEquals(self.calculate(-150043.0, 8973), -1346335839.00)

    def test0199(self):
        self.assertEquals(self.calculate(167075.0, -2724), -455112300.00)

    def test0200(self):
        self.assertEquals(self.calculate(101318.0, 15330), 1553204940.00)

    def test0201(self):
        self.assertEquals(self.calculate(-128362.0, -14274), 1832239188.00)

    def test0202(self):
        self.assertEquals(self.calculate(100479.0, 21388), 2149044852.00)

    def test0203(self):
        self.assertEquals(self.calculate(-65722.0, 3374), -221746028.00)

    def test0204(self):
        self.assertEquals(self.calculate(46756.0, 28401), 1327917156.00)

    def test0205(self):
        self.assertEquals(self.calculate(-152245.0, -8273), 1259522885.00)

    def test0206(self):
        self.assertEquals(self.calculate(-138108.0, -21007), 2901234756.00)

    def test0207(self):
        self.assertEquals(self.calculate(12471.0, 301), 3753771.00)

    def test0208(self):
        self.assertEquals(self.calculate(-51565.0, -7343), 378641795.00)

    def test0209(self):
        self.assertEquals(self.calculate(71858.0, -21484), -1543797272.00)

    def test0210(self):
        self.assertEquals(self.calculate(-31305.0, 29961), -937929105.00)

    def test0211(self):
        self.assertEquals(self.calculate(29668.0, 4338), 128699784.00)

    def test0212(self):
        self.assertEquals(self.calculate(33497.0, -13593), -455324721.00)

    def test0213(self):
        self.assertEquals(self.calculate(-41945.0, 4300), -180363500.00)

    def test0214(self):
        self.assertEquals(self.calculate(-150164.0, 30885), -4637815140.00)

    def test0215(self):
        self.assertEquals(self.calculate(-90892.0, 8569), -778853548.00)

    def test0216(self):
        self.assertEquals(self.calculate(-112092.0, 19675), -2205410100.00)

    def test0217(self):
        self.assertEquals(self.calculate(191363.0, -28529), -5459395027.00)

    def test0218(self):
        self.assertEquals(self.calculate(112165.0, 28835), 3234277775.00)

    def test0219(self):
        self.assertEquals(self.calculate(-114582.0, 5394), -618055308.00)

    def test0220(self):
        self.assertEquals(self.calculate(-147194.0, 28585), -4207540490.00)

    def test0221(self):
        self.assertEquals(self.calculate(93352.0, -25644), -2393918688.00)

    def test0222(self):
        self.assertEquals(self.calculate(59451.0, 19868), 1181172468.00)

    def test0223(self):
        self.assertEquals(self.calculate(-198333.0, -327), 64854891.00)

    def test0224(self):
        self.assertEquals(self.calculate(110987.0, -7356), -816420372.00)

    def test0225(self):
        self.assertEquals(self.calculate(101291.0, 784), 79412144.00)

    def test0226(self):
        self.assertEquals(self.calculate(46759.0, -10954), -512198086.00)

    def test0227(self):
        self.assertEquals(self.calculate(-102280.0, 22), -2250160.00)

    def test0228(self):
        self.assertEquals(self.calculate(-86113.0, 7004), -603135452.00)

    def test0229(self):
        self.assertEquals(self.calculate(-122747.0, -13612), 1670832164.00)

    def test0230(self):
        self.assertEquals(self.calculate(64875.0, -26213), -1700568375.00)

    def test0231(self):
        self.assertEquals(self.calculate(46235.0, 7750), 358321250.00)

    def test0232(self):
        self.assertEquals(self.calculate(93616.0, 28487), 2666838992.00)

    def test0233(self):
        self.assertEquals(self.calculate(-63306.0, -29155), 1845686430.00)

    def test0234(self):
        self.assertEquals(self.calculate(123891.0, 1017), 125997147.00)

    def test0235(self):
        self.assertEquals(self.calculate(-9727.0, -28691), 279077357.00)

    def test0236(self):
        self.assertEquals(self.calculate(56946.0, -19320), -1100196720.00)

    def test0237(self):
        self.assertEquals(self.calculate(173619.0, -23035), -3999313665.00)

    def test0238(self):
        self.assertEquals(self.calculate(-133446.0, 26547), -3542590962.00)

    def test0239(self):
        self.assertEquals(self.calculate(-125301.0, -7642), 957550242.00)

    def test0240(self):
        self.assertEquals(self.calculate(22650.0, -21146), -478956900.00)

    def test0241(self):
        self.assertEquals(self.calculate(2179.0, 1982), 4318778.00)

    def test0242(self):
        self.assertEquals(self.calculate(105386.0, -15103), -1591644758.00)

    def test0243(self):
        self.assertEquals(self.calculate(-170290.0, 854), -145427660.00)

    def test0244(self):
        self.assertEquals(self.calculate(-53856.0, -17784), 957775104.00)

    def test0245(self):
        self.assertEquals(self.calculate(35075.0, 25977), 911143275.00)

    def test0246(self):
        self.assertEquals(self.calculate(10253.0, 7529), 77194837.00)

    def test0247(self):
        self.assertEquals(self.calculate(-7787.0, -16025), 124786675.00)

    def test0248(self):
        self.assertEquals(self.calculate(174504.0, -19280), -3364437120.00)

    def test0249(self):
        self.assertEquals(self.calculate(126114.0, 1327), 167353278.00)

    def test0250(self):
        self.assertEquals(self.calculate(-100465.0, -13171), 1323224515.00)

    def test0251(self):
        self.assertEquals(self.calculate(-147026.0, 27369), -4023954594.00)

    def test0252(self):
        self.assertEquals(self.calculate(-132901.0, 1826), -242677226.00)

    def test0253(self):
        self.assertEquals(self.calculate(-197796.0, 25492), -5042215632.00)

    def test0254(self):
        self.assertEquals(self.calculate(-30849.0, 22962), -708354738.00)

    def test0255(self):
        self.assertEquals(self.calculate(2601.0, 24749), 64372149.00)

    def test0256(self):
        self.assertEquals(self.calculate(86661.0, -31387), -2720028807.00)

    def test0257(self):
        self.assertEquals(self.calculate(156350.0, -23952), -3744895200.00)

    def test0258(self):
        self.assertEquals(self.calculate(-87671.0, 27764), -2434097644.00)

    def test0259(self):
        self.assertEquals(self.calculate(134753.0, -7605), -1024796565.00)

    def test0260(self):
        self.assertEquals(self.calculate(129666.0, 24386), 3162035076.00)

    def test0261(self):
        self.assertEquals(self.calculate(160271.0, -32581), -5221789451.00)

    def test0262(self):
        self.assertEquals(self.calculate(23446.0, -16099), -377457154.00)

    def test0263(self):
        self.assertEquals(self.calculate(-167239.0, -19140), 3200954460.00)

    def test0264(self):
        self.assertEquals(self.calculate(-26266.0, 24151), -634350166.00)

    def test0265(self):
        self.assertEquals(self.calculate(-74692.0, 13110), -979212120.00)

    def test0266(self):
        self.assertEquals(self.calculate(165656.0, -24170), -4003905520.00)

    def test0267(self):
        self.assertEquals(self.calculate(-8496.0, -5802), 49293792.00)

    def test0268(self):
        self.assertEquals(self.calculate(-101512.0, 16966), -1722252592.00)

    def test0269(self):
        self.assertEquals(self.calculate(194823.0, 18651), 3633643773.00)

    def test0270(self):
        self.assertEquals(self.calculate(80290.0, -4623), -371180670.00)

    def test0271(self):
        self.assertEquals(self.calculate(182130.0, -1791), -326194830.00)

    def test0272(self):
        self.assertEquals(self.calculate(-132831.0, -7728), 1026517968.00)

    def test0273(self):
        self.assertEquals(self.calculate(-83956.0, 28810), -2418772360.00)

    def test0274(self):
        self.assertEquals(self.calculate(-46882.0, 13339), -625358998.00)

    def test0275(self):
        self.assertEquals(self.calculate(144071.0, -29293), -4220271803.00)

    def test0276(self):
        self.assertEquals(self.calculate(-1348.0, 22172), -29887856.00)

    def test0277(self):
        self.assertEquals(self.calculate(48205.0, 3196), 154063180.00)

    def test0278(self):
        self.assertEquals(self.calculate(-129334.0, -28723), 3714860482.00)

    def test0279(self):
        self.assertEquals(self.calculate(33518.0, -3585), -120162030.00)

    def test0280(self):
        self.assertEquals(self.calculate(-105560.0, -17428), 1839699680.00)

    def test0281(self):
        self.assertEquals(self.calculate(29002.0, -27223), -789521446.00)

    def test0282(self):
        self.assertEquals(self.calculate(173790.0, 12178), 2116414620.00)

    def test0283(self):
        self.assertEquals(self.calculate(-189948.0, 16051), -3048855348.00)

    def test0284(self):
        self.assertEquals(self.calculate(66249.0, -27922), -1849804578.00)

    def test0285(self):
        self.assertEquals(self.calculate(28866.0, -29770), -859340820.00)

    def test0286(self):
        self.assertEquals(self.calculate(-165528.0, 19146), -3169199088.00)

    def test0287(self):
        self.assertEquals(self.calculate(-173540.0, 12790), -2219576600.00)

    def test0288(self):
        self.assertEquals(self.calculate(18576.0, -28764), -534320064.00)

    def test0289(self):
        self.assertEquals(self.calculate(-12455.0, -31363), 390626165.00)

    def test0290(self):
        self.assertEquals(self.calculate(-76211.0, -22216), 1693103576.00)

    def test0291(self):
        self.assertEquals(self.calculate(95099.0, 8388), 797690412.00)

    def test0292(self):
        self.assertEquals(self.calculate(180639.0, 19101), 3450385539.00)

    def test0293(self):
        self.assertEquals(self.calculate(77753.0, 30329), 2358170737.00)

    def test0294(self):
        self.assertEquals(self.calculate(43491.0, 31836), 1384579476.00)

    def test0295(self):
        self.assertEquals(self.calculate(121195.0, -29294), -3550286330.00)

    def test0296(self):
        self.assertEquals(self.calculate(120023.0, -15269), -1832631187.00)

    def test0297(self):
        self.assertEquals(self.calculate(-26583.0, -2654), 70551282.00)

    def test0298(self):
        self.assertEquals(self.calculate(62019.0, 14033), 870312627.00)

    def test0299(self):
        self.assertEquals(self.calculate(99469.0, 10890), 1083217410.00)

    def test0300(self):
        self.assertEquals(self.calculate(-119479.0, 760), -90804040.00)

    def test0301(self):
        self.assertEquals(self.calculate(179605.0, -16922), -3039275810.00)

    def test0302(self):
        self.assertEquals(self.calculate(175971.0, 9821), 1728211191.00)

    def test0303(self):
        self.assertEquals(self.calculate(-99361.0, -11595), 1152090795.00)

    def test0304(self):
        self.assertEquals(self.calculate(-95877.0, 18931), -1815047487.00)

    def test0305(self):
        self.assertEquals(self.calculate(-167754.0, 30708), -5151389832.00)

    def test0306(self):
        self.assertEquals(self.calculate(-140087.0, 18013), -2523387131.00)

    def test0307(self):
        self.assertEquals(self.calculate(-84569.0, 8876), -750634444.00)

    def test0308(self):
        self.assertEquals(self.calculate(-115370.0, 6022), -694758140.00)

    def test0309(self):
        self.assertEquals(self.calculate(-63764.0, 1570), -100109480.00)

    def test0310(self):
        self.assertEquals(self.calculate(-160014.0, 30440), -4870826160.00)

    def test0311(self):
        self.assertEquals(self.calculate(-97079.0, -13486), 1309207394.00)

    def test0312(self):
        self.assertEquals(self.calculate(143093.0, 13427), 1921309711.00)

    def test0313(self):
        self.assertEquals(self.calculate(-44678.0, -24146), 1078794988.00)

    def test0314(self):
        self.assertEquals(self.calculate(124715.0, 8421), 1050225015.00)

    def test0315(self):
        self.assertEquals(self.calculate(44522.0, 21909), 975432498.00)

    def test0316(self):
        self.assertEquals(self.calculate(-182141.0, 13613), -2479485433.00)

    def test0317(self):
        self.assertEquals(self.calculate(135907.0, -31844), -4327822508.00)

    def test0318(self):
        self.assertEquals(self.calculate(-71629.0, 3144), -225201576.00)

    def test0319(self):
        self.assertEquals(self.calculate(-145988.0, -378), 55183464.00)

    def test0320(self):
        self.assertEquals(self.calculate(-46089.0, 10152), -467895528.00)

    def test0321(self):
        self.assertEquals(self.calculate(-56515.0, -18664), 1054795960.00)

    def test0322(self):
        self.assertEquals(self.calculate(27521.0, -5851), -161025371.00)

    def test0323(self):
        self.assertEquals(self.calculate(-37420.0, -12499), 467712580.00)

    def test0324(self):
        self.assertEquals(self.calculate(33783.0, -19946), -673835718.00)

    def test0325(self):
        self.assertEquals(self.calculate(99561.0, -10477), -1043100597.00)

    def test0326(self):
        self.assertEquals(self.calculate(-24357.0, 16043), -390759351.00)

    def test0327(self):
        self.assertEquals(self.calculate(-199647.0, -23455), 4682720385.00)

    def test0328(self):
        self.assertEquals(self.calculate(-153848.0, -2419), 372158312.00)

    def test0329(self):
        self.assertEquals(self.calculate(37416.0, -24450), -914821200.00)

    def test0330(self):
        self.assertEquals(self.calculate(112264.0, 29181), 3275975784.00)

    def test0331(self):
        self.assertEquals(self.calculate(-141187.0, -23054), 3254925098.00)

    def test0332(self):
        self.assertEquals(self.calculate(48771.0, -2508), -122317668.00)

    def test0333(self):
        self.assertEquals(self.calculate(-85500.0, -19954), 1706067000.00)

    def test0334(self):
        self.assertEquals(self.calculate(148157.0, -11027), -1633727239.00)

    def test0335(self):
        self.assertEquals(self.calculate(45794.0, -5622), -257453868.00)

    def test0336(self):
        self.assertEquals(self.calculate(-30841.0, -27628), 852075148.00)

    def test0337(self):
        self.assertEquals(self.calculate(137938.0, 28601), 3945164738.00)

    def test0338(self):
        self.assertEquals(self.calculate(152386.0, -681), -103774866.00)

    def test0339(self):
        self.assertEquals(self.calculate(166723.0, -23183), -3865139309.00)

    def test0340(self):
        self.assertEquals(self.calculate(8712.0, -7268), -63318816.00)

    def test0341(self):
        self.assertEquals(self.calculate(166458.0, -30324), -5047672392.00)

    def test0342(self):
        self.assertEquals(self.calculate(157609.0, -6134), -966773606.00)

    def test0343(self):
        self.assertEquals(self.calculate(119137.0, 8365), 996581005.00)

    def test0344(self):
        self.assertEquals(self.calculate(42191.0, 2129), 89824639.00)

    def test0345(self):
        self.assertEquals(self.calculate(-68833.0, -19597), 1348920301.00)

    def test0346(self):
        self.assertEquals(self.calculate(67233.0, -6551), -440443383.00)

    def test0347(self):
        self.assertEquals(self.calculate(1547.0, -12134), -18771298.00)

    def test0348(self):
        self.assertEquals(self.calculate(-173057.0, 22793), -3944488201.00)

    def test0349(self):
        self.assertEquals(self.calculate(-83508.0, 539), -45010812.00)

    def test0350(self):
        self.assertEquals(self.calculate(54642.0, -32763), -1790235846.00)

    def test0351(self):
        self.assertEquals(self.calculate(117008.0, -16793), -1964915344.00)

    def test0352(self):
        self.assertEquals(self.calculate(177432.0, 17164), 3045442848.00)

    def test0353(self):
        self.assertEquals(self.calculate(176560.0, -28283), -4993646480.00)

    def test0354(self):
        self.assertEquals(self.calculate(-133458.0, -12495), 1667557710.00)

    def test0355(self):
        self.assertEquals(self.calculate(-166435.0, -6264), 1042548840.00)

    def test0356(self):
        self.assertEquals(self.calculate(133547.0, -25412), -3393696364.00)

    def test0357(self):
        self.assertEquals(self.calculate(-77459.0, 10979), -850422361.00)

    def test0358(self):
        self.assertEquals(self.calculate(18410.0, -27189), -500549490.00)

    def test0359(self):
        self.assertEquals(self.calculate(-138422.0, -3126), 432707172.00)

    def test0360(self):
        self.assertEquals(self.calculate(148244.0, 23297), 3453640468.00)

    def test0361(self):
        self.assertEquals(self.calculate(-55257.0, 28861), -1594772277.00)

    def test0362(self):
        self.assertEquals(self.calculate(16497.0, -8447), -139350159.00)

    def test0363(self):
        self.assertEquals(self.calculate(117771.0, 29344), 3455872224.00)

    def test0364(self):
        self.assertEquals(self.calculate(-56159.0, -661), 37121099.00)

    def test0365(self):
        self.assertEquals(self.calculate(-159124.0, -4315), 686620060.00)

    def test0366(self):
        self.assertEquals(self.calculate(137585.0, -8353), -1149247505.00)

    def test0367(self):
        self.assertEquals(self.calculate(137131.0, 20065), 2751533515.00)

    def test0368(self):
        self.assertEquals(self.calculate(-39044.0, -9103), 355417532.00)

    def test0369(self):
        self.assertEquals(self.calculate(-79783.0, 13189), -1052257987.00)

    def test0370(self):
        self.assertEquals(self.calculate(152831.0, -7449), -1138438119.00)

    def test0371(self):
        self.assertEquals(self.calculate(-113373.0, 32006), -3628616238.00)

    def test0372(self):
        self.assertEquals(self.calculate(-93108.0, 11637), -1083497796.00)

    def test0373(self):
        self.assertEquals(self.calculate(-33372.0, -8669), 289301868.00)

    def test0374(self):
        self.assertEquals(self.calculate(-104154.0, 14490), -1509191460.00)

    def test0375(self):
        self.assertEquals(self.calculate(168525.0, 32656), 5503352400.00)

    def test0376(self):
        self.assertEquals(self.calculate(198286.0, 21791), 4320850226.00)

    def test0377(self):
        self.assertEquals(self.calculate(-145878.0, 4994), -728514732.00)

    def test0378(self):
        self.assertEquals(self.calculate(11471.0, -17214), -197461794.00)

    def test0379(self):
        self.assertEquals(self.calculate(98349.0, 30596), 3009086004.00)

    def test0380(self):
        self.assertEquals(self.calculate(33386.0, -25770), -860357220.00)

    def test0381(self):
        self.assertEquals(self.calculate(133013.0, -25426), -3381988538.00)

    def test0382(self):
        self.assertEquals(self.calculate(34606.0, -6012), -208051272.00)

    def test0383(self):
        self.assertEquals(self.calculate(100969.0, -21490), -2169823810.00)

    def test0384(self):
        self.assertEquals(self.calculate(-15455.0, -24185), 373779175.00)

    def test0385(self):
        self.assertEquals(self.calculate(-124484.0, 19482), -2425197288.00)

    def test0386(self):
        self.assertEquals(self.calculate(-70759.0, 6238), -441394642.00)

    def test0387(self):
        self.assertEquals(self.calculate(-110377.0, 29326), -3236915902.00)

    def test0388(self):
        self.assertEquals(self.calculate(-181033.0, 30178), -5463213874.00)

    def test0389(self):
        self.assertEquals(self.calculate(22711.0, 502), 11400922.00)

    def test0390(self):
        self.assertEquals(self.calculate(-198645.0, 8972), -1782242940.00)

    def test0391(self):
        self.assertEquals(self.calculate(166848.0, 22250), 3712368000.00)

    def test0392(self):
        self.assertEquals(self.calculate(-13760.0, 13238), -182154880.00)

    def test0393(self):
        self.assertEquals(self.calculate(-169838.0, -15270), 2593426260.00)

    def test0394(self):
        self.assertEquals(self.calculate(53546.0, 10991), 588524086.00)

    def test0395(self):
        self.assertEquals(self.calculate(-80566.0, 30702), -2473537332.00)

    def test0396(self):
        self.assertEquals(self.calculate(-160596.0, 3230), -518725080.00)

    def test0397(self):
        self.assertEquals(self.calculate(-181164.0, -11982), 2170707048.00)

    def test0398(self):
        self.assertEquals(self.calculate(161288.0, -22849), -3685269512.00)

    def test0399(self):
        self.assertEquals(self.calculate(195085.0, 4201), 819552085.00)

    def test0400(self):
        self.assertEquals(self.calculate(-154390.0, 25990), -4012596100.00)

    def test0401(self):
        self.assertEquals(self.calculate(-21355.0, 13560), -289573800.00)

    def test0402(self):
        self.assertEquals(self.calculate(175225.0, 17570), 3078703250.00)

    def test0403(self):
        self.assertEquals(self.calculate(-130745.0, -25168), 3290590160.00)

    def test0404(self):
        self.assertEquals(self.calculate(-103558.0, 27639), -2862239562.00)

    def test0405(self):
        self.assertEquals(self.calculate(-58151.0, 15781), -917680931.00)

    def test0406(self):
        self.assertEquals(self.calculate(55721.0, -11113), -619227473.00)

    def test0407(self):
        self.assertEquals(self.calculate(-100009.0, 30143), -3014571287.00)

    def test0408(self):
        self.assertEquals(self.calculate(11775.0, -15200), -178980000.00)

    def test0409(self):
        self.assertEquals(self.calculate(124118.0, -17592), -2183483856.00)

    def test0410(self):
        self.assertEquals(self.calculate(49087.0, 16809), 825103383.00)

    def test0411(self):
        self.assertEquals(self.calculate(-174630.0, 31163), -5441994690.00)

    def test0412(self):
        self.assertEquals(self.calculate(114421.0, -32521), -3721085341.00)

    def test0413(self):
        self.assertEquals(self.calculate(-176627.0, 29095), -5138962565.00)

    def test0414(self):
        self.assertEquals(self.calculate(-55455.0, 17916), -993531780.00)

    def test0415(self):
        self.assertEquals(self.calculate(-133014.0, -3112), 413939568.00)

    def test0416(self):
        self.assertEquals(self.calculate(122050.0, -21229), -2590999450.00)

    def test0417(self):
        self.assertEquals(self.calculate(163410.0, -23249), -3799119090.00)

    def test0418(self):
        self.assertEquals(self.calculate(-25722.0, -8760), 225324720.00)

    def test0419(self):
        self.assertEquals(self.calculate(-51053.0, 6385), -325973405.00)

    def test0420(self):
        self.assertEquals(self.calculate(176732.0, 18162), 3209806584.00)

    def test0421(self):
        self.assertEquals(self.calculate(58492.0, -22219), -1299633748.00)

    def test0422(self):
        self.assertEquals(self.calculate(130212.0, 24928), 3245924736.00)

    def test0423(self):
        self.assertEquals(self.calculate(146624.0, 14986), 2197307264.00)

    def test0424(self):
        self.assertEquals(self.calculate(-26235.0, -22368), 586824480.00)

    def test0425(self):
        self.assertEquals(self.calculate(-69239.0, 853), -59060867.00)

    def test0426(self):
        self.assertEquals(self.calculate(138168.0, 23163), 3200385384.00)

    def test0427(self):
        self.assertEquals(self.calculate(-77646.0, -20271), 1573962066.00)

    def test0428(self):
        self.assertEquals(self.calculate(-33163.0, -27688), 918217144.00)

    def test0429(self):
        self.assertEquals(self.calculate(-196256.0, -16618), 3261382208.00)

    def test0430(self):
        self.assertEquals(self.calculate(106659.0, -25176), -2685246984.00)

    def test0431(self):
        self.assertEquals(self.calculate(20214.0, -29339), -593058546.00)

    def test0432(self):
        self.assertEquals(self.calculate(-52094.0, 1288), -67097072.00)

    def test0433(self):
        self.assertEquals(self.calculate(119588.0, -14480), -1731634240.00)

    def test0434(self):
        self.assertEquals(self.calculate(49159.0, -8122), -399269398.00)

    def test0435(self):
        self.assertEquals(self.calculate(-97076.0, 23014), -2234107064.00)

    def test0436(self):
        self.assertEquals(self.calculate(144256.0, 10463), 1509350528.00)

    def test0437(self):
        self.assertEquals(self.calculate(-170238.0, -8812), 1500137256.00)

    def test0438(self):
        self.assertEquals(self.calculate(129314.0, -22953), -2968144242.00)

    def test0439(self):
        self.assertEquals(self.calculate(55622.0, 9490), 527852780.00)

    def test0440(self):
        self.assertEquals(self.calculate(6864.0, 1997), 13707408.00)

    def test0441(self):
        self.assertEquals(self.calculate(160343.0, -31228), -5007191204.00)

    def test0442(self):
        self.assertEquals(self.calculate(-89563.0, 15507), -1388853441.00)

    def test0443(self):
        self.assertEquals(self.calculate(9346.0, 12370), 115610020.00)

    def test0444(self):
        self.assertEquals(self.calculate(92053.0, -9639), -887298867.00)

    def test0445(self):
        self.assertEquals(self.calculate(-41404.0, 29225), -1210031900.00)

    def test0446(self):
        self.assertEquals(self.calculate(-146037.0, 25211), -3681738807.00)

    def test0447(self):
        self.assertEquals(self.calculate(170455.0, 10339), 1762334245.00)

    def test0448(self):
        self.assertEquals(self.calculate(146303.0, 19787), 2894897461.00)

    def test0449(self):
        self.assertEquals(self.calculate(133428.0, 16911), 2256400908.00)

    def test0450(self):
        self.assertEquals(self.calculate(-189204.0, 11747), -2222579388.00)

    def test0451(self):
        self.assertEquals(self.calculate(-181932.0, -22184), 4035979488.00)

    def test0452(self):
        self.assertEquals(self.calculate(150402.0, 4339), 652594278.00)

    def test0453(self):
        self.assertEquals(self.calculate(-67672.0, -1127), 76266344.00)

    def test0454(self):
        self.assertEquals(self.calculate(54278.0, -2632), -142859696.00)

    def test0455(self):
        self.assertEquals(self.calculate(-157455.0, 26509), -4173974595.00)

    def test0456(self):
        self.assertEquals(self.calculate(-16539.0, -652), 10783428.00)

    def test0457(self):
        self.assertEquals(self.calculate(53932.0, 32445), 1749823740.00)

    def test0458(self):
        self.assertEquals(self.calculate(-9775.0, -14399), 140750225.00)

    def test0459(self):
        self.assertEquals(self.calculate(-169983.0, -4153), 705939399.00)

    def test0460(self):
        self.assertEquals(self.calculate(-31441.0, 10314), -324282474.00)

    def test0461(self):
        self.assertEquals(self.calculate(52345.0, 5122), 268111090.00)

    def test0462(self):
        self.assertEquals(self.calculate(100774.0, 23565), 2374739310.00)

    def test0463(self):
        self.assertEquals(self.calculate(176779.0, -19557), -3457266903.00)

    def test0464(self):
        self.assertEquals(self.calculate(-104935.0, -17116), 1796067460.00)

    def test0465(self):
        self.assertEquals(self.calculate(170442.0, 1549), 264014658.00)

    def test0466(self):
        self.assertEquals(self.calculate(141384.0, 23677), 3347548968.00)

    def test0467(self):
        self.assertEquals(self.calculate(145911.0, -13054), -1904722194.00)

    def test0468(self):
        self.assertEquals(self.calculate(141247.0, 23814), 3363656058.00)

    def test0469(self):
        self.assertEquals(self.calculate(-165743.0, 26517), -4395007131.00)

    def test0470(self):
        self.assertEquals(self.calculate(154903.0, 23467), 3635108701.00)

    def test0471(self):
        self.assertEquals(self.calculate(-196584.0, -19145), 3763600680.00)

    def test0472(self):
        self.assertEquals(self.calculate(-15625.0, 14311), -223609375.00)

    def test0473(self):
        self.assertEquals(self.calculate(-16147.0, -13741), 221875927.00)

    def test0474(self):
        self.assertEquals(self.calculate(130579.0, -28688), -3746050352.00)

    def test0475(self):
        self.assertEquals(self.calculate(-7260.0, -2184), 15855840.00)

    def test0476(self):
        self.assertEquals(self.calculate(-40404.0, 24180), -976968720.00)

    def test0477(self):
        self.assertEquals(self.calculate(18090.0, 5282), 95551380.00)

    def test0478(self):
        self.assertEquals(self.calculate(114012.0, -6913), -788164956.00)

    def test0479(self):
        self.assertEquals(self.calculate(-123390.0, 26632), -3286122480.00)

    def test0480(self):
        self.assertEquals(self.calculate(-30336.0, 9989), -303026304.00)

    def test0481(self):
        self.assertEquals(self.calculate(138450.0, -13477), -1865890650.00)

    def test0482(self):
        self.assertEquals(self.calculate(-151996.0, -17384), 2642298464.00)

    def test0483(self):
        self.assertEquals(self.calculate(-94895.0, -844), 80091380.00)

    def test0484(self):
        self.assertEquals(self.calculate(-2086.0, 21422), -44686292.00)

    def test0485(self):
        self.assertEquals(self.calculate(5056.0, 28928), 146259968.00)

    def test0486(self):
        self.assertEquals(self.calculate(39483.0, -26879), -1061263557.00)

    def test0487(self):
        self.assertEquals(self.calculate(-50975.0, 23618), -1203927550.00)

    def test0488(self):
        self.assertEquals(self.calculate(58422.0, -26641), -1556420502.00)

    def test0489(self):
        self.assertEquals(self.calculate(-117639.0, -29169), 3431411991.00)

    def test0490(self):
        self.assertEquals(self.calculate(-68271.0, -20348), 1389178308.00)

    def test0491(self):
        self.assertEquals(self.calculate(45924.0, 3875), 177955500.00)

    def test0492(self):
        self.assertEquals(self.calculate(-163534.0, -9254), 1513343636.00)

    def test0493(self):
        self.assertEquals(self.calculate(-94563.0, -744), 70354872.00)

    def test0494(self):
        self.assertEquals(self.calculate(96487.0, -21468), -2071382916.00)

    def test0495(self):
        self.assertEquals(self.calculate(143223.0, -21350), -3057811050.00)

    def test0496(self):
        self.assertEquals(self.calculate(20528.0, -11015), -226115920.00)

    def test0497(self):
        self.assertEquals(self.calculate(-101984.0, -24815), 2530732960.00)

    def test0498(self):
        self.assertEquals(self.calculate(-446.0, 4577), -2041342.00)

    def test0499(self):
        self.assertEquals(self.calculate(91290.0, -365), -33320850.00)

    def test0500(self):
        self.assertEquals(self.calculate(91061.0, 27034), 2461743074.00)

    def test0501(self):
        self.assertEquals(self.calculate(-66118.0, -30267), 2001193506.00)

    def test0502(self):
        self.assertEquals(self.calculate(144953.0, 4815), 697948695.00)

    def test0503(self):
        self.assertEquals(self.calculate(-167559.0, -20197), 3384189123.00)

    def test0504(self):
        self.assertEquals(self.calculate(-174908.0, -28700), 5019859600.00)

    def test0505(self):
        self.assertEquals(self.calculate(-54900.0, -15005), 823774500.00)

    def test0506(self):
        self.assertEquals(self.calculate(98298.0, 21591), 2122352118.00)

    def test0507(self):
        self.assertEquals(self.calculate(45582.0, 16863), 768649266.00)

    def test0508(self):
        self.assertEquals(self.calculate(124128.0, -5971), -741168288.00)

    def test0509(self):
        self.assertEquals(self.calculate(30128.0, -4592), -138347776.00)

    def test0510(self):
        self.assertEquals(self.calculate(-103868.0, 1324), -137521232.00)

    def test0511(self):
        self.assertEquals(self.calculate(46624.0, -11051), -515241824.00)

    def test0512(self):
        self.assertEquals(self.calculate(-86923.0, 23854), -2073461242.00)

    def test0513(self):
        self.assertEquals(self.calculate(-59840.0, 15133), -905558720.00)

    def test0514(self):
        self.assertEquals(self.calculate(102158.0, -23406), -2391110148.00)

    def test0515(self):
        self.assertEquals(self.calculate(98305.0, 8327), 818585735.00)

    def test0516(self):
        self.assertEquals(self.calculate(40903.0, -30810), -1260221430.00)

    def test0517(self):
        self.assertEquals(self.calculate(-129165.0, -31949), 4126692585.00)

    def test0518(self):
        self.assertEquals(self.calculate(142586.0, -12037), -1716307682.00)

    def test0519(self):
        self.assertEquals(self.calculate(-173461.0, -8967), 1555424787.00)

    def test0520(self):
        self.assertEquals(self.calculate(91717.0, 31657), 2903485069.00)

    def test0521(self):
        self.assertEquals(self.calculate(156225.0, 27370), 4275878250.00)

    def test0522(self):
        self.assertEquals(self.calculate(-5042.0, 14988), -75569496.00)

    def test0523(self):
        self.assertEquals(self.calculate(50691.0, -6723), -340795593.00)

    def test0524(self):
        self.assertEquals(self.calculate(-85417.0, 32754), -2797748418.00)

    def test0525(self):
        self.assertEquals(self.calculate(138428.0, 31601), 4374463228.00)

    def test0526(self):
        self.assertEquals(self.calculate(85172.0, 6741), 574144452.00)

    def test0527(self):
        self.assertEquals(self.calculate(117028.0, 10671), 1248805788.00)

    def test0528(self):
        self.assertEquals(self.calculate(-141833.0, 2957), -419400181.00)

    def test0529(self):
        self.assertEquals(self.calculate(164333.0, -14052), -2309207316.00)

    def test0530(self):
        self.assertEquals(self.calculate(112956.0, -16327), -1844232612.00)

    def test0531(self):
        self.assertEquals(self.calculate(-108481.0, 5062), -549130822.00)

    def test0532(self):
        self.assertEquals(self.calculate(-166513.0, -22461), 3740048493.00)

    def test0533(self):
        self.assertEquals(self.calculate(53726.0, 20018), 1075487068.00)

    def test0534(self):
        self.assertEquals(self.calculate(-68989.0, 2228), -153707492.00)

    def test0535(self):
        self.assertEquals(self.calculate(-122485.0, -5298), 648925530.00)

    def test0536(self):
        self.assertEquals(self.calculate(147946.0, -7449), -1102049754.00)

    def test0537(self):
        self.assertEquals(self.calculate(155768.0, 23641), 3682511288.00)

    def test0538(self):
        self.assertEquals(self.calculate(-64653.0, -2881), 186265293.00)

    def test0539(self):
        self.assertEquals(self.calculate(48899.0, 18466), 902968934.00)

    def test0540(self):
        self.assertEquals(self.calculate(195115.0, 1323), 258137145.00)

    def test0541(self):
        self.assertEquals(self.calculate(-26933.0, -25040), 674402320.00)

    def test0542(self):
        self.assertEquals(self.calculate(103452.0, 3894), 402842088.00)

    def test0543(self):
        self.assertEquals(self.calculate(-1439.0, -15009), 21597951.00)

    def test0544(self):
        self.assertEquals(self.calculate(-145311.0, 25823), -3752365953.00)

    def test0545(self):
        self.assertEquals(self.calculate(182167.0, -2498), -455053166.00)

    def test0546(self):
        self.assertEquals(self.calculate(-153782.0, 3613), -555614366.00)

    def test0547(self):
        self.assertEquals(self.calculate(51877.0, -832), -43161664.00)

    def test0548(self):
        self.assertEquals(self.calculate(64738.0, 165), 10681770.00)

    def test0549(self):
        self.assertEquals(self.calculate(126807.0, 17492), 2218108044.00)

    def test0550(self):
        self.assertEquals(self.calculate(16151.0, 15274), 246690374.00)

    def test0551(self):
        self.assertEquals(self.calculate(-124673.0, 12294), -1532729862.00)

    def test0552(self):
        self.assertEquals(self.calculate(197561.0, -953), -188275633.00)

    def test0553(self):
        self.assertEquals(self.calculate(77845.0, -32511), -2530818795.00)

    def test0554(self):
        self.assertEquals(self.calculate(142964.0, -17750), -2537611000.00)

    def test0555(self):
        self.assertEquals(self.calculate(71277.0, 30114), 2146435578.00)

    def test0556(self):
        self.assertEquals(self.calculate(-77496.0, 17117), -1326499032.00)

    def test0557(self):
        self.assertEquals(self.calculate(177770.0, -1235), -219545950.00)

    def test0558(self):
        self.assertEquals(self.calculate(-182498.0, -18923), 3453409654.00)

    def test0559(self):
        self.assertEquals(self.calculate(-106252.0, 18727), -1989781204.00)

    def test0560(self):
        self.assertEquals(self.calculate(-66769.0, -23773), 1587299437.00)

    def test0561(self):
        self.assertEquals(self.calculate(-95341.0, 929), -88571789.00)

    def test0562(self):
        self.assertEquals(self.calculate(-5857.0, 18758), -109865606.00)

    def test0563(self):
        self.assertEquals(self.calculate(92577.0, -26069), -2413389813.00)

    def test0564(self):
        self.assertEquals(self.calculate(91110.0, -17646), -1607727060.00)

    def test0565(self):
        self.assertEquals(self.calculate(145729.0, -18161), -2646584369.00)

    def test0566(self):
        self.assertEquals(self.calculate(124294.0, -27460), -3413113240.00)

    def test0567(self):
        self.assertEquals(self.calculate(-121171.0, 4712), -570957752.00)

    def test0568(self):
        self.assertEquals(self.calculate(-157213.0, 17008), -2673878704.00)

    def test0569(self):
        self.assertEquals(self.calculate(157018.0, 10772), 1691397896.00)

    def test0570(self):
        self.assertEquals(self.calculate(-196320.0, -23641), 4641201120.00)

    def test0571(self):
        self.assertEquals(self.calculate(57393.0, -10941), -627936813.00)

    def test0572(self):
        self.assertEquals(self.calculate(153752.0, -13392), -2059046784.00)

    def test0573(self):
        self.assertEquals(self.calculate(84363.0, 11562), 975405006.00)

    def test0574(self):
        self.assertEquals(self.calculate(47120.0, 12550), 591356000.00)

    def test0575(self):
        self.assertEquals(self.calculate(-149307.0, -22289), 3327903723.00)

    def test0576(self):
        self.assertEquals(self.calculate(-180767.0, -28445), 5141917315.00)

    def test0577(self):
        self.assertEquals(self.calculate(-47793.0, 15330), -732666690.00)

    def test0578(self):
        self.assertEquals(self.calculate(-178787.0, 12662), -2263800994.00)

    def test0579(self):
        self.assertEquals(self.calculate(112529.0, 11973), 1347309717.00)

    def test0580(self):
        self.assertEquals(self.calculate(-32465.0, 3061), -99375365.00)

    def test0581(self):
        self.assertEquals(self.calculate(-11707.0, -9892), 115805644.00)

    def test0582(self):
        self.assertEquals(self.calculate(-197816.0, 11043), -2184482088.00)

    def test0583(self):
        self.assertEquals(self.calculate(178803.0, 15754), 2816862462.00)

    def test0584(self):
        self.assertEquals(self.calculate(-88225.0, -24710), 2180039750.00)

    def test0585(self):
        self.assertEquals(self.calculate(27230.0, 3555), 96802650.00)

    def test0586(self):
        self.assertEquals(self.calculate(-3226.0, -3288), 10607088.00)

    def test0587(self):
        self.assertEquals(self.calculate(-198996.0, -7008), 1394563968.00)

    def test0588(self):
        self.assertEquals(self.calculate(-73540.0, -32348), 2378871920.00)

    def test0589(self):
        self.assertEquals(self.calculate(-120520.0, 31341), -3777217320.00)

    def test0590(self):
        self.assertEquals(self.calculate(107689.0, -4677), -503661453.00)

    def test0591(self):
        self.assertEquals(self.calculate(160676.0, 3944), 633706144.00)

    def test0592(self):
        self.assertEquals(self.calculate(-174792.0, -6578), 1149781776.00)

    def test0593(self):
        self.assertEquals(self.calculate(154201.0, -7439), -1147101239.00)

    def test0594(self):
        self.assertEquals(self.calculate(155423.0, -9386), -1458800278.00)

    def test0595(self):
        self.assertEquals(self.calculate(-31599.0, 12760), -403203240.00)

    def test0596(self):
        self.assertEquals(self.calculate(26426.0, 16307), 430928782.00)

    def test0597(self):
        self.assertEquals(self.calculate(-68273.0, -22454), 1533001942.00)

    def test0598(self):
        self.assertEquals(self.calculate(93156.0, 5886), 548316216.00)

    def test0599(self):
        self.assertEquals(self.calculate(-138567.0, -22140), 3067873380.00)

    def test0600(self):
        self.assertEquals(self.calculate(74748.0, -29798), -2227340904.00)

    def test0601(self):
        self.assertEquals(self.calculate(119562.0, 4058), 485182596.00)

    def test0602(self):
        self.assertEquals(self.calculate(124278.0, -2974), -369602772.00)

    def test0603(self):
        self.assertEquals(self.calculate(-144141.0, 18291), -2636483031.00)

    def test0604(self):
        self.assertEquals(self.calculate(53417.0, 10835), 578773195.00)

    def test0605(self):
        self.assertEquals(self.calculate(141918.0, 23391), 3319603938.00)

    def test0606(self):
        self.assertEquals(self.calculate(-143817.0, 13144), -1890330648.00)

    def test0607(self):
        self.assertEquals(self.calculate(-184991.0, 8401), -1554109391.00)

    def test0608(self):
        self.assertEquals(self.calculate(192775.0, 29390), 5665657250.00)

    def test0609(self):
        self.assertEquals(self.calculate(-21152.0, 26213), -554457376.00)

    def test0610(self):
        self.assertEquals(self.calculate(-90172.0, 27456), -2475762432.00)

    def test0611(self):
        self.assertEquals(self.calculate(13307.0, 6987), 92976009.00)

    def test0612(self):
        self.assertEquals(self.calculate(19269.0, 1033), 19904877.00)

    def test0613(self):
        self.assertEquals(self.calculate(42643.0, -15645), -667149735.00)

    def test0614(self):
        self.assertEquals(self.calculate(-170168.0, 6556), -1115621408.00)

    def test0615(self):
        self.assertEquals(self.calculate(-82716.0, -11623), 961408068.00)

    def test0616(self):
        self.assertEquals(self.calculate(-194372.0, -21990), 4274240280.00)

    def test0617(self):
        self.assertEquals(self.calculate(133057.0, 20693), 2753348501.00)

    def test0618(self):
        self.assertEquals(self.calculate(-39322.0, -2273), 89378906.00)

    def test0619(self):
        self.assertEquals(self.calculate(164520.0, 24318), 4000797360.00)

    def test0620(self):
        self.assertEquals(self.calculate(-168576.0, 29778), -5019856128.00)

    def test0621(self):
        self.assertEquals(self.calculate(130545.0, -27706), -3616879770.00)

    def test0622(self):
        self.assertEquals(self.calculate(36400.0, 11422), 415760800.00)

    def test0623(self):
        self.assertEquals(self.calculate(-183029.0, -32685), 5982302865.00)

    def test0624(self):
        self.assertEquals(self.calculate(74425.0, 25946), 1931031050.00)

    def test0625(self):
        self.assertEquals(self.calculate(153917.0, 4023), 619208091.00)

    def test0626(self):
        self.assertEquals(self.calculate(-75272.0, -683), 51410776.00)

    def test0627(self):
        self.assertEquals(self.calculate(-175253.0, 13131), -2301247143.00)

    def test0628(self):
        self.assertEquals(self.calculate(94053.0, 1887), 177478011.00)

    def test0629(self):
        self.assertEquals(self.calculate(26448.0, -2532), -66966336.00)

    def test0630(self):
        self.assertEquals(self.calculate(92554.0, -16144), -1494191776.00)

    def test0631(self):
        self.assertEquals(self.calculate(125833.0, -1220), -153516260.00)

    def test0632(self):
        self.assertEquals(self.calculate(99171.0, -13873), -1375799283.00)

    def test0633(self):
        self.assertEquals(self.calculate(-66437.0, -10018), 665565866.00)

    def test0634(self):
        self.assertEquals(self.calculate(-54338.0, -27422), 1490056636.00)

    def test0635(self):
        self.assertEquals(self.calculate(112439.0, 29045), 3265790755.00)

    def test0636(self):
        self.assertEquals(self.calculate(142112.0, -11733), -1667400096.00)

    def test0637(self):
        self.assertEquals(self.calculate(-141862.0, -26484), 3757073208.00)

    def test0638(self):
        self.assertEquals(self.calculate(-127461.0, 18931), -2412964191.00)

    def test0639(self):
        self.assertEquals(self.calculate(185141.0, -591), -109418331.00)

    def test0640(self):
        self.assertEquals(self.calculate(21948.0, 16263), 356940324.00)

    def test0641(self):
        self.assertEquals(self.calculate(144937.0, 17683), 2562920971.00)

    def test0642(self):
        self.assertEquals(self.calculate(2411.0, -9059), -21841249.00)

    def test0643(self):
        self.assertEquals(self.calculate(-43211.0, 28485), -1230865335.00)

    def test0644(self):
        self.assertEquals(self.calculate(-59636.0, 17323), -1033074428.00)

    def test0645(self):
        self.assertEquals(self.calculate(174457.0, -23134), -4035888238.00)

    def test0646(self):
        self.assertEquals(self.calculate(168817.0, 10121), 1708596857.00)

    def test0647(self):
        self.assertEquals(self.calculate(92636.0, -12592), -1166472512.00)

    def test0648(self):
        self.assertEquals(self.calculate(190782.0, 9564), 1824639048.00)

    def test0649(self):
        self.assertEquals(self.calculate(53978.0, 32762), 1768427236.00)

    def test0650(self):
        self.assertEquals(self.calculate(47752.0, -29034), -1386431568.00)

    def test0651(self):
        self.assertEquals(self.calculate(-25752.0, 2890), -74423280.00)

    def test0652(self):
        self.assertEquals(self.calculate(-53203.0, -21954), 1168018662.00)

    def test0653(self):
        self.assertEquals(self.calculate(-121300.0, -28400), 3444920000.00)

    def test0654(self):
        self.assertEquals(self.calculate(-47706.0, -5269), 251362914.00)

    def test0655(self):
        self.assertEquals(self.calculate(35690.0, 23691), 845531790.00)

    def test0656(self):
        self.assertEquals(self.calculate(-177045.0, 31126), -5510702670.00)

    def test0657(self):
        self.assertEquals(self.calculate(185977.0, 13846), 2575037542.00)

    def test0658(self):
        self.assertEquals(self.calculate(-141237.0, -31910), 4506872670.00)

    def test0659(self):
        self.assertEquals(self.calculate(27448.0, -15700), -430933600.00)

    def test0660(self):
        self.assertEquals(self.calculate(131519.0, -13054), -1716849026.00)

    def test0661(self):
        self.assertEquals(self.calculate(-92664.0, -13159), 1219365576.00)

    def test0662(self):
        self.assertEquals(self.calculate(133239.0, -23835), -3175751565.00)

    def test0663(self):
        self.assertEquals(self.calculate(-187666.0, -2376), 445894416.00)

    def test0664(self):
        self.assertEquals(self.calculate(-60710.0, 11220), -681166200.00)

    def test0665(self):
        self.assertEquals(self.calculate(122408.0, 10468), 1281366944.00)

    def test0666(self):
        self.assertEquals(self.calculate(-18776.0, 19271), -361832296.00)

    def test0667(self):
        self.assertEquals(self.calculate(-138940.0, -3359), 466699460.00)

    def test0668(self):
        self.assertEquals(self.calculate(170947.0, 1503), 256933341.00)

    def test0669(self):
        self.assertEquals(self.calculate(140496.0, 12603), 1770671088.00)

    def test0670(self):
        self.assertEquals(self.calculate(115675.0, -7275), -841535625.00)

    def test0671(self):
        self.assertEquals(self.calculate(-72390.0, -25153), 1820825670.00)

    def test0672(self):
        self.assertEquals(self.calculate(-138180.0, -14836), 2050038480.00)

    def test0673(self):
        self.assertEquals(self.calculate(155103.0, -3417), -529986951.00)

    def test0674(self):
        self.assertEquals(self.calculate(-112135.0, -28170), 3158842950.00)

    def test0675(self):
        self.assertEquals(self.calculate(20002.0, 29785), 595759570.00)

    def test0676(self):
        self.assertEquals(self.calculate(-90574.0, 4134), -374432916.00)

    def test0677(self):
        self.assertEquals(self.calculate(-136981.0, -21139), 2895641359.00)

    def test0678(self):
        self.assertEquals(self.calculate(68473.0, 23137), 1584259801.00)

    def test0679(self):
        self.assertEquals(self.calculate(-77696.0, -11162), 867242752.00)

    def test0680(self):
        self.assertEquals(self.calculate(35306.0, -3470), -122511820.00)

    def test0681(self):
        self.assertEquals(self.calculate(66494.0, 13540), 900328760.00)

    def test0682(self):
        self.assertEquals(self.calculate(-56088.0, 8681), -486899928.00)

    def test0683(self):
        self.assertEquals(self.calculate(-176363.0, -8165), 1440003895.00)

    def test0684(self):
        self.assertEquals(self.calculate(-123849.0, 23828), -2951073972.00)

    def test0685(self):
        self.assertEquals(self.calculate(-457.0, 9233), -4219481.00)

    def test0686(self):
        self.assertEquals(self.calculate(-37978.0, -25604), 972388712.00)

    def test0687(self):
        self.assertEquals(self.calculate(89191.0, -20838), -1858562058.00)

    def test0688(self):
        self.assertEquals(self.calculate(1013.0, -6115), -6194495.00)

    def test0689(self):
        self.assertEquals(self.calculate(-37798.0, -8287), 313232026.00)

    def test0690(self):
        self.assertEquals(self.calculate(-105794.0, 2957), -312832858.00)

    def test0691(self):
        self.assertEquals(self.calculate(-174914.0, 29673), -5190223122.00)

    def test0692(self):
        self.assertEquals(self.calculate(154666.0, 10594), 1638531604.00)

    def test0693(self):
        self.assertEquals(self.calculate(5845.0, 3830), 22386350.00)

    def test0694(self):
        self.assertEquals(self.calculate(31941.0, -7463), -238375683.00)

    def test0695(self):
        self.assertEquals(self.calculate(-192836.0, -25786), 4972469096.00)

    def test0696(self):
        self.assertEquals(self.calculate(186389.0, -15083), -2811305287.00)

    def test0697(self):
        self.assertEquals(self.calculate(74224.0, -13584), -1008258816.00)

    def test0698(self):
        self.assertEquals(self.calculate(-102043.0, 7752), -791037336.00)

    def test0699(self):
        self.assertEquals(self.calculate(-75069.0, 18073), -1356722037.00)

    def test0700(self):
        self.assertEquals(self.calculate(12258.0, 12156), 149008248.00)

    def test0701(self):
        self.assertEquals(self.calculate(-48039.0, -22125), 1062862875.00)

    def test0702(self):
        self.assertEquals(self.calculate(195981.0, 8397), 1645652457.00)

    def test0703(self):
        self.assertEquals(self.calculate(9502.0, 15565), 147898630.00)

    def test0704(self):
        self.assertEquals(self.calculate(-162437.0, -5466), 887880642.00)

    def test0705(self):
        self.assertEquals(self.calculate(134669.0, 16407), 2209514283.00)

    def test0706(self):
        self.assertEquals(self.calculate(-64464.0, 7713), -497210832.00)

    def test0707(self):
        self.assertEquals(self.calculate(177581.0, 1822), 323552582.00)

    def test0708(self):
        self.assertEquals(self.calculate(45488.0, 25687), 1168450256.00)

    def test0709(self):
        self.assertEquals(self.calculate(67975.0, 635), 43164125.00)

    def test0710(self):
        self.assertEquals(self.calculate(-12044.0, -4041), 48669804.00)

    def test0711(self):
        self.assertEquals(self.calculate(-64461.0, -22813), 1470548793.00)

    def test0712(self):
        self.assertEquals(self.calculate(-7477.0, -22215), 166101555.00)

    def test0713(self):
        self.assertEquals(self.calculate(124338.0, -12313), -1530973794.00)

    def test0714(self):
        self.assertEquals(self.calculate(-167369.0, -12488), 2090104072.00)

    def test0715(self):
        self.assertEquals(self.calculate(132242.0, 17901), 2367264042.00)

    def test0716(self):
        self.assertEquals(self.calculate(-71929.0, 24276), -1746148404.00)

    def test0717(self):
        self.assertEquals(self.calculate(148736.0, -4320), -642539520.00)

    def test0718(self):
        self.assertEquals(self.calculate(-196857.0, 20656), -4066278192.00)

    def test0719(self):
        self.assertEquals(self.calculate(145813.0, -16433), -2396145029.00)

    def test0720(self):
        self.assertEquals(self.calculate(68402.0, -2267), -155067334.00)

    def test0721(self):
        self.assertEquals(self.calculate(119864.0, 17017), 2039725688.00)

    def test0722(self):
        self.assertEquals(self.calculate(-27345.0, 22855), -624969975.00)

    def test0723(self):
        self.assertEquals(self.calculate(88678.0, 10459), 927483202.00)

    def test0724(self):
        self.assertEquals(self.calculate(-77870.0, -21439), 1669454930.00)

    def test0725(self):
        self.assertEquals(self.calculate(43930.0, -10424), -457926320.00)

    def test0726(self):
        self.assertEquals(self.calculate(-157910.0, -10935), 1726745850.00)

    def test0727(self):
        self.assertEquals(self.calculate(-175907.0, -6016), 1058256512.00)

    def test0728(self):
        self.assertEquals(self.calculate(176933.0, -11452), -2026236716.00)

    def test0729(self):
        self.assertEquals(self.calculate(16194.0, -19072), -308851968.00)

    def test0730(self):
        self.assertEquals(self.calculate(68152.0, -1194), -81373488.00)

    def test0731(self):
        self.assertEquals(self.calculate(78461.0, 16346), 1282523506.00)

    def test0732(self):
        self.assertEquals(self.calculate(140355.0, -7776), -1091400480.00)

    def test0733(self):
        self.assertEquals(self.calculate(13930.0, 15238), 212265340.00)

    def test0734(self):
        self.assertEquals(self.calculate(-22578.0, 23441), -529250898.00)

    def test0735(self):
        self.assertEquals(self.calculate(-31602.0, -9662), 305338524.00)

    def test0736(self):
        self.assertEquals(self.calculate(132790.0, -228), -30276120.00)

    def test0737(self):
        self.assertEquals(self.calculate(89317.0, -28648), -2558753416.00)

    def test0738(self):
        self.assertEquals(self.calculate(112259.0, -17969), -2017181971.00)

    def test0739(self):
        self.assertEquals(self.calculate(-129073.0, 22395), -2890589835.00)

    def test0740(self):
        self.assertEquals(self.calculate(-70282.0, -12487), 877611334.00)

    def test0741(self):
        self.assertEquals(self.calculate(162891.0, -8657), -1410147387.00)

    def test0742(self):
        self.assertEquals(self.calculate(-196188.0, 19159), -3758765892.00)

    def test0743(self):
        self.assertEquals(self.calculate(-49811.0, -14613), 727888143.00)

    def test0744(self):
        self.assertEquals(self.calculate(-160511.0, -24583), 3945841913.00)

    def test0745(self):
        self.assertEquals(self.calculate(175838.0, 23247), 4087705986.00)

    def test0746(self):
        self.assertEquals(self.calculate(-94898.0, -31430), 2982644140.00)

    def test0747(self):
        self.assertEquals(self.calculate(-193898.0, -4653), 902207394.00)

    def test0748(self):
        self.assertEquals(self.calculate(155631.0, 26926), 4190520306.00)

    def test0749(self):
        self.assertEquals(self.calculate(157789.0, -15641), -2467977749.00)

    def test0750(self):
        self.assertEquals(self.calculate(-55214.0, 11483), -634022362.00)

    def test0751(self):
        self.assertEquals(self.calculate(14415.0, 5371), 77422965.00)

    def test0752(self):
        self.assertEquals(self.calculate(-116339.0, -17989), 2092822271.00)

    def test0753(self):
        self.assertEquals(self.calculate(-179533.0, 9821), -1763193593.00)

    def test0754(self):
        self.assertEquals(self.calculate(-123217.0, 21048), -2593471416.00)

    def test0755(self):
        self.assertEquals(self.calculate(-118267.0, -12201), 1442975667.00)

    def test0756(self):
        self.assertEquals(self.calculate(-56454.0, -3577), 201935958.00)

    def test0757(self):
        self.assertEquals(self.calculate(165332.0, 13621), 2251987172.00)

    def test0758(self):
        self.assertEquals(self.calculate(-104397.0, 31866), -3326714802.00)

    def test0759(self):
        self.assertEquals(self.calculate(-119940.0, -26111), 3131753340.00)

    def test0760(self):
        self.assertEquals(self.calculate(-110374.0, -27009), 2981091366.00)

    def test0761(self):
        self.assertEquals(self.calculate(-115538.0, 2877), -332402826.00)

    def test0762(self):
        self.assertEquals(self.calculate(40534.0, -24063), -975369642.00)

    def test0763(self):
        self.assertEquals(self.calculate(116806.0, 20747), 2423374082.00)

    def test0764(self):
        self.assertEquals(self.calculate(164972.0, -24637), -4064415164.00)

    def test0765(self):
        self.assertEquals(self.calculate(178172.0, -30616), -5454913952.00)

    def test0766(self):
        self.assertEquals(self.calculate(-57965.0, 27111), -1571489115.00)

    def test0767(self):
        self.assertEquals(self.calculate(-70248.0, 27729), -1947906792.00)

    def test0768(self):
        self.assertEquals(self.calculate(-177601.0, 5031), -893510631.00)

    def test0769(self):
        self.assertEquals(self.calculate(116934.0, 27181), 3178383054.00)

    def test0770(self):
        self.assertEquals(self.calculate(5078.0, 17541), 89073198.00)

    def test0771(self):
        self.assertEquals(self.calculate(110402.0, 30800), 3400381600.00)

    def test0772(self):
        self.assertEquals(self.calculate(52032.0, 29088), 1513506816.00)

    def test0773(self):
        self.assertEquals(self.calculate(-94239.0, -11890), 1120501710.00)

    def test0774(self):
        self.assertEquals(self.calculate(-169366.0, 15829), -2680894414.00)

    def test0775(self):
        self.assertEquals(self.calculate(158194.0, -31523), -4986749462.00)

    def test0776(self):
        self.assertEquals(self.calculate(-125300.0, -15791), 1978612300.00)

    def test0777(self):
        self.assertEquals(self.calculate(55466.0, 852), 47257032.00)

    def test0778(self):
        self.assertEquals(self.calculate(-67306.0, -24674), 1660708244.00)

    def test0779(self):
        self.assertEquals(self.calculate(-108134.0, -23725), 2565479150.00)

    def test0780(self):
        self.assertEquals(self.calculate(-97292.0, 9008), -876406336.00)

    def test0781(self):
        self.assertEquals(self.calculate(147468.0, -20081), -2961304908.00)

    def test0782(self):
        self.assertEquals(self.calculate(101986.0, 15491), 1579865126.00)

    def test0783(self):
        self.assertEquals(self.calculate(62610.0, 12295), 769789950.00)

    def test0784(self):
        self.assertEquals(self.calculate(107620.0, -8129), -874842980.00)

    def test0785(self):
        self.assertEquals(self.calculate(102814.0, 9402), 966657228.00)

    def test0786(self):
        self.assertEquals(self.calculate(37887.0, -27140), -1028253180.00)

    def test0787(self):
        self.assertEquals(self.calculate(135735.0, -1170), -158809950.00)

    def test0788(self):
        self.assertEquals(self.calculate(-48282.0, -4734), 228566988.00)

    def test0789(self):
        self.assertEquals(self.calculate(-86087.0, 20400), -1756174800.00)

    def test0790(self):
        self.assertEquals(self.calculate(-187272.0, -12103), 2266553016.00)

    def test0791(self):
        self.assertEquals(self.calculate(-135001.0, 1818), -245431818.00)

    def test0792(self):
        self.assertEquals(self.calculate(35746.0, -25952), -927680192.00)

    def test0793(self):
        self.assertEquals(self.calculate(144324.0, 3746), 540637704.00)

    def test0794(self):
        self.assertEquals(self.calculate(23575.0, 25425), 599394375.00)

    def test0795(self):
        self.assertEquals(self.calculate(117074.0, -26517), -3104451258.00)

    def test0796(self):
        self.assertEquals(self.calculate(-185617.0, -5303), 984326951.00)

    def test0797(self):
        self.assertEquals(self.calculate(104781.0, -23556), -2468221236.00)

    def test0798(self):
        self.assertEquals(self.calculate(-99915.0, 14706), -1469349990.00)

    def test0799(self):
        self.assertEquals(self.calculate(112503.0, 23864), 2684771592.00)

    def test0800(self):
        self.assertEquals(self.calculate(181448.0, -9565), -1735550120.00)

    def test0801(self):
        self.assertEquals(self.calculate(43067.0, -21416), -922322872.00)

    def test0802(self):
        self.assertEquals(self.calculate(162040.0, 8999), 1458197960.00)

    def test0803(self):
        self.assertEquals(self.calculate(-63688.0, 15971), -1017161048.00)

    def test0804(self):
        self.assertEquals(self.calculate(-69016.0, 14878), -1026820048.00)

    def test0805(self):
        self.assertEquals(self.calculate(11069.0, -16191), -179218179.00)

    def test0806(self):
        self.assertEquals(self.calculate(-104785.0, 6407), -671357495.00)

    def test0807(self):
        self.assertEquals(self.calculate(67254.0, -17656), -1187436624.00)

    def test0808(self):
        self.assertEquals(self.calculate(128867.0, -18450), -2377596150.00)

    def test0809(self):
        self.assertEquals(self.calculate(176076.0, 24986), 4399434936.00)

    def test0810(self):
        self.assertEquals(self.calculate(-12905.0, -5517), 71196885.00)

    def test0811(self):
        self.assertEquals(self.calculate(14113.0, 2181), 30780453.00)

    def test0812(self):
        self.assertEquals(self.calculate(-102424.0, -32375), 3315977000.00)

    def test0813(self):
        self.assertEquals(self.calculate(140895.0, 4569), 643749255.00)

    def test0814(self):
        self.assertEquals(self.calculate(49943.0, -31930), -1594679990.00)

    def test0815(self):
        self.assertEquals(self.calculate(19236.0, 9660), 185819760.00)

    def test0816(self):
        self.assertEquals(self.calculate(6132.0, 23624), 144862368.00)

    def test0817(self):
        self.assertEquals(self.calculate(121900.0, 22336), 2722758400.00)

    def test0818(self):
        self.assertEquals(self.calculate(61505.0, 3137), 192941185.00)

    def test0819(self):
        self.assertEquals(self.calculate(52137.0, -30047), -1566560439.00)

    def test0820(self):
        self.assertEquals(self.calculate(114180.0, 28018), 3199095240.00)

    def test0821(self):
        self.assertEquals(self.calculate(-7237.0, -17756), 128500172.00)

    def test0822(self):
        self.assertEquals(self.calculate(10873.0, -12917), -140446541.00)

    def test0823(self):
        self.assertEquals(self.calculate(-178895.0, -14640), 2619022800.00)

    def test0824(self):
        self.assertEquals(self.calculate(-1542.0, 412), -635304.00)

    def test0825(self):
        self.assertEquals(self.calculate(123853.0, 12547), 1553983591.00)

    def test0826(self):
        self.assertEquals(self.calculate(-75126.0, -31722), 2383146972.00)

    def test0827(self):
        self.assertEquals(self.calculate(92311.0, 31472), 2905211792.00)

    def test0828(self):
        self.assertEquals(self.calculate(-18115.0, -15528), 281289720.00)

    def test0829(self):
        self.assertEquals(self.calculate(169877.0, -21623), -3673250371.00)

    def test0830(self):
        self.assertEquals(self.calculate(140149.0, 17188), 2408881012.00)

    def test0831(self):
        self.assertEquals(self.calculate(68821.0, -18300), -1259424300.00)

    def test0832(self):
        self.assertEquals(self.calculate(118514.0, 1809), 214391826.00)

    def test0833(self):
        self.assertEquals(self.calculate(-1405.0, -21669), 30444945.00)

    def test0834(self):
        self.assertEquals(self.calculate(91104.0, -14568), -1327203072.00)

    def test0835(self):
        self.assertEquals(self.calculate(18542.0, 3959), 73407778.00)

    def test0836(self):
        self.assertEquals(self.calculate(-137831.0, 15264), -2103852384.00)

    def test0837(self):
        self.assertEquals(self.calculate(33586.0, 3863), 129742718.00)

    def test0838(self):
        self.assertEquals(self.calculate(-55580.0, 4110), -228433800.00)

    def test0839(self):
        self.assertEquals(self.calculate(-142653.0, -28387), 4049490711.00)

    def test0840(self):
        self.assertEquals(self.calculate(19725.0, 20802), 410319450.00)

    def test0841(self):
        self.assertEquals(self.calculate(143189.0, 16859), 2414023351.00)

    def test0842(self):
        self.assertEquals(self.calculate(-69875.0, 9876), -690085500.00)

    def test0843(self):
        self.assertEquals(self.calculate(14215.0, 24113), 342766295.00)

    def test0844(self):
        self.assertEquals(self.calculate(105795.0, -6193), -655188435.00)

    def test0845(self):
        self.assertEquals(self.calculate(120657.0, 30964), 3736023348.00)

    def test0846(self):
        self.assertEquals(self.calculate(-111922.0, 741), -82934202.00)

    def test0847(self):
        self.assertEquals(self.calculate(-159063.0, 26707), -4248095541.00)

    def test0848(self):
        self.assertEquals(self.calculate(181352.0, -15162), -2749659024.00)

    def test0849(self):
        self.assertEquals(self.calculate(91446.0, -13820), -1263783720.00)

    def test0850(self):
        self.assertEquals(self.calculate(-187952.0, -17632), 3313969664.00)

    def test0851(self):
        self.assertEquals(self.calculate(56742.0, -18025), -1022774550.00)

    def test0852(self):
        self.assertEquals(self.calculate(-197575.0, 7102), -1403177650.00)

    def test0853(self):
        self.assertEquals(self.calculate(12787.0, 9024), 115389888.00)

    def test0854(self):
        self.assertEquals(self.calculate(120878.0, 12680), 1532733040.00)

    def test0855(self):
        self.assertEquals(self.calculate(142736.0, -1543), -220241648.00)

    def test0856(self):
        self.assertEquals(self.calculate(171355.0, -17447), -2989630685.00)

    def test0857(self):
        self.assertEquals(self.calculate(-97135.0, -12411), 1205542485.00)

    def test0858(self):
        self.assertEquals(self.calculate(-192918.0, -17586), 3392655948.00)

    def test0859(self):
        self.assertEquals(self.calculate(139111.0, 14197), 1974958867.00)

    def test0860(self):
        self.assertEquals(self.calculate(-145389.0, 23703), -3446155467.00)

    def test0861(self):
        self.assertEquals(self.calculate(114403.0, -7522), -860539366.00)

    def test0862(self):
        self.assertEquals(self.calculate(66511.0, -1384), -92051224.00)

    def test0863(self):
        self.assertEquals(self.calculate(-180833.0, -15125), 2735099125.00)

    def test0864(self):
        self.assertEquals(self.calculate(175298.0, 29371), 5148677558.00)

    def test0865(self):
        self.assertEquals(self.calculate(-11836.0, -15099), 178711764.00)

    def test0866(self):
        self.assertEquals(self.calculate(31053.0, -3331), -103437543.00)

    def test0867(self):
        self.assertEquals(self.calculate(26183.0, -24618), -644573094.00)

    def test0868(self):
        self.assertEquals(self.calculate(-181411.0, 6946), -1260080806.00)

    def test0869(self):
        self.assertEquals(self.calculate(197974.0, 12550), 2484573700.00)

    def test0870(self):
        self.assertEquals(self.calculate(-144559.0, 23149), -3346396291.00)

    def test0871(self):
        self.assertEquals(self.calculate(45919.0, 28197), 1294778043.00)

    def test0872(self):
        self.assertEquals(self.calculate(8169.0, -18), -147042.00)

    def test0873(self):
        self.assertEquals(self.calculate(-51292.0, 1335), -68474820.00)

    def test0874(self):
        self.assertEquals(self.calculate(-88090.0, -15018), 1322935620.00)

    def test0875(self):
        self.assertEquals(self.calculate(-29772.0, 30165), -898072380.00)

    def test0876(self):
        self.assertEquals(self.calculate(-106218.0, 985), -104624730.00)

    def test0877(self):
        self.assertEquals(self.calculate(-168210.0, -30972), 5209800120.00)

    def test0878(self):
        self.assertEquals(self.calculate(-77333.0, -3184), 246228272.00)

    def test0879(self):
        self.assertEquals(self.calculate(-186300.0, -24988), 4655264400.00)

    def test0880(self):
        self.assertEquals(self.calculate(-108930.0, -15946), 1736997780.00)

    def test0881(self):
        self.assertEquals(self.calculate(-53083.0, 21637), -1148556871.00)

    def test0882(self):
        self.assertEquals(self.calculate(-147108.0, -26484), 3896008272.00)

    def test0883(self):
        self.assertEquals(self.calculate(-67008.0, -4042), 270846336.00)

    def test0884(self):
        self.assertEquals(self.calculate(-185581.0, -8700), 1614554700.00)

    def test0885(self):
        self.assertEquals(self.calculate(-98103.0, -12709), 1246791027.00)

    def test0886(self):
        self.assertEquals(self.calculate(-72134.0, -946), 68238764.00)

    def test0887(self):
        self.assertEquals(self.calculate(-75192.0, 26453), -1989053976.00)

    def test0888(self):
        self.assertEquals(self.calculate(105696.0, -25351), -2679499296.00)

    def test0889(self):
        self.assertEquals(self.calculate(160406.0, -23622), -3789110532.00)

    def test0890(self):
        self.assertEquals(self.calculate(66139.0, 11054), 731100506.00)

    def test0891(self):
        self.assertEquals(self.calculate(-119510.0, 10694), -1278039940.00)

    def test0892(self):
        self.assertEquals(self.calculate(128345.0, -9800), -1257781000.00)

    def test0893(self):
        self.assertEquals(self.calculate(-26292.0, -10232), 269019744.00)

    def test0894(self):
        self.assertEquals(self.calculate(-2212.0, -2806), 6206872.00)

    def test0895(self):
        self.assertEquals(self.calculate(-139110.0, -1253), 174304830.00)

    def test0896(self):
        self.assertEquals(self.calculate(72907.0, -26809), -1954563763.00)

    def test0897(self):
        self.assertEquals(self.calculate(15790.0, 7594), 119909260.00)

    def test0898(self):
        self.assertEquals(self.calculate(49936.0, 29599), 1478055664.00)

    def test0899(self):
        self.assertEquals(self.calculate(171612.0, 1314), 225498168.00)

    def test0900(self):
        self.assertEquals(self.calculate(172523.0, -10096), -1741792208.00)

    def test0901(self):
        self.assertEquals(self.calculate(82693.0, 22171), 1833386503.00)

    def test0902(self):
        self.assertEquals(self.calculate(179780.0, -21762), -3912372360.00)

    def test0903(self):
        self.assertEquals(self.calculate(-22458.0, -31141), 699364578.00)

    def test0904(self):
        self.assertEquals(self.calculate(81889.0, 26169), 2142953241.00)

    def test0905(self):
        self.assertEquals(self.calculate(-72043.0, -16533), 1191086919.00)

    def test0906(self):
        self.assertEquals(self.calculate(-169595.0, -29344), 4976595680.00)

    def test0907(self):
        self.assertEquals(self.calculate(-88990.0, 2019), -179670810.00)

    def test0908(self):
        self.assertEquals(self.calculate(107691.0, 1777), 191366907.00)

    def test0909(self):
        self.assertEquals(self.calculate(198381.0, -3527), -699689787.00)

    def test0910(self):
        self.assertEquals(self.calculate(-192044.0, -287), 55116628.00)

    def test0911(self):
        self.assertEquals(self.calculate(-155869.0, -12704), 1980159776.00)

    def test0912(self):
        self.assertEquals(self.calculate(143909.0, 32009), 4606383181.00)

    def test0913(self):
        self.assertEquals(self.calculate(-153717.0, -30188), 4640408796.00)

    def test0914(self):
        self.assertEquals(self.calculate(34199.0, 16823), 575329777.00)

    def test0915(self):
        self.assertEquals(self.calculate(-28159.0, -28369), 798842671.00)

    def test0916(self):
        self.assertEquals(self.calculate(88104.0, -23588), -2078197152.00)

    def test0917(self):
        self.assertEquals(self.calculate(-146106.0, 26026), -3802554756.00)

    def test0918(self):
        self.assertEquals(self.calculate(106421.0, -8993), -957044053.00)

    def test0919(self):
        self.assertEquals(self.calculate(-188155.0, -19753), 3716625715.00)

    def test0920(self):
        self.assertEquals(self.calculate(100683.0, 16526), 1663887258.00)

    def test0921(self):
        self.assertEquals(self.calculate(-139843.0, -11206), 1567080658.00)

    def test0922(self):
        self.assertEquals(self.calculate(154066.0, -13887), -2139514542.00)

    def test0923(self):
        self.assertEquals(self.calculate(27444.0, 25009), 686346996.00)

    def test0924(self):
        self.assertEquals(self.calculate(-194067.0, -25152), 4881173184.00)

    def test0925(self):
        self.assertEquals(self.calculate(-62056.0, -21956), 1362501536.00)

    def test0926(self):
        self.assertEquals(self.calculate(-36198.0, -24954), 903284892.00)

    def test0927(self):
        self.assertEquals(self.calculate(81636.0, -26777), -2185967172.00)

    def test0928(self):
        self.assertEquals(self.calculate(-45018.0, -27502), 1238085036.00)

    def test0929(self):
        self.assertEquals(self.calculate(64541.0, 2382), 153736662.00)

    def test0930(self):
        self.assertEquals(self.calculate(77636.0, -28411), -2205716396.00)

    def test0931(self):
        self.assertEquals(self.calculate(52046.0, -8212), -427401752.00)

    def test0932(self):
        self.assertEquals(self.calculate(-85759.0, -30548), 2619765932.00)

    def test0933(self):
        self.assertEquals(self.calculate(-101310.0, -21159), 2143618290.00)

    def test0934(self):
        self.assertEquals(self.calculate(-3080.0, 23166), -71351280.00)

    def test0935(self):
        self.assertEquals(self.calculate(31191.0, 1569), 48938679.00)

    def test0936(self):
        self.assertEquals(self.calculate(-50994.0, 11614), -592244316.00)

    def test0937(self):
        self.assertEquals(self.calculate(-174473.0, 6894), -1202816862.00)

    def test0938(self):
        self.assertEquals(self.calculate(22228.0, -26794), -595577032.00)

    def test0939(self):
        self.assertEquals(self.calculate(170350.0, 16459), 2803790650.00)

    def test0940(self):
        self.assertEquals(self.calculate(-195751.0, 31410), -6148538910.00)

    def test0941(self):
        self.assertEquals(self.calculate(116265.0, 24923), 2897672595.00)

    def test0942(self):
        self.assertEquals(self.calculate(-10658.0, -28943), 308474494.00)

    def test0943(self):
        self.assertEquals(self.calculate(189447.0, -11402), -2160074694.00)

    def test0944(self):
        self.assertEquals(self.calculate(-59994.0, 16298), -977782212.00)

    def test0945(self):
        self.assertEquals(self.calculate(52482.0, -4432), -232600224.00)

    def test0946(self):
        self.assertEquals(self.calculate(-108962.0, 20621), -2246905402.00)

    def test0947(self):
        self.assertEquals(self.calculate(117074.0, -6145), -719419730.00)

    def test0948(self):
        self.assertEquals(self.calculate(-63292.0, 32098), -2031546616.00)

    def test0949(self):
        self.assertEquals(self.calculate(196778.0, -8352), -1643489856.00)

    def test0950(self):
        self.assertEquals(self.calculate(-192257.0, 1188), -228401316.00)

    def test0951(self):
        self.assertEquals(self.calculate(23314.0, -18860), -439702040.00)

    def test0952(self):
        self.assertEquals(self.calculate(-19169.0, -11748), 225197412.00)

    def test0953(self):
        self.assertEquals(self.calculate(47087.0, 30050), 1414964350.00)

    def test0954(self):
        self.assertEquals(self.calculate(80739.0, 25032), 2021058648.00)

    def test0955(self):
        self.assertEquals(self.calculate(-109445.0, -165), 18058425.00)

    def test0956(self):
        self.assertEquals(self.calculate(-72117.0, 17244), -1243585548.00)

    def test0957(self):
        self.assertEquals(self.calculate(-186235.0, 549), -102243015.00)

    def test0958(self):
        self.assertEquals(self.calculate(-9498.0, -6760), 64206480.00)

    def test0959(self):
        self.assertEquals(self.calculate(127000.0, 18269), 2320163000.00)

    def test0960(self):
        self.assertEquals(self.calculate(-144582.0, 24850), -3592862700.00)

    def test0961(self):
        self.assertEquals(self.calculate(-199265.0, -29726), 5923351390.00)

    def test0962(self):
        self.assertEquals(self.calculate(57699.0, 26283), 1516502817.00)

    def test0963(self):
        self.assertEquals(self.calculate(79591.0, 560), 44570960.00)

    def test0964(self):
        self.assertEquals(self.calculate(-33023.0, 23666), -781522318.00)

    def test0965(self):
        self.assertEquals(self.calculate(151059.0, 24448), 3693090432.00)

    def test0966(self):
        self.assertEquals(self.calculate(-18623.0, 29403), -547572069.00)

    def test0967(self):
        self.assertEquals(self.calculate(-26809.0, 20833), -558511897.00)

    def test0968(self):
        self.assertEquals(self.calculate(65877.0, -1812), -119369124.00)

    def test0969(self):
        self.assertEquals(self.calculate(16832.0, -22149), -372811968.00)

    def test0970(self):
        self.assertEquals(self.calculate(-31106.0, -8288), 257806528.00)

    def test0971(self):
        self.assertEquals(self.calculate(-142776.0, 13419), -1915911144.00)

    def test0972(self):
        self.assertEquals(self.calculate(-139743.0, -28913), 4040389359.00)

    def test0973(self):
        self.assertEquals(self.calculate(21744.0, -17847), -388065168.00)

    def test0974(self):
        self.assertEquals(self.calculate(-169416.0, 3151), -533829816.00)

    def test0975(self):
        self.assertEquals(self.calculate(72756.0, -22773), -1656872388.00)

    def test0976(self):
        self.assertEquals(self.calculate(-70358.0, 31557), -2220287406.00)

    def test0977(self):
        self.assertEquals(self.calculate(187408.0, -3928), -736138624.00)

    def test0978(self):
        self.assertEquals(self.calculate(26477.0, 11826), 313117002.00)

    def test0979(self):
        self.assertEquals(self.calculate(-94547.0, -17548), 1659110756.00)

    def test0980(self):
        self.assertEquals(self.calculate(132549.0, -18932), -2509417668.00)

    def test0981(self):
        self.assertEquals(self.calculate(179418.0, -19087), -3424551366.00)

    def test0982(self):
        self.assertEquals(self.calculate(139942.0, -28151), -3939507242.00)

    def test0983(self):
        self.assertEquals(self.calculate(121004.0, -8153), -986545612.00)

    def test0984(self):
        self.assertEquals(self.calculate(-111848.0, -15257), 1706464936.00)

    def test0985(self):
        self.assertEquals(self.calculate(137135.0, -21769), -2985291815.00)

    def test0986(self):
        self.assertEquals(self.calculate(-193577.0, 15936), -3084843072.00)

    def test0987(self):
        self.assertEquals(self.calculate(-98798.0, 14954), -1477425292.00)

    def test0988(self):
        self.assertEquals(self.calculate(14327.0, -5374), -76993298.00)

    def test0989(self):
        self.assertEquals(self.calculate(79704.0, -10397), -828682488.00)

    def test0990(self):
        self.assertEquals(self.calculate(99074.0, 11304), 1119932496.00)

    def test0991(self):
        self.assertEquals(self.calculate(143112.0, 12033), 1722066696.00)

    def test0992(self):
        self.assertEquals(self.calculate(180484.0, 6866), 1239203144.00)

    def test0993(self):
        self.assertEquals(self.calculate(-6152.0, -3793), 23334536.00)

    def test0994(self):
        self.assertEquals(self.calculate(-22793.0, -10239), 233377527.00)

    def test0995(self):
        self.assertEquals(self.calculate(11431.0, 12863), 147036953.00)

    def test0996(self):
        self.assertEquals(self.calculate(-42785.0, 868), -37137380.00)

    def test0997(self):
        self.assertEquals(self.calculate(129725.0, 252), 32690700.00)

    def test0998(self):
        self.assertEquals(self.calculate(-160120.0, 11441), -1831932920.00)

    def test0999(self):
        self.assertEquals(self.calculate(10874.0, -13947), -151659678.00)

    def test1000(self):
        self.assertEquals(self.calculate(-183619.0, -7604), 1396238876.00)

    def test1001(self):
        self.assertEquals(self.calculate(-161044.0, -18264), 2941307616.00)

    def test1002(self):
        self.assertEquals(self.calculate(-194103.0, 2870), -557075610.00)

    def test1003(self):
        self.assertEquals(self.calculate(133443.0, 13083), 1745834769.00)

    def test1004(self):
        self.assertEquals(self.calculate(-104338.0, -6522), 680492436.00)

    def test1005(self):
        self.assertEquals(self.calculate(129822.0, 2800), 363501600.00)

    def test1006(self):
        self.assertEquals(self.calculate(36057.0, 11629), 419306853.00)

    def test1007(self):
        self.assertEquals(self.calculate(11881.0, 24623), 292545863.00)

    def test1008(self):
        self.assertEquals(self.calculate(-181839.0, -17514), 3184728246.00)

    def test1009(self):
        self.assertEquals(self.calculate(143732.0, -17798), -2558142136.00)

    def test1010(self):
        self.assertEquals(self.calculate(-77181.0, 23292), -1797699852.00)

    def test1011(self):
        self.assertEquals(self.calculate(156608.0, 10417), 1631385536.00)

    def test1012(self):
        self.assertEquals(self.calculate(71775.0, 13685), 982240875.00)

    def test1013(self):
        self.assertEquals(self.calculate(-164276.0, 29901), -4912016676.00)

    def test1014(self):
        self.assertEquals(self.calculate(-57201.0, -7232), 413677632.00)

    def test1015(self):
        self.assertEquals(self.calculate(-116961.0, 20090), -2349746490.00)

    def test1016(self):
        self.assertEquals(self.calculate(172494.0, 8807), 1519154658.00)

    def test1017(self):
        self.assertEquals(self.calculate(56357.0, 20525), 1156727425.00)

    def test1018(self):
        self.assertEquals(self.calculate(31040.0, -9490), -294569600.00)

    def test1019(self):
        self.assertEquals(self.calculate(-81744.0, 9244), -755641536.00)

    def test1020(self):
        self.assertEquals(self.calculate(74727.0, -20296), -1516659192.00)

    def test1021(self):
        self.assertEquals(self.calculate(6072.0, 5971), 36255912.00)

    def test1022(self):
        self.assertEquals(self.calculate(78001.0, -29578), -2307113578.00)

    def test1023(self):
        self.assertEquals(self.calculate(15403.0, 27710), 426817130.00)



class TestVM_Mul_FloatLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushL(rhs)
        v.VM_Mul()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(110760.0, 902809219), 99995149096440.00)

    def test0001(self):
        self.assertEquals(self.calculate(108952.0, 147887665), 16112656877080.00)

    def test0002(self):
        self.assertEquals(self.calculate(-43060.0, 1097325635), -47250841843100.00)

    def test0003(self):
        self.assertEquals(self.calculate(-120114.0, -1371833755), 164776439648070.00)

    def test0004(self):
        self.assertEquals(self.calculate(180778.0, -392709889), -70993308313642.00)

    def test0005(self):
        self.assertEquals(self.calculate(134105.0, -1955965436), -262304744794780.00)

    def test0006(self):
        self.assertEquals(self.calculate(10276.0, 301679898), 3100062631848.00)

    def test0007(self):
        self.assertEquals(self.calculate(156958.0, 658990995), 103433908593210.00)

    def test0008(self):
        self.assertEquals(self.calculate(-51005.0, -1243774372), 63438711843860.00)

    def test0009(self):
        self.assertEquals(self.calculate(-10316.0, 1930662948), -19916718971568.00)

    def test0010(self):
        self.assertEquals(self.calculate(53376.0, 1995985462), 106537720019712.00)

    def test0011(self):
        self.assertEquals(self.calculate(-23172.0, 1188259403), -27534346886316.00)

    def test0012(self):
        self.assertEquals(self.calculate(-134771.0, -211969338), 28567319651598.00)

    def test0013(self):
        self.assertEquals(self.calculate(79086.0, 918692602), 72655723121772.00)

    def test0014(self):
        self.assertEquals(self.calculate(188129.0, 884033927), 166312418652583.00)

    def test0015(self):
        self.assertEquals(self.calculate(-101358.0, 1651752628), -167418342868824.00)

    def test0016(self):
        self.assertEquals(self.calculate(76697.0, -1763954400), -135290010616800.00)

    def test0017(self):
        self.assertEquals(self.calculate(-18841.0, 111666293), -2103904626413.00)

    def test0018(self):
        self.assertEquals(self.calculate(45680.0, -48281279), -2205488824720.00)

    def test0019(self):
        self.assertEquals(self.calculate(113826.0, 1602178764), 182369599991064.00)

    def test0020(self):
        self.assertEquals(self.calculate(-162761.0, 171807712), -27963595012832.00)

    def test0021(self):
        self.assertEquals(self.calculate(28022.0, 1300401995), 36439864703890.00)

    def test0022(self):
        self.assertEquals(self.calculate(-112294.0, 1456250802), -163528227559788.00)

    def test0023(self):
        self.assertEquals(self.calculate(-138857.0, -1602397158), 222504062168406.00)

    def test0024(self):
        self.assertEquals(self.calculate(126903.0, 564809546), 71676025816038.00)

    def test0025(self):
        self.assertEquals(self.calculate(-54325.0, -329975246), 17925905238950.00)

    def test0026(self):
        self.assertEquals(self.calculate(85145.0, 152544615), 12988411244175.00)

    def test0027(self):
        self.assertEquals(self.calculate(157978.0, 604751418), 95537419512804.00)

    def test0028(self):
        self.assertEquals(self.calculate(-96963.0, 1619571455), -157038506991165.00)

    def test0029(self):
        self.assertEquals(self.calculate(145255.0, -1973221315), -286620262110325.00)

    def test0030(self):
        self.assertEquals(self.calculate(-193717.0, -1655514699), 320701340946183.00)

    def test0031(self):
        self.assertEquals(self.calculate(117985.0, 1239507701), 146243316102485.00)

    def test0032(self):
        self.assertEquals(self.calculate(192485.0, 776086706), 149385049604410.00)

    def test0033(self):
        self.assertEquals(self.calculate(-78676.0, 406651230), -31993692171480.00)

    def test0034(self):
        self.assertEquals(self.calculate(42395.0, -428202138), -18153629640510.00)

    def test0035(self):
        self.assertEquals(self.calculate(157356.0, -583015841), -91741040676396.00)

    def test0036(self):
        self.assertEquals(self.calculate(-42675.0, 1632093268), -69649580211900.00)

    def test0037(self):
        self.assertEquals(self.calculate(-1161.0, 1920570985), -2229782913585.00)

    def test0038(self):
        self.assertEquals(self.calculate(43328.0, 1234783298), 53500690735744.00)

    def test0039(self):
        self.assertEquals(self.calculate(143986.0, 242736180), 34950611613480.00)

    def test0040(self):
        self.assertEquals(self.calculate(112016.0, -1911571433), -214126585638928.00)

    def test0041(self):
        self.assertEquals(self.calculate(198353.0, -1399206945), -277536895161585.00)

    def test0042(self):
        self.assertEquals(self.calculate(-186902.0, -1151515553), 215220559886806.00)

    def test0043(self):
        self.assertEquals(self.calculate(133282.0, 695332613), 92675321325866.00)

    def test0044(self):
        self.assertEquals(self.calculate(-31207.0, 1393700148), -43493200518636.00)

    def test0045(self):
        self.assertEquals(self.calculate(39307.0, -186180311), -7318189484477.00)

    def test0046(self):
        self.assertEquals(self.calculate(-168141.0, -735867486), 123729494963526.00)

    def test0047(self):
        self.assertEquals(self.calculate(-130495.0, -1312198693), 171235368443035.00)

    def test0048(self):
        self.assertEquals(self.calculate(-20349.0, 782874356), -15930710270244.00)

    def test0049(self):
        self.assertEquals(self.calculate(177082.0, 1086003650), 192311698349300.00)

    def test0050(self):
        self.assertEquals(self.calculate(-90564.0, 1649682568), -149401852088352.00)

    def test0051(self):
        self.assertEquals(self.calculate(-15473.0, -1195038339), 18490828219347.00)

    def test0052(self):
        self.assertEquals(self.calculate(69444.0, 285420692), 19820754535248.00)

    def test0053(self):
        self.assertEquals(self.calculate(37301.0, -2121846184), -79146984509384.00)

    def test0054(self):
        self.assertEquals(self.calculate(-30768.0, 1811314942), -55730538135456.00)

    def test0055(self):
        self.assertEquals(self.calculate(-149362.0, 1438047926), -214789714323212.00)

    def test0056(self):
        self.assertEquals(self.calculate(-150498.0, -1759298669), 264770931087162.00)

    def test0057(self):
        self.assertEquals(self.calculate(185461.0, 894886657), 165966574293877.00)

    def test0058(self):
        self.assertEquals(self.calculate(157155.0, 1548700154), 243385972701870.00)

    def test0059(self):
        self.assertEquals(self.calculate(-116268.0, -133624142), 15536211742056.00)

    def test0060(self):
        self.assertEquals(self.calculate(199358.0, 1298782014), 258922584747012.00)

    def test0061(self):
        self.assertEquals(self.calculate(121083.0, -850664576), -103001018855808.00)

    def test0062(self):
        self.assertEquals(self.calculate(3766.0, -924914329), -3483227363014.00)

    def test0063(self):
        self.assertEquals(self.calculate(194804.0, -843703193), -164356756809172.00)

    def test0064(self):
        self.assertEquals(self.calculate(36528.0, -1735923865), -63409826940720.00)

    def test0065(self):
        self.assertEquals(self.calculate(23185.0, -1835839752), -42563944650120.00)

    def test0066(self):
        self.assertEquals(self.calculate(-29401.0, -42767942), 1257420262742.00)

    def test0067(self):
        self.assertEquals(self.calculate(-52485.0, -263167368), 13812339309480.00)

    def test0068(self):
        self.assertEquals(self.calculate(-138874.0, -75054737), 10423151546138.00)

    def test0069(self):
        self.assertEquals(self.calculate(99695.0, -819312503), -81681359986585.00)

    def test0070(self):
        self.assertEquals(self.calculate(152641.0, -982574379), -149981135784939.00)

    def test0071(self):
        self.assertEquals(self.calculate(-167372.0, 2117508637), -354411655591964.00)

    def test0072(self):
        self.assertEquals(self.calculate(-198484.0, 765219393), -151883806000212.00)

    def test0073(self):
        self.assertEquals(self.calculate(-57225.0, -619847997), 35470801628325.00)

    def test0074(self):
        self.assertEquals(self.calculate(141134.0, 1526503189), 215441501076326.00)

    def test0075(self):
        self.assertEquals(self.calculate(10935.0, 17724642), 193818960270.00)

    def test0076(self):
        self.assertEquals(self.calculate(-132626.0, -860276090), 114094976712340.00)

    def test0077(self):
        self.assertEquals(self.calculate(-129085.0, -349502765), 45115564420025.00)

    def test0078(self):
        self.assertEquals(self.calculate(71137.0, 1266753273), 90113027581401.00)

    def test0079(self):
        self.assertEquals(self.calculate(99003.0, -1416984108), -140285677644324.00)

    def test0080(self):
        self.assertEquals(self.calculate(199484.0, 1012891806), 202055709028104.00)

    def test0081(self):
        self.assertEquals(self.calculate(-119193.0, 908467397), -108282954450621.00)

    def test0082(self):
        self.assertEquals(self.calculate(-83121.0, -1517305172), 126119923201812.00)

    def test0083(self):
        self.assertEquals(self.calculate(74250.0, -1141204295), -84734418903750.00)

    def test0084(self):
        self.assertEquals(self.calculate(99783.0, 1583579107), 158014274033781.00)

    def test0085(self):
        self.assertEquals(self.calculate(-89937.0, -2095141183), 188430712575471.00)

    def test0086(self):
        self.assertEquals(self.calculate(-31156.0, -998165094), 31098831668664.00)

    def test0087(self):
        self.assertEquals(self.calculate(-139494.0, -416304063), 58071918964122.00)

    def test0088(self):
        self.assertEquals(self.calculate(106534.0, -1296700638), -138142705768692.00)

    def test0089(self):
        self.assertEquals(self.calculate(107487.0, 1079318162), 116012671278894.00)

    def test0090(self):
        self.assertEquals(self.calculate(-90085.0, -389228306), 35063631946010.00)

    def test0091(self):
        self.assertEquals(self.calculate(-28602.0, -373664757), 10687559379714.00)

    def test0092(self):
        self.assertEquals(self.calculate(42865.0, 123987712), 5314733274880.00)

    def test0093(self):
        self.assertEquals(self.calculate(28830.0, -745176470), -21483437630100.00)

    def test0094(self):
        self.assertEquals(self.calculate(-156871.0, -1779932622), 279219810345762.00)

    def test0095(self):
        self.assertEquals(self.calculate(22278.0, 151833791), 3382553195898.00)

    def test0096(self):
        self.assertEquals(self.calculate(-126851.0, 1832696111), -232479334376461.00)

    def test0097(self):
        self.assertEquals(self.calculate(4386.0, -41530306), -182151922116.00)

    def test0098(self):
        self.assertEquals(self.calculate(5053.0, -1076814767), -5441145017651.00)

    def test0099(self):
        self.assertEquals(self.calculate(19309.0, 1520680190), 29362813788710.00)

    def test0100(self):
        self.assertEquals(self.calculate(50248.0, -727954547), -36578260077656.00)

    def test0101(self):
        self.assertEquals(self.calculate(27014.0, -1205554421), -32566847128894.00)

    def test0102(self):
        self.assertEquals(self.calculate(-16688.0, -465987355), 7776396980240.00)

    def test0103(self):
        self.assertEquals(self.calculate(106600.0, 27183578), 2897769414800.00)

    def test0104(self):
        self.assertEquals(self.calculate(-114761.0, -1263809744), 145036070031184.00)

    def test0105(self):
        self.assertEquals(self.calculate(59217.0, 1820108160), 107781344910720.00)

    def test0106(self):
        self.assertEquals(self.calculate(75030.0, -1636714862), -122802716095860.00)

    def test0107(self):
        self.assertEquals(self.calculate(187886.0, 882127917), 165739485813462.00)

    def test0108(self):
        self.assertEquals(self.calculate(-124515.0, 2115354914), -263393417116710.00)

    def test0109(self):
        self.assertEquals(self.calculate(133836.0, -1213242523), -162375526308228.00)

    def test0110(self):
        self.assertEquals(self.calculate(92834.0, -581797629), -54010601090586.00)

    def test0111(self):
        self.assertEquals(self.calculate(169391.0, -494974570), -83844237386870.00)

    def test0112(self):
        self.assertEquals(self.calculate(-65572.0, 1184997706), -77702669577832.00)

    def test0113(self):
        self.assertEquals(self.calculate(-85290.0, -1278836963), 109072004574270.00)

    def test0114(self):
        self.assertEquals(self.calculate(-133295.0, 1314223208), -175179382510360.00)

    def test0115(self):
        self.assertEquals(self.calculate(110725.0, -919433832), -101804311048200.00)

    def test0116(self):
        self.assertEquals(self.calculate(-92698.0, -228711721), 21201119113258.00)

    def test0117(self):
        self.assertEquals(self.calculate(-87252.0, -2033015990), 177384711159480.00)

    def test0118(self):
        self.assertEquals(self.calculate(169637.0, 150367635), 25507914498495.00)

    def test0119(self):
        self.assertEquals(self.calculate(-107456.0, -1631152608), 175277134645248.00)

    def test0120(self):
        self.assertEquals(self.calculate(-148129.0, 1792486688), -265519260606752.00)

    def test0121(self):
        self.assertEquals(self.calculate(-29246.0, -626178385), 18313213047710.00)

    def test0122(self):
        self.assertEquals(self.calculate(160293.0, 1516690835), 243114924014655.00)

    def test0123(self):
        self.assertEquals(self.calculate(74482.0, 393761939), 29328176740598.00)

    def test0124(self):
        self.assertEquals(self.calculate(-79387.0, 336303908), -26698158344396.00)

    def test0125(self):
        self.assertEquals(self.calculate(43790.0, -613183093), -26851287642470.00)

    def test0126(self):
        self.assertEquals(self.calculate(131424.0, -1781749781), -234164683218144.00)

    def test0127(self):
        self.assertEquals(self.calculate(-63065.0, 1190707619), -75091975992235.00)

    def test0128(self):
        self.assertEquals(self.calculate(105615.0, -1525386549), -161103700372635.00)

    def test0129(self):
        self.assertEquals(self.calculate(167003.0, 1227277641), 204959047879923.00)

    def test0130(self):
        self.assertEquals(self.calculate(134591.0, 9880905), 1329880884855.00)

    def test0131(self):
        self.assertEquals(self.calculate(-129122.0, 1005992077), -129895708966394.00)

    def test0132(self):
        self.assertEquals(self.calculate(187952.0, -1439245252), -270509023603904.00)

    def test0133(self):
        self.assertEquals(self.calculate(44371.0, -1072858671), -47603812090941.00)

    def test0134(self):
        self.assertEquals(self.calculate(-151236.0, -494271069), 74751579391284.00)

    def test0135(self):
        self.assertEquals(self.calculate(-154508.0, 1246978092), -192668091038736.00)

    def test0136(self):
        self.assertEquals(self.calculate(-150246.0, 1116805710), -167795590704660.00)

    def test0137(self):
        self.assertEquals(self.calculate(126898.0, -434949713), -55194248680274.00)

    def test0138(self):
        self.assertEquals(self.calculate(97290.0, -799140916), -77748419717640.00)

    def test0139(self):
        self.assertEquals(self.calculate(57975.0, -873555528), -50644381735800.00)

    def test0140(self):
        self.assertEquals(self.calculate(-78546.0, -922169566), 72432730731036.00)

    def test0141(self):
        self.assertEquals(self.calculate(132730.0, -1498020989), -198832325869970.00)

    def test0142(self):
        self.assertEquals(self.calculate(-142264.0, -2140915050), 304575138673200.00)

    def test0143(self):
        self.assertEquals(self.calculate(146261.0, 1837155331), 268704175867391.00)

    def test0144(self):
        self.assertEquals(self.calculate(73074.0, -921863769), -67364273055906.00)

    def test0145(self):
        self.assertEquals(self.calculate(83578.0, -927454820), -77514818945960.00)

    def test0146(self):
        self.assertEquals(self.calculate(181681.0, -231141678), -41994051200718.00)

    def test0147(self):
        self.assertEquals(self.calculate(-55855.0, -551773007), 30819281305985.00)

    def test0148(self):
        self.assertEquals(self.calculate(162023.0, 147006250), 23818393643750.00)

    def test0149(self):
        self.assertEquals(self.calculate(16417.0, -325893758), -5350197825086.00)

    def test0150(self):
        self.assertEquals(self.calculate(-67021.0, -1260673122), 84491573309562.00)

    def test0151(self):
        self.assertEquals(self.calculate(148500.0, 1717148122), 254996496117000.00)

    def test0152(self):
        self.assertEquals(self.calculate(579.0, -1813091003), -1049779690737.00)

    def test0153(self):
        self.assertEquals(self.calculate(126565.0, -626621406), -79308338250390.00)

    def test0154(self):
        self.assertEquals(self.calculate(197187.0, -1817724497), -358431640389939.00)

    def test0155(self):
        self.assertEquals(self.calculate(-127778.0, -1462798597), 186913479127466.00)

    def test0156(self):
        self.assertEquals(self.calculate(92916.0, 637405990), 59225214966840.00)

    def test0157(self):
        self.assertEquals(self.calculate(-35062.0, 801024243), -28085512008066.00)

    def test0158(self):
        self.assertEquals(self.calculate(188114.0, -276528706), -52018921000484.00)

    def test0159(self):
        self.assertEquals(self.calculate(546.0, 993968578), 542706843588.00)

    def test0160(self):
        self.assertEquals(self.calculate(46117.0, -163100572), -7521709078924.00)

    def test0161(self):
        self.assertEquals(self.calculate(47981.0, -1637394813), -78563840522553.00)

    def test0162(self):
        self.assertEquals(self.calculate(-158184.0, -238217367), 37682175981528.00)

    def test0163(self):
        self.assertEquals(self.calculate(-36008.0, -1845721539), 66460741176312.00)

    def test0164(self):
        self.assertEquals(self.calculate(107129.0, -2026052015), -217048926314935.00)

    def test0165(self):
        self.assertEquals(self.calculate(-33905.0, 398981097), -13527454093785.00)

    def test0166(self):
        self.assertEquals(self.calculate(126482.0, 982119590), 124220449982380.00)

    def test0167(self):
        self.assertEquals(self.calculate(-28559.0, -1093511436), 31229593100724.00)

    def test0168(self):
        self.assertEquals(self.calculate(-126394.0, -1474392482), 186354363369908.00)

    def test0169(self):
        self.assertEquals(self.calculate(148861.0, -1709577355), -254489394642655.00)

    def test0170(self):
        self.assertEquals(self.calculate(124359.0, 871469454), 108375069829986.00)

    def test0171(self):
        self.assertEquals(self.calculate(8654.0, -2022120149), -17499427769446.00)

    def test0172(self):
        self.assertEquals(self.calculate(-159127.0, 1334717772), -212389634905044.00)

    def test0173(self):
        self.assertEquals(self.calculate(124677.0, 1724714016), 215032169372832.00)

    def test0174(self):
        self.assertEquals(self.calculate(-186606.0, 230007912), -42920856426672.00)

    def test0175(self):
        self.assertEquals(self.calculate(185238.0, -600508871), -111237062246298.00)

    def test0176(self):
        self.assertEquals(self.calculate(-144914.0, 384670585), -55744153154690.00)

    def test0177(self):
        self.assertEquals(self.calculate(72740.0, 1753980374), 127584532404760.00)

    def test0178(self):
        self.assertEquals(self.calculate(58419.0, 2137026347), 124842942165393.00)

    def test0179(self):
        self.assertEquals(self.calculate(46251.0, -1974854262), -91338984471762.00)

    def test0180(self):
        self.assertEquals(self.calculate(-19289.0, 1492982937), -28798147871793.00)

    def test0181(self):
        self.assertEquals(self.calculate(154597.0, -367950009), -56883967541373.00)

    def test0182(self):
        self.assertEquals(self.calculate(-34215.0, 1089411237), -37274205473955.00)

    def test0183(self):
        self.assertEquals(self.calculate(169873.0, 1601176721), 271996693126433.00)

    def test0184(self):
        self.assertEquals(self.calculate(90976.0, 69891590), 6358457291840.00)

    def test0185(self):
        self.assertEquals(self.calculate(129316.0, 643001198), 83150342920568.00)

    def test0186(self):
        self.assertEquals(self.calculate(-102140.0, 1447800257), -147878318249980.00)

    def test0187(self):
        self.assertEquals(self.calculate(-122912.0, 1837480967), -225848460615904.00)

    def test0188(self):
        self.assertEquals(self.calculate(130708.0, 1883338867), 246167456627836.00)

    def test0189(self):
        self.assertEquals(self.calculate(166362.0, 199984519), 33269824549878.00)

    def test0190(self):
        self.assertEquals(self.calculate(74897.0, -299950421), -22465386681637.00)

    def test0191(self):
        self.assertEquals(self.calculate(-18370.0, 808083265), -14844489578050.00)

    def test0192(self):
        self.assertEquals(self.calculate(162160.0, -1952984758), -316696008357280.00)

    def test0193(self):
        self.assertEquals(self.calculate(-82104.0, -196047863), 16096313743752.00)

    def test0194(self):
        self.assertEquals(self.calculate(128012.0, -1313346816), -168124152609792.00)

    def test0195(self):
        self.assertEquals(self.calculate(47621.0, 753347866), 35875178726786.00)

    def test0196(self):
        self.assertEquals(self.calculate(-126574.0, -2096284691), 265335138478634.00)

    def test0197(self):
        self.assertEquals(self.calculate(105050.0, -1576644432), -165626497581600.00)

    def test0198(self):
        self.assertEquals(self.calculate(-109252.0, 911525063), -99585936182876.00)

    def test0199(self):
        self.assertEquals(self.calculate(-125537.0, 661933117), -83097097708829.00)

    def test0200(self):
        self.assertEquals(self.calculate(48656.0, -1947386844), -94752054281664.00)

    def test0201(self):
        self.assertEquals(self.calculate(-63204.0, -562145788), 35529862384752.00)

    def test0202(self):
        self.assertEquals(self.calculate(138374.0, -971230781), -134393088090094.00)

    def test0203(self):
        self.assertEquals(self.calculate(190654.0, 815814313), 155538262030702.00)

    def test0204(self):
        self.assertEquals(self.calculate(-155907.0, 821462741), -128071791561087.00)

    def test0205(self):
        self.assertEquals(self.calculate(62444.0, 87393999), 5457230873556.00)

    def test0206(self):
        self.assertEquals(self.calculate(120237.0, -582780744), -70071808316328.00)

    def test0207(self):
        self.assertEquals(self.calculate(154944.0, -1393205225), -215868790382400.00)

    def test0208(self):
        self.assertEquals(self.calculate(165931.0, -975141357), -161806180508367.00)

    def test0209(self):
        self.assertEquals(self.calculate(-193372.0, 1360033637), -262992424453964.00)

    def test0210(self):
        self.assertEquals(self.calculate(94053.0, 1546755967), 145477038964251.00)

    def test0211(self):
        self.assertEquals(self.calculate(-171471.0, 1261396411), -216292903990581.00)

    def test0212(self):
        self.assertEquals(self.calculate(54782.0, 585684914), 32084990958748.00)

    def test0213(self):
        self.assertEquals(self.calculate(32629.0, 1250656039), 40807655896531.00)

    def test0214(self):
        self.assertEquals(self.calculate(-20142.0, -1563282784), 31487641835328.00)

    def test0215(self):
        self.assertEquals(self.calculate(-70525.0, 223858323), -15787608229575.00)

    def test0216(self):
        self.assertEquals(self.calculate(-161098.0, 845631441), -136229533882218.00)

    def test0217(self):
        self.assertEquals(self.calculate(-120552.0, 932855079), -112457545483608.00)

    def test0218(self):
        self.assertEquals(self.calculate(53552.0, -676209973), -36212396474096.00)

    def test0219(self):
        self.assertEquals(self.calculate(-175618.0, -893872233), 156980053814994.00)

    def test0220(self):
        self.assertEquals(self.calculate(131871.0, 2125103299), 280239497142429.00)

    def test0221(self):
        self.assertEquals(self.calculate(-107683.0, 1626947847), -175194625008501.00)

    def test0222(self):
        self.assertEquals(self.calculate(-69265.0, 912702867), -63218364082755.00)

    def test0223(self):
        self.assertEquals(self.calculate(-188250.0, 1786987170), -336400334752500.00)

    def test0224(self):
        self.assertEquals(self.calculate(-24421.0, 1393677486), -34034997885606.00)

    def test0225(self):
        self.assertEquals(self.calculate(-167056.0, 1896631840), -316843728663040.00)

    def test0226(self):
        self.assertEquals(self.calculate(-39201.0, 549737295), -21550251701295.00)

    def test0227(self):
        self.assertEquals(self.calculate(-93154.0, -439578641), 40948508723714.00)

    def test0228(self):
        self.assertEquals(self.calculate(189344.0, 457237492), 86575175685248.00)

    def test0229(self):
        self.assertEquals(self.calculate(32377.0, -1981624685), -64159062426245.00)

    def test0230(self):
        self.assertEquals(self.calculate(-92427.0, -1131139132), 104547796553364.00)

    def test0231(self):
        self.assertEquals(self.calculate(123087.0, 466746346), 57450407490102.00)

    def test0232(self):
        self.assertEquals(self.calculate(-194014.0, -341505228), 66256795305192.00)

    def test0233(self):
        self.assertEquals(self.calculate(-100797.0, -1526051191), 153821381899227.00)

    def test0234(self):
        self.assertEquals(self.calculate(-18535.0, 525021116), -9731266385060.00)

    def test0235(self):
        self.assertEquals(self.calculate(192759.0, 1928397454), 371715964835586.00)

    def test0236(self):
        self.assertEquals(self.calculate(-178805.0, -1249412707), 223401239075135.00)

    def test0237(self):
        self.assertEquals(self.calculate(140245.0, -659242347), -92455442955015.00)

    def test0238(self):
        self.assertEquals(self.calculate(-140949.0, 1159472735), -163426522525515.00)

    def test0239(self):
        self.assertEquals(self.calculate(180464.0, 1087047621), 196172961876144.00)

    def test0240(self):
        self.assertEquals(self.calculate(85032.0, 30284580), 2575158406560.00)

    def test0241(self):
        self.assertEquals(self.calculate(-83014.0, -1314031879), 109083042403306.00)

    def test0242(self):
        self.assertEquals(self.calculate(-167359.0, 2132730963), -356931721236717.00)

    def test0243(self):
        self.assertEquals(self.calculate(92343.0, 192346398), 17761843430514.00)

    def test0244(self):
        self.assertEquals(self.calculate(-66231.0, -2022707571), 133965945134901.00)

    def test0245(self):
        self.assertEquals(self.calculate(-186565.0, -72284908), 13485833861020.00)

    def test0246(self):
        self.assertEquals(self.calculate(182361.0, 642827693), 117226700923173.00)

    def test0247(self):
        self.assertEquals(self.calculate(81452.0, -815104505), -66391892141260.00)

    def test0248(self):
        self.assertEquals(self.calculate(113177.0, -1204286024), -136297479338248.00)

    def test0249(self):
        self.assertEquals(self.calculate(100074.0, -1947681032), -194912231596368.00)

    def test0250(self):
        self.assertEquals(self.calculate(-25290.0, -921635591), 23308164096390.00)

    def test0251(self):
        self.assertEquals(self.calculate(100510.0, -1934471725), -194433753079750.00)

    def test0252(self):
        self.assertEquals(self.calculate(-159479.0, 1143983065), -182441275223135.00)

    def test0253(self):
        self.assertEquals(self.calculate(-109088.0, 861526615), -93982215377120.00)

    def test0254(self):
        self.assertEquals(self.calculate(153717.0, 463383538), 71229927310746.00)

    def test0255(self):
        self.assertEquals(self.calculate(44151.0, -480213508), -21201906591708.00)

    def test0256(self):
        self.assertEquals(self.calculate(-20378.0, -745677976), 15195425794928.00)

    def test0257(self):
        self.assertEquals(self.calculate(-177372.0, -942962394), 167255125748568.00)

    def test0258(self):
        self.assertEquals(self.calculate(-105649.0, 1561417294), -164962175693806.00)

    def test0259(self):
        self.assertEquals(self.calculate(138144.0, -1442678284), -199297348864896.00)

    def test0260(self):
        self.assertEquals(self.calculate(117249.0, 660349686), 77425340333814.00)

    def test0261(self):
        self.assertEquals(self.calculate(199244.0, -1944058793), -387342050152492.00)

    def test0262(self):
        self.assertEquals(self.calculate(-16291.0, -442147034), 7203017330894.00)

    def test0263(self):
        self.assertEquals(self.calculate(-57770.0, -347478288), 20073820697760.00)

    def test0264(self):
        self.assertEquals(self.calculate(126648.0, -217759976), -27578865440448.00)

    def test0265(self):
        self.assertEquals(self.calculate(-80510.0, 1667062078), -134215167899780.00)

    def test0266(self):
        self.assertEquals(self.calculate(82363.0, -1010204704), -83203490035552.00)

    def test0267(self):
        self.assertEquals(self.calculate(18349.0, -633821284), -11629986740116.00)

    def test0268(self):
        self.assertEquals(self.calculate(39905.0, 1721318564), 68689217296420.00)

    def test0269(self):
        self.assertEquals(self.calculate(174575.0, 300353507), 52434213484525.00)

    def test0270(self):
        self.assertEquals(self.calculate(-147316.0, -391640837), 57694961543492.00)

    def test0271(self):
        self.assertEquals(self.calculate(-19004.0, 609115680), -11575634382720.00)

    def test0272(self):
        self.assertEquals(self.calculate(167791.0, -1856934896), -311576963134736.00)

    def test0273(self):
        self.assertEquals(self.calculate(161106.0, -1638970326), -264047953340556.00)

    def test0274(self):
        self.assertEquals(self.calculate(56590.0, 92981671), 5261832761890.00)

    def test0275(self):
        self.assertEquals(self.calculate(133885.0, -1941848645), -259984405835825.00)

    def test0276(self):
        self.assertEquals(self.calculate(190705.0, 1429523862), 272617348102710.00)

    def test0277(self):
        self.assertEquals(self.calculate(-170708.0, 159174540), -27172367374320.00)

    def test0278(self):
        self.assertEquals(self.calculate(189251.0, -248206371), -46973303918121.00)

    def test0279(self):
        self.assertEquals(self.calculate(15693.0, 1815578631), 28491875456283.00)

    def test0280(self):
        self.assertEquals(self.calculate(-149429.0, 1325554004), -198076209263716.00)

    def test0281(self):
        self.assertEquals(self.calculate(42055.0, -819770724), -34475457797820.00)

    def test0282(self):
        self.assertEquals(self.calculate(71672.0, -1725333059), -123658071004648.00)

    def test0283(self):
        self.assertEquals(self.calculate(-173322.0, 2126836022), -368627473005084.00)

    def test0284(self):
        self.assertEquals(self.calculate(43563.0, -1942872923), -84637373144649.00)

    def test0285(self):
        self.assertEquals(self.calculate(106360.0, 2081167215), 221352944987400.00)

    def test0286(self):
        self.assertEquals(self.calculate(-166740.0, -174275212), 29058648848880.00)

    def test0287(self):
        self.assertEquals(self.calculate(3729.0, -1773566660), -6613630075140.00)

    def test0288(self):
        self.assertEquals(self.calculate(-196729.0, 875167726), -172170871568254.00)

    def test0289(self):
        self.assertEquals(self.calculate(-153280.0, 961897668), -147439674551040.00)

    def test0290(self):
        self.assertEquals(self.calculate(68903.0, -1163056349), -80138071615147.00)

    def test0291(self):
        self.assertEquals(self.calculate(135635.0, 1045061910), 141746972162850.00)

    def test0292(self):
        self.assertEquals(self.calculate(80921.0, -1063008926), -86019745300846.00)

    def test0293(self):
        self.assertEquals(self.calculate(17579.0, -1122883029), -19739160766791.00)

    def test0294(self):
        self.assertEquals(self.calculate(-146491.0, 1354114187), -198365541367817.00)

    def test0295(self):
        self.assertEquals(self.calculate(-4420.0, 1189823877), -5259021536340.00)

    def test0296(self):
        self.assertEquals(self.calculate(70775.0, 929223104), 65765765185600.00)

    def test0297(self):
        self.assertEquals(self.calculate(89259.0, 1211903801), 108173321373459.00)

    def test0298(self):
        self.assertEquals(self.calculate(-188671.0, -1795865232), 338827689186672.00)

    def test0299(self):
        self.assertEquals(self.calculate(195279.0, 82651099), 16140023961621.00)

    def test0300(self):
        self.assertEquals(self.calculate(-193959.0, 16505209), -3201333832431.00)

    def test0301(self):
        self.assertEquals(self.calculate(-9587.0, -1460458346), 14001414163102.00)

    def test0302(self):
        self.assertEquals(self.calculate(109148.0, 659649765), 71999452550220.00)

    def test0303(self):
        self.assertEquals(self.calculate(87547.0, 1980329153), 173371876357691.00)

    def test0304(self):
        self.assertEquals(self.calculate(22503.0, 47160025), 1061242042575.00)

    def test0305(self):
        self.assertEquals(self.calculate(157438.0, -27778854), -4373447216052.00)

    def test0306(self):
        self.assertEquals(self.calculate(148780.0, -1912690674), -284570118477720.00)

    def test0307(self):
        self.assertEquals(self.calculate(-148029.0, -555113346), 82172873495034.00)

    def test0308(self):
        self.assertEquals(self.calculate(42357.0, -1991026928), -84333927589296.00)

    def test0309(self):
        self.assertEquals(self.calculate(62037.0, -1040295434), -64536807839058.00)

    def test0310(self):
        self.assertEquals(self.calculate(165146.0, -1110699735), -183427618436310.00)

    def test0311(self):
        self.assertEquals(self.calculate(15914.0, 419187404), 6670948347256.00)

    def test0312(self):
        self.assertEquals(self.calculate(174123.0, 1588285502), 276557036464746.00)

    def test0313(self):
        self.assertEquals(self.calculate(-122897.0, 49119733), -6036667826501.00)

    def test0314(self):
        self.assertEquals(self.calculate(110886.0, 1506491231), 167048786640666.00)

    def test0315(self):
        self.assertEquals(self.calculate(-115708.0, -1148139857), 132848966573756.00)

    def test0316(self):
        self.assertEquals(self.calculate(-169077.0, 1587917714), -268480363329978.00)

    def test0317(self):
        self.assertEquals(self.calculate(20679.0, 466726046), 9651427905234.00)

    def test0318(self):
        self.assertEquals(self.calculate(91691.0, 1701238720), 155988279475520.00)

    def test0319(self):
        self.assertEquals(self.calculate(147826.0, -315126986), -46583961832436.00)

    def test0320(self):
        self.assertEquals(self.calculate(-74722.0, -1504539911), 112422231229742.00)

    def test0321(self):
        self.assertEquals(self.calculate(-25357.0, -645624470), 16371099685790.00)

    def test0322(self):
        self.assertEquals(self.calculate(107740.0, -1783960052), -192203856002480.00)

    def test0323(self):
        self.assertEquals(self.calculate(-187927.0, -1308828038), 245964126697226.00)

    def test0324(self):
        self.assertEquals(self.calculate(-49431.0, -1683663912), 83225190834072.00)

    def test0325(self):
        self.assertEquals(self.calculate(125667.0, -903386636), -113525888386212.00)

    def test0326(self):
        self.assertEquals(self.calculate(24247.0, 218438932), 5296488784204.00)

    def test0327(self):
        self.assertEquals(self.calculate(-70254.0, -2092052224), 146975036944896.00)

    def test0328(self):
        self.assertEquals(self.calculate(-118397.0, 1463970419), -173329705698343.00)

    def test0329(self):
        self.assertEquals(self.calculate(-127436.0, 216276452), -27561405937072.00)

    def test0330(self):
        self.assertEquals(self.calculate(-167580.0, -1702537842), 285311291562360.00)

    def test0331(self):
        self.assertEquals(self.calculate(-140628.0, -1137672802), 159988650799656.00)

    def test0332(self):
        self.assertEquals(self.calculate(121737.0, 427709176), 52068031958712.00)

    def test0333(self):
        self.assertEquals(self.calculate(-55477.0, 1518808061), -84258914800097.00)

    def test0334(self):
        self.assertEquals(self.calculate(105988.0, -1657965612), -175724459284656.00)

    def test0335(self):
        self.assertEquals(self.calculate(11395.0, 1917599577), 21851047179915.00)

    def test0336(self):
        self.assertEquals(self.calculate(97279.0, -2105089992), -204781049331768.00)

    def test0337(self):
        self.assertEquals(self.calculate(-8016.0, -492208555), 3945543776880.00)

    def test0338(self):
        self.assertEquals(self.calculate(184524.0, -253340914), -46747478814936.00)

    def test0339(self):
        self.assertEquals(self.calculate(-162494.0, -1634496244), 265595832672536.00)

    def test0340(self):
        self.assertEquals(self.calculate(29467.0, -1513707923), -44604431367041.00)

    def test0341(self):
        self.assertEquals(self.calculate(159800.0, -1660457675), -265341136465000.00)

    def test0342(self):
        self.assertEquals(self.calculate(184353.0, 1077328181), 198608682151893.00)

    def test0343(self):
        self.assertEquals(self.calculate(127849.0, 1363756112), 174354855163088.00)

    def test0344(self):
        self.assertEquals(self.calculate(83940.0, 385254156), 32338233854640.00)

    def test0345(self):
        self.assertEquals(self.calculate(26209.0, -1995865033), -52309626649897.00)

    def test0346(self):
        self.assertEquals(self.calculate(68162.0, -1660281225), -113168088858450.00)

    def test0347(self):
        self.assertEquals(self.calculate(-33680.0, -1075082677), 36208784561360.00)

    def test0348(self):
        self.assertEquals(self.calculate(-108409.0, -1739957011), 188626999605499.00)

    def test0349(self):
        self.assertEquals(self.calculate(-161537.0, 1890453653), -305378211744661.00)

    def test0350(self):
        self.assertEquals(self.calculate(-177994.0, -1231093170), 219127197700980.00)

    def test0351(self):
        self.assertEquals(self.calculate(38402.0, -693427089), -26628987071778.00)

    def test0352(self):
        self.assertEquals(self.calculate(-116834.0, -321326009), 37541802935506.00)

    def test0353(self):
        self.assertEquals(self.calculate(92214.0, 2126165635), 196062237865890.00)

    def test0354(self):
        self.assertEquals(self.calculate(13127.0, 2105287051), 27636103118477.00)

    def test0355(self):
        self.assertEquals(self.calculate(167251.0, -502164497), -83987514287747.00)

    def test0356(self):
        self.assertEquals(self.calculate(132062.0, -560159881), -73975834204622.00)

    def test0357(self):
        self.assertEquals(self.calculate(72558.0, -617849635), -44829933816330.00)

    def test0358(self):
        self.assertEquals(self.calculate(25465.0, -488935219), -12450735351835.00)

    def test0359(self):
        self.assertEquals(self.calculate(130373.0, -194106758), -25306280360734.00)

    def test0360(self):
        self.assertEquals(self.calculate(-55304.0, -886915236), 49049960211744.00)

    def test0361(self):
        self.assertEquals(self.calculate(124244.0, -686080146), -85241341659624.00)

    def test0362(self):
        self.assertEquals(self.calculate(-31583.0, 1229666304), -38836550879232.00)

    def test0363(self):
        self.assertEquals(self.calculate(165192.0, 1731465407), 286024233513144.00)

    def test0364(self):
        self.assertEquals(self.calculate(57239.0, -1999789589), -114465956284771.00)

    def test0365(self):
        self.assertEquals(self.calculate(160581.0, -879129191), -141171444619971.00)

    def test0366(self):
        self.assertEquals(self.calculate(-102096.0, -1861498302), 190051530640992.00)

    def test0367(self):
        self.assertEquals(self.calculate(-45322.0, 2018551369), -91484785145818.00)

    def test0368(self):
        self.assertEquals(self.calculate(192524.0, 951768137), 183238208807788.00)

    def test0369(self):
        self.assertEquals(self.calculate(25963.0, 1074721277), 27902988514751.00)

    def test0370(self):
        self.assertEquals(self.calculate(-49741.0, 220755059), -10980577389719.00)

    def test0371(self):
        self.assertEquals(self.calculate(172715.0, 2055138025), 354953163987875.00)

    def test0372(self):
        self.assertEquals(self.calculate(65162.0, -884699590), -57648794683580.00)

    def test0373(self):
        self.assertEquals(self.calculate(70741.0, 2079236858), 147087294571778.00)

    def test0374(self):
        self.assertEquals(self.calculate(-74877.0, -959631444), 71854323632388.00)

    def test0375(self):
        self.assertEquals(self.calculate(-60521.0, -1021802202), 61840491067242.00)

    def test0376(self):
        self.assertEquals(self.calculate(-15386.0, 1951468441), -30025293433226.00)

    def test0377(self):
        self.assertEquals(self.calculate(37936.0, -1003289456), -38060788802816.00)

    def test0378(self):
        self.assertEquals(self.calculate(-183321.0, 1904673985), -349166739604185.00)

    def test0379(self):
        self.assertEquals(self.calculate(123621.0, -321671977), -39765411468717.00)

    def test0380(self):
        self.assertEquals(self.calculate(-191433.0, 734382879), -140585117675607.00)

    def test0381(self):
        self.assertEquals(self.calculate(-10225.0, 537202669), -5492897290525.00)

    def test0382(self):
        self.assertEquals(self.calculate(45582.0, -2132183619), -97189193721258.00)

    def test0383(self):
        self.assertEquals(self.calculate(150359.0, 1683487690), 253127525580710.00)

    def test0384(self):
        self.assertEquals(self.calculate(-108595.0, -1140836220), 123889109310900.00)

    def test0385(self):
        self.assertEquals(self.calculate(140359.0, 838177543), 117645761757937.00)

    def test0386(self):
        self.assertEquals(self.calculate(116408.0, -848531776), -98775886980608.00)

    def test0387(self):
        self.assertEquals(self.calculate(-85666.0, -36111271), 3093508141486.00)

    def test0388(self):
        self.assertEquals(self.calculate(-53724.0, -466170171), 25044526266804.00)

    def test0389(self):
        self.assertEquals(self.calculate(-114765.0, 502426076), -57660928612140.00)

    def test0390(self):
        self.assertEquals(self.calculate(-179284.0, 1861498971), -333736981516764.00)

    def test0391(self):
        self.assertEquals(self.calculate(-35501.0, 1862883477), -66134226316977.00)

    def test0392(self):
        self.assertEquals(self.calculate(-37845.0, 475402993), -17991626270085.00)

    def test0393(self):
        self.assertEquals(self.calculate(175506.0, 129458688), 22720776496128.00)

    def test0394(self):
        self.assertEquals(self.calculate(-143470.0, -1577020304), 226255103014880.00)

    def test0395(self):
        self.assertEquals(self.calculate(-22254.0, 1182116125), -26306812245750.00)

    def test0396(self):
        self.assertEquals(self.calculate(-109554.0, 2091764407), -229161157844478.00)

    def test0397(self):
        self.assertEquals(self.calculate(-114518.0, 439451614), -50325119932052.00)

    def test0398(self):
        self.assertEquals(self.calculate(-93689.0, 1850861800), -173405391180200.00)

    def test0399(self):
        self.assertEquals(self.calculate(-14832.0, 2021269246), -29979465456672.00)

    def test0400(self):
        self.assertEquals(self.calculate(-187888.0, -18920727), 3554977554576.00)

    def test0401(self):
        self.assertEquals(self.calculate(108245.0, 682246258), 73849746197210.00)

    def test0402(self):
        self.assertEquals(self.calculate(77311.0, -1560063281), -120610052317391.00)

    def test0403(self):
        self.assertEquals(self.calculate(125748.0, 1999106840), 251383686916320.00)

    def test0404(self):
        self.assertEquals(self.calculate(-127083.0, 1318579138), -167568992594454.00)

    def test0405(self):
        self.assertEquals(self.calculate(-159334.0, 870644568), -138723281597712.00)

    def test0406(self):
        self.assertEquals(self.calculate(35012.0, -2008672750), -70327650323000.00)

    def test0407(self):
        self.assertEquals(self.calculate(-55562.0, 143824823), -7991194815526.00)

    def test0408(self):
        self.assertEquals(self.calculate(4145.0, -2109859324), -8745366897980.00)

    def test0409(self):
        self.assertEquals(self.calculate(39513.0, -402511560), -15904439270280.00)

    def test0410(self):
        self.assertEquals(self.calculate(-56443.0, 1499758630), -84650876353090.00)

    def test0411(self):
        self.assertEquals(self.calculate(-191526.0, 1245988916), -238639273125816.00)

    def test0412(self):
        self.assertEquals(self.calculate(101168.0, 1266522707), 128131569221776.00)

    def test0413(self):
        self.assertEquals(self.calculate(177879.0, -868943973), -154566884973267.00)

    def test0414(self):
        self.assertEquals(self.calculate(36196.0, 594084679), 21503489041084.00)

    def test0415(self):
        self.assertEquals(self.calculate(15572.0, 1992436949), 31026228169828.00)

    def test0416(self):
        self.assertEquals(self.calculate(-117698.0, 1187779495), -139799271002510.00)

    def test0417(self):
        self.assertEquals(self.calculate(48863.0, 1206752541), 58965549410883.00)

    def test0418(self):
        self.assertEquals(self.calculate(-131345.0, 1882403887), -247244338538015.00)

    def test0419(self):
        self.assertEquals(self.calculate(122157.0, -525100048), -64144646563536.00)

    def test0420(self):
        self.assertEquals(self.calculate(121175.0, -1382336398), -167504613027650.00)

    def test0421(self):
        self.assertEquals(self.calculate(166169.0, 1136444966), 188841923555254.00)

    def test0422(self):
        self.assertEquals(self.calculate(-25638.0, 1200599188), -30780961981944.00)

    def test0423(self):
        self.assertEquals(self.calculate(60018.0, -1281199199), -76895013525582.00)

    def test0424(self):
        self.assertEquals(self.calculate(-192472.0, -1979252599), 380950706234728.00)

    def test0425(self):
        self.assertEquals(self.calculate(174272.0, -429979313), -74933354835136.00)

    def test0426(self):
        self.assertEquals(self.calculate(-109362.0, 51806181), -5665627566522.00)

    def test0427(self):
        self.assertEquals(self.calculate(157857.0, -1968562573), -310751382086061.00)

    def test0428(self):
        self.assertEquals(self.calculate(-177409.0, 1985071052), -352169470264268.00)

    def test0429(self):
        self.assertEquals(self.calculate(-5748.0, -531014122), 3052269173256.00)

    def test0430(self):
        self.assertEquals(self.calculate(-159140.0, 1381145950), -219795566483000.00)

    def test0431(self):
        self.assertEquals(self.calculate(-79368.0, -1557674662), 123629522573616.00)

    def test0432(self):
        self.assertEquals(self.calculate(160895.0, -2103970154), -338518277927830.00)

    def test0433(self):
        self.assertEquals(self.calculate(-82448.0, -605986703), 49962391688944.00)

    def test0434(self):
        self.assertEquals(self.calculate(4251.0, -1775695103), -7548479882853.00)

    def test0435(self):
        self.assertEquals(self.calculate(-11113.0, 355825899), -3954293215587.00)

    def test0436(self):
        self.assertEquals(self.calculate(-50290.0, -940409509), 47293194207610.00)

    def test0437(self):
        self.assertEquals(self.calculate(-71555.0, 701423074), -50190328060070.00)

    def test0438(self):
        self.assertEquals(self.calculate(-157391.0, 1954635418), -307642023074438.00)

    def test0439(self):
        self.assertEquals(self.calculate(-116414.0, 946312235), -110163992525290.00)

    def test0440(self):
        self.assertEquals(self.calculate(49563.0, -1394144530), -69097985340390.00)

    def test0441(self):
        self.assertEquals(self.calculate(66916.0, -362173946), -24235231770536.00)

    def test0442(self):
        self.assertEquals(self.calculate(51767.0, -1299173337), -67254306136479.00)

    def test0443(self):
        self.assertEquals(self.calculate(-146633.0, -1054314782), 154597339429006.00)

    def test0444(self):
        self.assertEquals(self.calculate(-33022.0, 703153148), -23219523253256.00)

    def test0445(self):
        self.assertEquals(self.calculate(77569.0, 243361119), 18877278639711.00)

    def test0446(self):
        self.assertEquals(self.calculate(149667.0, -650476426), -97354855250142.00)

    def test0447(self):
        self.assertEquals(self.calculate(-76864.0, -1433834781), 110210276606784.00)

    def test0448(self):
        self.assertEquals(self.calculate(13516.0, 923441738), 12481238530808.00)

    def test0449(self):
        self.assertEquals(self.calculate(115063.0, 9021077), 1037992182851.00)

    def test0450(self):
        self.assertEquals(self.calculate(-90777.0, -401758553), 36470436165681.00)

    def test0451(self):
        self.assertEquals(self.calculate(-165005.0, 2137400482), -352681766532410.00)

    def test0452(self):
        self.assertEquals(self.calculate(-154389.0, 1555006181), -240075849278409.00)

    def test0453(self):
        self.assertEquals(self.calculate(57970.0, -312693981), -18126870078570.00)

    def test0454(self):
        self.assertEquals(self.calculate(-50207.0, -1430459458), 71819078007806.00)

    def test0455(self):
        self.assertEquals(self.calculate(-19521.0, 18938357), -369695666997.00)

    def test0456(self):
        self.assertEquals(self.calculate(68638.0, -1209053545), -82987017221710.00)

    def test0457(self):
        self.assertEquals(self.calculate(-13618.0, 1081047156), -14721700170408.00)

    def test0458(self):
        self.assertEquals(self.calculate(-169120.0, 1344949004), -227457775556480.00)

    def test0459(self):
        self.assertEquals(self.calculate(-43986.0, 671685330), -29544750925380.00)

    def test0460(self):
        self.assertEquals(self.calculate(187499.0, 904524007), 169597346788493.00)

    def test0461(self):
        self.assertEquals(self.calculate(93287.0, -532382267), -49664344541629.00)

    def test0462(self):
        self.assertEquals(self.calculate(134969.0, 119616957), 16144581069333.00)

    def test0463(self):
        self.assertEquals(self.calculate(-20387.0, -853771225), 17405833964075.00)

    def test0464(self):
        self.assertEquals(self.calculate(-178452.0, 993117001), -177223715062452.00)

    def test0465(self):
        self.assertEquals(self.calculate(13999.0, 1365590761), 19116905063239.00)

    def test0466(self):
        self.assertEquals(self.calculate(104503.0, 1765589332), 184509381961996.00)

    def test0467(self):
        self.assertEquals(self.calculate(140853.0, -591929208), -83375004734424.00)

    def test0468(self):
        self.assertEquals(self.calculate(-68035.0, -701538068), 47729142456380.00)

    def test0469(self):
        self.assertEquals(self.calculate(158843.0, -1106874569), -175819277163667.00)

    def test0470(self):
        self.assertEquals(self.calculate(56617.0, 459424052), 26011211552084.00)

    def test0471(self):
        self.assertEquals(self.calculate(-34591.0, -144118363), 4985198294533.00)

    def test0472(self):
        self.assertEquals(self.calculate(-73362.0, -520759392), 38203950515904.00)

    def test0473(self):
        self.assertEquals(self.calculate(-132711.0, 1776250416), -235727968957776.00)

    def test0474(self):
        self.assertEquals(self.calculate(-874.0, 1927605185), -1684726931690.00)

    def test0475(self):
        self.assertEquals(self.calculate(-189938.0, -877672094), 166703282190172.00)

    def test0476(self):
        self.assertEquals(self.calculate(-111508.0, 1622448413), -180915977636804.00)

    def test0477(self):
        self.assertEquals(self.calculate(-133377.0, 2054746827), -274055967544779.00)

    def test0478(self):
        self.assertEquals(self.calculate(-40356.0, 1057325912), -42669444504672.00)

    def test0479(self):
        self.assertEquals(self.calculate(23115.0, 630058571), 14563803868665.00)

    def test0480(self):
        self.assertEquals(self.calculate(-31013.0, 1156581298), -35869055794874.00)

    def test0481(self):
        self.assertEquals(self.calculate(-66929.0, 1785729479), -119517088299991.00)

    def test0482(self):
        self.assertEquals(self.calculate(-167868.0, 613692156), -103019274843408.00)

    def test0483(self):
        self.assertEquals(self.calculate(64754.0, 306397647), 19840473233838.00)

    def test0484(self):
        self.assertEquals(self.calculate(-139075.0, 123483230), -17173430212250.00)

    def test0485(self):
        self.assertEquals(self.calculate(-12215.0, 827298597), -10105452362355.00)

    def test0486(self):
        self.assertEquals(self.calculate(-193585.0, -1574666478), 304831810143630.00)

    def test0487(self):
        self.assertEquals(self.calculate(-23661.0, -728974618), 17248268436498.00)

    def test0488(self):
        self.assertEquals(self.calculate(-10625.0, -777772747), 8263835436875.00)

    def test0489(self):
        self.assertEquals(self.calculate(-2807.0, -751780917), 2110249034019.00)

    def test0490(self):
        self.assertEquals(self.calculate(33072.0, 1581900886), 52316626101792.00)

    def test0491(self):
        self.assertEquals(self.calculate(-151912.0, -766589688), 116454172683456.00)

    def test0492(self):
        self.assertEquals(self.calculate(-123743.0, -1706088886), 211116557020298.00)

    def test0493(self):
        self.assertEquals(self.calculate(145915.0, 1114535928), 162627509934120.00)

    def test0494(self):
        self.assertEquals(self.calculate(24705.0, -596657446), -14740422203430.00)

    def test0495(self):
        self.assertEquals(self.calculate(85248.0, 1325139560), 112965497210880.00)

    def test0496(self):
        self.assertEquals(self.calculate(127353.0, -1679712985), -213916487778705.00)

    def test0497(self):
        self.assertEquals(self.calculate(-73227.0, -351417727), 25733265895029.00)

    def test0498(self):
        self.assertEquals(self.calculate(76094.0, -651640590), -49585939055460.00)

    def test0499(self):
        self.assertEquals(self.calculate(-141001.0, 1349645049), -190301301554049.00)

    def test0500(self):
        self.assertEquals(self.calculate(-89555.0, -412814805), 36969629861775.00)

    def test0501(self):
        self.assertEquals(self.calculate(162386.0, 2049918007), 332877985484702.00)

    def test0502(self):
        self.assertEquals(self.calculate(85027.0, -244160192), -20760208645184.00)

    def test0503(self):
        self.assertEquals(self.calculate(108978.0, 758531494), 82663245153132.00)

    def test0504(self):
        self.assertEquals(self.calculate(-121600.0, 1140651459), -138703217414400.00)

    def test0505(self):
        self.assertEquals(self.calculate(-9986.0, 1775817153), -17733310089858.00)

    def test0506(self):
        self.assertEquals(self.calculate(153451.0, 1808256851), 277478822042801.00)

    def test0507(self):
        self.assertEquals(self.calculate(-182849.0, 1848029595), -337910363416155.00)

    def test0508(self):
        self.assertEquals(self.calculate(-78744.0, -789651640), 62180328740160.00)

    def test0509(self):
        self.assertEquals(self.calculate(-75248.0, -1417983891), 106700451829968.00)

    def test0510(self):
        self.assertEquals(self.calculate(-56518.0, -1959167126), 110728207627268.00)

    def test0511(self):
        self.assertEquals(self.calculate(-151717.0, -1499012404), 227425664897668.00)

    def test0512(self):
        self.assertEquals(self.calculate(-139777.0, 1878196638), -262528691469726.00)

    def test0513(self):
        self.assertEquals(self.calculate(-95867.0, -1049859050), 100646837546350.00)

    def test0514(self):
        self.assertEquals(self.calculate(79920.0, -162338488), -12974091960960.00)

    def test0515(self):
        self.assertEquals(self.calculate(-39627.0, -1140165094), 45181322179938.00)

    def test0516(self):
        self.assertEquals(self.calculate(-129261.0, 1957564180), -253036703470980.00)

    def test0517(self):
        self.assertEquals(self.calculate(46000.0, -133815046), -6155492116000.00)

    def test0518(self):
        self.assertEquals(self.calculate(-179558.0, 1470776428), -264089673858824.00)

    def test0519(self):
        self.assertEquals(self.calculate(-120787.0, -465941502), 56279676202074.00)

    def test0520(self):
        self.assertEquals(self.calculate(-108375.0, 6956221), -753880450875.00)

    def test0521(self):
        self.assertEquals(self.calculate(131320.0, 1289829211), 169380371988520.00)

    def test0522(self):
        self.assertEquals(self.calculate(31952.0, -2002768936), -63992473043072.00)

    def test0523(self):
        self.assertEquals(self.calculate(-125176.0, -1718101343), 215065053711368.00)

    def test0524(self):
        self.assertEquals(self.calculate(-21823.0, -2079603063), 45383177643849.00)

    def test0525(self):
        self.assertEquals(self.calculate(33571.0, 1611279605), 54092267619455.00)

    def test0526(self):
        self.assertEquals(self.calculate(139082.0, 2120715263), 294953320208566.00)

    def test0527(self):
        self.assertEquals(self.calculate(-29322.0, -1730171915), 50732100891630.00)

    def test0528(self):
        self.assertEquals(self.calculate(-134675.0, -1094636128), 147420120538400.00)

    def test0529(self):
        self.assertEquals(self.calculate(-51148.0, 2099647074), -107392748540952.00)

    def test0530(self):
        self.assertEquals(self.calculate(199153.0, 1706254831), 339805768358143.00)

    def test0531(self):
        self.assertEquals(self.calculate(-3357.0, -2134754115), 7166369564055.00)

    def test0532(self):
        self.assertEquals(self.calculate(159047.0, -1026870772), -163320715674284.00)

    def test0533(self):
        self.assertEquals(self.calculate(64991.0, -1660420863), -107912412307233.00)

    def test0534(self):
        self.assertEquals(self.calculate(111063.0, 1989100197), 220915435179411.00)

    def test0535(self):
        self.assertEquals(self.calculate(30713.0, 894522481), 27473468958953.00)

    def test0536(self):
        self.assertEquals(self.calculate(91969.0, 1632491662), 150138625662478.00)

    def test0537(self):
        self.assertEquals(self.calculate(-75115.0, -1337444775), 100462164274125.00)

    def test0538(self):
        self.assertEquals(self.calculate(-123803.0, -664434450), 82258978213350.00)

    def test0539(self):
        self.assertEquals(self.calculate(-150790.0, 2063260565), -311119060596350.00)

    def test0540(self):
        self.assertEquals(self.calculate(-128490.0, -583816980), 75014643760200.00)

    def test0541(self):
        self.assertEquals(self.calculate(185666.0, 329538959), 61184180361694.00)

    def test0542(self):
        self.assertEquals(self.calculate(190172.0, 860517654), 163646363296488.00)

    def test0543(self):
        self.assertEquals(self.calculate(95207.0, -176561291), -16809870832237.00)

    def test0544(self):
        self.assertEquals(self.calculate(-98151.0, -1456628899), 142969583065749.00)

    def test0545(self):
        self.assertEquals(self.calculate(115091.0, -325813471), -37498198190861.00)

    def test0546(self):
        self.assertEquals(self.calculate(-134893.0, -666747977), 89939634861461.00)

    def test0547(self):
        self.assertEquals(self.calculate(-11925.0, -1586211197), 18915568524225.00)

    def test0548(self):
        self.assertEquals(self.calculate(196333.0, 1210685171), 237697451677943.00)

    def test0549(self):
        self.assertEquals(self.calculate(37300.0, -379527303), -14156368401900.00)

    def test0550(self):
        self.assertEquals(self.calculate(-42053.0, -444555056), 18694873769968.00)

    def test0551(self):
        self.assertEquals(self.calculate(-39717.0, 421427067), -16737818820039.00)

    def test0552(self):
        self.assertEquals(self.calculate(59977.0, -381172837), -22861603244749.00)

    def test0553(self):
        self.assertEquals(self.calculate(-81129.0, 1640863146), -133121586171834.00)

    def test0554(self):
        self.assertEquals(self.calculate(-160821.0, 2067802146), -332546008921866.00)

    def test0555(self):
        self.assertEquals(self.calculate(71940.0, 1825848288), 131351525838720.00)

    def test0556(self):
        self.assertEquals(self.calculate(51929.0, 2027456862), 105283807386798.00)

    def test0557(self):
        self.assertEquals(self.calculate(-74026.0, -1127308706), 83450154270356.00)

    def test0558(self):
        self.assertEquals(self.calculate(-58063.0, 611372577), -35498125938351.00)

    def test0559(self):
        self.assertEquals(self.calculate(-112934.0, -1897579228), 214301212534952.00)

    def test0560(self):
        self.assertEquals(self.calculate(-135654.0, -1546140976), 209740207958304.00)

    def test0561(self):
        self.assertEquals(self.calculate(158715.0, -1673717842), -265644127293030.00)

    def test0562(self):
        self.assertEquals(self.calculate(58666.0, 1252376883), 73471942218078.00)

    def test0563(self):
        self.assertEquals(self.calculate(-6093.0, -1498990636), 9133349945148.00)

    def test0564(self):
        self.assertEquals(self.calculate(147732.0, -1135765650), -167788931005800.00)

    def test0565(self):
        self.assertEquals(self.calculate(-159060.0, -649121731), 103249302532860.00)

    def test0566(self):
        self.assertEquals(self.calculate(-169406.0, 102683544), -17395208454864.00)

    def test0567(self):
        self.assertEquals(self.calculate(139699.0, -1717372093), -239915164020007.00)

    def test0568(self):
        self.assertEquals(self.calculate(12388.0, 659252649), 8166821815812.00)

    def test0569(self):
        self.assertEquals(self.calculate(67751.0, 2041595691), 138320149660941.00)

    def test0570(self):
        self.assertEquals(self.calculate(-70117.0, -1844929517), 129360922943489.00)

    def test0571(self):
        self.assertEquals(self.calculate(100936.0, -1622137653), -163732086143208.00)

    def test0572(self):
        self.assertEquals(self.calculate(-195142.0, -1134958866), 221478143028972.00)

    def test0573(self):
        self.assertEquals(self.calculate(-198243.0, 51072224), -10124710902432.00)

    def test0574(self):
        self.assertEquals(self.calculate(-104642.0, -326072140), 34120840873880.00)

    def test0575(self):
        self.assertEquals(self.calculate(-155785.0, 2130217903), -331855996018855.00)

    def test0576(self):
        self.assertEquals(self.calculate(-93799.0, -545252546), 51144143562254.00)

    def test0577(self):
        self.assertEquals(self.calculate(88312.0, 128855613), 11379496895256.00)

    def test0578(self):
        self.assertEquals(self.calculate(-88047.0, -610382945), 53742387158415.00)

    def test0579(self):
        self.assertEquals(self.calculate(-43735.0, 2029793677), -88773026463595.00)

    def test0580(self):
        self.assertEquals(self.calculate(-85917.0, 429144928), -36870844778976.00)

    def test0581(self):
        self.assertEquals(self.calculate(44909.0, 1396934224), 62734919065616.00)

    def test0582(self):
        self.assertEquals(self.calculate(66411.0, -1138361720), -75599740186920.00)

    def test0583(self):
        self.assertEquals(self.calculate(-23557.0, -1096838817), 25838232012069.00)

    def test0584(self):
        self.assertEquals(self.calculate(-126743.0, -1090156026), 138169645203318.00)

    def test0585(self):
        self.assertEquals(self.calculate(156256.0, 1788901112), 279526532156672.00)

    def test0586(self):
        self.assertEquals(self.calculate(-36253.0, -1866445152), 67664236095456.00)

    def test0587(self):
        self.assertEquals(self.calculate(101827.0, -977650426), -99551209928302.00)

    def test0588(self):
        self.assertEquals(self.calculate(9638.0, 1383688863), 13335993261594.00)

    def test0589(self):
        self.assertEquals(self.calculate(-15850.0, 223868411), -3548314314350.00)

    def test0590(self):
        self.assertEquals(self.calculate(165351.0, 185365272), 30650333090472.00)

    def test0591(self):
        self.assertEquals(self.calculate(46171.0, -1596410701), -73707878475871.00)

    def test0592(self):
        self.assertEquals(self.calculate(-191245.0, 15803015), -3022247603675.00)

    def test0593(self):
        self.assertEquals(self.calculate(-59650.0, -156903171), 9359274150150.00)

    def test0594(self):
        self.assertEquals(self.calculate(18621.0, 293672003), 5468466367863.00)

    def test0595(self):
        self.assertEquals(self.calculate(-34149.0, -368244251), 12575172927399.00)

    def test0596(self):
        self.assertEquals(self.calculate(-153631.0, -162958327), 25035450735337.00)

    def test0597(self):
        self.assertEquals(self.calculate(86236.0, -1197088791), -103232148980676.00)

    def test0598(self):
        self.assertEquals(self.calculate(-88198.0, -2055792480), 181316785151040.00)

    def test0599(self):
        self.assertEquals(self.calculate(47390.0, -351916956), -16677344544840.00)

    def test0600(self):
        self.assertEquals(self.calculate(-87436.0, -851229707), 74428120661252.00)

    def test0601(self):
        self.assertEquals(self.calculate(-139848.0, -501295120), 70105119941760.00)

    def test0602(self):
        self.assertEquals(self.calculate(171753.0, 1086730900), 186649292267700.00)

    def test0603(self):
        self.assertEquals(self.calculate(3322.0, -2122403393), -7050624071546.00)

    def test0604(self):
        self.assertEquals(self.calculate(-151530.0, -123088631), 18651620255430.00)

    def test0605(self):
        self.assertEquals(self.calculate(-18184.0, 1861128230), -33842755734320.00)

    def test0606(self):
        self.assertEquals(self.calculate(181558.0, -1472696234), -267379782852572.00)

    def test0607(self):
        self.assertEquals(self.calculate(-168671.0, 1644785137), -277427553842927.00)

    def test0608(self):
        self.assertEquals(self.calculate(19477.0, 1329644562), 25897487134074.00)

    def test0609(self):
        self.assertEquals(self.calculate(-168497.0, 1326683615), -223542209076655.00)

    def test0610(self):
        self.assertEquals(self.calculate(-106783.0, 362272108), -38684502508564.00)

    def test0611(self):
        self.assertEquals(self.calculate(157761.0, -1948107287), -307335353704407.00)

    def test0612(self):
        self.assertEquals(self.calculate(-138346.0, 2084712903), -288411691278438.00)

    def test0613(self):
        self.assertEquals(self.calculate(-179535.0, 562735312), -101030684239920.00)

    def test0614(self):
        self.assertEquals(self.calculate(26132.0, 1905445679), 49793106483628.00)

    def test0615(self):
        self.assertEquals(self.calculate(114625.0, -1306286072), -149733041003000.00)

    def test0616(self):
        self.assertEquals(self.calculate(-145406.0, 1238779873), -180126026213438.00)

    def test0617(self):
        self.assertEquals(self.calculate(64531.0, -830839810), -53614923779110.00)

    def test0618(self):
        self.assertEquals(self.calculate(93057.0, 742799273), 69122671947561.00)

    def test0619(self):
        self.assertEquals(self.calculate(84017.0, 698947016), 58723431443272.00)

    def test0620(self):
        self.assertEquals(self.calculate(-28492.0, -822028369), 23421232289548.00)

    def test0621(self):
        self.assertEquals(self.calculate(9513.0, 347561090), 3306348649170.00)

    def test0622(self):
        self.assertEquals(self.calculate(-161463.0, -35660834), 5757905240142.00)

    def test0623(self):
        self.assertEquals(self.calculate(-142955.0, 1307278848), -186882047715840.00)

    def test0624(self):
        self.assertEquals(self.calculate(166359.0, 2131909097), 354662265467823.00)

    def test0625(self):
        self.assertEquals(self.calculate(59062.0, -1114349239), -65815694753818.00)

    def test0626(self):
        self.assertEquals(self.calculate(-81674.0, 954626421), -77968158308754.00)

    def test0627(self):
        self.assertEquals(self.calculate(-112773.0, 1500696850), -169238085865050.00)

    def test0628(self):
        self.assertEquals(self.calculate(-193222.0, -1084966437), 209639384890014.00)

    def test0629(self):
        self.assertEquals(self.calculate(-74629.0, -323778804), 24163288363716.00)

    def test0630(self):
        self.assertEquals(self.calculate(-105778.0, 1991046370), -210608902925860.00)

    def test0631(self):
        self.assertEquals(self.calculate(77433.0, -1940800439), -150282000393087.00)

    def test0632(self):
        self.assertEquals(self.calculate(32012.0, -517493677), -16566007588124.00)

    def test0633(self):
        self.assertEquals(self.calculate(-155598.0, -1914488236), 297890540545128.00)

    def test0634(self):
        self.assertEquals(self.calculate(73376.0, -1265914246), -92887723714496.00)

    def test0635(self):
        self.assertEquals(self.calculate(-125451.0, -1497079668), 187810141430268.00)

    def test0636(self):
        self.assertEquals(self.calculate(123508.0, 1860195566), 229749033965528.00)

    def test0637(self):
        self.assertEquals(self.calculate(197445.0, -138005388), -27248473833660.00)

    def test0638(self):
        self.assertEquals(self.calculate(-103745.0, -937209080), 97230756004600.00)

    def test0639(self):
        self.assertEquals(self.calculate(106462.0, 388457538), 41355966410556.00)

    def test0640(self):
        self.assertEquals(self.calculate(140831.0, -1858184506), -261689982164486.00)

    def test0641(self):
        self.assertEquals(self.calculate(172968.0, 725743879), 125530467262872.00)

    def test0642(self):
        self.assertEquals(self.calculate(-11488.0, -640619092), 7359432128896.00)

    def test0643(self):
        self.assertEquals(self.calculate(188017.0, 997658777), 187576810275209.00)

    def test0644(self):
        self.assertEquals(self.calculate(3052.0, -2099124184), -6406527009568.00)

    def test0645(self):
        self.assertEquals(self.calculate(171272.0, -583682650), -99968494830800.00)

    def test0646(self):
        self.assertEquals(self.calculate(-130297.0, 257406348), -33539274925356.00)

    def test0647(self):
        self.assertEquals(self.calculate(25022.0, 989374056), 24756117629232.00)

    def test0648(self):
        self.assertEquals(self.calculate(-48398.0, -1321572), 63961441656.00)

    def test0649(self):
        self.assertEquals(self.calculate(27815.0, 1677445769), 46658154064735.00)

    def test0650(self):
        self.assertEquals(self.calculate(167223.0, -728305850), -121789489154550.00)

    def test0651(self):
        self.assertEquals(self.calculate(-110610.0, 644043590), -71237661489900.00)

    def test0652(self):
        self.assertEquals(self.calculate(87199.0, 2097669993), 182914725719607.00)

    def test0653(self):
        self.assertEquals(self.calculate(-195478.0, 1085078763), -212109026433714.00)

    def test0654(self):
        self.assertEquals(self.calculate(168482.0, -940207997), -158408123750554.00)

    def test0655(self):
        self.assertEquals(self.calculate(-34036.0, 1239885667), -42200748562012.00)

    def test0656(self):
        self.assertEquals(self.calculate(-123797.0, -320359665), 39659565448005.00)

    def test0657(self):
        self.assertEquals(self.calculate(-62025.0, -1710849392), 106115433538800.00)

    def test0658(self):
        self.assertEquals(self.calculate(192014.0, 1138854533), 218676014299462.00)

    def test0659(self):
        self.assertEquals(self.calculate(136259.0, -307071946), -41841316290014.00)

    def test0660(self):
        self.assertEquals(self.calculate(48461.0, 1691104883), 81952633735063.00)

    def test0661(self):
        self.assertEquals(self.calculate(91936.0, 1188199700), 109238327619200.00)

    def test0662(self):
        self.assertEquals(self.calculate(118684.0, -282158229), -33487667250636.00)

    def test0663(self):
        self.assertEquals(self.calculate(-68622.0, -19181434), 1316268363948.00)

    def test0664(self):
        self.assertEquals(self.calculate(-99898.0, 17253180), -1723558175640.00)

    def test0665(self):
        self.assertEquals(self.calculate(82910.0, 1521590528), 126155070676480.00)

    def test0666(self):
        self.assertEquals(self.calculate(74723.0, -2097419225), -156725456749675.00)

    def test0667(self):
        self.assertEquals(self.calculate(2451.0, 410552698), 1006264662798.00)

    def test0668(self):
        self.assertEquals(self.calculate(-46384.0, -1594989958), 73982014211872.00)

    def test0669(self):
        self.assertEquals(self.calculate(41203.0, -643611848), -26518738973144.00)

    def test0670(self):
        self.assertEquals(self.calculate(96931.0, -205573257), -19926421374267.00)

    def test0671(self):
        self.assertEquals(self.calculate(-90546.0, -384827072), 34844552061312.00)

    def test0672(self):
        self.assertEquals(self.calculate(147863.0, 480635799), 71068251147537.00)

    def test0673(self):
        self.assertEquals(self.calculate(16017.0, 444385701), 7117725772917.00)

    def test0674(self):
        self.assertEquals(self.calculate(-62067.0, 1759291034), -109193916607278.00)

    def test0675(self):
        self.assertEquals(self.calculate(-86639.0, 1531638555), -132699632766645.00)

    def test0676(self):
        self.assertEquals(self.calculate(-4458.0, 1791727928), -7987523103024.00)

    def test0677(self):
        self.assertEquals(self.calculate(105361.0, -1994643711), -210157656034671.00)

    def test0678(self):
        self.assertEquals(self.calculate(-135073.0, 2061548369), -278459522845937.00)

    def test0679(self):
        self.assertEquals(self.calculate(109989.0, -1018965714), -112075019917146.00)

    def test0680(self):
        self.assertEquals(self.calculate(33839.0, -1700221415), -57533792462185.00)

    def test0681(self):
        self.assertEquals(self.calculate(192065.0, -1639782159), -314944760368335.00)

    def test0682(self):
        self.assertEquals(self.calculate(83051.0, -2116153769), -175748686669219.00)

    def test0683(self):
        self.assertEquals(self.calculate(59884.0, 618658913), 37047770346092.00)

    def test0684(self):
        self.assertEquals(self.calculate(67127.0, 169714891), 11392451488157.00)

    def test0685(self):
        self.assertEquals(self.calculate(171094.0, -1207257018), -206554432237692.00)

    def test0686(self):
        self.assertEquals(self.calculate(-172011.0, -1345668880), 231469849717680.00)

    def test0687(self):
        self.assertEquals(self.calculate(39631.0, -1980735577), -78498531652087.00)

    def test0688(self):
        self.assertEquals(self.calculate(164489.0, -978246921), -160910857788369.00)

    def test0689(self):
        self.assertEquals(self.calculate(-133671.0, 1962233193), -262293673141503.00)

    def test0690(self):
        self.assertEquals(self.calculate(7105.0, 1814530875), 12892241866875.00)

    def test0691(self):
        self.assertEquals(self.calculate(73837.0, -700070168), -51691080994616.00)

    def test0692(self):
        self.assertEquals(self.calculate(-93168.0, 1244446957), -115942634089776.00)

    def test0693(self):
        self.assertEquals(self.calculate(-121138.0, 503943612), -61046721270456.00)

    def test0694(self):
        self.assertEquals(self.calculate(-12360.0, 229304119), -2834198910840.00)

    def test0695(self):
        self.assertEquals(self.calculate(153664.0, 2104943287), 323454005253568.00)

    def test0696(self):
        self.assertEquals(self.calculate(166555.0, 1957190765), 325979907864575.00)

    def test0697(self):
        self.assertEquals(self.calculate(-171747.0, 939230604), -161310038545188.00)

    def test0698(self):
        self.assertEquals(self.calculate(56179.0, 1746430375), 98112712037125.00)

    def test0699(self):
        self.assertEquals(self.calculate(-66368.0, -1469202235), 97508013932480.00)

    def test0700(self):
        self.assertEquals(self.calculate(-10716.0, -1499803408), 16071893320128.00)

    def test0701(self):
        self.assertEquals(self.calculate(-66212.0, 1486472436), -98422312932432.00)

    def test0702(self):
        self.assertEquals(self.calculate(-23764.0, -1339320715), 31827617471260.00)

    def test0703(self):
        self.assertEquals(self.calculate(-110864.0, -1435879151), 159187306196464.00)

    def test0704(self):
        self.assertEquals(self.calculate(106418.0, 1343117715), 142931900994870.00)

    def test0705(self):
        self.assertEquals(self.calculate(-131794.0, 140235803), -18482237420582.00)

    def test0706(self):
        self.assertEquals(self.calculate(175200.0, -1238237417), -216939195458400.00)

    def test0707(self):
        self.assertEquals(self.calculate(-27013.0, -1406094821), 37982839399673.00)

    def test0708(self):
        self.assertEquals(self.calculate(21731.0, -2005084933), -43572500679023.00)

    def test0709(self):
        self.assertEquals(self.calculate(-43373.0, -598898349), 25976018091177.00)

    def test0710(self):
        self.assertEquals(self.calculate(145128.0, 1792525524), 260145644247072.00)

    def test0711(self):
        self.assertEquals(self.calculate(1847.0, -737365452), -1361913989844.00)

    def test0712(self):
        self.assertEquals(self.calculate(73751.0, -2143063765), -158053095732515.00)

    def test0713(self):
        self.assertEquals(self.calculate(-126853.0, 957976540), -121522198028620.00)

    def test0714(self):
        self.assertEquals(self.calculate(158620.0, -490792216), -77849461301920.00)

    def test0715(self):
        self.assertEquals(self.calculate(9405.0, 363358426), 3417385996530.00)

    def test0716(self):
        self.assertEquals(self.calculate(-126832.0, -1890383066), 239761065026912.00)

    def test0717(self):
        self.assertEquals(self.calculate(-45093.0, 239571148), -10802981776764.00)

    def test0718(self):
        self.assertEquals(self.calculate(12902.0, 1239928914), 15997562848428.00)

    def test0719(self):
        self.assertEquals(self.calculate(186080.0, 2127269743), 395842353777440.00)

    def test0720(self):
        self.assertEquals(self.calculate(90188.0, 1247150489), 112478008301932.00)

    def test0721(self):
        self.assertEquals(self.calculate(-62985.0, 906771558), -57113006580630.00)

    def test0722(self):
        self.assertEquals(self.calculate(102834.0, -877108345), -90196559549730.00)

    def test0723(self):
        self.assertEquals(self.calculate(-189800.0, -1719233502), 326310518679600.00)

    def test0724(self):
        self.assertEquals(self.calculate(72129.0, 351242756), 25334788747524.00)

    def test0725(self):
        self.assertEquals(self.calculate(159759.0, 1506041597), 240603699495123.00)

    def test0726(self):
        self.assertEquals(self.calculate(148975.0, 477313729), 71107812777775.00)

    def test0727(self):
        self.assertEquals(self.calculate(-74886.0, -853952792), 63949108781712.00)

    def test0728(self):
        self.assertEquals(self.calculate(138942.0, -1515224862), -210528372776004.00)

    def test0729(self):
        self.assertEquals(self.calculate(-189377.0, -1790067384), 338997590979768.00)

    def test0730(self):
        self.assertEquals(self.calculate(186671.0, -678352806), -126628796648826.00)

    def test0731(self):
        self.assertEquals(self.calculate(79430.0, 2144276892), 170319913531560.00)

    def test0732(self):
        self.assertEquals(self.calculate(-97837.0, -950955865), 93038668964005.00)

    def test0733(self):
        self.assertEquals(self.calculate(64865.0, 374061809), 24263519240785.00)

    def test0734(self):
        self.assertEquals(self.calculate(66289.0, -1543480252), -102315762424828.00)

    def test0735(self):
        self.assertEquals(self.calculate(-60239.0, 757512802), -45631813679678.00)

    def test0736(self):
        self.assertEquals(self.calculate(-51578.0, 863444374), -44534733922172.00)

    def test0737(self):
        self.assertEquals(self.calculate(-34966.0, 1500007179), -52449251020914.00)

    def test0738(self):
        self.assertEquals(self.calculate(-169135.0, -1605089024), 271476732074240.00)

    def test0739(self):
        self.assertEquals(self.calculate(-5560.0, -1752187427), 9742162094120.00)

    def test0740(self):
        self.assertEquals(self.calculate(108249.0, 1407988363), 152413332306387.00)

    def test0741(self):
        self.assertEquals(self.calculate(-177450.0, -2061589165), 365828997329250.00)

    def test0742(self):
        self.assertEquals(self.calculate(-164203.0, 1199137367), -196901953073501.00)

    def test0743(self):
        self.assertEquals(self.calculate(-130210.0, 1458271284), -189881503889640.00)

    def test0744(self):
        self.assertEquals(self.calculate(-174554.0, 2067579938), -360904348497652.00)

    def test0745(self):
        self.assertEquals(self.calculate(-74949.0, -297230205), 22277106634545.00)

    def test0746(self):
        self.assertEquals(self.calculate(136139.0, 1591467132), 216660743883348.00)

    def test0747(self):
        self.assertEquals(self.calculate(-86125.0, 1894458896), -163160272418000.00)

    def test0748(self):
        self.assertEquals(self.calculate(69859.0, -545823714), -38130698836326.00)

    def test0749(self):
        self.assertEquals(self.calculate(138681.0, 932696403), 129347269864443.00)

    def test0750(self):
        self.assertEquals(self.calculate(-99980.0, -287278329), 28722087333420.00)

    def test0751(self):
        self.assertEquals(self.calculate(143019.0, 454221028), 64962237203532.00)

    def test0752(self):
        self.assertEquals(self.calculate(-88436.0, 1288321563), -113934005745468.00)

    def test0753(self):
        self.assertEquals(self.calculate(-196760.0, -135278701), 26617437208760.00)

    def test0754(self):
        self.assertEquals(self.calculate(-105712.0, -2123234811), 224451398340432.00)

    def test0755(self):
        self.assertEquals(self.calculate(69576.0, 1883775538), 131065566831888.00)

    def test0756(self):
        self.assertEquals(self.calculate(-35299.0, -589089620), 20794274496380.00)

    def test0757(self):
        self.assertEquals(self.calculate(93539.0, 1704238532), 159412768044748.00)

    def test0758(self):
        self.assertEquals(self.calculate(103928.0, 2090199929), 217230298221112.00)

    def test0759(self):
        self.assertEquals(self.calculate(146690.0, -773174162), -113416917823780.00)

    def test0760(self):
        self.assertEquals(self.calculate(173828.0, -1626190319), -282677410771132.00)

    def test0761(self):
        self.assertEquals(self.calculate(-129530.0, 638035071), -82644682746630.00)

    def test0762(self):
        self.assertEquals(self.calculate(-88186.0, 392754970), -34635489784420.00)

    def test0763(self):
        self.assertEquals(self.calculate(-198934.0, -1930685073), 384078904312182.00)

    def test0764(self):
        self.assertEquals(self.calculate(-91107.0, 1537556882), -140082194848374.00)

    def test0765(self):
        self.assertEquals(self.calculate(-189853.0, 655204108), -124392465516124.00)

    def test0766(self):
        self.assertEquals(self.calculate(47999.0, -1749957772), -83996223098228.00)

    def test0767(self):
        self.assertEquals(self.calculate(-85238.0, 95420766), -8133475252308.00)

    def test0768(self):
        self.assertEquals(self.calculate(4352.0, 1676869102), 7297734331904.00)

    def test0769(self):
        self.assertEquals(self.calculate(-165900.0, 1506973814), -250006955742600.00)

    def test0770(self):
        self.assertEquals(self.calculate(-136312.0, -1976315721), 269395548560952.00)

    def test0771(self):
        self.assertEquals(self.calculate(-95274.0, -219499940), 20912637283560.00)

    def test0772(self):
        self.assertEquals(self.calculate(-100108.0, -13214738), 1322900991704.00)

    def test0773(self):
        self.assertEquals(self.calculate(150911.0, 1708182733), 257783564419763.00)

    def test0774(self):
        self.assertEquals(self.calculate(43114.0, -695093795), -29968273877630.00)

    def test0775(self):
        self.assertEquals(self.calculate(-104457.0, 1915678322), -200106010481154.00)

    def test0776(self):
        self.assertEquals(self.calculate(22168.0, 90165678), 1998792749904.00)

    def test0777(self):
        self.assertEquals(self.calculate(166961.0, 228890488), 38215784766968.00)

    def test0778(self):
        self.assertEquals(self.calculate(111843.0, -164599862), -18409342365666.00)

    def test0779(self):
        self.assertEquals(self.calculate(-87396.0, 1921038115), -167891047098540.00)

    def test0780(self):
        self.assertEquals(self.calculate(-109696.0, -1646543013), 180619182354048.00)

    def test0781(self):
        self.assertEquals(self.calculate(-48902.0, -323688756), 15829027545912.00)

    def test0782(self):
        self.assertEquals(self.calculate(136218.0, 228988647), 31192375517046.00)

    def test0783(self):
        self.assertEquals(self.calculate(-155730.0, 527258331), -82109939886630.00)

    def test0784(self):
        self.assertEquals(self.calculate(-110432.0, 1138355136), -125710834378752.00)

    def test0785(self):
        self.assertEquals(self.calculate(-36316.0, -1830506594), 66476677467704.00)

    def test0786(self):
        self.assertEquals(self.calculate(-105564.0, 719577180), -75961445429520.00)

    def test0787(self):
        self.assertEquals(self.calculate(-72034.0, 1974093908), -142201880568872.00)

    def test0788(self):
        self.assertEquals(self.calculate(38874.0, 13584216), 528072812784.00)

    def test0789(self):
        self.assertEquals(self.calculate(-40923.0, 1830478607), -74908676034261.00)

    def test0790(self):
        self.assertEquals(self.calculate(144246.0, 2038201612), 294002429724552.00)

    def test0791(self):
        self.assertEquals(self.calculate(125932.0, -294170804), -37045517689328.00)

    def test0792(self):
        self.assertEquals(self.calculate(-44937.0, -710653853), 31934652192261.00)

    def test0793(self):
        self.assertEquals(self.calculate(38180.0, 699833867), 26719657042060.00)

    def test0794(self):
        self.assertEquals(self.calculate(-145086.0, -458552461), 66529542356646.00)

    def test0795(self):
        self.assertEquals(self.calculate(-144188.0, 1467658027), -211618675597076.00)

    def test0796(self):
        self.assertEquals(self.calculate(-21095.0, -365659920), 7713596012400.00)

    def test0797(self):
        self.assertEquals(self.calculate(43736.0, -1691126691), -73963116957576.00)

    def test0798(self):
        self.assertEquals(self.calculate(141668.0, -1322811095), -187400002206460.00)

    def test0799(self):
        self.assertEquals(self.calculate(-125101.0, 854772662), -106932914788862.00)

    def test0800(self):
        self.assertEquals(self.calculate(52263.0, -1616768147), -84497153666661.00)

    def test0801(self):
        self.assertEquals(self.calculate(57667.0, -966853432), -55755536863144.00)

    def test0802(self):
        self.assertEquals(self.calculate(-170578.0, -632188042), 107837371828276.00)

    def test0803(self):
        self.assertEquals(self.calculate(-141441.0, -1152749310), 163046015155710.00)

    def test0804(self):
        self.assertEquals(self.calculate(-32328.0, 264892046), -8563430063088.00)

    def test0805(self):
        self.assertEquals(self.calculate(-48355.0, -1294101645), 62576285043975.00)

    def test0806(self):
        self.assertEquals(self.calculate(44811.0, -653229855), -29271883032405.00)

    def test0807(self):
        self.assertEquals(self.calculate(-83940.0, 1240734207), -104147229335580.00)

    def test0808(self):
        self.assertEquals(self.calculate(-158937.0, -226577674), 36011575772538.00)

    def test0809(self):
        self.assertEquals(self.calculate(-114347.0, -1379635416), 157757170913352.00)

    def test0810(self):
        self.assertEquals(self.calculate(58225.0, -1586674783), -92384139240175.00)

    def test0811(self):
        self.assertEquals(self.calculate(-72551.0, 645479619), -46830191838069.00)

    def test0812(self):
        self.assertEquals(self.calculate(-82029.0, -208062064), 17067123047856.00)

    def test0813(self):
        self.assertEquals(self.calculate(150273.0, -1870520756), -281088765566388.00)

    def test0814(self):
        self.assertEquals(self.calculate(48428.0, -1635579736), -79207855455008.00)

    def test0815(self):
        self.assertEquals(self.calculate(-89288.0, 1364522361), -121835472568968.00)

    def test0816(self):
        self.assertEquals(self.calculate(7060.0, -747862261), -5279907562660.00)

    def test0817(self):
        self.assertEquals(self.calculate(112357.0, -515861309), -57960629095313.00)

    def test0818(self):
        self.assertEquals(self.calculate(108318.0, 1760009291), 190640686382538.00)

    def test0819(self):
        self.assertEquals(self.calculate(-104465.0, 554069210), -57880840022650.00)

    def test0820(self):
        self.assertEquals(self.calculate(-149108.0, -595881932), 88850763116656.00)

    def test0821(self):
        self.assertEquals(self.calculate(157977.0, 313635475), 49547191434075.00)

    def test0822(self):
        self.assertEquals(self.calculate(124804.0, 1922407724), 239924173586096.00)

    def test0823(self):
        self.assertEquals(self.calculate(-51264.0, 1938268332), -99363387771648.00)

    def test0824(self):
        self.assertEquals(self.calculate(82762.0, 1341844337), 111053721018794.00)

    def test0825(self):
        self.assertEquals(self.calculate(134415.0, 720252575), 96812749868625.00)

    def test0826(self):
        self.assertEquals(self.calculate(-31827.0, -1500061798), 47742466844946.00)

    def test0827(self):
        self.assertEquals(self.calculate(-60519.0, 430460024), -26051010192456.00)

    def test0828(self):
        self.assertEquals(self.calculate(24563.0, -1351019354), -33185088392302.00)

    def test0829(self):
        self.assertEquals(self.calculate(-11665.0, -412800102), 4815313189830.00)

    def test0830(self):
        self.assertEquals(self.calculate(115209.0, -189136199), -21790192350591.00)

    def test0831(self):
        self.assertEquals(self.calculate(-107459.0, -1990904415), 213940597531485.00)

    def test0832(self):
        self.assertEquals(self.calculate(185350.0, 1366560163), 253291926212050.00)

    def test0833(self):
        self.assertEquals(self.calculate(182536.0, 1712096289), 312519208208904.00)

    def test0834(self):
        self.assertEquals(self.calculate(-152787.0, -996126258), 152195142581046.00)

    def test0835(self):
        self.assertEquals(self.calculate(92724.0, -403966457), -37457385758868.00)

    def test0836(self):
        self.assertEquals(self.calculate(137828.0, -612438486), -84411171648408.00)

    def test0837(self):
        self.assertEquals(self.calculate(163807.0, 134573637), 22044103756059.00)

    def test0838(self):
        self.assertEquals(self.calculate(126278.0, -570877160), -72089226010480.00)

    def test0839(self):
        self.assertEquals(self.calculate(-85529.0, 811375377), -69396124619433.00)

    def test0840(self):
        self.assertEquals(self.calculate(76856.0, 101785689), 7822840913784.00)

    def test0841(self):
        self.assertEquals(self.calculate(161632.0, 1319010981), 213194382880992.00)

    def test0842(self):
        self.assertEquals(self.calculate(139657.0, 1392474973), 194468877304261.00)

    def test0843(self):
        self.assertEquals(self.calculate(-146998.0, -1460655471), 214713432926058.00)

    def test0844(self):
        self.assertEquals(self.calculate(69731.0, -1836678209), -128073408191779.00)

    def test0845(self):
        self.assertEquals(self.calculate(180225.0, -699898703), -126139243748175.00)

    def test0846(self):
        self.assertEquals(self.calculate(140798.0, -998894896), -140642403567008.00)

    def test0847(self):
        self.assertEquals(self.calculate(-149512.0, -412835318), 61723834064816.00)

    def test0848(self):
        self.assertEquals(self.calculate(-129604.0, 1874791570), -242980486638280.00)

    def test0849(self):
        self.assertEquals(self.calculate(178339.0, -381681242), -68068651017038.00)

    def test0850(self):
        self.assertEquals(self.calculate(66665.0, -5162037), -344127196605.00)

    def test0851(self):
        self.assertEquals(self.calculate(-104143.0, 1558388557), -162295259491651.00)

    def test0852(self):
        self.assertEquals(self.calculate(54808.0, -152037407), -8332866202856.00)

    def test0853(self):
        self.assertEquals(self.calculate(-78732.0, 681682277), -53670209032764.00)

    def test0854(self):
        self.assertEquals(self.calculate(171969.0, 1039597344), 178778515650336.00)

    def test0855(self):
        self.assertEquals(self.calculate(144914.0, -6720104), -973837151056.00)

    def test0856(self):
        self.assertEquals(self.calculate(-180721.0, -387932819), 70107606982499.00)

    def test0857(self):
        self.assertEquals(self.calculate(-99490.0, -1144212357), 113837687397930.00)

    def test0858(self):
        self.assertEquals(self.calculate(61963.0, 334894442), 20751064309646.00)

    def test0859(self):
        self.assertEquals(self.calculate(-93515.0, 1947262050), -182098210605750.00)

    def test0860(self):
        self.assertEquals(self.calculate(-76423.0, -1862651906), 142349446612238.00)

    def test0861(self):
        self.assertEquals(self.calculate(43791.0, -1460979250), -63977742336750.00)

    def test0862(self):
        self.assertEquals(self.calculate(-113.0, -537532741), 60741199733.00)

    def test0863(self):
        self.assertEquals(self.calculate(90492.0, -138948343), -12573713454756.00)

    def test0864(self):
        self.assertEquals(self.calculate(-27193.0, -362629192), 9860975618056.00)

    def test0865(self):
        self.assertEquals(self.calculate(118828.0, 1453433792), 172708630635776.00)

    def test0866(self):
        self.assertEquals(self.calculate(184978.0, -1836560360), -339723262272080.00)

    def test0867(self):
        self.assertEquals(self.calculate(-158186.0, -463730412), 73355658952632.00)

    def test0868(self):
        self.assertEquals(self.calculate(-156471.0, -1533417240), 239935328960040.00)

    def test0869(self):
        self.assertEquals(self.calculate(95989.0, -444994042), -42714533097538.00)

    def test0870(self):
        self.assertEquals(self.calculate(-52225.0, 381635410), -19930909287250.00)

    def test0871(self):
        self.assertEquals(self.calculate(-79011.0, -221174253), 17475198903783.00)

    def test0872(self):
        self.assertEquals(self.calculate(142244.0, 2142617538), 304774489075272.00)

    def test0873(self):
        self.assertEquals(self.calculate(-154573.0, -1923540102), 297327364186446.00)

    def test0874(self):
        self.assertEquals(self.calculate(183033.0, 1675099033), 306598401307089.00)

    def test0875(self):
        self.assertEquals(self.calculate(147886.0, -1999095609), -295638253232574.00)

    def test0876(self):
        self.assertEquals(self.calculate(-147896.0, -820821027), 121396146609192.00)

    def test0877(self):
        self.assertEquals(self.calculate(15510.0, 123536541), 1916051750910.00)

    def test0878(self):
        self.assertEquals(self.calculate(-78667.0, 939832987), -73933841588329.00)

    def test0879(self):
        self.assertEquals(self.calculate(-67754.0, 1399601471), -94828598066134.00)

    def test0880(self):
        self.assertEquals(self.calculate(-13042.0, 1668466757), -21760143444794.00)

    def test0881(self):
        self.assertEquals(self.calculate(139758.0, -691944944), -96704841483552.00)

    def test0882(self):
        self.assertEquals(self.calculate(42673.0, -25064787), -1069589655651.00)

    def test0883(self):
        self.assertEquals(self.calculate(92150.0, 1388232027), 127925581288050.00)

    def test0884(self):
        self.assertEquals(self.calculate(-37917.0, -587895660), 22291239740220.00)

    def test0885(self):
        self.assertEquals(self.calculate(-79569.0, 864405970), -68779918626930.00)

    def test0886(self):
        self.assertEquals(self.calculate(143454.0, -1340736823), -192334060206642.00)

    def test0887(self):
        self.assertEquals(self.calculate(-16708.0, -2027236281), 33871063782948.00)

    def test0888(self):
        self.assertEquals(self.calculate(109502.0, 1765162371), 193288809949242.00)

    def test0889(self):
        self.assertEquals(self.calculate(-140808.0, -1301599042), 183275557905936.00)

    def test0890(self):
        self.assertEquals(self.calculate(-123287.0, -1527025074), 188262340298238.00)

    def test0891(self):
        self.assertEquals(self.calculate(-117540.0, -95648846), 11242565358840.00)

    def test0892(self):
        self.assertEquals(self.calculate(30771.0, -1311793145), -40365186864795.00)

    def test0893(self):
        self.assertEquals(self.calculate(185419.0, -1701652422), -315518690434818.00)

    def test0894(self):
        self.assertEquals(self.calculate(57581.0, -1680757996), -96779726167676.00)

    def test0895(self):
        self.assertEquals(self.calculate(36060.0, -1429441616), -51545664672960.00)

    def test0896(self):
        self.assertEquals(self.calculate(-167969.0, -626442271), 105222881817599.00)

    def test0897(self):
        self.assertEquals(self.calculate(132243.0, 2108355398), 278815242897714.00)

    def test0898(self):
        self.assertEquals(self.calculate(29412.0, -1978755061), -58199143854132.00)

    def test0899(self):
        self.assertEquals(self.calculate(-84031.0, 2113228868), -177576735006908.00)

    def test0900(self):
        self.assertEquals(self.calculate(-17005.0, -1523330758), 25904239539790.00)

    def test0901(self):
        self.assertEquals(self.calculate(107686.0, 277086742), 29838362899012.00)

    def test0902(self):
        self.assertEquals(self.calculate(-141735.0, -1488287071), 210942368008185.00)

    def test0903(self):
        self.assertEquals(self.calculate(-143786.0, -188588586), 27116398426596.00)

    def test0904(self):
        self.assertEquals(self.calculate(124607.0, 1725046797), 214952906233779.00)

    def test0905(self):
        self.assertEquals(self.calculate(139463.0, 939672957), 131049609602091.00)

    def test0906(self):
        self.assertEquals(self.calculate(-97580.0, -59520387), 5807999363460.00)

    def test0907(self):
        self.assertEquals(self.calculate(-154855.0, 779453408), -120702257495840.00)

    def test0908(self):
        self.assertEquals(self.calculate(-187488.0, -619026990), 116060132301120.00)

    def test0909(self):
        self.assertEquals(self.calculate(58481.0, 744670653), 43549084458093.00)

    def test0910(self):
        self.assertEquals(self.calculate(-46261.0, -1788466386), 82736243482746.00)

    def test0911(self):
        self.assertEquals(self.calculate(-35454.0, -1222941615), 43358172018210.00)

    def test0912(self):
        self.assertEquals(self.calculate(-9995.0, 756769376), -7563909913120.00)

    def test0913(self):
        self.assertEquals(self.calculate(-185445.0, 253353788), -46983193215660.00)

    def test0914(self):
        self.assertEquals(self.calculate(-186.0, 944852177), -175742504922.00)

    def test0915(self):
        self.assertEquals(self.calculate(-48293.0, 1579579599), -76282637574507.00)

    def test0916(self):
        self.assertEquals(self.calculate(-77697.0, -384358881), 29863531977057.00)

    def test0917(self):
        self.assertEquals(self.calculate(32424.0, 375503380), 12175321593120.00)

    def test0918(self):
        self.assertEquals(self.calculate(39015.0, 935701094), 36506378182410.00)

    def test0919(self):
        self.assertEquals(self.calculate(-40733.0, 1393649160), -56767511234280.00)

    def test0920(self):
        self.assertEquals(self.calculate(165791.0, 179275356), 29722240546596.00)

    def test0921(self):
        self.assertEquals(self.calculate(136224.0, -1222552396), -166540977592704.00)

    def test0922(self):
        self.assertEquals(self.calculate(-23862.0, -1432811112), 34189738754544.00)

    def test0923(self):
        self.assertEquals(self.calculate(-89526.0, -1219426069), 109170338253294.00)

    def test0924(self):
        self.assertEquals(self.calculate(-198857.0, 116648243), -23196319658251.00)

    def test0925(self):
        self.assertEquals(self.calculate(43893.0, 1049621025), 46071015650325.00)

    def test0926(self):
        self.assertEquals(self.calculate(5475.0, -2092101861), -11454257688975.00)

    def test0927(self):
        self.assertEquals(self.calculate(-57214.0, -1510708911), 86433699633954.00)

    def test0928(self):
        self.assertEquals(self.calculate(23729.0, -1811725426), -42990432633554.00)

    def test0929(self):
        self.assertEquals(self.calculate(180631.0, 1349610459), 243781486819629.00)

    def test0930(self):
        self.assertEquals(self.calculate(94956.0, 1787617975), 169745052434100.00)

    def test0931(self):
        self.assertEquals(self.calculate(-154843.0, -2117208971), 327834988696553.00)

    def test0932(self):
        self.assertEquals(self.calculate(-74072.0, 1827245015), -135347692751080.00)

    def test0933(self):
        self.assertEquals(self.calculate(65981.0, -1175843349), -77583320010369.00)

    def test0934(self):
        self.assertEquals(self.calculate(-49824.0, 171888582), -8564176709568.00)

    def test0935(self):
        self.assertEquals(self.calculate(-128880.0, 759178004), -97842861155520.00)

    def test0936(self):
        self.assertEquals(self.calculate(167721.0, 530739231), 89016114562551.00)

    def test0937(self):
        self.assertEquals(self.calculate(-83194.0, -747255775), 62167196945350.00)

    def test0938(self):
        self.assertEquals(self.calculate(136832.0, -2065827381), -282671292196992.00)

    def test0939(self):
        self.assertEquals(self.calculate(-15460.0, 110369861), -1706318051060.00)

    def test0940(self):
        self.assertEquals(self.calculate(36558.0, -801389845), -29297209953510.00)

    def test0941(self):
        self.assertEquals(self.calculate(51772.0, -2013309858), -104233077968376.00)

    def test0942(self):
        self.assertEquals(self.calculate(-106223.0, -786023860), 83493812480780.00)

    def test0943(self):
        self.assertEquals(self.calculate(-174950.0, 1705707024), -298413443848800.00)

    def test0944(self):
        self.assertEquals(self.calculate(-9428.0, 53044462), -500103187736.00)

    def test0945(self):
        self.assertEquals(self.calculate(187661.0, -1998933060), -375121776972660.00)

    def test0946(self):
        self.assertEquals(self.calculate(113221.0, -1174769734), -133008604053214.00)

    def test0947(self):
        self.assertEquals(self.calculate(144408.0, -288041308), -41595469205664.00)

    def test0948(self):
        self.assertEquals(self.calculate(-79834.0, 730318281), -58304229645354.00)

    def test0949(self):
        self.assertEquals(self.calculate(142006.0, -1658508674), -235518182760044.00)

    def test0950(self):
        self.assertEquals(self.calculate(-55907.0, -754029839), 42155546208973.00)

    def test0951(self):
        self.assertEquals(self.calculate(118621.0, 2077038271), 246380356744291.00)

    def test0952(self):
        self.assertEquals(self.calculate(-37351.0, 1539009149), -57483530724299.00)

    def test0953(self):
        self.assertEquals(self.calculate(-57849.0, -2001555132), 115787962831068.00)

    def test0954(self):
        self.assertEquals(self.calculate(106038.0, 961639701), 101970350614638.00)

    def test0955(self):
        self.assertEquals(self.calculate(-172160.0, -1516385175), 261060871728000.00)

    def test0956(self):
        self.assertEquals(self.calculate(-14311.0, -59954048), 858002380928.00)

    def test0957(self):
        self.assertEquals(self.calculate(-141781.0, 1809832996), -256599932005876.00)

    def test0958(self):
        self.assertEquals(self.calculate(-74142.0, 500010425), -37071772930350.00)

    def test0959(self):
        self.assertEquals(self.calculate(-151123.0, 620462551), -93766162094773.00)

    def test0960(self):
        self.assertEquals(self.calculate(170111.0, 239561926), 40752118793786.00)

    def test0961(self):
        self.assertEquals(self.calculate(67034.0, 1306421327), 87574647234118.00)

    def test0962(self):
        self.assertEquals(self.calculate(104352.0, 512722763), 53503645764576.00)

    def test0963(self):
        self.assertEquals(self.calculate(-50077.0, 1992769912), -99791938883224.00)

    def test0964(self):
        self.assertEquals(self.calculate(-172318.0, -287902477), 49610779031686.00)

    def test0965(self):
        self.assertEquals(self.calculate(-197913.0, -1974295054), 390738657022302.00)

    def test0966(self):
        self.assertEquals(self.calculate(-53650.0, 1486991378), -79777087429700.00)

    def test0967(self):
        self.assertEquals(self.calculate(180836.0, -1008546927), -182381592090972.00)

    def test0968(self):
        self.assertEquals(self.calculate(32992.0, -1329283784), -43855730601728.00)

    def test0969(self):
        self.assertEquals(self.calculate(80312.0, 1119436640), 89904195431680.00)

    def test0970(self):
        self.assertEquals(self.calculate(-175942.0, -700729324), 123287718723208.00)

    def test0971(self):
        self.assertEquals(self.calculate(-160249.0, 1703846114), -273039635922386.00)

    def test0972(self):
        self.assertEquals(self.calculate(-45870.0, 2010640336), -92228072212320.00)

    def test0973(self):
        self.assertEquals(self.calculate(21568.0, -1361913217), -29373744264256.00)

    def test0974(self):
        self.assertEquals(self.calculate(-36944.0, 1957779007), -72328187634608.00)

    def test0975(self):
        self.assertEquals(self.calculate(105130.0, -1223362841), -128612135474330.00)

    def test0976(self):
        self.assertEquals(self.calculate(-81916.0, 232528976), -19047843598016.00)

    def test0977(self):
        self.assertEquals(self.calculate(-98112.0, -1681604923), 164985622205376.00)

    def test0978(self):
        self.assertEquals(self.calculate(-30588.0, -358581713), 10968297437244.00)

    def test0979(self):
        self.assertEquals(self.calculate(143469.0, -1313465853), -188441632464057.00)

    def test0980(self):
        self.assertEquals(self.calculate(-9922.0, 1552602241), -15404919435202.00)

    def test0981(self):
        self.assertEquals(self.calculate(64540.0, 2137655321), 137964274417340.00)

    def test0982(self):
        self.assertEquals(self.calculate(136940.0, -659794577), -90352269374380.00)

    def test0983(self):
        self.assertEquals(self.calculate(-112881.0, -1335155931), 150713736647211.00)

    def test0984(self):
        self.assertEquals(self.calculate(-89713.0, 62414064), -5599352923632.00)

    def test0985(self):
        self.assertEquals(self.calculate(-42613.0, -986173148), 42023796355724.00)

    def test0986(self):
        self.assertEquals(self.calculate(-196503.0, -1451828247), 285288606020241.00)

    def test0987(self):
        self.assertEquals(self.calculate(-43683.0, -1504230390), 65709296126370.00)

    def test0988(self):
        self.assertEquals(self.calculate(-65154.0, -35176186), 2291869222644.00)

    def test0989(self):
        self.assertEquals(self.calculate(-159634.0, -991634189), 158298532126826.00)

    def test0990(self):
        self.assertEquals(self.calculate(-9150.0, -1674580632), 15322412782800.00)

    def test0991(self):
        self.assertEquals(self.calculate(68986.0, -85539611), -5901035604446.00)

    def test0992(self):
        self.assertEquals(self.calculate(115245.0, 837949692), 96569512254540.00)

    def test0993(self):
        self.assertEquals(self.calculate(-110568.0, -2016324711), 222940990645848.00)

    def test0994(self):
        self.assertEquals(self.calculate(110885.0, 580181727), 64333450798395.00)

    def test0995(self):
        self.assertEquals(self.calculate(100384.0, -1888111486), -189536183410624.00)

    def test0996(self):
        self.assertEquals(self.calculate(116889.0, 848451557), 99174654046173.00)

    def test0997(self):
        self.assertEquals(self.calculate(120253.0, 1387932105), 166902999422565.00)

    def test0998(self):
        self.assertEquals(self.calculate(73715.0, -677025909), -49906964881935.00)

    def test0999(self):
        self.assertEquals(self.calculate(-134643.0, -188479387), 25377430103841.00)

    def test1000(self):
        self.assertEquals(self.calculate(172900.0, 1347793978), 233033578796200.00)

    def test1001(self):
        self.assertEquals(self.calculate(-56810.0, 982031789), -55789225933090.00)

    def test1002(self):
        self.assertEquals(self.calculate(95746.0, -1673123932), -160194923993272.00)

    def test1003(self):
        self.assertEquals(self.calculate(65954.0, -1677560942), -110641854368668.00)

    def test1004(self):
        self.assertEquals(self.calculate(-10669.0, 1298726376), -13856111705544.00)

    def test1005(self):
        self.assertEquals(self.calculate(69151.0, -1730811654), -119687356685754.00)

    def test1006(self):
        self.assertEquals(self.calculate(36610.0, -2086952373), -76403326375530.00)

    def test1007(self):
        self.assertEquals(self.calculate(-110102.0, 906839577), -99844851106854.00)

    def test1008(self):
        self.assertEquals(self.calculate(-145314.0, 121363506), -17635816510884.00)

    def test1009(self):
        self.assertEquals(self.calculate(-162877.0, -980087497), 159633711248869.00)

    def test1010(self):
        self.assertEquals(self.calculate(150987.0, -516982074), -78057572407038.00)

    def test1011(self):
        self.assertEquals(self.calculate(-196585.0, -1378598487), 271011783566895.00)

    def test1012(self):
        self.assertEquals(self.calculate(-32319.0, 1095655866), -35410501933254.00)

    def test1013(self):
        self.assertEquals(self.calculate(-93323.0, 882969834), -82401393818382.00)

    def test1014(self):
        self.assertEquals(self.calculate(-154935.0, 1102176476), -170765712309060.00)

    def test1015(self):
        self.assertEquals(self.calculate(16240.0, 1390769298), 22586093399520.00)

    def test1016(self):
        self.assertEquals(self.calculate(27415.0, -36189554), -992136622910.00)

    def test1017(self):
        self.assertEquals(self.calculate(34996.0, -2074169862), -72587648490552.00)

    def test1018(self):
        self.assertEquals(self.calculate(-65740.0, -866342496), 56953355687040.00)

    def test1019(self):
        self.assertEquals(self.calculate(-75256.0, 1786166364), -134419735889184.00)

    def test1020(self):
        self.assertEquals(self.calculate(113409.0, -1959586224), -222234714077616.00)

    def test1021(self):
        self.assertEquals(self.calculate(48754.0, 68341805), 3331936360970.00)

    def test1022(self):
        self.assertEquals(self.calculate(-26495.0, -1668232149), 44199810787755.00)

    def test1023(self):
        self.assertEquals(self.calculate(189524.0, -903107910), -171160623534840.00)



class TestVM_Mul_FloatFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushF(rhs)
        v.VM_Mul()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(137118.0, 22957.0), 3147817926.00)

    def test0001(self):
        self.assertEquals(self.calculate(-136376.0, -69794.0), 9518226544.00)

    def test0002(self):
        self.assertEquals(self.calculate(54460.0, -35952.0), -1957945920.00)

    def test0003(self):
        self.assertEquals(self.calculate(-140576.0, 11593.0), -1629697568.00)

    def test0004(self):
        self.assertEquals(self.calculate(96648.0, 71008.0), 6862781184.00)

    def test0005(self):
        self.assertEquals(self.calculate(173866.0, 140100.0), 24358626600.00)

    def test0006(self):
        self.assertEquals(self.calculate(80867.0, 172736.0), 13968642112.00)

    def test0007(self):
        self.assertEquals(self.calculate(-134904.0, -112498.0), 15176430192.00)

    def test0008(self):
        self.assertEquals(self.calculate(142495.0, -50784.0), -7236466080.00)

    def test0009(self):
        self.assertEquals(self.calculate(9789.0, -167535.0), -1640000115.00)

    def test0010(self):
        self.assertEquals(self.calculate(-191619.0, -83249.0), 15952090131.00)

    def test0011(self):
        self.assertEquals(self.calculate(177562.0, 124953.0), 22186904586.00)

    def test0012(self):
        self.assertEquals(self.calculate(-69105.0, 95898.0), -6627031290.00)

    def test0013(self):
        self.assertEquals(self.calculate(31562.0, 29865.0), 942599130.00)

    def test0014(self):
        self.assertEquals(self.calculate(15467.0, -164171.0), -2539232857.00)

    def test0015(self):
        self.assertEquals(self.calculate(11243.0, -148180.0), -1665987740.00)

    def test0016(self):
        self.assertEquals(self.calculate(-30465.0, -19617.0), 597631905.00)

    def test0017(self):
        self.assertEquals(self.calculate(-44211.0, 123020.0), -5438837220.00)

    def test0018(self):
        self.assertEquals(self.calculate(-177629.0, 84799.0), -15062761571.00)

    def test0019(self):
        self.assertEquals(self.calculate(185814.0, -168380.0), -31287361320.00)

    def test0020(self):
        self.assertEquals(self.calculate(-173846.0, -86597.0), 15054542062.00)

    def test0021(self):
        self.assertEquals(self.calculate(121248.0, 62619.0), 7592428512.00)

    def test0022(self):
        self.assertEquals(self.calculate(72972.0, 36211.0), 2642389092.00)

    def test0023(self):
        self.assertEquals(self.calculate(-114185.0, -80448.0), 9185954880.00)

    def test0024(self):
        self.assertEquals(self.calculate(96187.0, 191900.0), 18458285300.00)

    def test0025(self):
        self.assertEquals(self.calculate(93784.0, 153173.0), 14365176632.00)

    def test0026(self):
        self.assertEquals(self.calculate(-28200.0, -67708.0), 1909365600.00)

    def test0027(self):
        self.assertEquals(self.calculate(31183.0, 103617.0), 3231088911.00)

    def test0028(self):
        self.assertEquals(self.calculate(30031.0, 195987.0), 5885685597.00)

    def test0029(self):
        self.assertEquals(self.calculate(17655.0, 17179.0), 303295245.00)

    def test0030(self):
        self.assertEquals(self.calculate(30805.0, 101743.0), 3134193115.00)

    def test0031(self):
        self.assertEquals(self.calculate(163344.0, 91218.0), 14899912992.00)

    def test0032(self):
        self.assertEquals(self.calculate(127303.0, 188077.0), 23942766331.00)

    def test0033(self):
        self.assertEquals(self.calculate(-21691.0, 194475.0), -4218357225.00)

    def test0034(self):
        self.assertEquals(self.calculate(-140186.0, 129541.0), -18159834626.00)

    def test0035(self):
        self.assertEquals(self.calculate(21532.0, 183583.0), 3952909156.00)

    def test0036(self):
        self.assertEquals(self.calculate(-88056.0, -182721.0), 16089680376.00)

    def test0037(self):
        self.assertEquals(self.calculate(-113290.0, 175765.0), -19912416850.00)

    def test0038(self):
        self.assertEquals(self.calculate(48543.0, -22659.0), -1099935837.00)

    def test0039(self):
        self.assertEquals(self.calculate(86497.0, -59787.0), -5171396139.00)

    def test0040(self):
        self.assertEquals(self.calculate(169285.0, 176704.0), 29913336640.00)

    def test0041(self):
        self.assertEquals(self.calculate(116990.0, 197073.0), 23055570270.00)

    def test0042(self):
        self.assertEquals(self.calculate(-183995.0, -16097.0), 2961767515.00)

    def test0043(self):
        self.assertEquals(self.calculate(-60873.0, 87373.0), -5318656629.00)

    def test0044(self):
        self.assertEquals(self.calculate(67140.0, 176207.0), 11830537980.00)

    def test0045(self):
        self.assertEquals(self.calculate(29582.0, -99109.0), -2931842438.00)

    def test0046(self):
        self.assertEquals(self.calculate(-41359.0, -119903.0), 4959068177.00)

    def test0047(self):
        self.assertEquals(self.calculate(-160833.0, -12514.0), 2012664162.00)

    def test0048(self):
        self.assertEquals(self.calculate(91644.0, -109215.0), -10008899460.00)

    def test0049(self):
        self.assertEquals(self.calculate(48145.0, 134853.0), 6492497685.00)

    def test0050(self):
        self.assertEquals(self.calculate(-100173.0, -183555.0), 18387255015.00)

    def test0051(self):
        self.assertEquals(self.calculate(-71787.0, 18539.0), -1330859193.00)

    def test0052(self):
        self.assertEquals(self.calculate(185507.0, 112817.0), 20928343219.00)

    def test0053(self):
        self.assertEquals(self.calculate(3837.0, 143987.0), 552478119.00)

    def test0054(self):
        self.assertEquals(self.calculate(41325.0, 162538.0), 6716882850.00)

    def test0055(self):
        self.assertEquals(self.calculate(96251.0, -113377.0), -10912649627.00)

    def test0056(self):
        self.assertEquals(self.calculate(218.0, -3453.0), -752754.00)

    def test0057(self):
        self.assertEquals(self.calculate(-106524.0, -123430.0), 13148257320.00)

    def test0058(self):
        self.assertEquals(self.calculate(99572.0, -47185.0), -4698304820.00)

    def test0059(self):
        self.assertEquals(self.calculate(197610.0, -72989.0), -14423356290.00)

    def test0060(self):
        self.assertEquals(self.calculate(-116752.0, 69417.0), -8104573584.00)

    def test0061(self):
        self.assertEquals(self.calculate(31819.0, 31321.0), 996602899.00)

    def test0062(self):
        self.assertEquals(self.calculate(98692.0, 121194.0), 11960878248.00)

    def test0063(self):
        self.assertEquals(self.calculate(124820.0, 56492.0), 7051331440.00)

    def test0064(self):
        self.assertEquals(self.calculate(161303.0, 189455.0), 30559659865.00)

    def test0065(self):
        self.assertEquals(self.calculate(-25134.0, -187866.0), 4721824044.00)

    def test0066(self):
        self.assertEquals(self.calculate(-129829.0, 102890.0), -13358105810.00)

    def test0067(self):
        self.assertEquals(self.calculate(-43666.0, -67156.0), 2932433896.00)

    def test0068(self):
        self.assertEquals(self.calculate(39112.0, -25351.0), -991528312.00)

    def test0069(self):
        self.assertEquals(self.calculate(174139.0, -69786.0), -12152464254.00)

    def test0070(self):
        self.assertEquals(self.calculate(164540.0, -34907.0), -5743597780.00)

    def test0071(self):
        self.assertEquals(self.calculate(191828.0, -18803.0), -3606941884.00)

    def test0072(self):
        self.assertEquals(self.calculate(-84725.0, -53028.0), 4492797300.00)

    def test0073(self):
        self.assertEquals(self.calculate(68902.0, 85018.0), 5857910236.00)

    def test0074(self):
        self.assertEquals(self.calculate(-115021.0, -15526.0), 1785816046.00)

    def test0075(self):
        self.assertEquals(self.calculate(-55724.0, -87101.0), 4853616124.00)

    def test0076(self):
        self.assertEquals(self.calculate(-158481.0, -14669.0), 2324757789.00)

    def test0077(self):
        self.assertEquals(self.calculate(122368.0, 198570.0), 24298613760.00)

    def test0078(self):
        self.assertEquals(self.calculate(-109421.0, -166521.0), 18220894341.00)

    def test0079(self):
        self.assertEquals(self.calculate(-105223.0, -93927.0), 9883280721.00)

    def test0080(self):
        self.assertEquals(self.calculate(186664.0, 161051.0), 30062423864.00)

    def test0081(self):
        self.assertEquals(self.calculate(-120284.0, -31271.0), 3761400964.00)

    def test0082(self):
        self.assertEquals(self.calculate(-45872.0, 98251.0), -4506969872.00)

    def test0083(self):
        self.assertEquals(self.calculate(-51473.0, 166327.0), -8561349671.00)

    def test0084(self):
        self.assertEquals(self.calculate(-90975.0, 143845.0), -13086298875.00)

    def test0085(self):
        self.assertEquals(self.calculate(-138997.0, 147538.0), -20507339386.00)

    def test0086(self):
        self.assertEquals(self.calculate(-148163.0, 141813.0), -21011439519.00)

    def test0087(self):
        self.assertEquals(self.calculate(-90957.0, -183596.0), 16699341372.00)

    def test0088(self):
        self.assertEquals(self.calculate(-185755.0, -125368.0), 23287732840.00)

    def test0089(self):
        self.assertEquals(self.calculate(183009.0, -39879.0), -7298215911.00)

    def test0090(self):
        self.assertEquals(self.calculate(-100709.0, 142716.0), -14372785644.00)

    def test0091(self):
        self.assertEquals(self.calculate(148981.0, 92299.0), 13750797319.00)

    def test0092(self):
        self.assertEquals(self.calculate(-194565.0, -195565.0), 38050104225.00)

    def test0093(self):
        self.assertEquals(self.calculate(189016.0, 298.0), 56326768.00)

    def test0094(self):
        self.assertEquals(self.calculate(-102091.0, -85651.0), 8744196241.00)

    def test0095(self):
        self.assertEquals(self.calculate(-166347.0, -100281.0), 16681443507.00)

    def test0096(self):
        self.assertEquals(self.calculate(-106665.0, -65406.0), 6976530990.00)

    def test0097(self):
        self.assertEquals(self.calculate(-152288.0, -13082.0), 1992231616.00)

    def test0098(self):
        self.assertEquals(self.calculate(199354.0, -19835.0), -3954186590.00)

    def test0099(self):
        self.assertEquals(self.calculate(134650.0, 32085.0), 4320245250.00)

    def test0100(self):
        self.assertEquals(self.calculate(-108509.0, -46184.0), 5011379656.00)

    def test0101(self):
        self.assertEquals(self.calculate(43914.0, -115367.0), -5066226438.00)

    def test0102(self):
        self.assertEquals(self.calculate(45425.0, -51956.0), -2360101300.00)

    def test0103(self):
        self.assertEquals(self.calculate(33631.0, -22641.0), -761439471.00)

    def test0104(self):
        self.assertEquals(self.calculate(72665.0, -137293.0), -9976395845.00)

    def test0105(self):
        self.assertEquals(self.calculate(-103045.0, 142366.0), -14670104470.00)

    def test0106(self):
        self.assertEquals(self.calculate(33563.0, 36718.0), 1232366234.00)

    def test0107(self):
        self.assertEquals(self.calculate(6322.0, -155442.0), -982704324.00)

    def test0108(self):
        self.assertEquals(self.calculate(-67902.0, 190048.0), -12904639296.00)

    def test0109(self):
        self.assertEquals(self.calculate(164941.0, 2392.0), 394538872.00)

    def test0110(self):
        self.assertEquals(self.calculate(85852.0, -99346.0), -8529052792.00)

    def test0111(self):
        self.assertEquals(self.calculate(145292.0, -69901.0), -10156056092.00)

    def test0112(self):
        self.assertEquals(self.calculate(69334.0, 153822.0), 10665094548.00)

    def test0113(self):
        self.assertEquals(self.calculate(-195443.0, -76336.0), 14919336848.00)

    def test0114(self):
        self.assertEquals(self.calculate(-141107.0, -144836.0), 20437373452.00)

    def test0115(self):
        self.assertEquals(self.calculate(42775.0, -56236.0), -2405494900.00)

    def test0116(self):
        self.assertEquals(self.calculate(12043.0, 72323.0), 870985889.00)

    def test0117(self):
        self.assertEquals(self.calculate(130389.0, -4741.0), -618174249.00)

    def test0118(self):
        self.assertEquals(self.calculate(-158711.0, 15020.0), -2383839220.00)

    def test0119(self):
        self.assertEquals(self.calculate(178306.0, -41448.0), -7390427088.00)

    def test0120(self):
        self.assertEquals(self.calculate(-80046.0, 79737.0), -6382627902.00)

    def test0121(self):
        self.assertEquals(self.calculate(-163810.0, 113585.0), -18606358850.00)

    def test0122(self):
        self.assertEquals(self.calculate(-121402.0, -22331.0), 2711028062.00)

    def test0123(self):
        self.assertEquals(self.calculate(11696.0, 11050.0), 129240800.00)

    def test0124(self):
        self.assertEquals(self.calculate(-27964.0, -41422.0), 1158324808.00)

    def test0125(self):
        self.assertEquals(self.calculate(-186193.0, 185017.0), -34448870281.00)

    def test0126(self):
        self.assertEquals(self.calculate(133677.0, 143427.0), 19172891079.00)

    def test0127(self):
        self.assertEquals(self.calculate(-176013.0, -61545.0), 10832720085.00)

    def test0128(self):
        self.assertEquals(self.calculate(36553.0, -163213.0), -5965924789.00)

    def test0129(self):
        self.assertEquals(self.calculate(-90932.0, -91828.0), 8350103696.00)

    def test0130(self):
        self.assertEquals(self.calculate(-98294.0, -155343.0), 15269284842.00)

    def test0131(self):
        self.assertEquals(self.calculate(-12724.0, 112266.0), -1428472584.00)

    def test0132(self):
        self.assertEquals(self.calculate(160021.0, -148442.0), -23753837282.00)

    def test0133(self):
        self.assertEquals(self.calculate(-138181.0, 109166.0), -15084667046.00)

    def test0134(self):
        self.assertEquals(self.calculate(22011.0, 6946.0), 152888406.00)

    def test0135(self):
        self.assertEquals(self.calculate(-124101.0, 153307.0), -19025552007.00)

    def test0136(self):
        self.assertEquals(self.calculate(181740.0, -180250.0), -32758635000.00)

    def test0137(self):
        self.assertEquals(self.calculate(-60044.0, -145423.0), 8731778612.00)

    def test0138(self):
        self.assertEquals(self.calculate(70364.0, -72418.0), -5095620152.00)

    def test0139(self):
        self.assertEquals(self.calculate(28715.0, -149447.0), -4291370605.00)

    def test0140(self):
        self.assertEquals(self.calculate(68964.0, 121533.0), 8381401812.00)

    def test0141(self):
        self.assertEquals(self.calculate(145453.0, -171058.0), -24880899274.00)

    def test0142(self):
        self.assertEquals(self.calculate(-194862.0, -21102.0), 4111977924.00)

    def test0143(self):
        self.assertEquals(self.calculate(-112479.0, -174314.0), 19606664406.00)

    def test0144(self):
        self.assertEquals(self.calculate(5108.0, 32408.0), 165540064.00)

    def test0145(self):
        self.assertEquals(self.calculate(-173991.0, 110404.0), -19209302364.00)

    def test0146(self):
        self.assertEquals(self.calculate(191515.0, -194383.0), -37227260245.00)

    def test0147(self):
        self.assertEquals(self.calculate(9486.0, -37677.0), -357404022.00)

    def test0148(self):
        self.assertEquals(self.calculate(-73590.0, -150368.0), 11065581120.00)

    def test0149(self):
        self.assertEquals(self.calculate(199376.0, 155384.0), 30979840384.00)

    def test0150(self):
        self.assertEquals(self.calculate(94568.0, -71069.0), -6720853192.00)

    def test0151(self):
        self.assertEquals(self.calculate(-43850.0, -87296.0), 3827929600.00)

    def test0152(self):
        self.assertEquals(self.calculate(-46808.0, -44571.0), 2086279368.00)

    def test0153(self):
        self.assertEquals(self.calculate(-179752.0, -94812.0), 17042646624.00)

    def test0154(self):
        self.assertEquals(self.calculate(-114300.0, -151260.0), 17289018000.00)

    def test0155(self):
        self.assertEquals(self.calculate(35018.0, 112604.0), 3943166872.00)

    def test0156(self):
        self.assertEquals(self.calculate(-153588.0, -39592.0), 6080856096.00)

    def test0157(self):
        self.assertEquals(self.calculate(-56571.0, 158826.0), -8984945646.00)

    def test0158(self):
        self.assertEquals(self.calculate(-173995.0, 118294.0), -20582564530.00)

    def test0159(self):
        self.assertEquals(self.calculate(174761.0, 100229.0), 17516120269.00)

    def test0160(self):
        self.assertEquals(self.calculate(-77455.0, 38474.0), -2980003670.00)

    def test0161(self):
        self.assertEquals(self.calculate(90842.0, -188056.0), -17083383152.00)

    def test0162(self):
        self.assertEquals(self.calculate(145913.0, -75995.0), -11088658435.00)

    def test0163(self):
        self.assertEquals(self.calculate(-90419.0, 50028.0), -4523481732.00)

    def test0164(self):
        self.assertEquals(self.calculate(58734.0, -113445.0), -6663078630.00)

    def test0165(self):
        self.assertEquals(self.calculate(83650.0, -145562.0), -12176261300.00)

    def test0166(self):
        self.assertEquals(self.calculate(-47124.0, -31246.0), 1472436504.00)

    def test0167(self):
        self.assertEquals(self.calculate(-3685.0, 138343.0), -509793955.00)

    def test0168(self):
        self.assertEquals(self.calculate(145836.0, -183480.0), -26757989280.00)

    def test0169(self):
        self.assertEquals(self.calculate(15484.0, -29004.0), -449097936.00)

    def test0170(self):
        self.assertEquals(self.calculate(-180476.0, 195971.0), -35368062196.00)

    def test0171(self):
        self.assertEquals(self.calculate(-91563.0, -66439.0), 6083354157.00)

    def test0172(self):
        self.assertEquals(self.calculate(-115949.0, -20260.0), 2349126740.00)

    def test0173(self):
        self.assertEquals(self.calculate(80402.0, 77163.0), 6204059526.00)

    def test0174(self):
        self.assertEquals(self.calculate(-42937.0, 93271.0), -4004776927.00)

    def test0175(self):
        self.assertEquals(self.calculate(-144497.0, -116468.0), 16829276596.00)

    def test0176(self):
        self.assertEquals(self.calculate(-14127.0, 25056.0), -353966112.00)

    def test0177(self):
        self.assertEquals(self.calculate(199828.0, 123145.0), 24607819060.00)

    def test0178(self):
        self.assertEquals(self.calculate(192492.0, -41000.0), -7892172000.00)

    def test0179(self):
        self.assertEquals(self.calculate(-127893.0, -166840.0), 21337668120.00)

    def test0180(self):
        self.assertEquals(self.calculate(-100397.0, -137412.0), 13795752564.00)

    def test0181(self):
        self.assertEquals(self.calculate(88968.0, 56910.0), 5063168880.00)

    def test0182(self):
        self.assertEquals(self.calculate(150719.0, 66206.0), 9978502114.00)

    def test0183(self):
        self.assertEquals(self.calculate(132424.0, 37896.0), 5018339904.00)

    def test0184(self):
        self.assertEquals(self.calculate(-42244.0, 114475.0), -4835881900.00)

    def test0185(self):
        self.assertEquals(self.calculate(-65420.0, 88888.0), -5815052960.00)

    def test0186(self):
        self.assertEquals(self.calculate(-2904.0, 116190.0), -337415760.00)

    def test0187(self):
        self.assertEquals(self.calculate(4447.0, 11666.0), 51878702.00)

    def test0188(self):
        self.assertEquals(self.calculate(-78147.0, -90928.0), 7105750416.00)

    def test0189(self):
        self.assertEquals(self.calculate(-146533.0, 12699.0), -1860822567.00)

    def test0190(self):
        self.assertEquals(self.calculate(114251.0, 154042.0), 17599452542.00)

    def test0191(self):
        self.assertEquals(self.calculate(114130.0, 99931.0), 11405125030.00)

    def test0192(self):
        self.assertEquals(self.calculate(76136.0, 52526.0), 3999119536.00)

    def test0193(self):
        self.assertEquals(self.calculate(144598.0, 125716.0), 18178282168.00)

    def test0194(self):
        self.assertEquals(self.calculate(171873.0, -149129.0), -25631248617.00)

    def test0195(self):
        self.assertEquals(self.calculate(-192618.0, -62357.0), 12011080626.00)

    def test0196(self):
        self.assertEquals(self.calculate(-192783.0, 192894.0), -37186684002.00)

    def test0197(self):
        self.assertEquals(self.calculate(-72327.0, -198851.0), 14382296277.00)

    def test0198(self):
        self.assertEquals(self.calculate(-132208.0, -115248.0), 15236707584.00)

    def test0199(self):
        self.assertEquals(self.calculate(-21419.0, 111059.0), -2378772721.00)

    def test0200(self):
        self.assertEquals(self.calculate(9452.0, -165739.0), -1566565028.00)

    def test0201(self):
        self.assertEquals(self.calculate(84472.0, 193810.0), 16371518320.00)

    def test0202(self):
        self.assertEquals(self.calculate(194131.0, 63683.0), 12362844473.00)

    def test0203(self):
        self.assertEquals(self.calculate(-42820.0, 44172.0), -1891445040.00)

    def test0204(self):
        self.assertEquals(self.calculate(-43791.0, -86201.0), 3774827991.00)

    def test0205(self):
        self.assertEquals(self.calculate(43479.0, 7582.0), 329657778.00)

    def test0206(self):
        self.assertEquals(self.calculate(1407.0, 37920.0), 53353440.00)

    def test0207(self):
        self.assertEquals(self.calculate(-92599.0, 151379.0), -14017544021.00)

    def test0208(self):
        self.assertEquals(self.calculate(144819.0, 18701.0), 2708260119.00)

    def test0209(self):
        self.assertEquals(self.calculate(155432.0, -24650.0), -3831398800.00)

    def test0210(self):
        self.assertEquals(self.calculate(-42594.0, -128419.0), 5469878886.00)

    def test0211(self):
        self.assertEquals(self.calculate(7592.0, -137675.0), -1045228600.00)

    def test0212(self):
        self.assertEquals(self.calculate(-118102.0, 62846.0), -7422238292.00)

    def test0213(self):
        self.assertEquals(self.calculate(-59548.0, -53228.0), 3169620944.00)

    def test0214(self):
        self.assertEquals(self.calculate(28631.0, -30087.0), -861420897.00)

    def test0215(self):
        self.assertEquals(self.calculate(-192782.0, 12158.0), -2343843556.00)

    def test0216(self):
        self.assertEquals(self.calculate(36936.0, 1541.0), 56918376.00)

    def test0217(self):
        self.assertEquals(self.calculate(37385.0, -87000.0), -3252495000.00)

    def test0218(self):
        self.assertEquals(self.calculate(71618.0, -182747.0), -13087974646.00)

    def test0219(self):
        self.assertEquals(self.calculate(-115559.0, -73132.0), 8451060788.00)

    def test0220(self):
        self.assertEquals(self.calculate(134784.0, 56382.0), 7599391488.00)

    def test0221(self):
        self.assertEquals(self.calculate(-171391.0, -155398.0), 26633818618.00)

    def test0222(self):
        self.assertEquals(self.calculate(-61105.0, 159732.0), -9760423860.00)

    def test0223(self):
        self.assertEquals(self.calculate(-3307.0, 186221.0), -615832847.00)

    def test0224(self):
        self.assertEquals(self.calculate(25224.0, -96093.0), -2423849832.00)

    def test0225(self):
        self.assertEquals(self.calculate(-26462.0, -28728.0), 760200336.00)

    def test0226(self):
        self.assertEquals(self.calculate(-193440.0, -84169.0), 16281651360.00)

    def test0227(self):
        self.assertEquals(self.calculate(-191022.0, 194809.0), -37212804798.00)

    def test0228(self):
        self.assertEquals(self.calculate(-19118.0, -31057.0), 593747726.00)

    def test0229(self):
        self.assertEquals(self.calculate(159324.0, -73371.0), -11689761204.00)

    def test0230(self):
        self.assertEquals(self.calculate(193056.0, 36056.0), 6960827136.00)

    def test0231(self):
        self.assertEquals(self.calculate(2329.0, 166114.0), 386879506.00)

    def test0232(self):
        self.assertEquals(self.calculate(13199.0, -199574.0), -2634177226.00)

    def test0233(self):
        self.assertEquals(self.calculate(24870.0, 11269.0), 280260030.00)

    def test0234(self):
        self.assertEquals(self.calculate(152692.0, -28374.0), -4332482808.00)

    def test0235(self):
        self.assertEquals(self.calculate(-64131.0, -194049.0), 12444556419.00)

    def test0236(self):
        self.assertEquals(self.calculate(118156.0, -192260.0), -22716672560.00)

    def test0237(self):
        self.assertEquals(self.calculate(178048.0, -171044.0), -30454042112.00)

    def test0238(self):
        self.assertEquals(self.calculate(26672.0, -73033.0), -1947936176.00)

    def test0239(self):
        self.assertEquals(self.calculate(25123.0, -135908.0), -3414416684.00)

    def test0240(self):
        self.assertEquals(self.calculate(130436.0, 11998.0), 1564971128.00)

    def test0241(self):
        self.assertEquals(self.calculate(184637.0, -53731.0), -9920730647.00)

    def test0242(self):
        self.assertEquals(self.calculate(54651.0, -100791.0), -5508328941.00)

    def test0243(self):
        self.assertEquals(self.calculate(-107882.0, -14989.0), 1617043298.00)

    def test0244(self):
        self.assertEquals(self.calculate(134926.0, -112802.0), -15219922652.00)

    def test0245(self):
        self.assertEquals(self.calculate(147390.0, 85205.0), 12558364950.00)

    def test0246(self):
        self.assertEquals(self.calculate(138899.0, -76912.0), -10682999888.00)

    def test0247(self):
        self.assertEquals(self.calculate(83431.0, 109547.0), 9139615757.00)

    def test0248(self):
        self.assertEquals(self.calculate(-157741.0, -144451.0), 22785845191.00)

    def test0249(self):
        self.assertEquals(self.calculate(99627.0, -151319.0), -15075458013.00)

    def test0250(self):
        self.assertEquals(self.calculate(104062.0, -33413.0), -3477023606.00)

    def test0251(self):
        self.assertEquals(self.calculate(172471.0, -37426.0), -6454899646.00)

    def test0252(self):
        self.assertEquals(self.calculate(-132766.0, 109401.0), -14524733166.00)

    def test0253(self):
        self.assertEquals(self.calculate(85854.0, -53673.0), -4608041742.00)

    def test0254(self):
        self.assertEquals(self.calculate(191243.0, -132753.0), -25388081979.00)

    def test0255(self):
        self.assertEquals(self.calculate(-197850.0, -188425.0), 37279886250.00)

    def test0256(self):
        self.assertEquals(self.calculate(-88823.0, -33041.0), 2934800743.00)

    def test0257(self):
        self.assertEquals(self.calculate(182602.0, 98553.0), 17995974906.00)

    def test0258(self):
        self.assertEquals(self.calculate(-31937.0, 118300.0), -3778147100.00)

    def test0259(self):
        self.assertEquals(self.calculate(56157.0, -39649.0), -2226568893.00)

    def test0260(self):
        self.assertEquals(self.calculate(-174771.0, -76156.0), 13309860276.00)

    def test0261(self):
        self.assertEquals(self.calculate(97854.0, 914.0), 89438556.00)

    def test0262(self):
        self.assertEquals(self.calculate(-50681.0, -65398.0), 3314436038.00)

    def test0263(self):
        self.assertEquals(self.calculate(35184.0, 69810.0), 2456195040.00)

    def test0264(self):
        self.assertEquals(self.calculate(-107230.0, 44454.0), -4766802420.00)

    def test0265(self):
        self.assertEquals(self.calculate(-105651.0, -117582.0), 12422655882.00)

    def test0266(self):
        self.assertEquals(self.calculate(-58487.0, 112385.0), -6573061495.00)

    def test0267(self):
        self.assertEquals(self.calculate(37799.0, 70104.0), 2649861096.00)

    def test0268(self):
        self.assertEquals(self.calculate(-175635.0, 38132.0), -6697313820.00)

    def test0269(self):
        self.assertEquals(self.calculate(-3812.0, 185951.0), -708845212.00)

    def test0270(self):
        self.assertEquals(self.calculate(175021.0, 35181.0), 6157413801.00)

    def test0271(self):
        self.assertEquals(self.calculate(183955.0, -11141.0), -2049442655.00)

    def test0272(self):
        self.assertEquals(self.calculate(187613.0, -59365.0), -11137645745.00)

    def test0273(self):
        self.assertEquals(self.calculate(-20110.0, 157983.0), -3177038130.00)

    def test0274(self):
        self.assertEquals(self.calculate(165683.0, 116015.0), 19221713245.00)

    def test0275(self):
        self.assertEquals(self.calculate(-190246.0, 150345.0), -28602534870.00)

    def test0276(self):
        self.assertEquals(self.calculate(87042.0, -24964.0), -2172916488.00)

    def test0277(self):
        self.assertEquals(self.calculate(-197598.0, -121450.0), 23998277100.00)

    def test0278(self):
        self.assertEquals(self.calculate(-93471.0, 113500.0), -10608958500.00)

    def test0279(self):
        self.assertEquals(self.calculate(18336.0, -21948.0), -402438528.00)

    def test0280(self):
        self.assertEquals(self.calculate(129688.0, 187151.0), 24271238888.00)

    def test0281(self):
        self.assertEquals(self.calculate(45019.0, -192496.0), -8665977424.00)

    def test0282(self):
        self.assertEquals(self.calculate(-146900.0, 4255.0), -625059500.00)

    def test0283(self):
        self.assertEquals(self.calculate(191734.0, -153559.0), -29442481306.00)

    def test0284(self):
        self.assertEquals(self.calculate(-128794.0, 34837.0), -4486796578.00)

    def test0285(self):
        self.assertEquals(self.calculate(-40440.0, -176341.0), 7131230040.00)

    def test0286(self):
        self.assertEquals(self.calculate(20802.0, 194326.0), 4042369452.00)

    def test0287(self):
        self.assertEquals(self.calculate(143583.0, 106983.0), 15360940089.00)

    def test0288(self):
        self.assertEquals(self.calculate(-176409.0, 168940.0), -29802536460.00)

    def test0289(self):
        self.assertEquals(self.calculate(67381.0, 171240.0), 11538322440.00)

    def test0290(self):
        self.assertEquals(self.calculate(-120054.0, -51563.0), 6190344402.00)

    def test0291(self):
        self.assertEquals(self.calculate(-52566.0, 53872.0), -2831835552.00)

    def test0292(self):
        self.assertEquals(self.calculate(-145283.0, 140555.0), -20420252065.00)

    def test0293(self):
        self.assertEquals(self.calculate(-175766.0, -113193.0), 19895480838.00)

    def test0294(self):
        self.assertEquals(self.calculate(111115.0, 168759.0), 18751656285.00)

    def test0295(self):
        self.assertEquals(self.calculate(133178.0, -4743.0), -631663254.00)

    def test0296(self):
        self.assertEquals(self.calculate(8596.0, -135226.0), -1162402696.00)

    def test0297(self):
        self.assertEquals(self.calculate(98320.0, -155556.0), -15294265920.00)

    def test0298(self):
        self.assertEquals(self.calculate(-95621.0, 112342.0), -10742254382.00)

    def test0299(self):
        self.assertEquals(self.calculate(-97812.0, -53606.0), 5243310072.00)

    def test0300(self):
        self.assertEquals(self.calculate(-123825.0, -76950.0), 9528333750.00)

    def test0301(self):
        self.assertEquals(self.calculate(161967.0, 21243.0), 3440664981.00)

    def test0302(self):
        self.assertEquals(self.calculate(100434.0, 83704.0), 8406727536.00)

    def test0303(self):
        self.assertEquals(self.calculate(143038.0, 151796.0), 21712596248.00)

    def test0304(self):
        self.assertEquals(self.calculate(132494.0, -26136.0), -3462863184.00)

    def test0305(self):
        self.assertEquals(self.calculate(-28909.0, -4014.0), 116040726.00)

    def test0306(self):
        self.assertEquals(self.calculate(-51915.0, 64666.0), -3357135390.00)

    def test0307(self):
        self.assertEquals(self.calculate(-145859.0, -35395.0), 5162679305.00)

    def test0308(self):
        self.assertEquals(self.calculate(84587.0, -23321.0), -1972653427.00)

    def test0309(self):
        self.assertEquals(self.calculate(-57857.0, -38807.0), 2245256599.00)

    def test0310(self):
        self.assertEquals(self.calculate(-118672.0, 189371.0), -22473035312.00)

    def test0311(self):
        self.assertEquals(self.calculate(-87593.0, -48643.0), 4260786299.00)

    def test0312(self):
        self.assertEquals(self.calculate(-128486.0, 108117.0), -13891520862.00)

    def test0313(self):
        self.assertEquals(self.calculate(-116605.0, 160666.0), -18734458930.00)

    def test0314(self):
        self.assertEquals(self.calculate(-172266.0, -138568.0), 23870555088.00)

    def test0315(self):
        self.assertEquals(self.calculate(-121705.0, -181169.0), 22049173145.00)

    def test0316(self):
        self.assertEquals(self.calculate(50266.0, -61212.0), -3076882392.00)

    def test0317(self):
        self.assertEquals(self.calculate(51885.0, -66402.0), -3445267770.00)

    def test0318(self):
        self.assertEquals(self.calculate(-32997.0, -159538.0), 5264275386.00)

    def test0319(self):
        self.assertEquals(self.calculate(28922.0, 51392.0), 1486359424.00)

    def test0320(self):
        self.assertEquals(self.calculate(-83187.0, 11474.0), -954487638.00)

    def test0321(self):
        self.assertEquals(self.calculate(110394.0, 155426.0), 17158097844.00)

    def test0322(self):
        self.assertEquals(self.calculate(145262.0, -126195.0), -18331338090.00)

    def test0323(self):
        self.assertEquals(self.calculate(-17283.0, -64114.0), 1108082262.00)

    def test0324(self):
        self.assertEquals(self.calculate(16712.0, -78319.0), -1308867128.00)

    def test0325(self):
        self.assertEquals(self.calculate(140335.0, 21250.0), 2982118750.00)

    def test0326(self):
        self.assertEquals(self.calculate(-94529.0, -147491.0), 13942176739.00)

    def test0327(self):
        self.assertEquals(self.calculate(-116769.0, -194314.0), 22689851466.00)

    def test0328(self):
        self.assertEquals(self.calculate(142820.0, 46633.0), 6660125060.00)

    def test0329(self):
        self.assertEquals(self.calculate(105154.0, -75872.0), -7978244288.00)

    def test0330(self):
        self.assertEquals(self.calculate(120810.0, 11907.0), 1438484670.00)

    def test0331(self):
        self.assertEquals(self.calculate(-20445.0, 20830.0), -425869350.00)

    def test0332(self):
        self.assertEquals(self.calculate(113108.0, 152028.0), 17195583024.00)

    def test0333(self):
        self.assertEquals(self.calculate(104311.0, 192054.0), 20033344794.00)

    def test0334(self):
        self.assertEquals(self.calculate(-35069.0, -71549.0), 2509151881.00)

    def test0335(self):
        self.assertEquals(self.calculate(-35863.0, 177418.0), -6362741734.00)

    def test0336(self):
        self.assertEquals(self.calculate(-99774.0, 16702.0), -1666425348.00)

    def test0337(self):
        self.assertEquals(self.calculate(-146537.0, -101491.0), 14872186667.00)

    def test0338(self):
        self.assertEquals(self.calculate(-20670.0, -4921.0), 101717070.00)

    def test0339(self):
        self.assertEquals(self.calculate(-167896.0, -13685.0), 2297656760.00)

    def test0340(self):
        self.assertEquals(self.calculate(100002.0, -45574.0), -4557491148.00)

    def test0341(self):
        self.assertEquals(self.calculate(39454.0, 1800.0), 71017200.00)

    def test0342(self):
        self.assertEquals(self.calculate(-64962.0, -160449.0), 10423087938.00)

    def test0343(self):
        self.assertEquals(self.calculate(-53313.0, -89108.0), 4750614804.00)

    def test0344(self):
        self.assertEquals(self.calculate(-71460.0, 146391.0), -10461100860.00)

    def test0345(self):
        self.assertEquals(self.calculate(149431.0, -143252.0), -21406289612.00)

    def test0346(self):
        self.assertEquals(self.calculate(-113972.0, -126858.0), 14458259976.00)

    def test0347(self):
        self.assertEquals(self.calculate(45272.0, -124418.0), -5632651696.00)

    def test0348(self):
        self.assertEquals(self.calculate(178592.0, 155350.0), 27744267200.00)

    def test0349(self):
        self.assertEquals(self.calculate(5769.0, -103369.0), -596335761.00)

    def test0350(self):
        self.assertEquals(self.calculate(-152751.0, -179112.0), 27359537112.00)

    def test0351(self):
        self.assertEquals(self.calculate(-31299.0, 67884.0), -2124701316.00)

    def test0352(self):
        self.assertEquals(self.calculate(-109497.0, -27109.0), 2968354173.00)

    def test0353(self):
        self.assertEquals(self.calculate(137843.0, 153820.0), 21203010260.00)

    def test0354(self):
        self.assertEquals(self.calculate(65270.0, -74173.0), -4841271710.00)

    def test0355(self):
        self.assertEquals(self.calculate(-1346.0, -143712.0), 193436352.00)

    def test0356(self):
        self.assertEquals(self.calculate(50725.0, 163584.0), 8297798400.00)

    def test0357(self):
        self.assertEquals(self.calculate(109965.0, 126424.0), 13902215160.00)

    def test0358(self):
        self.assertEquals(self.calculate(53110.0, -91921.0), -4881924310.00)

    def test0359(self):
        self.assertEquals(self.calculate(-184160.0, -50459.0), 9292529440.00)

    def test0360(self):
        self.assertEquals(self.calculate(-195620.0, -188078.0), 36791818360.00)

    def test0361(self):
        self.assertEquals(self.calculate(-73293.0, 109779.0), -8046032247.00)

    def test0362(self):
        self.assertEquals(self.calculate(-23199.0, -108161.0), 2509227039.00)

    def test0363(self):
        self.assertEquals(self.calculate(68174.0, 90559.0), 6173769266.00)

    def test0364(self):
        self.assertEquals(self.calculate(56700.0, 193230.0), 10956141000.00)

    def test0365(self):
        self.assertEquals(self.calculate(128066.0, -162033.0), -20750918178.00)

    def test0366(self):
        self.assertEquals(self.calculate(-96683.0, -96612.0), 9340737996.00)

    def test0367(self):
        self.assertEquals(self.calculate(129888.0, 106982.0), 13895678016.00)

    def test0368(self):
        self.assertEquals(self.calculate(-112890.0, 87519.0), -9880019910.00)

    def test0369(self):
        self.assertEquals(self.calculate(-46944.0, -196711.0), 9234401184.00)

    def test0370(self):
        self.assertEquals(self.calculate(198262.0, -186728.0), -37021066736.00)

    def test0371(self):
        self.assertEquals(self.calculate(-179724.0, 176185.0), -31664672940.00)

    def test0372(self):
        self.assertEquals(self.calculate(149435.0, -25372.0), -3791464820.00)

    def test0373(self):
        self.assertEquals(self.calculate(-34923.0, -184539.0), 6444655497.00)

    def test0374(self):
        self.assertEquals(self.calculate(44994.0, 104821.0), 4716316074.00)

    def test0375(self):
        self.assertEquals(self.calculate(182268.0, 185866.0), 33877424088.00)

    def test0376(self):
        self.assertEquals(self.calculate(-10504.0, 1094.0), -11491376.00)

    def test0377(self):
        self.assertEquals(self.calculate(143175.0, 87266.0), 12494309550.00)

    def test0378(self):
        self.assertEquals(self.calculate(180309.0, 54896.0), 9898242864.00)

    def test0379(self):
        self.assertEquals(self.calculate(-141262.0, 89058.0), -12580511196.00)

    def test0380(self):
        self.assertEquals(self.calculate(118422.0, 14884.0), 1762593048.00)

    def test0381(self):
        self.assertEquals(self.calculate(-126647.0, -51865.0), 6568546655.00)

    def test0382(self):
        self.assertEquals(self.calculate(-147643.0, -26415.0), 3899989845.00)

    def test0383(self):
        self.assertEquals(self.calculate(-65258.0, -95064.0), 6203686512.00)

    def test0384(self):
        self.assertEquals(self.calculate(96423.0, 196473.0), 18944516079.00)

    def test0385(self):
        self.assertEquals(self.calculate(113368.0, 16462.0), 1866264016.00)

    def test0386(self):
        self.assertEquals(self.calculate(161788.0, 94048.0), 15215837824.00)

    def test0387(self):
        self.assertEquals(self.calculate(187723.0, 108149.0), 20302054727.00)

    def test0388(self):
        self.assertEquals(self.calculate(67619.0, 63305.0), 4280620795.00)

    def test0389(self):
        self.assertEquals(self.calculate(99799.0, 88999.0), 8882011201.00)

    def test0390(self):
        self.assertEquals(self.calculate(-144658.0, -107165.0), 15502274570.00)

    def test0391(self):
        self.assertEquals(self.calculate(-131667.0, -60132.0), 7917400044.00)

    def test0392(self):
        self.assertEquals(self.calculate(-175211.0, 184871.0), -32391432781.00)

    def test0393(self):
        self.assertEquals(self.calculate(-174176.0, 6958.0), -1211916608.00)

    def test0394(self):
        self.assertEquals(self.calculate(129839.0, 86101.0), 11179267739.00)

    def test0395(self):
        self.assertEquals(self.calculate(-199048.0, -141222.0), 28109956656.00)

    def test0396(self):
        self.assertEquals(self.calculate(53869.0, -31769.0), -1711364261.00)

    def test0397(self):
        self.assertEquals(self.calculate(-53795.0, -120937.0), 6505805915.00)

    def test0398(self):
        self.assertEquals(self.calculate(138447.0, -2119.0), -293369193.00)

    def test0399(self):
        self.assertEquals(self.calculate(125727.0, -164441.0), -20674673607.00)

    def test0400(self):
        self.assertEquals(self.calculate(-188169.0, -110409.0), 20775551121.00)

    def test0401(self):
        self.assertEquals(self.calculate(1194.0, 122700.0), 146503800.00)

    def test0402(self):
        self.assertEquals(self.calculate(90919.0, 6125.0), 556878875.00)

    def test0403(self):
        self.assertEquals(self.calculate(-156419.0, -101249.0), 15837267331.00)

    def test0404(self):
        self.assertEquals(self.calculate(113079.0, 181395.0), 20511965205.00)

    def test0405(self):
        self.assertEquals(self.calculate(-57223.0, 109717.0), -6278335891.00)

    def test0406(self):
        self.assertEquals(self.calculate(123612.0, -99315.0), -12276525780.00)

    def test0407(self):
        self.assertEquals(self.calculate(135334.0, 144051.0), 19494998034.00)

    def test0408(self):
        self.assertEquals(self.calculate(48279.0, -54484.0), -2630433036.00)

    def test0409(self):
        self.assertEquals(self.calculate(-67281.0, 75378.0), -5071507218.00)

    def test0410(self):
        self.assertEquals(self.calculate(167196.0, -111253.0), -18601056588.00)

    def test0411(self):
        self.assertEquals(self.calculate(-194313.0, -78066.0), 15169238658.00)

    def test0412(self):
        self.assertEquals(self.calculate(28035.0, 89023.0), 2495759805.00)

    def test0413(self):
        self.assertEquals(self.calculate(46738.0, 45645.0), 2133356010.00)

    def test0414(self):
        self.assertEquals(self.calculate(165248.0, 67335.0), 11126974080.00)

    def test0415(self):
        self.assertEquals(self.calculate(64738.0, 100136.0), 6482604368.00)

    def test0416(self):
        self.assertEquals(self.calculate(165214.0, 115198.0), 19032322372.00)

    def test0417(self):
        self.assertEquals(self.calculate(127740.0, -114252.0), -14594550480.00)

    def test0418(self):
        self.assertEquals(self.calculate(127526.0, 153024.0), 19514538624.00)

    def test0419(self):
        self.assertEquals(self.calculate(8925.0, 42991.0), 383694675.00)

    def test0420(self):
        self.assertEquals(self.calculate(-85583.0, 54086.0), -4628842138.00)

    def test0421(self):
        self.assertEquals(self.calculate(-3417.0, -124492.0), 425389164.00)

    def test0422(self):
        self.assertEquals(self.calculate(53469.0, -49952.0), -2670883488.00)

    def test0423(self):
        self.assertEquals(self.calculate(-51589.0, -120763.0), 6230042407.00)

    def test0424(self):
        self.assertEquals(self.calculate(154591.0, -104210.0), -16109928110.00)

    def test0425(self):
        self.assertEquals(self.calculate(132757.0, -34800.0), -4619943600.00)

    def test0426(self):
        self.assertEquals(self.calculate(10567.0, -50518.0), -533823706.00)

    def test0427(self):
        self.assertEquals(self.calculate(172855.0, -1901.0), -328597355.00)

    def test0428(self):
        self.assertEquals(self.calculate(-123952.0, 197273.0), -24452382896.00)

    def test0429(self):
        self.assertEquals(self.calculate(-31273.0, 192339.0), -6015017547.00)

    def test0430(self):
        self.assertEquals(self.calculate(104935.0, 22953.0), 2408573055.00)

    def test0431(self):
        self.assertEquals(self.calculate(-128259.0, -68603.0), 8798952177.00)

    def test0432(self):
        self.assertEquals(self.calculate(-189554.0, 198787.0), -37680870998.00)

    def test0433(self):
        self.assertEquals(self.calculate(-135191.0, 47428.0), -6411838748.00)

    def test0434(self):
        self.assertEquals(self.calculate(-101779.0, 22949.0), -2335726271.00)

    def test0435(self):
        self.assertEquals(self.calculate(96964.0, -197363.0), -19137105932.00)

    def test0436(self):
        self.assertEquals(self.calculate(-136121.0, -177687.0), 24186932127.00)

    def test0437(self):
        self.assertEquals(self.calculate(171815.0, 79765.0), 13704823475.00)

    def test0438(self):
        self.assertEquals(self.calculate(-29065.0, 185219.0), -5383390235.00)

    def test0439(self):
        self.assertEquals(self.calculate(-187607.0, 13237.0), -2483353859.00)

    def test0440(self):
        self.assertEquals(self.calculate(99810.0, 18336.0), 1830116160.00)

    def test0441(self):
        self.assertEquals(self.calculate(-157626.0, 83779.0), -13205748654.00)

    def test0442(self):
        self.assertEquals(self.calculate(-640.0, -17621.0), 11277440.00)

    def test0443(self):
        self.assertEquals(self.calculate(188404.0, -150580.0), -28369874320.00)

    def test0444(self):
        self.assertEquals(self.calculate(-193911.0, -52918.0), 10261382298.00)

    def test0445(self):
        self.assertEquals(self.calculate(117886.0, -127721.0), -15056517806.00)

    def test0446(self):
        self.assertEquals(self.calculate(6840.0, 3826.0), 26169840.00)

    def test0447(self):
        self.assertEquals(self.calculate(46014.0, 15920.0), 732542880.00)

    def test0448(self):
        self.assertEquals(self.calculate(-7148.0, -24855.0), 177663540.00)

    def test0449(self):
        self.assertEquals(self.calculate(70914.0, -64650.0), -4584590100.00)

    def test0450(self):
        self.assertEquals(self.calculate(-145874.0, 57340.0), -8364415160.00)

    def test0451(self):
        self.assertEquals(self.calculate(191936.0, -171749.0), -32964816064.00)

    def test0452(self):
        self.assertEquals(self.calculate(174572.0, 171805.0), 29992342460.00)

    def test0453(self):
        self.assertEquals(self.calculate(-173255.0, -132093.0), 22885772715.00)

    def test0454(self):
        self.assertEquals(self.calculate(157055.0, 175246.0), 27523260530.00)

    def test0455(self):
        self.assertEquals(self.calculate(182276.0, -92495.0), -16859618620.00)

    def test0456(self):
        self.assertEquals(self.calculate(-123824.0, -63133.0), 7817380592.00)

    def test0457(self):
        self.assertEquals(self.calculate(8769.0, -117584.0), -1031094096.00)

    def test0458(self):
        self.assertEquals(self.calculate(-66385.0, 163953.0), -10884019905.00)

    def test0459(self):
        self.assertEquals(self.calculate(-67301.0, -170623.0), 11483098523.00)

    def test0460(self):
        self.assertEquals(self.calculate(85900.0, -176319.0), -15145802100.00)

    def test0461(self):
        self.assertEquals(self.calculate(-47204.0, 65126.0), -3074207704.00)

    def test0462(self):
        self.assertEquals(self.calculate(92360.0, 82427.0), 7612957720.00)

    def test0463(self):
        self.assertEquals(self.calculate(169910.0, 746.0), 126752860.00)

    def test0464(self):
        self.assertEquals(self.calculate(-77269.0, -19441.0), 1502186629.00)

    def test0465(self):
        self.assertEquals(self.calculate(-187201.0, -167687.0), 31391174087.00)

    def test0466(self):
        self.assertEquals(self.calculate(32921.0, 40750.0), 1341530750.00)

    def test0467(self):
        self.assertEquals(self.calculate(-42395.0, -32218.0), 1365882110.00)

    def test0468(self):
        self.assertEquals(self.calculate(-177080.0, -106012.0), 18772604960.00)

    def test0469(self):
        self.assertEquals(self.calculate(132520.0, -97945.0), -12979671400.00)

    def test0470(self):
        self.assertEquals(self.calculate(188249.0, 145374.0), 27366510126.00)

    def test0471(self):
        self.assertEquals(self.calculate(-57033.0, -76875.0), 4384411875.00)

    def test0472(self):
        self.assertEquals(self.calculate(182466.0, -63782.0), -11638046412.00)

    def test0473(self):
        self.assertEquals(self.calculate(181144.0, 193109.0), 34980536696.00)

    def test0474(self):
        self.assertEquals(self.calculate(-95094.0, -12539.0), 1192383666.00)

    def test0475(self):
        self.assertEquals(self.calculate(-15671.0, 160859.0), -2520821389.00)

    def test0476(self):
        self.assertEquals(self.calculate(-4750.0, 193729.0), -920212750.00)

    def test0477(self):
        self.assertEquals(self.calculate(12732.0, 123121.0), 1567576572.00)

    def test0478(self):
        self.assertEquals(self.calculate(-63587.0, 130320.0), -8286657840.00)

    def test0479(self):
        self.assertEquals(self.calculate(19143.0, -147082.0), -2815590726.00)

    def test0480(self):
        self.assertEquals(self.calculate(-52178.0, 133827.0), -6982825206.00)

    def test0481(self):
        self.assertEquals(self.calculate(107108.0, 97995.0), 10496048460.00)

    def test0482(self):
        self.assertEquals(self.calculate(-1179.0, 7009.0), -8263611.00)

    def test0483(self):
        self.assertEquals(self.calculate(-139725.0, 31265.0), -4368502125.00)

    def test0484(self):
        self.assertEquals(self.calculate(-20594.0, 98319.0), -2024781486.00)

    def test0485(self):
        self.assertEquals(self.calculate(75325.0, -128162.0), -9653802650.00)

    def test0486(self):
        self.assertEquals(self.calculate(96466.0, 87001.0), 8392638466.00)

    def test0487(self):
        self.assertEquals(self.calculate(13244.0, -108072.0), -1431305568.00)

    def test0488(self):
        self.assertEquals(self.calculate(44546.0, -136709.0), -6089839114.00)

    def test0489(self):
        self.assertEquals(self.calculate(13356.0, 51014.0), 681342984.00)

    def test0490(self):
        self.assertEquals(self.calculate(118152.0, -166360.0), -19655766720.00)

    def test0491(self):
        self.assertEquals(self.calculate(96760.0, 165288.0), 15993266880.00)

    def test0492(self):
        self.assertEquals(self.calculate(159703.0, -103743.0), -16568068329.00)

    def test0493(self):
        self.assertEquals(self.calculate(47674.0, 144433.0), 6885698842.00)

    def test0494(self):
        self.assertEquals(self.calculate(57816.0, -199538.0), -11536489008.00)

    def test0495(self):
        self.assertEquals(self.calculate(-65645.0, -187760.0), 12325505200.00)

    def test0496(self):
        self.assertEquals(self.calculate(-182253.0, -170940.0), 31154327820.00)

    def test0497(self):
        self.assertEquals(self.calculate(191227.0, -83736.0), -16012584072.00)

    def test0498(self):
        self.assertEquals(self.calculate(-35403.0, -1736.0), 61459608.00)

    def test0499(self):
        self.assertEquals(self.calculate(-70720.0, -137829.0), 9747266880.00)

    def test0500(self):
        self.assertEquals(self.calculate(-17507.0, -180524.0), 3160433668.00)

    def test0501(self):
        self.assertEquals(self.calculate(-191490.0, -97890.0), 18744956100.00)

    def test0502(self):
        self.assertEquals(self.calculate(-42514.0, 155316.0), -6603104424.00)

    def test0503(self):
        self.assertEquals(self.calculate(73916.0, -110073.0), -8136155868.00)

    def test0504(self):
        self.assertEquals(self.calculate(-102802.0, 48566.0), -4992681932.00)

    def test0505(self):
        self.assertEquals(self.calculate(123715.0, -133371.0), -16499993265.00)

    def test0506(self):
        self.assertEquals(self.calculate(112630.0, 23343.0), 2629122090.00)

    def test0507(self):
        self.assertEquals(self.calculate(-180658.0, 47501.0), -8581435658.00)

    def test0508(self):
        self.assertEquals(self.calculate(-48970.0, -126508.0), 6195096760.00)

    def test0509(self):
        self.assertEquals(self.calculate(25520.0, -140012.0), -3573106240.00)

    def test0510(self):
        self.assertEquals(self.calculate(162148.0, -50347.0), -8163665356.00)

    def test0511(self):
        self.assertEquals(self.calculate(172666.0, -63609.0), -10983111594.00)

    def test0512(self):
        self.assertEquals(self.calculate(188911.0, 27230.0), 5144046530.00)

    def test0513(self):
        self.assertEquals(self.calculate(25502.0, -127161.0), -3242859822.00)

    def test0514(self):
        self.assertEquals(self.calculate(-38478.0, 184315.0), -7092072570.00)

    def test0515(self):
        self.assertEquals(self.calculate(199273.0, 104238.0), 20771818974.00)

    def test0516(self):
        self.assertEquals(self.calculate(-173146.0, 166473.0), -28824134058.00)

    def test0517(self):
        self.assertEquals(self.calculate(119481.0, 24743.0), 2956318383.00)

    def test0518(self):
        self.assertEquals(self.calculate(-49634.0, 169425.0), -8409240450.00)

    def test0519(self):
        self.assertEquals(self.calculate(-51795.0, 35358.0), -1831367610.00)

    def test0520(self):
        self.assertEquals(self.calculate(93978.0, -54318.0), -5104697004.00)

    def test0521(self):
        self.assertEquals(self.calculate(-165892.0, 115231.0), -19115901052.00)

    def test0522(self):
        self.assertEquals(self.calculate(-31316.0, 63098.0), -1975976968.00)

    def test0523(self):
        self.assertEquals(self.calculate(-14011.0, -167720.0), 2349924920.00)

    def test0524(self):
        self.assertEquals(self.calculate(164059.0, 45897.0), 7529815923.00)

    def test0525(self):
        self.assertEquals(self.calculate(93404.0, -47144.0), -4403438176.00)

    def test0526(self):
        self.assertEquals(self.calculate(-87566.0, 145968.0), -12781833888.00)

    def test0527(self):
        self.assertEquals(self.calculate(74516.0, 142853.0), 10644834148.00)

    def test0528(self):
        self.assertEquals(self.calculate(9439.0, 137475.0), 1297626525.00)

    def test0529(self):
        self.assertEquals(self.calculate(-118975.0, -25347.0), 3015659325.00)

    def test0530(self):
        self.assertEquals(self.calculate(167761.0, -195400.0), -32780499400.00)

    def test0531(self):
        self.assertEquals(self.calculate(-129515.0, 123885.0), -16044965775.00)

    def test0532(self):
        self.assertEquals(self.calculate(97725.0, 159319.0), 15569449275.00)

    def test0533(self):
        self.assertEquals(self.calculate(172078.0, 48626.0), 8367464828.00)

    def test0534(self):
        self.assertEquals(self.calculate(138640.0, -64937.0), -9002865680.00)

    def test0535(self):
        self.assertEquals(self.calculate(-143463.0, 76144.0), -10923846672.00)

    def test0536(self):
        self.assertEquals(self.calculate(130893.0, 122729.0), 16064366997.00)

    def test0537(self):
        self.assertEquals(self.calculate(110804.0, 88341.0), 9788536164.00)

    def test0538(self):
        self.assertEquals(self.calculate(-198469.0, -124636.0), 24736382284.00)

    def test0539(self):
        self.assertEquals(self.calculate(-165454.0, -149832.0), 24790303728.00)

    def test0540(self):
        self.assertEquals(self.calculate(21613.0, 15360.0), 331975680.00)

    def test0541(self):
        self.assertEquals(self.calculate(-160525.0, -55464.0), 8903358600.00)

    def test0542(self):
        self.assertEquals(self.calculate(94157.0, 196831.0), 18533016467.00)

    def test0543(self):
        self.assertEquals(self.calculate(16885.0, 78007.0), 1317148195.00)

    def test0544(self):
        self.assertEquals(self.calculate(-96251.0, 60256.0), -5799700256.00)

    def test0545(self):
        self.assertEquals(self.calculate(-174471.0, 14931.0), -2605026501.00)

    def test0546(self):
        self.assertEquals(self.calculate(72273.0, -173580.0), -12545147340.00)

    def test0547(self):
        self.assertEquals(self.calculate(8267.0, -181649.0), -1501692283.00)

    def test0548(self):
        self.assertEquals(self.calculate(42926.0, 2154.0), 92462604.00)

    def test0549(self):
        self.assertEquals(self.calculate(-85342.0, 77494.0), -6613492948.00)

    def test0550(self):
        self.assertEquals(self.calculate(-172282.0, -130884.0), 22548957288.00)

    def test0551(self):
        self.assertEquals(self.calculate(189690.0, -49873.0), -9460409370.00)

    def test0552(self):
        self.assertEquals(self.calculate(-38210.0, 197107.0), -7531458470.00)

    def test0553(self):
        self.assertEquals(self.calculate(88027.0, 163995.0), 14435987865.00)

    def test0554(self):
        self.assertEquals(self.calculate(148328.0, 187702.0), 27841462256.00)

    def test0555(self):
        self.assertEquals(self.calculate(-180700.0, -57298.0), 10353748600.00)

    def test0556(self):
        self.assertEquals(self.calculate(54550.0, -168325.0), -9182128750.00)

    def test0557(self):
        self.assertEquals(self.calculate(-168505.0, -21871.0), 3685372855.00)

    def test0558(self):
        self.assertEquals(self.calculate(-9284.0, -159155.0), 1477595020.00)

    def test0559(self):
        self.assertEquals(self.calculate(110530.0, -130549.0), -14429580970.00)

    def test0560(self):
        self.assertEquals(self.calculate(-25293.0, -124617.0), 3151937781.00)

    def test0561(self):
        self.assertEquals(self.calculate(-105518.0, 74665.0), -7878501470.00)

    def test0562(self):
        self.assertEquals(self.calculate(191924.0, -110441.0), -21196278484.00)

    def test0563(self):
        self.assertEquals(self.calculate(-180342.0, 122932.0), -22169802744.00)

    def test0564(self):
        self.assertEquals(self.calculate(-37404.0, 189093.0), -7072834572.00)

    def test0565(self):
        self.assertEquals(self.calculate(43035.0, -175880.0), -7568995800.00)

    def test0566(self):
        self.assertEquals(self.calculate(-66217.0, 67852.0), -4492955884.00)

    def test0567(self):
        self.assertEquals(self.calculate(76776.0, -118657.0), -9110009832.00)

    def test0568(self):
        self.assertEquals(self.calculate(48256.0, -51483.0), -2484363648.00)

    def test0569(self):
        self.assertEquals(self.calculate(27102.0, -4643.0), -125834586.00)

    def test0570(self):
        self.assertEquals(self.calculate(-178279.0, -32477.0), 5789967083.00)

    def test0571(self):
        self.assertEquals(self.calculate(127930.0, 124766.0), 15961314380.00)

    def test0572(self):
        self.assertEquals(self.calculate(186115.0, -49664.0), -9243215360.00)

    def test0573(self):
        self.assertEquals(self.calculate(29749.0, 192640.0), 5730847360.00)

    def test0574(self):
        self.assertEquals(self.calculate(-90298.0, -71984.0), 6500011232.00)

    def test0575(self):
        self.assertEquals(self.calculate(-164204.0, 175894.0), -28882498376.00)

    def test0576(self):
        self.assertEquals(self.calculate(46678.0, -134111.0), -6260033258.00)

    def test0577(self):
        self.assertEquals(self.calculate(176051.0, -100117.0), -17625697967.00)

    def test0578(self):
        self.assertEquals(self.calculate(178994.0, 121648.0), 21774262112.00)

    def test0579(self):
        self.assertEquals(self.calculate(-34942.0, 173497.0), -6062332174.00)

    def test0580(self):
        self.assertEquals(self.calculate(-189038.0, -61162.0), 11561942156.00)

    def test0581(self):
        self.assertEquals(self.calculate(-4172.0, 192150.0), -801649800.00)

    def test0582(self):
        self.assertEquals(self.calculate(108743.0, -100813.0), -10962708059.00)

    def test0583(self):
        self.assertEquals(self.calculate(-18694.0, -68202.0), 1274968188.00)

    def test0584(self):
        self.assertEquals(self.calculate(-171109.0, 15053.0), -2575703777.00)

    def test0585(self):
        self.assertEquals(self.calculate(83012.0, 12276.0), 1019055312.00)

    def test0586(self):
        self.assertEquals(self.calculate(24909.0, 130669.0), 3254834121.00)

    def test0587(self):
        self.assertEquals(self.calculate(183501.0, -50497.0), -9266249997.00)

    def test0588(self):
        self.assertEquals(self.calculate(98824.0, 102530.0), 10132424720.00)

    def test0589(self):
        self.assertEquals(self.calculate(-158290.0, -16978.0), 2687447620.00)

    def test0590(self):
        self.assertEquals(self.calculate(-29194.0, -194019.0), 5664190686.00)

    def test0591(self):
        self.assertEquals(self.calculate(74170.0, 179184.0), 13290077280.00)

    def test0592(self):
        self.assertEquals(self.calculate(188533.0, 80401.0), 15158241733.00)

    def test0593(self):
        self.assertEquals(self.calculate(57001.0, -54077.0), -3082443077.00)

    def test0594(self):
        self.assertEquals(self.calculate(122821.0, 16450.0), 2020405450.00)

    def test0595(self):
        self.assertEquals(self.calculate(58407.0, 194960.0), 11387028720.00)

    def test0596(self):
        self.assertEquals(self.calculate(-115862.0, 133855.0), -15508708010.00)

    def test0597(self):
        self.assertEquals(self.calculate(28145.0, 121904.0), 3430988080.00)

    def test0598(self):
        self.assertEquals(self.calculate(-45061.0, -184329.0), 8306049069.00)

    def test0599(self):
        self.assertEquals(self.calculate(-124020.0, -34783.0), 4313787660.00)

    def test0600(self):
        self.assertEquals(self.calculate(37741.0, -19173.0), -723608193.00)

    def test0601(self):
        self.assertEquals(self.calculate(-58953.0, -86790.0), 5116530870.00)

    def test0602(self):
        self.assertEquals(self.calculate(-36249.0, -13102.0), 474934398.00)

    def test0603(self):
        self.assertEquals(self.calculate(-82936.0, -151497.0), 12564555192.00)

    def test0604(self):
        self.assertEquals(self.calculate(-180483.0, -145715.0), 26299080345.00)

    def test0605(self):
        self.assertEquals(self.calculate(29182.0, 85097.0), 2483300654.00)

    def test0606(self):
        self.assertEquals(self.calculate(198330.0, -39064.0), -7747563120.00)

    def test0607(self):
        self.assertEquals(self.calculate(94348.0, 129318.0), 12200894664.00)

    def test0608(self):
        self.assertEquals(self.calculate(-22162.0, 22180.0), -491553160.00)

    def test0609(self):
        self.assertEquals(self.calculate(-199044.0, 6126.0), -1219343544.00)

    def test0610(self):
        self.assertEquals(self.calculate(-21754.0, -103827.0), 2258652558.00)

    def test0611(self):
        self.assertEquals(self.calculate(-141294.0, 43787.0), -6186840378.00)

    def test0612(self):
        self.assertEquals(self.calculate(-1688.0, -122569.0), 206896472.00)

    def test0613(self):
        self.assertEquals(self.calculate(192184.0, 95496.0), 18352803264.00)

    def test0614(self):
        self.assertEquals(self.calculate(-4643.0, -34690.0), 161065670.00)

    def test0615(self):
        self.assertEquals(self.calculate(106467.0, -164971.0), -17563967457.00)

    def test0616(self):
        self.assertEquals(self.calculate(-134718.0, 40562.0), -5464431516.00)

    def test0617(self):
        self.assertEquals(self.calculate(181322.0, 190351.0), 34514824022.00)

    def test0618(self):
        self.assertEquals(self.calculate(14861.0, -138992.0), -2065560112.00)

    def test0619(self):
        self.assertEquals(self.calculate(168945.0, -187298.0), -31643060610.00)

    def test0620(self):
        self.assertEquals(self.calculate(-107392.0, 194148.0), -20849942016.00)

    def test0621(self):
        self.assertEquals(self.calculate(-7836.0, -156404.0), 1225581744.00)

    def test0622(self):
        self.assertEquals(self.calculate(-185377.0, -50119.0), 9290909863.00)

    def test0623(self):
        self.assertEquals(self.calculate(112228.0, 97691.0), 10963665548.00)

    def test0624(self):
        self.assertEquals(self.calculate(107215.0, 165192.0), 17711060280.00)

    def test0625(self):
        self.assertEquals(self.calculate(121319.0, 92052.0), 11167656588.00)

    def test0626(self):
        self.assertEquals(self.calculate(-156769.0, -14177.0), 2222514113.00)

    def test0627(self):
        self.assertEquals(self.calculate(-72643.0, -30148.0), 2190041164.00)

    def test0628(self):
        self.assertEquals(self.calculate(189455.0, 49594.0), 9395831270.00)

    def test0629(self):
        self.assertEquals(self.calculate(34506.0, 149806.0), 5169205836.00)

    def test0630(self):
        self.assertEquals(self.calculate(-199461.0, -98817.0), 19710137637.00)

    def test0631(self):
        self.assertEquals(self.calculate(-182777.0, 94159.0), -17210099543.00)

    def test0632(self):
        self.assertEquals(self.calculate(174502.0, -79543.0), -13880412586.00)

    def test0633(self):
        self.assertEquals(self.calculate(-68967.0, -90640.0), 6251168880.00)

    def test0634(self):
        self.assertEquals(self.calculate(43372.0, -175243.0), -7600639396.00)

    def test0635(self):
        self.assertEquals(self.calculate(144894.0, 26790.0), 3881710260.00)

    def test0636(self):
        self.assertEquals(self.calculate(39298.0, 149191.0), 5862907918.00)

    def test0637(self):
        self.assertEquals(self.calculate(-73943.0, -91131.0), 6738499533.00)

    def test0638(self):
        self.assertEquals(self.calculate(-102066.0, 73991.0), -7551965406.00)

    def test0639(self):
        self.assertEquals(self.calculate(138680.0, -188119.0), -26088342920.00)

    def test0640(self):
        self.assertEquals(self.calculate(36881.0, -141516.0), -5219251596.00)

    def test0641(self):
        self.assertEquals(self.calculate(44561.0, 57461.0), 2560519621.00)

    def test0642(self):
        self.assertEquals(self.calculate(-10842.0, -122791.0), 1331300022.00)

    def test0643(self):
        self.assertEquals(self.calculate(137576.0, -54530.0), -7502019280.00)

    def test0644(self):
        self.assertEquals(self.calculate(155081.0, -17293.0), -2681815733.00)

    def test0645(self):
        self.assertEquals(self.calculate(47604.0, -69839.0), -3324615756.00)

    def test0646(self):
        self.assertEquals(self.calculate(158007.0, -35580.0), -5621889060.00)

    def test0647(self):
        self.assertEquals(self.calculate(-117471.0, 109072.0), -12812796912.00)

    def test0648(self):
        self.assertEquals(self.calculate(195372.0, 55593.0), 10861315596.00)

    def test0649(self):
        self.assertEquals(self.calculate(-35196.0, 22669.0), -797858124.00)

    def test0650(self):
        self.assertEquals(self.calculate(-144651.0, 86032.0), -12444614832.00)

    def test0651(self):
        self.assertEquals(self.calculate(-8827.0, -22306.0), 196895062.00)

    def test0652(self):
        self.assertEquals(self.calculate(-174331.0, -95012.0), 16563536972.00)

    def test0653(self):
        self.assertEquals(self.calculate(78864.0, -25675.0), -2024833200.00)

    def test0654(self):
        self.assertEquals(self.calculate(-41795.0, -58357.0), 2439030815.00)

    def test0655(self):
        self.assertEquals(self.calculate(193971.0, -52501.0), -10183671471.00)

    def test0656(self):
        self.assertEquals(self.calculate(95701.0, 118408.0), 11331764008.00)

    def test0657(self):
        self.assertEquals(self.calculate(-88694.0, -77644.0), 6886556936.00)

    def test0658(self):
        self.assertEquals(self.calculate(-25473.0, 187051.0), -4764750123.00)

    def test0659(self):
        self.assertEquals(self.calculate(154589.0, 146480.0), 22644196720.00)

    def test0660(self):
        self.assertEquals(self.calculate(169603.0, 98982.0), 16787644146.00)

    def test0661(self):
        self.assertEquals(self.calculate(-79204.0, -133878.0), 10603673112.00)

    def test0662(self):
        self.assertEquals(self.calculate(-24717.0, -2346.0), 57986082.00)

    def test0663(self):
        self.assertEquals(self.calculate(-93106.0, 70097.0), -6526451282.00)

    def test0664(self):
        self.assertEquals(self.calculate(-142591.0, -49222.0), 7018614202.00)

    def test0665(self):
        self.assertEquals(self.calculate(-197806.0, -11485.0), 2271801910.00)

    def test0666(self):
        self.assertEquals(self.calculate(-191305.0, -43036.0), 8233001980.00)

    def test0667(self):
        self.assertEquals(self.calculate(-37062.0, -63418.0), 2350397916.00)

    def test0668(self):
        self.assertEquals(self.calculate(-147637.0, -6325.0), 933804025.00)

    def test0669(self):
        self.assertEquals(self.calculate(144254.0, -53278.0), -7685564612.00)

    def test0670(self):
        self.assertEquals(self.calculate(-177020.0, -67315.0), 11916101300.00)

    def test0671(self):
        self.assertEquals(self.calculate(106333.0, 96698.0), 10282188434.00)

    def test0672(self):
        self.assertEquals(self.calculate(-26921.0, 160530.0), -4321628130.00)

    def test0673(self):
        self.assertEquals(self.calculate(-14427.0, 117789.0), -1699341903.00)

    def test0674(self):
        self.assertEquals(self.calculate(-125078.0, -87771.0), 10978221138.00)

    def test0675(self):
        self.assertEquals(self.calculate(125224.0, -77731.0), -9733786744.00)

    def test0676(self):
        self.assertEquals(self.calculate(-149248.0, 44102.0), -6582135296.00)

    def test0677(self):
        self.assertEquals(self.calculate(126135.0, -93209.0), -11756917215.00)

    def test0678(self):
        self.assertEquals(self.calculate(-135735.0, 187935.0), -25509357225.00)

    def test0679(self):
        self.assertEquals(self.calculate(-143026.0, -10389.0), 1485897114.00)

    def test0680(self):
        self.assertEquals(self.calculate(98355.0, -147127.0), -14470676085.00)

    def test0681(self):
        self.assertEquals(self.calculate(-110011.0, -27215.0), 2993949365.00)

    def test0682(self):
        self.assertEquals(self.calculate(-23503.0, 29679.0), -697545537.00)

    def test0683(self):
        self.assertEquals(self.calculate(-13444.0, -163124.0), 2193039056.00)

    def test0684(self):
        self.assertEquals(self.calculate(39741.0, 11831.0), 470175771.00)

    def test0685(self):
        self.assertEquals(self.calculate(72198.0, -192414.0), -13891905972.00)

    def test0686(self):
        self.assertEquals(self.calculate(-144198.0, -165526.0), 23868518148.00)

    def test0687(self):
        self.assertEquals(self.calculate(117949.0, -141523.0), -16692496327.00)

    def test0688(self):
        self.assertEquals(self.calculate(150812.0, -69869.0), -10537083628.00)

    def test0689(self):
        self.assertEquals(self.calculate(153386.0, 64293.0), 9861646098.00)

    def test0690(self):
        self.assertEquals(self.calculate(18667.0, -165462.0), -3088679154.00)

    def test0691(self):
        self.assertEquals(self.calculate(-75638.0, 171240.0), -12952251120.00)

    def test0692(self):
        self.assertEquals(self.calculate(186007.0, 2037.0), 378896259.00)

    def test0693(self):
        self.assertEquals(self.calculate(67790.0, 197340.0), 13377678600.00)

    def test0694(self):
        self.assertEquals(self.calculate(-84531.0, -163017.0), 13779990027.00)

    def test0695(self):
        self.assertEquals(self.calculate(152757.0, 49368.0), 7541307576.00)

    def test0696(self):
        self.assertEquals(self.calculate(-141652.0, 50623.0), -7170849196.00)

    def test0697(self):
        self.assertEquals(self.calculate(6584.0, -123417.0), -812577528.00)

    def test0698(self):
        self.assertEquals(self.calculate(182476.0, 27304.0), 4982324704.00)

    def test0699(self):
        self.assertEquals(self.calculate(105016.0, -175164.0), -18395022624.00)

    def test0700(self):
        self.assertEquals(self.calculate(-9130.0, 191319.0), -1746742470.00)

    def test0701(self):
        self.assertEquals(self.calculate(-2392.0, 188544.0), -450997248.00)

    def test0702(self):
        self.assertEquals(self.calculate(-67751.0, 48470.0), -3283890970.00)

    def test0703(self):
        self.assertEquals(self.calculate(-35807.0, -177585.0), 6358786095.00)

    def test0704(self):
        self.assertEquals(self.calculate(-144078.0, -178733.0), 25751493174.00)

    def test0705(self):
        self.assertEquals(self.calculate(120887.0, -69191.0), -8364292417.00)

    def test0706(self):
        self.assertEquals(self.calculate(-183406.0, -139504.0), 25585870624.00)

    def test0707(self):
        self.assertEquals(self.calculate(-116164.0, -7535.0), 875295740.00)

    def test0708(self):
        self.assertEquals(self.calculate(168263.0, -64615.0), -10872313745.00)

    def test0709(self):
        self.assertEquals(self.calculate(-11147.0, 184120.0), -2052385640.00)

    def test0710(self):
        self.assertEquals(self.calculate(20325.0, -187316.0), -3807197700.00)

    def test0711(self):
        self.assertEquals(self.calculate(4402.0, -143856.0), -633254112.00)

    def test0712(self):
        self.assertEquals(self.calculate(-143077.0, 32508.0), -4651147116.00)

    def test0713(self):
        self.assertEquals(self.calculate(98537.0, -181087.0), -17843769719.00)

    def test0714(self):
        self.assertEquals(self.calculate(37025.0, 194777.0), 7211618425.00)

    def test0715(self):
        self.assertEquals(self.calculate(-53090.0, -175130.0), 9297651700.00)

    def test0716(self):
        self.assertEquals(self.calculate(-80862.0, -160515.0), 12979563930.00)

    def test0717(self):
        self.assertEquals(self.calculate(-89703.0, -74198.0), 6655783194.00)

    def test0718(self):
        self.assertEquals(self.calculate(-21325.0, 51033.0), -1088278725.00)

    def test0719(self):
        self.assertEquals(self.calculate(156170.0, 8898.0), 1389600660.00)

    def test0720(self):
        self.assertEquals(self.calculate(-177343.0, 56967.0), -10102698681.00)

    def test0721(self):
        self.assertEquals(self.calculate(32400.0, 13049.0), 422787600.00)

    def test0722(self):
        self.assertEquals(self.calculate(-183788.0, 103478.0), -19018014664.00)

    def test0723(self):
        self.assertEquals(self.calculate(185388.0, -157921.0), -29276658348.00)

    def test0724(self):
        self.assertEquals(self.calculate(-93152.0, -2097.0), 195339744.00)

    def test0725(self):
        self.assertEquals(self.calculate(-141096.0, 40617.0), -5730896232.00)

    def test0726(self):
        self.assertEquals(self.calculate(-136047.0, -168758.0), 22959019626.00)

    def test0727(self):
        self.assertEquals(self.calculate(-149013.0, -127007.0), 18925694091.00)

    def test0728(self):
        self.assertEquals(self.calculate(39657.0, -73346.0), -2908682322.00)

    def test0729(self):
        self.assertEquals(self.calculate(69763.0, 146314.0), 10207303582.00)

    def test0730(self):
        self.assertEquals(self.calculate(143214.0, -30682.0), -4394091948.00)

    def test0731(self):
        self.assertEquals(self.calculate(-63048.0, 41042.0), -2587616016.00)

    def test0732(self):
        self.assertEquals(self.calculate(-187697.0, -95380.0), 17902539860.00)

    def test0733(self):
        self.assertEquals(self.calculate(-14212.0, 53977.0), -767121124.00)

    def test0734(self):
        self.assertEquals(self.calculate(-186380.0, 196200.0), -36567756000.00)

    def test0735(self):
        self.assertEquals(self.calculate(-183405.0, 91246.0), -16734972630.00)

    def test0736(self):
        self.assertEquals(self.calculate(40609.0, 151898.0), 6168425882.00)

    def test0737(self):
        self.assertEquals(self.calculate(-28331.0, -540.0), 15298740.00)

    def test0738(self):
        self.assertEquals(self.calculate(79698.0, 60356.0), 4810252488.00)

    def test0739(self):
        self.assertEquals(self.calculate(180712.0, 139193.0), 25153845416.00)

    def test0740(self):
        self.assertEquals(self.calculate(-123517.0, -114259.0), 14112928903.00)

    def test0741(self):
        self.assertEquals(self.calculate(-190866.0, 72303.0), -13800184398.00)

    def test0742(self):
        self.assertEquals(self.calculate(-75624.0, 29178.0), -2206557072.00)

    def test0743(self):
        self.assertEquals(self.calculate(188377.0, -15843.0), -2984456811.00)

    def test0744(self):
        self.assertEquals(self.calculate(88173.0, 197224.0), 17389831752.00)

    def test0745(self):
        self.assertEquals(self.calculate(125126.0, -10014.0), -1253011764.00)

    def test0746(self):
        self.assertEquals(self.calculate(124174.0, 16188.0), 2010128712.00)

    def test0747(self):
        self.assertEquals(self.calculate(123120.0, -129371.0), -15928157520.00)

    def test0748(self):
        self.assertEquals(self.calculate(185020.0, 121503.0), 22480485060.00)

    def test0749(self):
        self.assertEquals(self.calculate(174643.0, -164604.0), -28746936372.00)

    def test0750(self):
        self.assertEquals(self.calculate(-198681.0, -185830.0), 36920890230.00)

    def test0751(self):
        self.assertEquals(self.calculate(-95499.0, 82306.0), -7860140694.00)

    def test0752(self):
        self.assertEquals(self.calculate(-158049.0, 180959.0), -28600388991.00)

    def test0753(self):
        self.assertEquals(self.calculate(178597.0, 147256.0), 26299479832.00)

    def test0754(self):
        self.assertEquals(self.calculate(166436.0, -169706.0), -28245187816.00)

    def test0755(self):
        self.assertEquals(self.calculate(-60757.0, 51347.0), -3119689679.00)

    def test0756(self):
        self.assertEquals(self.calculate(64808.0, 83384.0), 5403950272.00)

    def test0757(self):
        self.assertEquals(self.calculate(118372.0, 71853.0), 8505383316.00)

    def test0758(self):
        self.assertEquals(self.calculate(63796.0, 94641.0), 6037717236.00)

    def test0759(self):
        self.assertEquals(self.calculate(-148386.0, 104951.0), -15573259086.00)

    def test0760(self):
        self.assertEquals(self.calculate(-93210.0, -194104.0), 18092433840.00)

    def test0761(self):
        self.assertEquals(self.calculate(-31488.0, -85597.0), 2695278336.00)

    def test0762(self):
        self.assertEquals(self.calculate(152810.0, -78691.0), -12024771710.00)

    def test0763(self):
        self.assertEquals(self.calculate(114470.0, 14152.0), 1619979440.00)

    def test0764(self):
        self.assertEquals(self.calculate(-176500.0, 45427.0), -8017865500.00)

    def test0765(self):
        self.assertEquals(self.calculate(-99729.0, -71567.0), 7137305343.00)

    def test0766(self):
        self.assertEquals(self.calculate(80501.0, 103791.0), 8355279291.00)

    def test0767(self):
        self.assertEquals(self.calculate(183230.0, 175180.0), 32098231400.00)

    def test0768(self):
        self.assertEquals(self.calculate(14549.0, 103829.0), 1510608121.00)

    def test0769(self):
        self.assertEquals(self.calculate(10395.0, 4500.0), 46777500.00)

    def test0770(self):
        self.assertEquals(self.calculate(-62129.0, 158196.0), -9828559284.00)

    def test0771(self):
        self.assertEquals(self.calculate(114145.0, 72717.0), 8300281965.00)

    def test0772(self):
        self.assertEquals(self.calculate(52535.0, -142466.0), -7484451310.00)

    def test0773(self):
        self.assertEquals(self.calculate(-146756.0, -15371.0), 2255786476.00)

    def test0774(self):
        self.assertEquals(self.calculate(49264.0, -107888.0), -5314994432.00)

    def test0775(self):
        self.assertEquals(self.calculate(-27221.0, -180759.0), 4920440739.00)

    def test0776(self):
        self.assertEquals(self.calculate(-28432.0, -36364.0), 1033901248.00)

    def test0777(self):
        self.assertEquals(self.calculate(114400.0, -8168.0), -934419200.00)

    def test0778(self):
        self.assertEquals(self.calculate(26922.0, 180026.0), 4846659972.00)

    def test0779(self):
        self.assertEquals(self.calculate(-193302.0, 66217.0), -12799878534.00)

    def test0780(self):
        self.assertEquals(self.calculate(127774.0, 140707.0), 17978696218.00)

    def test0781(self):
        self.assertEquals(self.calculate(149175.0, -138488.0), -20658947400.00)

    def test0782(self):
        self.assertEquals(self.calculate(-142715.0, -126625.0), 18071286875.00)

    def test0783(self):
        self.assertEquals(self.calculate(125337.0, -169759.0), -21277083783.00)

    def test0784(self):
        self.assertEquals(self.calculate(83231.0, 153038.0), 12737505778.00)

    def test0785(self):
        self.assertEquals(self.calculate(172412.0, -169728.0), -29263143936.00)

    def test0786(self):
        self.assertEquals(self.calculate(159838.0, 88169.0), 14092756622.00)

    def test0787(self):
        self.assertEquals(self.calculate(128978.0, 192605.0), 24841807690.00)

    def test0788(self):
        self.assertEquals(self.calculate(175020.0, 25076.0), 4388801520.00)

    def test0789(self):
        self.assertEquals(self.calculate(14266.0, 107149.0), 1528587634.00)

    def test0790(self):
        self.assertEquals(self.calculate(-116150.0, -184757.0), 21459525550.00)

    def test0791(self):
        self.assertEquals(self.calculate(119499.0, 180028.0), 21513165972.00)

    def test0792(self):
        self.assertEquals(self.calculate(14714.0, -35452.0), -521640728.00)

    def test0793(self):
        self.assertEquals(self.calculate(48093.0, -20180.0), -970516740.00)

    def test0794(self):
        self.assertEquals(self.calculate(-163749.0, -70592.0), 11559369408.00)

    def test0795(self):
        self.assertEquals(self.calculate(-140016.0, -60390.0), 8455566240.00)

    def test0796(self):
        self.assertEquals(self.calculate(-118124.0, -69791.0), 8243992084.00)

    def test0797(self):
        self.assertEquals(self.calculate(74580.0, 9427.0), 703065660.00)

    def test0798(self):
        self.assertEquals(self.calculate(-168141.0, 49911.0), -8392085451.00)

    def test0799(self):
        self.assertEquals(self.calculate(-113014.0, -183755.0), 20766887570.00)

    def test0800(self):
        self.assertEquals(self.calculate(-65408.0, 97208.0), -6358180864.00)

    def test0801(self):
        self.assertEquals(self.calculate(120779.0, -70625.0), -8530016875.00)

    def test0802(self):
        self.assertEquals(self.calculate(-197588.0, -168632.0), 33319659616.00)

    def test0803(self):
        self.assertEquals(self.calculate(51240.0, 75113.0), 3848790120.00)

    def test0804(self):
        self.assertEquals(self.calculate(141591.0, -16973.0), -2403224043.00)

    def test0805(self):
        self.assertEquals(self.calculate(-16927.0, 180768.0), -3059859936.00)

    def test0806(self):
        self.assertEquals(self.calculate(14049.0, -97531.0), -1370213019.00)

    def test0807(self):
        self.assertEquals(self.calculate(-31585.0, -29789.0), 940885565.00)

    def test0808(self):
        self.assertEquals(self.calculate(105288.0, 8578.0), 903160464.00)

    def test0809(self):
        self.assertEquals(self.calculate(48181.0, 156328.0), 7532039368.00)

    def test0810(self):
        self.assertEquals(self.calculate(-134333.0, -112291.0), 15084386903.00)

    def test0811(self):
        self.assertEquals(self.calculate(-175755.0, -112449.0), 19763473995.00)

    def test0812(self):
        self.assertEquals(self.calculate(-124835.0, 5269.0), -657755615.00)

    def test0813(self):
        self.assertEquals(self.calculate(-49823.0, 161357.0), -8039289811.00)

    def test0814(self):
        self.assertEquals(self.calculate(153098.0, 14513.0), 2221911274.00)

    def test0815(self):
        self.assertEquals(self.calculate(-68487.0, -6198.0), 424482426.00)

    def test0816(self):
        self.assertEquals(self.calculate(-99299.0, -41756.0), 4146329044.00)

    def test0817(self):
        self.assertEquals(self.calculate(148279.0, -20021.0), -2968693859.00)

    def test0818(self):
        self.assertEquals(self.calculate(70891.0, -181103.0), -12838572773.00)

    def test0819(self):
        self.assertEquals(self.calculate(126507.0, -151109.0), -19116346263.00)

    def test0820(self):
        self.assertEquals(self.calculate(6864.0, -191119.0), -1311840816.00)

    def test0821(self):
        self.assertEquals(self.calculate(127971.0, -951.0), -121700421.00)

    def test0822(self):
        self.assertEquals(self.calculate(-17543.0, 147657.0), -2590346751.00)

    def test0823(self):
        self.assertEquals(self.calculate(149307.0, 49150.0), 7338439050.00)

    def test0824(self):
        self.assertEquals(self.calculate(-22190.0, -4040.0), 89647600.00)

    def test0825(self):
        self.assertEquals(self.calculate(-120332.0, 170395.0), -20503971140.00)

    def test0826(self):
        self.assertEquals(self.calculate(127471.0, -186303.0), -23748229713.00)

    def test0827(self):
        self.assertEquals(self.calculate(14580.0, 81038.0), 1181534040.00)

    def test0828(self):
        self.assertEquals(self.calculate(195874.0, -153315.0), -30030422310.00)

    def test0829(self):
        self.assertEquals(self.calculate(149443.0, -169953.0), -25398286179.00)

    def test0830(self):
        self.assertEquals(self.calculate(20693.0, 181041.0), 3746281413.00)

    def test0831(self):
        self.assertEquals(self.calculate(141381.0, 169452.0), 23957293212.00)

    def test0832(self):
        self.assertEquals(self.calculate(-86586.0, -9101.0), 788019186.00)

    def test0833(self):
        self.assertEquals(self.calculate(42592.0, -105302.0), -4485022784.00)

    def test0834(self):
        self.assertEquals(self.calculate(3950.0, -193938.0), -766055100.00)

    def test0835(self):
        self.assertEquals(self.calculate(6660.0, 154173.0), 1026792180.00)

    def test0836(self):
        self.assertEquals(self.calculate(-186707.0, 14505.0), -2708185035.00)

    def test0837(self):
        self.assertEquals(self.calculate(-172828.0, 42485.0), -7342597580.00)

    def test0838(self):
        self.assertEquals(self.calculate(40072.0, 31931.0), 1279539032.00)

    def test0839(self):
        self.assertEquals(self.calculate(67952.0, 92458.0), 6282706016.00)

    def test0840(self):
        self.assertEquals(self.calculate(-60867.0, -94409.0), 5746392603.00)

    def test0841(self):
        self.assertEquals(self.calculate(-46898.0, -126409.0), 5928329282.00)

    def test0842(self):
        self.assertEquals(self.calculate(23622.0, -18716.0), -442109352.00)

    def test0843(self):
        self.assertEquals(self.calculate(105182.0, 148753.0), 15646138046.00)

    def test0844(self):
        self.assertEquals(self.calculate(-60332.0, 24497.0), -1477953004.00)

    def test0845(self):
        self.assertEquals(self.calculate(96503.0, 71116.0), 6862907348.00)

    def test0846(self):
        self.assertEquals(self.calculate(-4814.0, -184690.0), 889097660.00)

    def test0847(self):
        self.assertEquals(self.calculate(-22299.0, -132055.0), 2944694445.00)

    def test0848(self):
        self.assertEquals(self.calculate(90166.0, 94479.0), 8518793514.00)

    def test0849(self):
        self.assertEquals(self.calculate(-86400.0, 44505.0), -3845232000.00)

    def test0850(self):
        self.assertEquals(self.calculate(-73391.0, 151377.0), -11109709407.00)

    def test0851(self):
        self.assertEquals(self.calculate(4379.0, 138438.0), 606220002.00)

    def test0852(self):
        self.assertEquals(self.calculate(191392.0, -189227.0), -36216533984.00)

    def test0853(self):
        self.assertEquals(self.calculate(-164440.0, -65426.0), 10758651440.00)

    def test0854(self):
        self.assertEquals(self.calculate(-123794.0, -28663.0), 3548307422.00)

    def test0855(self):
        self.assertEquals(self.calculate(156540.0, -99397.0), -15559606380.00)

    def test0856(self):
        self.assertEquals(self.calculate(-192813.0, 69593.0), -13418435109.00)

    def test0857(self):
        self.assertEquals(self.calculate(-177644.0, -33843.0), 6012005892.00)

    def test0858(self):
        self.assertEquals(self.calculate(43687.0, -153445.0), -6703551715.00)

    def test0859(self):
        self.assertEquals(self.calculate(-136998.0, -1429.0), 195770142.00)

    def test0860(self):
        self.assertEquals(self.calculate(-84619.0, -122733.0), 10385543727.00)

    def test0861(self):
        self.assertEquals(self.calculate(-188135.0, 115619.0), -21751980565.00)

    def test0862(self):
        self.assertEquals(self.calculate(109261.0, 2009.0), 219505349.00)

    def test0863(self):
        self.assertEquals(self.calculate(86621.0, -124920.0), -10820695320.00)

    def test0864(self):
        self.assertEquals(self.calculate(115848.0, -172300.0), -19960610400.00)

    def test0865(self):
        self.assertEquals(self.calculate(31355.0, -45680.0), -1432296400.00)

    def test0866(self):
        self.assertEquals(self.calculate(77395.0, -129578.0), -10028689310.00)

    def test0867(self):
        self.assertEquals(self.calculate(184828.0, -131698.0), -24341477944.00)

    def test0868(self):
        self.assertEquals(self.calculate(-160193.0, -155868.0), 24968962524.00)

    def test0869(self):
        self.assertEquals(self.calculate(198201.0, -152472.0), -30220102872.00)

    def test0870(self):
        self.assertEquals(self.calculate(-30078.0, 85711.0), -2578015458.00)

    def test0871(self):
        self.assertEquals(self.calculate(178513.0, -162786.0), -29059417218.00)

    def test0872(self):
        self.assertEquals(self.calculate(-50751.0, -57006.0), 2893111506.00)

    def test0873(self):
        self.assertEquals(self.calculate(195318.0, -123156.0), -24054583608.00)

    def test0874(self):
        self.assertEquals(self.calculate(51939.0, -46198.0), -2399477922.00)

    def test0875(self):
        self.assertEquals(self.calculate(11931.0, 182421.0), 2176464951.00)

    def test0876(self):
        self.assertEquals(self.calculate(-75866.0, 161863.0), -12279898358.00)

    def test0877(self):
        self.assertEquals(self.calculate(-110479.0, -148479.0), 16403811441.00)

    def test0878(self):
        self.assertEquals(self.calculate(66100.0, -60083.0), -3971486300.00)

    def test0879(self):
        self.assertEquals(self.calculate(163195.0, 10834.0), 1768054630.00)

    def test0880(self):
        self.assertEquals(self.calculate(-125600.0, -166194.0), 20873966400.00)

    def test0881(self):
        self.assertEquals(self.calculate(25447.0, 131197.0), 3338570059.00)

    def test0882(self):
        self.assertEquals(self.calculate(-186200.0, 69881.0), -13011842200.00)

    def test0883(self):
        self.assertEquals(self.calculate(-116347.0, 173319.0), -20165145693.00)

    def test0884(self):
        self.assertEquals(self.calculate(-115210.0, -196956.0), 22691300760.00)

    def test0885(self):
        self.assertEquals(self.calculate(136920.0, 112535.0), 15408292200.00)

    def test0886(self):
        self.assertEquals(self.calculate(-112235.0, -57028.0), 6400537580.00)

    def test0887(self):
        self.assertEquals(self.calculate(66220.0, -150714.0), -9980281080.00)

    def test0888(self):
        self.assertEquals(self.calculate(-151301.0, 13377.0), -2023953477.00)

    def test0889(self):
        self.assertEquals(self.calculate(92017.0, 41550.0), 3823306350.00)

    def test0890(self):
        self.assertEquals(self.calculate(101442.0, -104667.0), -10617629814.00)

    def test0891(self):
        self.assertEquals(self.calculate(-70698.0, 10303.0), -728401494.00)

    def test0892(self):
        self.assertEquals(self.calculate(-179205.0, -137238.0), 24593735790.00)

    def test0893(self):
        self.assertEquals(self.calculate(-57092.0, 116709.0), -6663150228.00)

    def test0894(self):
        self.assertEquals(self.calculate(-178739.0, 65069.0), -11630367991.00)

    def test0895(self):
        self.assertEquals(self.calculate(-54059.0, 89430.0), -4834496370.00)

    def test0896(self):
        self.assertEquals(self.calculate(-104973.0, -145645.0), 15288792585.00)

    def test0897(self):
        self.assertEquals(self.calculate(-64660.0, 164403.0), -10630297980.00)

    def test0898(self):
        self.assertEquals(self.calculate(116070.0, 129278.0), 15005297460.00)

    def test0899(self):
        self.assertEquals(self.calculate(-154034.0, -42281.0), 6512711554.00)

    def test0900(self):
        self.assertEquals(self.calculate(122359.0, -161621.0), -19775783939.00)

    def test0901(self):
        self.assertEquals(self.calculate(119840.0, -48275.0), -5785276000.00)

    def test0902(self):
        self.assertEquals(self.calculate(-31114.0, -105694.0), 3288563116.00)

    def test0903(self):
        self.assertEquals(self.calculate(-84431.0, 14679.0), -1239362649.00)

    def test0904(self):
        self.assertEquals(self.calculate(-56295.0, 168973.0), -9512335035.00)

    def test0905(self):
        self.assertEquals(self.calculate(-108703.0, -45329.0), 4927398287.00)

    def test0906(self):
        self.assertEquals(self.calculate(51339.0, 102608.0), 5267792112.00)

    def test0907(self):
        self.assertEquals(self.calculate(-165819.0, -190990.0), 31669770810.00)

    def test0908(self):
        self.assertEquals(self.calculate(-21351.0, -66121.0), 1411749471.00)

    def test0909(self):
        self.assertEquals(self.calculate(-34257.0, -167776.0), 5747502432.00)

    def test0910(self):
        self.assertEquals(self.calculate(92000.0, 185106.0), 17029752000.00)

    def test0911(self):
        self.assertEquals(self.calculate(15050.0, 134631.0), 2026196550.00)

    def test0912(self):
        self.assertEquals(self.calculate(-89698.0, -64430.0), 5779242140.00)

    def test0913(self):
        self.assertEquals(self.calculate(107593.0, -170801.0), -18376991993.00)

    def test0914(self):
        self.assertEquals(self.calculate(-111879.0, -144196.0), 16132504284.00)

    def test0915(self):
        self.assertEquals(self.calculate(-138987.0, -101406.0), 14094115722.00)

    def test0916(self):
        self.assertEquals(self.calculate(134570.0, -56859.0), -7651515630.00)

    def test0917(self):
        self.assertEquals(self.calculate(-55896.0, -188482.0), 10535389872.00)

    def test0918(self):
        self.assertEquals(self.calculate(-77086.0, -86897.0), 6698542142.00)

    def test0919(self):
        self.assertEquals(self.calculate(-170708.0, -73532.0), 12552500656.00)

    def test0920(self):
        self.assertEquals(self.calculate(172089.0, -43168.0), -7428737952.00)

    def test0921(self):
        self.assertEquals(self.calculate(125301.0, -152074.0), -19055024274.00)

    def test0922(self):
        self.assertEquals(self.calculate(-50446.0, -120907.0), 6099274522.00)

    def test0923(self):
        self.assertEquals(self.calculate(-22619.0, 98404.0), -2225800076.00)

    def test0924(self):
        self.assertEquals(self.calculate(-177025.0, 107442.0), -19019920050.00)

    def test0925(self):
        self.assertEquals(self.calculate(-3712.0, 29572.0), -109771264.00)

    def test0926(self):
        self.assertEquals(self.calculate(-166907.0, -353.0), 58918171.00)

    def test0927(self):
        self.assertEquals(self.calculate(-59038.0, -143135.0), 8450404130.00)

    def test0928(self):
        self.assertEquals(self.calculate(176163.0, -142232.0), -25056015816.00)

    def test0929(self):
        self.assertEquals(self.calculate(49521.0, -98248.0), -4865339208.00)

    def test0930(self):
        self.assertEquals(self.calculate(6595.0, -32456.0), -214047320.00)

    def test0931(self):
        self.assertEquals(self.calculate(84198.0, 41840.0), 3522844320.00)

    def test0932(self):
        self.assertEquals(self.calculate(-45005.0, 62651.0), -2819608255.00)

    def test0933(self):
        self.assertEquals(self.calculate(130791.0, 96058.0), 12563521878.00)

    def test0934(self):
        self.assertEquals(self.calculate(-133844.0, 131112.0), -17548554528.00)

    def test0935(self):
        self.assertEquals(self.calculate(82484.0, 144491.0), 11918195644.00)

    def test0936(self):
        self.assertEquals(self.calculate(-9967.0, -85096.0), 848151832.00)

    def test0937(self):
        self.assertEquals(self.calculate(38320.0, 106106.0), 4065981920.00)

    def test0938(self):
        self.assertEquals(self.calculate(79749.0, -22508.0), -1794990492.00)

    def test0939(self):
        self.assertEquals(self.calculate(-64557.0, -167344.0), 10803226608.00)

    def test0940(self):
        self.assertEquals(self.calculate(-36271.0, -160204.0), 5810759284.00)

    def test0941(self):
        self.assertEquals(self.calculate(-120157.0, -111595.0), 13408920415.00)

    def test0942(self):
        self.assertEquals(self.calculate(81014.0, 124260.0), 10066799640.00)

    def test0943(self):
        self.assertEquals(self.calculate(37362.0, -32808.0), -1225772496.00)

    def test0944(self):
        self.assertEquals(self.calculate(135502.0, 27359.0), 3707199218.00)

    def test0945(self):
        self.assertEquals(self.calculate(-95850.0, 94240.0), -9032904000.00)

    def test0946(self):
        self.assertEquals(self.calculate(-178708.0, -23463.0), 4193025804.00)

    def test0947(self):
        self.assertEquals(self.calculate(-52178.0, 70288.0), -3667487264.00)

    def test0948(self):
        self.assertEquals(self.calculate(83258.0, 23351.0), 1944157558.00)

    def test0949(self):
        self.assertEquals(self.calculate(-46479.0, -14834.0), 689469486.00)

    def test0950(self):
        self.assertEquals(self.calculate(-100210.0, 106334.0), -10655730140.00)

    def test0951(self):
        self.assertEquals(self.calculate(12171.0, -130019.0), -1582461249.00)

    def test0952(self):
        self.assertEquals(self.calculate(177519.0, -112857.0), -20034261783.00)

    def test0953(self):
        self.assertEquals(self.calculate(192942.0, 163777.0), 31599461934.00)

    def test0954(self):
        self.assertEquals(self.calculate(-73037.0, -125352.0), 9155334024.00)

    def test0955(self):
        self.assertEquals(self.calculate(137331.0, 87581.0), 12027586311.00)

    def test0956(self):
        self.assertEquals(self.calculate(126920.0, -55219.0), -7008395480.00)

    def test0957(self):
        self.assertEquals(self.calculate(-116588.0, -187844.0), 21900356272.00)

    def test0958(self):
        self.assertEquals(self.calculate(-99722.0, 157118.0), -15668121196.00)

    def test0959(self):
        self.assertEquals(self.calculate(-127459.0, 139643.0), -17798757137.00)

    def test0960(self):
        self.assertEquals(self.calculate(-19057.0, 121811.0), -2321352227.00)

    def test0961(self):
        self.assertEquals(self.calculate(-54966.0, 158961.0), -8737450326.00)

    def test0962(self):
        self.assertEquals(self.calculate(180000.0, -196098.0), -35297640000.00)

    def test0963(self):
        self.assertEquals(self.calculate(68646.0, -74134.0), -5089002564.00)

    def test0964(self):
        self.assertEquals(self.calculate(24345.0, 145331.0), 3538083195.00)

    def test0965(self):
        self.assertEquals(self.calculate(-151541.0, -26172.0), 3966131052.00)

    def test0966(self):
        self.assertEquals(self.calculate(51610.0, -155603.0), -8030670830.00)

    def test0967(self):
        self.assertEquals(self.calculate(103944.0, -55608.0), -5780117952.00)

    def test0968(self):
        self.assertEquals(self.calculate(-33956.0, -123182.0), 4182767992.00)

    def test0969(self):
        self.assertEquals(self.calculate(71257.0, -82323.0), -5866090011.00)

    def test0970(self):
        self.assertEquals(self.calculate(-126627.0, -92115.0), 11664246105.00)

    def test0971(self):
        self.assertEquals(self.calculate(-77782.0, -81034.0), 6302986588.00)

    def test0972(self):
        self.assertEquals(self.calculate(113270.0, 41372.0), 4686206440.00)

    def test0973(self):
        self.assertEquals(self.calculate(-119590.0, -102063.0), 12205714170.00)

    def test0974(self):
        self.assertEquals(self.calculate(127608.0, -186132.0), -23751932256.00)

    def test0975(self):
        self.assertEquals(self.calculate(-44354.0, -94584.0), 4195178736.00)

    def test0976(self):
        self.assertEquals(self.calculate(55414.0, -83592.0), -4632167088.00)

    def test0977(self):
        self.assertEquals(self.calculate(161300.0, -189655.0), -30591351500.00)

    def test0978(self):
        self.assertEquals(self.calculate(164807.0, -192915.0), -31793742405.00)

    def test0979(self):
        self.assertEquals(self.calculate(-35599.0, 67610.0), -2406848390.00)

    def test0980(self):
        self.assertEquals(self.calculate(124870.0, -146281.0), -18266108470.00)

    def test0981(self):
        self.assertEquals(self.calculate(-81285.0, 44907.0), -3650265495.00)

    def test0982(self):
        self.assertEquals(self.calculate(-75215.0, -29959.0), 2253366185.00)

    def test0983(self):
        self.assertEquals(self.calculate(71414.0, 91162.0), 6510243068.00)

    def test0984(self):
        self.assertEquals(self.calculate(139375.0, 44117.0), 6148806875.00)

    def test0985(self):
        self.assertEquals(self.calculate(166655.0, 5724.0), 953933220.00)

    def test0986(self):
        self.assertEquals(self.calculate(-175707.0, 42802.0), -7520611014.00)

    def test0987(self):
        self.assertEquals(self.calculate(-124359.0, -170273.0), 21174980007.00)

    def test0988(self):
        self.assertEquals(self.calculate(191000.0, 135588.0), 25897308000.00)

    def test0989(self):
        self.assertEquals(self.calculate(146750.0, 189332.0), 27784471000.00)

    def test0990(self):
        self.assertEquals(self.calculate(-1398.0, 163976.0), -229238448.00)

    def test0991(self):
        self.assertEquals(self.calculate(-189633.0, -87116.0), 16520068428.00)

    def test0992(self):
        self.assertEquals(self.calculate(162189.0, -30607.0), -4964118723.00)

    def test0993(self):
        self.assertEquals(self.calculate(84704.0, -43796.0), -3709696384.00)

    def test0994(self):
        self.assertEquals(self.calculate(161754.0, -164486.0), -26606268444.00)

    def test0995(self):
        self.assertEquals(self.calculate(-47521.0, 199999.0), -9504152479.00)

    def test0996(self):
        self.assertEquals(self.calculate(-20673.0, -140845.0), 2911688685.00)

    def test0997(self):
        self.assertEquals(self.calculate(62781.0, 151548.0), 9514334988.00)

    def test0998(self):
        self.assertEquals(self.calculate(-130270.0, 87136.0), -11351206720.00)

    def test0999(self):
        self.assertEquals(self.calculate(-123616.0, -136356.0), 16855783296.00)

    def test1000(self):
        self.assertEquals(self.calculate(-187423.0, -197586.0), 37032160878.00)

    def test1001(self):
        self.assertEquals(self.calculate(94902.0, 25332.0), 2404057464.00)

    def test1002(self):
        self.assertEquals(self.calculate(-70979.0, -169538.0), 12033637702.00)

    def test1003(self):
        self.assertEquals(self.calculate(-144605.0, -95780.0), 13850266900.00)

    def test1004(self):
        self.assertEquals(self.calculate(19596.0, 79443.0), 1556765028.00)

    def test1005(self):
        self.assertEquals(self.calculate(122226.0, -66443.0), -8121062118.00)

    def test1006(self):
        self.assertEquals(self.calculate(183132.0, -74499.0), -13643150868.00)

    def test1007(self):
        self.assertEquals(self.calculate(-75081.0, 47360.0), -3555836160.00)

    def test1008(self):
        self.assertEquals(self.calculate(163851.0, 42598.0), 6979724898.00)

    def test1009(self):
        self.assertEquals(self.calculate(-112769.0, -47541.0), 5361151029.00)

    def test1010(self):
        self.assertEquals(self.calculate(78192.0, 121521.0), 9501970032.00)

    def test1011(self):
        self.assertEquals(self.calculate(32818.0, 100634.0), 3302606612.00)

    def test1012(self):
        self.assertEquals(self.calculate(118709.0, 22956.0), 2725083804.00)

    def test1013(self):
        self.assertEquals(self.calculate(90185.0, 103289.0), 9315118465.00)

    def test1014(self):
        self.assertEquals(self.calculate(-78986.0, 43224.0), -3414090864.00)

    def test1015(self):
        self.assertEquals(self.calculate(171511.0, -72715.0), -12471422365.00)

    def test1016(self):
        self.assertEquals(self.calculate(-176580.0, -77741.0), 13727505780.00)

    def test1017(self):
        self.assertEquals(self.calculate(-108780.0, 168906.0), -18373594680.00)

    def test1018(self):
        self.assertEquals(self.calculate(151225.0, -194657.0), -29437004825.00)

    def test1019(self):
        self.assertEquals(self.calculate(-63627.0, 195225.0), -12421581075.00)

    def test1020(self):
        self.assertEquals(self.calculate(65028.0, 163159.0), 10609903452.00)

    def test1021(self):
        self.assertEquals(self.calculate(92839.0, -125898.0), -11688244422.00)

    def test1022(self):
        self.assertEquals(self.calculate(191541.0, -83848.0), -16060329768.00)

    def test1023(self):
        self.assertEquals(self.calculate(-112608.0, -55677.0), 6269675616.00)


#
unittest.main()

