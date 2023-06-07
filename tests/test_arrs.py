from utils.arrs import get, my_slice





def test_get_non_existing_index():
    # Тестирование получения значения по несуществующему индексу == ==
    array = [1, 2, 3, 4, 5]
    index = 10
    default = "Not found"
    expected_result = default

    result = get(array, index, default)

    assert result == expected_result



def test_get_existing_index():
    # Тестирование получения значения по существующему индексу
    array = [1, 2, 3, 4, 5]
    index = 1
    default = "Not found"
    expected_result = array[index]

    result = get(array, index, default)

    assert result == expected_result


def test_get_negative_index():
    # Тестирование получения значения по отрицательному индексу ==
    array = [1, 2, 3, 4, 5]
    index = -2
    default = None
    expected_result = default

    result = get(array, index, default)

    assert result == expected_result


def test_my_slice_start():
    # Тестирование извлечения среза с указанием начального индекса
    coll = [1, 2, 3, 4, 5]
    start = 2
    expected_result = [3, 4, 5]

    result = my_slice(coll, start=start)

    assert result == expected_result

def test_my_slice_default_arguments():
    # Тестирование извлечения среза с использованием значений по умолчанию
    coll = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]

    result = my_slice(coll)

    assert result == expected_result




def test_my_slice_end():
    # Тестирование извлечения среза с указанием конечного индекса
    coll = [1, 2, 3, 4, 5]
    end = 4
    expected_result = [1, 2, 3, 4]

    result = my_slice(coll, end=end)

    assert result == expected_result


def test_my_slice_negative_indices():
    # Тестирование извлечения среза с использованием отрицательных индексов
    coll = [1, 2, 3, 4, 5]
    start = -3
    end = -1
    expected_result = [3, 4]

    result = my_slice(coll, start, end)

    assert result == expected_result



def test_get_non_existing_index():
    # Тестирование получения значения по несуществующему индексу
    array = [1, 2, 3, 4, 5]
    index = 10
    default = "Not found"
    expected_result = default

    result = get(array, index, default)

    assert result == expected_result


def test_get_existing_index():
    # Тестирование получения значения по существующему индексу
    array = [1, 2, 3, 4, 5]
    index = 1
    default = "Not found"
    expected_result = array[index]

    result = get(array, index, default)

    assert result == expected_result


def test_get_negative_index():
    # Тестирование получения значения по отрицательному индексу
    array = [1, 2, 3, 4, 5]
    index = -2
    default = None
    expected_result = default

    result = get(array, index, default)

    assert result == expected_result


def test_my_slice_start():
    # Тестирование извлечения среза с указанием начального индекса
    coll = [1, 2, 3, 4, 5]
    start = 2
    expected_result = [3, 4, 5]

    result = my_slice(coll, start=start)

    assert result == expected_result


def test_my_slice_default_arguments():
    # Тестирование извлечения среза с использованием значений по умолчанию
    coll = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]

    result = my_slice(coll)

    assert result == expected_result


def test_my_slice_end():
    # Тестирование извлечения среза с указанием конечного индекса
    coll = [1, 2, 3, 4, 5]
    end = 4
    expected_result = [1, 2, 3, 4]

    result = my_slice(coll, end=end)

    assert result == expected_result


def test_my_slice_negative_indices():
    # Тестирование извлечения среза с использованием отрицательных индексов
    coll = [1, 2, 3, 4, 5]
    start = -3
    end = -1
    expected_result = [3, 4]

    result = my_slice(coll, start, end)

    assert result == expected_result


def test_get_out_of_range_index():
    # Тестирование получения значения по индексу, выходящему за границы списка
    array = [1, 2, 3, 4, 5]
    index = 10
    default = "Not found"
    expected_result = default

    result = get(array, index, default)

    assert result == expected_result


def test_my_slice_negative_start():
    # Тестирование извлечения среза с отрицательным начальным индексом
    coll = [1, 2, 3, 4, 5]
    start = -5
    expected_result = coll

    result = my_slice(coll, start=start)

    assert result == expected_result
