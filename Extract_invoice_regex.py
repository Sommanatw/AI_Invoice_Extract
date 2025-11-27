import InvoiceExtract
import os
import re
import json

#regex pattern
def extract_field(text):
    patterns = {
        "Invoice No": r"Invoice No\.?\s*(\d+)",
        "Booking ref": r"Booking ref\.?\s*([\w\d]+)",
        "Arrival": r"Arrival\s*:?\s*([\d/]+)",
        "Departure": r"Departure\s*:?\s*([\d/]+)",
        "Total Non Vatable Amt": r"Total Non Vatable Amt\s*([\d.,]+\s*THB)",
        "Total Amount": r"Total Amount\s*([\d.,]+\s*THB)",
        "Total Vatable Amount": r"Total Vatable Amount\s*([\d.,]+\s*THB)",
        "VAT": r"VAT\s*([\d.,]+\s*THB)",
        "Total": r"Total\s*([\d.,]+\s*THB)",
        "Balance": r"Balance\s*([\d.,]+\s*THB)"
    }

    result = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        result[key] = match.group(1) if match else ""

    json_output = json.dumps(result, indent=4, ensure_ascii=False)
    #print(json_output)
    return json_output




def main():
    folder_invoice = "./Invoice/"
    folder_textfile = "./Result_1/Invoice_text/"
    folder_invoice_json = "./Result_1/Invoice_json/"

    # วนลูปอ่านไฟล์ PDF ในโฟลเดอร์ folder_invoice
    for filename in os.listdir(folder_invoice):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_invoice, filename)
            print(f"\nProcessing file: {file_path}")
            extracted_data = InvoiceExtract.ExtractInvoice.read_pdf_text(file_path)
            #print("\n--- ข้อมูลที่สกัดได้จากใบแจ้งหนี้ ---")
            #print(extracted_data)

            textfile_path = os.path.join(folder_textfile, filename.replace(".pdf", ".txt"))
            with open(textfile_path, "w", encoding="utf-8") as textfile:
                textfile.write(extracted_data)
            
            json_result = extract_field(extracted_data)
            #print(f"\nExtracted JSON data:\n{json_result}")

            
            jsonfile_path = os.path.join(folder_invoice_json, filename.replace(".pdf", ".json").replace(" ", ""))
            #print(f"\nWriting JSON file: {jsonfile_path}")
            with open(jsonfile_path, "w", encoding="utf-8") as jsonfile:
                jsonfile.write(json_result)


            
            


if __name__ == "__main__":
    main()