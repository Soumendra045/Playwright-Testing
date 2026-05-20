FROM jenkins/jenkins:2.555.2-jdk21

USER root

# Install Python and utilities
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    ca-certificates \
    lsb-release \
    gnupg \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
    https://download.docker.com/linux/debian bookworm stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && apt-get install -y docker-ce-cli

# Copy requirements file
COPY requirements.txt /tmp/requirements.txt

# Install Python packages
RUN pip3 install -r /tmp/requirements.txt

# Install Playwright browsers
RUN playwright install --with-deps

USER jenkins

RUN jenkins-plugin-cli --plugins "blueocean docker-workflow json-path-api"