"""Full Retirement Age"""
# Input Birth Year & Month
# Returns A Tuple Of Year And Month Of Retirement Age
def get_retirement_age(year, month):
    # Return Retirement Age
    if year < 1938:
        return (65, 0)
    elif year > 1937 and year < 1943:
        return (65, (year - 1937) * 2)
    elif year > 1942 and year < 1955:
        return (66, 0)
    elif year < 1960:
        return (66, (year - 1954) * 2)
    else:
        return (67, 0)


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        year = int(input("Enter The Year Of Birth (-1 To Exit): "))
        #  Break If User Enters -1
        if year == -1:
            break
        # Input Month
        month = int(input("Enter The Month Of Birth: "))

        # Get Retirement Age
        (ret_age, ret_age_month) = get_retirement_age(year, month)

        # Add Retirement Age And Month To Birth Year And Month
        ret_year = year + ret_age
        ret_year_month = ret_age_month + month

        # If Month Is More Than 12 Subtract 12 From It And Add 1 To Year
        if ret_year_month >= 12:
            ret_year_month = ret_year_month - 12
            ret_year += 1
        # Display Result
        print(f"Your Full Retirement Age Is {ret_age} And {ret_age_month} Months")
        print(f"This Will Be In {months[ret_year_month - 1]} Of {ret_year}")


if __name__ == "__main__":
    main()