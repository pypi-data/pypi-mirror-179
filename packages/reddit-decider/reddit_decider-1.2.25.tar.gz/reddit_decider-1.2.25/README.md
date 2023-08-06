# rust_decider

Rust implementation of bucketing, targeting, overrides, and dynamic config logic.

# Usage

## class `Decider`

A class used to expose these APIs:

- `choose(feature_name: str, context: Mapping[str, JsonValue]) -> Decision`

example:

```python
from rust_decider import Decider
from rust_decider import DeciderException
from rust_decider import DeciderFeatureNotFoundException
from rust_decider import DeciderInitException

# initialize Decider instance
try:
    decider = Decider("../cfg.json")
except DeciderInitException as e:
    print(e)

# get a Decision for a feature via choose()
try:
    decision = decider.choose(feature_name="exp_1", context={"user_id": "3", "app_name": "ios"})
except DeciderException as e:
    print(e)

assert dict(decision) == {
    "variant": "variant_0",
    "feature_id": 3246,
    "feature_name": "exp_1",
    "feature_version": 2,
    "events": [
      "0::::3246::::exp_1::::2::::variant_0::::3::::user_id::::37173982::::2147483648::::test"
    ]
}

# `user_id` targeting not satisfied so "variant" is `None` in the returned Decision
try:
    decision = decider.choose(feature_name="exp_1", context={"user_id": "1"})
except DeciderException as e:
    print(e)

assert dict(decision) == {
  "variant": None,
  "feature_id": 3246,
  "feature_name": "exp_1",
  "feature_version": 2,
  "events": []
}

# handle "feature not found" exception
# (`DeciderFeatureNotFoundException` is a subclass of `DeciderException`)
try:
    decision = decider.choose(feature_name="not_here", context={"user_id": "1"})
except DeciderFeatureNotFoundException as e:
  print("handle feature not found exception:")
  print(e)
except DeciderException as e:
    print(e)
```

## python bindings used in `Decider` class

```python
import rust_decider

# Init decider
decider = rust_decider.init("darkmode overrides targeting holdout mutex_group fractional_availability value", "../cfg.json")

# Bucketing needs a context
ctx = rust_decider.make_ctx({"user_id": "7"})

# Get a decision
choice = decider.choose("exp_1", ctx)
assert choice.err() is None # check for errors
choice.decision() # get the variant

# Get a dynamic config value
dc = decider.get_map("dc_map", ctx) # fetch a map DC
assert dc.err() is None # check for errors
dc.val() # get the actual map itself
```

# Development

## Updating package with latest `src/lib.rs` changes

```sh
# In a virtualenv, python >= 3.7
$ cd decider-py
$ pip install -r requirements-dev.txt
$ maturin develop
```

## Running tests

```sh
$ pytest decider-py/test/
```

## Publishing

Package is automatically published on merge to master to https://pypi.org/project/reddit-decider/ via drone pipeline.

# Formatting / Linting

```sh
$ cargo fmt    --manifest-path decider-py/test/Cargo.toml
$ cargo clippy --manifest-path decider-py/test/Cargo.toml
```
