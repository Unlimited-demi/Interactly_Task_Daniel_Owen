from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments
import pandas as pd

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

resume_df = pd.read_csv('../data/resume.csv')

def encode(data):
    return tokenizer(data, return_tensors='pt', max_length=512, truncation=True, padding="max_length")

tokenized_resumes = resume_df['Resume_str'].apply(encode)

dataset = TextDataset(
    tokenizer=tokenizer,
    file_path="../data/resume.txt",
    block_size=128,
)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
    eval_dataset=dataset,
)

trainer.train()

model.save_pretrained("../models/fine_tuned_gpt2")
print("Fine-tuning complete.")
