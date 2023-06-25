import os
import shutil

from utilities.create_path import to_file, create_dir
from utilities.write_to_file import append_to_file


class CaseLogs:

    def __init__(self, artifacts_dir: str):
        self.artifacts_dir = artifacts_dir
        self.full_path = None

    def create(self, test_name: str) -> None:
        # get file name
        log_name = "steps_for_" + test_name + ".txt"

        # create general dir if it does not exist
        path_to_step_logs = to_file(self.artifacts_dir, 'test_case_logs')
        create_dir(path_to_step_logs)

        # get path to file
        self.full_path = to_file(path_to_step_logs, log_name)

        # create file if it doesn't exist yet
        if not os.path.exists(self.full_path): open(self.full_path, 'a').close()

    def add_step(self, content: str) -> None:
        if self.full_path is None:
            raise Exception("Use create method to create log file before adding steps.")
        else:
            append_to_file(self.full_path, content)

    def clean_artifacts(self) -> None:
        if os.path.exists(self.artifacts_dir):
            shutil.rmtree(self.artifacts_dir)
