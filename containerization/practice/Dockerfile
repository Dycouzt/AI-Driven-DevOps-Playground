# ---- Builder Stage ----
FROM python:3.10-slim as builder

WORKDIR .

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# ---- Final Stage ----
FROM python:3.10-slim

WORKDIR .

# Create a non-root user
RUN useradd --create-home appuser
USER appuser

# Copy dependencies from builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
# Copy application code
COPY app.py .

EXPOSE 8080
CMD [ "python", "./app.py" ]