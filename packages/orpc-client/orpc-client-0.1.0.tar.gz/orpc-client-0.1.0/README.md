# orpc-client

Open RPC client.

## Install

```
pip install orpc-client
```

## Server Install

```
pip install orpc
```

## Protocol

### oRPC request

- request_package = 4bytes-length-byteorder-big + msgstack.dumps(request_body)
- request_body = {"event": "xxx", "args": [], "kwargs": {}}

### oRPC response

- response_package = 4bytes-length-byteorder-big + msgstack.dumps(response_body)
- response_body = {"result": xx, "code": 0, "message": "xxx"}

## Releases

### v0.1.0

- First release.
