## Rationale

There are several guides on bypassing the admin BIOS password on HP computers out there, and a few supporting tools. I have yet to encounter a tool which automates the process of entering MPM (manufacturer programming mode) to accomplish this bypass. The present tool will perform the required modifications to your binary dump and create a file with the suffix _patched which can be flashed onto your main BIOS chip to enter this mode.

## Usage

This is a simple python program which takes as a single argument a UNC path to a binary dump of the Main BIOS chip data from an HP computer. The tool will modify the binary data by removing an nvram section called UserCreds AND by patching the H.p.M.p.m value with a hex sequence that triggers boot into MPM (manufacturer programming mode). From this mode, it is possible to bypass the administrator BIOS password by first resetting Factory default settings and subsequently resetting security settings. You can then set your own BIOS password if desired. NOTE that you will need to manually input device information if you reset to factory defaults. Have this info extracted prior to usage (F1 during boot process or use a third party tool or extract it from the BIOS dump). 

## Warnings

BE WARNED, flashing BIOS can lead to a bricked computer if not done correctly. The output from this program is in no way guaranteed to work, so use this at your own risk! ALWAYS ensure that you have 3 consistent backups of your original BIOS data prior to attempting modification, so that you can rollback if needed. This tool is NOT meant to be used on the dump from an Embedded Controller. Only use the main BIOS chip dump with this program.
Additionally, be aware that entering MPM and resetting factory default settings will clear various import DMI data such as serial number, feature byte, Product UUID, etc from your BIOS. **You must extract this information prior** to this operation so that it **can be manually repopulated** via the BIOS menu after resetting to factory default. You can extract this data from the BIOS information screen even on locked computers by pressing F1 ("show system information") boot, finding a way to navigate from the BIOS menu to "system information", or extracting via third party tools or dump information manually.

## Demo
![demo]("https://github.com/PN-Tester/pn-patcher/blob/a763200128ed063ee3a6d7d1eeee64ba15be4cc1/pn-patcher.gif")

