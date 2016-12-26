#move the file hackerspaceshop_ws2801 to /etc/init.d 
sudo mv init-xmas-lights /etc/init.d

# set executable bit
sudo chmod +x /etc/init.d/init-xmas-lights

# update init scripts (ignore warnings)
sudo update-rc.d init-xmas-lights defaults
