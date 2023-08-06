
import unittest

class tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_trigger_pdb(self):
        #this is the way I do it now
        from jackals import BoolSeries, IntSeries, FloatSeries, StrSeries, TDataFrame
        
        price = FloatSeries(elements=[7.0, 3.5, 8.0, 6.0])
        sales = IntSeries(elements=[5, 3, 1, 10])
        taxed = BoolSeries(elements=[False, False, True, False])
        SKU = StrSeries(elements=["X4E", "T3B", "F8D", "C7X"])

        df = TDataFrame({"price" : price, "sales" : sales, "taxed" : taxed, "SKU" : SKU })

        result = df[(df["price"] + 5.0 > 10.0) and (df["sales"] > 3) and df["taxed"] ==  False]["SKU"]


        
if __name__=='__main__':
    unittest.main()