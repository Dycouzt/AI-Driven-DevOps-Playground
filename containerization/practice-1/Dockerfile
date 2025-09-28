# ---- Builder Stage ----
FROM python:3.10-slim AS builder

# Set working directory to root of context
WORKDIR /app

# Install dependencies first (if you have a requirements.txt)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt, skipping"

# Copy app.py
COPY app.py .

# ---- Final Stage ----
FROM python:3.10-slim AS runtime 
# Same to use AS runtime than without it. name is only useful when referencing it in a --from=builder
WORKDIR /app

# Create a non-root user
RUN useradd --create-home appuser
USER appuser

# Copy dependencies from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
# Copy application code
COPY --from=builder /app/app.py .

EXPOSE 8080
CMD ["python", "app.py"]
