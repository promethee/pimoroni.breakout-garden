#!/bin/sh
docker run -d --privileged --device /dev/i2c-1:/dev/i2c-1 --name $(basename "$PWD") $USER/$(basename "$PWD"):latest
