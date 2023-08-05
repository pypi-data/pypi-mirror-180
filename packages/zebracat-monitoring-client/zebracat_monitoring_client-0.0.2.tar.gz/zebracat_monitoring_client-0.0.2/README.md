# Monitoring Package

This is monitoring client package.
just use it for Zebracat monitoring server

```python
from zebracat_monitoring_client.client import ZebraClient
cli = ZebraClient(
        sensor_id="1",
        server_address="<address>:<port>",
        schema="http"
    )

handler = cli.get_handler()
handler.info("hi")
cli.send(value="100")
```