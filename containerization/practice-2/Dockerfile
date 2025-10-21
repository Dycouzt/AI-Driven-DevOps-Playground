FROM python:3.10-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || echo 'installing requirements.txt'
COPY app.py .

# Final Stage
FROM python:3.10-slim as runtime
WORKDIR /app
RUN adduser --no-create-home appuser
USER appuser
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app/app.py .
EXPOSE 8080
CMD ["python", "app.py"]
