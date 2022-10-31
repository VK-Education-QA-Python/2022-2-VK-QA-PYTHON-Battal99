import os


def file_path(name_file: str):
    rep = os.path.abspath(os.path.join(__file__, os.path.pardir))
    return os.path.join(rep, 'files', name_file)
