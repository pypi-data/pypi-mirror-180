# godot-build

Build tool for Godot projects, this makes it easy to do CI/CD.

Features:
* Export projects: release, debug, pack
* Use global templates and system installed godot
* Use local templates and game engine
* Download the required version of templates and game engine
* Auto patch `export_presets.cfg` to use required templates
* Run tests (GUT support)

Return code is 0 if build/test normally. Else return code is 1.

**Warning**: support for operating systems other than Linux is not guaranteed and has not been tested!

## Install

Required python: >= 3.6

```sh
pip install godot-build
# or
yay -S godot-build
```

Or download source code and run `python godot-build/gdbuild.py`.

## Use

```sh
gdbuild -p $PATH_TO_PROJECT -i
# after edit gdbuild.json
gdbuild -p $PATH_TO_PROJECT --test all
gdbuild -p $PATH_TO_PROJECT -o $PATH_TO_BIN_OUTPUT --preset HTML5
```

More help:
```sh
[user@pc gdbuild]$ gdbuild --help
usage: gdbuild --preset HTML5

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to godot project directory
  -o OUTPUT, --output OUTPUT
                        path to output directory
  --preset PRESET       name of preset
  --pack PACK           export pack (*.pck or *.zip)
  --debug DEBUG         export debug build
  --test {internal,all,command}
                        run test
  -i, --init            initialize gdbuild project
  -d, --download        download engine and templates
  ```

  ### Config

  `gdbuild -p $PATH_TO_PROJECT -i` or `gdbuild -p $PATH_TO_PROJECT --init` will create file `gdbuild.json` in given path.

  Options:
  * `engine_url`: url for download engine (zip file)
  * `templates_url`: url for download templatez (tpz or zip file)
  * `sha512`: hashes for validate downloaded archives (by file name)
  * `templates`: contains template files by preset name (will use in patch `export_presets.cfg`)
  * `custom`: toggle use global (false) or local (true) templates and engine
  * `global`: global paths to templates and game engine bin
  * `version`: require version of templates and game engine
  * `test_cmd`: command for run tests (default setup for GUT)
  * `timeout`: limit for run build or test in seconds
  * `fail_regex`: regex for parse failed tests (return code is also will check)
  * `cache_dir`: path to dir for templates and engines cache store
  * `engine_file`: name of local (cached) game engine file

  Details:
  * `engine_url`, `templates_url`, `global.templates`, `engine_file` require contains `{version}` part
  * templates archive is zip archive (*.tpz or *.zip), require contains `templates` dir
  * game engine archive is zip archive, contains bin file (not in subdirs)
  * `test_cmd` require `{godot}` and `{path}` parts
  * check `version`: global may differ from local (example: `3.5` is local and `3.5.stable` is global, see `global.templates` path)
  * check [repository](https://downloads.tuxfamily.org/godotengine) for more details (version names and sha512 hashes)
  
## License

GNU GPL v3
