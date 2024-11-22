from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
import pandas as pd
from stock_app.models import MACD_Data 
from stock_app.models import EMA_Data

@csrf_exempt
@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_csv(request):
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    try:
        # Read the uploaded file
        csv_file = request.FILES['file']
        df = pd.read_csv(csv_file)

        # Insert each row into the database
        for _, row in df.iterrows():
            MACD_Data.objects.create(
                symbol=row['symbol'],
                timestamp=row['timestamp'],
                open=row['open'],
                high=row['high'],
                low=row['low'],
                close=row['close'],
                volume=row['volume'],
                trade_count=row['trade_count'],
                vwap=row['vwap'],
                macd=row['macd'],
                signal_line=row['signal_line'],
                label=row['label']
            )
        return JsonResponse({'message': 'Data successfully uploaded'}, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_ema(request):
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

    try:
        # Read the uploaded file
        csv_file = request.FILES['file']
        df = pd.read_csv(csv_file)

        # Insert each row into the database
        for _, row in df.iterrows():
            EMA_Data.objects.create(
                symbol=row['symbol'],
                timestamp=row['timestamp'],
                open=row['open'],
                high=row['high'],
                low=row['low'],
                close=row['close'],
                volume=row['volume'],
                trade_count=row['trade_count'],
                vwap=row['vwap'],
                ema=row['ema'],
                label=row['label']
            )
        return JsonResponse({'message': 'Data successfully uploaded'}, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# GET endpoint to get the processed data for the ML model
@api_view(['GET'])
def get_macd_data(request):
    try:
        # Get data from SQLite DB
        macd_data = MACD_Data.objects.all()
        # Convert results above to a list of dictionaries
        data = list(macd_data.values(
            'symbol', 'timestamp', 'open', 'high', 'low', 
            'close', 'volume', 'trade_count', 'vwap', 
            'macd', 'signal_line', 'label'
        ))

        df = pd.DataFrame(data)

        # create CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="macd_data.csv"'

        # Write dataframe to the response as CSV
        df.to_csv(path_or_buf=response, index=False)

        return response

    except Exception as e:
        # handle exceptions and return an error response
        return HttpResponse(f"Error: {str(e)}", content_type="text/plain", status=500)
