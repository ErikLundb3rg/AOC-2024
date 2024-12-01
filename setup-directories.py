import os 

def main():
  print("Creating directories...") 
  for day in range(1, 25):
    os.mkdir(f'day{day}')
    f = open(f'./day{day}/solve_part_1.py', 'x')
    f = open(f'./day{day}/solve_part_2.py', 'x')
    f = open(f'./day{day}/input.in', 'x')
  print("Done!") 

if __name__ == '__main__':
  main()