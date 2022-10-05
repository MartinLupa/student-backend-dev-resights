import json

with open('data/ResightsApS.json', 'r') as f:
    network = json.load(f)


# CODE:

#Ask for company/person name input for which/whose property value over focus company should be calculated:
input = input("Enter target company: ")


#Iterate over dataset and generate required information for later comparison:
for input_company in network:
    if (input == input_company["source_name"]):
        input_source_name = input_company["source_name"]
        input_source_depth = int(input_company["source_depth"])
        input_target_name = input_company["target_name"]
        input_share = input_company["share"]
        break


#Share format conversion: If share is an interval
if "-" in input_share:
   converted_input_share_list =  [int(x) for x in input_share.replace("%", "").split("-")]

#Share format conversion: If share is a percentage
else:
   converted_input_share = int(input_share.replace("%", ""))


#Iterate over dataset:
for company in network:
    if input_target_name == "Resights ApS":
        company_share = company["share"]
        converted_company_share = [int(x) for x in company_share.replace("%", "").split("-")]
        break

    elif input_target_name == company["source_name"]:
        while input_source_depth > 0:  
            company_share = company["share"]
            converted_company_share = [int(x) for x in company_share.replace("%", "").split("-")]

            if converted_input_share != None:
                converted_company_share[0] = converted_company_share[0] * converted_input_share/100
                converted_company_share[1] = converted_company_share[1] * converted_input_share/100
                input_source_depth -= 1

            elif converted_input_share_list != None:
                converted_company_share[0] = converted_company_share[0] * converted_input_share_list[0]/100
                converted_company_share[1] = converted_company_share[1] * converted_input_share_list[1]/100 
                input_source_depth -= 1


#Print required output (lower, middle and upper values)
company_share_range = converted_company_share[1] - converted_company_share[0]

print("Lower value: ", converted_company_share[0], "%")
print("Middle value: ", converted_company_share[0] + company_share_range/2, "%")
print("Upper value: ", converted_company_share[1], "%")
