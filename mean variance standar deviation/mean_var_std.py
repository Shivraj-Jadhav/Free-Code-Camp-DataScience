import numpy as np

def calculate(list1):
  try:
      arr = np.array(list1).reshape((3,3))
  except ValueError:
    raise ValueError("List must contain nine numbers.")


  mean = []
  variance = []
  stD = []
  maxi = []
  mini = []
  sum1 = []
  mean.append(np.mean(arr, axis=0).tolist())
  mean.append(np.mean(arr, axis=1).tolist()) 
  mean.append(np.mean(arr).tolist())
        
  variance.append(np.var(arr, axis=0).tolist())
  variance.append(np.var(arr, axis=1).tolist())
  variance.append(np.var(arr).tolist())

  stD.append(np.std(arr, axis=0).tolist()) 
  stD.append(np.std(arr, axis=1).tolist())
  stD.append(np.std(arr).tolist())

  maxi.append(np.max(arr, axis=0).tolist()) 
  maxi.append(np.max(arr, axis=1).tolist())
  maxi.append(np.max(arr).tolist())

  mini.append(np.min(arr, axis=0).tolist())
  mini.append(np.min(arr, axis=1).tolist())
  mini.append(np.min(arr).tolist())

  sum1.append(np.sum(arr, axis=0).tolist())
  sum1.append(np.sum(arr, axis=1).tolist())
  sum1.append(np.sum(arr).tolist())
  calculations = {
    "mean" : mean,
    "variance" : variance,
    "standard deviation" : stD,
    "max" : maxi,
    "min" : mini,
    "sum" : sum1
    }

  return calculations