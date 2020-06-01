# pythonfuzz_example

Pythonfuzz example with bazel build and pybind.

Built on https://github.com/av8ramit/pybind_example

To attempt at compiling with sanitizers:

```
bazel clean --expunge
LD_PRELOAD=/lib/clang/9/lib/linux/libclang_rt.asan-x86_64.so bazel build -s --copt=-fsanitize=address --linkopt=-fsanitize=address --copt=-lasan --linkopt=-lasan --copt=-lubsan --linkopt=-lubsan module:math_test
```

Command:

```
bazel build -s --copt=-fsanitize=address --linkopt=-fsanitize=address  module:math_test
```
Leads to
```
undefined symbol: __asan_option_detect_stack_use_after_return
```
