bbibbi
======

It's a simple service locator that I made for use.


.. end-of-readme-intro

Installation
------------

::

    pip install bbibbi


Usage
--------
::

    from bbibbi import container, Symbol

    SERVICE_SYMBOL = Symbol("SomeService")

    class Service:
        def ten(self) -> int:
            return 10

    container.register(SERVICE_SYMBOL, Service())

    service: Service = container.get(SERVICE_SYMBOL)
    assert service.ten() == 10

