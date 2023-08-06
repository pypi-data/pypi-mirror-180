#!/usr/bin/python3
#
# Download the (tiny) translation models from the 'translatelocally'
# project into 'data/' and write our kotki 'registry.json'
#
import shutil
import json
import tempfile
import tarfile
import io
import os

import requests

_log = lambda k: print(f"[*] {k}")
dest_dir = os.path.join(os.getcwd(), "data")
if os.path.exists(dest_dir):
    _log(f"please remove '{dest_dir}' first (destination directory)")
    exit(1)

registry = {}

url = "https://translatelocally.com/models.json"
_log(url)
r = requests.get(url)
blob = r.json()

with tempfile.TemporaryDirectory() as tmp_dir:
    _log(tmp_dir)

    for item in blob.get('models', []):
        model_name = item.get('modelName', '')
        if 'tiny' not in model_name.lower():
            _log(f"skipping {model_name}")
            continue

        from_lang, to_lang = item['code'].split('-')[:2]
        code = from_lang + to_lang
        obj = {}

        _url = item['url']
        _log(_url)
        with requests.get(_url, stream=True) as r:
            r.raise_for_status()
            _log("tar open")
            with tarfile.open(fileobj=io.BytesIO(r.content), mode="r:gz") as tar:
                for member in tar.getmembers():
                    _name = os.path.basename(member.name)
                    path = None
                    t = None

                    for req in ["model.", "vocab.", "lex."]:
                        _key = req.replace(".", "")
                        if req in _name:
                            _name = _name.replace(req, f"{req}{code}.")
                            obj[_key] = {
                                "name": _name,
                                "size": member.size,
                                "modelType": "prod",
                                "version": item['version'],
                                "API": item['API']
                            }
                            t = tar.extractfile(member)
                            path = os.path.join(tmp_dir, _name)
                            _log(f"write: {path}")

                    if path is not None and t is not None:
                        with open(path, "wb") as f:
                            f.write(t.read())
                        t.close()

        for req in ["model", "lex", "vocab"]:
            if req not in obj:
                print(f"skipping code {code} because {req} was not found")
                continue

        registry.setdefault(code, {})
        registry[code] = obj

    _log("writing registry.json")
    reg_path = os.path.join(tmp_dir, "registry.json")
    with open(reg_path, "wb") as f:
        f.write(json.dumps(registry, indent=4, sort_keys=True).encode())

    _log(f"{tmp_dir} -> {dest_dir}")
    shutil.move(tmp_dir, dest_dir)
