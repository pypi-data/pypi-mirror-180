# Middleware

[//]: # (::: medux.core.middleware)

You should add [TenantMiddleware][medux.common.middleware.TenantMiddleware] and [DeviceMiddleware][medux.core.middleware.DeviceMiddleware] to your Django settings.py's `MIDDLEWARE`:

```python
    MIDDLEWARE = [
        # ...
        "medux.core.middleware.DeviceMiddleware",
    ]
```

Then the current device (from where you access the application) will get added to the request automatically.
