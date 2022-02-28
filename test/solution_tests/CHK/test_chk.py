from solutions.CHK import checkout_solution


class TestChk():
    def test_chk(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('AAAAA') == 200
        assert checkout_solution.checkout('AAAAAA') == 250
        assert checkout_solution.checkout('BBB') == 75
        assert checkout_solution.checkout('') == 0
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('W') == -1
        assert checkout_solution.checkout('BBBEE') == 140

