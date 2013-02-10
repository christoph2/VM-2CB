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

class TestVM_Add_IntInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushW(rhs)
        v.VM_Add()
        res = v.VM_PopW()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-32708, 27128), -5580, "")

    def test0001(self):
        self.assertEquals(self.calculate(-32234, -11296), 22006, "")

    def test0002(self):
        self.assertEquals(self.calculate(31513, 12314), -21709, "")

    def test0003(self):
        self.assertEquals(self.calculate(-23433, 28861), 5428, "")

    def test0004(self):
        self.assertEquals(self.calculate(-20240, 22855), 2615, "")

    def test0005(self):
        self.assertEquals(self.calculate(-32641, -25847), 7048, "")

    def test0006(self):
        self.assertEquals(self.calculate(-12837, -7050), -19887, "")

    def test0007(self):
        self.assertEquals(self.calculate(-24943, 10535), -14408, "")

    def test0008(self):
        self.assertEquals(self.calculate(-10684, 27464), 16780, "")

    def test0009(self):
        self.assertEquals(self.calculate(-12156, -17989), -30145, "")

    def test0010(self):
        self.assertEquals(self.calculate(25610, 20789), -19137, "")

    def test0011(self):
        self.assertEquals(self.calculate(-27460, -9040), 29036, "")

    def test0012(self):
        self.assertEquals(self.calculate(6175, 30664), -28697, "")

    def test0013(self):
        self.assertEquals(self.calculate(26715, -16740), 9975, "")

    def test0014(self):
        self.assertEquals(self.calculate(-7096, 6853), -243, "")

    def test0015(self):
        self.assertEquals(self.calculate(-3108, -25109), -28217, "")

    def test0016(self):
        self.assertEquals(self.calculate(-30213, -9576), 25747, "")

    def test0017(self):
        self.assertEquals(self.calculate(-20669, -12708), 32159, "")

    def test0018(self):
        self.assertEquals(self.calculate(-25194, 19304), -5890, "")

    def test0019(self):
        self.assertEquals(self.calculate(-4908, -23287), -28195, "")

    def test0020(self):
        self.assertEquals(self.calculate(-16188, -11430), -27618, "")

    def test0021(self):
        self.assertEquals(self.calculate(30926, -15052), 15874, "")

    def test0022(self):
        self.assertEquals(self.calculate(19103, -12306), 6797, "")

    def test0023(self):
        self.assertEquals(self.calculate(3952, 15626), 19578, "")

    def test0024(self):
        self.assertEquals(self.calculate(14931, -10849), 4082, "")

    def test0025(self):
        self.assertEquals(self.calculate(-24109, 32011), 7902, "")

    def test0026(self):
        self.assertEquals(self.calculate(2963, -8025), -5062, "")

    def test0027(self):
        self.assertEquals(self.calculate(-27452, 18992), -8460, "")

    def test0028(self):
        self.assertEquals(self.calculate(-11856, -16), -11872, "")

    def test0029(self):
        self.assertEquals(self.calculate(-26599, -15626), 23311, "")

    def test0030(self):
        self.assertEquals(self.calculate(-29842, 19622), -10220, "")

    def test0031(self):
        self.assertEquals(self.calculate(31814, -8933), 22881, "")

    def test0032(self):
        self.assertEquals(self.calculate(3702, 3544), 7246, "")

    def test0033(self):
        self.assertEquals(self.calculate(-12689, -10298), -22987, "")

    def test0034(self):
        self.assertEquals(self.calculate(18236, -6293), 11943, "")

    def test0035(self):
        self.assertEquals(self.calculate(6132, 13783), 19915, "")

    def test0036(self):
        self.assertEquals(self.calculate(21429, 12890), -31217, "")

    def test0037(self):
        self.assertEquals(self.calculate(-27848, 8217), -19631, "")

    def test0038(self):
        self.assertEquals(self.calculate(-18201, -8663), -26864, "")

    def test0039(self):
        self.assertEquals(self.calculate(28120, -7809), 20311, "")

    def test0040(self):
        self.assertEquals(self.calculate(-6993, 32612), 25619, "")

    def test0041(self):
        self.assertEquals(self.calculate(-694, -15159), -15853, "")

    def test0042(self):
        self.assertEquals(self.calculate(-16254, 21490), 5236, "")

    def test0043(self):
        self.assertEquals(self.calculate(-3437, -23360), -26797, "")

    def test0044(self):
        self.assertEquals(self.calculate(-20237, -13788), 31511, "")

    def test0045(self):
        self.assertEquals(self.calculate(-16572, -5226), -21798, "")

    def test0046(self):
        self.assertEquals(self.calculate(-15789, 20402), 4613, "")

    def test0047(self):
        self.assertEquals(self.calculate(26342, 27216), -11978, "")

    def test0048(self):
        self.assertEquals(self.calculate(-8984, -1815), -10799, "")

    def test0049(self):
        self.assertEquals(self.calculate(9764, 6081), 15845, "")

    def test0050(self):
        self.assertEquals(self.calculate(-28040, -32175), 5321, "")

    def test0051(self):
        self.assertEquals(self.calculate(-28540, -30312), 6684, "")

    def test0052(self):
        self.assertEquals(self.calculate(-11187, 32625), 21438, "")

    def test0053(self):
        self.assertEquals(self.calculate(29518, 16909), -19109, "")

    def test0054(self):
        self.assertEquals(self.calculate(6647, -17979), -11332, "")

    def test0055(self):
        self.assertEquals(self.calculate(4715, 17366), 22081, "")

    def test0056(self):
        self.assertEquals(self.calculate(-26347, 10547), -15800, "")

    def test0057(self):
        self.assertEquals(self.calculate(24660, -13129), 11531, "")

    def test0058(self):
        self.assertEquals(self.calculate(-12413, 25801), 13388, "")

    def test0059(self):
        self.assertEquals(self.calculate(8295, 32699), -24542, "")

    def test0060(self):
        self.assertEquals(self.calculate(-26810, 5704), -21106, "")

    def test0061(self):
        self.assertEquals(self.calculate(13021, 17081), 30102, "")

    def test0062(self):
        self.assertEquals(self.calculate(5316, -32450), -27134, "")

    def test0063(self):
        self.assertEquals(self.calculate(-4966, 24011), 19045, "")

    def test0064(self):
        self.assertEquals(self.calculate(-17752, 9311), -8441, "")

    def test0065(self):
        self.assertEquals(self.calculate(7689, -17363), -9674, "")

    def test0066(self):
        self.assertEquals(self.calculate(-14581, -5158), -19739, "")

    def test0067(self):
        self.assertEquals(self.calculate(-13128, -19610), -32738, "")

    def test0068(self):
        self.assertEquals(self.calculate(16533, 9117), 25650, "")

    def test0069(self):
        self.assertEquals(self.calculate(-16315, -10922), -27237, "")

    def test0070(self):
        self.assertEquals(self.calculate(3929, -302), 3627, "")

    def test0071(self):
        self.assertEquals(self.calculate(-17373, 12535), -4838, "")

    def test0072(self):
        self.assertEquals(self.calculate(-15549, 11480), -4069, "")

    def test0073(self):
        self.assertEquals(self.calculate(15170, 17424), 32594, "")

    def test0074(self):
        self.assertEquals(self.calculate(-5524, -5585), -11109, "")

    def test0075(self):
        self.assertEquals(self.calculate(26751, 13163), -25622, "")

    def test0076(self):
        self.assertEquals(self.calculate(25860, 12129), -27547, "")

    def test0077(self):
        self.assertEquals(self.calculate(-32607, -30204), 2725, "")

    def test0078(self):
        self.assertEquals(self.calculate(3802, 7819), 11621, "")

    def test0079(self):
        self.assertEquals(self.calculate(24841, -14196), 10645, "")

    def test0080(self):
        self.assertEquals(self.calculate(23077, -29167), -6090, "")

    def test0081(self):
        self.assertEquals(self.calculate(-25909, -11006), 28621, "")

    def test0082(self):
        self.assertEquals(self.calculate(-14937, -10762), -25699, "")

    def test0083(self):
        self.assertEquals(self.calculate(27487, -26422), 1065, "")

    def test0084(self):
        self.assertEquals(self.calculate(-15303, -16266), -31569, "")

    def test0085(self):
        self.assertEquals(self.calculate(10587, 8842), 19429, "")

    def test0086(self):
        self.assertEquals(self.calculate(-2006, -23074), -25080, "")

    def test0087(self):
        self.assertEquals(self.calculate(-27750, -11995), 25791, "")

    def test0088(self):
        self.assertEquals(self.calculate(-22799, 28686), 5887, "")

    def test0089(self):
        self.assertEquals(self.calculate(-17795, 26842), 9047, "")

    def test0090(self):
        self.assertEquals(self.calculate(-2734, -31610), 31192, "")

    def test0091(self):
        self.assertEquals(self.calculate(-10885, -31336), 23315, "")

    def test0092(self):
        self.assertEquals(self.calculate(14620, -6787), 7833, "")

    def test0093(self):
        self.assertEquals(self.calculate(31257, -13304), 17953, "")

    def test0094(self):
        self.assertEquals(self.calculate(8003, 32054), -25479, "")

    def test0095(self):
        self.assertEquals(self.calculate(11642, 21356), -32538, "")

    def test0096(self):
        self.assertEquals(self.calculate(-16018, 8017), -8001, "")

    def test0097(self):
        self.assertEquals(self.calculate(-26288, 21208), -5080, "")

    def test0098(self):
        self.assertEquals(self.calculate(15794, -8883), 6911, "")

    def test0099(self):
        self.assertEquals(self.calculate(5900, -30211), -24311, "")

    def test0100(self):
        self.assertEquals(self.calculate(19418, 16222), -29896, "")

    def test0101(self):
        self.assertEquals(self.calculate(10418, -6544), 3874, "")

    def test0102(self):
        self.assertEquals(self.calculate(12108, 24252), -29176, "")

    def test0103(self):
        self.assertEquals(self.calculate(-2719, 15865), 13146, "")

    def test0104(self):
        self.assertEquals(self.calculate(-26365, -21295), 17876, "")

    def test0105(self):
        self.assertEquals(self.calculate(2727, 29757), 32484, "")

    def test0106(self):
        self.assertEquals(self.calculate(-30397, -11464), 23675, "")

    def test0107(self):
        self.assertEquals(self.calculate(10851, 21899), 32750, "")

    def test0108(self):
        self.assertEquals(self.calculate(23672, 15026), -26838, "")

    def test0109(self):
        self.assertEquals(self.calculate(-12886, -26351), 26299, "")

    def test0110(self):
        self.assertEquals(self.calculate(2555, 22194), 24749, "")

    def test0111(self):
        self.assertEquals(self.calculate(-6846, 20006), 13160, "")

    def test0112(self):
        self.assertEquals(self.calculate(17235, 5492), 22727, "")

    def test0113(self):
        self.assertEquals(self.calculate(-18684, 15568), -3116, "")

    def test0114(self):
        self.assertEquals(self.calculate(-8051, 11381), 3330, "")

    def test0115(self):
        self.assertEquals(self.calculate(26989, -1461), 25528, "")

    def test0116(self):
        self.assertEquals(self.calculate(13165, -20594), -7429, "")

    def test0117(self):
        self.assertEquals(self.calculate(-14998, -486), -15484, "")

    def test0118(self):
        self.assertEquals(self.calculate(-14586, -2742), -17328, "")

    def test0119(self):
        self.assertEquals(self.calculate(-17119, -11554), -28673, "")

    def test0120(self):
        self.assertEquals(self.calculate(-6379, -31053), 28104, "")

    def test0121(self):
        self.assertEquals(self.calculate(23843, 10802), -30891, "")

    def test0122(self):
        self.assertEquals(self.calculate(11114, -2266), 8848, "")

    def test0123(self):
        self.assertEquals(self.calculate(-26494, 11952), -14542, "")

    def test0124(self):
        self.assertEquals(self.calculate(-462, 22528), 22066, "")

    def test0125(self):
        self.assertEquals(self.calculate(-1110, 19960), 18850, "")

    def test0126(self):
        self.assertEquals(self.calculate(-29227, -13232), 23077, "")

    def test0127(self):
        self.assertEquals(self.calculate(25794, -7597), 18197, "")

    def test0128(self):
        self.assertEquals(self.calculate(-31090, 22115), -8975, "")

    def test0129(self):
        self.assertEquals(self.calculate(-17990, 25643), 7653, "")

    def test0130(self):
        self.assertEquals(self.calculate(-17748, -10388), -28136, "")

    def test0131(self):
        self.assertEquals(self.calculate(-2249, 10267), 8018, "")

    def test0132(self):
        self.assertEquals(self.calculate(4850, 23746), 28596, "")

    def test0133(self):
        self.assertEquals(self.calculate(27680, -10473), 17207, "")

    def test0134(self):
        self.assertEquals(self.calculate(8589, -26530), -17941, "")

    def test0135(self):
        self.assertEquals(self.calculate(11551, -2495), 9056, "")

    def test0136(self):
        self.assertEquals(self.calculate(-4456, 4073), -383, "")

    def test0137(self):
        self.assertEquals(self.calculate(23713, -30814), -7101, "")

    def test0138(self):
        self.assertEquals(self.calculate(-29396, 9307), -20089, "")

    def test0139(self):
        self.assertEquals(self.calculate(16182, 10638), 26820, "")

    def test0140(self):
        self.assertEquals(self.calculate(8324, -25783), -17459, "")

    def test0141(self):
        self.assertEquals(self.calculate(-16323, 21542), 5219, "")

    def test0142(self):
        self.assertEquals(self.calculate(-17200, 7619), -9581, "")

    def test0143(self):
        self.assertEquals(self.calculate(4998, 21380), 26378, "")

    def test0144(self):
        self.assertEquals(self.calculate(16626, -5817), 10809, "")

    def test0145(self):
        self.assertEquals(self.calculate(-18781, -28278), 18477, "")

    def test0146(self):
        self.assertEquals(self.calculate(-17190, 11994), -5196, "")

    def test0147(self):
        self.assertEquals(self.calculate(-18853, -6215), -25068, "")

    def test0148(self):
        self.assertEquals(self.calculate(28330, -3171), 25159, "")

    def test0149(self):
        self.assertEquals(self.calculate(-10701, -31636), 23199, "")

    def test0150(self):
        self.assertEquals(self.calculate(-14146, -8850), -22996, "")

    def test0151(self):
        self.assertEquals(self.calculate(-2072, -10867), -12939, "")

    def test0152(self):
        self.assertEquals(self.calculate(23458, -25041), -1583, "")

    def test0153(self):
        self.assertEquals(self.calculate(10097, -14022), -3925, "")

    def test0154(self):
        self.assertEquals(self.calculate(-23284, -24121), 18131, "")

    def test0155(self):
        self.assertEquals(self.calculate(21614, -17371), 4243, "")

    def test0156(self):
        self.assertEquals(self.calculate(-1577, -16823), -18400, "")

    def test0157(self):
        self.assertEquals(self.calculate(-12697, -7463), -20160, "")

    def test0158(self):
        self.assertEquals(self.calculate(-30059, 8694), -21365, "")

    def test0159(self):
        self.assertEquals(self.calculate(-20567, 20179), -388, "")

    def test0160(self):
        self.assertEquals(self.calculate(-12312, 10490), -1822, "")

    def test0161(self):
        self.assertEquals(self.calculate(18137, -26025), -7888, "")

    def test0162(self):
        self.assertEquals(self.calculate(-16317, -16589), 32630, "")

    def test0163(self):
        self.assertEquals(self.calculate(-22006, 2079), -19927, "")

    def test0164(self):
        self.assertEquals(self.calculate(-10647, -23057), 31832, "")

    def test0165(self):
        self.assertEquals(self.calculate(-185, 13753), 13568, "")

    def test0166(self):
        self.assertEquals(self.calculate(-24754, -30156), 10626, "")

    def test0167(self):
        self.assertEquals(self.calculate(-27704, -5017), -32721, "")

    def test0168(self):
        self.assertEquals(self.calculate(-16081, -4254), -20335, "")

    def test0169(self):
        self.assertEquals(self.calculate(-2566, -25617), -28183, "")

    def test0170(self):
        self.assertEquals(self.calculate(29622, -15607), 14015, "")

    def test0171(self):
        self.assertEquals(self.calculate(-16026, 17705), 1679, "")

    def test0172(self):
        self.assertEquals(self.calculate(30430, -30685), -255, "")

    def test0173(self):
        self.assertEquals(self.calculate(3619, -5683), -2064, "")

    def test0174(self):
        self.assertEquals(self.calculate(-5290, 13187), 7897, "")

    def test0175(self):
        self.assertEquals(self.calculate(1074, -17606), -16532, "")

    def test0176(self):
        self.assertEquals(self.calculate(18120, -2549), 15571, "")

    def test0177(self):
        self.assertEquals(self.calculate(-26287, 3638), -22649, "")

    def test0178(self):
        self.assertEquals(self.calculate(32722, -27211), 5511, "")

    def test0179(self):
        self.assertEquals(self.calculate(14972, 13991), 28963, "")

    def test0180(self):
        self.assertEquals(self.calculate(-11040, 16449), 5409, "")

    def test0181(self):
        self.assertEquals(self.calculate(14849, 21808), -28879, "")

    def test0182(self):
        self.assertEquals(self.calculate(3873, 18458), 22331, "")

    def test0183(self):
        self.assertEquals(self.calculate(-6234, -3397), -9631, "")

    def test0184(self):
        self.assertEquals(self.calculate(1681, -28297), -26616, "")

    def test0185(self):
        self.assertEquals(self.calculate(-27191, 31343), 4152, "")

    def test0186(self):
        self.assertEquals(self.calculate(-6858, -24114), -30972, "")

    def test0187(self):
        self.assertEquals(self.calculate(-15906, -5456), -21362, "")

    def test0188(self):
        self.assertEquals(self.calculate(-4605, 22558), 17953, "")

    def test0189(self):
        self.assertEquals(self.calculate(-937, 16026), 15089, "")

    def test0190(self):
        self.assertEquals(self.calculate(-15432, -18076), 32028, "")

    def test0191(self):
        self.assertEquals(self.calculate(30285, -2827), 27458, "")

    def test0192(self):
        self.assertEquals(self.calculate(15964, -1567), 14397, "")

    def test0193(self):
        self.assertEquals(self.calculate(-28719, -16118), 20699, "")

    def test0194(self):
        self.assertEquals(self.calculate(-10771, 69), -10702, "")

    def test0195(self):
        self.assertEquals(self.calculate(-21762, -23662), 20112, "")

    def test0196(self):
        self.assertEquals(self.calculate(29854, 30381), -5301, "")

    def test0197(self):
        self.assertEquals(self.calculate(2357, -5175), -2818, "")

    def test0198(self):
        self.assertEquals(self.calculate(25409, 154), 25563, "")

    def test0199(self):
        self.assertEquals(self.calculate(29412, 12349), -23775, "")

    def test0200(self):
        self.assertEquals(self.calculate(27155, 13566), -24815, "")

    def test0201(self):
        self.assertEquals(self.calculate(16908, 14399), 31307, "")

    def test0202(self):
        self.assertEquals(self.calculate(3807, -19405), -15598, "")

    def test0203(self):
        self.assertEquals(self.calculate(-27474, 4446), -23028, "")

    def test0204(self):
        self.assertEquals(self.calculate(-15607, -27060), 22869, "")

    def test0205(self):
        self.assertEquals(self.calculate(-20315, -20942), 24279, "")

    def test0206(self):
        self.assertEquals(self.calculate(-19568, -29489), 16479, "")

    def test0207(self):
        self.assertEquals(self.calculate(26177, -21095), 5082, "")

    def test0208(self):
        self.assertEquals(self.calculate(-4191, -23942), -28133, "")

    def test0209(self):
        self.assertEquals(self.calculate(9632, -17745), -8113, "")

    def test0210(self):
        self.assertEquals(self.calculate(12649, -28031), -15382, "")

    def test0211(self):
        self.assertEquals(self.calculate(25999, -14319), 11680, "")

    def test0212(self):
        self.assertEquals(self.calculate(13951, -24584), -10633, "")

    def test0213(self):
        self.assertEquals(self.calculate(19920, 23049), -22567, "")

    def test0214(self):
        self.assertEquals(self.calculate(6824, 12871), 19695, "")

    def test0215(self):
        self.assertEquals(self.calculate(11945, 2689), 14634, "")

    def test0216(self):
        self.assertEquals(self.calculate(8317, -1791), 6526, "")

    def test0217(self):
        self.assertEquals(self.calculate(-1326, 4218), 2892, "")

    def test0218(self):
        self.assertEquals(self.calculate(28232, -3825), 24407, "")

    def test0219(self):
        self.assertEquals(self.calculate(-23639, 20781), -2858, "")

    def test0220(self):
        self.assertEquals(self.calculate(-6749, -16383), -23132, "")

    def test0221(self):
        self.assertEquals(self.calculate(-28675, 1584), -27091, "")

    def test0222(self):
        self.assertEquals(self.calculate(20765, 19359), -25412, "")

    def test0223(self):
        self.assertEquals(self.calculate(-2597, 19161), 16564, "")

    def test0224(self):
        self.assertEquals(self.calculate(-16152, 11276), -4876, "")

    def test0225(self):
        self.assertEquals(self.calculate(-10415, 19121), 8706, "")

    def test0226(self):
        self.assertEquals(self.calculate(-93, 15269), 15176, "")

    def test0227(self):
        self.assertEquals(self.calculate(-5451, -24450), -29901, "")

    def test0228(self):
        self.assertEquals(self.calculate(-17382, 13923), -3459, "")

    def test0229(self):
        self.assertEquals(self.calculate(-6155, 29856), 23701, "")

    def test0230(self):
        self.assertEquals(self.calculate(13873, 24570), -27093, "")

    def test0231(self):
        self.assertEquals(self.calculate(-23956, 20597), -3359, "")

    def test0232(self):
        self.assertEquals(self.calculate(9191, 6577), 15768, "")

    def test0233(self):
        self.assertEquals(self.calculate(-17657, 6820), -10837, "")

    def test0234(self):
        self.assertEquals(self.calculate(7055, -30766), -23711, "")

    def test0235(self):
        self.assertEquals(self.calculate(-17463, -23723), 24350, "")

    def test0236(self):
        self.assertEquals(self.calculate(-16711, 2706), -14005, "")

    def test0237(self):
        self.assertEquals(self.calculate(-17983, 23271), 5288, "")

    def test0238(self):
        self.assertEquals(self.calculate(10255, -30736), -20481, "")

    def test0239(self):
        self.assertEquals(self.calculate(28193, 815), 29008, "")

    def test0240(self):
        self.assertEquals(self.calculate(-9915, 14379), 4464, "")

    def test0241(self):
        self.assertEquals(self.calculate(26376, 16461), -22699, "")

    def test0242(self):
        self.assertEquals(self.calculate(-24199, -23290), 18047, "")

    def test0243(self):
        self.assertEquals(self.calculate(-6895, -12471), -19366, "")

    def test0244(self):
        self.assertEquals(self.calculate(29995, 18764), -16777, "")

    def test0245(self):
        self.assertEquals(self.calculate(-21298, 10484), -10814, "")

    def test0246(self):
        self.assertEquals(self.calculate(-23903, -20836), 20797, "")

    def test0247(self):
        self.assertEquals(self.calculate(-18921, -29961), 16654, "")

    def test0248(self):
        self.assertEquals(self.calculate(9887, 8542), 18429, "")

    def test0249(self):
        self.assertEquals(self.calculate(14404, 13002), 27406, "")

    def test0250(self):
        self.assertEquals(self.calculate(-31855, 29771), -2084, "")

    def test0251(self):
        self.assertEquals(self.calculate(6743, 29404), -29389, "")

    def test0252(self):
        self.assertEquals(self.calculate(-9865, 23399), 13534, "")

    def test0253(self):
        self.assertEquals(self.calculate(16934, 6444), 23378, "")

    def test0254(self):
        self.assertEquals(self.calculate(-12472, 25886), 13414, "")

    def test0255(self):
        self.assertEquals(self.calculate(-15465, -28723), 21348, "")

    def test0256(self):
        self.assertEquals(self.calculate(28239, 31789), -5508, "")

    def test0257(self):
        self.assertEquals(self.calculate(-24701, 19932), -4769, "")

    def test0258(self):
        self.assertEquals(self.calculate(20529, 18532), -26475, "")

    def test0259(self):
        self.assertEquals(self.calculate(-15582, -22703), 27251, "")

    def test0260(self):
        self.assertEquals(self.calculate(331, 3528), 3859, "")

    def test0261(self):
        self.assertEquals(self.calculate(2727, -26834), -24107, "")

    def test0262(self):
        self.assertEquals(self.calculate(-3818, -1379), -5197, "")

    def test0263(self):
        self.assertEquals(self.calculate(-452, 27974), 27522, "")

    def test0264(self):
        self.assertEquals(self.calculate(6146, -15469), -9323, "")

    def test0265(self):
        self.assertEquals(self.calculate(18664, 6537), 25201, "")

    def test0266(self):
        self.assertEquals(self.calculate(-5885, -2218), -8103, "")

    def test0267(self):
        self.assertEquals(self.calculate(-4968, -30842), 29726, "")

    def test0268(self):
        self.assertEquals(self.calculate(-22198, -10666), 32672, "")

    def test0269(self):
        self.assertEquals(self.calculate(671, 15951), 16622, "")

    def test0270(self):
        self.assertEquals(self.calculate(25876, -6411), 19465, "")

    def test0271(self):
        self.assertEquals(self.calculate(-20704, 27037), 6333, "")

    def test0272(self):
        self.assertEquals(self.calculate(-6416, -26979), 32141, "")

    def test0273(self):
        self.assertEquals(self.calculate(-25357, 15481), -9876, "")

    def test0274(self):
        self.assertEquals(self.calculate(-16605, -1369), -17974, "")

    def test0275(self):
        self.assertEquals(self.calculate(-24525, 29241), 4716, "")

    def test0276(self):
        self.assertEquals(self.calculate(14954, 28440), -22142, "")

    def test0277(self):
        self.assertEquals(self.calculate(-17834, -25581), 22121, "")

    def test0278(self):
        self.assertEquals(self.calculate(12284, -16016), -3732, "")

    def test0279(self):
        self.assertEquals(self.calculate(-16683, 25734), 9051, "")

    def test0280(self):
        self.assertEquals(self.calculate(-31037, -18239), 16260, "")

    def test0281(self):
        self.assertEquals(self.calculate(22698, -12009), 10689, "")

    def test0282(self):
        self.assertEquals(self.calculate(-2743, 2772), 29, "")

    def test0283(self):
        self.assertEquals(self.calculate(19473, 12552), 32025, "")

    def test0284(self):
        self.assertEquals(self.calculate(-5034, 16350), 11316, "")

    def test0285(self):
        self.assertEquals(self.calculate(-30513, -4140), 30883, "")

    def test0286(self):
        self.assertEquals(self.calculate(23946, 27126), -14464, "")

    def test0287(self):
        self.assertEquals(self.calculate(24426, 29021), -12089, "")

    def test0288(self):
        self.assertEquals(self.calculate(18292, 8812), 27104, "")

    def test0289(self):
        self.assertEquals(self.calculate(-21287, -31656), 12593, "")

    def test0290(self):
        self.assertEquals(self.calculate(6935, -16508), -9573, "")

    def test0291(self):
        self.assertEquals(self.calculate(1559, 20457), 22016, "")

    def test0292(self):
        self.assertEquals(self.calculate(-25469, -14195), 25872, "")

    def test0293(self):
        self.assertEquals(self.calculate(-25112, 18508), -6604, "")

    def test0294(self):
        self.assertEquals(self.calculate(-31222, 9826), -21396, "")

    def test0295(self):
        self.assertEquals(self.calculate(15053, 27085), -23398, "")

    def test0296(self):
        self.assertEquals(self.calculate(31640, -30667), 973, "")

    def test0297(self):
        self.assertEquals(self.calculate(4701, -30085), -25384, "")

    def test0298(self):
        self.assertEquals(self.calculate(27351, 11), 27362, "")

    def test0299(self):
        self.assertEquals(self.calculate(-25625, 10912), -14713, "")

    def test0300(self):
        self.assertEquals(self.calculate(-16908, -29448), 19180, "")

    def test0301(self):
        self.assertEquals(self.calculate(18627, -11301), 7326, "")

    def test0302(self):
        self.assertEquals(self.calculate(-6334, 7982), 1648, "")

    def test0303(self):
        self.assertEquals(self.calculate(-28464, 28945), 481, "")

    def test0304(self):
        self.assertEquals(self.calculate(-3908, -11311), -15219, "")

    def test0305(self):
        self.assertEquals(self.calculate(2844, -20891), -18047, "")

    def test0306(self):
        self.assertEquals(self.calculate(-5672, 251), -5421, "")

    def test0307(self):
        self.assertEquals(self.calculate(-17570, 15835), -1735, "")

    def test0308(self):
        self.assertEquals(self.calculate(-12613, 32610), 19997, "")

    def test0309(self):
        self.assertEquals(self.calculate(10398, -29891), -19493, "")

    def test0310(self):
        self.assertEquals(self.calculate(29624, -31606), -1982, "")

    def test0311(self):
        self.assertEquals(self.calculate(19855, 2549), 22404, "")

    def test0312(self):
        self.assertEquals(self.calculate(-22806, 16740), -6066, "")

    def test0313(self):
        self.assertEquals(self.calculate(15010, 32552), -17974, "")

    def test0314(self):
        self.assertEquals(self.calculate(-13932, 761), -13171, "")

    def test0315(self):
        self.assertEquals(self.calculate(18864, -27390), -8526, "")

    def test0316(self):
        self.assertEquals(self.calculate(8538, 5288), 13826, "")

    def test0317(self):
        self.assertEquals(self.calculate(-14290, -9769), -24059, "")

    def test0318(self):
        self.assertEquals(self.calculate(1136, -6), 1130, "")

    def test0319(self):
        self.assertEquals(self.calculate(2985, 17305), 20290, "")

    def test0320(self):
        self.assertEquals(self.calculate(15038, 23326), -27172, "")

    def test0321(self):
        self.assertEquals(self.calculate(-23945, -1733), -25678, "")

    def test0322(self):
        self.assertEquals(self.calculate(7275, 11570), 18845, "")

    def test0323(self):
        self.assertEquals(self.calculate(-29187, 25325), -3862, "")

    def test0324(self):
        self.assertEquals(self.calculate(25076, -26551), -1475, "")

    def test0325(self):
        self.assertEquals(self.calculate(5781, 15586), 21367, "")

    def test0326(self):
        self.assertEquals(self.calculate(6650, -8132), -1482, "")

    def test0327(self):
        self.assertEquals(self.calculate(9305, 21085), 30390, "")

    def test0328(self):
        self.assertEquals(self.calculate(-8302, 24842), 16540, "")

    def test0329(self):
        self.assertEquals(self.calculate(-28896, -31085), 5555, "")

    def test0330(self):
        self.assertEquals(self.calculate(-1336, 6468), 5132, "")

    def test0331(self):
        self.assertEquals(self.calculate(1957, -13015), -11058, "")

    def test0332(self):
        self.assertEquals(self.calculate(19740, 17337), -28459, "")

    def test0333(self):
        self.assertEquals(self.calculate(-30305, 15095), -15210, "")

    def test0334(self):
        self.assertEquals(self.calculate(18456, 1794), 20250, "")

    def test0335(self):
        self.assertEquals(self.calculate(16871, -4706), 12165, "")

    def test0336(self):
        self.assertEquals(self.calculate(-25397, 31963), 6566, "")

    def test0337(self):
        self.assertEquals(self.calculate(16702, 966), 17668, "")

    def test0338(self):
        self.assertEquals(self.calculate(-13729, 16504), 2775, "")

    def test0339(self):
        self.assertEquals(self.calculate(-9198, 30288), 21090, "")

    def test0340(self):
        self.assertEquals(self.calculate(14744, -7764), 6980, "")

    def test0341(self):
        self.assertEquals(self.calculate(17743, 28769), -19024, "")

    def test0342(self):
        self.assertEquals(self.calculate(5728, 21412), 27140, "")

    def test0343(self):
        self.assertEquals(self.calculate(16521, -20261), -3740, "")

    def test0344(self):
        self.assertEquals(self.calculate(-20288, 4323), -15965, "")

    def test0345(self):
        self.assertEquals(self.calculate(27940, -15411), 12529, "")

    def test0346(self):
        self.assertEquals(self.calculate(-16992, -24559), 23985, "")

    def test0347(self):
        self.assertEquals(self.calculate(-9414, 14352), 4938, "")

    def test0348(self):
        self.assertEquals(self.calculate(-20286, -5266), -25552, "")

    def test0349(self):
        self.assertEquals(self.calculate(-7613, 4243), -3370, "")

    def test0350(self):
        self.assertEquals(self.calculate(-9517, 30598), 21081, "")

    def test0351(self):
        self.assertEquals(self.calculate(3728, -23394), -19666, "")

    def test0352(self):
        self.assertEquals(self.calculate(28498, -13098), 15400, "")

    def test0353(self):
        self.assertEquals(self.calculate(25275, 11878), -28383, "")

    def test0354(self):
        self.assertEquals(self.calculate(26694, 29138), -9704, "")

    def test0355(self):
        self.assertEquals(self.calculate(14767, 15736), 30503, "")

    def test0356(self):
        self.assertEquals(self.calculate(-10296, -3537), -13833, "")

    def test0357(self):
        self.assertEquals(self.calculate(28904, -17065), 11839, "")

    def test0358(self):
        self.assertEquals(self.calculate(-29298, 21890), -7408, "")

    def test0359(self):
        self.assertEquals(self.calculate(28063, 16346), -21127, "")

    def test0360(self):
        self.assertEquals(self.calculate(-15942, 27888), 11946, "")

    def test0361(self):
        self.assertEquals(self.calculate(5762, -5026), 736, "")

    def test0362(self):
        self.assertEquals(self.calculate(-24953, 32075), 7122, "")

    def test0363(self):
        self.assertEquals(self.calculate(9548, 6914), 16462, "")

    def test0364(self):
        self.assertEquals(self.calculate(-15402, 5970), -9432, "")

    def test0365(self):
        self.assertEquals(self.calculate(-23303, 1189), -22114, "")

    def test0366(self):
        self.assertEquals(self.calculate(32729, 23536), -9271, "")

    def test0367(self):
        self.assertEquals(self.calculate(-20009, -16293), 29234, "")

    def test0368(self):
        self.assertEquals(self.calculate(-31224, 32240), 1016, "")

    def test0369(self):
        self.assertEquals(self.calculate(11397, 14577), 25974, "")

    def test0370(self):
        self.assertEquals(self.calculate(26086, 10620), -28830, "")

    def test0371(self):
        self.assertEquals(self.calculate(-21054, -25630), 18852, "")

    def test0372(self):
        self.assertEquals(self.calculate(3531, 2217), 5748, "")

    def test0373(self):
        self.assertEquals(self.calculate(19591, 4671), 24262, "")

    def test0374(self):
        self.assertEquals(self.calculate(2665, -19065), -16400, "")

    def test0375(self):
        self.assertEquals(self.calculate(26086, 19961), -19489, "")

    def test0376(self):
        self.assertEquals(self.calculate(27172, 15347), -23017, "")

    def test0377(self):
        self.assertEquals(self.calculate(29444, -5493), 23951, "")

    def test0378(self):
        self.assertEquals(self.calculate(10450, 31935), -23151, "")

    def test0379(self):
        self.assertEquals(self.calculate(-13826, -15656), -29482, "")

    def test0380(self):
        self.assertEquals(self.calculate(-16380, -4134), -20514, "")

    def test0381(self):
        self.assertEquals(self.calculate(4903, 23523), 28426, "")

    def test0382(self):
        self.assertEquals(self.calculate(11865, 16809), 28674, "")

    def test0383(self):
        self.assertEquals(self.calculate(-20228, -7912), -28140, "")

    def test0384(self):
        self.assertEquals(self.calculate(-623, 32441), 31818, "")

    def test0385(self):
        self.assertEquals(self.calculate(-12834, 4575), -8259, "")

    def test0386(self):
        self.assertEquals(self.calculate(-30384, 4188), -26196, "")

    def test0387(self):
        self.assertEquals(self.calculate(-24657, -30746), 10133, "")

    def test0388(self):
        self.assertEquals(self.calculate(6584, -32353), -25769, "")

    def test0389(self):
        self.assertEquals(self.calculate(-3777, -21727), -25504, "")

    def test0390(self):
        self.assertEquals(self.calculate(27064, 24206), -14266, "")

    def test0391(self):
        self.assertEquals(self.calculate(-29007, 2682), -26325, "")

    def test0392(self):
        self.assertEquals(self.calculate(-11298, 22675), 11377, "")

    def test0393(self):
        self.assertEquals(self.calculate(-23580, 13866), -9714, "")

    def test0394(self):
        self.assertEquals(self.calculate(15968, 15824), 31792, "")

    def test0395(self):
        self.assertEquals(self.calculate(-12202, -12838), -25040, "")

    def test0396(self):
        self.assertEquals(self.calculate(27124, 7202), -31210, "")

    def test0397(self):
        self.assertEquals(self.calculate(-7118, 9041), 1923, "")

    def test0398(self):
        self.assertEquals(self.calculate(-26174, -12794), 26568, "")

    def test0399(self):
        self.assertEquals(self.calculate(14935, -23293), -8358, "")

    def test0400(self):
        self.assertEquals(self.calculate(26853, 31473), -7210, "")

    def test0401(self):
        self.assertEquals(self.calculate(30898, 12584), -22054, "")

    def test0402(self):
        self.assertEquals(self.calculate(25259, 11472), -28805, "")

    def test0403(self):
        self.assertEquals(self.calculate(-3883, 4411), 528, "")

    def test0404(self):
        self.assertEquals(self.calculate(-14717, -3709), -18426, "")

    def test0405(self):
        self.assertEquals(self.calculate(8407, -26982), -18575, "")

    def test0406(self):
        self.assertEquals(self.calculate(25954, -12363), 13591, "")

    def test0407(self):
        self.assertEquals(self.calculate(-8219, 11858), 3639, "")

    def test0408(self):
        self.assertEquals(self.calculate(16939, -22700), -5761, "")

    def test0409(self):
        self.assertEquals(self.calculate(-8472, -32108), 24956, "")

    def test0410(self):
        self.assertEquals(self.calculate(17026, -21041), -4015, "")

    def test0411(self):
        self.assertEquals(self.calculate(-18778, -6585), -25363, "")

    def test0412(self):
        self.assertEquals(self.calculate(-11822, -22738), 30976, "")

    def test0413(self):
        self.assertEquals(self.calculate(9313, -27655), -18342, "")

    def test0414(self):
        self.assertEquals(self.calculate(30694, 27959), -6883, "")

    def test0415(self):
        self.assertEquals(self.calculate(-21121, -4161), -25282, "")

    def test0416(self):
        self.assertEquals(self.calculate(5826, 9660), 15486, "")

    def test0417(self):
        self.assertEquals(self.calculate(-11100, -17243), -28343, "")

    def test0418(self):
        self.assertEquals(self.calculate(12434, -7949), 4485, "")

    def test0419(self):
        self.assertEquals(self.calculate(-19950, 26832), 6882, "")

    def test0420(self):
        self.assertEquals(self.calculate(168, -10123), -9955, "")

    def test0421(self):
        self.assertEquals(self.calculate(15861, -15574), 287, "")

    def test0422(self):
        self.assertEquals(self.calculate(-16604, 21335), 4731, "")

    def test0423(self):
        self.assertEquals(self.calculate(22345, 21596), -21595, "")

    def test0424(self):
        self.assertEquals(self.calculate(-25580, 254), -25326, "")

    def test0425(self):
        self.assertEquals(self.calculate(-29397, -19462), 16677, "")

    def test0426(self):
        self.assertEquals(self.calculate(22012, -8903), 13109, "")

    def test0427(self):
        self.assertEquals(self.calculate(29156, 7845), -28535, "")

    def test0428(self):
        self.assertEquals(self.calculate(10877, -848), 10029, "")

    def test0429(self):
        self.assertEquals(self.calculate(-20798, -28304), 16434, "")

    def test0430(self):
        self.assertEquals(self.calculate(28647, 11864), -25025, "")

    def test0431(self):
        self.assertEquals(self.calculate(-3355, -18243), -21598, "")

    def test0432(self):
        self.assertEquals(self.calculate(-19832, -11496), -31328, "")

    def test0433(self):
        self.assertEquals(self.calculate(9452, 7917), 17369, "")

    def test0434(self):
        self.assertEquals(self.calculate(16401, 24429), -24706, "")

    def test0435(self):
        self.assertEquals(self.calculate(-20734, 7989), -12745, "")

    def test0436(self):
        self.assertEquals(self.calculate(-20817, 25203), 4386, "")

    def test0437(self):
        self.assertEquals(self.calculate(-10181, -16695), -26876, "")

    def test0438(self):
        self.assertEquals(self.calculate(848, 4526), 5374, "")

    def test0439(self):
        self.assertEquals(self.calculate(6268, -6739), -471, "")

    def test0440(self):
        self.assertEquals(self.calculate(-6915, 16317), 9402, "")

    def test0441(self):
        self.assertEquals(self.calculate(2078, 7745), 9823, "")

    def test0442(self):
        self.assertEquals(self.calculate(13029, -31058), -18029, "")

    def test0443(self):
        self.assertEquals(self.calculate(-16184, 2087), -14097, "")

    def test0444(self):
        self.assertEquals(self.calculate(-7857, 5721), -2136, "")

    def test0445(self):
        self.assertEquals(self.calculate(-14441, -10669), -25110, "")

    def test0446(self):
        self.assertEquals(self.calculate(4881, -22760), -17879, "")

    def test0447(self):
        self.assertEquals(self.calculate(-30097, 2177), -27920, "")

    def test0448(self):
        self.assertEquals(self.calculate(-27281, 13260), -14021, "")

    def test0449(self):
        self.assertEquals(self.calculate(-3738, -16531), -20269, "")

    def test0450(self):
        self.assertEquals(self.calculate(4663, -29155), -24492, "")

    def test0451(self):
        self.assertEquals(self.calculate(-6078, -4571), -10649, "")

    def test0452(self):
        self.assertEquals(self.calculate(4537, 31152), -29847, "")

    def test0453(self):
        self.assertEquals(self.calculate(-5528, 28691), 23163, "")

    def test0454(self):
        self.assertEquals(self.calculate(-12020, -30798), 22718, "")

    def test0455(self):
        self.assertEquals(self.calculate(14707, 16337), 31044, "")

    def test0456(self):
        self.assertEquals(self.calculate(-15490, -23760), 26286, "")

    def test0457(self):
        self.assertEquals(self.calculate(8008, 10636), 18644, "")

    def test0458(self):
        self.assertEquals(self.calculate(-2692, -22769), -25461, "")

    def test0459(self):
        self.assertEquals(self.calculate(11659, 16814), 28473, "")

    def test0460(self):
        self.assertEquals(self.calculate(12493, -7544), 4949, "")

    def test0461(self):
        self.assertEquals(self.calculate(-16720, 1709), -15011, "")

    def test0462(self):
        self.assertEquals(self.calculate(4120, 12977), 17097, "")

    def test0463(self):
        self.assertEquals(self.calculate(28069, 8934), -28533, "")

    def test0464(self):
        self.assertEquals(self.calculate(7223, 13783), 21006, "")

    def test0465(self):
        self.assertEquals(self.calculate(26135, 11335), -28066, "")

    def test0466(self):
        self.assertEquals(self.calculate(-25500, -6100), -31600, "")

    def test0467(self):
        self.assertEquals(self.calculate(3736, -8835), -5099, "")

    def test0468(self):
        self.assertEquals(self.calculate(5669, 32649), -27218, "")

    def test0469(self):
        self.assertEquals(self.calculate(-18567, 26190), 7623, "")

    def test0470(self):
        self.assertEquals(self.calculate(15912, -32174), -16262, "")

    def test0471(self):
        self.assertEquals(self.calculate(24089, -27373), -3284, "")

    def test0472(self):
        self.assertEquals(self.calculate(16943, -700), 16243, "")

    def test0473(self):
        self.assertEquals(self.calculate(23701, 15464), -26371, "")

    def test0474(self):
        self.assertEquals(self.calculate(-10535, -2915), -13450, "")

    def test0475(self):
        self.assertEquals(self.calculate(-6303, -6830), -13133, "")

    def test0476(self):
        self.assertEquals(self.calculate(29582, 1119), 30701, "")

    def test0477(self):
        self.assertEquals(self.calculate(-17477, -32685), 15374, "")

    def test0478(self):
        self.assertEquals(self.calculate(20417, 3847), 24264, "")

    def test0479(self):
        self.assertEquals(self.calculate(7905, 11773), 19678, "")

    def test0480(self):
        self.assertEquals(self.calculate(2180, -9481), -7301, "")

    def test0481(self):
        self.assertEquals(self.calculate(-23309, 18510), -4799, "")

    def test0482(self):
        self.assertEquals(self.calculate(26768, 9967), -28801, "")

    def test0483(self):
        self.assertEquals(self.calculate(3542, 29297), -32697, "")

    def test0484(self):
        self.assertEquals(self.calculate(-22587, -21207), 21742, "")

    def test0485(self):
        self.assertEquals(self.calculate(-19455, 22190), 2735, "")

    def test0486(self):
        self.assertEquals(self.calculate(-26401, 20793), -5608, "")

    def test0487(self):
        self.assertEquals(self.calculate(29045, -2016), 27029, "")

    def test0488(self):
        self.assertEquals(self.calculate(850, 6388), 7238, "")

    def test0489(self):
        self.assertEquals(self.calculate(18281, -30062), -11781, "")

    def test0490(self):
        self.assertEquals(self.calculate(-13163, -7597), -20760, "")

    def test0491(self):
        self.assertEquals(self.calculate(-8682, -5250), -13932, "")

    def test0492(self):
        self.assertEquals(self.calculate(-13212, 23273), 10061, "")

    def test0493(self):
        self.assertEquals(self.calculate(17531, 27188), -20817, "")

    def test0494(self):
        self.assertEquals(self.calculate(-13603, -19399), 32534, "")

    def test0495(self):
        self.assertEquals(self.calculate(9316, -11068), -1752, "")

    def test0496(self):
        self.assertEquals(self.calculate(-1348, 30622), 29274, "")

    def test0497(self):
        self.assertEquals(self.calculate(-3962, 5821), 1859, "")

    def test0498(self):
        self.assertEquals(self.calculate(23822, 12736), -28978, "")

    def test0499(self):
        self.assertEquals(self.calculate(9235, 4347), 13582, "")

    def test0500(self):
        self.assertEquals(self.calculate(-4036, -4261), -8297, "")

    def test0501(self):
        self.assertEquals(self.calculate(-2125, -2397), -4522, "")

    def test0502(self):
        self.assertEquals(self.calculate(16831, 24844), -23861, "")

    def test0503(self):
        self.assertEquals(self.calculate(4742, -12201), -7459, "")

    def test0504(self):
        self.assertEquals(self.calculate(20580, 23991), -20965, "")

    def test0505(self):
        self.assertEquals(self.calculate(-17998, -2659), -20657, "")

    def test0506(self):
        self.assertEquals(self.calculate(-6836, -22948), -29784, "")

    def test0507(self):
        self.assertEquals(self.calculate(27075, 5545), 32620, "")

    def test0508(self):
        self.assertEquals(self.calculate(-4855, -17170), -22025, "")

    def test0509(self):
        self.assertEquals(self.calculate(25946, -248), 25698, "")

    def test0510(self):
        self.assertEquals(self.calculate(31297, -13890), 17407, "")

    def test0511(self):
        self.assertEquals(self.calculate(7186, -28906), -21720, "")

    def test0512(self):
        self.assertEquals(self.calculate(-17418, 30599), 13181, "")

    def test0513(self):
        self.assertEquals(self.calculate(83, 9114), 9197, "")

    def test0514(self):
        self.assertEquals(self.calculate(23553, -24642), -1089, "")

    def test0515(self):
        self.assertEquals(self.calculate(31700, -29314), 2386, "")

    def test0516(self):
        self.assertEquals(self.calculate(25831, 9412), -30293, "")

    def test0517(self):
        self.assertEquals(self.calculate(5608, 4069), 9677, "")

    def test0518(self):
        self.assertEquals(self.calculate(5859, 19258), 25117, "")

    def test0519(self):
        self.assertEquals(self.calculate(-11708, -8696), -20404, "")

    def test0520(self):
        self.assertEquals(self.calculate(-30390, -8117), 27029, "")

    def test0521(self):
        self.assertEquals(self.calculate(30490, -7618), 22872, "")

    def test0522(self):
        self.assertEquals(self.calculate(28751, -4196), 24555, "")

    def test0523(self):
        self.assertEquals(self.calculate(15656, -253), 15403, "")

    def test0524(self):
        self.assertEquals(self.calculate(-13492, 7288), -6204, "")

    def test0525(self):
        self.assertEquals(self.calculate(-29390, 21790), -7600, "")

    def test0526(self):
        self.assertEquals(self.calculate(-9311, -24854), 31371, "")

    def test0527(self):
        self.assertEquals(self.calculate(28918, -17532), 11386, "")

    def test0528(self):
        self.assertEquals(self.calculate(32334, -28546), 3788, "")

    def test0529(self):
        self.assertEquals(self.calculate(30116, 16363), -19057, "")

    def test0530(self):
        self.assertEquals(self.calculate(-16210, -4288), -20498, "")

    def test0531(self):
        self.assertEquals(self.calculate(6880, 8972), 15852, "")

    def test0532(self):
        self.assertEquals(self.calculate(3651, 17913), 21564, "")

    def test0533(self):
        self.assertEquals(self.calculate(4295, 21890), 26185, "")

    def test0534(self):
        self.assertEquals(self.calculate(-30809, -26584), 8143, "")

    def test0535(self):
        self.assertEquals(self.calculate(31154, 20460), -13922, "")

    def test0536(self):
        self.assertEquals(self.calculate(3479, -12490), -9011, "")

    def test0537(self):
        self.assertEquals(self.calculate(-30358, 19947), -10411, "")

    def test0538(self):
        self.assertEquals(self.calculate(-19640, -21772), 24124, "")

    def test0539(self):
        self.assertEquals(self.calculate(11706, -9569), 2137, "")

    def test0540(self):
        self.assertEquals(self.calculate(18129, 8277), 26406, "")

    def test0541(self):
        self.assertEquals(self.calculate(-2719, 1811), -908, "")

    def test0542(self):
        self.assertEquals(self.calculate(-29035, -9767), 26734, "")

    def test0543(self):
        self.assertEquals(self.calculate(28229, 31954), -5353, "")

    def test0544(self):
        self.assertEquals(self.calculate(19130, -18665), 465, "")

    def test0545(self):
        self.assertEquals(self.calculate(11996, -31066), -19070, "")

    def test0546(self):
        self.assertEquals(self.calculate(13628, -30072), -16444, "")

    def test0547(self):
        self.assertEquals(self.calculate(-13898, 19535), 5637, "")

    def test0548(self):
        self.assertEquals(self.calculate(3977, 11631), 15608, "")

    def test0549(self):
        self.assertEquals(self.calculate(16310, -26915), -10605, "")

    def test0550(self):
        self.assertEquals(self.calculate(7911, 12257), 20168, "")

    def test0551(self):
        self.assertEquals(self.calculate(-16174, -16574), -32748, "")

    def test0552(self):
        self.assertEquals(self.calculate(13945, 31332), -20259, "")

    def test0553(self):
        self.assertEquals(self.calculate(-30780, -19128), 15628, "")

    def test0554(self):
        self.assertEquals(self.calculate(-6629, -19536), -26165, "")

    def test0555(self):
        self.assertEquals(self.calculate(-23568, -12208), 29760, "")

    def test0556(self):
        self.assertEquals(self.calculate(19066, -31399), -12333, "")

    def test0557(self):
        self.assertEquals(self.calculate(451, -32123), -31672, "")

    def test0558(self):
        self.assertEquals(self.calculate(-20414, -6517), -26931, "")

    def test0559(self):
        self.assertEquals(self.calculate(28618, 25666), -11252, "")

    def test0560(self):
        self.assertEquals(self.calculate(29640, -8577), 21063, "")

    def test0561(self):
        self.assertEquals(self.calculate(18931, 16451), -30154, "")

    def test0562(self):
        self.assertEquals(self.calculate(30492, -31828), -1336, "")

    def test0563(self):
        self.assertEquals(self.calculate(-22742, -5469), -28211, "")

    def test0564(self):
        self.assertEquals(self.calculate(10451, -26356), -15905, "")

    def test0565(self):
        self.assertEquals(self.calculate(29685, 14436), -21415, "")

    def test0566(self):
        self.assertEquals(self.calculate(14262, -10893), 3369, "")

    def test0567(self):
        self.assertEquals(self.calculate(13109, -25976), -12867, "")

    def test0568(self):
        self.assertEquals(self.calculate(-15359, -18711), 31466, "")

    def test0569(self):
        self.assertEquals(self.calculate(-31866, -16268), 17402, "")

    def test0570(self):
        self.assertEquals(self.calculate(-31850, -7973), 25713, "")

    def test0571(self):
        self.assertEquals(self.calculate(26743, -5171), 21572, "")

    def test0572(self):
        self.assertEquals(self.calculate(28280, -14505), 13775, "")

    def test0573(self):
        self.assertEquals(self.calculate(-11990, -29273), 24273, "")

    def test0574(self):
        self.assertEquals(self.calculate(28514, -2829), 25685, "")

    def test0575(self):
        self.assertEquals(self.calculate(-30592, -7559), 27385, "")

    def test0576(self):
        self.assertEquals(self.calculate(12034, -8011), 4023, "")

    def test0577(self):
        self.assertEquals(self.calculate(25319, -18397), 6922, "")

    def test0578(self):
        self.assertEquals(self.calculate(-3251, 28407), 25156, "")

    def test0579(self):
        self.assertEquals(self.calculate(-13812, -22497), 29227, "")

    def test0580(self):
        self.assertEquals(self.calculate(25749, -12288), 13461, "")

    def test0581(self):
        self.assertEquals(self.calculate(-694, -7621), -8315, "")

    def test0582(self):
        self.assertEquals(self.calculate(21922, 20707), -22907, "")

    def test0583(self):
        self.assertEquals(self.calculate(-27855, -4750), -32605, "")

    def test0584(self):
        self.assertEquals(self.calculate(-14100, 28867), 14767, "")

    def test0585(self):
        self.assertEquals(self.calculate(-14897, 13508), -1389, "")

    def test0586(self):
        self.assertEquals(self.calculate(-27037, -15499), 23000, "")

    def test0587(self):
        self.assertEquals(self.calculate(7546, -2553), 4993, "")

    def test0588(self):
        self.assertEquals(self.calculate(-13064, -29178), 23294, "")

    def test0589(self):
        self.assertEquals(self.calculate(28165, -29500), -1335, "")

    def test0590(self):
        self.assertEquals(self.calculate(22355, -20980), 1375, "")

    def test0591(self):
        self.assertEquals(self.calculate(3542, -20328), -16786, "")

    def test0592(self):
        self.assertEquals(self.calculate(-20279, -5019), -25298, "")

    def test0593(self):
        self.assertEquals(self.calculate(-23389, -7671), -31060, "")

    def test0594(self):
        self.assertEquals(self.calculate(-15900, -31299), 18337, "")

    def test0595(self):
        self.assertEquals(self.calculate(-10592, -16859), -27451, "")

    def test0596(self):
        self.assertEquals(self.calculate(8867, 19701), 28568, "")

    def test0597(self):
        self.assertEquals(self.calculate(-10211, -17507), -27718, "")

    def test0598(self):
        self.assertEquals(self.calculate(13167, 31315), -21054, "")

    def test0599(self):
        self.assertEquals(self.calculate(18332, -29731), -11399, "")

    def test0600(self):
        self.assertEquals(self.calculate(-9387, 7705), -1682, "")

    def test0601(self):
        self.assertEquals(self.calculate(24859, -15630), 9229, "")

    def test0602(self):
        self.assertEquals(self.calculate(18329, -16998), 1331, "")

    def test0603(self):
        self.assertEquals(self.calculate(-5697, -32088), 27751, "")

    def test0604(self):
        self.assertEquals(self.calculate(24423, 16749), -24364, "")

    def test0605(self):
        self.assertEquals(self.calculate(2832, -29905), -27073, "")

    def test0606(self):
        self.assertEquals(self.calculate(11476, 30959), -23101, "")

    def test0607(self):
        self.assertEquals(self.calculate(13401, -13051), 350, "")

    def test0608(self):
        self.assertEquals(self.calculate(27173, 3056), 30229, "")

    def test0609(self):
        self.assertEquals(self.calculate(-11828, 20319), 8491, "")

    def test0610(self):
        self.assertEquals(self.calculate(-30133, 22123), -8010, "")

    def test0611(self):
        self.assertEquals(self.calculate(20088, 458), 20546, "")

    def test0612(self):
        self.assertEquals(self.calculate(26499, 25374), -13663, "")

    def test0613(self):
        self.assertEquals(self.calculate(-7553, -4872), -12425, "")

    def test0614(self):
        self.assertEquals(self.calculate(-14653, 2793), -11860, "")

    def test0615(self):
        self.assertEquals(self.calculate(-7088, -22632), -29720, "")

    def test0616(self):
        self.assertEquals(self.calculate(-27354, -10962), 27220, "")

    def test0617(self):
        self.assertEquals(self.calculate(7703, 27647), -30186, "")

    def test0618(self):
        self.assertEquals(self.calculate(8556, -16733), -8177, "")

    def test0619(self):
        self.assertEquals(self.calculate(32367, -21382), 10985, "")

    def test0620(self):
        self.assertEquals(self.calculate(-329, -10624), -10953, "")

    def test0621(self):
        self.assertEquals(self.calculate(-27164, 16248), -10916, "")

    def test0622(self):
        self.assertEquals(self.calculate(-11721, -12598), -24319, "")

    def test0623(self):
        self.assertEquals(self.calculate(18159, -27410), -9251, "")

    def test0624(self):
        self.assertEquals(self.calculate(2300, -1652), 648, "")

    def test0625(self):
        self.assertEquals(self.calculate(-30392, 15254), -15138, "")

    def test0626(self):
        self.assertEquals(self.calculate(-1615, 17589), 15974, "")

    def test0627(self):
        self.assertEquals(self.calculate(2920, -22248), -19328, "")

    def test0628(self):
        self.assertEquals(self.calculate(-11678, 25801), 14123, "")

    def test0629(self):
        self.assertEquals(self.calculate(-18741, 31317), 12576, "")

    def test0630(self):
        self.assertEquals(self.calculate(-5535, 8361), 2826, "")

    def test0631(self):
        self.assertEquals(self.calculate(-21175, -25461), 18900, "")

    def test0632(self):
        self.assertEquals(self.calculate(17837, 18199), -29500, "")

    def test0633(self):
        self.assertEquals(self.calculate(3765, 21944), 25709, "")

    def test0634(self):
        self.assertEquals(self.calculate(-24721, -24424), 16391, "")

    def test0635(self):
        self.assertEquals(self.calculate(-22381, 24477), 2096, "")

    def test0636(self):
        self.assertEquals(self.calculate(-9799, -2472), -12271, "")

    def test0637(self):
        self.assertEquals(self.calculate(10120, 11175), 21295, "")

    def test0638(self):
        self.assertEquals(self.calculate(-14760, 27304), 12544, "")

    def test0639(self):
        self.assertEquals(self.calculate(62, -21233), -21171, "")

    def test0640(self):
        self.assertEquals(self.calculate(-13700, 7338), -6362, "")

    def test0641(self):
        self.assertEquals(self.calculate(17405, 15287), 32692, "")

    def test0642(self):
        self.assertEquals(self.calculate(19361, 31603), -14572, "")

    def test0643(self):
        self.assertEquals(self.calculate(14891, -3230), 11661, "")

    def test0644(self):
        self.assertEquals(self.calculate(-31652, 21459), -10193, "")

    def test0645(self):
        self.assertEquals(self.calculate(10665, 23906), -30965, "")

    def test0646(self):
        self.assertEquals(self.calculate(-29532, -3705), 32299, "")

    def test0647(self):
        self.assertEquals(self.calculate(23300, 15613), -26623, "")

    def test0648(self):
        self.assertEquals(self.calculate(7632, 5639), 13271, "")

    def test0649(self):
        self.assertEquals(self.calculate(-5088, 14080), 8992, "")

    def test0650(self):
        self.assertEquals(self.calculate(-12151, -16798), -28949, "")

    def test0651(self):
        self.assertEquals(self.calculate(-3739, -15276), -19015, "")

    def test0652(self):
        self.assertEquals(self.calculate(24137, 23929), -17470, "")

    def test0653(self):
        self.assertEquals(self.calculate(824, -21470), -20646, "")

    def test0654(self):
        self.assertEquals(self.calculate(-32558, -6525), 26453, "")

    def test0655(self):
        self.assertEquals(self.calculate(2716, 22820), 25536, "")

    def test0656(self):
        self.assertEquals(self.calculate(22899, -18994), 3905, "")

    def test0657(self):
        self.assertEquals(self.calculate(15415, -21976), -6561, "")

    def test0658(self):
        self.assertEquals(self.calculate(-8935, -20051), -28986, "")

    def test0659(self):
        self.assertEquals(self.calculate(-31372, 1191), -30181, "")

    def test0660(self):
        self.assertEquals(self.calculate(4321, 19140), 23461, "")

    def test0661(self):
        self.assertEquals(self.calculate(25512, -13297), 12215, "")

    def test0662(self):
        self.assertEquals(self.calculate(24297, -5165), 19132, "")

    def test0663(self):
        self.assertEquals(self.calculate(-19795, -4267), -24062, "")

    def test0664(self):
        self.assertEquals(self.calculate(11182, 25577), -28777, "")

    def test0665(self):
        self.assertEquals(self.calculate(21898, -31804), -9906, "")

    def test0666(self):
        self.assertEquals(self.calculate(31223, -25728), 5495, "")

    def test0667(self):
        self.assertEquals(self.calculate(-11399, -32514), 21623, "")

    def test0668(self):
        self.assertEquals(self.calculate(30443, -17610), 12833, "")

    def test0669(self):
        self.assertEquals(self.calculate(-29929, 16285), -13644, "")

    def test0670(self):
        self.assertEquals(self.calculate(-27815, 28453), 638, "")

    def test0671(self):
        self.assertEquals(self.calculate(-31341, -4134), 30061, "")

    def test0672(self):
        self.assertEquals(self.calculate(30104, -26726), 3378, "")

    def test0673(self):
        self.assertEquals(self.calculate(883, 7451), 8334, "")

    def test0674(self):
        self.assertEquals(self.calculate(6695, 5307), 12002, "")

    def test0675(self):
        self.assertEquals(self.calculate(612, -85), 527, "")

    def test0676(self):
        self.assertEquals(self.calculate(-21956, -19336), 24244, "")

    def test0677(self):
        self.assertEquals(self.calculate(-18163, -26951), 20422, "")

    def test0678(self):
        self.assertEquals(self.calculate(15757, 28601), -21178, "")

    def test0679(self):
        self.assertEquals(self.calculate(3433, -24465), -21032, "")

    def test0680(self):
        self.assertEquals(self.calculate(707, -32063), -31356, "")

    def test0681(self):
        self.assertEquals(self.calculate(31865, -9684), 22181, "")

    def test0682(self):
        self.assertEquals(self.calculate(16859, -29845), -12986, "")

    def test0683(self):
        self.assertEquals(self.calculate(-284, -4657), -4941, "")

    def test0684(self):
        self.assertEquals(self.calculate(-1088, -8524), -9612, "")

    def test0685(self):
        self.assertEquals(self.calculate(25362, 23025), -17149, "")

    def test0686(self):
        self.assertEquals(self.calculate(12416, 7583), 19999, "")

    def test0687(self):
        self.assertEquals(self.calculate(1427, -27545), -26118, "")

    def test0688(self):
        self.assertEquals(self.calculate(-27520, -5101), -32621, "")

    def test0689(self):
        self.assertEquals(self.calculate(-25448, -20214), 19874, "")

    def test0690(self):
        self.assertEquals(self.calculate(-29350, 20708), -8642, "")

    def test0691(self):
        self.assertEquals(self.calculate(7469, 28213), -29854, "")

    def test0692(self):
        self.assertEquals(self.calculate(-1405, -28303), -29708, "")

    def test0693(self):
        self.assertEquals(self.calculate(-18847, 30773), 11926, "")

    def test0694(self):
        self.assertEquals(self.calculate(14579, 25516), -25441, "")

    def test0695(self):
        self.assertEquals(self.calculate(-10582, 27657), 17075, "")

    def test0696(self):
        self.assertEquals(self.calculate(-3951, 19523), 15572, "")

    def test0697(self):
        self.assertEquals(self.calculate(7834, 28621), -29081, "")

    def test0698(self):
        self.assertEquals(self.calculate(29378, 29991), -6167, "")

    def test0699(self):
        self.assertEquals(self.calculate(-32339, -15061), 18136, "")

    def test0700(self):
        self.assertEquals(self.calculate(-6733, 2403), -4330, "")

    def test0701(self):
        self.assertEquals(self.calculate(-31177, 27753), -3424, "")

    def test0702(self):
        self.assertEquals(self.calculate(22976, 18233), -24327, "")

    def test0703(self):
        self.assertEquals(self.calculate(18319, 5561), 23880, "")

    def test0704(self):
        self.assertEquals(self.calculate(-6348, 2721), -3627, "")

    def test0705(self):
        self.assertEquals(self.calculate(2099, 18698), 20797, "")

    def test0706(self):
        self.assertEquals(self.calculate(16590, 5344), 21934, "")

    def test0707(self):
        self.assertEquals(self.calculate(11070, 31363), -23103, "")

    def test0708(self):
        self.assertEquals(self.calculate(26957, -27557), -600, "")

    def test0709(self):
        self.assertEquals(self.calculate(28966, 8257), -28313, "")

    def test0710(self):
        self.assertEquals(self.calculate(-11581, 29334), 17753, "")

    def test0711(self):
        self.assertEquals(self.calculate(8753, 13150), 21903, "")

    def test0712(self):
        self.assertEquals(self.calculate(-19204, -21229), 25103, "")

    def test0713(self):
        self.assertEquals(self.calculate(4915, 9434), 14349, "")

    def test0714(self):
        self.assertEquals(self.calculate(2629, 3855), 6484, "")

    def test0715(self):
        self.assertEquals(self.calculate(-885, -26756), -27641, "")

    def test0716(self):
        self.assertEquals(self.calculate(145, 28352), 28497, "")

    def test0717(self):
        self.assertEquals(self.calculate(-12183, -8713), -20896, "")

    def test0718(self):
        self.assertEquals(self.calculate(5386, 161), 5547, "")

    def test0719(self):
        self.assertEquals(self.calculate(-25702, -23515), 16319, "")

    def test0720(self):
        self.assertEquals(self.calculate(-13531, -14632), -28163, "")

    def test0721(self):
        self.assertEquals(self.calculate(-31075, -29207), 5254, "")

    def test0722(self):
        self.assertEquals(self.calculate(-12231, -4376), -16607, "")

    def test0723(self):
        self.assertEquals(self.calculate(-23323, -12447), 29766, "")

    def test0724(self):
        self.assertEquals(self.calculate(-20261, -13397), 31878, "")

    def test0725(self):
        self.assertEquals(self.calculate(-12179, -20638), 32719, "")

    def test0726(self):
        self.assertEquals(self.calculate(-32498, 25829), -6669, "")

    def test0727(self):
        self.assertEquals(self.calculate(1590, -12216), -10626, "")

    def test0728(self):
        self.assertEquals(self.calculate(-3256, -19657), -22913, "")

    def test0729(self):
        self.assertEquals(self.calculate(-15415, -14004), -29419, "")

    def test0730(self):
        self.assertEquals(self.calculate(16723, 3372), 20095, "")

    def test0731(self):
        self.assertEquals(self.calculate(-302, -28191), -28493, "")

    def test0732(self):
        self.assertEquals(self.calculate(8915, -314), 8601, "")

    def test0733(self):
        self.assertEquals(self.calculate(-31542, -3790), 30204, "")

    def test0734(self):
        self.assertEquals(self.calculate(459, -21103), -20644, "")

    def test0735(self):
        self.assertEquals(self.calculate(-15036, -7171), -22207, "")

    def test0736(self):
        self.assertEquals(self.calculate(26420, 5299), 31719, "")

    def test0737(self):
        self.assertEquals(self.calculate(22820, -24940), -2120, "")

    def test0738(self):
        self.assertEquals(self.calculate(23072, 2263), 25335, "")

    def test0739(self):
        self.assertEquals(self.calculate(7060, 23747), 30807, "")

    def test0740(self):
        self.assertEquals(self.calculate(-8803, -10462), -19265, "")

    def test0741(self):
        self.assertEquals(self.calculate(-32084, 20594), -11490, "")

    def test0742(self):
        self.assertEquals(self.calculate(189, 11020), 11209, "")

    def test0743(self):
        self.assertEquals(self.calculate(-11500, -31833), 22203, "")

    def test0744(self):
        self.assertEquals(self.calculate(-7640, -30186), 27710, "")

    def test0745(self):
        self.assertEquals(self.calculate(18689, 25031), -21816, "")

    def test0746(self):
        self.assertEquals(self.calculate(5340, -17718), -12378, "")

    def test0747(self):
        self.assertEquals(self.calculate(-29589, 781), -28808, "")

    def test0748(self):
        self.assertEquals(self.calculate(-10808, 25356), 14548, "")

    def test0749(self):
        self.assertEquals(self.calculate(-30140, 31928), 1788, "")

    def test0750(self):
        self.assertEquals(self.calculate(5841, -4776), 1065, "")

    def test0751(self):
        self.assertEquals(self.calculate(24439, -15665), 8774, "")

    def test0752(self):
        self.assertEquals(self.calculate(14451, 13719), 28170, "")

    def test0753(self):
        self.assertEquals(self.calculate(30461, 17808), -17267, "")

    def test0754(self):
        self.assertEquals(self.calculate(-20665, -32175), 12696, "")

    def test0755(self):
        self.assertEquals(self.calculate(16642, -24213), -7571, "")

    def test0756(self):
        self.assertEquals(self.calculate(-32507, -6100), 26929, "")

    def test0757(self):
        self.assertEquals(self.calculate(-32402, 4114), -28288, "")

    def test0758(self):
        self.assertEquals(self.calculate(9799, -17306), -7507, "")

    def test0759(self):
        self.assertEquals(self.calculate(15264, -14628), 636, "")

    def test0760(self):
        self.assertEquals(self.calculate(-3056, 25952), 22896, "")

    def test0761(self):
        self.assertEquals(self.calculate(18509, 15250), -31777, "")

    def test0762(self):
        self.assertEquals(self.calculate(-30094, 21155), -8939, "")

    def test0763(self):
        self.assertEquals(self.calculate(6862, -20183), -13321, "")

    def test0764(self):
        self.assertEquals(self.calculate(15869, -16231), -362, "")

    def test0765(self):
        self.assertEquals(self.calculate(-4163, -28929), 32444, "")

    def test0766(self):
        self.assertEquals(self.calculate(16776, -21518), -4742, "")

    def test0767(self):
        self.assertEquals(self.calculate(-14944, -10141), -25085, "")

    def test0768(self):
        self.assertEquals(self.calculate(6190, 3577), 9767, "")

    def test0769(self):
        self.assertEquals(self.calculate(21631, -31688), -10057, "")

    def test0770(self):
        self.assertEquals(self.calculate(-16235, -13526), -29761, "")

    def test0771(self):
        self.assertEquals(self.calculate(8214, 10194), 18408, "")

    def test0772(self):
        self.assertEquals(self.calculate(-3088, -26374), -29462, "")

    def test0773(self):
        self.assertEquals(self.calculate(20546, -25511), -4965, "")

    def test0774(self):
        self.assertEquals(self.calculate(1065, -18047), -16982, "")

    def test0775(self):
        self.assertEquals(self.calculate(24965, 12817), -27754, "")

    def test0776(self):
        self.assertEquals(self.calculate(6592, -28065), -21473, "")

    def test0777(self):
        self.assertEquals(self.calculate(23072, 16407), -26057, "")

    def test0778(self):
        self.assertEquals(self.calculate(19053, -30780), -11727, "")

    def test0779(self):
        self.assertEquals(self.calculate(22218, 7314), 29532, "")

    def test0780(self):
        self.assertEquals(self.calculate(13262, 4686), 17948, "")

    def test0781(self):
        self.assertEquals(self.calculate(-20480, -17243), 27813, "")

    def test0782(self):
        self.assertEquals(self.calculate(365, 23353), 23718, "")

    def test0783(self):
        self.assertEquals(self.calculate(-5359, 15460), 10101, "")

    def test0784(self):
        self.assertEquals(self.calculate(26710, 6223), -32603, "")

    def test0785(self):
        self.assertEquals(self.calculate(25562, -10541), 15021, "")

    def test0786(self):
        self.assertEquals(self.calculate(18185, 31951), -15400, "")

    def test0787(self):
        self.assertEquals(self.calculate(-17015, 15198), -1817, "")

    def test0788(self):
        self.assertEquals(self.calculate(-14753, -22799), 27984, "")

    def test0789(self):
        self.assertEquals(self.calculate(8130, 18621), 26751, "")

    def test0790(self):
        self.assertEquals(self.calculate(5338, 22225), 27563, "")

    def test0791(self):
        self.assertEquals(self.calculate(-6816, 25972), 19156, "")

    def test0792(self):
        self.assertEquals(self.calculate(30208, -9545), 20663, "")

    def test0793(self):
        self.assertEquals(self.calculate(-25888, -11304), 28344, "")

    def test0794(self):
        self.assertEquals(self.calculate(10136, -31989), -21853, "")

    def test0795(self):
        self.assertEquals(self.calculate(18836, 24466), -22234, "")

    def test0796(self):
        self.assertEquals(self.calculate(14248, 24863), -26425, "")

    def test0797(self):
        self.assertEquals(self.calculate(12763, 16293), 29056, "")

    def test0798(self):
        self.assertEquals(self.calculate(-26974, 22653), -4321, "")

    def test0799(self):
        self.assertEquals(self.calculate(14164, 14247), 28411, "")

    def test0800(self):
        self.assertEquals(self.calculate(-22229, 22626), 397, "")

    def test0801(self):
        self.assertEquals(self.calculate(24507, 10152), -30877, "")

    def test0802(self):
        self.assertEquals(self.calculate(2340, 19059), 21399, "")

    def test0803(self):
        self.assertEquals(self.calculate(-29373, 3902), -25471, "")

    def test0804(self):
        self.assertEquals(self.calculate(-11199, -12140), -23339, "")

    def test0805(self):
        self.assertEquals(self.calculate(-9818, -2034), -11852, "")

    def test0806(self):
        self.assertEquals(self.calculate(-14675, -11657), -26332, "")

    def test0807(self):
        self.assertEquals(self.calculate(-2029, 26589), 24560, "")

    def test0808(self):
        self.assertEquals(self.calculate(-28520, 6215), -22305, "")

    def test0809(self):
        self.assertEquals(self.calculate(13941, 1713), 15654, "")

    def test0810(self):
        self.assertEquals(self.calculate(13376, 10335), 23711, "")

    def test0811(self):
        self.assertEquals(self.calculate(16847, 14765), 31612, "")

    def test0812(self):
        self.assertEquals(self.calculate(28924, -15049), 13875, "")

    def test0813(self):
        self.assertEquals(self.calculate(26829, -6605), 20224, "")

    def test0814(self):
        self.assertEquals(self.calculate(-14555, -18004), -32559, "")

    def test0815(self):
        self.assertEquals(self.calculate(1144, 24164), 25308, "")

    def test0816(self):
        self.assertEquals(self.calculate(5333, 16896), 22229, "")

    def test0817(self):
        self.assertEquals(self.calculate(-10682, -6783), -17465, "")

    def test0818(self):
        self.assertEquals(self.calculate(13227, 3680), 16907, "")

    def test0819(self):
        self.assertEquals(self.calculate(-12727, -8606), -21333, "")

    def test0820(self):
        self.assertEquals(self.calculate(-31331, -3046), 31159, "")

    def test0821(self):
        self.assertEquals(self.calculate(-18548, -8023), -26571, "")

    def test0822(self):
        self.assertEquals(self.calculate(31339, -17642), 13697, "")

    def test0823(self):
        self.assertEquals(self.calculate(10460, -29184), -18724, "")

    def test0824(self):
        self.assertEquals(self.calculate(18055, 21468), -26013, "")

    def test0825(self):
        self.assertEquals(self.calculate(-28370, -10954), 26212, "")

    def test0826(self):
        self.assertEquals(self.calculate(13734, 12676), 26410, "")

    def test0827(self):
        self.assertEquals(self.calculate(6221, 6426), 12647, "")

    def test0828(self):
        self.assertEquals(self.calculate(32680, 23167), -9689, "")

    def test0829(self):
        self.assertEquals(self.calculate(29492, 15662), -20382, "")

    def test0830(self):
        self.assertEquals(self.calculate(28608, -16126), 12482, "")

    def test0831(self):
        self.assertEquals(self.calculate(13737, 12026), 25763, "")

    def test0832(self):
        self.assertEquals(self.calculate(-23977, -28863), 12696, "")

    def test0833(self):
        self.assertEquals(self.calculate(27687, 25446), -12403, "")

    def test0834(self):
        self.assertEquals(self.calculate(25484, 31642), -8410, "")

    def test0835(self):
        self.assertEquals(self.calculate(32763, -6306), 26457, "")

    def test0836(self):
        self.assertEquals(self.calculate(-3714, -11830), -15544, "")

    def test0837(self):
        self.assertEquals(self.calculate(-28764, 10039), -18725, "")

    def test0838(self):
        self.assertEquals(self.calculate(-15720, -16038), -31758, "")

    def test0839(self):
        self.assertEquals(self.calculate(4620, -2602), 2018, "")

    def test0840(self):
        self.assertEquals(self.calculate(23575, 2363), 25938, "")

    def test0841(self):
        self.assertEquals(self.calculate(30759, -13095), 17664, "")

    def test0842(self):
        self.assertEquals(self.calculate(-14866, -23351), 27319, "")

    def test0843(self):
        self.assertEquals(self.calculate(-8095, 29208), 21113, "")

    def test0844(self):
        self.assertEquals(self.calculate(-19334, 20050), 716, "")

    def test0845(self):
        self.assertEquals(self.calculate(-4028, -28828), 32680, "")

    def test0846(self):
        self.assertEquals(self.calculate(12195, -379), 11816, "")

    def test0847(self):
        self.assertEquals(self.calculate(-5791, 29196), 23405, "")

    def test0848(self):
        self.assertEquals(self.calculate(-32211, -23005), 10320, "")

    def test0849(self):
        self.assertEquals(self.calculate(-9106, -1421), -10527, "")

    def test0850(self):
        self.assertEquals(self.calculate(-22618, 31198), 8580, "")

    def test0851(self):
        self.assertEquals(self.calculate(-27195, 5364), -21831, "")

    def test0852(self):
        self.assertEquals(self.calculate(13181, 25908), -26447, "")

    def test0853(self):
        self.assertEquals(self.calculate(-2379, 739), -1640, "")

    def test0854(self):
        self.assertEquals(self.calculate(1864, -2406), -542, "")

    def test0855(self):
        self.assertEquals(self.calculate(-7104, 3236), -3868, "")

    def test0856(self):
        self.assertEquals(self.calculate(15505, -4083), 11422, "")

    def test0857(self):
        self.assertEquals(self.calculate(-12221, 2784), -9437, "")

    def test0858(self):
        self.assertEquals(self.calculate(14846, 153), 14999, "")

    def test0859(self):
        self.assertEquals(self.calculate(21161, -15280), 5881, "")

    def test0860(self):
        self.assertEquals(self.calculate(9225, 31187), -25124, "")

    def test0861(self):
        self.assertEquals(self.calculate(-4492, 24475), 19983, "")

    def test0862(self):
        self.assertEquals(self.calculate(-11728, 23883), 12155, "")

    def test0863(self):
        self.assertEquals(self.calculate(-28078, 1805), -26273, "")

    def test0864(self):
        self.assertEquals(self.calculate(25302, 7506), -32728, "")

    def test0865(self):
        self.assertEquals(self.calculate(-25403, -28651), 11482, "")

    def test0866(self):
        self.assertEquals(self.calculate(32278, 6119), -27139, "")

    def test0867(self):
        self.assertEquals(self.calculate(1822, 7970), 9792, "")

    def test0868(self):
        self.assertEquals(self.calculate(-30611, -20096), 14829, "")

    def test0869(self):
        self.assertEquals(self.calculate(-31327, 10347), -20980, "")

    def test0870(self):
        self.assertEquals(self.calculate(-29320, 32173), 2853, "")

    def test0871(self):
        self.assertEquals(self.calculate(26705, 10407), -28424, "")

    def test0872(self):
        self.assertEquals(self.calculate(3880, -23490), -19610, "")

    def test0873(self):
        self.assertEquals(self.calculate(-6307, 10114), 3807, "")

    def test0874(self):
        self.assertEquals(self.calculate(-9155, 16961), 7806, "")

    def test0875(self):
        self.assertEquals(self.calculate(-31823, -11147), 22566, "")

    def test0876(self):
        self.assertEquals(self.calculate(-1639, 18617), 16978, "")

    def test0877(self):
        self.assertEquals(self.calculate(-185, 28480), 28295, "")

    def test0878(self):
        self.assertEquals(self.calculate(-10341, -27499), 27696, "")

    def test0879(self):
        self.assertEquals(self.calculate(19724, 14879), -30933, "")

    def test0880(self):
        self.assertEquals(self.calculate(12266, 30445), -22825, "")

    def test0881(self):
        self.assertEquals(self.calculate(-17778, -10538), -28316, "")

    def test0882(self):
        self.assertEquals(self.calculate(6496, -26489), -19993, "")

    def test0883(self):
        self.assertEquals(self.calculate(20936, -9029), 11907, "")

    def test0884(self):
        self.assertEquals(self.calculate(22390, -28097), -5707, "")

    def test0885(self):
        self.assertEquals(self.calculate(3658, 8325), 11983, "")

    def test0886(self):
        self.assertEquals(self.calculate(-11599, 10454), -1145, "")

    def test0887(self):
        self.assertEquals(self.calculate(-28366, -2924), -31290, "")

    def test0888(self):
        self.assertEquals(self.calculate(-2807, -25792), -28599, "")

    def test0889(self):
        self.assertEquals(self.calculate(7285, -25770), -18485, "")

    def test0890(self):
        self.assertEquals(self.calculate(-26406, 27328), 922, "")

    def test0891(self):
        self.assertEquals(self.calculate(-18748, 19964), 1216, "")

    def test0892(self):
        self.assertEquals(self.calculate(19610, -5746), 13864, "")

    def test0893(self):
        self.assertEquals(self.calculate(24142, -16961), 7181, "")

    def test0894(self):
        self.assertEquals(self.calculate(-18286, 27951), 9665, "")

    def test0895(self):
        self.assertEquals(self.calculate(20782, -28091), -7309, "")

    def test0896(self):
        self.assertEquals(self.calculate(20235, -29899), -9664, "")

    def test0897(self):
        self.assertEquals(self.calculate(-4493, 5837), 1344, "")

    def test0898(self):
        self.assertEquals(self.calculate(7616, -24), 7592, "")

    def test0899(self):
        self.assertEquals(self.calculate(14156, 650), 14806, "")

    def test0900(self):
        self.assertEquals(self.calculate(-4740, 7550), 2810, "")

    def test0901(self):
        self.assertEquals(self.calculate(23835, -14625), 9210, "")

    def test0902(self):
        self.assertEquals(self.calculate(24123, -29786), -5663, "")

    def test0903(self):
        self.assertEquals(self.calculate(-30394, 23865), -6529, "")

    def test0904(self):
        self.assertEquals(self.calculate(-30943, -2219), 32374, "")

    def test0905(self):
        self.assertEquals(self.calculate(12617, 7319), 19936, "")

    def test0906(self):
        self.assertEquals(self.calculate(-32021, -18207), 15308, "")

    def test0907(self):
        self.assertEquals(self.calculate(28713, 14971), -21852, "")

    def test0908(self):
        self.assertEquals(self.calculate(-12485, -22577), 30474, "")

    def test0909(self):
        self.assertEquals(self.calculate(23813, -24690), -877, "")

    def test0910(self):
        self.assertEquals(self.calculate(21775, -4375), 17400, "")

    def test0911(self):
        self.assertEquals(self.calculate(-6136, 19119), 12983, "")

    def test0912(self):
        self.assertEquals(self.calculate(20556, -17355), 3201, "")

    def test0913(self):
        self.assertEquals(self.calculate(4805, -19788), -14983, "")

    def test0914(self):
        self.assertEquals(self.calculate(4842, 22633), 27475, "")

    def test0915(self):
        self.assertEquals(self.calculate(-8907, 13427), 4520, "")

    def test0916(self):
        self.assertEquals(self.calculate(15284, -30392), -15108, "")

    def test0917(self):
        self.assertEquals(self.calculate(10190, -7561), 2629, "")

    def test0918(self):
        self.assertEquals(self.calculate(-19256, 7472), -11784, "")

    def test0919(self):
        self.assertEquals(self.calculate(10478, -14689), -4211, "")

    def test0920(self):
        self.assertEquals(self.calculate(24850, 31736), -8950, "")

    def test0921(self):
        self.assertEquals(self.calculate(14507, 31937), -19092, "")

    def test0922(self):
        self.assertEquals(self.calculate(-984, -4157), -5141, "")

    def test0923(self):
        self.assertEquals(self.calculate(13084, 25398), -27054, "")

    def test0924(self):
        self.assertEquals(self.calculate(30659, 19699), -15178, "")

    def test0925(self):
        self.assertEquals(self.calculate(28812, 19657), -17067, "")

    def test0926(self):
        self.assertEquals(self.calculate(6382, -22019), -15637, "")

    def test0927(self):
        self.assertEquals(self.calculate(-12221, -27837), 25478, "")

    def test0928(self):
        self.assertEquals(self.calculate(-31783, 567), -31216, "")

    def test0929(self):
        self.assertEquals(self.calculate(-31543, 12328), -19215, "")

    def test0930(self):
        self.assertEquals(self.calculate(5108, 32172), -28256, "")

    def test0931(self):
        self.assertEquals(self.calculate(-20600, 24922), 4322, "")

    def test0932(self):
        self.assertEquals(self.calculate(28578, 11722), -25236, "")

    def test0933(self):
        self.assertEquals(self.calculate(-25838, 15176), -10662, "")

    def test0934(self):
        self.assertEquals(self.calculate(-8474, -13225), -21699, "")

    def test0935(self):
        self.assertEquals(self.calculate(-2031, 5458), 3427, "")

    def test0936(self):
        self.assertEquals(self.calculate(-30269, 15578), -14691, "")

    def test0937(self):
        self.assertEquals(self.calculate(-12490, 3500), -8990, "")

    def test0938(self):
        self.assertEquals(self.calculate(-8035, -9384), -17419, "")

    def test0939(self):
        self.assertEquals(self.calculate(-15992, -22745), 26799, "")

    def test0940(self):
        self.assertEquals(self.calculate(20849, 3026), 23875, "")

    def test0941(self):
        self.assertEquals(self.calculate(-28894, 25353), -3541, "")

    def test0942(self):
        self.assertEquals(self.calculate(-3283, 8974), 5691, "")

    def test0943(self):
        self.assertEquals(self.calculate(20890, -2946), 17944, "")

    def test0944(self):
        self.assertEquals(self.calculate(-14212, 23473), 9261, "")

    def test0945(self):
        self.assertEquals(self.calculate(9738, -4863), 4875, "")

    def test0946(self):
        self.assertEquals(self.calculate(-23802, 17550), -6252, "")

    def test0947(self):
        self.assertEquals(self.calculate(16651, -29615), -12964, "")

    def test0948(self):
        self.assertEquals(self.calculate(23146, -444), 22702, "")

    def test0949(self):
        self.assertEquals(self.calculate(19128, -25469), -6341, "")

    def test0950(self):
        self.assertEquals(self.calculate(-6285, 22259), 15974, "")

    def test0951(self):
        self.assertEquals(self.calculate(16458, 1404), 17862, "")

    def test0952(self):
        self.assertEquals(self.calculate(-15788, 18059), 2271, "")

    def test0953(self):
        self.assertEquals(self.calculate(-24340, 31760), 7420, "")

    def test0954(self):
        self.assertEquals(self.calculate(30097, 27610), -7829, "")

    def test0955(self):
        self.assertEquals(self.calculate(-3142, -26185), -29327, "")

    def test0956(self):
        self.assertEquals(self.calculate(128, 11588), 11716, "")

    def test0957(self):
        self.assertEquals(self.calculate(20077, 6885), 26962, "")

    def test0958(self):
        self.assertEquals(self.calculate(-9241, 19417), 10176, "")

    def test0959(self):
        self.assertEquals(self.calculate(-4326, -12468), -16794, "")

    def test0960(self):
        self.assertEquals(self.calculate(-95, 11408), 11313, "")

    def test0961(self):
        self.assertEquals(self.calculate(12719, -7892), 4827, "")

    def test0962(self):
        self.assertEquals(self.calculate(1846, -22804), -20958, "")

    def test0963(self):
        self.assertEquals(self.calculate(11666, 13643), 25309, "")

    def test0964(self):
        self.assertEquals(self.calculate(9319, 24677), -31540, "")

    def test0965(self):
        self.assertEquals(self.calculate(-11732, -3780), -15512, "")

    def test0966(self):
        self.assertEquals(self.calculate(-14837, -2887), -17724, "")

    def test0967(self):
        self.assertEquals(self.calculate(-26647, 1568), -25079, "")

    def test0968(self):
        self.assertEquals(self.calculate(-21703, -6144), -27847, "")

    def test0969(self):
        self.assertEquals(self.calculate(-7262, -3570), -10832, "")

    def test0970(self):
        self.assertEquals(self.calculate(21136, 8673), 29809, "")

    def test0971(self):
        self.assertEquals(self.calculate(-31241, 26249), -4992, "")

    def test0972(self):
        self.assertEquals(self.calculate(6670, 31299), -27567, "")

    def test0973(self):
        self.assertEquals(self.calculate(-12272, -19354), -31626, "")

    def test0974(self):
        self.assertEquals(self.calculate(12533, -5144), 7389, "")

    def test0975(self):
        self.assertEquals(self.calculate(21658, 1248), 22906, "")

    def test0976(self):
        self.assertEquals(self.calculate(23505, -471), 23034, "")

    def test0977(self):
        self.assertEquals(self.calculate(-30154, 673), -29481, "")

    def test0978(self):
        self.assertEquals(self.calculate(-27351, -4478), -31829, "")

    def test0979(self):
        self.assertEquals(self.calculate(3361, -11365), -8004, "")

    def test0980(self):
        self.assertEquals(self.calculate(21880, 26883), -16773, "")

    def test0981(self):
        self.assertEquals(self.calculate(1513, 10441), 11954, "")

    def test0982(self):
        self.assertEquals(self.calculate(-22171, -24897), 18468, "")

    def test0983(self):
        self.assertEquals(self.calculate(17161, -14575), 2586, "")

    def test0984(self):
        self.assertEquals(self.calculate(-1600, 24380), 22780, "")

    def test0985(self):
        self.assertEquals(self.calculate(-2532, 31885), 29353, "")

    def test0986(self):
        self.assertEquals(self.calculate(30321, 3718), -31497, "")

    def test0987(self):
        self.assertEquals(self.calculate(-6604, 6629), 25, "")

    def test0988(self):
        self.assertEquals(self.calculate(31680, -15127), 16553, "")

    def test0989(self):
        self.assertEquals(self.calculate(2083, -5845), -3762, "")

    def test0990(self):
        self.assertEquals(self.calculate(-5052, 16300), 11248, "")

    def test0991(self):
        self.assertEquals(self.calculate(-30604, 18887), -11717, "")

    def test0992(self):
        self.assertEquals(self.calculate(17648, 18343), -29545, "")

    def test0993(self):
        self.assertEquals(self.calculate(7312, 25428), 32740, "")

    def test0994(self):
        self.assertEquals(self.calculate(-12769, 8484), -4285, "")

    def test0995(self):
        self.assertEquals(self.calculate(4940, -29255), -24315, "")

    def test0996(self):
        self.assertEquals(self.calculate(9424, 30419), -25693, "")

    def test0997(self):
        self.assertEquals(self.calculate(-3673, 20808), 17135, "")

    def test0998(self):
        self.assertEquals(self.calculate(11782, 18103), 29885, "")

    def test0999(self):
        self.assertEquals(self.calculate(30899, 29854), -4783, "")

    def test1000(self):
        self.assertEquals(self.calculate(-6695, 1976), -4719, "")

    def test1001(self):
        self.assertEquals(self.calculate(-7794, -31071), 26671, "")

    def test1002(self):
        self.assertEquals(self.calculate(25950, -557), 25393, "")

    def test1003(self):
        self.assertEquals(self.calculate(6947, 9661), 16608, "")

    def test1004(self):
        self.assertEquals(self.calculate(15146, 28946), -21444, "")

    def test1005(self):
        self.assertEquals(self.calculate(16596, -26176), -9580, "")

    def test1006(self):
        self.assertEquals(self.calculate(3418, -32303), -28885, "")

    def test1007(self):
        self.assertEquals(self.calculate(-7336, 2218), -5118, "")

    def test1008(self):
        self.assertEquals(self.calculate(-5954, -20273), -26227, "")

    def test1009(self):
        self.assertEquals(self.calculate(20174, -6056), 14118, "")

    def test1010(self):
        self.assertEquals(self.calculate(13275, -31479), -18204, "")

    def test1011(self):
        self.assertEquals(self.calculate(14360, -19095), -4735, "")

    def test1012(self):
        self.assertEquals(self.calculate(-7814, 14451), 6637, "")

    def test1013(self):
        self.assertEquals(self.calculate(-12919, -16912), -29831, "")

    def test1014(self):
        self.assertEquals(self.calculate(-18244, -10645), -28889, "")

    def test1015(self):
        self.assertEquals(self.calculate(29295, 27967), -8274, "")

    def test1016(self):
        self.assertEquals(self.calculate(27975, -12436), 15539, "")

    def test1017(self):
        self.assertEquals(self.calculate(-9451, 32369), 22918, "")

    def test1018(self):
        self.assertEquals(self.calculate(30329, -13662), 16667, "")

    def test1019(self):
        self.assertEquals(self.calculate(22385, 32423), -10728, "")

    def test1020(self):
        self.assertEquals(self.calculate(-32618, 2463), -30155, "")

    def test1021(self):
        self.assertEquals(self.calculate(-21279, 9730), -11549, "")

    def test1022(self):
        self.assertEquals(self.calculate(-22599, 32314), 9715, "")

    def test1023(self):
        self.assertEquals(self.calculate(-20224, 12461), -7763, "")


class TestVM_Add_IntLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushL(rhs)
        v.VM_Add()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-15423, 1614125735), 1614110312)

    def test0001(self):
        self.assertEquals(self.calculate(19118, 665377650), 665396768)

    def test0002(self):
        self.assertEquals(self.calculate(-17934, 1635585081), 1635567147)

    def test0003(self):
        self.assertEquals(self.calculate(5370, 1088635519), 1088640889)

    def test0004(self):
        self.assertEquals(self.calculate(21482, -1827993685), -1827972203)

    def test0005(self):
        self.assertEquals(self.calculate(15265, -270874147), -270858882)

    def test0006(self):
        self.assertEquals(self.calculate(-26786, -731521580), -731548366)

    def test0007(self):
        self.assertEquals(self.calculate(-14583, -818340320), -818354903)

    def test0008(self):
        self.assertEquals(self.calculate(-6748, -2032365222), -2032371970)

    def test0009(self):
        self.assertEquals(self.calculate(-7724, 1936966312), 1936958588)

    def test0010(self):
        self.assertEquals(self.calculate(-19759, -126732548), -126752307)

    def test0011(self):
        self.assertEquals(self.calculate(11687, -978943965), -978932278)

    def test0012(self):
        self.assertEquals(self.calculate(29753, 617901034), 617930787)

    def test0013(self):
        self.assertEquals(self.calculate(-24310, -1611329463), -1611353773)

    def test0014(self):
        self.assertEquals(self.calculate(16128, 1827880273), 1827896401)

    def test0015(self):
        self.assertEquals(self.calculate(32005, 604653795), 604685800)

    def test0016(self):
        self.assertEquals(self.calculate(9210, 1293027899), 1293037109)

    def test0017(self):
        self.assertEquals(self.calculate(2021, -1129730389), -1129728368)

    def test0018(self):
        self.assertEquals(self.calculate(4861, 2063772812), 2063777673)

    def test0019(self):
        self.assertEquals(self.calculate(-22159, -807984094), -808006253)

    def test0020(self):
        self.assertEquals(self.calculate(-22840, -1061418209), -1061441049)

    def test0021(self):
        self.assertEquals(self.calculate(31613, -490996692), -490965079)

    def test0022(self):
        self.assertEquals(self.calculate(-25409, 1401259511), 1401234102)

    def test0023(self):
        self.assertEquals(self.calculate(-1932, -412559724), -412561656)

    def test0024(self):
        self.assertEquals(self.calculate(-18215, -1498913169), -1498931384)

    def test0025(self):
        self.assertEquals(self.calculate(-18468, 1591745693), 1591727225)

    def test0026(self):
        self.assertEquals(self.calculate(-8398, -1284873022), -1284881420)

    def test0027(self):
        self.assertEquals(self.calculate(32362, -1896906743), -1896874381)

    def test0028(self):
        self.assertEquals(self.calculate(-18994, -259798141), -259817135)

    def test0029(self):
        self.assertEquals(self.calculate(-5320, -1332634297), -1332639617)

    def test0030(self):
        self.assertEquals(self.calculate(-3109, -599240096), -599243205)

    def test0031(self):
        self.assertEquals(self.calculate(11447, -514636546), -514625099)

    def test0032(self):
        self.assertEquals(self.calculate(-9512, 907790035), 907780523)

    def test0033(self):
        self.assertEquals(self.calculate(9059, 465361274), 465370333)

    def test0034(self):
        self.assertEquals(self.calculate(20729, 1692432968), 1692453697)

    def test0035(self):
        self.assertEquals(self.calculate(-4726, 325114393), 325109667)

    def test0036(self):
        self.assertEquals(self.calculate(12625, 1853298401), 1853311026)

    def test0037(self):
        self.assertEquals(self.calculate(31841, -423920737), -423888896)

    def test0038(self):
        self.assertEquals(self.calculate(3290, -1484269391), -1484266101)

    def test0039(self):
        self.assertEquals(self.calculate(26163, -1003905217), -1003879054)

    def test0040(self):
        self.assertEquals(self.calculate(-13794, -1481622705), -1481636499)

    def test0041(self):
        self.assertEquals(self.calculate(-8632, -1798862759), -1798871391)

    def test0042(self):
        self.assertEquals(self.calculate(14613, 1308464315), 1308478928)

    def test0043(self):
        self.assertEquals(self.calculate(-4180, 1140761513), 1140757333)

    def test0044(self):
        self.assertEquals(self.calculate(30226, -1332128824), -1332098598)

    def test0045(self):
        self.assertEquals(self.calculate(26931, -2017946921), -2017919990)

    def test0046(self):
        self.assertEquals(self.calculate(-13863, 1357567597), 1357553734)

    def test0047(self):
        self.assertEquals(self.calculate(604, -765264521), -765263917)

    def test0048(self):
        self.assertEquals(self.calculate(-19560, -527584556), -527604116)

    def test0049(self):
        self.assertEquals(self.calculate(31673, 609652348), 609684021)

    def test0050(self):
        self.assertEquals(self.calculate(22209, 542536757), 542558966)

    def test0051(self):
        self.assertEquals(self.calculate(-15049, 1574816794), 1574801745)

    def test0052(self):
        self.assertEquals(self.calculate(18084, 1911963697), 1911981781)

    def test0053(self):
        self.assertEquals(self.calculate(19954, 573379381), 573399335)

    def test0054(self):
        self.assertEquals(self.calculate(13084, 1956883853), 1956896937)

    def test0055(self):
        self.assertEquals(self.calculate(29903, -40828559), -40798656)

    def test0056(self):
        self.assertEquals(self.calculate(3594, -653231947), -653228353)

    def test0057(self):
        self.assertEquals(self.calculate(-30347, 269417603), 269387256)

    def test0058(self):
        self.assertEquals(self.calculate(-30331, -691011321), -691041652)

    def test0059(self):
        self.assertEquals(self.calculate(945, -1297927755), -1297926810)

    def test0060(self):
        self.assertEquals(self.calculate(16061, -1588472918), -1588456857)

    def test0061(self):
        self.assertEquals(self.calculate(-28373, 1256218916), 1256190543)

    def test0062(self):
        self.assertEquals(self.calculate(25036, -917213607), -917188571)

    def test0063(self):
        self.assertEquals(self.calculate(-15363, -1184568409), -1184583772)

    def test0064(self):
        self.assertEquals(self.calculate(-14765, -1783211916), -1783226681)

    def test0065(self):
        self.assertEquals(self.calculate(15291, 1930055730), 1930071021)

    def test0066(self):
        self.assertEquals(self.calculate(-5817, -1754540458), -1754546275)

    def test0067(self):
        self.assertEquals(self.calculate(17122, 641662480), 641679602)

    def test0068(self):
        self.assertEquals(self.calculate(-6800, 109976673), 109969873)

    def test0069(self):
        self.assertEquals(self.calculate(618, 1448218148), 1448218766)

    def test0070(self):
        self.assertEquals(self.calculate(-27652, 1061762959), 1061735307)

    def test0071(self):
        self.assertEquals(self.calculate(1518, 333975013), 333976531)

    def test0072(self):
        self.assertEquals(self.calculate(17569, -2026598441), -2026580872)

    def test0073(self):
        self.assertEquals(self.calculate(1656, 980337285), 980338941)

    def test0074(self):
        self.assertEquals(self.calculate(25554, -1740868846), -1740843292)

    def test0075(self):
        self.assertEquals(self.calculate(3516, -1054878751), -1054875235)

    def test0076(self):
        self.assertEquals(self.calculate(-30220, 673232689), 673202469)

    def test0077(self):
        self.assertEquals(self.calculate(29585, -1975441471), -1975411886)

    def test0078(self):
        self.assertEquals(self.calculate(-11360, -553887852), -553899212)

    def test0079(self):
        self.assertEquals(self.calculate(32411, 30192306), 30224717)

    def test0080(self):
        self.assertEquals(self.calculate(-10791, 1601420270), 1601409479)

    def test0081(self):
        self.assertEquals(self.calculate(-314, 88682679), 88682365)

    def test0082(self):
        self.assertEquals(self.calculate(-966, 924972594), 924971628)

    def test0083(self):
        self.assertEquals(self.calculate(-1726, 1383577663), 1383575937)

    def test0084(self):
        self.assertEquals(self.calculate(12535, -1485048911), -1485036376)

    def test0085(self):
        self.assertEquals(self.calculate(-6851, 1765958042), 1765951191)

    def test0086(self):
        self.assertEquals(self.calculate(8161, -1304632853), -1304624692)

    def test0087(self):
        self.assertEquals(self.calculate(-11881, -769183342), -769195223)

    def test0088(self):
        self.assertEquals(self.calculate(30323, -88595880), -88565557)

    def test0089(self):
        self.assertEquals(self.calculate(2620, -1662156859), -1662154239)

    def test0090(self):
        self.assertEquals(self.calculate(13972, 1101685367), 1101699339)

    def test0091(self):
        self.assertEquals(self.calculate(-24963, -1939457984), -1939482947)

    def test0092(self):
        self.assertEquals(self.calculate(-27163, -485305652), -485332815)

    def test0093(self):
        self.assertEquals(self.calculate(-23096, -696833157), -696856253)

    def test0094(self):
        self.assertEquals(self.calculate(-7760, -648894258), -648902018)

    def test0095(self):
        self.assertEquals(self.calculate(-15104, -1717752311), -1717767415)

    def test0096(self):
        self.assertEquals(self.calculate(9342, 1990244771), 1990254113)

    def test0097(self):
        self.assertEquals(self.calculate(-4731, 1831711327), 1831706596)

    def test0098(self):
        self.assertEquals(self.calculate(2540, -1554816521), -1554813981)

    def test0099(self):
        self.assertEquals(self.calculate(-22883, 4374058), 4351175)

    def test0100(self):
        self.assertEquals(self.calculate(1929, 2132826695), 2132828624)

    def test0101(self):
        self.assertEquals(self.calculate(-23407, -1005248022), -1005271429)

    def test0102(self):
        self.assertEquals(self.calculate(10894, 684545410), 684556304)

    def test0103(self):
        self.assertEquals(self.calculate(20212, 856183870), 856204082)

    def test0104(self):
        self.assertEquals(self.calculate(-10913, -1995534660), -1995545573)

    def test0105(self):
        self.assertEquals(self.calculate(31287, 1119976540), 1120007827)

    def test0106(self):
        self.assertEquals(self.calculate(9563, -1916951428), -1916941865)

    def test0107(self):
        self.assertEquals(self.calculate(3732, -1505909319), -1505905587)

    def test0108(self):
        self.assertEquals(self.calculate(2742, 88963133), 88965875)

    def test0109(self):
        self.assertEquals(self.calculate(22021, -1763300592), -1763278571)

    def test0110(self):
        self.assertEquals(self.calculate(4290, 2019102825), 2019107115)

    def test0111(self):
        self.assertEquals(self.calculate(16780, 1231135991), 1231152771)

    def test0112(self):
        self.assertEquals(self.calculate(32573, -1020987472), -1020954899)

    def test0113(self):
        self.assertEquals(self.calculate(-21514, -229326567), -229348081)

    def test0114(self):
        self.assertEquals(self.calculate(-7834, -1791570454), -1791578288)

    def test0115(self):
        self.assertEquals(self.calculate(-1827, -106015185), -106017012)

    def test0116(self):
        self.assertEquals(self.calculate(24947, 1266035822), 1266060769)

    def test0117(self):
        self.assertEquals(self.calculate(-14261, 792852526), 792838265)

    def test0118(self):
        self.assertEquals(self.calculate(-622, -416553588), -416554210)

    def test0119(self):
        self.assertEquals(self.calculate(6373, 1257964214), 1257970587)

    def test0120(self):
        self.assertEquals(self.calculate(-24504, 1115145478), 1115120974)

    def test0121(self):
        self.assertEquals(self.calculate(-20788, -1520507202), -1520527990)

    def test0122(self):
        self.assertEquals(self.calculate(-21825, 2071965768), 2071943943)

    def test0123(self):
        self.assertEquals(self.calculate(25256, 621625610), 621650866)

    def test0124(self):
        self.assertEquals(self.calculate(-18908, -629110773), -629129681)

    def test0125(self):
        self.assertEquals(self.calculate(11654, -1635680030), -1635668376)

    def test0126(self):
        self.assertEquals(self.calculate(-3662, -716532187), -716535849)

    def test0127(self):
        self.assertEquals(self.calculate(-26550, -1706271916), -1706298466)

    def test0128(self):
        self.assertEquals(self.calculate(18991, 1019028009), 1019047000)

    def test0129(self):
        self.assertEquals(self.calculate(-14394, -1716670667), -1716685061)

    def test0130(self):
        self.assertEquals(self.calculate(31873, -1429522623), -1429490750)

    def test0131(self):
        self.assertEquals(self.calculate(15953, 982901528), 982917481)

    def test0132(self):
        self.assertEquals(self.calculate(350, 24231313), 24231663)

    def test0133(self):
        self.assertEquals(self.calculate(-7385, -1728017135), -1728024520)

    def test0134(self):
        self.assertEquals(self.calculate(12122, 1611993127), 1612005249)

    def test0135(self):
        self.assertEquals(self.calculate(-23324, -1892151967), -1892175291)

    def test0136(self):
        self.assertEquals(self.calculate(17717, 1746592241), 1746609958)

    def test0137(self):
        self.assertEquals(self.calculate(9007, -738451696), -738442689)

    def test0138(self):
        self.assertEquals(self.calculate(2528, -1441873068), -1441870540)

    def test0139(self):
        self.assertEquals(self.calculate(-16635, -227056551), -227073186)

    def test0140(self):
        self.assertEquals(self.calculate(28695, -1795009136), -1794980441)

    def test0141(self):
        self.assertEquals(self.calculate(1816, 1978302530), 1978304346)

    def test0142(self):
        self.assertEquals(self.calculate(-17906, 2122973987), 2122956081)

    def test0143(self):
        self.assertEquals(self.calculate(-4474, 1206766085), 1206761611)

    def test0144(self):
        self.assertEquals(self.calculate(24027, 107680386), 107704413)

    def test0145(self):
        self.assertEquals(self.calculate(-30789, -765634273), -765665062)

    def test0146(self):
        self.assertEquals(self.calculate(31684, -908590422), -908558738)

    def test0147(self):
        self.assertEquals(self.calculate(-23576, 519861392), 519837816)

    def test0148(self):
        self.assertEquals(self.calculate(-4513, 1329169313), 1329164800)

    def test0149(self):
        self.assertEquals(self.calculate(-28220, -1721638884), -1721667104)

    def test0150(self):
        self.assertEquals(self.calculate(-18907, -619889063), -619907970)

    def test0151(self):
        self.assertEquals(self.calculate(15432, 1933507453), 1933522885)

    def test0152(self):
        self.assertEquals(self.calculate(8583, 1596641072), 1596649655)

    def test0153(self):
        self.assertEquals(self.calculate(-20558, 844743436), 844722878)

    def test0154(self):
        self.assertEquals(self.calculate(20534, -62819255), -62798721)

    def test0155(self):
        self.assertEquals(self.calculate(-28382, -2023316669), -2023345051)

    def test0156(self):
        self.assertEquals(self.calculate(15015, 1934657192), 1934672207)

    def test0157(self):
        self.assertEquals(self.calculate(-13388, 1286269918), 1286256530)

    def test0158(self):
        self.assertEquals(self.calculate(15479, 912030740), 912046219)

    def test0159(self):
        self.assertEquals(self.calculate(-712, 614533851), 614533139)

    def test0160(self):
        self.assertEquals(self.calculate(-6414, -976577714), -976584128)

    def test0161(self):
        self.assertEquals(self.calculate(4851, -840340885), -840336034)

    def test0162(self):
        self.assertEquals(self.calculate(22895, 602129569), 602152464)

    def test0163(self):
        self.assertEquals(self.calculate(-10954, -1178037357), -1178048311)

    def test0164(self):
        self.assertEquals(self.calculate(-19854, 1341980694), 1341960840)

    def test0165(self):
        self.assertEquals(self.calculate(19397, 1193442600), 1193461997)

    def test0166(self):
        self.assertEquals(self.calculate(17304, 718730801), 718748105)

    def test0167(self):
        self.assertEquals(self.calculate(-13402, 1147948488), 1147935086)

    def test0168(self):
        self.assertEquals(self.calculate(2343, -1609595798), -1609593455)

    def test0169(self):
        self.assertEquals(self.calculate(-21127, -357781069), -357802196)

    def test0170(self):
        self.assertEquals(self.calculate(-26782, -599804655), -599831437)

    def test0171(self):
        self.assertEquals(self.calculate(15034, 896693218), 896708252)

    def test0172(self):
        self.assertEquals(self.calculate(29783, 1396076566), 1396106349)

    def test0173(self):
        self.assertEquals(self.calculate(5534, 983283741), 983289275)

    def test0174(self):
        self.assertEquals(self.calculate(-17931, -1354872911), -1354890842)

    def test0175(self):
        self.assertEquals(self.calculate(26316, -518505006), -518478690)

    def test0176(self):
        self.assertEquals(self.calculate(-5647, -1641667572), -1641673219)

    def test0177(self):
        self.assertEquals(self.calculate(-13298, 1032581573), 1032568275)

    def test0178(self):
        self.assertEquals(self.calculate(9514, 958598379), 958607893)

    def test0179(self):
        self.assertEquals(self.calculate(13290, 1573098474), 1573111764)

    def test0180(self):
        self.assertEquals(self.calculate(-6575, 1993161632), 1993155057)

    def test0181(self):
        self.assertEquals(self.calculate(3954, 101648317), 101652271)

    def test0182(self):
        self.assertEquals(self.calculate(-14199, 1130605300), 1130591101)

    def test0183(self):
        self.assertEquals(self.calculate(-28926, 835863620), 835834694)

    def test0184(self):
        self.assertEquals(self.calculate(-7888, 1675024028), 1675016140)

    def test0185(self):
        self.assertEquals(self.calculate(-6911, 1523810747), 1523803836)

    def test0186(self):
        self.assertEquals(self.calculate(-23258, -1115687544), -1115710802)

    def test0187(self):
        self.assertEquals(self.calculate(-11330, -927494163), -927505493)

    def test0188(self):
        self.assertEquals(self.calculate(-9611, 2140442853), 2140433242)

    def test0189(self):
        self.assertEquals(self.calculate(4212, 1418397970), 1418402182)

    def test0190(self):
        self.assertEquals(self.calculate(-83, 514342978), 514342895)

    def test0191(self):
        self.assertEquals(self.calculate(-7778, 496190996), 496183218)

    def test0192(self):
        self.assertEquals(self.calculate(-22798, 2124774555), 2124751757)

    def test0193(self):
        self.assertEquals(self.calculate(32566, -474929878), -474897312)

    def test0194(self):
        self.assertEquals(self.calculate(891, 1018664924), 1018665815)

    def test0195(self):
        self.assertEquals(self.calculate(5684, -754788531), -754782847)

    def test0196(self):
        self.assertEquals(self.calculate(5302, -189039670), -189034368)

    def test0197(self):
        self.assertEquals(self.calculate(-4505, -1110829659), -1110834164)

    def test0198(self):
        self.assertEquals(self.calculate(7134, 898267577), 898274711)

    def test0199(self):
        self.assertEquals(self.calculate(11938, 1526798974), 1526810912)

    def test0200(self):
        self.assertEquals(self.calculate(8906, 1817004353), 1817013259)

    def test0201(self):
        self.assertEquals(self.calculate(-2569, 1720734524), 1720731955)

    def test0202(self):
        self.assertEquals(self.calculate(17159, 1266466196), 1266483355)

    def test0203(self):
        self.assertEquals(self.calculate(-10746, 213592621), 213581875)

    def test0204(self):
        self.assertEquals(self.calculate(-1487, 2112230238), 2112228751)

    def test0205(self):
        self.assertEquals(self.calculate(169, -1918341552), -1918341383)

    def test0206(self):
        self.assertEquals(self.calculate(11719, -243810677), -243798958)

    def test0207(self):
        self.assertEquals(self.calculate(14983, 1957069548), 1957084531)

    def test0208(self):
        self.assertEquals(self.calculate(-477, -1993801906), -1993802383)

    def test0209(self):
        self.assertEquals(self.calculate(-14139, -165357499), -165371638)

    def test0210(self):
        self.assertEquals(self.calculate(26949, -161014496), -160987547)

    def test0211(self):
        self.assertEquals(self.calculate(9802, 80186604), 80196406)

    def test0212(self):
        self.assertEquals(self.calculate(2761, 604093526), 604096287)

    def test0213(self):
        self.assertEquals(self.calculate(-2302, 2120089552), 2120087250)

    def test0214(self):
        self.assertEquals(self.calculate(-2803, 447364207), 447361404)

    def test0215(self):
        self.assertEquals(self.calculate(3808, 1286417315), 1286421123)

    def test0216(self):
        self.assertEquals(self.calculate(3778, -1724342345), -1724338567)

    def test0217(self):
        self.assertEquals(self.calculate(26728, -1445691492), -1445664764)

    def test0218(self):
        self.assertEquals(self.calculate(-6865, 2035041117), 2035034252)

    def test0219(self):
        self.assertEquals(self.calculate(-1137, 843929932), 843928795)

    def test0220(self):
        self.assertEquals(self.calculate(-15052, 150796159), 150781107)

    def test0221(self):
        self.assertEquals(self.calculate(-8271, -1726392014), -1726400285)

    def test0222(self):
        self.assertEquals(self.calculate(9220, -703513236), -703504016)

    def test0223(self):
        self.assertEquals(self.calculate(-22250, 976319691), 976297441)

    def test0224(self):
        self.assertEquals(self.calculate(-13497, 1769171627), 1769158130)

    def test0225(self):
        self.assertEquals(self.calculate(32708, 1392389520), 1392422228)

    def test0226(self):
        self.assertEquals(self.calculate(-3519, -279636720), -279640239)

    def test0227(self):
        self.assertEquals(self.calculate(-2519, -1726472621), -1726475140)

    def test0228(self):
        self.assertEquals(self.calculate(-28692, -23782089), -23810781)

    def test0229(self):
        self.assertEquals(self.calculate(-31892, 1505399868), 1505367976)

    def test0230(self):
        self.assertEquals(self.calculate(18497, 1899274567), 1899293064)

    def test0231(self):
        self.assertEquals(self.calculate(19346, 1447645167), 1447664513)

    def test0232(self):
        self.assertEquals(self.calculate(-22157, -1211453700), -1211475857)

    def test0233(self):
        self.assertEquals(self.calculate(-3077, -902931037), -902934114)

    def test0234(self):
        self.assertEquals(self.calculate(-1628, -129603561), -129605189)

    def test0235(self):
        self.assertEquals(self.calculate(22538, -1769323418), -1769300880)

    def test0236(self):
        self.assertEquals(self.calculate(-15270, -1232600892), -1232616162)

    def test0237(self):
        self.assertEquals(self.calculate(15542, -95601232), -95585690)

    def test0238(self):
        self.assertEquals(self.calculate(-17908, 106233626), 106215718)

    def test0239(self):
        self.assertEquals(self.calculate(-2730, -753563388), -753566118)

    def test0240(self):
        self.assertEquals(self.calculate(5415, 1416271455), 1416276870)

    def test0241(self):
        self.assertEquals(self.calculate(16349, 1167656426), 1167672775)

    def test0242(self):
        self.assertEquals(self.calculate(3045, 532756760), 532759805)

    def test0243(self):
        self.assertEquals(self.calculate(20912, -260137838), -260116926)

    def test0244(self):
        self.assertEquals(self.calculate(12999, -378399736), -378386737)

    def test0245(self):
        self.assertEquals(self.calculate(18404, 1456538613), 1456557017)

    def test0246(self):
        self.assertEquals(self.calculate(-25631, 2001976933), 2001951302)

    def test0247(self):
        self.assertEquals(self.calculate(-28041, -1546215553), -1546243594)

    def test0248(self):
        self.assertEquals(self.calculate(-32757, -1525515638), -1525548395)

    def test0249(self):
        self.assertEquals(self.calculate(-30732, -797916958), -797947690)

    def test0250(self):
        self.assertEquals(self.calculate(11139, -1781547034), -1781535895)

    def test0251(self):
        self.assertEquals(self.calculate(-14943, 1483990876), 1483975933)

    def test0252(self):
        self.assertEquals(self.calculate(17647, -1349773757), -1349756110)

    def test0253(self):
        self.assertEquals(self.calculate(-30936, 801124550), 801093614)

    def test0254(self):
        self.assertEquals(self.calculate(-10574, -2108470874), -2108481448)

    def test0255(self):
        self.assertEquals(self.calculate(-13068, -882908280), -882921348)

    def test0256(self):
        self.assertEquals(self.calculate(-525, -1408204609), -1408205134)

    def test0257(self):
        self.assertEquals(self.calculate(24915, -1278911530), -1278886615)

    def test0258(self):
        self.assertEquals(self.calculate(1880, -2018069545), -2018067665)

    def test0259(self):
        self.assertEquals(self.calculate(-10998, 742967028), 742956030)

    def test0260(self):
        self.assertEquals(self.calculate(-24786, 650321249), 650296463)

    def test0261(self):
        self.assertEquals(self.calculate(-23278, -1284525967), -1284549245)

    def test0262(self):
        self.assertEquals(self.calculate(6102, -1644206395), -1644200293)

    def test0263(self):
        self.assertEquals(self.calculate(28913, 419168395), 419197308)

    def test0264(self):
        self.assertEquals(self.calculate(30406, 117006490), 117036896)

    def test0265(self):
        self.assertEquals(self.calculate(-21592, -88823884), -88845476)

    def test0266(self):
        self.assertEquals(self.calculate(-16744, 468848171), 468831427)

    def test0267(self):
        self.assertEquals(self.calculate(-10987, -1442204646), -1442215633)

    def test0268(self):
        self.assertEquals(self.calculate(-28465, 1993333521), 1993305056)

    def test0269(self):
        self.assertEquals(self.calculate(13556, 2019112674), 2019126230)

    def test0270(self):
        self.assertEquals(self.calculate(9434, -1906660277), -1906650843)

    def test0271(self):
        self.assertEquals(self.calculate(-22396, 1535492672), 1535470276)

    def test0272(self):
        self.assertEquals(self.calculate(-20860, 952416820), 952395960)

    def test0273(self):
        self.assertEquals(self.calculate(-1719, 703898264), 703896545)

    def test0274(self):
        self.assertEquals(self.calculate(-10461, -2050463917), -2050474378)

    def test0275(self):
        self.assertEquals(self.calculate(-13271, 447444232), 447430961)

    def test0276(self):
        self.assertEquals(self.calculate(-8114, 489311999), 489303885)

    def test0277(self):
        self.assertEquals(self.calculate(24089, 1997530270), 1997554359)

    def test0278(self):
        self.assertEquals(self.calculate(-27617, -551427829), -551455446)

    def test0279(self):
        self.assertEquals(self.calculate(29574, 2087265232), 2087294806)

    def test0280(self):
        self.assertEquals(self.calculate(19417, -1650415330), -1650395913)

    def test0281(self):
        self.assertEquals(self.calculate(-15716, -2122564919), -2122580635)

    def test0282(self):
        self.assertEquals(self.calculate(-1661, -1301798951), -1301800612)

    def test0283(self):
        self.assertEquals(self.calculate(8251, -1524675326), -1524667075)

    def test0284(self):
        self.assertEquals(self.calculate(-26658, 413421072), 413394414)

    def test0285(self):
        self.assertEquals(self.calculate(-1499, 1996995066), 1996993567)

    def test0286(self):
        self.assertEquals(self.calculate(7877, -365858391), -365850514)

    def test0287(self):
        self.assertEquals(self.calculate(-13177, 1630743130), 1630729953)

    def test0288(self):
        self.assertEquals(self.calculate(31471, -51643049), -51611578)

    def test0289(self):
        self.assertEquals(self.calculate(-17842, 1465775212), 1465757370)

    def test0290(self):
        self.assertEquals(self.calculate(-5731, 354270135), 354264404)

    def test0291(self):
        self.assertEquals(self.calculate(-21860, -459692704), -459714564)

    def test0292(self):
        self.assertEquals(self.calculate(25061, -1790433541), -1790408480)

    def test0293(self):
        self.assertEquals(self.calculate(17973, -459734122), -459716149)

    def test0294(self):
        self.assertEquals(self.calculate(-8356, -1269288478), -1269296834)

    def test0295(self):
        self.assertEquals(self.calculate(-3612, 997992348), 997988736)

    def test0296(self):
        self.assertEquals(self.calculate(-30132, 43716748), 43686616)

    def test0297(self):
        self.assertEquals(self.calculate(16149, 1601418940), 1601435089)

    def test0298(self):
        self.assertEquals(self.calculate(-18758, -1290740538), -1290759296)

    def test0299(self):
        self.assertEquals(self.calculate(11750, 1789773761), 1789785511)

    def test0300(self):
        self.assertEquals(self.calculate(-11118, -1768479409), -1768490527)

    def test0301(self):
        self.assertEquals(self.calculate(20325, -1652502151), -1652481826)

    def test0302(self):
        self.assertEquals(self.calculate(22156, 350698203), 350720359)

    def test0303(self):
        self.assertEquals(self.calculate(-16225, -1173329591), -1173345816)

    def test0304(self):
        self.assertEquals(self.calculate(1660, -699134810), -699133150)

    def test0305(self):
        self.assertEquals(self.calculate(-30423, 1003683382), 1003652959)

    def test0306(self):
        self.assertEquals(self.calculate(-25917, 477267284), 477241367)

    def test0307(self):
        self.assertEquals(self.calculate(16808, 389885745), 389902553)

    def test0308(self):
        self.assertEquals(self.calculate(-5072, 1300139972), 1300134900)

    def test0309(self):
        self.assertEquals(self.calculate(-5950, -987702779), -987708729)

    def test0310(self):
        self.assertEquals(self.calculate(-5763, -1608162801), -1608168564)

    def test0311(self):
        self.assertEquals(self.calculate(-22582, 1848649693), 1848627111)

    def test0312(self):
        self.assertEquals(self.calculate(6141, -1873566520), -1873560379)

    def test0313(self):
        self.assertEquals(self.calculate(78, 732187173), 732187251)

    def test0314(self):
        self.assertEquals(self.calculate(16653, 928160650), 928177303)

    def test0315(self):
        self.assertEquals(self.calculate(-9979, -308956005), -308965984)

    def test0316(self):
        self.assertEquals(self.calculate(24779, -347794918), -347770139)

    def test0317(self):
        self.assertEquals(self.calculate(-8824, -194977488), -194986312)

    def test0318(self):
        self.assertEquals(self.calculate(26557, 537374221), 537400778)

    def test0319(self):
        self.assertEquals(self.calculate(14882, -2112883438), -2112868556)

    def test0320(self):
        self.assertEquals(self.calculate(12979, -986913151), -986900172)

    def test0321(self):
        self.assertEquals(self.calculate(13854, -1372204552), -1372190698)

    def test0322(self):
        self.assertEquals(self.calculate(21513, -995697261), -995675748)

    def test0323(self):
        self.assertEquals(self.calculate(14094, -794112161), -794098067)

    def test0324(self):
        self.assertEquals(self.calculate(2506, 1672926350), 1672928856)

    def test0325(self):
        self.assertEquals(self.calculate(-9263, 500424023), 500414760)

    def test0326(self):
        self.assertEquals(self.calculate(16160, 1791856539), 1791872699)

    def test0327(self):
        self.assertEquals(self.calculate(20719, 165935851), 165956570)

    def test0328(self):
        self.assertEquals(self.calculate(-6732, -203915400), -203922132)

    def test0329(self):
        self.assertEquals(self.calculate(6840, -158130943), -158124103)

    def test0330(self):
        self.assertEquals(self.calculate(14071, -549716944), -549702873)

    def test0331(self):
        self.assertEquals(self.calculate(25124, -1236160085), -1236134961)

    def test0332(self):
        self.assertEquals(self.calculate(2849, -1426480244), -1426477395)

    def test0333(self):
        self.assertEquals(self.calculate(8046, -278024963), -278016917)

    def test0334(self):
        self.assertEquals(self.calculate(-2131, 282115201), 282113070)

    def test0335(self):
        self.assertEquals(self.calculate(-3401, 426461850), 426458449)

    def test0336(self):
        self.assertEquals(self.calculate(-30252, 370867284), 370837032)

    def test0337(self):
        self.assertEquals(self.calculate(-16547, 728367835), 728351288)

    def test0338(self):
        self.assertEquals(self.calculate(27751, -347014596), -346986845)

    def test0339(self):
        self.assertEquals(self.calculate(-24890, -1650450329), -1650475219)

    def test0340(self):
        self.assertEquals(self.calculate(27619, -1656281330), -1656253711)

    def test0341(self):
        self.assertEquals(self.calculate(26620, 548021542), 548048162)

    def test0342(self):
        self.assertEquals(self.calculate(4295, -1850637340), -1850633045)

    def test0343(self):
        self.assertEquals(self.calculate(8892, -2045155879), -2045146987)

    def test0344(self):
        self.assertEquals(self.calculate(-25030, -1200927870), -1200952900)

    def test0345(self):
        self.assertEquals(self.calculate(-12623, 1715891826), 1715879203)

    def test0346(self):
        self.assertEquals(self.calculate(17020, 777085288), 777102308)

    def test0347(self):
        self.assertEquals(self.calculate(7880, -1921698721), -1921690841)

    def test0348(self):
        self.assertEquals(self.calculate(-23701, -287316211), -287339912)

    def test0349(self):
        self.assertEquals(self.calculate(15467, 104309917), 104325384)

    def test0350(self):
        self.assertEquals(self.calculate(-20792, 1618458398), 1618437606)

    def test0351(self):
        self.assertEquals(self.calculate(-17503, 1243809628), 1243792125)

    def test0352(self):
        self.assertEquals(self.calculate(28746, -1178244417), -1178215671)

    def test0353(self):
        self.assertEquals(self.calculate(12562, -913668144), -913655582)

    def test0354(self):
        self.assertEquals(self.calculate(-11999, 1690117539), 1690105540)

    def test0355(self):
        self.assertEquals(self.calculate(-20106, 1551687732), 1551667626)

    def test0356(self):
        self.assertEquals(self.calculate(-9001, -1874503392), -1874512393)

    def test0357(self):
        self.assertEquals(self.calculate(-10100, 1438721770), 1438711670)

    def test0358(self):
        self.assertEquals(self.calculate(21759, 1578342850), 1578364609)

    def test0359(self):
        self.assertEquals(self.calculate(1012, -2109700729), -2109699717)

    def test0360(self):
        self.assertEquals(self.calculate(-17071, 917089660), 917072589)

    def test0361(self):
        self.assertEquals(self.calculate(-24740, -938133313), -938158053)

    def test0362(self):
        self.assertEquals(self.calculate(1539, -1981504689), -1981503150)

    def test0363(self):
        self.assertEquals(self.calculate(-17239, -1960312126), -1960329365)

    def test0364(self):
        self.assertEquals(self.calculate(-2060, -733361441), -733363501)

    def test0365(self):
        self.assertEquals(self.calculate(-6145, 1874938532), 1874932387)

    def test0366(self):
        self.assertEquals(self.calculate(-16807, 1336876992), 1336860185)

    def test0367(self):
        self.assertEquals(self.calculate(23006, 2032546997), 2032570003)

    def test0368(self):
        self.assertEquals(self.calculate(6655, 646676119), 646682774)

    def test0369(self):
        self.assertEquals(self.calculate(22125, 816205457), 816227582)

    def test0370(self):
        self.assertEquals(self.calculate(-21965, -1760218333), -1760240298)

    def test0371(self):
        self.assertEquals(self.calculate(31275, 889704034), 889735309)

    def test0372(self):
        self.assertEquals(self.calculate(3410, -1981974002), -1981970592)

    def test0373(self):
        self.assertEquals(self.calculate(-24428, 792152166), 792127738)

    def test0374(self):
        self.assertEquals(self.calculate(-7828, -1627153455), -1627161283)

    def test0375(self):
        self.assertEquals(self.calculate(6565, -1931469234), -1931462669)

    def test0376(self):
        self.assertEquals(self.calculate(-8422, 2136651707), 2136643285)

    def test0377(self):
        self.assertEquals(self.calculate(-14136, 2143564957), 2143550821)

    def test0378(self):
        self.assertEquals(self.calculate(15845, 135201203), 135217048)

    def test0379(self):
        self.assertEquals(self.calculate(32223, -1444716144), -1444683921)

    def test0380(self):
        self.assertEquals(self.calculate(-14091, -1609501789), -1609515880)

    def test0381(self):
        self.assertEquals(self.calculate(10382, 864233501), 864243883)

    def test0382(self):
        self.assertEquals(self.calculate(-2698, 1218964102), 1218961404)

    def test0383(self):
        self.assertEquals(self.calculate(-13640, 242204885), 242191245)

    def test0384(self):
        self.assertEquals(self.calculate(-14360, -746896892), -746911252)

    def test0385(self):
        self.assertEquals(self.calculate(-13926, -268327054), -268340980)

    def test0386(self):
        self.assertEquals(self.calculate(-14200, 1905354121), 1905339921)

    def test0387(self):
        self.assertEquals(self.calculate(18552, 1126293345), 1126311897)

    def test0388(self):
        self.assertEquals(self.calculate(-5394, -2053069214), -2053074608)

    def test0389(self):
        self.assertEquals(self.calculate(-31586, 1405370062), 1405338476)

    def test0390(self):
        self.assertEquals(self.calculate(12724, 174851070), 174863794)

    def test0391(self):
        self.assertEquals(self.calculate(-4781, 262441863), 262437082)

    def test0392(self):
        self.assertEquals(self.calculate(12858, -1907480004), -1907467146)

    def test0393(self):
        self.assertEquals(self.calculate(2306, -1972874734), -1972872428)

    def test0394(self):
        self.assertEquals(self.calculate(-14610, -4362970), -4377580)

    def test0395(self):
        self.assertEquals(self.calculate(-18170, -346632818), -346650988)

    def test0396(self):
        self.assertEquals(self.calculate(-1147, 731714107), 731712960)

    def test0397(self):
        self.assertEquals(self.calculate(-4167, 1647610654), 1647606487)

    def test0398(self):
        self.assertEquals(self.calculate(26838, -961296801), -961269963)

    def test0399(self):
        self.assertEquals(self.calculate(12804, 1803138912), 1803151716)

    def test0400(self):
        self.assertEquals(self.calculate(-21683, 495433701), 495412018)

    def test0401(self):
        self.assertEquals(self.calculate(2531, -2129509885), -2129507354)

    def test0402(self):
        self.assertEquals(self.calculate(16976, -594643705), -594626729)

    def test0403(self):
        self.assertEquals(self.calculate(3278, -988902263), -988898985)

    def test0404(self):
        self.assertEquals(self.calculate(-23193, 1360360080), 1360336887)

    def test0405(self):
        self.assertEquals(self.calculate(-3239, -1077340555), -1077343794)

    def test0406(self):
        self.assertEquals(self.calculate(-19059, 1476503621), 1476484562)

    def test0407(self):
        self.assertEquals(self.calculate(5535, 235739731), 235745266)

    def test0408(self):
        self.assertEquals(self.calculate(11454, -1469544776), -1469533322)

    def test0409(self):
        self.assertEquals(self.calculate(24069, -650107116), -650083047)

    def test0410(self):
        self.assertEquals(self.calculate(28592, -1292671102), -1292642510)

    def test0411(self):
        self.assertEquals(self.calculate(8807, -694612603), -694603796)

    def test0412(self):
        self.assertEquals(self.calculate(27285, -1804980314), -1804953029)

    def test0413(self):
        self.assertEquals(self.calculate(-10947, 623352815), 623341868)

    def test0414(self):
        self.assertEquals(self.calculate(32029, -1057778391), -1057746362)

    def test0415(self):
        self.assertEquals(self.calculate(-6260, 1426565242), 1426558982)

    def test0416(self):
        self.assertEquals(self.calculate(-12127, -883815968), -883828095)

    def test0417(self):
        self.assertEquals(self.calculate(32442, 146658583), 146691025)

    def test0418(self):
        self.assertEquals(self.calculate(17210, -1163674670), -1163657460)

    def test0419(self):
        self.assertEquals(self.calculate(-17521, 2122945145), 2122927624)

    def test0420(self):
        self.assertEquals(self.calculate(9346, -1413695956), -1413686610)

    def test0421(self):
        self.assertEquals(self.calculate(30981, -984647440), -984616459)

    def test0422(self):
        self.assertEquals(self.calculate(25114, -1256615171), -1256590057)

    def test0423(self):
        self.assertEquals(self.calculate(30904, -22338700), -22307796)

    def test0424(self):
        self.assertEquals(self.calculate(-28252, 12412225), 12383973)

    def test0425(self):
        self.assertEquals(self.calculate(28645, 2054372575), 2054401220)

    def test0426(self):
        self.assertEquals(self.calculate(28732, 2141434646), 2141463378)

    def test0427(self):
        self.assertEquals(self.calculate(16371, 41611438), 41627809)

    def test0428(self):
        self.assertEquals(self.calculate(30766, -948165714), -948134948)

    def test0429(self):
        self.assertEquals(self.calculate(14688, 2072274609), 2072289297)

    def test0430(self):
        self.assertEquals(self.calculate(-1672, 147688626), 147686954)

    def test0431(self):
        self.assertEquals(self.calculate(-14706, 1422612754), 1422598048)

    def test0432(self):
        self.assertEquals(self.calculate(-27127, 406212053), 406184926)

    def test0433(self):
        self.assertEquals(self.calculate(-10733, 777176025), 777165292)

    def test0434(self):
        self.assertEquals(self.calculate(27656, 127951314), 127978970)

    def test0435(self):
        self.assertEquals(self.calculate(14410, -1489632709), -1489618299)

    def test0436(self):
        self.assertEquals(self.calculate(16519, -751562094), -751545575)

    def test0437(self):
        self.assertEquals(self.calculate(14397, -1213907487), -1213893090)

    def test0438(self):
        self.assertEquals(self.calculate(-1145, 1633746206), 1633745061)

    def test0439(self):
        self.assertEquals(self.calculate(-28311, -1662369884), -1662398195)

    def test0440(self):
        self.assertEquals(self.calculate(-32023, -1926275862), -1926307885)

    def test0441(self):
        self.assertEquals(self.calculate(1531, -285504573), -285503042)

    def test0442(self):
        self.assertEquals(self.calculate(22802, -515902559), -515879757)

    def test0443(self):
        self.assertEquals(self.calculate(14811, 809297745), 809312556)

    def test0444(self):
        self.assertEquals(self.calculate(22557, 632536222), 632558779)

    def test0445(self):
        self.assertEquals(self.calculate(29852, -1898736748), -1898706896)

    def test0446(self):
        self.assertEquals(self.calculate(29975, 436033697), 436063672)

    def test0447(self):
        self.assertEquals(self.calculate(15561, -795887869), -795872308)

    def test0448(self):
        self.assertEquals(self.calculate(8262, 346408402), 346416664)

    def test0449(self):
        self.assertEquals(self.calculate(5182, 498133199), 498138381)

    def test0450(self):
        self.assertEquals(self.calculate(11224, -1989897299), -1989886075)

    def test0451(self):
        self.assertEquals(self.calculate(-12687, -1135388830), -1135401517)

    def test0452(self):
        self.assertEquals(self.calculate(26274, -1949961863), -1949935589)

    def test0453(self):
        self.assertEquals(self.calculate(-1806, 874624405), 874622599)

    def test0454(self):
        self.assertEquals(self.calculate(16085, -1696918619), -1696902534)

    def test0455(self):
        self.assertEquals(self.calculate(-16776, -779251200), -779267976)

    def test0456(self):
        self.assertEquals(self.calculate(4957, 694367426), 694372383)

    def test0457(self):
        self.assertEquals(self.calculate(31716, 2093153820), 2093185536)

    def test0458(self):
        self.assertEquals(self.calculate(10233, -347443571), -347433338)

    def test0459(self):
        self.assertEquals(self.calculate(4099, -800804779), -800800680)

    def test0460(self):
        self.assertEquals(self.calculate(5354, 1325885892), 1325891246)

    def test0461(self):
        self.assertEquals(self.calculate(29345, -2130968467), -2130939122)

    def test0462(self):
        self.assertEquals(self.calculate(-21953, -625460806), -625482759)

    def test0463(self):
        self.assertEquals(self.calculate(-11896, -1998823758), -1998835654)

    def test0464(self):
        self.assertEquals(self.calculate(-28923, 1479791125), 1479762202)

    def test0465(self):
        self.assertEquals(self.calculate(-14866, 619028794), 619013928)

    def test0466(self):
        self.assertEquals(self.calculate(24745, -2068776210), -2068751465)

    def test0467(self):
        self.assertEquals(self.calculate(-32139, 1210412272), 1210380133)

    def test0468(self):
        self.assertEquals(self.calculate(-9795, 1782894007), 1782884212)

    def test0469(self):
        self.assertEquals(self.calculate(26212, -1182358117), -1182331905)

    def test0470(self):
        self.assertEquals(self.calculate(-3630, 1462056859), 1462053229)

    def test0471(self):
        self.assertEquals(self.calculate(29144, 1828731959), 1828761103)

    def test0472(self):
        self.assertEquals(self.calculate(15769, 725678389), 725694158)

    def test0473(self):
        self.assertEquals(self.calculate(15390, -1815533953), -1815518563)

    def test0474(self):
        self.assertEquals(self.calculate(4950, -1261723910), -1261718960)

    def test0475(self):
        self.assertEquals(self.calculate(-12849, -2105604360), -2105617209)

    def test0476(self):
        self.assertEquals(self.calculate(18000, 1808045725), 1808063725)

    def test0477(self):
        self.assertEquals(self.calculate(-30229, -1205184839), -1205215068)

    def test0478(self):
        self.assertEquals(self.calculate(635, 11697567), 11698202)

    def test0479(self):
        self.assertEquals(self.calculate(-31364, 1646472010), 1646440646)

    def test0480(self):
        self.assertEquals(self.calculate(21091, 2043589883), 2043610974)

    def test0481(self):
        self.assertEquals(self.calculate(22411, 897045088), 897067499)

    def test0482(self):
        self.assertEquals(self.calculate(-26416, 1559130232), 1559103816)

    def test0483(self):
        self.assertEquals(self.calculate(24665, 1891299860), 1891324525)

    def test0484(self):
        self.assertEquals(self.calculate(10727, -69047236), -69036509)

    def test0485(self):
        self.assertEquals(self.calculate(21562, 1285592445), 1285614007)

    def test0486(self):
        self.assertEquals(self.calculate(-25811, 1044327666), 1044301855)

    def test0487(self):
        self.assertEquals(self.calculate(-4760, -34604456), -34609216)

    def test0488(self):
        self.assertEquals(self.calculate(7712, 512073180), 512080892)

    def test0489(self):
        self.assertEquals(self.calculate(28749, 198080153), 198108902)

    def test0490(self):
        self.assertEquals(self.calculate(-32208, 546080503), 546048295)

    def test0491(self):
        self.assertEquals(self.calculate(14204, 2132279235), 2132293439)

    def test0492(self):
        self.assertEquals(self.calculate(5891, -78896781), -78890890)

    def test0493(self):
        self.assertEquals(self.calculate(-2247, -1445905706), -1445907953)

    def test0494(self):
        self.assertEquals(self.calculate(-3405, 1398059862), 1398056457)

    def test0495(self):
        self.assertEquals(self.calculate(-1111, -1428176446), -1428177557)

    def test0496(self):
        self.assertEquals(self.calculate(-15996, -1304489560), -1304505556)

    def test0497(self):
        self.assertEquals(self.calculate(-1560, 1805690811), 1805689251)

    def test0498(self):
        self.assertEquals(self.calculate(-4259, 88418853), 88414594)

    def test0499(self):
        self.assertEquals(self.calculate(31953, -1362150520), -1362118567)

    def test0500(self):
        self.assertEquals(self.calculate(-9028, -1828496309), -1828505337)

    def test0501(self):
        self.assertEquals(self.calculate(-1602, -816557991), -816559593)

    def test0502(self):
        self.assertEquals(self.calculate(-2591, 1118803491), 1118800900)

    def test0503(self):
        self.assertEquals(self.calculate(13280, -157128885), -157115605)

    def test0504(self):
        self.assertEquals(self.calculate(5477, -1826893672), -1826888195)

    def test0505(self):
        self.assertEquals(self.calculate(-23961, -1591747906), -1591771867)

    def test0506(self):
        self.assertEquals(self.calculate(20371, -246199758), -246179387)

    def test0507(self):
        self.assertEquals(self.calculate(29236, -177921226), -177891990)

    def test0508(self):
        self.assertEquals(self.calculate(-1714, 1365710818), 1365709104)

    def test0509(self):
        self.assertEquals(self.calculate(-29822, -1972837902), -1972867724)

    def test0510(self):
        self.assertEquals(self.calculate(32521, 357723045), 357755566)

    def test0511(self):
        self.assertEquals(self.calculate(6145, -78851043), -78844898)

    def test0512(self):
        self.assertEquals(self.calculate(10879, 421547346), 421558225)

    def test0513(self):
        self.assertEquals(self.calculate(11534, -147677286), -147665752)

    def test0514(self):
        self.assertEquals(self.calculate(-122, 1758400262), 1758400140)

    def test0515(self):
        self.assertEquals(self.calculate(-15340, 883343049), 883327709)

    def test0516(self):
        self.assertEquals(self.calculate(-25735, 1939584738), 1939559003)

    def test0517(self):
        self.assertEquals(self.calculate(10061, -948459525), -948449464)

    def test0518(self):
        self.assertEquals(self.calculate(32402, 1875935946), 1875968348)

    def test0519(self):
        self.assertEquals(self.calculate(32660, 1895574558), 1895607218)

    def test0520(self):
        self.assertEquals(self.calculate(-8033, -1515174074), -1515182107)

    def test0521(self):
        self.assertEquals(self.calculate(-8642, 870025583), 870016941)

    def test0522(self):
        self.assertEquals(self.calculate(-5519, 1698800208), 1698794689)

    def test0523(self):
        self.assertEquals(self.calculate(-19854, 2052326970), 2052307116)

    def test0524(self):
        self.assertEquals(self.calculate(-4, 1572916811), 1572916807)

    def test0525(self):
        self.assertEquals(self.calculate(12907, -256602793), -256589886)

    def test0526(self):
        self.assertEquals(self.calculate(-28439, 155952934), 155924495)

    def test0527(self):
        self.assertEquals(self.calculate(27408, 693307733), 693335141)

    def test0528(self):
        self.assertEquals(self.calculate(10625, -1781266970), -1781256345)

    def test0529(self):
        self.assertEquals(self.calculate(-30860, -1755560155), -1755591015)

    def test0530(self):
        self.assertEquals(self.calculate(22387, 758050009), 758072396)

    def test0531(self):
        self.assertEquals(self.calculate(2948, 1720856159), 1720859107)

    def test0532(self):
        self.assertEquals(self.calculate(13693, 624095375), 624109068)

    def test0533(self):
        self.assertEquals(self.calculate(-13336, 673641707), 673628371)

    def test0534(self):
        self.assertEquals(self.calculate(-13739, -2092609886), -2092623625)

    def test0535(self):
        self.assertEquals(self.calculate(-14233, -630844157), -630858390)

    def test0536(self):
        self.assertEquals(self.calculate(-29613, -1013958958), -1013988571)

    def test0537(self):
        self.assertEquals(self.calculate(-17591, -1173589647), -1173607238)

    def test0538(self):
        self.assertEquals(self.calculate(7477, 1551085603), 1551093080)

    def test0539(self):
        self.assertEquals(self.calculate(-24157, -1820768803), -1820792960)

    def test0540(self):
        self.assertEquals(self.calculate(17761, -1891853405), -1891835644)

    def test0541(self):
        self.assertEquals(self.calculate(2190, -1408585140), -1408582950)

    def test0542(self):
        self.assertEquals(self.calculate(8910, 1899978348), 1899987258)

    def test0543(self):
        self.assertEquals(self.calculate(9041, 1408392701), 1408401742)

    def test0544(self):
        self.assertEquals(self.calculate(-32094, 722456821), 722424727)

    def test0545(self):
        self.assertEquals(self.calculate(26771, 1801547980), 1801574751)

    def test0546(self):
        self.assertEquals(self.calculate(19980, 1007204795), 1007224775)

    def test0547(self):
        self.assertEquals(self.calculate(18154, 1807866786), 1807884940)

    def test0548(self):
        self.assertEquals(self.calculate(3788, -772899584), -772895796)

    def test0549(self):
        self.assertEquals(self.calculate(-31486, -643646923), -643678409)

    def test0550(self):
        self.assertEquals(self.calculate(-8345, -1503978506), -1503986851)

    def test0551(self):
        self.assertEquals(self.calculate(-13224, -1452963248), -1452976472)

    def test0552(self):
        self.assertEquals(self.calculate(-15516, -292636960), -292652476)

    def test0553(self):
        self.assertEquals(self.calculate(19879, 1339991022), 1340010901)

    def test0554(self):
        self.assertEquals(self.calculate(17624, -1049057688), -1049040064)

    def test0555(self):
        self.assertEquals(self.calculate(16759, -267012918), -266996159)

    def test0556(self):
        self.assertEquals(self.calculate(-10994, -1832516599), -1832527593)

    def test0557(self):
        self.assertEquals(self.calculate(-17653, -1303740940), -1303758593)

    def test0558(self):
        self.assertEquals(self.calculate(24184, -2070907854), -2070883670)

    def test0559(self):
        self.assertEquals(self.calculate(-10891, 2116146171), 2116135280)

    def test0560(self):
        self.assertEquals(self.calculate(22006, 453431571), 453453577)

    def test0561(self):
        self.assertEquals(self.calculate(3454, 2020180578), 2020184032)

    def test0562(self):
        self.assertEquals(self.calculate(-20434, 1184541906), 1184521472)

    def test0563(self):
        self.assertEquals(self.calculate(15995, 691468360), 691484355)

    def test0564(self):
        self.assertEquals(self.calculate(-20902, -119812037), -119832939)

    def test0565(self):
        self.assertEquals(self.calculate(-411, -773578353), -773578764)

    def test0566(self):
        self.assertEquals(self.calculate(-19977, -340181718), -340201695)

    def test0567(self):
        self.assertEquals(self.calculate(-4872, 795255469), 795250597)

    def test0568(self):
        self.assertEquals(self.calculate(24416, 863551817), 863576233)

    def test0569(self):
        self.assertEquals(self.calculate(12624, -2139724647), -2139712023)

    def test0570(self):
        self.assertEquals(self.calculate(29117, -87493554), -87464437)

    def test0571(self):
        self.assertEquals(self.calculate(29251, -206135154), -206105903)

    def test0572(self):
        self.assertEquals(self.calculate(-10294, -898757629), -898767923)

    def test0573(self):
        self.assertEquals(self.calculate(-2312, -832653883), -832656195)

    def test0574(self):
        self.assertEquals(self.calculate(-4370, -840768155), -840772525)

    def test0575(self):
        self.assertEquals(self.calculate(-28556, -1258655610), -1258684166)

    def test0576(self):
        self.assertEquals(self.calculate(-20253, -197897087), -197917340)

    def test0577(self):
        self.assertEquals(self.calculate(16788, -893406311), -893389523)

    def test0578(self):
        self.assertEquals(self.calculate(-11449, -109186324), -109197773)

    def test0579(self):
        self.assertEquals(self.calculate(-13082, 1804717646), 1804704564)

    def test0580(self):
        self.assertEquals(self.calculate(-31901, -1126690127), -1126722028)

    def test0581(self):
        self.assertEquals(self.calculate(-4195, 1478804400), 1478800205)

    def test0582(self):
        self.assertEquals(self.calculate(22012, -1025746538), -1025724526)

    def test0583(self):
        self.assertEquals(self.calculate(7171, 283454344), 283461515)

    def test0584(self):
        self.assertEquals(self.calculate(20033, 549813086), 549833119)

    def test0585(self):
        self.assertEquals(self.calculate(325, 2119657784), 2119658109)

    def test0586(self):
        self.assertEquals(self.calculate(27044, -843880191), -843853147)

    def test0587(self):
        self.assertEquals(self.calculate(-9763, -943064137), -943073900)

    def test0588(self):
        self.assertEquals(self.calculate(-13541, 1991934811), 1991921270)

    def test0589(self):
        self.assertEquals(self.calculate(1058, -474811505), -474810447)

    def test0590(self):
        self.assertEquals(self.calculate(-6954, 283524589), 283517635)

    def test0591(self):
        self.assertEquals(self.calculate(7481, 594592000), 594599481)

    def test0592(self):
        self.assertEquals(self.calculate(-1759, -1288406835), -1288408594)

    def test0593(self):
        self.assertEquals(self.calculate(1448, -1550365355), -1550363907)

    def test0594(self):
        self.assertEquals(self.calculate(14124, 1081731789), 1081745913)

    def test0595(self):
        self.assertEquals(self.calculate(24308, 914771834), 914796142)

    def test0596(self):
        self.assertEquals(self.calculate(-20361, -854276246), -854296607)

    def test0597(self):
        self.assertEquals(self.calculate(-26505, 997068835), 997042330)

    def test0598(self):
        self.assertEquals(self.calculate(18714, -826196298), -826177584)

    def test0599(self):
        self.assertEquals(self.calculate(-4618, -1934011190), -1934015808)

    def test0600(self):
        self.assertEquals(self.calculate(22523, 84170151), 84192674)

    def test0601(self):
        self.assertEquals(self.calculate(28644, -457080710), -457052066)

    def test0602(self):
        self.assertEquals(self.calculate(-15139, -1093798158), -1093813297)

    def test0603(self):
        self.assertEquals(self.calculate(-29793, -836786930), -836816723)

    def test0604(self):
        self.assertEquals(self.calculate(11122, 1408299637), 1408310759)

    def test0605(self):
        self.assertEquals(self.calculate(-891, 1054251355), 1054250464)

    def test0606(self):
        self.assertEquals(self.calculate(3804, 794522125), 794525929)

    def test0607(self):
        self.assertEquals(self.calculate(-6538, 1453005155), 1452998617)

    def test0608(self):
        self.assertEquals(self.calculate(-32294, 1972010317), 1971978023)

    def test0609(self):
        self.assertEquals(self.calculate(-27795, -1070316229), -1070344024)

    def test0610(self):
        self.assertEquals(self.calculate(21480, 1796608632), 1796630112)

    def test0611(self):
        self.assertEquals(self.calculate(-31511, 1540574286), 1540542775)

    def test0612(self):
        self.assertEquals(self.calculate(25866, -1122069304), -1122043438)

    def test0613(self):
        self.assertEquals(self.calculate(5723, -510689141), -510683418)

    def test0614(self):
        self.assertEquals(self.calculate(14215, 1647183483), 1647197698)

    def test0615(self):
        self.assertEquals(self.calculate(-25652, -1470212558), -1470238210)

    def test0616(self):
        self.assertEquals(self.calculate(12810, 1204284013), 1204296823)

    def test0617(self):
        self.assertEquals(self.calculate(24076, 1803050403), 1803074479)

    def test0618(self):
        self.assertEquals(self.calculate(5459, 1290882395), 1290887854)

    def test0619(self):
        self.assertEquals(self.calculate(-12638, 522570789), 522558151)

    def test0620(self):
        self.assertEquals(self.calculate(-29909, 532067670), 532037761)

    def test0621(self):
        self.assertEquals(self.calculate(7797, 269084406), 269092203)

    def test0622(self):
        self.assertEquals(self.calculate(-17395, -835653129), -835670524)

    def test0623(self):
        self.assertEquals(self.calculate(21281, 838397862), 838419143)

    def test0624(self):
        self.assertEquals(self.calculate(-32099, 930098415), 930066316)

    def test0625(self):
        self.assertEquals(self.calculate(29667, 1716013449), 1716043116)

    def test0626(self):
        self.assertEquals(self.calculate(11247, 1079806483), 1079817730)

    def test0627(self):
        self.assertEquals(self.calculate(-13859, 1266445373), 1266431514)

    def test0628(self):
        self.assertEquals(self.calculate(11674, 15978916), 15990590)

    def test0629(self):
        self.assertEquals(self.calculate(27181, 233606417), 233633598)

    def test0630(self):
        self.assertEquals(self.calculate(19005, 2000282251), 2000301256)

    def test0631(self):
        self.assertEquals(self.calculate(28921, 299373611), 299402532)

    def test0632(self):
        self.assertEquals(self.calculate(5102, -295633986), -295628884)

    def test0633(self):
        self.assertEquals(self.calculate(5954, 863481614), 863487568)

    def test0634(self):
        self.assertEquals(self.calculate(9903, -1829414193), -1829404290)

    def test0635(self):
        self.assertEquals(self.calculate(27821, -548268048), -548240227)

    def test0636(self):
        self.assertEquals(self.calculate(25008, -1501986821), -1501961813)

    def test0637(self):
        self.assertEquals(self.calculate(19953, -1079934811), -1079914858)

    def test0638(self):
        self.assertEquals(self.calculate(-15925, 1460241291), 1460225366)

    def test0639(self):
        self.assertEquals(self.calculate(-26796, -812780531), -812807327)

    def test0640(self):
        self.assertEquals(self.calculate(19773, 272879399), 272899172)

    def test0641(self):
        self.assertEquals(self.calculate(20386, -5076069), -5055683)

    def test0642(self):
        self.assertEquals(self.calculate(-4626, 1904369363), 1904364737)

    def test0643(self):
        self.assertEquals(self.calculate(31740, 1059963438), 1059995178)

    def test0644(self):
        self.assertEquals(self.calculate(-14557, 1911911122), 1911896565)

    def test0645(self):
        self.assertEquals(self.calculate(-12743, 1299278557), 1299265814)

    def test0646(self):
        self.assertEquals(self.calculate(14350, 1813583569), 1813597919)

    def test0647(self):
        self.assertEquals(self.calculate(-2692, -1565660356), -1565663048)

    def test0648(self):
        self.assertEquals(self.calculate(3569, -1836582413), -1836578844)

    def test0649(self):
        self.assertEquals(self.calculate(15608, -204406796), -204391188)

    def test0650(self):
        self.assertEquals(self.calculate(21578, 104737373), 104758951)

    def test0651(self):
        self.assertEquals(self.calculate(-32007, 633202012), 633170005)

    def test0652(self):
        self.assertEquals(self.calculate(14145, 115252470), 115266615)

    def test0653(self):
        self.assertEquals(self.calculate(-9583, -925372195), -925381778)

    def test0654(self):
        self.assertEquals(self.calculate(-13796, -2115999584), -2116013380)

    def test0655(self):
        self.assertEquals(self.calculate(12304, 2058657697), 2058670001)

    def test0656(self):
        self.assertEquals(self.calculate(11191, -1120941085), -1120929894)

    def test0657(self):
        self.assertEquals(self.calculate(-32338, 575424308), 575391970)

    def test0658(self):
        self.assertEquals(self.calculate(-14843, 1016121521), 1016106678)

    def test0659(self):
        self.assertEquals(self.calculate(29684, 132868604), 132898288)

    def test0660(self):
        self.assertEquals(self.calculate(24648, -1496251069), -1496226421)

    def test0661(self):
        self.assertEquals(self.calculate(12853, 1536663755), 1536676608)

    def test0662(self):
        self.assertEquals(self.calculate(-23785, 1916392476), 1916368691)

    def test0663(self):
        self.assertEquals(self.calculate(18766, -1568428240), -1568409474)

    def test0664(self):
        self.assertEquals(self.calculate(-7285, 1229923567), 1229916282)

    def test0665(self):
        self.assertEquals(self.calculate(-10034, -1211120675), -1211130709)

    def test0666(self):
        self.assertEquals(self.calculate(-30568, -637903492), -637934060)

    def test0667(self):
        self.assertEquals(self.calculate(13093, 1577973782), 1577986875)

    def test0668(self):
        self.assertEquals(self.calculate(15401, -85543919), -85528518)

    def test0669(self):
        self.assertEquals(self.calculate(17873, 1644699882), 1644717755)

    def test0670(self):
        self.assertEquals(self.calculate(13122, -1912422155), -1912409033)

    def test0671(self):
        self.assertEquals(self.calculate(-16464, -276043400), -276059864)

    def test0672(self):
        self.assertEquals(self.calculate(17572, 1873399683), 1873417255)

    def test0673(self):
        self.assertEquals(self.calculate(-17244, -119309530), -119326774)

    def test0674(self):
        self.assertEquals(self.calculate(25884, -355862786), -355836902)

    def test0675(self):
        self.assertEquals(self.calculate(17519, 875718553), 875736072)

    def test0676(self):
        self.assertEquals(self.calculate(-2348, -1338693494), -1338695842)

    def test0677(self):
        self.assertEquals(self.calculate(-31395, 1383286727), 1383255332)

    def test0678(self):
        self.assertEquals(self.calculate(-16317, -1540023390), -1540039707)

    def test0679(self):
        self.assertEquals(self.calculate(-640, -68623754), -68624394)

    def test0680(self):
        self.assertEquals(self.calculate(32237, -1748696232), -1748663995)

    def test0681(self):
        self.assertEquals(self.calculate(-17516, 2147248740), 2147231224)

    def test0682(self):
        self.assertEquals(self.calculate(25298, 556779566), 556804864)

    def test0683(self):
        self.assertEquals(self.calculate(-10334, -1280061400), -1280071734)

    def test0684(self):
        self.assertEquals(self.calculate(9850, 334569903), 334579753)

    def test0685(self):
        self.assertEquals(self.calculate(26446, 372917394), 372943840)

    def test0686(self):
        self.assertEquals(self.calculate(26127, -555437486), -555411359)

    def test0687(self):
        self.assertEquals(self.calculate(-24680, -1173992171), -1174016851)

    def test0688(self):
        self.assertEquals(self.calculate(4717, 1531462976), 1531467693)

    def test0689(self):
        self.assertEquals(self.calculate(-7441, -1431765763), -1431773204)

    def test0690(self):
        self.assertEquals(self.calculate(-28759, 46648753), 46619994)

    def test0691(self):
        self.assertEquals(self.calculate(7822, 1718368171), 1718375993)

    def test0692(self):
        self.assertEquals(self.calculate(-17568, -2067554969), -2067572537)

    def test0693(self):
        self.assertEquals(self.calculate(-9425, -1567405536), -1567414961)

    def test0694(self):
        self.assertEquals(self.calculate(-7313, -200514812), -200522125)

    def test0695(self):
        self.assertEquals(self.calculate(-2403, 250486330), 250483927)

    def test0696(self):
        self.assertEquals(self.calculate(-30174, 2070285191), 2070255017)

    def test0697(self):
        self.assertEquals(self.calculate(5781, -1516912801), -1516907020)

    def test0698(self):
        self.assertEquals(self.calculate(-18892, 957591804), 957572912)

    def test0699(self):
        self.assertEquals(self.calculate(26470, 1074195380), 1074221850)

    def test0700(self):
        self.assertEquals(self.calculate(25284, 1908510180), 1908535464)

    def test0701(self):
        self.assertEquals(self.calculate(5515, 1845933100), 1845938615)

    def test0702(self):
        self.assertEquals(self.calculate(11659, 791008489), 791020148)

    def test0703(self):
        self.assertEquals(self.calculate(17789, 1158430047), 1158447836)

    def test0704(self):
        self.assertEquals(self.calculate(15453, 1954996699), 1955012152)

    def test0705(self):
        self.assertEquals(self.calculate(-16597, -865993731), -866010328)

    def test0706(self):
        self.assertEquals(self.calculate(5636, 2102359933), 2102365569)

    def test0707(self):
        self.assertEquals(self.calculate(11698, 1374870012), 1374881710)

    def test0708(self):
        self.assertEquals(self.calculate(-30021, 1105098499), 1105068478)

    def test0709(self):
        self.assertEquals(self.calculate(-1057, 353124056), 353122999)

    def test0710(self):
        self.assertEquals(self.calculate(-6353, 1533292288), 1533285935)

    def test0711(self):
        self.assertEquals(self.calculate(-17069, -889069690), -889086759)

    def test0712(self):
        self.assertEquals(self.calculate(15303, -1180780448), -1180765145)

    def test0713(self):
        self.assertEquals(self.calculate(28215, -79635233), -79607018)

    def test0714(self):
        self.assertEquals(self.calculate(25358, 1550271920), 1550297278)

    def test0715(self):
        self.assertEquals(self.calculate(-22807, -911156138), -911178945)

    def test0716(self):
        self.assertEquals(self.calculate(-26105, 488689877), 488663772)

    def test0717(self):
        self.assertEquals(self.calculate(9427, -1730124942), -1730115515)

    def test0718(self):
        self.assertEquals(self.calculate(28695, 1749896802), 1749925497)

    def test0719(self):
        self.assertEquals(self.calculate(15894, 626601495), 626617389)

    def test0720(self):
        self.assertEquals(self.calculate(-28487, 1233696414), 1233667927)

    def test0721(self):
        self.assertEquals(self.calculate(-788, -1686856737), -1686857525)

    def test0722(self):
        self.assertEquals(self.calculate(-29587, -1852632569), -1852662156)

    def test0723(self):
        self.assertEquals(self.calculate(-1822, 411414285), 411412463)

    def test0724(self):
        self.assertEquals(self.calculate(-27603, -539915094), -539942697)

    def test0725(self):
        self.assertEquals(self.calculate(4510, 69137846), 69142356)

    def test0726(self):
        self.assertEquals(self.calculate(18864, 505223382), 505242246)

    def test0727(self):
        self.assertEquals(self.calculate(20337, -805245711), -805225374)

    def test0728(self):
        self.assertEquals(self.calculate(-29896, 419212181), 419182285)

    def test0729(self):
        self.assertEquals(self.calculate(-17324, 1916979866), 1916962542)

    def test0730(self):
        self.assertEquals(self.calculate(-18204, -1526177788), -1526195992)

    def test0731(self):
        self.assertEquals(self.calculate(14072, -1337815789), -1337801717)

    def test0732(self):
        self.assertEquals(self.calculate(30679, -30068981), -30038302)

    def test0733(self):
        self.assertEquals(self.calculate(31232, -1909437855), -1909406623)

    def test0734(self):
        self.assertEquals(self.calculate(23752, 1010879379), 1010903131)

    def test0735(self):
        self.assertEquals(self.calculate(30492, -588460283), -588429791)

    def test0736(self):
        self.assertEquals(self.calculate(29512, 1016042321), 1016071833)

    def test0737(self):
        self.assertEquals(self.calculate(15248, -672403183), -672387935)

    def test0738(self):
        self.assertEquals(self.calculate(-25834, 1735742109), 1735716275)

    def test0739(self):
        self.assertEquals(self.calculate(-1894, -540372698), -540374592)

    def test0740(self):
        self.assertEquals(self.calculate(31593, -1117249088), -1117217495)

    def test0741(self):
        self.assertEquals(self.calculate(16853, -183290861), -183274008)

    def test0742(self):
        self.assertEquals(self.calculate(18354, -1032730816), -1032712462)

    def test0743(self):
        self.assertEquals(self.calculate(25623, 13037634), 13063257)

    def test0744(self):
        self.assertEquals(self.calculate(-11913, 263167899), 263155986)

    def test0745(self):
        self.assertEquals(self.calculate(-458, 1477098995), 1477098537)

    def test0746(self):
        self.assertEquals(self.calculate(16729, -1247857961), -1247841232)

    def test0747(self):
        self.assertEquals(self.calculate(-23324, 2028706956), 2028683632)

    def test0748(self):
        self.assertEquals(self.calculate(24849, -1344300026), -1344275177)

    def test0749(self):
        self.assertEquals(self.calculate(8852, -651154414), -651145562)

    def test0750(self):
        self.assertEquals(self.calculate(14241, 796031604), 796045845)

    def test0751(self):
        self.assertEquals(self.calculate(-2445, 1940329868), 1940327423)

    def test0752(self):
        self.assertEquals(self.calculate(-11771, -871905096), -871916867)

    def test0753(self):
        self.assertEquals(self.calculate(159, 65772016), 65772175)

    def test0754(self):
        self.assertEquals(self.calculate(-26547, -1365956636), -1365983183)

    def test0755(self):
        self.assertEquals(self.calculate(-2609, 1231589348), 1231586739)

    def test0756(self):
        self.assertEquals(self.calculate(-17204, 1057471356), 1057454152)

    def test0757(self):
        self.assertEquals(self.calculate(27713, -580633578), -580605865)

    def test0758(self):
        self.assertEquals(self.calculate(7009, 1712369150), 1712376159)

    def test0759(self):
        self.assertEquals(self.calculate(6030, -1515501692), -1515495662)

    def test0760(self):
        self.assertEquals(self.calculate(-31680, -1822739765), -1822771445)

    def test0761(self):
        self.assertEquals(self.calculate(-16426, -218410731), -218427157)

    def test0762(self):
        self.assertEquals(self.calculate(-27355, -661310787), -661338142)

    def test0763(self):
        self.assertEquals(self.calculate(10486, -226729623), -226719137)

    def test0764(self):
        self.assertEquals(self.calculate(12504, 1483950580), 1483963084)

    def test0765(self):
        self.assertEquals(self.calculate(-20445, 366733382), 366712937)

    def test0766(self):
        self.assertEquals(self.calculate(28977, 235050558), 235079535)

    def test0767(self):
        self.assertEquals(self.calculate(-1005, 1116713952), 1116712947)

    def test0768(self):
        self.assertEquals(self.calculate(-10948, -517577209), -517588157)

    def test0769(self):
        self.assertEquals(self.calculate(30919, 1288182394), 1288213313)

    def test0770(self):
        self.assertEquals(self.calculate(19229, 441999219), 442018448)

    def test0771(self):
        self.assertEquals(self.calculate(-28315, -213688186), -213716501)

    def test0772(self):
        self.assertEquals(self.calculate(-11222, 84403446), 84392224)

    def test0773(self):
        self.assertEquals(self.calculate(-1704, 448829718), 448828014)

    def test0774(self):
        self.assertEquals(self.calculate(-18725, 22685203), 22666478)

    def test0775(self):
        self.assertEquals(self.calculate(-27264, -747347364), -747374628)

    def test0776(self):
        self.assertEquals(self.calculate(-14195, 882502258), 882488063)

    def test0777(self):
        self.assertEquals(self.calculate(8732, -1916172293), -1916163561)

    def test0778(self):
        self.assertEquals(self.calculate(18437, 1003131855), 1003150292)

    def test0779(self):
        self.assertEquals(self.calculate(-27872, -1665173988), -1665201860)

    def test0780(self):
        self.assertEquals(self.calculate(20510, 605545504), 605566014)

    def test0781(self):
        self.assertEquals(self.calculate(-27666, -406501212), -406528878)

    def test0782(self):
        self.assertEquals(self.calculate(2688, 1796316951), 1796319639)

    def test0783(self):
        self.assertEquals(self.calculate(27910, 1091675352), 1091703262)

    def test0784(self):
        self.assertEquals(self.calculate(1381, 280566701), 280568082)

    def test0785(self):
        self.assertEquals(self.calculate(8570, 1590777985), 1590786555)

    def test0786(self):
        self.assertEquals(self.calculate(2384, -799570357), -799567973)

    def test0787(self):
        self.assertEquals(self.calculate(-10351, 2010156557), 2010146206)

    def test0788(self):
        self.assertEquals(self.calculate(-26315, -1700407774), -1700434089)

    def test0789(self):
        self.assertEquals(self.calculate(-22477, -977885816), -977908293)

    def test0790(self):
        self.assertEquals(self.calculate(-6757, 321920531), 321913774)

    def test0791(self):
        self.assertEquals(self.calculate(3416, 1782307270), 1782310686)

    def test0792(self):
        self.assertEquals(self.calculate(16280, 1002786061), 1002802341)

    def test0793(self):
        self.assertEquals(self.calculate(623, -12457415), -12456792)

    def test0794(self):
        self.assertEquals(self.calculate(-29673, -1170067919), -1170097592)

    def test0795(self):
        self.assertEquals(self.calculate(23531, -192348358), -192324827)

    def test0796(self):
        self.assertEquals(self.calculate(20766, -242222690), -242201924)

    def test0797(self):
        self.assertEquals(self.calculate(-16865, 1672540764), 1672523899)

    def test0798(self):
        self.assertEquals(self.calculate(-28967, 503791695), 503762728)

    def test0799(self):
        self.assertEquals(self.calculate(-12646, -1563123629), -1563136275)

    def test0800(self):
        self.assertEquals(self.calculate(15748, -256151854), -256136106)

    def test0801(self):
        self.assertEquals(self.calculate(7681, 433567851), 433575532)

    def test0802(self):
        self.assertEquals(self.calculate(15932, 326880813), 326896745)

    def test0803(self):
        self.assertEquals(self.calculate(-7359, -345610416), -345617775)

    def test0804(self):
        self.assertEquals(self.calculate(-11558, 42130172), 42118614)

    def test0805(self):
        self.assertEquals(self.calculate(-16205, -1959221321), -1959237526)

    def test0806(self):
        self.assertEquals(self.calculate(-30531, 1663371918), 1663341387)

    def test0807(self):
        self.assertEquals(self.calculate(-4682, -1395437551), -1395442233)

    def test0808(self):
        self.assertEquals(self.calculate(12040, 977186105), 977198145)

    def test0809(self):
        self.assertEquals(self.calculate(23476, -899685414), -899661938)

    def test0810(self):
        self.assertEquals(self.calculate(-15852, -1601263040), -1601278892)

    def test0811(self):
        self.assertEquals(self.calculate(10263, 353476529), 353486792)

    def test0812(self):
        self.assertEquals(self.calculate(21764, -686116977), -686095213)

    def test0813(self):
        self.assertEquals(self.calculate(7894, -878119291), -878111397)

    def test0814(self):
        self.assertEquals(self.calculate(-22283, -1947482171), -1947504454)

    def test0815(self):
        self.assertEquals(self.calculate(12583, -1849939528), -1849926945)

    def test0816(self):
        self.assertEquals(self.calculate(1685, 1769202177), 1769203862)

    def test0817(self):
        self.assertEquals(self.calculate(-3440, 521209546), 521206106)

    def test0818(self):
        self.assertEquals(self.calculate(-31141, 1464501761), 1464470620)

    def test0819(self):
        self.assertEquals(self.calculate(-31131, -318301005), -318332136)

    def test0820(self):
        self.assertEquals(self.calculate(-10033, -820709145), -820719178)

    def test0821(self):
        self.assertEquals(self.calculate(17743, 1362874603), 1362892346)

    def test0822(self):
        self.assertEquals(self.calculate(-732, -1094611249), -1094611981)

    def test0823(self):
        self.assertEquals(self.calculate(15051, -337094282), -337079231)

    def test0824(self):
        self.assertEquals(self.calculate(5947, 1825203099), 1825209046)

    def test0825(self):
        self.assertEquals(self.calculate(16304, 130745354), 130761658)

    def test0826(self):
        self.assertEquals(self.calculate(5425, -441853830), -441848405)

    def test0827(self):
        self.assertEquals(self.calculate(21983, -244468573), -244446590)

    def test0828(self):
        self.assertEquals(self.calculate(18029, -1706930733), -1706912704)

    def test0829(self):
        self.assertEquals(self.calculate(17027, 365000830), 365017857)

    def test0830(self):
        self.assertEquals(self.calculate(14415, 638134724), 638149139)

    def test0831(self):
        self.assertEquals(self.calculate(17701, 1840379256), 1840396957)

    def test0832(self):
        self.assertEquals(self.calculate(10615, -908940782), -908930167)

    def test0833(self):
        self.assertEquals(self.calculate(-9325, 985537345), 985528020)

    def test0834(self):
        self.assertEquals(self.calculate(-15777, -1369685662), -1369701439)

    def test0835(self):
        self.assertEquals(self.calculate(14793, 1295531378), 1295546171)

    def test0836(self):
        self.assertEquals(self.calculate(-16595, 753944054), 753927459)

    def test0837(self):
        self.assertEquals(self.calculate(-22056, 1164012882), 1163990826)

    def test0838(self):
        self.assertEquals(self.calculate(-30063, 689133585), 689103522)

    def test0839(self):
        self.assertEquals(self.calculate(-11037, 1296873507), 1296862470)

    def test0840(self):
        self.assertEquals(self.calculate(-3456, -1503299768), -1503303224)

    def test0841(self):
        self.assertEquals(self.calculate(-14155, -289429198), -289443353)

    def test0842(self):
        self.assertEquals(self.calculate(-1340, -65815689), -65817029)

    def test0843(self):
        self.assertEquals(self.calculate(9469, 1698866686), 1698876155)

    def test0844(self):
        self.assertEquals(self.calculate(15818, -1330334508), -1330318690)

    def test0845(self):
        self.assertEquals(self.calculate(888, -1448844901), -1448844013)

    def test0846(self):
        self.assertEquals(self.calculate(2128, 1517114792), 1517116920)

    def test0847(self):
        self.assertEquals(self.calculate(30346, 1102260443), 1102290789)

    def test0848(self):
        self.assertEquals(self.calculate(-7944, -1640970064), -1640978008)

    def test0849(self):
        self.assertEquals(self.calculate(-28307, -843313291), -843341598)

    def test0850(self):
        self.assertEquals(self.calculate(-24522, -1176422183), -1176446705)

    def test0851(self):
        self.assertEquals(self.calculate(-22315, -743701467), -743723782)

    def test0852(self):
        self.assertEquals(self.calculate(-30579, 1452188466), 1452157887)

    def test0853(self):
        self.assertEquals(self.calculate(-27328, -1325240804), -1325268132)

    def test0854(self):
        self.assertEquals(self.calculate(-25186, -412254314), -412279500)

    def test0855(self):
        self.assertEquals(self.calculate(-13438, 2059904913), 2059891475)

    def test0856(self):
        self.assertEquals(self.calculate(1644, -1128909178), -1128907534)

    def test0857(self):
        self.assertEquals(self.calculate(21340, -2133782943), -2133761603)

    def test0858(self):
        self.assertEquals(self.calculate(-17070, 1511936883), 1511919813)

    def test0859(self):
        self.assertEquals(self.calculate(32759, -1938940867), -1938908108)

    def test0860(self):
        self.assertEquals(self.calculate(6104, 638578887), 638584991)

    def test0861(self):
        self.assertEquals(self.calculate(29939, -1756347765), -1756317826)

    def test0862(self):
        self.assertEquals(self.calculate(-11396, -755836532), -755847928)

    def test0863(self):
        self.assertEquals(self.calculate(28416, -1864329699), -1864301283)

    def test0864(self):
        self.assertEquals(self.calculate(-15109, 586455653), 586440544)

    def test0865(self):
        self.assertEquals(self.calculate(28475, 1350629286), 1350657761)

    def test0866(self):
        self.assertEquals(self.calculate(-8788, -76534150), -76542938)

    def test0867(self):
        self.assertEquals(self.calculate(-24355, 1784870144), 1784845789)

    def test0868(self):
        self.assertEquals(self.calculate(-24306, -807745014), -807769320)

    def test0869(self):
        self.assertEquals(self.calculate(23830, -522474438), -522450608)

    def test0870(self):
        self.assertEquals(self.calculate(17273, -1448540105), -1448522832)

    def test0871(self):
        self.assertEquals(self.calculate(26651, 392068269), 392094920)

    def test0872(self):
        self.assertEquals(self.calculate(14008, 130380277), 130394285)

    def test0873(self):
        self.assertEquals(self.calculate(-2043, -1480730104), -1480732147)

    def test0874(self):
        self.assertEquals(self.calculate(13591, -1119522197), -1119508606)

    def test0875(self):
        self.assertEquals(self.calculate(-5199, 789292341), 789287142)

    def test0876(self):
        self.assertEquals(self.calculate(-30673, -198176012), -198206685)

    def test0877(self):
        self.assertEquals(self.calculate(-17246, -496844560), -496861806)

    def test0878(self):
        self.assertEquals(self.calculate(-30555, 1296771238), 1296740683)

    def test0879(self):
        self.assertEquals(self.calculate(-22155, 1178016384), 1177994229)

    def test0880(self):
        self.assertEquals(self.calculate(16706, 195102930), 195119636)

    def test0881(self):
        self.assertEquals(self.calculate(25638, -1919188143), -1919162505)

    def test0882(self):
        self.assertEquals(self.calculate(-6922, -1867841951), -1867848873)

    def test0883(self):
        self.assertEquals(self.calculate(11482, 1777445478), 1777456960)

    def test0884(self):
        self.assertEquals(self.calculate(29480, 767822374), 767851854)

    def test0885(self):
        self.assertEquals(self.calculate(32725, -576098955), -576066230)

    def test0886(self):
        self.assertEquals(self.calculate(-6677, 1477719262), 1477712585)

    def test0887(self):
        self.assertEquals(self.calculate(20440, -820840849), -820820409)

    def test0888(self):
        self.assertEquals(self.calculate(-14681, -1603682377), -1603697058)

    def test0889(self):
        self.assertEquals(self.calculate(6077, -1157365239), -1157359162)

    def test0890(self):
        self.assertEquals(self.calculate(10055, 1191160504), 1191170559)

    def test0891(self):
        self.assertEquals(self.calculate(31921, 1256259393), 1256291314)

    def test0892(self):
        self.assertEquals(self.calculate(30507, -1935232877), -1935202370)

    def test0893(self):
        self.assertEquals(self.calculate(-22748, -1920174960), -1920197708)

    def test0894(self):
        self.assertEquals(self.calculate(17785, -1765635557), -1765617772)

    def test0895(self):
        self.assertEquals(self.calculate(9006, -548749548), -548740542)

    def test0896(self):
        self.assertEquals(self.calculate(3727, -1234035357), -1234031630)

    def test0897(self):
        self.assertEquals(self.calculate(-18145, -1698421166), -1698439311)

    def test0898(self):
        self.assertEquals(self.calculate(28200, -2137096431), -2137068231)

    def test0899(self):
        self.assertEquals(self.calculate(25349, -489771676), -489746327)

    def test0900(self):
        self.assertEquals(self.calculate(-23890, 700562304), 700538414)

    def test0901(self):
        self.assertEquals(self.calculate(30875, -1798252696), -1798221821)

    def test0902(self):
        self.assertEquals(self.calculate(24889, 579392385), 579417274)

    def test0903(self):
        self.assertEquals(self.calculate(2747, 1913199684), 1913202431)

    def test0904(self):
        self.assertEquals(self.calculate(1710, -160442509), -160440799)

    def test0905(self):
        self.assertEquals(self.calculate(-22519, -1571386087), -1571408606)

    def test0906(self):
        self.assertEquals(self.calculate(720, -486339675), -486338955)

    def test0907(self):
        self.assertEquals(self.calculate(28932, -1717343541), -1717314609)

    def test0908(self):
        self.assertEquals(self.calculate(-15087, -253883168), -253898255)

    def test0909(self):
        self.assertEquals(self.calculate(-16110, -476451480), -476467590)

    def test0910(self):
        self.assertEquals(self.calculate(20251, 1353007610), 1353027861)

    def test0911(self):
        self.assertEquals(self.calculate(-27620, 1447771355), 1447743735)

    def test0912(self):
        self.assertEquals(self.calculate(-22325, 695019777), 694997452)

    def test0913(self):
        self.assertEquals(self.calculate(-32063, 576441273), 576409210)

    def test0914(self):
        self.assertEquals(self.calculate(15518, 1708451760), 1708467278)

    def test0915(self):
        self.assertEquals(self.calculate(-13584, 1340778281), 1340764697)

    def test0916(self):
        self.assertEquals(self.calculate(-23246, -540315920), -540339166)

    def test0917(self):
        self.assertEquals(self.calculate(23861, 480427655), 480451516)

    def test0918(self):
        self.assertEquals(self.calculate(-177, -1701602359), -1701602536)

    def test0919(self):
        self.assertEquals(self.calculate(14899, -1640772447), -1640757548)

    def test0920(self):
        self.assertEquals(self.calculate(3969, -152672101), -152668132)

    def test0921(self):
        self.assertEquals(self.calculate(-20648, -487039214), -487059862)

    def test0922(self):
        self.assertEquals(self.calculate(-20915, 1357755327), 1357734412)

    def test0923(self):
        self.assertEquals(self.calculate(28528, -1591183521), -1591154993)

    def test0924(self):
        self.assertEquals(self.calculate(-16449, -1925973370), -1925989819)

    def test0925(self):
        self.assertEquals(self.calculate(-24440, -1805777643), -1805802083)

    def test0926(self):
        self.assertEquals(self.calculate(25380, 1029618041), 1029643421)

    def test0927(self):
        self.assertEquals(self.calculate(21868, -330709948), -330688080)

    def test0928(self):
        self.assertEquals(self.calculate(-20800, -1141572862), -1141593662)

    def test0929(self):
        self.assertEquals(self.calculate(19410, 1375638147), 1375657557)

    def test0930(self):
        self.assertEquals(self.calculate(9354, -713921836), -713912482)

    def test0931(self):
        self.assertEquals(self.calculate(-20313, 1202805666), 1202785353)

    def test0932(self):
        self.assertEquals(self.calculate(-8579, -1141063774), -1141072353)

    def test0933(self):
        self.assertEquals(self.calculate(21719, 302521023), 302542742)

    def test0934(self):
        self.assertEquals(self.calculate(4419, 2062295197), 2062299616)

    def test0935(self):
        self.assertEquals(self.calculate(28655, 1693747747), 1693776402)

    def test0936(self):
        self.assertEquals(self.calculate(29631, -642416057), -642386426)

    def test0937(self):
        self.assertEquals(self.calculate(364, 708734937), 708735301)

    def test0938(self):
        self.assertEquals(self.calculate(-10048, -1088804147), -1088814195)

    def test0939(self):
        self.assertEquals(self.calculate(-29544, -556627093), -556656637)

    def test0940(self):
        self.assertEquals(self.calculate(-22406, 305711570), 305689164)

    def test0941(self):
        self.assertEquals(self.calculate(16083, -299994691), -299978608)

    def test0942(self):
        self.assertEquals(self.calculate(32466, 897090131), 897122597)

    def test0943(self):
        self.assertEquals(self.calculate(-20971, 1447485542), 1447464571)

    def test0944(self):
        self.assertEquals(self.calculate(8594, 818439851), 818448445)

    def test0945(self):
        self.assertEquals(self.calculate(-9882, 803499937), 803490055)

    def test0946(self):
        self.assertEquals(self.calculate(-18803, 1474132659), 1474113856)

    def test0947(self):
        self.assertEquals(self.calculate(9805, 1469438170), 1469447975)

    def test0948(self):
        self.assertEquals(self.calculate(-11365, -1672969276), -1672980641)

    def test0949(self):
        self.assertEquals(self.calculate(13074, 525177632), 525190706)

    def test0950(self):
        self.assertEquals(self.calculate(18872, 1891890385), 1891909257)

    def test0951(self):
        self.assertEquals(self.calculate(27279, -1248954149), -1248926870)

    def test0952(self):
        self.assertEquals(self.calculate(9673, -816815956), -816806283)

    def test0953(self):
        self.assertEquals(self.calculate(-12124, 846852623), 846840499)

    def test0954(self):
        self.assertEquals(self.calculate(7471, -614252456), -614244985)

    def test0955(self):
        self.assertEquals(self.calculate(-22451, 2076561429), 2076538978)

    def test0956(self):
        self.assertEquals(self.calculate(-27873, 1396626888), 1396599015)

    def test0957(self):
        self.assertEquals(self.calculate(-24154, -883849199), -883873353)

    def test0958(self):
        self.assertEquals(self.calculate(-13419, 290331044), 290317625)

    def test0959(self):
        self.assertEquals(self.calculate(-935, 190683026), 190682091)

    def test0960(self):
        self.assertEquals(self.calculate(27338, -803379831), -803352493)

    def test0961(self):
        self.assertEquals(self.calculate(-26212, 2001762822), 2001736610)

    def test0962(self):
        self.assertEquals(self.calculate(-16347, 234590576), 234574229)

    def test0963(self):
        self.assertEquals(self.calculate(30754, 1954638765), 1954669519)

    def test0964(self):
        self.assertEquals(self.calculate(17405, 904150976), 904168381)

    def test0965(self):
        self.assertEquals(self.calculate(-23935, 1798129552), 1798105617)

    def test0966(self):
        self.assertEquals(self.calculate(15568, 314461793), 314477361)

    def test0967(self):
        self.assertEquals(self.calculate(-1940, 1155372080), 1155370140)

    def test0968(self):
        self.assertEquals(self.calculate(4599, -1159220422), -1159215823)

    def test0969(self):
        self.assertEquals(self.calculate(9192, 418717786), 418726978)

    def test0970(self):
        self.assertEquals(self.calculate(-26819, -379853994), -379880813)

    def test0971(self):
        self.assertEquals(self.calculate(-24014, -463660164), -463684178)

    def test0972(self):
        self.assertEquals(self.calculate(15298, -647963280), -647947982)

    def test0973(self):
        self.assertEquals(self.calculate(-9182, 852342549), 852333367)

    def test0974(self):
        self.assertEquals(self.calculate(-8498, 869550118), 869541620)

    def test0975(self):
        self.assertEquals(self.calculate(-6419, 1780171377), 1780164958)

    def test0976(self):
        self.assertEquals(self.calculate(337, -204424935), -204424598)

    def test0977(self):
        self.assertEquals(self.calculate(-29172, -1529542194), -1529571366)

    def test0978(self):
        self.assertEquals(self.calculate(16443, -1254570221), -1254553778)

    def test0979(self):
        self.assertEquals(self.calculate(-3031, 2045804963), 2045801932)

    def test0980(self):
        self.assertEquals(self.calculate(-8313, -753868788), -753877101)

    def test0981(self):
        self.assertEquals(self.calculate(-29449, 332531256), 332501807)

    def test0982(self):
        self.assertEquals(self.calculate(30406, 1856727976), 1856758382)

    def test0983(self):
        self.assertEquals(self.calculate(-30534, -1583822150), -1583852684)

    def test0984(self):
        self.assertEquals(self.calculate(22181, 326433622), 326455803)

    def test0985(self):
        self.assertEquals(self.calculate(-14937, -773345693), -773360630)

    def test0986(self):
        self.assertEquals(self.calculate(20883, -601743959), -601723076)

    def test0987(self):
        self.assertEquals(self.calculate(-24285, 1629519520), 1629495235)

    def test0988(self):
        self.assertEquals(self.calculate(24343, -1961270990), -1961246647)

    def test0989(self):
        self.assertEquals(self.calculate(31521, -1907542745), -1907511224)

    def test0990(self):
        self.assertEquals(self.calculate(18941, 1328832629), 1328851570)

    def test0991(self):
        self.assertEquals(self.calculate(9073, 1568594747), 1568603820)

    def test0992(self):
        self.assertEquals(self.calculate(-30792, -43963740), -43994532)

    def test0993(self):
        self.assertEquals(self.calculate(23287, 1396262169), 1396285456)

    def test0994(self):
        self.assertEquals(self.calculate(-4977, 439599387), 439594410)

    def test0995(self):
        self.assertEquals(self.calculate(-13689, 2082105617), 2082091928)

    def test0996(self):
        self.assertEquals(self.calculate(-7160, 114840541), 114833381)

    def test0997(self):
        self.assertEquals(self.calculate(17452, 1421770351), 1421787803)

    def test0998(self):
        self.assertEquals(self.calculate(20106, -988879826), -988859720)

    def test0999(self):
        self.assertEquals(self.calculate(-29699, -2040020631), -2040050330)

    def test1000(self):
        self.assertEquals(self.calculate(9414, -460192304), -460182890)

    def test1001(self):
        self.assertEquals(self.calculate(92, 1961538122), 1961538214)

    def test1002(self):
        self.assertEquals(self.calculate(6546, -1934819620), -1934813074)

    def test1003(self):
        self.assertEquals(self.calculate(20274, -209827429), -209807155)

    def test1004(self):
        self.assertEquals(self.calculate(-28325, 1339918470), 1339890145)

    def test1005(self):
        self.assertEquals(self.calculate(6417, 848661416), 848667833)

    def test1006(self):
        self.assertEquals(self.calculate(13574, 341679840), 341693414)

    def test1007(self):
        self.assertEquals(self.calculate(-4339, 1708742458), 1708738119)

    def test1008(self):
        self.assertEquals(self.calculate(-4505, -48900880), -48905385)

    def test1009(self):
        self.assertEquals(self.calculate(12525, -1058965025), -1058952500)

    def test1010(self):
        self.assertEquals(self.calculate(-1697, 1169312933), 1169311236)

    def test1011(self):
        self.assertEquals(self.calculate(-6306, -623518061), -623524367)

    def test1012(self):
        self.assertEquals(self.calculate(2553, 1224653762), 1224656315)

    def test1013(self):
        self.assertEquals(self.calculate(-28689, -254732966), -254761655)

    def test1014(self):
        self.assertEquals(self.calculate(-8748, -92804927), -92813675)

    def test1015(self):
        self.assertEquals(self.calculate(32715, -165170957), -165138242)

    def test1016(self):
        self.assertEquals(self.calculate(-4761, -1491913769), -1491918530)

    def test1017(self):
        self.assertEquals(self.calculate(-20774, -847902073), -847922847)

    def test1018(self):
        self.assertEquals(self.calculate(-8343, -21224786), -21233129)

    def test1019(self):
        self.assertEquals(self.calculate(17843, -3942909), -3925066)

    def test1020(self):
        self.assertEquals(self.calculate(26117, -1546474162), -1546448045)

    def test1021(self):
        self.assertEquals(self.calculate(17426, 1534150894), 1534168320)

    def test1022(self):
        self.assertEquals(self.calculate(18880, -1274844295), -1274825415)

    def test1023(self):
        self.assertEquals(self.calculate(21682, -1827216458), -1827194776)


class TestVM_Add_IntFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_INT_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushW(lhs)
        v.VM_PushF(rhs)
        v.VM_Add()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(-14698, -160200.0), -174898.00, "")

    def test0001(self):
        self.assertEquals(self.calculate(18945, -20239.0), -1294.00, "")

    def test0002(self):
        self.assertEquals(self.calculate(16441, -11248.0), 5193.00, "")

    def test0003(self):
        self.assertEquals(self.calculate(-2532, -43129.0), -45661.00, "")

    def test0004(self):
        self.assertEquals(self.calculate(20141, 111710.0), 131851.00, "")

    def test0005(self):
        self.assertEquals(self.calculate(-24229, -151230.0), -175459.00, "")

    def test0006(self):
        self.assertEquals(self.calculate(10266, 29031.0), 39297.00, "")

    def test0007(self):
        self.assertEquals(self.calculate(-13697, 43964.0), 30267.00, "")

    def test0008(self):
        self.assertEquals(self.calculate(-15963, 175780.0), 159817.00, "")

    def test0009(self):
        self.assertEquals(self.calculate(5889, -79022.0), -73133.00, "")

    def test0010(self):
        self.assertEquals(self.calculate(9516, 62049.0), 71565.00, "")

    def test0011(self):
        self.assertEquals(self.calculate(-29052, -190114.0), -219166.00, "")

    def test0012(self):
        self.assertEquals(self.calculate(26145, 165819.0), 191964.00, "")

    def test0013(self):
        self.assertEquals(self.calculate(23421, 156052.0), 179473.00, "")

    def test0014(self):
        self.assertEquals(self.calculate(1547, 114020.0), 115567.00, "")

    def test0015(self):
        self.assertEquals(self.calculate(-9201, -91785.0), -100986.00, "")

    def test0016(self):
        self.assertEquals(self.calculate(-22158, -125558.0), -147716.00, "")

    def test0017(self):
        self.assertEquals(self.calculate(-21442, 123549.0), 102107.00, "")

    def test0018(self):
        self.assertEquals(self.calculate(-25463, 125106.0), 99643.00, "")

    def test0019(self):
        self.assertEquals(self.calculate(4016, 45576.0), 49592.00, "")

    def test0020(self):
        self.assertEquals(self.calculate(-17794, -82976.0), -100770.00, "")

    def test0021(self):
        self.assertEquals(self.calculate(-9247, 69693.0), 60446.00, "")

    def test0022(self):
        self.assertEquals(self.calculate(-32647, 80929.0), 48282.00, "")

    def test0023(self):
        self.assertEquals(self.calculate(14216, -49290.0), -35074.00, "")

    def test0024(self):
        self.assertEquals(self.calculate(-27198, 55175.0), 27977.00, "")

    def test0025(self):
        self.assertEquals(self.calculate(-28830, -133678.0), -162508.00, "")

    def test0026(self):
        self.assertEquals(self.calculate(-9434, 155458.0), 146024.00, "")

    def test0027(self):
        self.assertEquals(self.calculate(-9189, 77739.0), 68550.00, "")

    def test0028(self):
        self.assertEquals(self.calculate(10913, 59011.0), 69924.00, "")

    def test0029(self):
        self.assertEquals(self.calculate(-5562, -133473.0), -139035.00, "")

    def test0030(self):
        self.assertEquals(self.calculate(-7729, -39322.0), -47051.00, "")

    def test0031(self):
        self.assertEquals(self.calculate(-18280, 124787.0), 106507.00, "")

    def test0032(self):
        self.assertEquals(self.calculate(10542, 83570.0), 94112.00, "")

    def test0033(self):
        self.assertEquals(self.calculate(-27734, -141623.0), -169357.00, "")

    def test0034(self):
        self.assertEquals(self.calculate(21113, -148164.0), -127051.00, "")

    def test0035(self):
        self.assertEquals(self.calculate(-10999, 71736.0), 60737.00, "")

    def test0036(self):
        self.assertEquals(self.calculate(12027, -88739.0), -76712.00, "")

    def test0037(self):
        self.assertEquals(self.calculate(-795, 86944.0), 86149.00, "")

    def test0038(self):
        self.assertEquals(self.calculate(1190, -85023.0), -83833.00, "")

    def test0039(self):
        self.assertEquals(self.calculate(-1773, -176399.0), -178172.00, "")

    def test0040(self):
        self.assertEquals(self.calculate(-20216, 132686.0), 112470.00, "")

    def test0041(self):
        self.assertEquals(self.calculate(-29413, -60609.0), -90022.00, "")

    def test0042(self):
        self.assertEquals(self.calculate(-14134, 153113.0), 138979.00, "")

    def test0043(self):
        self.assertEquals(self.calculate(8110, 56921.0), 65031.00, "")

    def test0044(self):
        self.assertEquals(self.calculate(-3388, 52191.0), 48803.00, "")

    def test0045(self):
        self.assertEquals(self.calculate(-4068, 106004.0), 101936.00, "")

    def test0046(self):
        self.assertEquals(self.calculate(-25422, 23547.0), -1875.00, "")

    def test0047(self):
        self.assertEquals(self.calculate(86, -73939.0), -73853.00, "")

    def test0048(self):
        self.assertEquals(self.calculate(23549, -50899.0), -27350.00, "")

    def test0049(self):
        self.assertEquals(self.calculate(12237, -166626.0), -154389.00, "")

    def test0050(self):
        self.assertEquals(self.calculate(-25467, 94551.0), 69084.00, "")

    def test0051(self):
        self.assertEquals(self.calculate(-31927, 103269.0), 71342.00, "")

    def test0052(self):
        self.assertEquals(self.calculate(-10705, -119719.0), -130424.00, "")

    def test0053(self):
        self.assertEquals(self.calculate(-2683, 184963.0), 182280.00, "")

    def test0054(self):
        self.assertEquals(self.calculate(9604, 117249.0), 126853.00, "")

    def test0055(self):
        self.assertEquals(self.calculate(3743, -110947.0), -107204.00, "")

    def test0056(self):
        self.assertEquals(self.calculate(20401, 171803.0), 192204.00, "")

    def test0057(self):
        self.assertEquals(self.calculate(23275, -115668.0), -92393.00, "")

    def test0058(self):
        self.assertEquals(self.calculate(29781, 72020.0), 101801.00, "")

    def test0059(self):
        self.assertEquals(self.calculate(-5788, -139718.0), -145506.00, "")

    def test0060(self):
        self.assertEquals(self.calculate(31503, -112369.0), -80866.00, "")

    def test0061(self):
        self.assertEquals(self.calculate(-11370, 178537.0), 167167.00, "")

    def test0062(self):
        self.assertEquals(self.calculate(-10536, 149426.0), 138890.00, "")

    def test0063(self):
        self.assertEquals(self.calculate(-9475, -81777.0), -91252.00, "")

    def test0064(self):
        self.assertEquals(self.calculate(12963, 174833.0), 187796.00, "")

    def test0065(self):
        self.assertEquals(self.calculate(2107, 163089.0), 165196.00, "")

    def test0066(self):
        self.assertEquals(self.calculate(-1125, -36432.0), -37557.00, "")

    def test0067(self):
        self.assertEquals(self.calculate(25788, 99450.0), 125238.00, "")

    def test0068(self):
        self.assertEquals(self.calculate(-23423, -124542.0), -147965.00, "")

    def test0069(self):
        self.assertEquals(self.calculate(-2443, 28656.0), 26213.00, "")

    def test0070(self):
        self.assertEquals(self.calculate(-23858, -45159.0), -69017.00, "")

    def test0071(self):
        self.assertEquals(self.calculate(-26490, -11618.0), -38108.00, "")

    def test0072(self):
        self.assertEquals(self.calculate(32685, -30963.0), 1722.00, "")

    def test0073(self):
        self.assertEquals(self.calculate(-25244, 69901.0), 44657.00, "")

    def test0074(self):
        self.assertEquals(self.calculate(-25372, -126444.0), -151816.00, "")

    def test0075(self):
        self.assertEquals(self.calculate(-9344, -17405.0), -26749.00, "")

    def test0076(self):
        self.assertEquals(self.calculate(30549, -174049.0), -143500.00, "")

    def test0077(self):
        self.assertEquals(self.calculate(-16740, 83506.0), 66766.00, "")

    def test0078(self):
        self.assertEquals(self.calculate(31389, 187402.0), 218791.00, "")

    def test0079(self):
        self.assertEquals(self.calculate(-19902, 174097.0), 154195.00, "")

    def test0080(self):
        self.assertEquals(self.calculate(-23278, -97524.0), -120802.00, "")

    def test0081(self):
        self.assertEquals(self.calculate(-15663, 120127.0), 104464.00, "")

    def test0082(self):
        self.assertEquals(self.calculate(22240, 39597.0), 61837.00, "")

    def test0083(self):
        self.assertEquals(self.calculate(27194, 186359.0), 213553.00, "")

    def test0084(self):
        self.assertEquals(self.calculate(-15281, 11984.0), -3297.00, "")

    def test0085(self):
        self.assertEquals(self.calculate(-5463, 80562.0), 75099.00, "")

    def test0086(self):
        self.assertEquals(self.calculate(6151, -131848.0), -125697.00, "")

    def test0087(self):
        self.assertEquals(self.calculate(-7771, -19096.0), -26867.00, "")

    def test0088(self):
        self.assertEquals(self.calculate(828, -78739.0), -77911.00, "")

    def test0089(self):
        self.assertEquals(self.calculate(-29929, -46577.0), -76506.00, "")

    def test0090(self):
        self.assertEquals(self.calculate(-29659, -47958.0), -77617.00, "")

    def test0091(self):
        self.assertEquals(self.calculate(25717, -110773.0), -85056.00, "")

    def test0092(self):
        self.assertEquals(self.calculate(-19788, 30532.0), 10744.00, "")

    def test0093(self):
        self.assertEquals(self.calculate(13118, 19173.0), 32291.00, "")

    def test0094(self):
        self.assertEquals(self.calculate(14110, -16230.0), -2120.00, "")

    def test0095(self):
        self.assertEquals(self.calculate(13930, 159303.0), 173233.00, "")

    def test0096(self):
        self.assertEquals(self.calculate(29769, 11481.0), 41250.00, "")

    def test0097(self):
        self.assertEquals(self.calculate(2011, 160290.0), 162301.00, "")

    def test0098(self):
        self.assertEquals(self.calculate(-12137, 11649.0), -488.00, "")

    def test0099(self):
        self.assertEquals(self.calculate(-1486, -114409.0), -115895.00, "")

    def test0100(self):
        self.assertEquals(self.calculate(15499, -62960.0), -47461.00, "")

    def test0101(self):
        self.assertEquals(self.calculate(29389, -142615.0), -113226.00, "")

    def test0102(self):
        self.assertEquals(self.calculate(-4649, -155541.0), -160190.00, "")

    def test0103(self):
        self.assertEquals(self.calculate(-16508, 8847.0), -7661.00, "")

    def test0104(self):
        self.assertEquals(self.calculate(-24361, 106900.0), 82539.00, "")

    def test0105(self):
        self.assertEquals(self.calculate(-1772, -176365.0), -178137.00, "")

    def test0106(self):
        self.assertEquals(self.calculate(30386, -101986.0), -71600.00, "")

    def test0107(self):
        self.assertEquals(self.calculate(20594, 156160.0), 176754.00, "")

    def test0108(self):
        self.assertEquals(self.calculate(12117, 68411.0), 80528.00, "")

    def test0109(self):
        self.assertEquals(self.calculate(12095, 69360.0), 81455.00, "")

    def test0110(self):
        self.assertEquals(self.calculate(5571, -145217.0), -139646.00, "")

    def test0111(self):
        self.assertEquals(self.calculate(-9593, 163934.0), 154341.00, "")

    def test0112(self):
        self.assertEquals(self.calculate(-16110, -96612.0), -112722.00, "")

    def test0113(self):
        self.assertEquals(self.calculate(21209, 41290.0), 62499.00, "")

    def test0114(self):
        self.assertEquals(self.calculate(-11917, -55221.0), -67138.00, "")

    def test0115(self):
        self.assertEquals(self.calculate(16199, -89903.0), -73704.00, "")

    def test0116(self):
        self.assertEquals(self.calculate(7302, -59321.0), -52019.00, "")

    def test0117(self):
        self.assertEquals(self.calculate(-22413, 124927.0), 102514.00, "")

    def test0118(self):
        self.assertEquals(self.calculate(4329, 84567.0), 88896.00, "")

    def test0119(self):
        self.assertEquals(self.calculate(15686, 125779.0), 141465.00, "")

    def test0120(self):
        self.assertEquals(self.calculate(-21715, 136329.0), 114614.00, "")

    def test0121(self):
        self.assertEquals(self.calculate(14575, -23622.0), -9047.00, "")

    def test0122(self):
        self.assertEquals(self.calculate(9934, -69358.0), -59424.00, "")

    def test0123(self):
        self.assertEquals(self.calculate(-30977, 184690.0), 153713.00, "")

    def test0124(self):
        self.assertEquals(self.calculate(4, 98021.0), 98025.00, "")

    def test0125(self):
        self.assertEquals(self.calculate(-17819, -163017.0), -180836.00, "")

    def test0126(self):
        self.assertEquals(self.calculate(22955, 66971.0), 89926.00, "")

    def test0127(self):
        self.assertEquals(self.calculate(1724, -35682.0), -33958.00, "")

    def test0128(self):
        self.assertEquals(self.calculate(-26009, 126885.0), 100876.00, "")

    def test0129(self):
        self.assertEquals(self.calculate(28199, 182727.0), 210926.00, "")

    def test0130(self):
        self.assertEquals(self.calculate(14678, 167608.0), 182286.00, "")

    def test0131(self):
        self.assertEquals(self.calculate(-9143, 88028.0), 78885.00, "")

    def test0132(self):
        self.assertEquals(self.calculate(13258, -90988.0), -77730.00, "")

    def test0133(self):
        self.assertEquals(self.calculate(24158, -39593.0), -15435.00, "")

    def test0134(self):
        self.assertEquals(self.calculate(16235, 112615.0), 128850.00, "")

    def test0135(self):
        self.assertEquals(self.calculate(-26350, 60776.0), 34426.00, "")

    def test0136(self):
        self.assertEquals(self.calculate(-29473, 92100.0), 62627.00, "")

    def test0137(self):
        self.assertEquals(self.calculate(-16852, -99252.0), -116104.00, "")

    def test0138(self):
        self.assertEquals(self.calculate(25445, -223.0), 25222.00, "")

    def test0139(self):
        self.assertEquals(self.calculate(-6292, -167814.0), -174106.00, "")

    def test0140(self):
        self.assertEquals(self.calculate(24732, 50596.0), 75328.00, "")

    def test0141(self):
        self.assertEquals(self.calculate(2002, 140863.0), 142865.00, "")

    def test0142(self):
        self.assertEquals(self.calculate(-13502, -137244.0), -150746.00, "")

    def test0143(self):
        self.assertEquals(self.calculate(3361, 99243.0), 102604.00, "")

    def test0144(self):
        self.assertEquals(self.calculate(-23865, -135774.0), -159639.00, "")

    def test0145(self):
        self.assertEquals(self.calculate(11003, -110019.0), -99016.00, "")

    def test0146(self):
        self.assertEquals(self.calculate(-25362, 47132.0), 21770.00, "")

    def test0147(self):
        self.assertEquals(self.calculate(31563, 49300.0), 80863.00, "")

    def test0148(self):
        self.assertEquals(self.calculate(-26886, 54623.0), 27737.00, "")

    def test0149(self):
        self.assertEquals(self.calculate(-29617, -158404.0), -188021.00, "")

    def test0150(self):
        self.assertEquals(self.calculate(-30647, -178345.0), -208992.00, "")

    def test0151(self):
        self.assertEquals(self.calculate(-24969, -154117.0), -179086.00, "")

    def test0152(self):
        self.assertEquals(self.calculate(-15793, -88103.0), -103896.00, "")

    def test0153(self):
        self.assertEquals(self.calculate(31216, 124804.0), 156020.00, "")

    def test0154(self):
        self.assertEquals(self.calculate(-22133, 193197.0), 171064.00, "")

    def test0155(self):
        self.assertEquals(self.calculate(-6161, -113632.0), -119793.00, "")

    def test0156(self):
        self.assertEquals(self.calculate(8285, 194751.0), 203036.00, "")

    def test0157(self):
        self.assertEquals(self.calculate(-12821, -138985.0), -151806.00, "")

    def test0158(self):
        self.assertEquals(self.calculate(-9363, 104719.0), 95356.00, "")

    def test0159(self):
        self.assertEquals(self.calculate(-25503, -182220.0), -207723.00, "")

    def test0160(self):
        self.assertEquals(self.calculate(22304, -154347.0), -132043.00, "")

    def test0161(self):
        self.assertEquals(self.calculate(31749, -8713.0), 23036.00, "")

    def test0162(self):
        self.assertEquals(self.calculate(-27070, -136555.0), -163625.00, "")

    def test0163(self):
        self.assertEquals(self.calculate(-10178, 139323.0), 129145.00, "")

    def test0164(self):
        self.assertEquals(self.calculate(15255, 66108.0), 81363.00, "")

    def test0165(self):
        self.assertEquals(self.calculate(-15571, -62367.0), -77938.00, "")

    def test0166(self):
        self.assertEquals(self.calculate(30120, -176114.0), -145994.00, "")

    def test0167(self):
        self.assertEquals(self.calculate(20413, 80709.0), 101122.00, "")

    def test0168(self):
        self.assertEquals(self.calculate(-17019, 17717.0), 698.00, "")

    def test0169(self):
        self.assertEquals(self.calculate(-17065, -196722.0), -213787.00, "")

    def test0170(self):
        self.assertEquals(self.calculate(29356, 59976.0), 89332.00, "")

    def test0171(self):
        self.assertEquals(self.calculate(32478, 47577.0), 80055.00, "")

    def test0172(self):
        self.assertEquals(self.calculate(-4661, 127236.0), 122575.00, "")

    def test0173(self):
        self.assertEquals(self.calculate(-32750, 72924.0), 40174.00, "")

    def test0174(self):
        self.assertEquals(self.calculate(31285, -30576.0), 709.00, "")

    def test0175(self):
        self.assertEquals(self.calculate(4224, -37475.0), -33251.00, "")

    def test0176(self):
        self.assertEquals(self.calculate(-4643, 118850.0), 114207.00, "")

    def test0177(self):
        self.assertEquals(self.calculate(-3158, -97713.0), -100871.00, "")

    def test0178(self):
        self.assertEquals(self.calculate(17758, -148098.0), -130340.00, "")

    def test0179(self):
        self.assertEquals(self.calculate(2827, -173088.0), -170261.00, "")

    def test0180(self):
        self.assertEquals(self.calculate(-30332, -99158.0), -129490.00, "")

    def test0181(self):
        self.assertEquals(self.calculate(-5240, 120412.0), 115172.00, "")

    def test0182(self):
        self.assertEquals(self.calculate(-1030, -69878.0), -70908.00, "")

    def test0183(self):
        self.assertEquals(self.calculate(-28653, 46849.0), 18196.00, "")

    def test0184(self):
        self.assertEquals(self.calculate(2458, 159444.0), 161902.00, "")

    def test0185(self):
        self.assertEquals(self.calculate(-13769, -100677.0), -114446.00, "")

    def test0186(self):
        self.assertEquals(self.calculate(28854, 160792.0), 189646.00, "")

    def test0187(self):
        self.assertEquals(self.calculate(6817, 196812.0), 203629.00, "")

    def test0188(self):
        self.assertEquals(self.calculate(-28647, -94078.0), -122725.00, "")

    def test0189(self):
        self.assertEquals(self.calculate(9338, 74754.0), 84092.00, "")

    def test0190(self):
        self.assertEquals(self.calculate(2163, 125807.0), 127970.00, "")

    def test0191(self):
        self.assertEquals(self.calculate(-1326, 64169.0), 62843.00, "")

    def test0192(self):
        self.assertEquals(self.calculate(9544, -137412.0), -127868.00, "")

    def test0193(self):
        self.assertEquals(self.calculate(-6962, -53457.0), -60419.00, "")

    def test0194(self):
        self.assertEquals(self.calculate(3576, 169275.0), 172851.00, "")

    def test0195(self):
        self.assertEquals(self.calculate(-18690, 114050.0), 95360.00, "")

    def test0196(self):
        self.assertEquals(self.calculate(-22526, -84190.0), -106716.00, "")

    def test0197(self):
        self.assertEquals(self.calculate(-28586, -73108.0), -101694.00, "")

    def test0198(self):
        self.assertEquals(self.calculate(-17825, 84868.0), 67043.00, "")

    def test0199(self):
        self.assertEquals(self.calculate(-8229, 112154.0), 103925.00, "")

    def test0200(self):
        self.assertEquals(self.calculate(858, -190593.0), -189735.00, "")

    def test0201(self):
        self.assertEquals(self.calculate(-2992, -29184.0), -32176.00, "")

    def test0202(self):
        self.assertEquals(self.calculate(27874, -17361.0), 10513.00, "")

    def test0203(self):
        self.assertEquals(self.calculate(-4305, 116327.0), 112022.00, "")

    def test0204(self):
        self.assertEquals(self.calculate(-16348, -143839.0), -160187.00, "")

    def test0205(self):
        self.assertEquals(self.calculate(16906, -182813.0), -165907.00, "")

    def test0206(self):
        self.assertEquals(self.calculate(14712, 127828.0), 142540.00, "")

    def test0207(self):
        self.assertEquals(self.calculate(-22161, 756.0), -21405.00, "")

    def test0208(self):
        self.assertEquals(self.calculate(9697, 58934.0), 68631.00, "")

    def test0209(self):
        self.assertEquals(self.calculate(8267, 130786.0), 139053.00, "")

    def test0210(self):
        self.assertEquals(self.calculate(-924, 11593.0), 10669.00, "")

    def test0211(self):
        self.assertEquals(self.calculate(-16031, 120851.0), 104820.00, "")

    def test0212(self):
        self.assertEquals(self.calculate(-11786, -108967.0), -120753.00, "")

    def test0213(self):
        self.assertEquals(self.calculate(-17377, -40741.0), -58118.00, "")

    def test0214(self):
        self.assertEquals(self.calculate(-1699, 199799.0), 198100.00, "")

    def test0215(self):
        self.assertEquals(self.calculate(-18679, 62582.0), 43903.00, "")

    def test0216(self):
        self.assertEquals(self.calculate(-24238, -178710.0), -202948.00, "")

    def test0217(self):
        self.assertEquals(self.calculate(21098, 121648.0), 142746.00, "")

    def test0218(self):
        self.assertEquals(self.calculate(1856, -184111.0), -182255.00, "")

    def test0219(self):
        self.assertEquals(self.calculate(-2212, -24101.0), -26313.00, "")

    def test0220(self):
        self.assertEquals(self.calculate(30014, -171579.0), -141565.00, "")

    def test0221(self):
        self.assertEquals(self.calculate(-30886, 49767.0), 18881.00, "")

    def test0222(self):
        self.assertEquals(self.calculate(-12874, 168292.0), 155418.00, "")

    def test0223(self):
        self.assertEquals(self.calculate(19100, -137759.0), -118659.00, "")

    def test0224(self):
        self.assertEquals(self.calculate(11639, 199250.0), 210889.00, "")

    def test0225(self):
        self.assertEquals(self.calculate(27229, -102053.0), -74824.00, "")

    def test0226(self):
        self.assertEquals(self.calculate(16721, -10104.0), 6617.00, "")

    def test0227(self):
        self.assertEquals(self.calculate(-29946, -61391.0), -91337.00, "")

    def test0228(self):
        self.assertEquals(self.calculate(8466, 125197.0), 133663.00, "")

    def test0229(self):
        self.assertEquals(self.calculate(6935, 77031.0), 83966.00, "")

    def test0230(self):
        self.assertEquals(self.calculate(-26349, -5805.0), -32154.00, "")

    def test0231(self):
        self.assertEquals(self.calculate(7800, 83933.0), 91733.00, "")

    def test0232(self):
        self.assertEquals(self.calculate(-4561, 184303.0), 179742.00, "")

    def test0233(self):
        self.assertEquals(self.calculate(26569, -91341.0), -64772.00, "")

    def test0234(self):
        self.assertEquals(self.calculate(21262, -6226.0), 15036.00, "")

    def test0235(self):
        self.assertEquals(self.calculate(3344, 169665.0), 173009.00, "")

    def test0236(self):
        self.assertEquals(self.calculate(-352, 18722.0), 18370.00, "")

    def test0237(self):
        self.assertEquals(self.calculate(24398, -193944.0), -169546.00, "")

    def test0238(self):
        self.assertEquals(self.calculate(14342, -81467.0), -67125.00, "")

    def test0239(self):
        self.assertEquals(self.calculate(-19657, 1070.0), -18587.00, "")

    def test0240(self):
        self.assertEquals(self.calculate(-9136, -129623.0), -138759.00, "")

    def test0241(self):
        self.assertEquals(self.calculate(-26939, 65631.0), 38692.00, "")

    def test0242(self):
        self.assertEquals(self.calculate(10042, -89839.0), -79797.00, "")

    def test0243(self):
        self.assertEquals(self.calculate(-27187, 194631.0), 167444.00, "")

    def test0244(self):
        self.assertEquals(self.calculate(-6280, -167351.0), -173631.00, "")

    def test0245(self):
        self.assertEquals(self.calculate(25451, -164771.0), -139320.00, "")

    def test0246(self):
        self.assertEquals(self.calculate(28222, 122118.0), 150340.00, "")

    def test0247(self):
        self.assertEquals(self.calculate(-2902, 5735.0), 2833.00, "")

    def test0248(self):
        self.assertEquals(self.calculate(6360, 49363.0), 55723.00, "")

    def test0249(self):
        self.assertEquals(self.calculate(27103, 94248.0), 121351.00, "")

    def test0250(self):
        self.assertEquals(self.calculate(26651, -794.0), 25857.00, "")

    def test0251(self):
        self.assertEquals(self.calculate(-16622, -93116.0), -109738.00, "")

    def test0252(self):
        self.assertEquals(self.calculate(-570, 45965.0), 45395.00, "")

    def test0253(self):
        self.assertEquals(self.calculate(15186, 197198.0), 212384.00, "")

    def test0254(self):
        self.assertEquals(self.calculate(32498, 70448.0), 102946.00, "")

    def test0255(self):
        self.assertEquals(self.calculate(5583, -159948.0), -154365.00, "")

    def test0256(self):
        self.assertEquals(self.calculate(-18455, -74372.0), -92827.00, "")

    def test0257(self):
        self.assertEquals(self.calculate(-22960, 8086.0), -14874.00, "")

    def test0258(self):
        self.assertEquals(self.calculate(6307, -185346.0), -179039.00, "")

    def test0259(self):
        self.assertEquals(self.calculate(-11120, -160185.0), -171305.00, "")

    def test0260(self):
        self.assertEquals(self.calculate(-16367, -18402.0), -34769.00, "")

    def test0261(self):
        self.assertEquals(self.calculate(-18032, 57773.0), 39741.00, "")

    def test0262(self):
        self.assertEquals(self.calculate(-6650, 157489.0), 150839.00, "")

    def test0263(self):
        self.assertEquals(self.calculate(21871, 98273.0), 120144.00, "")

    def test0264(self):
        self.assertEquals(self.calculate(-32043, 104957.0), 72914.00, "")

    def test0265(self):
        self.assertEquals(self.calculate(9850, -97518.0), -87668.00, "")

    def test0266(self):
        self.assertEquals(self.calculate(17262, -44782.0), -27520.00, "")

    def test0267(self):
        self.assertEquals(self.calculate(-23910, 177135.0), 153225.00, "")

    def test0268(self):
        self.assertEquals(self.calculate(27369, -5039.0), 22330.00, "")

    def test0269(self):
        self.assertEquals(self.calculate(25922, -11546.0), 14376.00, "")

    def test0270(self):
        self.assertEquals(self.calculate(-30664, 104041.0), 73377.00, "")

    def test0271(self):
        self.assertEquals(self.calculate(-8319, -82417.0), -90736.00, "")

    def test0272(self):
        self.assertEquals(self.calculate(15324, -110520.0), -95196.00, "")

    def test0273(self):
        self.assertEquals(self.calculate(22421, -58268.0), -35847.00, "")

    def test0274(self):
        self.assertEquals(self.calculate(-17032, -191154.0), -208186.00, "")

    def test0275(self):
        self.assertEquals(self.calculate(-28739, 134069.0), 105330.00, "")

    def test0276(self):
        self.assertEquals(self.calculate(-4560, -118562.0), -123122.00, "")

    def test0277(self):
        self.assertEquals(self.calculate(-24855, -67568.0), -92423.00, "")

    def test0278(self):
        self.assertEquals(self.calculate(-7563, -71537.0), -79100.00, "")

    def test0279(self):
        self.assertEquals(self.calculate(-19357, 68713.0), 49356.00, "")

    def test0280(self):
        self.assertEquals(self.calculate(23316, -40409.0), -17093.00, "")

    def test0281(self):
        self.assertEquals(self.calculate(7475, 23792.0), 31267.00, "")

    def test0282(self):
        self.assertEquals(self.calculate(30897, -42357.0), -11460.00, "")

    def test0283(self):
        self.assertEquals(self.calculate(-9546, -181835.0), -191381.00, "")

    def test0284(self):
        self.assertEquals(self.calculate(7357, -45833.0), -38476.00, "")

    def test0285(self):
        self.assertEquals(self.calculate(-19871, 181958.0), 162087.00, "")

    def test0286(self):
        self.assertEquals(self.calculate(15002, -71114.0), -56112.00, "")

    def test0287(self):
        self.assertEquals(self.calculate(8432, -189475.0), -181043.00, "")

    def test0288(self):
        self.assertEquals(self.calculate(19223, 71005.0), 90228.00, "")

    def test0289(self):
        self.assertEquals(self.calculate(-4681, -66574.0), -71255.00, "")

    def test0290(self):
        self.assertEquals(self.calculate(-2203, -43539.0), -45742.00, "")

    def test0291(self):
        self.assertEquals(self.calculate(6330, 103639.0), 109969.00, "")

    def test0292(self):
        self.assertEquals(self.calculate(10408, -94812.0), -84404.00, "")

    def test0293(self):
        self.assertEquals(self.calculate(-10961, -95029.0), -105990.00, "")

    def test0294(self):
        self.assertEquals(self.calculate(6351, 104975.0), 111326.00, "")

    def test0295(self):
        self.assertEquals(self.calculate(28174, 33566.0), 61740.00, "")

    def test0296(self):
        self.assertEquals(self.calculate(7242, -188265.0), -181023.00, "")

    def test0297(self):
        self.assertEquals(self.calculate(-10302, 113345.0), 103043.00, "")

    def test0298(self):
        self.assertEquals(self.calculate(551, -184126.0), -183575.00, "")

    def test0299(self):
        self.assertEquals(self.calculate(26247, 144741.0), 170988.00, "")

    def test0300(self):
        self.assertEquals(self.calculate(878, -117671.0), -116793.00, "")

    def test0301(self):
        self.assertEquals(self.calculate(12605, -89074.0), -76469.00, "")

    def test0302(self):
        self.assertEquals(self.calculate(-31979, 194915.0), 162936.00, "")

    def test0303(self):
        self.assertEquals(self.calculate(26825, -159300.0), -132475.00, "")

    def test0304(self):
        self.assertEquals(self.calculate(31498, -17662.0), 13836.00, "")

    def test0305(self):
        self.assertEquals(self.calculate(5057, 9026.0), 14083.00, "")

    def test0306(self):
        self.assertEquals(self.calculate(-29800, -114573.0), -144373.00, "")

    def test0307(self):
        self.assertEquals(self.calculate(-5839, -145119.0), -150958.00, "")

    def test0308(self):
        self.assertEquals(self.calculate(-22295, 152537.0), 130242.00, "")

    def test0309(self):
        self.assertEquals(self.calculate(28531, 89508.0), 118039.00, "")

    def test0310(self):
        self.assertEquals(self.calculate(32238, -62902.0), -30664.00, "")

    def test0311(self):
        self.assertEquals(self.calculate(2055, 45427.0), 47482.00, "")

    def test0312(self):
        self.assertEquals(self.calculate(-32644, -31303.0), -63947.00, "")

    def test0313(self):
        self.assertEquals(self.calculate(8593, -133714.0), -125121.00, "")

    def test0314(self):
        self.assertEquals(self.calculate(17622, -116770.0), -99148.00, "")

    def test0315(self):
        self.assertEquals(self.calculate(-16601, -127694.0), -144295.00, "")

    def test0316(self):
        self.assertEquals(self.calculate(-27323, 112618.0), 85295.00, "")

    def test0317(self):
        self.assertEquals(self.calculate(-30156, -22090.0), -52246.00, "")

    def test0318(self):
        self.assertEquals(self.calculate(-18506, 158244.0), 139738.00, "")

    def test0319(self):
        self.assertEquals(self.calculate(-12769, -45270.0), -58039.00, "")

    def test0320(self):
        self.assertEquals(self.calculate(7392, -3893.0), 3499.00, "")

    def test0321(self):
        self.assertEquals(self.calculate(-20732, -75501.0), -96233.00, "")

    def test0322(self):
        self.assertEquals(self.calculate(4895, 26639.0), 31534.00, "")

    def test0323(self):
        self.assertEquals(self.calculate(9455, 130273.0), 139728.00, "")

    def test0324(self):
        self.assertEquals(self.calculate(26302, -134843.0), -108541.00, "")

    def test0325(self):
        self.assertEquals(self.calculate(29050, -161073.0), -132023.00, "")

    def test0326(self):
        self.assertEquals(self.calculate(-1138, 6281.0), 5143.00, "")

    def test0327(self):
        self.assertEquals(self.calculate(-22128, 152111.0), 129983.00, "")

    def test0328(self):
        self.assertEquals(self.calculate(-31876, -7996.0), -39872.00, "")

    def test0329(self):
        self.assertEquals(self.calculate(-5593, 133514.0), 127921.00, "")

    def test0330(self):
        self.assertEquals(self.calculate(11494, -59789.0), -48295.00, "")

    def test0331(self):
        self.assertEquals(self.calculate(-26248, -95563.0), -121811.00, "")

    def test0332(self):
        self.assertEquals(self.calculate(11469, -53034.0), -41565.00, "")

    def test0333(self):
        self.assertEquals(self.calculate(-1423, 148453.0), 147030.00, "")

    def test0334(self):
        self.assertEquals(self.calculate(25321, -55875.0), -30554.00, "")

    def test0335(self):
        self.assertEquals(self.calculate(-26269, -155933.0), -182202.00, "")

    def test0336(self):
        self.assertEquals(self.calculate(7424, 127932.0), 135356.00, "")

    def test0337(self):
        self.assertEquals(self.calculate(27062, 180900.0), 207962.00, "")

    def test0338(self):
        self.assertEquals(self.calculate(-8781, -19638.0), -28419.00, "")

    def test0339(self):
        self.assertEquals(self.calculate(-21131, -143726.0), -164857.00, "")

    def test0340(self):
        self.assertEquals(self.calculate(1504, -124005.0), -122501.00, "")

    def test0341(self):
        self.assertEquals(self.calculate(-12169, 180498.0), 168329.00, "")

    def test0342(self):
        self.assertEquals(self.calculate(12504, -196970.0), -184466.00, "")

    def test0343(self):
        self.assertEquals(self.calculate(-11678, -140290.0), -151968.00, "")

    def test0344(self):
        self.assertEquals(self.calculate(-2232, -49210.0), -51442.00, "")

    def test0345(self):
        self.assertEquals(self.calculate(25547, -158093.0), -132546.00, "")

    def test0346(self):
        self.assertEquals(self.calculate(15057, 189052.0), 204109.00, "")

    def test0347(self):
        self.assertEquals(self.calculate(11459, -181782.0), -170323.00, "")

    def test0348(self):
        self.assertEquals(self.calculate(-19777, -133176.0), -152953.00, "")

    def test0349(self):
        self.assertEquals(self.calculate(-27307, -169229.0), -196536.00, "")

    def test0350(self):
        self.assertEquals(self.calculate(17951, -43909.0), -25958.00, "")

    def test0351(self):
        self.assertEquals(self.calculate(10147, -132051.0), -121904.00, "")

    def test0352(self):
        self.assertEquals(self.calculate(16750, -94432.0), -77682.00, "")

    def test0353(self):
        self.assertEquals(self.calculate(-16347, 153562.0), 137215.00, "")

    def test0354(self):
        self.assertEquals(self.calculate(21954, 123385.0), 145339.00, "")

    def test0355(self):
        self.assertEquals(self.calculate(30245, 156881.0), 187126.00, "")

    def test0356(self):
        self.assertEquals(self.calculate(2433, 120508.0), 122941.00, "")

    def test0357(self):
        self.assertEquals(self.calculate(2865, 145342.0), 148207.00, "")

    def test0358(self):
        self.assertEquals(self.calculate(-29514, -35371.0), -64885.00, "")

    def test0359(self):
        self.assertEquals(self.calculate(15027, -12889.0), 2138.00, "")

    def test0360(self):
        self.assertEquals(self.calculate(22688, -158503.0), -135815.00, "")

    def test0361(self):
        self.assertEquals(self.calculate(18549, 28598.0), 47147.00, "")

    def test0362(self):
        self.assertEquals(self.calculate(13362, 82984.0), 96346.00, "")

    def test0363(self):
        self.assertEquals(self.calculate(-10588, 52762.0), 42174.00, "")

    def test0364(self):
        self.assertEquals(self.calculate(-5595, 85693.0), 80098.00, "")

    def test0365(self):
        self.assertEquals(self.calculate(29944, -65212.0), -35268.00, "")

    def test0366(self):
        self.assertEquals(self.calculate(26894, -62818.0), -35924.00, "")

    def test0367(self):
        self.assertEquals(self.calculate(-5087, 107510.0), 102423.00, "")

    def test0368(self):
        self.assertEquals(self.calculate(276, -155655.0), -155379.00, "")

    def test0369(self):
        self.assertEquals(self.calculate(16125, 38518.0), 54643.00, "")

    def test0370(self):
        self.assertEquals(self.calculate(18167, 113419.0), 131586.00, "")

    def test0371(self):
        self.assertEquals(self.calculate(-21393, 142094.0), 120701.00, "")

    def test0372(self):
        self.assertEquals(self.calculate(19285, 51468.0), 70753.00, "")

    def test0373(self):
        self.assertEquals(self.calculate(-30388, 16503.0), -13885.00, "")

    def test0374(self):
        self.assertEquals(self.calculate(-19141, -136986.0), -156127.00, "")

    def test0375(self):
        self.assertEquals(self.calculate(21680, -73302.0), -51622.00, "")

    def test0376(self):
        self.assertEquals(self.calculate(-10605, 51278.0), 40673.00, "")

    def test0377(self):
        self.assertEquals(self.calculate(10387, -135403.0), -125016.00, "")

    def test0378(self):
        self.assertEquals(self.calculate(7113, -182504.0), -175391.00, "")

    def test0379(self):
        self.assertEquals(self.calculate(-10155, -156215.0), -166370.00, "")

    def test0380(self):
        self.assertEquals(self.calculate(14897, -101827.0), -86930.00, "")

    def test0381(self):
        self.assertEquals(self.calculate(1241, 113974.0), 115215.00, "")

    def test0382(self):
        self.assertEquals(self.calculate(26685, -112817.0), -86132.00, "")

    def test0383(self):
        self.assertEquals(self.calculate(-13332, 29061.0), 15729.00, "")

    def test0384(self):
        self.assertEquals(self.calculate(13697, -143050.0), -129353.00, "")

    def test0385(self):
        self.assertEquals(self.calculate(-840, 78597.0), 77757.00, "")

    def test0386(self):
        self.assertEquals(self.calculate(-17955, -49492.0), -67447.00, "")

    def test0387(self):
        self.assertEquals(self.calculate(6153, 91816.0), 97969.00, "")

    def test0388(self):
        self.assertEquals(self.calculate(-10648, -122669.0), -133317.00, "")

    def test0389(self):
        self.assertEquals(self.calculate(4344, -179212.0), -174868.00, "")

    def test0390(self):
        self.assertEquals(self.calculate(-18844, -177224.0), -196068.00, "")

    def test0391(self):
        self.assertEquals(self.calculate(-6108, 53568.0), 47460.00, "")

    def test0392(self):
        self.assertEquals(self.calculate(15018, -63256.0), -48238.00, "")

    def test0393(self):
        self.assertEquals(self.calculate(5708, -16534.0), -10826.00, "")

    def test0394(self):
        self.assertEquals(self.calculate(6122, 79661.0), 85783.00, "")

    def test0395(self):
        self.assertEquals(self.calculate(-30450, -72602.0), -103052.00, "")

    def test0396(self):
        self.assertEquals(self.calculate(20780, 131051.0), 151831.00, "")

    def test0397(self):
        self.assertEquals(self.calculate(13344, -20097.0), -6753.00, "")

    def test0398(self):
        self.assertEquals(self.calculate(15816, -28318.0), -12502.00, "")

    def test0399(self):
        self.assertEquals(self.calculate(28802, 186022.0), 214824.00, "")

    def test0400(self):
        self.assertEquals(self.calculate(3298, 62086.0), 65384.00, "")

    def test0401(self):
        self.assertEquals(self.calculate(23261, 128592.0), 151853.00, "")

    def test0402(self):
        self.assertEquals(self.calculate(-20300, -34765.0), -55065.00, "")

    def test0403(self):
        self.assertEquals(self.calculate(6944, 84291.0), 91235.00, "")

    def test0404(self):
        self.assertEquals(self.calculate(-20407, -100710.0), -121117.00, "")

    def test0405(self):
        self.assertEquals(self.calculate(8317, 134810.0), 143127.00, "")

    def test0406(self):
        self.assertEquals(self.calculate(-7505, 54230.0), 46725.00, "")

    def test0407(self):
        self.assertEquals(self.calculate(-31726, -100107.0), -131833.00, "")

    def test0408(self):
        self.assertEquals(self.calculate(32413, 23465.0), 55878.00, "")

    def test0409(self):
        self.assertEquals(self.calculate(-18278, 121303.0), 103025.00, "")

    def test0410(self):
        self.assertEquals(self.calculate(-22251, 84907.0), 62656.00, "")

    def test0411(self):
        self.assertEquals(self.calculate(-9582, 143026.0), 133444.00, "")

    def test0412(self):
        self.assertEquals(self.calculate(822, 125562.0), 126384.00, "")

    def test0413(self):
        self.assertEquals(self.calculate(-13508, 165841.0), 152333.00, "")

    def test0414(self):
        self.assertEquals(self.calculate(-11404, -72967.0), -84371.00, "")

    def test0415(self):
        self.assertEquals(self.calculate(-11952, 18343.0), 6391.00, "")

    def test0416(self):
        self.assertEquals(self.calculate(6018, -161732.0), -155714.00, "")

    def test0417(self):
        self.assertEquals(self.calculate(-31855, -84392.0), -116247.00, "")

    def test0418(self):
        self.assertEquals(self.calculate(26740, 115375.0), 142115.00, "")

    def test0419(self):
        self.assertEquals(self.calculate(-13852, 120800.0), 106948.00, "")

    def test0420(self):
        self.assertEquals(self.calculate(-12567, 148090.0), 135523.00, "")

    def test0421(self):
        self.assertEquals(self.calculate(-7390, 27054.0), 19664.00, "")

    def test0422(self):
        self.assertEquals(self.calculate(20468, 34624.0), 55092.00, "")

    def test0423(self):
        self.assertEquals(self.calculate(22148, -46527.0), -24379.00, "")

    def test0424(self):
        self.assertEquals(self.calculate(20666, 82605.0), 103271.00, "")

    def test0425(self):
        self.assertEquals(self.calculate(18897, 162734.0), 181631.00, "")

    def test0426(self):
        self.assertEquals(self.calculate(-24530, -199191.0), -223721.00, "")

    def test0427(self):
        self.assertEquals(self.calculate(-7847, -14334.0), -22181.00, "")

    def test0428(self):
        self.assertEquals(self.calculate(-31192, -101973.0), -133165.00, "")

    def test0429(self):
        self.assertEquals(self.calculate(-19972, 48026.0), 28054.00, "")

    def test0430(self):
        self.assertEquals(self.calculate(-13979, -62478.0), -76457.00, "")

    def test0431(self):
        self.assertEquals(self.calculate(23489, 99745.0), 123234.00, "")

    def test0432(self):
        self.assertEquals(self.calculate(-268, -12445.0), -12713.00, "")

    def test0433(self):
        self.assertEquals(self.calculate(-8349, -170453.0), -178802.00, "")

    def test0434(self):
        self.assertEquals(self.calculate(32578, -79490.0), -46912.00, "")

    def test0435(self):
        self.assertEquals(self.calculate(-9090, -189951.0), -199041.00, "")

    def test0436(self):
        self.assertEquals(self.calculate(-12261, -147560.0), -159821.00, "")

    def test0437(self):
        self.assertEquals(self.calculate(-16721, -100969.0), -117690.00, "")

    def test0438(self):
        self.assertEquals(self.calculate(-13435, 140899.0), 127464.00, "")

    def test0439(self):
        self.assertEquals(self.calculate(30186, -85299.0), -55113.00, "")

    def test0440(self):
        self.assertEquals(self.calculate(68, 9527.0), 9595.00, "")

    def test0441(self):
        self.assertEquals(self.calculate(-19803, 47229.0), 27426.00, "")

    def test0442(self):
        self.assertEquals(self.calculate(-17250, -194541.0), -211791.00, "")

    def test0443(self):
        self.assertEquals(self.calculate(10517, 13274.0), 23791.00, "")

    def test0444(self):
        self.assertEquals(self.calculate(-12426, 94493.0), 82067.00, "")

    def test0445(self):
        self.assertEquals(self.calculate(30470, -101800.0), -71330.00, "")

    def test0446(self):
        self.assertEquals(self.calculate(-22788, -195497.0), -218285.00, "")

    def test0447(self):
        self.assertEquals(self.calculate(32335, -48972.0), -16637.00, "")

    def test0448(self):
        self.assertEquals(self.calculate(-18795, -50864.0), -69659.00, "")

    def test0449(self):
        self.assertEquals(self.calculate(-13200, -156123.0), -169323.00, "")

    def test0450(self):
        self.assertEquals(self.calculate(-26887, 126687.0), 99800.00, "")

    def test0451(self):
        self.assertEquals(self.calculate(-31506, 57584.0), 26078.00, "")

    def test0452(self):
        self.assertEquals(self.calculate(-20757, 145427.0), 124670.00, "")

    def test0453(self):
        self.assertEquals(self.calculate(6815, -171233.0), -164418.00, "")

    def test0454(self):
        self.assertEquals(self.calculate(-18921, 9737.0), -9184.00, "")

    def test0455(self):
        self.assertEquals(self.calculate(14983, 95617.0), 110600.00, "")

    def test0456(self):
        self.assertEquals(self.calculate(27514, 54066.0), 81580.00, "")

    def test0457(self):
        self.assertEquals(self.calculate(1550, 85755.0), 87305.00, "")

    def test0458(self):
        self.assertEquals(self.calculate(899, -156976.0), -156077.00, "")

    def test0459(self):
        self.assertEquals(self.calculate(-22480, -154105.0), -176585.00, "")

    def test0460(self):
        self.assertEquals(self.calculate(-21852, 199110.0), 177258.00, "")

    def test0461(self):
        self.assertEquals(self.calculate(-1206, 80762.0), 79556.00, "")

    def test0462(self):
        self.assertEquals(self.calculate(12233, 85679.0), 97912.00, "")

    def test0463(self):
        self.assertEquals(self.calculate(-9491, 177557.0), 168066.00, "")

    def test0464(self):
        self.assertEquals(self.calculate(32222, 161445.0), 193667.00, "")

    def test0465(self):
        self.assertEquals(self.calculate(-20753, 23903.0), 3150.00, "")

    def test0466(self):
        self.assertEquals(self.calculate(14057, 94233.0), 108290.00, "")

    def test0467(self):
        self.assertEquals(self.calculate(18528, -197927.0), -179399.00, "")

    def test0468(self):
        self.assertEquals(self.calculate(21051, 127236.0), 148287.00, "")

    def test0469(self):
        self.assertEquals(self.calculate(-6763, 2052.0), -4711.00, "")

    def test0470(self):
        self.assertEquals(self.calculate(7658, 13651.0), 21309.00, "")

    def test0471(self):
        self.assertEquals(self.calculate(-23170, -96648.0), -119818.00, "")

    def test0472(self):
        self.assertEquals(self.calculate(-20719, -100172.0), -120891.00, "")

    def test0473(self):
        self.assertEquals(self.calculate(3692, 72862.0), 76554.00, "")

    def test0474(self):
        self.assertEquals(self.calculate(19573, -147380.0), -127807.00, "")

    def test0475(self):
        self.assertEquals(self.calculate(-9157, 54886.0), 45729.00, "")

    def test0476(self):
        self.assertEquals(self.calculate(26529, 186754.0), 213283.00, "")

    def test0477(self):
        self.assertEquals(self.calculate(21613, -76760.0), -55147.00, "")

    def test0478(self):
        self.assertEquals(self.calculate(-17407, 144995.0), 127588.00, "")

    def test0479(self):
        self.assertEquals(self.calculate(13338, -63582.0), -50244.00, "")

    def test0480(self):
        self.assertEquals(self.calculate(12871, 169706.0), 182577.00, "")

    def test0481(self):
        self.assertEquals(self.calculate(-21698, 176441.0), 154743.00, "")

    def test0482(self):
        self.assertEquals(self.calculate(-8745, 119759.0), 111014.00, "")

    def test0483(self):
        self.assertEquals(self.calculate(-6376, 168266.0), 161890.00, "")

    def test0484(self):
        self.assertEquals(self.calculate(28709, -66608.0), -37899.00, "")

    def test0485(self):
        self.assertEquals(self.calculate(25620, -53507.0), -27887.00, "")

    def test0486(self):
        self.assertEquals(self.calculate(15728, 197882.0), 213610.00, "")

    def test0487(self):
        self.assertEquals(self.calculate(-15704, -187160.0), -202864.00, "")

    def test0488(self):
        self.assertEquals(self.calculate(9962, -176427.0), -166465.00, "")

    def test0489(self):
        self.assertEquals(self.calculate(14623, 117056.0), 131679.00, "")

    def test0490(self):
        self.assertEquals(self.calculate(27983, 53413.0), 81396.00, "")

    def test0491(self):
        self.assertEquals(self.calculate(13343, 91877.0), 105220.00, "")

    def test0492(self):
        self.assertEquals(self.calculate(27508, 125526.0), 153034.00, "")

    def test0493(self):
        self.assertEquals(self.calculate(6312, 64122.0), 70434.00, "")

    def test0494(self):
        self.assertEquals(self.calculate(32409, -118949.0), -86540.00, "")

    def test0495(self):
        self.assertEquals(self.calculate(-24116, -180275.0), -204391.00, "")

    def test0496(self):
        self.assertEquals(self.calculate(-27655, 41613.0), 13958.00, "")

    def test0497(self):
        self.assertEquals(self.calculate(-17296, -25739.0), -43035.00, "")

    def test0498(self):
        self.assertEquals(self.calculate(32028, -127411.0), -95383.00, "")

    def test0499(self):
        self.assertEquals(self.calculate(28035, 148782.0), 176817.00, "")

    def test0500(self):
        self.assertEquals(self.calculate(-9751, -35042.0), -44793.00, "")

    def test0501(self):
        self.assertEquals(self.calculate(2420, -143472.0), -141052.00, "")

    def test0502(self):
        self.assertEquals(self.calculate(-24820, 39367.0), 14547.00, "")

    def test0503(self):
        self.assertEquals(self.calculate(517, 175917.0), 176434.00, "")

    def test0504(self):
        self.assertEquals(self.calculate(-13214, -119090.0), -132304.00, "")

    def test0505(self):
        self.assertEquals(self.calculate(5869, -115436.0), -109567.00, "")

    def test0506(self):
        self.assertEquals(self.calculate(-13213, 84925.0), 71712.00, "")

    def test0507(self):
        self.assertEquals(self.calculate(27311, 10685.0), 37996.00, "")

    def test0508(self):
        self.assertEquals(self.calculate(-30722, 45347.0), 14625.00, "")

    def test0509(self):
        self.assertEquals(self.calculate(12334, -98051.0), -85717.00, "")

    def test0510(self):
        self.assertEquals(self.calculate(-20516, -42726.0), -63242.00, "")

    def test0511(self):
        self.assertEquals(self.calculate(-24866, -40084.0), -64950.00, "")

    def test0512(self):
        self.assertEquals(self.calculate(-9472, 67008.0), 57536.00, "")

    def test0513(self):
        self.assertEquals(self.calculate(9912, -139197.0), -129285.00, "")

    def test0514(self):
        self.assertEquals(self.calculate(192, -192625.0), -192433.00, "")

    def test0515(self):
        self.assertEquals(self.calculate(17574, -119773.0), -102199.00, "")

    def test0516(self):
        self.assertEquals(self.calculate(16049, 113917.0), 129966.00, "")

    def test0517(self):
        self.assertEquals(self.calculate(-2036, 148924.0), 146888.00, "")

    def test0518(self):
        self.assertEquals(self.calculate(-3210, -77764.0), -80974.00, "")

    def test0519(self):
        self.assertEquals(self.calculate(6879, -127306.0), -120427.00, "")

    def test0520(self):
        self.assertEquals(self.calculate(27838, 127945.0), 155783.00, "")

    def test0521(self):
        self.assertEquals(self.calculate(9175, 185539.0), 194714.00, "")

    def test0522(self):
        self.assertEquals(self.calculate(32526, 147365.0), 179891.00, "")

    def test0523(self):
        self.assertEquals(self.calculate(11591, -85833.0), -74242.00, "")

    def test0524(self):
        self.assertEquals(self.calculate(23802, 73720.0), 97522.00, "")

    def test0525(self):
        self.assertEquals(self.calculate(15326, 110629.0), 125955.00, "")

    def test0526(self):
        self.assertEquals(self.calculate(-13834, 199079.0), 185245.00, "")

    def test0527(self):
        self.assertEquals(self.calculate(7539, -29391.0), -21852.00, "")

    def test0528(self):
        self.assertEquals(self.calculate(4647, -47111.0), -42464.00, "")

    def test0529(self):
        self.assertEquals(self.calculate(-22779, 100264.0), 77485.00, "")

    def test0530(self):
        self.assertEquals(self.calculate(-29545, -9015.0), -38560.00, "")

    def test0531(self):
        self.assertEquals(self.calculate(7012, -180043.0), -173031.00, "")

    def test0532(self):
        self.assertEquals(self.calculate(28208, -113347.0), -85139.00, "")

    def test0533(self):
        self.assertEquals(self.calculate(8465, 187752.0), 196217.00, "")

    def test0534(self):
        self.assertEquals(self.calculate(-28840, 82829.0), 53989.00, "")

    def test0535(self):
        self.assertEquals(self.calculate(-15698, 67230.0), 51532.00, "")

    def test0536(self):
        self.assertEquals(self.calculate(28958, -67282.0), -38324.00, "")

    def test0537(self):
        self.assertEquals(self.calculate(-3260, -63514.0), -66774.00, "")

    def test0538(self):
        self.assertEquals(self.calculate(26143, 102940.0), 129083.00, "")

    def test0539(self):
        self.assertEquals(self.calculate(-10896, -95158.0), -106054.00, "")

    def test0540(self):
        self.assertEquals(self.calculate(-10771, -151485.0), -162256.00, "")

    def test0541(self):
        self.assertEquals(self.calculate(12575, -162646.0), -150071.00, "")

    def test0542(self):
        self.assertEquals(self.calculate(-20626, 45398.0), 24772.00, "")

    def test0543(self):
        self.assertEquals(self.calculate(-530, 136775.0), 136245.00, "")

    def test0544(self):
        self.assertEquals(self.calculate(-3872, -118287.0), -122159.00, "")

    def test0545(self):
        self.assertEquals(self.calculate(9386, 80091.0), 89477.00, "")

    def test0546(self):
        self.assertEquals(self.calculate(-28673, -54418.0), -83091.00, "")

    def test0547(self):
        self.assertEquals(self.calculate(-467, -112826.0), -113293.00, "")

    def test0548(self):
        self.assertEquals(self.calculate(114, -147599.0), -147485.00, "")

    def test0549(self):
        self.assertEquals(self.calculate(6228, -158806.0), -152578.00, "")

    def test0550(self):
        self.assertEquals(self.calculate(-31864, 45985.0), 14121.00, "")

    def test0551(self):
        self.assertEquals(self.calculate(30881, 21963.0), 52844.00, "")

    def test0552(self):
        self.assertEquals(self.calculate(19414, 129537.0), 148951.00, "")

    def test0553(self):
        self.assertEquals(self.calculate(30669, 46568.0), 77237.00, "")

    def test0554(self):
        self.assertEquals(self.calculate(8073, 74935.0), 83008.00, "")

    def test0555(self):
        self.assertEquals(self.calculate(12689, 184124.0), 196813.00, "")

    def test0556(self):
        self.assertEquals(self.calculate(-2511, -94580.0), -97091.00, "")

    def test0557(self):
        self.assertEquals(self.calculate(16428, -155571.0), -139143.00, "")

    def test0558(self):
        self.assertEquals(self.calculate(-24342, 45128.0), 20786.00, "")

    def test0559(self):
        self.assertEquals(self.calculate(20647, -195548.0), -174901.00, "")

    def test0560(self):
        self.assertEquals(self.calculate(-18871, -70785.0), -89656.00, "")

    def test0561(self):
        self.assertEquals(self.calculate(11756, 48428.0), 60184.00, "")

    def test0562(self):
        self.assertEquals(self.calculate(13201, 116481.0), 129682.00, "")

    def test0563(self):
        self.assertEquals(self.calculate(8494, -88816.0), -80322.00, "")

    def test0564(self):
        self.assertEquals(self.calculate(7625, 126684.0), 134309.00, "")

    def test0565(self):
        self.assertEquals(self.calculate(13735, -94298.0), -80563.00, "")

    def test0566(self):
        self.assertEquals(self.calculate(-24451, -111922.0), -136373.00, "")

    def test0567(self):
        self.assertEquals(self.calculate(14304, 135829.0), 150133.00, "")

    def test0568(self):
        self.assertEquals(self.calculate(469, 137132.0), 137601.00, "")

    def test0569(self):
        self.assertEquals(self.calculate(-2231, 89160.0), 86929.00, "")

    def test0570(self):
        self.assertEquals(self.calculate(18071, 11416.0), 29487.00, "")

    def test0571(self):
        self.assertEquals(self.calculate(-19700, 30320.0), 10620.00, "")

    def test0572(self):
        self.assertEquals(self.calculate(-12847, -149051.0), -161898.00, "")

    def test0573(self):
        self.assertEquals(self.calculate(6474, -35163.0), -28689.00, "")

    def test0574(self):
        self.assertEquals(self.calculate(-28844, 57210.0), 28366.00, "")

    def test0575(self):
        self.assertEquals(self.calculate(-9122, -111069.0), -120191.00, "")

    def test0576(self):
        self.assertEquals(self.calculate(-6754, -6457.0), -13211.00, "")

    def test0577(self):
        self.assertEquals(self.calculate(-27669, -79105.0), -106774.00, "")

    def test0578(self):
        self.assertEquals(self.calculate(2075, 7213.0), 9288.00, "")

    def test0579(self):
        self.assertEquals(self.calculate(-25541, 1741.0), -23800.00, "")

    def test0580(self):
        self.assertEquals(self.calculate(16150, -61617.0), -45467.00, "")

    def test0581(self):
        self.assertEquals(self.calculate(-22801, 132994.0), 110193.00, "")

    def test0582(self):
        self.assertEquals(self.calculate(-1988, -16433.0), -18421.00, "")

    def test0583(self):
        self.assertEquals(self.calculate(-25725, -3783.0), -29508.00, "")

    def test0584(self):
        self.assertEquals(self.calculate(29267, -132550.0), -103283.00, "")

    def test0585(self):
        self.assertEquals(self.calculate(25805, 157155.0), 182960.00, "")

    def test0586(self):
        self.assertEquals(self.calculate(-22856, -37779.0), -60635.00, "")

    def test0587(self):
        self.assertEquals(self.calculate(-27338, -75513.0), -102851.00, "")

    def test0588(self):
        self.assertEquals(self.calculate(31916, 75195.0), 107111.00, "")

    def test0589(self):
        self.assertEquals(self.calculate(12834, 86296.0), 99130.00, "")

    def test0590(self):
        self.assertEquals(self.calculate(-10210, 12238.0), 2028.00, "")

    def test0591(self):
        self.assertEquals(self.calculate(-10372, -118975.0), -129347.00, "")

    def test0592(self):
        self.assertEquals(self.calculate(-16396, 148289.0), 131893.00, "")

    def test0593(self):
        self.assertEquals(self.calculate(-25092, 169611.0), 144519.00, "")

    def test0594(self):
        self.assertEquals(self.calculate(-27407, 14993.0), -12414.00, "")

    def test0595(self):
        self.assertEquals(self.calculate(16154, -121390.0), -105236.00, "")

    def test0596(self):
        self.assertEquals(self.calculate(-3614, -163624.0), -167238.00, "")

    def test0597(self):
        self.assertEquals(self.calculate(8630, 112422.0), 121052.00, "")

    def test0598(self):
        self.assertEquals(self.calculate(-7718, -100645.0), -108363.00, "")

    def test0599(self):
        self.assertEquals(self.calculate(16989, 140380.0), 157369.00, "")

    def test0600(self):
        self.assertEquals(self.calculate(25925, 171331.0), 197256.00, "")

    def test0601(self):
        self.assertEquals(self.calculate(-27038, 83331.0), 56293.00, "")

    def test0602(self):
        self.assertEquals(self.calculate(20099, -156199.0), -136100.00, "")

    def test0603(self):
        self.assertEquals(self.calculate(-155, 133322.0), 133167.00, "")

    def test0604(self):
        self.assertEquals(self.calculate(19868, 197968.0), 217836.00, "")

    def test0605(self):
        self.assertEquals(self.calculate(-25376, -97988.0), -123364.00, "")

    def test0606(self):
        self.assertEquals(self.calculate(3273, 101386.0), 104659.00, "")

    def test0607(self):
        self.assertEquals(self.calculate(-19434, -152431.0), -171865.00, "")

    def test0608(self):
        self.assertEquals(self.calculate(-15399, 180904.0), 165505.00, "")

    def test0609(self):
        self.assertEquals(self.calculate(5487, -6157.0), -670.00, "")

    def test0610(self):
        self.assertEquals(self.calculate(31455, 19599.0), 51054.00, "")

    def test0611(self):
        self.assertEquals(self.calculate(5916, -60235.0), -54319.00, "")

    def test0612(self):
        self.assertEquals(self.calculate(-17877, 131835.0), 113958.00, "")

    def test0613(self):
        self.assertEquals(self.calculate(2514, -47539.0), -45025.00, "")

    def test0614(self):
        self.assertEquals(self.calculate(29308, -88481.0), -59173.00, "")

    def test0615(self):
        self.assertEquals(self.calculate(17508, 16003.0), 33511.00, "")

    def test0616(self):
        self.assertEquals(self.calculate(18270, 106689.0), 124959.00, "")

    def test0617(self):
        self.assertEquals(self.calculate(17909, 15635.0), 33544.00, "")

    def test0618(self):
        self.assertEquals(self.calculate(23074, 192461.0), 215535.00, "")

    def test0619(self):
        self.assertEquals(self.calculate(1357, -144134.0), -142777.00, "")

    def test0620(self):
        self.assertEquals(self.calculate(-30249, 30639.0), 390.00, "")

    def test0621(self):
        self.assertEquals(self.calculate(-20093, 35419.0), 15326.00, "")

    def test0622(self):
        self.assertEquals(self.calculate(2115, -169255.0), -167140.00, "")

    def test0623(self):
        self.assertEquals(self.calculate(7392, 86410.0), 93802.00, "")

    def test0624(self):
        self.assertEquals(self.calculate(-13425, 54657.0), 41232.00, "")

    def test0625(self):
        self.assertEquals(self.calculate(18995, -146096.0), -127101.00, "")

    def test0626(self):
        self.assertEquals(self.calculate(-14865, -32314.0), -47179.00, "")

    def test0627(self):
        self.assertEquals(self.calculate(15364, 68673.0), 84037.00, "")

    def test0628(self):
        self.assertEquals(self.calculate(-19531, -133688.0), -153219.00, "")

    def test0629(self):
        self.assertEquals(self.calculate(-17668, -113532.0), -131200.00, "")

    def test0630(self):
        self.assertEquals(self.calculate(-25509, -135703.0), -161212.00, "")

    def test0631(self):
        self.assertEquals(self.calculate(-22808, -52690.0), -75498.00, "")

    def test0632(self):
        self.assertEquals(self.calculate(28169, -172297.0), -144128.00, "")

    def test0633(self):
        self.assertEquals(self.calculate(11270, -77374.0), -66104.00, "")

    def test0634(self):
        self.assertEquals(self.calculate(-20256, 186421.0), 166165.00, "")

    def test0635(self):
        self.assertEquals(self.calculate(27977, 72184.0), 100161.00, "")

    def test0636(self):
        self.assertEquals(self.calculate(24127, 48394.0), 72521.00, "")

    def test0637(self):
        self.assertEquals(self.calculate(9614, 92087.0), 101701.00, "")

    def test0638(self):
        self.assertEquals(self.calculate(24036, 110150.0), 134186.00, "")

    def test0639(self):
        self.assertEquals(self.calculate(-380, 105294.0), 104914.00, "")

    def test0640(self):
        self.assertEquals(self.calculate(-2900, -128633.0), -131533.00, "")

    def test0641(self):
        self.assertEquals(self.calculate(4709, 128258.0), 132967.00, "")

    def test0642(self):
        self.assertEquals(self.calculate(-12759, -113043.0), -125802.00, "")

    def test0643(self):
        self.assertEquals(self.calculate(28274, 143248.0), 171522.00, "")

    def test0644(self):
        self.assertEquals(self.calculate(19163, -196222.0), -177059.00, "")

    def test0645(self):
        self.assertEquals(self.calculate(-10111, -134547.0), -144658.00, "")

    def test0646(self):
        self.assertEquals(self.calculate(16399, 87026.0), 103425.00, "")

    def test0647(self):
        self.assertEquals(self.calculate(-5888, -150240.0), -156128.00, "")

    def test0648(self):
        self.assertEquals(self.calculate(-9640, -27498.0), -37138.00, "")

    def test0649(self):
        self.assertEquals(self.calculate(28597, -86665.0), -58068.00, "")

    def test0650(self):
        self.assertEquals(self.calculate(22347, -38128.0), -15781.00, "")

    def test0651(self):
        self.assertEquals(self.calculate(-22815, -145505.0), -168320.00, "")

    def test0652(self):
        self.assertEquals(self.calculate(-13915, 152270.0), 138355.00, "")

    def test0653(self):
        self.assertEquals(self.calculate(4559, 95533.0), 100092.00, "")

    def test0654(self):
        self.assertEquals(self.calculate(-26198, -55919.0), -82117.00, "")

    def test0655(self):
        self.assertEquals(self.calculate(-15717, -23587.0), -39304.00, "")

    def test0656(self):
        self.assertEquals(self.calculate(8640, -71057.0), -62417.00, "")

    def test0657(self):
        self.assertEquals(self.calculate(-2779, -23837.0), -26616.00, "")

    def test0658(self):
        self.assertEquals(self.calculate(3019, 149079.0), 152098.00, "")

    def test0659(self):
        self.assertEquals(self.calculate(12050, -154417.0), -142367.00, "")

    def test0660(self):
        self.assertEquals(self.calculate(-31385, 87299.0), 55914.00, "")

    def test0661(self):
        self.assertEquals(self.calculate(2554, -16052.0), -13498.00, "")

    def test0662(self):
        self.assertEquals(self.calculate(30490, -37764.0), -7274.00, "")

    def test0663(self):
        self.assertEquals(self.calculate(15843, -110824.0), -94981.00, "")

    def test0664(self):
        self.assertEquals(self.calculate(381, -184713.0), -184332.00, "")

    def test0665(self):
        self.assertEquals(self.calculate(27539, 121446.0), 148985.00, "")

    def test0666(self):
        self.assertEquals(self.calculate(-20996, 54005.0), 33009.00, "")

    def test0667(self):
        self.assertEquals(self.calculate(-28000, 85068.0), 57068.00, "")

    def test0668(self):
        self.assertEquals(self.calculate(16491, 43046.0), 59537.00, "")

    def test0669(self):
        self.assertEquals(self.calculate(10472, -103093.0), -92621.00, "")

    def test0670(self):
        self.assertEquals(self.calculate(590, 87757.0), 88347.00, "")

    def test0671(self):
        self.assertEquals(self.calculate(26967, -95615.0), -68648.00, "")

    def test0672(self):
        self.assertEquals(self.calculate(32014, 158400.0), 190414.00, "")

    def test0673(self):
        self.assertEquals(self.calculate(-15182, -32967.0), -48149.00, "")

    def test0674(self):
        self.assertEquals(self.calculate(-10182, 146122.0), 135940.00, "")

    def test0675(self):
        self.assertEquals(self.calculate(-8503, 150237.0), 141734.00, "")

    def test0676(self):
        self.assertEquals(self.calculate(-24161, -53035.0), -77196.00, "")

    def test0677(self):
        self.assertEquals(self.calculate(14835, -13056.0), 1779.00, "")

    def test0678(self):
        self.assertEquals(self.calculate(-22672, 166695.0), 144023.00, "")

    def test0679(self):
        self.assertEquals(self.calculate(-27858, 123483.0), 95625.00, "")

    def test0680(self):
        self.assertEquals(self.calculate(28212, -144992.0), -116780.00, "")

    def test0681(self):
        self.assertEquals(self.calculate(-32347, -147739.0), -180086.00, "")

    def test0682(self):
        self.assertEquals(self.calculate(453, 96963.0), 97416.00, "")

    def test0683(self):
        self.assertEquals(self.calculate(22030, 74307.0), 96337.00, "")

    def test0684(self):
        self.assertEquals(self.calculate(-21106, 92542.0), 71436.00, "")

    def test0685(self):
        self.assertEquals(self.calculate(-9040, 165698.0), 156658.00, "")

    def test0686(self):
        self.assertEquals(self.calculate(-30219, -22931.0), -53150.00, "")

    def test0687(self):
        self.assertEquals(self.calculate(16744, 189402.0), 206146.00, "")

    def test0688(self):
        self.assertEquals(self.calculate(-20248, 143587.0), 123339.00, "")

    def test0689(self):
        self.assertEquals(self.calculate(-22025, 67580.0), 45555.00, "")

    def test0690(self):
        self.assertEquals(self.calculate(-7478, 144517.0), 137039.00, "")

    def test0691(self):
        self.assertEquals(self.calculate(4708, -100709.0), -96001.00, "")

    def test0692(self):
        self.assertEquals(self.calculate(12126, -140189.0), -128063.00, "")

    def test0693(self):
        self.assertEquals(self.calculate(25971, -146882.0), -120911.00, "")

    def test0694(self):
        self.assertEquals(self.calculate(20637, 144136.0), 164773.00, "")

    def test0695(self):
        self.assertEquals(self.calculate(4468, 74686.0), 79154.00, "")

    def test0696(self):
        self.assertEquals(self.calculate(7805, 25045.0), 32850.00, "")

    def test0697(self):
        self.assertEquals(self.calculate(4657, 107314.0), 111971.00, "")

    def test0698(self):
        self.assertEquals(self.calculate(23673, 35591.0), 59264.00, "")

    def test0699(self):
        self.assertEquals(self.calculate(8092, -111891.0), -103799.00, "")

    def test0700(self):
        self.assertEquals(self.calculate(-22350, 162463.0), 140113.00, "")

    def test0701(self):
        self.assertEquals(self.calculate(8508, 19448.0), 27956.00, "")

    def test0702(self):
        self.assertEquals(self.calculate(11251, -84302.0), -73051.00, "")

    def test0703(self):
        self.assertEquals(self.calculate(7965, -72302.0), -64337.00, "")

    def test0704(self):
        self.assertEquals(self.calculate(9297, -96104.0), -86807.00, "")

    def test0705(self):
        self.assertEquals(self.calculate(-12432, 198747.0), 186315.00, "")

    def test0706(self):
        self.assertEquals(self.calculate(-16645, 122614.0), 105969.00, "")

    def test0707(self):
        self.assertEquals(self.calculate(-17631, -96512.0), -114143.00, "")

    def test0708(self):
        self.assertEquals(self.calculate(7380, 143766.0), 151146.00, "")

    def test0709(self):
        self.assertEquals(self.calculate(6763, 87708.0), 94471.00, "")

    def test0710(self):
        self.assertEquals(self.calculate(29916, 178353.0), 208269.00, "")

    def test0711(self):
        self.assertEquals(self.calculate(3609, -39691.0), -36082.00, "")

    def test0712(self):
        self.assertEquals(self.calculate(-9490, 94577.0), 85087.00, "")

    def test0713(self):
        self.assertEquals(self.calculate(16737, -128695.0), -111958.00, "")

    def test0714(self):
        self.assertEquals(self.calculate(-30902, 10179.0), -20723.00, "")

    def test0715(self):
        self.assertEquals(self.calculate(-32247, 122453.0), 90206.00, "")

    def test0716(self):
        self.assertEquals(self.calculate(26179, 136018.0), 162197.00, "")

    def test0717(self):
        self.assertEquals(self.calculate(12174, -53070.0), -40896.00, "")

    def test0718(self):
        self.assertEquals(self.calculate(-8249, -28636.0), -36885.00, "")

    def test0719(self):
        self.assertEquals(self.calculate(25661, 184378.0), 210039.00, "")

    def test0720(self):
        self.assertEquals(self.calculate(-12223, -61027.0), -73250.00, "")

    def test0721(self):
        self.assertEquals(self.calculate(-18218, -103957.0), -122175.00, "")

    def test0722(self):
        self.assertEquals(self.calculate(14860, 129579.0), 144439.00, "")

    def test0723(self):
        self.assertEquals(self.calculate(3042, 131437.0), 134479.00, "")

    def test0724(self):
        self.assertEquals(self.calculate(8338, 38162.0), 46500.00, "")

    def test0725(self):
        self.assertEquals(self.calculate(-10951, 20573.0), 9622.00, "")

    def test0726(self):
        self.assertEquals(self.calculate(8870, -111230.0), -102360.00, "")

    def test0727(self):
        self.assertEquals(self.calculate(32575, -193988.0), -161413.00, "")

    def test0728(self):
        self.assertEquals(self.calculate(-7266, 13071.0), 5805.00, "")

    def test0729(self):
        self.assertEquals(self.calculate(-23741, 40002.0), 16261.00, "")

    def test0730(self):
        self.assertEquals(self.calculate(16674, -114715.0), -98041.00, "")

    def test0731(self):
        self.assertEquals(self.calculate(5905, 101945.0), 107850.00, "")

    def test0732(self):
        self.assertEquals(self.calculate(-4798, 181761.0), 176963.00, "")

    def test0733(self):
        self.assertEquals(self.calculate(4905, 109807.0), 114712.00, "")

    def test0734(self):
        self.assertEquals(self.calculate(10670, 105490.0), 116160.00, "")

    def test0735(self):
        self.assertEquals(self.calculate(17332, -37051.0), -19719.00, "")

    def test0736(self):
        self.assertEquals(self.calculate(25206, 166649.0), 191855.00, "")

    def test0737(self):
        self.assertEquals(self.calculate(-12659, 12818.0), 159.00, "")

    def test0738(self):
        self.assertEquals(self.calculate(-30491, 12439.0), -18052.00, "")

    def test0739(self):
        self.assertEquals(self.calculate(29992, 166194.0), 196186.00, "")

    def test0740(self):
        self.assertEquals(self.calculate(-30303, -128376.0), -158679.00, "")

    def test0741(self):
        self.assertEquals(self.calculate(-1570, 172118.0), 170548.00, "")

    def test0742(self):
        self.assertEquals(self.calculate(-14497, -166755.0), -181252.00, "")

    def test0743(self):
        self.assertEquals(self.calculate(-24122, 178823.0), 154701.00, "")

    def test0744(self):
        self.assertEquals(self.calculate(-29669, 129148.0), 99479.00, "")

    def test0745(self):
        self.assertEquals(self.calculate(-23176, 100463.0), 77287.00, "")

    def test0746(self):
        self.assertEquals(self.calculate(-12439, 146104.0), 133665.00, "")

    def test0747(self):
        self.assertEquals(self.calculate(14239, 74715.0), 88954.00, "")

    def test0748(self):
        self.assertEquals(self.calculate(-29376, -180135.0), -209511.00, "")

    def test0749(self):
        self.assertEquals(self.calculate(-27626, 60922.0), 33296.00, "")

    def test0750(self):
        self.assertEquals(self.calculate(-46, -69167.0), -69213.00, "")

    def test0751(self):
        self.assertEquals(self.calculate(-23599, -57931.0), -81530.00, "")

    def test0752(self):
        self.assertEquals(self.calculate(8754, -102216.0), -93462.00, "")

    def test0753(self):
        self.assertEquals(self.calculate(6899, 179686.0), 186585.00, "")

    def test0754(self):
        self.assertEquals(self.calculate(-16266, 20743.0), 4477.00, "")

    def test0755(self):
        self.assertEquals(self.calculate(-11854, 160530.0), 148676.00, "")

    def test0756(self):
        self.assertEquals(self.calculate(14167, -12541.0), 1626.00, "")

    def test0757(self):
        self.assertEquals(self.calculate(3389, 6564.0), 9953.00, "")

    def test0758(self):
        self.assertEquals(self.calculate(-5449, -71464.0), -76913.00, "")

    def test0759(self):
        self.assertEquals(self.calculate(-23546, -143898.0), -167444.00, "")

    def test0760(self):
        self.assertEquals(self.calculate(-25560, -62407.0), -87967.00, "")

    def test0761(self):
        self.assertEquals(self.calculate(-28188, 188469.0), 160281.00, "")

    def test0762(self):
        self.assertEquals(self.calculate(-188, 136984.0), 136796.00, "")

    def test0763(self):
        self.assertEquals(self.calculate(-19027, 196898.0), 177871.00, "")

    def test0764(self):
        self.assertEquals(self.calculate(-28368, -12795.0), -41163.00, "")

    def test0765(self):
        self.assertEquals(self.calculate(23861, -125633.0), -101772.00, "")

    def test0766(self):
        self.assertEquals(self.calculate(22537, 165498.0), 188035.00, "")

    def test0767(self):
        self.assertEquals(self.calculate(-13675, -178983.0), -192658.00, "")

    def test0768(self):
        self.assertEquals(self.calculate(-19778, -144571.0), -164349.00, "")

    def test0769(self):
        self.assertEquals(self.calculate(-17394, 97567.0), 80173.00, "")

    def test0770(self):
        self.assertEquals(self.calculate(12526, 188567.0), 201093.00, "")

    def test0771(self):
        self.assertEquals(self.calculate(25910, -193662.0), -167752.00, "")

    def test0772(self):
        self.assertEquals(self.calculate(31390, 88361.0), 119751.00, "")

    def test0773(self):
        self.assertEquals(self.calculate(13514, 117255.0), 130769.00, "")

    def test0774(self):
        self.assertEquals(self.calculate(6055, 83487.0), 89542.00, "")

    def test0775(self):
        self.assertEquals(self.calculate(-26150, -198778.0), -224928.00, "")

    def test0776(self):
        self.assertEquals(self.calculate(-488, -6726.0), -7214.00, "")

    def test0777(self):
        self.assertEquals(self.calculate(-30543, -179322.0), -209865.00, "")

    def test0778(self):
        self.assertEquals(self.calculate(3541, -142517.0), -138976.00, "")

    def test0779(self):
        self.assertEquals(self.calculate(-24055, -170462.0), -194517.00, "")

    def test0780(self):
        self.assertEquals(self.calculate(16894, 111899.0), 128793.00, "")

    def test0781(self):
        self.assertEquals(self.calculate(2859, -84978.0), -82119.00, "")

    def test0782(self):
        self.assertEquals(self.calculate(20884, 29704.0), 50588.00, "")

    def test0783(self):
        self.assertEquals(self.calculate(-13335, 32935.0), 19600.00, "")

    def test0784(self):
        self.assertEquals(self.calculate(-23707, 149919.0), 126212.00, "")

    def test0785(self):
        self.assertEquals(self.calculate(28957, 67225.0), 96182.00, "")

    def test0786(self):
        self.assertEquals(self.calculate(18982, -137471.0), -118489.00, "")

    def test0787(self):
        self.assertEquals(self.calculate(-13489, 121160.0), 107671.00, "")

    def test0788(self):
        self.assertEquals(self.calculate(6293, 150905.0), 157198.00, "")

    def test0789(self):
        self.assertEquals(self.calculate(-9200, 42390.0), 33190.00, "")

    def test0790(self):
        self.assertEquals(self.calculate(27662, 126470.0), 154132.00, "")

    def test0791(self):
        self.assertEquals(self.calculate(-14583, -130175.0), -144758.00, "")

    def test0792(self):
        self.assertEquals(self.calculate(6201, 85103.0), 91304.00, "")

    def test0793(self):
        self.assertEquals(self.calculate(-10091, 76194.0), 66103.00, "")

    def test0794(self):
        self.assertEquals(self.calculate(-27681, -64271.0), -91952.00, "")

    def test0795(self):
        self.assertEquals(self.calculate(5633, 5038.0), 10671.00, "")

    def test0796(self):
        self.assertEquals(self.calculate(-6405, 27477.0), 21072.00, "")

    def test0797(self):
        self.assertEquals(self.calculate(-25596, -81537.0), -107133.00, "")

    def test0798(self):
        self.assertEquals(self.calculate(15695, -97602.0), -81907.00, "")

    def test0799(self):
        self.assertEquals(self.calculate(25136, -24030.0), 1106.00, "")

    def test0800(self):
        self.assertEquals(self.calculate(-502, -67477.0), -67979.00, "")

    def test0801(self):
        self.assertEquals(self.calculate(-29609, 94598.0), 64989.00, "")

    def test0802(self):
        self.assertEquals(self.calculate(11314, 150972.0), 162286.00, "")

    def test0803(self):
        self.assertEquals(self.calculate(30473, -38944.0), -8471.00, "")

    def test0804(self):
        self.assertEquals(self.calculate(11316, 78527.0), 89843.00, "")

    def test0805(self):
        self.assertEquals(self.calculate(29068, -135320.0), -106252.00, "")

    def test0806(self):
        self.assertEquals(self.calculate(-17280, 7442.0), -9838.00, "")

    def test0807(self):
        self.assertEquals(self.calculate(15912, -138752.0), -122840.00, "")

    def test0808(self):
        self.assertEquals(self.calculate(-14773, 188206.0), 173433.00, "")

    def test0809(self):
        self.assertEquals(self.calculate(-2026, -179447.0), -181473.00, "")

    def test0810(self):
        self.assertEquals(self.calculate(27042, -157853.0), -130811.00, "")

    def test0811(self):
        self.assertEquals(self.calculate(-16482, 161929.0), 145447.00, "")

    def test0812(self):
        self.assertEquals(self.calculate(-6697, -37622.0), -44319.00, "")

    def test0813(self):
        self.assertEquals(self.calculate(-17186, -119885.0), -137071.00, "")

    def test0814(self):
        self.assertEquals(self.calculate(9809, -2292.0), 7517.00, "")

    def test0815(self):
        self.assertEquals(self.calculate(-14296, 113665.0), 99369.00, "")

    def test0816(self):
        self.assertEquals(self.calculate(11359, -98991.0), -87632.00, "")

    def test0817(self):
        self.assertEquals(self.calculate(-24029, 45731.0), 21702.00, "")

    def test0818(self):
        self.assertEquals(self.calculate(25390, -14508.0), 10882.00, "")

    def test0819(self):
        self.assertEquals(self.calculate(18969, -24914.0), -5945.00, "")

    def test0820(self):
        self.assertEquals(self.calculate(-14425, -131538.0), -145963.00, "")

    def test0821(self):
        self.assertEquals(self.calculate(31117, -33129.0), -2012.00, "")

    def test0822(self):
        self.assertEquals(self.calculate(24444, 166256.0), 190700.00, "")

    def test0823(self):
        self.assertEquals(self.calculate(-25409, -186113.0), -211522.00, "")

    def test0824(self):
        self.assertEquals(self.calculate(850, 90893.0), 91743.00, "")

    def test0825(self):
        self.assertEquals(self.calculate(6522, 114354.0), 120876.00, "")

    def test0826(self):
        self.assertEquals(self.calculate(-9917, 111329.0), 101412.00, "")

    def test0827(self):
        self.assertEquals(self.calculate(-30747, 159293.0), 128546.00, "")

    def test0828(self):
        self.assertEquals(self.calculate(32369, 55580.0), 87949.00, "")

    def test0829(self):
        self.assertEquals(self.calculate(27612, -50317.0), -22705.00, "")

    def test0830(self):
        self.assertEquals(self.calculate(-23961, -24471.0), -48432.00, "")

    def test0831(self):
        self.assertEquals(self.calculate(14903, -117680.0), -102777.00, "")

    def test0832(self):
        self.assertEquals(self.calculate(-30915, 15610.0), -15305.00, "")

    def test0833(self):
        self.assertEquals(self.calculate(31937, -109477.0), -77540.00, "")

    def test0834(self):
        self.assertEquals(self.calculate(11412, -65259.0), -53847.00, "")

    def test0835(self):
        self.assertEquals(self.calculate(17283, 174064.0), 191347.00, "")

    def test0836(self):
        self.assertEquals(self.calculate(-23681, -20663.0), -44344.00, "")

    def test0837(self):
        self.assertEquals(self.calculate(29781, -150684.0), -120903.00, "")

    def test0838(self):
        self.assertEquals(self.calculate(13160, 191451.0), 204611.00, "")

    def test0839(self):
        self.assertEquals(self.calculate(-28241, -97024.0), -125265.00, "")

    def test0840(self):
        self.assertEquals(self.calculate(30726, -164244.0), -133518.00, "")

    def test0841(self):
        self.assertEquals(self.calculate(21368, 156190.0), 177558.00, "")

    def test0842(self):
        self.assertEquals(self.calculate(32525, -32439.0), 86.00, "")

    def test0843(self):
        self.assertEquals(self.calculate(30965, 123312.0), 154277.00, "")

    def test0844(self):
        self.assertEquals(self.calculate(1729, 63194.0), 64923.00, "")

    def test0845(self):
        self.assertEquals(self.calculate(-27539, -3693.0), -31232.00, "")

    def test0846(self):
        self.assertEquals(self.calculate(20281, 131055.0), 151336.00, "")

    def test0847(self):
        self.assertEquals(self.calculate(-20735, 126766.0), 106031.00, "")

    def test0848(self):
        self.assertEquals(self.calculate(-7673, -162795.0), -170468.00, "")

    def test0849(self):
        self.assertEquals(self.calculate(17918, 150602.0), 168520.00, "")

    def test0850(self):
        self.assertEquals(self.calculate(20852, -7586.0), 13266.00, "")

    def test0851(self):
        self.assertEquals(self.calculate(-28969, -186882.0), -215851.00, "")

    def test0852(self):
        self.assertEquals(self.calculate(-27077, -142850.0), -169927.00, "")

    def test0853(self):
        self.assertEquals(self.calculate(17891, 128539.0), 146430.00, "")

    def test0854(self):
        self.assertEquals(self.calculate(-30479, 121513.0), 91034.00, "")

    def test0855(self):
        self.assertEquals(self.calculate(-29394, 67013.0), 37619.00, "")

    def test0856(self):
        self.assertEquals(self.calculate(-14790, 130804.0), 116014.00, "")

    def test0857(self):
        self.assertEquals(self.calculate(27709, 199377.0), 227086.00, "")

    def test0858(self):
        self.assertEquals(self.calculate(-24611, 112883.0), 88272.00, "")

    def test0859(self):
        self.assertEquals(self.calculate(17906, 121688.0), 139594.00, "")

    def test0860(self):
        self.assertEquals(self.calculate(25375, -93708.0), -68333.00, "")

    def test0861(self):
        self.assertEquals(self.calculate(18411, -162891.0), -144480.00, "")

    def test0862(self):
        self.assertEquals(self.calculate(-8363, 194689.0), 186326.00, "")

    def test0863(self):
        self.assertEquals(self.calculate(-31883, 101028.0), 69145.00, "")

    def test0864(self):
        self.assertEquals(self.calculate(-14951, 185240.0), 170289.00, "")

    def test0865(self):
        self.assertEquals(self.calculate(-6006, -18415.0), -24421.00, "")

    def test0866(self):
        self.assertEquals(self.calculate(-29370, 112567.0), 83197.00, "")

    def test0867(self):
        self.assertEquals(self.calculate(9922, -31727.0), -21805.00, "")

    def test0868(self):
        self.assertEquals(self.calculate(-25715, 25887.0), 172.00, "")

    def test0869(self):
        self.assertEquals(self.calculate(31873, -6645.0), 25228.00, "")

    def test0870(self):
        self.assertEquals(self.calculate(19178, -148399.0), -129221.00, "")

    def test0871(self):
        self.assertEquals(self.calculate(8958, 176733.0), 185691.00, "")

    def test0872(self):
        self.assertEquals(self.calculate(5162, -34925.0), -29763.00, "")

    def test0873(self):
        self.assertEquals(self.calculate(5545, -187329.0), -181784.00, "")

    def test0874(self):
        self.assertEquals(self.calculate(31750, -143559.0), -111809.00, "")

    def test0875(self):
        self.assertEquals(self.calculate(-29291, 133559.0), 104268.00, "")

    def test0876(self):
        self.assertEquals(self.calculate(19189, -82411.0), -63222.00, "")

    def test0877(self):
        self.assertEquals(self.calculate(29779, -130473.0), -100694.00, "")

    def test0878(self):
        self.assertEquals(self.calculate(-26618, -160865.0), -187483.00, "")

    def test0879(self):
        self.assertEquals(self.calculate(11259, -169172.0), -157913.00, "")

    def test0880(self):
        self.assertEquals(self.calculate(3853, -166492.0), -162639.00, "")

    def test0881(self):
        self.assertEquals(self.calculate(-30354, 33938.0), 3584.00, "")

    def test0882(self):
        self.assertEquals(self.calculate(29402, 2242.0), 31644.00, "")

    def test0883(self):
        self.assertEquals(self.calculate(20748, -103378.0), -82630.00, "")

    def test0884(self):
        self.assertEquals(self.calculate(29325, 26931.0), 56256.00, "")

    def test0885(self):
        self.assertEquals(self.calculate(-1629, -78751.0), -80380.00, "")

    def test0886(self):
        self.assertEquals(self.calculate(-28338, 183688.0), 155350.00, "")

    def test0887(self):
        self.assertEquals(self.calculate(-23288, -31576.0), -54864.00, "")

    def test0888(self):
        self.assertEquals(self.calculate(9272, 138430.0), 147702.00, "")

    def test0889(self):
        self.assertEquals(self.calculate(-11795, 189632.0), 177837.00, "")

    def test0890(self):
        self.assertEquals(self.calculate(-29288, -125480.0), -154768.00, "")

    def test0891(self):
        self.assertEquals(self.calculate(27325, 5214.0), 32539.00, "")

    def test0892(self):
        self.assertEquals(self.calculate(27832, 169233.0), 197065.00, "")

    def test0893(self):
        self.assertEquals(self.calculate(25865, -147970.0), -122105.00, "")

    def test0894(self):
        self.assertEquals(self.calculate(11862, 99820.0), 111682.00, "")

    def test0895(self):
        self.assertEquals(self.calculate(-31460, -21218.0), -52678.00, "")

    def test0896(self):
        self.assertEquals(self.calculate(26620, 52230.0), 78850.00, "")

    def test0897(self):
        self.assertEquals(self.calculate(1701, -171495.0), -169794.00, "")

    def test0898(self):
        self.assertEquals(self.calculate(-215, -91649.0), -91864.00, "")

    def test0899(self):
        self.assertEquals(self.calculate(-26587, 131150.0), 104563.00, "")

    def test0900(self):
        self.assertEquals(self.calculate(-714, 196714.0), 196000.00, "")

    def test0901(self):
        self.assertEquals(self.calculate(3983, 172795.0), 176778.00, "")

    def test0902(self):
        self.assertEquals(self.calculate(6949, 133417.0), 140366.00, "")

    def test0903(self):
        self.assertEquals(self.calculate(-12156, 81458.0), 69302.00, "")

    def test0904(self):
        self.assertEquals(self.calculate(6134, -181715.0), -175581.00, "")

    def test0905(self):
        self.assertEquals(self.calculate(22599, -1967.0), 20632.00, "")

    def test0906(self):
        self.assertEquals(self.calculate(-17885, 59717.0), 41832.00, "")

    def test0907(self):
        self.assertEquals(self.calculate(14132, -65026.0), -50894.00, "")

    def test0908(self):
        self.assertEquals(self.calculate(6408, 78857.0), 85265.00, "")

    def test0909(self):
        self.assertEquals(self.calculate(24922, 81082.0), 106004.00, "")

    def test0910(self):
        self.assertEquals(self.calculate(5544, 1477.0), 7021.00, "")

    def test0911(self):
        self.assertEquals(self.calculate(-10868, -187826.0), -198694.00, "")

    def test0912(self):
        self.assertEquals(self.calculate(3371, -166838.0), -163467.00, "")

    def test0913(self):
        self.assertEquals(self.calculate(18025, -156950.0), -138925.00, "")

    def test0914(self):
        self.assertEquals(self.calculate(367, -80054.0), -79687.00, "")

    def test0915(self):
        self.assertEquals(self.calculate(32130, -127226.0), -95096.00, "")

    def test0916(self):
        self.assertEquals(self.calculate(27004, -48746.0), -21742.00, "")

    def test0917(self):
        self.assertEquals(self.calculate(9430, 157234.0), 166664.00, "")

    def test0918(self):
        self.assertEquals(self.calculate(14800, -172487.0), -157687.00, "")

    def test0919(self):
        self.assertEquals(self.calculate(-8445, 168802.0), 160357.00, "")

    def test0920(self):
        self.assertEquals(self.calculate(13566, -83900.0), -70334.00, "")

    def test0921(self):
        self.assertEquals(self.calculate(6082, -177094.0), -171012.00, "")

    def test0922(self):
        self.assertEquals(self.calculate(-18248, -151243.0), -169491.00, "")

    def test0923(self):
        self.assertEquals(self.calculate(-27528, 138054.0), 110526.00, "")

    def test0924(self):
        self.assertEquals(self.calculate(12397, -76823.0), -64426.00, "")

    def test0925(self):
        self.assertEquals(self.calculate(29361, 176607.0), 205968.00, "")

    def test0926(self):
        self.assertEquals(self.calculate(-2971, 6527.0), 3556.00, "")

    def test0927(self):
        self.assertEquals(self.calculate(-27249, -1366.0), -28615.00, "")

    def test0928(self):
        self.assertEquals(self.calculate(-19821, -59113.0), -78934.00, "")

    def test0929(self):
        self.assertEquals(self.calculate(-11633, 181340.0), 169707.00, "")

    def test0930(self):
        self.assertEquals(self.calculate(-1459, 54942.0), 53483.00, "")

    def test0931(self):
        self.assertEquals(self.calculate(32207, 30297.0), 62504.00, "")

    def test0932(self):
        self.assertEquals(self.calculate(-6983, -107528.0), -114511.00, "")

    def test0933(self):
        self.assertEquals(self.calculate(17089, -82470.0), -65381.00, "")

    def test0934(self):
        self.assertEquals(self.calculate(13024, -134921.0), -121897.00, "")

    def test0935(self):
        self.assertEquals(self.calculate(29133, 72248.0), 101381.00, "")

    def test0936(self):
        self.assertEquals(self.calculate(-26845, 97373.0), 70528.00, "")

    def test0937(self):
        self.assertEquals(self.calculate(-28834, -4858.0), -33692.00, "")

    def test0938(self):
        self.assertEquals(self.calculate(9732, 128845.0), 138577.00, "")

    def test0939(self):
        self.assertEquals(self.calculate(-14220, 75619.0), 61399.00, "")

    def test0940(self):
        self.assertEquals(self.calculate(-25108, -121334.0), -146442.00, "")

    def test0941(self):
        self.assertEquals(self.calculate(19320, -189044.0), -169724.00, "")

    def test0942(self):
        self.assertEquals(self.calculate(7221, -49661.0), -42440.00, "")

    def test0943(self):
        self.assertEquals(self.calculate(11561, -28678.0), -17117.00, "")

    def test0944(self):
        self.assertEquals(self.calculate(13308, 103273.0), 116581.00, "")

    def test0945(self):
        self.assertEquals(self.calculate(9024, -73743.0), -64719.00, "")

    def test0946(self):
        self.assertEquals(self.calculate(-1084, 151985.0), 150901.00, "")

    def test0947(self):
        self.assertEquals(self.calculate(-10302, -198932.0), -209234.00, "")

    def test0948(self):
        self.assertEquals(self.calculate(-698, -81947.0), -82645.00, "")

    def test0949(self):
        self.assertEquals(self.calculate(-28274, 86094.0), 57820.00, "")

    def test0950(self):
        self.assertEquals(self.calculate(-7250, 160232.0), 152982.00, "")

    def test0951(self):
        self.assertEquals(self.calculate(11756, 40079.0), 51835.00, "")

    def test0952(self):
        self.assertEquals(self.calculate(-6387, -34989.0), -41376.00, "")

    def test0953(self):
        self.assertEquals(self.calculate(-11584, -159132.0), -170716.00, "")

    def test0954(self):
        self.assertEquals(self.calculate(-6831, -130089.0), -136920.00, "")

    def test0955(self):
        self.assertEquals(self.calculate(27240, 132350.0), 159590.00, "")

    def test0956(self):
        self.assertEquals(self.calculate(27893, 84027.0), 111920.00, "")

    def test0957(self):
        self.assertEquals(self.calculate(23639, 116335.0), 139974.00, "")

    def test0958(self):
        self.assertEquals(self.calculate(-12434, 118806.0), 106372.00, "")

    def test0959(self):
        self.assertEquals(self.calculate(20562, 162798.0), 183360.00, "")

    def test0960(self):
        self.assertEquals(self.calculate(-24077, -164208.0), -188285.00, "")

    def test0961(self):
        self.assertEquals(self.calculate(16686, 154195.0), 170881.00, "")

    def test0962(self):
        self.assertEquals(self.calculate(6789, 164222.0), 171011.00, "")

    def test0963(self):
        self.assertEquals(self.calculate(21881, 5265.0), 27146.00, "")

    def test0964(self):
        self.assertEquals(self.calculate(-16379, 60838.0), 44459.00, "")

    def test0965(self):
        self.assertEquals(self.calculate(23924, 49236.0), 73160.00, "")

    def test0966(self):
        self.assertEquals(self.calculate(17362, -132860.0), -115498.00, "")

    def test0967(self):
        self.assertEquals(self.calculate(-22884, -106977.0), -129861.00, "")

    def test0968(self):
        self.assertEquals(self.calculate(-26636, -21459.0), -48095.00, "")

    def test0969(self):
        self.assertEquals(self.calculate(14583, -198285.0), -183702.00, "")

    def test0970(self):
        self.assertEquals(self.calculate(-28800, -44037.0), -72837.00, "")

    def test0971(self):
        self.assertEquals(self.calculate(-10939, -34848.0), -45787.00, "")

    def test0972(self):
        self.assertEquals(self.calculate(23999, 155460.0), 179459.00, "")

    def test0973(self):
        self.assertEquals(self.calculate(-5867, 172116.0), 166249.00, "")

    def test0974(self):
        self.assertEquals(self.calculate(-17556, -159905.0), -177461.00, "")

    def test0975(self):
        self.assertEquals(self.calculate(-22835, 29195.0), 6360.00, "")

    def test0976(self):
        self.assertEquals(self.calculate(23608, 72452.0), 96060.00, "")

    def test0977(self):
        self.assertEquals(self.calculate(-25609, 47804.0), 22195.00, "")

    def test0978(self):
        self.assertEquals(self.calculate(-20099, 63710.0), 43611.00, "")

    def test0979(self):
        self.assertEquals(self.calculate(21508, 9883.0), 31391.00, "")

    def test0980(self):
        self.assertEquals(self.calculate(-27521, 119171.0), 91650.00, "")

    def test0981(self):
        self.assertEquals(self.calculate(2187, -175963.0), -173776.00, "")

    def test0982(self):
        self.assertEquals(self.calculate(-19164, 61331.0), 42167.00, "")

    def test0983(self):
        self.assertEquals(self.calculate(-8910, 144283.0), 135373.00, "")

    def test0984(self):
        self.assertEquals(self.calculate(-17331, 145523.0), 128192.00, "")

    def test0985(self):
        self.assertEquals(self.calculate(-11647, 169109.0), 157462.00, "")

    def test0986(self):
        self.assertEquals(self.calculate(25553, -109205.0), -83652.00, "")

    def test0987(self):
        self.assertEquals(self.calculate(9724, -52404.0), -42680.00, "")

    def test0988(self):
        self.assertEquals(self.calculate(-27528, -152880.0), -180408.00, "")

    def test0989(self):
        self.assertEquals(self.calculate(-22244, 14063.0), -8181.00, "")

    def test0990(self):
        self.assertEquals(self.calculate(-6176, -13942.0), -20118.00, "")

    def test0991(self):
        self.assertEquals(self.calculate(7384, -181056.0), -173672.00, "")

    def test0992(self):
        self.assertEquals(self.calculate(27190, 62855.0), 90045.00, "")

    def test0993(self):
        self.assertEquals(self.calculate(-8967, -17050.0), -26017.00, "")

    def test0994(self):
        self.assertEquals(self.calculate(-10053, 10684.0), 631.00, "")

    def test0995(self):
        self.assertEquals(self.calculate(8294, -17124.0), -8830.00, "")

    def test0996(self):
        self.assertEquals(self.calculate(-21567, -56128.0), -77695.00, "")

    def test0997(self):
        self.assertEquals(self.calculate(-20430, -112312.0), -132742.00, "")

    def test0998(self):
        self.assertEquals(self.calculate(-10708, 124833.0), 114125.00, "")

    def test0999(self):
        self.assertEquals(self.calculate(-8410, 195192.0), 186782.00, "")

    def test1000(self):
        self.assertEquals(self.calculate(-6357, 123694.0), 117337.00, "")

    def test1001(self):
        self.assertEquals(self.calculate(965, 111344.0), 112309.00, "")

    def test1002(self):
        self.assertEquals(self.calculate(-13005, -156649.0), -169654.00, "")

    def test1003(self):
        self.assertEquals(self.calculate(-25748, -87503.0), -113251.00, "")

    def test1004(self):
        self.assertEquals(self.calculate(-3948, 172870.0), 168922.00, "")

    def test1005(self):
        self.assertEquals(self.calculate(-19894, 63656.0), 43762.00, "")

    def test1006(self):
        self.assertEquals(self.calculate(-22984, 150230.0), 127246.00, "")

    def test1007(self):
        self.assertEquals(self.calculate(18881, 178554.0), 197435.00, "")

    def test1008(self):
        self.assertEquals(self.calculate(-18862, -102465.0), -121327.00, "")

    def test1009(self):
        self.assertEquals(self.calculate(10931, 45739.0), 56670.00, "")

    def test1010(self):
        self.assertEquals(self.calculate(-12289, 163428.0), 151139.00, "")

    def test1011(self):
        self.assertEquals(self.calculate(-24469, -50815.0), -75284.00, "")

    def test1012(self):
        self.assertEquals(self.calculate(24153, 159047.0), 183200.00, "")

    def test1013(self):
        self.assertEquals(self.calculate(13482, -37586.0), -24104.00, "")

    def test1014(self):
        self.assertEquals(self.calculate(-31715, 143296.0), 111581.00, "")

    def test1015(self):
        self.assertEquals(self.calculate(14490, -56094.0), -41604.00, "")

    def test1016(self):
        self.assertEquals(self.calculate(15508, 127357.0), 142865.00, "")

    def test1017(self):
        self.assertEquals(self.calculate(-32713, 33873.0), 1160.00, "")

    def test1018(self):
        self.assertEquals(self.calculate(1391, 46397.0), 47788.00, "")

    def test1019(self):
        self.assertEquals(self.calculate(-2493, 41451.0), 38958.00, "")

    def test1020(self):
        self.assertEquals(self.calculate(30492, -124499.0), -94007.00, "")

    def test1021(self):
        self.assertEquals(self.calculate(-19789, 156879.0), 137090.00, "")

    def test1022(self):
        self.assertEquals(self.calculate(27056, -31599.0), -4543.00, "")

    def test1023(self):
        self.assertEquals(self.calculate(24042, 82864.0), 106906.00, "")



class TestVM_Add_LongInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushW(rhs)
        v.VM_Add()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(525630099, 16082), 525646181)

    def test0001(self):
        self.assertEquals(self.calculate(2139252742, 5944), 2139258686)

    def test0002(self):
        self.assertEquals(self.calculate(-1075094418, -1390), -1075095808)

    def test0003(self):
        self.assertEquals(self.calculate(1645612220, -21767), 1645590453)

    def test0004(self):
        self.assertEquals(self.calculate(611731641, -22082), 611709559)

    def test0005(self):
        self.assertEquals(self.calculate(207145769, 7093), 207152862)

    def test0006(self):
        self.assertEquals(self.calculate(-1745855375, 10651), -1745844724)

    def test0007(self):
        self.assertEquals(self.calculate(-978166317, 2686), -978163631)

    def test0008(self):
        self.assertEquals(self.calculate(-703512586, 13870), -703498716)

    def test0009(self):
        self.assertEquals(self.calculate(-679223362, -22314), -679245676)

    def test0010(self):
        self.assertEquals(self.calculate(62282101, -5131), 62276970)

    def test0011(self):
        self.assertEquals(self.calculate(1706550955, -32586), 1706518369)

    def test0012(self):
        self.assertEquals(self.calculate(627361008, -31081), 627329927)

    def test0013(self):
        self.assertEquals(self.calculate(910654763, -3624), 910651139)

    def test0014(self):
        self.assertEquals(self.calculate(2012234592, 16190), 2012250782)

    def test0015(self):
        self.assertEquals(self.calculate(1549584312, -6509), 1549577803)

    def test0016(self):
        self.assertEquals(self.calculate(-961747536, -17075), -961764611)

    def test0017(self):
        self.assertEquals(self.calculate(-2064139555, -19394), -2064158949)

    def test0018(self):
        self.assertEquals(self.calculate(816026256, -11295), 816014961)

    def test0019(self):
        self.assertEquals(self.calculate(742387141, 24806), 742411947)

    def test0020(self):
        self.assertEquals(self.calculate(2082705764, 2718), 2082708482)

    def test0021(self):
        self.assertEquals(self.calculate(-344039829, 27825), -344012004)

    def test0022(self):
        self.assertEquals(self.calculate(1656685718, 20187), 1656705905)

    def test0023(self):
        self.assertEquals(self.calculate(1182496435, 10172), 1182506607)

    def test0024(self):
        self.assertEquals(self.calculate(1480534605, -13159), 1480521446)

    def test0025(self):
        self.assertEquals(self.calculate(1826304009, -18064), 1826285945)

    def test0026(self):
        self.assertEquals(self.calculate(1997038720, 2477), 1997041197)

    def test0027(self):
        self.assertEquals(self.calculate(-2067254940, -23996), -2067278936)

    def test0028(self):
        self.assertEquals(self.calculate(-1870213165, -4507), -1870217672)

    def test0029(self):
        self.assertEquals(self.calculate(115338906, -22296), 115316610)

    def test0030(self):
        self.assertEquals(self.calculate(474933576, 14765), 474948341)

    def test0031(self):
        self.assertEquals(self.calculate(-934361708, -28997), -934390705)

    def test0032(self):
        self.assertEquals(self.calculate(2089730326, -31897), 2089698429)

    def test0033(self):
        self.assertEquals(self.calculate(104302248, 13401), 104315649)

    def test0034(self):
        self.assertEquals(self.calculate(436354485, -16441), 436338044)

    def test0035(self):
        self.assertEquals(self.calculate(374546839, -18234), 374528605)

    def test0036(self):
        self.assertEquals(self.calculate(1546684024, 29288), 1546713312)

    def test0037(self):
        self.assertEquals(self.calculate(-1723767856, -13992), -1723781848)

    def test0038(self):
        self.assertEquals(self.calculate(1219129847, 32163), 1219162010)

    def test0039(self):
        self.assertEquals(self.calculate(1344009939, 9103), 1344019042)

    def test0040(self):
        self.assertEquals(self.calculate(273994882, 26104), 274020986)

    def test0041(self):
        self.assertEquals(self.calculate(-1137238732, -13413), -1137252145)

    def test0042(self):
        self.assertEquals(self.calculate(-804632991, 2618), -804630373)

    def test0043(self):
        self.assertEquals(self.calculate(-1403839145, -17453), -1403856598)

    def test0044(self):
        self.assertEquals(self.calculate(979467044, -4242), 979462802)

    def test0045(self):
        self.assertEquals(self.calculate(-1150577928, -17343), -1150595271)

    def test0046(self):
        self.assertEquals(self.calculate(1284738242, -1627), 1284736615)

    def test0047(self):
        self.assertEquals(self.calculate(-1231740552, -29137), -1231769689)

    def test0048(self):
        self.assertEquals(self.calculate(607759188, 2626), 607761814)

    def test0049(self):
        self.assertEquals(self.calculate(-1895796287, -2393), -1895798680)

    def test0050(self):
        self.assertEquals(self.calculate(1197525545, -30430), 1197495115)

    def test0051(self):
        self.assertEquals(self.calculate(102285968, 23695), 102309663)

    def test0052(self):
        self.assertEquals(self.calculate(303174916, 1263), 303176179)

    def test0053(self):
        self.assertEquals(self.calculate(-471072081, 6738), -471065343)

    def test0054(self):
        self.assertEquals(self.calculate(1604735592, 4620), 1604740212)

    def test0055(self):
        self.assertEquals(self.calculate(-2053139697, 15543), -2053124154)

    def test0056(self):
        self.assertEquals(self.calculate(-2072473067, 14153), -2072458914)

    def test0057(self):
        self.assertEquals(self.calculate(-1180834358, 22672), -1180811686)

    def test0058(self):
        self.assertEquals(self.calculate(1966575014, -26988), 1966548026)

    def test0059(self):
        self.assertEquals(self.calculate(911760453, -14581), 911745872)

    def test0060(self):
        self.assertEquals(self.calculate(209213142, -21118), 209192024)

    def test0061(self):
        self.assertEquals(self.calculate(-1504934132, -31272), -1504965404)

    def test0062(self):
        self.assertEquals(self.calculate(747765956, -1360), 747764596)

    def test0063(self):
        self.assertEquals(self.calculate(-1364466112, -10023), -1364476135)

    def test0064(self):
        self.assertEquals(self.calculate(676676502, -1603), 676674899)

    def test0065(self):
        self.assertEquals(self.calculate(-1236910220, 2960), -1236907260)

    def test0066(self):
        self.assertEquals(self.calculate(-366380576, -9977), -366390553)

    def test0067(self):
        self.assertEquals(self.calculate(-1771463048, -2857), -1771465905)

    def test0068(self):
        self.assertEquals(self.calculate(576497222, 4616), 576501838)

    def test0069(self):
        self.assertEquals(self.calculate(94357287, -23777), 94333510)

    def test0070(self):
        self.assertEquals(self.calculate(787387607, 125), 787387732)

    def test0071(self):
        self.assertEquals(self.calculate(-407839448, -23016), -407862464)

    def test0072(self):
        self.assertEquals(self.calculate(-1613281464, 5585), -1613275879)

    def test0073(self):
        self.assertEquals(self.calculate(-1778708834, -6924), -1778715758)

    def test0074(self):
        self.assertEquals(self.calculate(1064579270, -32414), 1064546856)

    def test0075(self):
        self.assertEquals(self.calculate(-1264274407, -29430), -1264303837)

    def test0076(self):
        self.assertEquals(self.calculate(-1768871920, -30167), -1768902087)

    def test0077(self):
        self.assertEquals(self.calculate(-970747859, 8183), -970739676)

    def test0078(self):
        self.assertEquals(self.calculate(-1496036797, 9605), -1496027192)

    def test0079(self):
        self.assertEquals(self.calculate(-1800531820, 12969), -1800518851)

    def test0080(self):
        self.assertEquals(self.calculate(535874552, 19325), 535893877)

    def test0081(self):
        self.assertEquals(self.calculate(1389662974, 14964), 1389677938)

    def test0082(self):
        self.assertEquals(self.calculate(202505924, -3157), 202502767)

    def test0083(self):
        self.assertEquals(self.calculate(282683510, -10279), 282673231)

    def test0084(self):
        self.assertEquals(self.calculate(-892832601, -3060), -892835661)

    def test0085(self):
        self.assertEquals(self.calculate(-1433259772, 31161), -1433228611)

    def test0086(self):
        self.assertEquals(self.calculate(1033350369, 19793), 1033370162)

    def test0087(self):
        self.assertEquals(self.calculate(-1762446776, 2378), -1762444398)

    def test0088(self):
        self.assertEquals(self.calculate(1404230486, -19633), 1404210853)

    def test0089(self):
        self.assertEquals(self.calculate(1155978478, 6175), 1155984653)

    def test0090(self):
        self.assertEquals(self.calculate(-498387585, -3270), -498390855)

    def test0091(self):
        self.assertEquals(self.calculate(1846301881, 31072), 1846332953)

    def test0092(self):
        self.assertEquals(self.calculate(889111890, 16653), 889128543)

    def test0093(self):
        self.assertEquals(self.calculate(-1170775476, -13868), -1170789344)

    def test0094(self):
        self.assertEquals(self.calculate(2036349323, 12237), 2036361560)

    def test0095(self):
        self.assertEquals(self.calculate(1579212489, -24068), 1579188421)

    def test0096(self):
        self.assertEquals(self.calculate(-1685242795, 13866), -1685228929)

    def test0097(self):
        self.assertEquals(self.calculate(-46566306, 19889), -46546417)

    def test0098(self):
        self.assertEquals(self.calculate(90014856, 29910), 90044766)

    def test0099(self):
        self.assertEquals(self.calculate(-192825303, -27752), -192853055)

    def test0100(self):
        self.assertEquals(self.calculate(-355688560, -10505), -355699065)

    def test0101(self):
        self.assertEquals(self.calculate(2003860307, 4119), 2003864426)

    def test0102(self):
        self.assertEquals(self.calculate(161687564, 13664), 161701228)

    def test0103(self):
        self.assertEquals(self.calculate(364122715, 3480), 364126195)

    def test0104(self):
        self.assertEquals(self.calculate(-1574664798, -27054), -1574691852)

    def test0105(self):
        self.assertEquals(self.calculate(-2130457019, -26592), -2130483611)

    def test0106(self):
        self.assertEquals(self.calculate(-1013431817, -19106), -1013450923)

    def test0107(self):
        self.assertEquals(self.calculate(-767919808, -206), -767920014)

    def test0108(self):
        self.assertEquals(self.calculate(821342613, -20322), 821322291)

    def test0109(self):
        self.assertEquals(self.calculate(-549992766, -31779), -550024545)

    def test0110(self):
        self.assertEquals(self.calculate(-720942023, 5468), -720936555)

    def test0111(self):
        self.assertEquals(self.calculate(-245256850, -30743), -245287593)

    def test0112(self):
        self.assertEquals(self.calculate(1538885880, -734), 1538885146)

    def test0113(self):
        self.assertEquals(self.calculate(-1002109911, -15348), -1002125259)

    def test0114(self):
        self.assertEquals(self.calculate(-1909424353, -11111), -1909435464)

    def test0115(self):
        self.assertEquals(self.calculate(148117771, -27573), 148090198)

    def test0116(self):
        self.assertEquals(self.calculate(5854454, -2136), 5852318)

    def test0117(self):
        self.assertEquals(self.calculate(399481126, -23707), 399457419)

    def test0118(self):
        self.assertEquals(self.calculate(-842920598, -25880), -842946478)

    def test0119(self):
        self.assertEquals(self.calculate(1175960433, 6501), 1175966934)

    def test0120(self):
        self.assertEquals(self.calculate(376038519, 1673), 376040192)

    def test0121(self):
        self.assertEquals(self.calculate(1113266016, 32633), 1113298649)

    def test0122(self):
        self.assertEquals(self.calculate(927079328, 2288), 927081616)

    def test0123(self):
        self.assertEquals(self.calculate(-892685860, -24017), -892709877)

    def test0124(self):
        self.assertEquals(self.calculate(1379819530, 20146), 1379839676)

    def test0125(self):
        self.assertEquals(self.calculate(-133232558, 2720), -133229838)

    def test0126(self):
        self.assertEquals(self.calculate(-1613336376, -26576), -1613362952)

    def test0127(self):
        self.assertEquals(self.calculate(-77351068, 14247), -77336821)

    def test0128(self):
        self.assertEquals(self.calculate(695646435, 18801), 695665236)

    def test0129(self):
        self.assertEquals(self.calculate(-1879166098, -30400), -1879196498)

    def test0130(self):
        self.assertEquals(self.calculate(1807089169, 2100), 1807091269)

    def test0131(self):
        self.assertEquals(self.calculate(636520652, 14512), 636535164)

    def test0132(self):
        self.assertEquals(self.calculate(-1550195313, -14124), -1550209437)

    def test0133(self):
        self.assertEquals(self.calculate(1706194046, 29917), 1706223963)

    def test0134(self):
        self.assertEquals(self.calculate(-2067242249, -25810), -2067268059)

    def test0135(self):
        self.assertEquals(self.calculate(1322347289, -32340), 1322314949)

    def test0136(self):
        self.assertEquals(self.calculate(-1857804230, 2117), -1857802113)

    def test0137(self):
        self.assertEquals(self.calculate(-1490808253, -30639), -1490838892)

    def test0138(self):
        self.assertEquals(self.calculate(-1381230452, -6334), -1381236786)

    def test0139(self):
        self.assertEquals(self.calculate(1289731511, 27451), 1289758962)

    def test0140(self):
        self.assertEquals(self.calculate(1285035081, -7740), 1285027341)

    def test0141(self):
        self.assertEquals(self.calculate(-466833684, 11706), -466821978)

    def test0142(self):
        self.assertEquals(self.calculate(-2030131665, -3458), -2030135123)

    def test0143(self):
        self.assertEquals(self.calculate(-587879671, -26891), -587906562)

    def test0144(self):
        self.assertEquals(self.calculate(320629463, -30056), 320599407)

    def test0145(self):
        self.assertEquals(self.calculate(222621947, -29075), 222592872)

    def test0146(self):
        self.assertEquals(self.calculate(-1942177897, 2085), -1942175812)

    def test0147(self):
        self.assertEquals(self.calculate(611636004, 22549), 611658553)

    def test0148(self):
        self.assertEquals(self.calculate(1554964866, -21395), 1554943471)

    def test0149(self):
        self.assertEquals(self.calculate(1626763995, -6058), 1626757937)

    def test0150(self):
        self.assertEquals(self.calculate(-1577212959, 9560), -1577203399)

    def test0151(self):
        self.assertEquals(self.calculate(1132716577, 22068), 1132738645)

    def test0152(self):
        self.assertEquals(self.calculate(-1572068269, 11418), -1572056851)

    def test0153(self):
        self.assertEquals(self.calculate(-1018940582, -11089), -1018951671)

    def test0154(self):
        self.assertEquals(self.calculate(833822494, -22828), 833799666)

    def test0155(self):
        self.assertEquals(self.calculate(-272529610, -969), -272530579)

    def test0156(self):
        self.assertEquals(self.calculate(-608515421, 26587), -608488834)

    def test0157(self):
        self.assertEquals(self.calculate(1156642240, -28008), 1156614232)

    def test0158(self):
        self.assertEquals(self.calculate(-644591911, 27738), -644564173)

    def test0159(self):
        self.assertEquals(self.calculate(-1720441399, 7569), -1720433830)

    def test0160(self):
        self.assertEquals(self.calculate(-86122933, 9298), -86113635)

    def test0161(self):
        self.assertEquals(self.calculate(1518432565, 15836), 1518448401)

    def test0162(self):
        self.assertEquals(self.calculate(1289700265, -953), 1289699312)

    def test0163(self):
        self.assertEquals(self.calculate(588084105, 26315), 588110420)

    def test0164(self):
        self.assertEquals(self.calculate(2089551895, 20739), 2089572634)

    def test0165(self):
        self.assertEquals(self.calculate(1496382711, 31391), 1496414102)

    def test0166(self):
        self.assertEquals(self.calculate(1252802683, 1854), 1252804537)

    def test0167(self):
        self.assertEquals(self.calculate(-1209529211, 16169), -1209513042)

    def test0168(self):
        self.assertEquals(self.calculate(767138846, -12437), 767126409)

    def test0169(self):
        self.assertEquals(self.calculate(-777366972, -6091), -777373063)

    def test0170(self):
        self.assertEquals(self.calculate(1647247538, 28335), 1647275873)

    def test0171(self):
        self.assertEquals(self.calculate(-813403624, 23774), -813379850)

    def test0172(self):
        self.assertEquals(self.calculate(1959878466, 9606), 1959888072)

    def test0173(self):
        self.assertEquals(self.calculate(-1580313066, 3485), -1580309581)

    def test0174(self):
        self.assertEquals(self.calculate(-1597862710, -7779), -1597870489)

    def test0175(self):
        self.assertEquals(self.calculate(-829047599, -26098), -829073697)

    def test0176(self):
        self.assertEquals(self.calculate(-2113181943, 21973), -2113159970)

    def test0177(self):
        self.assertEquals(self.calculate(-2004374181, -7221), -2004381402)

    def test0178(self):
        self.assertEquals(self.calculate(407750549, 5112), 407755661)

    def test0179(self):
        self.assertEquals(self.calculate(1322320005, 16151), 1322336156)

    def test0180(self):
        self.assertEquals(self.calculate(-546071618, -6506), -546078124)

    def test0181(self):
        self.assertEquals(self.calculate(-957786196, -30220), -957816416)

    def test0182(self):
        self.assertEquals(self.calculate(1985283456, -27980), 1985255476)

    def test0183(self):
        self.assertEquals(self.calculate(-613388438, 25059), -613363379)

    def test0184(self):
        self.assertEquals(self.calculate(-425490385, 29743), -425460642)

    def test0185(self):
        self.assertEquals(self.calculate(-149683168, -13600), -149696768)

    def test0186(self):
        self.assertEquals(self.calculate(-1933477998, -28364), -1933506362)

    def test0187(self):
        self.assertEquals(self.calculate(363955750, 18885), 363974635)

    def test0188(self):
        self.assertEquals(self.calculate(495080947, 20435), 495101382)

    def test0189(self):
        self.assertEquals(self.calculate(-490710853, -26464), -490737317)

    def test0190(self):
        self.assertEquals(self.calculate(755411802, -11963), 755399839)

    def test0191(self):
        self.assertEquals(self.calculate(1808277668, 10471), 1808288139)

    def test0192(self):
        self.assertEquals(self.calculate(907015833, -6714), 907009119)

    def test0193(self):
        self.assertEquals(self.calculate(-230891021, -11630), -230902651)

    def test0194(self):
        self.assertEquals(self.calculate(1518465483, 4652), 1518470135)

    def test0195(self):
        self.assertEquals(self.calculate(-500339589, -12899), -500352488)

    def test0196(self):
        self.assertEquals(self.calculate(-415269100, -16400), -415285500)

    def test0197(self):
        self.assertEquals(self.calculate(-1574289560, 11875), -1574277685)

    def test0198(self):
        self.assertEquals(self.calculate(-1380555910, -17025), -1380572935)

    def test0199(self):
        self.assertEquals(self.calculate(789606408, 22444), 789628852)

    def test0200(self):
        self.assertEquals(self.calculate(-1568538631, 9303), -1568529328)

    def test0201(self):
        self.assertEquals(self.calculate(1165314634, 20530), 1165335164)

    def test0202(self):
        self.assertEquals(self.calculate(1602969470, 8282), 1602977752)

    def test0203(self):
        self.assertEquals(self.calculate(-1846688254, -5976), -1846694230)

    def test0204(self):
        self.assertEquals(self.calculate(-1900702602, -29121), -1900731723)

    def test0205(self):
        self.assertEquals(self.calculate(-154925150, -10904), -154936054)

    def test0206(self):
        self.assertEquals(self.calculate(1199615269, 4718), 1199619987)

    def test0207(self):
        self.assertEquals(self.calculate(1362550884, -13102), 1362537782)

    def test0208(self):
        self.assertEquals(self.calculate(1996296799, 25271), 1996322070)

    def test0209(self):
        self.assertEquals(self.calculate(376775312, -8240), 376767072)

    def test0210(self):
        self.assertEquals(self.calculate(1766985957, -29065), 1766956892)

    def test0211(self):
        self.assertEquals(self.calculate(1200322758, 3568), 1200326326)

    def test0212(self):
        self.assertEquals(self.calculate(-1708609798, 3524), -1708606274)

    def test0213(self):
        self.assertEquals(self.calculate(-1301329034, 12641), -1301316393)

    def test0214(self):
        self.assertEquals(self.calculate(846887037, -21175), 846865862)

    def test0215(self):
        self.assertEquals(self.calculate(-542010887, -4198), -542015085)

    def test0216(self):
        self.assertEquals(self.calculate(-1522058919, 13044), -1522045875)

    def test0217(self):
        self.assertEquals(self.calculate(892970902, -3655), 892967247)

    def test0218(self):
        self.assertEquals(self.calculate(-2055042283, -16956), -2055059239)

    def test0219(self):
        self.assertEquals(self.calculate(-233641172, -8619), -233649791)

    def test0220(self):
        self.assertEquals(self.calculate(-114167512, -18954), -114186466)

    def test0221(self):
        self.assertEquals(self.calculate(714845957, -9328), 714836629)

    def test0222(self):
        self.assertEquals(self.calculate(666940920, 5491), 666946411)

    def test0223(self):
        self.assertEquals(self.calculate(-725598530, -20414), -725618944)

    def test0224(self):
        self.assertEquals(self.calculate(-2092434495, -19476), -2092453971)

    def test0225(self):
        self.assertEquals(self.calculate(-1235481615, -22659), -1235504274)

    def test0226(self):
        self.assertEquals(self.calculate(-1476908519, 11871), -1476896648)

    def test0227(self):
        self.assertEquals(self.calculate(-1298953971, -10838), -1298964809)

    def test0228(self):
        self.assertEquals(self.calculate(1398925830, -1573), 1398924257)

    def test0229(self):
        self.assertEquals(self.calculate(783435257, -10468), 783424789)

    def test0230(self):
        self.assertEquals(self.calculate(74455743, -32332), 74423411)

    def test0231(self):
        self.assertEquals(self.calculate(-2020456195, 23953), -2020432242)

    def test0232(self):
        self.assertEquals(self.calculate(-2039314058, 13410), -2039300648)

    def test0233(self):
        self.assertEquals(self.calculate(-489272520, 13179), -489259341)

    def test0234(self):
        self.assertEquals(self.calculate(-1332194629, -28485), -1332223114)

    def test0235(self):
        self.assertEquals(self.calculate(1477551658, 13170), 1477564828)

    def test0236(self):
        self.assertEquals(self.calculate(783632057, 8926), 783640983)

    def test0237(self):
        self.assertEquals(self.calculate(1051342117, -24177), 1051317940)

    def test0238(self):
        self.assertEquals(self.calculate(1622759164, 16420), 1622775584)

    def test0239(self):
        self.assertEquals(self.calculate(1962286365, -12753), 1962273612)

    def test0240(self):
        self.assertEquals(self.calculate(856878841, -29683), 856849158)

    def test0241(self):
        self.assertEquals(self.calculate(319394869, 16405), 319411274)

    def test0242(self):
        self.assertEquals(self.calculate(2141839148, -24136), 2141815012)

    def test0243(self):
        self.assertEquals(self.calculate(-264776796, -24825), -264801621)

    def test0244(self):
        self.assertEquals(self.calculate(1007664193, -7235), 1007656958)

    def test0245(self):
        self.assertEquals(self.calculate(-1268491763, 16528), -1268475235)

    def test0246(self):
        self.assertEquals(self.calculate(1390889927, 23372), 1390913299)

    def test0247(self):
        self.assertEquals(self.calculate(1187850462, -30753), 1187819709)

    def test0248(self):
        self.assertEquals(self.calculate(-319906035, 5028), -319901007)

    def test0249(self):
        self.assertEquals(self.calculate(-1252063214, -23767), -1252086981)

    def test0250(self):
        self.assertEquals(self.calculate(-1488471896, -8848), -1488480744)

    def test0251(self):
        self.assertEquals(self.calculate(1857854784, 14634), 1857869418)

    def test0252(self):
        self.assertEquals(self.calculate(-1996358581, 13354), -1996345227)

    def test0253(self):
        self.assertEquals(self.calculate(1788654171, 963), 1788655134)

    def test0254(self):
        self.assertEquals(self.calculate(-877789798, -10112), -877799910)

    def test0255(self):
        self.assertEquals(self.calculate(389435607, 10663), 389446270)

    def test0256(self):
        self.assertEquals(self.calculate(65388619, 24040), 65412659)

    def test0257(self):
        self.assertEquals(self.calculate(-1768018439, -26817), -1768045256)

    def test0258(self):
        self.assertEquals(self.calculate(-734452844, -22449), -734475293)

    def test0259(self):
        self.assertEquals(self.calculate(444328832, 15327), 444344159)

    def test0260(self):
        self.assertEquals(self.calculate(-1241383903, 23127), -1241360776)

    def test0261(self):
        self.assertEquals(self.calculate(-39596163, 25229), -39570934)

    def test0262(self):
        self.assertEquals(self.calculate(2038890383, -23442), 2038866941)

    def test0263(self):
        self.assertEquals(self.calculate(1984065282, 5178), 1984070460)

    def test0264(self):
        self.assertEquals(self.calculate(-1012790297, -30471), -1012820768)

    def test0265(self):
        self.assertEquals(self.calculate(-1537223239, -16323), -1537239562)

    def test0266(self):
        self.assertEquals(self.calculate(-559452979, -10191), -559463170)

    def test0267(self):
        self.assertEquals(self.calculate(-886876631, -15249), -886891880)

    def test0268(self):
        self.assertEquals(self.calculate(428520195, -16302), 428503893)

    def test0269(self):
        self.assertEquals(self.calculate(1921764124, -20992), 1921743132)

    def test0270(self):
        self.assertEquals(self.calculate(1206043438, 3039), 1206046477)

    def test0271(self):
        self.assertEquals(self.calculate(-2106218961, 24137), -2106194824)

    def test0272(self):
        self.assertEquals(self.calculate(113270119, 6121), 113276240)

    def test0273(self):
        self.assertEquals(self.calculate(728358280, -12177), 728346103)

    def test0274(self):
        self.assertEquals(self.calculate(-1875938611, 30658), -1875907953)

    def test0275(self):
        self.assertEquals(self.calculate(558022837, -8364), 558014473)

    def test0276(self):
        self.assertEquals(self.calculate(174296368, -15403), 174280965)

    def test0277(self):
        self.assertEquals(self.calculate(1651282259, -31131), 1651251128)

    def test0278(self):
        self.assertEquals(self.calculate(1262679984, 25633), 1262705617)

    def test0279(self):
        self.assertEquals(self.calculate(-35279900, -2226), -35282126)

    def test0280(self):
        self.assertEquals(self.calculate(-1725960318, -31705), -1725992023)

    def test0281(self):
        self.assertEquals(self.calculate(764663602, -29551), 764634051)

    def test0282(self):
        self.assertEquals(self.calculate(2032426003, 30825), 2032456828)

    def test0283(self):
        self.assertEquals(self.calculate(1839886473, 14728), 1839901201)

    def test0284(self):
        self.assertEquals(self.calculate(-1470303896, 6767), -1470297129)

    def test0285(self):
        self.assertEquals(self.calculate(359997023, -25242), 359971781)

    def test0286(self):
        self.assertEquals(self.calculate(619161079, -29200), 619131879)

    def test0287(self):
        self.assertEquals(self.calculate(-1531183372, 8382), -1531174990)

    def test0288(self):
        self.assertEquals(self.calculate(-967763302, 22654), -967740648)

    def test0289(self):
        self.assertEquals(self.calculate(1914619654, -24714), 1914594940)

    def test0290(self):
        self.assertEquals(self.calculate(11606732, -4792), 11601940)

    def test0291(self):
        self.assertEquals(self.calculate(-119894464, 6552), -119887912)

    def test0292(self):
        self.assertEquals(self.calculate(-1355798840, -22043), -1355820883)

    def test0293(self):
        self.assertEquals(self.calculate(-1383280736, 30849), -1383249887)

    def test0294(self):
        self.assertEquals(self.calculate(-981462932, -5283), -981468215)

    def test0295(self):
        self.assertEquals(self.calculate(-1508434133, 9132), -1508425001)

    def test0296(self):
        self.assertEquals(self.calculate(1658873920, -4531), 1658869389)

    def test0297(self):
        self.assertEquals(self.calculate(-883176441, 21567), -883154874)

    def test0298(self):
        self.assertEquals(self.calculate(-2136145133, -8585), -2136153718)

    def test0299(self):
        self.assertEquals(self.calculate(-1916640826, 9010), -1916631816)

    def test0300(self):
        self.assertEquals(self.calculate(864420200, 20846), 864441046)

    def test0301(self):
        self.assertEquals(self.calculate(-1398804724, 27725), -1398776999)

    def test0302(self):
        self.assertEquals(self.calculate(1557738496, 30521), 1557769017)

    def test0303(self):
        self.assertEquals(self.calculate(-440485327, -32401), -440517728)

    def test0304(self):
        self.assertEquals(self.calculate(-685020719, -24732), -685045451)

    def test0305(self):
        self.assertEquals(self.calculate(357660413, 4459), 357664872)

    def test0306(self):
        self.assertEquals(self.calculate(-1345051969, -10654), -1345062623)

    def test0307(self):
        self.assertEquals(self.calculate(-1464877092, 2393), -1464874699)

    def test0308(self):
        self.assertEquals(self.calculate(-1941469266, 1214), -1941468052)

    def test0309(self):
        self.assertEquals(self.calculate(2120724243, -23385), 2120700858)

    def test0310(self):
        self.assertEquals(self.calculate(1258753773, 13160), 1258766933)

    def test0311(self):
        self.assertEquals(self.calculate(1609640334, 3891), 1609644225)

    def test0312(self):
        self.assertEquals(self.calculate(-1607051929, -22609), -1607074538)

    def test0313(self):
        self.assertEquals(self.calculate(194521939, -30300), 194491639)

    def test0314(self):
        self.assertEquals(self.calculate(1555266554, 8024), 1555274578)

    def test0315(self):
        self.assertEquals(self.calculate(-1085124510, 16420), -1085108090)

    def test0316(self):
        self.assertEquals(self.calculate(378358623, 13191), 378371814)

    def test0317(self):
        self.assertEquals(self.calculate(1288164295, 19700), 1288183995)

    def test0318(self):
        self.assertEquals(self.calculate(-1983695700, -8806), -1983704506)

    def test0319(self):
        self.assertEquals(self.calculate(2084156149, -13322), 2084142827)

    def test0320(self):
        self.assertEquals(self.calculate(1574963555, 25935), 1574989490)

    def test0321(self):
        self.assertEquals(self.calculate(243898536, 9776), 243908312)

    def test0322(self):
        self.assertEquals(self.calculate(1514051576, 29895), 1514081471)

    def test0323(self):
        self.assertEquals(self.calculate(-632007331, 9723), -631997608)

    def test0324(self):
        self.assertEquals(self.calculate(-548182796, -27233), -548210029)

    def test0325(self):
        self.assertEquals(self.calculate(-2110330036, 3634), -2110326402)

    def test0326(self):
        self.assertEquals(self.calculate(1674023565, -11351), 1674012214)

    def test0327(self):
        self.assertEquals(self.calculate(-1110516691, -7557), -1110524248)

    def test0328(self):
        self.assertEquals(self.calculate(-1781970173, 3378), -1781966795)

    def test0329(self):
        self.assertEquals(self.calculate(584721520, -15046), 584706474)

    def test0330(self):
        self.assertEquals(self.calculate(-705346958, 16028), -705330930)

    def test0331(self):
        self.assertEquals(self.calculate(-1200393628, 11109), -1200382519)

    def test0332(self):
        self.assertEquals(self.calculate(-824156031, -3064), -824159095)

    def test0333(self):
        self.assertEquals(self.calculate(1770987652, 2089), 1770989741)

    def test0334(self):
        self.assertEquals(self.calculate(-1440717840, -7159), -1440724999)

    def test0335(self):
        self.assertEquals(self.calculate(1600532186, -29512), 1600502674)

    def test0336(self):
        self.assertEquals(self.calculate(-1495481418, 15076), -1495466342)

    def test0337(self):
        self.assertEquals(self.calculate(1109055884, 4307), 1109060191)

    def test0338(self):
        self.assertEquals(self.calculate(82519547, -29969), 82489578)

    def test0339(self):
        self.assertEquals(self.calculate(1014165815, -1142), 1014164673)

    def test0340(self):
        self.assertEquals(self.calculate(-1521052308, -3239), -1521055547)

    def test0341(self):
        self.assertEquals(self.calculate(-233600449, -6082), -233606531)

    def test0342(self):
        self.assertEquals(self.calculate(1891531425, -31805), 1891499620)

    def test0343(self):
        self.assertEquals(self.calculate(-1725657584, 15263), -1725642321)

    def test0344(self):
        self.assertEquals(self.calculate(-1847741668, 25874), -1847715794)

    def test0345(self):
        self.assertEquals(self.calculate(465983266, 19213), 466002479)

    def test0346(self):
        self.assertEquals(self.calculate(270112272, -11340), 270100932)

    def test0347(self):
        self.assertEquals(self.calculate(-439899570, -7823), -439907393)

    def test0348(self):
        self.assertEquals(self.calculate(-2019030463, -19226), -2019049689)

    def test0349(self):
        self.assertEquals(self.calculate(120793319, 20337), 120813656)

    def test0350(self):
        self.assertEquals(self.calculate(728899201, 28460), 728927661)

    def test0351(self):
        self.assertEquals(self.calculate(-1560646175, 5809), -1560640366)

    def test0352(self):
        self.assertEquals(self.calculate(1233856050, -22680), 1233833370)

    def test0353(self):
        self.assertEquals(self.calculate(984411054, 30880), 984441934)

    def test0354(self):
        self.assertEquals(self.calculate(601354117, -22138), 601331979)

    def test0355(self):
        self.assertEquals(self.calculate(-927357121, 14968), -927342153)

    def test0356(self):
        self.assertEquals(self.calculate(-1139374514, 24019), -1139350495)

    def test0357(self):
        self.assertEquals(self.calculate(735378262, 5364), 735383626)

    def test0358(self):
        self.assertEquals(self.calculate(2011833412, 15469), 2011848881)

    def test0359(self):
        self.assertEquals(self.calculate(-2123089718, -10693), -2123100411)

    def test0360(self):
        self.assertEquals(self.calculate(1969204009, 9506), 1969213515)

    def test0361(self):
        self.assertEquals(self.calculate(1117868103, -821), 1117867282)

    def test0362(self):
        self.assertEquals(self.calculate(1765508213, 26657), 1765534870)

    def test0363(self):
        self.assertEquals(self.calculate(-320929361, 31926), -320897435)

    def test0364(self):
        self.assertEquals(self.calculate(1179194302, -20398), 1179173904)

    def test0365(self):
        self.assertEquals(self.calculate(1635289517, -5756), 1635283761)

    def test0366(self):
        self.assertEquals(self.calculate(511503519, -13168), 511490351)

    def test0367(self):
        self.assertEquals(self.calculate(817717602, -1491), 817716111)

    def test0368(self):
        self.assertEquals(self.calculate(-1929680311, 14768), -1929665543)

    def test0369(self):
        self.assertEquals(self.calculate(-62620414, 24823), -62595591)

    def test0370(self):
        self.assertEquals(self.calculate(-1309067079, -26751), -1309093830)

    def test0371(self):
        self.assertEquals(self.calculate(1556914451, 25976), 1556940427)

    def test0372(self):
        self.assertEquals(self.calculate(804554170, 30723), 804584893)

    def test0373(self):
        self.assertEquals(self.calculate(-1217618425, -14008), -1217632433)

    def test0374(self):
        self.assertEquals(self.calculate(-1565297845, 5417), -1565292428)

    def test0375(self):
        self.assertEquals(self.calculate(568465866, -17489), 568448377)

    def test0376(self):
        self.assertEquals(self.calculate(577776004, 9660), 577785664)

    def test0377(self):
        self.assertEquals(self.calculate(-1616089410, -28102), -1616117512)

    def test0378(self):
        self.assertEquals(self.calculate(-72154088, -6696), -72160784)

    def test0379(self):
        self.assertEquals(self.calculate(1740938271, -1200), 1740937071)

    def test0380(self):
        self.assertEquals(self.calculate(206825019, 18476), 206843495)

    def test0381(self):
        self.assertEquals(self.calculate(1813629197, -13768), 1813615429)

    def test0382(self):
        self.assertEquals(self.calculate(-1510316164, 8163), -1510308001)

    def test0383(self):
        self.assertEquals(self.calculate(-1176774568, 3471), -1176771097)

    def test0384(self):
        self.assertEquals(self.calculate(-1645598543, -24079), -1645622622)

    def test0385(self):
        self.assertEquals(self.calculate(-257218057, -11684), -257229741)

    def test0386(self):
        self.assertEquals(self.calculate(-1999141579, -22279), -1999163858)

    def test0387(self):
        self.assertEquals(self.calculate(1055260235, -363), 1055259872)

    def test0388(self):
        self.assertEquals(self.calculate(-124695655, 709), -124694946)

    def test0389(self):
        self.assertEquals(self.calculate(-1776260565, 14972), -1776245593)

    def test0390(self):
        self.assertEquals(self.calculate(34233596, 5257), 34238853)

    def test0391(self):
        self.assertEquals(self.calculate(79544020, 6465), 79550485)

    def test0392(self):
        self.assertEquals(self.calculate(906008307, 30719), 906039026)

    def test0393(self):
        self.assertEquals(self.calculate(-1238017293, -5550), -1238022843)

    def test0394(self):
        self.assertEquals(self.calculate(-2026091883, 19508), -2026072375)

    def test0395(self):
        self.assertEquals(self.calculate(-1863839905, -14139), -1863854044)

    def test0396(self):
        self.assertEquals(self.calculate(1778229518, -2327), 1778227191)

    def test0397(self):
        self.assertEquals(self.calculate(-1470955959, -15815), -1470971774)

    def test0398(self):
        self.assertEquals(self.calculate(-1847249570, -22103), -1847271673)

    def test0399(self):
        self.assertEquals(self.calculate(1949366416, 20184), 1949386600)

    def test0400(self):
        self.assertEquals(self.calculate(1367085136, 15116), 1367100252)

    def test0401(self):
        self.assertEquals(self.calculate(-1605243574, 31923), -1605211651)

    def test0402(self):
        self.assertEquals(self.calculate(-833686999, 15833), -833671166)

    def test0403(self):
        self.assertEquals(self.calculate(-41874027, 23708), -41850319)

    def test0404(self):
        self.assertEquals(self.calculate(-1452370520, 26132), -1452344388)

    def test0405(self):
        self.assertEquals(self.calculate(-1574242729, -6832), -1574249561)

    def test0406(self):
        self.assertEquals(self.calculate(-1251962484, 16688), -1251945796)

    def test0407(self):
        self.assertEquals(self.calculate(-769290112, -14996), -769305108)

    def test0408(self):
        self.assertEquals(self.calculate(-87748248, -4582), -87752830)

    def test0409(self):
        self.assertEquals(self.calculate(1561874918, 24125), 1561899043)

    def test0410(self):
        self.assertEquals(self.calculate(1859564394, 17022), 1859581416)

    def test0411(self):
        self.assertEquals(self.calculate(-1412106623, 14595), -1412092028)

    def test0412(self):
        self.assertEquals(self.calculate(-1393383913, -21255), -1393405168)

    def test0413(self):
        self.assertEquals(self.calculate(-2079111585, 15222), -2079096363)

    def test0414(self):
        self.assertEquals(self.calculate(214351979, 12147), 214364126)

    def test0415(self):
        self.assertEquals(self.calculate(-2099943003, -30012), -2099973015)

    def test0416(self):
        self.assertEquals(self.calculate(792903471, -11015), 792892456)

    def test0417(self):
        self.assertEquals(self.calculate(-1676532383, -24909), -1676557292)

    def test0418(self):
        self.assertEquals(self.calculate(-1977719218, -24626), -1977743844)

    def test0419(self):
        self.assertEquals(self.calculate(-2068563169, 3723), -2068559446)

    def test0420(self):
        self.assertEquals(self.calculate(262737520, -6245), 262731275)

    def test0421(self):
        self.assertEquals(self.calculate(-991896802, 30611), -991866191)

    def test0422(self):
        self.assertEquals(self.calculate(-840194808, -19264), -840214072)

    def test0423(self):
        self.assertEquals(self.calculate(-2094717347, 25040), -2094692307)

    def test0424(self):
        self.assertEquals(self.calculate(722094681, 11671), 722106352)

    def test0425(self):
        self.assertEquals(self.calculate(196417030, 18687), 196435717)

    def test0426(self):
        self.assertEquals(self.calculate(-91959367, 1832), -91957535)

    def test0427(self):
        self.assertEquals(self.calculate(341502242, 24590), 341526832)

    def test0428(self):
        self.assertEquals(self.calculate(400076636, 7702), 400084338)

    def test0429(self):
        self.assertEquals(self.calculate(-613974015, 2020), -613971995)

    def test0430(self):
        self.assertEquals(self.calculate(-912481529, -23687), -912505216)

    def test0431(self):
        self.assertEquals(self.calculate(1780076842, -22140), 1780054702)

    def test0432(self):
        self.assertEquals(self.calculate(527591005, 24996), 527616001)

    def test0433(self):
        self.assertEquals(self.calculate(1791231195, -9165), 1791222030)

    def test0434(self):
        self.assertEquals(self.calculate(1242401421, 8013), 1242409434)

    def test0435(self):
        self.assertEquals(self.calculate(-1771881304, -17771), -1771899075)

    def test0436(self):
        self.assertEquals(self.calculate(812251079, 17778), 812268857)

    def test0437(self):
        self.assertEquals(self.calculate(312426429, 10547), 312436976)

    def test0438(self):
        self.assertEquals(self.calculate(247762368, -25291), 247737077)

    def test0439(self):
        self.assertEquals(self.calculate(1442728988, -25619), 1442703369)

    def test0440(self):
        self.assertEquals(self.calculate(-866496671, -27055), -866523726)

    def test0441(self):
        self.assertEquals(self.calculate(-72887648, -24452), -72912100)

    def test0442(self):
        self.assertEquals(self.calculate(-1390434108, 9189), -1390424919)

    def test0443(self):
        self.assertEquals(self.calculate(-437489159, 11248), -437477911)

    def test0444(self):
        self.assertEquals(self.calculate(746194577, -22541), 746172036)

    def test0445(self):
        self.assertEquals(self.calculate(-794591045, 30000), -794561045)

    def test0446(self):
        self.assertEquals(self.calculate(-1584691846, 11648), -1584680198)

    def test0447(self):
        self.assertEquals(self.calculate(-983760804, 15492), -983745312)

    def test0448(self):
        self.assertEquals(self.calculate(-464733572, -20306), -464753878)

    def test0449(self):
        self.assertEquals(self.calculate(-404689999, -1261), -404691260)

    def test0450(self):
        self.assertEquals(self.calculate(1942305192, 30418), 1942335610)

    def test0451(self):
        self.assertEquals(self.calculate(543651261, 12059), 543663320)

    def test0452(self):
        self.assertEquals(self.calculate(845271223, -5879), 845265344)

    def test0453(self):
        self.assertEquals(self.calculate(-2071007193, 10466), -2070996727)

    def test0454(self):
        self.assertEquals(self.calculate(-1351151334, -13783), -1351165117)

    def test0455(self):
        self.assertEquals(self.calculate(-714664470, -10242), -714674712)

    def test0456(self):
        self.assertEquals(self.calculate(-1959091954, 471), -1959091483)

    def test0457(self):
        self.assertEquals(self.calculate(427584869, -3121), 427581748)

    def test0458(self):
        self.assertEquals(self.calculate(-497746728, -26809), -497773537)

    def test0459(self):
        self.assertEquals(self.calculate(-721627541, 19374), -721608167)

    def test0460(self):
        self.assertEquals(self.calculate(1147185271, 10853), 1147196124)

    def test0461(self):
        self.assertEquals(self.calculate(-1343093133, 30752), -1343062381)

    def test0462(self):
        self.assertEquals(self.calculate(1918035011, -32361), 1918002650)

    def test0463(self):
        self.assertEquals(self.calculate(-253207157, -31117), -253238274)

    def test0464(self):
        self.assertEquals(self.calculate(800230631, 25360), 800255991)

    def test0465(self):
        self.assertEquals(self.calculate(2099667905, -14840), 2099653065)

    def test0466(self):
        self.assertEquals(self.calculate(-73089204, -31612), -73120816)

    def test0467(self):
        self.assertEquals(self.calculate(972992633, -27947), 972964686)

    def test0468(self):
        self.assertEquals(self.calculate(-382047804, -9321), -382057125)

    def test0469(self):
        self.assertEquals(self.calculate(1912915626, 19261), 1912934887)

    def test0470(self):
        self.assertEquals(self.calculate(1041199307, -365), 1041198942)

    def test0471(self):
        self.assertEquals(self.calculate(-1504490721, -29083), -1504519804)

    def test0472(self):
        self.assertEquals(self.calculate(-230492637, -16144), -230508781)

    def test0473(self):
        self.assertEquals(self.calculate(-1000015439, -29789), -1000045228)

    def test0474(self):
        self.assertEquals(self.calculate(-168089751, -6859), -168096610)

    def test0475(self):
        self.assertEquals(self.calculate(-1479959666, 19658), -1479940008)

    def test0476(self):
        self.assertEquals(self.calculate(-22590450, -8187), -22598637)

    def test0477(self):
        self.assertEquals(self.calculate(607707414, 5984), 607713398)

    def test0478(self):
        self.assertEquals(self.calculate(-134289683, -1294), -134290977)

    def test0479(self):
        self.assertEquals(self.calculate(1671709695, -22819), 1671686876)

    def test0480(self):
        self.assertEquals(self.calculate(-1975745175, -28820), -1975773995)

    def test0481(self):
        self.assertEquals(self.calculate(-2046263895, -28927), -2046292822)

    def test0482(self):
        self.assertEquals(self.calculate(1924832840, 10170), 1924843010)

    def test0483(self):
        self.assertEquals(self.calculate(-2097493751, 26671), -2097467080)

    def test0484(self):
        self.assertEquals(self.calculate(1465829572, 11485), 1465841057)

    def test0485(self):
        self.assertEquals(self.calculate(1125407786, -6251), 1125401535)

    def test0486(self):
        self.assertEquals(self.calculate(-963942703, -22415), -963965118)

    def test0487(self):
        self.assertEquals(self.calculate(1770688264, -32300), 1770655964)

    def test0488(self):
        self.assertEquals(self.calculate(729566955, 5000), 729571955)

    def test0489(self):
        self.assertEquals(self.calculate(-1127638824, -17720), -1127656544)

    def test0490(self):
        self.assertEquals(self.calculate(-1205727895, -7173), -1205735068)

    def test0491(self):
        self.assertEquals(self.calculate(-883506912, 29344), -883477568)

    def test0492(self):
        self.assertEquals(self.calculate(1468409923, 20344), 1468430267)

    def test0493(self):
        self.assertEquals(self.calculate(710604566, -1333), 710603233)

    def test0494(self):
        self.assertEquals(self.calculate(-898681783, 27065), -898654718)

    def test0495(self):
        self.assertEquals(self.calculate(-1627049338, 7088), -1627042250)

    def test0496(self):
        self.assertEquals(self.calculate(1724690367, 16825), 1724707192)

    def test0497(self):
        self.assertEquals(self.calculate(2113210934, 20655), 2113231589)

    def test0498(self):
        self.assertEquals(self.calculate(1132102234, -23806), 1132078428)

    def test0499(self):
        self.assertEquals(self.calculate(1452547422, 10553), 1452557975)

    def test0500(self):
        self.assertEquals(self.calculate(-114140704, 1352), -114139352)

    def test0501(self):
        self.assertEquals(self.calculate(-856438851, 26428), -856412423)

    def test0502(self):
        self.assertEquals(self.calculate(365234721, -12629), 365222092)

    def test0503(self):
        self.assertEquals(self.calculate(-22282009, 20634), -22261375)

    def test0504(self):
        self.assertEquals(self.calculate(2141233131, 16674), 2141249805)

    def test0505(self):
        self.assertEquals(self.calculate(-540174111, -28682), -540202793)

    def test0506(self):
        self.assertEquals(self.calculate(-884222953, 31062), -884191891)

    def test0507(self):
        self.assertEquals(self.calculate(-406032744, 4580), -406028164)

    def test0508(self):
        self.assertEquals(self.calculate(1814208557, -17534), 1814191023)

    def test0509(self):
        self.assertEquals(self.calculate(-850295009, -4563), -850299572)

    def test0510(self):
        self.assertEquals(self.calculate(-668406790, 14627), -668392163)

    def test0511(self):
        self.assertEquals(self.calculate(-1543944258, 4880), -1543939378)

    def test0512(self):
        self.assertEquals(self.calculate(381876471, 16322), 381892793)

    def test0513(self):
        self.assertEquals(self.calculate(23615787, 25848), 23641635)

    def test0514(self):
        self.assertEquals(self.calculate(504728271, -14171), 504714100)

    def test0515(self):
        self.assertEquals(self.calculate(-355994159, -11465), -356005624)

    def test0516(self):
        self.assertEquals(self.calculate(783770867, 1573), 783772440)

    def test0517(self):
        self.assertEquals(self.calculate(-1807117706, 12315), -1807105391)

    def test0518(self):
        self.assertEquals(self.calculate(1689587549, 9572), 1689597121)

    def test0519(self):
        self.assertEquals(self.calculate(-299873662, 10917), -299862745)

    def test0520(self):
        self.assertEquals(self.calculate(-406673504, -18752), -406692256)

    def test0521(self):
        self.assertEquals(self.calculate(-589926353, 7673), -589918680)

    def test0522(self):
        self.assertEquals(self.calculate(-1541313892, -14191), -1541328083)

    def test0523(self):
        self.assertEquals(self.calculate(-1405105972, -7508), -1405113480)

    def test0524(self):
        self.assertEquals(self.calculate(440919514, -26918), 440892596)

    def test0525(self):
        self.assertEquals(self.calculate(-886001760, 894), -886000866)

    def test0526(self):
        self.assertEquals(self.calculate(-1246453445, 5522), -1246447923)

    def test0527(self):
        self.assertEquals(self.calculate(996937817, 27931), 996965748)

    def test0528(self):
        self.assertEquals(self.calculate(607146028, -4395), 607141633)

    def test0529(self):
        self.assertEquals(self.calculate(-517962642, -20234), -517982876)

    def test0530(self):
        self.assertEquals(self.calculate(869225927, 20787), 869246714)

    def test0531(self):
        self.assertEquals(self.calculate(424877903, -2055), 424875848)

    def test0532(self):
        self.assertEquals(self.calculate(1984708009, 29920), 1984737929)

    def test0533(self):
        self.assertEquals(self.calculate(-1098602239, 11060), -1098591179)

    def test0534(self):
        self.assertEquals(self.calculate(958477587, 21957), 958499544)

    def test0535(self):
        self.assertEquals(self.calculate(-837607711, -31689), -837639400)

    def test0536(self):
        self.assertEquals(self.calculate(2143543824, 17751), 2143561575)

    def test0537(self):
        self.assertEquals(self.calculate(625074210, -71), 625074139)

    def test0538(self):
        self.assertEquals(self.calculate(1730009977, -30951), 1729979026)

    def test0539(self):
        self.assertEquals(self.calculate(-690639047, 24604), -690614443)

    def test0540(self):
        self.assertEquals(self.calculate(850712619, 5634), 850718253)

    def test0541(self):
        self.assertEquals(self.calculate(-1517846328, 17528), -1517828800)

    def test0542(self):
        self.assertEquals(self.calculate(-1613655979, 24007), -1613631972)

    def test0543(self):
        self.assertEquals(self.calculate(771226442, -16833), 771209609)

    def test0544(self):
        self.assertEquals(self.calculate(-1950736546, 20923), -1950715623)

    def test0545(self):
        self.assertEquals(self.calculate(-705794822, -12851), -705807673)

    def test0546(self):
        self.assertEquals(self.calculate(-1441307609, 3716), -1441303893)

    def test0547(self):
        self.assertEquals(self.calculate(1092100012, -18154), 1092081858)

    def test0548(self):
        self.assertEquals(self.calculate(1548919472, -16849), 1548902623)

    def test0549(self):
        self.assertEquals(self.calculate(92194057, 30644), 92224701)

    def test0550(self):
        self.assertEquals(self.calculate(2093497033, 11892), 2093508925)

    def test0551(self):
        self.assertEquals(self.calculate(-966104533, -5250), -966109783)

    def test0552(self):
        self.assertEquals(self.calculate(1384779425, -13045), 1384766380)

    def test0553(self):
        self.assertEquals(self.calculate(2121136509, 17468), 2121153977)

    def test0554(self):
        self.assertEquals(self.calculate(539740898, -5680), 539735218)

    def test0555(self):
        self.assertEquals(self.calculate(2101847179, -15496), 2101831683)

    def test0556(self):
        self.assertEquals(self.calculate(1772516053, -27304), 1772488749)

    def test0557(self):
        self.assertEquals(self.calculate(519638101, 12331), 519650432)

    def test0558(self):
        self.assertEquals(self.calculate(37386409, 21032), 37407441)

    def test0559(self):
        self.assertEquals(self.calculate(295465296, -29500), 295435796)

    def test0560(self):
        self.assertEquals(self.calculate(28440282, 2127), 28442409)

    def test0561(self):
        self.assertEquals(self.calculate(-1120632420, 31493), -1120600927)

    def test0562(self):
        self.assertEquals(self.calculate(355039126, -22493), 355016633)

    def test0563(self):
        self.assertEquals(self.calculate(1112801208, -16184), 1112785024)

    def test0564(self):
        self.assertEquals(self.calculate(804537687, 21629), 804559316)

    def test0565(self):
        self.assertEquals(self.calculate(-100939891, -3963), -100943854)

    def test0566(self):
        self.assertEquals(self.calculate(128977539, 4904), 128982443)

    def test0567(self):
        self.assertEquals(self.calculate(1132883812, 20834), 1132904646)

    def test0568(self):
        self.assertEquals(self.calculate(-1727593425, -25289), -1727618714)

    def test0569(self):
        self.assertEquals(self.calculate(476356851, 3664), 476360515)

    def test0570(self):
        self.assertEquals(self.calculate(-1892172876, 29957), -1892142919)

    def test0571(self):
        self.assertEquals(self.calculate(165495814, 23728), 165519542)

    def test0572(self):
        self.assertEquals(self.calculate(1561894840, 27410), 1561922250)

    def test0573(self):
        self.assertEquals(self.calculate(-1278667910, -10104), -1278678014)

    def test0574(self):
        self.assertEquals(self.calculate(-2065221685, -29658), -2065251343)

    def test0575(self):
        self.assertEquals(self.calculate(-204315835, -30793), -204346628)

    def test0576(self):
        self.assertEquals(self.calculate(476438260, 13820), 476452080)

    def test0577(self):
        self.assertEquals(self.calculate(85316077, -8744), 85307333)

    def test0578(self):
        self.assertEquals(self.calculate(138695889, 10041), 138705930)

    def test0579(self):
        self.assertEquals(self.calculate(161200527, 28134), 161228661)

    def test0580(self):
        self.assertEquals(self.calculate(-1576904109, -1749), -1576905858)

    def test0581(self):
        self.assertEquals(self.calculate(96620403, 25122), 96645525)

    def test0582(self):
        self.assertEquals(self.calculate(1125045094, 26025), 1125071119)

    def test0583(self):
        self.assertEquals(self.calculate(-1842465100, -20459), -1842485559)

    def test0584(self):
        self.assertEquals(self.calculate(-375868024, 23119), -375844905)

    def test0585(self):
        self.assertEquals(self.calculate(1869268369, 9578), 1869277947)

    def test0586(self):
        self.assertEquals(self.calculate(1584461495, 26197), 1584487692)

    def test0587(self):
        self.assertEquals(self.calculate(1826716629, -4702), 1826711927)

    def test0588(self):
        self.assertEquals(self.calculate(2137398493, 1174), 2137399667)

    def test0589(self):
        self.assertEquals(self.calculate(225114132, 7944), 225122076)

    def test0590(self):
        self.assertEquals(self.calculate(-1604549481, -7839), -1604557320)

    def test0591(self):
        self.assertEquals(self.calculate(-295370148, 15982), -295354166)

    def test0592(self):
        self.assertEquals(self.calculate(1879821366, -28588), 1879792778)

    def test0593(self):
        self.assertEquals(self.calculate(1336473799, -12113), 1336461686)

    def test0594(self):
        self.assertEquals(self.calculate(-792150212, -4437), -792154649)

    def test0595(self):
        self.assertEquals(self.calculate(-199065097, -27031), -199092128)

    def test0596(self):
        self.assertEquals(self.calculate(-274060986, -22923), -274083909)

    def test0597(self):
        self.assertEquals(self.calculate(-1304156818, -6678), -1304163496)

    def test0598(self):
        self.assertEquals(self.calculate(1293629023, -28382), 1293600641)

    def test0599(self):
        self.assertEquals(self.calculate(2001602102, -18718), 2001583384)

    def test0600(self):
        self.assertEquals(self.calculate(-882903245, 16275), -882886970)

    def test0601(self):
        self.assertEquals(self.calculate(303403469, 19056), 303422525)

    def test0602(self):
        self.assertEquals(self.calculate(1425203797, -6114), 1425197683)

    def test0603(self):
        self.assertEquals(self.calculate(-1170062192, 25999), -1170036193)

    def test0604(self):
        self.assertEquals(self.calculate(-687318865, -13918), -687332783)

    def test0605(self):
        self.assertEquals(self.calculate(1419089035, 1571), 1419090606)

    def test0606(self):
        self.assertEquals(self.calculate(-1687264184, 2539), -1687261645)

    def test0607(self):
        self.assertEquals(self.calculate(460420680, 14359), 460435039)

    def test0608(self):
        self.assertEquals(self.calculate(-245552722, -25720), -245578442)

    def test0609(self):
        self.assertEquals(self.calculate(-1646984807, -7286), -1646992093)

    def test0610(self):
        self.assertEquals(self.calculate(-886507051, -12248), -886519299)

    def test0611(self):
        self.assertEquals(self.calculate(841863620, 30742), 841894362)

    def test0612(self):
        self.assertEquals(self.calculate(-323779846, -15260), -323795106)

    def test0613(self):
        self.assertEquals(self.calculate(1749106153, -8261), 1749097892)

    def test0614(self):
        self.assertEquals(self.calculate(-728254489, 32237), -728222252)

    def test0615(self):
        self.assertEquals(self.calculate(-43030469, 225), -43030244)

    def test0616(self):
        self.assertEquals(self.calculate(87072985, -29375), 87043610)

    def test0617(self):
        self.assertEquals(self.calculate(330933136, -9519), 330923617)

    def test0618(self):
        self.assertEquals(self.calculate(959518736, 21098), 959539834)

    def test0619(self):
        self.assertEquals(self.calculate(1445830278, -17211), 1445813067)

    def test0620(self):
        self.assertEquals(self.calculate(54798318, 4664), 54802982)

    def test0621(self):
        self.assertEquals(self.calculate(658075873, 32524), 658108397)

    def test0622(self):
        self.assertEquals(self.calculate(-820249860, -32405), -820282265)

    def test0623(self):
        self.assertEquals(self.calculate(61972781, -17230), 61955551)

    def test0624(self):
        self.assertEquals(self.calculate(1145773672, -30194), 1145743478)

    def test0625(self):
        self.assertEquals(self.calculate(206321907, 31513), 206353420)

    def test0626(self):
        self.assertEquals(self.calculate(561030672, -23555), 561007117)

    def test0627(self):
        self.assertEquals(self.calculate(-1930926839, 23645), -1930903194)

    def test0628(self):
        self.assertEquals(self.calculate(-2014955960, 15525), -2014940435)

    def test0629(self):
        self.assertEquals(self.calculate(-1554532652, -31065), -1554563717)

    def test0630(self):
        self.assertEquals(self.calculate(-1965761442, -24333), -1965785775)

    def test0631(self):
        self.assertEquals(self.calculate(1487107651, 30159), 1487137810)

    def test0632(self):
        self.assertEquals(self.calculate(-1196593760, 9210), -1196584550)

    def test0633(self):
        self.assertEquals(self.calculate(323620555, 5898), 323626453)

    def test0634(self):
        self.assertEquals(self.calculate(-24872145, -25096), -24897241)

    def test0635(self):
        self.assertEquals(self.calculate(395722834, 14319), 395737153)

    def test0636(self):
        self.assertEquals(self.calculate(1915446874, 2028), 1915448902)

    def test0637(self):
        self.assertEquals(self.calculate(-1735110297, -4266), -1735114563)

    def test0638(self):
        self.assertEquals(self.calculate(782693184, 18391), 782711575)

    def test0639(self):
        self.assertEquals(self.calculate(-95125721, 11662), -95114059)

    def test0640(self):
        self.assertEquals(self.calculate(-2062137337, -31353), -2062168690)

    def test0641(self):
        self.assertEquals(self.calculate(1961834367, -31713), 1961802654)

    def test0642(self):
        self.assertEquals(self.calculate(675345351, -15242), 675330109)

    def test0643(self):
        self.assertEquals(self.calculate(-2134317304, 4767), -2134312537)

    def test0644(self):
        self.assertEquals(self.calculate(-96913623, -17532), -96931155)

    def test0645(self):
        self.assertEquals(self.calculate(990720937, -2122), 990718815)

    def test0646(self):
        self.assertEquals(self.calculate(-1113513834, 4220), -1113509614)

    def test0647(self):
        self.assertEquals(self.calculate(983352398, 6705), 983359103)

    def test0648(self):
        self.assertEquals(self.calculate(1550260132, -14528), 1550245604)

    def test0649(self):
        self.assertEquals(self.calculate(497896318, -27626), 497868692)

    def test0650(self):
        self.assertEquals(self.calculate(-193710612, 20894), -193689718)

    def test0651(self):
        self.assertEquals(self.calculate(1444750878, -2578), 1444748300)

    def test0652(self):
        self.assertEquals(self.calculate(1736753801, 12576), 1736766377)

    def test0653(self):
        self.assertEquals(self.calculate(1999311399, -4496), 1999306903)

    def test0654(self):
        self.assertEquals(self.calculate(137805075, 18836), 137823911)

    def test0655(self):
        self.assertEquals(self.calculate(1671906112, 72), 1671906184)

    def test0656(self):
        self.assertEquals(self.calculate(275195556, 20479), 275216035)

    def test0657(self):
        self.assertEquals(self.calculate(-1386683254, -7200), -1386690454)

    def test0658(self):
        self.assertEquals(self.calculate(-357812957, 11073), -357801884)

    def test0659(self):
        self.assertEquals(self.calculate(-1285181503, 25227), -1285156276)

    def test0660(self):
        self.assertEquals(self.calculate(2109677601, 22175), 2109699776)

    def test0661(self):
        self.assertEquals(self.calculate(144152415, -15690), 144136725)

    def test0662(self):
        self.assertEquals(self.calculate(-1120297066, 7474), -1120289592)

    def test0663(self):
        self.assertEquals(self.calculate(1996383954, -16819), 1996367135)

    def test0664(self):
        self.assertEquals(self.calculate(1681494051, -25105), 1681468946)

    def test0665(self):
        self.assertEquals(self.calculate(1100623870, 32552), 1100656422)

    def test0666(self):
        self.assertEquals(self.calculate(1792881215, 16760), 1792897975)

    def test0667(self):
        self.assertEquals(self.calculate(-332359675, -27652), -332387327)

    def test0668(self):
        self.assertEquals(self.calculate(-743855281, -7699), -743862980)

    def test0669(self):
        self.assertEquals(self.calculate(-1051573997, -2837), -1051576834)

    def test0670(self):
        self.assertEquals(self.calculate(-234565573, -32212), -234597785)

    def test0671(self):
        self.assertEquals(self.calculate(-912906000, -25825), -912931825)

    def test0672(self):
        self.assertEquals(self.calculate(984083991, 6377), 984090368)

    def test0673(self):
        self.assertEquals(self.calculate(769151188, 30500), 769181688)

    def test0674(self):
        self.assertEquals(self.calculate(91615450, 20203), 91635653)

    def test0675(self):
        self.assertEquals(self.calculate(40826147, -30305), 40795842)

    def test0676(self):
        self.assertEquals(self.calculate(-798123203, -15539), -798138742)

    def test0677(self):
        self.assertEquals(self.calculate(-1850014065, 26342), -1849987723)

    def test0678(self):
        self.assertEquals(self.calculate(1264831075, -26985), 1264804090)

    def test0679(self):
        self.assertEquals(self.calculate(-552826358, -11109), -552837467)

    def test0680(self):
        self.assertEquals(self.calculate(-1002753513, -13784), -1002767297)

    def test0681(self):
        self.assertEquals(self.calculate(46039408, -6556), 46032852)

    def test0682(self):
        self.assertEquals(self.calculate(-1958969412, 25231), -1958944181)

    def test0683(self):
        self.assertEquals(self.calculate(914009460, 28719), 914038179)

    def test0684(self):
        self.assertEquals(self.calculate(-1609103648, 24861), -1609078787)

    def test0685(self):
        self.assertEquals(self.calculate(35787786, 6882), 35794668)

    def test0686(self):
        self.assertEquals(self.calculate(-1724661932, 17495), -1724644437)

    def test0687(self):
        self.assertEquals(self.calculate(-446547087, -11436), -446558523)

    def test0688(self):
        self.assertEquals(self.calculate(-1314240188, 28487), -1314211701)

    def test0689(self):
        self.assertEquals(self.calculate(-165987468, 17093), -165970375)

    def test0690(self):
        self.assertEquals(self.calculate(949321667, 13259), 949334926)

    def test0691(self):
        self.assertEquals(self.calculate(1487815651, -16765), 1487798886)

    def test0692(self):
        self.assertEquals(self.calculate(-1330332477, 25975), -1330306502)

    def test0693(self):
        self.assertEquals(self.calculate(35031804, -5559), 35026245)

    def test0694(self):
        self.assertEquals(self.calculate(994724582, 17434), 994742016)

    def test0695(self):
        self.assertEquals(self.calculate(925150346, 15958), 925166304)

    def test0696(self):
        self.assertEquals(self.calculate(-77491890, -23760), -77515650)

    def test0697(self):
        self.assertEquals(self.calculate(-1467205498, 3740), -1467201758)

    def test0698(self):
        self.assertEquals(self.calculate(-1258622649, -4334), -1258626983)

    def test0699(self):
        self.assertEquals(self.calculate(784451765, -11815), 784439950)

    def test0700(self):
        self.assertEquals(self.calculate(1377580130, -12315), 1377567815)

    def test0701(self):
        self.assertEquals(self.calculate(1388850557, 6912), 1388857469)

    def test0702(self):
        self.assertEquals(self.calculate(2074489993, 30352), 2074520345)

    def test0703(self):
        self.assertEquals(self.calculate(743141796, 21124), 743162920)

    def test0704(self):
        self.assertEquals(self.calculate(1165803342, 28188), 1165831530)

    def test0705(self):
        self.assertEquals(self.calculate(1933788916, -22805), 1933766111)

    def test0706(self):
        self.assertEquals(self.calculate(-1502281451, 22537), -1502258914)

    def test0707(self):
        self.assertEquals(self.calculate(-1719214898, -29976), -1719244874)

    def test0708(self):
        self.assertEquals(self.calculate(1781683622, 9243), 1781692865)

    def test0709(self):
        self.assertEquals(self.calculate(-656910241, -692), -656910933)

    def test0710(self):
        self.assertEquals(self.calculate(-1376710658, -122), -1376710780)

    def test0711(self):
        self.assertEquals(self.calculate(876770894, 14116), 876785010)

    def test0712(self):
        self.assertEquals(self.calculate(1704541835, 21777), 1704563612)

    def test0713(self):
        self.assertEquals(self.calculate(102011670, 14454), 102026124)

    def test0714(self):
        self.assertEquals(self.calculate(-1290054960, 30079), -1290024881)

    def test0715(self):
        self.assertEquals(self.calculate(684932591, -1166), 684931425)

    def test0716(self):
        self.assertEquals(self.calculate(1882630166, 29727), 1882659893)

    def test0717(self):
        self.assertEquals(self.calculate(1602365160, -12753), 1602352407)

    def test0718(self):
        self.assertEquals(self.calculate(-921785143, -12260), -921797403)

    def test0719(self):
        self.assertEquals(self.calculate(779930631, 15033), 779945664)

    def test0720(self):
        self.assertEquals(self.calculate(458228475, 15569), 458244044)

    def test0721(self):
        self.assertEquals(self.calculate(725203542, 5742), 725209284)

    def test0722(self):
        self.assertEquals(self.calculate(-393302061, 22630), -393279431)

    def test0723(self):
        self.assertEquals(self.calculate(1625114081, -24572), 1625089509)

    def test0724(self):
        self.assertEquals(self.calculate(1668795362, 16381), 1668811743)

    def test0725(self):
        self.assertEquals(self.calculate(1873568310, -27936), 1873540374)

    def test0726(self):
        self.assertEquals(self.calculate(-1604587064, 9744), -1604577320)

    def test0727(self):
        self.assertEquals(self.calculate(1009882630, 13323), 1009895953)

    def test0728(self):
        self.assertEquals(self.calculate(-2004230982, -31879), -2004262861)

    def test0729(self):
        self.assertEquals(self.calculate(1969394579, -10731), 1969383848)

    def test0730(self):
        self.assertEquals(self.calculate(-963111237, 17620), -963093617)

    def test0731(self):
        self.assertEquals(self.calculate(-1937771087, 18679), -1937752408)

    def test0732(self):
        self.assertEquals(self.calculate(-2036690544, -10872), -2036701416)

    def test0733(self):
        self.assertEquals(self.calculate(-1424956366, -14620), -1424970986)

    def test0734(self):
        self.assertEquals(self.calculate(327700168, -19974), 327680194)

    def test0735(self):
        self.assertEquals(self.calculate(-1965231360, -14008), -1965245368)

    def test0736(self):
        self.assertEquals(self.calculate(187146565, 157), 187146722)

    def test0737(self):
        self.assertEquals(self.calculate(-601933016, 30107), -601902909)

    def test0738(self):
        self.assertEquals(self.calculate(1762541056, 10689), 1762551745)

    def test0739(self):
        self.assertEquals(self.calculate(2126807773, 893), 2126808666)

    def test0740(self):
        self.assertEquals(self.calculate(569492049, -30206), 569461843)

    def test0741(self):
        self.assertEquals(self.calculate(1145797873, -25129), 1145772744)

    def test0742(self):
        self.assertEquals(self.calculate(788340574, 29260), 788369834)

    def test0743(self):
        self.assertEquals(self.calculate(723585653, -6975), 723578678)

    def test0744(self):
        self.assertEquals(self.calculate(-1764826501, 6845), -1764819656)

    def test0745(self):
        self.assertEquals(self.calculate(971492631, -31312), 971461319)

    def test0746(self):
        self.assertEquals(self.calculate(1527442009, 19220), 1527461229)

    def test0747(self):
        self.assertEquals(self.calculate(141436133, -19477), 141416656)

    def test0748(self):
        self.assertEquals(self.calculate(1486018467, 2731), 1486021198)

    def test0749(self):
        self.assertEquals(self.calculate(1373500166, -15672), 1373484494)

    def test0750(self):
        self.assertEquals(self.calculate(-1805422045, -9121), -1805431166)

    def test0751(self):
        self.assertEquals(self.calculate(1153539084, 30704), 1153569788)

    def test0752(self):
        self.assertEquals(self.calculate(1793580098, 8339), 1793588437)

    def test0753(self):
        self.assertEquals(self.calculate(321351998, -8458), 321343540)

    def test0754(self):
        self.assertEquals(self.calculate(-1055311972, 7177), -1055304795)

    def test0755(self):
        self.assertEquals(self.calculate(1836873261, -28970), 1836844291)

    def test0756(self):
        self.assertEquals(self.calculate(583585817, -24031), 583561786)

    def test0757(self):
        self.assertEquals(self.calculate(-548887454, -17175), -548904629)

    def test0758(self):
        self.assertEquals(self.calculate(1180993937, -2570), 1180991367)

    def test0759(self):
        self.assertEquals(self.calculate(-1537159259, 13922), -1537145337)

    def test0760(self):
        self.assertEquals(self.calculate(122626537, -13591), 122612946)

    def test0761(self):
        self.assertEquals(self.calculate(982288709, 3102), 982291811)

    def test0762(self):
        self.assertEquals(self.calculate(-1017268863, 17474), -1017251389)

    def test0763(self):
        self.assertEquals(self.calculate(1626338271, 23323), 1626361594)

    def test0764(self):
        self.assertEquals(self.calculate(156948022, -16981), 156931041)

    def test0765(self):
        self.assertEquals(self.calculate(1571287631, -19182), 1571268449)

    def test0766(self):
        self.assertEquals(self.calculate(1447609101, -6644), 1447602457)

    def test0767(self):
        self.assertEquals(self.calculate(92771456, 9321), 92780777)

    def test0768(self):
        self.assertEquals(self.calculate(-1272072545, -24935), -1272097480)

    def test0769(self):
        self.assertEquals(self.calculate(487037522, -4695), 487032827)

    def test0770(self):
        self.assertEquals(self.calculate(-302633312, 31038), -302602274)

    def test0771(self):
        self.assertEquals(self.calculate(-1122546758, -19596), -1122566354)

    def test0772(self):
        self.assertEquals(self.calculate(802411825, -24303), 802387522)

    def test0773(self):
        self.assertEquals(self.calculate(1368913615, 10690), 1368924305)

    def test0774(self):
        self.assertEquals(self.calculate(-1057314695, -19172), -1057333867)

    def test0775(self):
        self.assertEquals(self.calculate(328903584, 15086), 328918670)

    def test0776(self):
        self.assertEquals(self.calculate(977524678, -47), 977524631)

    def test0777(self):
        self.assertEquals(self.calculate(-1040634747, 24025), -1040610722)

    def test0778(self):
        self.assertEquals(self.calculate(613789675, -9297), 613780378)

    def test0779(self):
        self.assertEquals(self.calculate(-326428735, -27273), -326456008)

    def test0780(self):
        self.assertEquals(self.calculate(366655871, -16563), 366639308)

    def test0781(self):
        self.assertEquals(self.calculate(-1716837230, -27879), -1716865109)

    def test0782(self):
        self.assertEquals(self.calculate(1343417142, -12183), 1343404959)

    def test0783(self):
        self.assertEquals(self.calculate(2029648979, -15018), 2029633961)

    def test0784(self):
        self.assertEquals(self.calculate(-1256009838, 11738), -1255998100)

    def test0785(self):
        self.assertEquals(self.calculate(1867576908, 7216), 1867584124)

    def test0786(self):
        self.assertEquals(self.calculate(-431811216, -10508), -431821724)

    def test0787(self):
        self.assertEquals(self.calculate(410133892, -27131), 410106761)

    def test0788(self):
        self.assertEquals(self.calculate(-2040494103, 30722), -2040463381)

    def test0789(self):
        self.assertEquals(self.calculate(-310742362, 3333), -310739029)

    def test0790(self):
        self.assertEquals(self.calculate(-1779217079, -3635), -1779220714)

    def test0791(self):
        self.assertEquals(self.calculate(-1756177320, -628), -1756177948)

    def test0792(self):
        self.assertEquals(self.calculate(-1287881372, 14953), -1287866419)

    def test0793(self):
        self.assertEquals(self.calculate(-2110053773, -11315), -2110065088)

    def test0794(self):
        self.assertEquals(self.calculate(1464673251, -10856), 1464662395)

    def test0795(self):
        self.assertEquals(self.calculate(1871176205, 20747), 1871196952)

    def test0796(self):
        self.assertEquals(self.calculate(758225223, 3263), 758228486)

    def test0797(self):
        self.assertEquals(self.calculate(-273004704, -28417), -273033121)

    def test0798(self):
        self.assertEquals(self.calculate(-141982450, 14043), -141968407)

    def test0799(self):
        self.assertEquals(self.calculate(211899885, 22755), 211922640)

    def test0800(self):
        self.assertEquals(self.calculate(1171491005, 24201), 1171515206)

    def test0801(self):
        self.assertEquals(self.calculate(-148875101, -20368), -148895469)

    def test0802(self):
        self.assertEquals(self.calculate(1763077850, 17045), 1763094895)

    def test0803(self):
        self.assertEquals(self.calculate(1856331809, 6704), 1856338513)

    def test0804(self):
        self.assertEquals(self.calculate(602578855, -11865), 602566990)

    def test0805(self):
        self.assertEquals(self.calculate(-1684228740, 25237), -1684203503)

    def test0806(self):
        self.assertEquals(self.calculate(-866533693, 4436), -866529257)

    def test0807(self):
        self.assertEquals(self.calculate(-1395681106, 2651), -1395678455)

    def test0808(self):
        self.assertEquals(self.calculate(-1408301511, 22985), -1408278526)

    def test0809(self):
        self.assertEquals(self.calculate(278954135, -30991), 278923144)

    def test0810(self):
        self.assertEquals(self.calculate(-634075631, -8791), -634084422)

    def test0811(self):
        self.assertEquals(self.calculate(705411497, -4000), 705407497)

    def test0812(self):
        self.assertEquals(self.calculate(-1062878149, -16534), -1062894683)

    def test0813(self):
        self.assertEquals(self.calculate(1258062397, -7012), 1258055385)

    def test0814(self):
        self.assertEquals(self.calculate(1594488519, -4890), 1594483629)

    def test0815(self):
        self.assertEquals(self.calculate(-453883395, 23542), -453859853)

    def test0816(self):
        self.assertEquals(self.calculate(385092158, -26237), 385065921)

    def test0817(self):
        self.assertEquals(self.calculate(-1819519277, -23888), -1819543165)

    def test0818(self):
        self.assertEquals(self.calculate(1421753439, 7274), 1421760713)

    def test0819(self):
        self.assertEquals(self.calculate(1437026418, 10081), 1437036499)

    def test0820(self):
        self.assertEquals(self.calculate(-1160489906, 28512), -1160461394)

    def test0821(self):
        self.assertEquals(self.calculate(-391034357, 28839), -391005518)

    def test0822(self):
        self.assertEquals(self.calculate(1728410328, -1149), 1728409179)

    def test0823(self):
        self.assertEquals(self.calculate(1296732793, -19414), 1296713379)

    def test0824(self):
        self.assertEquals(self.calculate(1615025407, -19711), 1615005696)

    def test0825(self):
        self.assertEquals(self.calculate(-364394394, -1299), -364395693)

    def test0826(self):
        self.assertEquals(self.calculate(-310151653, 9453), -310142200)

    def test0827(self):
        self.assertEquals(self.calculate(1522004655, 9573), 1522014228)

    def test0828(self):
        self.assertEquals(self.calculate(519316004, 8366), 519324370)

    def test0829(self):
        self.assertEquals(self.calculate(-1566680082, 32284), -1566647798)

    def test0830(self):
        self.assertEquals(self.calculate(655507250, 5482), 655512732)

    def test0831(self):
        self.assertEquals(self.calculate(-664918262, 25102), -664893160)

    def test0832(self):
        self.assertEquals(self.calculate(1849034547, -11578), 1849022969)

    def test0833(self):
        self.assertEquals(self.calculate(-298664685, 19430), -298645255)

    def test0834(self):
        self.assertEquals(self.calculate(435493514, 3790), 435497304)

    def test0835(self):
        self.assertEquals(self.calculate(174555991, 23584), 174579575)

    def test0836(self):
        self.assertEquals(self.calculate(1167258944, -20499), 1167238445)

    def test0837(self):
        self.assertEquals(self.calculate(-95408938, -13066), -95422004)

    def test0838(self):
        self.assertEquals(self.calculate(712634239, -24248), 712609991)

    def test0839(self):
        self.assertEquals(self.calculate(-670642248, -25697), -670667945)

    def test0840(self):
        self.assertEquals(self.calculate(-2100748487, 21789), -2100726698)

    def test0841(self):
        self.assertEquals(self.calculate(-599197178, -27123), -599224301)

    def test0842(self):
        self.assertEquals(self.calculate(1985654876, -26805), 1985628071)

    def test0843(self):
        self.assertEquals(self.calculate(-1992323615, 10451), -1992313164)

    def test0844(self):
        self.assertEquals(self.calculate(-1455758741, -13753), -1455772494)

    def test0845(self):
        self.assertEquals(self.calculate(-453356259, -10193), -453366452)

    def test0846(self):
        self.assertEquals(self.calculate(-947051282, 19311), -947031971)

    def test0847(self):
        self.assertEquals(self.calculate(-412827141, 10227), -412816914)

    def test0848(self):
        self.assertEquals(self.calculate(-2019772335, -13365), -2019785700)

    def test0849(self):
        self.assertEquals(self.calculate(2024853009, -11453), 2024841556)

    def test0850(self):
        self.assertEquals(self.calculate(1890877627, 4495), 1890882122)

    def test0851(self):
        self.assertEquals(self.calculate(-716363895, -29868), -716393763)

    def test0852(self):
        self.assertEquals(self.calculate(742500629, -28682), 742471947)

    def test0853(self):
        self.assertEquals(self.calculate(1136343301, -27631), 1136315670)

    def test0854(self):
        self.assertEquals(self.calculate(-299368379, -341), -299368720)

    def test0855(self):
        self.assertEquals(self.calculate(1473941423, -31230), 1473910193)

    def test0856(self):
        self.assertEquals(self.calculate(-762759468, -16506), -762775974)

    def test0857(self):
        self.assertEquals(self.calculate(-552348868, 29336), -552319532)

    def test0858(self):
        self.assertEquals(self.calculate(1089393864, 27849), 1089421713)

    def test0859(self):
        self.assertEquals(self.calculate(-774992709, -4340), -774997049)

    def test0860(self):
        self.assertEquals(self.calculate(362273905, -18922), 362254983)

    def test0861(self):
        self.assertEquals(self.calculate(740342678, -15366), 740327312)

    def test0862(self):
        self.assertEquals(self.calculate(804853251, -28199), 804825052)

    def test0863(self):
        self.assertEquals(self.calculate(1216998878, -3863), 1216995015)

    def test0864(self):
        self.assertEquals(self.calculate(-1610801667, -12080), -1610813747)

    def test0865(self):
        self.assertEquals(self.calculate(-1190483946, -23290), -1190507236)

    def test0866(self):
        self.assertEquals(self.calculate(2071456617, -18817), 2071437800)

    def test0867(self):
        self.assertEquals(self.calculate(-764560704, -15550), -764576254)

    def test0868(self):
        self.assertEquals(self.calculate(-1377379386, 5673), -1377373713)

    def test0869(self):
        self.assertEquals(self.calculate(-96198414, -6807), -96205221)

    def test0870(self):
        self.assertEquals(self.calculate(1565630490, -17113), 1565613377)

    def test0871(self):
        self.assertEquals(self.calculate(1425952081, 10287), 1425962368)

    def test0872(self):
        self.assertEquals(self.calculate(113063192, -4569), 113058623)

    def test0873(self):
        self.assertEquals(self.calculate(1838120321, 20125), 1838140446)

    def test0874(self):
        self.assertEquals(self.calculate(1318438690, 15269), 1318453959)

    def test0875(self):
        self.assertEquals(self.calculate(-2067363710, 24242), -2067339468)

    def test0876(self):
        self.assertEquals(self.calculate(-1872152007, 29524), -1872122483)

    def test0877(self):
        self.assertEquals(self.calculate(-32819932, 27288), -32792644)

    def test0878(self):
        self.assertEquals(self.calculate(643581877, 24168), 643606045)

    def test0879(self):
        self.assertEquals(self.calculate(-783107116, -12114), -783119230)

    def test0880(self):
        self.assertEquals(self.calculate(42012025, -22590), 41989435)

    def test0881(self):
        self.assertEquals(self.calculate(-1199731571, 7037), -1199724534)

    def test0882(self):
        self.assertEquals(self.calculate(-2074655454, 15086), -2074640368)

    def test0883(self):
        self.assertEquals(self.calculate(441397771, 8584), 441406355)

    def test0884(self):
        self.assertEquals(self.calculate(-750929199, -29970), -750959169)

    def test0885(self):
        self.assertEquals(self.calculate(-1240151460, -7060), -1240158520)

    def test0886(self):
        self.assertEquals(self.calculate(-1930675250, -12054), -1930687304)

    def test0887(self):
        self.assertEquals(self.calculate(-166707003, 14633), -166692370)

    def test0888(self):
        self.assertEquals(self.calculate(573204865, 4765), 573209630)

    def test0889(self):
        self.assertEquals(self.calculate(-615911974, -15403), -615927377)

    def test0890(self):
        self.assertEquals(self.calculate(776211272, -1782), 776209490)

    def test0891(self):
        self.assertEquals(self.calculate(-1025902922, 24713), -1025878209)

    def test0892(self):
        self.assertEquals(self.calculate(-1083201427, 4252), -1083197175)

    def test0893(self):
        self.assertEquals(self.calculate(-1322545512, -29369), -1322574881)

    def test0894(self):
        self.assertEquals(self.calculate(-610628800, -22670), -610651470)

    def test0895(self):
        self.assertEquals(self.calculate(981036212, 3866), 981040078)

    def test0896(self):
        self.assertEquals(self.calculate(-315271566, -25812), -315297378)

    def test0897(self):
        self.assertEquals(self.calculate(1779701701, -22114), 1779679587)

    def test0898(self):
        self.assertEquals(self.calculate(1098533511, 372), 1098533883)

    def test0899(self):
        self.assertEquals(self.calculate(-1003398302, -6985), -1003405287)

    def test0900(self):
        self.assertEquals(self.calculate(660066970, -19959), 660047011)

    def test0901(self):
        self.assertEquals(self.calculate(-481911543, 14506), -481897037)

    def test0902(self):
        self.assertEquals(self.calculate(-2100759099, -25299), -2100784398)

    def test0903(self):
        self.assertEquals(self.calculate(1957532851, 6585), 1957539436)

    def test0904(self):
        self.assertEquals(self.calculate(-1088686050, -28300), -1088714350)

    def test0905(self):
        self.assertEquals(self.calculate(-75133526, 23), -75133503)

    def test0906(self):
        self.assertEquals(self.calculate(185738678, 7480), 185746158)

    def test0907(self):
        self.assertEquals(self.calculate(1930379172, -20702), 1930358470)

    def test0908(self):
        self.assertEquals(self.calculate(2107395219, -11320), 2107383899)

    def test0909(self):
        self.assertEquals(self.calculate(2108453034, -5640), 2108447394)

    def test0910(self):
        self.assertEquals(self.calculate(45543993, 22791), 45566784)

    def test0911(self):
        self.assertEquals(self.calculate(892234597, 25197), 892259794)

    def test0912(self):
        self.assertEquals(self.calculate(1863435166, 28257), 1863463423)

    def test0913(self):
        self.assertEquals(self.calculate(2112661654, -21873), 2112639781)

    def test0914(self):
        self.assertEquals(self.calculate(-382594766, -13429), -382608195)

    def test0915(self):
        self.assertEquals(self.calculate(1213304961, -30215), 1213274746)

    def test0916(self):
        self.assertEquals(self.calculate(1208287369, 24926), 1208312295)

    def test0917(self):
        self.assertEquals(self.calculate(80680689, -31542), 80649147)

    def test0918(self):
        self.assertEquals(self.calculate(-86820045, 15133), -86804912)

    def test0919(self):
        self.assertEquals(self.calculate(-937873665, 31182), -937842483)

    def test0920(self):
        self.assertEquals(self.calculate(-1508468149, -18167), -1508486316)

    def test0921(self):
        self.assertEquals(self.calculate(-2013080413, 6847), -2013073566)

    def test0922(self):
        self.assertEquals(self.calculate(-1233655314, -26358), -1233681672)

    def test0923(self):
        self.assertEquals(self.calculate(1955239941, 31367), 1955271308)

    def test0924(self):
        self.assertEquals(self.calculate(240028863, -15355), 240013508)

    def test0925(self):
        self.assertEquals(self.calculate(-1663532510, 15220), -1663517290)

    def test0926(self):
        self.assertEquals(self.calculate(1448006970, 10593), 1448017563)

    def test0927(self):
        self.assertEquals(self.calculate(-1027605211, -12467), -1027617678)

    def test0928(self):
        self.assertEquals(self.calculate(770518822, 30418), 770549240)

    def test0929(self):
        self.assertEquals(self.calculate(-735735014, -6719), -735741733)

    def test0930(self):
        self.assertEquals(self.calculate(-1789449021, -26209), -1789475230)

    def test0931(self):
        self.assertEquals(self.calculate(342832248, -21074), 342811174)

    def test0932(self):
        self.assertEquals(self.calculate(-1265157580, 21875), -1265135705)

    def test0933(self):
        self.assertEquals(self.calculate(-1385660806, -13381), -1385674187)

    def test0934(self):
        self.assertEquals(self.calculate(-766188080, -6025), -766194105)

    def test0935(self):
        self.assertEquals(self.calculate(-912239750, -12712), -912252462)

    def test0936(self):
        self.assertEquals(self.calculate(245542909, -7082), 245535827)

    def test0937(self):
        self.assertEquals(self.calculate(-2098119410, 11565), -2098107845)

    def test0938(self):
        self.assertEquals(self.calculate(905490330, -2562), 905487768)

    def test0939(self):
        self.assertEquals(self.calculate(1901109614, -5785), 1901103829)

    def test0940(self):
        self.assertEquals(self.calculate(935259714, 10345), 935270059)

    def test0941(self):
        self.assertEquals(self.calculate(1506882205, -8652), 1506873553)

    def test0942(self):
        self.assertEquals(self.calculate(-1254418315, -26010), -1254444325)

    def test0943(self):
        self.assertEquals(self.calculate(711609344, 16183), 711625527)

    def test0944(self):
        self.assertEquals(self.calculate(-1196665964, 28840), -1196637124)

    def test0945(self):
        self.assertEquals(self.calculate(466987144, -29370), 466957774)

    def test0946(self):
        self.assertEquals(self.calculate(1551731149, -25770), 1551705379)

    def test0947(self):
        self.assertEquals(self.calculate(1041707891, 22325), 1041730216)

    def test0948(self):
        self.assertEquals(self.calculate(-85859235, 11876), -85847359)

    def test0949(self):
        self.assertEquals(self.calculate(-569373930, 7541), -569366389)

    def test0950(self):
        self.assertEquals(self.calculate(-1856660591, -2147), -1856662738)

    def test0951(self):
        self.assertEquals(self.calculate(-1757655793, 6425), -1757649368)

    def test0952(self):
        self.assertEquals(self.calculate(639933755, 21673), 639955428)

    def test0953(self):
        self.assertEquals(self.calculate(354944922, 10473), 354955395)

    def test0954(self):
        self.assertEquals(self.calculate(54010171, 23488), 54033659)

    def test0955(self):
        self.assertEquals(self.calculate(1378745184, 13007), 1378758191)

    def test0956(self):
        self.assertEquals(self.calculate(-981572880, -18467), -981591347)

    def test0957(self):
        self.assertEquals(self.calculate(592509849, -3811), 592506038)

    def test0958(self):
        self.assertEquals(self.calculate(51827218, 14936), 51842154)

    def test0959(self):
        self.assertEquals(self.calculate(-935655269, -20437), -935675706)

    def test0960(self):
        self.assertEquals(self.calculate(-247043115, 11888), -247031227)

    def test0961(self):
        self.assertEquals(self.calculate(-1471810727, -10181), -1471820908)

    def test0962(self):
        self.assertEquals(self.calculate(-1948034528, -20998), -1948055526)

    def test0963(self):
        self.assertEquals(self.calculate(-1931078623, 15635), -1931062988)

    def test0964(self):
        self.assertEquals(self.calculate(-1835760793, -11941), -1835772734)

    def test0965(self):
        self.assertEquals(self.calculate(311768747, 12860), 311781607)

    def test0966(self):
        self.assertEquals(self.calculate(-1197954940, -21446), -1197976386)

    def test0967(self):
        self.assertEquals(self.calculate(-772779888, -2730), -772782618)

    def test0968(self):
        self.assertEquals(self.calculate(-1814466207, 7829), -1814458378)

    def test0969(self):
        self.assertEquals(self.calculate(-258906898, 24203), -258882695)

    def test0970(self):
        self.assertEquals(self.calculate(-1551369942, 16538), -1551353404)

    def test0971(self):
        self.assertEquals(self.calculate(777776475, 25329), 777801804)

    def test0972(self):
        self.assertEquals(self.calculate(1558537663, 483), 1558538146)

    def test0973(self):
        self.assertEquals(self.calculate(1649842352, 78), 1649842430)

    def test0974(self):
        self.assertEquals(self.calculate(-432089668, -9509), -432099177)

    def test0975(self):
        self.assertEquals(self.calculate(-1927441975, -3662), -1927445637)

    def test0976(self):
        self.assertEquals(self.calculate(-35012220, 22417), -34989803)

    def test0977(self):
        self.assertEquals(self.calculate(-703383172, -14225), -703397397)

    def test0978(self):
        self.assertEquals(self.calculate(-1432268386, -9479), -1432277865)

    def test0979(self):
        self.assertEquals(self.calculate(1879427240, -10268), 1879416972)

    def test0980(self):
        self.assertEquals(self.calculate(144383411, 23634), 144407045)

    def test0981(self):
        self.assertEquals(self.calculate(1520877971, 29610), 1520907581)

    def test0982(self):
        self.assertEquals(self.calculate(-1322456011, -18826), -1322474837)

    def test0983(self):
        self.assertEquals(self.calculate(-576736880, 8133), -576728747)

    def test0984(self):
        self.assertEquals(self.calculate(-1360639068, 17314), -1360621754)

    def test0985(self):
        self.assertEquals(self.calculate(-572266566, -23050), -572289616)

    def test0986(self):
        self.assertEquals(self.calculate(2141976166, -3086), 2141973080)

    def test0987(self):
        self.assertEquals(self.calculate(1593586725, -10269), 1593576456)

    def test0988(self):
        self.assertEquals(self.calculate(-1040994987, 24641), -1040970346)

    def test0989(self):
        self.assertEquals(self.calculate(-210750673, -10266), -210760939)

    def test0990(self):
        self.assertEquals(self.calculate(1287769036, 9589), 1287778625)

    def test0991(self):
        self.assertEquals(self.calculate(756085839, -24109), 756061730)

    def test0992(self):
        self.assertEquals(self.calculate(-1089896717, 18945), -1089877772)

    def test0993(self):
        self.assertEquals(self.calculate(1835618467, 4610), 1835623077)

    def test0994(self):
        self.assertEquals(self.calculate(-654143039, 7400), -654135639)

    def test0995(self):
        self.assertEquals(self.calculate(1633633944, 18338), 1633652282)

    def test0996(self):
        self.assertEquals(self.calculate(-1881445905, 11374), -1881434531)

    def test0997(self):
        self.assertEquals(self.calculate(-95054450, 19716), -95034734)

    def test0998(self):
        self.assertEquals(self.calculate(650034102, 7355), 650041457)

    def test0999(self):
        self.assertEquals(self.calculate(674878548, 15990), 674894538)

    def test1000(self):
        self.assertEquals(self.calculate(-2066343567, 31697), -2066311870)

    def test1001(self):
        self.assertEquals(self.calculate(872189586, 24033), 872213619)

    def test1002(self):
        self.assertEquals(self.calculate(1141233733, 8005), 1141241738)

    def test1003(self):
        self.assertEquals(self.calculate(-807623908, -29313), -807653221)

    def test1004(self):
        self.assertEquals(self.calculate(-825077615, -20991), -825098606)

    def test1005(self):
        self.assertEquals(self.calculate(1890798479, -17965), 1890780514)

    def test1006(self):
        self.assertEquals(self.calculate(-1250389356, -14660), -1250404016)

    def test1007(self):
        self.assertEquals(self.calculate(-1393083941, 32489), -1393051452)

    def test1008(self):
        self.assertEquals(self.calculate(25975447, -19816), 25955631)

    def test1009(self):
        self.assertEquals(self.calculate(-1012735968, 2690), -1012733278)

    def test1010(self):
        self.assertEquals(self.calculate(418853180, -26486), 418826694)

    def test1011(self):
        self.assertEquals(self.calculate(1397197907, 348), 1397198255)

    def test1012(self):
        self.assertEquals(self.calculate(-2084980559, 20324), -2084960235)

    def test1013(self):
        self.assertEquals(self.calculate(-2116046350, 13222), -2116033128)

    def test1014(self):
        self.assertEquals(self.calculate(10355654, 4798), 10360452)

    def test1015(self):
        self.assertEquals(self.calculate(1326049932, 14304), 1326064236)

    def test1016(self):
        self.assertEquals(self.calculate(2011322891, 14953), 2011337844)

    def test1017(self):
        self.assertEquals(self.calculate(-1349631836, 21617), -1349610219)

    def test1018(self):
        self.assertEquals(self.calculate(-935267291, 4573), -935262718)

    def test1019(self):
        self.assertEquals(self.calculate(399791430, 1819), 399793249)

    def test1020(self):
        self.assertEquals(self.calculate(1712381950, -8643), 1712373307)

    def test1021(self):
        self.assertEquals(self.calculate(-1260260653, 24392), -1260236261)

    def test1022(self):
        self.assertEquals(self.calculate(-601026375, 19699), -601006676)

    def test1023(self):
        self.assertEquals(self.calculate(-2010526006, 10874), -2010515132)




class TestVM_Add_LongLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushL(rhs)
        v.VM_Add()
        res = v.VM_PopL()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(1306646907, 1848643647), -1139676742)

    def test0001(self):
        self.assertEquals(self.calculate(-538472339, 83528923), -454943416)

    def test0002(self):
        self.assertEquals(self.calculate(1883565519, -1249239191), 634326328)

    def test0003(self):
        self.assertEquals(self.calculate(560523426, 411616975), 972140401)

    def test0004(self):
        self.assertEquals(self.calculate(-1037580925, -550065709), -1587646634)

    def test0005(self):
        self.assertEquals(self.calculate(1981990062, 954646409), -1358330825)

    def test0006(self):
        self.assertEquals(self.calculate(844604411, -402206752), 442397659)

    def test0007(self):
        self.assertEquals(self.calculate(-172564231, 1748998954), 1576434723)

    def test0008(self):
        self.assertEquals(self.calculate(-1454755061, -55998933), -1510753994)

    def test0009(self):
        self.assertEquals(self.calculate(1985494663, 1056087477), -1253385156)

    def test0010(self):
        self.assertEquals(self.calculate(-191879285, 1819846324), 1627967039)

    def test0011(self):
        self.assertEquals(self.calculate(-1426833900, -512932898), -1939766798)

    def test0012(self):
        self.assertEquals(self.calculate(-976421584, -590384324), -1566805908)

    def test0013(self):
        self.assertEquals(self.calculate(1843648747, -2071834308), -228185561)

    def test0014(self):
        self.assertEquals(self.calculate(-274220954, 1862845943), 1588624989)

    def test0015(self):
        self.assertEquals(self.calculate(437253769, 575220687), 1012474456)

    def test0016(self):
        self.assertEquals(self.calculate(-831744332, 785954426), -45789906)

    def test0017(self):
        self.assertEquals(self.calculate(2028608692, -1163752917), 864855775)

    def test0018(self):
        self.assertEquals(self.calculate(-1087838015, 995148079), -92689936)

    def test0019(self):
        self.assertEquals(self.calculate(-1439623750, -846655105), 2008688441)

    def test0020(self):
        self.assertEquals(self.calculate(256972862, -1077400921), -820428059)

    def test0021(self):
        self.assertEquals(self.calculate(618293807, 1090215066), 1708508873)

    def test0022(self):
        self.assertEquals(self.calculate(-652930644, -493412765), -1146343409)

    def test0023(self):
        self.assertEquals(self.calculate(1156065110, -967142069), 188923041)

    def test0024(self):
        self.assertEquals(self.calculate(-721369161, -2037211184), 1536386951)

    def test0025(self):
        self.assertEquals(self.calculate(245984924, -199224995), 46759929)

    def test0026(self):
        self.assertEquals(self.calculate(1593748044, -1104082137), 489665907)

    def test0027(self):
        self.assertEquals(self.calculate(-106326394, 1980555042), 1874228648)

    def test0028(self):
        self.assertEquals(self.calculate(-280328060, -1340784022), -1621112082)

    def test0029(self):
        self.assertEquals(self.calculate(1854069208, -798257455), 1055811753)

    def test0030(self):
        self.assertEquals(self.calculate(1346748263, -1174070852), 172677411)

    def test0031(self):
        self.assertEquals(self.calculate(1964649273, -533645861), 1431003412)

    def test0032(self):
        self.assertEquals(self.calculate(-1092086338, -945782509), -2037868847)

    def test0033(self):
        self.assertEquals(self.calculate(-908660202, -229543990), -1138204192)

    def test0034(self):
        self.assertEquals(self.calculate(1693022822, -123841545), 1569181277)

    def test0035(self):
        self.assertEquals(self.calculate(-1268639490, 889942037), -378697453)

    def test0036(self):
        self.assertEquals(self.calculate(1649385865, -1892534116), -243148251)

    def test0037(self):
        self.assertEquals(self.calculate(-343657266, -666878070), -1010535336)

    def test0038(self):
        self.assertEquals(self.calculate(1180348431, -1925865252), -745516821)

    def test0039(self):
        self.assertEquals(self.calculate(-1015136874, -1879131058), 1400699364)

    def test0040(self):
        self.assertEquals(self.calculate(-507091745, 1877567100), 1370475355)

    def test0041(self):
        self.assertEquals(self.calculate(-737351647, 165004743), -572346904)

    def test0042(self):
        self.assertEquals(self.calculate(-831239051, -1866879628), 1596848617)

    def test0043(self):
        self.assertEquals(self.calculate(-1958299574, -706386171), 1630281551)

    def test0044(self):
        self.assertEquals(self.calculate(293931247, -76271267), 217659980)

    def test0045(self):
        self.assertEquals(self.calculate(-782699683, -1772628805), 1739638808)

    def test0046(self):
        self.assertEquals(self.calculate(1979932904, 558259425), -1756774967)

    def test0047(self):
        self.assertEquals(self.calculate(-2011581364, -715757275), 1567628657)

    def test0048(self):
        self.assertEquals(self.calculate(817951300, 550508281), 1368459581)

    def test0049(self):
        self.assertEquals(self.calculate(-2081462208, -338050024), 1875455064)

    def test0050(self):
        self.assertEquals(self.calculate(1636811266, -2125869049), -489057783)

    def test0051(self):
        self.assertEquals(self.calculate(-536380509, 148967823), -387412686)

    def test0052(self):
        self.assertEquals(self.calculate(907392503, 1870732722), -1516842071)

    def test0053(self):
        self.assertEquals(self.calculate(2026081344, 1275338556), -993547396)

    def test0054(self):
        self.assertEquals(self.calculate(-1149757374, -1891539882), 1253670040)

    def test0055(self):
        self.assertEquals(self.calculate(-1982741374, -592788313), 1719437609)

    def test0056(self):
        self.assertEquals(self.calculate(1559793297, 379197421), 1938990718)

    def test0057(self):
        self.assertEquals(self.calculate(2022960440, 798232833), -1473774023)

    def test0058(self):
        self.assertEquals(self.calculate(1521113831, -180147130), 1340966701)

    def test0059(self):
        self.assertEquals(self.calculate(2082160247, 1956357689), -256449360)

    def test0060(self):
        self.assertEquals(self.calculate(-579460609, 1786167641), 1206707032)

    def test0061(self):
        self.assertEquals(self.calculate(-1994529617, -1017434326), 1283003353)

    def test0062(self):
        self.assertEquals(self.calculate(-458092183, 186658695), -271433488)

    def test0063(self):
        self.assertEquals(self.calculate(971777699, 2142313438), -1180876159)

    def test0064(self):
        self.assertEquals(self.calculate(-487075955, 173341977), -313733978)

    def test0065(self):
        self.assertEquals(self.calculate(361853307, 1093523566), 1455376873)

    def test0066(self):
        self.assertEquals(self.calculate(141550954, 1800667467), 1942218421)

    def test0067(self):
        self.assertEquals(self.calculate(2008066945, -1931451197), 76615748)

    def test0068(self):
        self.assertEquals(self.calculate(2032845172, -773839163), 1259006009)

    def test0069(self):
        self.assertEquals(self.calculate(1980680281, 1170372223), -1143914792)

    def test0070(self):
        self.assertEquals(self.calculate(595601779, -1350758565), -755156786)

    def test0071(self):
        self.assertEquals(self.calculate(-930063227, 453032354), -477030873)

    def test0072(self):
        self.assertEquals(self.calculate(-1703256770, -1695988148), 895722378)

    def test0073(self):
        self.assertEquals(self.calculate(-732285845, 329842488), -402443357)

    def test0074(self):
        self.assertEquals(self.calculate(-1424479612, 1275330614), -149148998)

    def test0075(self):
        self.assertEquals(self.calculate(-1169298665, 1562986809), 393688144)

    def test0076(self):
        self.assertEquals(self.calculate(313021147, 1762571994), 2075593141)

    def test0077(self):
        self.assertEquals(self.calculate(1092905315, -1512773183), -419867868)

    def test0078(self):
        self.assertEquals(self.calculate(769815321, -1882502125), -1112686804)

    def test0079(self):
        self.assertEquals(self.calculate(-1131745672, -1611063206), 1552158418)

    def test0080(self):
        self.assertEquals(self.calculate(-1012016453, 581614897), -430401556)

    def test0081(self):
        self.assertEquals(self.calculate(1171323914, 1725306109), -1398337273)

    def test0082(self):
        self.assertEquals(self.calculate(1745870495, -1861448061), -115577566)

    def test0083(self):
        self.assertEquals(self.calculate(1029661243, 1538886309), -1726419744)

    def test0084(self):
        self.assertEquals(self.calculate(-1126042379, -1534428927), 1634495990)

    def test0085(self):
        self.assertEquals(self.calculate(-59611864, -630684827), -690296691)

    def test0086(self):
        self.assertEquals(self.calculate(-511644592, -1054662908), -1566307500)

    def test0087(self):
        self.assertEquals(self.calculate(-1379605838, -1168098222), 1747263236)

    def test0088(self):
        self.assertEquals(self.calculate(-655052519, -988397753), -1643450272)

    def test0089(self):
        self.assertEquals(self.calculate(935150725, 728770845), 1663921570)

    def test0090(self):
        self.assertEquals(self.calculate(1857490575, 1635864548), -801612173)

    def test0091(self):
        self.assertEquals(self.calculate(1389410177, -780236239), 609173938)

    def test0092(self):
        self.assertEquals(self.calculate(-543001901, -1449262334), -1992264235)

    def test0093(self):
        self.assertEquals(self.calculate(-320215971, 437439973), 117224002)

    def test0094(self):
        self.assertEquals(self.calculate(1373214248, 1959147568), -962605480)

    def test0095(self):
        self.assertEquals(self.calculate(442488854, 1857644048), -1994834394)

    def test0096(self):
        self.assertEquals(self.calculate(653857854, 2123575324), -1517534118)

    def test0097(self):
        self.assertEquals(self.calculate(-1520544551, -672655463), 2101767282)

    def test0098(self):
        self.assertEquals(self.calculate(-1129796192, 370425366), -759370826)

    def test0099(self):
        self.assertEquals(self.calculate(248745441, -1777390832), -1528645391)

    def test0100(self):
        self.assertEquals(self.calculate(-1196282539, 1663528313), 467245774)

    def test0101(self):
        self.assertEquals(self.calculate(-319133329, -719763821), -1038897150)

    def test0102(self):
        self.assertEquals(self.calculate(-534609325, 1261835360), 727226035)

    def test0103(self):
        self.assertEquals(self.calculate(656797560, -2015647545), -1358849985)

    def test0104(self):
        self.assertEquals(self.calculate(-1675150072, -33224572), -1708374644)

    def test0105(self):
        self.assertEquals(self.calculate(417959555, 88301058), 506260613)

    def test0106(self):
        self.assertEquals(self.calculate(624806171, 1055161216), 1679967387)

    def test0107(self):
        self.assertEquals(self.calculate(-115784864, 298503935), 182719071)

    def test0108(self):
        self.assertEquals(self.calculate(-788513286, 534512461), -254000825)

    def test0109(self):
        self.assertEquals(self.calculate(1020667857, 900371563), 1921039420)

    def test0110(self):
        self.assertEquals(self.calculate(-1051174492, -1341371175), 1902421629)

    def test0111(self):
        self.assertEquals(self.calculate(-985049205, 1653057736), 668008531)

    def test0112(self):
        self.assertEquals(self.calculate(962611180, -109713232), 852897948)

    def test0113(self):
        self.assertEquals(self.calculate(-1822570910, -1926005575), 546390811)

    def test0114(self):
        self.assertEquals(self.calculate(193401796, -1243793541), -1050391745)

    def test0115(self):
        self.assertEquals(self.calculate(210817920, 837133577), 1047951497)

    def test0116(self):
        self.assertEquals(self.calculate(447662209, 1362556210), 1810218419)

    def test0117(self):
        self.assertEquals(self.calculate(-731314326, -1520533223), 2043119747)

    def test0118(self):
        self.assertEquals(self.calculate(1453400734, -77764215), 1375636519)

    def test0119(self):
        self.assertEquals(self.calculate(-144280434, -1116716141), -1260996575)

    def test0120(self):
        self.assertEquals(self.calculate(56414871, 1244934870), 1301349741)

    def test0121(self):
        self.assertEquals(self.calculate(-1120280431, -407510221), -1527790652)

    def test0122(self):
        self.assertEquals(self.calculate(734803234, 808755117), 1543558351)

    def test0123(self):
        self.assertEquals(self.calculate(-553945061, -1192848422), -1746793483)

    def test0124(self):
        self.assertEquals(self.calculate(670137598, -1596064577), -925926979)

    def test0125(self):
        self.assertEquals(self.calculate(535929558, -554761204), -18831646)

    def test0126(self):
        self.assertEquals(self.calculate(564534717, 1814225014), -1916207565)

    def test0127(self):
        self.assertEquals(self.calculate(-1607940114, 264455862), -1343484252)

    def test0128(self):
        self.assertEquals(self.calculate(-457939119, 2131646748), 1673707629)

    def test0129(self):
        self.assertEquals(self.calculate(1547049393, 1249008254), -1498909649)

    def test0130(self):
        self.assertEquals(self.calculate(54740556, -1326281398), -1271540842)

    def test0131(self):
        self.assertEquals(self.calculate(267991199, -1508962437), -1240971238)

    def test0132(self):
        self.assertEquals(self.calculate(-705897087, 1291878251), 585981164)

    def test0133(self):
        self.assertEquals(self.calculate(1180002166, -568772102), 611230064)

    def test0134(self):
        self.assertEquals(self.calculate(320210338, -438045523), -117835185)

    def test0135(self):
        self.assertEquals(self.calculate(2042543296, 1742818231), -509605769)

    def test0136(self):
        self.assertEquals(self.calculate(-1959837009, -1489146566), 845983721)

    def test0137(self):
        self.assertEquals(self.calculate(-1163685509, -2038677951), 1092603836)

    def test0138(self):
        self.assertEquals(self.calculate(-1783521009, 2139930214), 356409205)

    def test0139(self):
        self.assertEquals(self.calculate(248763332, -672127689), -423364357)

    def test0140(self):
        self.assertEquals(self.calculate(921517262, 115058723), 1036575985)

    def test0141(self):
        self.assertEquals(self.calculate(1118072685, -682733833), 435338852)

    def test0142(self):
        self.assertEquals(self.calculate(465114446, 797748095), 1262862541)

    def test0143(self):
        self.assertEquals(self.calculate(-1811345488, -1904866051), 578755757)

    def test0144(self):
        self.assertEquals(self.calculate(-1436554698, 134009040), -1302545658)

    def test0145(self):
        self.assertEquals(self.calculate(-957500044, 1877672734), 920172690)

    def test0146(self):
        self.assertEquals(self.calculate(-428676495, -1018832322), -1447508817)

    def test0147(self):
        self.assertEquals(self.calculate(-2086500678, 858130739), -1228369939)

    def test0148(self):
        self.assertEquals(self.calculate(-214214654, -1207144338), -1421358992)

    def test0149(self):
        self.assertEquals(self.calculate(-824569183, 1854060079), 1029490896)

    def test0150(self):
        self.assertEquals(self.calculate(1859385155, -1104756464), 754628691)

    def test0151(self):
        self.assertEquals(self.calculate(2036073524, -2077030265), -40956741)

    def test0152(self):
        self.assertEquals(self.calculate(1191956270, 425245512), 1617201782)

    def test0153(self):
        self.assertEquals(self.calculate(1744732140, 1192602711), -1357632445)

    def test0154(self):
        self.assertEquals(self.calculate(-839437284, 644737653), -194699631)

    def test0155(self):
        self.assertEquals(self.calculate(363317455, -1004848949), -641531494)

    def test0156(self):
        self.assertEquals(self.calculate(1042811835, 1133302176), -2118853285)

    def test0157(self):
        self.assertEquals(self.calculate(-637102825, 1407431178), 770328353)

    def test0158(self):
        self.assertEquals(self.calculate(1960179101, 1618498900), -716289295)

    def test0159(self):
        self.assertEquals(self.calculate(-1940620073, 1750589800), -190030273)

    def test0160(self):
        self.assertEquals(self.calculate(793336179, 1250629235), 2043965414)

    def test0161(self):
        self.assertEquals(self.calculate(-878302240, 864328399), -13973841)

    def test0162(self):
        self.assertEquals(self.calculate(851549204, 1474772224), -1968645868)

    def test0163(self):
        self.assertEquals(self.calculate(-1826341310, -1293095165), 1175530821)

    def test0164(self):
        self.assertEquals(self.calculate(1895153848, 684346546), -1715466902)

    def test0165(self):
        self.assertEquals(self.calculate(-577269341, 1811920002), 1234650661)

    def test0166(self):
        self.assertEquals(self.calculate(-122783677, -366771653), -489555330)

    def test0167(self):
        self.assertEquals(self.calculate(-684352579, 929573115), 245220536)

    def test0168(self):
        self.assertEquals(self.calculate(-42130017, 1799966733), 1757836716)

    def test0169(self):
        self.assertEquals(self.calculate(-1622916027, -760928286), 1911122983)

    def test0170(self):
        self.assertEquals(self.calculate(612847843, -1621865934), -1009018091)

    def test0171(self):
        self.assertEquals(self.calculate(-869452164, -944433005), -1813885169)

    def test0172(self):
        self.assertEquals(self.calculate(-188702954, -564026334), -752729288)

    def test0173(self):
        self.assertEquals(self.calculate(427043395, 1247545904), 1674589299)

    def test0174(self):
        self.assertEquals(self.calculate(989190477, 656245379), 1645435856)

    def test0175(self):
        self.assertEquals(self.calculate(231926091, -2033758990), -1801832899)

    def test0176(self):
        self.assertEquals(self.calculate(1044464620, -1645599703), -601135083)

    def test0177(self):
        self.assertEquals(self.calculate(1287622965, 331446140), 1619069105)

    def test0178(self):
        self.assertEquals(self.calculate(-1079506915, 351405596), -728101319)

    def test0179(self):
        self.assertEquals(self.calculate(220589987, 1122262070), 1342852057)

    def test0180(self):
        self.assertEquals(self.calculate(986822784, -945389867), 41432917)

    def test0181(self):
        self.assertEquals(self.calculate(-606028211, 1868723915), 1262695704)

    def test0182(self):
        self.assertEquals(self.calculate(856902450, 316037119), 1172939569)

    def test0183(self):
        self.assertEquals(self.calculate(1644862059, 1331772412), -1318332825)

    def test0184(self):
        self.assertEquals(self.calculate(-1680529072, 1697808006), 17278934)

    def test0185(self):
        self.assertEquals(self.calculate(1516080699, -1302241799), 213838900)

    def test0186(self):
        self.assertEquals(self.calculate(973968192, -2107938663), -1133970471)

    def test0187(self):
        self.assertEquals(self.calculate(-1133834880, -317880617), -1451715497)

    def test0188(self):
        self.assertEquals(self.calculate(296370498, -1669622095), -1373251597)

    def test0189(self):
        self.assertEquals(self.calculate(1483818812, 837775403), -1973373081)

    def test0190(self):
        self.assertEquals(self.calculate(-1575988231, 2072238819), 496250588)

    def test0191(self):
        self.assertEquals(self.calculate(962622598, 687591062), 1650213660)

    def test0192(self):
        self.assertEquals(self.calculate(1133575934, -312651455), 820924479)

    def test0193(self):
        self.assertEquals(self.calculate(-1709632644, -1299446737), 1285887915)

    def test0194(self):
        self.assertEquals(self.calculate(-812490193, 765241302), -47248891)

    def test0195(self):
        self.assertEquals(self.calculate(1047619578, 114118274), 1161737852)

    def test0196(self):
        self.assertEquals(self.calculate(1293691458, -1905687349), -611995891)

    def test0197(self):
        self.assertEquals(self.calculate(-1336915138, -1993702764), 964349394)

    def test0198(self):
        self.assertEquals(self.calculate(-1778014816, -732568222), 1784384258)

    def test0199(self):
        self.assertEquals(self.calculate(629722503, 1306835558), 1936558061)

    def test0200(self):
        self.assertEquals(self.calculate(-992330517, -583133727), -1575464244)

    def test0201(self):
        self.assertEquals(self.calculate(-1001560011, -715885681), -1717445692)

    def test0202(self):
        self.assertEquals(self.calculate(-850747725, 233778987), -616968738)

    def test0203(self):
        self.assertEquals(self.calculate(1309827881, 297983937), 1607811818)

    def test0204(self):
        self.assertEquals(self.calculate(1258922275, 1235740897), -1800304124)

    def test0205(self):
        self.assertEquals(self.calculate(-1201349347, -496439543), -1697788890)

    def test0206(self):
        self.assertEquals(self.calculate(1535325546, 1828917640), -930724110)

    def test0207(self):
        self.assertEquals(self.calculate(290973969, 937797746), 1228771715)

    def test0208(self):
        self.assertEquals(self.calculate(-1635244447, -2069474582), 590248267)

    def test0209(self):
        self.assertEquals(self.calculate(-192345579, 1418064527), 1225718948)

    def test0210(self):
        self.assertEquals(self.calculate(152473335, -1392548062), -1240074727)

    def test0211(self):
        self.assertEquals(self.calculate(-776476094, -846639243), -1623115337)

    def test0212(self):
        self.assertEquals(self.calculate(1050678177, -330284179), 720393998)

    def test0213(self):
        self.assertEquals(self.calculate(-254559824, 1490352058), 1235792234)

    def test0214(self):
        self.assertEquals(self.calculate(-1603136326, 966619155), -636517171)

    def test0215(self):
        self.assertEquals(self.calculate(1723314662, 151499957), 1874814619)

    def test0216(self):
        self.assertEquals(self.calculate(-965276083, 1193446705), 228170622)

    def test0217(self):
        self.assertEquals(self.calculate(2037435672, 1336328881), -921202743)

    def test0218(self):
        self.assertEquals(self.calculate(49962315, 557532547), 607494862)

    def test0219(self):
        self.assertEquals(self.calculate(782852452, 363267694), 1146120146)

    def test0220(self):
        self.assertEquals(self.calculate(-1626883601, 1323463393), -303420208)

    def test0221(self):
        self.assertEquals(self.calculate(-367890342, 891612613), 523722271)

    def test0222(self):
        self.assertEquals(self.calculate(2103687208, 1351416021), -839864067)

    def test0223(self):
        self.assertEquals(self.calculate(1782474747, -497784174), 1284690573)

    def test0224(self):
        self.assertEquals(self.calculate(1549935305, -488500446), 1061434859)

    def test0225(self):
        self.assertEquals(self.calculate(-694375936, 1475323446), 780947510)

    def test0226(self):
        self.assertEquals(self.calculate(896775862, 1099271511), 1996047373)

    def test0227(self):
        self.assertEquals(self.calculate(-351343633, -1661247986), -2012591619)

    def test0228(self):
        self.assertEquals(self.calculate(-1728456996, -392795214), -2121252210)

    def test0229(self):
        self.assertEquals(self.calculate(-302599641, -1154223903), -1456823544)

    def test0230(self):
        self.assertEquals(self.calculate(-1182006969, 1000466218), -181540751)

    def test0231(self):
        self.assertEquals(self.calculate(1500842922, -1909664118), -408821196)

    def test0232(self):
        self.assertEquals(self.calculate(153681939, -1094826139), -941144200)

    def test0233(self):
        self.assertEquals(self.calculate(-1342636771, 426257865), -916378906)

    def test0234(self):
        self.assertEquals(self.calculate(-1992404878, -1478887591), 823674827)

    def test0235(self):
        self.assertEquals(self.calculate(-1221545655, -893878923), -2115424578)

    def test0236(self):
        self.assertEquals(self.calculate(964474251, 2107317093), -1223175952)

    def test0237(self):
        self.assertEquals(self.calculate(91624599, 2062244386), -2141098311)

    def test0238(self):
        self.assertEquals(self.calculate(492368407, 1957079854), -1845519035)

    def test0239(self):
        self.assertEquals(self.calculate(-1541753865, -1782833495), 970379936)

    def test0240(self):
        self.assertEquals(self.calculate(-1054950544, 1826481809), 771531265)

    def test0241(self):
        self.assertEquals(self.calculate(-19339541, -1602290775), -1621630316)

    def test0242(self):
        self.assertEquals(self.calculate(-387289578, -1597338446), -1984628024)

    def test0243(self):
        self.assertEquals(self.calculate(-1231825757, -1526060827), 1537080712)

    def test0244(self):
        self.assertEquals(self.calculate(645975968, 855248287), 1501224255)

    def test0245(self):
        self.assertEquals(self.calculate(1950015330, -251304544), 1698710786)

    def test0246(self):
        self.assertEquals(self.calculate(288311301, 1612342742), 1900654043)

    def test0247(self):
        self.assertEquals(self.calculate(911381789, 1699186780), -1684398727)

    def test0248(self):
        self.assertEquals(self.calculate(1172224580, 83151769), 1255376349)

    def test0249(self):
        self.assertEquals(self.calculate(-1224106574, 1136554707), -87551867)

    def test0250(self):
        self.assertEquals(self.calculate(1698802263, 1271063882), -1325101151)

    def test0251(self):
        self.assertEquals(self.calculate(398822855, -1797943800), -1399120945)

    def test0252(self):
        self.assertEquals(self.calculate(1882198024, 38404129), 1920602153)

    def test0253(self):
        self.assertEquals(self.calculate(883733182, -1772323714), -888590532)

    def test0254(self):
        self.assertEquals(self.calculate(1176599840, 1682929383), -1435438073)

    def test0255(self):
        self.assertEquals(self.calculate(1850369952, 120521354), 1970891306)

    def test0256(self):
        self.assertEquals(self.calculate(-1960263852, -1212349535), 1122353909)

    def test0257(self):
        self.assertEquals(self.calculate(-1869814157, -75327032), -1945141189)

    def test0258(self):
        self.assertEquals(self.calculate(-905655715, 531262044), -374393671)

    def test0259(self):
        self.assertEquals(self.calculate(1883274720, 2061635232), -350057344)

    def test0260(self):
        self.assertEquals(self.calculate(-1764984602, 1535530000), -229454602)

    def test0261(self):
        self.assertEquals(self.calculate(-693494795, -661424104), -1354918899)

    def test0262(self):
        self.assertEquals(self.calculate(869811095, 206718977), 1076530072)

    def test0263(self):
        self.assertEquals(self.calculate(-1466162440, -1421613841), 1407191015)

    def test0264(self):
        self.assertEquals(self.calculate(2032430765, 2107589032), -154947499)

    def test0265(self):
        self.assertEquals(self.calculate(1959936621, -318526564), 1641410057)

    def test0266(self):
        self.assertEquals(self.calculate(1673665663, -2084094983), -410429320)

    def test0267(self):
        self.assertEquals(self.calculate(-1945644243, -2136673431), 212649622)

    def test0268(self):
        self.assertEquals(self.calculate(1087203851, 213328923), 1300532774)

    def test0269(self):
        self.assertEquals(self.calculate(1882124432, 1674477059), -738365805)

    def test0270(self):
        self.assertEquals(self.calculate(2022089298, -1573553830), 448535468)

    def test0271(self):
        self.assertEquals(self.calculate(-390613973, 1179579077), 788965104)

    def test0272(self):
        self.assertEquals(self.calculate(-1742137652, 2147476685), 405339033)

    def test0273(self):
        self.assertEquals(self.calculate(-909517394, 313045054), -596472340)

    def test0274(self):
        self.assertEquals(self.calculate(1595100404, 1633226275), -1066640617)

    def test0275(self):
        self.assertEquals(self.calculate(-333993364, 970336857), 636343493)

    def test0276(self):
        self.assertEquals(self.calculate(-1928500745, -2028182060), 338284491)

    def test0277(self):
        self.assertEquals(self.calculate(-1838283778, 1565473116), -272810662)

    def test0278(self):
        self.assertEquals(self.calculate(1720196644, -1411109499), 309087145)

    def test0279(self):
        self.assertEquals(self.calculate(2051599938, -1187897292), 863702646)

    def test0280(self):
        self.assertEquals(self.calculate(292830946, 2021173922), -1980962428)

    def test0281(self):
        self.assertEquals(self.calculate(393104146, -669918383), -276814237)

    def test0282(self):
        self.assertEquals(self.calculate(-1547804276, -523788551), -2071592827)

    def test0283(self):
        self.assertEquals(self.calculate(1902637970, 594445841), -1797883485)

    def test0284(self):
        self.assertEquals(self.calculate(1569625387, 1503357457), -1221984452)

    def test0285(self):
        self.assertEquals(self.calculate(415964195, 1171397453), 1587361648)

    def test0286(self):
        self.assertEquals(self.calculate(402760618, -1683326505), -1280565887)

    def test0287(self):
        self.assertEquals(self.calculate(-1503693591, -1046267835), 1745005870)

    def test0288(self):
        self.assertEquals(self.calculate(-1295191112, -250006719), -1545197831)

    def test0289(self):
        self.assertEquals(self.calculate(-1332849219, 725695686), -607153533)

    def test0290(self):
        self.assertEquals(self.calculate(1985846195, -2022833549), -36987354)

    def test0291(self):
        self.assertEquals(self.calculate(-219427659, -133397358), -352825017)

    def test0292(self):
        self.assertEquals(self.calculate(967849970, 1611497331), -1715619995)

    def test0293(self):
        self.assertEquals(self.calculate(2109742155, 235232496), -1949992645)

    def test0294(self):
        self.assertEquals(self.calculate(-1158475978, 103285914), -1055190064)

    def test0295(self):
        self.assertEquals(self.calculate(1520313298, -1241849497), 278463801)

    def test0296(self):
        self.assertEquals(self.calculate(1911178533, -1065188536), 845989997)

    def test0297(self):
        self.assertEquals(self.calculate(-1287781205, -385964491), -1673745696)

    def test0298(self):
        self.assertEquals(self.calculate(1835082415, -999517463), 835564952)

    def test0299(self):
        self.assertEquals(self.calculate(-1380768581, -1656236105), 1257962610)

    def test0300(self):
        self.assertEquals(self.calculate(303992080, 897207343), 1201199423)

    def test0301(self):
        self.assertEquals(self.calculate(221672607, 2047871416), -2025423273)

    def test0302(self):
        self.assertEquals(self.calculate(460839997, 729148554), 1189988551)

    def test0303(self):
        self.assertEquals(self.calculate(-1687799274, -556771528), 2050396494)

    def test0304(self):
        self.assertEquals(self.calculate(1950614924, -739991855), 1210623069)

    def test0305(self):
        self.assertEquals(self.calculate(-80714169, 857034290), 776320121)

    def test0306(self):
        self.assertEquals(self.calculate(-433490084, -1934178066), 1927299146)

    def test0307(self):
        self.assertEquals(self.calculate(1413820055, -2142189479), -728369424)

    def test0308(self):
        self.assertEquals(self.calculate(1320429316, -1673222401), -352793085)

    def test0309(self):
        self.assertEquals(self.calculate(-187905926, 2034084122), 1846178196)

    def test0310(self):
        self.assertEquals(self.calculate(557026158, -287166790), 269859368)

    def test0311(self):
        self.assertEquals(self.calculate(822272785, 371781791), 1194054576)

    def test0312(self):
        self.assertEquals(self.calculate(-1799035803, -1547512006), 948419487)

    def test0313(self):
        self.assertEquals(self.calculate(1142595548, -1496605288), -354009740)

    def test0314(self):
        self.assertEquals(self.calculate(-559063788, 1658217726), 1099153938)

    def test0315(self):
        self.assertEquals(self.calculate(1003301102, -122995377), 880305725)

    def test0316(self):
        self.assertEquals(self.calculate(334762072, 151552028), 486314100)

    def test0317(self):
        self.assertEquals(self.calculate(239910729, 1942870174), -2112186393)

    def test0318(self):
        self.assertEquals(self.calculate(543934790, 553912746), 1097847536)

    def test0319(self):
        self.assertEquals(self.calculate(1057450964, -847814763), 209636201)

    def test0320(self):
        self.assertEquals(self.calculate(-2044310228, 754676422), -1289633806)

    def test0321(self):
        self.assertEquals(self.calculate(205610612, 1560255067), 1765865679)

    def test0322(self):
        self.assertEquals(self.calculate(-1666504603, 1279832262), -386672341)

    def test0323(self):
        self.assertEquals(self.calculate(-1114694655, -1790523103), 1389749538)

    def test0324(self):
        self.assertEquals(self.calculate(579257946, 1619634854), -2096074496)

    def test0325(self):
        self.assertEquals(self.calculate(1731389078, -1483847553), 247541525)

    def test0326(self):
        self.assertEquals(self.calculate(-125046878, -1666350096), -1791396974)

    def test0327(self):
        self.assertEquals(self.calculate(1946120988, 978063424), -1370782884)

    def test0328(self):
        self.assertEquals(self.calculate(1706498711, -1209941361), 496557350)

    def test0329(self):
        self.assertEquals(self.calculate(-1872042844, 392564546), -1479478298)

    def test0330(self):
        self.assertEquals(self.calculate(1954051259, 12523155), 1966574414)

    def test0331(self):
        self.assertEquals(self.calculate(-1823376506, 1756012102), -67364404)

    def test0332(self):
        self.assertEquals(self.calculate(1187318992, 1826487003), -1281161301)

    def test0333(self):
        self.assertEquals(self.calculate(1945027830, -682055122), 1262972708)

    def test0334(self):
        self.assertEquals(self.calculate(394947514, -2108771291), -1713823777)

    def test0335(self):
        self.assertEquals(self.calculate(149985233, 1860230401), 2010215634)

    def test0336(self):
        self.assertEquals(self.calculate(-1778141941, -373862991), 2142962364)

    def test0337(self):
        self.assertEquals(self.calculate(-1094785982, -58263951), -1153049933)

    def test0338(self):
        self.assertEquals(self.calculate(-1491565746, 536884374), -954681372)

    def test0339(self):
        self.assertEquals(self.calculate(-1983158358, -1030770766), 1281038172)

    def test0340(self):
        self.assertEquals(self.calculate(1911654055, 1883598198), -499715043)

    def test0341(self):
        self.assertEquals(self.calculate(-1544898351, -1527776487), 1222292458)

    def test0342(self):
        self.assertEquals(self.calculate(-1377160786, 156090398), -1221070388)

    def test0343(self):
        self.assertEquals(self.calculate(-1554452477, 710802161), -843650316)

    def test0344(self):
        self.assertEquals(self.calculate(-2045432742, 1534082696), -511350046)

    def test0345(self):
        self.assertEquals(self.calculate(2009250691, -638271982), 1370978709)

    def test0346(self):
        self.assertEquals(self.calculate(170473513, 700993440), 871466953)

    def test0347(self):
        self.assertEquals(self.calculate(-1606316767, 1038261014), -568055753)

    def test0348(self):
        self.assertEquals(self.calculate(1774945456, 410094581), -2109927259)

    def test0349(self):
        self.assertEquals(self.calculate(-154440583, -1257512538), -1411953121)

    def test0350(self):
        self.assertEquals(self.calculate(816232765, -1889147491), -1072914726)

    def test0351(self):
        self.assertEquals(self.calculate(-1423097462, -1962801900), 909067934)

    def test0352(self):
        self.assertEquals(self.calculate(819870248, 354220301), 1174090549)

    def test0353(self):
        self.assertEquals(self.calculate(-612294509, 1057185208), 444890699)

    def test0354(self):
        self.assertEquals(self.calculate(-1696929601, 394995062), -1301934539)

    def test0355(self):
        self.assertEquals(self.calculate(921884156, -1873042486), -951158330)

    def test0356(self):
        self.assertEquals(self.calculate(322584003, -1475595733), -1153011730)

    def test0357(self):
        self.assertEquals(self.calculate(-354431107, 1319802895), 965371788)

    def test0358(self):
        self.assertEquals(self.calculate(-1680744165, 544898599), -1135845566)

    def test0359(self):
        self.assertEquals(self.calculate(-1875939461, -1412889489), 1006138346)

    def test0360(self):
        self.assertEquals(self.calculate(1603960694, -102567043), 1501393651)

    def test0361(self):
        self.assertEquals(self.calculate(476527443, -650527980), -174000537)

    def test0362(self):
        self.assertEquals(self.calculate(971909929, -746961473), 224948456)

    def test0363(self):
        self.assertEquals(self.calculate(-1067868722, 1150519697), 82650975)

    def test0364(self):
        self.assertEquals(self.calculate(448099353, -1691971886), -1243872533)

    def test0365(self):
        self.assertEquals(self.calculate(664758769, -44356556), 620402213)

    def test0366(self):
        self.assertEquals(self.calculate(-1803010436, -1851496371), 640460489)

    def test0367(self):
        self.assertEquals(self.calculate(-2035219957, 2081870435), 46650478)

    def test0368(self):
        self.assertEquals(self.calculate(-1917758390, -1557208529), 820000377)

    def test0369(self):
        self.assertEquals(self.calculate(1923060031, 1929090441), -442816824)

    def test0370(self):
        self.assertEquals(self.calculate(-1376526580, -501666358), -1878192938)

    def test0371(self):
        self.assertEquals(self.calculate(-1887767201, -514385543), 1892814552)

    def test0372(self):
        self.assertEquals(self.calculate(-57296098, 1775950037), 1718653939)

    def test0373(self):
        self.assertEquals(self.calculate(-1204981300, -971218832), 2118767164)

    def test0374(self):
        self.assertEquals(self.calculate(-138909393, 688383255), 549473862)

    def test0375(self):
        self.assertEquals(self.calculate(729946263, 1859432366), -1705588667)

    def test0376(self):
        self.assertEquals(self.calculate(-1940830464, -1610734618), 743402214)

    def test0377(self):
        self.assertEquals(self.calculate(875786048, 2012274152), -1406907096)

    def test0378(self):
        self.assertEquals(self.calculate(1799849822, -1337829027), 462020795)

    def test0379(self):
        self.assertEquals(self.calculate(-1273286539, 472006543), -801279996)

    def test0380(self):
        self.assertEquals(self.calculate(-1494893544, -644160832), -2139054376)

    def test0381(self):
        self.assertEquals(self.calculate(-1329547948, 1092577340), -236970608)

    def test0382(self):
        self.assertEquals(self.calculate(2124494628, -430992663), 1693501965)

    def test0383(self):
        self.assertEquals(self.calculate(440390097, -226786702), 213603395)

    def test0384(self):
        self.assertEquals(self.calculate(890918507, -59328525), 831589982)

    def test0385(self):
        self.assertEquals(self.calculate(-562152727, 351223289), -210929438)

    def test0386(self):
        self.assertEquals(self.calculate(-600369110, 965840262), 365471152)

    def test0387(self):
        self.assertEquals(self.calculate(-1001875167, 359012012), -642863155)

    def test0388(self):
        self.assertEquals(self.calculate(1027471247, -206918473), 820552774)

    def test0389(self):
        self.assertEquals(self.calculate(-1277187296, -1583275133), 1434504867)

    def test0390(self):
        self.assertEquals(self.calculate(1104370810, -768311822), 336058988)

    def test0391(self):
        self.assertEquals(self.calculate(1011003438, 1225928991), -2058034867)

    def test0392(self):
        self.assertEquals(self.calculate(-1073734213, -897178002), -1970912215)

    def test0393(self):
        self.assertEquals(self.calculate(189652272, -165435924), 24216348)

    def test0394(self):
        self.assertEquals(self.calculate(974935296, 1192236938), -2127795062)

    def test0395(self):
        self.assertEquals(self.calculate(-1915575550, -120485481), -2036061031)

    def test0396(self):
        self.assertEquals(self.calculate(-1175858001, -2145761123), 973348172)

    def test0397(self):
        self.assertEquals(self.calculate(-1867639716, 1103820524), -763819192)

    def test0398(self):
        self.assertEquals(self.calculate(-1671881839, -115553458), -1787435297)

    def test0399(self):
        self.assertEquals(self.calculate(-887835558, -356392014), -1244227572)

    def test0400(self):
        self.assertEquals(self.calculate(-2002602330, -746209683), 1546155283)

    def test0401(self):
        self.assertEquals(self.calculate(430888543, 1336148140), 1767036683)

    def test0402(self):
        self.assertEquals(self.calculate(6361303, 1627969402), 1634330705)

    def test0403(self):
        self.assertEquals(self.calculate(-973162453, -1591806403), 1729998440)

    def test0404(self):
        self.assertEquals(self.calculate(-170848220, 1880821951), 1709973731)

    def test0405(self):
        self.assertEquals(self.calculate(480741204, -492770408), -12029204)

    def test0406(self):
        self.assertEquals(self.calculate(1327675458, -1452779781), -125104323)

    def test0407(self):
        self.assertEquals(self.calculate(-983487471, -1970578637), 1340901188)

    def test0408(self):
        self.assertEquals(self.calculate(768432583, 1070391387), 1838823970)

    def test0409(self):
        self.assertEquals(self.calculate(1175734650, 680406952), 1856141602)

    def test0410(self):
        self.assertEquals(self.calculate(1632018504, -1540046923), 91971581)

    def test0411(self):
        self.assertEquals(self.calculate(-1092800679, -517748360), -1610549039)

    def test0412(self):
        self.assertEquals(self.calculate(998324191, 1285773717), -2010869388)

    def test0413(self):
        self.assertEquals(self.calculate(222818613, -549731552), -326912939)

    def test0414(self):
        self.assertEquals(self.calculate(-226991309, -424201653), -651192962)

    def test0415(self):
        self.assertEquals(self.calculate(-19034802, 1503543599), 1484508797)

    def test0416(self):
        self.assertEquals(self.calculate(-544564257, 66102112), -478462145)

    def test0417(self):
        self.assertEquals(self.calculate(962339929, 1858396658), -1474230709)

    def test0418(self):
        self.assertEquals(self.calculate(616050414, -1461259624), -845209210)

    def test0419(self):
        self.assertEquals(self.calculate(-288669563, 1344806200), 1056136637)

    def test0420(self):
        self.assertEquals(self.calculate(-1576543184, -1233943969), 1484480143)

    def test0421(self):
        self.assertEquals(self.calculate(-1718050488, -400761370), -2118811858)

    def test0422(self):
        self.assertEquals(self.calculate(-485769369, 1078292015), 592522646)

    def test0423(self):
        self.assertEquals(self.calculate(977392466, -1166349277), -188956811)

    def test0424(self):
        self.assertEquals(self.calculate(1507797124, 1176505701), -1610664471)

    def test0425(self):
        self.assertEquals(self.calculate(1424255136, 1917143126), -953569034)

    def test0426(self):
        self.assertEquals(self.calculate(806878302, 1304639852), 2111518154)

    def test0427(self):
        self.assertEquals(self.calculate(-201906039, 1649630666), 1447724627)

    def test0428(self):
        self.assertEquals(self.calculate(-364217849, -127874580), -492092429)

    def test0429(self):
        self.assertEquals(self.calculate(-283852183, -1504167694), -1788019877)

    def test0430(self):
        self.assertEquals(self.calculate(-839518972, -1357539949), 2097908375)

    def test0431(self):
        self.assertEquals(self.calculate(436850922, -539225662), -102374740)

    def test0432(self):
        self.assertEquals(self.calculate(1265786808, -1629652664), -363865856)

    def test0433(self):
        self.assertEquals(self.calculate(569723995, 865232910), 1434956905)

    def test0434(self):
        self.assertEquals(self.calculate(-291326142, -1717509927), -2008836069)

    def test0435(self):
        self.assertEquals(self.calculate(-1128183651, -1050155033), 2116628612)

    def test0436(self):
        self.assertEquals(self.calculate(61490380, 528489327), 589979707)

    def test0437(self):
        self.assertEquals(self.calculate(-1555375474, 671076737), -884298737)

    def test0438(self):
        self.assertEquals(self.calculate(-1698547432, 2036172447), 337625015)

    def test0439(self):
        self.assertEquals(self.calculate(1464525481, 1295534125), -1534907690)

    def test0440(self):
        self.assertEquals(self.calculate(-791738385, 1782588954), 990850569)

    def test0441(self):
        self.assertEquals(self.calculate(-172280265, 1633108506), 1460828241)

    def test0442(self):
        self.assertEquals(self.calculate(-1585535397, -54549868), -1640085265)

    def test0443(self):
        self.assertEquals(self.calculate(-1841367219, 558928870), -1282438349)

    def test0444(self):
        self.assertEquals(self.calculate(-850675121, 85971295), -764703826)

    def test0445(self):
        self.assertEquals(self.calculate(1575092337, -338484924), 1236607413)

    def test0446(self):
        self.assertEquals(self.calculate(1683708263, 1028186760), -1583072273)

    def test0447(self):
        self.assertEquals(self.calculate(-1213663897, -246735923), -1460399820)

    def test0448(self):
        self.assertEquals(self.calculate(1165368815, 619739062), 1785107877)

    def test0449(self):
        self.assertEquals(self.calculate(-1196737152, 814102197), -382634955)

    def test0450(self):
        self.assertEquals(self.calculate(-1364869853, 1769011670), 404141817)

    def test0451(self):
        self.assertEquals(self.calculate(1103085644, -1018936087), 84149557)

    def test0452(self):
        self.assertEquals(self.calculate(-1938675050, 181192650), -1757482400)

    def test0453(self):
        self.assertEquals(self.calculate(-171558878, 129506165), -42052713)

    def test0454(self):
        self.assertEquals(self.calculate(-2078933279, 1894581046), -184352233)

    def test0455(self):
        self.assertEquals(self.calculate(-2105219582, 1868164470), -237055112)

    def test0456(self):
        self.assertEquals(self.calculate(-1383202038, -212038102), -1595240140)

    def test0457(self):
        self.assertEquals(self.calculate(-83814937, 1037150095), 953335158)

    def test0458(self):
        self.assertEquals(self.calculate(-1070881726, -906125115), -1977006841)

    def test0459(self):
        self.assertEquals(self.calculate(211851474, 475409824), 687261298)

    def test0460(self):
        self.assertEquals(self.calculate(1187252683, 637729688), 1824982371)

    def test0461(self):
        self.assertEquals(self.calculate(-1172619195, -175942742), -1348561937)

    def test0462(self):
        self.assertEquals(self.calculate(-1890794162, -1493323992), 910849142)

    def test0463(self):
        self.assertEquals(self.calculate(-342231180, 494244913), 152013733)

    def test0464(self):
        self.assertEquals(self.calculate(1506533930, -1821650776), -315116846)

    def test0465(self):
        self.assertEquals(self.calculate(835866316, 307508718), 1143375034)

    def test0466(self):
        self.assertEquals(self.calculate(953746058, 2106293751), -1234927487)

    def test0467(self):
        self.assertEquals(self.calculate(187225418, -341200518), -153975100)

    def test0468(self):
        self.assertEquals(self.calculate(-1829804367, 146996134), -1682808233)

    def test0469(self):
        self.assertEquals(self.calculate(-1151039954, -1303762421), 1840164921)

    def test0470(self):
        self.assertEquals(self.calculate(1245647332, 569341488), 1814988820)

    def test0471(self):
        self.assertEquals(self.calculate(1632611238, -1892995385), -260384147)

    def test0472(self):
        self.assertEquals(self.calculate(-1897374581, -1109547523), 1288045192)

    def test0473(self):
        self.assertEquals(self.calculate(1500922142, -324816634), 1176105508)

    def test0474(self):
        self.assertEquals(self.calculate(-656066519, 1787553236), 1131486717)

    def test0475(self):
        self.assertEquals(self.calculate(1157244548, -1556010403), -398765855)

    def test0476(self):
        self.assertEquals(self.calculate(-1935701768, -47666480), -1983368248)

    def test0477(self):
        self.assertEquals(self.calculate(-831175382, 241902629), -589272753)

    def test0478(self):
        self.assertEquals(self.calculate(124568443, 1065353929), 1189922372)

    def test0479(self):
        self.assertEquals(self.calculate(378640943, -389385182), -10744239)

    def test0480(self):
        self.assertEquals(self.calculate(1265311146, -280847166), 984463980)

    def test0481(self):
        self.assertEquals(self.calculate(-1757107463, -316143417), -2073250880)

    def test0482(self):
        self.assertEquals(self.calculate(864163651, 1256364429), 2120528080)

    def test0483(self):
        self.assertEquals(self.calculate(-82894382, 2085391048), 2002496666)

    def test0484(self):
        self.assertEquals(self.calculate(-1871280262, -119823057), -1991103319)

    def test0485(self):
        self.assertEquals(self.calculate(1433428654, 555149891), 1988578545)

    def test0486(self):
        self.assertEquals(self.calculate(2043273575, -1872999613), 170273962)

    def test0487(self):
        self.assertEquals(self.calculate(776983532, 1434982832), -2083000932)

    def test0488(self):
        self.assertEquals(self.calculate(-573831270, 977319271), 403488001)

    def test0489(self):
        self.assertEquals(self.calculate(-1892122334, 1956507317), 64384983)

    def test0490(self):
        self.assertEquals(self.calculate(1346977854, -1252530066), 94447788)

    def test0491(self):
        self.assertEquals(self.calculate(1837880608, 900331738), -1556754950)

    def test0492(self):
        self.assertEquals(self.calculate(-1054538181, 2089706952), 1035168771)

    def test0493(self):
        self.assertEquals(self.calculate(1160001036, -1903664316), -743663280)

    def test0494(self):
        self.assertEquals(self.calculate(-1349257084, 1912338260), 563081176)

    def test0495(self):
        self.assertEquals(self.calculate(1169177926, -4186195), 1164991731)

    def test0496(self):
        self.assertEquals(self.calculate(-1148970796, -1521973421), 1624023079)

    def test0497(self):
        self.assertEquals(self.calculate(-661548746, -1380937030), -2042485776)

    def test0498(self):
        self.assertEquals(self.calculate(-765133140, -882183532), -1647316672)

    def test0499(self):
        self.assertEquals(self.calculate(-597524494, -1200138116), -1797662610)

    def test0500(self):
        self.assertEquals(self.calculate(955723892, 1474916145), -1864327259)

    def test0501(self):
        self.assertEquals(self.calculate(-528679192, -1022255112), -1550934304)

    def test0502(self):
        self.assertEquals(self.calculate(-1305308282, -579764538), -1885072820)

    def test0503(self):
        self.assertEquals(self.calculate(1467101773, 844146911), -1983718612)

    def test0504(self):
        self.assertEquals(self.calculate(-577406517, 1702607349), 1125200832)

    def test0505(self):
        self.assertEquals(self.calculate(114847607, -573421944), -458574337)

    def test0506(self):
        self.assertEquals(self.calculate(-828596330, -782012680), -1610609010)

    def test0507(self):
        self.assertEquals(self.calculate(-1678558070, 1582698920), -95859150)

    def test0508(self):
        self.assertEquals(self.calculate(2006379524, -2141618412), -135238888)

    def test0509(self):
        self.assertEquals(self.calculate(953273815, -840565891), 112707924)

    def test0510(self):
        self.assertEquals(self.calculate(-782930580, 1419566659), 636636079)

    def test0511(self):
        self.assertEquals(self.calculate(737433067, -786166262), -48733195)

    def test0512(self):
        self.assertEquals(self.calculate(1608004920, -2033764236), -425759316)

    def test0513(self):
        self.assertEquals(self.calculate(-1713357046, 1518674790), -194682256)

    def test0514(self):
        self.assertEquals(self.calculate(-164824943, 1689492528), 1524667585)

    def test0515(self):
        self.assertEquals(self.calculate(-10218662, -1043379228), -1053597890)

    def test0516(self):
        self.assertEquals(self.calculate(-2121691978, -1477866086), 695409232)

    def test0517(self):
        self.assertEquals(self.calculate(574875026, -1254648693), -679773667)

    def test0518(self):
        self.assertEquals(self.calculate(1654758848, 1279536287), -1360672161)

    def test0519(self):
        self.assertEquals(self.calculate(-1689938812, -96218661), -1786157473)

    def test0520(self):
        self.assertEquals(self.calculate(-611708910, -1207699813), -1819408723)

    def test0521(self):
        self.assertEquals(self.calculate(-1489149796, -183106093), -1672255889)

    def test0522(self):
        self.assertEquals(self.calculate(-1786329202, 821392294), -964936908)

    def test0523(self):
        self.assertEquals(self.calculate(-1903848674, -465659025), 1925459597)

    def test0524(self):
        self.assertEquals(self.calculate(-1966019425, 1845657226), -120362199)

    def test0525(self):
        self.assertEquals(self.calculate(537432712, 714384074), 1251816786)

    def test0526(self):
        self.assertEquals(self.calculate(833065851, -1455508347), -622442496)

    def test0527(self):
        self.assertEquals(self.calculate(1610894186, -347492828), 1263401358)

    def test0528(self):
        self.assertEquals(self.calculate(1427913739, 1317241960), -1549811597)

    def test0529(self):
        self.assertEquals(self.calculate(-562739889, -123562052), -686301941)

    def test0530(self):
        self.assertEquals(self.calculate(-243016384, 246391502), 3375118)

    def test0531(self):
        self.assertEquals(self.calculate(-1960799922, 1981454327), 20654405)

    def test0532(self):
        self.assertEquals(self.calculate(741250457, 545619169), 1286869626)

    def test0533(self):
        self.assertEquals(self.calculate(-1635233786, 1372618785), -262615001)

    def test0534(self):
        self.assertEquals(self.calculate(1258638375, 1909937406), -1126391515)

    def test0535(self):
        self.assertEquals(self.calculate(-505440910, -2129675950), 1659850436)

    def test0536(self):
        self.assertEquals(self.calculate(1121105941, 876357114), 1997463055)

    def test0537(self):
        self.assertEquals(self.calculate(-1159902475, -1448673850), 1686390971)

    def test0538(self):
        self.assertEquals(self.calculate(1569813419, -1947944458), -378131039)

    def test0539(self):
        self.assertEquals(self.calculate(-74193730, -366005398), -440199128)

    def test0540(self):
        self.assertEquals(self.calculate(1199993847, 855910432), 2055904279)

    def test0541(self):
        self.assertEquals(self.calculate(529557207, -1583255100), -1053697893)

    def test0542(self):
        self.assertEquals(self.calculate(188145024, 826961633), 1015106657)

    def test0543(self):
        self.assertEquals(self.calculate(-1165933281, -1909409881), 1219624134)

    def test0544(self):
        self.assertEquals(self.calculate(1539924289, 752824172), -2002218835)

    def test0545(self):
        self.assertEquals(self.calculate(686927042, -825036645), -138109603)

    def test0546(self):
        self.assertEquals(self.calculate(-1370858307, 1981970054), 611111747)

    def test0547(self):
        self.assertEquals(self.calculate(-1791518784, 414228880), -1377289904)

    def test0548(self):
        self.assertEquals(self.calculate(-356982457, -1250094375), -1607076832)

    def test0549(self):
        self.assertEquals(self.calculate(297000631, 171436806), 468437437)

    def test0550(self):
        self.assertEquals(self.calculate(1130949337, -1369212168), -238262831)

    def test0551(self):
        self.assertEquals(self.calculate(753882541, 1457286518), -2083798237)

    def test0552(self):
        self.assertEquals(self.calculate(-1351937496, 924583918), -427353578)

    def test0553(self):
        self.assertEquals(self.calculate(-2017845571, -1223239174), 1053882551)

    def test0554(self):
        self.assertEquals(self.calculate(2044710235, 1978232516), -272024545)

    def test0555(self):
        self.assertEquals(self.calculate(-1324522110, 1841067830), 516545720)

    def test0556(self):
        self.assertEquals(self.calculate(538398809, 2084370004), -1672198483)

    def test0557(self):
        self.assertEquals(self.calculate(-631708406, -683969620), -1315678026)

    def test0558(self):
        self.assertEquals(self.calculate(101244169, -475102485), -373858316)

    def test0559(self):
        self.assertEquals(self.calculate(1643143218, -1798156094), -155012876)

    def test0560(self):
        self.assertEquals(self.calculate(1068063667, 1323825133), -1903078496)

    def test0561(self):
        self.assertEquals(self.calculate(-311092971, 1364109276), 1053016305)

    def test0562(self):
        self.assertEquals(self.calculate(-1500431853, -1903422325), 891113118)

    def test0563(self):
        self.assertEquals(self.calculate(-1866435594, 238504828), -1627930766)

    def test0564(self):
        self.assertEquals(self.calculate(229927109, 902111585), 1132038694)

    def test0565(self):
        self.assertEquals(self.calculate(1435034818, 359139124), 1794173942)

    def test0566(self):
        self.assertEquals(self.calculate(1726403798, 663918765), -1904644733)

    def test0567(self):
        self.assertEquals(self.calculate(1385356841, -704900191), 680456650)

    def test0568(self):
        self.assertEquals(self.calculate(-262705362, -1717889062), -1980594424)

    def test0569(self):
        self.assertEquals(self.calculate(1146094954, -413341796), 732753158)

    def test0570(self):
        self.assertEquals(self.calculate(-2093985836, 321863583), -1772122253)

    def test0571(self):
        self.assertEquals(self.calculate(1088060023, 1448005644), -1758901629)

    def test0572(self):
        self.assertEquals(self.calculate(433166611, 930732037), 1363898648)

    def test0573(self):
        self.assertEquals(self.calculate(650817019, -559220595), 91596424)

    def test0574(self):
        self.assertEquals(self.calculate(-2144395641, 882042181), -1262353460)

    def test0575(self):
        self.assertEquals(self.calculate(1112956421, -101428191), 1011528230)

    def test0576(self):
        self.assertEquals(self.calculate(-1564251567, -939611088), 1791104641)

    def test0577(self):
        self.assertEquals(self.calculate(540883707, -1654848523), -1113964816)

    def test0578(self):
        self.assertEquals(self.calculate(-1143909287, -483357345), -1627266632)

    def test0579(self):
        self.assertEquals(self.calculate(53597873, -1437538822), -1383940949)

    def test0580(self):
        self.assertEquals(self.calculate(-409430734, -1326997547), -1736428281)

    def test0581(self):
        self.assertEquals(self.calculate(-1646303232, -1473865733), 1174798331)

    def test0582(self):
        self.assertEquals(self.calculate(1143208283, -1717589597), -574381314)

    def test0583(self):
        self.assertEquals(self.calculate(898332303, 454531049), 1352863352)

    def test0584(self):
        self.assertEquals(self.calculate(-548591358, -1570084186), -2118675544)

    def test0585(self):
        self.assertEquals(self.calculate(-638757902, 1258384078), 619626176)

    def test0586(self):
        self.assertEquals(self.calculate(1911656210, 521089881), -1862221205)

    def test0587(self):
        self.assertEquals(self.calculate(-1008176023, -738608768), -1746784791)

    def test0588(self):
        self.assertEquals(self.calculate(686274202, -110799911), 575474291)

    def test0589(self):
        self.assertEquals(self.calculate(1480283933, -1017657697), 462626236)

    def test0590(self):
        self.assertEquals(self.calculate(-558290475, 1579303003), 1021012528)

    def test0591(self):
        self.assertEquals(self.calculate(1672165346, -550082626), 1122082720)

    def test0592(self):
        self.assertEquals(self.calculate(1814029404, -917937654), 896091750)

    def test0593(self):
        self.assertEquals(self.calculate(-474002934, -1074172236), -1548175170)

    def test0594(self):
        self.assertEquals(self.calculate(388192938, 1412982378), 1801175316)

    def test0595(self):
        self.assertEquals(self.calculate(1247773714, 523510695), 1771284409)

    def test0596(self):
        self.assertEquals(self.calculate(-237899805, -81730862), -319630667)

    def test0597(self):
        self.assertEquals(self.calculate(-1444634497, -624055228), -2068689725)

    def test0598(self):
        self.assertEquals(self.calculate(-1631716461, 1714401314), 82684853)

    def test0599(self):
        self.assertEquals(self.calculate(2141633357, 399134826), -1754199113)

    def test0600(self):
        self.assertEquals(self.calculate(-1682433908, -1357813815), 1254719573)

    def test0601(self):
        self.assertEquals(self.calculate(209929432, 2128109098), -1956928766)

    def test0602(self):
        self.assertEquals(self.calculate(351905901, 973324942), 1325230843)

    def test0603(self):
        self.assertEquals(self.calculate(-1919328238, -345888993), 2029750065)

    def test0604(self):
        self.assertEquals(self.calculate(1728895355, -534056392), 1194838963)

    def test0605(self):
        self.assertEquals(self.calculate(588233047, 206501396), 794734443)

    def test0606(self):
        self.assertEquals(self.calculate(-912178983, -249405610), -1161584593)

    def test0607(self):
        self.assertEquals(self.calculate(-388146659, 2068026103), 1679879444)

    def test0608(self):
        self.assertEquals(self.calculate(-198168067, 1435187186), 1237019119)

    def test0609(self):
        self.assertEquals(self.calculate(293734057, -349174732), -55440675)

    def test0610(self):
        self.assertEquals(self.calculate(-1422527874, 1575549832), 153021958)

    def test0611(self):
        self.assertEquals(self.calculate(997644769, -657025430), 340619339)

    def test0612(self):
        self.assertEquals(self.calculate(-107633341, -1049103200), -1156736541)

    def test0613(self):
        self.assertEquals(self.calculate(290471148, 1238929831), 1529400979)

    def test0614(self):
        self.assertEquals(self.calculate(1658556607, -1714495471), -55938864)

    def test0615(self):
        self.assertEquals(self.calculate(1140813292, 185920013), 1326733305)

    def test0616(self):
        self.assertEquals(self.calculate(-439889283, 2083582460), 1643693177)

    def test0617(self):
        self.assertEquals(self.calculate(1320254231, 332603231), 1652857462)

    def test0618(self):
        self.assertEquals(self.calculate(-2083111882, 2013487430), -69624452)

    def test0619(self):
        self.assertEquals(self.calculate(-1667272039, -1018626002), 1609069255)

    def test0620(self):
        self.assertEquals(self.calculate(-202959642, 72983174), -129976468)

    def test0621(self):
        self.assertEquals(self.calculate(-1139943264, 1729074599), 589131335)

    def test0622(self):
        self.assertEquals(self.calculate(1295535537, -713882047), 581653490)

    def test0623(self):
        self.assertEquals(self.calculate(-1772286830, -1289987126), 1232693340)

    def test0624(self):
        self.assertEquals(self.calculate(931325466, -632238429), 299087037)

    def test0625(self):
        self.assertEquals(self.calculate(-1848336163, 1348763048), -499573115)

    def test0626(self):
        self.assertEquals(self.calculate(-77224369, -733257148), -810481517)

    def test0627(self):
        self.assertEquals(self.calculate(1638885231, 30394970), 1669280201)

    def test0628(self):
        self.assertEquals(self.calculate(-2002002952, -208635670), 2084328674)

    def test0629(self):
        self.assertEquals(self.calculate(873467318, -982106835), -108639517)

    def test0630(self):
        self.assertEquals(self.calculate(743157868, -214624889), 528532979)

    def test0631(self):
        self.assertEquals(self.calculate(447537380, -1872239609), -1424702229)

    def test0632(self):
        self.assertEquals(self.calculate(1599452078, -1059464158), 539987920)

    def test0633(self):
        self.assertEquals(self.calculate(328882218, -1192918224), -864036006)

    def test0634(self):
        self.assertEquals(self.calculate(1810129820, 1447873624), -1036963852)

    def test0635(self):
        self.assertEquals(self.calculate(208408915, -246383419), -37974504)

    def test0636(self):
        self.assertEquals(self.calculate(469601196, 279265393), 748866589)

    def test0637(self):
        self.assertEquals(self.calculate(613376222, 387037487), 1000413709)

    def test0638(self):
        self.assertEquals(self.calculate(1102859448, 20045401), 1122904849)

    def test0639(self):
        self.assertEquals(self.calculate(1602299719, -1646231760), -43932041)

    def test0640(self):
        self.assertEquals(self.calculate(-657876182, 1796270037), 1138393855)

    def test0641(self):
        self.assertEquals(self.calculate(1968215163, 77786992), 2046002155)

    def test0642(self):
        self.assertEquals(self.calculate(836375612, -2146757156), -1310381544)

    def test0643(self):
        self.assertEquals(self.calculate(107960779, -701935701), -593974922)

    def test0644(self):
        self.assertEquals(self.calculate(-431150196, 1607522920), 1176372724)

    def test0645(self):
        self.assertEquals(self.calculate(2145594898, -950113888), 1195481010)

    def test0646(self):
        self.assertEquals(self.calculate(-1249822826, 778946967), -470875859)

    def test0647(self):
        self.assertEquals(self.calculate(-725265342, -385169888), -1110435230)

    def test0648(self):
        self.assertEquals(self.calculate(-534043043, -1788221069), 1972703184)

    def test0649(self):
        self.assertEquals(self.calculate(-797598978, -1411451489), 2085916829)

    def test0650(self):
        self.assertEquals(self.calculate(-1892165053, 498956368), -1393208685)

    def test0651(self):
        self.assertEquals(self.calculate(1816420696, -1013794139), 802626557)

    def test0652(self):
        self.assertEquals(self.calculate(802266435, -992736826), -190470391)

    def test0653(self):
        self.assertEquals(self.calculate(-810203219, -1181886159), -1992089378)

    def test0654(self):
        self.assertEquals(self.calculate(1815201110, 5725483), 1820926593)

    def test0655(self):
        self.assertEquals(self.calculate(280064894, -714775961), -434711067)

    def test0656(self):
        self.assertEquals(self.calculate(-143912462, 1435243494), 1291331032)

    def test0657(self):
        self.assertEquals(self.calculate(312681033, -299475776), 13205257)

    def test0658(self):
        self.assertEquals(self.calculate(-1662036071, -1277205268), 1355725957)

    def test0659(self):
        self.assertEquals(self.calculate(161918062, 1792022353), 1953940415)

    def test0660(self):
        self.assertEquals(self.calculate(-1401733372, -697509896), -2099243268)

    def test0661(self):
        self.assertEquals(self.calculate(-1381159370, 1384016679), 2857309)

    def test0662(self):
        self.assertEquals(self.calculate(824040767, -1310576359), -486535592)

    def test0663(self):
        self.assertEquals(self.calculate(1904293407, -731920216), 1172373191)

    def test0664(self):
        self.assertEquals(self.calculate(131083041, -722177156), -591094115)

    def test0665(self):
        self.assertEquals(self.calculate(669464799, 2105936217), -1519566280)

    def test0666(self):
        self.assertEquals(self.calculate(1425838725, -8572667), 1417266058)

    def test0667(self):
        self.assertEquals(self.calculate(-880313737, 877582291), -2731446)

    def test0668(self):
        self.assertEquals(self.calculate(2060007671, 2045551319), -189408306)

    def test0669(self):
        self.assertEquals(self.calculate(46194381, 172683194), 218877575)

    def test0670(self):
        self.assertEquals(self.calculate(-1520526795, -173933926), -1694460721)

    def test0671(self):
        self.assertEquals(self.calculate(-1941985815, -1434671301), 918310180)

    def test0672(self):
        self.assertEquals(self.calculate(-442801681, -1785312142), 2066853473)

    def test0673(self):
        self.assertEquals(self.calculate(569609506, 1672223115), -2053134675)

    def test0674(self):
        self.assertEquals(self.calculate(-1602682371, 1629506844), 26824473)

    def test0675(self):
        self.assertEquals(self.calculate(1423967253, 538368869), 1962336122)

    def test0676(self):
        self.assertEquals(self.calculate(1662540700, -1882544835), -220004135)

    def test0677(self):
        self.assertEquals(self.calculate(1948079756, -1752592600), 195487156)

    def test0678(self):
        self.assertEquals(self.calculate(1066513757, 16940715), 1083454472)

    def test0679(self):
        self.assertEquals(self.calculate(-1996187318, -1644907949), 653872029)

    def test0680(self):
        self.assertEquals(self.calculate(-2007605343, -365424840), 1921937113)

    def test0681(self):
        self.assertEquals(self.calculate(-683591360, 275380684), -408210676)

    def test0682(self):
        self.assertEquals(self.calculate(334684357, -269590594), 65093763)

    def test0683(self):
        self.assertEquals(self.calculate(-92295366, -1164808084), -1257103450)

    def test0684(self):
        self.assertEquals(self.calculate(-356500915, -860615912), -1217116827)

    def test0685(self):
        self.assertEquals(self.calculate(1714214662, -1590592408), 123622254)

    def test0686(self):
        self.assertEquals(self.calculate(65713026, 1666645890), 1732358916)

    def test0687(self):
        self.assertEquals(self.calculate(-773156098, -388196719), -1161352817)

    def test0688(self):
        self.assertEquals(self.calculate(-854783031, -144377979), -999161010)

    def test0689(self):
        self.assertEquals(self.calculate(728679288, 1117169741), 1845849029)

    def test0690(self):
        self.assertEquals(self.calculate(-1755204164, -1511194190), 1028568942)

    def test0691(self):
        self.assertEquals(self.calculate(1995122678, -1487247935), 507874743)

    def test0692(self):
        self.assertEquals(self.calculate(-2064423162, -678849263), 1551694871)

    def test0693(self):
        self.assertEquals(self.calculate(-1488535795, 979366975), -509168820)

    def test0694(self):
        self.assertEquals(self.calculate(-1070521551, 661173996), -409347555)

    def test0695(self):
        self.assertEquals(self.calculate(-1659622801, 1700674484), 41051683)

    def test0696(self):
        self.assertEquals(self.calculate(1438624634, -1498887084), -60262450)

    def test0697(self):
        self.assertEquals(self.calculate(-287675003, -85574833), -373249836)

    def test0698(self):
        self.assertEquals(self.calculate(222855153, -734940282), -512085129)

    def test0699(self):
        self.assertEquals(self.calculate(540174496, 1086403963), 1626578459)

    def test0700(self):
        self.assertEquals(self.calculate(-1035455790, -485113353), -1520569143)

    def test0701(self):
        self.assertEquals(self.calculate(1775274417, 647165909), -1872526970)

    def test0702(self):
        self.assertEquals(self.calculate(-561675682, -2128833851), 1604457763)

    def test0703(self):
        self.assertEquals(self.calculate(2031052105, 384729447), -1879185744)

    def test0704(self):
        self.assertEquals(self.calculate(836228257, -627283723), 208944534)

    def test0705(self):
        self.assertEquals(self.calculate(232993454, -961199015), -728205561)

    def test0706(self):
        self.assertEquals(self.calculate(83055971, 1243910302), 1326966273)

    def test0707(self):
        self.assertEquals(self.calculate(308175649, 592506037), 900681686)

    def test0708(self):
        self.assertEquals(self.calculate(1167244980, 1601619792), -1526102524)

    def test0709(self):
        self.assertEquals(self.calculate(367631401, -815173612), -447542211)

    def test0710(self):
        self.assertEquals(self.calculate(-2083731279, -626785676), 1584450341)

    def test0711(self):
        self.assertEquals(self.calculate(490217981, -1876505091), -1386287110)

    def test0712(self):
        self.assertEquals(self.calculate(2138873809, 1565183716), -590909771)

    def test0713(self):
        self.assertEquals(self.calculate(545263738, -519725220), 25538518)

    def test0714(self):
        self.assertEquals(self.calculate(-1237657493, 58226084), -1179431409)

    def test0715(self):
        self.assertEquals(self.calculate(1066313623, 588113872), 1654427495)

    def test0716(self):
        self.assertEquals(self.calculate(382176791, 1369632910), 1751809701)

    def test0717(self):
        self.assertEquals(self.calculate(1010006339, -2020766681), -1010760342)

    def test0718(self):
        self.assertEquals(self.calculate(1903761197, -1969676951), -65915754)

    def test0719(self):
        self.assertEquals(self.calculate(-1117381784, 1938614585), 821232801)

    def test0720(self):
        self.assertEquals(self.calculate(1882528146, -1470266786), 412261360)

    def test0721(self):
        self.assertEquals(self.calculate(36471405, 1422075656), 1458547061)

    def test0722(self):
        self.assertEquals(self.calculate(-1019927295, -1762384954), 1512655047)

    def test0723(self):
        self.assertEquals(self.calculate(-164170444, -624656861), -788827305)

    def test0724(self):
        self.assertEquals(self.calculate(-378643643, -1585149706), -1963793349)

    def test0725(self):
        self.assertEquals(self.calculate(-284024051, 324950496), 40926445)

    def test0726(self):
        self.assertEquals(self.calculate(380441201, 375952665), 756393866)

    def test0727(self):
        self.assertEquals(self.calculate(1198441299, -711096594), 487344705)

    def test0728(self):
        self.assertEquals(self.calculate(1319759846, 579300588), 1899060434)

    def test0729(self):
        self.assertEquals(self.calculate(404986175, 1566585617), 1971571792)

    def test0730(self):
        self.assertEquals(self.calculate(764234954, -962865005), -198630051)

    def test0731(self):
        self.assertEquals(self.calculate(-402430596, 1299574481), 897143885)

    def test0732(self):
        self.assertEquals(self.calculate(223677066, -923314275), -699637209)

    def test0733(self):
        self.assertEquals(self.calculate(-370692593, 116425568), -254267025)

    def test0734(self):
        self.assertEquals(self.calculate(-2039266878, -1942935694), 312764724)

    def test0735(self):
        self.assertEquals(self.calculate(1525234102, 1750620331), -1019112863)

    def test0736(self):
        self.assertEquals(self.calculate(1302654300, 57894739), 1360549039)

    def test0737(self):
        self.assertEquals(self.calculate(1348610423, 1469269893), -1477086980)

    def test0738(self):
        self.assertEquals(self.calculate(-1247228140, -1394821653), 1652917503)

    def test0739(self):
        self.assertEquals(self.calculate(378858685, -983371547), -604512862)

    def test0740(self):
        self.assertEquals(self.calculate(-736798173, 1801706536), 1064908363)

    def test0741(self):
        self.assertEquals(self.calculate(-326716954, -1875171459), 2093078883)

    def test0742(self):
        self.assertEquals(self.calculate(805839414, 593342255), 1399181669)

    def test0743(self):
        self.assertEquals(self.calculate(1835846735, 1144909871), -1314210690)

    def test0744(self):
        self.assertEquals(self.calculate(-2044833900, -854583573), 1395549823)

    def test0745(self):
        self.assertEquals(self.calculate(1117356451, 330489319), 1447845770)

    def test0746(self):
        self.assertEquals(self.calculate(-280480618, -429694465), -710175083)

    def test0747(self):
        self.assertEquals(self.calculate(1233295682, 89535848), 1322831530)

    def test0748(self):
        self.assertEquals(self.calculate(-229726993, -483800737), -713527730)

    def test0749(self):
        self.assertEquals(self.calculate(2007513273, 101239956), 2108753229)

    def test0750(self):
        self.assertEquals(self.calculate(47840937, 473143580), 520984517)

    def test0751(self):
        self.assertEquals(self.calculate(-1749744412, 707566627), -1042177785)

    def test0752(self):
        self.assertEquals(self.calculate(-2136068233, 551973491), -1584094742)

    def test0753(self):
        self.assertEquals(self.calculate(-727270282, 807667215), 80396933)

    def test0754(self):
        self.assertEquals(self.calculate(1267571263, -1161314149), 106257114)

    def test0755(self):
        self.assertEquals(self.calculate(-801310717, -366718893), -1168029610)

    def test0756(self):
        self.assertEquals(self.calculate(373970837, -1649118253), -1275147416)

    def test0757(self):
        self.assertEquals(self.calculate(1950049635, -1849888957), 100160678)

    def test0758(self):
        self.assertEquals(self.calculate(-1972844269, -2058995510), 263127517)

    def test0759(self):
        self.assertEquals(self.calculate(-1310492302, 1724074063), 413581761)

    def test0760(self):
        self.assertEquals(self.calculate(-1430785617, -1237401294), 1626780385)

    def test0761(self):
        self.assertEquals(self.calculate(-1018263673, -49315838), -1067579511)

    def test0762(self):
        self.assertEquals(self.calculate(1217310193, -1205311327), 11998866)

    def test0763(self):
        self.assertEquals(self.calculate(929521273, -1584968472), -655447199)

    def test0764(self):
        self.assertEquals(self.calculate(-46224045, 589543036), 543318991)

    def test0765(self):
        self.assertEquals(self.calculate(-574052026, -1001875114), -1575927140)

    def test0766(self):
        self.assertEquals(self.calculate(-731053273, -2090421026), 1473492997)

    def test0767(self):
        self.assertEquals(self.calculate(1353324508, -134940346), 1218384162)

    def test0768(self):
        self.assertEquals(self.calculate(1906616955, 2061448141), -326902200)

    def test0769(self):
        self.assertEquals(self.calculate(-1201480901, 1286691998), 85211097)

    def test0770(self):
        self.assertEquals(self.calculate(-1067171590, -393205271), -1460376861)

    def test0771(self):
        self.assertEquals(self.calculate(355644613, -730787735), -375143122)

    def test0772(self):
        self.assertEquals(self.calculate(-1954871926, -384186378), 1955908992)

    def test0773(self):
        self.assertEquals(self.calculate(-1880759199, 1050030527), -830728672)

    def test0774(self):
        self.assertEquals(self.calculate(-1672694242, 1448001020), -224693222)

    def test0775(self):
        self.assertEquals(self.calculate(-3214214, 807009793), 803795579)

    def test0776(self):
        self.assertEquals(self.calculate(1820240009, 184985837), 2005225846)

    def test0777(self):
        self.assertEquals(self.calculate(249756259, -1521574453), -1271818194)

    def test0778(self):
        self.assertEquals(self.calculate(1375819929, 1917011486), -1002135881)

    def test0779(self):
        self.assertEquals(self.calculate(-1172338273, 1281870871), 109532598)

    def test0780(self):
        self.assertEquals(self.calculate(369242766, -1355608891), -986366125)

    def test0781(self):
        self.assertEquals(self.calculate(-2085045217, -2125424492), 84497587)

    def test0782(self):
        self.assertEquals(self.calculate(922970738, 1706503281), -1665493277)

    def test0783(self):
        self.assertEquals(self.calculate(2041160178, -1258601462), 782558716)

    def test0784(self):
        self.assertEquals(self.calculate(-1569451842, 633835888), -935615954)

    def test0785(self):
        self.assertEquals(self.calculate(265054324, -1439947938), -1174893614)

    def test0786(self):
        self.assertEquals(self.calculate(621779517, 764003422), 1385782939)

    def test0787(self):
        self.assertEquals(self.calculate(1968619734, 1108823498), -1217524064)

    def test0788(self):
        self.assertEquals(self.calculate(-318221028, 459003399), 140782371)

    def test0789(self):
        self.assertEquals(self.calculate(-1279596614, 1924775565), 645178951)

    def test0790(self):
        self.assertEquals(self.calculate(-1151486676, 1273411228), 121924552)

    def test0791(self):
        self.assertEquals(self.calculate(-1323317798, -1801236837), 1170412661)

    def test0792(self):
        self.assertEquals(self.calculate(-857687967, 1521013301), 663325334)

    def test0793(self):
        self.assertEquals(self.calculate(2127302236, -138952410), 1988349826)

    def test0794(self):
        self.assertEquals(self.calculate(1149720470, 1552373317), -1592873509)

    def test0795(self):
        self.assertEquals(self.calculate(-1247811436, 651238197), -596573239)

    def test0796(self):
        self.assertEquals(self.calculate(-1803077129, 943559057), -859518072)

    def test0797(self):
        self.assertEquals(self.calculate(-535652519, 304539387), -231113132)

    def test0798(self):
        self.assertEquals(self.calculate(-1445046335, -1310843663), 1539077298)

    def test0799(self):
        self.assertEquals(self.calculate(1307121323, -2069246025), -762124702)

    def test0800(self):
        self.assertEquals(self.calculate(-1758940915, 1209437660), -549503255)

    def test0801(self):
        self.assertEquals(self.calculate(1880935140, 185199344), 2066134484)

    def test0802(self):
        self.assertEquals(self.calculate(-172962471, -1248934494), -1421896965)

    def test0803(self):
        self.assertEquals(self.calculate(-162551063, 1007963319), 845412256)

    def test0804(self):
        self.assertEquals(self.calculate(-134212297, -378466998), -512679295)

    def test0805(self):
        self.assertEquals(self.calculate(-966924006, -473426091), -1440350097)

    def test0806(self):
        self.assertEquals(self.calculate(776034079, 29495104), 805529183)

    def test0807(self):
        self.assertEquals(self.calculate(-1562665537, -1054791584), 1677510175)

    def test0808(self):
        self.assertEquals(self.calculate(1745701678, 132331599), 1878033277)

    def test0809(self):
        self.assertEquals(self.calculate(-190553745, 53940225), -136613520)

    def test0810(self):
        self.assertEquals(self.calculate(308825346, 1196083391), 1504908737)

    def test0811(self):
        self.assertEquals(self.calculate(629362558, -2100310840), -1470948282)

    def test0812(self):
        self.assertEquals(self.calculate(-301079285, -1855247593), 2138640418)

    def test0813(self):
        self.assertEquals(self.calculate(1756991500, -1759883523), -2892023)

    def test0814(self):
        self.assertEquals(self.calculate(-1662056225, -346934474), -2008990699)

    def test0815(self):
        self.assertEquals(self.calculate(1908867113, -848555624), 1060311489)

    def test0816(self):
        self.assertEquals(self.calculate(-1965954864, 243299066), -1722655798)

    def test0817(self):
        self.assertEquals(self.calculate(-638258539, 522447460), -115811079)

    def test0818(self):
        self.assertEquals(self.calculate(-1780091907, -1782621392), 732253997)

    def test0819(self):
        self.assertEquals(self.calculate(19966043, 1111796567), 1131762610)

    def test0820(self):
        self.assertEquals(self.calculate(1429703309, -251646830), 1178056479)

    def test0821(self):
        self.assertEquals(self.calculate(945818044, -1865284620), -919466576)

    def test0822(self):
        self.assertEquals(self.calculate(-587752370, 1964999198), 1377246828)

    def test0823(self):
        self.assertEquals(self.calculate(-516298394, -1199795528), -1716093922)

    def test0824(self):
        self.assertEquals(self.calculate(2132966536, 858383398), -1303617362)

    def test0825(self):
        self.assertEquals(self.calculate(892088162, 943743514), 1835831676)

    def test0826(self):
        self.assertEquals(self.calculate(2005759964, 1061950604), -1227256728)

    def test0827(self):
        self.assertEquals(self.calculate(-352576452, 1698011596), 1345435144)

    def test0828(self):
        self.assertEquals(self.calculate(-1126795539, -1597070246), 1571101511)

    def test0829(self):
        self.assertEquals(self.calculate(2122892159, 1100004353), -1072070784)

    def test0830(self):
        self.assertEquals(self.calculate(-2005283402, 1559414877), -445868525)

    def test0831(self):
        self.assertEquals(self.calculate(-838321200, 998573063), 160251863)

    def test0832(self):
        self.assertEquals(self.calculate(-649482906, -601893432), -1251376338)

    def test0833(self):
        self.assertEquals(self.calculate(-2069998885, -597403192), 1627565219)

    def test0834(self):
        self.assertEquals(self.calculate(-603339516, -1289347223), -1892686739)

    def test0835(self):
        self.assertEquals(self.calculate(468077959, 905719485), 1373797444)

    def test0836(self):
        self.assertEquals(self.calculate(1130809973, 646903665), 1777713638)

    def test0837(self):
        self.assertEquals(self.calculate(1470741579, 1976423069), -847802648)

    def test0838(self):
        self.assertEquals(self.calculate(786696960, 426333722), 1213030682)

    def test0839(self):
        self.assertEquals(self.calculate(2086647247, -879676643), 1206970604)

    def test0840(self):
        self.assertEquals(self.calculate(481583529, -740054765), -258471236)

    def test0841(self):
        self.assertEquals(self.calculate(386520370, 1713524056), 2100044426)

    def test0842(self):
        self.assertEquals(self.calculate(1364117909, -858841880), 505276029)

    def test0843(self):
        self.assertEquals(self.calculate(1464222196, -1638101345), -173879149)

    def test0844(self):
        self.assertEquals(self.calculate(-388328873, 1028526240), 640197367)

    def test0845(self):
        self.assertEquals(self.calculate(-1456375940, 912972017), -543403923)

    def test0846(self):
        self.assertEquals(self.calculate(-413344606, 1952507050), 1539162444)

    def test0847(self):
        self.assertEquals(self.calculate(-56473643, 1273012007), 1216538364)

    def test0848(self):
        self.assertEquals(self.calculate(1421657146, 1969403178), -903906972)

    def test0849(self):
        self.assertEquals(self.calculate(462322313, 1142499053), 1604821366)

    def test0850(self):
        self.assertEquals(self.calculate(-582441278, 1226986131), 644544853)

    def test0851(self):
        self.assertEquals(self.calculate(1353455338, 830881163), -2110630795)

    def test0852(self):
        self.assertEquals(self.calculate(383553314, 1985537756), -1925876226)

    def test0853(self):
        self.assertEquals(self.calculate(-26480676, 1964300096), 1937819420)

    def test0854(self):
        self.assertEquals(self.calculate(-591514061, 872618167), 281104106)

    def test0855(self):
        self.assertEquals(self.calculate(-1052893398, -639991242), -1692884640)

    def test0856(self):
        self.assertEquals(self.calculate(-146761473, 1153809734), 1007048261)

    def test0857(self):
        self.assertEquals(self.calculate(-1284448168, -1885940333), 1124578795)

    def test0858(self):
        self.assertEquals(self.calculate(2072356410, -1561195649), 511160761)

    def test0859(self):
        self.assertEquals(self.calculate(-878409161, -1339157712), 2077400423)

    def test0860(self):
        self.assertEquals(self.calculate(1558481808, 956493449), -1779992039)

    def test0861(self):
        self.assertEquals(self.calculate(671469379, 623274288), 1294743667)

    def test0862(self):
        self.assertEquals(self.calculate(-1252631978, -1239950391), 1802384927)

    def test0863(self):
        self.assertEquals(self.calculate(982800955, 2020638110), -1291528231)

    def test0864(self):
        self.assertEquals(self.calculate(-1772835871, 1366438077), -406397794)

    def test0865(self):
        self.assertEquals(self.calculate(-344060886, 70576742), -273484144)

    def test0866(self):
        self.assertEquals(self.calculate(954399553, -1579507583), -625108030)

    def test0867(self):
        self.assertEquals(self.calculate(2022294540, -1172687224), 849607316)

    def test0868(self):
        self.assertEquals(self.calculate(1722746873, 542734830), -2029485593)

    def test0869(self):
        self.assertEquals(self.calculate(-1032483505, -269021437), -1301504942)

    def test0870(self):
        self.assertEquals(self.calculate(-1584293000, -1286717259), 1423957037)

    def test0871(self):
        self.assertEquals(self.calculate(1756254261, 733636652), -1805076383)

    def test0872(self):
        self.assertEquals(self.calculate(-86829542, -1598413746), -1685243288)

    def test0873(self):
        self.assertEquals(self.calculate(-1382624791, 309828825), -1072795966)

    def test0874(self):
        self.assertEquals(self.calculate(1340583635, -1126362412), 214221223)

    def test0875(self):
        self.assertEquals(self.calculate(-732165977, -523053282), -1255219259)

    def test0876(self):
        self.assertEquals(self.calculate(1240798941, 1694626095), -1359542260)

    def test0877(self):
        self.assertEquals(self.calculate(1291019968, 585018477), 1876038445)

    def test0878(self):
        self.assertEquals(self.calculate(-110170199, -1569223163), -1679393362)

    def test0879(self):
        self.assertEquals(self.calculate(-1031765113, 2004514077), 972748964)

    def test0880(self):
        self.assertEquals(self.calculate(-1962989528, 240752530), -1722236998)

    def test0881(self):
        self.assertEquals(self.calculate(-816527518, 1547287913), 730760395)

    def test0882(self):
        self.assertEquals(self.calculate(-880950657, -1231287535), -2112238192)

    def test0883(self):
        self.assertEquals(self.calculate(1120350499, -1185434767), -65084268)

    def test0884(self):
        self.assertEquals(self.calculate(-470217060, 1251087953), 780870893)

    def test0885(self):
        self.assertEquals(self.calculate(-1837680358, 1480538470), -357141888)

    def test0886(self):
        self.assertEquals(self.calculate(-497930555, -2034963719), 1762073022)

    def test0887(self):
        self.assertEquals(self.calculate(-455288754, -1088425684), -1543714438)

    def test0888(self):
        self.assertEquals(self.calculate(184453649, 1567938879), 1752392528)

    def test0889(self):
        self.assertEquals(self.calculate(-873769853, -888792744), -1762562597)

    def test0890(self):
        self.assertEquals(self.calculate(585519491, 1178359879), 1763879370)

    def test0891(self):
        self.assertEquals(self.calculate(-1151191853, -531296782), -1682488635)

    def test0892(self):
        self.assertEquals(self.calculate(364325975, 164917818), 529243793)

    def test0893(self):
        self.assertEquals(self.calculate(1876467867, -398464671), 1478003196)

    def test0894(self):
        self.assertEquals(self.calculate(1451661899, 2083821956), -759483441)

    def test0895(self):
        self.assertEquals(self.calculate(-465635513, -631975365), -1097610878)

    def test0896(self):
        self.assertEquals(self.calculate(2136571889, 901557760), -1256837647)

    def test0897(self):
        self.assertEquals(self.calculate(-405027338, 999411064), 594383726)

    def test0898(self):
        self.assertEquals(self.calculate(1349295451, -821159767), 528135684)

    def test0899(self):
        self.assertEquals(self.calculate(996991684, 1352038152), -1945937460)

    def test0900(self):
        self.assertEquals(self.calculate(1179291389, 720191994), 1899483383)

    def test0901(self):
        self.assertEquals(self.calculate(-398112202, -1745155195), -2143267397)

    def test0902(self):
        self.assertEquals(self.calculate(-196564769, 1344918333), 1148353564)

    def test0903(self):
        self.assertEquals(self.calculate(405335659, 1559132092), 1964467751)

    def test0904(self):
        self.assertEquals(self.calculate(834317795, -761130369), 73187426)

    def test0905(self):
        self.assertEquals(self.calculate(-345275240, -2015970877), 1933721179)

    def test0906(self):
        self.assertEquals(self.calculate(134011951, 1604495549), 1738507500)

    def test0907(self):
        self.assertEquals(self.calculate(690282943, -1412494482), -722211539)

    def test0908(self):
        self.assertEquals(self.calculate(-160949734, 1288909770), 1127960036)

    def test0909(self):
        self.assertEquals(self.calculate(778680834, -1847533752), -1068852918)

    def test0910(self):
        self.assertEquals(self.calculate(-1924397459, 851679525), -1072717934)

    def test0911(self):
        self.assertEquals(self.calculate(-691220120, 640280031), -50940089)

    def test0912(self):
        self.assertEquals(self.calculate(1661730043, -647830316), 1013899727)

    def test0913(self):
        self.assertEquals(self.calculate(-1738206487, 310912623), -1427293864)

    def test0914(self):
        self.assertEquals(self.calculate(-938993044, 1423671749), 484678705)

    def test0915(self):
        self.assertEquals(self.calculate(1143305587, 815793426), 1959099013)

    def test0916(self):
        self.assertEquals(self.calculate(-1110754043, -212775712), -1323529755)

    def test0917(self):
        self.assertEquals(self.calculate(-841332419, -1994108295), 1459526582)

    def test0918(self):
        self.assertEquals(self.calculate(1540236413, 640162017), -2114568866)

    def test0919(self):
        self.assertEquals(self.calculate(-2053997300, -1644484563), 596485433)

    def test0920(self):
        self.assertEquals(self.calculate(-1942670233, 1159602755), -783067478)

    def test0921(self):
        self.assertEquals(self.calculate(1949532572, 487764613), -1857670111)

    def test0922(self):
        self.assertEquals(self.calculate(794498611, 235107946), 1029606557)

    def test0923(self):
        self.assertEquals(self.calculate(-447193633, -529132824), -976326457)

    def test0924(self):
        self.assertEquals(self.calculate(-2068921736, 109872036), -1959049700)

    def test0925(self):
        self.assertEquals(self.calculate(-1509381094, -587965841), -2097346935)

    def test0926(self):
        self.assertEquals(self.calculate(539406716, -1234573005), -695166289)

    def test0927(self):
        self.assertEquals(self.calculate(1256460403, 1568592561), -1469914332)

    def test0928(self):
        self.assertEquals(self.calculate(282766128, -1734497984), -1451731856)

    def test0929(self):
        self.assertEquals(self.calculate(280749989, -1722205956), -1441455967)

    def test0930(self):
        self.assertEquals(self.calculate(-1699115629, 1857130392), 158014763)

    def test0931(self):
        self.assertEquals(self.calculate(-772599703, 359993799), -412605904)

    def test0932(self):
        self.assertEquals(self.calculate(1835029171, -669702583), 1165326588)

    def test0933(self):
        self.assertEquals(self.calculate(-282744275, 930880495), 648136220)

    def test0934(self):
        self.assertEquals(self.calculate(-1152091920, 645222246), -506869674)

    def test0935(self):
        self.assertEquals(self.calculate(-1864350859, -936990311), 1493626126)

    def test0936(self):
        self.assertEquals(self.calculate(-413301305, 428206899), 14905594)

    def test0937(self):
        self.assertEquals(self.calculate(42056463, 720930928), 762987391)

    def test0938(self):
        self.assertEquals(self.calculate(1526489766, -871988016), 654501750)

    def test0939(self):
        self.assertEquals(self.calculate(1889340325, 1775820798), -629806173)

    def test0940(self):
        self.assertEquals(self.calculate(1861226400, -1208166606), 653059794)

    def test0941(self):
        self.assertEquals(self.calculate(-1157005686, 1632825859), 475820173)

    def test0942(self):
        self.assertEquals(self.calculate(174740801, 120814139), 295554940)

    def test0943(self):
        self.assertEquals(self.calculate(1180224337, -1056718906), 123505431)

    def test0944(self):
        self.assertEquals(self.calculate(-659059181, -1350487276), -2009546457)

    def test0945(self):
        self.assertEquals(self.calculate(-1752972837, -733696199), 1808298260)

    def test0946(self):
        self.assertEquals(self.calculate(1443252096, -1343517317), 99734779)

    def test0947(self):
        self.assertEquals(self.calculate(-128580255, 2118912580), 1990332325)

    def test0948(self):
        self.assertEquals(self.calculate(957737335, -1689158458), -731421123)

    def test0949(self):
        self.assertEquals(self.calculate(-1977008224, 328012862), -1648995362)

    def test0950(self):
        self.assertEquals(self.calculate(1359106016, 966424841), -1969436439)

    def test0951(self):
        self.assertEquals(self.calculate(904841931, -1061959168), -157117237)

    def test0952(self):
        self.assertEquals(self.calculate(-1058222890, 360092060), -698130830)

    def test0953(self):
        self.assertEquals(self.calculate(1876341371, 1317141295), -1101484630)

    def test0954(self):
        self.assertEquals(self.calculate(822663284, -632004430), 190658854)

    def test0955(self):
        self.assertEquals(self.calculate(-231857090, 528718100), 296861010)

    def test0956(self):
        self.assertEquals(self.calculate(745047126, 1208949398), 1953996524)

    def test0957(self):
        self.assertEquals(self.calculate(-632039714, -2028449200), 1634478382)

    def test0958(self):
        self.assertEquals(self.calculate(-240317057, 775719759), 535402702)

    def test0959(self):
        self.assertEquals(self.calculate(1206953203, -1170782640), 36170563)

    def test0960(self):
        self.assertEquals(self.calculate(-1217928470, -1144342656), 1932696170)

    def test0961(self):
        self.assertEquals(self.calculate(-1050503664, -1123659293), 2120804339)

    def test0962(self):
        self.assertEquals(self.calculate(800668390, -1930391525), -1129723135)

    def test0963(self):
        self.assertEquals(self.calculate(-332451051, -1274965956), -1607417007)

    def test0964(self):
        self.assertEquals(self.calculate(-1325586826, 1910655675), 585068849)

    def test0965(self):
        self.assertEquals(self.calculate(-355900094, -82439373), -438339467)

    def test0966(self):
        self.assertEquals(self.calculate(-934750691, 1192608278), 257857587)

    def test0967(self):
        self.assertEquals(self.calculate(-2082725801, 919830825), -1162894976)

    def test0968(self):
        self.assertEquals(self.calculate(61032850, 1738472075), 1799504925)

    def test0969(self):
        self.assertEquals(self.calculate(-1924724412, -1060208161), 1310034723)

    def test0970(self):
        self.assertEquals(self.calculate(1831543462, 826063523), -1637360311)

    def test0971(self):
        self.assertEquals(self.calculate(-140983866, -31796546), -172780412)

    def test0972(self):
        self.assertEquals(self.calculate(-819224407, -448214073), -1267438480)

    def test0973(self):
        self.assertEquals(self.calculate(306834802, -868743500), -561908698)

    def test0974(self):
        self.assertEquals(self.calculate(427814930, -1611043181), -1183228251)

    def test0975(self):
        self.assertEquals(self.calculate(161340370, -1552359845), -1391019475)

    def test0976(self):
        self.assertEquals(self.calculate(-1740631498, 1157535366), -583096132)

    def test0977(self):
        self.assertEquals(self.calculate(141108098, -1803577013), -1662468915)

    def test0978(self):
        self.assertEquals(self.calculate(-1769021801, -2145054781), 380890714)

    def test0979(self):
        self.assertEquals(self.calculate(-1483771771, 1541126371), 57354600)

    def test0980(self):
        self.assertEquals(self.calculate(-1595633250, 1366455290), -229177960)

    def test0981(self):
        self.assertEquals(self.calculate(358657283, -526991202), -168333919)

    def test0982(self):
        self.assertEquals(self.calculate(-1613749439, -98406135), -1712155574)

    def test0983(self):
        self.assertEquals(self.calculate(54494898, 949139268), 1003634166)

    def test0984(self):
        self.assertEquals(self.calculate(-367472421, -2140811274), 1786683601)

    def test0985(self):
        self.assertEquals(self.calculate(865795757, 1516630251), -1912541288)

    def test0986(self):
        self.assertEquals(self.calculate(1284555276, -177647249), 1106908027)

    def test0987(self):
        self.assertEquals(self.calculate(-1016980533, 1156476430), 139495897)

    def test0988(self):
        self.assertEquals(self.calculate(-1636437551, -761165521), 1897364224)

    def test0989(self):
        self.assertEquals(self.calculate(230690810, 145563954), 376254764)

    def test0990(self):
        self.assertEquals(self.calculate(1226583443, 904483308), 2131066751)

    def test0991(self):
        self.assertEquals(self.calculate(-1692207191, 744543865), -947663326)

    def test0992(self):
        self.assertEquals(self.calculate(-949827387, -1395368576), 1949771333)

    def test0993(self):
        self.assertEquals(self.calculate(-863870422, -454763948), -1318634370)

    def test0994(self):
        self.assertEquals(self.calculate(370888227, -928012959), -557124732)

    def test0995(self):
        self.assertEquals(self.calculate(-307702421, 514306136), 206603715)

    def test0996(self):
        self.assertEquals(self.calculate(-1766717644, -1021990165), 1506259487)

    def test0997(self):
        self.assertEquals(self.calculate(-698782090, 977373139), 278591049)

    def test0998(self):
        self.assertEquals(self.calculate(-2093284462, -1652241387), 549441447)

    def test0999(self):
        self.assertEquals(self.calculate(-1687722697, -117032980), -1804755677)

    def test1000(self):
        self.assertEquals(self.calculate(949612926, 1333676792), -2011677578)

    def test1001(self):
        self.assertEquals(self.calculate(-2141168675, 1470867901), -670300774)

    def test1002(self):
        self.assertEquals(self.calculate(-1068358189, 1245377147), 177018958)

    def test1003(self):
        self.assertEquals(self.calculate(-1277045766, 2107409977), 830364211)

    def test1004(self):
        self.assertEquals(self.calculate(73246283, 665271372), 738517655)

    def test1005(self):
        self.assertEquals(self.calculate(-957766001, -746926018), -1704692019)

    def test1006(self):
        self.assertEquals(self.calculate(1277363350, -1076362180), 201001170)

    def test1007(self):
        self.assertEquals(self.calculate(-686391332, -1004190842), -1690582174)

    def test1008(self):
        self.assertEquals(self.calculate(-1208840590, -456775472), -1665616062)

    def test1009(self):
        self.assertEquals(self.calculate(-1042702418, 1131030650), 88328232)

    def test1010(self):
        self.assertEquals(self.calculate(-18600828, 1085220840), 1066620012)

    def test1011(self):
        self.assertEquals(self.calculate(-1504824915, 758974888), -745850027)

    def test1012(self):
        self.assertEquals(self.calculate(1904640371, -754782727), 1149857644)

    def test1013(self):
        self.assertEquals(self.calculate(-634036214, -396846360), -1030882574)

    def test1014(self):
        self.assertEquals(self.calculate(-1969039048, 1112405576), -856633472)

    def test1015(self):
        self.assertEquals(self.calculate(671242505, 535377658), 1206620163)

    def test1016(self):
        self.assertEquals(self.calculate(253250570, -3419412), 249831158)

    def test1017(self):
        self.assertEquals(self.calculate(-590424655, 1789437446), 1199012791)

    def test1018(self):
        self.assertEquals(self.calculate(706595151, 1117694278), 1824289429)

    def test1019(self):
        self.assertEquals(self.calculate(1244935190, 1763895136), -1286136970)

    def test1020(self):
        self.assertEquals(self.calculate(-1055015771, -831570986), -1886586757)

    def test1021(self):
        self.assertEquals(self.calculate(1385363606, 1063115090), -1846488600)

    def test1022(self):
        self.assertEquals(self.calculate(1728489457, -968899691), 759589766)

    def test1023(self):
        self.assertEquals(self.calculate(-593986447, 1771640165), 1177653718)


class TestVM_Add_LongFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_LONG_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushL(lhs)
        v.VM_PushF(rhs)
        v.VM_Add()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(1073148002, 178046.0), 1073326048.00)

    def test0001(self):
        self.assertEquals(self.calculate(620171772, 98337.0), 620270109.00)

    def test0002(self):
        self.assertEquals(self.calculate(-1184389830, 84582.0), -1184305248.00)

    def test0003(self):
        self.assertEquals(self.calculate(-89147556, 60344.0), -89087212.00)

    def test0004(self):
        self.assertEquals(self.calculate(-1768731187, 120921.0), -1768610266.00)

    def test0005(self):
        self.assertEquals(self.calculate(750648231, -106452.0), 750541779.00)

    def test0006(self):
        self.assertEquals(self.calculate(527003927, -73844.0), 526930083.00)

    def test0007(self):
        self.assertEquals(self.calculate(1222577309, 144097.0), 1222721406.00)

    def test0008(self):
        self.assertEquals(self.calculate(-1918640498, 103657.0), -1918536841.00)

    def test0009(self):
        self.assertEquals(self.calculate(-1955152284, 11142.0), -1955141142.00)

    def test0010(self):
        self.assertEquals(self.calculate(455769959, 69439.0), 455839398.00)

    def test0011(self):
        self.assertEquals(self.calculate(1041365660, 169351.0), 1041535011.00)

    def test0012(self):
        self.assertEquals(self.calculate(-1806893713, -131525.0), -1807025238.00)

    def test0013(self):
        self.assertEquals(self.calculate(2135927149, 137188.0), 2136064337.00)

    def test0014(self):
        self.assertEquals(self.calculate(-399500366, -46074.0), -399546440.00)

    def test0015(self):
        self.assertEquals(self.calculate(306613763, -112677.0), 306501086.00)

    def test0016(self):
        self.assertEquals(self.calculate(-882383776, 20901.0), -882362875.00)

    def test0017(self):
        self.assertEquals(self.calculate(1654906215, -165572.0), 1654740643.00)

    def test0018(self):
        self.assertEquals(self.calculate(1578299740, -99724.0), 1578200016.00)

    def test0019(self):
        self.assertEquals(self.calculate(-1280652399, -21979.0), -1280674378.00)

    def test0020(self):
        self.assertEquals(self.calculate(-1066796590, -46450.0), -1066843040.00)

    def test0021(self):
        self.assertEquals(self.calculate(-930915776, 39535.0), -930876241.00)

    def test0022(self):
        self.assertEquals(self.calculate(-1486527295, 33731.0), -1486493564.00)

    def test0023(self):
        self.assertEquals(self.calculate(-777818191, -129184.0), -777947375.00)

    def test0024(self):
        self.assertEquals(self.calculate(882721762, 145501.0), 882867263.00)

    def test0025(self):
        self.assertEquals(self.calculate(-1340365438, -17341.0), -1340382779.00)

    def test0026(self):
        self.assertEquals(self.calculate(-1891862953, 167523.0), -1891695430.00)

    def test0027(self):
        self.assertEquals(self.calculate(1156490269, 154743.0), 1156645012.00)

    def test0028(self):
        self.assertEquals(self.calculate(2090769609, -10362.0), 2090759247.00)

    def test0029(self):
        self.assertEquals(self.calculate(-989353639, -112242.0), -989465881.00)

    def test0030(self):
        self.assertEquals(self.calculate(1661947496, -86767.0), 1661860729.00)

    def test0031(self):
        self.assertEquals(self.calculate(376686167, -128683.0), 376557484.00)

    def test0032(self):
        self.assertEquals(self.calculate(343929405, -99428.0), 343829977.00)

    def test0033(self):
        self.assertEquals(self.calculate(1470397899, 109174.0), 1470507073.00)

    def test0034(self):
        self.assertEquals(self.calculate(625754158, -24981.0), 625729177.00)

    def test0035(self):
        self.assertEquals(self.calculate(-31989112, -119927.0), -32109039.00)

    def test0036(self):
        self.assertEquals(self.calculate(-627130720, -148888.0), -627279608.00)

    def test0037(self):
        self.assertEquals(self.calculate(83622358, 87183.0), 83709541.00)

    def test0038(self):
        self.assertEquals(self.calculate(-1320774022, -178513.0), -1320952535.00)

    def test0039(self):
        self.assertEquals(self.calculate(-1596090762, 173575.0), -1595917187.00)

    def test0040(self):
        self.assertEquals(self.calculate(865788037, -134049.0), 865653988.00)

    def test0041(self):
        self.assertEquals(self.calculate(314702254, -98537.0), 314603717.00)

    def test0042(self):
        self.assertEquals(self.calculate(-232580919, 36734.0), -232544185.00)

    def test0043(self):
        self.assertEquals(self.calculate(-1743676370, -89585.0), -1743765955.00)

    def test0044(self):
        self.assertEquals(self.calculate(-1122244108, -114860.0), -1122358968.00)

    def test0045(self):
        self.assertEquals(self.calculate(-844411225, -123916.0), -844535141.00)

    def test0046(self):
        self.assertEquals(self.calculate(417481704, 46909.0), 417528613.00)

    def test0047(self):
        self.assertEquals(self.calculate(-989212635, 121325.0), -989091310.00)

    def test0048(self):
        self.assertEquals(self.calculate(1722825731, -143179.0), 1722682552.00)

    def test0049(self):
        self.assertEquals(self.calculate(549241876, -109971.0), 549131905.00)

    def test0050(self):
        self.assertEquals(self.calculate(1644941107, -111066.0), 1644830041.00)

    def test0051(self):
        self.assertEquals(self.calculate(135901111, -162455.0), 135738656.00)

    def test0052(self):
        self.assertEquals(self.calculate(-1740557694, 21139.0), -1740536555.00)

    def test0053(self):
        self.assertEquals(self.calculate(-132603104, -13712.0), -132616816.00)

    def test0054(self):
        self.assertEquals(self.calculate(1980082681, -184881.0), 1979897800.00)

    def test0055(self):
        self.assertEquals(self.calculate(-528732712, 124574.0), -528608138.00)

    def test0056(self):
        self.assertEquals(self.calculate(859849883, -192542.0), 859657341.00)

    def test0057(self):
        self.assertEquals(self.calculate(-888324739, 29976.0), -888294763.00)

    def test0058(self):
        self.assertEquals(self.calculate(2001040246, -96108.0), 2000944138.00)

    def test0059(self):
        self.assertEquals(self.calculate(-1965109211, 174113.0), -1964935098.00)

    def test0060(self):
        self.assertEquals(self.calculate(-1072862655, 59343.0), -1072803312.00)

    def test0061(self):
        self.assertEquals(self.calculate(-491204570, 103059.0), -491101511.00)

    def test0062(self):
        self.assertEquals(self.calculate(-693442370, 103654.0), -693338716.00)

    def test0063(self):
        self.assertEquals(self.calculate(1755813780, 106803.0), 1755920583.00)

    def test0064(self):
        self.assertEquals(self.calculate(-1388363639, 106470.0), -1388257169.00)

    def test0065(self):
        self.assertEquals(self.calculate(1605797718, 30230.0), 1605827948.00)

    def test0066(self):
        self.assertEquals(self.calculate(1033770319, -141717.0), 1033628602.00)

    def test0067(self):
        self.assertEquals(self.calculate(-806817426, 154366.0), -806663060.00)

    def test0068(self):
        self.assertEquals(self.calculate(-1508112117, 19108.0), -1508093009.00)

    def test0069(self):
        self.assertEquals(self.calculate(-135333777, 76351.0), -135257426.00)

    def test0070(self):
        self.assertEquals(self.calculate(-1255292883, -170932.0), -1255463815.00)

    def test0071(self):
        self.assertEquals(self.calculate(2106685457, -3628.0), 2106681829.00)

    def test0072(self):
        self.assertEquals(self.calculate(459030158, 108537.0), 459138695.00)

    def test0073(self):
        self.assertEquals(self.calculate(-778499599, -145577.0), -778645176.00)

    def test0074(self):
        self.assertEquals(self.calculate(522488343, -186176.0), 522302167.00)

    def test0075(self):
        self.assertEquals(self.calculate(-500116260, 85455.0), -500030805.00)

    def test0076(self):
        self.assertEquals(self.calculate(1143610312, -4072.0), 1143606240.00)

    def test0077(self):
        self.assertEquals(self.calculate(453034677, 84489.0), 453119166.00)

    def test0078(self):
        self.assertEquals(self.calculate(-211390472, -182672.0), -211573144.00)

    def test0079(self):
        self.assertEquals(self.calculate(2145919872, -56081.0), 2145863791.00)

    def test0080(self):
        self.assertEquals(self.calculate(-735109347, -93673.0), -735203020.00)

    def test0081(self):
        self.assertEquals(self.calculate(1078179015, 173627.0), 1078352642.00)

    def test0082(self):
        self.assertEquals(self.calculate(2061314948, 198939.0), 2061513887.00)

    def test0083(self):
        self.assertEquals(self.calculate(-1620129781, -68059.0), -1620197840.00)

    def test0084(self):
        self.assertEquals(self.calculate(-1925670683, -34596.0), -1925705279.00)

    def test0085(self):
        self.assertEquals(self.calculate(1886818106, 141365.0), 1886959471.00)

    def test0086(self):
        self.assertEquals(self.calculate(-1191185605, -2520.0), -1191188125.00)

    def test0087(self):
        self.assertEquals(self.calculate(-671623214, 51549.0), -671571665.00)

    def test0088(self):
        self.assertEquals(self.calculate(-2065924491, -188831.0), -2066113322.00)

    def test0089(self):
        self.assertEquals(self.calculate(-726181636, -37957.0), -726219593.00)

    def test0090(self):
        self.assertEquals(self.calculate(736869159, 132794.0), 737001953.00)

    def test0091(self):
        self.assertEquals(self.calculate(-963062477, -26658.0), -963089135.00)

    def test0092(self):
        self.assertEquals(self.calculate(-780663021, -22976.0), -780685997.00)

    def test0093(self):
        self.assertEquals(self.calculate(-2053621017, -172058.0), -2053793075.00)

    def test0094(self):
        self.assertEquals(self.calculate(239075055, -133698.0), 238941357.00)

    def test0095(self):
        self.assertEquals(self.calculate(1737667133, -45890.0), 1737621243.00)

    def test0096(self):
        self.assertEquals(self.calculate(-610385497, -147572.0), -610533069.00)

    def test0097(self):
        self.assertEquals(self.calculate(1883617225, 109566.0), 1883726791.00)

    def test0098(self):
        self.assertEquals(self.calculate(-1039281986, -160630.0), -1039442616.00)

    def test0099(self):
        self.assertEquals(self.calculate(779420472, 45309.0), 779465781.00)

    def test0100(self):
        self.assertEquals(self.calculate(2101321813, -191875.0), 2101129938.00)

    def test0101(self):
        self.assertEquals(self.calculate(84477440, 169849.0), 84647289.00)

    def test0102(self):
        self.assertEquals(self.calculate(2143409488, 197915.0), 2143607403.00)

    def test0103(self):
        self.assertEquals(self.calculate(458434186, 195761.0), 458629947.00)

    def test0104(self):
        self.assertEquals(self.calculate(616954301, 43786.0), 616998087.00)

    def test0105(self):
        self.assertEquals(self.calculate(1886838389, -118080.0), 1886720309.00)

    def test0106(self):
        self.assertEquals(self.calculate(-377126188, -25745.0), -377151933.00)

    def test0107(self):
        self.assertEquals(self.calculate(2120637494, -25873.0), 2120611621.00)

    def test0108(self):
        self.assertEquals(self.calculate(839481468, -174448.0), 839307020.00)

    def test0109(self):
        self.assertEquals(self.calculate(185509851, 69186.0), 185579037.00)

    def test0110(self):
        self.assertEquals(self.calculate(-1890514440, 34593.0), -1890479847.00)

    def test0111(self):
        self.assertEquals(self.calculate(1550018837, -169198.0), 1549849639.00)

    def test0112(self):
        self.assertEquals(self.calculate(374047922, 76664.0), 374124586.00)

    def test0113(self):
        self.assertEquals(self.calculate(-1442368127, -185064.0), -1442553191.00)

    def test0114(self):
        self.assertEquals(self.calculate(40102688, 78187.0), 40180875.00)

    def test0115(self):
        self.assertEquals(self.calculate(-1505242139, -167700.0), -1505409839.00)

    def test0116(self):
        self.assertEquals(self.calculate(-1216556790, -57677.0), -1216614467.00)

    def test0117(self):
        self.assertEquals(self.calculate(-1313406857, 70358.0), -1313336499.00)

    def test0118(self):
        self.assertEquals(self.calculate(-83171666, -101654.0), -83273320.00)

    def test0119(self):
        self.assertEquals(self.calculate(2009023344, 141502.0), 2009164846.00)

    def test0120(self):
        self.assertEquals(self.calculate(413441930, 144099.0), 413586029.00)

    def test0121(self):
        self.assertEquals(self.calculate(1796534682, -74458.0), 1796460224.00)

    def test0122(self):
        self.assertEquals(self.calculate(-1227976174, 97447.0), -1227878727.00)

    def test0123(self):
        self.assertEquals(self.calculate(1772683428, -190840.0), 1772492588.00)

    def test0124(self):
        self.assertEquals(self.calculate(1945261882, 20482.0), 1945282364.00)

    def test0125(self):
        self.assertEquals(self.calculate(-1701362251, 166438.0), -1701195813.00)

    def test0126(self):
        self.assertEquals(self.calculate(1046356448, 80531.0), 1046436979.00)

    def test0127(self):
        self.assertEquals(self.calculate(1861315371, 177935.0), 1861493306.00)

    def test0128(self):
        self.assertEquals(self.calculate(-1503494678, -123369.0), -1503618047.00)

    def test0129(self):
        self.assertEquals(self.calculate(-1491607206, 192210.0), -1491414996.00)

    def test0130(self):
        self.assertEquals(self.calculate(1588044436, 47611.0), 1588092047.00)

    def test0131(self):
        self.assertEquals(self.calculate(2079985837, -115658.0), 2079870179.00)

    def test0132(self):
        self.assertEquals(self.calculate(-506164280, 167645.0), -505996635.00)

    def test0133(self):
        self.assertEquals(self.calculate(-1439748284, -168773.0), -1439917057.00)

    def test0134(self):
        self.assertEquals(self.calculate(-2070820324, 68299.0), -2070752025.00)

    def test0135(self):
        self.assertEquals(self.calculate(-547288382, -93672.0), -547382054.00)

    def test0136(self):
        self.assertEquals(self.calculate(-1371891936, 61747.0), -1371830189.00)

    def test0137(self):
        self.assertEquals(self.calculate(-970975279, 145326.0), -970829953.00)

    def test0138(self):
        self.assertEquals(self.calculate(-1479830542, -54401.0), -1479884943.00)

    def test0139(self):
        self.assertEquals(self.calculate(1267400956, 163416.0), 1267564372.00)

    def test0140(self):
        self.assertEquals(self.calculate(957185999, 4674.0), 957190673.00)

    def test0141(self):
        self.assertEquals(self.calculate(-2004045082, 14432.0), -2004030650.00)

    def test0142(self):
        self.assertEquals(self.calculate(-372423281, -161144.0), -372584425.00)

    def test0143(self):
        self.assertEquals(self.calculate(-467738922, -26885.0), -467765807.00)

    def test0144(self):
        self.assertEquals(self.calculate(-190467967, 69693.0), -190398274.00)

    def test0145(self):
        self.assertEquals(self.calculate(1990113543, -155671.0), 1989957872.00)

    def test0146(self):
        self.assertEquals(self.calculate(-1359373101, 68924.0), -1359304177.00)

    def test0147(self):
        self.assertEquals(self.calculate(2029206889, 64161.0), 2029271050.00)

    def test0148(self):
        self.assertEquals(self.calculate(603729913, 122466.0), 603852379.00)

    def test0149(self):
        self.assertEquals(self.calculate(1058972353, -180991.0), 1058791362.00)

    def test0150(self):
        self.assertEquals(self.calculate(-1517361079, 75000.0), -1517286079.00)

    def test0151(self):
        self.assertEquals(self.calculate(-1055179638, -172770.0), -1055352408.00)

    def test0152(self):
        self.assertEquals(self.calculate(-1620597923, 154577.0), -1620443346.00)

    def test0153(self):
        self.assertEquals(self.calculate(1838921546, 47816.0), 1838969362.00)

    def test0154(self):
        self.assertEquals(self.calculate(-1172131442, -36706.0), -1172168148.00)

    def test0155(self):
        self.assertEquals(self.calculate(-1825374432, 92421.0), -1825282011.00)

    def test0156(self):
        self.assertEquals(self.calculate(-673254596, 33293.0), -673221303.00)

    def test0157(self):
        self.assertEquals(self.calculate(734925332, -161446.0), 734763886.00)

    def test0158(self):
        self.assertEquals(self.calculate(-915130617, 94048.0), -915036569.00)

    def test0159(self):
        self.assertEquals(self.calculate(1511367241, 124390.0), 1511491631.00)

    def test0160(self):
        self.assertEquals(self.calculate(2054350088, 50707.0), 2054400795.00)

    def test0161(self):
        self.assertEquals(self.calculate(-1744993260, 184868.0), -1744808392.00)

    def test0162(self):
        self.assertEquals(self.calculate(-1461931746, 110115.0), -1461821631.00)

    def test0163(self):
        self.assertEquals(self.calculate(464329981, -89246.0), 464240735.00)

    def test0164(self):
        self.assertEquals(self.calculate(-289604418, 140530.0), -289463888.00)

    def test0165(self):
        self.assertEquals(self.calculate(1230597359, -105689.0), 1230491670.00)

    def test0166(self):
        self.assertEquals(self.calculate(-1408059417, -188036.0), -1408247453.00)

    def test0167(self):
        self.assertEquals(self.calculate(-1376241651, -190584.0), -1376432235.00)

    def test0168(self):
        self.assertEquals(self.calculate(-1964368967, -7010.0), -1964375977.00)

    def test0169(self):
        self.assertEquals(self.calculate(190100907, -48821.0), 190052086.00)

    def test0170(self):
        self.assertEquals(self.calculate(-1222911082, -102911.0), -1223013993.00)

    def test0171(self):
        self.assertEquals(self.calculate(932636214, 67437.0), 932703651.00)

    def test0172(self):
        self.assertEquals(self.calculate(1906298212, -12181.0), 1906286031.00)

    def test0173(self):
        self.assertEquals(self.calculate(1873753158, 13536.0), 1873766694.00)

    def test0174(self):
        self.assertEquals(self.calculate(1932550910, 108423.0), 1932659333.00)

    def test0175(self):
        self.assertEquals(self.calculate(283297433, 13065.0), 283310498.00)

    def test0176(self):
        self.assertEquals(self.calculate(-721435570, 159493.0), -721276077.00)

    def test0177(self):
        self.assertEquals(self.calculate(-1897253901, 115453.0), -1897138448.00)

    def test0178(self):
        self.assertEquals(self.calculate(-879097116, 104057.0), -878993059.00)

    def test0179(self):
        self.assertEquals(self.calculate(-113441922, 101643.0), -113340279.00)

    def test0180(self):
        self.assertEquals(self.calculate(1574928667, 166932.0), 1575095599.00)

    def test0181(self):
        self.assertEquals(self.calculate(2128633486, 74501.0), 2128707987.00)

    def test0182(self):
        self.assertEquals(self.calculate(907763675, 88283.0), 907851958.00)

    def test0183(self):
        self.assertEquals(self.calculate(722362116, 1328.0), 722363444.00)

    def test0184(self):
        self.assertEquals(self.calculate(-676752368, -76158.0), -676828526.00)

    def test0185(self):
        self.assertEquals(self.calculate(150141516, -4761.0), 150136755.00)

    def test0186(self):
        self.assertEquals(self.calculate(1723241783, 190163.0), 1723431946.00)

    def test0187(self):
        self.assertEquals(self.calculate(823941645, -44823.0), 823896822.00)

    def test0188(self):
        self.assertEquals(self.calculate(-1806145901, -125658.0), -1806271559.00)

    def test0189(self):
        self.assertEquals(self.calculate(-921898687, -94554.0), -921993241.00)

    def test0190(self):
        self.assertEquals(self.calculate(-1302836676, 114268.0), -1302722408.00)

    def test0191(self):
        self.assertEquals(self.calculate(1254403151, -7928.0), 1254395223.00)

    def test0192(self):
        self.assertEquals(self.calculate(2088121887, -139208.0), 2087982679.00)

    def test0193(self):
        self.assertEquals(self.calculate(-323239384, -45501.0), -323284885.00)

    def test0194(self):
        self.assertEquals(self.calculate(1544725095, 88699.0), 1544813794.00)

    def test0195(self):
        self.assertEquals(self.calculate(-1169319117, -168785.0), -1169487902.00)

    def test0196(self):
        self.assertEquals(self.calculate(-2945956, 178006.0), -2767950.00)

    def test0197(self):
        self.assertEquals(self.calculate(1402070968, -163601.0), 1401907367.00)

    def test0198(self):
        self.assertEquals(self.calculate(1309255893, 57937.0), 1309313830.00)

    def test0199(self):
        self.assertEquals(self.calculate(598906568, 74700.0), 598981268.00)

    def test0200(self):
        self.assertEquals(self.calculate(956788194, 82547.0), 956870741.00)

    def test0201(self):
        self.assertEquals(self.calculate(1554912616, 36682.0), 1554949298.00)

    def test0202(self):
        self.assertEquals(self.calculate(-714936256, -152507.0), -715088763.00)

    def test0203(self):
        self.assertEquals(self.calculate(1374421250, 110444.0), 1374531694.00)

    def test0204(self):
        self.assertEquals(self.calculate(117654493, 123142.0), 117777635.00)

    def test0205(self):
        self.assertEquals(self.calculate(-395265753, -130860.0), -395396613.00)

    def test0206(self):
        self.assertEquals(self.calculate(-1400554054, 29670.0), -1400524384.00)

    def test0207(self):
        self.assertEquals(self.calculate(659323222, -1967.0), 659321255.00)

    def test0208(self):
        self.assertEquals(self.calculate(1391681842, 158860.0), 1391840702.00)

    def test0209(self):
        self.assertEquals(self.calculate(1245489089, -62214.0), 1245426875.00)

    def test0210(self):
        self.assertEquals(self.calculate(-1164385969, 123134.0), -1164262835.00)

    def test0211(self):
        self.assertEquals(self.calculate(107689309, -164783.0), 107524526.00)

    def test0212(self):
        self.assertEquals(self.calculate(583522540, -18051.0), 583504489.00)

    def test0213(self):
        self.assertEquals(self.calculate(515077368, 133732.0), 515211100.00)

    def test0214(self):
        self.assertEquals(self.calculate(1486033428, 96040.0), 1486129468.00)

    def test0215(self):
        self.assertEquals(self.calculate(-581417551, -48508.0), -581466059.00)

    def test0216(self):
        self.assertEquals(self.calculate(-829783864, 52542.0), -829731322.00)

    def test0217(self):
        self.assertEquals(self.calculate(2106312372, -173572.0), 2106138800.00)

    def test0218(self):
        self.assertEquals(self.calculate(1065016756, -108572.0), 1064908184.00)

    def test0219(self):
        self.assertEquals(self.calculate(-1750872072, 55307.0), -1750816765.00)

    def test0220(self):
        self.assertEquals(self.calculate(1531642041, -163789.0), 1531478252.00)

    def test0221(self):
        self.assertEquals(self.calculate(-1459282796, -162949.0), -1459445745.00)

    def test0222(self):
        self.assertEquals(self.calculate(2080221227, -155378.0), 2080065849.00)

    def test0223(self):
        self.assertEquals(self.calculate(909481109, 136671.0), 909617780.00)

    def test0224(self):
        self.assertEquals(self.calculate(-1151379703, 57169.0), -1151322534.00)

    def test0225(self):
        self.assertEquals(self.calculate(-2134251679, 100059.0), -2134151620.00)

    def test0226(self):
        self.assertEquals(self.calculate(-284324088, 195654.0), -284128434.00)

    def test0227(self):
        self.assertEquals(self.calculate(636029559, 110346.0), 636139905.00)

    def test0228(self):
        self.assertEquals(self.calculate(1740125712, -114470.0), 1740011242.00)

    def test0229(self):
        self.assertEquals(self.calculate(-757773369, 192454.0), -757580915.00)

    def test0230(self):
        self.assertEquals(self.calculate(1103701523, -19181.0), 1103682342.00)

    def test0231(self):
        self.assertEquals(self.calculate(1954062791, -25734.0), 1954037057.00)

    def test0232(self):
        self.assertEquals(self.calculate(-1932800396, 118842.0), -1932681554.00)

    def test0233(self):
        self.assertEquals(self.calculate(2012429344, 79286.0), 2012508630.00)

    def test0234(self):
        self.assertEquals(self.calculate(-1300493615, -72910.0), -1300566525.00)

    def test0235(self):
        self.assertEquals(self.calculate(-2136873170, -58146.0), -2136931316.00)

    def test0236(self):
        self.assertEquals(self.calculate(1228870522, -7162.0), 1228863360.00)

    def test0237(self):
        self.assertEquals(self.calculate(-1651990306, -886.0), -1651991192.00)

    def test0238(self):
        self.assertEquals(self.calculate(95704985, 187738.0), 95892723.00)

    def test0239(self):
        self.assertEquals(self.calculate(584196553, 23963.0), 584220516.00)

    def test0240(self):
        self.assertEquals(self.calculate(1582489877, -5417.0), 1582484460.00)

    def test0241(self):
        self.assertEquals(self.calculate(350374567, 46900.0), 350421467.00)

    def test0242(self):
        self.assertEquals(self.calculate(-1923889673, -130169.0), -1924019842.00)

    def test0243(self):
        self.assertEquals(self.calculate(-1970736965, -190545.0), -1970927510.00)

    def test0244(self):
        self.assertEquals(self.calculate(-1078201941, -180329.0), -1078382270.00)

    def test0245(self):
        self.assertEquals(self.calculate(-258396610, -96408.0), -258493018.00)

    def test0246(self):
        self.assertEquals(self.calculate(-437420496, -40668.0), -437461164.00)

    def test0247(self):
        self.assertEquals(self.calculate(760917085, 100597.0), 761017682.00)

    def test0248(self):
        self.assertEquals(self.calculate(-1723781217, 37456.0), -1723743761.00)

    def test0249(self):
        self.assertEquals(self.calculate(-603398560, 162051.0), -603236509.00)

    def test0250(self):
        self.assertEquals(self.calculate(521907651, 145721.0), 522053372.00)

    def test0251(self):
        self.assertEquals(self.calculate(-251562232, 75161.0), -251487071.00)

    def test0252(self):
        self.assertEquals(self.calculate(1316766388, 23346.0), 1316789734.00)

    def test0253(self):
        self.assertEquals(self.calculate(-1462956416, -121696.0), -1463078112.00)

    def test0254(self):
        self.assertEquals(self.calculate(-1123378810, -151681.0), -1123530491.00)

    def test0255(self):
        self.assertEquals(self.calculate(958423410, 168948.0), 958592358.00)

    def test0256(self):
        self.assertEquals(self.calculate(-147373662, 67026.0), -147306636.00)

    def test0257(self):
        self.assertEquals(self.calculate(-806454333, 80223.0), -806374110.00)

    def test0258(self):
        self.assertEquals(self.calculate(-1602592743, -119514.0), -1602712257.00)

    def test0259(self):
        self.assertEquals(self.calculate(-532916740, -60211.0), -532976951.00)

    def test0260(self):
        self.assertEquals(self.calculate(-2057512453, -103603.0), -2057616056.00)

    def test0261(self):
        self.assertEquals(self.calculate(556279537, -100555.0), 556178982.00)

    def test0262(self):
        self.assertEquals(self.calculate(-960767491, 196057.0), -960571434.00)

    def test0263(self):
        self.assertEquals(self.calculate(304869056, 74141.0), 304943197.00)

    def test0264(self):
        self.assertEquals(self.calculate(371937870, -128694.0), 371809176.00)

    def test0265(self):
        self.assertEquals(self.calculate(1418623048, 167988.0), 1418791036.00)

    def test0266(self):
        self.assertEquals(self.calculate(1534255436, 153092.0), 1534408528.00)

    def test0267(self):
        self.assertEquals(self.calculate(646243444, -139411.0), 646104033.00)

    def test0268(self):
        self.assertEquals(self.calculate(363856232, -176889.0), 363679343.00)

    def test0269(self):
        self.assertEquals(self.calculate(163006060, -40475.0), 162965585.00)

    def test0270(self):
        self.assertEquals(self.calculate(161859558, 61895.0), 161921453.00)

    def test0271(self):
        self.assertEquals(self.calculate(-1078891793, 2465.0), -1078889328.00)

    def test0272(self):
        self.assertEquals(self.calculate(490266465, 66815.0), 490333280.00)

    def test0273(self):
        self.assertEquals(self.calculate(-1617652852, -93078.0), -1617745930.00)

    def test0274(self):
        self.assertEquals(self.calculate(-887332270, 2879.0), -887329391.00)

    def test0275(self):
        self.assertEquals(self.calculate(-786898070, 23546.0), -786874524.00)

    def test0276(self):
        self.assertEquals(self.calculate(270083984, 136238.0), 270220222.00)

    def test0277(self):
        self.assertEquals(self.calculate(1584749969, 46219.0), 1584796188.00)

    def test0278(self):
        self.assertEquals(self.calculate(-453910548, 118268.0), -453792280.00)

    def test0279(self):
        self.assertEquals(self.calculate(1527092542, 127178.0), 1527219720.00)

    def test0280(self):
        self.assertEquals(self.calculate(1702130693, 97189.0), 1702227882.00)

    def test0281(self):
        self.assertEquals(self.calculate(471926680, 71943.0), 471998623.00)

    def test0282(self):
        self.assertEquals(self.calculate(-1190939092, 15826.0), -1190923266.00)

    def test0283(self):
        self.assertEquals(self.calculate(1692784715, 35679.0), 1692820394.00)

    def test0284(self):
        self.assertEquals(self.calculate(-1123496415, -72469.0), -1123568884.00)

    def test0285(self):
        self.assertEquals(self.calculate(-933354211, 96498.0), -933257713.00)

    def test0286(self):
        self.assertEquals(self.calculate(352869933, -159514.0), 352710419.00)

    def test0287(self):
        self.assertEquals(self.calculate(1961689263, -167309.0), 1961521954.00)

    def test0288(self):
        self.assertEquals(self.calculate(-1213536810, 50467.0), -1213486343.00)

    def test0289(self):
        self.assertEquals(self.calculate(489741292, 85875.0), 489827167.00)

    def test0290(self):
        self.assertEquals(self.calculate(-243644671, -91183.0), -243735854.00)

    def test0291(self):
        self.assertEquals(self.calculate(-1071453455, -143528.0), -1071596983.00)

    def test0292(self):
        self.assertEquals(self.calculate(122260988, -131886.0), 122129102.00)

    def test0293(self):
        self.assertEquals(self.calculate(-1507683158, 85824.0), -1507597334.00)

    def test0294(self):
        self.assertEquals(self.calculate(-2033017611, -136651.0), -2033154262.00)

    def test0295(self):
        self.assertEquals(self.calculate(-1766770095, 78605.0), -1766691490.00)

    def test0296(self):
        self.assertEquals(self.calculate(-1168895393, -29070.0), -1168924463.00)

    def test0297(self):
        self.assertEquals(self.calculate(1911913962, -148055.0), 1911765907.00)

    def test0298(self):
        self.assertEquals(self.calculate(-1766264548, 79209.0), -1766185339.00)

    def test0299(self):
        self.assertEquals(self.calculate(-1714803783, 118323.0), -1714685460.00)

    def test0300(self):
        self.assertEquals(self.calculate(-1226531007, 165475.0), -1226365532.00)

    def test0301(self):
        self.assertEquals(self.calculate(-1268718657, -32372.0), -1268751029.00)

    def test0302(self):
        self.assertEquals(self.calculate(1339479466, 29900.0), 1339509366.00)

    def test0303(self):
        self.assertEquals(self.calculate(-1993386295, -167629.0), -1993553924.00)

    def test0304(self):
        self.assertEquals(self.calculate(263193851, 43947.0), 263237798.00)

    def test0305(self):
        self.assertEquals(self.calculate(207224861, 62413.0), 207287274.00)

    def test0306(self):
        self.assertEquals(self.calculate(146255935, -25617.0), 146230318.00)

    def test0307(self):
        self.assertEquals(self.calculate(1567092151, -115145.0), 1566977006.00)

    def test0308(self):
        self.assertEquals(self.calculate(114936794, 35646.0), 114972440.00)

    def test0309(self):
        self.assertEquals(self.calculate(-835509711, -119963.0), -835629674.00)

    def test0310(self):
        self.assertEquals(self.calculate(223422518, 155595.0), 223578113.00)

    def test0311(self):
        self.assertEquals(self.calculate(1248486325, 78345.0), 1248564670.00)

    def test0312(self):
        self.assertEquals(self.calculate(-260026508, 111557.0), -259914951.00)

    def test0313(self):
        self.assertEquals(self.calculate(943660093, 150030.0), 943810123.00)

    def test0314(self):
        self.assertEquals(self.calculate(44867606, 152778.0), 45020384.00)

    def test0315(self):
        self.assertEquals(self.calculate(-1238809583, 144084.0), -1238665499.00)

    def test0316(self):
        self.assertEquals(self.calculate(-297632377, -22740.0), -297655117.00)

    def test0317(self):
        self.assertEquals(self.calculate(-1901532069, -56915.0), -1901588984.00)

    def test0318(self):
        self.assertEquals(self.calculate(-819597309, 165216.0), -819432093.00)

    def test0319(self):
        self.assertEquals(self.calculate(-1675299332, -15457.0), -1675314789.00)

    def test0320(self):
        self.assertEquals(self.calculate(-990417424, 36605.0), -990380819.00)

    def test0321(self):
        self.assertEquals(self.calculate(1159895256, -121494.0), 1159773762.00)

    def test0322(self):
        self.assertEquals(self.calculate(-1224879456, -140080.0), -1225019536.00)

    def test0323(self):
        self.assertEquals(self.calculate(422614406, -196598.0), 422417808.00)

    def test0324(self):
        self.assertEquals(self.calculate(-230325642, 162985.0), -230162657.00)

    def test0325(self):
        self.assertEquals(self.calculate(317389639, -153847.0), 317235792.00)

    def test0326(self):
        self.assertEquals(self.calculate(-1443264451, 68704.0), -1443195747.00)

    def test0327(self):
        self.assertEquals(self.calculate(1170768268, -99952.0), 1170668316.00)

    def test0328(self):
        self.assertEquals(self.calculate(1280726973, -53828.0), 1280673145.00)

    def test0329(self):
        self.assertEquals(self.calculate(1422970494, -44362.0), 1422926132.00)

    def test0330(self):
        self.assertEquals(self.calculate(1143198191, 146996.0), 1143345187.00)

    def test0331(self):
        self.assertEquals(self.calculate(-90151618, -174357.0), -90325975.00)

    def test0332(self):
        self.assertEquals(self.calculate(1127021684, 24573.0), 1127046257.00)

    def test0333(self):
        self.assertEquals(self.calculate(1363631655, 34247.0), 1363665902.00)

    def test0334(self):
        self.assertEquals(self.calculate(1910673557, 183511.0), 1910857068.00)

    def test0335(self):
        self.assertEquals(self.calculate(1483888452, 128835.0), 1484017287.00)

    def test0336(self):
        self.assertEquals(self.calculate(210144131, -116989.0), 210027142.00)

    def test0337(self):
        self.assertEquals(self.calculate(2073927706, 10969.0), 2073938675.00)

    def test0338(self):
        self.assertEquals(self.calculate(419337940, 81104.0), 419419044.00)

    def test0339(self):
        self.assertEquals(self.calculate(400296393, 76044.0), 400372437.00)

    def test0340(self):
        self.assertEquals(self.calculate(879825517, 192910.0), 880018427.00)

    def test0341(self):
        self.assertEquals(self.calculate(-1693266543, 163035.0), -1693103508.00)

    def test0342(self):
        self.assertEquals(self.calculate(1835869362, -133593.0), 1835735769.00)

    def test0343(self):
        self.assertEquals(self.calculate(1862210453, -23998.0), 1862186455.00)

    def test0344(self):
        self.assertEquals(self.calculate(-1499488783, -173535.0), -1499662318.00)

    def test0345(self):
        self.assertEquals(self.calculate(2002482278, -194523.0), 2002287755.00)

    def test0346(self):
        self.assertEquals(self.calculate(-1297512125, 166580.0), -1297345545.00)

    def test0347(self):
        self.assertEquals(self.calculate(-873152631, -44381.0), -873197012.00)

    def test0348(self):
        self.assertEquals(self.calculate(383954728, 94530.0), 384049258.00)

    def test0349(self):
        self.assertEquals(self.calculate(-494067679, 155642.0), -493912037.00)

    def test0350(self):
        self.assertEquals(self.calculate(-174265006, -147976.0), -174412982.00)

    def test0351(self):
        self.assertEquals(self.calculate(-674952485, 22239.0), -674930246.00)

    def test0352(self):
        self.assertEquals(self.calculate(1305977642, 151504.0), 1306129146.00)

    def test0353(self):
        self.assertEquals(self.calculate(-269479772, 194781.0), -269284991.00)

    def test0354(self):
        self.assertEquals(self.calculate(1960702510, 47956.0), 1960750466.00)

    def test0355(self):
        self.assertEquals(self.calculate(-199523403, 59724.0), -199463679.00)

    def test0356(self):
        self.assertEquals(self.calculate(-2130745821, 127643.0), -2130618178.00)

    def test0357(self):
        self.assertEquals(self.calculate(-218358400, -193935.0), -218552335.00)

    def test0358(self):
        self.assertEquals(self.calculate(-1464224438, 157151.0), -1464067287.00)

    def test0359(self):
        self.assertEquals(self.calculate(-735847811, -179595.0), -736027406.00)

    def test0360(self):
        self.assertEquals(self.calculate(-1585170652, 46129.0), -1585124523.00)

    def test0361(self):
        self.assertEquals(self.calculate(-1487363936, -36937.0), -1487400873.00)

    def test0362(self):
        self.assertEquals(self.calculate(925139880, -82339.0), 925057541.00)

    def test0363(self):
        self.assertEquals(self.calculate(-1860697624, 40359.0), -1860657265.00)

    def test0364(self):
        self.assertEquals(self.calculate(-1504620163, 170988.0), -1504449175.00)

    def test0365(self):
        self.assertEquals(self.calculate(23979921, -145161.0), 23834760.00)

    def test0366(self):
        self.assertEquals(self.calculate(1808990660, -56084.0), 1808934576.00)

    def test0367(self):
        self.assertEquals(self.calculate(-451269898, 94512.0), -451175386.00)

    def test0368(self):
        self.assertEquals(self.calculate(-472604007, 164501.0), -472439506.00)

    def test0369(self):
        self.assertEquals(self.calculate(-690579129, -16992.0), -690596121.00)

    def test0370(self):
        self.assertEquals(self.calculate(-442730565, -81795.0), -442812360.00)

    def test0371(self):
        self.assertEquals(self.calculate(-980952350, 65893.0), -980886457.00)

    def test0372(self):
        self.assertEquals(self.calculate(-1007157223, -30760.0), -1007187983.00)

    def test0373(self):
        self.assertEquals(self.calculate(-708216069, 192010.0), -708024059.00)

    def test0374(self):
        self.assertEquals(self.calculate(864534302, 155043.0), 864689345.00)

    def test0375(self):
        self.assertEquals(self.calculate(35437522, -185216.0), 35252306.00)

    def test0376(self):
        self.assertEquals(self.calculate(-771277152, 83621.0), -771193531.00)

    def test0377(self):
        self.assertEquals(self.calculate(-758559160, 118361.0), -758440799.00)

    def test0378(self):
        self.assertEquals(self.calculate(557958648, 193849.0), 558152497.00)

    def test0379(self):
        self.assertEquals(self.calculate(290007198, -189311.0), 289817887.00)

    def test0380(self):
        self.assertEquals(self.calculate(1847974551, 118596.0), 1848093147.00)

    def test0381(self):
        self.assertEquals(self.calculate(41924926, -45085.0), 41879841.00)

    def test0382(self):
        self.assertEquals(self.calculate(-1639882722, -126120.0), -1640008842.00)

    def test0383(self):
        self.assertEquals(self.calculate(1477995651, 59306.0), 1478054957.00)

    def test0384(self):
        self.assertEquals(self.calculate(345595104, 150216.0), 345745320.00)

    def test0385(self):
        self.assertEquals(self.calculate(-2077595187, -113649.0), -2077708836.00)

    def test0386(self):
        self.assertEquals(self.calculate(-1978758487, 18423.0), -1978740064.00)

    def test0387(self):
        self.assertEquals(self.calculate(-823969902, 186744.0), -823783158.00)

    def test0388(self):
        self.assertEquals(self.calculate(-1324912306, -160927.0), -1325073233.00)

    def test0389(self):
        self.assertEquals(self.calculate(-708844112, 167561.0), -708676551.00)

    def test0390(self):
        self.assertEquals(self.calculate(-288917484, 140100.0), -288777384.00)

    def test0391(self):
        self.assertEquals(self.calculate(-848226460, -127454.0), -848353914.00)

    def test0392(self):
        self.assertEquals(self.calculate(1934226550, -108191.0), 1934118359.00)

    def test0393(self):
        self.assertEquals(self.calculate(-2105567081, 75792.0), -2105491289.00)

    def test0394(self):
        self.assertEquals(self.calculate(113183143, -192607.0), 112990536.00)

    def test0395(self):
        self.assertEquals(self.calculate(-2122408158, -133946.0), -2122542104.00)

    def test0396(self):
        self.assertEquals(self.calculate(1659596462, 86300.0), 1659682762.00)

    def test0397(self):
        self.assertEquals(self.calculate(39696187, -135943.0), 39560244.00)

    def test0398(self):
        self.assertEquals(self.calculate(1430693372, 119909.0), 1430813281.00)

    def test0399(self):
        self.assertEquals(self.calculate(-1678113484, -50468.0), -1678163952.00)

    def test0400(self):
        self.assertEquals(self.calculate(-2032920123, -182516.0), -2033102639.00)

    def test0401(self):
        self.assertEquals(self.calculate(832558208, -180855.0), 832377353.00)

    def test0402(self):
        self.assertEquals(self.calculate(1341821805, -55484.0), 1341766321.00)

    def test0403(self):
        self.assertEquals(self.calculate(1826124811, -157727.0), 1825967084.00)

    def test0404(self):
        self.assertEquals(self.calculate(-247513927, -122068.0), -247635995.00)

    def test0405(self):
        self.assertEquals(self.calculate(-2043974112, 109583.0), -2043864529.00)

    def test0406(self):
        self.assertEquals(self.calculate(-709432089, 50934.0), -709381155.00)

    def test0407(self):
        self.assertEquals(self.calculate(-1980928517, -170760.0), -1981099277.00)

    def test0408(self):
        self.assertEquals(self.calculate(2101273583, -132701.0), 2101140882.00)

    def test0409(self):
        self.assertEquals(self.calculate(-1719693951, 109019.0), -1719584932.00)

    def test0410(self):
        self.assertEquals(self.calculate(-833853132, -144826.0), -833997958.00)

    def test0411(self):
        self.assertEquals(self.calculate(-1571692631, 174204.0), -1571518427.00)

    def test0412(self):
        self.assertEquals(self.calculate(-26255734, -130419.0), -26386153.00)

    def test0413(self):
        self.assertEquals(self.calculate(-1889152436, -169813.0), -1889322249.00)

    def test0414(self):
        self.assertEquals(self.calculate(-467103380, 44514.0), -467058866.00)

    def test0415(self):
        self.assertEquals(self.calculate(-1640387014, 161663.0), -1640225351.00)

    def test0416(self):
        self.assertEquals(self.calculate(-2037889485, -127546.0), -2038017031.00)

    def test0417(self):
        self.assertEquals(self.calculate(-111379885, 188180.0), -111191705.00)

    def test0418(self):
        self.assertEquals(self.calculate(-1948840222, -195728.0), -1949035950.00)

    def test0419(self):
        self.assertEquals(self.calculate(775916621, -70185.0), 775846436.00)

    def test0420(self):
        self.assertEquals(self.calculate(-1160350471, 197696.0), -1160152775.00)

    def test0421(self):
        self.assertEquals(self.calculate(-381425630, -122110.0), -381547740.00)

    def test0422(self):
        self.assertEquals(self.calculate(1808021004, -23169.0), 1807997835.00)

    def test0423(self):
        self.assertEquals(self.calculate(-1725130883, 51846.0), -1725079037.00)

    def test0424(self):
        self.assertEquals(self.calculate(248579310, -126239.0), 248453071.00)

    def test0425(self):
        self.assertEquals(self.calculate(-949618491, -133080.0), -949751571.00)

    def test0426(self):
        self.assertEquals(self.calculate(-99933819, 163951.0), -99769868.00)

    def test0427(self):
        self.assertEquals(self.calculate(-348848973, 138174.0), -348710799.00)

    def test0428(self):
        self.assertEquals(self.calculate(114243850, 112511.0), 114356361.00)

    def test0429(self):
        self.assertEquals(self.calculate(-1891054949, -150804.0), -1891205753.00)

    def test0430(self):
        self.assertEquals(self.calculate(972124563, 181075.0), 972305638.00)

    def test0431(self):
        self.assertEquals(self.calculate(1627553276, -117200.0), 1627436076.00)

    def test0432(self):
        self.assertEquals(self.calculate(-287868603, -2933.0), -287871536.00)

    def test0433(self):
        self.assertEquals(self.calculate(2100215979, 45881.0), 2100261860.00)

    def test0434(self):
        self.assertEquals(self.calculate(-819047360, 44429.0), -819002931.00)

    def test0435(self):
        self.assertEquals(self.calculate(1438341451, -85752.0), 1438255699.00)

    def test0436(self):
        self.assertEquals(self.calculate(1372923140, 38246.0), 1372961386.00)

    def test0437(self):
        self.assertEquals(self.calculate(-815477627, 134879.0), -815342748.00)

    def test0438(self):
        self.assertEquals(self.calculate(-1555828856, 48487.0), -1555780369.00)

    def test0439(self):
        self.assertEquals(self.calculate(513205675, -12910.0), 513192765.00)

    def test0440(self):
        self.assertEquals(self.calculate(-413649741, -178852.0), -413828593.00)

    def test0441(self):
        self.assertEquals(self.calculate(315822794, -66942.0), 315755852.00)

    def test0442(self):
        self.assertEquals(self.calculate(328625984, -32254.0), 328593730.00)

    def test0443(self):
        self.assertEquals(self.calculate(1200072873, 33788.0), 1200106661.00)

    def test0444(self):
        self.assertEquals(self.calculate(-1427953318, 121265.0), -1427832053.00)

    def test0445(self):
        self.assertEquals(self.calculate(515140008, -25033.0), 515114975.00)

    def test0446(self):
        self.assertEquals(self.calculate(-139096340, 157266.0), -138939074.00)

    def test0447(self):
        self.assertEquals(self.calculate(-410695938, -142453.0), -410838391.00)

    def test0448(self):
        self.assertEquals(self.calculate(-1141347330, -64587.0), -1141411917.00)

    def test0449(self):
        self.assertEquals(self.calculate(-1510829058, -115167.0), -1510944225.00)

    def test0450(self):
        self.assertEquals(self.calculate(1712279590, 5343.0), 1712284933.00)

    def test0451(self):
        self.assertEquals(self.calculate(544702005, -26884.0), 544675121.00)

    def test0452(self):
        self.assertEquals(self.calculate(999688442, 104800.0), 999793242.00)

    def test0453(self):
        self.assertEquals(self.calculate(-783594731, -81663.0), -783676394.00)

    def test0454(self):
        self.assertEquals(self.calculate(-693446531, -120715.0), -693567246.00)

    def test0455(self):
        self.assertEquals(self.calculate(135183698, -64979.0), 135118719.00)

    def test0456(self):
        self.assertEquals(self.calculate(321072261, -145758.0), 320926503.00)

    def test0457(self):
        self.assertEquals(self.calculate(1895918600, 170097.0), 1896088697.00)

    def test0458(self):
        self.assertEquals(self.calculate(312872171, 194086.0), 313066257.00)

    def test0459(self):
        self.assertEquals(self.calculate(1459122003, -177925.0), 1458944078.00)

    def test0460(self):
        self.assertEquals(self.calculate(435450707, 161041.0), 435611748.00)

    def test0461(self):
        self.assertEquals(self.calculate(-755898124, 176561.0), -755721563.00)

    def test0462(self):
        self.assertEquals(self.calculate(-231238122, 54570.0), -231183552.00)

    def test0463(self):
        self.assertEquals(self.calculate(-2143348107, -54022.0), -2143402129.00)

    def test0464(self):
        self.assertEquals(self.calculate(-540656903, -27897.0), -540684800.00)

    def test0465(self):
        self.assertEquals(self.calculate(-250669763, 154022.0), -250515741.00)

    def test0466(self):
        self.assertEquals(self.calculate(-390943265, -2798.0), -390946063.00)

    def test0467(self):
        self.assertEquals(self.calculate(1046128431, 138939.0), 1046267370.00)

    def test0468(self):
        self.assertEquals(self.calculate(1509415944, 76591.0), 1509492535.00)

    def test0469(self):
        self.assertEquals(self.calculate(255996528, -185291.0), 255811237.00)

    def test0470(self):
        self.assertEquals(self.calculate(-1422159037, -48052.0), -1422207089.00)

    def test0471(self):
        self.assertEquals(self.calculate(-376033806, -116078.0), -376149884.00)

    def test0472(self):
        self.assertEquals(self.calculate(-1327252462, 9799.0), -1327242663.00)

    def test0473(self):
        self.assertEquals(self.calculate(46658585, -182971.0), 46475614.00)

    def test0474(self):
        self.assertEquals(self.calculate(-2049000714, 18571.0), -2048982143.00)

    def test0475(self):
        self.assertEquals(self.calculate(1878710467, -92815.0), 1878617652.00)

    def test0476(self):
        self.assertEquals(self.calculate(-559814803, -97298.0), -559912101.00)

    def test0477(self):
        self.assertEquals(self.calculate(752973236, -12835.0), 752960401.00)

    def test0478(self):
        self.assertEquals(self.calculate(670873558, -50301.0), 670823257.00)

    def test0479(self):
        self.assertEquals(self.calculate(358451461, 92311.0), 358543772.00)

    def test0480(self):
        self.assertEquals(self.calculate(698374671, 15475.0), 698390146.00)

    def test0481(self):
        self.assertEquals(self.calculate(1531716210, 159632.0), 1531875842.00)

    def test0482(self):
        self.assertEquals(self.calculate(-1851600560, -98397.0), -1851698957.00)

    def test0483(self):
        self.assertEquals(self.calculate(398380165, -174531.0), 398205634.00)

    def test0484(self):
        self.assertEquals(self.calculate(1390486506, -137055.0), 1390349451.00)

    def test0485(self):
        self.assertEquals(self.calculate(748826549, 90212.0), 748916761.00)

    def test0486(self):
        self.assertEquals(self.calculate(687574509, 83641.0), 687658150.00)

    def test0487(self):
        self.assertEquals(self.calculate(-1924817234, -188059.0), -1925005293.00)

    def test0488(self):
        self.assertEquals(self.calculate(-1147476929, 38178.0), -1147438751.00)

    def test0489(self):
        self.assertEquals(self.calculate(1426758527, 12850.0), 1426771377.00)

    def test0490(self):
        self.assertEquals(self.calculate(-1887810084, -41043.0), -1887851127.00)

    def test0491(self):
        self.assertEquals(self.calculate(-1448887330, 95089.0), -1448792241.00)

    def test0492(self):
        self.assertEquals(self.calculate(804126959, -110481.0), 804016478.00)

    def test0493(self):
        self.assertEquals(self.calculate(-1361247310, -50614.0), -1361297924.00)

    def test0494(self):
        self.assertEquals(self.calculate(1209996649, 76960.0), 1210073609.00)

    def test0495(self):
        self.assertEquals(self.calculate(665289234, -71323.0), 665217911.00)

    def test0496(self):
        self.assertEquals(self.calculate(1435928895, 133470.0), 1436062365.00)

    def test0497(self):
        self.assertEquals(self.calculate(525675380, 94271.0), 525769651.00)

    def test0498(self):
        self.assertEquals(self.calculate(214417921, -16270.0), 214401651.00)

    def test0499(self):
        self.assertEquals(self.calculate(1880663795, 10728.0), 1880674523.00)

    def test0500(self):
        self.assertEquals(self.calculate(-110055390, -95736.0), -110151126.00)

    def test0501(self):
        self.assertEquals(self.calculate(1291797065, -51942.0), 1291745123.00)

    def test0502(self):
        self.assertEquals(self.calculate(434328186, -153489.0), 434174697.00)

    def test0503(self):
        self.assertEquals(self.calculate(320332125, 73382.0), 320405507.00)

    def test0504(self):
        self.assertEquals(self.calculate(-961807039, 92850.0), -961714189.00)

    def test0505(self):
        self.assertEquals(self.calculate(452229218, -96647.0), 452132571.00)

    def test0506(self):
        self.assertEquals(self.calculate(297797939, -64631.0), 297733308.00)

    def test0507(self):
        self.assertEquals(self.calculate(675281095, 101013.0), 675382108.00)

    def test0508(self):
        self.assertEquals(self.calculate(2005861609, -10650.0), 2005850959.00)

    def test0509(self):
        self.assertEquals(self.calculate(-564092516, -72985.0), -564165501.00)

    def test0510(self):
        self.assertEquals(self.calculate(1382596244, -130947.0), 1382465297.00)

    def test0511(self):
        self.assertEquals(self.calculate(1641053956, -159676.0), 1640894280.00)

    def test0512(self):
        self.assertEquals(self.calculate(-2061540196, -45067.0), -2061585263.00)

    def test0513(self):
        self.assertEquals(self.calculate(-1919371267, 100933.0), -1919270334.00)

    def test0514(self):
        self.assertEquals(self.calculate(-2124400622, 171562.0), -2124229060.00)

    def test0515(self):
        self.assertEquals(self.calculate(2081122783, 174737.0), 2081297520.00)

    def test0516(self):
        self.assertEquals(self.calculate(-1541217034, -5380.0), -1541222414.00)

    def test0517(self):
        self.assertEquals(self.calculate(-900589242, 161194.0), -900428048.00)

    def test0518(self):
        self.assertEquals(self.calculate(-1650560104, 117793.0), -1650442311.00)

    def test0519(self):
        self.assertEquals(self.calculate(-957104835, 43799.0), -957061036.00)

    def test0520(self):
        self.assertEquals(self.calculate(-789904792, 110088.0), -789794704.00)

    def test0521(self):
        self.assertEquals(self.calculate(1558913584, 135297.0), 1559048881.00)

    def test0522(self):
        self.assertEquals(self.calculate(113386576, 112348.0), 113498924.00)

    def test0523(self):
        self.assertEquals(self.calculate(101561219, -23795.0), 101537424.00)

    def test0524(self):
        self.assertEquals(self.calculate(815352572, 55019.0), 815407591.00)

    def test0525(self):
        self.assertEquals(self.calculate(107184235, 46960.0), 107231195.00)

    def test0526(self):
        self.assertEquals(self.calculate(-506971331, -198076.0), -507169407.00)

    def test0527(self):
        self.assertEquals(self.calculate(741763147, 188060.0), 741951207.00)

    def test0528(self):
        self.assertEquals(self.calculate(142745827, 145363.0), 142891190.00)

    def test0529(self):
        self.assertEquals(self.calculate(1066212012, 179475.0), 1066391487.00)

    def test0530(self):
        self.assertEquals(self.calculate(1123778043, -188624.0), 1123589419.00)

    def test0531(self):
        self.assertEquals(self.calculate(1961418592, 175438.0), 1961594030.00)

    def test0532(self):
        self.assertEquals(self.calculate(1171661, 78287.0), 1249948.00)

    def test0533(self):
        self.assertEquals(self.calculate(2112620722, -61446.0), 2112559276.00)

    def test0534(self):
        self.assertEquals(self.calculate(-1317653453, -188460.0), -1317841913.00)

    def test0535(self):
        self.assertEquals(self.calculate(715622539, 163973.0), 715786512.00)

    def test0536(self):
        self.assertEquals(self.calculate(1774812386, -191238.0), 1774621148.00)

    def test0537(self):
        self.assertEquals(self.calculate(1748346412, 162561.0), 1748508973.00)

    def test0538(self):
        self.assertEquals(self.calculate(992471382, -140480.0), 992330902.00)

    def test0539(self):
        self.assertEquals(self.calculate(506944973, 135388.0), 507080361.00)

    def test0540(self):
        self.assertEquals(self.calculate(750778247, 172827.0), 750951074.00)

    def test0541(self):
        self.assertEquals(self.calculate(-720499433, 83036.0), -720416397.00)

    def test0542(self):
        self.assertEquals(self.calculate(-989015813, -141123.0), -989156936.00)

    def test0543(self):
        self.assertEquals(self.calculate(882510958, -10746.0), 882500212.00)

    def test0544(self):
        self.assertEquals(self.calculate(2052836957, -57003.0), 2052779954.00)

    def test0545(self):
        self.assertEquals(self.calculate(1971861508, -29477.0), 1971832031.00)

    def test0546(self):
        self.assertEquals(self.calculate(1363985197, 186625.0), 1364171822.00)

    def test0547(self):
        self.assertEquals(self.calculate(-148267944, -17859.0), -148285803.00)

    def test0548(self):
        self.assertEquals(self.calculate(-122450002, 73490.0), -122376512.00)

    def test0549(self):
        self.assertEquals(self.calculate(673831430, 77714.0), 673909144.00)

    def test0550(self):
        self.assertEquals(self.calculate(-1183845115, -85558.0), -1183930673.00)

    def test0551(self):
        self.assertEquals(self.calculate(372963728, 53395.0), 373017123.00)

    def test0552(self):
        self.assertEquals(self.calculate(-1642612959, 42689.0), -1642570270.00)

    def test0553(self):
        self.assertEquals(self.calculate(1725872391, 113949.0), 1725986340.00)

    def test0554(self):
        self.assertEquals(self.calculate(-980679535, -167444.0), -980846979.00)

    def test0555(self):
        self.assertEquals(self.calculate(-929540818, 199707.0), -929341111.00)

    def test0556(self):
        self.assertEquals(self.calculate(-1798687610, 87463.0), -1798600147.00)

    def test0557(self):
        self.assertEquals(self.calculate(1835866013, -107313.0), 1835758700.00)

    def test0558(self):
        self.assertEquals(self.calculate(-1562615657, 157191.0), -1562458466.00)

    def test0559(self):
        self.assertEquals(self.calculate(866477803, -92465.0), 866385338.00)

    def test0560(self):
        self.assertEquals(self.calculate(-1380810295, -117119.0), -1380927414.00)

    def test0561(self):
        self.assertEquals(self.calculate(-608793222, 116738.0), -608676484.00)

    def test0562(self):
        self.assertEquals(self.calculate(1014393228, -28203.0), 1014365025.00)

    def test0563(self):
        self.assertEquals(self.calculate(1623127439, 66355.0), 1623193794.00)

    def test0564(self):
        self.assertEquals(self.calculate(313308632, -98157.0), 313210475.00)

    def test0565(self):
        self.assertEquals(self.calculate(-691929914, -128491.0), -692058405.00)

    def test0566(self):
        self.assertEquals(self.calculate(1416744742, -75750.0), 1416668992.00)

    def test0567(self):
        self.assertEquals(self.calculate(-922537241, 186852.0), -922350389.00)

    def test0568(self):
        self.assertEquals(self.calculate(793995807, 140261.0), 794136068.00)

    def test0569(self):
        self.assertEquals(self.calculate(-291485166, -84297.0), -291569463.00)

    def test0570(self):
        self.assertEquals(self.calculate(-553832735, 135686.0), -553697049.00)

    def test0571(self):
        self.assertEquals(self.calculate(1815204384, -102027.0), 1815102357.00)

    def test0572(self):
        self.assertEquals(self.calculate(892985037, 165534.0), 893150571.00)

    def test0573(self):
        self.assertEquals(self.calculate(2123559766, -76818.0), 2123482948.00)

    def test0574(self):
        self.assertEquals(self.calculate(-669082000, -139459.0), -669221459.00)

    def test0575(self):
        self.assertEquals(self.calculate(-1715624648, 124655.0), -1715499993.00)

    def test0576(self):
        self.assertEquals(self.calculate(763802763, -32728.0), 763770035.00)

    def test0577(self):
        self.assertEquals(self.calculate(-1959307479, -15656.0), -1959323135.00)

    def test0578(self):
        self.assertEquals(self.calculate(-1838428037, -7008.0), -1838435045.00)

    def test0579(self):
        self.assertEquals(self.calculate(891608090, -51420.0), 891556670.00)

    def test0580(self):
        self.assertEquals(self.calculate(462647589, 123016.0), 462770605.00)

    def test0581(self):
        self.assertEquals(self.calculate(923351144, 95835.0), 923446979.00)

    def test0582(self):
        self.assertEquals(self.calculate(946670527, 153144.0), 946823671.00)

    def test0583(self):
        self.assertEquals(self.calculate(-1416899528, -107089.0), -1417006617.00)

    def test0584(self):
        self.assertEquals(self.calculate(-1262339180, 115215.0), -1262223965.00)

    def test0585(self):
        self.assertEquals(self.calculate(-874462618, 34423.0), -874428195.00)

    def test0586(self):
        self.assertEquals(self.calculate(-850257668, -181854.0), -850439522.00)

    def test0587(self):
        self.assertEquals(self.calculate(1262716899, 93608.0), 1262810507.00)

    def test0588(self):
        self.assertEquals(self.calculate(1679136122, -163274.0), 1678972848.00)

    def test0589(self):
        self.assertEquals(self.calculate(157619424, -93662.0), 157525762.00)

    def test0590(self):
        self.assertEquals(self.calculate(861043429, 164273.0), 861207702.00)

    def test0591(self):
        self.assertEquals(self.calculate(-571390148, -2567.0), -571392715.00)

    def test0592(self):
        self.assertEquals(self.calculate(970198777, -141448.0), 970057329.00)

    def test0593(self):
        self.assertEquals(self.calculate(-1780484954, -70285.0), -1780555239.00)

    def test0594(self):
        self.assertEquals(self.calculate(-432302069, 159075.0), -432142994.00)

    def test0595(self):
        self.assertEquals(self.calculate(591593717, 7765.0), 591601482.00)

    def test0596(self):
        self.assertEquals(self.calculate(205242067, 57022.0), 205299089.00)

    def test0597(self):
        self.assertEquals(self.calculate(1428045302, -110368.0), 1427934934.00)

    def test0598(self):
        self.assertEquals(self.calculate(165706921, -133624.0), 165573297.00)

    def test0599(self):
        self.assertEquals(self.calculate(805469041, -148129.0), 805320912.00)

    def test0600(self):
        self.assertEquals(self.calculate(1810550068, 17827.0), 1810567895.00)

    def test0601(self):
        self.assertEquals(self.calculate(1203552213, -104847.0), 1203447366.00)

    def test0602(self):
        self.assertEquals(self.calculate(-2030952224, 59395.0), -2030892829.00)

    def test0603(self):
        self.assertEquals(self.calculate(781164010, 186946.0), 781350956.00)

    def test0604(self):
        self.assertEquals(self.calculate(-541202120, -48564.0), -541250684.00)

    def test0605(self):
        self.assertEquals(self.calculate(-103844131, 166306.0), -103677825.00)

    def test0606(self):
        self.assertEquals(self.calculate(153003112, -101798.0), 152901314.00)

    def test0607(self):
        self.assertEquals(self.calculate(327085155, -7348.0), 327077807.00)

    def test0608(self):
        self.assertEquals(self.calculate(-601304801, 109955.0), -601194846.00)

    def test0609(self):
        self.assertEquals(self.calculate(-44422539, 147123.0), -44275416.00)

    def test0610(self):
        self.assertEquals(self.calculate(-771811548, -111739.0), -771923287.00)

    def test0611(self):
        self.assertEquals(self.calculate(1154345988, 50469.0), 1154396457.00)

    def test0612(self):
        self.assertEquals(self.calculate(516975995, -78135.0), 516897860.00)

    def test0613(self):
        self.assertEquals(self.calculate(800222860, -158282.0), 800064578.00)

    def test0614(self):
        self.assertEquals(self.calculate(-774361693, 54938.0), -774306755.00)

    def test0615(self):
        self.assertEquals(self.calculate(153648904, 190063.0), 153838967.00)

    def test0616(self):
        self.assertEquals(self.calculate(250460882, -133153.0), 250327729.00)

    def test0617(self):
        self.assertEquals(self.calculate(-891009486, 37641.0), -890971845.00)

    def test0618(self):
        self.assertEquals(self.calculate(304995788, 195085.0), 305190873.00)

    def test0619(self):
        self.assertEquals(self.calculate(263077438, 143518.0), 263220956.00)

    def test0620(self):
        self.assertEquals(self.calculate(-427154212, 108218.0), -427045994.00)

    def test0621(self):
        self.assertEquals(self.calculate(-1996393395, -127943.0), -1996521338.00)

    def test0622(self):
        self.assertEquals(self.calculate(1141389890, -127920.0), 1141261970.00)

    def test0623(self):
        self.assertEquals(self.calculate(591266037, -25899.0), 591240138.00)

    def test0624(self):
        self.assertEquals(self.calculate(-1258093190, -79575.0), -1258172765.00)

    def test0625(self):
        self.assertEquals(self.calculate(-1250980012, -135475.0), -1251115487.00)

    def test0626(self):
        self.assertEquals(self.calculate(671104583, -11870.0), 671092713.00)

    def test0627(self):
        self.assertEquals(self.calculate(-72792728, -180592.0), -72973320.00)

    def test0628(self):
        self.assertEquals(self.calculate(-611126308, -45799.0), -611172107.00)

    def test0629(self):
        self.assertEquals(self.calculate(-1853365224, 147588.0), -1853217636.00)

    def test0630(self):
        self.assertEquals(self.calculate(-1288982943, 127796.0), -1288855147.00)

    def test0631(self):
        self.assertEquals(self.calculate(432796716, 193497.0), 432990213.00)

    def test0632(self):
        self.assertEquals(self.calculate(-1498391869, 2837.0), -1498389032.00)

    def test0633(self):
        self.assertEquals(self.calculate(-577447900, 96339.0), -577351561.00)

    def test0634(self):
        self.assertEquals(self.calculate(390474572, 74097.0), 390548669.00)

    def test0635(self):
        self.assertEquals(self.calculate(-227045510, -172663.0), -227218173.00)

    def test0636(self):
        self.assertEquals(self.calculate(-2057474683, -121054.0), -2057595737.00)

    def test0637(self):
        self.assertEquals(self.calculate(-885936411, -75248.0), -886011659.00)

    def test0638(self):
        self.assertEquals(self.calculate(-261177627, -70496.0), -261248123.00)

    def test0639(self):
        self.assertEquals(self.calculate(-1799987859, -183637.0), -1800171496.00)

    def test0640(self):
        self.assertEquals(self.calculate(389452279, 145894.0), 389598173.00)

    def test0641(self):
        self.assertEquals(self.calculate(-1067919754, -57742.0), -1067977496.00)

    def test0642(self):
        self.assertEquals(self.calculate(-1019811866, -13621.0), -1019825487.00)

    def test0643(self):
        self.assertEquals(self.calculate(1685685217, -68231.0), 1685616986.00)

    def test0644(self):
        self.assertEquals(self.calculate(-2005510774, -85247.0), -2005596021.00)

    def test0645(self):
        self.assertEquals(self.calculate(1085077546, 195236.0), 1085272782.00)

    def test0646(self):
        self.assertEquals(self.calculate(1515259093, 68399.0), 1515327492.00)

    def test0647(self):
        self.assertEquals(self.calculate(108012797, -151945.0), 107860852.00)

    def test0648(self):
        self.assertEquals(self.calculate(1903595867, 141367.0), 1903737234.00)

    def test0649(self):
        self.assertEquals(self.calculate(-1224635883, 129459.0), -1224506424.00)

    def test0650(self):
        self.assertEquals(self.calculate(-1942195492, 70028.0), -1942125464.00)

    def test0651(self):
        self.assertEquals(self.calculate(654764543, -130723.0), 654633820.00)

    def test0652(self):
        self.assertEquals(self.calculate(-342200280, 1421.0), -342198859.00)

    def test0653(self):
        self.assertEquals(self.calculate(-871443455, -139137.0), -871582592.00)

    def test0654(self):
        self.assertEquals(self.calculate(49618435, -167613.0), 49450822.00)

    def test0655(self):
        self.assertEquals(self.calculate(112555805, -73440.0), 112482365.00)

    def test0656(self):
        self.assertEquals(self.calculate(-1433132913, 8642.0), -1433124271.00)

    def test0657(self):
        self.assertEquals(self.calculate(-1084508193, 33957.0), -1084474236.00)

    def test0658(self):
        self.assertEquals(self.calculate(2037620098, -45437.0), 2037574661.00)

    def test0659(self):
        self.assertEquals(self.calculate(-1762816694, -33278.0), -1762849972.00)

    def test0660(self):
        self.assertEquals(self.calculate(-1187529775, 170201.0), -1187359574.00)

    def test0661(self):
        self.assertEquals(self.calculate(-1902669541, -88883.0), -1902758424.00)

    def test0662(self):
        self.assertEquals(self.calculate(-1887772584, 27472.0), -1887745112.00)

    def test0663(self):
        self.assertEquals(self.calculate(-1084113581, 48881.0), -1084064700.00)

    def test0664(self):
        self.assertEquals(self.calculate(-199433124, 46047.0), -199387077.00)

    def test0665(self):
        self.assertEquals(self.calculate(68436021, -159934.0), 68276087.00)

    def test0666(self):
        self.assertEquals(self.calculate(-1187440357, 101463.0), -1187338894.00)

    def test0667(self):
        self.assertEquals(self.calculate(378006553, 190943.0), 378197496.00)

    def test0668(self):
        self.assertEquals(self.calculate(1032125335, -52149.0), 1032073186.00)

    def test0669(self):
        self.assertEquals(self.calculate(-1501083494, 35493.0), -1501048001.00)

    def test0670(self):
        self.assertEquals(self.calculate(-1763497539, -93972.0), -1763591511.00)

    def test0671(self):
        self.assertEquals(self.calculate(978701220, -116171.0), 978585049.00)

    def test0672(self):
        self.assertEquals(self.calculate(-1255127963, -16853.0), -1255144816.00)

    def test0673(self):
        self.assertEquals(self.calculate(-25682505, 23854.0), -25658651.00)

    def test0674(self):
        self.assertEquals(self.calculate(-982737757, -198776.0), -982936533.00)

    def test0675(self):
        self.assertEquals(self.calculate(773045233, -70353.0), 772974880.00)

    def test0676(self):
        self.assertEquals(self.calculate(358042244, -159310.0), 357882934.00)

    def test0677(self):
        self.assertEquals(self.calculate(1515102279, 109553.0), 1515211832.00)

    def test0678(self):
        self.assertEquals(self.calculate(634102718, 131813.0), 634234531.00)

    def test0679(self):
        self.assertEquals(self.calculate(-1481821628, -4738.0), -1481826366.00)

    def test0680(self):
        self.assertEquals(self.calculate(687820352, 98252.0), 687918604.00)

    def test0681(self):
        self.assertEquals(self.calculate(985604417, 169607.0), 985774024.00)

    def test0682(self):
        self.assertEquals(self.calculate(284428977, 89669.0), 284518646.00)

    def test0683(self):
        self.assertEquals(self.calculate(-1799221290, -154770.0), -1799376060.00)

    def test0684(self):
        self.assertEquals(self.calculate(-775077047, -45877.0), -775122924.00)

    def test0685(self):
        self.assertEquals(self.calculate(-1657845819, 192504.0), -1657653315.00)

    def test0686(self):
        self.assertEquals(self.calculate(759576310, -162312.0), 759413998.00)

    def test0687(self):
        self.assertEquals(self.calculate(554273474, 34638.0), 554308112.00)

    def test0688(self):
        self.assertEquals(self.calculate(1911212881, -188274.0), 1911024607.00)

    def test0689(self):
        self.assertEquals(self.calculate(-510455758, 6508.0), -510449250.00)

    def test0690(self):
        self.assertEquals(self.calculate(332234186, -181656.0), 332052530.00)

    def test0691(self):
        self.assertEquals(self.calculate(1882944354, 78464.0), 1883022818.00)

    def test0692(self):
        self.assertEquals(self.calculate(-634808420, 185622.0), -634622798.00)

    def test0693(self):
        self.assertEquals(self.calculate(1719342440, -165009.0), 1719177431.00)

    def test0694(self):
        self.assertEquals(self.calculate(826035584, 117753.0), 826153337.00)

    def test0695(self):
        self.assertEquals(self.calculate(-1835425100, -71688.0), -1835496788.00)

    def test0696(self):
        self.assertEquals(self.calculate(-426016907, -10155.0), -426027062.00)

    def test0697(self):
        self.assertEquals(self.calculate(-1904176586, -89798.0), -1904266384.00)

    def test0698(self):
        self.assertEquals(self.calculate(-2035325369, 51291.0), -2035274078.00)

    def test0699(self):
        self.assertEquals(self.calculate(801903665, 126560.0), 802030225.00)

    def test0700(self):
        self.assertEquals(self.calculate(-1466771419, 183521.0), -1466587898.00)

    def test0701(self):
        self.assertEquals(self.calculate(-1742966540, 47055.0), -1742919485.00)

    def test0702(self):
        self.assertEquals(self.calculate(661031739, -183393.0), 660848346.00)

    def test0703(self):
        self.assertEquals(self.calculate(808663983, 143329.0), 808807312.00)

    def test0704(self):
        self.assertEquals(self.calculate(-980737235, 109834.0), -980627401.00)

    def test0705(self):
        self.assertEquals(self.calculate(-757219532, 133809.0), -757085723.00)

    def test0706(self):
        self.assertEquals(self.calculate(-1685079804, 142461.0), -1684937343.00)

    def test0707(self):
        self.assertEquals(self.calculate(1702786041, -110039.0), 1702676002.00)

    def test0708(self):
        self.assertEquals(self.calculate(531221181, 43717.0), 531264898.00)

    def test0709(self):
        self.assertEquals(self.calculate(-1603848342, -12615.0), -1603860957.00)

    def test0710(self):
        self.assertEquals(self.calculate(-1242311609, -174104.0), -1242485713.00)

    def test0711(self):
        self.assertEquals(self.calculate(-1204726398, -14275.0), -1204740673.00)

    def test0712(self):
        self.assertEquals(self.calculate(-19665225, -178680.0), -19843905.00)

    def test0713(self):
        self.assertEquals(self.calculate(1594727328, -149077.0), 1594578251.00)

    def test0714(self):
        self.assertEquals(self.calculate(1460871973, -80157.0), 1460791816.00)

    def test0715(self):
        self.assertEquals(self.calculate(2088768414, -176423.0), 2088591991.00)

    def test0716(self):
        self.assertEquals(self.calculate(-1718726807, -180817.0), -1718907624.00)

    def test0717(self):
        self.assertEquals(self.calculate(2062866552, -18343.0), 2062848209.00)

    def test0718(self):
        self.assertEquals(self.calculate(1637708006, -147510.0), 1637560496.00)

    def test0719(self):
        self.assertEquals(self.calculate(-1454381736, -120185.0), -1454501921.00)

    def test0720(self):
        self.assertEquals(self.calculate(-1802235619, -113147.0), -1802348766.00)

    def test0721(self):
        self.assertEquals(self.calculate(-147124207, 18618.0), -147105589.00)

    def test0722(self):
        self.assertEquals(self.calculate(-1953162388, 149117.0), -1953013271.00)

    def test0723(self):
        self.assertEquals(self.calculate(-633460262, -19240.0), -633479502.00)

    def test0724(self):
        self.assertEquals(self.calculate(1184704397, 110362.0), 1184814759.00)

    def test0725(self):
        self.assertEquals(self.calculate(1649368745, -136468.0), 1649232277.00)

    def test0726(self):
        self.assertEquals(self.calculate(2119995095, 61794.0), 2120056889.00)

    def test0727(self):
        self.assertEquals(self.calculate(276778587, -188313.0), 276590274.00)

    def test0728(self):
        self.assertEquals(self.calculate(813261782, 88241.0), 813350023.00)

    def test0729(self):
        self.assertEquals(self.calculate(-772851835, -80643.0), -772932478.00)

    def test0730(self):
        self.assertEquals(self.calculate(-1849906012, 167503.0), -1849738509.00)

    def test0731(self):
        self.assertEquals(self.calculate(8811737, -44750.0), 8766987.00)

    def test0732(self):
        self.assertEquals(self.calculate(977316011, 135832.0), 977451843.00)

    def test0733(self):
        self.assertEquals(self.calculate(1654035199, -179426.0), 1653855773.00)

    def test0734(self):
        self.assertEquals(self.calculate(1081539513, 168599.0), 1081708112.00)

    def test0735(self):
        self.assertEquals(self.calculate(1968514683, -69491.0), 1968445192.00)

    def test0736(self):
        self.assertEquals(self.calculate(-2121293469, -157559.0), -2121451028.00)

    def test0737(self):
        self.assertEquals(self.calculate(858678767, 108576.0), 858787343.00)

    def test0738(self):
        self.assertEquals(self.calculate(732270338, -194370.0), 732075968.00)

    def test0739(self):
        self.assertEquals(self.calculate(-1151287634, -5396.0), -1151293030.00)

    def test0740(self):
        self.assertEquals(self.calculate(1810133530, 32539.0), 1810166069.00)

    def test0741(self):
        self.assertEquals(self.calculate(1407113340, 162588.0), 1407275928.00)

    def test0742(self):
        self.assertEquals(self.calculate(-766739675, 72667.0), -766667008.00)

    def test0743(self):
        self.assertEquals(self.calculate(455261940, -143438.0), 455118502.00)

    def test0744(self):
        self.assertEquals(self.calculate(1450306327, -66373.0), 1450239954.00)

    def test0745(self):
        self.assertEquals(self.calculate(-86430159, -36326.0), -86466485.00)

    def test0746(self):
        self.assertEquals(self.calculate(-1681274336, 199779.0), -1681074557.00)

    def test0747(self):
        self.assertEquals(self.calculate(-1477011693, -113666.0), -1477125359.00)

    def test0748(self):
        self.assertEquals(self.calculate(-607617297, 180782.0), -607436515.00)

    def test0749(self):
        self.assertEquals(self.calculate(519042057, 6658.0), 519048715.00)

    def test0750(self):
        self.assertEquals(self.calculate(1786139739, 125634.0), 1786265373.00)

    def test0751(self):
        self.assertEquals(self.calculate(1803949690, 71518.0), 1804021208.00)

    def test0752(self):
        self.assertEquals(self.calculate(23443282, -66637.0), 23376645.00)

    def test0753(self):
        self.assertEquals(self.calculate(-683511825, 54665.0), -683457160.00)

    def test0754(self):
        self.assertEquals(self.calculate(1290057508, -158741.0), 1289898767.00)

    def test0755(self):
        self.assertEquals(self.calculate(1882546469, 186757.0), 1882733226.00)

    def test0756(self):
        self.assertEquals(self.calculate(1984090509, -76327.0), 1984014182.00)

    def test0757(self):
        self.assertEquals(self.calculate(213352180, 104048.0), 213456228.00)

    def test0758(self):
        self.assertEquals(self.calculate(-1732031173, 60934.0), -1731970239.00)

    def test0759(self):
        self.assertEquals(self.calculate(356253240, -50161.0), 356203079.00)

    def test0760(self):
        self.assertEquals(self.calculate(1034915409, 119516.0), 1035034925.00)

    def test0761(self):
        self.assertEquals(self.calculate(94462331, -122963.0), 94339368.00)

    def test0762(self):
        self.assertEquals(self.calculate(1316692165, 83160.0), 1316775325.00)

    def test0763(self):
        self.assertEquals(self.calculate(2119240291, -76560.0), 2119163731.00)

    def test0764(self):
        self.assertEquals(self.calculate(1940747362, 131855.0), 1940879217.00)

    def test0765(self):
        self.assertEquals(self.calculate(1382165724, -55887.0), 1382109837.00)

    def test0766(self):
        self.assertEquals(self.calculate(1008792965, 175737.0), 1008968702.00)

    def test0767(self):
        self.assertEquals(self.calculate(-544528383, -11622.0), -544540005.00)

    def test0768(self):
        self.assertEquals(self.calculate(-1390815414, -106340.0), -1390921754.00)

    def test0769(self):
        self.assertEquals(self.calculate(-1418065538, -106866.0), -1418172404.00)

    def test0770(self):
        self.assertEquals(self.calculate(376768676, 159810.0), 376928486.00)

    def test0771(self):
        self.assertEquals(self.calculate(1007620418, 32698.0), 1007653116.00)

    def test0772(self):
        self.assertEquals(self.calculate(676078149, 29924.0), 676108073.00)

    def test0773(self):
        self.assertEquals(self.calculate(339074203, 159311.0), 339233514.00)

    def test0774(self):
        self.assertEquals(self.calculate(180328445, 85964.0), 180414409.00)

    def test0775(self):
        self.assertEquals(self.calculate(-757551426, 25630.0), -757525796.00)

    def test0776(self):
        self.assertEquals(self.calculate(-1651382468, -120858.0), -1651503326.00)

    def test0777(self):
        self.assertEquals(self.calculate(541715306, -32445.0), 541682861.00)

    def test0778(self):
        self.assertEquals(self.calculate(-284595787, 46073.0), -284549714.00)

    def test0779(self):
        self.assertEquals(self.calculate(1063324934, -7463.0), 1063317471.00)

    def test0780(self):
        self.assertEquals(self.calculate(1497378357, -109255.0), 1497269102.00)

    def test0781(self):
        self.assertEquals(self.calculate(1135561800, 61543.0), 1135623343.00)

    def test0782(self):
        self.assertEquals(self.calculate(-1018836201, -14087.0), -1018850288.00)

    def test0783(self):
        self.assertEquals(self.calculate(212895287, 134562.0), 213029849.00)

    def test0784(self):
        self.assertEquals(self.calculate(1639880093, 199192.0), 1640079285.00)

    def test0785(self):
        self.assertEquals(self.calculate(784064164, 94549.0), 784158713.00)

    def test0786(self):
        self.assertEquals(self.calculate(-1148252182, -108765.0), -1148360947.00)

    def test0787(self):
        self.assertEquals(self.calculate(-202184119, -150488.0), -202334607.00)

    def test0788(self):
        self.assertEquals(self.calculate(1037473073, 75721.0), 1037548794.00)

    def test0789(self):
        self.assertEquals(self.calculate(1627910953, 63051.0), 1627974004.00)

    def test0790(self):
        self.assertEquals(self.calculate(-2016078835, 141632.0), -2015937203.00)

    def test0791(self):
        self.assertEquals(self.calculate(552466873, 147934.0), 552614807.00)

    def test0792(self):
        self.assertEquals(self.calculate(-1258525834, -132320.0), -1258658154.00)

    def test0793(self):
        self.assertEquals(self.calculate(-1738112499, 140023.0), -1737972476.00)

    def test0794(self):
        self.assertEquals(self.calculate(-1173947829, 128192.0), -1173819637.00)

    def test0795(self):
        self.assertEquals(self.calculate(890723276, 30634.0), 890753910.00)

    def test0796(self):
        self.assertEquals(self.calculate(-2099188476, 44939.0), -2099143537.00)

    def test0797(self):
        self.assertEquals(self.calculate(1516670511, 63922.0), 1516734433.00)

    def test0798(self):
        self.assertEquals(self.calculate(-430797670, 98303.0), -430699367.00)

    def test0799(self):
        self.assertEquals(self.calculate(756130371, 128128.0), 756258499.00)

    def test0800(self):
        self.assertEquals(self.calculate(1771323931, -164761.0), 1771159170.00)

    def test0801(self):
        self.assertEquals(self.calculate(-1717583598, -103523.0), -1717687121.00)

    def test0802(self):
        self.assertEquals(self.calculate(597255018, -21084.0), 597233934.00)

    def test0803(self):
        self.assertEquals(self.calculate(-542116486, -66666.0), -542183152.00)

    def test0804(self):
        self.assertEquals(self.calculate(557059655, -106305.0), 556953350.00)

    def test0805(self):
        self.assertEquals(self.calculate(836655523, -198834.0), 836456689.00)

    def test0806(self):
        self.assertEquals(self.calculate(-1248160225, 14614.0), -1248145611.00)

    def test0807(self):
        self.assertEquals(self.calculate(-374151851, 189087.0), -373962764.00)

    def test0808(self):
        self.assertEquals(self.calculate(773556942, 70929.0), 773627871.00)

    def test0809(self):
        self.assertEquals(self.calculate(42061133, -196160.0), 41864973.00)

    def test0810(self):
        self.assertEquals(self.calculate(-344912802, -65600.0), -344978402.00)

    def test0811(self):
        self.assertEquals(self.calculate(-1387038371, 196145.0), -1386842226.00)

    def test0812(self):
        self.assertEquals(self.calculate(-117048008, 114150.0), -116933858.00)

    def test0813(self):
        self.assertEquals(self.calculate(1030377102, -119851.0), 1030257251.00)

    def test0814(self):
        self.assertEquals(self.calculate(-524622088, -120298.0), -524742386.00)

    def test0815(self):
        self.assertEquals(self.calculate(-845143674, 108486.0), -845035188.00)

    def test0816(self):
        self.assertEquals(self.calculate(-1680538126, -142028.0), -1680680154.00)

    def test0817(self):
        self.assertEquals(self.calculate(927320914, -114634.0), 927206280.00)

    def test0818(self):
        self.assertEquals(self.calculate(-2027579607, -160585.0), -2027740192.00)

    def test0819(self):
        self.assertEquals(self.calculate(-179982082, -160406.0), -180142488.00)

    def test0820(self):
        self.assertEquals(self.calculate(-798521138, -32544.0), -798553682.00)

    def test0821(self):
        self.assertEquals(self.calculate(1967879292, -115088.0), 1967764204.00)

    def test0822(self):
        self.assertEquals(self.calculate(-1404147267, 12766.0), -1404134501.00)

    def test0823(self):
        self.assertEquals(self.calculate(388868419, 117017.0), 388985436.00)

    def test0824(self):
        self.assertEquals(self.calculate(-807582100, 33404.0), -807548696.00)

    def test0825(self):
        self.assertEquals(self.calculate(937066505, -129337.0), 936937168.00)

    def test0826(self):
        self.assertEquals(self.calculate(-1730506478, -34981.0), -1730541459.00)

    def test0827(self):
        self.assertEquals(self.calculate(358703392, 179945.0), 358883337.00)

    def test0828(self):
        self.assertEquals(self.calculate(1983136094, 105208.0), 1983241302.00)

    def test0829(self):
        self.assertEquals(self.calculate(1673334544, -193649.0), 1673140895.00)

    def test0830(self):
        self.assertEquals(self.calculate(1585826580, 187124.0), 1586013704.00)

    def test0831(self):
        self.assertEquals(self.calculate(-9056039, -187415.0), -9243454.00)

    def test0832(self):
        self.assertEquals(self.calculate(-1086039143, 28291.0), -1086010852.00)

    def test0833(self):
        self.assertEquals(self.calculate(939901547, 166649.0), 940068196.00)

    def test0834(self):
        self.assertEquals(self.calculate(342885259, 193785.0), 343079044.00)

    def test0835(self):
        self.assertEquals(self.calculate(1942296839, 88509.0), 1942385348.00)

    def test0836(self):
        self.assertEquals(self.calculate(650915511, -151619.0), 650763892.00)

    def test0837(self):
        self.assertEquals(self.calculate(-2042304402, -86001.0), -2042390403.00)

    def test0838(self):
        self.assertEquals(self.calculate(254972876, -58172.0), 254914704.00)

    def test0839(self):
        self.assertEquals(self.calculate(745860113, -197242.0), 745662871.00)

    def test0840(self):
        self.assertEquals(self.calculate(925702811, 59058.0), 925761869.00)

    def test0841(self):
        self.assertEquals(self.calculate(991943633, -167676.0), 991775957.00)

    def test0842(self):
        self.assertEquals(self.calculate(1750777628, 156400.0), 1750934028.00)

    def test0843(self):
        self.assertEquals(self.calculate(-859933881, 22309.0), -859911572.00)

    def test0844(self):
        self.assertEquals(self.calculate(1368898927, -49669.0), 1368849258.00)

    def test0845(self):
        self.assertEquals(self.calculate(1002482620, -145288.0), 1002337332.00)

    def test0846(self):
        self.assertEquals(self.calculate(-1134911551, -164436.0), -1135075987.00)

    def test0847(self):
        self.assertEquals(self.calculate(1237293629, -172971.0), 1237120658.00)

    def test0848(self):
        self.assertEquals(self.calculate(-782520712, 145105.0), -782375607.00)

    def test0849(self):
        self.assertEquals(self.calculate(337426071, 37711.0), 337463782.00)

    def test0850(self):
        self.assertEquals(self.calculate(953556677, 136005.0), 953692682.00)

    def test0851(self):
        self.assertEquals(self.calculate(-816997673, -174016.0), -817171689.00)

    def test0852(self):
        self.assertEquals(self.calculate(1474859233, 132811.0), 1474992044.00)

    def test0853(self):
        self.assertEquals(self.calculate(2046249701, 137277.0), 2046386978.00)

    def test0854(self):
        self.assertEquals(self.calculate(633505135, 38453.0), 633543588.00)

    def test0855(self):
        self.assertEquals(self.calculate(-323919497, -106966.0), -324026463.00)

    def test0856(self):
        self.assertEquals(self.calculate(-2080743772, 5548.0), -2080738224.00)

    def test0857(self):
        self.assertEquals(self.calculate(1019050259, -27101.0), 1019023158.00)

    def test0858(self):
        self.assertEquals(self.calculate(-1962108417, -132719.0), -1962241136.00)

    def test0859(self):
        self.assertEquals(self.calculate(-310667718, 158676.0), -310509042.00)

    def test0860(self):
        self.assertEquals(self.calculate(187188480, -189777.0), 186998703.00)

    def test0861(self):
        self.assertEquals(self.calculate(-1979192114, -5690.0), -1979197804.00)

    def test0862(self):
        self.assertEquals(self.calculate(1669203780, -137080.0), 1669066700.00)

    def test0863(self):
        self.assertEquals(self.calculate(305785993, 113840.0), 305899833.00)

    def test0864(self):
        self.assertEquals(self.calculate(-273134692, 133263.0), -273001429.00)

    def test0865(self):
        self.assertEquals(self.calculate(1169541770, -5893.0), 1169535877.00)

    def test0866(self):
        self.assertEquals(self.calculate(-898675646, 189369.0), -898486277.00)

    def test0867(self):
        self.assertEquals(self.calculate(-677172862, -29054.0), -677201916.00)

    def test0868(self):
        self.assertEquals(self.calculate(-1673951930, -124344.0), -1674076274.00)

    def test0869(self):
        self.assertEquals(self.calculate(-680191652, -46943.0), -680238595.00)

    def test0870(self):
        self.assertEquals(self.calculate(-431509582, -32598.0), -431542180.00)

    def test0871(self):
        self.assertEquals(self.calculate(810608426, 153546.0), 810761972.00)

    def test0872(self):
        self.assertEquals(self.calculate(316930568, 94600.0), 317025168.00)

    def test0873(self):
        self.assertEquals(self.calculate(1313853260, -174758.0), 1313678502.00)

    def test0874(self):
        self.assertEquals(self.calculate(842224324, 39709.0), 842264033.00)

    def test0875(self):
        self.assertEquals(self.calculate(-1208198738, 151457.0), -1208047281.00)

    def test0876(self):
        self.assertEquals(self.calculate(242171445, 19715.0), 242191160.00)

    def test0877(self):
        self.assertEquals(self.calculate(-1150161360, 109979.0), -1150051381.00)

    def test0878(self):
        self.assertEquals(self.calculate(1303947707, -13791.0), 1303933916.00)

    def test0879(self):
        self.assertEquals(self.calculate(-1051565373, -92168.0), -1051657541.00)

    def test0880(self):
        self.assertEquals(self.calculate(1776915023, -78783.0), 1776836240.00)

    def test0881(self):
        self.assertEquals(self.calculate(1478573283, 133437.0), 1478706720.00)

    def test0882(self):
        self.assertEquals(self.calculate(-583533957, -120143.0), -583654100.00)

    def test0883(self):
        self.assertEquals(self.calculate(-1660178374, 132708.0), -1660045666.00)

    def test0884(self):
        self.assertEquals(self.calculate(-1816828356, 135210.0), -1816693146.00)

    def test0885(self):
        self.assertEquals(self.calculate(-545670672, 181212.0), -545489460.00)

    def test0886(self):
        self.assertEquals(self.calculate(391696247, 198480.0), 391894727.00)

    def test0887(self):
        self.assertEquals(self.calculate(1497739487, -46761.0), 1497692726.00)

    def test0888(self):
        self.assertEquals(self.calculate(-260557672, 23705.0), -260533967.00)

    def test0889(self):
        self.assertEquals(self.calculate(836326311, -120862.0), 836205449.00)

    def test0890(self):
        self.assertEquals(self.calculate(-145548666, -130784.0), -145679450.00)

    def test0891(self):
        self.assertEquals(self.calculate(-640377586, 89851.0), -640287735.00)

    def test0892(self):
        self.assertEquals(self.calculate(2081443403, -125802.0), 2081317601.00)

    def test0893(self):
        self.assertEquals(self.calculate(355873527, -61215.0), 355812312.00)

    def test0894(self):
        self.assertEquals(self.calculate(405288194, -48480.0), 405239714.00)

    def test0895(self):
        self.assertEquals(self.calculate(-1317054787, 99120.0), -1316955667.00)

    def test0896(self):
        self.assertEquals(self.calculate(2062147539, 143688.0), 2062291227.00)

    def test0897(self):
        self.assertEquals(self.calculate(1964319089, 59325.0), 1964378414.00)

    def test0898(self):
        self.assertEquals(self.calculate(-941206855, -176998.0), -941383853.00)

    def test0899(self):
        self.assertEquals(self.calculate(-767484267, -177816.0), -767662083.00)

    def test0900(self):
        self.assertEquals(self.calculate(1021758975, 127875.0), 1021886850.00)

    def test0901(self):
        self.assertEquals(self.calculate(-598141109, 197123.0), -597943986.00)

    def test0902(self):
        self.assertEquals(self.calculate(-2134296427, -19455.0), -2134315882.00)

    def test0903(self):
        self.assertEquals(self.calculate(-1941292271, -93279.0), -1941385550.00)

    def test0904(self):
        self.assertEquals(self.calculate(-1031200553, -31073.0), -1031231626.00)

    def test0905(self):
        self.assertEquals(self.calculate(-172056372, 46642.0), -172009730.00)

    def test0906(self):
        self.assertEquals(self.calculate(2120447029, -155953.0), 2120291076.00)

    def test0907(self):
        self.assertEquals(self.calculate(-1314878757, 36666.0), -1314842091.00)

    def test0908(self):
        self.assertEquals(self.calculate(1104732645, 75742.0), 1104808387.00)

    def test0909(self):
        self.assertEquals(self.calculate(1001489866, -33858.0), 1001456008.00)

    def test0910(self):
        self.assertEquals(self.calculate(-229765682, -46000.0), -229811682.00)

    def test0911(self):
        self.assertEquals(self.calculate(1462528781, 19090.0), 1462547871.00)

    def test0912(self):
        self.assertEquals(self.calculate(349764028, 151241.0), 349915269.00)

    def test0913(self):
        self.assertEquals(self.calculate(-833711163, -104002.0), -833815165.00)

    def test0914(self):
        self.assertEquals(self.calculate(1085942417, 115106.0), 1086057523.00)

    def test0915(self):
        self.assertEquals(self.calculate(-595232786, -58393.0), -595291179.00)

    def test0916(self):
        self.assertEquals(self.calculate(1307218090, -124606.0), 1307093484.00)

    def test0917(self):
        self.assertEquals(self.calculate(-752590277, 22683.0), -752567594.00)

    def test0918(self):
        self.assertEquals(self.calculate(-875992424, -110350.0), -876102774.00)

    def test0919(self):
        self.assertEquals(self.calculate(1488136909, -129867.0), 1488007042.00)

    def test0920(self):
        self.assertEquals(self.calculate(2054514646, -128230.0), 2054386416.00)

    def test0921(self):
        self.assertEquals(self.calculate(-1798148009, 75418.0), -1798072591.00)

    def test0922(self):
        self.assertEquals(self.calculate(1109598354, 76833.0), 1109675187.00)

    def test0923(self):
        self.assertEquals(self.calculate(-761205812, 49356.0), -761156456.00)

    def test0924(self):
        self.assertEquals(self.calculate(644091514, -90846.0), 644000668.00)

    def test0925(self):
        self.assertEquals(self.calculate(-1926275128, -74241.0), -1926349369.00)

    def test0926(self):
        self.assertEquals(self.calculate(1836079299, -81944.0), 1835997355.00)

    def test0927(self):
        self.assertEquals(self.calculate(-783217149, 158317.0), -783058832.00)

    def test0928(self):
        self.assertEquals(self.calculate(43542320, -177480.0), 43364840.00)

    def test0929(self):
        self.assertEquals(self.calculate(910799966, 58075.0), 910858041.00)

    def test0930(self):
        self.assertEquals(self.calculate(1439618590, 138609.0), 1439757199.00)

    def test0931(self):
        self.assertEquals(self.calculate(-1775325212, -158579.0), -1775483791.00)

    def test0932(self):
        self.assertEquals(self.calculate(-1697229859, -19489.0), -1697249348.00)

    def test0933(self):
        self.assertEquals(self.calculate(-1467247784, -24569.0), -1467272353.00)

    def test0934(self):
        self.assertEquals(self.calculate(-592150190, -102092.0), -592252282.00)

    def test0935(self):
        self.assertEquals(self.calculate(2086133514, 101262.0), 2086234776.00)

    def test0936(self):
        self.assertEquals(self.calculate(664576686, -45017.0), 664531669.00)

    def test0937(self):
        self.assertEquals(self.calculate(1771263645, 152685.0), 1771416330.00)

    def test0938(self):
        self.assertEquals(self.calculate(-1402884652, 150618.0), -1402734034.00)

    def test0939(self):
        self.assertEquals(self.calculate(1542512798, -55335.0), 1542457463.00)

    def test0940(self):
        self.assertEquals(self.calculate(-1897841149, -181339.0), -1898022488.00)

    def test0941(self):
        self.assertEquals(self.calculate(-1084977374, 140188.0), -1084837186.00)

    def test0942(self):
        self.assertEquals(self.calculate(-707385948, 164855.0), -707221093.00)

    def test0943(self):
        self.assertEquals(self.calculate(762681104, 183646.0), 762864750.00)

    def test0944(self):
        self.assertEquals(self.calculate(-1790465931, 48001.0), -1790417930.00)

    def test0945(self):
        self.assertEquals(self.calculate(1206418552, -56601.0), 1206361951.00)

    def test0946(self):
        self.assertEquals(self.calculate(-1082530609, 43893.0), -1082486716.00)

    def test0947(self):
        self.assertEquals(self.calculate(-837813765, 137103.0), -837676662.00)

    def test0948(self):
        self.assertEquals(self.calculate(223573269, -164188.0), 223409081.00)

    def test0949(self):
        self.assertEquals(self.calculate(70950142, -172527.0), 70777615.00)

    def test0950(self):
        self.assertEquals(self.calculate(654729943, 183220.0), 654913163.00)

    def test0951(self):
        self.assertEquals(self.calculate(-589635300, 60773.0), -589574527.00)

    def test0952(self):
        self.assertEquals(self.calculate(-2020055001, 45850.0), -2020009151.00)

    def test0953(self):
        self.assertEquals(self.calculate(-1189542567, 91367.0), -1189451200.00)

    def test0954(self):
        self.assertEquals(self.calculate(924045008, 27114.0), 924072122.00)

    def test0955(self):
        self.assertEquals(self.calculate(1818767803, -144478.0), 1818623325.00)

    def test0956(self):
        self.assertEquals(self.calculate(-1736373247, 39230.0), -1736334017.00)

    def test0957(self):
        self.assertEquals(self.calculate(-332257854, 13881.0), -332243973.00)

    def test0958(self):
        self.assertEquals(self.calculate(1539083709, 91238.0), 1539174947.00)

    def test0959(self):
        self.assertEquals(self.calculate(325269766, -121925.0), 325147841.00)

    def test0960(self):
        self.assertEquals(self.calculate(-943479315, 19593.0), -943459722.00)

    def test0961(self):
        self.assertEquals(self.calculate(-1046306548, 63768.0), -1046242780.00)

    def test0962(self):
        self.assertEquals(self.calculate(-2089049311, 168745.0), -2088880566.00)

    def test0963(self):
        self.assertEquals(self.calculate(8579078, 44533.0), 8623611.00)

    def test0964(self):
        self.assertEquals(self.calculate(270765664, 195781.0), 270961445.00)

    def test0965(self):
        self.assertEquals(self.calculate(1113489992, -148412.0), 1113341580.00)

    def test0966(self):
        self.assertEquals(self.calculate(2059572374, -89602.0), 2059482772.00)

    def test0967(self):
        self.assertEquals(self.calculate(-1132133346, 144402.0), -1131988944.00)

    def test0968(self):
        self.assertEquals(self.calculate(-2012105339, 53617.0), -2012051722.00)

    def test0969(self):
        self.assertEquals(self.calculate(-5726169, 147054.0), -5579115.00)

    def test0970(self):
        self.assertEquals(self.calculate(-1679247943, 105365.0), -1679142578.00)

    def test0971(self):
        self.assertEquals(self.calculate(-1953052160, 118299.0), -1952933861.00)

    def test0972(self):
        self.assertEquals(self.calculate(-521863264, -1829.0), -521865093.00)

    def test0973(self):
        self.assertEquals(self.calculate(1623214730, 128045.0), 1623342775.00)

    def test0974(self):
        self.assertEquals(self.calculate(321440508, 22050.0), 321462558.00)

    def test0975(self):
        self.assertEquals(self.calculate(-1411564790, 37858.0), -1411526932.00)

    def test0976(self):
        self.assertEquals(self.calculate(649220982, 97896.0), 649318878.00)

    def test0977(self):
        self.assertEquals(self.calculate(-1878819700, -36081.0), -1878855781.00)

    def test0978(self):
        self.assertEquals(self.calculate(-120476957, -190325.0), -120667282.00)

    def test0979(self):
        self.assertEquals(self.calculate(846917142, -81101.0), 846836041.00)

    def test0980(self):
        self.assertEquals(self.calculate(52429403, 148450.0), 52577853.00)

    def test0981(self):
        self.assertEquals(self.calculate(1142748750, 53005.0), 1142801755.00)

    def test0982(self):
        self.assertEquals(self.calculate(-1842548346, -78340.0), -1842626686.00)

    def test0983(self):
        self.assertEquals(self.calculate(-1979840621, 139927.0), -1979700694.00)

    def test0984(self):
        self.assertEquals(self.calculate(-1644807578, -48616.0), -1644856194.00)

    def test0985(self):
        self.assertEquals(self.calculate(-1006211419, 60774.0), -1006150645.00)

    def test0986(self):
        self.assertEquals(self.calculate(481191806, 162859.0), 481354665.00)

    def test0987(self):
        self.assertEquals(self.calculate(-1435160317, 190912.0), -1434969405.00)

    def test0988(self):
        self.assertEquals(self.calculate(-1506443097, 17794.0), -1506425303.00)

    def test0989(self):
        self.assertEquals(self.calculate(-1351553155, 89636.0), -1351463519.00)

    def test0990(self):
        self.assertEquals(self.calculate(1198370601, -9333.0), 1198361268.00)

    def test0991(self):
        self.assertEquals(self.calculate(-409807834, 44034.0), -409763800.00)

    def test0992(self):
        self.assertEquals(self.calculate(218734445, 2748.0), 218737193.00)

    def test0993(self):
        self.assertEquals(self.calculate(2097721964, -108550.0), 2097613414.00)

    def test0994(self):
        self.assertEquals(self.calculate(-1712338804, 134733.0), -1712204071.00)

    def test0995(self):
        self.assertEquals(self.calculate(1147930918, -148240.0), 1147782678.00)

    def test0996(self):
        self.assertEquals(self.calculate(1896162366, -34878.0), 1896127488.00)

    def test0997(self):
        self.assertEquals(self.calculate(-983617916, 119508.0), -983498408.00)

    def test0998(self):
        self.assertEquals(self.calculate(974162018, 174042.0), 974336060.00)

    def test0999(self):
        self.assertEquals(self.calculate(-1421086664, 71247.0), -1421015417.00)

    def test1000(self):
        self.assertEquals(self.calculate(1070595394, -164774.0), 1070430620.00)

    def test1001(self):
        self.assertEquals(self.calculate(-1487336873, -189353.0), -1487526226.00)

    def test1002(self):
        self.assertEquals(self.calculate(823179250, 192152.0), 823371402.00)

    def test1003(self):
        self.assertEquals(self.calculate(-771900498, -191479.0), -772091977.00)

    def test1004(self):
        self.assertEquals(self.calculate(-465488856, 194381.0), -465294475.00)

    def test1005(self):
        self.assertEquals(self.calculate(-1943392239, -116099.0), -1943508338.00)

    def test1006(self):
        self.assertEquals(self.calculate(1228700329, -136326.0), 1228564003.00)

    def test1007(self):
        self.assertEquals(self.calculate(596072983, -149542.0), 595923441.00)

    def test1008(self):
        self.assertEquals(self.calculate(-1644882845, -75372.0), -1644958217.00)

    def test1009(self):
        self.assertEquals(self.calculate(-1297062834, 119384.0), -1296943450.00)

    def test1010(self):
        self.assertEquals(self.calculate(759873985, -152368.0), 759721617.00)

    def test1011(self):
        self.assertEquals(self.calculate(-535772686, -34304.0), -535806990.00)

    def test1012(self):
        self.assertEquals(self.calculate(1244179541, -2766.0), 1244176775.00)

    def test1013(self):
        self.assertEquals(self.calculate(-548060672, 149598.0), -547911074.00)

    def test1014(self):
        self.assertEquals(self.calculate(-60500635, -32377.0), -60533012.00)

    def test1015(self):
        self.assertEquals(self.calculate(-2076186244, -147847.0), -2076334091.00)

    def test1016(self):
        self.assertEquals(self.calculate(1409691039, 166242.0), 1409857281.00)

    def test1017(self):
        self.assertEquals(self.calculate(-1636105655, 194864.0), -1635910791.00)

    def test1018(self):
        self.assertEquals(self.calculate(534393691, 183270.0), 534576961.00)

    def test1019(self):
        self.assertEquals(self.calculate(-1656683538, -115106.0), -1656798644.00)

    def test1020(self):
        self.assertEquals(self.calculate(-350766220, 49233.0), -350716987.00)

    def test1021(self):
        self.assertEquals(self.calculate(569327438, 19499.0), 569346937.00)

    def test1022(self):
        self.assertEquals(self.calculate(911779352, 176739.0), 911956091.00)

    def test1023(self):
        self.assertEquals(self.calculate(-1901269821, -18798.0), -1901288619.00)




class TestVM_Add_FloatInt(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_INT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushW(rhs)
        v.VM_Add()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(136388.0, 20182), 156570.00)

    def test0001(self):
        self.assertEquals(self.calculate(-142785.0, -3049), -145834.00)

    def test0002(self):
        self.assertEquals(self.calculate(5529.0, -3539), 1990.00)

    def test0003(self):
        self.assertEquals(self.calculate(-81061.0, -8895), -89956.00)

    def test0004(self):
        self.assertEquals(self.calculate(-72667.0, 289), -72378.00)

    def test0005(self):
        self.assertEquals(self.calculate(-51460.0, -29899), -81359.00)

    def test0006(self):
        self.assertEquals(self.calculate(-64350.0, -27374), -91724.00)

    def test0007(self):
        self.assertEquals(self.calculate(-102345.0, -17010), -119355.00)

    def test0008(self):
        self.assertEquals(self.calculate(-147596.0, -24), -147620.00)

    def test0009(self):
        self.assertEquals(self.calculate(7326.0, 3475), 10801.00)

    def test0010(self):
        self.assertEquals(self.calculate(80771.0, 20597), 101368.00)

    def test0011(self):
        self.assertEquals(self.calculate(180635.0, -14900), 165735.00)

    def test0012(self):
        self.assertEquals(self.calculate(38834.0, -26240), 12594.00)

    def test0013(self):
        self.assertEquals(self.calculate(183903.0, -6080), 177823.00)

    def test0014(self):
        self.assertEquals(self.calculate(109015.0, 18419), 127434.00)

    def test0015(self):
        self.assertEquals(self.calculate(86448.0, 10623), 97071.00)

    def test0016(self):
        self.assertEquals(self.calculate(-115745.0, -24693), -140438.00)

    def test0017(self):
        self.assertEquals(self.calculate(-125718.0, -18895), -144613.00)

    def test0018(self):
        self.assertEquals(self.calculate(115616.0, -20868), 94748.00)

    def test0019(self):
        self.assertEquals(self.calculate(-98125.0, -6607), -104732.00)

    def test0020(self):
        self.assertEquals(self.calculate(-120505.0, -28950), -149455.00)

    def test0021(self):
        self.assertEquals(self.calculate(86462.0, -13068), 73394.00)

    def test0022(self):
        self.assertEquals(self.calculate(7755.0, 21763), 29518.00)

    def test0023(self):
        self.assertEquals(self.calculate(125470.0, -29223), 96247.00)

    def test0024(self):
        self.assertEquals(self.calculate(-37777.0, -16723), -54500.00)

    def test0025(self):
        self.assertEquals(self.calculate(174005.0, -20588), 153417.00)

    def test0026(self):
        self.assertEquals(self.calculate(-133199.0, -25944), -159143.00)

    def test0027(self):
        self.assertEquals(self.calculate(24708.0, 9059), 33767.00)

    def test0028(self):
        self.assertEquals(self.calculate(78954.0, 4718), 83672.00)

    def test0029(self):
        self.assertEquals(self.calculate(136501.0, -3850), 132651.00)

    def test0030(self):
        self.assertEquals(self.calculate(62748.0, 2106), 64854.00)

    def test0031(self):
        self.assertEquals(self.calculate(-105010.0, 19629), -85381.00)

    def test0032(self):
        self.assertEquals(self.calculate(-134935.0, -9633), -144568.00)

    def test0033(self):
        self.assertEquals(self.calculate(25360.0, 12965), 38325.00)

    def test0034(self):
        self.assertEquals(self.calculate(-127336.0, 18535), -108801.00)

    def test0035(self):
        self.assertEquals(self.calculate(-116548.0, -5606), -122154.00)

    def test0036(self):
        self.assertEquals(self.calculate(-115719.0, 18128), -97591.00)

    def test0037(self):
        self.assertEquals(self.calculate(-122464.0, -2860), -125324.00)

    def test0038(self):
        self.assertEquals(self.calculate(-229.0, 25134), 24905.00)

    def test0039(self):
        self.assertEquals(self.calculate(-25661.0, 21504), -4157.00)

    def test0040(self):
        self.assertEquals(self.calculate(125091.0, -9224), 115867.00)

    def test0041(self):
        self.assertEquals(self.calculate(194929.0, 23651), 218580.00)

    def test0042(self):
        self.assertEquals(self.calculate(13399.0, -19460), -6061.00)

    def test0043(self):
        self.assertEquals(self.calculate(-17029.0, -3442), -20471.00)

    def test0044(self):
        self.assertEquals(self.calculate(-67993.0, 8444), -59549.00)

    def test0045(self):
        self.assertEquals(self.calculate(-74967.0, 26627), -48340.00)

    def test0046(self):
        self.assertEquals(self.calculate(-50523.0, 12419), -38104.00)

    def test0047(self):
        self.assertEquals(self.calculate(48874.0, 16324), 65198.00)

    def test0048(self):
        self.assertEquals(self.calculate(30589.0, 30963), 61552.00)

    def test0049(self):
        self.assertEquals(self.calculate(-145264.0, 21862), -123402.00)

    def test0050(self):
        self.assertEquals(self.calculate(-35552.0, 13149), -22403.00)

    def test0051(self):
        self.assertEquals(self.calculate(72934.0, -22905), 50029.00)

    def test0052(self):
        self.assertEquals(self.calculate(182510.0, -7666), 174844.00)

    def test0053(self):
        self.assertEquals(self.calculate(-104080.0, 17171), -86909.00)

    def test0054(self):
        self.assertEquals(self.calculate(170112.0, 31970), 202082.00)

    def test0055(self):
        self.assertEquals(self.calculate(-44588.0, -17927), -62515.00)

    def test0056(self):
        self.assertEquals(self.calculate(106016.0, 1255), 107271.00)

    def test0057(self):
        self.assertEquals(self.calculate(87156.0, 14052), 101208.00)

    def test0058(self):
        self.assertEquals(self.calculate(79000.0, -12097), 66903.00)

    def test0059(self):
        self.assertEquals(self.calculate(-141528.0, -7296), -148824.00)

    def test0060(self):
        self.assertEquals(self.calculate(66935.0, -23225), 43710.00)

    def test0061(self):
        self.assertEquals(self.calculate(-127677.0, 20512), -107165.00)

    def test0062(self):
        self.assertEquals(self.calculate(-102067.0, 14897), -87170.00)

    def test0063(self):
        self.assertEquals(self.calculate(198693.0, 18837), 217530.00)

    def test0064(self):
        self.assertEquals(self.calculate(-92213.0, 28981), -63232.00)

    def test0065(self):
        self.assertEquals(self.calculate(-83541.0, 26469), -57072.00)

    def test0066(self):
        self.assertEquals(self.calculate(197499.0, 23470), 220969.00)

    def test0067(self):
        self.assertEquals(self.calculate(80937.0, -1834), 79103.00)

    def test0068(self):
        self.assertEquals(self.calculate(97634.0, -9461), 88173.00)

    def test0069(self):
        self.assertEquals(self.calculate(-89727.0, 3253), -86474.00)

    def test0070(self):
        self.assertEquals(self.calculate(-70876.0, -3820), -74696.00)

    def test0071(self):
        self.assertEquals(self.calculate(-125998.0, -4469), -130467.00)

    def test0072(self):
        self.assertEquals(self.calculate(47681.0, 10751), 58432.00)

    def test0073(self):
        self.assertEquals(self.calculate(29382.0, 5043), 34425.00)

    def test0074(self):
        self.assertEquals(self.calculate(-31576.0, 16408), -15168.00)

    def test0075(self):
        self.assertEquals(self.calculate(-124334.0, 17226), -107108.00)

    def test0076(self):
        self.assertEquals(self.calculate(-26364.0, -14231), -40595.00)

    def test0077(self):
        self.assertEquals(self.calculate(-135245.0, 6951), -128294.00)

    def test0078(self):
        self.assertEquals(self.calculate(57947.0, -27983), 29964.00)

    def test0079(self):
        self.assertEquals(self.calculate(55724.0, 21750), 77474.00)

    def test0080(self):
        self.assertEquals(self.calculate(-98402.0, -26520), -124922.00)

    def test0081(self):
        self.assertEquals(self.calculate(82148.0, -23259), 58889.00)

    def test0082(self):
        self.assertEquals(self.calculate(124156.0, 15315), 139471.00)

    def test0083(self):
        self.assertEquals(self.calculate(-36683.0, 3142), -33541.00)

    def test0084(self):
        self.assertEquals(self.calculate(-10096.0, 18278), 8182.00)

    def test0085(self):
        self.assertEquals(self.calculate(-147686.0, -31888), -179574.00)

    def test0086(self):
        self.assertEquals(self.calculate(-113807.0, -14093), -127900.00)

    def test0087(self):
        self.assertEquals(self.calculate(-75850.0, 10406), -65444.00)

    def test0088(self):
        self.assertEquals(self.calculate(-126676.0, -8006), -134682.00)

    def test0089(self):
        self.assertEquals(self.calculate(-154081.0, 23774), -130307.00)

    def test0090(self):
        self.assertEquals(self.calculate(-178678.0, -7369), -186047.00)

    def test0091(self):
        self.assertEquals(self.calculate(76661.0, -24535), 52126.00)

    def test0092(self):
        self.assertEquals(self.calculate(-8920.0, -6801), -15721.00)

    def test0093(self):
        self.assertEquals(self.calculate(-183352.0, 8410), -174942.00)

    def test0094(self):
        self.assertEquals(self.calculate(-7983.0, 6876), -1107.00)

    def test0095(self):
        self.assertEquals(self.calculate(-55544.0, 24485), -31059.00)

    def test0096(self):
        self.assertEquals(self.calculate(51460.0, 8642), 60102.00)

    def test0097(self):
        self.assertEquals(self.calculate(-29959.0, 85), -29874.00)

    def test0098(self):
        self.assertEquals(self.calculate(147461.0, -5680), 141781.00)

    def test0099(self):
        self.assertEquals(self.calculate(-158603.0, -3450), -162053.00)

    def test0100(self):
        self.assertEquals(self.calculate(-3571.0, -16028), -19599.00)

    def test0101(self):
        self.assertEquals(self.calculate(6261.0, -26210), -19949.00)

    def test0102(self):
        self.assertEquals(self.calculate(122656.0, -19986), 102670.00)

    def test0103(self):
        self.assertEquals(self.calculate(-173813.0, 27532), -146281.00)

    def test0104(self):
        self.assertEquals(self.calculate(167382.0, 22609), 189991.00)

    def test0105(self):
        self.assertEquals(self.calculate(-65694.0, 22247), -43447.00)

    def test0106(self):
        self.assertEquals(self.calculate(-149629.0, 6252), -143377.00)

    def test0107(self):
        self.assertEquals(self.calculate(-23149.0, 8391), -14758.00)

    def test0108(self):
        self.assertEquals(self.calculate(539.0, 30835), 31374.00)

    def test0109(self):
        self.assertEquals(self.calculate(-27632.0, 24236), -3396.00)

    def test0110(self):
        self.assertEquals(self.calculate(-150902.0, -17356), -168258.00)

    def test0111(self):
        self.assertEquals(self.calculate(-146605.0, 18396), -128209.00)

    def test0112(self):
        self.assertEquals(self.calculate(14891.0, -30020), -15129.00)

    def test0113(self):
        self.assertEquals(self.calculate(-145023.0, -2775), -147798.00)

    def test0114(self):
        self.assertEquals(self.calculate(9759.0, -10508), -749.00)

    def test0115(self):
        self.assertEquals(self.calculate(175852.0, -29082), 146770.00)

    def test0116(self):
        self.assertEquals(self.calculate(66364.0, 16728), 83092.00)

    def test0117(self):
        self.assertEquals(self.calculate(137735.0, -2885), 134850.00)

    def test0118(self):
        self.assertEquals(self.calculate(76914.0, -18981), 57933.00)

    def test0119(self):
        self.assertEquals(self.calculate(28399.0, 13609), 42008.00)

    def test0120(self):
        self.assertEquals(self.calculate(-122733.0, 1502), -121231.00)

    def test0121(self):
        self.assertEquals(self.calculate(191794.0, 25542), 217336.00)

    def test0122(self):
        self.assertEquals(self.calculate(32125.0, -14422), 17703.00)

    def test0123(self):
        self.assertEquals(self.calculate(-174876.0, -11425), -186301.00)

    def test0124(self):
        self.assertEquals(self.calculate(-87300.0, -27011), -114311.00)

    def test0125(self):
        self.assertEquals(self.calculate(30275.0, 2141), 32416.00)

    def test0126(self):
        self.assertEquals(self.calculate(-86851.0, -20478), -107329.00)

    def test0127(self):
        self.assertEquals(self.calculate(177917.0, -25109), 152808.00)

    def test0128(self):
        self.assertEquals(self.calculate(195263.0, 24614), 219877.00)

    def test0129(self):
        self.assertEquals(self.calculate(166442.0, 23531), 189973.00)

    def test0130(self):
        self.assertEquals(self.calculate(77954.0, 20267), 98221.00)

    def test0131(self):
        self.assertEquals(self.calculate(-2477.0, 11864), 9387.00)

    def test0132(self):
        self.assertEquals(self.calculate(179616.0, 26677), 206293.00)

    def test0133(self):
        self.assertEquals(self.calculate(123182.0, -3015), 120167.00)

    def test0134(self):
        self.assertEquals(self.calculate(189090.0, 14594), 203684.00)

    def test0135(self):
        self.assertEquals(self.calculate(-131078.0, 5431), -125647.00)

    def test0136(self):
        self.assertEquals(self.calculate(-173353.0, 24873), -148480.00)

    def test0137(self):
        self.assertEquals(self.calculate(-122967.0, -24474), -147441.00)

    def test0138(self):
        self.assertEquals(self.calculate(55426.0, -27409), 28017.00)

    def test0139(self):
        self.assertEquals(self.calculate(-18871.0, 25340), 6469.00)

    def test0140(self):
        self.assertEquals(self.calculate(116867.0, 17044), 133911.00)

    def test0141(self):
        self.assertEquals(self.calculate(-174791.0, -4978), -179769.00)

    def test0142(self):
        self.assertEquals(self.calculate(181929.0, 25890), 207819.00)

    def test0143(self):
        self.assertEquals(self.calculate(-101829.0, 30718), -71111.00)

    def test0144(self):
        self.assertEquals(self.calculate(147632.0, -24782), 122850.00)

    def test0145(self):
        self.assertEquals(self.calculate(-83488.0, 29084), -54404.00)

    def test0146(self):
        self.assertEquals(self.calculate(10373.0, -15257), -4884.00)

    def test0147(self):
        self.assertEquals(self.calculate(-106976.0, 29814), -77162.00)

    def test0148(self):
        self.assertEquals(self.calculate(149830.0, 22708), 172538.00)

    def test0149(self):
        self.assertEquals(self.calculate(-78877.0, 25611), -53266.00)

    def test0150(self):
        self.assertEquals(self.calculate(-42132.0, -16978), -59110.00)

    def test0151(self):
        self.assertEquals(self.calculate(757.0, -26798), -26041.00)

    def test0152(self):
        self.assertEquals(self.calculate(-191370.0, -31517), -222887.00)

    def test0153(self):
        self.assertEquals(self.calculate(-89887.0, -7513), -97400.00)

    def test0154(self):
        self.assertEquals(self.calculate(-156034.0, 18100), -137934.00)

    def test0155(self):
        self.assertEquals(self.calculate(-76205.0, -7672), -83877.00)

    def test0156(self):
        self.assertEquals(self.calculate(41561.0, -6502), 35059.00)

    def test0157(self):
        self.assertEquals(self.calculate(142217.0, -2683), 139534.00)

    def test0158(self):
        self.assertEquals(self.calculate(-183269.0, -3330), -186599.00)

    def test0159(self):
        self.assertEquals(self.calculate(87188.0, -24453), 62735.00)

    def test0160(self):
        self.assertEquals(self.calculate(16626.0, 14566), 31192.00)

    def test0161(self):
        self.assertEquals(self.calculate(19937.0, 26510), 46447.00)

    def test0162(self):
        self.assertEquals(self.calculate(-87161.0, 5461), -81700.00)

    def test0163(self):
        self.assertEquals(self.calculate(-27068.0, -17582), -44650.00)

    def test0164(self):
        self.assertEquals(self.calculate(-3234.0, -29575), -32809.00)

    def test0165(self):
        self.assertEquals(self.calculate(20102.0, 11343), 31445.00)

    def test0166(self):
        self.assertEquals(self.calculate(112538.0, 19983), 132521.00)

    def test0167(self):
        self.assertEquals(self.calculate(-114863.0, -7873), -122736.00)

    def test0168(self):
        self.assertEquals(self.calculate(-183123.0, -15430), -198553.00)

    def test0169(self):
        self.assertEquals(self.calculate(32244.0, -30225), 2019.00)

    def test0170(self):
        self.assertEquals(self.calculate(51350.0, 29102), 80452.00)

    def test0171(self):
        self.assertEquals(self.calculate(-109665.0, -21192), -130857.00)

    def test0172(self):
        self.assertEquals(self.calculate(-28388.0, -19645), -48033.00)

    def test0173(self):
        self.assertEquals(self.calculate(111887.0, -10156), 101731.00)

    def test0174(self):
        self.assertEquals(self.calculate(-57968.0, -30424), -88392.00)

    def test0175(self):
        self.assertEquals(self.calculate(1550.0, -9679), -8129.00)

    def test0176(self):
        self.assertEquals(self.calculate(99134.0, -19285), 79849.00)

    def test0177(self):
        self.assertEquals(self.calculate(83364.0, 32120), 115484.00)

    def test0178(self):
        self.assertEquals(self.calculate(-101620.0, 853), -100767.00)

    def test0179(self):
        self.assertEquals(self.calculate(96704.0, -12801), 83903.00)

    def test0180(self):
        self.assertEquals(self.calculate(-139026.0, 2268), -136758.00)

    def test0181(self):
        self.assertEquals(self.calculate(-141185.0, -4871), -146056.00)

    def test0182(self):
        self.assertEquals(self.calculate(144324.0, 13902), 158226.00)

    def test0183(self):
        self.assertEquals(self.calculate(149831.0, 20430), 170261.00)

    def test0184(self):
        self.assertEquals(self.calculate(73668.0, 12476), 86144.00)

    def test0185(self):
        self.assertEquals(self.calculate(102194.0, 18205), 120399.00)

    def test0186(self):
        self.assertEquals(self.calculate(-91212.0, 19030), -72182.00)

    def test0187(self):
        self.assertEquals(self.calculate(-35682.0, -8899), -44581.00)

    def test0188(self):
        self.assertEquals(self.calculate(142855.0, -5774), 137081.00)

    def test0189(self):
        self.assertEquals(self.calculate(-37106.0, -31340), -68446.00)

    def test0190(self):
        self.assertEquals(self.calculate(-22256.0, 1893), -20363.00)

    def test0191(self):
        self.assertEquals(self.calculate(-64650.0, 15151), -49499.00)

    def test0192(self):
        self.assertEquals(self.calculate(-104325.0, -24959), -129284.00)

    def test0193(self):
        self.assertEquals(self.calculate(-124272.0, 4152), -120120.00)

    def test0194(self):
        self.assertEquals(self.calculate(48144.0, -12323), 35821.00)

    def test0195(self):
        self.assertEquals(self.calculate(124935.0, -28032), 96903.00)

    def test0196(self):
        self.assertEquals(self.calculate(137745.0, 28183), 165928.00)

    def test0197(self):
        self.assertEquals(self.calculate(140150.0, -32087), 108063.00)

    def test0198(self):
        self.assertEquals(self.calculate(177323.0, 1596), 178919.00)

    def test0199(self):
        self.assertEquals(self.calculate(165479.0, 13407), 178886.00)

    def test0200(self):
        self.assertEquals(self.calculate(38152.0, 16554), 54706.00)

    def test0201(self):
        self.assertEquals(self.calculate(-68312.0, 7073), -61239.00)

    def test0202(self):
        self.assertEquals(self.calculate(-87787.0, 12954), -74833.00)

    def test0203(self):
        self.assertEquals(self.calculate(103990.0, 20323), 124313.00)

    def test0204(self):
        self.assertEquals(self.calculate(178912.0, 21039), 199951.00)

    def test0205(self):
        self.assertEquals(self.calculate(96085.0, -27302), 68783.00)

    def test0206(self):
        self.assertEquals(self.calculate(-188680.0, -15690), -204370.00)

    def test0207(self):
        self.assertEquals(self.calculate(-178939.0, -8361), -187300.00)

    def test0208(self):
        self.assertEquals(self.calculate(158541.0, -14158), 144383.00)

    def test0209(self):
        self.assertEquals(self.calculate(-165769.0, -28607), -194376.00)

    def test0210(self):
        self.assertEquals(self.calculate(-83327.0, 29352), -53975.00)

    def test0211(self):
        self.assertEquals(self.calculate(191407.0, 814), 192221.00)

    def test0212(self):
        self.assertEquals(self.calculate(-187671.0, 13544), -174127.00)

    def test0213(self):
        self.assertEquals(self.calculate(-52561.0, 19136), -33425.00)

    def test0214(self):
        self.assertEquals(self.calculate(-56447.0, -25776), -82223.00)

    def test0215(self):
        self.assertEquals(self.calculate(87020.0, -8438), 78582.00)

    def test0216(self):
        self.assertEquals(self.calculate(122211.0, -25372), 96839.00)

    def test0217(self):
        self.assertEquals(self.calculate(-26073.0, -32081), -58154.00)

    def test0218(self):
        self.assertEquals(self.calculate(136968.0, -24800), 112168.00)

    def test0219(self):
        self.assertEquals(self.calculate(-115742.0, 21182), -94560.00)

    def test0220(self):
        self.assertEquals(self.calculate(30517.0, -19299), 11218.00)

    def test0221(self):
        self.assertEquals(self.calculate(48860.0, 21554), 70414.00)

    def test0222(self):
        self.assertEquals(self.calculate(-116263.0, 19085), -97178.00)

    def test0223(self):
        self.assertEquals(self.calculate(45367.0, 1193), 46560.00)

    def test0224(self):
        self.assertEquals(self.calculate(-58338.0, 17264), -41074.00)

    def test0225(self):
        self.assertEquals(self.calculate(-162602.0, 14124), -148478.00)

    def test0226(self):
        self.assertEquals(self.calculate(-75171.0, 31613), -43558.00)

    def test0227(self):
        self.assertEquals(self.calculate(-115940.0, 16499), -99441.00)

    def test0228(self):
        self.assertEquals(self.calculate(150104.0, 3496), 153600.00)

    def test0229(self):
        self.assertEquals(self.calculate(-137466.0, 18652), -118814.00)

    def test0230(self):
        self.assertEquals(self.calculate(-70051.0, -22414), -92465.00)

    def test0231(self):
        self.assertEquals(self.calculate(162155.0, -23983), 138172.00)

    def test0232(self):
        self.assertEquals(self.calculate(-21352.0, -26275), -47627.00)

    def test0233(self):
        self.assertEquals(self.calculate(19903.0, -12393), 7510.00)

    def test0234(self):
        self.assertEquals(self.calculate(-3279.0, 15738), 12459.00)

    def test0235(self):
        self.assertEquals(self.calculate(-76001.0, -32212), -108213.00)

    def test0236(self):
        self.assertEquals(self.calculate(-135199.0, -31725), -166924.00)

    def test0237(self):
        self.assertEquals(self.calculate(-94460.0, 28466), -65994.00)

    def test0238(self):
        self.assertEquals(self.calculate(-130175.0, 28285), -101890.00)

    def test0239(self):
        self.assertEquals(self.calculate(63894.0, 25169), 89063.00)

    def test0240(self):
        self.assertEquals(self.calculate(80946.0, 4906), 85852.00)

    def test0241(self):
        self.assertEquals(self.calculate(28768.0, -10473), 18295.00)

    def test0242(self):
        self.assertEquals(self.calculate(134232.0, -28743), 105489.00)

    def test0243(self):
        self.assertEquals(self.calculate(-113845.0, 14353), -99492.00)

    def test0244(self):
        self.assertEquals(self.calculate(317.0, 29827), 30144.00)

    def test0245(self):
        self.assertEquals(self.calculate(-46255.0, 6034), -40221.00)

    def test0246(self):
        self.assertEquals(self.calculate(-66287.0, 23481), -42806.00)

    def test0247(self):
        self.assertEquals(self.calculate(2180.0, 32455), 34635.00)

    def test0248(self):
        self.assertEquals(self.calculate(-102478.0, 26772), -75706.00)

    def test0249(self):
        self.assertEquals(self.calculate(148549.0, 30213), 178762.00)

    def test0250(self):
        self.assertEquals(self.calculate(172357.0, 20093), 192450.00)

    def test0251(self):
        self.assertEquals(self.calculate(-93159.0, -3278), -96437.00)

    def test0252(self):
        self.assertEquals(self.calculate(-90068.0, -29702), -119770.00)

    def test0253(self):
        self.assertEquals(self.calculate(-52959.0, 8839), -44120.00)

    def test0254(self):
        self.assertEquals(self.calculate(-84477.0, -25873), -110350.00)

    def test0255(self):
        self.assertEquals(self.calculate(-124664.0, 6554), -118110.00)

    def test0256(self):
        self.assertEquals(self.calculate(79058.0, -23844), 55214.00)

    def test0257(self):
        self.assertEquals(self.calculate(-188134.0, 9698), -178436.00)

    def test0258(self):
        self.assertEquals(self.calculate(96241.0, 1737), 97978.00)

    def test0259(self):
        self.assertEquals(self.calculate(145917.0, 13658), 159575.00)

    def test0260(self):
        self.assertEquals(self.calculate(7213.0, 22375), 29588.00)

    def test0261(self):
        self.assertEquals(self.calculate(-139732.0, -20328), -160060.00)

    def test0262(self):
        self.assertEquals(self.calculate(-128530.0, -23221), -151751.00)

    def test0263(self):
        self.assertEquals(self.calculate(175818.0, -5976), 169842.00)

    def test0264(self):
        self.assertEquals(self.calculate(33209.0, 28127), 61336.00)

    def test0265(self):
        self.assertEquals(self.calculate(-6101.0, 26327), 20226.00)

    def test0266(self):
        self.assertEquals(self.calculate(144090.0, 14736), 158826.00)

    def test0267(self):
        self.assertEquals(self.calculate(127167.0, -19309), 107858.00)

    def test0268(self):
        self.assertEquals(self.calculate(27311.0, -25385), 1926.00)

    def test0269(self):
        self.assertEquals(self.calculate(46724.0, -9612), 37112.00)

    def test0270(self):
        self.assertEquals(self.calculate(-58693.0, 8626), -50067.00)

    def test0271(self):
        self.assertEquals(self.calculate(-132270.0, -9122), -141392.00)

    def test0272(self):
        self.assertEquals(self.calculate(-56114.0, 32463), -23651.00)

    def test0273(self):
        self.assertEquals(self.calculate(-132477.0, -16982), -149459.00)

    def test0274(self):
        self.assertEquals(self.calculate(-178769.0, 11805), -166964.00)

    def test0275(self):
        self.assertEquals(self.calculate(-92051.0, -17368), -109419.00)

    def test0276(self):
        self.assertEquals(self.calculate(28291.0, 19855), 48146.00)

    def test0277(self):
        self.assertEquals(self.calculate(29044.0, -17215), 11829.00)

    def test0278(self):
        self.assertEquals(self.calculate(165316.0, -13568), 151748.00)

    def test0279(self):
        self.assertEquals(self.calculate(129941.0, -23111), 106830.00)

    def test0280(self):
        self.assertEquals(self.calculate(158970.0, -18712), 140258.00)

    def test0281(self):
        self.assertEquals(self.calculate(-95809.0, -3562), -99371.00)

    def test0282(self):
        self.assertEquals(self.calculate(189721.0, 18780), 208501.00)

    def test0283(self):
        self.assertEquals(self.calculate(183217.0, 14415), 197632.00)

    def test0284(self):
        self.assertEquals(self.calculate(-116824.0, -32316), -149140.00)

    def test0285(self):
        self.assertEquals(self.calculate(-149971.0, 627), -149344.00)

    def test0286(self):
        self.assertEquals(self.calculate(183736.0, -22964), 160772.00)

    def test0287(self):
        self.assertEquals(self.calculate(-101333.0, -3640), -104973.00)

    def test0288(self):
        self.assertEquals(self.calculate(-117806.0, 1357), -116449.00)

    def test0289(self):
        self.assertEquals(self.calculate(-170293.0, 31074), -139219.00)

    def test0290(self):
        self.assertEquals(self.calculate(36289.0, 14131), 50420.00)

    def test0291(self):
        self.assertEquals(self.calculate(27994.0, -1148), 26846.00)

    def test0292(self):
        self.assertEquals(self.calculate(-175287.0, 12375), -162912.00)

    def test0293(self):
        self.assertEquals(self.calculate(-114355.0, -323), -114678.00)

    def test0294(self):
        self.assertEquals(self.calculate(38570.0, -5239), 33331.00)

    def test0295(self):
        self.assertEquals(self.calculate(-181187.0, -19414), -200601.00)

    def test0296(self):
        self.assertEquals(self.calculate(-30909.0, -26847), -57756.00)

    def test0297(self):
        self.assertEquals(self.calculate(-92023.0, 20481), -71542.00)

    def test0298(self):
        self.assertEquals(self.calculate(-180454.0, -29211), -209665.00)

    def test0299(self):
        self.assertEquals(self.calculate(102623.0, -29910), 72713.00)

    def test0300(self):
        self.assertEquals(self.calculate(112283.0, 21148), 133431.00)

    def test0301(self):
        self.assertEquals(self.calculate(-22266.0, 24047), 1781.00)

    def test0302(self):
        self.assertEquals(self.calculate(189897.0, -23246), 166651.00)

    def test0303(self):
        self.assertEquals(self.calculate(-104549.0, -2354), -106903.00)

    def test0304(self):
        self.assertEquals(self.calculate(13500.0, -14754), -1254.00)

    def test0305(self):
        self.assertEquals(self.calculate(-122842.0, 11541), -111301.00)

    def test0306(self):
        self.assertEquals(self.calculate(-31098.0, -19873), -50971.00)

    def test0307(self):
        self.assertEquals(self.calculate(-116510.0, -27191), -143701.00)

    def test0308(self):
        self.assertEquals(self.calculate(-23184.0, 30095), 6911.00)

    def test0309(self):
        self.assertEquals(self.calculate(-45280.0, -18578), -63858.00)

    def test0310(self):
        self.assertEquals(self.calculate(2874.0, -3634), -760.00)

    def test0311(self):
        self.assertEquals(self.calculate(-166830.0, 13853), -152977.00)

    def test0312(self):
        self.assertEquals(self.calculate(-160149.0, 19826), -140323.00)

    def test0313(self):
        self.assertEquals(self.calculate(155797.0, 6984), 162781.00)

    def test0314(self):
        self.assertEquals(self.calculate(94347.0, -19514), 74833.00)

    def test0315(self):
        self.assertEquals(self.calculate(173702.0, 30732), 204434.00)

    def test0316(self):
        self.assertEquals(self.calculate(-45208.0, -17226), -62434.00)

    def test0317(self):
        self.assertEquals(self.calculate(-112980.0, -20183), -133163.00)

    def test0318(self):
        self.assertEquals(self.calculate(-113682.0, 16733), -96949.00)

    def test0319(self):
        self.assertEquals(self.calculate(-131119.0, 24307), -106812.00)

    def test0320(self):
        self.assertEquals(self.calculate(112801.0, 22553), 135354.00)

    def test0321(self):
        self.assertEquals(self.calculate(174367.0, -15358), 159009.00)

    def test0322(self):
        self.assertEquals(self.calculate(-47630.0, 14856), -32774.00)

    def test0323(self):
        self.assertEquals(self.calculate(180331.0, 28136), 208467.00)

    def test0324(self):
        self.assertEquals(self.calculate(-61134.0, -8708), -69842.00)

    def test0325(self):
        self.assertEquals(self.calculate(135329.0, 16094), 151423.00)

    def test0326(self):
        self.assertEquals(self.calculate(-10609.0, -5717), -16326.00)

    def test0327(self):
        self.assertEquals(self.calculate(188056.0, 28954), 217010.00)

    def test0328(self):
        self.assertEquals(self.calculate(3738.0, -4059), -321.00)

    def test0329(self):
        self.assertEquals(self.calculate(-60374.0, -7289), -67663.00)

    def test0330(self):
        self.assertEquals(self.calculate(40983.0, -21903), 19080.00)

    def test0331(self):
        self.assertEquals(self.calculate(-29441.0, -18325), -47766.00)

    def test0332(self):
        self.assertEquals(self.calculate(162212.0, -26981), 135231.00)

    def test0333(self):
        self.assertEquals(self.calculate(-187592.0, -29249), -216841.00)

    def test0334(self):
        self.assertEquals(self.calculate(162459.0, -28859), 133600.00)

    def test0335(self):
        self.assertEquals(self.calculate(161077.0, 6393), 167470.00)

    def test0336(self):
        self.assertEquals(self.calculate(183274.0, 28811), 212085.00)

    def test0337(self):
        self.assertEquals(self.calculate(562.0, -9903), -9341.00)

    def test0338(self):
        self.assertEquals(self.calculate(-152922.0, 25957), -126965.00)

    def test0339(self):
        self.assertEquals(self.calculate(-162913.0, 24304), -138609.00)

    def test0340(self):
        self.assertEquals(self.calculate(-123929.0, -32604), -156533.00)

    def test0341(self):
        self.assertEquals(self.calculate(8487.0, -21346), -12859.00)

    def test0342(self):
        self.assertEquals(self.calculate(54276.0, -25288), 28988.00)

    def test0343(self):
        self.assertEquals(self.calculate(123037.0, 30104), 153141.00)

    def test0344(self):
        self.assertEquals(self.calculate(140165.0, 26596), 166761.00)

    def test0345(self):
        self.assertEquals(self.calculate(-134778.0, 32277), -102501.00)

    def test0346(self):
        self.assertEquals(self.calculate(73161.0, 23435), 96596.00)

    def test0347(self):
        self.assertEquals(self.calculate(120973.0, -1774), 119199.00)

    def test0348(self):
        self.assertEquals(self.calculate(135241.0, -20982), 114259.00)

    def test0349(self):
        self.assertEquals(self.calculate(-140305.0, 1139), -139166.00)

    def test0350(self):
        self.assertEquals(self.calculate(145450.0, -22005), 123445.00)

    def test0351(self):
        self.assertEquals(self.calculate(-120235.0, -27517), -147752.00)

    def test0352(self):
        self.assertEquals(self.calculate(35758.0, -2675), 33083.00)

    def test0353(self):
        self.assertEquals(self.calculate(-84299.0, -11028), -95327.00)

    def test0354(self):
        self.assertEquals(self.calculate(3263.0, 27724), 30987.00)

    def test0355(self):
        self.assertEquals(self.calculate(-23364.0, -5571), -28935.00)

    def test0356(self):
        self.assertEquals(self.calculate(119343.0, -4162), 115181.00)

    def test0357(self):
        self.assertEquals(self.calculate(-119403.0, -30584), -149987.00)

    def test0358(self):
        self.assertEquals(self.calculate(-48119.0, 30659), -17460.00)

    def test0359(self):
        self.assertEquals(self.calculate(-166348.0, -26272), -192620.00)

    def test0360(self):
        self.assertEquals(self.calculate(85882.0, 25307), 111189.00)

    def test0361(self):
        self.assertEquals(self.calculate(179485.0, 3540), 183025.00)

    def test0362(self):
        self.assertEquals(self.calculate(38376.0, 4442), 42818.00)

    def test0363(self):
        self.assertEquals(self.calculate(-103046.0, -8451), -111497.00)

    def test0364(self):
        self.assertEquals(self.calculate(185698.0, 8067), 193765.00)

    def test0365(self):
        self.assertEquals(self.calculate(-7151.0, 13995), 6844.00)

    def test0366(self):
        self.assertEquals(self.calculate(-154637.0, 11558), -143079.00)

    def test0367(self):
        self.assertEquals(self.calculate(178648.0, 23940), 202588.00)

    def test0368(self):
        self.assertEquals(self.calculate(67612.0, 3387), 70999.00)

    def test0369(self):
        self.assertEquals(self.calculate(-88170.0, -24806), -112976.00)

    def test0370(self):
        self.assertEquals(self.calculate(67671.0, 3506), 71177.00)

    def test0371(self):
        self.assertEquals(self.calculate(-176125.0, 31946), -144179.00)

    def test0372(self):
        self.assertEquals(self.calculate(-52300.0, -31097), -83397.00)

    def test0373(self):
        self.assertEquals(self.calculate(-183928.0, 7161), -176767.00)

    def test0374(self):
        self.assertEquals(self.calculate(183715.0, -4225), 179490.00)

    def test0375(self):
        self.assertEquals(self.calculate(-37250.0, -26565), -63815.00)

    def test0376(self):
        self.assertEquals(self.calculate(145540.0, -13425), 132115.00)

    def test0377(self):
        self.assertEquals(self.calculate(24607.0, -29945), -5338.00)

    def test0378(self):
        self.assertEquals(self.calculate(-98472.0, 14296), -84176.00)

    def test0379(self):
        self.assertEquals(self.calculate(-148538.0, -22361), -170899.00)

    def test0380(self):
        self.assertEquals(self.calculate(-176645.0, 2422), -174223.00)

    def test0381(self):
        self.assertEquals(self.calculate(142439.0, 28141), 170580.00)

    def test0382(self):
        self.assertEquals(self.calculate(180774.0, 20677), 201451.00)

    def test0383(self):
        self.assertEquals(self.calculate(-169356.0, 3116), -166240.00)

    def test0384(self):
        self.assertEquals(self.calculate(88994.0, 3733), 92727.00)

    def test0385(self):
        self.assertEquals(self.calculate(63387.0, 8726), 72113.00)

    def test0386(self):
        self.assertEquals(self.calculate(-49152.0, -6633), -55785.00)

    def test0387(self):
        self.assertEquals(self.calculate(-129476.0, 19042), -110434.00)

    def test0388(self):
        self.assertEquals(self.calculate(-107313.0, -11674), -118987.00)

    def test0389(self):
        self.assertEquals(self.calculate(40489.0, 7070), 47559.00)

    def test0390(self):
        self.assertEquals(self.calculate(-8214.0, 16180), 7966.00)

    def test0391(self):
        self.assertEquals(self.calculate(193060.0, -26262), 166798.00)

    def test0392(self):
        self.assertEquals(self.calculate(101725.0, 32418), 134143.00)

    def test0393(self):
        self.assertEquals(self.calculate(-173147.0, -3235), -176382.00)

    def test0394(self):
        self.assertEquals(self.calculate(85664.0, -17907), 67757.00)

    def test0395(self):
        self.assertEquals(self.calculate(36490.0, -15160), 21330.00)

    def test0396(self):
        self.assertEquals(self.calculate(157671.0, -21334), 136337.00)

    def test0397(self):
        self.assertEquals(self.calculate(145818.0, 21315), 167133.00)

    def test0398(self):
        self.assertEquals(self.calculate(-37127.0, 2644), -34483.00)

    def test0399(self):
        self.assertEquals(self.calculate(168519.0, 6228), 174747.00)

    def test0400(self):
        self.assertEquals(self.calculate(-186433.0, -14914), -201347.00)

    def test0401(self):
        self.assertEquals(self.calculate(-166340.0, 26892), -139448.00)

    def test0402(self):
        self.assertEquals(self.calculate(-129090.0, 25875), -103215.00)

    def test0403(self):
        self.assertEquals(self.calculate(160436.0, -14187), 146249.00)

    def test0404(self):
        self.assertEquals(self.calculate(-31649.0, -13156), -44805.00)

    def test0405(self):
        self.assertEquals(self.calculate(-42318.0, 19554), -22764.00)

    def test0406(self):
        self.assertEquals(self.calculate(-5261.0, -5182), -10443.00)

    def test0407(self):
        self.assertEquals(self.calculate(107468.0, 30542), 138010.00)

    def test0408(self):
        self.assertEquals(self.calculate(167965.0, -22619), 145346.00)

    def test0409(self):
        self.assertEquals(self.calculate(-3373.0, 2206), -1167.00)

    def test0410(self):
        self.assertEquals(self.calculate(4432.0, -16564), -12132.00)

    def test0411(self):
        self.assertEquals(self.calculate(-190052.0, 12867), -177185.00)

    def test0412(self):
        self.assertEquals(self.calculate(-164536.0, 14967), -149569.00)

    def test0413(self):
        self.assertEquals(self.calculate(176672.0, 26951), 203623.00)

    def test0414(self):
        self.assertEquals(self.calculate(-185998.0, -11896), -197894.00)

    def test0415(self):
        self.assertEquals(self.calculate(-148298.0, -10114), -158412.00)

    def test0416(self):
        self.assertEquals(self.calculate(-158319.0, -28935), -187254.00)

    def test0417(self):
        self.assertEquals(self.calculate(42731.0, -3199), 39532.00)

    def test0418(self):
        self.assertEquals(self.calculate(-42468.0, 28639), -13829.00)

    def test0419(self):
        self.assertEquals(self.calculate(-171694.0, -9040), -180734.00)

    def test0420(self):
        self.assertEquals(self.calculate(95081.0, 27048), 122129.00)

    def test0421(self):
        self.assertEquals(self.calculate(172785.0, 19995), 192780.00)

    def test0422(self):
        self.assertEquals(self.calculate(141984.0, 4538), 146522.00)

    def test0423(self):
        self.assertEquals(self.calculate(-14223.0, -32683), -46906.00)

    def test0424(self):
        self.assertEquals(self.calculate(-191553.0, -1898), -193451.00)

    def test0425(self):
        self.assertEquals(self.calculate(124196.0, -30591), 93605.00)

    def test0426(self):
        self.assertEquals(self.calculate(-145692.0, -18751), -164443.00)

    def test0427(self):
        self.assertEquals(self.calculate(-125922.0, 9954), -115968.00)

    def test0428(self):
        self.assertEquals(self.calculate(-191745.0, -32356), -224101.00)

    def test0429(self):
        self.assertEquals(self.calculate(-39363.0, -16993), -56356.00)

    def test0430(self):
        self.assertEquals(self.calculate(64286.0, -10194), 54092.00)

    def test0431(self):
        self.assertEquals(self.calculate(-194429.0, 10357), -184072.00)

    def test0432(self):
        self.assertEquals(self.calculate(-60936.0, 8139), -52797.00)

    def test0433(self):
        self.assertEquals(self.calculate(130582.0, -10775), 119807.00)

    def test0434(self):
        self.assertEquals(self.calculate(93867.0, 18154), 112021.00)

    def test0435(self):
        self.assertEquals(self.calculate(17176.0, 4548), 21724.00)

    def test0436(self):
        self.assertEquals(self.calculate(-159124.0, -14644), -173768.00)

    def test0437(self):
        self.assertEquals(self.calculate(-176338.0, 29479), -146859.00)

    def test0438(self):
        self.assertEquals(self.calculate(-33520.0, -15703), -49223.00)

    def test0439(self):
        self.assertEquals(self.calculate(76239.0, 18751), 94990.00)

    def test0440(self):
        self.assertEquals(self.calculate(119638.0, -437), 119201.00)

    def test0441(self):
        self.assertEquals(self.calculate(-60728.0, 22975), -37753.00)

    def test0442(self):
        self.assertEquals(self.calculate(-127782.0, 1521), -126261.00)

    def test0443(self):
        self.assertEquals(self.calculate(-187769.0, -25760), -213529.00)

    def test0444(self):
        self.assertEquals(self.calculate(-42221.0, -5529), -47750.00)

    def test0445(self):
        self.assertEquals(self.calculate(-184588.0, -25385), -209973.00)

    def test0446(self):
        self.assertEquals(self.calculate(-13426.0, -3224), -16650.00)

    def test0447(self):
        self.assertEquals(self.calculate(149954.0, 24161), 174115.00)

    def test0448(self):
        self.assertEquals(self.calculate(-62624.0, 19637), -42987.00)

    def test0449(self):
        self.assertEquals(self.calculate(-130656.0, 23043), -107613.00)

    def test0450(self):
        self.assertEquals(self.calculate(-159967.0, -19670), -179637.00)

    def test0451(self):
        self.assertEquals(self.calculate(4844.0, 14294), 19138.00)

    def test0452(self):
        self.assertEquals(self.calculate(139184.0, 20232), 159416.00)

    def test0453(self):
        self.assertEquals(self.calculate(124902.0, 24223), 149125.00)

    def test0454(self):
        self.assertEquals(self.calculate(-162014.0, -3434), -165448.00)

    def test0455(self):
        self.assertEquals(self.calculate(169964.0, -16662), 153302.00)

    def test0456(self):
        self.assertEquals(self.calculate(-72456.0, 26806), -45650.00)

    def test0457(self):
        self.assertEquals(self.calculate(-158085.0, -3063), -161148.00)

    def test0458(self):
        self.assertEquals(self.calculate(-169121.0, 6859), -162262.00)

    def test0459(self):
        self.assertEquals(self.calculate(53826.0, -28500), 25326.00)

    def test0460(self):
        self.assertEquals(self.calculate(-78306.0, 414), -77892.00)

    def test0461(self):
        self.assertEquals(self.calculate(-193559.0, -20045), -213604.00)

    def test0462(self):
        self.assertEquals(self.calculate(133612.0, -10469), 123143.00)

    def test0463(self):
        self.assertEquals(self.calculate(31630.0, 18024), 49654.00)

    def test0464(self):
        self.assertEquals(self.calculate(102646.0, -28976), 73670.00)

    def test0465(self):
        self.assertEquals(self.calculate(187096.0, -1712), 185384.00)

    def test0466(self):
        self.assertEquals(self.calculate(-48595.0, -10285), -58880.00)

    def test0467(self):
        self.assertEquals(self.calculate(27700.0, 822), 28522.00)

    def test0468(self):
        self.assertEquals(self.calculate(56260.0, 12118), 68378.00)

    def test0469(self):
        self.assertEquals(self.calculate(67037.0, -1658), 65379.00)

    def test0470(self):
        self.assertEquals(self.calculate(78260.0, 28182), 106442.00)

    def test0471(self):
        self.assertEquals(self.calculate(144501.0, -32303), 112198.00)

    def test0472(self):
        self.assertEquals(self.calculate(131561.0, -20352), 111209.00)

    def test0473(self):
        self.assertEquals(self.calculate(-124514.0, -2537), -127051.00)

    def test0474(self):
        self.assertEquals(self.calculate(143452.0, 11037), 154489.00)

    def test0475(self):
        self.assertEquals(self.calculate(-34158.0, -19516), -53674.00)

    def test0476(self):
        self.assertEquals(self.calculate(-142790.0, -3078), -145868.00)

    def test0477(self):
        self.assertEquals(self.calculate(-58587.0, 28590), -29997.00)

    def test0478(self):
        self.assertEquals(self.calculate(-191853.0, 27407), -164446.00)

    def test0479(self):
        self.assertEquals(self.calculate(158567.0, -19558), 139009.00)

    def test0480(self):
        self.assertEquals(self.calculate(-33188.0, 7015), -26173.00)

    def test0481(self):
        self.assertEquals(self.calculate(71962.0, -4976), 66986.00)

    def test0482(self):
        self.assertEquals(self.calculate(-113960.0, -8673), -122633.00)

    def test0483(self):
        self.assertEquals(self.calculate(-104825.0, 2622), -102203.00)

    def test0484(self):
        self.assertEquals(self.calculate(-123717.0, 20074), -103643.00)

    def test0485(self):
        self.assertEquals(self.calculate(29653.0, -15149), 14504.00)

    def test0486(self):
        self.assertEquals(self.calculate(-43159.0, -29914), -73073.00)

    def test0487(self):
        self.assertEquals(self.calculate(83638.0, 14080), 97718.00)

    def test0488(self):
        self.assertEquals(self.calculate(-191699.0, 3088), -188611.00)

    def test0489(self):
        self.assertEquals(self.calculate(-167618.0, -7099), -174717.00)

    def test0490(self):
        self.assertEquals(self.calculate(193294.0, -6373), 186921.00)

    def test0491(self):
        self.assertEquals(self.calculate(87462.0, 26054), 113516.00)

    def test0492(self):
        self.assertEquals(self.calculate(-143049.0, 30387), -112662.00)

    def test0493(self):
        self.assertEquals(self.calculate(94906.0, 25123), 120029.00)

    def test0494(self):
        self.assertEquals(self.calculate(61856.0, -21297), 40559.00)

    def test0495(self):
        self.assertEquals(self.calculate(74099.0, -20055), 54044.00)

    def test0496(self):
        self.assertEquals(self.calculate(61473.0, -12635), 48838.00)

    def test0497(self):
        self.assertEquals(self.calculate(-189307.0, 21350), -167957.00)

    def test0498(self):
        self.assertEquals(self.calculate(-100794.0, 6892), -93902.00)

    def test0499(self):
        self.assertEquals(self.calculate(-137423.0, -433), -137856.00)

    def test0500(self):
        self.assertEquals(self.calculate(-153932.0, 19710), -134222.00)

    def test0501(self):
        self.assertEquals(self.calculate(53707.0, 16201), 69908.00)

    def test0502(self):
        self.assertEquals(self.calculate(-136338.0, 22606), -113732.00)

    def test0503(self):
        self.assertEquals(self.calculate(-26169.0, 14535), -11634.00)

    def test0504(self):
        self.assertEquals(self.calculate(125276.0, -9834), 115442.00)

    def test0505(self):
        self.assertEquals(self.calculate(-75746.0, -31659), -107405.00)

    def test0506(self):
        self.assertEquals(self.calculate(178123.0, -30081), 148042.00)

    def test0507(self):
        self.assertEquals(self.calculate(-76098.0, -29496), -105594.00)

    def test0508(self):
        self.assertEquals(self.calculate(101391.0, 21652), 123043.00)

    def test0509(self):
        self.assertEquals(self.calculate(138772.0, 22104), 160876.00)

    def test0510(self):
        self.assertEquals(self.calculate(-136662.0, -19913), -156575.00)

    def test0511(self):
        self.assertEquals(self.calculate(-193439.0, -29190), -222629.00)

    def test0512(self):
        self.assertEquals(self.calculate(-112601.0, -21253), -133854.00)

    def test0513(self):
        self.assertEquals(self.calculate(101193.0, -13813), 87380.00)

    def test0514(self):
        self.assertEquals(self.calculate(114639.0, 4525), 119164.00)

    def test0515(self):
        self.assertEquals(self.calculate(102314.0, 22501), 124815.00)

    def test0516(self):
        self.assertEquals(self.calculate(-51147.0, 15236), -35911.00)

    def test0517(self):
        self.assertEquals(self.calculate(77432.0, 13834), 91266.00)

    def test0518(self):
        self.assertEquals(self.calculate(73632.0, -24943), 48689.00)

    def test0519(self):
        self.assertEquals(self.calculate(-87290.0, -9898), -97188.00)

    def test0520(self):
        self.assertEquals(self.calculate(-121889.0, 17766), -104123.00)

    def test0521(self):
        self.assertEquals(self.calculate(-191948.0, 29126), -162822.00)

    def test0522(self):
        self.assertEquals(self.calculate(-123470.0, 24976), -98494.00)

    def test0523(self):
        self.assertEquals(self.calculate(130303.0, -15201), 115102.00)

    def test0524(self):
        self.assertEquals(self.calculate(-73031.0, 7339), -65692.00)

    def test0525(self):
        self.assertEquals(self.calculate(-163246.0, -2342), -165588.00)

    def test0526(self):
        self.assertEquals(self.calculate(-4883.0, -6424), -11307.00)

    def test0527(self):
        self.assertEquals(self.calculate(-141231.0, 13770), -127461.00)

    def test0528(self):
        self.assertEquals(self.calculate(-59035.0, -20682), -79717.00)

    def test0529(self):
        self.assertEquals(self.calculate(192319.0, -29756), 162563.00)

    def test0530(self):
        self.assertEquals(self.calculate(188966.0, 15790), 204756.00)

    def test0531(self):
        self.assertEquals(self.calculate(-147980.0, 21310), -126670.00)

    def test0532(self):
        self.assertEquals(self.calculate(179930.0, 6145), 186075.00)

    def test0533(self):
        self.assertEquals(self.calculate(-153968.0, -7947), -161915.00)

    def test0534(self):
        self.assertEquals(self.calculate(-141832.0, -17154), -158986.00)

    def test0535(self):
        self.assertEquals(self.calculate(-89841.0, 20400), -69441.00)

    def test0536(self):
        self.assertEquals(self.calculate(-97733.0, -16422), -114155.00)

    def test0537(self):
        self.assertEquals(self.calculate(121645.0, -24783), 96862.00)

    def test0538(self):
        self.assertEquals(self.calculate(-87777.0, 17361), -70416.00)

    def test0539(self):
        self.assertEquals(self.calculate(-186498.0, 13203), -173295.00)

    def test0540(self):
        self.assertEquals(self.calculate(1826.0, -23163), -21337.00)

    def test0541(self):
        self.assertEquals(self.calculate(116949.0, -22278), 94671.00)

    def test0542(self):
        self.assertEquals(self.calculate(173577.0, 15239), 188816.00)

    def test0543(self):
        self.assertEquals(self.calculate(119794.0, 18115), 137909.00)

    def test0544(self):
        self.assertEquals(self.calculate(184745.0, 31019), 215764.00)

    def test0545(self):
        self.assertEquals(self.calculate(134185.0, 5120), 139305.00)

    def test0546(self):
        self.assertEquals(self.calculate(-93275.0, 19337), -73938.00)

    def test0547(self):
        self.assertEquals(self.calculate(-68481.0, 23374), -45107.00)

    def test0548(self):
        self.assertEquals(self.calculate(170646.0, 1546), 172192.00)

    def test0549(self):
        self.assertEquals(self.calculate(73897.0, 28471), 102368.00)

    def test0550(self):
        self.assertEquals(self.calculate(-76747.0, 19549), -57198.00)

    def test0551(self):
        self.assertEquals(self.calculate(20182.0, -8930), 11252.00)

    def test0552(self):
        self.assertEquals(self.calculate(90922.0, -28244), 62678.00)

    def test0553(self):
        self.assertEquals(self.calculate(46963.0, -25415), 21548.00)

    def test0554(self):
        self.assertEquals(self.calculate(154211.0, 30250), 184461.00)

    def test0555(self):
        self.assertEquals(self.calculate(-56266.0, -15933), -72199.00)

    def test0556(self):
        self.assertEquals(self.calculate(-79380.0, 24404), -54976.00)

    def test0557(self):
        self.assertEquals(self.calculate(166099.0, -945), 165154.00)

    def test0558(self):
        self.assertEquals(self.calculate(-96125.0, -5415), -101540.00)

    def test0559(self):
        self.assertEquals(self.calculate(-49829.0, -21265), -71094.00)

    def test0560(self):
        self.assertEquals(self.calculate(-189484.0, 9570), -179914.00)

    def test0561(self):
        self.assertEquals(self.calculate(-85639.0, 31136), -54503.00)

    def test0562(self):
        self.assertEquals(self.calculate(17095.0, 25935), 43030.00)

    def test0563(self):
        self.assertEquals(self.calculate(69690.0, 31666), 101356.00)

    def test0564(self):
        self.assertEquals(self.calculate(-126219.0, 13046), -113173.00)

    def test0565(self):
        self.assertEquals(self.calculate(115366.0, -17422), 97944.00)

    def test0566(self):
        self.assertEquals(self.calculate(-38354.0, -5865), -44219.00)

    def test0567(self):
        self.assertEquals(self.calculate(-168024.0, 2543), -165481.00)

    def test0568(self):
        self.assertEquals(self.calculate(-131724.0, 11465), -120259.00)

    def test0569(self):
        self.assertEquals(self.calculate(-130891.0, 253), -130638.00)

    def test0570(self):
        self.assertEquals(self.calculate(-56669.0, 17090), -39579.00)

    def test0571(self):
        self.assertEquals(self.calculate(-198116.0, 22374), -175742.00)

    def test0572(self):
        self.assertEquals(self.calculate(144540.0, -848), 143692.00)

    def test0573(self):
        self.assertEquals(self.calculate(-43572.0, 1894), -41678.00)

    def test0574(self):
        self.assertEquals(self.calculate(136615.0, -30814), 105801.00)

    def test0575(self):
        self.assertEquals(self.calculate(4334.0, -22740), -18406.00)

    def test0576(self):
        self.assertEquals(self.calculate(-61780.0, 11998), -49782.00)

    def test0577(self):
        self.assertEquals(self.calculate(-58742.0, 20202), -38540.00)

    def test0578(self):
        self.assertEquals(self.calculate(18609.0, -26987), -8378.00)

    def test0579(self):
        self.assertEquals(self.calculate(-33005.0, -8645), -41650.00)

    def test0580(self):
        self.assertEquals(self.calculate(-58962.0, -12473), -71435.00)

    def test0581(self):
        self.assertEquals(self.calculate(174666.0, 18615), 193281.00)

    def test0582(self):
        self.assertEquals(self.calculate(-98654.0, 1958), -96696.00)

    def test0583(self):
        self.assertEquals(self.calculate(169738.0, 5905), 175643.00)

    def test0584(self):
        self.assertEquals(self.calculate(-88494.0, -28765), -117259.00)

    def test0585(self):
        self.assertEquals(self.calculate(127617.0, 16991), 144608.00)

    def test0586(self):
        self.assertEquals(self.calculate(16060.0, -5354), 10706.00)

    def test0587(self):
        self.assertEquals(self.calculate(12660.0, -11115), 1545.00)

    def test0588(self):
        self.assertEquals(self.calculate(83.0, -6314), -6231.00)

    def test0589(self):
        self.assertEquals(self.calculate(18168.0, 30400), 48568.00)

    def test0590(self):
        self.assertEquals(self.calculate(51514.0, 23591), 75105.00)

    def test0591(self):
        self.assertEquals(self.calculate(197443.0, 14154), 211597.00)

    def test0592(self):
        self.assertEquals(self.calculate(-77693.0, 12262), -65431.00)

    def test0593(self):
        self.assertEquals(self.calculate(-51812.0, 10747), -41065.00)

    def test0594(self):
        self.assertEquals(self.calculate(-94011.0, 5791), -88220.00)

    def test0595(self):
        self.assertEquals(self.calculate(47359.0, 8149), 55508.00)

    def test0596(self):
        self.assertEquals(self.calculate(-69507.0, -3060), -72567.00)

    def test0597(self):
        self.assertEquals(self.calculate(-32474.0, 227), -32247.00)

    def test0598(self):
        self.assertEquals(self.calculate(79183.0, -20192), 58991.00)

    def test0599(self):
        self.assertEquals(self.calculate(90729.0, 26522), 117251.00)

    def test0600(self):
        self.assertEquals(self.calculate(-170139.0, 26280), -143859.00)

    def test0601(self):
        self.assertEquals(self.calculate(90524.0, 31913), 122437.00)

    def test0602(self):
        self.assertEquals(self.calculate(193960.0, 24958), 218918.00)

    def test0603(self):
        self.assertEquals(self.calculate(-152278.0, 28966), -123312.00)

    def test0604(self):
        self.assertEquals(self.calculate(63418.0, 17919), 81337.00)

    def test0605(self):
        self.assertEquals(self.calculate(39308.0, -7075), 32233.00)

    def test0606(self):
        self.assertEquals(self.calculate(-165357.0, -17638), -182995.00)

    def test0607(self):
        self.assertEquals(self.calculate(62565.0, -13448), 49117.00)

    def test0608(self):
        self.assertEquals(self.calculate(-169616.0, 2797), -166819.00)

    def test0609(self):
        self.assertEquals(self.calculate(130102.0, 31278), 161380.00)

    def test0610(self):
        self.assertEquals(self.calculate(171749.0, -4439), 167310.00)

    def test0611(self):
        self.assertEquals(self.calculate(138224.0, 16549), 154773.00)

    def test0612(self):
        self.assertEquals(self.calculate(-55972.0, -870), -56842.00)

    def test0613(self):
        self.assertEquals(self.calculate(133630.0, 26925), 160555.00)

    def test0614(self):
        self.assertEquals(self.calculate(-133941.0, -17636), -151577.00)

    def test0615(self):
        self.assertEquals(self.calculate(-74550.0, 12178), -62372.00)

    def test0616(self):
        self.assertEquals(self.calculate(8389.0, -13539), -5150.00)

    def test0617(self):
        self.assertEquals(self.calculate(-127596.0, -23074), -150670.00)

    def test0618(self):
        self.assertEquals(self.calculate(-49056.0, 2455), -46601.00)

    def test0619(self):
        self.assertEquals(self.calculate(81181.0, -24476), 56705.00)

    def test0620(self):
        self.assertEquals(self.calculate(143229.0, -32051), 111178.00)

    def test0621(self):
        self.assertEquals(self.calculate(118542.0, -19898), 98644.00)

    def test0622(self):
        self.assertEquals(self.calculate(9442.0, -18528), -9086.00)

    def test0623(self):
        self.assertEquals(self.calculate(158484.0, 29020), 187504.00)

    def test0624(self):
        self.assertEquals(self.calculate(189865.0, 8188), 198053.00)

    def test0625(self):
        self.assertEquals(self.calculate(-137887.0, -11494), -149381.00)

    def test0626(self):
        self.assertEquals(self.calculate(-157931.0, 7717), -150214.00)

    def test0627(self):
        self.assertEquals(self.calculate(-110056.0, 19141), -90915.00)

    def test0628(self):
        self.assertEquals(self.calculate(112765.0, -20152), 92613.00)

    def test0629(self):
        self.assertEquals(self.calculate(-197122.0, -14128), -211250.00)

    def test0630(self):
        self.assertEquals(self.calculate(61716.0, -32709), 29007.00)

    def test0631(self):
        self.assertEquals(self.calculate(-119331.0, 22060), -97271.00)

    def test0632(self):
        self.assertEquals(self.calculate(74512.0, 2807), 77319.00)

    def test0633(self):
        self.assertEquals(self.calculate(-126658.0, 31836), -94822.00)

    def test0634(self):
        self.assertEquals(self.calculate(-187542.0, 9395), -178147.00)

    def test0635(self):
        self.assertEquals(self.calculate(143979.0, 1075), 145054.00)

    def test0636(self):
        self.assertEquals(self.calculate(-141061.0, -32185), -173246.00)

    def test0637(self):
        self.assertEquals(self.calculate(11024.0, 14631), 25655.00)

    def test0638(self):
        self.assertEquals(self.calculate(95618.0, -24853), 70765.00)

    def test0639(self):
        self.assertEquals(self.calculate(-177000.0, -19093), -196093.00)

    def test0640(self):
        self.assertEquals(self.calculate(29982.0, -23073), 6909.00)

    def test0641(self):
        self.assertEquals(self.calculate(-190511.0, 31350), -159161.00)

    def test0642(self):
        self.assertEquals(self.calculate(-49034.0, 30044), -18990.00)

    def test0643(self):
        self.assertEquals(self.calculate(-171587.0, -14919), -186506.00)

    def test0644(self):
        self.assertEquals(self.calculate(194581.0, 22676), 217257.00)

    def test0645(self):
        self.assertEquals(self.calculate(151702.0, 12815), 164517.00)

    def test0646(self):
        self.assertEquals(self.calculate(119345.0, 23623), 142968.00)

    def test0647(self):
        self.assertEquals(self.calculate(-20392.0, -13232), -33624.00)

    def test0648(self):
        self.assertEquals(self.calculate(-75889.0, 2293), -73596.00)

    def test0649(self):
        self.assertEquals(self.calculate(49785.0, -4672), 45113.00)

    def test0650(self):
        self.assertEquals(self.calculate(45154.0, -21200), 23954.00)

    def test0651(self):
        self.assertEquals(self.calculate(24598.0, -15484), 9114.00)

    def test0652(self):
        self.assertEquals(self.calculate(145160.0, 8599), 153759.00)

    def test0653(self):
        self.assertEquals(self.calculate(39216.0, 25775), 64991.00)

    def test0654(self):
        self.assertEquals(self.calculate(232.0, -18609), -18377.00)

    def test0655(self):
        self.assertEquals(self.calculate(-194378.0, -23061), -217439.00)

    def test0656(self):
        self.assertEquals(self.calculate(171063.0, 12215), 183278.00)

    def test0657(self):
        self.assertEquals(self.calculate(-149622.0, -8295), -157917.00)

    def test0658(self):
        self.assertEquals(self.calculate(-153862.0, -29830), -183692.00)

    def test0659(self):
        self.assertEquals(self.calculate(-158355.0, 19505), -138850.00)

    def test0660(self):
        self.assertEquals(self.calculate(-166959.0, 2756), -164203.00)

    def test0661(self):
        self.assertEquals(self.calculate(-8377.0, 25823), 17446.00)

    def test0662(self):
        self.assertEquals(self.calculate(44604.0, 6941), 51545.00)

    def test0663(self):
        self.assertEquals(self.calculate(146832.0, 11526), 158358.00)

    def test0664(self):
        self.assertEquals(self.calculate(-187912.0, -2925), -190837.00)

    def test0665(self):
        self.assertEquals(self.calculate(131092.0, -26056), 105036.00)

    def test0666(self):
        self.assertEquals(self.calculate(-18401.0, 8516), -9885.00)

    def test0667(self):
        self.assertEquals(self.calculate(186254.0, 3649), 189903.00)

    def test0668(self):
        self.assertEquals(self.calculate(-130418.0, 22194), -108224.00)

    def test0669(self):
        self.assertEquals(self.calculate(58061.0, 25911), 83972.00)

    def test0670(self):
        self.assertEquals(self.calculate(-59872.0, -2849), -62721.00)

    def test0671(self):
        self.assertEquals(self.calculate(-6376.0, 3642), -2734.00)

    def test0672(self):
        self.assertEquals(self.calculate(-17634.0, -27546), -45180.00)

    def test0673(self):
        self.assertEquals(self.calculate(52867.0, 19876), 72743.00)

    def test0674(self):
        self.assertEquals(self.calculate(-194295.0, -10857), -205152.00)

    def test0675(self):
        self.assertEquals(self.calculate(-136055.0, -6693), -142748.00)

    def test0676(self):
        self.assertEquals(self.calculate(-82812.0, -24176), -106988.00)

    def test0677(self):
        self.assertEquals(self.calculate(149626.0, -12418), 137208.00)

    def test0678(self):
        self.assertEquals(self.calculate(-138239.0, -30169), -168408.00)

    def test0679(self):
        self.assertEquals(self.calculate(-49943.0, 4093), -45850.00)

    def test0680(self):
        self.assertEquals(self.calculate(119719.0, -30270), 89449.00)

    def test0681(self):
        self.assertEquals(self.calculate(50232.0, -27178), 23054.00)

    def test0682(self):
        self.assertEquals(self.calculate(151141.0, 27326), 178467.00)

    def test0683(self):
        self.assertEquals(self.calculate(97982.0, -23793), 74189.00)

    def test0684(self):
        self.assertEquals(self.calculate(-77963.0, 8142), -69821.00)

    def test0685(self):
        self.assertEquals(self.calculate(-1641.0, 17220), 15579.00)

    def test0686(self):
        self.assertEquals(self.calculate(-189532.0, -22474), -212006.00)

    def test0687(self):
        self.assertEquals(self.calculate(95225.0, -11639), 83586.00)

    def test0688(self):
        self.assertEquals(self.calculate(34807.0, -21602), 13205.00)

    def test0689(self):
        self.assertEquals(self.calculate(63044.0, 3702), 66746.00)

    def test0690(self):
        self.assertEquals(self.calculate(-54201.0, -8900), -63101.00)

    def test0691(self):
        self.assertEquals(self.calculate(-192931.0, 7816), -185115.00)

    def test0692(self):
        self.assertEquals(self.calculate(-104636.0, 22958), -81678.00)

    def test0693(self):
        self.assertEquals(self.calculate(-181980.0, 24586), -157394.00)

    def test0694(self):
        self.assertEquals(self.calculate(-66470.0, -15619), -82089.00)

    def test0695(self):
        self.assertEquals(self.calculate(-5898.0, -24575), -30473.00)

    def test0696(self):
        self.assertEquals(self.calculate(113063.0, 32149), 145212.00)

    def test0697(self):
        self.assertEquals(self.calculate(147018.0, -4745), 142273.00)

    def test0698(self):
        self.assertEquals(self.calculate(-52805.0, -27811), -80616.00)

    def test0699(self):
        self.assertEquals(self.calculate(-77902.0, 22186), -55716.00)

    def test0700(self):
        self.assertEquals(self.calculate(190794.0, -30022), 160772.00)

    def test0701(self):
        self.assertEquals(self.calculate(-95979.0, -8074), -104053.00)

    def test0702(self):
        self.assertEquals(self.calculate(-171215.0, -7901), -179116.00)

    def test0703(self):
        self.assertEquals(self.calculate(-50030.0, 28545), -21485.00)

    def test0704(self):
        self.assertEquals(self.calculate(84977.0, -1258), 83719.00)

    def test0705(self):
        self.assertEquals(self.calculate(-6780.0, 1229), -5551.00)

    def test0706(self):
        self.assertEquals(self.calculate(120076.0, 16745), 136821.00)

    def test0707(self):
        self.assertEquals(self.calculate(-145663.0, -16553), -162216.00)

    def test0708(self):
        self.assertEquals(self.calculate(13105.0, -30768), -17663.00)

    def test0709(self):
        self.assertEquals(self.calculate(80483.0, -12035), 68448.00)

    def test0710(self):
        self.assertEquals(self.calculate(149183.0, -11942), 137241.00)

    def test0711(self):
        self.assertEquals(self.calculate(-71261.0, 27316), -43945.00)

    def test0712(self):
        self.assertEquals(self.calculate(43302.0, 4933), 48235.00)

    def test0713(self):
        self.assertEquals(self.calculate(32292.0, 14449), 46741.00)

    def test0714(self):
        self.assertEquals(self.calculate(196969.0, 2331), 199300.00)

    def test0715(self):
        self.assertEquals(self.calculate(160142.0, -3412), 156730.00)

    def test0716(self):
        self.assertEquals(self.calculate(14143.0, -3155), 10988.00)

    def test0717(self):
        self.assertEquals(self.calculate(163275.0, -24689), 138586.00)

    def test0718(self):
        self.assertEquals(self.calculate(-100716.0, -28072), -128788.00)

    def test0719(self):
        self.assertEquals(self.calculate(-154363.0, -22368), -176731.00)

    def test0720(self):
        self.assertEquals(self.calculate(-37210.0, -2715), -39925.00)

    def test0721(self):
        self.assertEquals(self.calculate(-84995.0, 7464), -77531.00)

    def test0722(self):
        self.assertEquals(self.calculate(-6116.0, 8453), 2337.00)

    def test0723(self):
        self.assertEquals(self.calculate(137808.0, -6990), 130818.00)

    def test0724(self):
        self.assertEquals(self.calculate(-91772.0, 15847), -75925.00)

    def test0725(self):
        self.assertEquals(self.calculate(-94593.0, -30925), -125518.00)

    def test0726(self):
        self.assertEquals(self.calculate(134777.0, -16435), 118342.00)

    def test0727(self):
        self.assertEquals(self.calculate(-124027.0, 16325), -107702.00)

    def test0728(self):
        self.assertEquals(self.calculate(18111.0, 15710), 33821.00)

    def test0729(self):
        self.assertEquals(self.calculate(-156402.0, -18615), -175017.00)

    def test0730(self):
        self.assertEquals(self.calculate(-81359.0, 20552), -60807.00)

    def test0731(self):
        self.assertEquals(self.calculate(165513.0, 4052), 169565.00)

    def test0732(self):
        self.assertEquals(self.calculate(112097.0, 14516), 126613.00)

    def test0733(self):
        self.assertEquals(self.calculate(-47021.0, -25534), -72555.00)

    def test0734(self):
        self.assertEquals(self.calculate(-199184.0, -19880), -219064.00)

    def test0735(self):
        self.assertEquals(self.calculate(-44889.0, 26735), -18154.00)

    def test0736(self):
        self.assertEquals(self.calculate(-27712.0, 2030), -25682.00)

    def test0737(self):
        self.assertEquals(self.calculate(74476.0, 26153), 100629.00)

    def test0738(self):
        self.assertEquals(self.calculate(-87936.0, -4382), -92318.00)

    def test0739(self):
        self.assertEquals(self.calculate(129896.0, 830), 130726.00)

    def test0740(self):
        self.assertEquals(self.calculate(2285.0, 22036), 24321.00)

    def test0741(self):
        self.assertEquals(self.calculate(119112.0, 21507), 140619.00)

    def test0742(self):
        self.assertEquals(self.calculate(-87314.0, 6945), -80369.00)

    def test0743(self):
        self.assertEquals(self.calculate(-53680.0, 28558), -25122.00)

    def test0744(self):
        self.assertEquals(self.calculate(179286.0, -26312), 152974.00)

    def test0745(self):
        self.assertEquals(self.calculate(133609.0, -10638), 122971.00)

    def test0746(self):
        self.assertEquals(self.calculate(-29391.0, -25709), -55100.00)

    def test0747(self):
        self.assertEquals(self.calculate(-117175.0, -10598), -127773.00)

    def test0748(self):
        self.assertEquals(self.calculate(11114.0, -13170), -2056.00)

    def test0749(self):
        self.assertEquals(self.calculate(75237.0, -32635), 42602.00)

    def test0750(self):
        self.assertEquals(self.calculate(-151448.0, -20981), -172429.00)

    def test0751(self):
        self.assertEquals(self.calculate(46552.0, 4257), 50809.00)

    def test0752(self):
        self.assertEquals(self.calculate(-95288.0, 30476), -64812.00)

    def test0753(self):
        self.assertEquals(self.calculate(-9248.0, -27540), -36788.00)

    def test0754(self):
        self.assertEquals(self.calculate(184727.0, 19394), 204121.00)

    def test0755(self):
        self.assertEquals(self.calculate(-173430.0, -9297), -182727.00)

    def test0756(self):
        self.assertEquals(self.calculate(-92751.0, 4865), -87886.00)

    def test0757(self):
        self.assertEquals(self.calculate(-40709.0, 12871), -27838.00)

    def test0758(self):
        self.assertEquals(self.calculate(27694.0, 20728), 48422.00)

    def test0759(self):
        self.assertEquals(self.calculate(180388.0, 26070), 206458.00)

    def test0760(self):
        self.assertEquals(self.calculate(-171152.0, -12962), -184114.00)

    def test0761(self):
        self.assertEquals(self.calculate(146401.0, -21306), 125095.00)

    def test0762(self):
        self.assertEquals(self.calculate(-9697.0, 12644), 2947.00)

    def test0763(self):
        self.assertEquals(self.calculate(-4514.0, -14066), -18580.00)

    def test0764(self):
        self.assertEquals(self.calculate(3963.0, 8703), 12666.00)

    def test0765(self):
        self.assertEquals(self.calculate(128171.0, -7790), 120381.00)

    def test0766(self):
        self.assertEquals(self.calculate(163266.0, -8503), 154763.00)

    def test0767(self):
        self.assertEquals(self.calculate(63994.0, 22942), 86936.00)

    def test0768(self):
        self.assertEquals(self.calculate(153866.0, 5974), 159840.00)

    def test0769(self):
        self.assertEquals(self.calculate(129473.0, -1767), 127706.00)

    def test0770(self):
        self.assertEquals(self.calculate(79894.0, 30375), 110269.00)

    def test0771(self):
        self.assertEquals(self.calculate(-78413.0, 4210), -74203.00)

    def test0772(self):
        self.assertEquals(self.calculate(50251.0, 28364), 78615.00)

    def test0773(self):
        self.assertEquals(self.calculate(-133522.0, 31258), -102264.00)

    def test0774(self):
        self.assertEquals(self.calculate(19393.0, 17200), 36593.00)

    def test0775(self):
        self.assertEquals(self.calculate(168665.0, -26387), 142278.00)

    def test0776(self):
        self.assertEquals(self.calculate(-65428.0, 8914), -56514.00)

    def test0777(self):
        self.assertEquals(self.calculate(42313.0, -23198), 19115.00)

    def test0778(self):
        self.assertEquals(self.calculate(-48904.0, 13224), -35680.00)

    def test0779(self):
        self.assertEquals(self.calculate(-65745.0, 1549), -64196.00)

    def test0780(self):
        self.assertEquals(self.calculate(-3296.0, 6935), 3639.00)

    def test0781(self):
        self.assertEquals(self.calculate(193303.0, 3668), 196971.00)

    def test0782(self):
        self.assertEquals(self.calculate(-90982.0, -17129), -108111.00)

    def test0783(self):
        self.assertEquals(self.calculate(-188359.0, -25042), -213401.00)

    def test0784(self):
        self.assertEquals(self.calculate(-174949.0, 1485), -173464.00)

    def test0785(self):
        self.assertEquals(self.calculate(107801.0, -2503), 105298.00)

    def test0786(self):
        self.assertEquals(self.calculate(182761.0, -13830), 168931.00)

    def test0787(self):
        self.assertEquals(self.calculate(-63282.0, 31785), -31497.00)

    def test0788(self):
        self.assertEquals(self.calculate(67768.0, 31658), 99426.00)

    def test0789(self):
        self.assertEquals(self.calculate(-24156.0, -26960), -51116.00)

    def test0790(self):
        self.assertEquals(self.calculate(20500.0, 11163), 31663.00)

    def test0791(self):
        self.assertEquals(self.calculate(-46552.0, 17877), -28675.00)

    def test0792(self):
        self.assertEquals(self.calculate(42263.0, 27235), 69498.00)

    def test0793(self):
        self.assertEquals(self.calculate(-79688.0, 12795), -66893.00)

    def test0794(self):
        self.assertEquals(self.calculate(108557.0, 30195), 138752.00)

    def test0795(self):
        self.assertEquals(self.calculate(18407.0, -15194), 3213.00)

    def test0796(self):
        self.assertEquals(self.calculate(173188.0, 9386), 182574.00)

    def test0797(self):
        self.assertEquals(self.calculate(-192880.0, -20097), -212977.00)

    def test0798(self):
        self.assertEquals(self.calculate(165131.0, 1910), 167041.00)

    def test0799(self):
        self.assertEquals(self.calculate(-129005.0, 31903), -97102.00)

    def test0800(self):
        self.assertEquals(self.calculate(158079.0, 29480), 187559.00)

    def test0801(self):
        self.assertEquals(self.calculate(4815.0, 3042), 7857.00)

    def test0802(self):
        self.assertEquals(self.calculate(-89082.0, -12948), -102030.00)

    def test0803(self):
        self.assertEquals(self.calculate(188502.0, -32122), 156380.00)

    def test0804(self):
        self.assertEquals(self.calculate(-90712.0, 3342), -87370.00)

    def test0805(self):
        self.assertEquals(self.calculate(-74986.0, -2778), -77764.00)

    def test0806(self):
        self.assertEquals(self.calculate(166933.0, -20719), 146214.00)

    def test0807(self):
        self.assertEquals(self.calculate(180773.0, -23030), 157743.00)

    def test0808(self):
        self.assertEquals(self.calculate(-26563.0, -3393), -29956.00)

    def test0809(self):
        self.assertEquals(self.calculate(139556.0, 12890), 152446.00)

    def test0810(self):
        self.assertEquals(self.calculate(195625.0, -5495), 190130.00)

    def test0811(self):
        self.assertEquals(self.calculate(176311.0, 330), 176641.00)

    def test0812(self):
        self.assertEquals(self.calculate(38142.0, 32410), 70552.00)

    def test0813(self):
        self.assertEquals(self.calculate(-83939.0, 24944), -58995.00)

    def test0814(self):
        self.assertEquals(self.calculate(126239.0, 24470), 150709.00)

    def test0815(self):
        self.assertEquals(self.calculate(73538.0, 3089), 76627.00)

    def test0816(self):
        self.assertEquals(self.calculate(199544.0, -21604), 177940.00)

    def test0817(self):
        self.assertEquals(self.calculate(-193561.0, 17553), -176008.00)

    def test0818(self):
        self.assertEquals(self.calculate(95477.0, 30582), 126059.00)

    def test0819(self):
        self.assertEquals(self.calculate(2426.0, -4461), -2035.00)

    def test0820(self):
        self.assertEquals(self.calculate(15811.0, 22049), 37860.00)

    def test0821(self):
        self.assertEquals(self.calculate(167093.0, 20710), 187803.00)

    def test0822(self):
        self.assertEquals(self.calculate(-105949.0, -27026), -132975.00)

    def test0823(self):
        self.assertEquals(self.calculate(-119774.0, 17372), -102402.00)

    def test0824(self):
        self.assertEquals(self.calculate(171820.0, -230), 171590.00)

    def test0825(self):
        self.assertEquals(self.calculate(161019.0, -12673), 148346.00)

    def test0826(self):
        self.assertEquals(self.calculate(-166169.0, 20799), -145370.00)

    def test0827(self):
        self.assertEquals(self.calculate(-77952.0, 6063), -71889.00)

    def test0828(self):
        self.assertEquals(self.calculate(131354.0, -4552), 126802.00)

    def test0829(self):
        self.assertEquals(self.calculate(-187073.0, 23703), -163370.00)

    def test0830(self):
        self.assertEquals(self.calculate(-101259.0, -2740), -103999.00)

    def test0831(self):
        self.assertEquals(self.calculate(130060.0, -27449), 102611.00)

    def test0832(self):
        self.assertEquals(self.calculate(-89495.0, -4961), -94456.00)

    def test0833(self):
        self.assertEquals(self.calculate(150988.0, -25580), 125408.00)

    def test0834(self):
        self.assertEquals(self.calculate(-109690.0, 15765), -93925.00)

    def test0835(self):
        self.assertEquals(self.calculate(101735.0, -6713), 95022.00)

    def test0836(self):
        self.assertEquals(self.calculate(-60246.0, -4623), -64869.00)

    def test0837(self):
        self.assertEquals(self.calculate(-129912.0, -20595), -150507.00)

    def test0838(self):
        self.assertEquals(self.calculate(113272.0, -17898), 95374.00)

    def test0839(self):
        self.assertEquals(self.calculate(-23038.0, -24317), -47355.00)

    def test0840(self):
        self.assertEquals(self.calculate(-164362.0, 23129), -141233.00)

    def test0841(self):
        self.assertEquals(self.calculate(-102497.0, 16754), -85743.00)

    def test0842(self):
        self.assertEquals(self.calculate(-49087.0, -103), -49190.00)

    def test0843(self):
        self.assertEquals(self.calculate(13833.0, -19897), -6064.00)

    def test0844(self):
        self.assertEquals(self.calculate(-44862.0, 8849), -36013.00)

    def test0845(self):
        self.assertEquals(self.calculate(-7584.0, -6771), -14355.00)

    def test0846(self):
        self.assertEquals(self.calculate(159910.0, 28399), 188309.00)

    def test0847(self):
        self.assertEquals(self.calculate(-44790.0, -21008), -65798.00)

    def test0848(self):
        self.assertEquals(self.calculate(7061.0, 13318), 20379.00)

    def test0849(self):
        self.assertEquals(self.calculate(-154691.0, 30044), -124647.00)

    def test0850(self):
        self.assertEquals(self.calculate(-76056.0, -11269), -87325.00)

    def test0851(self):
        self.assertEquals(self.calculate(73444.0, 27648), 101092.00)

    def test0852(self):
        self.assertEquals(self.calculate(108408.0, -27890), 80518.00)

    def test0853(self):
        self.assertEquals(self.calculate(191569.0, -15934), 175635.00)

    def test0854(self):
        self.assertEquals(self.calculate(28535.0, 27838), 56373.00)

    def test0855(self):
        self.assertEquals(self.calculate(-166928.0, 18627), -148301.00)

    def test0856(self):
        self.assertEquals(self.calculate(-98605.0, -13596), -112201.00)

    def test0857(self):
        self.assertEquals(self.calculate(-65282.0, -28257), -93539.00)

    def test0858(self):
        self.assertEquals(self.calculate(55324.0, 27385), 82709.00)

    def test0859(self):
        self.assertEquals(self.calculate(167021.0, 1304), 168325.00)

    def test0860(self):
        self.assertEquals(self.calculate(-190418.0, 3105), -187313.00)

    def test0861(self):
        self.assertEquals(self.calculate(-5334.0, 3459), -1875.00)

    def test0862(self):
        self.assertEquals(self.calculate(-152256.0, 32431), -119825.00)

    def test0863(self):
        self.assertEquals(self.calculate(-122046.0, 3109), -118937.00)

    def test0864(self):
        self.assertEquals(self.calculate(-159293.0, -21209), -180502.00)

    def test0865(self):
        self.assertEquals(self.calculate(-41714.0, 14860), -26854.00)

    def test0866(self):
        self.assertEquals(self.calculate(-179452.0, -8091), -187543.00)

    def test0867(self):
        self.assertEquals(self.calculate(41958.0, 21207), 63165.00)

    def test0868(self):
        self.assertEquals(self.calculate(-142.0, -30550), -30692.00)

    def test0869(self):
        self.assertEquals(self.calculate(-191241.0, -3574), -194815.00)

    def test0870(self):
        self.assertEquals(self.calculate(12015.0, -13505), -1490.00)

    def test0871(self):
        self.assertEquals(self.calculate(111259.0, -22564), 88695.00)

    def test0872(self):
        self.assertEquals(self.calculate(24021.0, 17395), 41416.00)

    def test0873(self):
        self.assertEquals(self.calculate(43085.0, -342), 42743.00)

    def test0874(self):
        self.assertEquals(self.calculate(19174.0, 20627), 39801.00)

    def test0875(self):
        self.assertEquals(self.calculate(108265.0, -30118), 78147.00)

    def test0876(self):
        self.assertEquals(self.calculate(-164067.0, -17445), -181512.00)

    def test0877(self):
        self.assertEquals(self.calculate(198763.0, 18359), 217122.00)

    def test0878(self):
        self.assertEquals(self.calculate(72923.0, 12545), 85468.00)

    def test0879(self):
        self.assertEquals(self.calculate(-152930.0, 5617), -147313.00)

    def test0880(self):
        self.assertEquals(self.calculate(-180544.0, -17526), -198070.00)

    def test0881(self):
        self.assertEquals(self.calculate(11560.0, 4532), 16092.00)

    def test0882(self):
        self.assertEquals(self.calculate(-186253.0, 22944), -163309.00)

    def test0883(self):
        self.assertEquals(self.calculate(-190218.0, -13604), -203822.00)

    def test0884(self):
        self.assertEquals(self.calculate(-98848.0, -6036), -104884.00)

    def test0885(self):
        self.assertEquals(self.calculate(-195995.0, -21927), -217922.00)

    def test0886(self):
        self.assertEquals(self.calculate(-170400.0, -25178), -195578.00)

    def test0887(self):
        self.assertEquals(self.calculate(-164091.0, 14734), -149357.00)

    def test0888(self):
        self.assertEquals(self.calculate(-12117.0, 10930), -1187.00)

    def test0889(self):
        self.assertEquals(self.calculate(-93241.0, 3706), -89535.00)

    def test0890(self):
        self.assertEquals(self.calculate(-43840.0, 6184), -37656.00)

    def test0891(self):
        self.assertEquals(self.calculate(7232.0, 15778), 23010.00)

    def test0892(self):
        self.assertEquals(self.calculate(186390.0, -17011), 169379.00)

    def test0893(self):
        self.assertEquals(self.calculate(193339.0, 4304), 197643.00)

    def test0894(self):
        self.assertEquals(self.calculate(199334.0, -5630), 193704.00)

    def test0895(self):
        self.assertEquals(self.calculate(-67092.0, -75), -67167.00)

    def test0896(self):
        self.assertEquals(self.calculate(33878.0, 16411), 50289.00)

    def test0897(self):
        self.assertEquals(self.calculate(186114.0, 21829), 207943.00)

    def test0898(self):
        self.assertEquals(self.calculate(104624.0, -19948), 84676.00)

    def test0899(self):
        self.assertEquals(self.calculate(39542.0, -30612), 8930.00)

    def test0900(self):
        self.assertEquals(self.calculate(-20922.0, -25679), -46601.00)

    def test0901(self):
        self.assertEquals(self.calculate(9235.0, 18006), 27241.00)

    def test0902(self):
        self.assertEquals(self.calculate(-58173.0, -927), -59100.00)

    def test0903(self):
        self.assertEquals(self.calculate(-219.0, -12496), -12715.00)

    def test0904(self):
        self.assertEquals(self.calculate(-123282.0, -16471), -139753.00)

    def test0905(self):
        self.assertEquals(self.calculate(74947.0, -18327), 56620.00)

    def test0906(self):
        self.assertEquals(self.calculate(-96316.0, 23407), -72909.00)

    def test0907(self):
        self.assertEquals(self.calculate(83944.0, 26206), 110150.00)

    def test0908(self):
        self.assertEquals(self.calculate(99586.0, 19480), 119066.00)

    def test0909(self):
        self.assertEquals(self.calculate(161134.0, 25884), 187018.00)

    def test0910(self):
        self.assertEquals(self.calculate(77088.0, 634), 77722.00)

    def test0911(self):
        self.assertEquals(self.calculate(185959.0, 1173), 187132.00)

    def test0912(self):
        self.assertEquals(self.calculate(-99978.0, 7128), -92850.00)

    def test0913(self):
        self.assertEquals(self.calculate(-22988.0, 30712), 7724.00)

    def test0914(self):
        self.assertEquals(self.calculate(-135497.0, 2989), -132508.00)

    def test0915(self):
        self.assertEquals(self.calculate(88412.0, 32183), 120595.00)

    def test0916(self):
        self.assertEquals(self.calculate(6230.0, -18571), -12341.00)

    def test0917(self):
        self.assertEquals(self.calculate(-5813.0, -7472), -13285.00)

    def test0918(self):
        self.assertEquals(self.calculate(-103910.0, 347), -103563.00)

    def test0919(self):
        self.assertEquals(self.calculate(197836.0, 31382), 229218.00)

    def test0920(self):
        self.assertEquals(self.calculate(38213.0, 31245), 69458.00)

    def test0921(self):
        self.assertEquals(self.calculate(-89069.0, -29703), -118772.00)

    def test0922(self):
        self.assertEquals(self.calculate(-101561.0, -19833), -121394.00)

    def test0923(self):
        self.assertEquals(self.calculate(176492.0, -12282), 164210.00)

    def test0924(self):
        self.assertEquals(self.calculate(-124376.0, -3052), -127428.00)

    def test0925(self):
        self.assertEquals(self.calculate(60121.0, -22933), 37188.00)

    def test0926(self):
        self.assertEquals(self.calculate(-37443.0, -2223), -39666.00)

    def test0927(self):
        self.assertEquals(self.calculate(97950.0, -6482), 91468.00)

    def test0928(self):
        self.assertEquals(self.calculate(3913.0, 16820), 20733.00)

    def test0929(self):
        self.assertEquals(self.calculate(16667.0, -31630), -14963.00)

    def test0930(self):
        self.assertEquals(self.calculate(-77590.0, -29386), -106976.00)

    def test0931(self):
        self.assertEquals(self.calculate(-169912.0, 15957), -153955.00)

    def test0932(self):
        self.assertEquals(self.calculate(53254.0, 27961), 81215.00)

    def test0933(self):
        self.assertEquals(self.calculate(-59375.0, -6846), -66221.00)

    def test0934(self):
        self.assertEquals(self.calculate(88921.0, -28824), 60097.00)

    def test0935(self):
        self.assertEquals(self.calculate(-181229.0, 28452), -152777.00)

    def test0936(self):
        self.assertEquals(self.calculate(-130283.0, -6163), -136446.00)

    def test0937(self):
        self.assertEquals(self.calculate(-75767.0, 18026), -57741.00)

    def test0938(self):
        self.assertEquals(self.calculate(-106254.0, 14107), -92147.00)

    def test0939(self):
        self.assertEquals(self.calculate(78584.0, 17000), 95584.00)

    def test0940(self):
        self.assertEquals(self.calculate(143390.0, 5638), 149028.00)

    def test0941(self):
        self.assertEquals(self.calculate(-81403.0, 19870), -61533.00)

    def test0942(self):
        self.assertEquals(self.calculate(-30350.0, 24438), -5912.00)

    def test0943(self):
        self.assertEquals(self.calculate(183835.0, -13760), 170075.00)

    def test0944(self):
        self.assertEquals(self.calculate(-21436.0, 23293), 1857.00)

    def test0945(self):
        self.assertEquals(self.calculate(78433.0, 2858), 81291.00)

    def test0946(self):
        self.assertEquals(self.calculate(-164118.0, -20739), -184857.00)

    def test0947(self):
        self.assertEquals(self.calculate(-186169.0, -29638), -215807.00)

    def test0948(self):
        self.assertEquals(self.calculate(170058.0, -8250), 161808.00)

    def test0949(self):
        self.assertEquals(self.calculate(44791.0, 18100), 62891.00)

    def test0950(self):
        self.assertEquals(self.calculate(98939.0, 29229), 128168.00)

    def test0951(self):
        self.assertEquals(self.calculate(-83292.0, -31060), -114352.00)

    def test0952(self):
        self.assertEquals(self.calculate(-153293.0, 5216), -148077.00)

    def test0953(self):
        self.assertEquals(self.calculate(89311.0, 11399), 100710.00)

    def test0954(self):
        self.assertEquals(self.calculate(101270.0, 18983), 120253.00)

    def test0955(self):
        self.assertEquals(self.calculate(139096.0, 15161), 154257.00)

    def test0956(self):
        self.assertEquals(self.calculate(139644.0, -31120), 108524.00)

    def test0957(self):
        self.assertEquals(self.calculate(-39348.0, 16557), -22791.00)

    def test0958(self):
        self.assertEquals(self.calculate(-10537.0, -28310), -38847.00)

    def test0959(self):
        self.assertEquals(self.calculate(69330.0, -30863), 38467.00)

    def test0960(self):
        self.assertEquals(self.calculate(99735.0, 26792), 126527.00)

    def test0961(self):
        self.assertEquals(self.calculate(62295.0, 5583), 67878.00)

    def test0962(self):
        self.assertEquals(self.calculate(71746.0, -21073), 50673.00)

    def test0963(self):
        self.assertEquals(self.calculate(31183.0, -2025), 29158.00)

    def test0964(self):
        self.assertEquals(self.calculate(-170463.0, 24557), -145906.00)

    def test0965(self):
        self.assertEquals(self.calculate(136967.0, -25231), 111736.00)

    def test0966(self):
        self.assertEquals(self.calculate(42855.0, -20812), 22043.00)

    def test0967(self):
        self.assertEquals(self.calculate(-157531.0, -3780), -161311.00)

    def test0968(self):
        self.assertEquals(self.calculate(182719.0, 4468), 187187.00)

    def test0969(self):
        self.assertEquals(self.calculate(-105395.0, 11199), -94196.00)

    def test0970(self):
        self.assertEquals(self.calculate(178509.0, 187), 178696.00)

    def test0971(self):
        self.assertEquals(self.calculate(-18588.0, 27956), 9368.00)

    def test0972(self):
        self.assertEquals(self.calculate(28572.0, 19932), 48504.00)

    def test0973(self):
        self.assertEquals(self.calculate(-142507.0, -19645), -162152.00)

    def test0974(self):
        self.assertEquals(self.calculate(-143373.0, -2331), -145704.00)

    def test0975(self):
        self.assertEquals(self.calculate(-58260.0, -20603), -78863.00)

    def test0976(self):
        self.assertEquals(self.calculate(64147.0, 5518), 69665.00)

    def test0977(self):
        self.assertEquals(self.calculate(-56237.0, -24808), -81045.00)

    def test0978(self):
        self.assertEquals(self.calculate(-140022.0, -2306), -142328.00)

    def test0979(self):
        self.assertEquals(self.calculate(-161120.0, -20742), -181862.00)

    def test0980(self):
        self.assertEquals(self.calculate(-116542.0, 6140), -110402.00)

    def test0981(self):
        self.assertEquals(self.calculate(-82065.0, -6695), -88760.00)

    def test0982(self):
        self.assertEquals(self.calculate(-112396.0, -25954), -138350.00)

    def test0983(self):
        self.assertEquals(self.calculate(34465.0, 5766), 40231.00)

    def test0984(self):
        self.assertEquals(self.calculate(-106523.0, 19609), -86914.00)

    def test0985(self):
        self.assertEquals(self.calculate(95014.0, -17672), 77342.00)

    def test0986(self):
        self.assertEquals(self.calculate(-60137.0, -22662), -82799.00)

    def test0987(self):
        self.assertEquals(self.calculate(184267.0, -16663), 167604.00)

    def test0988(self):
        self.assertEquals(self.calculate(-102198.0, -21765), -123963.00)

    def test0989(self):
        self.assertEquals(self.calculate(-129740.0, -30878), -160618.00)

    def test0990(self):
        self.assertEquals(self.calculate(-112340.0, 8163), -104177.00)

    def test0991(self):
        self.assertEquals(self.calculate(-5014.0, -5787), -10801.00)

    def test0992(self):
        self.assertEquals(self.calculate(2028.0, -8775), -6747.00)

    def test0993(self):
        self.assertEquals(self.calculate(-192585.0, -21492), -214077.00)

    def test0994(self):
        self.assertEquals(self.calculate(115622.0, -26001), 89621.00)

    def test0995(self):
        self.assertEquals(self.calculate(-82424.0, 32365), -50059.00)

    def test0996(self):
        self.assertEquals(self.calculate(-23886.0, 21075), -2811.00)

    def test0997(self):
        self.assertEquals(self.calculate(165978.0, -11113), 154865.00)

    def test0998(self):
        self.assertEquals(self.calculate(-131513.0, -14615), -146128.00)

    def test0999(self):
        self.assertEquals(self.calculate(-164838.0, -17114), -181952.00)

    def test1000(self):
        self.assertEquals(self.calculate(-192571.0, 22082), -170489.00)

    def test1001(self):
        self.assertEquals(self.calculate(29417.0, -2322), 27095.00)

    def test1002(self):
        self.assertEquals(self.calculate(-46453.0, 9431), -37022.00)

    def test1003(self):
        self.assertEquals(self.calculate(33053.0, 30741), 63794.00)

    def test1004(self):
        self.assertEquals(self.calculate(116302.0, 27065), 143367.00)

    def test1005(self):
        self.assertEquals(self.calculate(813.0, 28085), 28898.00)

    def test1006(self):
        self.assertEquals(self.calculate(-151327.0, -27426), -178753.00)

    def test1007(self):
        self.assertEquals(self.calculate(-183486.0, 27184), -156302.00)

    def test1008(self):
        self.assertEquals(self.calculate(-177823.0, -579), -178402.00)

    def test1009(self):
        self.assertEquals(self.calculate(-196365.0, 18749), -177616.00)

    def test1010(self):
        self.assertEquals(self.calculate(-83555.0, 31529), -52026.00)

    def test1011(self):
        self.assertEquals(self.calculate(122023.0, -15255), 106768.00)

    def test1012(self):
        self.assertEquals(self.calculate(182182.0, 31977), 214159.00)

    def test1013(self):
        self.assertEquals(self.calculate(70616.0, -18048), 52568.00)

    def test1014(self):
        self.assertEquals(self.calculate(46703.0, -8018), 38685.00)

    def test1015(self):
        self.assertEquals(self.calculate(-92332.0, 20061), -72271.00)

    def test1016(self):
        self.assertEquals(self.calculate(-88661.0, 4859), -83802.00)

    def test1017(self):
        self.assertEquals(self.calculate(124996.0, 32479), 157475.00)

    def test1018(self):
        self.assertEquals(self.calculate(-184946.0, 18912), -166034.00)

    def test1019(self):
        self.assertEquals(self.calculate(-93720.0, -4576), -98296.00)

    def test1020(self):
        self.assertEquals(self.calculate(-1674.0, -30502), -32176.00)

    def test1021(self):
        self.assertEquals(self.calculate(42238.0, -27035), 15203.00)

    def test1022(self):
        self.assertEquals(self.calculate(48940.0, -17448), 31492.00)

    def test1023(self):
        self.assertEquals(self.calculate(81509.0, -19140), 62369.00)



class TestVM_Add_FloatLong(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_LONG)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushL(rhs)
        v.VM_Add()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(112744.0, -213837052), -213724308.00)

    def test0001(self):
        self.assertEquals(self.calculate(-54387.0, -189123659), -189178046.00)

    def test0002(self):
        self.assertEquals(self.calculate(-109028.0, 801690900), 801581872.00)

    def test0003(self):
        self.assertEquals(self.calculate(184081.0, -861027386), -860843305.00)

    def test0004(self):
        self.assertEquals(self.calculate(-164240.0, 593091556), 592927316.00)

    def test0005(self):
        self.assertEquals(self.calculate(-134416.0, -633401479), -633535895.00)

    def test0006(self):
        self.assertEquals(self.calculate(4478.0, -1313802327), -1313797849.00)

    def test0007(self):
        self.assertEquals(self.calculate(76049.0, 62759195), 62835244.00)

    def test0008(self):
        self.assertEquals(self.calculate(-189578.0, 1824210888), 1824021310.00)

    def test0009(self):
        self.assertEquals(self.calculate(-124719.0, -129456581), -129581300.00)

    def test0010(self):
        self.assertEquals(self.calculate(-119269.0, -1208094299), -1208213568.00)

    def test0011(self):
        self.assertEquals(self.calculate(-28059.0, 713882257), 713854198.00)

    def test0012(self):
        self.assertEquals(self.calculate(-110146.0, -997177070), -997287216.00)

    def test0013(self):
        self.assertEquals(self.calculate(-151834.0, 1872577496), 1872425662.00)

    def test0014(self):
        self.assertEquals(self.calculate(108486.0, 1689250968), 1689359454.00)

    def test0015(self):
        self.assertEquals(self.calculate(37035.0, 1062176641), 1062213676.00)

    def test0016(self):
        self.assertEquals(self.calculate(-58259.0, 858405578), 858347319.00)

    def test0017(self):
        self.assertEquals(self.calculate(-143651.0, -267611361), -267755012.00)

    def test0018(self):
        self.assertEquals(self.calculate(105033.0, -1056817138), -1056712105.00)

    def test0019(self):
        self.assertEquals(self.calculate(189159.0, 909073622), 909262781.00)

    def test0020(self):
        self.assertEquals(self.calculate(-101666.0, -413389980), -413491646.00)

    def test0021(self):
        self.assertEquals(self.calculate(144309.0, 1400220417), 1400364726.00)

    def test0022(self):
        self.assertEquals(self.calculate(24452.0, 1748067975), 1748092427.00)

    def test0023(self):
        self.assertEquals(self.calculate(-18830.0, 1963318202), 1963299372.00)

    def test0024(self):
        self.assertEquals(self.calculate(79048.0, 911098942), 911177990.00)

    def test0025(self):
        self.assertEquals(self.calculate(-17176.0, -342657522), -342674698.00)

    def test0026(self):
        self.assertEquals(self.calculate(13514.0, 144837485), 144850999.00)

    def test0027(self):
        self.assertEquals(self.calculate(-77743.0, 1634002599), 1633924856.00)

    def test0028(self):
        self.assertEquals(self.calculate(-18429.0, 398597452), 398579023.00)

    def test0029(self):
        self.assertEquals(self.calculate(-158081.0, 120900648), 120742567.00)

    def test0030(self):
        self.assertEquals(self.calculate(55726.0, -1783237872), -1783182146.00)

    def test0031(self):
        self.assertEquals(self.calculate(98853.0, 1679108222), 1679207075.00)

    def test0032(self):
        self.assertEquals(self.calculate(-38810.0, -84072678), -84111488.00)

    def test0033(self):
        self.assertEquals(self.calculate(149849.0, -467996756), -467846907.00)

    def test0034(self):
        self.assertEquals(self.calculate(-37382.0, 956241489), 956204107.00)

    def test0035(self):
        self.assertEquals(self.calculate(-28905.0, 1079436303), 1079407398.00)

    def test0036(self):
        self.assertEquals(self.calculate(122423.0, 1142023906), 1142146329.00)

    def test0037(self):
        self.assertEquals(self.calculate(-172575.0, -752224166), -752396741.00)

    def test0038(self):
        self.assertEquals(self.calculate(-154892.0, 165817212), 165662320.00)

    def test0039(self):
        self.assertEquals(self.calculate(-96909.0, -1606063109), -1606160018.00)

    def test0040(self):
        self.assertEquals(self.calculate(32786.0, 1573045498), 1573078284.00)

    def test0041(self):
        self.assertEquals(self.calculate(14791.0, 654813865), 654828656.00)

    def test0042(self):
        self.assertEquals(self.calculate(92147.0, -570183338), -570091191.00)

    def test0043(self):
        self.assertEquals(self.calculate(86102.0, 81028033), 81114135.00)

    def test0044(self):
        self.assertEquals(self.calculate(57150.0, 1141410290), 1141467440.00)

    def test0045(self):
        self.assertEquals(self.calculate(158507.0, -140304570), -140146063.00)

    def test0046(self):
        self.assertEquals(self.calculate(163872.0, 1091326794), 1091490666.00)

    def test0047(self):
        self.assertEquals(self.calculate(-23502.0, -1677611789), -1677635291.00)

    def test0048(self):
        self.assertEquals(self.calculate(-177994.0, 899898239), 899720245.00)

    def test0049(self):
        self.assertEquals(self.calculate(-126606.0, -78984862), -79111468.00)

    def test0050(self):
        self.assertEquals(self.calculate(-117769.0, 1161878284), 1161760515.00)

    def test0051(self):
        self.assertEquals(self.calculate(66932.0, 518075385), 518142317.00)

    def test0052(self):
        self.assertEquals(self.calculate(155421.0, -586532660), -586377239.00)

    def test0053(self):
        self.assertEquals(self.calculate(-51512.0, 168080592), 168029080.00)

    def test0054(self):
        self.assertEquals(self.calculate(88346.0, 936515634), 936603980.00)

    def test0055(self):
        self.assertEquals(self.calculate(192184.0, 602651133), 602843317.00)

    def test0056(self):
        self.assertEquals(self.calculate(42294.0, -1706403257), -1706360963.00)

    def test0057(self):
        self.assertEquals(self.calculate(117675.0, 331593257), 331710932.00)

    def test0058(self):
        self.assertEquals(self.calculate(156646.0, 1585460284), 1585616930.00)

    def test0059(self):
        self.assertEquals(self.calculate(-96063.0, 17248020), 17151957.00)

    def test0060(self):
        self.assertEquals(self.calculate(-109607.0, -1295047031), -1295156638.00)

    def test0061(self):
        self.assertEquals(self.calculate(131199.0, 2121519507), 2121650706.00)

    def test0062(self):
        self.assertEquals(self.calculate(99947.0, -119444197), -119344250.00)

    def test0063(self):
        self.assertEquals(self.calculate(-152409.0, 172464211), 172311802.00)

    def test0064(self):
        self.assertEquals(self.calculate(23509.0, -808156332), -808132823.00)

    def test0065(self):
        self.assertEquals(self.calculate(-87400.0, 689855795), 689768395.00)

    def test0066(self):
        self.assertEquals(self.calculate(-90857.0, 39703751), 39612894.00)

    def test0067(self):
        self.assertEquals(self.calculate(-5086.0, -30508875), -30513961.00)

    def test0068(self):
        self.assertEquals(self.calculate(-191225.0, 742087245), 741896020.00)

    def test0069(self):
        self.assertEquals(self.calculate(-103547.0, -1815170733), -1815274280.00)

    def test0070(self):
        self.assertEquals(self.calculate(5755.0, 36135271), 36141026.00)

    def test0071(self):
        self.assertEquals(self.calculate(-184134.0, 1809654575), 1809470441.00)

    def test0072(self):
        self.assertEquals(self.calculate(-78919.0, -1919449255), -1919528174.00)

    def test0073(self):
        self.assertEquals(self.calculate(-167022.0, 1372734095), 1372567073.00)

    def test0074(self):
        self.assertEquals(self.calculate(-105934.0, -335212826), -335318760.00)

    def test0075(self):
        self.assertEquals(self.calculate(71485.0, -1206388139), -1206316654.00)

    def test0076(self):
        self.assertEquals(self.calculate(-14821.0, -713138532), -713153353.00)

    def test0077(self):
        self.assertEquals(self.calculate(188327.0, 1628027044), 1628215371.00)

    def test0078(self):
        self.assertEquals(self.calculate(-156439.0, -2137445345), -2137601784.00)

    def test0079(self):
        self.assertEquals(self.calculate(-151200.0, -1455750826), -1455902026.00)

    def test0080(self):
        self.assertEquals(self.calculate(-77224.0, -2032509732), -2032586956.00)

    def test0081(self):
        self.assertEquals(self.calculate(-124933.0, -546077323), -546202256.00)

    def test0082(self):
        self.assertEquals(self.calculate(146117.0, -682188980), -682042863.00)

    def test0083(self):
        self.assertEquals(self.calculate(75918.0, 2002190424), 2002266342.00)

    def test0084(self):
        self.assertEquals(self.calculate(-16781.0, 921659220), 921642439.00)

    def test0085(self):
        self.assertEquals(self.calculate(94452.0, 1553504233), 1553598685.00)

    def test0086(self):
        self.assertEquals(self.calculate(76664.0, -3245911), -3169247.00)

    def test0087(self):
        self.assertEquals(self.calculate(-149178.0, 494939429), 494790251.00)

    def test0088(self):
        self.assertEquals(self.calculate(134487.0, 483791874), 483926361.00)

    def test0089(self):
        self.assertEquals(self.calculate(-18017.0, 2130145869), 2130127852.00)

    def test0090(self):
        self.assertEquals(self.calculate(-136400.0, -1798651853), -1798788253.00)

    def test0091(self):
        self.assertEquals(self.calculate(-86198.0, -1902273274), -1902359472.00)

    def test0092(self):
        self.assertEquals(self.calculate(166646.0, 132539129), 132705775.00)

    def test0093(self):
        self.assertEquals(self.calculate(118232.0, -2104879507), -2104761275.00)

    def test0094(self):
        self.assertEquals(self.calculate(-147722.0, -790907173), -791054895.00)

    def test0095(self):
        self.assertEquals(self.calculate(-44041.0, -541525621), -541569662.00)

    def test0096(self):
        self.assertEquals(self.calculate(176038.0, 934087933), 934263971.00)

    def test0097(self):
        self.assertEquals(self.calculate(176522.0, -940454563), -940278041.00)

    def test0098(self):
        self.assertEquals(self.calculate(-105855.0, -1384655180), -1384761035.00)

    def test0099(self):
        self.assertEquals(self.calculate(7645.0, 658424306), 658431951.00)

    def test0100(self):
        self.assertEquals(self.calculate(125997.0, 1249787832), 1249913829.00)

    def test0101(self):
        self.assertEquals(self.calculate(61435.0, 95852688), 95914123.00)

    def test0102(self):
        self.assertEquals(self.calculate(-130026.0, 1639198595), 1639068569.00)

    def test0103(self):
        self.assertEquals(self.calculate(-195945.0, 1732433155), 1732237210.00)

    def test0104(self):
        self.assertEquals(self.calculate(-165697.0, -1766879314), -1767045011.00)

    def test0105(self):
        self.assertEquals(self.calculate(-94722.0, 576025608), 575930886.00)

    def test0106(self):
        self.assertEquals(self.calculate(-153589.0, 1699555769), 1699402180.00)

    def test0107(self):
        self.assertEquals(self.calculate(191317.0, -93573564), -93382247.00)

    def test0108(self):
        self.assertEquals(self.calculate(123284.0, 355622229), 355745513.00)

    def test0109(self):
        self.assertEquals(self.calculate(-60728.0, 100943718), 100882990.00)

    def test0110(self):
        self.assertEquals(self.calculate(98241.0, -1748977956), -1748879715.00)

    def test0111(self):
        self.assertEquals(self.calculate(-1266.0, -711029326), -711030592.00)

    def test0112(self):
        self.assertEquals(self.calculate(87096.0, 639378110), 639465206.00)

    def test0113(self):
        self.assertEquals(self.calculate(-29074.0, 2006202986), 2006173912.00)

    def test0114(self):
        self.assertEquals(self.calculate(110833.0, -384738638), -384627805.00)

    def test0115(self):
        self.assertEquals(self.calculate(-199052.0, -893810396), -894009448.00)

    def test0116(self):
        self.assertEquals(self.calculate(-110399.0, 1984811290), 1984700891.00)

    def test0117(self):
        self.assertEquals(self.calculate(-15496.0, -1702288398), -1702303894.00)

    def test0118(self):
        self.assertEquals(self.calculate(-193081.0, 789859350), 789666269.00)

    def test0119(self):
        self.assertEquals(self.calculate(-180892.0, -839925350), -840106242.00)

    def test0120(self):
        self.assertEquals(self.calculate(-94329.0, 1965005119), 1964910790.00)

    def test0121(self):
        self.assertEquals(self.calculate(25318.0, -1937492447), -1937467129.00)

    def test0122(self):
        self.assertEquals(self.calculate(127124.0, -1380304505), -1380177381.00)

    def test0123(self):
        self.assertEquals(self.calculate(-133232.0, -7182500), -7315732.00)

    def test0124(self):
        self.assertEquals(self.calculate(-24543.0, -701769687), -701794230.00)

    def test0125(self):
        self.assertEquals(self.calculate(103565.0, -1649422813), -1649319248.00)

    def test0126(self):
        self.assertEquals(self.calculate(92727.0, 1723706208), 1723798935.00)

    def test0127(self):
        self.assertEquals(self.calculate(94427.0, -315567682), -315473255.00)

    def test0128(self):
        self.assertEquals(self.calculate(190918.0, 1004116314), 1004307232.00)

    def test0129(self):
        self.assertEquals(self.calculate(34564.0, -544406196), -544371632.00)

    def test0130(self):
        self.assertEquals(self.calculate(61260.0, -1729176723), -1729115463.00)

    def test0131(self):
        self.assertEquals(self.calculate(-102069.0, 471327062), 471224993.00)

    def test0132(self):
        self.assertEquals(self.calculate(55417.0, 1805483320), 1805538737.00)

    def test0133(self):
        self.assertEquals(self.calculate(29488.0, -1716392354), -1716362866.00)

    def test0134(self):
        self.assertEquals(self.calculate(-162335.0, -832479144), -832641479.00)

    def test0135(self):
        self.assertEquals(self.calculate(197408.0, -1989981459), -1989784051.00)

    def test0136(self):
        self.assertEquals(self.calculate(195952.0, 74995183), 75191135.00)

    def test0137(self):
        self.assertEquals(self.calculate(-81240.0, 209932774), 209851534.00)

    def test0138(self):
        self.assertEquals(self.calculate(155934.0, -1656257486), -1656101552.00)

    def test0139(self):
        self.assertEquals(self.calculate(-19812.0, -1854047404), -1854067216.00)

    def test0140(self):
        self.assertEquals(self.calculate(-12908.0, -1903763755), -1903776663.00)

    def test0141(self):
        self.assertEquals(self.calculate(-64786.0, -1119808239), -1119873025.00)

    def test0142(self):
        self.assertEquals(self.calculate(8162.0, 92515645), 92523807.00)

    def test0143(self):
        self.assertEquals(self.calculate(-29069.0, 972437015), 972407946.00)

    def test0144(self):
        self.assertEquals(self.calculate(92776.0, 52238119), 52330895.00)

    def test0145(self):
        self.assertEquals(self.calculate(-126104.0, 1271092134), 1270966030.00)

    def test0146(self):
        self.assertEquals(self.calculate(10920.0, -1084374457), -1084363537.00)

    def test0147(self):
        self.assertEquals(self.calculate(138554.0, 1908859881), 1908998435.00)

    def test0148(self):
        self.assertEquals(self.calculate(-112878.0, -2119493544), -2119606422.00)

    def test0149(self):
        self.assertEquals(self.calculate(-106427.0, 490430630), 490324203.00)

    def test0150(self):
        self.assertEquals(self.calculate(117764.0, 1962624376), 1962742140.00)

    def test0151(self):
        self.assertEquals(self.calculate(-161524.0, 996001109), 995839585.00)

    def test0152(self):
        self.assertEquals(self.calculate(33462.0, 1963822225), 1963855687.00)

    def test0153(self):
        self.assertEquals(self.calculate(44193.0, 896966633), 897010826.00)

    def test0154(self):
        self.assertEquals(self.calculate(-126006.0, 1544946099), 1544820093.00)

    def test0155(self):
        self.assertEquals(self.calculate(-4531.0, -411118545), -411123076.00)

    def test0156(self):
        self.assertEquals(self.calculate(72907.0, 1795271054), 1795343961.00)

    def test0157(self):
        self.assertEquals(self.calculate(87370.0, 1731776041), 1731863411.00)

    def test0158(self):
        self.assertEquals(self.calculate(22233.0, 18832714), 18854947.00)

    def test0159(self):
        self.assertEquals(self.calculate(-143812.0, 2030095350), 2029951538.00)

    def test0160(self):
        self.assertEquals(self.calculate(88024.0, -2104226217), -2104138193.00)

    def test0161(self):
        self.assertEquals(self.calculate(95412.0, -1109447696), -1109352284.00)

    def test0162(self):
        self.assertEquals(self.calculate(-20239.0, 460564351), 460544112.00)

    def test0163(self):
        self.assertEquals(self.calculate(-149704.0, 330149241), 329999537.00)

    def test0164(self):
        self.assertEquals(self.calculate(-118361.0, -328922127), -329040488.00)

    def test0165(self):
        self.assertEquals(self.calculate(91281.0, 851763924), 851855205.00)

    def test0166(self):
        self.assertEquals(self.calculate(74956.0, -628517246), -628442290.00)

    def test0167(self):
        self.assertEquals(self.calculate(192417.0, -226888628), -226696211.00)

    def test0168(self):
        self.assertEquals(self.calculate(73785.0, 918701389), 918775174.00)

    def test0169(self):
        self.assertEquals(self.calculate(88238.0, 2075544703), 2075632941.00)

    def test0170(self):
        self.assertEquals(self.calculate(107196.0, 329366778), 329473974.00)

    def test0171(self):
        self.assertEquals(self.calculate(-84435.0, 328160113), 328075678.00)

    def test0172(self):
        self.assertEquals(self.calculate(147977.0, 1260103144), 1260251121.00)

    def test0173(self):
        self.assertEquals(self.calculate(51327.0, -784039745), -783988418.00)

    def test0174(self):
        self.assertEquals(self.calculate(-2803.0, -1127881299), -1127884102.00)

    def test0175(self):
        self.assertEquals(self.calculate(-107579.0, -1524662506), -1524770085.00)

    def test0176(self):
        self.assertEquals(self.calculate(194632.0, 577306085), 577500717.00)

    def test0177(self):
        self.assertEquals(self.calculate(-30454.0, -577763621), -577794075.00)

    def test0178(self):
        self.assertEquals(self.calculate(-106255.0, 1589101099), 1588994844.00)

    def test0179(self):
        self.assertEquals(self.calculate(176147.0, -270639172), -270463025.00)

    def test0180(self):
        self.assertEquals(self.calculate(-67734.0, -1848065392), -1848133126.00)

    def test0181(self):
        self.assertEquals(self.calculate(-52109.0, 1807206333), 1807154224.00)

    def test0182(self):
        self.assertEquals(self.calculate(13486.0, 462965420), 462978906.00)

    def test0183(self):
        self.assertEquals(self.calculate(41285.0, 1188021294), 1188062579.00)

    def test0184(self):
        self.assertEquals(self.calculate(167183.0, 615399061), 615566244.00)

    def test0185(self):
        self.assertEquals(self.calculate(-65200.0, -970344684), -970409884.00)

    def test0186(self):
        self.assertEquals(self.calculate(8337.0, 821404900), 821413237.00)

    def test0187(self):
        self.assertEquals(self.calculate(-123642.0, -590432759), -590556401.00)

    def test0188(self):
        self.assertEquals(self.calculate(159359.0, -289273827), -289114468.00)

    def test0189(self):
        self.assertEquals(self.calculate(-43718.0, 1154045334), 1154001616.00)

    def test0190(self):
        self.assertEquals(self.calculate(146636.0, -2009699332), -2009552696.00)

    def test0191(self):
        self.assertEquals(self.calculate(61549.0, 1169057547), 1169119096.00)

    def test0192(self):
        self.assertEquals(self.calculate(100595.0, 385094371), 385194966.00)

    def test0193(self):
        self.assertEquals(self.calculate(-153095.0, 1367387840), 1367234745.00)

    def test0194(self):
        self.assertEquals(self.calculate(100729.0, -1939288528), -1939187799.00)

    def test0195(self):
        self.assertEquals(self.calculate(197672.0, -1033482445), -1033284773.00)

    def test0196(self):
        self.assertEquals(self.calculate(-47322.0, 912593611), 912546289.00)

    def test0197(self):
        self.assertEquals(self.calculate(22178.0, -1186290249), -1186268071.00)

    def test0198(self):
        self.assertEquals(self.calculate(-3173.0, 1985635394), 1985632221.00)

    def test0199(self):
        self.assertEquals(self.calculate(-123006.0, 2127294075), 2127171069.00)

    def test0200(self):
        self.assertEquals(self.calculate(-53251.0, 1328469039), 1328415788.00)

    def test0201(self):
        self.assertEquals(self.calculate(155879.0, 1746600608), 1746756487.00)

    def test0202(self):
        self.assertEquals(self.calculate(-66322.0, -1847370160), -1847436482.00)

    def test0203(self):
        self.assertEquals(self.calculate(164890.0, -230225376), -230060486.00)

    def test0204(self):
        self.assertEquals(self.calculate(149511.0, -638938473), -638788962.00)

    def test0205(self):
        self.assertEquals(self.calculate(68816.0, 1451542092), 1451610908.00)

    def test0206(self):
        self.assertEquals(self.calculate(74154.0, 1534456465), 1534530619.00)

    def test0207(self):
        self.assertEquals(self.calculate(-141071.0, -948057646), -948198717.00)

    def test0208(self):
        self.assertEquals(self.calculate(117955.0, -12520413), -12402458.00)

    def test0209(self):
        self.assertEquals(self.calculate(187810.0, -1381559132), -1381371322.00)

    def test0210(self):
        self.assertEquals(self.calculate(148645.0, -198887775), -198739130.00)

    def test0211(self):
        self.assertEquals(self.calculate(-188957.0, 1162262735), 1162073778.00)

    def test0212(self):
        self.assertEquals(self.calculate(133183.0, -96034942), -95901759.00)

    def test0213(self):
        self.assertEquals(self.calculate(151262.0, 1894852244), 1895003506.00)

    def test0214(self):
        self.assertEquals(self.calculate(-28304.0, 23396818), 23368514.00)

    def test0215(self):
        self.assertEquals(self.calculate(26621.0, 159791279), 159817900.00)

    def test0216(self):
        self.assertEquals(self.calculate(91465.0, 1165014510), 1165105975.00)

    def test0217(self):
        self.assertEquals(self.calculate(66968.0, 988784642), 988851610.00)

    def test0218(self):
        self.assertEquals(self.calculate(-111938.0, 1058578040), 1058466102.00)

    def test0219(self):
        self.assertEquals(self.calculate(-175393.0, 412069325), 411893932.00)

    def test0220(self):
        self.assertEquals(self.calculate(-87580.0, -1854954517), -1855042097.00)

    def test0221(self):
        self.assertEquals(self.calculate(190146.0, -201161064), -200970918.00)

    def test0222(self):
        self.assertEquals(self.calculate(-59292.0, 792766009), 792706717.00)

    def test0223(self):
        self.assertEquals(self.calculate(103053.0, -1606703585), -1606600532.00)

    def test0224(self):
        self.assertEquals(self.calculate(-91838.0, 422925079), 422833241.00)

    def test0225(self):
        self.assertEquals(self.calculate(47342.0, 192083465), 192130807.00)

    def test0226(self):
        self.assertEquals(self.calculate(-54318.0, -1713845073), -1713899391.00)

    def test0227(self):
        self.assertEquals(self.calculate(62780.0, 2090857565), 2090920345.00)

    def test0228(self):
        self.assertEquals(self.calculate(-6542.0, -2112300893), -2112307435.00)

    def test0229(self):
        self.assertEquals(self.calculate(86018.0, -195860990), -195774972.00)

    def test0230(self):
        self.assertEquals(self.calculate(-188470.0, 680882281), 680693811.00)

    def test0231(self):
        self.assertEquals(self.calculate(88558.0, 639630012), 639718570.00)

    def test0232(self):
        self.assertEquals(self.calculate(-141742.0, 326925160), 326783418.00)

    def test0233(self):
        self.assertEquals(self.calculate(100500.0, -1370071128), -1369970628.00)

    def test0234(self):
        self.assertEquals(self.calculate(112346.0, -491353936), -491241590.00)

    def test0235(self):
        self.assertEquals(self.calculate(-53666.0, 1405601646), 1405547980.00)

    def test0236(self):
        self.assertEquals(self.calculate(77978.0, -1543240132), -1543162154.00)

    def test0237(self):
        self.assertEquals(self.calculate(-49368.0, 226726290), 226676922.00)

    def test0238(self):
        self.assertEquals(self.calculate(89530.0, 760727815), 760817345.00)

    def test0239(self):
        self.assertEquals(self.calculate(143431.0, -2023339708), -2023196277.00)

    def test0240(self):
        self.assertEquals(self.calculate(5828.0, -802987750), -802981922.00)

    def test0241(self):
        self.assertEquals(self.calculate(172085.0, 251416086), 251588171.00)

    def test0242(self):
        self.assertEquals(self.calculate(55693.0, 1949886063), 1949941756.00)

    def test0243(self):
        self.assertEquals(self.calculate(44104.0, -1675502656), -1675458552.00)

    def test0244(self):
        self.assertEquals(self.calculate(-147329.0, 1621119214), 1620971885.00)

    def test0245(self):
        self.assertEquals(self.calculate(-23233.0, 851558693), 851535460.00)

    def test0246(self):
        self.assertEquals(self.calculate(186778.0, 1396780703), 1396967481.00)

    def test0247(self):
        self.assertEquals(self.calculate(185413.0, 868178366), 868363779.00)

    def test0248(self):
        self.assertEquals(self.calculate(-181478.0, 544443740), 544262262.00)

    def test0249(self):
        self.assertEquals(self.calculate(-105443.0, 321498119), 321392676.00)

    def test0250(self):
        self.assertEquals(self.calculate(46066.0, -16553599), -16507533.00)

    def test0251(self):
        self.assertEquals(self.calculate(-157638.0, 163189364), 163031726.00)

    def test0252(self):
        self.assertEquals(self.calculate(100148.0, -1565494332), -1565394184.00)

    def test0253(self):
        self.assertEquals(self.calculate(-52485.0, 1975244006), 1975191521.00)

    def test0254(self):
        self.assertEquals(self.calculate(-99163.0, 1636614337), 1636515174.00)

    def test0255(self):
        self.assertEquals(self.calculate(107631.0, -2134610597), -2134502966.00)

    def test0256(self):
        self.assertEquals(self.calculate(115802.0, 355158386), 355274188.00)

    def test0257(self):
        self.assertEquals(self.calculate(27873.0, -693814161), -693786288.00)

    def test0258(self):
        self.assertEquals(self.calculate(112555.0, -494922719), -494810164.00)

    def test0259(self):
        self.assertEquals(self.calculate(50866.0, 1704337587), 1704388453.00)

    def test0260(self):
        self.assertEquals(self.calculate(-145665.0, -23853355), -23999020.00)

    def test0261(self):
        self.assertEquals(self.calculate(-60733.0, 944717437), 944656704.00)

    def test0262(self):
        self.assertEquals(self.calculate(-109947.0, -216417825), -216527772.00)

    def test0263(self):
        self.assertEquals(self.calculate(91643.0, -671184305), -671092662.00)

    def test0264(self):
        self.assertEquals(self.calculate(193812.0, 611114974), 611308786.00)

    def test0265(self):
        self.assertEquals(self.calculate(61227.0, 647191493), 647252720.00)

    def test0266(self):
        self.assertEquals(self.calculate(-168437.0, -1489431220), -1489599657.00)

    def test0267(self):
        self.assertEquals(self.calculate(176812.0, 60252410), 60429222.00)

    def test0268(self):
        self.assertEquals(self.calculate(195842.0, -61487022), -61291180.00)

    def test0269(self):
        self.assertEquals(self.calculate(110638.0, -532539271), -532428633.00)

    def test0270(self):
        self.assertEquals(self.calculate(565.0, 1447289490), 1447290055.00)

    def test0271(self):
        self.assertEquals(self.calculate(37292.0, 1485153681), 1485190973.00)

    def test0272(self):
        self.assertEquals(self.calculate(132016.0, -1189529412), -1189397396.00)

    def test0273(self):
        self.assertEquals(self.calculate(-3997.0, -889902247), -889906244.00)

    def test0274(self):
        self.assertEquals(self.calculate(-184852.0, 407656293), 407471441.00)

    def test0275(self):
        self.assertEquals(self.calculate(-16026.0, 487111990), 487095964.00)

    def test0276(self):
        self.assertEquals(self.calculate(-195178.0, -1071194326), -1071389504.00)

    def test0277(self):
        self.assertEquals(self.calculate(-23014.0, 1143317553), 1143294539.00)

    def test0278(self):
        self.assertEquals(self.calculate(-76919.0, -1107723420), -1107800339.00)

    def test0279(self):
        self.assertEquals(self.calculate(-10497.0, 741616712), 741606215.00)

    def test0280(self):
        self.assertEquals(self.calculate(-39351.0, -1396102210), -1396141561.00)

    def test0281(self):
        self.assertEquals(self.calculate(-16960.0, -642143809), -642160769.00)

    def test0282(self):
        self.assertEquals(self.calculate(-195225.0, 1378070490), 1377875265.00)

    def test0283(self):
        self.assertEquals(self.calculate(156006.0, -1565635213), -1565479207.00)

    def test0284(self):
        self.assertEquals(self.calculate(96410.0, -2110373240), -2110276830.00)

    def test0285(self):
        self.assertEquals(self.calculate(152029.0, 826185116), 826337145.00)

    def test0286(self):
        self.assertEquals(self.calculate(-188627.0, -1059738446), -1059927073.00)

    def test0287(self):
        self.assertEquals(self.calculate(75712.0, 1035010122), 1035085834.00)

    def test0288(self):
        self.assertEquals(self.calculate(-3052.0, 1502412898), 1502409846.00)

    def test0289(self):
        self.assertEquals(self.calculate(25675.0, -1090504516), -1090478841.00)

    def test0290(self):
        self.assertEquals(self.calculate(156051.0, 351451934), 351607985.00)

    def test0291(self):
        self.assertEquals(self.calculate(40466.0, -445903109), -445862643.00)

    def test0292(self):
        self.assertEquals(self.calculate(15699.0, 600985608), 601001307.00)

    def test0293(self):
        self.assertEquals(self.calculate(-2480.0, -983270760), -983273240.00)

    def test0294(self):
        self.assertEquals(self.calculate(136865.0, 1529058112), 1529194977.00)

    def test0295(self):
        self.assertEquals(self.calculate(167277.0, 671671926), 671839203.00)

    def test0296(self):
        self.assertEquals(self.calculate(-198308.0, -954896132), -955094440.00)

    def test0297(self):
        self.assertEquals(self.calculate(-143736.0, 583572627), 583428891.00)

    def test0298(self):
        self.assertEquals(self.calculate(49307.0, 1965341870), 1965391177.00)

    def test0299(self):
        self.assertEquals(self.calculate(-22218.0, -94572566), -94594784.00)

    def test0300(self):
        self.assertEquals(self.calculate(-189049.0, 513415948), 513226899.00)

    def test0301(self):
        self.assertEquals(self.calculate(94268.0, -345118217), -345023949.00)

    def test0302(self):
        self.assertEquals(self.calculate(51446.0, -687812174), -687760728.00)

    def test0303(self):
        self.assertEquals(self.calculate(152198.0, 54721014), 54873212.00)

    def test0304(self):
        self.assertEquals(self.calculate(146286.0, -931977429), -931831143.00)

    def test0305(self):
        self.assertEquals(self.calculate(186268.0, -2065522046), -2065335778.00)

    def test0306(self):
        self.assertEquals(self.calculate(-115693.0, 1307278999), 1307163306.00)

    def test0307(self):
        self.assertEquals(self.calculate(80014.0, 1838725013), 1838805027.00)

    def test0308(self):
        self.assertEquals(self.calculate(-92023.0, 955037572), 954945549.00)

    def test0309(self):
        self.assertEquals(self.calculate(-114591.0, 1057730607), 1057616016.00)

    def test0310(self):
        self.assertEquals(self.calculate(-120001.0, -156106884), -156226885.00)

    def test0311(self):
        self.assertEquals(self.calculate(5479.0, -1539134361), -1539128882.00)

    def test0312(self):
        self.assertEquals(self.calculate(-157070.0, 933322599), 933165529.00)

    def test0313(self):
        self.assertEquals(self.calculate(155509.0, 652728931), 652884440.00)

    def test0314(self):
        self.assertEquals(self.calculate(147849.0, -770558105), -770410256.00)

    def test0315(self):
        self.assertEquals(self.calculate(85444.0, 989435807), 989521251.00)

    def test0316(self):
        self.assertEquals(self.calculate(-120346.0, 1118749720), 1118629374.00)

    def test0317(self):
        self.assertEquals(self.calculate(-141203.0, 485252343), 485111140.00)

    def test0318(self):
        self.assertEquals(self.calculate(26451.0, 804635971), 804662422.00)

    def test0319(self):
        self.assertEquals(self.calculate(-113858.0, 1037549729), 1037435871.00)

    def test0320(self):
        self.assertEquals(self.calculate(-8927.0, -633375182), -633384109.00)

    def test0321(self):
        self.assertEquals(self.calculate(-1835.0, 1623024830), 1623022995.00)

    def test0322(self):
        self.assertEquals(self.calculate(37608.0, -1884356869), -1884319261.00)

    def test0323(self):
        self.assertEquals(self.calculate(-196418.0, 1324933966), 1324737548.00)

    def test0324(self):
        self.assertEquals(self.calculate(128775.0, 1057321514), 1057450289.00)

    def test0325(self):
        self.assertEquals(self.calculate(136631.0, -1998015043), -1997878412.00)

    def test0326(self):
        self.assertEquals(self.calculate(47604.0, 2078239291), 2078286895.00)

    def test0327(self):
        self.assertEquals(self.calculate(-190545.0, 1550694550), 1550504005.00)

    def test0328(self):
        self.assertEquals(self.calculate(69818.0, -551115561), -551045743.00)

    def test0329(self):
        self.assertEquals(self.calculate(174768.0, -1933447113), -1933272345.00)

    def test0330(self):
        self.assertEquals(self.calculate(34102.0, -638600208), -638566106.00)

    def test0331(self):
        self.assertEquals(self.calculate(-4962.0, -252608327), -252613289.00)

    def test0332(self):
        self.assertEquals(self.calculate(48721.0, -1576345751), -1576297030.00)

    def test0333(self):
        self.assertEquals(self.calculate(167673.0, 1653909380), 1654077053.00)

    def test0334(self):
        self.assertEquals(self.calculate(100134.0, 1411249694), 1411349828.00)

    def test0335(self):
        self.assertEquals(self.calculate(-133005.0, 1132743624), 1132610619.00)

    def test0336(self):
        self.assertEquals(self.calculate(79151.0, -2031395106), -2031315955.00)

    def test0337(self):
        self.assertEquals(self.calculate(52577.0, 673315513), 673368090.00)

    def test0338(self):
        self.assertEquals(self.calculate(197648.0, 79005535), 79203183.00)

    def test0339(self):
        self.assertEquals(self.calculate(188888.0, -1802220588), -1802031700.00)

    def test0340(self):
        self.assertEquals(self.calculate(-68918.0, 97789968), 97721050.00)

    def test0341(self):
        self.assertEquals(self.calculate(-135769.0, 1642035727), 1641899958.00)

    def test0342(self):
        self.assertEquals(self.calculate(109329.0, -398107412), -397998083.00)

    def test0343(self):
        self.assertEquals(self.calculate(199749.0, -884018954), -883819205.00)

    def test0344(self):
        self.assertEquals(self.calculate(-117268.0, -1194467821), -1194585089.00)

    def test0345(self):
        self.assertEquals(self.calculate(-149128.0, -618246940), -618396068.00)

    def test0346(self):
        self.assertEquals(self.calculate(160036.0, -2140547097), -2140387061.00)

    def test0347(self):
        self.assertEquals(self.calculate(149389.0, -762818433), -762669044.00)

    def test0348(self):
        self.assertEquals(self.calculate(-144570.0, -1214553824), -1214698394.00)

    def test0349(self):
        self.assertEquals(self.calculate(49352.0, -1262113467), -1262064115.00)

    def test0350(self):
        self.assertEquals(self.calculate(166897.0, 1951110557), 1951277454.00)

    def test0351(self):
        self.assertEquals(self.calculate(-124756.0, 1937364357), 1937239601.00)

    def test0352(self):
        self.assertEquals(self.calculate(124142.0, -23034352), -22910210.00)

    def test0353(self):
        self.assertEquals(self.calculate(-177905.0, 206821908), 206644003.00)

    def test0354(self):
        self.assertEquals(self.calculate(-193733.0, 430993074), 430799341.00)

    def test0355(self):
        self.assertEquals(self.calculate(-59452.0, -416074571), -416134023.00)

    def test0356(self):
        self.assertEquals(self.calculate(111681.0, -1742269281), -1742157600.00)

    def test0357(self):
        self.assertEquals(self.calculate(-145685.0, 1594949331), 1594803646.00)

    def test0358(self):
        self.assertEquals(self.calculate(-2558.0, -1450542451), -1450545009.00)

    def test0359(self):
        self.assertEquals(self.calculate(196648.0, 342283835), 342480483.00)

    def test0360(self):
        self.assertEquals(self.calculate(-67430.0, 1604811273), 1604743843.00)

    def test0361(self):
        self.assertEquals(self.calculate(165528.0, -1304472378), -1304306850.00)

    def test0362(self):
        self.assertEquals(self.calculate(119930.0, -642111825), -641991895.00)

    def test0363(self):
        self.assertEquals(self.calculate(-179562.0, -1298991120), -1299170682.00)

    def test0364(self):
        self.assertEquals(self.calculate(26521.0, 763149520), 763176041.00)

    def test0365(self):
        self.assertEquals(self.calculate(107909.0, -1076184343), -1076076434.00)

    def test0366(self):
        self.assertEquals(self.calculate(135568.0, 1629637553), 1629773121.00)

    def test0367(self):
        self.assertEquals(self.calculate(645.0, -1441655701), -1441655056.00)

    def test0368(self):
        self.assertEquals(self.calculate(-38032.0, -667912739), -667950771.00)

    def test0369(self):
        self.assertEquals(self.calculate(-106500.0, 1085584487), 1085477987.00)

    def test0370(self):
        self.assertEquals(self.calculate(26799.0, -1998340246), -1998313447.00)

    def test0371(self):
        self.assertEquals(self.calculate(61959.0, 1329348631), 1329410590.00)

    def test0372(self):
        self.assertEquals(self.calculate(34523.0, 1986696708), 1986731231.00)

    def test0373(self):
        self.assertEquals(self.calculate(147952.0, 783094248), 783242200.00)

    def test0374(self):
        self.assertEquals(self.calculate(-128230.0, 1400424641), 1400296411.00)

    def test0375(self):
        self.assertEquals(self.calculate(25971.0, -1202988846), -1202962875.00)

    def test0376(self):
        self.assertEquals(self.calculate(189681.0, 1656726950), 1656916631.00)

    def test0377(self):
        self.assertEquals(self.calculate(131717.0, -142726964), -142595247.00)

    def test0378(self):
        self.assertEquals(self.calculate(-198590.0, 1360162285), 1359963695.00)

    def test0379(self):
        self.assertEquals(self.calculate(-78346.0, -1612443337), -1612521683.00)

    def test0380(self):
        self.assertEquals(self.calculate(150654.0, 1970542780), 1970693434.00)

    def test0381(self):
        self.assertEquals(self.calculate(-169012.0, -695833838), -696002850.00)

    def test0382(self):
        self.assertEquals(self.calculate(50414.0, 331815676), 331866090.00)

    def test0383(self):
        self.assertEquals(self.calculate(154082.0, 1159320471), 1159474553.00)

    def test0384(self):
        self.assertEquals(self.calculate(-71226.0, -134858705), -134929931.00)

    def test0385(self):
        self.assertEquals(self.calculate(92988.0, -1310029645), -1309936657.00)

    def test0386(self):
        self.assertEquals(self.calculate(-198336.0, 1579501536), 1579303200.00)

    def test0387(self):
        self.assertEquals(self.calculate(36481.0, 382849434), 382885915.00)

    def test0388(self):
        self.assertEquals(self.calculate(-936.0, -1376626958), -1376627894.00)

    def test0389(self):
        self.assertEquals(self.calculate(53177.0, -1561140396), -1561087219.00)

    def test0390(self):
        self.assertEquals(self.calculate(-79326.0, 591615955), 591536629.00)

    def test0391(self):
        self.assertEquals(self.calculate(-55599.0, 922547566), 922491967.00)

    def test0392(self):
        self.assertEquals(self.calculate(20028.0, -2021626165), -2021606137.00)

    def test0393(self):
        self.assertEquals(self.calculate(-185973.0, 1323609402), 1323423429.00)

    def test0394(self):
        self.assertEquals(self.calculate(-123099.0, -1753745973), -1753869072.00)

    def test0395(self):
        self.assertEquals(self.calculate(-34753.0, -769876529), -769911282.00)

    def test0396(self):
        self.assertEquals(self.calculate(-22897.0, -1189471656), -1189494553.00)

    def test0397(self):
        self.assertEquals(self.calculate(-42917.0, 814935766), 814892849.00)

    def test0398(self):
        self.assertEquals(self.calculate(74360.0, 2009047758), 2009122118.00)

    def test0399(self):
        self.assertEquals(self.calculate(140296.0, -346632671), -346492375.00)

    def test0400(self):
        self.assertEquals(self.calculate(-128438.0, -669977725), -670106163.00)

    def test0401(self):
        self.assertEquals(self.calculate(147734.0, -545379998), -545232264.00)

    def test0402(self):
        self.assertEquals(self.calculate(7590.0, -507258638), -507251048.00)

    def test0403(self):
        self.assertEquals(self.calculate(-13370.0, -1917466070), -1917479440.00)

    def test0404(self):
        self.assertEquals(self.calculate(-109557.0, 1714598211), 1714488654.00)

    def test0405(self):
        self.assertEquals(self.calculate(55344.0, 2019513206), 2019568550.00)

    def test0406(self):
        self.assertEquals(self.calculate(-132362.0, 350961466), 350829104.00)

    def test0407(self):
        self.assertEquals(self.calculate(-23030.0, 314808035), 314785005.00)

    def test0408(self):
        self.assertEquals(self.calculate(-169445.0, -685040535), -685209980.00)

    def test0409(self):
        self.assertEquals(self.calculate(-192861.0, -625197342), -625390203.00)

    def test0410(self):
        self.assertEquals(self.calculate(33620.0, 710477716), 710511336.00)

    def test0411(self):
        self.assertEquals(self.calculate(-89078.0, -372245936), -372335014.00)

    def test0412(self):
        self.assertEquals(self.calculate(11352.0, 493854963), 493866315.00)

    def test0413(self):
        self.assertEquals(self.calculate(-93538.0, 675974667), 675881129.00)

    def test0414(self):
        self.assertEquals(self.calculate(-134877.0, -257319843), -257454720.00)

    def test0415(self):
        self.assertEquals(self.calculate(-146647.0, -1322318142), -1322464789.00)

    def test0416(self):
        self.assertEquals(self.calculate(-169841.0, 1253947301), 1253777460.00)

    def test0417(self):
        self.assertEquals(self.calculate(-37457.0, 456968632), 456931175.00)

    def test0418(self):
        self.assertEquals(self.calculate(-183122.0, 1411692952), 1411509830.00)

    def test0419(self):
        self.assertEquals(self.calculate(90643.0, 1804494328), 1804584971.00)

    def test0420(self):
        self.assertEquals(self.calculate(116874.0, -127865361), -127748487.00)

    def test0421(self):
        self.assertEquals(self.calculate(-48160.0, -779257779), -779305939.00)

    def test0422(self):
        self.assertEquals(self.calculate(-198263.0, 413305150), 413106887.00)

    def test0423(self):
        self.assertEquals(self.calculate(106760.0, 796101521), 796208281.00)

    def test0424(self):
        self.assertEquals(self.calculate(-69900.0, -705586453), -705656353.00)

    def test0425(self):
        self.assertEquals(self.calculate(-129837.0, -1633932056), -1634061893.00)

    def test0426(self):
        self.assertEquals(self.calculate(-95353.0, 73887153), 73791800.00)

    def test0427(self):
        self.assertEquals(self.calculate(-176759.0, -301588984), -301765743.00)

    def test0428(self):
        self.assertEquals(self.calculate(-193546.0, 451490371), 451296825.00)

    def test0429(self):
        self.assertEquals(self.calculate(11978.0, -936785976), -936773998.00)

    def test0430(self):
        self.assertEquals(self.calculate(112791.0, 1589365161), 1589477952.00)

    def test0431(self):
        self.assertEquals(self.calculate(81634.0, -735400074), -735318440.00)

    def test0432(self):
        self.assertEquals(self.calculate(-99031.0, -2119393359), -2119492390.00)

    def test0433(self):
        self.assertEquals(self.calculate(-98934.0, 1867031850), 1866932916.00)

    def test0434(self):
        self.assertEquals(self.calculate(24222.0, -478666567), -478642345.00)

    def test0435(self):
        self.assertEquals(self.calculate(93282.0, 1071829281), 1071922563.00)

    def test0436(self):
        self.assertEquals(self.calculate(186291.0, 1644907755), 1645094046.00)

    def test0437(self):
        self.assertEquals(self.calculate(-109631.0, 1893308537), 1893198906.00)

    def test0438(self):
        self.assertEquals(self.calculate(63994.0, 217484427), 217548421.00)

    def test0439(self):
        self.assertEquals(self.calculate(-30116.0, 959038971), 959008855.00)

    def test0440(self):
        self.assertEquals(self.calculate(-188737.0, -2092340249), -2092528986.00)

    def test0441(self):
        self.assertEquals(self.calculate(14683.0, -1091281656), -1091266973.00)

    def test0442(self):
        self.assertEquals(self.calculate(-58380.0, 755076582), 755018202.00)

    def test0443(self):
        self.assertEquals(self.calculate(153477.0, 1438651019), 1438804496.00)

    def test0444(self):
        self.assertEquals(self.calculate(30881.0, 98611614), 98642495.00)

    def test0445(self):
        self.assertEquals(self.calculate(-24634.0, 306023034), 305998400.00)

    def test0446(self):
        self.assertEquals(self.calculate(56492.0, -596549562), -596493070.00)

    def test0447(self):
        self.assertEquals(self.calculate(-48659.0, -4860911), -4909570.00)

    def test0448(self):
        self.assertEquals(self.calculate(-128907.0, -79440945), -79569852.00)

    def test0449(self):
        self.assertEquals(self.calculate(90014.0, 1586296876), 1586386890.00)

    def test0450(self):
        self.assertEquals(self.calculate(21609.0, 91849916), 91871525.00)

    def test0451(self):
        self.assertEquals(self.calculate(-14906.0, -13883594), -13898500.00)

    def test0452(self):
        self.assertEquals(self.calculate(-164510.0, -1360710693), -1360875203.00)

    def test0453(self):
        self.assertEquals(self.calculate(28516.0, -16987857), -16959341.00)

    def test0454(self):
        self.assertEquals(self.calculate(-108160.0, -237949985), -238058145.00)

    def test0455(self):
        self.assertEquals(self.calculate(65738.0, 1440860414), 1440926152.00)

    def test0456(self):
        self.assertEquals(self.calculate(-84534.0, 104317603), 104233069.00)

    def test0457(self):
        self.assertEquals(self.calculate(-75755.0, -2072880824), -2072956579.00)

    def test0458(self):
        self.assertEquals(self.calculate(-22419.0, 1031075260), 1031052841.00)

    def test0459(self):
        self.assertEquals(self.calculate(13974.0, -1797975101), -1797961127.00)

    def test0460(self):
        self.assertEquals(self.calculate(-23808.0, -104516326), -104540134.00)

    def test0461(self):
        self.assertEquals(self.calculate(-27422.0, 1609315914), 1609288492.00)

    def test0462(self):
        self.assertEquals(self.calculate(173388.0, 1520033523), 1520206911.00)

    def test0463(self):
        self.assertEquals(self.calculate(44547.0, -1322738773), -1322694226.00)

    def test0464(self):
        self.assertEquals(self.calculate(106402.0, 843593750), 843700152.00)

    def test0465(self):
        self.assertEquals(self.calculate(-184430.0, -1161306265), -1161490695.00)

    def test0466(self):
        self.assertEquals(self.calculate(39272.0, 1934385563), 1934424835.00)

    def test0467(self):
        self.assertEquals(self.calculate(-13489.0, -214512131), -214525620.00)

    def test0468(self):
        self.assertEquals(self.calculate(88768.0, 180513421), 180602189.00)

    def test0469(self):
        self.assertEquals(self.calculate(131253.0, 1269378425), 1269509678.00)

    def test0470(self):
        self.assertEquals(self.calculate(-22128.0, 926403463), 926381335.00)

    def test0471(self):
        self.assertEquals(self.calculate(-184510.0, 210038724), 209854214.00)

    def test0472(self):
        self.assertEquals(self.calculate(169786.0, 1499477326), 1499647112.00)

    def test0473(self):
        self.assertEquals(self.calculate(-15078.0, -543844301), -543859379.00)

    def test0474(self):
        self.assertEquals(self.calculate(41472.0, -1897585942), -1897544470.00)

    def test0475(self):
        self.assertEquals(self.calculate(15872.0, 688920039), 688935911.00)

    def test0476(self):
        self.assertEquals(self.calculate(-37734.0, 391456538), 391418804.00)

    def test0477(self):
        self.assertEquals(self.calculate(-87169.0, 1363328737), 1363241568.00)

    def test0478(self):
        self.assertEquals(self.calculate(150981.0, 1461669272), 1461820253.00)

    def test0479(self):
        self.assertEquals(self.calculate(-72092.0, -1323805008), -1323877100.00)

    def test0480(self):
        self.assertEquals(self.calculate(155820.0, 702607136), 702762956.00)

    def test0481(self):
        self.assertEquals(self.calculate(-88549.0, -1507099079), -1507187628.00)

    def test0482(self):
        self.assertEquals(self.calculate(-90231.0, 481492563), 481402332.00)

    def test0483(self):
        self.assertEquals(self.calculate(181007.0, 2103081580), 2103262587.00)

    def test0484(self):
        self.assertEquals(self.calculate(87707.0, 195653422), 195741129.00)

    def test0485(self):
        self.assertEquals(self.calculate(-172656.0, 845974975), 845802319.00)

    def test0486(self):
        self.assertEquals(self.calculate(189100.0, -1753714907), -1753525807.00)

    def test0487(self):
        self.assertEquals(self.calculate(99597.0, 80401071), 80500668.00)

    def test0488(self):
        self.assertEquals(self.calculate(-164400.0, -720728540), -720892940.00)

    def test0489(self):
        self.assertEquals(self.calculate(-56786.0, -1481663017), -1481719803.00)

    def test0490(self):
        self.assertEquals(self.calculate(127510.0, -660486672), -660359162.00)

    def test0491(self):
        self.assertEquals(self.calculate(-171654.0, -1521994347), -1522166001.00)

    def test0492(self):
        self.assertEquals(self.calculate(-180181.0, 1578712594), 1578532413.00)

    def test0493(self):
        self.assertEquals(self.calculate(80560.0, -2046435134), -2046354574.00)

    def test0494(self):
        self.assertEquals(self.calculate(-142445.0, 803589045), 803446600.00)

    def test0495(self):
        self.assertEquals(self.calculate(-179385.0, 1491380698), 1491201313.00)

    def test0496(self):
        self.assertEquals(self.calculate(84508.0, 2133448916), 2133533424.00)

    def test0497(self):
        self.assertEquals(self.calculate(81225.0, -34568613), -34487388.00)

    def test0498(self):
        self.assertEquals(self.calculate(189041.0, -1786549250), -1786360209.00)

    def test0499(self):
        self.assertEquals(self.calculate(142335.0, 1638242570), 1638384905.00)

    def test0500(self):
        self.assertEquals(self.calculate(-41399.0, 1999353609), 1999312210.00)

    def test0501(self):
        self.assertEquals(self.calculate(28653.0, -1789277643), -1789248990.00)

    def test0502(self):
        self.assertEquals(self.calculate(-76584.0, 1061329417), 1061252833.00)

    def test0503(self):
        self.assertEquals(self.calculate(-96104.0, 1441696454), 1441600350.00)

    def test0504(self):
        self.assertEquals(self.calculate(-84993.0, 411434808), 411349815.00)

    def test0505(self):
        self.assertEquals(self.calculate(68236.0, 2103194631), 2103262867.00)

    def test0506(self):
        self.assertEquals(self.calculate(-70041.0, 981922610), 981852569.00)

    def test0507(self):
        self.assertEquals(self.calculate(16831.0, -1838499617), -1838482786.00)

    def test0508(self):
        self.assertEquals(self.calculate(110237.0, -1758113858), -1758003621.00)

    def test0509(self):
        self.assertEquals(self.calculate(38452.0, 575663686), 575702138.00)

    def test0510(self):
        self.assertEquals(self.calculate(185935.0, -1247995441), -1247809506.00)

    def test0511(self):
        self.assertEquals(self.calculate(-49792.0, -1503160974), -1503210766.00)

    def test0512(self):
        self.assertEquals(self.calculate(14282.0, 1644680421), 1644694703.00)

    def test0513(self):
        self.assertEquals(self.calculate(-198705.0, -184743676), -184942381.00)

    def test0514(self):
        self.assertEquals(self.calculate(41981.0, -1502864198), -1502822217.00)

    def test0515(self):
        self.assertEquals(self.calculate(62420.0, -1954108754), -1954046334.00)

    def test0516(self):
        self.assertEquals(self.calculate(168884.0, -268604413), -268435529.00)

    def test0517(self):
        self.assertEquals(self.calculate(198240.0, 1388340874), 1388539114.00)

    def test0518(self):
        self.assertEquals(self.calculate(25102.0, 1875416229), 1875441331.00)

    def test0519(self):
        self.assertEquals(self.calculate(-115356.0, -265210887), -265326243.00)

    def test0520(self):
        self.assertEquals(self.calculate(-75308.0, 829740000), 829664692.00)

    def test0521(self):
        self.assertEquals(self.calculate(-83194.0, -1885984558), -1886067752.00)

    def test0522(self):
        self.assertEquals(self.calculate(-70357.0, 2055539680), 2055469323.00)

    def test0523(self):
        self.assertEquals(self.calculate(-66344.0, 2124269056), 2124202712.00)

    def test0524(self):
        self.assertEquals(self.calculate(-87987.0, -397004596), -397092583.00)

    def test0525(self):
        self.assertEquals(self.calculate(-87849.0, -362761434), -362849283.00)

    def test0526(self):
        self.assertEquals(self.calculate(-29402.0, 1342774889), 1342745487.00)

    def test0527(self):
        self.assertEquals(self.calculate(-112749.0, -1318085958), -1318198707.00)

    def test0528(self):
        self.assertEquals(self.calculate(78125.0, 2097576764), 2097654889.00)

    def test0529(self):
        self.assertEquals(self.calculate(159327.0, 598985162), 599144489.00)

    def test0530(self):
        self.assertEquals(self.calculate(74071.0, 1208060021), 1208134092.00)

    def test0531(self):
        self.assertEquals(self.calculate(91978.0, 831919743), 832011721.00)

    def test0532(self):
        self.assertEquals(self.calculate(67151.0, -1507537624), -1507470473.00)

    def test0533(self):
        self.assertEquals(self.calculate(157054.0, 1221430236), 1221587290.00)

    def test0534(self):
        self.assertEquals(self.calculate(-84807.0, 526251002), 526166195.00)

    def test0535(self):
        self.assertEquals(self.calculate(-24467.0, 339186275), 339161808.00)

    def test0536(self):
        self.assertEquals(self.calculate(185737.0, 1302396615), 1302582352.00)

    def test0537(self):
        self.assertEquals(self.calculate(92872.0, -625437527), -625344655.00)

    def test0538(self):
        self.assertEquals(self.calculate(-183718.0, -1217869174), -1218052892.00)

    def test0539(self):
        self.assertEquals(self.calculate(28512.0, -606755166), -606726654.00)

    def test0540(self):
        self.assertEquals(self.calculate(-185033.0, 2108242587), 2108057554.00)

    def test0541(self):
        self.assertEquals(self.calculate(-179166.0, -2052628685), -2052807851.00)

    def test0542(self):
        self.assertEquals(self.calculate(-4111.0, 1949931371), 1949927260.00)

    def test0543(self):
        self.assertEquals(self.calculate(61953.0, -541328502), -541266549.00)

    def test0544(self):
        self.assertEquals(self.calculate(-28721.0, -679533263), -679561984.00)

    def test0545(self):
        self.assertEquals(self.calculate(127283.0, 218111523), 218238806.00)

    def test0546(self):
        self.assertEquals(self.calculate(92986.0, -203246377), -203153391.00)

    def test0547(self):
        self.assertEquals(self.calculate(-123095.0, 297872808), 297749713.00)

    def test0548(self):
        self.assertEquals(self.calculate(42337.0, -987780343), -987738006.00)

    def test0549(self):
        self.assertEquals(self.calculate(-77344.0, -1488308844), -1488386188.00)

    def test0550(self):
        self.assertEquals(self.calculate(-69413.0, -426884432), -426953845.00)

    def test0551(self):
        self.assertEquals(self.calculate(-116061.0, -665807903), -665923964.00)

    def test0552(self):
        self.assertEquals(self.calculate(-164219.0, 147561776), 147397557.00)

    def test0553(self):
        self.assertEquals(self.calculate(11898.0, 1511829141), 1511841039.00)

    def test0554(self):
        self.assertEquals(self.calculate(-112436.0, -850928818), -851041254.00)

    def test0555(self):
        self.assertEquals(self.calculate(-157888.0, 46780675), 46622787.00)

    def test0556(self):
        self.assertEquals(self.calculate(118889.0, 450808694), 450927583.00)

    def test0557(self):
        self.assertEquals(self.calculate(129804.0, -1957869227), -1957739423.00)

    def test0558(self):
        self.assertEquals(self.calculate(89366.0, -1709823245), -1709733879.00)

    def test0559(self):
        self.assertEquals(self.calculate(-94479.0, 583882899), 583788420.00)

    def test0560(self):
        self.assertEquals(self.calculate(892.0, 1555953579), 1555954471.00)

    def test0561(self):
        self.assertEquals(self.calculate(-187869.0, -158045334), -158233203.00)

    def test0562(self):
        self.assertEquals(self.calculate(98757.0, 1365669398), 1365768155.00)

    def test0563(self):
        self.assertEquals(self.calculate(-166496.0, 1996967808), 1996801312.00)

    def test0564(self):
        self.assertEquals(self.calculate(32255.0, 1668294169), 1668326424.00)

    def test0565(self):
        self.assertEquals(self.calculate(44865.0, -909393716), -909348851.00)

    def test0566(self):
        self.assertEquals(self.calculate(-158281.0, -100885612), -101043893.00)

    def test0567(self):
        self.assertEquals(self.calculate(12805.0, -1818628061), -1818615256.00)

    def test0568(self):
        self.assertEquals(self.calculate(-82606.0, -367461533), -367544139.00)

    def test0569(self):
        self.assertEquals(self.calculate(62998.0, -939259300), -939196302.00)

    def test0570(self):
        self.assertEquals(self.calculate(-45059.0, 429307481), 429262422.00)

    def test0571(self):
        self.assertEquals(self.calculate(-186029.0, 1731988723), 1731802694.00)

    def test0572(self):
        self.assertEquals(self.calculate(141668.0, 1247487518), 1247629186.00)

    def test0573(self):
        self.assertEquals(self.calculate(-114756.0, 986316534), 986201778.00)

    def test0574(self):
        self.assertEquals(self.calculate(3747.0, -2032471346), -2032467599.00)

    def test0575(self):
        self.assertEquals(self.calculate(-10741.0, 1083478327), 1083467586.00)

    def test0576(self):
        self.assertEquals(self.calculate(111820.0, 32363889), 32475709.00)

    def test0577(self):
        self.assertEquals(self.calculate(-74834.0, -624358607), -624433441.00)

    def test0578(self):
        self.assertEquals(self.calculate(33379.0, 2018358492), 2018391871.00)

    def test0579(self):
        self.assertEquals(self.calculate(-112746.0, -837146374), -837259120.00)

    def test0580(self):
        self.assertEquals(self.calculate(96301.0, 23058013), 23154314.00)

    def test0581(self):
        self.assertEquals(self.calculate(-87836.0, -1321414714), -1321502550.00)

    def test0582(self):
        self.assertEquals(self.calculate(-64723.0, 1496627732), 1496563009.00)

    def test0583(self):
        self.assertEquals(self.calculate(191095.0, 1384110575), 1384301670.00)

    def test0584(self):
        self.assertEquals(self.calculate(-35406.0, 1266599210), 1266563804.00)

    def test0585(self):
        self.assertEquals(self.calculate(-88916.0, -1275983601), -1276072517.00)

    def test0586(self):
        self.assertEquals(self.calculate(139538.0, -252938990), -252799452.00)

    def test0587(self):
        self.assertEquals(self.calculate(135960.0, 1408982926), 1409118886.00)

    def test0588(self):
        self.assertEquals(self.calculate(-722.0, -1097631789), -1097632511.00)

    def test0589(self):
        self.assertEquals(self.calculate(95823.0, -969162375), -969066552.00)

    def test0590(self):
        self.assertEquals(self.calculate(46195.0, -945846761), -945800566.00)

    def test0591(self):
        self.assertEquals(self.calculate(-162537.0, 816919506), 816756969.00)

    def test0592(self):
        self.assertEquals(self.calculate(-78401.0, -648261029), -648339430.00)

    def test0593(self):
        self.assertEquals(self.calculate(-96722.0, -269819210), -269915932.00)

    def test0594(self):
        self.assertEquals(self.calculate(156203.0, -1361297352), -1361141149.00)

    def test0595(self):
        self.assertEquals(self.calculate(-153854.0, -1235721476), -1235875330.00)

    def test0596(self):
        self.assertEquals(self.calculate(-99750.0, -1344490590), -1344590340.00)

    def test0597(self):
        self.assertEquals(self.calculate(-149665.0, 1839234583), 1839084918.00)

    def test0598(self):
        self.assertEquals(self.calculate(-140290.0, -252235667), -252375957.00)

    def test0599(self):
        self.assertEquals(self.calculate(106392.0, 1093588473), 1093694865.00)

    def test0600(self):
        self.assertEquals(self.calculate(123871.0, -173767568), -173643697.00)

    def test0601(self):
        self.assertEquals(self.calculate(1366.0, -922709592), -922708226.00)

    def test0602(self):
        self.assertEquals(self.calculate(-40974.0, 836329370), 836288396.00)

    def test0603(self):
        self.assertEquals(self.calculate(-26323.0, 705043469), 705017146.00)

    def test0604(self):
        self.assertEquals(self.calculate(-144834.0, -778953696), -779098530.00)

    def test0605(self):
        self.assertEquals(self.calculate(199521.0, 239621482), 239821003.00)

    def test0606(self):
        self.assertEquals(self.calculate(148410.0, -878488752), -878340342.00)

    def test0607(self):
        self.assertEquals(self.calculate(-10678.0, -973147539), -973158217.00)

    def test0608(self):
        self.assertEquals(self.calculate(-179248.0, 1448802595), 1448623347.00)

    def test0609(self):
        self.assertEquals(self.calculate(-104563.0, 2020470358), 2020365795.00)

    def test0610(self):
        self.assertEquals(self.calculate(182067.0, 902791934), 902974001.00)

    def test0611(self):
        self.assertEquals(self.calculate(29602.0, -652386953), -652357351.00)

    def test0612(self):
        self.assertEquals(self.calculate(-180932.0, 405450613), 405269681.00)

    def test0613(self):
        self.assertEquals(self.calculate(136710.0, -1670675225), -1670538515.00)

    def test0614(self):
        self.assertEquals(self.calculate(-65600.0, 1834468760), 1834403160.00)

    def test0615(self):
        self.assertEquals(self.calculate(3866.0, 124345994), 124349860.00)

    def test0616(self):
        self.assertEquals(self.calculate(-28458.0, -42145799), -42174257.00)

    def test0617(self):
        self.assertEquals(self.calculate(158680.0, 1125936862), 1126095542.00)

    def test0618(self):
        self.assertEquals(self.calculate(-125586.0, 408416023), 408290437.00)

    def test0619(self):
        self.assertEquals(self.calculate(121350.0, 1030923830), 1031045180.00)

    def test0620(self):
        self.assertEquals(self.calculate(-143665.0, -1732271149), -1732414814.00)

    def test0621(self):
        self.assertEquals(self.calculate(-31938.0, 1480659404), 1480627466.00)

    def test0622(self):
        self.assertEquals(self.calculate(7110.0, -1209738724), -1209731614.00)

    def test0623(self):
        self.assertEquals(self.calculate(-93819.0, -2034308218), -2034402037.00)

    def test0624(self):
        self.assertEquals(self.calculate(101454.0, 445476401), 445577855.00)

    def test0625(self):
        self.assertEquals(self.calculate(-158694.0, -1571595750), -1571754444.00)

    def test0626(self):
        self.assertEquals(self.calculate(129931.0, -1496920280), -1496790349.00)

    def test0627(self):
        self.assertEquals(self.calculate(-52547.0, -444707422), -444759969.00)

    def test0628(self):
        self.assertEquals(self.calculate(-51593.0, -832968776), -833020369.00)

    def test0629(self):
        self.assertEquals(self.calculate(-120798.0, 2117527072), 2117406274.00)

    def test0630(self):
        self.assertEquals(self.calculate(-61641.0, 1512305940), 1512244299.00)

    def test0631(self):
        self.assertEquals(self.calculate(176127.0, 568702345), 568878472.00)

    def test0632(self):
        self.assertEquals(self.calculate(37038.0, 22833850), 22870888.00)

    def test0633(self):
        self.assertEquals(self.calculate(14778.0, 35268360), 35283138.00)

    def test0634(self):
        self.assertEquals(self.calculate(139918.0, -1311292798), -1311152880.00)

    def test0635(self):
        self.assertEquals(self.calculate(-91796.0, -1077297465), -1077389261.00)

    def test0636(self):
        self.assertEquals(self.calculate(-62802.0, -828708176), -828770978.00)

    def test0637(self):
        self.assertEquals(self.calculate(-119870.0, -622675717), -622795587.00)

    def test0638(self):
        self.assertEquals(self.calculate(-191500.0, -892035005), -892226505.00)

    def test0639(self):
        self.assertEquals(self.calculate(159901.0, 1297480338), 1297640239.00)

    def test0640(self):
        self.assertEquals(self.calculate(144086.0, 2126269425), 2126413511.00)

    def test0641(self):
        self.assertEquals(self.calculate(-116595.0, 673038731), 672922136.00)

    def test0642(self):
        self.assertEquals(self.calculate(-108184.0, 1534172110), 1534063926.00)

    def test0643(self):
        self.assertEquals(self.calculate(39558.0, 1003414753), 1003454311.00)

    def test0644(self):
        self.assertEquals(self.calculate(-135991.0, 649203134), 649067143.00)

    def test0645(self):
        self.assertEquals(self.calculate(103009.0, 815911060), 816014069.00)

    def test0646(self):
        self.assertEquals(self.calculate(-16317.0, 1673431846), 1673415529.00)

    def test0647(self):
        self.assertEquals(self.calculate(144609.0, -1819242359), -1819097750.00)

    def test0648(self):
        self.assertEquals(self.calculate(-21219.0, 1029224832), 1029203613.00)

    def test0649(self):
        self.assertEquals(self.calculate(189425.0, 1187408863), 1187598288.00)

    def test0650(self):
        self.assertEquals(self.calculate(23441.0, -1392071715), -1392048274.00)

    def test0651(self):
        self.assertEquals(self.calculate(-151064.0, 1360358831), 1360207767.00)

    def test0652(self):
        self.assertEquals(self.calculate(-61379.0, 208962190), 208900811.00)

    def test0653(self):
        self.assertEquals(self.calculate(195008.0, 2083809747), 2084004755.00)

    def test0654(self):
        self.assertEquals(self.calculate(60819.0, 332654187), 332715006.00)

    def test0655(self):
        self.assertEquals(self.calculate(-17361.0, -901715166), -901732527.00)

    def test0656(self):
        self.assertEquals(self.calculate(-69473.0, -1299149549), -1299219022.00)

    def test0657(self):
        self.assertEquals(self.calculate(-70616.0, 540874272), 540803656.00)

    def test0658(self):
        self.assertEquals(self.calculate(134884.0, 1960550122), 1960685006.00)

    def test0659(self):
        self.assertEquals(self.calculate(29277.0, 1580381992), 1580411269.00)

    def test0660(self):
        self.assertEquals(self.calculate(-7757.0, 358497476), 358489719.00)

    def test0661(self):
        self.assertEquals(self.calculate(-123498.0, 1618118085), 1617994587.00)

    def test0662(self):
        self.assertEquals(self.calculate(15159.0, 2117999950), 2118015109.00)

    def test0663(self):
        self.assertEquals(self.calculate(123128.0, -553168730), -553045602.00)

    def test0664(self):
        self.assertEquals(self.calculate(-192795.0, -66687062), -66879857.00)

    def test0665(self):
        self.assertEquals(self.calculate(-23150.0, 2123737578), 2123714428.00)

    def test0666(self):
        self.assertEquals(self.calculate(-133973.0, 1739703929), 1739569956.00)

    def test0667(self):
        self.assertEquals(self.calculate(-176314.0, 941726943), 941550629.00)

    def test0668(self):
        self.assertEquals(self.calculate(-138352.0, 1377114726), 1376976374.00)

    def test0669(self):
        self.assertEquals(self.calculate(-80538.0, 940223204), 940142666.00)

    def test0670(self):
        self.assertEquals(self.calculate(-12788.0, -681218360), -681231148.00)

    def test0671(self):
        self.assertEquals(self.calculate(-10888.0, 459112412), 459101524.00)

    def test0672(self):
        self.assertEquals(self.calculate(48172.0, 476074926), 476123098.00)

    def test0673(self):
        self.assertEquals(self.calculate(-115040.0, -1094133853), -1094248893.00)

    def test0674(self):
        self.assertEquals(self.calculate(66915.0, -2038000288), -2037933373.00)

    def test0675(self):
        self.assertEquals(self.calculate(-129768.0, -1468673855), -1468803623.00)

    def test0676(self):
        self.assertEquals(self.calculate(-61460.0, 199495314), 199433854.00)

    def test0677(self):
        self.assertEquals(self.calculate(-45900.0, 1511225921), 1511180021.00)

    def test0678(self):
        self.assertEquals(self.calculate(4688.0, -1517636480), -1517631792.00)

    def test0679(self):
        self.assertEquals(self.calculate(-114976.0, 1757976316), 1757861340.00)

    def test0680(self):
        self.assertEquals(self.calculate(66001.0, -717993642), -717927641.00)

    def test0681(self):
        self.assertEquals(self.calculate(43226.0, 2081025119), 2081068345.00)

    def test0682(self):
        self.assertEquals(self.calculate(-76978.0, -538851397), -538928375.00)

    def test0683(self):
        self.assertEquals(self.calculate(-40666.0, 1080433238), 1080392572.00)

    def test0684(self):
        self.assertEquals(self.calculate(99105.0, -697325723), -697226618.00)

    def test0685(self):
        self.assertEquals(self.calculate(-90214.0, 1597168567), 1597078353.00)

    def test0686(self):
        self.assertEquals(self.calculate(-108610.0, 238432541), 238323931.00)

    def test0687(self):
        self.assertEquals(self.calculate(-108993.0, 262234406), 262125413.00)

    def test0688(self):
        self.assertEquals(self.calculate(34841.0, -2047567186), -2047532345.00)

    def test0689(self):
        self.assertEquals(self.calculate(-161396.0, 463711084), 463549688.00)

    def test0690(self):
        self.assertEquals(self.calculate(182449.0, 1573672110), 1573854559.00)

    def test0691(self):
        self.assertEquals(self.calculate(-178469.0, -307162080), -307340549.00)

    def test0692(self):
        self.assertEquals(self.calculate(179112.0, -849275134), -849096022.00)

    def test0693(self):
        self.assertEquals(self.calculate(-10974.0, -1304212406), -1304223380.00)

    def test0694(self):
        self.assertEquals(self.calculate(96492.0, 1057177781), 1057274273.00)

    def test0695(self):
        self.assertEquals(self.calculate(-157615.0, 205703949), 205546334.00)

    def test0696(self):
        self.assertEquals(self.calculate(106249.0, -40276509), -40170260.00)

    def test0697(self):
        self.assertEquals(self.calculate(102762.0, -1718445000), -1718342238.00)

    def test0698(self):
        self.assertEquals(self.calculate(88617.0, -1875275760), -1875187143.00)

    def test0699(self):
        self.assertEquals(self.calculate(103296.0, 1478318417), 1478421713.00)

    def test0700(self):
        self.assertEquals(self.calculate(-45925.0, -859467835), -859513760.00)

    def test0701(self):
        self.assertEquals(self.calculate(-71678.0, 1340323274), 1340251596.00)

    def test0702(self):
        self.assertEquals(self.calculate(-125709.0, 1788743536), 1788617827.00)

    def test0703(self):
        self.assertEquals(self.calculate(136332.0, -1748637430), -1748501098.00)

    def test0704(self):
        self.assertEquals(self.calculate(154673.0, -1975364686), -1975210013.00)

    def test0705(self):
        self.assertEquals(self.calculate(110449.0, 301267317), 301377766.00)

    def test0706(self):
        self.assertEquals(self.calculate(10445.0, -2132331487), -2132321042.00)

    def test0707(self):
        self.assertEquals(self.calculate(-4663.0, 1784379989), 1784375326.00)

    def test0708(self):
        self.assertEquals(self.calculate(-161484.0, -970040694), -970202178.00)

    def test0709(self):
        self.assertEquals(self.calculate(83012.0, -655471589), -655388577.00)

    def test0710(self):
        self.assertEquals(self.calculate(49065.0, 1340923696), 1340972761.00)

    def test0711(self):
        self.assertEquals(self.calculate(-59245.0, -608271414), -608330659.00)

    def test0712(self):
        self.assertEquals(self.calculate(36637.0, 427930811), 427967448.00)

    def test0713(self):
        self.assertEquals(self.calculate(125399.0, 263094196), 263219595.00)

    def test0714(self):
        self.assertEquals(self.calculate(184943.0, 1116583974), 1116768917.00)

    def test0715(self):
        self.assertEquals(self.calculate(-138305.0, 251839344), 251701039.00)

    def test0716(self):
        self.assertEquals(self.calculate(163471.0, 870603191), 870766662.00)

    def test0717(self):
        self.assertEquals(self.calculate(124396.0, 1641547455), 1641671851.00)

    def test0718(self):
        self.assertEquals(self.calculate(119794.0, -734994885), -734875091.00)

    def test0719(self):
        self.assertEquals(self.calculate(53440.0, -1228393536), -1228340096.00)

    def test0720(self):
        self.assertEquals(self.calculate(5397.0, 905216294), 905221691.00)

    def test0721(self):
        self.assertEquals(self.calculate(43402.0, -1916472325), -1916428923.00)

    def test0722(self):
        self.assertEquals(self.calculate(-109853.0, -1435336022), -1435445875.00)

    def test0723(self):
        self.assertEquals(self.calculate(126242.0, -1857444938), -1857318696.00)

    def test0724(self):
        self.assertEquals(self.calculate(-180751.0, -975387099), -975567850.00)

    def test0725(self):
        self.assertEquals(self.calculate(75387.0, -795721326), -795645939.00)

    def test0726(self):
        self.assertEquals(self.calculate(-106324.0, 1636207128), 1636100804.00)

    def test0727(self):
        self.assertEquals(self.calculate(-11981.0, -1192101413), -1192113394.00)

    def test0728(self):
        self.assertEquals(self.calculate(29346.0, -1371607700), -1371578354.00)

    def test0729(self):
        self.assertEquals(self.calculate(103211.0, 214663213), 214766424.00)

    def test0730(self):
        self.assertEquals(self.calculate(84055.0, 1373583841), 1373667896.00)

    def test0731(self):
        self.assertEquals(self.calculate(189632.0, 260677241), 260866873.00)

    def test0732(self):
        self.assertEquals(self.calculate(137729.0, -1293513756), -1293376027.00)

    def test0733(self):
        self.assertEquals(self.calculate(105671.0, 549465223), 549570894.00)

    def test0734(self):
        self.assertEquals(self.calculate(-133261.0, 1626834469), 1626701208.00)

    def test0735(self):
        self.assertEquals(self.calculate(84962.0, 135642571), 135727533.00)

    def test0736(self):
        self.assertEquals(self.calculate(23216.0, -904281158), -904257942.00)

    def test0737(self):
        self.assertEquals(self.calculate(104814.0, 1530766245), 1530871059.00)

    def test0738(self):
        self.assertEquals(self.calculate(-42824.0, 934568465), 934525641.00)

    def test0739(self):
        self.assertEquals(self.calculate(57907.0, 1093662230), 1093720137.00)

    def test0740(self):
        self.assertEquals(self.calculate(-83278.0, -682750848), -682834126.00)

    def test0741(self):
        self.assertEquals(self.calculate(-191845.0, -900100443), -900292288.00)

    def test0742(self):
        self.assertEquals(self.calculate(-152814.0, -1944234775), -1944387589.00)

    def test0743(self):
        self.assertEquals(self.calculate(-198950.0, 1233196311), 1232997361.00)

    def test0744(self):
        self.assertEquals(self.calculate(46570.0, -799057769), -799011199.00)

    def test0745(self):
        self.assertEquals(self.calculate(125564.0, -1927809), -1802245.00)

    def test0746(self):
        self.assertEquals(self.calculate(68913.0, 1866812017), 1866880930.00)

    def test0747(self):
        self.assertEquals(self.calculate(120088.0, 379885765), 380005853.00)

    def test0748(self):
        self.assertEquals(self.calculate(186227.0, 588774768), 588960995.00)

    def test0749(self):
        self.assertEquals(self.calculate(65182.0, 1618501658), 1618566840.00)

    def test0750(self):
        self.assertEquals(self.calculate(-49945.0, 8275610), 8225665.00)

    def test0751(self):
        self.assertEquals(self.calculate(-153604.0, 1383665353), 1383511749.00)

    def test0752(self):
        self.assertEquals(self.calculate(186955.0, 2019875937), 2020062892.00)

    def test0753(self):
        self.assertEquals(self.calculate(132154.0, 773095343), 773227497.00)

    def test0754(self):
        self.assertEquals(self.calculate(-29445.0, -655523652), -655553097.00)

    def test0755(self):
        self.assertEquals(self.calculate(-159603.0, -1117649221), -1117808824.00)

    def test0756(self):
        self.assertEquals(self.calculate(-108636.0, -704971067), -705079703.00)

    def test0757(self):
        self.assertEquals(self.calculate(-147909.0, -1392117637), -1392265546.00)

    def test0758(self):
        self.assertEquals(self.calculate(-68035.0, -1163007995), -1163076030.00)

    def test0759(self):
        self.assertEquals(self.calculate(118409.0, 996579914), 996698323.00)

    def test0760(self):
        self.assertEquals(self.calculate(-116321.0, -1728991064), -1729107385.00)

    def test0761(self):
        self.assertEquals(self.calculate(-105251.0, -1101519158), -1101624409.00)

    def test0762(self):
        self.assertEquals(self.calculate(157074.0, -1897546618), -1897389544.00)

    def test0763(self):
        self.assertEquals(self.calculate(84362.0, 224422435), 224506797.00)

    def test0764(self):
        self.assertEquals(self.calculate(-142306.0, 523779919), 523637613.00)

    def test0765(self):
        self.assertEquals(self.calculate(186746.0, -266659309), -266472563.00)

    def test0766(self):
        self.assertEquals(self.calculate(-118780.0, -2007956906), -2008075686.00)

    def test0767(self):
        self.assertEquals(self.calculate(-39436.0, -1056121364), -1056160800.00)

    def test0768(self):
        self.assertEquals(self.calculate(-124900.0, 1779600691), 1779475791.00)

    def test0769(self):
        self.assertEquals(self.calculate(-58770.0, 1822805708), 1822746938.00)

    def test0770(self):
        self.assertEquals(self.calculate(167880.0, 325854427), 326022307.00)

    def test0771(self):
        self.assertEquals(self.calculate(-12513.0, 644506899), 644494386.00)

    def test0772(self):
        self.assertEquals(self.calculate(95261.0, -844075047), -843979786.00)

    def test0773(self):
        self.assertEquals(self.calculate(85614.0, -1267780907), -1267695293.00)

    def test0774(self):
        self.assertEquals(self.calculate(158183.0, -1906041279), -1905883096.00)

    def test0775(self):
        self.assertEquals(self.calculate(48192.0, -433259939), -433211747.00)

    def test0776(self):
        self.assertEquals(self.calculate(-165289.0, -1051257101), -1051422390.00)

    def test0777(self):
        self.assertEquals(self.calculate(-90768.0, -1220943639), -1221034407.00)

    def test0778(self):
        self.assertEquals(self.calculate(62344.0, -1964628870), -1964566526.00)

    def test0779(self):
        self.assertEquals(self.calculate(141817.0, 94970541), 95112358.00)

    def test0780(self):
        self.assertEquals(self.calculate(-110849.0, 374349366), 374238517.00)

    def test0781(self):
        self.assertEquals(self.calculate(-194532.0, -2147354715), -2147549247.00)

    def test0782(self):
        self.assertEquals(self.calculate(37369.0, -1286969810), -1286932441.00)

    def test0783(self):
        self.assertEquals(self.calculate(37434.0, -1298086287), -1298048853.00)

    def test0784(self):
        self.assertEquals(self.calculate(188637.0, 1486272493), 1486461130.00)

    def test0785(self):
        self.assertEquals(self.calculate(-65156.0, -1932423317), -1932488473.00)

    def test0786(self):
        self.assertEquals(self.calculate(163287.0, -1766470868), -1766307581.00)

    def test0787(self):
        self.assertEquals(self.calculate(-17680.0, 337072740), 337055060.00)

    def test0788(self):
        self.assertEquals(self.calculate(-199599.0, -812328026), -812527625.00)

    def test0789(self):
        self.assertEquals(self.calculate(-64395.0, -1715977400), -1716041795.00)

    def test0790(self):
        self.assertEquals(self.calculate(3288.0, 30447803), 30451091.00)

    def test0791(self):
        self.assertEquals(self.calculate(-60654.0, -497425343), -497485997.00)

    def test0792(self):
        self.assertEquals(self.calculate(-129822.0, 6401931), 6272109.00)

    def test0793(self):
        self.assertEquals(self.calculate(61209.0, 864722175), 864783384.00)

    def test0794(self):
        self.assertEquals(self.calculate(91035.0, 1357262047), 1357353082.00)

    def test0795(self):
        self.assertEquals(self.calculate(160235.0, 1034754408), 1034914643.00)

    def test0796(self):
        self.assertEquals(self.calculate(31789.0, 1852405542), 1852437331.00)

    def test0797(self):
        self.assertEquals(self.calculate(51133.0, -854219745), -854168612.00)

    def test0798(self):
        self.assertEquals(self.calculate(-82093.0, -1710874124), -1710956217.00)

    def test0799(self):
        self.assertEquals(self.calculate(-127964.0, 1490857083), 1490729119.00)

    def test0800(self):
        self.assertEquals(self.calculate(108226.0, 959992722), 960100948.00)

    def test0801(self):
        self.assertEquals(self.calculate(111802.0, -2115795034), -2115683232.00)

    def test0802(self):
        self.assertEquals(self.calculate(-77700.0, -238325069), -238402769.00)

    def test0803(self):
        self.assertEquals(self.calculate(-186617.0, 848186799), 848000182.00)

    def test0804(self):
        self.assertEquals(self.calculate(181564.0, 2102867350), 2103048914.00)

    def test0805(self):
        self.assertEquals(self.calculate(-20040.0, 2036990191), 2036970151.00)

    def test0806(self):
        self.assertEquals(self.calculate(175217.0, 826385344), 826560561.00)

    def test0807(self):
        self.assertEquals(self.calculate(-172433.0, 1257927819), 1257755386.00)

    def test0808(self):
        self.assertEquals(self.calculate(192186.0, 390244118), 390436304.00)

    def test0809(self):
        self.assertEquals(self.calculate(-170085.0, 469561530), 469391445.00)

    def test0810(self):
        self.assertEquals(self.calculate(150810.0, 1807577318), 1807728128.00)

    def test0811(self):
        self.assertEquals(self.calculate(-82952.0, -2066711965), -2066794917.00)

    def test0812(self):
        self.assertEquals(self.calculate(15964.0, 2030773137), 2030789101.00)

    def test0813(self):
        self.assertEquals(self.calculate(137360.0, 1066067154), 1066204514.00)

    def test0814(self):
        self.assertEquals(self.calculate(-145242.0, -567092209), -567237451.00)

    def test0815(self):
        self.assertEquals(self.calculate(67398.0, 703030921), 703098319.00)

    def test0816(self):
        self.assertEquals(self.calculate(60560.0, 613595165), 613655725.00)

    def test0817(self):
        self.assertEquals(self.calculate(-187451.0, -149427740), -149615191.00)

    def test0818(self):
        self.assertEquals(self.calculate(-89782.0, -855242690), -855332472.00)

    def test0819(self):
        self.assertEquals(self.calculate(-128709.0, 59578778), 59450069.00)

    def test0820(self):
        self.assertEquals(self.calculate(43858.0, -943732549), -943688691.00)

    def test0821(self):
        self.assertEquals(self.calculate(-164910.0, 191955315), 191790405.00)

    def test0822(self):
        self.assertEquals(self.calculate(-71924.0, 992096124), 992024200.00)

    def test0823(self):
        self.assertEquals(self.calculate(1011.0, 1285926765), 1285927776.00)

    def test0824(self):
        self.assertEquals(self.calculate(-154889.0, 566614107), 566459218.00)

    def test0825(self):
        self.assertEquals(self.calculate(188729.0, -197340740), -197152011.00)

    def test0826(self):
        self.assertEquals(self.calculate(-15379.0, -1797920473), -1797935852.00)

    def test0827(self):
        self.assertEquals(self.calculate(36871.0, 25444542), 25481413.00)

    def test0828(self):
        self.assertEquals(self.calculate(-157138.0, -594404621), -594561759.00)

    def test0829(self):
        self.assertEquals(self.calculate(39893.0, 1393231975), 1393271868.00)

    def test0830(self):
        self.assertEquals(self.calculate(131981.0, -427841356), -427709375.00)

    def test0831(self):
        self.assertEquals(self.calculate(-9583.0, -347314785), -347324368.00)

    def test0832(self):
        self.assertEquals(self.calculate(149211.0, -667960555), -667811344.00)

    def test0833(self):
        self.assertEquals(self.calculate(19299.0, 939908200), 939927499.00)

    def test0834(self):
        self.assertEquals(self.calculate(-125057.0, -1618708502), -1618833559.00)

    def test0835(self):
        self.assertEquals(self.calculate(-36159.0, -1312482185), -1312518344.00)

    def test0836(self):
        self.assertEquals(self.calculate(-14506.0, -1608083632), -1608098138.00)

    def test0837(self):
        self.assertEquals(self.calculate(-184123.0, 996607507), 996423384.00)

    def test0838(self):
        self.assertEquals(self.calculate(-181378.0, -485874802), -486056180.00)

    def test0839(self):
        self.assertEquals(self.calculate(-19280.0, 1414812550), 1414793270.00)

    def test0840(self):
        self.assertEquals(self.calculate(42643.0, 250472416), 250515059.00)

    def test0841(self):
        self.assertEquals(self.calculate(189130.0, 1773016899), 1773206029.00)

    def test0842(self):
        self.assertEquals(self.calculate(165578.0, 1429707492), 1429873070.00)

    def test0843(self):
        self.assertEquals(self.calculate(192314.0, -1586117323), -1585925009.00)

    def test0844(self):
        self.assertEquals(self.calculate(41571.0, -463639304), -463597733.00)

    def test0845(self):
        self.assertEquals(self.calculate(-187227.0, 1391546084), 1391358857.00)

    def test0846(self):
        self.assertEquals(self.calculate(175227.0, -2066509916), -2066334689.00)

    def test0847(self):
        self.assertEquals(self.calculate(-55512.0, -301589482), -301644994.00)

    def test0848(self):
        self.assertEquals(self.calculate(-74675.0, 314325307), 314250632.00)

    def test0849(self):
        self.assertEquals(self.calculate(-94462.0, 219770310), 219675848.00)

    def test0850(self):
        self.assertEquals(self.calculate(81607.0, 1989287296), 1989368903.00)

    def test0851(self):
        self.assertEquals(self.calculate(110351.0, -1612426964), -1612316613.00)

    def test0852(self):
        self.assertEquals(self.calculate(190939.0, -1995215457), -1995024518.00)

    def test0853(self):
        self.assertEquals(self.calculate(-33820.0, 1207279045), 1207245225.00)

    def test0854(self):
        self.assertEquals(self.calculate(-37531.0, 40544358), 40506827.00)

    def test0855(self):
        self.assertEquals(self.calculate(149975.0, 442726060), 442876035.00)

    def test0856(self):
        self.assertEquals(self.calculate(-150859.0, -2080151992), -2080302851.00)

    def test0857(self):
        self.assertEquals(self.calculate(8161.0, 1538532282), 1538540443.00)

    def test0858(self):
        self.assertEquals(self.calculate(-143499.0, -877401140), -877544639.00)

    def test0859(self):
        self.assertEquals(self.calculate(151709.0, 617336120), 617487829.00)

    def test0860(self):
        self.assertEquals(self.calculate(120774.0, -1917621311), -1917500537.00)

    def test0861(self):
        self.assertEquals(self.calculate(65515.0, -1514065398), -1513999883.00)

    def test0862(self):
        self.assertEquals(self.calculate(-58653.0, 1977139521), 1977080868.00)

    def test0863(self):
        self.assertEquals(self.calculate(166656.0, 297968023), 298134679.00)

    def test0864(self):
        self.assertEquals(self.calculate(-52085.0, 7152851), 7100766.00)

    def test0865(self):
        self.assertEquals(self.calculate(-120380.0, 1465379491), 1465259111.00)

    def test0866(self):
        self.assertEquals(self.calculate(30177.0, -1108411510), -1108381333.00)

    def test0867(self):
        self.assertEquals(self.calculate(-48584.0, -411653493), -411702077.00)

    def test0868(self):
        self.assertEquals(self.calculate(21512.0, -2077873741), -2077852229.00)

    def test0869(self):
        self.assertEquals(self.calculate(-131368.0, -2067925129), -2068056497.00)

    def test0870(self):
        self.assertEquals(self.calculate(-66451.0, -687944935), -688011386.00)

    def test0871(self):
        self.assertEquals(self.calculate(139595.0, -1336675738), -1336536143.00)

    def test0872(self):
        self.assertEquals(self.calculate(6216.0, -1874872174), -1874865958.00)

    def test0873(self):
        self.assertEquals(self.calculate(-96021.0, -1167486114), -1167582135.00)

    def test0874(self):
        self.assertEquals(self.calculate(149736.0, 1094096543), 1094246279.00)

    def test0875(self):
        self.assertEquals(self.calculate(140122.0, 1874175988), 1874316110.00)

    def test0876(self):
        self.assertEquals(self.calculate(-182850.0, 812818134), 812635284.00)

    def test0877(self):
        self.assertEquals(self.calculate(41879.0, 1930419833), 1930461712.00)

    def test0878(self):
        self.assertEquals(self.calculate(65495.0, 1327152863), 1327218358.00)

    def test0879(self):
        self.assertEquals(self.calculate(-150189.0, -1937288773), -1937438962.00)

    def test0880(self):
        self.assertEquals(self.calculate(-55238.0, 723608351), 723553113.00)

    def test0881(self):
        self.assertEquals(self.calculate(187325.0, 894051185), 894238510.00)

    def test0882(self):
        self.assertEquals(self.calculate(125785.0, -1281380962), -1281255177.00)

    def test0883(self):
        self.assertEquals(self.calculate(95284.0, 1867592536), 1867687820.00)

    def test0884(self):
        self.assertEquals(self.calculate(138577.0, 1266542757), 1266681334.00)

    def test0885(self):
        self.assertEquals(self.calculate(-1077.0, 1199748198), 1199747121.00)

    def test0886(self):
        self.assertEquals(self.calculate(163657.0, 1745632584), 1745796241.00)

    def test0887(self):
        self.assertEquals(self.calculate(-170610.0, -778533438), -778704048.00)

    def test0888(self):
        self.assertEquals(self.calculate(34872.0, -1809186468), -1809151596.00)

    def test0889(self):
        self.assertEquals(self.calculate(-122172.0, -2091024221), -2091146393.00)

    def test0890(self):
        self.assertEquals(self.calculate(-176258.0, 726235069), 726058811.00)

    def test0891(self):
        self.assertEquals(self.calculate(78488.0, 1207223884), 1207302372.00)

    def test0892(self):
        self.assertEquals(self.calculate(118187.0, -1966623564), -1966505377.00)

    def test0893(self):
        self.assertEquals(self.calculate(96313.0, 1011542124), 1011638437.00)

    def test0894(self):
        self.assertEquals(self.calculate(-13756.0, -1363549977), -1363563733.00)

    def test0895(self):
        self.assertEquals(self.calculate(7519.0, -1171275421), -1171267902.00)

    def test0896(self):
        self.assertEquals(self.calculate(-54704.0, 182655898), 182601194.00)

    def test0897(self):
        self.assertEquals(self.calculate(61636.0, 1716466346), 1716527982.00)

    def test0898(self):
        self.assertEquals(self.calculate(136521.0, -1992668523), -1992532002.00)

    def test0899(self):
        self.assertEquals(self.calculate(-13391.0, 1582656269), 1582642878.00)

    def test0900(self):
        self.assertEquals(self.calculate(75591.0, 1774870476), 1774946067.00)

    def test0901(self):
        self.assertEquals(self.calculate(107723.0, 934090028), 934197751.00)

    def test0902(self):
        self.assertEquals(self.calculate(198993.0, -1241091621), -1240892628.00)

    def test0903(self):
        self.assertEquals(self.calculate(41105.0, -899378250), -899337145.00)

    def test0904(self):
        self.assertEquals(self.calculate(-4258.0, -489597515), -489601773.00)

    def test0905(self):
        self.assertEquals(self.calculate(107244.0, 1498971815), 1499079059.00)

    def test0906(self):
        self.assertEquals(self.calculate(135096.0, 1357161412), 1357296508.00)

    def test0907(self):
        self.assertEquals(self.calculate(943.0, 932695647), 932696590.00)

    def test0908(self):
        self.assertEquals(self.calculate(-83184.0, -1408507865), -1408591049.00)

    def test0909(self):
        self.assertEquals(self.calculate(-94847.0, 1378143221), 1378048374.00)

    def test0910(self):
        self.assertEquals(self.calculate(86792.0, 467745788), 467832580.00)

    def test0911(self):
        self.assertEquals(self.calculate(72633.0, 2046628357), 2046700990.00)

    def test0912(self):
        self.assertEquals(self.calculate(-78593.0, 1443714226), 1443635633.00)

    def test0913(self):
        self.assertEquals(self.calculate(-95808.0, -184614733), -184710541.00)

    def test0914(self):
        self.assertEquals(self.calculate(165070.0, 1377275685), 1377440755.00)

    def test0915(self):
        self.assertEquals(self.calculate(-155589.0, -640166351), -640321940.00)

    def test0916(self):
        self.assertEquals(self.calculate(85044.0, 986121070), 986206114.00)

    def test0917(self):
        self.assertEquals(self.calculate(126587.0, 2026008328), 2026134915.00)

    def test0918(self):
        self.assertEquals(self.calculate(-55338.0, 1622827481), 1622772143.00)

    def test0919(self):
        self.assertEquals(self.calculate(171146.0, -1728812688), -1728641542.00)

    def test0920(self):
        self.assertEquals(self.calculate(-36021.0, -1270977083), -1271013104.00)

    def test0921(self):
        self.assertEquals(self.calculate(-19414.0, 1180665082), 1180645668.00)

    def test0922(self):
        self.assertEquals(self.calculate(26290.0, 1266118285), 1266144575.00)

    def test0923(self):
        self.assertEquals(self.calculate(-106517.0, -945478451), -945584968.00)

    def test0924(self):
        self.assertEquals(self.calculate(169641.0, -952377514), -952207873.00)

    def test0925(self):
        self.assertEquals(self.calculate(96377.0, -1422417177), -1422320800.00)

    def test0926(self):
        self.assertEquals(self.calculate(166786.0, 1750472649), 1750639435.00)

    def test0927(self):
        self.assertEquals(self.calculate(96136.0, -102371731), -102275595.00)

    def test0928(self):
        self.assertEquals(self.calculate(-170584.0, -1356980204), -1357150788.00)

    def test0929(self):
        self.assertEquals(self.calculate(51140.0, 584985263), 585036403.00)

    def test0930(self):
        self.assertEquals(self.calculate(-13145.0, -1584253576), -1584266721.00)

    def test0931(self):
        self.assertEquals(self.calculate(181125.0, -1749677729), -1749496604.00)

    def test0932(self):
        self.assertEquals(self.calculate(17270.0, 1506843761), 1506861031.00)

    def test0933(self):
        self.assertEquals(self.calculate(-152563.0, -1026776020), -1026928583.00)

    def test0934(self):
        self.assertEquals(self.calculate(43097.0, 525233020), 525276117.00)

    def test0935(self):
        self.assertEquals(self.calculate(163998.0, 1428074358), 1428238356.00)

    def test0936(self):
        self.assertEquals(self.calculate(-101466.0, -1473048859), -1473150325.00)

    def test0937(self):
        self.assertEquals(self.calculate(-40602.0, -1900111223), -1900151825.00)

    def test0938(self):
        self.assertEquals(self.calculate(64666.0, 1801704709), 1801769375.00)

    def test0939(self):
        self.assertEquals(self.calculate(-33227.0, 573128142), 573094915.00)

    def test0940(self):
        self.assertEquals(self.calculate(-194573.0, -1508990433), -1509185006.00)

    def test0941(self):
        self.assertEquals(self.calculate(-127126.0, -457431396), -457558522.00)

    def test0942(self):
        self.assertEquals(self.calculate(-95262.0, 454189496), 454094234.00)

    def test0943(self):
        self.assertEquals(self.calculate(-72866.0, -640777926), -640850792.00)

    def test0944(self):
        self.assertEquals(self.calculate(-48692.0, 42030511), 41981819.00)

    def test0945(self):
        self.assertEquals(self.calculate(-168034.0, 758155153), 757987119.00)

    def test0946(self):
        self.assertEquals(self.calculate(-144703.0, 592054881), 591910178.00)

    def test0947(self):
        self.assertEquals(self.calculate(134213.0, 961934844), 962069057.00)

    def test0948(self):
        self.assertEquals(self.calculate(-192468.0, -1448689760), -1448882228.00)

    def test0949(self):
        self.assertEquals(self.calculate(-32638.0, 1668734620), 1668701982.00)

    def test0950(self):
        self.assertEquals(self.calculate(32272.0, 2143075759), 2143108031.00)

    def test0951(self):
        self.assertEquals(self.calculate(-66268.0, 589152241), 589085973.00)

    def test0952(self):
        self.assertEquals(self.calculate(-65704.0, 1873516245), 1873450541.00)

    def test0953(self):
        self.assertEquals(self.calculate(25016.0, 1253493225), 1253518241.00)

    def test0954(self):
        self.assertEquals(self.calculate(18835.0, -405697780), -405678945.00)

    def test0955(self):
        self.assertEquals(self.calculate(-76567.0, -76705014), -76781581.00)

    def test0956(self):
        self.assertEquals(self.calculate(-24212.0, -344086051), -344110263.00)

    def test0957(self):
        self.assertEquals(self.calculate(-2588.0, 199974942), 199972354.00)

    def test0958(self):
        self.assertEquals(self.calculate(5900.0, 628739456), 628745356.00)

    def test0959(self):
        self.assertEquals(self.calculate(-165878.0, -2039328693), -2039494571.00)

    def test0960(self):
        self.assertEquals(self.calculate(-61790.0, 335322811), 335261021.00)

    def test0961(self):
        self.assertEquals(self.calculate(196183.0, -1873428731), -1873232548.00)

    def test0962(self):
        self.assertEquals(self.calculate(-193298.0, -2007003531), -2007196829.00)

    def test0963(self):
        self.assertEquals(self.calculate(103972.0, 1069737978), 1069841950.00)

    def test0964(self):
        self.assertEquals(self.calculate(-30772.0, -700929822), -700960594.00)

    def test0965(self):
        self.assertEquals(self.calculate(-27623.0, -125456304), -125483927.00)

    def test0966(self):
        self.assertEquals(self.calculate(31901.0, 645733254), 645765155.00)

    def test0967(self):
        self.assertEquals(self.calculate(-73488.0, 1057289147), 1057215659.00)

    def test0968(self):
        self.assertEquals(self.calculate(-122521.0, 1384551510), 1384428989.00)

    def test0969(self):
        self.assertEquals(self.calculate(125399.0, -376253124), -376127725.00)

    def test0970(self):
        self.assertEquals(self.calculate(24415.0, 2112697097), 2112721512.00)

    def test0971(self):
        self.assertEquals(self.calculate(170426.0, 305517811), 305688237.00)

    def test0972(self):
        self.assertEquals(self.calculate(-161159.0, -1468510427), -1468671586.00)

    def test0973(self):
        self.assertEquals(self.calculate(-48862.0, 1721521975), 1721473113.00)

    def test0974(self):
        self.assertEquals(self.calculate(-188172.0, 1109383750), 1109195578.00)

    def test0975(self):
        self.assertEquals(self.calculate(-137611.0, -1750381237), -1750518848.00)

    def test0976(self):
        self.assertEquals(self.calculate(-12313.0, 855872189), 855859876.00)

    def test0977(self):
        self.assertEquals(self.calculate(-185674.0, 1853802025), 1853616351.00)

    def test0978(self):
        self.assertEquals(self.calculate(188492.0, 1508623648), 1508812140.00)

    def test0979(self):
        self.assertEquals(self.calculate(-47617.0, 144183645), 144136028.00)

    def test0980(self):
        self.assertEquals(self.calculate(62485.0, 1371749633), 1371812118.00)

    def test0981(self):
        self.assertEquals(self.calculate(-176048.0, -1578707019), -1578883067.00)

    def test0982(self):
        self.assertEquals(self.calculate(-69827.0, -128429624), -128499451.00)

    def test0983(self):
        self.assertEquals(self.calculate(195750.0, -280870872), -280675122.00)

    def test0984(self):
        self.assertEquals(self.calculate(-66678.0, -2002035861), -2002102539.00)

    def test0985(self):
        self.assertEquals(self.calculate(135183.0, 989490443), 989625626.00)

    def test0986(self):
        self.assertEquals(self.calculate(-12018.0, -1909683733), -1909695751.00)

    def test0987(self):
        self.assertEquals(self.calculate(112358.0, -841226954), -841114596.00)

    def test0988(self):
        self.assertEquals(self.calculate(53088.0, -855995439), -855942351.00)

    def test0989(self):
        self.assertEquals(self.calculate(-128595.0, 267537805), 267409210.00)

    def test0990(self):
        self.assertEquals(self.calculate(140949.0, 1944966580), 1945107529.00)

    def test0991(self):
        self.assertEquals(self.calculate(135262.0, -1933965242), -1933829980.00)

    def test0992(self):
        self.assertEquals(self.calculate(-154135.0, 809062040), 808907905.00)

    def test0993(self):
        self.assertEquals(self.calculate(14249.0, -544987776), -544973527.00)

    def test0994(self):
        self.assertEquals(self.calculate(126483.0, -1573199939), -1573073456.00)

    def test0995(self):
        self.assertEquals(self.calculate(80944.0, -1416796662), -1416715718.00)

    def test0996(self):
        self.assertEquals(self.calculate(118789.0, 1259820174), 1259938963.00)

    def test0997(self):
        self.assertEquals(self.calculate(132059.0, 1225341656), 1225473715.00)

    def test0998(self):
        self.assertEquals(self.calculate(94464.0, -287915136), -287820672.00)

    def test0999(self):
        self.assertEquals(self.calculate(-5476.0, 1547693956), 1547688480.00)

    def test1000(self):
        self.assertEquals(self.calculate(-193049.0, 1655148764), 1654955715.00)

    def test1001(self):
        self.assertEquals(self.calculate(-118399.0, 674293837), 674175438.00)

    def test1002(self):
        self.assertEquals(self.calculate(145651.0, -211038033), -210892382.00)

    def test1003(self):
        self.assertEquals(self.calculate(-47206.0, 11760210), 11713004.00)

    def test1004(self):
        self.assertEquals(self.calculate(-116408.0, -1090641708), -1090758116.00)

    def test1005(self):
        self.assertEquals(self.calculate(-25603.0, 1605694165), 1605668562.00)

    def test1006(self):
        self.assertEquals(self.calculate(-77830.0, 1212717833), 1212640003.00)

    def test1007(self):
        self.assertEquals(self.calculate(-62478.0, -1677134152), -1677196630.00)

    def test1008(self):
        self.assertEquals(self.calculate(-174653.0, 916659791), 916485138.00)

    def test1009(self):
        self.assertEquals(self.calculate(56750.0, 615834856), 615891606.00)

    def test1010(self):
        self.assertEquals(self.calculate(-190110.0, 996995810), 996805700.00)

    def test1011(self):
        self.assertEquals(self.calculate(-145507.0, 1948409483), 1948263976.00)

    def test1012(self):
        self.assertEquals(self.calculate(-99583.0, 999336868), 999237285.00)

    def test1013(self):
        self.assertEquals(self.calculate(-99386.0, -392154235), -392253621.00)

    def test1014(self):
        self.assertEquals(self.calculate(190152.0, -362447653), -362257501.00)

    def test1015(self):
        self.assertEquals(self.calculate(-79351.0, 506408496), 506329145.00)

    def test1016(self):
        self.assertEquals(self.calculate(-28390.0, -1804087471), -1804115861.00)

    def test1017(self):
        self.assertEquals(self.calculate(-18368.0, 1839650426), 1839632058.00)

    def test1018(self):
        self.assertEquals(self.calculate(-106639.0, 732310687), 732204048.00)

    def test1019(self):
        self.assertEquals(self.calculate(-197275.0, -1692190117), -1692387392.00)

    def test1020(self):
        self.assertEquals(self.calculate(174399.0, 974321025), 974495424.00)

    def test1021(self):
        self.assertEquals(self.calculate(4012.0, 208384711), 208388723.00)

    def test1022(self):
        self.assertEquals(self.calculate(-197886.0, -1314905216), -1315103102.00)

    def test1023(self):
        self.assertEquals(self.calculate(113658.0, 338414308), 338527966.00)



class TestVM_Add_FloatFloat(unittest.TestCase):
    def setUp(self):
        v.setOperandB(CALC_FLOAT_FLOAT)

    def tearDown(self):
        pass

    def calculate(self, lhs, rhs):
        v.VM_PushF(lhs)
        v.VM_PushF(rhs)
        v.VM_Add()
        res = v.VM_PopF()
        self.assertEquals(v.getSP(), 0)
        return res

    def test0000(self):
        self.assertEquals(self.calculate(23489.0, -176579.0), -153090.00)

    def test0001(self):
        self.assertEquals(self.calculate(-25229.0, -6172.0), -31401.00)

    def test0002(self):
        self.assertEquals(self.calculate(-22765.0, -11631.0), -34396.00)

    def test0003(self):
        self.assertEquals(self.calculate(-82733.0, -87370.0), -170103.00)

    def test0004(self):
        self.assertEquals(self.calculate(35550.0, 77700.0), 113250.00)

    def test0005(self):
        self.assertEquals(self.calculate(131204.0, -97792.0), 33412.00)

    def test0006(self):
        self.assertEquals(self.calculate(-36870.0, 4655.0), -32215.00)

    def test0007(self):
        self.assertEquals(self.calculate(-136606.0, -122187.0), -258793.00)

    def test0008(self):
        self.assertEquals(self.calculate(-104190.0, 31164.0), -73026.00)

    def test0009(self):
        self.assertEquals(self.calculate(49361.0, 49811.0), 99172.00)

    def test0010(self):
        self.assertEquals(self.calculate(-157299.0, -193802.0), -351101.00)

    def test0011(self):
        self.assertEquals(self.calculate(45725.0, -53254.0), -7529.00)

    def test0012(self):
        self.assertEquals(self.calculate(-108048.0, -187939.0), -295987.00)

    def test0013(self):
        self.assertEquals(self.calculate(103179.0, -78271.0), 24908.00)

    def test0014(self):
        self.assertEquals(self.calculate(-56252.0, 60022.0), 3770.00)

    def test0015(self):
        self.assertEquals(self.calculate(119812.0, -114382.0), 5430.00)

    def test0016(self):
        self.assertEquals(self.calculate(4661.0, 116445.0), 121106.00)

    def test0017(self):
        self.assertEquals(self.calculate(61231.0, 89762.0), 150993.00)

    def test0018(self):
        self.assertEquals(self.calculate(160630.0, -145845.0), 14785.00)

    def test0019(self):
        self.assertEquals(self.calculate(-146319.0, -186480.0), -332799.00)

    def test0020(self):
        self.assertEquals(self.calculate(126581.0, -103613.0), 22968.00)

    def test0021(self):
        self.assertEquals(self.calculate(67155.0, -45488.0), 21667.00)

    def test0022(self):
        self.assertEquals(self.calculate(68595.0, -119824.0), -51229.00)

    def test0023(self):
        self.assertEquals(self.calculate(-17720.0, 135552.0), 117832.00)

    def test0024(self):
        self.assertEquals(self.calculate(-27278.0, -52232.0), -79510.00)

    def test0025(self):
        self.assertEquals(self.calculate(91465.0, 198954.0), 290419.00)

    def test0026(self):
        self.assertEquals(self.calculate(-177452.0, 173862.0), -3590.00)

    def test0027(self):
        self.assertEquals(self.calculate(31702.0, 186513.0), 218215.00)

    def test0028(self):
        self.assertEquals(self.calculate(-155782.0, -83289.0), -239071.00)

    def test0029(self):
        self.assertEquals(self.calculate(166380.0, -179825.0), -13445.00)

    def test0030(self):
        self.assertEquals(self.calculate(-42550.0, 157990.0), 115440.00)

    def test0031(self):
        self.assertEquals(self.calculate(-31170.0, 76035.0), 44865.00)

    def test0032(self):
        self.assertEquals(self.calculate(-78214.0, 10679.0), -67535.00)

    def test0033(self):
        self.assertEquals(self.calculate(-76441.0, 99167.0), 22726.00)

    def test0034(self):
        self.assertEquals(self.calculate(64140.0, 198257.0), 262397.00)

    def test0035(self):
        self.assertEquals(self.calculate(195093.0, 55182.0), 250275.00)

    def test0036(self):
        self.assertEquals(self.calculate(92217.0, 81809.0), 174026.00)

    def test0037(self):
        self.assertEquals(self.calculate(-33306.0, -159258.0), -192564.00)

    def test0038(self):
        self.assertEquals(self.calculate(16225.0, -3362.0), 12863.00)

    def test0039(self):
        self.assertEquals(self.calculate(156160.0, -46925.0), 109235.00)

    def test0040(self):
        self.assertEquals(self.calculate(-62034.0, 8700.0), -53334.00)

    def test0041(self):
        self.assertEquals(self.calculate(-132448.0, -181739.0), -314187.00)

    def test0042(self):
        self.assertEquals(self.calculate(53686.0, 162805.0), 216491.00)

    def test0043(self):
        self.assertEquals(self.calculate(26291.0, 42369.0), 68660.00)

    def test0044(self):
        self.assertEquals(self.calculate(-92019.0, 56195.0), -35824.00)

    def test0045(self):
        self.assertEquals(self.calculate(74718.0, -144833.0), -70115.00)

    def test0046(self):
        self.assertEquals(self.calculate(165264.0, -47244.0), 118020.00)

    def test0047(self):
        self.assertEquals(self.calculate(76589.0, -153080.0), -76491.00)

    def test0048(self):
        self.assertEquals(self.calculate(7744.0, 24211.0), 31955.00)

    def test0049(self):
        self.assertEquals(self.calculate(130129.0, 43975.0), 174104.00)

    def test0050(self):
        self.assertEquals(self.calculate(-13125.0, -115138.0), -128263.00)

    def test0051(self):
        self.assertEquals(self.calculate(-177734.0, -26950.0), -204684.00)

    def test0052(self):
        self.assertEquals(self.calculate(-151215.0, -144177.0), -295392.00)

    def test0053(self):
        self.assertEquals(self.calculate(92940.0, 21853.0), 114793.00)

    def test0054(self):
        self.assertEquals(self.calculate(-49252.0, 184732.0), 135480.00)

    def test0055(self):
        self.assertEquals(self.calculate(158784.0, -102456.0), 56328.00)

    def test0056(self):
        self.assertEquals(self.calculate(128991.0, 76696.0), 205687.00)

    def test0057(self):
        self.assertEquals(self.calculate(-139387.0, 113031.0), -26356.00)

    def test0058(self):
        self.assertEquals(self.calculate(156854.0, 124840.0), 281694.00)

    def test0059(self):
        self.assertEquals(self.calculate(151129.0, 98614.0), 249743.00)

    def test0060(self):
        self.assertEquals(self.calculate(-116223.0, -71494.0), -187717.00)

    def test0061(self):
        self.assertEquals(self.calculate(122020.0, -55587.0), 66433.00)

    def test0062(self):
        self.assertEquals(self.calculate(-49932.0, -54426.0), -104358.00)

    def test0063(self):
        self.assertEquals(self.calculate(-180910.0, -19341.0), -200251.00)

    def test0064(self):
        self.assertEquals(self.calculate(-75697.0, 168697.0), 93000.00)

    def test0065(self):
        self.assertEquals(self.calculate(61514.0, 156743.0), 218257.00)

    def test0066(self):
        self.assertEquals(self.calculate(192340.0, -27343.0), 164997.00)

    def test0067(self):
        self.assertEquals(self.calculate(195496.0, -152577.0), 42919.00)

    def test0068(self):
        self.assertEquals(self.calculate(-77917.0, -90174.0), -168091.00)

    def test0069(self):
        self.assertEquals(self.calculate(-148000.0, 91630.0), -56370.00)

    def test0070(self):
        self.assertEquals(self.calculate(-95924.0, -194641.0), -290565.00)

    def test0071(self):
        self.assertEquals(self.calculate(49804.0, -68629.0), -18825.00)

    def test0072(self):
        self.assertEquals(self.calculate(-131271.0, -23259.0), -154530.00)

    def test0073(self):
        self.assertEquals(self.calculate(-187985.0, -65381.0), -253366.00)

    def test0074(self):
        self.assertEquals(self.calculate(-106178.0, 104097.0), -2081.00)

    def test0075(self):
        self.assertEquals(self.calculate(-186962.0, 189711.0), 2749.00)

    def test0076(self):
        self.assertEquals(self.calculate(-41096.0, 163645.0), 122549.00)

    def test0077(self):
        self.assertEquals(self.calculate(64760.0, -171738.0), -106978.00)

    def test0078(self):
        self.assertEquals(self.calculate(-174396.0, -135415.0), -309811.00)

    def test0079(self):
        self.assertEquals(self.calculate(148840.0, -105443.0), 43397.00)

    def test0080(self):
        self.assertEquals(self.calculate(-121662.0, -194454.0), -316116.00)

    def test0081(self):
        self.assertEquals(self.calculate(-45339.0, -46146.0), -91485.00)

    def test0082(self):
        self.assertEquals(self.calculate(167404.0, -154882.0), 12522.00)

    def test0083(self):
        self.assertEquals(self.calculate(-257.0, -121963.0), -122220.00)

    def test0084(self):
        self.assertEquals(self.calculate(95076.0, -98901.0), -3825.00)

    def test0085(self):
        self.assertEquals(self.calculate(-99430.0, 26937.0), -72493.00)

    def test0086(self):
        self.assertEquals(self.calculate(90554.0, -109896.0), -19342.00)

    def test0087(self):
        self.assertEquals(self.calculate(182411.0, 131329.0), 313740.00)

    def test0088(self):
        self.assertEquals(self.calculate(-142447.0, 59443.0), -83004.00)

    def test0089(self):
        self.assertEquals(self.calculate(-36558.0, -76877.0), -113435.00)

    def test0090(self):
        self.assertEquals(self.calculate(-172481.0, 47870.0), -124611.00)

    def test0091(self):
        self.assertEquals(self.calculate(-99500.0, 115497.0), 15997.00)

    def test0092(self):
        self.assertEquals(self.calculate(-18645.0, -188938.0), -207583.00)

    def test0093(self):
        self.assertEquals(self.calculate(1989.0, -14761.0), -12772.00)

    def test0094(self):
        self.assertEquals(self.calculate(-162587.0, 18910.0), -143677.00)

    def test0095(self):
        self.assertEquals(self.calculate(64419.0, 122289.0), 186708.00)

    def test0096(self):
        self.assertEquals(self.calculate(195371.0, -59095.0), 136276.00)

    def test0097(self):
        self.assertEquals(self.calculate(67062.0, -53931.0), 13131.00)

    def test0098(self):
        self.assertEquals(self.calculate(-198864.0, -83344.0), -282208.00)

    def test0099(self):
        self.assertEquals(self.calculate(23299.0, 85278.0), 108577.00)

    def test0100(self):
        self.assertEquals(self.calculate(53771.0, -66577.0), -12806.00)

    def test0101(self):
        self.assertEquals(self.calculate(116041.0, 5590.0), 121631.00)

    def test0102(self):
        self.assertEquals(self.calculate(5896.0, 136876.0), 142772.00)

    def test0103(self):
        self.assertEquals(self.calculate(178778.0, -14119.0), 164659.00)

    def test0104(self):
        self.assertEquals(self.calculate(-183446.0, 196778.0), 13332.00)

    def test0105(self):
        self.assertEquals(self.calculate(172987.0, -78741.0), 94246.00)

    def test0106(self):
        self.assertEquals(self.calculate(120182.0, 7623.0), 127805.00)

    def test0107(self):
        self.assertEquals(self.calculate(-135124.0, -188870.0), -323994.00)

    def test0108(self):
        self.assertEquals(self.calculate(186685.0, 183729.0), 370414.00)

    def test0109(self):
        self.assertEquals(self.calculate(84300.0, -123998.0), -39698.00)

    def test0110(self):
        self.assertEquals(self.calculate(-184923.0, -193617.0), -378540.00)

    def test0111(self):
        self.assertEquals(self.calculate(59145.0, -184294.0), -125149.00)

    def test0112(self):
        self.assertEquals(self.calculate(-76280.0, -34482.0), -110762.00)

    def test0113(self):
        self.assertEquals(self.calculate(-185106.0, -22016.0), -207122.00)

    def test0114(self):
        self.assertEquals(self.calculate(-6276.0, -120817.0), -127093.00)

    def test0115(self):
        self.assertEquals(self.calculate(108149.0, -151808.0), -43659.00)

    def test0116(self):
        self.assertEquals(self.calculate(49812.0, -58979.0), -9167.00)

    def test0117(self):
        self.assertEquals(self.calculate(73367.0, -75218.0), -1851.00)

    def test0118(self):
        self.assertEquals(self.calculate(-46819.0, 71445.0), 24626.00)

    def test0119(self):
        self.assertEquals(self.calculate(-139104.0, 165664.0), 26560.00)

    def test0120(self):
        self.assertEquals(self.calculate(-116801.0, 129732.0), 12931.00)

    def test0121(self):
        self.assertEquals(self.calculate(-133721.0, -101106.0), -234827.00)

    def test0122(self):
        self.assertEquals(self.calculate(2647.0, -172149.0), -169502.00)

    def test0123(self):
        self.assertEquals(self.calculate(-184050.0, 37426.0), -146624.00)

    def test0124(self):
        self.assertEquals(self.calculate(67948.0, -13898.0), 54050.00)

    def test0125(self):
        self.assertEquals(self.calculate(-63258.0, -46202.0), -109460.00)

    def test0126(self):
        self.assertEquals(self.calculate(-34011.0, 175765.0), 141754.00)

    def test0127(self):
        self.assertEquals(self.calculate(-142656.0, 91935.0), -50721.00)

    def test0128(self):
        self.assertEquals(self.calculate(-68923.0, 176957.0), 108034.00)

    def test0129(self):
        self.assertEquals(self.calculate(-113338.0, 34033.0), -79305.00)

    def test0130(self):
        self.assertEquals(self.calculate(72325.0, 191200.0), 263525.00)

    def test0131(self):
        self.assertEquals(self.calculate(51892.0, 116719.0), 168611.00)

    def test0132(self):
        self.assertEquals(self.calculate(-171321.0, 154847.0), -16474.00)

    def test0133(self):
        self.assertEquals(self.calculate(-95352.0, 132744.0), 37392.00)

    def test0134(self):
        self.assertEquals(self.calculate(-49983.0, 47027.0), -2956.00)

    def test0135(self):
        self.assertEquals(self.calculate(-101145.0, -9529.0), -110674.00)

    def test0136(self):
        self.assertEquals(self.calculate(-54409.0, 46801.0), -7608.00)

    def test0137(self):
        self.assertEquals(self.calculate(-199962.0, 13456.0), -186506.00)

    def test0138(self):
        self.assertEquals(self.calculate(27716.0, 126686.0), 154402.00)

    def test0139(self):
        self.assertEquals(self.calculate(136612.0, 31094.0), 167706.00)

    def test0140(self):
        self.assertEquals(self.calculate(184949.0, -42812.0), 142137.00)

    def test0141(self):
        self.assertEquals(self.calculate(-78425.0, -44890.0), -123315.00)

    def test0142(self):
        self.assertEquals(self.calculate(102385.0, -68122.0), 34263.00)

    def test0143(self):
        self.assertEquals(self.calculate(195130.0, 198208.0), 393338.00)

    def test0144(self):
        self.assertEquals(self.calculate(132523.0, 158144.0), 290667.00)

    def test0145(self):
        self.assertEquals(self.calculate(-97012.0, -194386.0), -291398.00)

    def test0146(self):
        self.assertEquals(self.calculate(-103237.0, 98526.0), -4711.00)

    def test0147(self):
        self.assertEquals(self.calculate(57921.0, 75490.0), 133411.00)

    def test0148(self):
        self.assertEquals(self.calculate(-111886.0, -47306.0), -159192.00)

    def test0149(self):
        self.assertEquals(self.calculate(-90034.0, 157560.0), 67526.00)

    def test0150(self):
        self.assertEquals(self.calculate(3724.0, -10983.0), -7259.00)

    def test0151(self):
        self.assertEquals(self.calculate(-176855.0, -2137.0), -178992.00)

    def test0152(self):
        self.assertEquals(self.calculate(-96080.0, -26052.0), -122132.00)

    def test0153(self):
        self.assertEquals(self.calculate(193605.0, -178295.0), 15310.00)

    def test0154(self):
        self.assertEquals(self.calculate(117683.0, -168394.0), -50711.00)

    def test0155(self):
        self.assertEquals(self.calculate(139656.0, -40109.0), 99547.00)

    def test0156(self):
        self.assertEquals(self.calculate(-198436.0, 61371.0), -137065.00)

    def test0157(self):
        self.assertEquals(self.calculate(-4975.0, 94596.0), 89621.00)

    def test0158(self):
        self.assertEquals(self.calculate(32593.0, -168889.0), -136296.00)

    def test0159(self):
        self.assertEquals(self.calculate(116619.0, 52842.0), 169461.00)

    def test0160(self):
        self.assertEquals(self.calculate(-43660.0, 27988.0), -15672.00)

    def test0161(self):
        self.assertEquals(self.calculate(131297.0, 7138.0), 138435.00)

    def test0162(self):
        self.assertEquals(self.calculate(-192492.0, 55135.0), -137357.00)

    def test0163(self):
        self.assertEquals(self.calculate(197021.0, 188362.0), 385383.00)

    def test0164(self):
        self.assertEquals(self.calculate(113144.0, 127102.0), 240246.00)

    def test0165(self):
        self.assertEquals(self.calculate(166194.0, -168367.0), -2173.00)

    def test0166(self):
        self.assertEquals(self.calculate(-35118.0, 69303.0), 34185.00)

    def test0167(self):
        self.assertEquals(self.calculate(178555.0, -112514.0), 66041.00)

    def test0168(self):
        self.assertEquals(self.calculate(-156534.0, -66123.0), -222657.00)

    def test0169(self):
        self.assertEquals(self.calculate(147186.0, 28934.0), 176120.00)

    def test0170(self):
        self.assertEquals(self.calculate(-25044.0, 170604.0), 145560.00)

    def test0171(self):
        self.assertEquals(self.calculate(83199.0, 115401.0), 198600.00)

    def test0172(self):
        self.assertEquals(self.calculate(55003.0, 38615.0), 93618.00)

    def test0173(self):
        self.assertEquals(self.calculate(28153.0, 140205.0), 168358.00)

    def test0174(self):
        self.assertEquals(self.calculate(-144891.0, 155516.0), 10625.00)

    def test0175(self):
        self.assertEquals(self.calculate(120767.0, -14235.0), 106532.00)

    def test0176(self):
        self.assertEquals(self.calculate(54660.0, -175926.0), -121266.00)

    def test0177(self):
        self.assertEquals(self.calculate(35148.0, 43191.0), 78339.00)

    def test0178(self):
        self.assertEquals(self.calculate(60461.0, -120090.0), -59629.00)

    def test0179(self):
        self.assertEquals(self.calculate(-46688.0, 199532.0), 152844.00)

    def test0180(self):
        self.assertEquals(self.calculate(198243.0, 76486.0), 274729.00)

    def test0181(self):
        self.assertEquals(self.calculate(-39111.0, -2763.0), -41874.00)

    def test0182(self):
        self.assertEquals(self.calculate(-106997.0, 101802.0), -5195.00)

    def test0183(self):
        self.assertEquals(self.calculate(195294.0, -102717.0), 92577.00)

    def test0184(self):
        self.assertEquals(self.calculate(-13227.0, -158793.0), -172020.00)

    def test0185(self):
        self.assertEquals(self.calculate(-181707.0, -168874.0), -350581.00)

    def test0186(self):
        self.assertEquals(self.calculate(39298.0, -102995.0), -63697.00)

    def test0187(self):
        self.assertEquals(self.calculate(-110418.0, -50658.0), -161076.00)

    def test0188(self):
        self.assertEquals(self.calculate(-55504.0, -169109.0), -224613.00)

    def test0189(self):
        self.assertEquals(self.calculate(71266.0, 123213.0), 194479.00)

    def test0190(self):
        self.assertEquals(self.calculate(-147699.0, -126074.0), -273773.00)

    def test0191(self):
        self.assertEquals(self.calculate(-78689.0, -32963.0), -111652.00)

    def test0192(self):
        self.assertEquals(self.calculate(2338.0, -156631.0), -154293.00)

    def test0193(self):
        self.assertEquals(self.calculate(119385.0, 184998.0), 304383.00)

    def test0194(self):
        self.assertEquals(self.calculate(54364.0, -21492.0), 32872.00)

    def test0195(self):
        self.assertEquals(self.calculate(66378.0, -56222.0), 10156.00)

    def test0196(self):
        self.assertEquals(self.calculate(-21859.0, -90803.0), -112662.00)

    def test0197(self):
        self.assertEquals(self.calculate(48704.0, 67234.0), 115938.00)

    def test0198(self):
        self.assertEquals(self.calculate(-65681.0, 42374.0), -23307.00)

    def test0199(self):
        self.assertEquals(self.calculate(-33998.0, -197364.0), -231362.00)

    def test0200(self):
        self.assertEquals(self.calculate(-146747.0, -137070.0), -283817.00)

    def test0201(self):
        self.assertEquals(self.calculate(176927.0, -14601.0), 162326.00)

    def test0202(self):
        self.assertEquals(self.calculate(145855.0, -94051.0), 51804.00)

    def test0203(self):
        self.assertEquals(self.calculate(31219.0, -96223.0), -65004.00)

    def test0204(self):
        self.assertEquals(self.calculate(127418.0, 95583.0), 223001.00)

    def test0205(self):
        self.assertEquals(self.calculate(-197968.0, -166045.0), -364013.00)

    def test0206(self):
        self.assertEquals(self.calculate(172382.0, 64125.0), 236507.00)

    def test0207(self):
        self.assertEquals(self.calculate(-148412.0, 46276.0), -102136.00)

    def test0208(self):
        self.assertEquals(self.calculate(83756.0, -144560.0), -60804.00)

    def test0209(self):
        self.assertEquals(self.calculate(-125378.0, -122300.0), -247678.00)

    def test0210(self):
        self.assertEquals(self.calculate(-59476.0, -66778.0), -126254.00)

    def test0211(self):
        self.assertEquals(self.calculate(-28324.0, 86148.0), 57824.00)

    def test0212(self):
        self.assertEquals(self.calculate(-57148.0, -66344.0), -123492.00)

    def test0213(self):
        self.assertEquals(self.calculate(-131293.0, -97142.0), -228435.00)

    def test0214(self):
        self.assertEquals(self.calculate(-145940.0, -103982.0), -249922.00)

    def test0215(self):
        self.assertEquals(self.calculate(27983.0, -9823.0), 18160.00)

    def test0216(self):
        self.assertEquals(self.calculate(-145232.0, 140448.0), -4784.00)

    def test0217(self):
        self.assertEquals(self.calculate(-822.0, 132754.0), 131932.00)

    def test0218(self):
        self.assertEquals(self.calculate(186492.0, -177539.0), 8953.00)

    def test0219(self):
        self.assertEquals(self.calculate(-171088.0, -155401.0), -326489.00)

    def test0220(self):
        self.assertEquals(self.calculate(4505.0, -155007.0), -150502.00)

    def test0221(self):
        self.assertEquals(self.calculate(119593.0, 103810.0), 223403.00)

    def test0222(self):
        self.assertEquals(self.calculate(180202.0, 11555.0), 191757.00)

    def test0223(self):
        self.assertEquals(self.calculate(79153.0, -4333.0), 74820.00)

    def test0224(self):
        self.assertEquals(self.calculate(100219.0, 106334.0), 206553.00)

    def test0225(self):
        self.assertEquals(self.calculate(151361.0, 193099.0), 344460.00)

    def test0226(self):
        self.assertEquals(self.calculate(71855.0, 178567.0), 250422.00)

    def test0227(self):
        self.assertEquals(self.calculate(169623.0, -151262.0), 18361.00)

    def test0228(self):
        self.assertEquals(self.calculate(-79871.0, 186788.0), 106917.00)

    def test0229(self):
        self.assertEquals(self.calculate(120140.0, 102309.0), 222449.00)

    def test0230(self):
        self.assertEquals(self.calculate(-166407.0, 51000.0), -115407.00)

    def test0231(self):
        self.assertEquals(self.calculate(151044.0, 125523.0), 276567.00)

    def test0232(self):
        self.assertEquals(self.calculate(-15557.0, 72343.0), 56786.00)

    def test0233(self):
        self.assertEquals(self.calculate(152421.0, 35376.0), 187797.00)

    def test0234(self):
        self.assertEquals(self.calculate(109141.0, 196535.0), 305676.00)

    def test0235(self):
        self.assertEquals(self.calculate(-84632.0, -123864.0), -208496.00)

    def test0236(self):
        self.assertEquals(self.calculate(11019.0, -104805.0), -93786.00)

    def test0237(self):
        self.assertEquals(self.calculate(-27770.0, 166744.0), 138974.00)

    def test0238(self):
        self.assertEquals(self.calculate(-74344.0, -193275.0), -267619.00)

    def test0239(self):
        self.assertEquals(self.calculate(186697.0, -151031.0), 35666.00)

    def test0240(self):
        self.assertEquals(self.calculate(1806.0, -183344.0), -181538.00)

    def test0241(self):
        self.assertEquals(self.calculate(107816.0, 94825.0), 202641.00)

    def test0242(self):
        self.assertEquals(self.calculate(-26684.0, 33533.0), 6849.00)

    def test0243(self):
        self.assertEquals(self.calculate(125498.0, 166318.0), 291816.00)

    def test0244(self):
        self.assertEquals(self.calculate(-32936.0, -78556.0), -111492.00)

    def test0245(self):
        self.assertEquals(self.calculate(105099.0, 73280.0), 178379.00)

    def test0246(self):
        self.assertEquals(self.calculate(45645.0, -185702.0), -140057.00)

    def test0247(self):
        self.assertEquals(self.calculate(-87502.0, -92370.0), -179872.00)

    def test0248(self):
        self.assertEquals(self.calculate(-176590.0, -29328.0), -205918.00)

    def test0249(self):
        self.assertEquals(self.calculate(86705.0, 107758.0), 194463.00)

    def test0250(self):
        self.assertEquals(self.calculate(-148966.0, -19846.0), -168812.00)

    def test0251(self):
        self.assertEquals(self.calculate(34289.0, 173567.0), 207856.00)

    def test0252(self):
        self.assertEquals(self.calculate(-62496.0, -43248.0), -105744.00)

    def test0253(self):
        self.assertEquals(self.calculate(165042.0, 29815.0), 194857.00)

    def test0254(self):
        self.assertEquals(self.calculate(-54182.0, 40643.0), -13539.00)

    def test0255(self):
        self.assertEquals(self.calculate(-39478.0, -31593.0), -71071.00)

    def test0256(self):
        self.assertEquals(self.calculate(-36371.0, -39702.0), -76073.00)

    def test0257(self):
        self.assertEquals(self.calculate(29223.0, -115915.0), -86692.00)

    def test0258(self):
        self.assertEquals(self.calculate(193898.0, 191076.0), 384974.00)

    def test0259(self):
        self.assertEquals(self.calculate(-75505.0, -53103.0), -128608.00)

    def test0260(self):
        self.assertEquals(self.calculate(172584.0, 175050.0), 347634.00)

    def test0261(self):
        self.assertEquals(self.calculate(29955.0, 68836.0), 98791.00)

    def test0262(self):
        self.assertEquals(self.calculate(-177655.0, 188497.0), 10842.00)

    def test0263(self):
        self.assertEquals(self.calculate(90492.0, 100362.0), 190854.00)

    def test0264(self):
        self.assertEquals(self.calculate(93582.0, 74800.0), 168382.00)

    def test0265(self):
        self.assertEquals(self.calculate(-39407.0, -127070.0), -166477.00)

    def test0266(self):
        self.assertEquals(self.calculate(108879.0, 144670.0), 253549.00)

    def test0267(self):
        self.assertEquals(self.calculate(15467.0, 183187.0), 198654.00)

    def test0268(self):
        self.assertEquals(self.calculate(-128670.0, -163160.0), -291830.00)

    def test0269(self):
        self.assertEquals(self.calculate(101230.0, 140987.0), 242217.00)

    def test0270(self):
        self.assertEquals(self.calculate(-178035.0, 190242.0), 12207.00)

    def test0271(self):
        self.assertEquals(self.calculate(136977.0, -123312.0), 13665.00)

    def test0272(self):
        self.assertEquals(self.calculate(-123620.0, 120368.0), -3252.00)

    def test0273(self):
        self.assertEquals(self.calculate(79758.0, 158561.0), 238319.00)

    def test0274(self):
        self.assertEquals(self.calculate(109848.0, -27150.0), 82698.00)

    def test0275(self):
        self.assertEquals(self.calculate(194231.0, -180053.0), 14178.00)

    def test0276(self):
        self.assertEquals(self.calculate(112648.0, 47140.0), 159788.00)

    def test0277(self):
        self.assertEquals(self.calculate(-51881.0, 109118.0), 57237.00)

    def test0278(self):
        self.assertEquals(self.calculate(-132074.0, 40571.0), -91503.00)

    def test0279(self):
        self.assertEquals(self.calculate(-181440.0, 72908.0), -108532.00)

    def test0280(self):
        self.assertEquals(self.calculate(-74500.0, 186718.0), 112218.00)

    def test0281(self):
        self.assertEquals(self.calculate(17089.0, -64968.0), -47879.00)

    def test0282(self):
        self.assertEquals(self.calculate(97303.0, 38376.0), 135679.00)

    def test0283(self):
        self.assertEquals(self.calculate(199496.0, 43921.0), 243417.00)

    def test0284(self):
        self.assertEquals(self.calculate(59932.0, 190057.0), 249989.00)

    def test0285(self):
        self.assertEquals(self.calculate(-69480.0, 159208.0), 89728.00)

    def test0286(self):
        self.assertEquals(self.calculate(-186513.0, -57577.0), -244090.00)

    def test0287(self):
        self.assertEquals(self.calculate(-72774.0, 37627.0), -35147.00)

    def test0288(self):
        self.assertEquals(self.calculate(48883.0, 56536.0), 105419.00)

    def test0289(self):
        self.assertEquals(self.calculate(21961.0, -92422.0), -70461.00)

    def test0290(self):
        self.assertEquals(self.calculate(172229.0, 170060.0), 342289.00)

    def test0291(self):
        self.assertEquals(self.calculate(171096.0, -118517.0), 52579.00)

    def test0292(self):
        self.assertEquals(self.calculate(-20532.0, -12153.0), -32685.00)

    def test0293(self):
        self.assertEquals(self.calculate(824.0, 65704.0), 66528.00)

    def test0294(self):
        self.assertEquals(self.calculate(173458.0, -77730.0), 95728.00)

    def test0295(self):
        self.assertEquals(self.calculate(174332.0, -41854.0), 132478.00)

    def test0296(self):
        self.assertEquals(self.calculate(-126.0, -174882.0), -175008.00)

    def test0297(self):
        self.assertEquals(self.calculate(-163636.0, -103366.0), -267002.00)

    def test0298(self):
        self.assertEquals(self.calculate(13140.0, 52464.0), 65604.00)

    def test0299(self):
        self.assertEquals(self.calculate(120150.0, -143619.0), -23469.00)

    def test0300(self):
        self.assertEquals(self.calculate(-45987.0, 21844.0), -24143.00)

    def test0301(self):
        self.assertEquals(self.calculate(119956.0, 191828.0), 311784.00)

    def test0302(self):
        self.assertEquals(self.calculate(-57950.0, 107839.0), 49889.00)

    def test0303(self):
        self.assertEquals(self.calculate(-67892.0, 120297.0), 52405.00)

    def test0304(self):
        self.assertEquals(self.calculate(-74728.0, 144642.0), 69914.00)

    def test0305(self):
        self.assertEquals(self.calculate(-56487.0, 120839.0), 64352.00)

    def test0306(self):
        self.assertEquals(self.calculate(-100996.0, -146726.0), -247722.00)

    def test0307(self):
        self.assertEquals(self.calculate(-61001.0, -147328.0), -208329.00)

    def test0308(self):
        self.assertEquals(self.calculate(-8886.0, 67369.0), 58483.00)

    def test0309(self):
        self.assertEquals(self.calculate(142605.0, -133236.0), 9369.00)

    def test0310(self):
        self.assertEquals(self.calculate(-192979.0, -177895.0), -370874.00)

    def test0311(self):
        self.assertEquals(self.calculate(40058.0, 112746.0), 152804.00)

    def test0312(self):
        self.assertEquals(self.calculate(-105876.0, -101482.0), -207358.00)

    def test0313(self):
        self.assertEquals(self.calculate(-118816.0, 176250.0), 57434.00)

    def test0314(self):
        self.assertEquals(self.calculate(-62308.0, -94388.0), -156696.00)

    def test0315(self):
        self.assertEquals(self.calculate(-55726.0, 194516.0), 138790.00)

    def test0316(self):
        self.assertEquals(self.calculate(-47674.0, -41500.0), -89174.00)

    def test0317(self):
        self.assertEquals(self.calculate(186149.0, 154794.0), 340943.00)

    def test0318(self):
        self.assertEquals(self.calculate(162736.0, 14713.0), 177449.00)

    def test0319(self):
        self.assertEquals(self.calculate(-53989.0, -95322.0), -149311.00)

    def test0320(self):
        self.assertEquals(self.calculate(20769.0, 198781.0), 219550.00)

    def test0321(self):
        self.assertEquals(self.calculate(-35756.0, -140267.0), -176023.00)

    def test0322(self):
        self.assertEquals(self.calculate(-141627.0, 12423.0), -129204.00)

    def test0323(self):
        self.assertEquals(self.calculate(-11307.0, -54372.0), -65679.00)

    def test0324(self):
        self.assertEquals(self.calculate(149932.0, -1217.0), 148715.00)

    def test0325(self):
        self.assertEquals(self.calculate(186931.0, -182198.0), 4733.00)

    def test0326(self):
        self.assertEquals(self.calculate(41428.0, -95807.0), -54379.00)

    def test0327(self):
        self.assertEquals(self.calculate(59260.0, 177877.0), 237137.00)

    def test0328(self):
        self.assertEquals(self.calculate(-112661.0, -98670.0), -211331.00)

    def test0329(self):
        self.assertEquals(self.calculate(-12786.0, 171716.0), 158930.00)

    def test0330(self):
        self.assertEquals(self.calculate(-20468.0, 172120.0), 151652.00)

    def test0331(self):
        self.assertEquals(self.calculate(-23290.0, 181809.0), 158519.00)

    def test0332(self):
        self.assertEquals(self.calculate(-112692.0, 181220.0), 68528.00)

    def test0333(self):
        self.assertEquals(self.calculate(44067.0, 197136.0), 241203.00)

    def test0334(self):
        self.assertEquals(self.calculate(-64947.0, 110774.0), 45827.00)

    def test0335(self):
        self.assertEquals(self.calculate(-175551.0, -98165.0), -273716.00)

    def test0336(self):
        self.assertEquals(self.calculate(156514.0, 112946.0), 269460.00)

    def test0337(self):
        self.assertEquals(self.calculate(-44965.0, 132707.0), 87742.00)

    def test0338(self):
        self.assertEquals(self.calculate(-90319.0, 27689.0), -62630.00)

    def test0339(self):
        self.assertEquals(self.calculate(11429.0, 147830.0), 159259.00)

    def test0340(self):
        self.assertEquals(self.calculate(-30363.0, -2403.0), -32766.00)

    def test0341(self):
        self.assertEquals(self.calculate(-98406.0, -28744.0), -127150.00)

    def test0342(self):
        self.assertEquals(self.calculate(-51710.0, 105875.0), 54165.00)

    def test0343(self):
        self.assertEquals(self.calculate(4.0, 53844.0), 53848.00)

    def test0344(self):
        self.assertEquals(self.calculate(-191349.0, 58861.0), -132488.00)

    def test0345(self):
        self.assertEquals(self.calculate(118902.0, 95905.0), 214807.00)

    def test0346(self):
        self.assertEquals(self.calculate(-199127.0, -56356.0), -255483.00)

    def test0347(self):
        self.assertEquals(self.calculate(-129635.0, 178372.0), 48737.00)

    def test0348(self):
        self.assertEquals(self.calculate(108057.0, -87072.0), 20985.00)

    def test0349(self):
        self.assertEquals(self.calculate(-197153.0, 159399.0), -37754.00)

    def test0350(self):
        self.assertEquals(self.calculate(182073.0, 109505.0), 291578.00)

    def test0351(self):
        self.assertEquals(self.calculate(154440.0, 22380.0), 176820.00)

    def test0352(self):
        self.assertEquals(self.calculate(49582.0, 39360.0), 88942.00)

    def test0353(self):
        self.assertEquals(self.calculate(-47401.0, -14651.0), -62052.00)

    def test0354(self):
        self.assertEquals(self.calculate(53784.0, 2540.0), 56324.00)

    def test0355(self):
        self.assertEquals(self.calculate(-29549.0, -110494.0), -140043.00)

    def test0356(self):
        self.assertEquals(self.calculate(71052.0, -113588.0), -42536.00)

    def test0357(self):
        self.assertEquals(self.calculate(-144368.0, 36214.0), -108154.00)

    def test0358(self):
        self.assertEquals(self.calculate(-114870.0, 181937.0), 67067.00)

    def test0359(self):
        self.assertEquals(self.calculate(-196934.0, 21198.0), -175736.00)

    def test0360(self):
        self.assertEquals(self.calculate(45202.0, 21371.0), 66573.00)

    def test0361(self):
        self.assertEquals(self.calculate(-95108.0, 4004.0), -91104.00)

    def test0362(self):
        self.assertEquals(self.calculate(32789.0, 83895.0), 116684.00)

    def test0363(self):
        self.assertEquals(self.calculate(-199586.0, 186769.0), -12817.00)

    def test0364(self):
        self.assertEquals(self.calculate(-165883.0, 44442.0), -121441.00)

    def test0365(self):
        self.assertEquals(self.calculate(-106499.0, -35200.0), -141699.00)

    def test0366(self):
        self.assertEquals(self.calculate(42707.0, 65930.0), 108637.00)

    def test0367(self):
        self.assertEquals(self.calculate(-166134.0, -168080.0), -334214.00)

    def test0368(self):
        self.assertEquals(self.calculate(-20682.0, 98771.0), 78089.00)

    def test0369(self):
        self.assertEquals(self.calculate(-97900.0, 13538.0), -84362.00)

    def test0370(self):
        self.assertEquals(self.calculate(-172286.0, 141324.0), -30962.00)

    def test0371(self):
        self.assertEquals(self.calculate(24366.0, 80063.0), 104429.00)

    def test0372(self):
        self.assertEquals(self.calculate(-115111.0, -166238.0), -281349.00)

    def test0373(self):
        self.assertEquals(self.calculate(-160486.0, -38550.0), -199036.00)

    def test0374(self):
        self.assertEquals(self.calculate(-116561.0, 87868.0), -28693.00)

    def test0375(self):
        self.assertEquals(self.calculate(42517.0, -157014.0), -114497.00)

    def test0376(self):
        self.assertEquals(self.calculate(-77159.0, 31255.0), -45904.00)

    def test0377(self):
        self.assertEquals(self.calculate(44096.0, -179781.0), -135685.00)

    def test0378(self):
        self.assertEquals(self.calculate(-45177.0, -124076.0), -169253.00)

    def test0379(self):
        self.assertEquals(self.calculate(-148924.0, -135383.0), -284307.00)

    def test0380(self):
        self.assertEquals(self.calculate(-178190.0, 93351.0), -84839.00)

    def test0381(self):
        self.assertEquals(self.calculate(-157107.0, -64917.0), -222024.00)

    def test0382(self):
        self.assertEquals(self.calculate(-170776.0, -159419.0), -330195.00)

    def test0383(self):
        self.assertEquals(self.calculate(-182122.0, 151640.0), -30482.00)

    def test0384(self):
        self.assertEquals(self.calculate(139764.0, 81911.0), 221675.00)

    def test0385(self):
        self.assertEquals(self.calculate(-147740.0, 93592.0), -54148.00)

    def test0386(self):
        self.assertEquals(self.calculate(-140059.0, -36215.0), -176274.00)

    def test0387(self):
        self.assertEquals(self.calculate(197172.0, -56958.0), 140214.00)

    def test0388(self):
        self.assertEquals(self.calculate(25299.0, -48219.0), -22920.00)

    def test0389(self):
        self.assertEquals(self.calculate(-43031.0, -131298.0), -174329.00)

    def test0390(self):
        self.assertEquals(self.calculate(154198.0, 53077.0), 207275.00)

    def test0391(self):
        self.assertEquals(self.calculate(153539.0, 141084.0), 294623.00)

    def test0392(self):
        self.assertEquals(self.calculate(70613.0, -39603.0), 31010.00)

    def test0393(self):
        self.assertEquals(self.calculate(11772.0, -73771.0), -61999.00)

    def test0394(self):
        self.assertEquals(self.calculate(-79190.0, 5742.0), -73448.00)

    def test0395(self):
        self.assertEquals(self.calculate(177338.0, -74912.0), 102426.00)

    def test0396(self):
        self.assertEquals(self.calculate(76481.0, 168632.0), 245113.00)

    def test0397(self):
        self.assertEquals(self.calculate(-112889.0, -101262.0), -214151.00)

    def test0398(self):
        self.assertEquals(self.calculate(-1593.0, -137061.0), -138654.00)

    def test0399(self):
        self.assertEquals(self.calculate(163460.0, -187809.0), -24349.00)

    def test0400(self):
        self.assertEquals(self.calculate(93118.0, 37925.0), 131043.00)

    def test0401(self):
        self.assertEquals(self.calculate(-186334.0, 110077.0), -76257.00)

    def test0402(self):
        self.assertEquals(self.calculate(-185551.0, -143976.0), -329527.00)

    def test0403(self):
        self.assertEquals(self.calculate(-84353.0, -160256.0), -244609.00)

    def test0404(self):
        self.assertEquals(self.calculate(194255.0, 199113.0), 393368.00)

    def test0405(self):
        self.assertEquals(self.calculate(148098.0, 24879.0), 172977.00)

    def test0406(self):
        self.assertEquals(self.calculate(166711.0, 88733.0), 255444.00)

    def test0407(self):
        self.assertEquals(self.calculate(-89475.0, -85447.0), -174922.00)

    def test0408(self):
        self.assertEquals(self.calculate(-94167.0, 195574.0), 101407.00)

    def test0409(self):
        self.assertEquals(self.calculate(167774.0, 20764.0), 188538.00)

    def test0410(self):
        self.assertEquals(self.calculate(150181.0, -4307.0), 145874.00)

    def test0411(self):
        self.assertEquals(self.calculate(-176686.0, -164614.0), -341300.00)

    def test0412(self):
        self.assertEquals(self.calculate(-179023.0, 122506.0), -56517.00)

    def test0413(self):
        self.assertEquals(self.calculate(93219.0, 124809.0), 218028.00)

    def test0414(self):
        self.assertEquals(self.calculate(185171.0, -52613.0), 132558.00)

    def test0415(self):
        self.assertEquals(self.calculate(-88220.0, -95314.0), -183534.00)

    def test0416(self):
        self.assertEquals(self.calculate(-149823.0, 81249.0), -68574.00)

    def test0417(self):
        self.assertEquals(self.calculate(-75222.0, -75043.0), -150265.00)

    def test0418(self):
        self.assertEquals(self.calculate(104717.0, -42627.0), 62090.00)

    def test0419(self):
        self.assertEquals(self.calculate(-63425.0, -151488.0), -214913.00)

    def test0420(self):
        self.assertEquals(self.calculate(-77232.0, -50347.0), -127579.00)

    def test0421(self):
        self.assertEquals(self.calculate(-156086.0, 10238.0), -145848.00)

    def test0422(self):
        self.assertEquals(self.calculate(-7895.0, -178195.0), -186090.00)

    def test0423(self):
        self.assertEquals(self.calculate(-93527.0, 199620.0), 106093.00)

    def test0424(self):
        self.assertEquals(self.calculate(101389.0, 72911.0), 174300.00)

    def test0425(self):
        self.assertEquals(self.calculate(198561.0, -45707.0), 152854.00)

    def test0426(self):
        self.assertEquals(self.calculate(192548.0, 153634.0), 346182.00)

    def test0427(self):
        self.assertEquals(self.calculate(182257.0, -16367.0), 165890.00)

    def test0428(self):
        self.assertEquals(self.calculate(119433.0, -135076.0), -15643.00)

    def test0429(self):
        self.assertEquals(self.calculate(-89048.0, -62372.0), -151420.00)

    def test0430(self):
        self.assertEquals(self.calculate(-64981.0, -162053.0), -227034.00)

    def test0431(self):
        self.assertEquals(self.calculate(40758.0, 53400.0), 94158.00)

    def test0432(self):
        self.assertEquals(self.calculate(-99661.0, 48279.0), -51382.00)

    def test0433(self):
        self.assertEquals(self.calculate(-104119.0, 179263.0), 75144.00)

    def test0434(self):
        self.assertEquals(self.calculate(-63644.0, -134461.0), -198105.00)

    def test0435(self):
        self.assertEquals(self.calculate(109372.0, 36564.0), 145936.00)

    def test0436(self):
        self.assertEquals(self.calculate(49917.0, 127142.0), 177059.00)

    def test0437(self):
        self.assertEquals(self.calculate(87960.0, -101937.0), -13977.00)

    def test0438(self):
        self.assertEquals(self.calculate(-122305.0, 97276.0), -25029.00)

    def test0439(self):
        self.assertEquals(self.calculate(-25474.0, -190519.0), -215993.00)

    def test0440(self):
        self.assertEquals(self.calculate(98514.0, 125888.0), 224402.00)

    def test0441(self):
        self.assertEquals(self.calculate(179624.0, -97547.0), 82077.00)

    def test0442(self):
        self.assertEquals(self.calculate(-105739.0, 35240.0), -70499.00)

    def test0443(self):
        self.assertEquals(self.calculate(140504.0, -70273.0), 70231.00)

    def test0444(self):
        self.assertEquals(self.calculate(-45037.0, 49312.0), 4275.00)

    def test0445(self):
        self.assertEquals(self.calculate(-157586.0, 27313.0), -130273.00)

    def test0446(self):
        self.assertEquals(self.calculate(-53086.0, -30826.0), -83912.00)

    def test0447(self):
        self.assertEquals(self.calculate(-155691.0, -198963.0), -354654.00)

    def test0448(self):
        self.assertEquals(self.calculate(-130867.0, 78045.0), -52822.00)

    def test0449(self):
        self.assertEquals(self.calculate(-29936.0, 601.0), -29335.00)

    def test0450(self):
        self.assertEquals(self.calculate(-61708.0, -10458.0), -72166.00)

    def test0451(self):
        self.assertEquals(self.calculate(159807.0, 37201.0), 197008.00)

    def test0452(self):
        self.assertEquals(self.calculate(-141405.0, -87710.0), -229115.00)

    def test0453(self):
        self.assertEquals(self.calculate(97910.0, 15997.0), 113907.00)

    def test0454(self):
        self.assertEquals(self.calculate(74608.0, -52069.0), 22539.00)

    def test0455(self):
        self.assertEquals(self.calculate(-170917.0, 148649.0), -22268.00)

    def test0456(self):
        self.assertEquals(self.calculate(63500.0, -122611.0), -59111.00)

    def test0457(self):
        self.assertEquals(self.calculate(72508.0, 187586.0), 260094.00)

    def test0458(self):
        self.assertEquals(self.calculate(35122.0, 128673.0), 163795.00)

    def test0459(self):
        self.assertEquals(self.calculate(195824.0, 58309.0), 254133.00)

    def test0460(self):
        self.assertEquals(self.calculate(100223.0, 173671.0), 273894.00)

    def test0461(self):
        self.assertEquals(self.calculate(103248.0, 35186.0), 138434.00)

    def test0462(self):
        self.assertEquals(self.calculate(166560.0, -164110.0), 2450.00)

    def test0463(self):
        self.assertEquals(self.calculate(88142.0, 65755.0), 153897.00)

    def test0464(self):
        self.assertEquals(self.calculate(-151770.0, 14019.0), -137751.00)

    def test0465(self):
        self.assertEquals(self.calculate(-28762.0, -180276.0), -209038.00)

    def test0466(self):
        self.assertEquals(self.calculate(48813.0, 58216.0), 107029.00)

    def test0467(self):
        self.assertEquals(self.calculate(19852.0, 133430.0), 153282.00)

    def test0468(self):
        self.assertEquals(self.calculate(103506.0, -1919.0), 101587.00)

    def test0469(self):
        self.assertEquals(self.calculate(114820.0, 131711.0), 246531.00)

    def test0470(self):
        self.assertEquals(self.calculate(-16524.0, -6551.0), -23075.00)

    def test0471(self):
        self.assertEquals(self.calculate(183764.0, 12682.0), 196446.00)

    def test0472(self):
        self.assertEquals(self.calculate(135130.0, -143751.0), -8621.00)

    def test0473(self):
        self.assertEquals(self.calculate(160439.0, 140262.0), 300701.00)

    def test0474(self):
        self.assertEquals(self.calculate(-53215.0, 4855.0), -48360.00)

    def test0475(self):
        self.assertEquals(self.calculate(-144251.0, -93962.0), -238213.00)

    def test0476(self):
        self.assertEquals(self.calculate(-113715.0, -170784.0), -284499.00)

    def test0477(self):
        self.assertEquals(self.calculate(150480.0, -111012.0), 39468.00)

    def test0478(self):
        self.assertEquals(self.calculate(-21167.0, -44767.0), -65934.00)

    def test0479(self):
        self.assertEquals(self.calculate(162939.0, -116779.0), 46160.00)

    def test0480(self):
        self.assertEquals(self.calculate(133606.0, 138192.0), 271798.00)

    def test0481(self):
        self.assertEquals(self.calculate(172995.0, -115687.0), 57308.00)

    def test0482(self):
        self.assertEquals(self.calculate(-59905.0, -162855.0), -222760.00)

    def test0483(self):
        self.assertEquals(self.calculate(-129997.0, -113019.0), -243016.00)

    def test0484(self):
        self.assertEquals(self.calculate(159382.0, 134576.0), 293958.00)

    def test0485(self):
        self.assertEquals(self.calculate(-128889.0, 123592.0), -5297.00)

    def test0486(self):
        self.assertEquals(self.calculate(120256.0, -94433.0), 25823.00)

    def test0487(self):
        self.assertEquals(self.calculate(194462.0, -174504.0), 19958.00)

    def test0488(self):
        self.assertEquals(self.calculate(-167962.0, -12373.0), -180335.00)

    def test0489(self):
        self.assertEquals(self.calculate(-181752.0, 129614.0), -52138.00)

    def test0490(self):
        self.assertEquals(self.calculate(120725.0, -48683.0), 72042.00)

    def test0491(self):
        self.assertEquals(self.calculate(-194414.0, -121022.0), -315436.00)

    def test0492(self):
        self.assertEquals(self.calculate(174361.0, 60232.0), 234593.00)

    def test0493(self):
        self.assertEquals(self.calculate(-166844.0, 52838.0), -114006.00)

    def test0494(self):
        self.assertEquals(self.calculate(-123423.0, 21188.0), -102235.00)

    def test0495(self):
        self.assertEquals(self.calculate(16754.0, -170027.0), -153273.00)

    def test0496(self):
        self.assertEquals(self.calculate(61033.0, 96433.0), 157466.00)

    def test0497(self):
        self.assertEquals(self.calculate(-6899.0, -85173.0), -92072.00)

    def test0498(self):
        self.assertEquals(self.calculate(-27305.0, -7673.0), -34978.00)

    def test0499(self):
        self.assertEquals(self.calculate(11238.0, -167673.0), -156435.00)

    def test0500(self):
        self.assertEquals(self.calculate(-108464.0, -14659.0), -123123.00)

    def test0501(self):
        self.assertEquals(self.calculate(-34496.0, -97655.0), -132151.00)

    def test0502(self):
        self.assertEquals(self.calculate(-179237.0, -78427.0), -257664.00)

    def test0503(self):
        self.assertEquals(self.calculate(-6216.0, 143071.0), 136855.00)

    def test0504(self):
        self.assertEquals(self.calculate(-32162.0, 179537.0), 147375.00)

    def test0505(self):
        self.assertEquals(self.calculate(-15919.0, -76103.0), -92022.00)

    def test0506(self):
        self.assertEquals(self.calculate(164916.0, 188145.0), 353061.00)

    def test0507(self):
        self.assertEquals(self.calculate(-170243.0, -98857.0), -269100.00)

    def test0508(self):
        self.assertEquals(self.calculate(96839.0, 193802.0), 290641.00)

    def test0509(self):
        self.assertEquals(self.calculate(-71964.0, 159495.0), 87531.00)

    def test0510(self):
        self.assertEquals(self.calculate(168361.0, 134901.0), 303262.00)

    def test0511(self):
        self.assertEquals(self.calculate(176575.0, 51498.0), 228073.00)

    def test0512(self):
        self.assertEquals(self.calculate(111381.0, -167446.0), -56065.00)

    def test0513(self):
        self.assertEquals(self.calculate(-145587.0, 53950.0), -91637.00)

    def test0514(self):
        self.assertEquals(self.calculate(-166262.0, 102630.0), -63632.00)

    def test0515(self):
        self.assertEquals(self.calculate(76543.0, 69319.0), 145862.00)

    def test0516(self):
        self.assertEquals(self.calculate(-21633.0, 109357.0), 87724.00)

    def test0517(self):
        self.assertEquals(self.calculate(-146749.0, 43236.0), -103513.00)

    def test0518(self):
        self.assertEquals(self.calculate(146014.0, -134662.0), 11352.00)

    def test0519(self):
        self.assertEquals(self.calculate(-8706.0, 94571.0), 85865.00)

    def test0520(self):
        self.assertEquals(self.calculate(-176783.0, -196093.0), -372876.00)

    def test0521(self):
        self.assertEquals(self.calculate(-7544.0, -132540.0), -140084.00)

    def test0522(self):
        self.assertEquals(self.calculate(-115082.0, 140030.0), 24948.00)

    def test0523(self):
        self.assertEquals(self.calculate(-17368.0, 189269.0), 171901.00)

    def test0524(self):
        self.assertEquals(self.calculate(-184068.0, -188045.0), -372113.00)

    def test0525(self):
        self.assertEquals(self.calculate(64210.0, -10985.0), 53225.00)

    def test0526(self):
        self.assertEquals(self.calculate(-162643.0, 129998.0), -32645.00)

    def test0527(self):
        self.assertEquals(self.calculate(17146.0, -90093.0), -72947.00)

    def test0528(self):
        self.assertEquals(self.calculate(-173758.0, -164505.0), -338263.00)

    def test0529(self):
        self.assertEquals(self.calculate(161501.0, -150206.0), 11295.00)

    def test0530(self):
        self.assertEquals(self.calculate(-49858.0, 175052.0), 125194.00)

    def test0531(self):
        self.assertEquals(self.calculate(-78363.0, -87208.0), -165571.00)

    def test0532(self):
        self.assertEquals(self.calculate(-159330.0, -84029.0), -243359.00)

    def test0533(self):
        self.assertEquals(self.calculate(-177519.0, -172553.0), -350072.00)

    def test0534(self):
        self.assertEquals(self.calculate(-90121.0, 43790.0), -46331.00)

    def test0535(self):
        self.assertEquals(self.calculate(171171.0, 12626.0), 183797.00)

    def test0536(self):
        self.assertEquals(self.calculate(-167372.0, -128034.0), -295406.00)

    def test0537(self):
        self.assertEquals(self.calculate(195485.0, -131964.0), 63521.00)

    def test0538(self):
        self.assertEquals(self.calculate(-23805.0, -117039.0), -140844.00)

    def test0539(self):
        self.assertEquals(self.calculate(88133.0, 80134.0), 168267.00)

    def test0540(self):
        self.assertEquals(self.calculate(-142921.0, -144656.0), -287577.00)

    def test0541(self):
        self.assertEquals(self.calculate(-161404.0, 142835.0), -18569.00)

    def test0542(self):
        self.assertEquals(self.calculate(-32274.0, -190527.0), -222801.00)

    def test0543(self):
        self.assertEquals(self.calculate(49376.0, -150493.0), -101117.00)

    def test0544(self):
        self.assertEquals(self.calculate(131477.0, -15906.0), 115571.00)

    def test0545(self):
        self.assertEquals(self.calculate(-142117.0, -71897.0), -214014.00)

    def test0546(self):
        self.assertEquals(self.calculate(-87615.0, 116317.0), 28702.00)

    def test0547(self):
        self.assertEquals(self.calculate(53137.0, -108248.0), -55111.00)

    def test0548(self):
        self.assertEquals(self.calculate(46144.0, 35768.0), 81912.00)

    def test0549(self):
        self.assertEquals(self.calculate(197724.0, -20495.0), 177229.00)

    def test0550(self):
        self.assertEquals(self.calculate(-19939.0, 36756.0), 16817.00)

    def test0551(self):
        self.assertEquals(self.calculate(-110348.0, 1488.0), -108860.00)

    def test0552(self):
        self.assertEquals(self.calculate(149111.0, 90027.0), 239138.00)

    def test0553(self):
        self.assertEquals(self.calculate(-186950.0, 132895.0), -54055.00)

    def test0554(self):
        self.assertEquals(self.calculate(142838.0, 54881.0), 197719.00)

    def test0555(self):
        self.assertEquals(self.calculate(132306.0, -36821.0), 95485.00)

    def test0556(self):
        self.assertEquals(self.calculate(17711.0, 68029.0), 85740.00)

    def test0557(self):
        self.assertEquals(self.calculate(167846.0, 116157.0), 284003.00)

    def test0558(self):
        self.assertEquals(self.calculate(-197918.0, -194584.0), -392502.00)

    def test0559(self):
        self.assertEquals(self.calculate(160333.0, -30443.0), 129890.00)

    def test0560(self):
        self.assertEquals(self.calculate(-21086.0, -4232.0), -25318.00)

    def test0561(self):
        self.assertEquals(self.calculate(134266.0, 90912.0), 225178.00)

    def test0562(self):
        self.assertEquals(self.calculate(-54299.0, 167907.0), 113608.00)

    def test0563(self):
        self.assertEquals(self.calculate(142207.0, -142408.0), -201.00)

    def test0564(self):
        self.assertEquals(self.calculate(-192768.0, -82011.0), -274779.00)

    def test0565(self):
        self.assertEquals(self.calculate(41519.0, 121231.0), 162750.00)

    def test0566(self):
        self.assertEquals(self.calculate(-73314.0, 139569.0), 66255.00)

    def test0567(self):
        self.assertEquals(self.calculate(5829.0, 90434.0), 96263.00)

    def test0568(self):
        self.assertEquals(self.calculate(-179897.0, 143198.0), -36699.00)

    def test0569(self):
        self.assertEquals(self.calculate(-31058.0, 30725.0), -333.00)

    def test0570(self):
        self.assertEquals(self.calculate(-157155.0, -186623.0), -343778.00)

    def test0571(self):
        self.assertEquals(self.calculate(63104.0, -40996.0), 22108.00)

    def test0572(self):
        self.assertEquals(self.calculate(-135943.0, 195808.0), 59865.00)

    def test0573(self):
        self.assertEquals(self.calculate(-164422.0, 54171.0), -110251.00)

    def test0574(self):
        self.assertEquals(self.calculate(122645.0, 190810.0), 313455.00)

    def test0575(self):
        self.assertEquals(self.calculate(-71043.0, -116418.0), -187461.00)

    def test0576(self):
        self.assertEquals(self.calculate(56733.0, -61033.0), -4300.00)

    def test0577(self):
        self.assertEquals(self.calculate(-84316.0, -116926.0), -201242.00)

    def test0578(self):
        self.assertEquals(self.calculate(143281.0, 160182.0), 303463.00)

    def test0579(self):
        self.assertEquals(self.calculate(117207.0, 156197.0), 273404.00)

    def test0580(self):
        self.assertEquals(self.calculate(156720.0, 97023.0), 253743.00)

    def test0581(self):
        self.assertEquals(self.calculate(126265.0, 162586.0), 288851.00)

    def test0582(self):
        self.assertEquals(self.calculate(159662.0, 168493.0), 328155.00)

    def test0583(self):
        self.assertEquals(self.calculate(-132582.0, 93757.0), -38825.00)

    def test0584(self):
        self.assertEquals(self.calculate(-12740.0, -199741.0), -212481.00)

    def test0585(self):
        self.assertEquals(self.calculate(74300.0, 91675.0), 165975.00)

    def test0586(self):
        self.assertEquals(self.calculate(-55485.0, 57161.0), 1676.00)

    def test0587(self):
        self.assertEquals(self.calculate(138959.0, -97597.0), 41362.00)

    def test0588(self):
        self.assertEquals(self.calculate(141450.0, 88663.0), 230113.00)

    def test0589(self):
        self.assertEquals(self.calculate(-76697.0, 198979.0), 122282.00)

    def test0590(self):
        self.assertEquals(self.calculate(-22328.0, -86780.0), -109108.00)

    def test0591(self):
        self.assertEquals(self.calculate(59923.0, 55961.0), 115884.00)

    def test0592(self):
        self.assertEquals(self.calculate(90333.0, -92786.0), -2453.00)

    def test0593(self):
        self.assertEquals(self.calculate(82514.0, 41653.0), 124167.00)

    def test0594(self):
        self.assertEquals(self.calculate(15185.0, -171111.0), -155926.00)

    def test0595(self):
        self.assertEquals(self.calculate(-66074.0, 152034.0), 85960.00)

    def test0596(self):
        self.assertEquals(self.calculate(-34927.0, 144406.0), 109479.00)

    def test0597(self):
        self.assertEquals(self.calculate(-161692.0, 82516.0), -79176.00)

    def test0598(self):
        self.assertEquals(self.calculate(-178027.0, 36326.0), -141701.00)

    def test0599(self):
        self.assertEquals(self.calculate(2948.0, 111598.0), 114546.00)

    def test0600(self):
        self.assertEquals(self.calculate(-191927.0, 123166.0), -68761.00)

    def test0601(self):
        self.assertEquals(self.calculate(-170907.0, 184726.0), 13819.00)

    def test0602(self):
        self.assertEquals(self.calculate(-131999.0, 63853.0), -68146.00)

    def test0603(self):
        self.assertEquals(self.calculate(89357.0, 33400.0), 122757.00)

    def test0604(self):
        self.assertEquals(self.calculate(177200.0, -79803.0), 97397.00)

    def test0605(self):
        self.assertEquals(self.calculate(122126.0, -4877.0), 117249.00)

    def test0606(self):
        self.assertEquals(self.calculate(171090.0, 145664.0), 316754.00)

    def test0607(self):
        self.assertEquals(self.calculate(-2012.0, -46709.0), -48721.00)

    def test0608(self):
        self.assertEquals(self.calculate(62100.0, -155864.0), -93764.00)

    def test0609(self):
        self.assertEquals(self.calculate(84687.0, 70645.0), 155332.00)

    def test0610(self):
        self.assertEquals(self.calculate(1528.0, -29200.0), -27672.00)

    def test0611(self):
        self.assertEquals(self.calculate(-142427.0, 14252.0), -128175.00)

    def test0612(self):
        self.assertEquals(self.calculate(-32702.0, -193438.0), -226140.00)

    def test0613(self):
        self.assertEquals(self.calculate(86180.0, 10391.0), 96571.00)

    def test0614(self):
        self.assertEquals(self.calculate(-11280.0, -164858.0), -176138.00)

    def test0615(self):
        self.assertEquals(self.calculate(64968.0, 180415.0), 245383.00)

    def test0616(self):
        self.assertEquals(self.calculate(-36818.0, 78311.0), 41493.00)

    def test0617(self):
        self.assertEquals(self.calculate(-120631.0, 140795.0), 20164.00)

    def test0618(self):
        self.assertEquals(self.calculate(-137059.0, -50661.0), -187720.00)

    def test0619(self):
        self.assertEquals(self.calculate(43526.0, -148777.0), -105251.00)

    def test0620(self):
        self.assertEquals(self.calculate(-72223.0, 21843.0), -50380.00)

    def test0621(self):
        self.assertEquals(self.calculate(-116791.0, -3195.0), -119986.00)

    def test0622(self):
        self.assertEquals(self.calculate(31183.0, -37292.0), -6109.00)

    def test0623(self):
        self.assertEquals(self.calculate(-81571.0, -31924.0), -113495.00)

    def test0624(self):
        self.assertEquals(self.calculate(91988.0, -65695.0), 26293.00)

    def test0625(self):
        self.assertEquals(self.calculate(188837.0, -188637.0), 200.00)

    def test0626(self):
        self.assertEquals(self.calculate(17973.0, 99617.0), 117590.00)

    def test0627(self):
        self.assertEquals(self.calculate(142046.0, -96598.0), 45448.00)

    def test0628(self):
        self.assertEquals(self.calculate(-170518.0, -16310.0), -186828.00)

    def test0629(self):
        self.assertEquals(self.calculate(23488.0, -120726.0), -97238.00)

    def test0630(self):
        self.assertEquals(self.calculate(193814.0, 114878.0), 308692.00)

    def test0631(self):
        self.assertEquals(self.calculate(112012.0, 150411.0), 262423.00)

    def test0632(self):
        self.assertEquals(self.calculate(169764.0, 182675.0), 352439.00)

    def test0633(self):
        self.assertEquals(self.calculate(14053.0, -174820.0), -160767.00)

    def test0634(self):
        self.assertEquals(self.calculate(-194910.0, 29960.0), -164950.00)

    def test0635(self):
        self.assertEquals(self.calculate(-102269.0, 186084.0), 83815.00)

    def test0636(self):
        self.assertEquals(self.calculate(169020.0, -102706.0), 66314.00)

    def test0637(self):
        self.assertEquals(self.calculate(-10885.0, -35582.0), -46467.00)

    def test0638(self):
        self.assertEquals(self.calculate(178945.0, 20741.0), 199686.00)

    def test0639(self):
        self.assertEquals(self.calculate(-147943.0, 71176.0), -76767.00)

    def test0640(self):
        self.assertEquals(self.calculate(-163504.0, -192470.0), -355974.00)

    def test0641(self):
        self.assertEquals(self.calculate(190009.0, 160687.0), 350696.00)

    def test0642(self):
        self.assertEquals(self.calculate(37174.0, -44289.0), -7115.00)

    def test0643(self):
        self.assertEquals(self.calculate(-163700.0, 168142.0), 4442.00)

    def test0644(self):
        self.assertEquals(self.calculate(-142592.0, -89357.0), -231949.00)

    def test0645(self):
        self.assertEquals(self.calculate(105049.0, -176950.0), -71901.00)

    def test0646(self):
        self.assertEquals(self.calculate(-58617.0, -152302.0), -210919.00)

    def test0647(self):
        self.assertEquals(self.calculate(-52327.0, -153368.0), -205695.00)

    def test0648(self):
        self.assertEquals(self.calculate(-131365.0, 199730.0), 68365.00)

    def test0649(self):
        self.assertEquals(self.calculate(85977.0, -106086.0), -20109.00)

    def test0650(self):
        self.assertEquals(self.calculate(17412.0, -191532.0), -174120.00)

    def test0651(self):
        self.assertEquals(self.calculate(-129444.0, -32151.0), -161595.00)

    def test0652(self):
        self.assertEquals(self.calculate(120497.0, -89259.0), 31238.00)

    def test0653(self):
        self.assertEquals(self.calculate(-131612.0, 150269.0), 18657.00)

    def test0654(self):
        self.assertEquals(self.calculate(103160.0, -162875.0), -59715.00)

    def test0655(self):
        self.assertEquals(self.calculate(120482.0, -148172.0), -27690.00)

    def test0656(self):
        self.assertEquals(self.calculate(-135789.0, -80563.0), -216352.00)

    def test0657(self):
        self.assertEquals(self.calculate(-35634.0, -63785.0), -99419.00)

    def test0658(self):
        self.assertEquals(self.calculate(-22549.0, 63346.0), 40797.00)

    def test0659(self):
        self.assertEquals(self.calculate(60772.0, -7040.0), 53732.00)

    def test0660(self):
        self.assertEquals(self.calculate(97024.0, -28943.0), 68081.00)

    def test0661(self):
        self.assertEquals(self.calculate(-125390.0, 133257.0), 7867.00)

    def test0662(self):
        self.assertEquals(self.calculate(-75074.0, 71217.0), -3857.00)

    def test0663(self):
        self.assertEquals(self.calculate(-30513.0, 79037.0), 48524.00)

    def test0664(self):
        self.assertEquals(self.calculate(19268.0, -58405.0), -39137.00)

    def test0665(self):
        self.assertEquals(self.calculate(-190362.0, -109065.0), -299427.00)

    def test0666(self):
        self.assertEquals(self.calculate(-155103.0, 163158.0), 8055.00)

    def test0667(self):
        self.assertEquals(self.calculate(124264.0, 196450.0), 320714.00)

    def test0668(self):
        self.assertEquals(self.calculate(188271.0, 125379.0), 313650.00)

    def test0669(self):
        self.assertEquals(self.calculate(186646.0, -13155.0), 173491.00)

    def test0670(self):
        self.assertEquals(self.calculate(36527.0, -59088.0), -22561.00)

    def test0671(self):
        self.assertEquals(self.calculate(190760.0, 62487.0), 253247.00)

    def test0672(self):
        self.assertEquals(self.calculate(-77080.0, 78074.0), 994.00)

    def test0673(self):
        self.assertEquals(self.calculate(-9149.0, 191384.0), 182235.00)

    def test0674(self):
        self.assertEquals(self.calculate(144916.0, -128529.0), 16387.00)

    def test0675(self):
        self.assertEquals(self.calculate(-166163.0, 112382.0), -53781.00)

    def test0676(self):
        self.assertEquals(self.calculate(-154736.0, 116340.0), -38396.00)

    def test0677(self):
        self.assertEquals(self.calculate(4946.0, 135555.0), 140501.00)

    def test0678(self):
        self.assertEquals(self.calculate(110229.0, 58098.0), 168327.00)

    def test0679(self):
        self.assertEquals(self.calculate(45428.0, -193325.0), -147897.00)

    def test0680(self):
        self.assertEquals(self.calculate(-164336.0, 10886.0), -153450.00)

    def test0681(self):
        self.assertEquals(self.calculate(-9112.0, -197841.0), -206953.00)

    def test0682(self):
        self.assertEquals(self.calculate(-193388.0, 114194.0), -79194.00)

    def test0683(self):
        self.assertEquals(self.calculate(180640.0, -117507.0), 63133.00)

    def test0684(self):
        self.assertEquals(self.calculate(-67838.0, -85707.0), -153545.00)

    def test0685(self):
        self.assertEquals(self.calculate(160143.0, 118618.0), 278761.00)

    def test0686(self):
        self.assertEquals(self.calculate(-96506.0, -31282.0), -127788.00)

    def test0687(self):
        self.assertEquals(self.calculate(106515.0, 133989.0), 240504.00)

    def test0688(self):
        self.assertEquals(self.calculate(120863.0, -138025.0), -17162.00)

    def test0689(self):
        self.assertEquals(self.calculate(153473.0, -81583.0), 71890.00)

    def test0690(self):
        self.assertEquals(self.calculate(82736.0, 168147.0), 250883.00)

    def test0691(self):
        self.assertEquals(self.calculate(-186479.0, -59060.0), -245539.00)

    def test0692(self):
        self.assertEquals(self.calculate(175523.0, 142042.0), 317565.00)

    def test0693(self):
        self.assertEquals(self.calculate(-108588.0, 29584.0), -79004.00)

    def test0694(self):
        self.assertEquals(self.calculate(-65987.0, -7910.0), -73897.00)

    def test0695(self):
        self.assertEquals(self.calculate(-36391.0, -72638.0), -109029.00)

    def test0696(self):
        self.assertEquals(self.calculate(-60336.0, 113787.0), 53451.00)

    def test0697(self):
        self.assertEquals(self.calculate(153186.0, -23985.0), 129201.00)

    def test0698(self):
        self.assertEquals(self.calculate(153829.0, -33064.0), 120765.00)

    def test0699(self):
        self.assertEquals(self.calculate(-90295.0, 70691.0), -19604.00)

    def test0700(self):
        self.assertEquals(self.calculate(182304.0, 134263.0), 316567.00)

    def test0701(self):
        self.assertEquals(self.calculate(-153675.0, -136526.0), -290201.00)

    def test0702(self):
        self.assertEquals(self.calculate(85541.0, 64629.0), 150170.00)

    def test0703(self):
        self.assertEquals(self.calculate(-91543.0, 105885.0), 14342.00)

    def test0704(self):
        self.assertEquals(self.calculate(-124030.0, 144175.0), 20145.00)

    def test0705(self):
        self.assertEquals(self.calculate(-119002.0, -124318.0), -243320.00)

    def test0706(self):
        self.assertEquals(self.calculate(-66224.0, 176362.0), 110138.00)

    def test0707(self):
        self.assertEquals(self.calculate(7772.0, -181792.0), -174020.00)

    def test0708(self):
        self.assertEquals(self.calculate(-124969.0, -99601.0), -224570.00)

    def test0709(self):
        self.assertEquals(self.calculate(-112516.0, 77550.0), -34966.00)

    def test0710(self):
        self.assertEquals(self.calculate(-152589.0, -86788.0), -239377.00)

    def test0711(self):
        self.assertEquals(self.calculate(-71261.0, -13758.0), -85019.00)

    def test0712(self):
        self.assertEquals(self.calculate(-52867.0, -167326.0), -220193.00)

    def test0713(self):
        self.assertEquals(self.calculate(-164234.0, -159778.0), -324012.00)

    def test0714(self):
        self.assertEquals(self.calculate(-181824.0, 89692.0), -92132.00)

    def test0715(self):
        self.assertEquals(self.calculate(195739.0, -187313.0), 8426.00)

    def test0716(self):
        self.assertEquals(self.calculate(-190080.0, 92154.0), -97926.00)

    def test0717(self):
        self.assertEquals(self.calculate(-2009.0, -85070.0), -87079.00)

    def test0718(self):
        self.assertEquals(self.calculate(-55538.0, -190492.0), -246030.00)

    def test0719(self):
        self.assertEquals(self.calculate(82198.0, -51794.0), 30404.00)

    def test0720(self):
        self.assertEquals(self.calculate(-108354.0, -54246.0), -162600.00)

    def test0721(self):
        self.assertEquals(self.calculate(-103810.0, 197380.0), 93570.00)

    def test0722(self):
        self.assertEquals(self.calculate(-52837.0, 77498.0), 24661.00)

    def test0723(self):
        self.assertEquals(self.calculate(-78357.0, 184886.0), 106529.00)

    def test0724(self):
        self.assertEquals(self.calculate(-226.0, -117918.0), -118144.00)

    def test0725(self):
        self.assertEquals(self.calculate(34471.0, -109118.0), -74647.00)

    def test0726(self):
        self.assertEquals(self.calculate(30038.0, 199354.0), 229392.00)

    def test0727(self):
        self.assertEquals(self.calculate(-153713.0, -158798.0), -312511.00)

    def test0728(self):
        self.assertEquals(self.calculate(-100420.0, 174568.0), 74148.00)

    def test0729(self):
        self.assertEquals(self.calculate(-40630.0, 126140.0), 85510.00)

    def test0730(self):
        self.assertEquals(self.calculate(-184190.0, 67959.0), -116231.00)

    def test0731(self):
        self.assertEquals(self.calculate(21285.0, 99027.0), 120312.00)

    def test0732(self):
        self.assertEquals(self.calculate(-199319.0, -100479.0), -299798.00)

    def test0733(self):
        self.assertEquals(self.calculate(113784.0, 56639.0), 170423.00)

    def test0734(self):
        self.assertEquals(self.calculate(39620.0, -176381.0), -136761.00)

    def test0735(self):
        self.assertEquals(self.calculate(152251.0, 175306.0), 327557.00)

    def test0736(self):
        self.assertEquals(self.calculate(-123360.0, -161191.0), -284551.00)

    def test0737(self):
        self.assertEquals(self.calculate(-46096.0, -50961.0), -97057.00)

    def test0738(self):
        self.assertEquals(self.calculate(-132246.0, -162471.0), -294717.00)

    def test0739(self):
        self.assertEquals(self.calculate(143953.0, 22521.0), 166474.00)

    def test0740(self):
        self.assertEquals(self.calculate(-57860.0, -119192.0), -177052.00)

    def test0741(self):
        self.assertEquals(self.calculate(193141.0, 96556.0), 289697.00)

    def test0742(self):
        self.assertEquals(self.calculate(191931.0, 164158.0), 356089.00)

    def test0743(self):
        self.assertEquals(self.calculate(-174389.0, 165445.0), -8944.00)

    def test0744(self):
        self.assertEquals(self.calculate(-171324.0, 150997.0), -20327.00)

    def test0745(self):
        self.assertEquals(self.calculate(79098.0, -135272.0), -56174.00)

    def test0746(self):
        self.assertEquals(self.calculate(81752.0, 22216.0), 103968.00)

    def test0747(self):
        self.assertEquals(self.calculate(-96343.0, 74600.0), -21743.00)

    def test0748(self):
        self.assertEquals(self.calculate(166538.0, 68740.0), 235278.00)

    def test0749(self):
        self.assertEquals(self.calculate(99915.0, -188045.0), -88130.00)

    def test0750(self):
        self.assertEquals(self.calculate(152988.0, -104102.0), 48886.00)

    def test0751(self):
        self.assertEquals(self.calculate(-1408.0, 150524.0), 149116.00)

    def test0752(self):
        self.assertEquals(self.calculate(188532.0, 196235.0), 384767.00)

    def test0753(self):
        self.assertEquals(self.calculate(-53061.0, -69679.0), -122740.00)

    def test0754(self):
        self.assertEquals(self.calculate(156379.0, -84590.0), 71789.00)

    def test0755(self):
        self.assertEquals(self.calculate(-45799.0, 141822.0), 96023.00)

    def test0756(self):
        self.assertEquals(self.calculate(164597.0, 87590.0), 252187.00)

    def test0757(self):
        self.assertEquals(self.calculate(107103.0, 50110.0), 157213.00)

    def test0758(self):
        self.assertEquals(self.calculate(-186872.0, 182358.0), -4514.00)

    def test0759(self):
        self.assertEquals(self.calculate(43196.0, 80771.0), 123967.00)

    def test0760(self):
        self.assertEquals(self.calculate(111616.0, 118531.0), 230147.00)

    def test0761(self):
        self.assertEquals(self.calculate(-197266.0, 127051.0), -70215.00)

    def test0762(self):
        self.assertEquals(self.calculate(-148280.0, -77693.0), -225973.00)

    def test0763(self):
        self.assertEquals(self.calculate(-119253.0, 59638.0), -59615.00)

    def test0764(self):
        self.assertEquals(self.calculate(-41572.0, 5529.0), -36043.00)

    def test0765(self):
        self.assertEquals(self.calculate(3887.0, -162784.0), -158897.00)

    def test0766(self):
        self.assertEquals(self.calculate(112788.0, 65108.0), 177896.00)

    def test0767(self):
        self.assertEquals(self.calculate(-147025.0, -116423.0), -263448.00)

    def test0768(self):
        self.assertEquals(self.calculate(-70705.0, 2135.0), -68570.00)

    def test0769(self):
        self.assertEquals(self.calculate(-16481.0, 147058.0), 130577.00)

    def test0770(self):
        self.assertEquals(self.calculate(103181.0, 115095.0), 218276.00)

    def test0771(self):
        self.assertEquals(self.calculate(16630.0, 23058.0), 39688.00)

    def test0772(self):
        self.assertEquals(self.calculate(-183246.0, 106295.0), -76951.00)

    def test0773(self):
        self.assertEquals(self.calculate(-147997.0, 194141.0), 46144.00)

    def test0774(self):
        self.assertEquals(self.calculate(-146657.0, -165534.0), -312191.00)

    def test0775(self):
        self.assertEquals(self.calculate(129432.0, -47184.0), 82248.00)

    def test0776(self):
        self.assertEquals(self.calculate(-185783.0, -131435.0), -317218.00)

    def test0777(self):
        self.assertEquals(self.calculate(175143.0, 163420.0), 338563.00)

    def test0778(self):
        self.assertEquals(self.calculate(41035.0, -57433.0), -16398.00)

    def test0779(self):
        self.assertEquals(self.calculate(148375.0, 153960.0), 302335.00)

    def test0780(self):
        self.assertEquals(self.calculate(86214.0, 54875.0), 141089.00)

    def test0781(self):
        self.assertEquals(self.calculate(-39643.0, -76473.0), -116116.00)

    def test0782(self):
        self.assertEquals(self.calculate(89967.0, 119523.0), 209490.00)

    def test0783(self):
        self.assertEquals(self.calculate(-73254.0, 49608.0), -23646.00)

    def test0784(self):
        self.assertEquals(self.calculate(-47565.0, -56032.0), -103597.00)

    def test0785(self):
        self.assertEquals(self.calculate(6962.0, 67197.0), 74159.00)

    def test0786(self):
        self.assertEquals(self.calculate(107577.0, 77219.0), 184796.00)

    def test0787(self):
        self.assertEquals(self.calculate(-81091.0, 133392.0), 52301.00)

    def test0788(self):
        self.assertEquals(self.calculate(62855.0, 197473.0), 260328.00)

    def test0789(self):
        self.assertEquals(self.calculate(69610.0, 165854.0), 235464.00)

    def test0790(self):
        self.assertEquals(self.calculate(160325.0, -17833.0), 142492.00)

    def test0791(self):
        self.assertEquals(self.calculate(123131.0, 116395.0), 239526.00)

    def test0792(self):
        self.assertEquals(self.calculate(-57815.0, -67665.0), -125480.00)

    def test0793(self):
        self.assertEquals(self.calculate(71934.0, -149306.0), -77372.00)

    def test0794(self):
        self.assertEquals(self.calculate(-2695.0, 118100.0), 115405.00)

    def test0795(self):
        self.assertEquals(self.calculate(198094.0, -173807.0), 24287.00)

    def test0796(self):
        self.assertEquals(self.calculate(188644.0, -47445.0), 141199.00)

    def test0797(self):
        self.assertEquals(self.calculate(-126423.0, -126507.0), -252930.00)

    def test0798(self):
        self.assertEquals(self.calculate(-196139.0, 199410.0), 3271.00)

    def test0799(self):
        self.assertEquals(self.calculate(-193947.0, 145015.0), -48932.00)

    def test0800(self):
        self.assertEquals(self.calculate(90068.0, 31146.0), 121214.00)

    def test0801(self):
        self.assertEquals(self.calculate(-83275.0, 114022.0), 30747.00)

    def test0802(self):
        self.assertEquals(self.calculate(-90099.0, 65467.0), -24632.00)

    def test0803(self):
        self.assertEquals(self.calculate(-104892.0, 41130.0), -63762.00)

    def test0804(self):
        self.assertEquals(self.calculate(-188963.0, 58519.0), -130444.00)

    def test0805(self):
        self.assertEquals(self.calculate(97500.0, 110988.0), 208488.00)

    def test0806(self):
        self.assertEquals(self.calculate(-119949.0, -20782.0), -140731.00)

    def test0807(self):
        self.assertEquals(self.calculate(49783.0, 44184.0), 93967.00)

    def test0808(self):
        self.assertEquals(self.calculate(51508.0, -134700.0), -83192.00)

    def test0809(self):
        self.assertEquals(self.calculate(15201.0, -188061.0), -172860.00)

    def test0810(self):
        self.assertEquals(self.calculate(-152922.0, -198399.0), -351321.00)

    def test0811(self):
        self.assertEquals(self.calculate(136805.0, 98740.0), 235545.00)

    def test0812(self):
        self.assertEquals(self.calculate(-106217.0, -14997.0), -121214.00)

    def test0813(self):
        self.assertEquals(self.calculate(-115570.0, 144271.0), 28701.00)

    def test0814(self):
        self.assertEquals(self.calculate(184440.0, 78781.0), 263221.00)

    def test0815(self):
        self.assertEquals(self.calculate(-80525.0, -185406.0), -265931.00)

    def test0816(self):
        self.assertEquals(self.calculate(-186455.0, 1688.0), -184767.00)

    def test0817(self):
        self.assertEquals(self.calculate(134791.0, -17162.0), 117629.00)

    def test0818(self):
        self.assertEquals(self.calculate(28543.0, 167465.0), 196008.00)

    def test0819(self):
        self.assertEquals(self.calculate(-15796.0, 153782.0), 137986.00)

    def test0820(self):
        self.assertEquals(self.calculate(81738.0, -172487.0), -90749.00)

    def test0821(self):
        self.assertEquals(self.calculate(-149206.0, -132734.0), -281940.00)

    def test0822(self):
        self.assertEquals(self.calculate(-187615.0, -12617.0), -200232.00)

    def test0823(self):
        self.assertEquals(self.calculate(23828.0, 119315.0), 143143.00)

    def test0824(self):
        self.assertEquals(self.calculate(-182487.0, 130224.0), -52263.00)

    def test0825(self):
        self.assertEquals(self.calculate(-146786.0, 81237.0), -65549.00)

    def test0826(self):
        self.assertEquals(self.calculate(22589.0, -78470.0), -55881.00)

    def test0827(self):
        self.assertEquals(self.calculate(-163329.0, -192947.0), -356276.00)

    def test0828(self):
        self.assertEquals(self.calculate(130454.0, -114187.0), 16267.00)

    def test0829(self):
        self.assertEquals(self.calculate(-180165.0, -15831.0), -195996.00)

    def test0830(self):
        self.assertEquals(self.calculate(307.0, -54866.0), -54559.00)

    def test0831(self):
        self.assertEquals(self.calculate(-53767.0, 155355.0), 101588.00)

    def test0832(self):
        self.assertEquals(self.calculate(11713.0, 26766.0), 38479.00)

    def test0833(self):
        self.assertEquals(self.calculate(175134.0, 172646.0), 347780.00)

    def test0834(self):
        self.assertEquals(self.calculate(122672.0, 30725.0), 153397.00)

    def test0835(self):
        self.assertEquals(self.calculate(59723.0, -118814.0), -59091.00)

    def test0836(self):
        self.assertEquals(self.calculate(164522.0, -26696.0), 137826.00)

    def test0837(self):
        self.assertEquals(self.calculate(38239.0, -52824.0), -14585.00)

    def test0838(self):
        self.assertEquals(self.calculate(-105371.0, 86616.0), -18755.00)

    def test0839(self):
        self.assertEquals(self.calculate(-107595.0, -112936.0), -220531.00)

    def test0840(self):
        self.assertEquals(self.calculate(2231.0, 183935.0), 186166.00)

    def test0841(self):
        self.assertEquals(self.calculate(-76774.0, 36487.0), -40287.00)

    def test0842(self):
        self.assertEquals(self.calculate(-38547.0, 135453.0), 96906.00)

    def test0843(self):
        self.assertEquals(self.calculate(-8335.0, 190408.0), 182073.00)

    def test0844(self):
        self.assertEquals(self.calculate(-152943.0, 54361.0), -98582.00)

    def test0845(self):
        self.assertEquals(self.calculate(-163712.0, 117123.0), -46589.00)

    def test0846(self):
        self.assertEquals(self.calculate(142143.0, 108963.0), 251106.00)

    def test0847(self):
        self.assertEquals(self.calculate(12302.0, -70225.0), -57923.00)

    def test0848(self):
        self.assertEquals(self.calculate(-69039.0, -139634.0), -208673.00)

    def test0849(self):
        self.assertEquals(self.calculate(-44247.0, 111312.0), 67065.00)

    def test0850(self):
        self.assertEquals(self.calculate(14327.0, 179560.0), 193887.00)

    def test0851(self):
        self.assertEquals(self.calculate(-141405.0, -62765.0), -204170.00)

    def test0852(self):
        self.assertEquals(self.calculate(-178770.0, -164651.0), -343421.00)

    def test0853(self):
        self.assertEquals(self.calculate(-34161.0, -59920.0), -94081.00)

    def test0854(self):
        self.assertEquals(self.calculate(-52646.0, 47807.0), -4839.00)

    def test0855(self):
        self.assertEquals(self.calculate(179589.0, 42116.0), 221705.00)

    def test0856(self):
        self.assertEquals(self.calculate(171003.0, 175361.0), 346364.00)

    def test0857(self):
        self.assertEquals(self.calculate(28694.0, 28046.0), 56740.00)

    def test0858(self):
        self.assertEquals(self.calculate(-16586.0, 137396.0), 120810.00)

    def test0859(self):
        self.assertEquals(self.calculate(-17314.0, -74660.0), -91974.00)

    def test0860(self):
        self.assertEquals(self.calculate(-64989.0, -99746.0), -164735.00)

    def test0861(self):
        self.assertEquals(self.calculate(84679.0, -190511.0), -105832.00)

    def test0862(self):
        self.assertEquals(self.calculate(34236.0, -155187.0), -120951.00)

    def test0863(self):
        self.assertEquals(self.calculate(142367.0, 151963.0), 294330.00)

    def test0864(self):
        self.assertEquals(self.calculate(-41650.0, -17322.0), -58972.00)

    def test0865(self):
        self.assertEquals(self.calculate(-46494.0, -160524.0), -207018.00)

    def test0866(self):
        self.assertEquals(self.calculate(-29466.0, 112902.0), 83436.00)

    def test0867(self):
        self.assertEquals(self.calculate(99097.0, -82333.0), 16764.00)

    def test0868(self):
        self.assertEquals(self.calculate(-147731.0, 175653.0), 27922.00)

    def test0869(self):
        self.assertEquals(self.calculate(-47873.0, 187203.0), 139330.00)

    def test0870(self):
        self.assertEquals(self.calculate(-165477.0, -179625.0), -345102.00)

    def test0871(self):
        self.assertEquals(self.calculate(132497.0, 197371.0), 329868.00)

    def test0872(self):
        self.assertEquals(self.calculate(42166.0, -138480.0), -96314.00)

    def test0873(self):
        self.assertEquals(self.calculate(-24952.0, -130166.0), -155118.00)

    def test0874(self):
        self.assertEquals(self.calculate(1350.0, 172846.0), 174196.00)

    def test0875(self):
        self.assertEquals(self.calculate(41201.0, 45352.0), 86553.00)

    def test0876(self):
        self.assertEquals(self.calculate(-19175.0, -79152.0), -98327.00)

    def test0877(self):
        self.assertEquals(self.calculate(-126240.0, 110622.0), -15618.00)

    def test0878(self):
        self.assertEquals(self.calculate(-38637.0, -160125.0), -198762.00)

    def test0879(self):
        self.assertEquals(self.calculate(-65765.0, 106.0), -65659.00)

    def test0880(self):
        self.assertEquals(self.calculate(-36670.0, 121934.0), 85264.00)

    def test0881(self):
        self.assertEquals(self.calculate(195903.0, -77482.0), 118421.00)

    def test0882(self):
        self.assertEquals(self.calculate(164527.0, 185969.0), 350496.00)

    def test0883(self):
        self.assertEquals(self.calculate(181398.0, -71114.0), 110284.00)

    def test0884(self):
        self.assertEquals(self.calculate(-17154.0, -170778.0), -187932.00)

    def test0885(self):
        self.assertEquals(self.calculate(127391.0, 47993.0), 175384.00)

    def test0886(self):
        self.assertEquals(self.calculate(-78462.0, -171789.0), -250251.00)

    def test0887(self):
        self.assertEquals(self.calculate(-58687.0, -16101.0), -74788.00)

    def test0888(self):
        self.assertEquals(self.calculate(145094.0, 164648.0), 309742.00)

    def test0889(self):
        self.assertEquals(self.calculate(130071.0, 134627.0), 264698.00)

    def test0890(self):
        self.assertEquals(self.calculate(42531.0, -62553.0), -20022.00)

    def test0891(self):
        self.assertEquals(self.calculate(113892.0, -64970.0), 48922.00)

    def test0892(self):
        self.assertEquals(self.calculate(10293.0, 33878.0), 44171.00)

    def test0893(self):
        self.assertEquals(self.calculate(189692.0, 14497.0), 204189.00)

    def test0894(self):
        self.assertEquals(self.calculate(182840.0, 71365.0), 254205.00)

    def test0895(self):
        self.assertEquals(self.calculate(-126383.0, -186050.0), -312433.00)

    def test0896(self):
        self.assertEquals(self.calculate(-173980.0, 180128.0), 6148.00)

    def test0897(self):
        self.assertEquals(self.calculate(-19200.0, 154312.0), 135112.00)

    def test0898(self):
        self.assertEquals(self.calculate(108846.0, 26502.0), 135348.00)

    def test0899(self):
        self.assertEquals(self.calculate(42613.0, 117384.0), 159997.00)

    def test0900(self):
        self.assertEquals(self.calculate(-103488.0, 81886.0), -21602.00)

    def test0901(self):
        self.assertEquals(self.calculate(168535.0, -118203.0), 50332.00)

    def test0902(self):
        self.assertEquals(self.calculate(-32367.0, 95854.0), 63487.00)

    def test0903(self):
        self.assertEquals(self.calculate(103760.0, 187167.0), 290927.00)

    def test0904(self):
        self.assertEquals(self.calculate(-119791.0, 115005.0), -4786.00)

    def test0905(self):
        self.assertEquals(self.calculate(57272.0, 197952.0), 255224.00)

    def test0906(self):
        self.assertEquals(self.calculate(104269.0, 155988.0), 260257.00)

    def test0907(self):
        self.assertEquals(self.calculate(-163031.0, 89023.0), -74008.00)

    def test0908(self):
        self.assertEquals(self.calculate(59781.0, 155790.0), 215571.00)

    def test0909(self):
        self.assertEquals(self.calculate(-54220.0, -75990.0), -130210.00)

    def test0910(self):
        self.assertEquals(self.calculate(112388.0, 22184.0), 134572.00)

    def test0911(self):
        self.assertEquals(self.calculate(16041.0, 179616.0), 195657.00)

    def test0912(self):
        self.assertEquals(self.calculate(-137826.0, -106640.0), -244466.00)

    def test0913(self):
        self.assertEquals(self.calculate(-154314.0, 137356.0), -16958.00)

    def test0914(self):
        self.assertEquals(self.calculate(-123514.0, 115274.0), -8240.00)

    def test0915(self):
        self.assertEquals(self.calculate(23238.0, -130729.0), -107491.00)

    def test0916(self):
        self.assertEquals(self.calculate(91424.0, -72254.0), 19170.00)

    def test0917(self):
        self.assertEquals(self.calculate(-160729.0, 35940.0), -124789.00)

    def test0918(self):
        self.assertEquals(self.calculate(-178810.0, -157694.0), -336504.00)

    def test0919(self):
        self.assertEquals(self.calculate(37251.0, -10946.0), 26305.00)

    def test0920(self):
        self.assertEquals(self.calculate(-24433.0, -131195.0), -155628.00)

    def test0921(self):
        self.assertEquals(self.calculate(58995.0, 160091.0), 219086.00)

    def test0922(self):
        self.assertEquals(self.calculate(171220.0, -99046.0), 72174.00)

    def test0923(self):
        self.assertEquals(self.calculate(-114251.0, -3981.0), -118232.00)

    def test0924(self):
        self.assertEquals(self.calculate(-128597.0, -68614.0), -197211.00)

    def test0925(self):
        self.assertEquals(self.calculate(-15590.0, 177392.0), 161802.00)

    def test0926(self):
        self.assertEquals(self.calculate(-133838.0, 50362.0), -83476.00)

    def test0927(self):
        self.assertEquals(self.calculate(-67832.0, 94361.0), 26529.00)

    def test0928(self):
        self.assertEquals(self.calculate(167973.0, -22307.0), 145666.00)

    def test0929(self):
        self.assertEquals(self.calculate(-187338.0, -193267.0), -380605.00)

    def test0930(self):
        self.assertEquals(self.calculate(21684.0, 180352.0), 202036.00)

    def test0931(self):
        self.assertEquals(self.calculate(194217.0, 41951.0), 236168.00)

    def test0932(self):
        self.assertEquals(self.calculate(94936.0, 14929.0), 109865.00)

    def test0933(self):
        self.assertEquals(self.calculate(-101171.0, -31536.0), -132707.00)

    def test0934(self):
        self.assertEquals(self.calculate(-45499.0, -41585.0), -87084.00)

    def test0935(self):
        self.assertEquals(self.calculate(65220.0, -71380.0), -6160.00)

    def test0936(self):
        self.assertEquals(self.calculate(-68711.0, -92698.0), -161409.00)

    def test0937(self):
        self.assertEquals(self.calculate(98785.0, -60168.0), 38617.00)

    def test0938(self):
        self.assertEquals(self.calculate(-30526.0, 65183.0), 34657.00)

    def test0939(self):
        self.assertEquals(self.calculate(-76562.0, -169856.0), -246418.00)

    def test0940(self):
        self.assertEquals(self.calculate(-127375.0, 107792.0), -19583.00)

    def test0941(self):
        self.assertEquals(self.calculate(-37212.0, -164953.0), -202165.00)

    def test0942(self):
        self.assertEquals(self.calculate(-17941.0, -131706.0), -149647.00)

    def test0943(self):
        self.assertEquals(self.calculate(-2601.0, 58260.0), 55659.00)

    def test0944(self):
        self.assertEquals(self.calculate(180553.0, -140336.0), 40217.00)

    def test0945(self):
        self.assertEquals(self.calculate(147600.0, 26089.0), 173689.00)

    def test0946(self):
        self.assertEquals(self.calculate(85789.0, 34253.0), 120042.00)

    def test0947(self):
        self.assertEquals(self.calculate(-54419.0, -35999.0), -90418.00)

    def test0948(self):
        self.assertEquals(self.calculate(-95408.0, 62131.0), -33277.00)

    def test0949(self):
        self.assertEquals(self.calculate(-70440.0, 71010.0), 570.00)

    def test0950(self):
        self.assertEquals(self.calculate(-179687.0, 33375.0), -146312.00)

    def test0951(self):
        self.assertEquals(self.calculate(140858.0, 136954.0), 277812.00)

    def test0952(self):
        self.assertEquals(self.calculate(9438.0, -196030.0), -186592.00)

    def test0953(self):
        self.assertEquals(self.calculate(-35943.0, 92728.0), 56785.00)

    def test0954(self):
        self.assertEquals(self.calculate(-73417.0, 27632.0), -45785.00)

    def test0955(self):
        self.assertEquals(self.calculate(85413.0, 177364.0), 262777.00)

    def test0956(self):
        self.assertEquals(self.calculate(-32141.0, 189354.0), 157213.00)

    def test0957(self):
        self.assertEquals(self.calculate(-35585.0, -10983.0), -46568.00)

    def test0958(self):
        self.assertEquals(self.calculate(17097.0, 74685.0), 91782.00)

    def test0959(self):
        self.assertEquals(self.calculate(-106516.0, -69346.0), -175862.00)

    def test0960(self):
        self.assertEquals(self.calculate(-168505.0, -120223.0), -288728.00)

    def test0961(self):
        self.assertEquals(self.calculate(67831.0, -104471.0), -36640.00)

    def test0962(self):
        self.assertEquals(self.calculate(43285.0, -57015.0), -13730.00)

    def test0963(self):
        self.assertEquals(self.calculate(87334.0, 143613.0), 230947.00)

    def test0964(self):
        self.assertEquals(self.calculate(-37856.0, -145569.0), -183425.00)

    def test0965(self):
        self.assertEquals(self.calculate(132091.0, 3221.0), 135312.00)

    def test0966(self):
        self.assertEquals(self.calculate(191837.0, -137425.0), 54412.00)

    def test0967(self):
        self.assertEquals(self.calculate(99775.0, -48733.0), 51042.00)

    def test0968(self):
        self.assertEquals(self.calculate(-175025.0, 85359.0), -89666.00)

    def test0969(self):
        self.assertEquals(self.calculate(-181113.0, 1873.0), -179240.00)

    def test0970(self):
        self.assertEquals(self.calculate(113400.0, 176641.0), 290041.00)

    def test0971(self):
        self.assertEquals(self.calculate(46001.0, 63514.0), 109515.00)

    def test0972(self):
        self.assertEquals(self.calculate(-188332.0, -69020.0), -257352.00)

    def test0973(self):
        self.assertEquals(self.calculate(49285.0, -58299.0), -9014.00)

    def test0974(self):
        self.assertEquals(self.calculate(-159719.0, 187685.0), 27966.00)

    def test0975(self):
        self.assertEquals(self.calculate(-23189.0, -60990.0), -84179.00)

    def test0976(self):
        self.assertEquals(self.calculate(-179249.0, 113802.0), -65447.00)

    def test0977(self):
        self.assertEquals(self.calculate(-199470.0, 7171.0), -192299.00)

    def test0978(self):
        self.assertEquals(self.calculate(139850.0, 10702.0), 150552.00)

    def test0979(self):
        self.assertEquals(self.calculate(-90022.0, 38828.0), -51194.00)

    def test0980(self):
        self.assertEquals(self.calculate(-174255.0, 28374.0), -145881.00)

    def test0981(self):
        self.assertEquals(self.calculate(-138639.0, 85892.0), -52747.00)

    def test0982(self):
        self.assertEquals(self.calculate(166562.0, -94479.0), 72083.00)

    def test0983(self):
        self.assertEquals(self.calculate(-26165.0, 69570.0), 43405.00)

    def test0984(self):
        self.assertEquals(self.calculate(13058.0, -25937.0), -12879.00)

    def test0985(self):
        self.assertEquals(self.calculate(66022.0, 128944.0), 194966.00)

    def test0986(self):
        self.assertEquals(self.calculate(-159038.0, -146232.0), -305270.00)

    def test0987(self):
        self.assertEquals(self.calculate(18874.0, 42088.0), 60962.00)

    def test0988(self):
        self.assertEquals(self.calculate(41916.0, 177997.0), 219913.00)

    def test0989(self):
        self.assertEquals(self.calculate(-70019.0, 184742.0), 114723.00)

    def test0990(self):
        self.assertEquals(self.calculate(5997.0, 64803.0), 70800.00)

    def test0991(self):
        self.assertEquals(self.calculate(133859.0, -68500.0), 65359.00)

    def test0992(self):
        self.assertEquals(self.calculate(-85320.0, -84936.0), -170256.00)

    def test0993(self):
        self.assertEquals(self.calculate(175975.0, 92008.0), 267983.00)

    def test0994(self):
        self.assertEquals(self.calculate(54083.0, 128936.0), 183019.00)

    def test0995(self):
        self.assertEquals(self.calculate(70890.0, 58729.0), 129619.00)

    def test0996(self):
        self.assertEquals(self.calculate(-90350.0, -96637.0), -186987.00)

    def test0997(self):
        self.assertEquals(self.calculate(-28447.0, 142544.0), 114097.00)

    def test0998(self):
        self.assertEquals(self.calculate(91385.0, -126218.0), -34833.00)

    def test0999(self):
        self.assertEquals(self.calculate(-67901.0, 133529.0), 65628.00)

    def test1000(self):
        self.assertEquals(self.calculate(-33112.0, -83959.0), -117071.00)

    def test1001(self):
        self.assertEquals(self.calculate(-187959.0, -112978.0), -300937.00)

    def test1002(self):
        self.assertEquals(self.calculate(69112.0, -133915.0), -64803.00)

    def test1003(self):
        self.assertEquals(self.calculate(-184386.0, -159718.0), -344104.00)

    def test1004(self):
        self.assertEquals(self.calculate(-166466.0, 119335.0), -47131.00)

    def test1005(self):
        self.assertEquals(self.calculate(10805.0, 14543.0), 25348.00)

    def test1006(self):
        self.assertEquals(self.calculate(54405.0, -65363.0), -10958.00)

    def test1007(self):
        self.assertEquals(self.calculate(-32003.0, 142311.0), 110308.00)

    def test1008(self):
        self.assertEquals(self.calculate(-79043.0, 197551.0), 118508.00)

    def test1009(self):
        self.assertEquals(self.calculate(194629.0, 161073.0), 355702.00)

    def test1010(self):
        self.assertEquals(self.calculate(185726.0, -104829.0), 80897.00)

    def test1011(self):
        self.assertEquals(self.calculate(68640.0, 62263.0), 130903.00)

    def test1012(self):
        self.assertEquals(self.calculate(-157801.0, 64668.0), -93133.00)

    def test1013(self):
        self.assertEquals(self.calculate(140754.0, 122403.0), 263157.00)

    def test1014(self):
        self.assertEquals(self.calculate(-84517.0, -18677.0), -103194.00)

    def test1015(self):
        self.assertEquals(self.calculate(164293.0, 44683.0), 208976.00)

    def test1016(self):
        self.assertEquals(self.calculate(-129526.0, 26699.0), -102827.00)

    def test1017(self):
        self.assertEquals(self.calculate(145354.0, -106398.0), 38956.00)

    def test1018(self):
        self.assertEquals(self.calculate(-107933.0, -50823.0), -158756.00)

    def test1019(self):
        self.assertEquals(self.calculate(-46809.0, 81299.0), 34490.00)

    def test1020(self):
        self.assertEquals(self.calculate(107578.0, -116492.0), -8914.00)

    def test1021(self):
        self.assertEquals(self.calculate(-109312.0, 177186.0), 67874.00)

    def test1022(self):
        self.assertEquals(self.calculate(120350.0, -147694.0), -27344.00)

    def test1023(self):
        self.assertEquals(self.calculate(-78873.0, -71091.0), -149964.00)


#
unittest.main()

