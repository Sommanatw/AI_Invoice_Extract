from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

# ระบุชื่อโมเดล
model_name = "deepset/xlm-roberta-base-squad2"

# 2. โหลด Tokenizer และ Model ด้วยตัวเอง
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# 3. ส่ง model และ tokenizer ที่โหลดแล้วเข้าไปใน pipeline
qa_pipeline = pipeline(
    "question-answering",
    model=model,
    tokenizer=tokenizer
)

# ข้อมูล Invoice ที่เป็น string
context = """
SAMUI RESORT & SPA LIMITED99/9 Moo 1 Bophut Bay, Amphur KohSamui, Suratthani 84320Tax ID: 0105546043112 Branch: 00001Date 30/05/25Booking ref.INVOICE Invoice No. 5560 DSR0551J5DZD3Name: MI Squared Limited Room No. : 408Tax ID : 0105548119892 Arrival : 29/05/2588 The PARQ Building, 12th Floor Departure : 30/05/25Ratchadaphisek Road Page No. : 1 of 1Klongtoey, Klongtoey Re-Prints : 02/06/25 09:47Bangkok   10110 Cashier No. : VANNAKARN_KA@MINORThailand 7023Folio No. : 15126Tax ID/Tax Branch: 0105548119892Guest Name: Krampaibul, Phakee AR Number : 2600019...
"""

# ตั้งคำถามที่เฉพาะเจาะจง
questions = [
    "What is the Folio No.?",
    "What is the Tax ID for the company located at The PARQ Building?",
    "What is the invoice number?",
    "What is the total balance?"
]

# วนลูปเพื่อถามและพิมพ์คำตอบ
for question in questions:
    result = qa_pipeline(question=question, context=context)
    print(f"Question: {question}")
    print(f"Answer: {result['answer']} (Score: {result['score']:.4f})\n")



    token_num = InvoiceExtract.UseLLM.getnumTokens(extracted_data)
    print(f"\nจำนวนโทเค็นในข้อมูลที่สกัดได้: {token_num}")

    extracted_data = """Invoice No. 9297
Booking ref.
DSRE84ZB6UBAP
Arrival
: 04/04/25
Departure
: 07/04/25
Folio No.
: 43159
Total Non Vatable Amt
0.00
Total Amount
15,300.00
Total Vatable Amount
14,299.08
VAT
1,000.92
Total
15,300.00
0.00
Balance
15,300.00"""

    token_num = InvoiceExtract.UseLLM.getnumTokens(extracted_data)
    print(f"\nData extract token: {token_num}")

    CratePrompt = InvoiceExtract.WithLLM.CreatePromp(extracted_data)

    token_num = InvoiceExtract.UseLLM.getnumTokens(CratePrompt)
    print(f"\nPromp token: {token_num}")

    executed_result = InvoiceExtract.WithLLM.RunModelByPrompt(CratePrompt)
    print("\n--- ผลลัพธ์จาก Phi-3 ---")
    print(executed_result)