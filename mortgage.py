####################################Algorithm#############################################
#it asks the user to input their maximum square footage they plan on considering for the house.
#It asks the user to input their maximum monthly payment they can afford.
#It asks the user to prompt down payment amount.
#It asks the user to input the current annual rate percentage.
#It asks the user to input the location of the house they are considering.
#It asks the user if they want to make another attempt after making the initial attempt.
#It asks the user if they wish to print the monthly payment schedule.


NUMBER_OF_PAYMENTS = 360
APR_2023 = 0.0668  # The annual percentage rate (APR) for the year 2023


SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0

SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162

# constants if the user enters a city that is not mentioned/unknown. It calculates according to Average_national
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0

LOCATION_NOT_KNOWN_TEXT = '''\nUnknown location. Using national averages for price per square foot and tax rate.'''
NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.'''

# displaying the header of the page
WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
print(WELCOME_TEXT)


MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
print(MAIN_PROMPT)

# It asks the user if they want to make another attempt  after making the initial attempt
KEEP_GOING_TEXT = '''\nWould you like to make another attempt (Y or N)? '''
choice = 'Y'

while choice == 'Y':

    # Case 1 : location
    LOCATIONS_TEXT = '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)?'''
    print(LOCATIONS_TEXT)
    location = input()
    # Case 2 : square footage
    # It asks the user to input their maximum square footage they plan on considering for the house.
    SQUARE_FOOTAGE_TEXT = '''What is the maximum square footage you are considering? '''
    print(SQUARE_FOOTAGE_TEXT)
    square_ft = input()

    if square_ft == "NA" or square_ft == "na":
        square_ft = 0
    else:
        square_ft = float(square_ft)
    # case 3: maximum monthly payment
    # Asking the user for max_monthly_pay they can afford
    MAX_MONTHLY_PAYMENT_TEXT = '''What is the maximum monthly payment you can afford? '''
    print(MAX_MONTHLY_PAYMENT_TEXT)
    max_monthly_pay = input()
    if max_monthly_pay == "NA" or max_monthly_pay == "na":
        max_monthly_pay = 0.0
    else:
        max_monthly_pay = float(
            max_monthly_pay)

    # Asking the user to prompt down payment amount
    DOWN_PAYMENT_TEXT = '''How much money can you put down as a down payment? '''
    print(DOWN_PAYMENT_TEXT)
    down_pay = input()
    if down_pay == "NA" or down_pay == "na":
        down_pay = 0
    else:
        down_pay = float(down_pay)

    # Current Annual rate percentage
    APR_TEXT = '''What is the current annual percentage rate? '''
    print(APR_TEXT)
    apr = input()

    if apr == "NA" or apr == "na":
        apr = APR_2023
    else:
        apr = float(apr)
        apr = apr / 100

    # Determining property values and sales taxes based on the user's location
    if location == 'Seattle':
        f_price = SEATTLE_PRICE_PER_SQ_FOOT
        tax_rate = SEATTLE_PROPERTY_TAX_RATE
    elif location == 'San Francisco':
        f_price = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
    elif location == 'Austin':
        f_price = AUSTIN_PRICE_PER_SQ_FOOT
        tax_rate = AUSTIN_PROPERTY_TAX_RATE
    elif location == 'East Lansing':
        f_price = EAST_LANSING_PRICE_PER_SQ_FOOT
        tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
    else:
        # if the location is unknown or unfound from the given options, it uses national averages
        location = 'Unknown'
        f_price = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE

    # displaying message for unknown location and calculating  based on national averages
    if location == 'Unknown':
        print(LOCATION_NOT_KNOWN_TEXT)

        # calculating mortagage value when max_monthly_pay has not been provided.
        if max_monthly_pay == 0:
            home_cost = square_ft * f_price
            p_val = home_cost - down_pay
            month_tax = (home_cost * tax_rate) / 12
            mpr = apr / 12  #interest
            month_pay = p_val * (mpr * (1 + mpr) ** NUMBER_OF_PAYMENTS) / ((1 + mpr) ** NUMBER_OF_PAYMENTS - 1)
            percentage = apr * 100

            out = (
                '\nIn {}, an average {:,} sq. foot house would cost ${:,}.\nA 30-year fixed rate mortgage with a down payment of ${:,} at {:,.1f}% APR results \n'
                '\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}')
            print(out.format(location, int(square_ft), int(home_cost), int(down_pay), percentage, month_tax, month_pay,
                             month_tax + month_pay))

            # Asking the user if they wish to print the monthly payment schedule                 
            AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''

            table = input(AMORTIZATION_TEXT)
            if table.upper() == 'Y':
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
                print("=" * 48)

                balance = home_cost - down_pay

                r_loan = balance
                loan = 0
                for i in range(1,
                               361):
                    r_loan = r_loan - loan
                    interest = r_loan * apr / 12
                    loan = month_pay - interest

                    print("{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}".format(i, interest, loan, r_loan))


        elif max_monthly_pay == 0 and square_ft == 0:
            print(
                NOT_ENOUGH_INFORMATION_TEXT)
        else:

            home_cost = square_ft * f_price
            p_val = home_cost - down_pay
            month_tax = (home_cost * tax_rate) / 12
            mpr = apr / 12
            month_pay = p_val * (mpr * (1 + mpr) ** NUMBER_OF_PAYMENTS) / ((1 + mpr) ** NUMBER_OF_PAYMENTS - 1)
            percentage = apr * 100
            # printing new updated results after calculations
            out = (
                '\nIn the average U.S. housing market, an average {:,} sq. foot house would cost ${:,}. \n A 30-year fixed rate mortgage with a down payment of ${:,} at {:,.1f}% APR results \n '
                '\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}')
            print(out.format(int(square_ft), int(home_cost), int(down_pay), percentage, month_tax, month_pay,
                             month_tax + month_pay))

            if max_monthly_pay != 0.0:
                if (
                        month_tax + month_pay) > max_monthly_pay:  # Determining if the user can afford the house based on maximum monthly payment
                    print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(
                        max_monthly_pay))
                else:
                    print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(
                        max_monthly_pay))

            AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''

            table = input(AMORTIZATION_TEXT)
            if table.upper() == 'Y':
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
                print("=" * 48)

                balance = home_cost - down_pay

                r_loan = balance
                loan = 0

                for i in range(1, 361):
                    r_loan = r_loan - loan
                    interest = r_loan * apr / 12
                    loan = month_pay - interest

                    print("{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}".format(i, interest, loan, r_loan))
    else:
        if square_ft == 0:
            max_square_footage = 100
            months_per_year = 12

            while True:
                estimated_home_cost = max_square_footage * f_price
                principal_loan_amount = estimated_home_cost - down_pay
                mpr = apr / 12
                num_payments = NUMBER_OF_PAYMENTS
                monthly_payment_loan = principal_loan_amount * (mpr * (1 + mpr) ** num_payments) / (
                            (1 + mpr) ** num_payments - 1)
                monthly_payment_taxes = estimated_home_cost * tax_rate / 12


                total_monthly_payment = monthly_payment_loan + monthly_payment_taxes


                if total_monthly_payment > max_monthly_pay:
                    max_square_footage -= 1
                    break
                else:
                    max_square_footage += 1

            square_ft = max_square_footage
            home_cost = square_ft * f_price
            p_val = home_cost - down_pay
            month_tax = (home_cost * tax_rate) / 12
            mpr = apr / 12
            month_pay = p_val * (mpr * (1 + mpr) ** NUMBER_OF_PAYMENTS) / ((1 + mpr) ** NUMBER_OF_PAYMENTS - 1)
            percentage = apr * 100
            print('\n\nIn {}, a maximum monthly payment of ${:,.2f} '
                  'allows the purchase of a house of {:,} sq. feet for ${:,} \n'
                  '\t assuming a 30-year fixed rate mortgage with a ${:,} down payment at {:.1f}% APR.'.format(location,
                                                                                                               max_monthly_pay,
                                                                                                               int(square_ft),
                                                                                                               int(home_cost),                                                                                                               int(down_pay),
                                                                                                               percentage))
        elif max_monthly_pay == 0:
            home_cost = square_ft * f_price
            p_val = home_cost - down_pay
            month_tax = (home_cost * tax_rate) / 12
            mpr = apr / 12
            month_pay = p_val * (mpr * (1 + mpr) ** NUMBER_OF_PAYMENTS) / ((1 + mpr) ** NUMBER_OF_PAYMENTS - 1)
            percentage = apr * 100

            out = (
                '\nIn {}, an average {:,} sq. foot house would cost ${:,}.\nA 30-year fixed rate mortgage with a down payment of ${:,} at {:,.1f}% APR results \n'
                '\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}')
            print(out.format(location, int(square_ft), int(home_cost), int(down_pay), percentage, month_tax, month_pay,
                             month_tax + month_pay))

            AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''

            table = input(AMORTIZATION_TEXT)
            if table.upper() == 'Y':
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
                print("=" * 48)

                balance = home_cost - down_pay

                r_loan = balance
                loan = 0
                for i in range(1, 361):
                    r_loan = r_loan - loan
                    interest = r_loan * apr / 12
                    loan = month_pay - interest

                    print("{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}".format(i, interest, loan, r_loan))
        elif max_monthly_pay == 0 and square_ft == 0:
            print(NOT_ENOUGH_INFORMATION_TEXT)
        else:
            home_cost = square_ft * f_price
            p_val = home_cost - down_pay
            month_tax = (home_cost * tax_rate) / 12
            mpr = apr / 12
            month_pay = p_val * (mpr * (1 + mpr) ** NUMBER_OF_PAYMENTS) / ((1 + mpr) ** NUMBER_OF_PAYMENTS - 1)
            percentage = apr * 100

            out = (
                '\nIn {}, an average {:,} sq. foot house would cost ${:,}.\nA 30-year fixed rate mortgage with a down payment of ${:,} at {:,.1f}% APR results \n'
                '\tin an expected monthly payment of ${:,.2f} (taxes) + ${:,.2f} (mortgage payment) = ${:,.2f}')
            print(out.format(location, int(square_ft), int(home_cost), int(down_pay), percentage, month_tax, month_pay,
                             month_tax + month_pay))
            if max_monthly_pay != 0.0:
                if (month_tax + month_pay) > max_monthly_pay:
                    print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'.format(
                        max_monthly_pay))
                else:
                    print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'.format(
                        max_monthly_pay))
            AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''

            table = input(AMORTIZATION_TEXT)
            if table.upper() == 'Y':
                print('\n{:^7}|{:^12}|{:^13}|{:^14}'.format('Month', 'Interest', 'Payment', 'Balance'))
                print("=" * 48)

                balance = home_cost - down_pay

                r_loan = balance
                loan = 0
                for i in range(1, 361):
                    r_loan = r_loan - loan
                    interest = r_loan * apr / 12
                    loan = month_pay - interest

                    print("{:^7}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}".format(i, interest, loan, r_loan))


    choice = input(KEEP_GOING_TEXT)
    choice = choice.capitalize()
    if choice == 'Y':
        print(WELCOME_TEXT)  # If the user wants to continue, displaying the welcome message and main prompt again
        print(MAIN_PROMPT)




