from gendiff.file_reader import get_data
from gendiff.difference_finder import get_diff
from gendiff.formatter.stylish import get_stylish_view
from gendiff.formatter.plain import get_plain_view
from gendiff.formatter.json import write_in_json


def post_processing(data):
    replace_values = (("False", "false"), ("True", "true"), ("None", "null"))
    for first_value, second_value in replace_values:
        data = data.replace(first_value, second_value)
    return data


def get_result(first_file, second_file, formatter='stylish'):
    if formatter == 'stylish':
        return post_processing(get_stylish_view(
            get_diff(get_data(first_file), get_data(second_file))))

    elif formatter == 'json':
        return write_in_json(
            get_diff(get_data(first_file), get_data(second_file)))

    else:
        return post_processing(get_plain_view(
            get_diff(get_data(first_file), get_data(second_file))))
