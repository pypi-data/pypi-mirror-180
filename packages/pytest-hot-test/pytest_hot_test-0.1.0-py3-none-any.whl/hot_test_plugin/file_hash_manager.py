import os
import hashlib
import dataclasses
from hot_test_plugin import settings

from typing import List, Tuple


@dataclasses.dataclass
class FileHash:
    filepath: str
    hash: str

    @classmethod
    def from_filepath(cls, filepath: str):
        return get_file_hash(filepath)

    def __str__(self):
        return f"{self.filepath} : {self.hash}"


def get_file_hash(filepath: str) -> FileHash:
    if not os.path.exists(filepath):
        TypeError(f"Path does not exist: {filepath}. Cannot compute hash")
    with open(filepath, "r") as fp:
        file_content = fp.read()
        md5 = hashlib.md5(file_content.encode()).hexdigest()
        return FileHash(
            filepath=filepath,
            hash=md5,
        )


def _get_test_filename(filepath: str) -> str:
    return filepath.split("/")[-1].replace(".py", ".txt")


def _get_test_hash_filepath(filepath: str) -> str:
    test_folder = _get_test_folder()
    dir_, fp_ = _merge_folder(test_folder, filepath)
    _bootstrap_folder(dir_)
    filename = _get_test_filename(fp_)
    test_hash_filepath = os.path.join(dir_, filename)
    return test_hash_filepath


def _get_test_folder():
    return os.path.join(settings.PLUGIN_HASH_FOLDER, "test/")


def _get_dependencies_folder():
    return os.path.join(settings.PLUGIN_HASH_FOLDER, "dependencies/")


def _merge_folder(plugin_folder: str, test_filepath: str) -> Tuple[str, str]:
    # Merge with plugin hash source folder
    source_folder = plugin_folder
    filename = test_filepath.split("/")[-1]
    filename = filename.replace(".py", ".txt")
    filename = ".hashes_" + filename

    # Hashes filepath
    hashes_filepath = "/".join(test_filepath.split("/")[0:-1] + [filename])
    hashes_filepath = hashes_filepath[1:]
    hashes_filepath = os.path.join(source_folder, hashes_filepath)
    hashes_dir = os.path.dirname(hashes_filepath)
    hashes_filepath = hashes_filepath
    return hashes_dir, hashes_filepath


def _bootstrap_folder(folder: str):
    if not os.path.exists(folder):
        os.makedirs(folder)


def get_test_file_hash(filepath: str) -> List[FileHash]:
    test_hash_filepath = _get_test_hash_filepath(filepath)
    if os.path.exists(test_hash_filepath):
        return read_hash_file(test_hash_filepath)
    return []


def save_test_file_hash(filepath: str, file_hash: FileHash):
    test_hash_filepath = _get_test_hash_filepath(filepath)
    save_hash_file(test_hash_filepath, [file_hash])


def read_hash_file(filepath: str) -> List[FileHash]:
    with open(filepath, "r") as fp:
        lines = fp.readlines()

    file_hashes: List[FileHash] = []
    for line in lines:
        split = line.strip().split(" ")
        hash = split[0]
        file_ = split[1]
        file_hashes.append(FileHash(filepath=file_, hash=hash))
    return file_hashes


def save_hash_file(filepath: str, file_hashes: List[FileHash]):
    with open(filepath, "w") as fp:
        for file_hash in file_hashes:
            fp.write(f"{file_hash.hash} {file_hash.filepath}\n")


class HashManager:
    def __init__(self, filepath: str) -> None:
        dir_, fp_ = _merge_folder(_get_dependencies_folder(), filepath)
        self.hashes_dir = dir_
        self.hashes_filepath = fp_
        _bootstrap_folder(self.hashes_dir)

        self.hashes = []

    def load(self):
        if not os.path.exists(self.hashes_filepath):
            return []
        self.hashes = read_hash_file(self.hashes_filepath)
        return self.hashes

    def save(self, file_hashes: List[FileHash]):
        self.hashes = file_hashes
        save_hash_file(self.hashes_filepath, file_hashes)
