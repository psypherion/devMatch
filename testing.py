from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import AutoModelForTokenClassification, AutoTokenizer
from transformers import AutoModelForMaskedLM, AutoTokenizer
from transformers import AutoModelForMultipleChoice, AutoTokenizer
from transformers import AutoModelForNextSentencePrediction, AutoTokenizer


# model_name = "huggingface/falcon-7b"
model_name = "tiiuae/falcon-7b"  # or another model from your list

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

input_text = "Question: How many hours in one day? Answer: "
input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

outputs = model.generate(input_ids)
print(tokenizer.decode(outputs[0]))