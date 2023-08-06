## Page Object Elements

[pypy.org](https://pypi.org/project/page-object-elements/)

If you want to customize behaviour of **poe** loger's behaviour put `poe.ini` in the root of your project. If you
provide empty `logs_absolute_path`the Error will be thrown. Default **LOGS** location is working directory.

```ini
[LOGGER]
level = DEBUG
log_name = log
stdout = True
logs_absolute_path = C:\Users\<username>\workspace\<project>
```