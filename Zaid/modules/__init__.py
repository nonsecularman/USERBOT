import os

ALL_MODULES = []

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and not file.startswith("_"):
        ALL_MODULES.append(file[:-3])

__all__ = ALL_MODULES + ["ALL_MODULES"]
