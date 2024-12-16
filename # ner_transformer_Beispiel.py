# ner_transformer_Beispiel.py

from transformers import pipeline

# 使用Hugging Face的pipeline API，加载预训练模型进行NER任务
ner_model = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# 输入文本
text = """
Tesla, Inc. is an American electric vehicle and clean energy company. It was founded by Elon Musk in 2003 and is headquartered in Palo Alto, California.
"""

# 使用NER模型进行实体识别
entities = ner_model(text)

# 输出识别到的实体
print("Named Entities:")
for entity in entities:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}, Confidence: {entity['score']:.4f}")
