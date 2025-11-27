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


def save_to_dataset(prompt_text, json_answer_str, output_filename="train_dataset.jsonl"):
    full_text = f"\n{prompt_text}\n{json_answer_str}\n<|end|>"
    line_data = {"text": full_text}
    with open(output_filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(line_data, ensure_ascii=False) + "\n")


def main():
    folder_invoice = "./Invoice/"
    folder_textfile = "./Result_1/Invoice_text/"
    folder_invoice_json = "./Result_1/Invoice_json/"
    
    dataset_file = "train_dataset.jsonl"
    if os.path.exists(dataset_file):
        os.remove(dataset_file)
        print(f"Removed old {dataset_file}, starting fresh.")


    # วนลูปอ่านไฟล์ PDF ในโฟลเดอร์ folder_invoice
    for filename in os.listdir(folder_invoice):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_invoice, filename)
            print(f"\nProcessing file: {file_path}")

            extracted_data = InvoiceExtract.ExtractInvoice.read_pdf_text(file_path)
            #print(extracted_data)
            clean_text = re.sub(r'\n+', '\n', extracted_data).strip()
            #print(clean_text)
            CratePrompt = InvoiceExtract.WithLLM.CreatePromp(clean_text)
            #print(f"promp {CratePrompt}")
          
            json_result = extract_field(extracted_data)
            #print(f"\nExtracted JSON data:\n{json_result}")
            # ถ้าใน CratePrompt มีคำว่า STATEMENT OF ACCOUNT ให้ข้ามการบันทึก
            if "STATEMENT OF ACCOUNT" in CratePrompt:
                print("Skipped saving due to presence of 'STATEMENT OF ACCOUNT' in prompt.")
                continue
            save_to_dataset(CratePrompt, json_result, dataset_file)

if __name__ == "__main__":
    main()