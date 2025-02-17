import streamlit as st
import json
from packaging import Package, parse_package_string

def main():
    st.title("Package File Processor")
    
    uploaded_file = st.file_uploader("Choose a package data file", type=['txt'])
    
    if uploaded_file is not None:
        file_contents = uploaded_file.getvalue().decode("utf-8")
        
        try:
            packages = []
            for line in file_contents.split('\n'):
                line = line.strip()
                if line: 
                    package = parse_package_string(line)
                    packages.append({
                        "length": package.length,
                        "width": package.width,
                        "height": package.height,
                        "total_size": package.length * package.width * package.height
                    })
            
            st.subheader("Parsed Packages")
            for i, package in enumerate(packages, 1):
                st.write(f"Package {i}:")
                st.write(f"Length: {package['length']}")
                st.write(f"Width: {package['width']}")
                st.write(f"Height: {package['height']}")
                st.write(f"Total Size: {package['total_size']} cubic units")
                st.write("---")
            
            output_filename = "packages.json"
            with open(output_filename, 'w') as f:
                json.dump(packages, f, indent=4)
            
            st.success(f"Successfully wrote {len(packages)} packages to {output_filename}")
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()