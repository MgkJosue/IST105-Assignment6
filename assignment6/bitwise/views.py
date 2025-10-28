from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import NumberInputForm
from pymongo import MongoClient
from datetime import datetime

# Configuración de MongoDB
# Para desarrollo local
MONGO_URI = 'mongodb://localhost:27017/'
# Para EC2 (cambiarás esto después):
# MONGO_URI = 'mongodb://<MongoDB-EC2-Private-IP>:27017/'

def get_mongo_client():
    client = MongoClient(MONGO_URI)
    db = client['assignment6_db']
    collection = db['calculations']
    return collection

def process_numbers(numbers):
    """
    Procesa los números según los requisitos
    """
    results = {}
    
    # 1. Verificar que todos son numéricos (ya validado por Django)
    results['all_numeric'] = all(isinstance(n, (int, float)) for n in numbers)
    
    # 2. Advertir si hay negativos
    negative_numbers = [n for n in numbers if n < 0]
    results['has_negatives'] = len(negative_numbers) > 0
    results['negative_numbers'] = negative_numbers
    
    # 3. Calcular promedio y verificar si > 50
    average = sum(numbers) / len(numbers)
    results['average'] = round(average, 2)
    results['average_greater_than_50'] = average > 50
    
    # 4. Contar positivos y verificar par/impar con bitwise
    positive_count = sum(1 for n in numbers if n > 0)
    results['positive_count'] = positive_count
    # Verificar si es par usando bitwise AND con 1
    # Si el resultado es 0, es par; si es 1, es impar
    results['positive_count_is_even'] = (positive_count & 1) == 0
    
    # 5. Crear lista con valores > 10 y ordenar
    greater_than_10 = sorted([n for n in numbers if n > 10])
    results['greater_than_10'] = greater_than_10
    
    # Lista original
    results['original_numbers'] = numbers
    
    return results

def index(request):
    results = None
    
    if request.method == 'POST':
        form = NumberInputForm(request.POST)
        if form.is_valid():
            # Obtener los valores
            numbers = [
                form.cleaned_data['a'],
                form.cleaned_data['b'],
                form.cleaned_data['c'],
                form.cleaned_data['d'],
                form.cleaned_data['e']
            ]
            
            # Procesar números
            results = process_numbers(numbers)
            
            # Guardar en MongoDB
            try:
                collection = get_mongo_client()
                document = {
                    'timestamp': datetime.now(),
                    'input': {
                        'a': numbers[0],
                        'b': numbers[1],
                        'c': numbers[2],
                        'd': numbers[3],
                        'e': numbers[4]
                    },
                    'results': results
                }
                collection.insert_one(document)
                results['saved'] = True
            except Exception as e:
                results['saved'] = False
                results['error'] = str(e)
    else:
        form = NumberInputForm()
    
    return render(request, 'bitwise/index.html', {
        'form': form,
        'results': results
    })

def history(request):
    """
    Muestra todos los cálculos guardados
    """
    try:
        collection = get_mongo_client()
        entries = list(collection.find().sort('timestamp', -1))
        # Convertir ObjectId a string para el template
        for entry in entries:
            entry['_id'] = str(entry['_id'])
    except Exception as e:
        entries = []
        error = str(e)
        return render(request, 'bitwise/history.html', {'entries': entries, 'error': error})
    
    return render(request, 'bitwise/history.html', {'entries': entries})