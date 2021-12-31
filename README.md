<div align="center">

<img width="400" height="400" src="/media/iBackup-Pythonista-demo.gif">

# iBackup-Pythonista.py

### **Create Backups of Python Scripts in Pythonista iOS App**
> Python script for backing up Pythonista scripts on iOS. Simple backups of Pythonista folders allowing easy transfer to other devices.

![GitHub last commit](https://img.shields.io/github/last-commit/ConnerWill/iBackup-Pythonista)
![GitHub issues](https://img.shields.io/github/issues-raw/ConnerWill/iBackup-Pythonista)
![GitHub repo size](https://img.shields.io/github/repo-size/ConnerWill/iBackup-Pythonista)
[![GitLab](https://img.shields.io/static/v1?label=gitlab&logo=gitlab&color=E24329&message=mirrored)](https://gitlab.com/ConnerWill/iBackup-Pythonista)
![GitHub](https://img.shields.io/github/license/ConnerWill/iBackup-Pythonista)
![GitHub Repo stars](https://img.shields.io/github/stars/ConnerWill/iBackup-Pythonista?style=social)

---
</div>


# Features
[✔] Easily create backups of all Pythonista scripts compressed to a zip archive.

[✔] Simple configuration of backups using a configuration file.

[✔] Share backup to prefered location.

[✔] Exclude/include files and folders from being backed up.

[___] Autonomous transfer of backups.

---

# Table of Contents

<details>
  <summary>Click to expand!</summary>

  * [iBackup-Pythonista.py](#ibackup-pythonistapy)
* [Features](#features)
* [Table of Contents](#table-of-contents)
* [How To Use](#how-to-use)
   * [Installation](#installation)
   * [Configuration](#configuration)
      * [Configuration Variables](#configuration-variables)
      * [Configuration File](#configuration-file)
* [Other](#other)

</details>

# How To Use

## Installation

1. Download or clone **[iBackup-Pythonista](https://github.com/ConnerWill/iBackup-Pythonista)**
2. Edit the configuration file **[iBackup-Pythonista.cfg](https://github.com/ConnerWill/iBackup-Pythonista/iBackup-Pythonista.cfg)** to your preference
3. Run **[iBackup-Pythonista.py](https://github.com/ConnerWill/iBackup-Pythonista/iBackup-Pythonista.py)** to start the backup

*An even easier method of installing this script is to install [StaSH](https://github.com/ywangd/stash). Then, git clone this repository*

```Shell
git clone https://github.com/ConnerWill/iBackup-Pythonista.git
```
## Configuration
### Configuration Variables

**BackupDir**
: Root folder from where to start the backup. All subfolders will be backed up ***[string]***

**ExcludeList**
: List of folders to not backup ***[string]***
*(eg. Backups, tmp)*

**ArchiveDir**
: Location to save the backup ***[string]***

**ArchiveName**
: Name of the backup ***[string]***

**OpenInQuickLook**
: After backup has finished, open *'quicklook'* ***[bool]***

### Configuration File

<details>
  <summary>Click to expand configuration file contents</summary>

```INI
# Folder to backup
[BackupFrom]
BackupDir = ~/

# List of folders to exclude from backup
[Exclude]
ExcludeList = local-packages, Backups, tmp, Documents/tmp, Documents/tmp, Documents/Backups, .Trash, Documents/.Trash

# Location and name of the backup archive.
# Folder will be created if it doesn't exist and 
# is automatically excluded from the backup.
# The current date will be prepended to 'ArchiveName'.
[BackupTo]
ArchiveDir = Backups
ArchiveName = iBackup-Pythonista.zip

# Open QuickLook when backup is complete. (Leave as True for now, planning on adding automatic transfers/sharing) 
[Sharing]
OpenInQuickLook = True

# Output colors (R, G, B)
[Colors]
ErrorColor = 1.0, 0.0, 0.0
StartColor = 0.0, 1.0, 1.0
SuccessColor = 0.0, 1.0, 0.0
InfoColor = 0.0, 0.0, 1.0
ProgressColor = 0.7, 0.7, 0.0

# Output font
[Fonts]
TextFont = Anonymous Pro
```

</details>


---

# Other

[iBackup-Pythonista](https://github.com/ConnerWill/iBackup-Pythonista)  was writted for the iOS app, *Pythonista*.

Install [Pythonista](https://omz-software.com/pythonista) from the [iOS app store](https://apps.apple.com/us/app/pythonista-3/id1085978097).


** This script is still a work in progress. Use this script at your own risk! **

* *Tested on iPhone 7/8 *

* *iOS 15.0.1*

* *Pythonista Version 3.3 *


---


