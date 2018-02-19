#!/bin/sh

CMD=${1:-restart}

sudo systemctl $CMD toddkaye
sudo systemctl $CMD nginx
