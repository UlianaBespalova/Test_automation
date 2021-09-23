import pytest


# ----- Структура данных int -----
# Обычный тест
def test_integer_convert_to_bytes():
    output = (1024).to_bytes(2, byteorder='big')
    assert output == b'\x04\x00'


# Параметризованный тест
@pytest.mark.parametrize('input, expected', [(3.5, 3), (12.9, 12), ('10', 10), (' -10 ', -10), ('012', 12),
                                             ('6_27', 627), (' +15 ', 15), (10., 10), (3.33e-10, 0),
                                             (0o177, 127), (0x9ff, 2559), (0b101010, 42)])
def test_integer_converting_from_types(input, expected):
    output = int(input)
    assert output == expected


# Негативный тест
def test_integer_bytes_len_negative():
    num = '10'
    try:
        assert int.bit_length(num) == 4
    except TypeError:
        pass


# ----- Структура данных dist -----

@pytest.fixture
def dictionary():
    return dict(dec=31, jan=31, feb=28)


# Обычный тест
def test_dict_clear(dictionary):
    assert dictionary.clear() is None


# Параметризованный тест
@pytest.mark.parametrize('key, default, expected', [('feb', None, 28), ('dec', None, 31), ('sep', 'def', 'def')])
def test_dict_get(key, default, expected, dictionary):
    lenght_old = len(dictionary)
    output = dictionary.get(key, default)
    lenght_new = len(dictionary)

    assert output == expected
    assert lenght_old == lenght_new


# Негативный тест
def test_dict_get_negative(dictionary):
    output = dictionary.get('sep')
    assert output == None
