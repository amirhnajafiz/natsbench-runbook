import csv


"""export dataset is used to create a csv file
for a command results.

params:
    - location: string
    - array: list
"""
def export_dataset(location: str, array: list):
    with open(location, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["pub-stats", "sub-stats", "overall-stats"]
        writer.writerow(field)
        
        for subarray in array:  
            writer.writerow(subarray)
