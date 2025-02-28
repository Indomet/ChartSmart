# Author: Everyone
from django.urls import path
from stock_app import views, api_views

# Add home to path
urlpatterns = [
    path('', views.home, name='home'), # Render home html page
    path('stockadmin/', views.admin, name='admin'), # Render admin html page
    path('db_updates/macd/', api_views.upload_macd, name='upload_macd'), # endpoint for uploading macd data
    path('db_updates/ema/', api_views.upload_ema, name='upload_ema'),
    path('db_updates/rsi/', api_views.upload_rsi, name='upload_rsi'), 
    path('get_database/macd/', api_views.get_macd_data, name='get_macd'), 
    path('get_database/ema/', api_views.get_ema_data, name='get_ema'),
    path('get_database/rsi/', api_views.get_rsi_data, name='get_rsi'),
    path('validate-stock-data/', views.validate_stock_data, name='validate_stock_data'),
    path('upload_metadata/', api_views.upload_metadata, name='upload_metadata'),
    path('upload_model/', api_views.upload_model, name='upload_model'),  #for the pickle file  ,
    path('stockadmin/run_strategy/', api_views.retrain, name='retrain_model'),  
    path('stockadmin/get_models/', api_views.list_files, name='get_model'),
    path('stockadmin/change_model/', api_views.change_chosen_model, name='change_chosen_model'),
    path('stockadmin/get_performance/', api_views.get_performance, name='get_performance'),
    path('rename_metadata/', api_views.rename_metadata, name='rename_metadata'),
    path('upload_model/', api_views.upload_model, name='upload_model'),  #for the pickle file  
    path('predict/<str:strategy>/<str:stock_symbol>/', api_views.make_prediction, name='predict_stock') # for inference
]

