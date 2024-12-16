1. BERT 文本分类代码 (nlp_bert_text_classification.py)

# nlp_bert_text_classification.py

from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments
from datasets import load_dataset
import torch

# 加载预训练的BERT模型和分词器
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# 加载一个示例数据集，这里使用的是情感分析数据集
dataset = load_dataset("imdb")

# 定义数据处理函数：将文本转换为模型输入格式
def preprocess_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

# 处理数据集
encoded_dataset = dataset.map(preprocess_function, batched=True)

# 设置训练参数
training_args = TrainingArguments(
    output_dir="./results",          # 输出结果的文件夹
    num_train_epochs=3,              # 训练的轮数
    per_device_train_batch_size=8,   # 每个设备的训练批次大小
    per_device_eval_batch_size=8,    # 每个设备的评估批次大小
    warmup_steps=500,                # 预热步骤
    weight_decay=0.01,               # 权重衰减
    logging_dir="./logs",            # 日志文件夹
)

# 定义 Trainer
trainer = Trainer(
    model=model,                         # 使用的模型
    args=training_args,                  # 训练参数
    train_dataset=encoded_dataset["train"], # 训练数据集
    eval_dataset=encoded_dataset["test"],   # 测试数据集
)

# 开始训练
trainer.train()

# 测试模型
predictions, labels, metrics = trainer.predict(encoded_dataset["test"])
print("Predictions:", predictions[:5])  # 打印前5个预测结果


