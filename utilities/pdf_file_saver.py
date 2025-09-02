import os


def assertion_for_bytes(file_path: str):
    """ ASSERTION FOR EMPTY FILE TYPE """

    file_type = file_path.split('.')[1]
    file_size = os.path.getsize(file_path)
    match file_type:
        case "pdf":
            assert file_size > 1024
        case "doc":
            assert file_size > 24000
        case "docx":
            assert file_size > 6000
        case "xls":
            assert file_size > 16000
        case "xlsx":
            assert file_size > 7000


def save_response_to_file(file_path: str, response_data: bytes):
    with open(file_path, "wb") as f:
        f.write(response_data)

    assertion_for_bytes(file_path=file_path)

