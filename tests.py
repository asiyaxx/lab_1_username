import subprocess


def test_valid_username():
    input_text = "123\n"
    process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    assert "Username is valid" in stdout, "Password '123' must be valid"


def test_valid_long_username():
    input_text = "123456789101112\n"
    process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    assert "Username is valid" in stdout, "Password '123456789101112' must be valid"


def test_short_username():
    input_text = "ab\n"
    process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    assert "Please, enter username from 3 to 15 characters and don't use ! or @" in stdout, "Password 'ab' is invalid because length must be more than 2 characters."


def test_long_username():
    input_text = "someverylonguser\n"
    process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    assert "Please, enter username from 3 to 15 characters and don't use ! or @" in stdout, "Password 'someveryverylongusername' is invalid because length must be less than 16 characters."


def test_username_with_wrong_char():
    input_text = "user@123\n"
    process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    assert "Please, enter username from 3 to 15 characters and don't use ! or @" in stdout, "Password 'user@123' must be invalid. Please check the username on the @ sign."


def test_username_with_exclamation_mark():
    input_text = "user!123\n"
    process = subprocess.Popen(["python", "main.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_text)

    assert "Please, enter username from 3 to 15 characters and don't use ! or @" in stdout, "Password 'user!123' is invalid. Please check the username on the ! sign."
