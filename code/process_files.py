import streamlit as st
import json
from packaging import Package, parse_package_string

def initialize_session_state():
    if 'total_files' not in st.session_state:
        st.session_state.total_files = 0
    if 'total_lines' not in st.session_state:
        st.session_state.total_lines = 0
    if 'processed_files' not in st.session_state:
        st.session_state.processed_files = []

def main():
    st.title("Multiple Package Files Processor")
    initialize_session_state()
    
    uploaded_file = st.file_uploader("Choose a package data file", type=['txt'])
    
    if uploaded_file is not None:
        if uploaded_file.name in st.session_state.processed_files:
            st.warning(f"File {uploaded_file.name} was already processed!")
            return
        
        file_contents = uploaded_file.getvalue().decode("utf-8")
        packages = []
        line_count = 0
        
        try:
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
                    line_count += 1
            
            st.session_state.total_files += 1
            st.session_state.total_lines += line_count
            st.session_state.processed_files.append(uploaded_file.name)
            output_filename = f"{uploaded_file.name.split('.')[0]}.json"
            with open(output_filename, 'w') as f:
                json.dump(packages, f, indent=4)
            
            st.success(f"{len(packages)} packages written to {output_filename}")
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    
    st.subheader("Processing Summary")
    st.write(f"Total files processed: {st.session_state.total_files}")
    st.write(f"Total lines processed: {st.session_state.total_lines}")
    
    if st.session_state.processed_files:
        st.subheader("Processed Files")
        for file in st.session_state.processed_files:
            st.write(f"- {file}")

if __name__ == "__main__":
    main()