import pdfkit

def save_website_as_pdf(url, output_filename):
    try:
        pdfkit.from_url(url, output_filename)
        print(f"Successfully saved {url} as {output_filename}")
    except Exception as e:
        print(f"Failed to save {url} as PDF. Error: {str(e)}")

# Example usage:
website_url = "https://example.com"
output_file = "example.pdf"

save_website_as_pdf(website_url, output_file)
