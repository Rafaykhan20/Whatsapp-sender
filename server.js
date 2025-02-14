const { Client, LocalAuth } = require("whatsapp-web.js");
const express = require("express");
const app = express();

const client = new Client({
    authStrategy: new LocalAuth(),
});

client.on("qr", (qr) => {
    console.log("Scan this QR Code to log in:");
    console.log(qr);  // Display QR code in console
});

client.on("ready", () => {
    console.log("WhatsApp Web connected!");
});

client.initialize();

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
