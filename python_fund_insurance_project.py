import csv

#Importing insurance data
insurance_data = []
with open("/home/samorc/anaconda3/envs/codecademy/portfolio_insurance_project_starter_files/python-portfolio-project-starter-files/insurance.csv") as insurance_info:
    insurance_reader = csv.DictReader(insurance_info)
    for row in insurance_reader:
        insurance_data.append(row)


#Examining patient demographic data
#Finding average age of patients in dataset
def average_age(insurance_data):
    total_age = 0
    for row in insurance_data:
        total_age += int(row['age'])

    avg_age = total_age / len(insurance_data)  
    
    return round(avg_age, 0)

print("The average age of patients in this dataset is:", int(average_age(insurance_data)), "years")


#Finding percent males vs percent females
def male_female_dis(insurance_data):
    fem_count = 0
    male_count = 0
    for row in insurance_data:
        if row['sex'] == "female":
            fem_count += 1
        else:
            male_count += 1
    
    per_fem = fem_count / (male_count + fem_count) * 100
    per_male = male_count / (male_count + fem_count) * 100

    return round(per_fem,1), round(per_male,1)

per_female, per_male = male_female_dis(insurance_data)
print(str(per_female) + "%" + " of patients in this dataset are female and " + str(per_male) + "%" + " are male.")


#Finding percent of smokers and non-smokers
def smoker_percent(insurance_data):
    smoker_count = 0
    non_count = 0
    for row in insurance_data:
        if row["smoker"] == "yes":
            smoker_count += 1
        else:
            non_count += 1
    
    per_smoker = smoker_count / (smoker_count + non_count) * 100
    per_non = non_count / (smoker_count + non_count) * 100

    return round(per_smoker, 1), round(per_non, 1)

per_smoker, per_non_smoker = smoker_percent(insurance_data)
print(str(per_smoker) + "%" + " of patients in this dataset smoke and " + str(per_non_smoker) + "%" + " do not smoke.")


#Finding percent of patients with and without children
def children(insurance_data):
    no_children_count = 0
    children_count = 0
    for row in insurance_data:
        if row["children"] == "0":
            no_children_count += 1
        else:
            children_count += 1
    
    per_no_children = no_children_count / (no_children_count + children_count) * 100
    per_children = children_count / (no_children_count + children_count) * 100

    return round(per_no_children, 1), round(per_children, 1)

per_wout_children, per_w_children = children(insurance_data)
print(str(per_wout_children) + "%" + " of patients in this dataset do not have children and " 
        + str(per_w_children) + "%" + " have at least one child.")
    

#Finding geographical distribution of patients
def geo_location(insurance_data):
    ne_count = 0
    nw_count = 0
    se_count = 0
    sw_count = 0

    for row in insurance_data:
        if row["region"] == "northeast":
            ne_count += 1
        elif row["region"] == "northwest":
            nw_count += 1
        elif row["region"] == "southeast":
            se_count += 1
        else:
            sw_count += 1
    
    ne_percent = ne_count / (ne_count + nw_count + se_count + sw_count) * 100
    nw_percent = nw_count / (ne_count + nw_count + se_count + sw_count) * 100
    se_percent = se_count / (ne_count + nw_count + se_count + sw_count) * 100
    sw_percent = sw_count / (ne_count + nw_count + se_count + sw_count) * 100

    return round(ne_percent, 2) , round(nw_percent, 2), round(se_percent, 2), round(sw_percent,2)

ne_percent, nw_percent, se_percent, sw_percent = geo_location(insurance_data)
print(str(ne_percent) + "%" + " of patients are from the Northeast, " + str(nw_percent) + "%" 
        + " of patients are from the Northwest, " + str(se_percent) + "%" + " of patients are from the Southeast, and "
        + str(sw_percent) + "%" + " of patients are from the Southwest.")
 

#Cost comparisons
#Finding average costs for smokers vs non-smokers
def smoker_costs(insurance_data):
    smoker_total = 0
    non_smoker_total = 0
    smoker_count = 0
    non_smoker_count = 0

    for row in insurance_data:
        if row["smoker"] == "yes":
            smoker_total += float(row["charges"])
            smoker_count += 1
        else:
            non_smoker_total += float(row["charges"])
            non_smoker_count += 1
    
    smoker_avg = smoker_total / smoker_count
    non_smoker_avg = non_smoker_total / non_smoker_count

    return round(smoker_avg, 2), round(non_smoker_avg, 2)

smoker_avg, non_smoker_avg = smoker_costs(insurance_data)
print("On average, smokers paid $" + str(smoker_avg) + " while non-smokers on average paid $" + str(non_smoker_avg) + ".")


#Finding if there is a relationship between BMI and insurance costs
def BMI_costs(insurance_data):
    #These are max thresholds; obesity has a minimum BMI of 30.0
    BMI_cats = {"underweight": 18.49, "normal": 24.99, "overweight": 29.99}    
    underw_total = 0
    normalw_total = 0
    overw_total = 0
    obesew_total = 0
    underw_count = 0
    normalw_count = 0
    overw_count = 0
    obesew_count = 0

    for row in insurance_data:
        if float(row["bmi"]) <= BMI_cats["underweight"]:
            underw_total += float(row["charges"])
            underw_count += 1
        elif BMI_cats["underweight"] < float(row["bmi"]) <= BMI_cats["normal"]:
            normalw_total += float(row["charges"])
            normalw_count += 1
        elif BMI_cats["normal"] < float(row["bmi"]) <= BMI_cats["overweight"]:
            overw_total += float(row["charges"])
            overw_count += 1
        else:
            obesew_total += float(row["charges"])
            obesew_count += 1
    
    underw_avg = underw_total / underw_count
    normalw_avg = normalw_total / normalw_count
    overw_avg = overw_total /overw_count
    obesew_avg = obesew_total / obesew_count

    return round(underw_avg, 2), round(normalw_avg, 2), round(overw_avg, 2), round(obesew_avg, 2)

underw_avg, normal_avg, overw_avg, obese_avg = BMI_costs(insurance_data)
print("Those who were underweight paid an average of $" + str(underw_avg) + 
        ", those who had a normal BMI paid an average of $" + str(normal_avg) + 
        ", those who were overweight paid an average of $" + str(overw_avg) + 
        ", and those who were obese paid an average of $" + str(obese_avg) + ".")





