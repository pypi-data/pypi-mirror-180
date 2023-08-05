<p align="center">
<a href="https://pypi.org/project/chksum-cli/">
<img align="center" src="https://raw.githubusercontent.com/espehon/chksum-cli/main/docs/images/Demo.png"/>
</a>
</p>

# chksum
CLI for comparing two checksums

# Usage
```
CHKSUM [-?] [-i] [-d] position1 position2 [position3]

Calculate and compare the checksums of files or directories.
Can also compare against pasted strings.
ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512']

positional arguments:
  position1          Checksum, file, or algorithm
  position2          Checksum, file, or algorithm
  position3          Checksum, file, or algorithm

options:
  -?, --help         Show this help message and exit.
  -i, --interactive  Run in interactive mode.
  -d, --dots         Ignore '.' (dot) files from directories.

If the first 2 positional arguments are strings, the algorithm is not needed. Default is md5.
```
Arguments can be passed in any order\
E.g. the following are equivalent:\
`chksum <PathToFile> <PathToDir> sha256 -d`\
`chksum -d <PathToDir> sha256 <PathToFile>`


# Interactive mode
Use `-i` to enter the interactive mode where arguments can be passed one at a time.
```
$ chksum -i

      _     _
     | |   | |
  ___| |__ | | _____ _   _ _ __ ___
 / __| '_ \| |/ / __| | | | '_ ` _ \
| (__| | | |   <\__ \ |_| | | | | | |
 \___|_| |_|_|\_\___/\__,_|_| |_| |_|
 Copyright (c) 2022, espehon
 All rights reserved.

 ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512']

Enter Algorithm or path to File or Directory >
```
Inputs are checked after each entry and the prompt is updated accordingly
```
Enter Algorithm or path to File or Directory > ./
        Directory entered.
Enter Algorithm or path to File or Directory > ./
        Directory entered.
Enter Algorithm > md5
        Algorithm entered.
Do you want to include '.' (dot) files? [Y/n] > n
ignore_dots = True

-------------[MD5]--------------
23bbc59717b7375774fe97cbfc5fd12c
23bbc59717b7375774fe97cbfc5fd12c
√ Hashes Match
```



## Authors

- [@espehon](https://www.github.com/espehon)


