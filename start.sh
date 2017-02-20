#!/bin/bash
sudo systemctl start bluetooth
sudo startbt.sh
sleep 5
sudo python drive.py


