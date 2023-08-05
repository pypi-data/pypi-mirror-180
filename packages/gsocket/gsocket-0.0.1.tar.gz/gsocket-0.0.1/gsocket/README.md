# gsocket

一个仅 Python 使用的基于 socket 协议的模块

- SocketServer：连接服务端
- SocketClient：连接客户端
- SocketReceiver：自定义 on_open 等

注意：

- SocketServer、SocketClient、SocketReceiver 自带 send、sendall、sendfile 方法
- 本模块未匹配 websocket 协议，所有通信基于 struct 防止粘包，所以不适用

# SocketServer

```
from gsocket import SocketServer

SocketServer().start_server()
```

# SocketClient

推荐使用 with 上下文，不然需要手动关闭

```
from gsocket import SocketClient

with SocketClient() as s:
    s.send(msg="你好")
```

# SocketReceiver

SocketServer、SocketClient 都具备此参数，可以自由定义其接收方法
下面以 SocketServer 示例

```
from typing import Generator
from gsocket import SocketServer, SocketReceiver


class MySocketReceiver(SocketReceiver):
    def on_open(self):
        pass

    def on_message(self, msg: bytes):
        pass

    def on_file(self, filename: str, file_iterator: Generator):
        pass

    def on_close(self):
        pass


SocketServer(receiver=MySocketReceiver).start_server()
```