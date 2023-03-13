def main():
    n, k, l, c, d, p, nl, np = map(int, input().strip().split())
    drink = k * l // nl
    limes = c * d
    salt = p // np
    toasts = min(drink, limes, salt) // n
    print(toasts)

if __name__ == '__main__':
    main()
