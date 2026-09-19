from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
STATIC_DIR = PROJECT_DIR / "static_portal"


class PortalHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def log_message(self, format, *args):
        print(f"[portal] {format % args}")


def run_server(port: int = 8000):
    server = ThreadingHTTPServer(("0.0.0.0", port), PortalHandler)
    print(f"Portal is running on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
