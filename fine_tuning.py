from datasets import load_dataset, load_metric
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC, TrainingArguments, Trainer
import numpy as np
import re

# dataset retirado do https://commonvoice.mozilla.org/pt/datasets
# common_voice_11_0 e 
def dataset(linguagem:str):
    dataset_voice = load_dataset("mozilla-foundation/common_voice_11_0", linguagem, split="train+validation", trust_remote_code=True) 
    test_dataset_voice = load_dataset("mozilla-foundation/common_voice_11_0", linguagem, split="test", trust_remote_code=True)
    
    return dataset_voice, test_dataset_voice

dataset_voice, test_dataset_voice = dataset("pt")
print(dataset_voice[0]["audio"])

def remove_special_characters(observation):
    chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"]'
    observation["sentence"] = re.sub(chars_to_ignore_regex, '', observation["sentence"]).lower() + " "
    return observation

dataset_voice = dataset_voice.map(remove_special_characters)
test_dataset = test_dataset_voice.map(remove_special_characters)

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h") #facebook/wav2vec2-base-960h
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h", #facebook/wav2vec2-base-960h
                                       ctc_loss_reduction="mean", 
                                       pad_token_id=processor.tokenizer.pad_token_id)

def prepare_dataset(observation):
    observation["input_values"] = processor(observation.audio.array, sampling_rate=observation.audio.sampling_rate).input_values[0]
    with processor.as_target_processor():
        observation["labels"] = processor(observation["sentence"]).input_ids
    return observation

dataset_voice = dataset_voice.map(prepare_dataset, remove_columns=dataset_voice.column_names)
test_dataset = test_dataset.map(prepare_dataset, remove_columns=test_dataset.column_names)

training_args = TrainingArguments(
  output_dir="./wav2vec2",
  group_by_length=True,
  per_device_train_batch_size=16,
  gradient_accumulation_steps=2,
  evaluation_strategy="steps",
  num_train_epochs=3,
  save_steps=400,
  eval_steps=400,
  logging_steps=400,
  learning_rate=1e-4,
  warmup_steps=500,
  save_total_limit=2,
)

# Função para calcular as métricas
def compute_metrics(pred):
    wer_metric = load_metric("wer")
    pred_logits = pred.predictions
    pred_ids = np.argmax(pred_logits, axis=-1)
    pred.label_ids[pred.label_ids == -100] = processor.tokenizer.pad_token_id
    pred_str = processor.batch_decode(pred_ids)
    label_str = processor.batch_decode(pred.label_ids, group_tokens=False)
    wer = wer_metric.compute(predictions=pred_str, references=label_str)
    return {"wer": wer}

# Configurar o Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    compute_metrics=compute_metrics,
    train_dataset=dataset_voice,
    eval_dataset=test_dataset,
    tokenizer=processor.feature_extractor,
)

# Treinar o modelo
trainer.train()

# Avaliar e salvar o modelo
trainer.evaluate(test_dataset)
model.save_pretrained("./wav2vec2")
processor.save_pretrained("./wav2vec2")