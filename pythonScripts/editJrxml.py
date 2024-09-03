import os
import re
import csv

#CONFIG AREA
# 1. Strings to search for in XML source code
search_strings = search_strings = [
    "rigType.value",
    "shipName",
    "formerName",
    "formerOwner",
    "imo",
    "bodyNumber",
    "serialNumber",
    "officialNumber",
    "homeport",
    "classification.value",
    "serviceType.value",
    "type.value",
    "portOfRegistry",
    "office",
    "builder",
    "dateOfConstruction",
    "yearBuilt",
    "placeBuilt",
    "callSign",
    "yearConverted",
    "placeConverted",
    "vesselAcquisitionType.value",
    "lengthInM",
    "lengthInMDouble",
    "lengthOverallInM",
    "lengthOverallInMDouble",
    "breadthInM",
    "breadthInMDouble",
    "moldedDepthInM",
    "moldedDepthInMDouble",
    "depthInM",
    "depthInMDouble",
    "moldedDraughtInM",
    "moldedDraughtInMDouble",
    "grossTonnage",
    "netTonnage",
    "netRegisterTonnage",
    "netRegisterTonnageDouble",
    "dwt",
    "dwtDouble",
    "hullMaterial.value",
    "horsepower",
    "kilowatt",
    "passengerCapacity",
    "tradingArea.value",
    "nationality",
    "stemType.value",
    "sternType.value",
    "dateKeelLaid",
    "launchDate",
    "deliveryDate",
    "noOfDecks",
    "noOfMasts",
    "noOfKingPosts",
    "noOfAuxiliaryEngine",
    "auxiliaryEngineMake",
    "flagState"
]

# Optional way to replace
replace_strings =[
    'vesselUpdateInfo.rigType.value',
    'vesselUpdate.Info.yearBuilt'
]

# Directory containing .jrxml files
jrxml_dir = os.path.abspath("forEditing")

# Directory containing for editing .jrxml files
to_dir = os.path.abspath("edited")

# Compile regex patterns for searching
patterns = [re.compile(s, re.IGNORECASE) for s in search_strings]

# CSV file path for output
csv_output_file = "jasper_search_results.csv"
count=0
# Open CSV file in write mode
with open(csv_output_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Create CSV writer object
    csv_writer = csv.writer(csvfile)
    # Write header row
    csv_writer.writerow(["File Name", "Found Lines"])

    # Iterate over .jrxml files in directory
for filename in os.listdir(jrxml_dir):
    if filename.endswith(".jrxml"):
        # Load .jrxml file
        jrxml_file = os.path.join(jrxml_dir, filename)

        # Extract XML source code
        with open(jrxml_file, 'r', encoding='utf-8') as f:
            xml_source = f.read()

        # List to store modified lines
        modified_lines = []
        line_numbers = []
        
        # Split the source into lines for processing
        lines = xml_source.split('\n')

        # Iterate over lines and search for strings
        for line_number, line in enumerate(lines, start=1):
            modified_line = line
            found = False

            # Replace all occurrences of search strings in the line
            for search_string in search_strings:
                if search_string in modified_line:
                    modified_line = modified_line.replace(search_string, f"vesselUpdateInfo.{search_string}")
                    found = True

            # If the line was modified, store it
            if found:
                modified_lines.append(modified_line)
                line_numbers.append(line_number)
            else:
                modified_lines.append(line)

        # Write the modified content to a new XML file
        new_jasper_file = os.path.join(to_dir, f"{filename}")
        with open(new_jasper_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(modified_lines))