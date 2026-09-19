FROM python:3.11-slim

WORKDIR /app

COPY portal_server.py ./
COPY static_portal ./static_portal

EXPOSE 8000

CMD ["python", "portal_server.py"]
