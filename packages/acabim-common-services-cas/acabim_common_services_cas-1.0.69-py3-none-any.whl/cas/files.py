import os

from cas.aws import AwsFileType, AwsFileCategory, generate_bucket_path
from pathlib import Path

_ROOT_PATH = os.environ.get('FILE_MANAGER_ROOT') if os.environ.get('FILE_MANAGER_ROOT') is not None else Path.home()


def __get_dir_path(file_type: AwsFileType, file_category: AwsFileCategory, custom_path=None):
    dir_path = generate_bucket_path(file_category, file_type)
    result = Path(_ROOT_PATH).joinpath(dir_path)
    if custom_path is not None:
        result = result.joinpath(custom_path)

    return result


def get_file_path(file_type: AwsFileType, file_category: AwsFileCategory, file_name, custom_path=None):
    dir_path = __get_dir_path(file_type, file_category, custom_path)
    file_path = dir_path.joinpath(file_name)
    if file_path.suffix == '':
        ext = '.{0}'.format(file_type.name)
        file_path = file_path.with_suffix(ext)

    return file_path


if __name__ == '__main__':
    r = get_file_path(AwsFileType.IFC, AwsFileCategory.BuildingData, 'Building')
    print(r)
