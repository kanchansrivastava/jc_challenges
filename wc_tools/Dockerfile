FROM python:3.11-slim

# Install basic CLI tools
RUN apt-get update && apt-get install -y \
    curl git vim nano less \
    && apt-get clean

# Set working directory
WORKDIR /workspace

# Install unix_wc.py as CLI tool when container builds
# This only works correctly if unix_wc.py is present after volume mounts
RUN mkdir -p /workspace/wc_tools
COPY wc_tools /workspace/wc_tools
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
ENV PYTHONPATH=/workspace/wc_tools

COPY wc_tools/unix_wc.py /usr/local/bin/unix_wc

RUN chmod +x /usr/local/bin/unix_wc

# When container starts, bash will be ready
CMD ["bash"]
