FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Final Stage
FROM python:3.11-slim AS runtime
WORKDIR /app
RUN adduser --no-create-home appuser
COPY --from=builder /install/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# Copy binaries
COPY --from=builder /install/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=builder /app/app.py .
USER appuser
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]