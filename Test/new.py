from llama_cpp import Llama

# 1. โหลดโมเดล (ระบุ path ของไฟล์ .gguf ที่คุณโหลดมา)
# n_gpu_layers=0 คือการบังคับให้รันบน CPU 100%
# n_ctx คือขนาด context ที่โมเดลจะรับได้ (เช่น 4096)
print("กำลังโหลดโมเดล...")
llm = Llama(
    model_path="./Model/phi-3-mini-4k-instruct-q4.gguf",
    n_gpu_layers=0,  # <<< บังคับใช้ CPU
    n_ctx=4096,
    verbose=False
)
print("โมเดลโหลดเสร็จแล้ว")

# 2. เตรียม Prompt (สำหรับ Phi-3 ต้องใช้ format นี้)
invoice_text = """Date 07/04/25
INVOICE Invoice No. 9297
Booking ref.
DSRE84ZB6UBAP
Name: MI Squared Limited
Tax ID : 0105548119892
88 The PARQ Building, 12th Floor
Ratchadaphisek Road
Klongtoey, Klongtoey
Bangkok 10110
Thailand
Room No. : 1613
Arrival : 04/04/25
Departure : 07/04/25
Page No. : 1 of 1
Re-Prints : 08/04/25 13:32
Cashier No. : KANWARA_SR@MINOR 5509"""

prompt = f"""<|user|>
จงสกัดข้อมูลจากข้อความนี้เป็น JSON:
{invoice_text}
ต้องการให้ผลลัพธ์มีโครงสร้างดังนี้:
    {{
        "Invoice No.": "",
        "Booking ref.": "",
    }}
<|end|>
<|assistant|>""" # การจบด้วย <|assistant|> คือการบอกให้มันเริ่มตอบ

# 3. รันโมเดล
output = llm(
    prompt,
    max_tokens=256,      # จำกัดความยาวคำตอบ
    stop=["<|end|>"],  # สั่งให้หยุดเมื่อเจอ tag นี้
    echo=False           # ไม่ต้องพิมพ์ prompt ซ้ำ
)

# 4. แสดงผลลัพธ์
result_text = output["choices"][0]["text"]
print("\n--- ผลลัพธ์ ---")
print(result_text)


 
