from collections import OrderedDict


class Remote:

    def __init__(self, name, url, verify_ssl=True, disabled=False):
        self._name = name  # Read only, is the key
        self.url = url
        self.verify_ssl = verify_ssl
        self.disabled = disabled

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        if other is None:
            return False
        return self.name == other.name and \
               self.url == other.url and \
               self.verify_ssl == other.verify_ssl and \
               self.disabled == other.disabled

    def __str__(self):
        return "{}: {} [Verify SSL: {}, Enabled: {}]".format(self.name, self.url, self.verify_ssl,
                                                             not self.disabled)

    def __repr__(self):
        return str(self)


class _RecipeUploadData:
    def __init__(self, prefs):
        self.upload = True
        self.force = None
        self.dirty = None
        self.files = None
        self.packages = [_PackageUploadData(pref) for pref in prefs]

    def serialize(self):
        return {
            "dirty": self.dirty,
            "upload": self.upload,
            "force": self.force,
            "files": self.files,
            "packages": [r.serialize() for r in self.packages]
        }


class _PackageUploadData:
    def __init__(self, pref):
        self.pref = pref
        self.upload = True
        self.files = None
        self.force = None

    def serialize(self):
        return {
            "pref": repr(self.pref),
            "upload": self.upload,
            "force": self.force,
            "files": self.files
        }


class SelectBundle:
    def __init__(self):
        self.recipes = OrderedDict()

    def add_ref(self, ref):
        self.recipes.setdefault(ref, [])

    def refs(self):
        return self.recipes.keys()

    def prefs(self):
        prefs = []
        for v in self.recipes.values():
            prefs.extend(v)
        return prefs

    def add_prefs(self, prefs):
        for pref in prefs:
            self.recipes.setdefault(pref.ref, []).append(pref)


class UploadBundle:
    def __init__(self, select_bundle):
        self.recipes = OrderedDict()
        # We reverse the bundle so older revisions are uploaded first
        for ref, prefs in reversed(select_bundle.recipes.items()):
            self.recipes[ref] = _RecipeUploadData(reversed(prefs))

    def serialize(self):
        return {r.repr_notime(): v.serialize() for r, v in self.recipes.items()}

    @property
    def any_upload(self):
        for r in self.recipes.values():
            if r.upload:
                return True
            for p in r.packages:
                if p.upload:
                    return True
        return False
