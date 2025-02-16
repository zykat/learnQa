class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert a+b == 14
        expected_sum = 14
        assert a+b == expected_sum, f"Sum and variables a and b is not eqal to {expected_sum}"
    # python -m pytest .\test_examples.py -k "test_check_math"
    def test_check_math2(self):
        a = 5
        b = 11
        expected_sum = 14
        assert a+b == expected_sum, f"Sum and variables a and b is not eqal to {expected_sum}"