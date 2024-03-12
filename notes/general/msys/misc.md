# Additional Setup

## CompileDB

**NOTE:** Only use if Bear or PlatformIO is not available

```sh
mkdir -p $HOME/PyEnv;cd $HOME/PyEnv
virtualenv compiledb --system-site-packages

source $HOME/PyEnv/compiledb/bin/activate
pip install compiledb
deactivate
```

```sh
source $HOME/PyEnv/compiledb/bin/activate
compiledb -n make
deactivate

bat compile_commands.json
```
