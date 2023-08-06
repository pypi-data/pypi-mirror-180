## 1.3.2.1 (2022-12-07)

3rd-party stubtest: run on Python 3.10 (#9342)

## 1.3.2 (2022-07-31)

Clean up a few Python 2 remnants (#8452)

## 1.3.1 (2022-07-18)

croniter: make package, complete public API (#8316)

## 1.3.0 (2022-06-26)

[stubsabot] Bump croniter to 1.3.* (#8185)

## 1.0.11 (2022-06-26)

Check missing definitions for several packages (#8167)

Co-authored-by: hauntsaninja <>

## 1.0.10 (2022-04-27)

Drop Python 2 support from croniter (#7705)

## 1.0.9 (2022-04-16)

Use `TypeAlias` where possible for type aliases (#7630)

## 1.0.8 (2022-03-16)

Use PEP 604 syntax wherever possible (#7493)

## 1.0.7 (2022-01-10)

Always use `_typeshed.Self`, where applicable (#6880)

* Always use `_typeshed.Self`, where applicable

* Revert changes to `google-cloud-ndb` (ambiguous)

* Remove empty line added by script

* Revert changes to `stubs/python-dateutil/dateutil/relativedelta.pyi`

* Manually add a few more that the script missed

* Improve `filelock` annotation

Source code here: https://github.com/tox-dev/py-filelock/blob/79ec7b2826e33b982fe83b057f359448b9d966ba/src/filelock/_api.py#L207

* Improve `opentracing/scope` annotation

Source code here: https://github.com/opentracing/opentracing-python/blob/3e1d357a348269ef54d67f761302fab93dbfc0f7/opentracing/scope.py#L71

* Improve `redis/client` stub

Source code here: https://github.com/redis/redis-py/blob/15f315a496c3267c8cbcc6d6d9c6005ea4d4a4d5/redis/client.py#L1217

* Improve `redis/lock` annotation

Source code here: https://github.com/redis/redis-py/blob/15f315a496c3267c8cbcc6d6d9c6005ea4d4a4d5/redis/lock.py#L155

* Improve `requests/models` annotation

Source code here: https://github.com/psf/requests/blob/d718e753834b84018014a23d663369ac27d1ab9c/requests/models.py#L653

## 1.0.6 (2022-01-08)

Use lowercase `type` everywhere (#6853)

## 1.0.4 (2021-12-28)

Use PEP 585 syntax wherever possible (#6717)

## 1.0.3 (2021-10-30)

croniter: Add missing arguments and functions, add types (#6215)

## 1.0.2 (2021-10-15)

Use lowercase tuple where possible (#6170)

## 1.0.1 (2021-10-12)

Add star to all non-0.1 versions (#6146)

