import streamlit as st
from packaging import Package, parse_package_string
def main():
    st.title("Package Parser")
    package_input = st.text_area("Enter package data:")
    if package_input:
        try:
            package = parse_package_string(package_input)
            st.subheader("Package Information")
            st.write(f"Length: {package.length}")
            st.write(f"Width: {package.width}")
            st.write(f"Height: {package.height}") 
            total_size = package.length * package.width * package.height
            st.subheader("Total Package Size")
            st.write(f"{total_size} cubic units") 
        except Exception as e:
            st.error(f"Error package data: {str(e)}")
if __name__ == "__main__":
    main()