const WebSocket = require('ws');
const fs = require('fs');

// Create a WebSocket server instance on port 8080
const wss = new WebSocket.Server({ port: 8080 });





wss.on("connection", ws => {
    ws.on("message", data => {
        fs.appendFile("./cords.txt", data + ",", (err) => {
            if (err) {
                console.error("Error writing to file:", err);
            } else {
                console.log("Saved:", data);
            }
        });
    });
});