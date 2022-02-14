# nusp: 10258730
import sys
 
visited = []
 
def remove_at_index(arr, i):
  return arr[:i] + arr[i+1:]
 
def add_at_index(arr, i, item):
  return arr[:i] + [item] + arr[i:]
 
def solve(string, removes, results):
  results.append(string)
 
  if string in visited:
    return
   
  visited.append(string)
 
  for i in range(len(string)):
    char_to_remove = string[i]
 
    string = remove_at_index(string, i)
    removes = add_at_index(removes, i, char_to_remove)
 
    solve(string, removes, results)
 
    string = add_at_index(string, i, char_to_remove)
    removes = remove_at_index(removes, i)
 
def print_output(results):
  for result in results:
    print(result)
 
def main():
  linhas = '''abc
aaaaa
huehue
joao
pedro
gaby
mario'''.strip().split('\n')
  for linha in linhas:
    expr_arr = [c for c in linha]
    results = []
    solve(expr_arr, [], results)
    uniq = set(["".join(r) for r in results if r != []])
    results = sorted(list(uniq))
    print_output(results)
    print("")
 
  print("")
 
main()