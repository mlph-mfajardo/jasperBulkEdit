import os
import re
import csv
import shutil

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
# 2. Isolate detected file to forEditing
moveFiles = False


# Directory containing .jrxml files
jrxml_dir = os.path.abspath("jrxmlFiles")

# Directory containing for editing .jrxml files
to_dir = os.path.abspath("forEditing")

# Compile regex patterns for searching 
# use patterns if regex is required
patterns = [re.compile(s, re.IGNORECASE) for s in search_strings]

#Functions
def copy_and_move_file(source_file, to_directory):
    try:
        # Copy the file to the destination directory
        shutil.copy(source_file, to_directory)
        # Get the filename from the source file path
        filename = os.path.basename(source_file)
        # Generate the destination file path
        destination_file = os.path.join(to_directory, filename)
        # Return the destination file path
        return destination_file
    except Exception as e:
        print(f"Error: {e}")
        return None

# CSV file path for output
csv_output_file = "jasper_search_results.csv"
lines=0
jrxmlcount=0
with open(csv_output_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Create CSV writer object
    csv_writer = csv.writer(csvfile)
    # Write header row
    csv_writer.writerow(["File Name", "Found Lines"])

    for filename in os.listdir(jrxml_dir):
        if filename.endswith(".jrxml"):
            hasSigPosField=False
            jrxmlcount+=1
            # Load .jrxml file
            jrxml_file = os.path.join(jrxml_dir, filename)

            # Extract XML source code
            with open(jrxml_file, 'r', encoding='utf-8') as f:
                xml_source = f.read()

            # List to store found lines
            found_lines = []
            prev_line = ""

            # Search for specific strings in XML source code
            #for pattern in patterns:
            for search_string in search_strings:
                for line_number, line in enumerate(xml_source.split('\n'), start=1):
                    #if pattern.search(line):
                    if search_string in line:
                        found_lines.append(f"Line {line_number}: {line.strip()}")
                    #    found_lines.append(f"Previous Line {line_number-1}: {prev_line.strip()}") # if line is cut, seeing the previous line helps
                    #prev_line = line
                    

            # Write file name and found lines to CSV
            # runs once by file
            if found_lines:
                csv_writer.writerow(["\n"+filename + "\n", '\n'.join(found_lines)])
                lines+=1
                if moveFiles: 
                    copy_and_move_file(jrxml_file, to_dir)

print(lines,"---- total checked=", jrxmlcount)



