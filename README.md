# openvpn-parser 

A Python parser to parser openvpn-status.log file into a structured JSON output

#usecase

cd /etc/openvpn
python doParse.py

# the output is written to a file parseOutput.txt

# example
{
  "real_address": "106.51.36.237:47338",
  "virtual_address": "10.8.0.42",
  "common_name": "client",
  "bytes_sent": "878749415",
  "connected_since": "Wed Aug  7 17:41:16 2019",
  "bytes_received": "15756427"
}

