import fitz

def read_pdf_text(file_path):
    try:
        doc = fitz.open(file_path)
        full_text = ""        

        page = doc.load_page(0)  # อ่านเฉพาะหน้าที่ 0 (หรน้าแรก)
        full_text += page.get_text()    # ดึงข้อความ
        print(f"\n--- ข้อความจากหน้า 1 ---\n{full_text}")
        #ตัดข้อมความที่ไม่จำเป็นออก ตั้งแต่บรรทัดแรกจนถึงคำว่า INVOICE นำออกไม่เอา คำว่า INVOICE ก็ไม่เอา
        invoice_index = full_text.find("INVOICE")
        if invoice_index != -1:
            full_text = full_text[invoice_index + len("INVOICE"):]           

        #ตัดข้อมความที่ไม่จำเป็นออก ตั้งแต่คำว่า Name: จน Arrival นำออกไม่เอา
        name_index = full_text.find("Name:")
        arrival_index = full_text.find("Arrival")
        if name_index != -1 and arrival_index != -1 and arrival_index > name_index:
            full_text = full_text[:name_index] + full_text[arrival_index:]

        #ตัดข้อมความที่ไม่จำเป็นออก ค้นหา Please pay by cheque จนถึงบรรทัดสุดท้าย นำออกไม่เอา
        pay_index = full_text.find("Please pay by cheque")
        if pay_index != -1:
            full_text = full_text[:pay_index]

        #ตัดข้อมความที่ไม่จำเป็นออก ค้นหา In signing this bill จนถึงคำว่า Date นำออกไม่เอาแต่เอาคำว่า Date
        sign_index = full_text.find("In signing this bill")
        date_index = full_text.find("Date")
        if sign_index != -1 and date_index != -1 and date_index > sign_index:
            full_text = full_text[:sign_index] + full_text[date_index:]
        
        #ตัดข้อมความที่ไม่จำเป็นออก ตั้งแต่คำว่า Date จนถึงบรรทัดสุดท้าย นำออกไม่เอา

        doc.close()
        return full_text

    except Exception as e:
        print(f"Error on reading PDF: {e}")
        return None




def main():
    pdf_file = "D://GIT//AI_Invoice_Extract//Invoice//INV . 5334.pdf"
    invoice_text = read_pdf_text(pdf_file)

    if invoice_text:
        print("--- ข้อความที่ดึงได้จาก PDF ---")
        print(invoice_text)
    else:
        print("ไม่สามารถดึงข้อความได้")


if __name__ == "__main__":
    main()