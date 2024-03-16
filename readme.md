This is a simple python program which takes as a single argument a UNC path to a binary dump of the Main BIOS chip data from an HP computer. The tool will modify the binary data by removing an nvram section called UserCreds AND by patching the H.p.M.p.m value with a hex sequence that triggers boot into MPM (manufacturer programming mode). From this mode, it is possible to bypass the administrator BIOS password by resetting Factory default settings and subsequently resetting security settings.
BE WARNED, flashing BIOS is can lead to to a bricked computer if not done correctly. The output from this program is in no way guaranteed to work, so use this at your own risk! ALWAYS ensure that you have 3 consistent backups of your original BIOS data prior to attempting modification, so that you can rollback if needed.
Additionally, be aware that entering MPM and resetting factory default settings will clear various import DMI data such as serial number, feature byte, Product UUID, etc from your BIOS. You must extract this information prior to this operation so that it can be manually repopulated via the BIOS menu after resetting to factory default. You can extract this data from the BIOS information screen even on locked computers by pressing F1 ("show system information") during preboot.
