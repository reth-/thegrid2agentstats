# The-Grid to Agent-Stats converter
This application exports all statistics from The-Grid and outputs it in a format compatible for import on Agent-Stats.

## Usage
The script takes the API-key from The-Grid as a mandatory argument.  

## Optional command arguments
| Short   | Long          | Description                       |
| ------- | ------------- | --------------------------------- |
| -a DATE | --after DATE  | Only list entries newer than DATE |
| -b DATE | --before DATE | Only list entries older than DATE |
| -h      | --help        | Usage information                 |
| -u URL  | --url URL     | Alternate API URL                 |
  
DATE shall have format: YYYY-MM-DD  
URL shall have format: http(s)://foo.bar/api?key=  
API key will be appended to the URL.

## Usage examples
To send the data ready for import to paste buffer:  
./thegrid2agentstats.py MY-SECRET-API-KEY | xclip  
  
List stats newer than 2017-01-01:  
./thegrid2agentstats.py -a 2017-01-01 MY-SECRET-API-KEY

## Notes
If there are broken records from bad OCR scans on The-Grid then the import will fail. These entries have to manually be filtered out before import.

