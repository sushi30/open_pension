import os

for key in ("SCHEMAS_FILE", "OUT_DIRECTORY", "ENV"):
    if key not in os.environ.keys():
        raise EnvironmentError("Need to specify: " + key)
