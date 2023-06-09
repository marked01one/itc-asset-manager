import requests
from .error_service import error_handler_clean

BASE_URL = "http://127.0.0.1:8000/api"


class ManufacturerService:
  '''
  Utility class encapsulating HTTP calls for manufacturer data
  '''
  @staticmethod
  def get_manufacturers() -> dict:
    response = requests.get(f'{BASE_URL}/manufacturer/')
    return error_handler_clean(response)  


class RegionService:
  '''
  Utility class encapsulating HTTP calls for region data
  '''
  @staticmethod
  def get_regions() -> dict:
    response = requests.get(f'{BASE_URL}/region/')
    return error_handler_clean(response)
  

class TransformerService:
  '''
  Utility class encapsulating HTTP calls for manufacturer data
  '''
  @staticmethod
  def get_transformers(params_dict: dict | None = None) -> dict:
    if params_dict is None:
      response = requests.get(f'{BASE_URL}/transformer/')
    else:
      for key, value in params_dict.items():
        if value is None:
          del params_dict[key]
        
      response = requests.get(f'{BASE_URL}/transformer/', params=params_dict)
    
    return error_handler_clean(response)
  
  
  def create_new_transformer(request_body: dict | None = None) -> dict:
    if request_body is None:
      return


class FailureService:
  '''
  Utility class encapsulating HTTP calls for failure data
  '''
  @staticmethod
  def get_failures(transformer_serial: str | None = None) -> dict:
    if transformer_serial is None:
      response = requests.get(f'{BASE_URL}/failure/')
    else:
      response = requests.get(
        f'{BASE_URL}/failure/', 
        params={'transformer': transformer_serial}
      )
    
    return error_handler_clean(response)