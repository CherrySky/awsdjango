def load_ipython_extension():
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.

    import os, sys
    sys.path.insert(0, 'C:\\Users\\Don\\Jupyter\\dondjango')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dondjango.settings")
    import django
    django.setup()


load_ipython_extension()