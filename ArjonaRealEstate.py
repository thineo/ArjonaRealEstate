import math

MONTH_IN_YEAR = 12


# Function to convert anual rate to montly rate
def convert_to_month_rate(year_rate):
    return math.pow(2, (math.log(inflation, 2)/12))

# Present value over inflation
def present_value_over_inflation(future_value, period, rate):
    return future_value / math.pow((1+rate), period)

################
# Config Parameters
#############


transac_value = 1000000 # Real state desired Investment

real_estate_acquisition_fee_applied = 0.99

real_estate_appr_year_rate = 0 # Projected real state appreciation over inflation
vacancy_rate = 0.2 # expected vacancy rate
real_state_rental_rate = 0.005*(1-vacancy_rate) # Real state monthly rental rate

inflation = 1.03 # inflation projected
inflation_dollar = 1.01 # inflation projected


secure_investment_return_rate = 1.003 # secured investment price appreciation over inflation
real_estate_appr_year_rate = 1.003 # real state price appreciation over inflation

usd_to_reais_exc_rate = 5.41 # Rate to transact dolar -> real

usd_borrow_rate_year = 1.0475 # Year rate to borrow money in usd
usd_borrow_term_year = 5 # Year rate to borrow money in usd

reais_borrow_term_mo = 200 # Term for the following rate
reais_borrow_rate = 1.16 # fixed rate to a 200 mo term loan in reais

usd_amount_borrowed = (transac_value/2)/usd_to_reais_exc_rate
reais_amount_borrowed = transac_value/2



# Calculating total to be paid in usd/reais
total_to_be_paid_in_reais = reais_amount_borrowed * reais_borrow_rate
total_to_be_paid_in_dollar = usd_amount_borrowed * (math.pow(usd_borrow_rate_year, 5))

################
# Operation Overview
#############

print("Real estate investment:", transac_value)
print("Amount to be paid in reais: R$", total_to_be_paid_in_reais)
print("Amount to be paid in usd: U$", total_to_be_paid_in_dollar)
print("\n###################\n")


################
# Monthly Operation Overview
#############

monthly_payment_usd_for_dollar_term = total_to_be_paid_in_dollar / (usd_borrow_term_year * MONTH_IN_YEAR)
monthly_payment_rs_for_reais_term = total_to_be_paid_in_reais / reais_borrow_term_mo


print("Amount to be paid monthly in reais for 200 mo: R$", monthly_payment_rs_for_reais_term)
print("Amount to be paid montly in usd for 60 mo: U$", monthly_payment_usd_for_dollar_term)
print("\n###################\n")

monthly_inflation = convert_to_month_rate(inflation)
monthly_real_state_apprec_rate = convert_to_month_rate(inflation + real_estate_appr_year_rate)
monthly_secured_invest_apprec_rate = convert_to_month_rate(inflation + secure_investment_return_rate)


br_account = 0

baseline_account = 0
baseline_inflation_correction_calc = 0

real_estate_value = real_estate_acquisition_fee_applied * transac_value


for m in range(1, reais_borrow_term_mo+1):

    monthly_rental_revenue = real_state_rental_rate * real_estate_value * (1 - vacancy_rate)

    ################
    # Calculating appreciation real estate, monthly payment in reais
    ################

    # Investment income
    br_account = br_account * monthly_inflation

    # Rental - br payment diff added to account
    br_account += monthly_rental_revenue - monthly_payment_rs_for_reais_term

    real_estate_value = real_estate_value * monthly_inflation * monthly_real_state_apprec_rate
    monthly_payment_rs_for_reais_term = monthly_payment_rs_for_reais_term * monthly_inflation



################
# Operation result Summary
################

real_estate_value = (transac_value * real_estate_acquisition_fee_applied) * math.pow( (inflation + real_estate_appr_year_rate -1) , reais_borrow_term_mo/12)

print("Result after 15y\n---\n")

print("Real estate value:", real_estate_value)
print("BR account: ", br_account)



print("Balance after 15y: ", (real_estate_value + br_account))
print("\n###################\n")

################
# Baseline account
################

#
investment_to_present_value = present_value_over_inflation(total_to_be_paid_in_dollar * usd_to_reais_exc_rate, 5, inflation_dollar-1)

print("Total invested:", investment_to_present_value)
print("RoI Real Estate: ", (real_estate_value + br_account)/investment_to_present_value)

baseline_roi = math.pow(inflation*secure_investment_return_rate, reais_borrow_term_mo/12)

print("Baseline ROI: R$", baseline_roi)
print("Baseline Result: R$", baseline_roi*investment_to_present_value)


