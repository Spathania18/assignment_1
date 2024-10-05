from django.shortcuts import render
from transformers import pipeline
from pymongo import MongoClient

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
text_generator = pipeline("text-generation", model="gpt2")

def home(request):
    return render(request, 'index.html')

def classify_text(request):
    if request.method == 'POST':
        input_text = request.POST['text']
        label = classifier(input_text, candidate_labels=['positive', 'negative'])
        return render(request, 'result.html', {'result': label['labels'][0]})
    return render(request, 'index.html')

def generate_text(request):
    if request.method == 'POST':
        prompt = request.POST['prompt']
        generated = text_generator(prompt, max_length=100)
        return render(request, 'result.html', {'result': generated[0]['generated_text']})
    return render(request, 'index.html')
