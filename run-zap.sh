docker pull ghcr.io/zaproxy/zaproxy:stable
docker pull zaproxy/zap-stable

$(ip -f inet -o addr show docker0 | awk '{print $4}' | cut -d '/' -f 1)
docker run -t zaproxy/zap-weekly zap-baseline.py -t http://$(ip -f inet -o addr show docker0 | awk '{print $4}' | cut -d '/' -f 1):10080