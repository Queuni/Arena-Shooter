# main


# Improve the startup time by lazy-loading the heavy modules

# Support loading config from multiple files with later overriding earlier

# Fix the test that was flaky due to reliance on system time

# Remove obsolete workaround now that the upstream bug is fixed

# Add a small delay between retries to avoid thundering herd

# Handle the duplicate key case by merging the values instead of failing

# Fix race condition in the cache that could return stale data under load

# Bump the tool version and update the pre-commit hook config

# Support optional config file path via env var for easier deployment

# Correct typo in the error message shown when validation fails

# Fix incorrect type hint that was causing mypy to fail in CI

# Remove deprecated CLI flag and update docs to use the new option
