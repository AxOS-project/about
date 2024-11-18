# About AxOS 

Simple GTK app that shows basic information about AxOS.

## Build

```bash
meson build --prefix=/usr
ninja -C build
```

## Install
(after the build step)
```bash
sudo ninja -C build install
```

![screenshot](/screenshot/about.png)

