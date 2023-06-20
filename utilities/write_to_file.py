def save_file(file_path: str, content: any) -> None:
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path: str, content: any) -> None:
    with open(file_path, 'a') as file:
        file.write(content + "\n")
