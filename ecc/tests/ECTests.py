#
#	joeecc - A small Elliptic Curve Cryptography Demonstration.
#	Copyright (C) 2011-2015 Johannes Bauer
#
#	This file is part of joeecc.
#
#	joeecc is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	joeecc is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with joeecc; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>
#

import unittest
from ..ShortWeierstrassCurve import ShortWeierstrassCurve
from ..AffineCurvePoint import AffineCurvePoint
from .. import getcurvebyname

class ECTests(unittest.TestCase):
	def test_basic1(self):
		e = ShortWeierstrassCurve(-3, 5, 23, 0, 0, 13, 22)
		x = AffineCurvePoint(21, 16, e)
		y = AffineCurvePoint(14, 19, e)
		self.assertTrue(x.oncurve())
		self.assertTrue(y.oncurve())
		self.assertTrue((x + y).oncurve())
		self.assertEqual((x + y), AffineCurvePoint(14, 4, e))
		self.assertTrue((x + x).oncurve())
		self.assertEqual((x + x), AffineCurvePoint(5, 0, e))
		self.assertTrue((y + y).oncurve())
		self.assertEqual((y + y), AffineCurvePoint(21, 7, e))

	def test_basic2(self):
		e = ShortWeierstrassCurve(2, 5, 23, 0, 0, 9, 4)
		x = AffineCurvePoint(9, 4, e)
		y = AffineCurvePoint(10, 6, e)
		# (9, 4) + (10, 6) = (8, 21)
		# (9, 4) + (9, 4) = (6, 16)
		self.assertTrue(x.oncurve())
		self.assertTrue(y.oncurve())
		z = x + y

		self.assertTrue(z.oncurve())
		z = x + x
		self.assertTrue(z.oncurve())
		z = y + y
		self.assertTrue(z.oncurve())

		x = AffineCurvePoint(9, 5, e)
		self.assertFalse(x.oncurve())

	def test_basic3(self):
		# Testing data from http://christelbach.com/ECCalculator.aspx
		e = ShortWeierstrassCurve(3, 99, 101, 0, 0, 12, 34)
		self.assertTrue((e.G * 0).is_neutral)
		self.assertEqual((e.G * 1), e.G)
		self.assertEqual((e.G * 2), AffineCurvePoint(93, 88, e))
		self.assertEqual((e.G * 3), AffineCurvePoint(75, 25, e))
		self.assertEqual((e.G * 4), AffineCurvePoint(47, 72, e))
		self.assertEqual((e.G * 5), AffineCurvePoint(21, 63, e))
		self.assertEqual((e.G * 55), AffineCurvePoint(71, 28, e))
		self.assertEqual((e.G * 123), AffineCurvePoint(91, 33, e))
		self.assertTrue((e.G * 99).is_neutral)
		self.assertEqual(e.naive_order_calculation(), 99)

	def test_extd(self):
		e = getcurvebyname("secp112r1")
		points = [
			AffineCurvePoint(3117110232563059246980187946198621, 3317437604270820210689740076391407, e),
			AffineCurvePoint(1337243996230764682967860953280223, 2063522037029258959118399626141682, e),
			AffineCurvePoint(235253700287668808185890937034851, 830989660091878453658335933918000, e),
			AffineCurvePoint(627781032099779919607023000566247, 1603622602577594429014913566107033, e),
			AffineCurvePoint(1929761220615891268483335561783138, 1546624911677232240933310892908962, e),
			AffineCurvePoint(872432267721461912738308679449077, 2729640644726851734745963545037841, e),
		]
		for point in points:
			self.assertTrue(point.oncurve())
		self.assertEqual(points[0] + points[0], AffineCurvePoint(4064734346459959837711463108666078, 1633739364791553181243017790342803, e))
		self.assertTrue(AffineCurvePoint(4064734346459959837711463108666078, 1633739364791553181243017790342803, e).oncurve())
		self.assertEqual(points[0] + points[1], AffineCurvePoint(3723026810340743432839738672226419, 539418558131017701255799570461878, e))
		self.assertTrue(AffineCurvePoint(3723026810340743432839738672226419, 539418558131017701255799570461878, e).oncurve())
		self.assertEqual(points[0] + points[2], AffineCurvePoint(2666739795283455355388717400402993, 2972821526814170767052592315049242, e))
		self.assertTrue(AffineCurvePoint(2666739795283455355388717400402993, 2972821526814170767052592315049242, e).oncurve())
		self.assertEqual(points[0] + points[3], AffineCurvePoint(87040431305643233801949973598186, 4174712248394499122322627644575650, e))
		self.assertTrue(AffineCurvePoint(87040431305643233801949973598186, 4174712248394499122322627644575650, e).oncurve())
		self.assertEqual(points[0] + points[4], AffineCurvePoint(2802418382414800560683276089692115, 2630760185865310406957414586693079, e))
		self.assertTrue(AffineCurvePoint(2802418382414800560683276089692115, 2630760185865310406957414586693079, e).oncurve())
		self.assertEqual(points[0] + points[5], AffineCurvePoint(4288609280448373691375140747355688, 420581842128121271226447977613081, e))
		self.assertTrue(AffineCurvePoint(4288609280448373691375140747355688, 420581842128121271226447977613081, e).oncurve())
		self.assertEqual(points[1] + points[0], AffineCurvePoint(3723026810340743432839738672226419, 539418558131017701255799570461878, e))
		self.assertTrue(AffineCurvePoint(3723026810340743432839738672226419, 539418558131017701255799570461878, e).oncurve())
		self.assertEqual(points[1] + points[1], AffineCurvePoint(3591145884720261338103575780699807, 4315217519961907532019414100448261, e))
		self.assertTrue(AffineCurvePoint(3591145884720261338103575780699807, 4315217519961907532019414100448261, e).oncurve())
		self.assertEqual(points[1] + points[2], AffineCurvePoint(767654518279343783442373102239656, 931581834311445282420568360496919, e))
		self.assertTrue(AffineCurvePoint(767654518279343783442373102239656, 931581834311445282420568360496919, e).oncurve())
		self.assertEqual(points[1] + points[3], AffineCurvePoint(3586051730372413391716540216032874, 1732668913318031500067892336307807, e))
		self.assertTrue(AffineCurvePoint(3586051730372413391716540216032874, 1732668913318031500067892336307807, e).oncurve())
		self.assertEqual(points[1] + points[4], AffineCurvePoint(4319220890821527825482144178575612, 723068585981600829545356089627049, e))
		self.assertTrue(AffineCurvePoint(4319220890821527825482144178575612, 723068585981600829545356089627049, e).oncurve())
		self.assertEqual(points[1] + points[5], AffineCurvePoint(3782803895644916151556214584437161, 2771961082269130926455794722149390, e))
		self.assertTrue(AffineCurvePoint(3782803895644916151556214584437161, 2771961082269130926455794722149390, e).oncurve())
		self.assertEqual(points[2] + points[0], AffineCurvePoint(2666739795283455355388717400402993, 2972821526814170767052592315049242, e))
		self.assertTrue(AffineCurvePoint(2666739795283455355388717400402993, 2972821526814170767052592315049242, e).oncurve())
		self.assertEqual(points[2] + points[1], AffineCurvePoint(767654518279343783442373102239656, 931581834311445282420568360496919, e))
		self.assertTrue(AffineCurvePoint(767654518279343783442373102239656, 931581834311445282420568360496919, e).oncurve())
		self.assertEqual(points[2] + points[2], AffineCurvePoint(2120325548453476461903987486245115, 2843555047937458025861854944861757, e))
		self.assertTrue(AffineCurvePoint(2120325548453476461903987486245115, 2843555047937458025861854944861757, e).oncurve())
		self.assertEqual(points[2] + points[3], AffineCurvePoint(2869160181194689537159393771033225, 2388609795801451355008363813919312, e))
		self.assertTrue(AffineCurvePoint(2869160181194689537159393771033225, 2388609795801451355008363813919312, e).oncurve())
		self.assertEqual(points[2] + points[4], AffineCurvePoint(1443848317651251533912280184260615, 3507966784103250297258176930645556, e))
		self.assertTrue(AffineCurvePoint(1443848317651251533912280184260615, 3507966784103250297258176930645556, e).oncurve())
		self.assertEqual(points[2] + points[5], AffineCurvePoint(1528876984675717023713801774301100, 3700884665652262932134185881457463, e))
		self.assertTrue(AffineCurvePoint(1528876984675717023713801774301100, 3700884665652262932134185881457463, e).oncurve())
		self.assertEqual(points[3] + points[0], AffineCurvePoint(87040431305643233801949973598186, 4174712248394499122322627644575650, e))
		self.assertTrue(AffineCurvePoint(87040431305643233801949973598186, 4174712248394499122322627644575650, e).oncurve())
		self.assertEqual(points[3] + points[1], AffineCurvePoint(3586051730372413391716540216032874, 1732668913318031500067892336307807, e))
		self.assertTrue(AffineCurvePoint(3586051730372413391716540216032874, 1732668913318031500067892336307807, e).oncurve())
		self.assertEqual(points[3] + points[2], AffineCurvePoint(2869160181194689537159393771033225, 2388609795801451355008363813919312, e))
		self.assertTrue(AffineCurvePoint(2869160181194689537159393771033225, 2388609795801451355008363813919312, e).oncurve())
		self.assertEqual(points[3] + points[3], AffineCurvePoint(176878457604457698579663631864190, 721471289065271224834385424962611, e))
		self.assertTrue(AffineCurvePoint(176878457604457698579663631864190, 721471289065271224834385424962611, e).oncurve())
		self.assertEqual(points[3] + points[4], AffineCurvePoint(2562156057939871711326640460445945, 3577511574269877768475169588752653, e))
		self.assertTrue(AffineCurvePoint(2562156057939871711326640460445945, 3577511574269877768475169588752653, e).oncurve())
		self.assertEqual(points[3] + points[5], AffineCurvePoint(148146258284214251215275786030378, 1329592514181691255155018041558553, e))
		self.assertTrue(AffineCurvePoint(148146258284214251215275786030378, 1329592514181691255155018041558553, e).oncurve())
		self.assertEqual(points[4] + points[0], AffineCurvePoint(2802418382414800560683276089692115, 2630760185865310406957414586693079, e))
		self.assertTrue(AffineCurvePoint(2802418382414800560683276089692115, 2630760185865310406957414586693079, e).oncurve())
		self.assertEqual(points[4] + points[1], AffineCurvePoint(4319220890821527825482144178575612, 723068585981600829545356089627049, e))
		self.assertTrue(AffineCurvePoint(4319220890821527825482144178575612, 723068585981600829545356089627049, e).oncurve())
		self.assertEqual(points[4] + points[2], AffineCurvePoint(1443848317651251533912280184260615, 3507966784103250297258176930645556, e))
		self.assertTrue(AffineCurvePoint(1443848317651251533912280184260615, 3507966784103250297258176930645556, e).oncurve())
		self.assertEqual(points[4] + points[3], AffineCurvePoint(2562156057939871711326640460445945, 3577511574269877768475169588752653, e))
		self.assertTrue(AffineCurvePoint(2562156057939871711326640460445945, 3577511574269877768475169588752653, e).oncurve())
		self.assertEqual(points[4] + points[4], AffineCurvePoint(3074072036822685021436989941342785, 3157984599511588306440992673720004, e))
		self.assertTrue(AffineCurvePoint(3074072036822685021436989941342785, 3157984599511588306440992673720004, e).oncurve())
		self.assertEqual(points[4] + points[5], AffineCurvePoint(2219827979145724699972786737693217, 4167759417703712591322494207750534, e))
		self.assertTrue(AffineCurvePoint(2219827979145724699972786737693217, 4167759417703712591322494207750534, e).oncurve())
		self.assertEqual(points[5] + points[0], AffineCurvePoint(4288609280448373691375140747355688, 420581842128121271226447977613081, e))
		self.assertTrue(AffineCurvePoint(4288609280448373691375140747355688, 420581842128121271226447977613081, e).oncurve())
		self.assertEqual(points[5] + points[1], AffineCurvePoint(3782803895644916151556214584437161, 2771961082269130926455794722149390, e))
		self.assertTrue(AffineCurvePoint(3782803895644916151556214584437161, 2771961082269130926455794722149390, e).oncurve())
		self.assertEqual(points[5] + points[2], AffineCurvePoint(1528876984675717023713801774301100, 3700884665652262932134185881457463, e))
		self.assertTrue(AffineCurvePoint(1528876984675717023713801774301100, 3700884665652262932134185881457463, e).oncurve())
		self.assertEqual(points[5] + points[3], AffineCurvePoint(148146258284214251215275786030378, 1329592514181691255155018041558553, e))
		self.assertTrue(AffineCurvePoint(148146258284214251215275786030378, 1329592514181691255155018041558553, e).oncurve())
		self.assertEqual(points[5] + points[4], AffineCurvePoint(2219827979145724699972786737693217, 4167759417703712591322494207750534, e))
		self.assertTrue(AffineCurvePoint(2219827979145724699972786737693217, 4167759417703712591322494207750534, e).oncurve())
		self.assertEqual(points[5] + points[5], AffineCurvePoint(137680862920165800159415222573783, 3475375738534728619472562866721341, e))
		self.assertTrue(AffineCurvePoint(137680862920165800159415222573783, 3475375738534728619472562866721341, e).oncurve())
		self.assertEqual(244731188 * points[0], AffineCurvePoint(799343867892131331328116631700028, 3238045619580805561449053238064641, e))
		self.assertTrue(AffineCurvePoint(799343867892131331328116631700028, 3238045619580805561449053238064641, e).oncurve())
		self.assertEqual(479215585 * points[0], AffineCurvePoint(2706730081538110138078384782047852, 2881713554078961053511508101371441, e))
		self.assertTrue(AffineCurvePoint(2706730081538110138078384782047852, 2881713554078961053511508101371441, e).oncurve())
		self.assertEqual(615977890 * points[0], AffineCurvePoint(3838979374142936020593894026971284, 2353562327773064373435074287667816, e))
		self.assertTrue(AffineCurvePoint(3838979374142936020593894026971284, 2353562327773064373435074287667816, e).oncurve())
		self.assertEqual(550140093 * points[0], AffineCurvePoint(200065277622376526049681520014276, 51209742086984118724200802806153, e))
		self.assertTrue(AffineCurvePoint(200065277622376526049681520014276, 51209742086984118724200802806153, e).oncurve())
		self.assertEqual(540588643 * points[0], AffineCurvePoint(2708454351094974414186353284132004, 482908022980745877814430356771611, e))
		self.assertTrue(AffineCurvePoint(2708454351094974414186353284132004, 482908022980745877814430356771611, e).oncurve())
		self.assertEqual(672739461 * points[0], AffineCurvePoint(1030814758650133152061550844236032, 1823080711222015183880343693623151, e))
		self.assertTrue(AffineCurvePoint(1030814758650133152061550844236032, 1823080711222015183880343693623151, e).oncurve())
		self.assertEqual(910647265 * points[1], AffineCurvePoint(137737857707196532599472608676360, 957907527391095020531740031338079, e))
		self.assertTrue(AffineCurvePoint(137737857707196532599472608676360, 957907527391095020531740031338079, e).oncurve())
		self.assertEqual(399781155 * points[1], AffineCurvePoint(3761977973845283625480428585967217, 2353350788128670145920555879879491, e))
		self.assertTrue(AffineCurvePoint(3761977973845283625480428585967217, 2353350788128670145920555879879491, e).oncurve())
		self.assertEqual(438499287 * points[1], AffineCurvePoint(791784310872674310944665210228985, 1430904795413769943854621265242346, e))
		self.assertTrue(AffineCurvePoint(791784310872674310944665210228985, 1430904795413769943854621265242346, e).oncurve())
		self.assertEqual(30329342 * points[1], AffineCurvePoint(842488465058721644608558481954980, 3887929284060323035133050694924699, e))
		self.assertTrue(AffineCurvePoint(842488465058721644608558481954980, 3887929284060323035133050694924699, e).oncurve())
		self.assertEqual(967116404 * points[1], AffineCurvePoint(4155601987656967768431349496277491, 192440768853698673613506368932279, e))
		self.assertTrue(AffineCurvePoint(4155601987656967768431349496277491, 192440768853698673613506368932279, e).oncurve())
		self.assertEqual(927133616 * points[1], AffineCurvePoint(2556810828429079101914439119665354, 2524847108175393854549561825759512, e))
		self.assertTrue(AffineCurvePoint(2556810828429079101914439119665354, 2524847108175393854549561825759512, e).oncurve())
		self.assertEqual(206990082 * points[2], AffineCurvePoint(1707574986822913143399470421926442, 131328589915508399663105547392277, e))
		self.assertTrue(AffineCurvePoint(1707574986822913143399470421926442, 131328589915508399663105547392277, e).oncurve())
		self.assertEqual(145434778 * points[2], AffineCurvePoint(193470908356734603666578767473410, 3004503290193422403586016715967043, e))
		self.assertTrue(AffineCurvePoint(193470908356734603666578767473410, 3004503290193422403586016715967043, e).oncurve())
		self.assertEqual(454728583 * points[2], AffineCurvePoint(4400079036925892699736681855331890, 3088617866065122674311000109236495, e))
		self.assertTrue(AffineCurvePoint(4400079036925892699736681855331890, 3088617866065122674311000109236495, e).oncurve())
		self.assertEqual(135155369 * points[2], AffineCurvePoint(2027712979252276636045660473448539, 2164103391295458545875249924786406, e))
		self.assertTrue(AffineCurvePoint(2027712979252276636045660473448539, 2164103391295458545875249924786406, e).oncurve())
		self.assertEqual(3646348 * points[2], AffineCurvePoint(222482181719241110158914176464073, 1175253763932995577527931926137281, e))
		self.assertTrue(AffineCurvePoint(222482181719241110158914176464073, 1175253763932995577527931926137281, e).oncurve())
		self.assertEqual(510578945 * points[2], AffineCurvePoint(1261291574979275348201458226343995, 3102733652715577691117533666551442, e))
		self.assertTrue(AffineCurvePoint(1261291574979275348201458226343995, 3102733652715577691117533666551442, e).oncurve())
		self.assertEqual(773473903 * points[3], AffineCurvePoint(741959927009188871583680615949638, 2093971120945716035639075368016278, e))
		self.assertTrue(AffineCurvePoint(741959927009188871583680615949638, 2093971120945716035639075368016278, e).oncurve())
		self.assertEqual(997111420 * points[3], AffineCurvePoint(1248100720882585714838579280838399, 4438594924170079853980619795252553, e))
		self.assertTrue(AffineCurvePoint(1248100720882585714838579280838399, 4438594924170079853980619795252553, e).oncurve())
		self.assertEqual(668321744 * points[3], AffineCurvePoint(395886649333065339235666595510340, 3755881760237441545879003514708540, e))
		self.assertTrue(AffineCurvePoint(395886649333065339235666595510340, 3755881760237441545879003514708540, e).oncurve())
		self.assertEqual(829980073 * points[3], AffineCurvePoint(1735323911926967505958820072450473, 1405878229247618255874049365208656, e))
		self.assertTrue(AffineCurvePoint(1735323911926967505958820072450473, 1405878229247618255874049365208656, e).oncurve())
		self.assertEqual(441912688 * points[3], AffineCurvePoint(2904753317362970167836831382358365, 1137554067721498868296881430795660, e))
		self.assertTrue(AffineCurvePoint(2904753317362970167836831382358365, 1137554067721498868296881430795660, e).oncurve())
		self.assertEqual(970575074 * points[3], AffineCurvePoint(313100336875746517104210806321395, 2084520610118571098315493974262361, e))
		self.assertTrue(AffineCurvePoint(313100336875746517104210806321395, 2084520610118571098315493974262361, e).oncurve())
		self.assertEqual(606215582 * points[4], AffineCurvePoint(2850264680963666931636271668878004, 2167820720348711946721651674088979, e))
		self.assertTrue(AffineCurvePoint(2850264680963666931636271668878004, 2167820720348711946721651674088979, e).oncurve())
		self.assertEqual(968223364 * points[4], AffineCurvePoint(752966669767470049793829658672502, 817295934273335397573319216079235, e))
		self.assertTrue(AffineCurvePoint(752966669767470049793829658672502, 817295934273335397573319216079235, e).oncurve())
		self.assertEqual(26106169 * points[4], AffineCurvePoint(404431198475874236899098181363662, 2296789183245184747073488685011926, e))
		self.assertTrue(AffineCurvePoint(404431198475874236899098181363662, 2296789183245184747073488685011926, e).oncurve())
		self.assertEqual(379289443 * points[4], AffineCurvePoint(723353446510304113034686043795598, 292865962596212029663654924152756, e))
		self.assertTrue(AffineCurvePoint(723353446510304113034686043795598, 292865962596212029663654924152756, e).oncurve())
		self.assertEqual(523987778 * points[4], AffineCurvePoint(825694777938573065404675043994059, 1338729390845431942346396395449572, e))
		self.assertTrue(AffineCurvePoint(825694777938573065404675043994059, 1338729390845431942346396395449572, e).oncurve())
		self.assertEqual(885647483 * points[4], AffineCurvePoint(801298464780419945624371970788438, 4072001729606023524262744717618362, e))
		self.assertTrue(AffineCurvePoint(801298464780419945624371970788438, 4072001729606023524262744717618362, e).oncurve())
		self.assertEqual(634165049 * points[5], AffineCurvePoint(314787966440069146423812028140757, 3759178934144635742129828380139388, e))
		self.assertTrue(AffineCurvePoint(314787966440069146423812028140757, 3759178934144635742129828380139388, e).oncurve())
		self.assertEqual(406547467 * points[5], AffineCurvePoint(3915579942088610581276212551825744, 1735075139758492739634365954880527, e))
		self.assertTrue(AffineCurvePoint(3915579942088610581276212551825744, 1735075139758492739634365954880527, e).oncurve())
		self.assertEqual(977999735 * points[5], AffineCurvePoint(4047764598782335211666165260642656, 3390395305328029707188373076630799, e))
		self.assertTrue(AffineCurvePoint(4047764598782335211666165260642656, 3390395305328029707188373076630799, e).oncurve())
		self.assertEqual(59143884 * points[5], AffineCurvePoint(4142931471858723228703092484057487, 1211817578182076750442156342501316, e))
		self.assertTrue(AffineCurvePoint(4142931471858723228703092484057487, 1211817578182076750442156342501316, e).oncurve())
		self.assertEqual(130367752 * points[5], AffineCurvePoint(2080598045063511954398353433475040, 3372609893215355160406007246405785, e))
		self.assertTrue(AffineCurvePoint(2080598045063511954398353433475040, 3372609893215355160406007246405785, e).oncurve())
		self.assertEqual(537668229 * points[5], AffineCurvePoint(2137496744785763901399697229984622, 4394820220824082213468385758117630, e))
		self.assertTrue(AffineCurvePoint(2137496744785763901399697229984622, 4394820220824082213468385758117630, e).oncurve())

