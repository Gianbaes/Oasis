
#!/usr/bin/env bash
set -Eeuo pipefail

export DISPLAY=:1
export XDG_RUNTIME_DIR="/tmp/runtime-$(id -u)"

mkdir -p "$XDG_RUNTIME_DIR"
chmod 700 "$XDG_RUNTIME_DIR"

echo "Checking GUI dependencies..."
for cmd in Xvfb x11vnc fluxbox websockify; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Missing dependency: $cmd"
        echo "Install it with: sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc"
        exit 1
    fi
done

echo "Cleaning up stale GUI processes..."
pkill -x x11vnc 2>/dev/null || true
pkill -x Xvfb 2>/dev/null || true
pkill -x fluxbox 2>/dev/null || true
pkill -f 'websockify.*6080' 2>/dev/null || true
sleep 1

echo "Starting virtual display..."
Xvfb :1 -screen 0 1024x768x24 -ac &
XVFB_PID=$!

cleanup() {
    echo "Stopping GUI services..."
    kill "$WEBSOCKIFY_PID" "$VNC_PID" "$FLUXBOX_PID" "$XVFB_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

sleep 2
if ! kill -0 "$XVFB_PID" 2>/dev/null; then
    echo "Xvfb failed to start."
    exit 1
fi

echo "Starting window manager..."
fluxbox &
FLUXBOX_PID=$!

echo "Starting VNC server..."
x11vnc -display :1 -nopw -forever -shared -rfbport 5900 &
VNC_PID=$!

for i in {1..10}; do
    if (echo > /dev/tcp/127.0.0.1/5900) >/dev/null 2>&1; then
        break
    fi
    sleep 1
done

if ! (echo > /dev/tcp/127.0.0.1/5900) >/dev/null 2>&1; then
    echo "VNC did not start. Check x11vnc errors above."
    exit 1
fi

echo "Starting noVNC..."
websockify --web=/usr/share/novnc 6080 localhost:5900 &
WEBSOCKIFY_PID=$!

sleep 2
if ! kill -0 "$WEBSOCKIFY_PID" 2>/dev/null; then
    echo "noVNC failed to start."
    exit 1
fi

echo ""
echo "GUI is ready!"
echo "Open port 6080 in the Codespaces Ports tab."
echo "Keep this terminal running while using the GUI."

wait

