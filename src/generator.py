# from openai import OpenAI
# C:\Users\KIIT0001\anaconda3\python.exe -m pip install openai
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Generator:
    # def __init__(self, model="gpt-4o-mini"):
    #     self.model = model
    #     self.client = OpenAI()
    def __init__(self, model_name="google/flan-t5-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate(self, question, retrived_chunks):
        context = "\n\n".join(f"source:{chunk['filename']} \n {chunk['text']}" for chunk in retrived_chunks)
        prompt = f"""
                   You are a helpful assistant. Answer the question ONLY using the context below. If the answer is not contained in the context, say "I don't know."
                   Context: {context}
                   Question: {question}
                   Answer:
                """
        # response = self.client.chat.completions.create(
        #                model=self.model,
        #                messages=[{"role": "user", "content": prompt}],
        #                temperature=0
        #              )
        # return response.choices[0].message.content.strip()

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=150
        )
        answer = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        sources = list({chunk["filename"] for chunk in retrived_chunks})

        return {
            "answer": answer,
            "sources": sources
        }

        # return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

