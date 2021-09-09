# Changelog


## 2021-07-20
- Support custom headers in the client for API key or auth tokens

## 2021-07-26
- Remove hardcoded credentials and move to env-based configuration

## 2021-08-04
- Clean up duplicate logic between the sync and async code paths

## 2021-08-04
- Simplify the config validation by using a declarative schema

## 2021-08-19
- Implement a small in-memory cache for the config to avoid re-reading

## 2021-09-03
- Implement request ID propagation for better tracing across services

## 2021-09-09
- Implement basic rate limiting to avoid overwhelming the downstream service
