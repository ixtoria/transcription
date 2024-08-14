# Plagiarism Checker in Python

This Python script allows users to compare two text documents to check for plagiarism by measuring their content similarity. It uses the TF-IDF (Term Frequency-Inverse Document Frequency) method combined with cosine similarity to determine how much the documents overlap.

## Features
- **User Input**: Prompts the user to input the file paths of the two documents to be compared.
- **TF-IDF Vectorization**: Converts text from each document into numerical vectors based on word frequency and importance.
- **Cosine Similarity**: Calculates the similarity between the two document vectors, outputting a percentage that indicates how similar the documents are.

## How to Use
1. Clone or download the repository.
2. Run the script `plagiarism_check.py`.
3. Input the paths of the two documents when prompted.
4. The script will output the similarity percentage.

This tool is useful for detecting potential cases of plagiarism or comparing the content similarity between any two text documents.
