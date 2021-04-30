# Script for photo editing
## Problem
When editing raw files with photoshop camera raw there is no easy way to select all the files you edited at once. This is desirable because you will ultimately want to export these files to JPG or other format to share.

## Approach
When a file is edited with Photoshop it creates a parallel `.xmp` file. This script will open all raw files that have a corresponding `.xmp` file in the current directory (sub directories not included) for quick exporting.

_This assumes you have the proper program (in this case photoshop) to open the raw files by default_