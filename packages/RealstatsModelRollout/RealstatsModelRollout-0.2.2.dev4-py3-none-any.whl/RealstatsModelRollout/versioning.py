from .settings import Settings
from .global_functions import globalFunctions as GF
from github import Github
from datetime import date
import os
import json
import subprocess

from six import string_types


class Versioning():
    def __init__(self):
        self._repo_name = ""
        self._model_version = ""
        self._model_name = ""
        self._branch_name = "main"

    @property
    def Repo_name(self):
        """
        :type: string
        """
        return self._repo_name

    @Repo_name.setter
    def Repo_name(self, value):
        """
        :type: string
        """
        self._repo_name = GF.Check_instance(value=value, instance_type="string")

    @property
    def Branch_name(self):
        """
        :type: string
        """
        return self._branch_name

    @Branch_name.setter
    def Branch_name(self, value):
        """
        :type: string
        """
        self._branch_name = GF.Check_instance(value=value, instance_type="string")

    @property
    def Model_version(self):
        """
        :type: string
        """
        return self._model_version

    @Model_version.setter
    def Model_version(self, value):
        """
        :type: string
        """
        self._model_version = GF.Check_instance(value=value, instance_type="string")

    @property
    def Model_name(self):
        """
        :type: string
        """
        return self._model_name

    @Model_name.setter
    def Model_name(self, value):
        """
        :type: string
        """
        self._model_name = GF.Check_instance(value=value, instance_type="string")

    # Upload the model and all its data to the github repo
    def Upload_enviroment(self, enviroment_localpath="Optional"):
        git = Github(Settings.Gitaccesstoken)
        git_repo = ""
        try:
            git_repo = git.get_repo(self._repo_name)
        except Exception as e:
            print(e)
            print("Not able to get given repo: " + self._repo_name)
            return

        git_user = git.get_user()
        git_user_data = git_user.get_emails()

        local_envpath = ""
        # Get directory #
        print("Looking for directory")
        if enviroment_localpath != "Optional":
            if enviroment_localpath[-1] == '/':
                local_envpath = enviroment_localpath
            else:
                local_envpath = enviroment_localpath + "/"
        else:
            local_envpath = Settings.Base_path + \
                "virtualenv_" + Settings.Enviroment_name + "/"

        isDirectory = os.path.isdir(local_envpath)
        if isDirectory is False:
            return "This is not a correct directory"

        indexes = GF.Find(local_envpath, "/")
        max_count = len(indexes) - 1
        env_name = local_envpath[indexes[max_count - 1] + 1:indexes[max_count]]

        # Collect all data needed in dir #
        print("Collecting data")
        requirements_file = open(local_envpath + "requirements.txt", "r")
        requirements_string = requirements_file.read()

        requirements_file = open(local_envpath + "docs/documentation.txt", "r")
        requirements_string = requirements_file.read()

        # main_py_file = open(local_envpath + "main.py", "r")
        # main_py_file_data = main_py_file.read()

        model_file = open(local_envpath + "model/trained_model.pkl", "rb")
        model_file_data = model_file.read()

        validation_data_file = open(local_envpath + "data/data.gzip", "rb")
        validation_data_file_data = validation_data_file.read()

        # validation_data_control_file = open(
        #     local_envpath + "data/data_control.gzip", "rb")
        # validation_data_control_file_data = validation_data_control_file.read()

        main_py_file = open(local_envpath + "main.py", "r")
        main_py_file_data = main_py_file.read()

        function_py_file = open(local_envpath + "ms/functions.py", "r")
        function_py_file_data = function_py_file.read()

        init_py_file = open(local_envpath + "ms/__init__.py", "r")
        init_py_file_data = init_py_file.read()

        train_py_file = open(local_envpath + "ms/train_model.py", "r")
        train_py_file = train_py_file.read()

        # Generate date version
        print("Generating version data")
        today = date.today()
        version = today.strftime("%d%m%Y")

        # Check if app with version already exists, if it does, append number
        versionInUse = True
        additional = 1
        while versionInUse:
            try:
                git_repo.get_contents(
                    env_name + "/" + version + "/version_info.json")
                if additional == 1:
                    version = version + "-" + str(additional)
                else:
                    charloc = [i for i, ltr in enumerate(
                        version) if ltr == '-']
                    version = version[0: charloc[0] + 1]
                    version = version + str(additional)
                additional += 1
            except Exception as e:
                print(e)
                versionInUse = False
                pass
                break

        version_data = {
            "Upload_date": today.strftime("%d/%m/%Y"),
            "Model_name": env_name,
            "Package_version": Settings.Package_version,
            "Requirements": requirements_string,
            "uploaded_by": git_user_data[0].email
        }

        # Upload to Git #
        print("Uploading to Git")
        gitFilePath = env_name + "/" + version + "/"
        commitMessage = env_name + " - " + version + " published"

        # Create requirements file
        appFilePath = gitFilePath + "_requirements.txt"
        git_repo.create_file(appFilePath, commitMessage,
                             requirements_string, branch=self._branch_name)
        print("Requirements... done!")

        # Create main.py file
        appFilePath = gitFilePath + "main.py"
        git_repo.create_file(appFilePath, commitMessage,
                             main_py_file_data, branch=self._branch_name)
        print("Main code... done!")

        # Create python custom code file
        appFilePath = gitFilePath + "functions.py"
        git_repo.create_file(appFilePath, commitMessage,
                             function_py_file_data, branch=self._branch_name)
        print("Custom code... done!")

        # Create python custom code file
        appFilePath = gitFilePath + "__init__.py"
        git_repo.create_file(appFilePath, commitMessage,
                             init_py_file_data, branch=self._branch_name)
        print("Custom code... done!")

        # Create Validation data file
        appFilePath = gitFilePath + "validation_data.gzip"
        git_repo.create_file(appFilePath, commitMessage,
                             validation_data_file_data, branch=self._branch_name)
        print("Validation data... done!")

        # # Create validation control data file
        # appFilePath = gitFilePath + "validation_control_data.gzip"
        # git_repo.create_file(appFilePath, commitMessage,
        #                      validation_data_control_file_data, branch=self._branch_name)
        # print("Validation control data... done!")

        # Create model data file
        appFilePath = gitFilePath + "model.pkl"
        git_repo.create_file(appFilePath, commitMessage,
                             model_file_data, branch=self._branch_name)
        print("Model data... done!")

        # Create version data file
        version_info_json = json.dumps(version_data)
        appFilePath = gitFilePath + "version_info.json"
        git_repo.create_file(appFilePath, commitMessage,
                             version_info_json, branch=self._branch_name)
        print("Version data... done!")
        return "Saved model data under: " + self._repo_name + "/" + env_name + "/" + version

    def Download_enviroment(self, localpath="", generate_venv=True):
        git = Github(Settings.Gitaccesstoken)
        git_repo = ""
        try:
            git_repo = git.get_repo(self._repo_name)
        except Exception as e:
            print(e)
            print("Not able to get given repo: " + self._repo_name)
            return

        local_envpath = GF.Path_is_dir(localpath)

        # Get Files from repo
        print("Downloading files from remote")

        # Download requirements
        requirements = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/_requirements.txt")
        print("Requirements... Done!")

        # Download model
        model_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/model.pkl")
        print("Model... Done!")

        # Download validation data
        validation_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/validation_data.gzip")
        print("Validation data... Done!")

        # # Download validation control data
        # validation_control_data = git_repo.get_contents(
        #     self._model_name + '/' + self._model_version + "/validation_control_data.gzip")
        # print("Validation control data... Done!")

        # Download main python code
        main_code_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/main.py")
        print("Main python code... Done!")

        # Download Function code for model
        function_code_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/function.py")
        print("Function python code... Done!")

        # Download init code for model
        init_code_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/__init__.py")
        print("init python code... Done!")

        # Download training code for model
        train_model_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/train_model.py")
        print("init python code... Done!")

        # Download version info
        version_info_data = git_repo.get_contents(
            self._model_name + '/' + self._model_version + "/version_info.json")
        print("Version info... Done!")

        # Generate folder structure #
        print("Generating folder structure with data points")
        folders = [{"path": local_envpath + self._model_name + "/" + self._model_version + "/ms/functions.py",
                    "content": function_code_data.decoded_content.decode("utf-8")},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/ms/__init__.py",
                    "content": init_code_data.decoded_content.decode("utf-8")},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/ms/train_model.py",
                    "content": train_model_data.decoded_content.decode("utf-8")},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/data/data.gzip",
                    "content": validation_data.decoded_content},
                   #    {"path": local_envpath + self._model_name + "/" + self._model_version + "/data/data_control.gzip",
                   #     "content": validation_control_data.decoded_content},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/model/trained_model.pkl",
                    "content": model_data.decoded_content},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/requirements.txt",
                    "content": requirements.decoded_content.decode("utf-8")},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/docs/documentation.txt",
                    "content": version_info_data.decoded_content.decode("utf-8")},
                   {"path": local_envpath + self._model_name + "/" + self._model_version + "/main.py",
                    "content": main_code_data.decoded_content.decode("utf-8")}
                   ]

        # Write files and directory's #
        for item in folders:
            os.makedirs(os.path.dirname(item["path"]), exist_ok=True)
            if isinstance(item["content"], string_types):
                with open(item["path"], "w") as f:
                    f.write(item["content"])
            elif isinstance(item["content"], (bytes)):
                try:
                    with open(item["path"], "wb") as fb:
                        fb.write(item["content"])
                except Exception as e:
                    print(e)
                    print("Failed to write data to: " + item["path"])
            else:
                return "Not able to write file: " + item["path"] + "at all."

        if generate_venv:
            print("Generating VENV Data")
            cmd = 'python -m venv ' + local_envpath + \
                self._model_name + "/" + self._model_version
            p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())
            return
        else:
            return "Finished downloading"

    def Get_file_content(self, filename):
        git = Github(Settings.Gitaccesstoken)
        git_repo = ""
        downloaded_files = []

        try:
            git_repo = git.get_repo(self._repo_name)
        except Exception as e:
            print(e)
            print("Not able to get given repo: " + self._repo_name)
            return

        # Checks if the instance is a string or an array
        if isinstance(filename, string_types):
            print("Single file download")
            downloaded_files.append(git_repo.get_contents(
                self._model_name + '/' + self._model_version + "/" + filename).decoded_content)
        elif isinstance(filename, list):
            print("Multiple files download")
            for item in filename:
                downloaded_files.append(git_repo.get_contents(
                    self._model_name + '/' + self._model_version + "/" + item).decoded_content)

        return downloaded_files
