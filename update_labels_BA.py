import argparse

def update_pop_labels(list_samples, BA_file, output_file):
    """
    Updates population labels in BA3 file using a dictionary from a map file.
    
    Arguments:
    - list_samples (str): Path to the list of samples file
    - BA_file (str): Path to the input BA3 file
    - output_file (str): Path to the output file
    
    """
    # Load dictionary from map file
    dictionary = {}
    with open(list_samples) as map_file:
        for line in map_file:
            fields = line.strip().split()
            dictionary[fields[0]] = fields[1]

    # Update population labels in BA3 file
    with open(BA_file) as ba3_file, open(output_file, 'w') as out_file:
        for line in ba3_file:
            fields = line.strip().split()
            if fields[0] in dictionary:
                fields[1] = dictionary[fields[0]]
            out_file.write('\t'.join(fields) + '\n')

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Update population labels in BA3 file.')
    parser.add_argument('list_samples', help='Path to the list of samples file')
    parser.add_argument('BA_file', help='Path to the input BA3 file')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()

    # Call update_pop_labels function
    update_pop_labels(args.list_samples, args.BA_file, args.output_file)

