import hashlib
import random
import importlib.resources as pkg_resources


class WordHasher:
    def __init__(self):
        # https://dev.to/bowmanjd/easily-load-non-python-data-files-from-a-python-package-2e8g
        self.nouns = pkg_resources.read_text(__package__, "nouns.txt").splitlines()
        self.adjectives = pkg_resources.read_text(
            __package__, "adjectives.txt"
        ).splitlines()
        self.verbs = pkg_resources.read_text(__package__, "verbs.txt").splitlines()

        self.samplers = {
            "v": lambda: self.verbs[random.randrange(len(self.verbs))],
            "a": lambda: self.adjectives[random.randrange(len(self.adjectives))],
            "n": lambda: self.nouns[random.randrange(len(self.nouns))],
            "N": lambda: str(random.randrange(1000)),
        }
        self.modes = set(list(self.samplers.keys()))

    def from_str(self, text):
        h = hashlib.sha1(text.encode("utf-8")).hexdigest()

        n = int(h[:20], 16) % len(self.nouns)
        noun = self.nouns[n]

        a = int(h[30], 16) % len(self.adjectives)
        adj = self.adjectives[a]

        v = int(h[20:30], 16) % len(self.verbs)
        verb = self.verbs[v]

        wh = f"{verb}-{adj}-{noun}"
        return wh

    def from_file(self, file):
        with open(file, "r") as f:
            text = f.read()
        return self.from_str(text)

    def sample(self, mode: str = "vanN") -> str:
        assert mode != ""
        assert all(m in self.modes for m in mode)
        parts = [self.samplers[m]() for m in mode]
        return "-".join(parts)

    def __repr__(self):
        r = f"{self.__class__.__name__}:\n"
        r += f"       nouns: {len(self.nouns)}\n"
        r += f"  adjectives: {len(self.adjectives)}\n"
        r += f"       verbs: {len(self.verbs)}\n"
        return r
