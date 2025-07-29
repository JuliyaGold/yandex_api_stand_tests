
import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки

def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body,sender_stand_request.get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a") 


# Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Функция негативной проверки

def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body,sender_stand_request.get_new_user_token())
    assert response.status_code == 400

# Параметр name состоит из 0 символов
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_symbol("")

# Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Параметр name состоит из английских символов
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Параметр name состоит из русских символов
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Параметр name состоит из специальных символов
def test_create_kit_has_special_symbol_letter_in_name_get_success_response():
    negative_assert_symbol('"№%@",')

# Параметр name с пробелами
def test_create_kit_has_space_letter_in_name_get_success_response():
    positive_assert("Человек и КО")

# Параметр name состоит из цифр
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Функция негативной проверки

def negative_assert_no_name(kit_body):
   response = sender_stand_request.post_new_user(kit_body)
   assert response.status_code == 400

# Параметр name не передан в запросе
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

# Параметр name состоит из числа
def test_create_kit_has_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body,sender_stand_request.get_new_user_token())
    assert response.status_code == 400