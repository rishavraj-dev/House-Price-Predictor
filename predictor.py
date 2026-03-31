import pandas as pd
import pickle
import time
def main():
    try:
        with open('model/model.pkl', 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        print("Error: Could not find the model. Run train.py first!")
        exit()



    print("\n" + "="*50)
    print("  ESTIMATE YOUR PROPERTY'S MARKET VALUE 🏠")
    print("="*50)

    area = input("Enter Carpet Area (sqft):   ")
    bhk = input("Enter number of Bedrooms (BHK): ")
            
    baths = input("Enter number of Bathrooms:")
            
    print("\n--- Details ---")
    location = input("Enter City/Location : ")
    furnish = input("Furnishing : ")
    floor = input("Floor detail: ")
            
    resale_input = input("🔄 Is it a Resale? (y/n): ")
    is_resale = 1 if resale_input.lower() == 'y' else 0

    user_data = pd.DataFrame([{
                'BHK': float(bhk),
                'Area': float(area),
                'Is_Resale': is_resale,
                'Bathrooms': float(baths),
                'Location': location,
                'Floor': floor,
                'Furnishing': furnish
            }])

    print("\n Calculating market value based on current data...")

    predicted_price = model.predict(user_data)[0]
    final_price = max(predicted_price, 2000000)

    print("\n" + "-"*50)
    print(f"  ESTIMATED PROPERTY VALUE: ₹{final_price:,.2f}")
    print("-"*50 + "\n")
    print("Thank you for using the property price predictor! 🏡")
print("Welcome to the house price predictor :)")
choice=input("Choose an option: \n 1.Press 1 to predict property\n 2.Press any key except 1 to exit :  ")
if choice == '1':
    main()
    exit()
elif choice == '2':
    print("Exiting the program. Goodbye!")
    exit
else:
    exit()