FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install only what you REALLY need
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    poppler-utils curl && \
    rm -rf /var/lib/apt/lists/*

# Install uv (cached layer)
RUN pip install uv

ENV PATH="/root/.local/bin:$PATH"
ENV UV_LINK_MODE=copy
ENV PYTHONPATH="/app:/app/multi_doc_chat"

# Copy only requirements first (cache optimization)
COPY requirements.txt .

RUN uv pip install --system -r requirements.txt

# Now copy rest of code
COPY . .

EXPOSE 8080

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080"]