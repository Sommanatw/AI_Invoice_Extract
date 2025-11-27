from llama_cpp import Llama
import InvoiceExtract
from transformers import AutoTokenizer
import os


def main():
    folder_invoice = "./Invoice_LLM/"
    folder_textfile = "./Result_2/Invoice_text/"
    folder_invoice_json = "./Result_2/Invoice_json/"

    # วนลูปอ่านไฟล์ PDF ในโฟลเดอร์ folder_invoice
    for filename in os.listdir(folder_invoice):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_invoice, filename)
            print(f"\nProcessing file: {file_path}")
            extracted_data = InvoiceExtract.ExtractInvoice.read_pdf_text(file_path)
            print("\n--- ข้อมูลที่สกัดได้จากใบแจ้งหนี้ ---")
            print(extracted_data)

            #นำ extracted_data ไปเขียนลงใน text file
            textfile_path = os.path.join(folder_textfile, filename.replace(".pdf", ".txt"))
            with open(textfile_path, "w", encoding="utf-8") as textfile:
                textfile.write(extracted_data)
            


            # นับจำนวนโทเค็นใน extracted_data
            token_num = InvoiceExtract.UseLLM.getnumTokens(extracted_data)
            print(f"\nจำนวนโทเค็นในข้อมูลที่สกัดได้: {token_num}")

            
            # สร้าง prompt สำหรับรันโมเดล
            CratePrompt = InvoiceExtract.WithLLM.CreatePromp_1(extracted_data)
            print("\n--- Prompt ที่สร้างขึ้น ---")
            print(CratePrompt)
            token_num = InvoiceExtract.UseLLM.getnumTokens(CratePrompt)
            print(f"\nPromp token: {token_num}")

            executed_result = InvoiceExtract.WithLLM.RunModelByPrompt(CratePrompt)

            #นำ executed_result ไปเขียนลงใน json file
            jsonfile_path = os.path.join(folder_invoice_json, filename.replace(".pdf", ".json"))
            with open(jsonfile_path, "w", encoding="utf-8") as jsonfile:
                jsonfile.write(executed_result)
            
            
if __name__ == "__main__":
    main()