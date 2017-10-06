# The-Grid to Agent-Stats converter
This application exports all statistics from The-Grid and outputs it in a format compatible for import on Agent-Stats.

## Usage
The script takes the API-key from The-Grid asmandatory argument.  
It's also possible change API URL if needed via an optional argument.
  
To send the data ready for import to paste buffer:  
./thegrid2agentstats.py MY-SECRET-API-KEY | xclip

## Notes
If there are broken records from bad OCR scans on The-Grid then the import will fail. These entries have to manually be filtered out before import.

