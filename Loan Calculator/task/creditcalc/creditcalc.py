import math
import argparse


def payment(p, n, i):
    payment = int(math.ceil(p * i * pow(1 + i, n) / (pow(1 + i, n) - 1)))
    print(f"Your annuity payment = {payment}!")

    overpayment = payment * n - p
    print(f"Overpayment = {overpayment}")


def diff_payment(p, n, i):  # differentiated payment
    monthly_payment = 0
    total = 0
    for rate in range(1, (n + 1)):
        monthly_payment = int(math.ceil(p / n + i * (p - p * (rate - 1) / n)))
        total += monthly_payment
        print(f"Month {rate}: payment is {monthly_payment}")

    overpayment = int(total - p)
    print(f"Overpayment = {overpayment}")


def principal(a, n, i):
    principal = a / ((i * pow((i + 1), n)) / (pow((i + 1), n) - 1))
    print(f"Your loan principal = {principal}!")


def periods(p, a, i):
    periods = int(math.ceil(math.log(a / (a - i * p), i + 1)))
    years = periods // 12
    months = periods % 12

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

    overpayment = int(periods * a - p)
    print(f"Overpayment = {overpayment}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payment")
    parser.add_argument("--principal")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    parser.add_argument("--type")

    args = parser.parse_args()

    if args.payment:
        if float(args.payment) >= 0:
            a = float(args.payment)
    if args.principal:
        if float(args.principal) >= 0:
            p = float(args.principal)
    if args.periods:
        if int(args.periods) >= 0:
            n = int(args.periods)
    if args.interest:
        if float(args.interest) >= 0:
            # interest per month
            i = float(args.interest) / 12 / 100

    try:
        if args.type not in ["annuity", "diff"]:
            raise ValueError("Incorrect type")
        if args.payment is None:
            if args.type == "diff":
                diff_payment(p, n, i)
            else:
                payment(p, n, i)
        elif args.periods is None:
            periods(p, a, i)
        elif args.principal is None:
            principal(a, n, i)
        else:
            print("Incorrect parameters")

    except Exception:
        print("Incorrect parameters")


if __name__ == "__main__":
    main()
