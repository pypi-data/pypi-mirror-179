import importlib
import os
from collections import defaultdict, namedtuple


Format = namedtuple(
    "Format",
    ["pkg", "pkg_postimport", "load", "load_args", "save", "save_args", "hint"],
)


def _yaml_postimport(imported_pkg):
    representer = importlib.import_module("yaml.representer")
    imported_pkg.add_representer(defaultdict, representer.Representer.represent_dict)


class Encoder:
    ANOMALO_VERSION_ID_KEY = "AnomaloVersionID"
    ANOMALO_VERSION_ID = 1
    ENCODERS = {
        "yml": "yaml",
        "yaml": Format(
            pkg="yaml",
            pkg_postimport=_yaml_postimport,
            load="safe_load",
            load_args=None,
            save="dump",
            save_args=None,
            hint='Install anomalo with "pip install anomalo[yaml]"',
        ),
        "json": Format(
            pkg="json",
            pkg_postimport=None,
            load="load",
            load_args=None,
            save="dump",
            save_args={"indent": 4, "sort_keys": True},
            hint=None,
        ),
    }

    def __init__(self, filename):
        self.filename = filename
        self.file_ext = os.path.splitext(filename)[1][1:]
        if self.file_ext not in self.ENCODERS:
            raise Exception(
                f"Unsupported file type extension {self.file_ext}. "
                f"Supported extensions are: {', '.join(sorted(self.ENCODERS.keys()))}"
            )
        self.file_encoder = self.ENCODERS[self.file_ext]
        if isinstance(self.file_encoder, str):
            self.file_encoder = self.ENCODERS[self.file_encoder]
        try:
            self.pkg = importlib.import_module(self.file_encoder.pkg)
            if self.file_encoder.pkg_postimport:
                self.file_encoder.pkg_postimport(self.pkg)
        except ModuleNotFoundError as e:
            msg = (
                f'Package "{self.file_encoder.pkg}" for {self.file_ext} '
                "file type support was not found"
            )
            if self.file_encoder.hint:
                msg += os.linesep + f"Hint: {self.file_encoder.hint}"
            raise Exception(msg) from e

    def _wrap_obj(self, obj, component):
        return {self.ANOMALO_VERSION_ID_KEY: self.ANOMALO_VERSION_ID, component: obj}

    def _unwrap_obj(self, obj, component):
        if obj.get(self.ANOMALO_VERSION_ID_KEY) != self.ANOMALO_VERSION_ID:
            return {}
        return obj.get(component) or {}

    def load(self, component, *args, **kwargs):
        return self._unwrap_obj(
            getattr(self.pkg, self.file_encoder.load)(
                *args, **(kwargs | (self.file_encoder.load_args or {}))
            ),
            component,
        )

    def save(self, obj, component, *args, **kwargs):
        return getattr(self.pkg, self.file_encoder.save)(
            self._wrap_obj(obj, component),
            *args,
            **(kwargs | (self.file_encoder.save_args or {})),
        )
