import unittest
from termkit import clamp
class Tests(unittest.TestCase):
 def test_clamp(self): self.assertEqual(clamp(20,0,10),10); self.assertEqual(clamp(-1,0,10),0)
if __name__=='__main__': unittest.main()
