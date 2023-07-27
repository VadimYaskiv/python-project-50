### Hexlet tests and linter status:
[![Actions Status](https://github.com/VadimYaskiv/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/VadimYaskiv/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/bf71ead1321a0c6c9379/maintainability)](https://codeclimate.com/github/VadimYaskiv/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/bf71ead1321a0c6c9379/test_coverage)](https://codeclimate.com/github/VadimYaskiv/python-project-50/test_coverage)
[![linter-check](https://github.com/VadimYaskiv/python-project-50/actions/workflows/linter.yml/badge.svg)](https://github.com/VadimYaskiv/python-project-50/actions/workflows/linter.yml)

## File Difference Generator - Gendiff

### Descriptioin
This utility uses by command line. Compare two json files or yaml(yml) files, choose one of three format output type, get the difference between them.

### Install
```bash
$ git clone https://github.com/VadimYaskiv/python-project-50.git
$ cd python-project-50
$ make build 
$ make publish
$ make package-install
```

### Run
```bash
$ gendiff [-h] [-f {stylish, plain, json}] filepath1 filepath2
```

### asciinema. step 3. flat json files comparison
<a href="https://asciinema.org/a/b1EXOJLv7i7ZoBE4mMWZ29ivQ" target="_blank"><img src="https://asciinema.org/a/b1EXOJLv7i7ZoBE4mMWZ29ivQ.svg" /></a>

### asciinema. step 5. flat yaml files comparison
<a href="https://asciinema.org/a/FiaOKmKhzkbT7LUwd9mR1G1Pa" target="_blank"><img src="https://asciinema.org/a/FiaOKmKhzkbT7LUwd9mR1G1Pa.svg" /></a>

### asciinema. step 6. recursive file comparison and output of result
<a href="https://asciinema.org/a/4FyOgDgBXDM084L16SuSvWv0s" target="_blank"><img src="https://asciinema.org/a/4FyOgDgBXDM084L16SuSvWv0s.svg" /></a>

### asciinema. step 7. plain format output
<a href="https://asciinema.org/a/aPs39Q5BpRgqABD8S9oi6h4Ar" target="_blank"><img src="https://asciinema.org/a/aPs39Q5BpRgqABD8S9oi6h4Ar.svg" /></a>

### asciinema. step 8. json format output
<a href="https://asciinema.org/a/foS93idvsUWpDNWXkqPUOJouX" target="_blank"><img src="https://asciinema.org/a/foS93idvsUWpDNWXkqPUOJouX.svg" /></a>