import os


def join_path(parent_dir_path: str, subdir_path: str) -> str:
    joined_path = os.path.abspath(
        os.path.join(parent_dir_path, subdir_path)
    )
    return joined_path


def create_dir(dir_path: str) -> None:
    # create subdir path
    os.makedirs(dir_path, exist_ok=True)


def to_indexed_file(parent_dir_name: str, subdir_name: str, file_name: str) -> str:
    """
    USE FOR
    parent_dir/test_name_dir/image_1.png
    parent_dir/test_name_dir/image_2.png etc...
    """
    # path to the file
    subdir_plus_file_path = f"{subdir_name}/{file_name}"

    # create full path
    full_path = join_path(parent_dir_name, subdir_plus_file_path)

    # create subdir, so file can be saved inside
    create_dir(parent_dir_name+"/"+subdir_name)

    return full_path


def to_file(parent_dir_name: str, file_name: str) -> str:
    """
    USE FOR
    parent_dir/test_name.txt
    """
    full_path = join_path(parent_dir_name, file_name)
    create_dir(parent_dir_name)
    return full_path
