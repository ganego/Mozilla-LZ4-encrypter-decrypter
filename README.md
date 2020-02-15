# Mozilla-LZ4-encrypter-decrypter
Encrypt and decrypt mozl4, jsonlz4, lz4, baklz4 files from Mozilla Firefox 

Needs `lz4`. Install via `pip install lz4`

Save `Mozilla-LZ4.py` to your machine.  
Usage: `Mozilla-LZ4.py <inputfile>`

You can drag & drop files on it or use the command line to access it.

It only accepts one file path. If that file has a Mozilla LZ4 extension (.lz4, .mozlz4, .jsonlz4, .baklz4) it will decode/unpack, otherwise it will try to encode/pack the file (always to the same folder the original file was in). 
You will get an overwrite warning/question in case the output file already exists.
