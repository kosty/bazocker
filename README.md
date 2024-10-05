# Bazel docker (thus bazocker) usage example

Install `bazelisk` for your target OS, then run

## For basic python docker image
```sh
bazel run :python_tarball
```

## For generic ubuntu image

```sh
bazel run :ubuntu_tarball
```