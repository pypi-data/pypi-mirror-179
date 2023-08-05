import psutil
import socket

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer
from textual.binding import Binding


class TableApp(App):
    TITLE = "Listening Ports"
    BINDINGS = [
        Binding("ctrl+c,ctrl+q", "app.quit", "Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_column('PID', width=5)
        table.add_column('exe', width=80)
        table.add_column('name', width=30)
        table.add_column('ip', width=15)
        table.add_column('port', width=5)
        for c in tcp_ports():
            (ip, port) = c.laddr
            p = psutil.Process(c.pid)
            table.add_row(str(p.pid), p.exe(), p.name(), ip, str(port))


def tcp_ports():
    connections = psutil.net_connections('inet')
    tcp_connections = []
    for c in connections:
        (ip, port) = c.laddr
        if ip == '0.0.0.0' or ip == '::':
            if c.type == socket.SOCK_STREAM and c.status == psutil.CONN_LISTEN:
                tcp_connections.append(c)
    return tcp_connections
