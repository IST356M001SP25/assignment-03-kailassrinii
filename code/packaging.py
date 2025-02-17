'''
This is a module for parsing package data
'''

class Package:
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

def parse_package_string(package_str: str) -> Package:
    '''
    Parse a string containing package dimensions and return a Package object.
    Expected format: "length width height"
    Example: "10 20 30" creates a Package with length=10, width=20, height=30
    '''
    try:
        dimensions = package_str.strip().split()
        if len(dimensions) != 3:
            raise ValueError("Package string must contain exactly 3 numbers")
            
        length, width, height = map(float, dimensions)
        return Package(length, width, height)
    except ValueError as e:
        raise ValueError(f"Invalid package string format. Error: {str(e)}")

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''

    package = []
    for data in packaging_data.split('/'):
        item = data.split(" in ")[0]
        quantity = int(item.split()[0])
        item = item.split()[1].strip()
        package.append({item: quantity})
    
    # get the last one
    item = data.split(" in ")[-1]
    quantity = int(item.split()[0])
    item = item.split()[1].strip()
    package.append({item: quantity})

    return package

def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''

    total = 1
    for item in package:
        total *= list(item.values())[0]
    return total

def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    return list(package[0].keys())[0]

# This will only run from here, not when imported
# Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    # Test the package dimensions parser
    test_str = "10 20 30"
    package = parse_package_string(test_str)
    print(f"Length: {package.length}")
    print(f"Width: {package.width}")
    print(f"Height: {package.height}")
    
    # Test the packaging parser
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package_data = parse_packaging(text)
    print(package_data)

    package_total = calc_total_units(package_data)
    unit = get_unit(package_data)
    print(f"{package_total} {unit} total")