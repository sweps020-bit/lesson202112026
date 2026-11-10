from app.utils.utils import calculate_discount, is_even, get_full_name


def test_discount_20():
    assert calculate_discount(100, 20) == 80


def test_discount_50():
    assert calculate_discount(200, 50) == 100


def test_discount_0():
    assert calculate_discount(150, 0) == 150


def test_discount_price_0():
    assert calculate_discount(0, 30) == 0


def test_discount_other():
    assert calculate_discount(60, 15) == 51


def test_is_even_positive_even():
    assert is_even(4) == True


def test_is_even_positive_odd():
    assert is_even(7) == False


def test_is_even_negative_even():
    assert is_even(-6) == True


def test_is_even_negative_odd():
    assert is_even(-3) == False


def test_is_even_zero():
    assert is_even(0) == True


def test_full_name_tima_havryl():
    assert get_full_name("Tima", "Havryl") == "Tima Havryl"


def test_full_name_short_tim():
    assert get_full_name("Tim", "Havryl") == "Tim Havryl"


def test_full_name_long_timofey():
    assert get_full_name("Timofey", "Havryl") == "Timofey Havryl"


def test_full_name_one_letter_t_h():
    assert get_full_name("T", "H") == "T H"


def test_full_name_other_tima_h():
    assert get_full_name("Tima", "H") == "Tima H"