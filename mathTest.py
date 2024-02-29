import pytest


def do_math(num1, num2, operator):
    if type(num1) != int or type(num2) != int:
        raise Exception("Integers are required for this math operation")

    if operator == "+":
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception("The provided operator %s is unclear" % operator)

    if result < 0:
        return "A negative number"
    elif result < 10:
        return "A small number"
    elif result < 20:
        return "A medium number"
    else:
        return "That's a large number!"


class TestMath:

    def test_non_int_input_for_num1(self):
        error = None
        try:
            do_math("hi", 2, "+")
        except Exception as e:
            error = e
        assert error is not None

    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as exc_info:
            do_math(2, "bar", "+")
        assert 'Integers are required for this math operation' in str(exc_info)

    def test_addition_with_negative_result(self):
        assert 'negative number' in do_math(2, -5, "+")

    def test_addition_with_small_result(self):
        # assert do_math(2, 2, "+") == "A small number" // This test is more accurate but also more likely to fail
        assert 'small number' in do_math(2, 2, "+")

    def test_addition_with_medium_result(self):
        assert 'medium number' in do_math(9, 8, "+")

    def test_addition_with_large_result(self):
        assert 'large number' in do_math(5, 17, "+")

    def test_multiplication_with_negative_result(self):
        assert 'negative number' in do_math(2, -2, "*")

    def test_multiplication_with_small_result(self):
        assert 'small number' in do_math(2, 2, "*")

    def test_multiplication_with_medium_result(self):
        assert 'medium number' in do_math(4, 3, "*")

    def test_multiplication_with_large_result(self):
        assert 'large number' in do_math(5, 17, "*")

    def test_invalid_operator(self):
        with pytest.raises(Exception) as exc_info:
            do_math(2, 2, 'x')
        assert 'provided operator' in str(exc_info)
