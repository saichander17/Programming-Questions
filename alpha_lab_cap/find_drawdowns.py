def takeValue(el):
  return el["value"]

def find_drawdown(nav, n):
  inputs_valid = validate_inputs(nav, n)
  if inputs_valid==False:
    return False
  cur_max_index = 0
  cur_max=nav[0]
  drawdowns = []
  cur_drawdown = 0
  for index, item in enumerate(nav):
    if ((cur_max > item) and (cur_drawdown< (cur_max-item) )):
      cur_drawdown = cur_max-item
    if (item > cur_max) or (index == len(nav)-1):
      if (cur_drawdown>0):
        drawdowns.append({"value": cur_drawdown, "start_index": cur_max_index, "end_index": index-1})
      cur_drawdown = 0
      cur_max = item
      cur_max_index = index
  drawdowns.sort(key=takeValue, reverse=True)
  ans = []
  pp = 0
  while (pp < n) and (pp<len(drawdowns)):
    ans.append(drawdowns[pp])
    pp += 1
  return ans


def validate_inputs(nav, n):
  if isinstance(nav, list)==False:
    print("nav provided isn't an Array. Please provide different input")
    return False
  if isinstance(n, int)==False:
    print("n provided isn't an Integer. Please provide different input")
    return False
  return True


# def insert_into_drawdowns(dd):
# print(find_drawdown([3,4,5,4,2,6,1], 5))
print find_drawdown([3,2,1,5,2,7,3,10], 2)
print find_drawdown([1,2,3,4,5,4,3,4,3,4,5,6,7,4,3,6,2,10], 4)
print find_drawdown([1,2,3,4,5,7], 3)