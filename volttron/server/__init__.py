from pathlib import Path


# python3.8 and above have this implementation.
try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

# Try to get the version from written metadata, but
# if failed then get it from the pyproject.toml file
try:
    __version__ = importlib_metadata.version("volttron-server")
except importlib_metadata.PackageNotFoundError:
    # We should be in a develop environment therefore
    # we can get the version from the toml pyproject.toml
    root = Path(__file__).parent.parent.parent
    tomle_file = root.joinpath("pyproject.toml")
    if not tomle_file.exists():
        raise ValueError(
            f"Couldn't find pyproject.toml file for finding version. ({str(tomle_file)})"
        )
    import toml

    pyproject = toml.load(tomle_file)

    __version__ = pyproject["tool"]["poetry"]["version"]
