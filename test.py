from triangle import *
import unittest
import math

class testTriangle(unittest.TestCase):

    def testCheckinput1(self):
        self.assertEqual(True,checkinput(10.0,2.3,4.5))

    def testCheckinput2(self):
        self.assertEqual(True,checkinput(0.00001,0.00001,0.00001))

    def testCheckinput3(self):
        self.assertEqual(True,checkinput(1.0*(2**30),1.0*(2**30),1.0*(2**30)))

    def testCheckinput4(self):
        self.assertEqual(False,checkinput(1,12.0,3))

    def testCheckinput5(self):
        self.assertEqual(False,checkinput(0.00001,1,0.00001))

    def testCheckinput6(self):
        self.assertEqual(False,checkinput(2**30,1.0*(2**30),1.0*(2**30)))

    def testDetect_triangle1(self):
        self.assertEqual('tam giac deu',detect_triangle(5.0,5.0,5.0))

    def testDetect_triangle2(self):
        self.assertEqual('tam giac deu',detect_triangle(0.00001,0.00001,0.00001))

    def testDetect_triangle3(self):
        self.assertEqual('tam giac deu',detect_triangle(1.0*(2**30),1.0*(2**30),1.0*(2**30)))

    def testDetect_triangle4(self):
        self.assertEqual('tam giac vuong can',detect_triangle(5.0,5.0,5.0*math.sqrt(2)))

    def testDetect_triangle5(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*math.pow(10,-30),1.0*math.pow(10,-30),1.0*math.pow(10,-30)*math.sqrt(2)))

    def testDetect_triangle6(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*(2**30),1.0*(2**30),1.0*(2**30)*math.sqrt(2)))

    def testDetect_triangle7(self):
        self.assertEqual('tam giac can',detect_triangle(4.0,4.1,4.1))

    def testDetect_triangle8(self):
        self.assertEqual('tam giac can',detect_triangle(0.00001,0.000011,0.00001))

    def testDetect_triangle9(self):
        self.assertEqual('tam giac can',detect_triangle(1.0*(2**30),1.0*(2**30),1.2*(2**30)))

    def testDetect_triangle10(self):
        self.assertEqual('tam giac vuong',detect_triangle(4.0,3.0,5.0))

    def testDetect_triangle11(self):
        self.assertEqual('tam giac vuong',detect_triangle(0.00003,0.00004,0.00005))

    def testDetect_triangle12(self):
        self.assertEqual('tam giac vuong',detect_triangle(3.0*(10**31),4.0*(10**31),5.0*(10**31)))

    def testDetect_triangle13(self):
        self.assertEqual('tam giac thuong',detect_triangle(4.0,6.0,5.0))

    def testDetect_triangle14(self):
        self.assertEqual('tam giac thuong',detect_triangle(0.00004,0.00006,0.00005))

    def testDetect_triangle15(self):
        self.assertEqual('tam giac thuong',detect_triangle(4.0*(10**31),6.0*(10**31),5.0*(10**31)))

    def testDetect_triangle16(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0,3.0,8.0))

    def testDetect_triangle17(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(0.00004,0.00003,0.00008))
    
    def testDetect_triangle18(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0*(10**31),3.0*(10**31),9.0*(10**31)))

unittest.main()
