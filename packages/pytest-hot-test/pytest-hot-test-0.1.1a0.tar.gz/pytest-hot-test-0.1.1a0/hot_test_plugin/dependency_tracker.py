import re
import os
from typing import List, Tuple, Set, Any
import importlib
import inspect
from hot_test_plugin import settings
from hot_test_plugin import errors
from hot_test_plugin.message_handler import debug_statement


def _get_imports_from_file(path: str) -> List[str]:
    """Parses the lines of a file and filter lines that contain the substring 'import'

    This function also removes repeated whitespaces, to make it post-processing easier.
    """
    with open(path, "r") as fp:
        source_code = fp.readlines()
    import_statements = [
        re.sub(r"\s+", " ", line) for line in source_code if "import" in line
    ]
    return import_statements


def _find_dependencies_to_track(import_statements: List[str]):
    """Transforms the import lines above into a list of potential dependencies to track.
    These dependencies are modules or packages

    For instance, given this input:

        import inspect
        import mod1
        from package2 import mod4

    We'd get back a list:

        - inspect
        - mod1
        - package2

    """
    dependencies_to_track = []
    for import_ in import_statements:
        imported_module_or_package = import_.split(" ")[1]
        dependencies_to_track.append(imported_module_or_package)
    return dependencies_to_track


def _find_artifacts_in_project(
    root: str, dependencies_to_track: List[str]
) -> Tuple[List[str], List[str], List[str]]:
    """Finds in which files the modules or packages can be found in the project."""
    modules = []
    packages = []
    files = []
    list_files = list(os.walk(root))
    for dep in dependencies_to_track:
        module_dep = dep + ".py"
        for root_, dirs, files_ in list_files:
            package_name = re.sub(f"{root}/", "", root_).replace("/", ".", -1)
            if "__pycache__" in package_name:
                continue

            debug_statement("Package_name ", package_name, "--- dep ", dep)
            if package_name == dep:
                packages.append(dep)
                files.append(os.path.join(root, package_name))

            if module_dep in files_:
                modules.append(module_dep)
                files.append(os.path.join(root, module_dep))

            if "." in dep:
                top_level_module = dep.split(".")[-1]
                merged = f"{package_name}.{top_level_module}"
                debug_statement("Merged ", merged, "--- dep", dep)
                if merged == dep:
                    debug_statement("---> Found top level module!!")
                    debug_statement("Root ", root, "Files ", files_)
                    modules.append(merged)
                    files.append(os.path.join(root, dep))
    return files, packages, modules


def _absolute_path_to_root_relative_path(path: str) -> str:
    """Trims an absolute path to a relative path relative to the working directory.

    Example:
        path /Users/dev/pytest-hot-test/src/common/utils.py
        wd  /Users/dev/pytest-hot-test/
        Split  ['', 'src/common/utils.py']
        New files {'src/common/utils.py'}

    """
    wd = os.getcwd() + "/"
    split = path.split(wd)
    if len(split) > 1:
        return split[1]
    raise errors.SourcePathNotSet(f"""
    The path '{path}' is not a valid source file. 
    
    Make sure to set the environment variable like below:

    export PYTEST_HOT_TEST_SOURCE_ROOT=project_folder

    Where 'project_folder' represents the path to your source files,
    for instance 'src', or '{wd}'

    """
    )


def _import_modules_from_files(root, files) -> List[Any]:
    """Import a list of files as modules, starting from the root of the project."""
    imported_modules = []
    import sys
    for file in files:
        importable = (
            file.replace(f"{root}/", "", -1).replace(".py", "").replace("/", ".", -1)
        )
        sys.stdout.write(importable)
        sys.stdout.write("\n")
        imported_modules.append(importlib.import_module(importable))
    return imported_modules


def _find_referred_files(imported_modules) -> Set[str]:
    """Inspect a module and retrieves the source code where the module member is originally defined.

    Returns a set of filepaths with all used files.
    """
    refererred_files = []
    for imported in imported_modules:
        member_keys = dir(imported)
        for key in member_keys:
            member = getattr(imported, key)
            try:
                used_file = inspect.getfile(member)
                if settings.SOURCE_CODE_ROOT in used_file:
                    refererred_files.append(used_file)
            except TypeError:
                pass
    return set(refererred_files)


def find_dependencies(collection_path, str_path, config):
    debug_statement("Collecting path ", str_path)

    try:
        os.listdir(settings.SOURCE_CODE_ROOT)
    except FileNotFoundError:
        raise errors.InvalidSourcePath(f"""
        The path '{settings.SOURCE_CODE_ROOT}' could not be found or is not a directory.

        Make sure to set the environment variable like below:

        export PYTEST_HOT_TEST_SOURCE_ROOT=project_folder

        Where 'project_folder' represents the path to your source files,
        for instance 'src'.
        """)

    import_statements = _get_imports_from_file(str_path)
    debug_statement("Import statements ", import_statements)
    dependencies_to_track = _find_dependencies_to_track(import_statements)

    debug_statement("Dependencies", dependencies_to_track)
    files, packages, modules = _find_artifacts_in_project(
        settings.SOURCE_CODE_ROOT, dependencies_to_track
    )

    debug_statement("Packages ", packages)
    debug_statement("Modules ", modules)
    relevant_files = set(files)
    debug_statement("Relevant files", relevant_files)

    imported_modules = _import_modules_from_files(
        settings.SOURCE_CODE_ROOT, relevant_files
    )
    referred_files = _find_referred_files(imported_modules)
    debug_statement("Referred files ", referred_files)

    referred_files = set(
        [_absolute_path_to_root_relative_path(f) for f in referred_files]
    )

    new_files = referred_files - relevant_files
    relevant_files = relevant_files.union(new_files)
    debug_statement("New files", new_files)
    i = 0
    while len(new_files) > 0 and i < settings.MAX_ITER_SAFETY:
        imported_modules = _import_modules_from_files(
            settings.SOURCE_CODE_ROOT, new_files
        )
        referred_files = _find_referred_files(imported_modules)
        referred_files = set(
            [_absolute_path_to_root_relative_path(f) for f in referred_files]
        )
        new_files = referred_files - relevant_files
        relevant_files = relevant_files.union(new_files)
        i += 1

    if i == settings.MAX_ITER_SAFETY:
        raise ValueError("Infinite loop circuit breaker")

    debug_statement("Relevant files", relevant_files)
    return set([f for f in relevant_files if os.path.isfile(f) and f.endswith(".py")])
