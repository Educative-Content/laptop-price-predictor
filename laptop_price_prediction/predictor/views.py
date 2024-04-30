
from django.shortcuts import render
from .forms import LaptopForm
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

def predict_laptop_price(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            # Initialize input data with all features and set user-provided values
            input_data = {
                'Ram': [form.cleaned_data['Ram']],
                'Weight': [form.cleaned_data['Weight']],
                'TouchScreen': [1 if form.cleaned_data['TouchScreen'] else 0],
                'Ips': [1 if form.cleaned_data['Ips'] else 0],
                'Ppi': [form.cleaned_data['Ppi']],
                'HDD': [form.cleaned_data['HDD']],
                'SSD': [form.cleaned_data['SSD']],
                'Company_Acer': [1 if form.cleaned_data['Company'] == 'Acer' else 0],
                'Company_Apple': [1 if form.cleaned_data['Company'] == 'Apple' else 0],
                'Company_Asus': [1 if form.cleaned_data['Company'] == 'Asus' else 0],
                'Company_Chuwi': [1 if form.cleaned_data['Company'] == 'Chuwi' else 0],
                'Company_Dell': [1 if form.cleaned_data['Company'] == 'Dell' else 0],
                'Company_Fujitsu': [1 if form.cleaned_data['Company'] == 'Fujitsu' else 0],
                'Company_Google': [1 if form.cleaned_data['Company'] == 'Google' else 0],
                'Company_HP': [1 if form.cleaned_data['Company'] == 'HP' else 0],
                'Company_Huawei': [1 if form.cleaned_data['Company'] == 'Huawei' else 0],
                'Company_LG': [1 if form.cleaned_data['Company'] == 'LG' else 0],
                'Company_Lenovo': [1 if form.cleaned_data['Company'] == 'Lenovo' else 0],
                'Company_MSI': [1 if form.cleaned_data['Company'] == 'MSI' else 0],
                'Company_Mediacom': [1 if form.cleaned_data['Company'] == 'Mediacom' else 0],
                'Company_Microsoft': [1 if form.cleaned_data['Company'] == 'Microsoft' else 0],
                'Company_Razer': [1 if form.cleaned_data['Company'] == 'Razer' else 0],
                'Company_Samsung': [1 if form.cleaned_data['Company'] == 'Samsung' else 0],
                'Company_Toshiba': [1 if form.cleaned_data['Company'] == 'Toshiba' else 0],
                'Company_Vero': [1 if form.cleaned_data['Company'] == 'Vero' else 0],
                'Company_Xiaomi': [1 if form.cleaned_data['Company'] == 'Xiaomi' else 0],
                'TypeName_2 in 1 Convertible': [1 if form.cleaned_data['TypeName'] == '2 in 1 Convertible' else 0],
                'TypeName_Gaming': [1 if form.cleaned_data['TypeName'] == 'Gaming' else 0],
                'TypeName_Netbook': [1 if form.cleaned_data['TypeName'] == 'Netbook' else 0],
                'TypeName_Notebook': [1 if form.cleaned_data['TypeName'] == 'Notebook' else 0],
                'TypeName_Ultrabook': [1 if form.cleaned_data['TypeName'] == 'Ultrabook' else 0],
                'TypeName_Workstation': [1 if form.cleaned_data['TypeName'] == 'Workstation' else 0],
                'Cpu_brand_AMD Processor': [1 if form.cleaned_data['Cpu_brand'] == 'AMD Processor' else 0],
                'Cpu_brand_Intel Core i3': [1 if form.cleaned_data['Cpu_brand'] == 'Intel Core i3' else 0],
                'Cpu_brand_Intel Core i5': [1 if form.cleaned_data['Cpu_brand'] == 'Intel Core i5' else 0],
                'Cpu_brand_Intel Core i7': [1 if form.cleaned_data['Cpu_brand'] == 'Intel Core i7' else 0],
                'Cpu_brand_Other Intel Processor': [1 if form.cleaned_data['Cpu_brand'] == 'Other Intel Processor' else 0],
                'Gpu_brand_AMD': [1 if form.cleaned_data['Gpu_brand'] == 'AMD' else 0],
                'Gpu_brand_Intel': [1 if form.cleaned_data['Gpu_brand'] == 'Intel' else 0],
                'Gpu_brand_Nvidia': [1 if form.cleaned_data['Gpu_brand'] == 'Nvidia' else 0],
                'Os_Mac': [1 if form.cleaned_data['Os'] == 'Mac' else 0],
                'Os_Others': [1 if form.cleaned_data['Os'] == 'Others' else 0],
                'Os_Windows': [1 if form.cleaned_data['Os'] == 'Windows' else 0],
            }

            # Convert input data to DataFrame
            input_data_df = pd.DataFrame(input_data)

            # Load the trained XGBoost model
            with open('/fsx/dataset/laptop_data_cleansed.csv', 'rb') as model_file:
                loaded_model = pickle.load(model_file)

            # Make predictions
            predictions = loaded_model.predict(input_data_df)

            # Render the result
            context = {'form': form, 'predicted_price': predictions[0]}
            return render(request, 'predictor/predict_laptop_price.html', context)
    else:
        form = LaptopForm()
    return render(request, 'predictor/predict_laptop_price.html', {'form': form})






