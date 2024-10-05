# Bazel docker (thus bazocker) usage example

Install `bazelisk` for your target OS, then run

## For basic python docker image

```sh {"id":"01J9FCFFGRCZWPVQ10QK86WCPA"}
bazel run //samples/python
```

## For generic ubuntu image

```sh {"id":"01J9FCFFGRCZWPVQ10QP05JGZX"}
bazel run //samples/ubuntu
```