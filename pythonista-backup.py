'''
# ======================================================
# 	TITLE:
#		pythonista-backup.py
#
#	DESCRIPTION:
#		Python script for backing up Pythonista scripts on iOS.
#		Simple backups of Pythonista folders allowing transfers to other devices.
#
# 	AUTHOR:
#   		ConnerWill
# ======================================================
 __________________________________________
/                                          \
|         pythonista-backup.py             |
|                                          |
| Easily backup Pythonista scripts on iOS. |
|                                          |
\_______________________________________ '\
                                    ()    \\
                                      O    \\  .
                                        o  |\\/|
                                           / " '\
                                           . .   .
                                          /    ) |
                                         '  _.'  |
                                         '-'/    \
'''


import os
import sys
import zipfile
import datetime
import console
from configparser import ConfigParser

# Script Name
SCRIPTNAME = os.path.basename(__file__)
SCRIPTNAMENOEXT = os.path.splitext(SCRIPTNAME)[0]

# Configuration File
SCRIPTCONFIGNAME = (SCRIPTNAMENOEXT + ".cfg")
settingsconfig = ConfigParser()
settingsconfig.read(SCRIPTCONFIGNAME)

# Check if config file exists
ConfigExists = os.path.isfile(SCRIPTCONFIGNAME)
if ConfigExists:
	console.set_color(0.0, 0.3, 1.0)
	print("Parsing Configuration File ...")
else:
	console.set_color(1.0, 0.0, 0.0)
	print("Configuration File Does Not Exist!")
	sys.exit()


# Parse config file
BACKUPDIR = settingsconfig.get('BackupFrom', 'BackupDir')
EXCLUDES = settingsconfig.get('Exclude', 'ExcludeList').split(',')
ZIP_DIR = settingsconfig.get('BackupTo', 'ArchiveDir')
ARCHIVENAME = settingsconfig.get('BackupTo', 'ArchiveName')
ARCHIVENAME="%Y-%m-%d_%H%M%S_" + ARCHIVENAME

# SHARING
OpenInQuickLook = settingsconfig.get('Sharing', 'OpenInQuickLook')

# COLORS
ErrorColor = settingsconfig.get('Colors', 'ErrorColor').split(',')
StartColor = settingsconfig.get('Colors', 'StartColor').split(',')
SuccessColor = settingsconfig.get('Colors', 'SuccessColor').split(',')
InfoColor = settingsconfig.get('Colors', 'InfoColor').split(',')
ProgressColor = settingsconfig.get('Colors', 'ProgressColor').split(',')

# FONTS
TextFont = settingsconfig.get('Fonts', 'TextFont')

ARCHIVEFORMATTEDNAME=datetime.datetime.now().strftime(ARCHIVENAME)


console.clear()
console.set_font(TextFont)


def main():

	console.set_color(0.0, 0.7, 1.0)
	print("Starting Backup ...")
	excludelist=EXCLUDES
	open_in_quicklook = OpenInQuickLook
	excludelist.append(zip_dir)
	source_dir=os.path.expanduser(BACKUPDIR)
	zip_dir_full=os.path.join(source_dir,ZIP_DIR)
	fname=ARCHIVEFORMATTEDNAME
	zip_file=os.path.join(ZIP_DIR_full,fname)

	try:
		os.stat(ZIP_DIR_full)
	except:
		os.mkdir(ZIP_DIR_full)
	if not os.path.isdir(ZIP_DIR_full):

		console.set_color(1.0, 0.0, 0.0)
		print("could not create zip dest dir {zdf}".format(zdf=ZIP_DIR_full))
		sys.exit()

	make_zipfile(zip_file,source_dir,excludelist)
	console.set_color(0.0, 0.0, 1.0)
	print
	print("{fs} bytes written".format(fs=os.path.getsize(zip_file)))
	console.set_color(0.0, 1.0, 0.0)
	print("Done.")
	console.hud_alert("Done")

	if open_in_quicklook:
		console.quicklook(zip_file)


def make_zipfile(output_filename, source_dir, excludelist):
	relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
	with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
		for root, dirs, files in os.walk(source_dir,topdown=True):
			path_element=os.path.relpath(root,source_dir)
			# incredibly hacky and non-optimal way to implement an exclude list
			nextiter=False
			for path_ex in excludelist:
				if os.path.commonprefix([path_ex,path_element])==path_ex:
					nextiter=True
					break
			if nextiter==True:
				continue
			console.set_color(0.9, 0.8, 0.0)
			print("Adding {pe}".format(pe=path_element))
			zip.write(root, os.path.relpath(root, relroot))
			for file in files:
				filename = os.path.join(root, file)
				if os.path.isfile(filename): # regular files only
					arcname = os.path.join(os.path.relpath(root, relroot), file)
					zip.write(filename, arcname)

if __name__ == "__main__":
	main()



