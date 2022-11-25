# Cannot be parametrized in Jenkins...
FROM ubuntu

# We don't know the uid of the user who will build, so make the /cache directories world writable
RUN export DEBIAN_FRONTEND=noninteractive && \
  mkdir -p /cache/hugo && chmod ugo+rwx /cache/hugo && \
  apt-get update && \
  apt-get install -qyy ca-certificates hugo zip && \
  rm -rf /var/lib/apt/lists/* && \
  apt-get clean
