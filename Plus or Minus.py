def check_equation(a, b, c):
  if a + b == c:
    return "+"
  else:
    return "-"

def main():
  t = int(input())
  for _ in range(t):
    a, b, c = map(int, input().split())
    print(check_equation(a, b, c))

if __name__ == "__main__":
  main()
