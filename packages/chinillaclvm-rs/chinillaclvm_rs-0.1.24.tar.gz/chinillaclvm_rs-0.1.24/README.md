The `chinillaclvm_rs` wheel has python bindings for the rust implementation of chinillaclvm.

Build
-----

Use `maturin` to build the python interface. First, install into current virtualenv with

```
$ pip install maturin
```

While in the `wheel` directory, build `chinillaclvm_rs` into the current virtualenv with

```
$ maturin develop --release
```

On UNIX-based platforms, you may get a speed boost on `sha256` operations by building
with OpenSSL.

```
$ maturin develop --release --features=openssl
```


To build the wheel, do

```
$ maturin build --release
````

or

```
$ maturin build --release --features=openssl
```
