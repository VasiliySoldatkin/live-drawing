function startSocket() {
    var ws = new WebSocket("ws://localhost:8765/")
    ws.onopen = function (event) {
        ws.send(process.env.WEBSOCKET_HOST)
    }
}

startSocket();