from llama_cpp import Llama
from transformers import AutoTokenizer

print("Start loading model...")
llm = Llama(
    model_path="./Model/Phi-3-mini-4k-instruct-q4.gguf",
    n_gpu_layers=0,
    n_ctx=4096, # token context length ระวังเด้อ
    verbose=False
)

llm2 = Llama(
    model_path="./Model/phi3-invoice-finetuned-q4.gguf",
    n_gpu_layers=0,
    n_ctx=1000, # token context length ระวังเด้อ
    verbose=False
)
print("Model loaded successfully.")

# Phi-3 จาก Hugging Face
# (ใช้ trust_remote_code=True เพราะเป็นโมเดลใหม่)
tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct", 
    trust_remote_code=True
)

def getnumTokens(invoice_text):
    prompt = invoice_text
    # 1. ใช้ .encode() เพื่อแปลงข้อความเป็น "ตัวเลข" (Token IDs)
    tokens = tokenizer.encode(prompt)
    # 2. ใช้ len() เพื่อ "นับ" จำนวนตัวเลขนั้น
    token_count = len(tokens)
    print(f"Text has token : {token_count} tokens")
    return token_count

def RunModelByPrompt(prompt):
    print("Running phi3 mini model with prompt...")
    output = llm(
    prompt,
    max_tokens=2000,      # จำกัดความยาวคำตอบ
    stop=["<|end|>"],  # สั่งให้หยุดเมื่อเจอ tag นี้
    echo=False           # ไม่ต้องพิมพ์ prompt ซ้ำ
    )
    result_text = output["choices"][0]["text"]
    return result_text

def RunModelByPrompt2(prompt):
    print("Running fine-tuned invoice model...")
    output = llm2(
    prompt,
    max_tokens=2000,      # จำกัดความยาวคำตอบ
    stop=["<|end|>"],  # สั่งให้หยุดเมื่อเจอ tag นี้
    echo=False           # ไม่ต้องพิมพ์ prompt ซ้ำ
    )
    result_text = output["choices"][0]["text"]
    return result_text

def CreatePromp_1(invoice_text):
    prompt = f"""<|user|>
    จงสกัดข้อมูล,
    {invoice_text}
    ให้เป็น JSON ตามฟอร์แมตนี้:
    {{
        "Invoice No": "",    
        "Booking ref": "",  
        "Arrival": "",   
        "Departure": "",  
        "Total Non Vatable Amt": "",
        "Total Amount": "",
        "Total Vatable Amount": "",
        "VAT": "",
        "Total": ""
    }}
    <|end|>
    <|assistant|>
    """
    result_promptext = prompt
    return result_promptext

def CreatePromp_2(invoice_text):
    prompt = f"""<|user|>
    Extract_Invoice_Info,
    {invoice_text}
    <|end|>
    <|assistant|>
    """
    result_promptext = prompt
    return result_promptext

def CreatePromp_3(invoice_text):
    prompt = f"""<|user|>
    Extract_Invoice_Info,
    {invoice_text}
    <|end|>
    <|assistant|>
    """
    result_promptext = prompt
    return result_promptext


if __name__ == "__main__":
    # ทดสอบฟังก์ชันนับโทเค็น
    sample_text = "นี่คือข้อความตัวอย่างสำหรับทดสอบการนับโทเค็นใน Phi-3 โมเดล"
    getnumTokens(sample_text)