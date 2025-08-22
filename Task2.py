# Name: Ronak Manoj Maheshwari
# Topic : A SCRIPT THAT READS DATA FROM A FILE, ANALYZES IT, AND GENERATES A FORMATTED PDF REPORT
# Software : Visual Studio Code
# Language : Python


import csv
from fpdf import FPDF

# Step 1: Read and analyze data from CSV
def analyze_data(file_path = "C:/Users/Ronak/Desktop/data.csv"):
    names = []
    sales = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row['Name'])
            sales.append(int(row['Sales']))  # ✅ Fixed missing parenthesis

    total_sales = sum(sales)               # ✅ Removed extra parenthesis
    average_sales = total_sales / len(sales)
    max_sale = max(sales)
    max_person = names[sales.index(max_sale)]  # ✅ Added argument to index()

    return {
        "names": names,
        "sales": sales,
        "total_sales": total_sales,
        "average_sales": average_sales,
        "top_seller": max_person,
        "top_sale": max_sale
    }

# Step 2: Generate PDF report
def generate_pdf_report(data, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')
    pdf.ln(10)

    for name, sale in zip(data["names"], data["sales"]):
        pdf.cell(200, 10, txt=f"{name}: {sale}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Sales: {data['total_sales']}", ln=True)
    pdf.cell(200, 10, txt=f"Average Sales: {data['average_sales']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Top Seller: {data['top_seller']} ({data['top_sale']})", ln=True)

    pdf.output(output_file)

# Step 3: Run Functions
if __name__ == "__main__":  # ✅ Fixed comparison operator
    file_path = "data.csv"
    report_data = analyze_data(file_path)
    generate_pdf_report(report_data, "sales_report.pdf")
    print("Report Generated: sales_report.pdf")


import webbrowser
webbrowser.open("sales_report.pdf")

#Explaination : 
# This Python script automates the process of analyzing sales data from a CSV file and generating a PDF report.
# It uses two powerful libraries: csv for reading structured data and FPDF for dynamic PDF creation.
# The script is divided into three main parts: data analysis, PDF generation, and execution logic for modularity.
# In the first part, the analyze_data function reads the CSV file using csv.DictReader for easy column access.
# Each row is treated as a dictionary, allowing the script to extract names and sales figures efficiently.
# Sales values are converted into integers to enable numerical operations like summing, averaging, and finding the maximum.
# The function calculates total sales using sum(sales) and average sales by dividing total by number of entries.
# It identifies the highest sale using max(sales) and locates the top seller using sales.index(max_sale).
# All these metrics are returned in a dictionary, making them easily accessible for the next processing step.
# The second part, generate_pdf_report, takes the analyzed data and creates a clean, professional PDF document.
# It initializes a new PDF, adds a page, and sets the font to Arial with a size of 14.
# A centered title “Sales Report” is added, followed by a loop that prints each name and sales figure.
# After listing individual entries, the function adds summary statistics like total sales and average sales (formatted).
# It also highlights the top seller and their sales figure, giving the report a clear and informative structure.
# The PDF is saved using pdf.output(output_file), which writes the final document to disk automatically.
# The third part is the execution block, which runs only when the script is executed directly by the user.
# It sets the file path to the CSV, calls analyze_data, and passes results to generate_pdf_report function.
# A confirmation message is printed to indicate successful report generation, completing the automation workflow.
# This modular structure makes the script easy to maintain, extend, or integrate into larger Python applications.
# In practical terms, this tool is perfect for internships, academic projects, or startup environments needing quick reports.
# It eliminates manual calculations and formatting, saving time and reducing human error in repetitive tasks.
# For someone like you, Ronak, who blends technical skill with creative flair, this script is a perfect showcase.
# You can enhance it by adding charts using matplotlib, embedding logos, or customizing layout for branding.
# You could even turn it into a web-based tool using Flask, allowing users to upload CSVs and get PDFs.
# The ability to generate structured reports from raw data is a highly valuable skill across many industries today.
# This script gives you a solid foundation to build more advanced reporting tools with real-world applications.
# Whether you're preparing a client presentation, submitting a project report, or practicing Python, this tool shines.
# It’s practical, impressive, and a great example of how code can turn data into polished visual storytelling.
