def find_division(rating):
  if rating <= 1399:
    return "Division 4"
  elif rating <= 1599:
    return "Division 3"
  elif rating <= 1899:
    return "Division 2"
  else:
    return "Division 1"

def main():
  t = int(input())
  for _ in range(t):
    rating = int(input())
    print(find_division(rating))

if __name__ == "__main__":
  main()
