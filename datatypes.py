def data_type(param):
  if type(param) == str:
    return len(param)
  elif param is None:
    return 'no value'
  elif type(param) == bool:
    return param
  elif type(param) == int:
    if param < 100:
      return 'less than 100'
    elif param > 100:
      return 'more than 100'
    else:
        return 'equal to 100'
  else:
    if type(param) == list:
      if len(param) < 3:
        return None
      else:
        return param[2]