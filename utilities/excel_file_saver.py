

def saver_response_to_file(file_path: str, response_data:bytes):
    with open(file_path, "wb") as f:
        bytes_written = f.write(response_data)
        assert bytes_written > 0 , f"Failed to write Excel file: {file_path}"