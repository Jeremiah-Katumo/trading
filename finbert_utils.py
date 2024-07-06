
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import Tuple
device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification \
    .from_pretrained("ProsusAI/finbert").to(device)
labels = ["positive", "negative", "neutral"]

def estimate_sentiment(news):
    if news:
        tokens = tokenizer(news, return_tensors="pt", padding=True).to(device)

        result = model(tokens["input_ids"], attention_mask=tokens["attention_mask"])["legits"]
        result = torch.nn.functional.softmax(torch.sum(result, 0), dim=-1)
        probability = result[torch.argmax(result)]
        sentiment = labels[torch.argmax(result)]

        return probability, sentiment
    else:
        return 0, labels[-1]
    
def position_sizing(cash, last_price, cash_at_risk) -> int:
    quantity = round(cash_at_risk * cash / last_price, 0)
    
    return quantity


if __name__ == "__main__":
    tensor, sentiment = estimate_sentiment(
        ['Markets responded positively to the news!', 'Traders responded pleasantly to the news!']
    )
    print(tensor, sentiment)
    print(torch.cuda.is_available())