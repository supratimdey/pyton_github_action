 

from src.pymain import sdSqr
from src.pymain import sayHello


class  Testing_functions:

  def test_sqr(self):
    assert sdSqr(5) == 25
  
  def test_sayHello(self):
      assert sayHello('Tim') == "Hello Tim"


Testing_functions.test_sqr
Testing_functions.test_sayHello