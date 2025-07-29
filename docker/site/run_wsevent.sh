#!/bin/bash
set -e

# Setup websocket config
echo 'module.exports = { 
    get_host: "0.0.0.0", 
    get_port: 15100, 
    post_host: "0.0.0.0", 
    post_port: 15101, 
    http_host: "0.0.0.0", 
    http_port: 15102, 
    long_poll_timeout: 29000, 
};' > websocket/config.js

# Install websocket dependencies if not already installed
cd websocket && npm install qu ws simplesets

# Run websocket server
exec node websocket/daemon.js 