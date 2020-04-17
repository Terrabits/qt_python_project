# Qt for Python Project Template

This is a model-view-controller (MVC) project template built around Qt for Python.

The goal is to create a design pattern which leverages the usability of Qt Creator while spending as little time as possible with Qt itself.

## Requirements

This project should theoretically work with a broad range of environments.

- Python 3
- packages listed in `requirements.txt`

## Recommended

This project was developed and tested with the following, more specific versions:

- Python 3.8.1
- packages listed in `requirements.txt.lock`

## Qt Creator Integration

`MainWindow` can be opened in Qt Creator and edited via the included `qtcreator.pro` project file.

More information on Qt Creator can be found here:

[Getting Started | Qt Creator Manual](https://doc.qt.io/qtcreator/creator-getting-started.html)

To apply any changes, re-run `scripts/update-ui`. The updated `src/widgets/ui_mainwindow.py` file should be committed along with the updated `qtcreator/mainwindow.ui` file.

### StyleSheet

The Qt StyleSheet located at `src/widgets/stylesheet.css` gets loaded into MainWindow at runtime.

The practical effect of this is that the current styles are not reflected in the project in Qt Creator. As a work-around, to see them in Qt Creator, copy-paste the contents of the file into the widget property directly.

## scripts

There are bash scripts located in the `scripts` dir. They should be simple enough that, even if you are in windows, you can use them as a guide to performing the task at hand.
