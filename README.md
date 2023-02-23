# sensorsrt
sensorsrt is a one file Python script to provide real-time sensors reading from commands `sensors` and `hddtemp`

#### Compile using `pyinstaller` or `auto-py-to-exe`
* Be sure to make your changes to the file `sensorsrt.py` first, as `hddtemp` monitoring may not work properly due to device path differences (HDD1 is `/dev/sda` and HDD2 is `/dev/sdb` but that's not always the case)
* Also after compiling be sure to move the compiled file to `/usr/bin` for easier access later (by just typing `sudo sensorsrt`) using `sudo mv -fv sensorsrt /usr/bin/sensorsrt`

## Command-line usage
```sh
sensorsrt <refresh rate in sec(s)>
```
* default value for `<refresh rate in sec(s)>` is **2** when not specified
